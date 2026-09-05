
# One endpoint serves the whole statistics panel. Trimmed here to the shape:
# the real route also computes daily/weekly/monthly/yearly averages against a
# fixed reference date, and the longest-streak records.

@app.route('/api/dashboard')
def api_dashboard():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT DISTINCT game_title FROM games ORDER BY game_title")
    game_titles = [row[0] for row in cur.fetchall()]

    cur.execute("""
        SELECT game_title, COUNT(*) FROM games
        GROUP BY game_title ORDER BY COUNT(*) DESC LIMIT 5
    """)
    top_games = [{'game': r[0], 'count': r[1]} for r in cur.fetchall()]

    # "Today" is the user's today: each account stores its own timezone, so a
    # game logged at 11pm in Auckland does not land on yesterday in UTC.
    today = today_local()
    start_of_week = today - timedelta(days=today.weekday())
    start_of_month = today.replace(day=1)
    start_of_year = today.replace(month=1, day=1)
    end_of_last_week = start_of_week - timedelta(days=1)
    start_of_last_week = end_of_last_week - timedelta(days=6)

    def count(q, *args):
        cur.execute(q, args)
        return cur.fetchone()[0]

    def most_played(start, end=None):
        if end:
            cur.execute("""SELECT game_title, COUNT(*) FROM games
                           WHERE date_played BETWEEN %s AND %s
                           GROUP BY game_title ORDER BY COUNT(*) DESC LIMIT 1""",
                        (start, end))
        else:
            cur.execute("""SELECT game_title, COUNT(*) FROM games
                           WHERE date_played >= %s
                           GROUP BY game_title ORDER BY COUNT(*) DESC LIMIT 1""",
                        (start,))
        row = cur.fetchone()
        return {'game': row[0], 'count': row[1]} if row else {'game': None, 'count': 0}

    # Averages are each taken against a fixed reference date — omitted here,
    # along with the last-month and last-year periods, to keep the shape legible.
    records = {k: {'count': v['count'],
                   'start': v['start'].isoformat() if v['start'] else None}
               for k, v in period_records(cur).items()}

    result = {
        'game_titles': game_titles,
        'top_games': top_games,
        'today': today.isoformat(),
        'games_played': {
            'today':     count("SELECT COUNT(*) FROM games WHERE date_played = %s", today),
            'yesterday': count("SELECT COUNT(*) FROM games WHERE date_played = %s",
                               today - timedelta(days=1)),
            'this_week':  count("SELECT COUNT(*) FROM games WHERE date_played >= %s", start_of_week),
            'this_month': count("SELECT COUNT(*) FROM games WHERE date_played >= %s", start_of_month),
            'this_year':  count("SELECT COUNT(*) FROM games WHERE date_played >= %s", start_of_year),
            'last_week':  count("SELECT COUNT(*) FROM games WHERE date_played BETWEEN %s AND %s",
                                start_of_last_week, end_of_last_week),
            'daily_avg': daily_avg, 'weekly_avg': weekly_avg,
            'monthly_avg': monthly_avg, 'yearly_avg': yearly_avg,
        },
        'records': records,
        'most_played': {
            'this_week': most_played(start_of_week),
            'last_week': most_played(start_of_last_week, end_of_last_week),
            'this_year': most_played(start_of_year),
        },
    }
    cur.close()
    conn.close()
    return jsonify(result)
