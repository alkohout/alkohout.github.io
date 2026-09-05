
# Autocomplete for the title field. Distinct titles only — the point is to
# reuse the spelling already in the log rather than create a near-duplicate.

@app.route('/search_games', methods=['GET'])
def search_games():
    search_term = request.args.get('term', '')
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT DISTINCT game_title FROM games WHERE game_title ILIKE %s",
                (f"%{search_term}%",))
    suggestions = [row[0] for row in cur.fetchall()]

    cur.close()
    conn.close()
    return jsonify({'suggestions': suggestions})


# The full list, ranked by how often each game has been played, with the most
# recent note for each. RANK() rather than a row number, so two games played
# the same number of times share a place. This is what the "All games" page
# then sorts client-side.

@app.route('/api/all_games')
def api_all_games():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT game_title, RANK() OVER (ORDER BY COUNT(*) DESC), COUNT(*),
            COALESCE((SELECT notes FROM games g2 WHERE g2.game_title = g.game_title
                AND g2.notes IS NOT NULL ORDER BY g2.date_played DESC LIMIT 1), '')
        FROM games g GROUP BY game_title ORDER BY game_title
    """)
    rows = [{'game': r[0], 'rank': r[1], 'play_count': r[2], 'latest_note': r[3]}
            for r in cur.fetchall()]
    cur.close()
    conn.close()
    return jsonify(rows)
