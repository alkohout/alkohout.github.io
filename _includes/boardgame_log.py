
@app.route('/add', methods=['POST'])
def add_game():
    date_played = request.form['date_played']
    game_title = request.form['game_title']
    notes = request.form.get('notes', '')
    result = request.form.get('result','')
    level = request.form.get('level','')
    my_score = request.form.get('my_score','')
    bot_score = request.form.get('bot_score','')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO games (date_played, game_title, notes, result, level, my_score, bot_score) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (date_played, game_title, notes, result, level, my_score, bot_score)
    )
    conn.commit()

    cur.close()
    conn.close()

    # Redirect to the index page, passing stats as query parameters
    return redirect(url_for('index'))
