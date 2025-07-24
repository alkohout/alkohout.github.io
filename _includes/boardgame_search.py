
@app.route('/search_last_played', methods=['GET'])
def search_last_played():
    game_title = request.args.get('term', '')
    conn = get_db_connection()
    cur = conn.cursor()

    # Search for the most recent play and notes
    cur.execute("""
        SELECT g.date_played,  
        COALESCE( (SELECT g2.id
                 FROM games AS g2
                 WHERE g2.game_title = g.game_title
                 ORDER BY g2.id DESC
                 LIMIT 1), 0) 
        FROM games AS g 
        WHERE g.game_title ILIKE %s 
        ORDER BY g.date_played DESC 
        LIMIT 1
    """, (f"%{game_title}%",))
    last_played = cur.fetchone()

    # Fetch notes
    cur.execute("SELECT notes FROM games WHERE id = %s", (f"{last_played[1]}",))
    notes = cur.fetchone()[0]

    # Fetch result
    cur.execute("SELECT result FROM games WHERE id = %s", (f"{last_played[1]}",))
    result = cur.fetchone()[0]

    # Fetch level
    cur.execute("SELECT level FROM games WHERE id = %s", (f"{last_played[1]}",))
    level = cur.fetchone()[0]

    # Fetch my_score
    cur.execute("SELECT my_score FROM games WHERE id = %s", (f"{last_played[1]}",))
    my_score = cur.fetchone()[0]

    # Fetch bot_score
    cur.execute("SELECT bot_score FROM games WHERE id = %s", (f"{last_played[1]}",))
    bot_score = cur.fetchone()[0]

    # Fetch total number of times the game was played
    cur.execute("SELECT COUNT(*) FROM games WHERE game_title ILIKE %s", (f"%{game_title}%",))
    total_plays = cur.fetchone()[0]
    
    # Fetch the most recent play date for the game
    cur.execute("SELECT MAX(date_played) FROM games WHERE game_title ILIKE %s", (f"%{game_title}%",))
    last_played_date = cur.fetchone()[0]
    
    # Calculate date boundaries for the current week, month, and year
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    start_of_month = today.replace(day=1)
    start_of_year = today.replace(month=1, day=1)
    
    # Count games played this week
    cur.execute("SELECT COUNT(*) FROM games WHERE date_played >= %s AND game_title ILIKE %s", (start_of_week,f"%{game_title}%"))
    played_this_week = cur.fetchone()[0]
    
    # Count games played this month
    cur.execute("SELECT COUNT(*) FROM games WHERE date_played >= %s AND game_title ILIKE %s", (start_of_month,f"%{game_title}%"))
    played_this_month = cur.fetchone()[0]
    
    # Count games played this year
    cur.execute("SELECT COUNT(*) FROM games WHERE date_played >= %s AND game_title ILIKE %s", (start_of_year,f"%{game_title}%"))
    played_this_year = cur.fetchone()[0]

    # Query to get the ranking of games by play count
    cur.execute("SELECT game_title, RANK() OVER (ORDER BY COUNT(*) DESC) FROM games GROUP BY game_title")
    rankings = cur.fetchall()

    print(rankings)
    # Create a dictionary of game titles and their rankings
    rankings_dict = {game[0]: game[1] for game in rankings}

    # Get the ranking for the specified game
    ranking = rankings_dict.get(game_title, "Not ranked")

    # Search for the most recent play and notes
    cur.execute("""
        SELECT COALESCE( (SELECT g.id FROM games AS g 
        WHERE g.game_title ILIKE %s 
        AND ( (g.notes IS NOT NULL AND g.notes <> '' AND g.notes <> 'null') OR
        (g.result IS NOT NULL AND g.result <> '') )
    ORDER BY g.id DESC
        LIMIT 1),0)
    """, (f"%{game_title}%",))
    nonempty = cur.fetchone()

    # Fetch notes
    cur.execute("SELECT notes FROM games WHERE id = %s", nonempty)
    notes_nonempty = (res := cur.fetchone()) and res[0]

    # Fetch result
    cur.execute("SELECT result FROM games WHERE id = %s", (f"{nonempty[0]}",))
    result_nonempty = (res := cur.fetchone()) and res[0]

    # Fetch level
    cur.execute("SELECT level FROM games WHERE id = %s", (f"{nonempty[0]}",))
    level_nonempty = (res := cur.fetchone()) and res[0]

    # Fetch my_score
    cur.execute("SELECT my_score FROM games WHERE id = %s", (f"{nonempty[0]}",))
    my_score_nonempty = (res := cur.fetchone()) and res[0]

    # Fetch bot_score
    cur.execute("SELECT bot_score FROM games WHERE id = %s", (f"{nonempty[0]}",))
    bot_score_nonempty = (res := cur.fetchone()) and res[0]

    cur.close()
    conn.close()

    # Respond with JSON data, including stats
    if last_played:
        return jsonify({
            'notes': notes if notes else None,
            'result': result if result else None,
        'level': level if level else None,
        'my_score': my_score if my_score else None,
        'bot_score': bot_score if bot_score else None,
            'date_played': last_played[0].isoformat(),
            'notes_nonempty': notes_nonempty if notes_nonempty else None,
            'result_nonempty': result_nonempty if result_nonempty else None,
        'level_nonempty': level_nonempty if level_nonempty else None,
        'my_score_nonempty': my_score_nonempty if my_score_nonempty else None,
        'bot_score_nonempty': bot_score_nonempty if bot_score_nonempty else None,
            #'last_played_date': last_played_date.isoformat() if last_played_date else None,
            'total_times_played': total_plays,
            'played_this_week': played_this_week,
            'played_this_month': played_this_month,
            'played_this_year': played_this_year,
            'ranking': ranking
        })
    else:
        return jsonify({'Error': 'No record found for the specified game.'})
