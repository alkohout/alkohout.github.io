
# Running model-written SQL against a live database, defended in layers.

DB_QUERY_MAX_ROWS = 200               # rows handed back to the model and the page
DB_QUERY_MAX_CELL = 300               # characters per cell, so a stray blob can't flood

DB_QUERY_BANNED = re.compile(
    r'\b(insert|update|delete|drop|alter|create|truncate|grant|revoke|copy|'
    r'vacuum|reindex|merge|call|do|lock|listen|notify|prepare|execute|'
    r'pg_read_file|pg_sleep|dblink|pg_terminate_backend)\b', re.I)


def db_query_check(sql):
    """Reject anything that isn't a single read-only statement. Returns an error string."""
    stripped = sql.strip().rstrip(';').strip()
    if not stripped:
        return 'No SQL was produced.'
    if ';' in stripped:
        return 'Only a single statement is allowed.'
    if not re.match(r'^(select|with)\b', stripped, re.I):
        return 'Only SELECT queries are allowed.'
    banned = DB_QUERY_BANNED.search(stripped)
    if banned:
        return f'Query rejected: it contains "{banned.group(0)}".'
    return None


def db_query_run(sql, is_owner=False):
    """Run the query in a read-only transaction. Returns (columns, rows, truncated).

    On a connection of its own, deliberately. set_session can't be called with a
    transaction already open, which the shared request connection usually has —
    and a pooled connection handed back still marked read-only would break the
    next writer to borrow it. The extra connection costs about a second; an AI
    question already costs several.
    """
    conn = private_db_connection()
    try:
        # Read-only is enforced by Postgres, not by our own parsing of the SQL.
        conn.set_session(readonly=True, autocommit=False)
        cur = conn.cursor()
        cur.execute("SET LOCAL statement_timeout = '15s'")
        # Hand the model's SQL to a role that can only read game rows: no users
        # table, no rulebooks, and row-level security still scoped to the caller.
        cur.execute("SET LOCAL ROLE " + ('bgl_ai_owner' if is_owner else 'bgl_ai'))
        cur.execute(sql)
        columns = [d[0] for d in cur.description] if cur.description else []
        raw = cur.fetchmany(DB_QUERY_MAX_ROWS + 1)
        truncated = len(raw) > DB_QUERY_MAX_ROWS
        rows = [
            ['' if v is None else str(v)[:DB_QUERY_MAX_CELL] for v in row]
            for row in raw[:DB_QUERY_MAX_ROWS]
        ]
        conn.rollback()
        cur.close()
        return columns, rows, truncated
    finally:
        conn.close()


@app.route('/api/ask_database', methods=['POST'])
def api_ask_database():
    question = (request.get_json() or {}).get('question', '').strip()

    # This endpoint runs SQL the model writes, so it is only safe while the
    # database is enforcing row-level security. A superuser connection ignores
    # policies, which would let a generated query read every user's rows.
    if db_bypasses_rls():
        return jsonify({'success': False, 'message':
                        'Disabled: the app is connected as a superuser, which bypasses '
                        'row-level security. Point DB_USER at bgl_app and restart.'}), 503

    is_owner = bool(current_user() and current_user().get('is_owner'))
    schema = db_query_schema(cur, is_owner=is_owner)

    # 1. Question -> SQL. A question the schema cannot answer comes back as an
    #    explicit refusal rather than a plausible-looking wrong query.
    sql_system = (
        'You write PostgreSQL for a personal board game log. Reply with one '
        'SELECT statement and nothing else — no explanation, no markdown fences, '
        'no trailing semicolon. If the question cannot be answered from this '
        'schema, reply with exactly "UNSUPPORTED: " followed by a short reason.\n\n'
        f'Schema:\n{schema}\n{notes}\n'
        f'Return at most {DB_QUERY_MAX_ROWS} rows — add a LIMIT unless the query '
        'is already an aggregate. Never select the columns marked HUGE.'
    )
    sql = ask_model('db_query', sql_system, question, 2000, sql_via_claude).text

    if sql.upper().startswith('UNSUPPORTED'):
        return jsonify({'success': False, 'message': sql.split(':', 1)[-1].strip()})

    problem = db_query_check(sql)
    if problem:
        return jsonify({'success': False, 'message': problem, 'sql': sql}), 400

    # 2. Run it read-only, then 3. turn the rows back into plain English.
    columns, rows, truncated = db_query_run(sql.rstrip(';'), is_owner=is_owner)
    answer = ask_model('db_query', answer_system, answer_user, 1000, answer_via_claude).text

    # The generated SQL goes back with the answer, so the working can be checked.
    return jsonify({'success': True, 'answer': answer, 'sql': sql,
                    'columns': columns, 'rows': rows, 'truncated': truncated,
                    'cost_nzd': round(nzd, 4)})
