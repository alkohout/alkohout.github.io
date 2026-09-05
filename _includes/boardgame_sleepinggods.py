
# Sleeping Gods keeps a second table of its own: one row per location visited,
# with what it required, what it gave, and what it cost.
#
# Per-account since migration 014 — these rows carry a user_id and row-level
# security scopes them, so the endpoint is no longer the boundary.

@app.route('/search_sleeping_gods_location', methods=['GET'])
def search_sleeping_gods_location():
    # location is an integer column, so anything else is a 400 rather than a
    # 500 out of the driver. This only became reachable when the endpoint
    # stopped being owner-only — before that a stray value was refused earlier.
    try:
        location = int(request.args.get('term', '0'))
    except (TypeError, ValueError):
        return jsonify({'success': False, 'message': 'Location must be a number.'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id,* FROM sleeping_gods WHERE location = %s", (location,))
    results = cur.fetchall()
    cur.close()
    conn.close()

    data = [
        {
            'id': row[0], 'location': row[1], 'part': row[2],
            'required_keyword': row[3], 'gained_keyword': row[4],
            'visited': row[5], 'notes': row[6],
            'combat': row[7], 'combat_level': row[8],
            'gained': row[9], 'lost': row[10],
            # ... the resource, condition and totem columns follow
        }
        for row in results
    ]
    return jsonify(data)


# Logging a location writes forty columns — resources required and gained,
# conditions taken and removed, totems, challenges. The helpers coerce each
# to the right type so a blank field becomes 0 rather than an error.

@app.route('/api/add_sleeping_gods', methods=['POST'])
def api_add_sleeping_gods():
    try:
        d = request.get_json() or {}
        def i(k): return int(d.get(k) or 0)
        def s(k): return str(d.get(k) or '')
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO sleeping_gods (location, part, required_keyword,"
            " gained_keyword, visited, notes, combat, combat_level, gained,"
            " req_coins, req_meat, ... , gain_totem, challenge,"
            " challenge_level, gain_adventure)"
            " VALUES (" + ",".join(["%s"] * 40) + ")",
            (i('location'), s('part'), s('required_keyword'), s('gained_keyword'),
             '1' if d.get('visited') else '0', s('notes'),
             '1' if d.get('combat') else '0', i('combat_level'), s('gained'),
             i('req_coins'), i('req_meat'),
             # ... the remaining resource and condition fields
             s('gain_totem'), s('challenge'), i('challenge_level'),
             i('gain_adventure'))
        )
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
