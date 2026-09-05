
# Every game played in each period, rather than just the top few. One helper
# closes over the cursor and is called once per window.

@app.route('/api/games_overview')
def api_games_overview():
    conn = get_db_connection()
    cur = conn.cursor()
    today = today_local()
    start_of_week = today - timedelta(days=today.weekday())
    start_of_month = today.replace(day=1)
    start_of_year = today.replace(month=1, day=1)
    end_of_last_week = start_of_week - timedelta(days=1)
    start_of_last_week = end_of_last_week - timedelta(days=6)
    end_of_last_month = start_of_month - timedelta(days=1)
    start_of_last_month = end_of_last_month.replace(day=1)
    end_of_last_year = start_of_year - timedelta(days=1)
    start_of_last_year = end_of_last_year.replace(month=1, day=1)

    def fetch(start, end):
        cur.execute("""SELECT game_title, COUNT(*) FROM games
                       WHERE date_played BETWEEN %s AND %s
                       GROUP BY game_title ORDER BY COUNT(*) DESC""", (start, end))
        return [{'game': r[0], 'count': r[1]} for r in cur.fetchall()]

    result = {
        'this_week':  fetch(start_of_week, today),
        'this_month': fetch(start_of_month, today),
        'this_year':  fetch(start_of_year, today),
        'last_week':  fetch(start_of_last_week, end_of_last_week),
        'last_month': fetch(start_of_last_month, end_of_last_month),
        'last_year':  fetch(start_of_last_year, end_of_last_year),
    }
    cur.close()
    conn.close()
    return jsonify(result)
