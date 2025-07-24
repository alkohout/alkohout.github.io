
@app.route('/games_overview')
def games_overview():
    conn = get_db_connection()
    cur = conn.cursor()

    # Calculate date boundaries
    today = date.today()
    # Current Periods
    start_of_week = today - timedelta(days=today.weekday())
    start_of_month = today.replace(day=1)
    start_of_year = today.replace(month=1, day=1)

    # Last Periods
    # Last Week
    end_of_last_week = start_of_week - timedelta(days=1)
    start_of_last_week = end_of_last_week - timedelta(days=6)
    # Last Month
    end_of_last_month = start_of_month - timedelta(days=1)
    start_of_last_month = end_of_last_month.replace(day=1)
    # Last Year
    end_of_last_year = start_of_year - timedelta(days=1)
    start_of_last_year = end_of_last_year.replace(month=1, day=1)

    # Define a helper function to fetch games for a period
    def fetch_games(start_date, end_date):
        cur.execute("""
            SELECT game_title, COUNT(*) as play_count
            FROM games
            WHERE date_played BETWEEN %s AND %s
            GROUP BY game_title
            ORDER BY play_count DESC
        """, (start_date, end_date))
        return cur.fetchall()

    # Fetch games for each period
    games_this_week = fetch_games(start_of_week, today)
    games_this_month = fetch_games(start_of_month, today)
    games_this_year = fetch_games(start_of_year, today)
    games_last_week = fetch_games(start_of_last_week, end_of_last_week)
    games_last_month = fetch_games(start_of_last_month, end_of_last_month)
    games_last_year = fetch_games(start_of_last_year, end_of_last_year)

    cur.close()
    conn.close()

    return render_template('games_overview.html',
                           games_this_week=games_this_week,
                           games_this_month=games_this_month,
                           games_this_year=games_this_year,
                           games_last_week=games_last_week,
                           games_last_month=games_last_month,
                           games_last_year=games_last_year)

