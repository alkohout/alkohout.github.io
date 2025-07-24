
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT DISTINCT game_title FROM games")
    game_titles = [row[0] for row in cur.fetchall()]

    cur.execute("""
        SELECT game_title, COUNT(*) as play_count
        FROM games
        GROUP BY game_title
        ORDER BY play_count DESC
        LIMIT 5
    """)
    top_games = cur.fetchall()

    # Calculate date boundaries for the current week, month, and year
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    start_of_month = today.replace(day=1)
    start_of_year = today.replace(month=1, day=1)
    
    # Define date boundaries for last week, last month, and last year
    start_of_current_week = today - timedelta(days=today.weekday())
    end_of_last_week = start_of_current_week - timedelta(days=1)
    start_of_last_week = end_of_last_week - timedelta(days=6)

    start_of_current_month = today.replace(day=1)
    last_day_of_last_month = start_of_current_month - timedelta(days=1)
    start_of_last_month = last_day_of_last_month.replace(day=1)

    start_of_current_year = today.replace(month=1, day=1)
    last_day_of_last_year = start_of_current_year - timedelta(days=1)
    start_of_last_year = last_day_of_last_year.replace(month=1, day=1)

    # Count games played this week
    cur.execute("SELECT COUNT(*) FROM games WHERE date_played >= %s", (start_of_week,))
    games_this_week = cur.fetchone()[0]
    
    # Count games played this month
    cur.execute("SELECT COUNT(*) FROM games WHERE date_played >= %s", (start_of_month,))
    games_this_month = cur.fetchone()[0]
    
    # Count games played this year
    cur.execute("SELECT COUNT(*) FROM games WHERE date_played >= %s", (start_of_year,))
    games_this_year = cur.fetchone()[0]

    # Define date boundaries for last week, last month, and last year
    start_of_current_week = today - timedelta(days=today.weekday())
    end_of_last_week = start_of_current_week - timedelta(days=1)
    start_of_last_week = end_of_last_week - timedelta(days=6)

    start_of_current_month = today.replace(day=1)
    last_day_of_last_month = start_of_current_month - timedelta(days=1)
    start_of_last_month = last_day_of_last_month.replace(day=1)

    start_of_current_year = today.replace(month=1, day=1)
    last_day_of_last_year = start_of_current_year - timedelta(days=1)
    start_of_last_year = last_day_of_last_year.replace(month=1, day=1)

    # Games played last week
    cur.execute("SELECT COUNT(*) FROM games WHERE date_played BETWEEN %s AND %s", (start_of_last_week, end_of_last_week))
    games_last_week = cur.fetchone()[0]

    # Games played last month
    cur.execute("SELECT COUNT(*) FROM games WHERE date_played BETWEEN %s AND %s", (start_of_last_month, last_day_of_last_month))
    games_last_month = cur.fetchone()[0]

    # Games played last year
    cur.execute("SELECT COUNT(*) FROM games WHERE date_played BETWEEN %s AND %s", (start_of_last_year, last_day_of_last_year))
    games_last_year = cur.fetchone()[0]

    # Starting reference date for weekly and monthly averages calculation (removes the false 2023 data)
    start_date = date(2024, 1, 1)

    # End dates for averages (up to the start of the current period)
    end_of_last_week = start_of_week
    end_of_last_month = start_of_month
    end_of_last_year = start_of_year

    # Calculate total number of games and periods for averages
    # Weekly Average Calculation
    total_days = (end_of_last_week - start_date).days
    num_weeks = total_days // 7 if total_days >= 7 else 0

    if num_weeks > 0:
        cur.execute("SELECT COUNT(*) FROM games WHERE date_played >= %s AND date_played < %s", (start_date, end_of_last_week))
        total_games = cur.fetchone()[0]
        weekly_avg = round(total_games / num_weeks)
    else:
        weekly_avg = 0

    # Monthly Average Calculation
    num_months = (end_of_last_month.year - start_date.year) * 12 + (end_of_last_month.month - start_date.month)
    if num_months > 0:
        cur.execute("SELECT COUNT(*) FROM games WHERE date_played >= %s AND date_played < %s", (start_date, end_of_last_month))
        total_games = cur.fetchone()[0]
        monthly_avg = round(total_games / num_months)
    else:
        monthly_avg = 0

    # Yearly Average Calculation
    start_date = date(2023, 1, 1)
    num_years = end_of_last_year.year - start_date.year
    if num_years > 0:
        cur.execute("SELECT COUNT(*) FROM games WHERE date_played >= %s AND date_played < %s", (start_date, end_of_last_year))
        total_games = cur.fetchone()[0]
        yearly_avg = round(total_games / num_years)
    else:
        yearly_avg = 0

    # Most played game this week
    cur.execute("""
        SELECT game_title, COUNT(*) as play_count
        FROM games
        WHERE date_played >= %s
        GROUP BY game_title
        ORDER BY play_count DESC
        LIMIT 1
    """, (start_of_week,))
    most_played_this_week = cur.fetchone()
    if most_played_this_week:
        most_played_game_week = most_played_this_week[0]
        week_play_count = most_played_this_week[1]
    else:
        most_played_game_week = None
        week_play_count = 0

    # Most played game this month
    cur.execute("""
        SELECT game_title, COUNT(*) as play_count
        FROM games
        WHERE date_played >= %s
        GROUP BY game_title
        ORDER BY play_count DESC
        LIMIT 1
    """, (start_of_month,))
    most_played_this_month = cur.fetchone()
    if most_played_this_month:
        most_played_game_month = most_played_this_month[0]
        month_play_count = most_played_this_month[1]
    else:
        most_played_game_month = None
        month_play_count = 0

    # Most played game this year
    cur.execute("""
        SELECT game_title, COUNT(*) as play_count
        FROM games
        WHERE date_played >= %s
        GROUP BY game_title
        ORDER BY play_count DESC
        LIMIT 1
    """, (start_of_year,))
    most_played_this_year = cur.fetchone()
    if most_played_this_year:
        most_played_game_year = most_played_this_year[0]
        year_play_count = most_played_this_year[1]
    else:
        most_played_game_year = None
        year_play_count = 0

   # Most played game last week
    cur.execute("""
        SELECT game_title, COUNT(*) as play_count
        FROM games
        WHERE date_played BETWEEN %s AND %s
        GROUP BY game_title
        ORDER BY play_count DESC
        LIMIT 1
    """, (start_of_last_week, end_of_last_week))
    most_played_last_week = cur.fetchone()
    if most_played_last_week:
        most_played_game_last_week = most_played_last_week[0]
        last_week_play_count = most_played_last_week[1]
    else:
        most_played_game_last_week = None
        last_week_play_count = 0

    # Most played game last month
    cur.execute("""
        SELECT game_title, COUNT(*) as play_count
        FROM games
        WHERE date_played BETWEEN %s AND %s
        GROUP BY game_title
        ORDER BY play_count DESC
        LIMIT 1
    """, (start_of_last_month, last_day_of_last_month))
    most_played_last_month = cur.fetchone()
    if most_played_last_month:
        most_played_game_last_month = most_played_last_month[0]
        last_month_play_count = most_played_last_month[1]
    else:
        most_played_game_last_month = None
        last_month_play_count = 0

    # Most played game last year
    cur.execute("""
        SELECT game_title, COUNT(*) as play_count
        FROM games
        WHERE date_played BETWEEN %s AND %s
        GROUP BY game_title
        ORDER BY play_count DESC
        LIMIT 1
    """, (start_of_last_year, last_day_of_last_year))
    most_played_last_year = cur.fetchone()
    if most_played_last_year:
        most_played_game_last_year = most_played_last_year[0]
        last_year_play_count = most_played_last_year[1]
    else:
        most_played_game_last_year = None
        last_year_play_count = 0

    cur.close()
    conn.close()
    return render_template(
        'index.html',
        game_titles=sorted(game_titles),
        top_games=top_games,
        today=date.today().isoformat(),
        games_this_week=games_this_week,
        games_this_month=games_this_month,
        games_this_year=games_this_year,
        games_last_week=games_last_week,
        games_last_month=games_last_month,
        games_last_year=games_last_year,
        most_played_game_week=most_played_game_week,
        most_played_game_month=most_played_game_month,
        most_played_game_year=most_played_game_year,
        week_play_count=week_play_count,
        month_play_count=month_play_count,
        year_play_count=year_play_count,
    most_played_game_last_week=most_played_game_last_week,
    most_played_game_last_month=most_played_game_last_month,
    most_played_game_last_year=most_played_game_last_year,
    last_week_play_count=last_week_play_count,
    last_month_play_count=last_month_play_count,
    last_year_play_count=last_year_play_count,
        weekly_avg = weekly_avg,
        monthly_avg = monthly_avg,
        yearly_avg = yearly_avg
    )

@app.route('/search_games', methods=['GET'])
def search_games():
    search_term = request.args.get('term', '')
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT DISTINCT game_title FROM games WHERE game_title ILIKE %s", (f"%{search_term}%",))
    suggestions = [row[0] for row in cur.fetchall()]

    cur.close()
    conn.close()
    return jsonify({'suggestions': suggestions})

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
