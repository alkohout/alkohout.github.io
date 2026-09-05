
# The logger is now a JSON API behind a bearer token; the static frontend
# posts to this rather than submitting a server-rendered form.
#
# Every column a per-game tracker needs is written here, and the helpers
# (spirit_island_fields, ares_fields, ...) return NULLs for a game that
# does not use them — so one endpoint serves every game.

@app.route('/api/add_game', methods=['POST'])
def api_add_game():
    data = request.get_json() or {}
    spirit, adversary, level, scenario = spirit_island_fields(data)
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO games (date_played, game_title, notes, result, level,"
            " my_score, bot_score, spirit, adversary, adversary_level, scenario,"
            " civilisation, my_civilisation, zoo_map, start_appeal,"
            " scenario_number, ares_temp_me, ares_oxygen_me, ares_oceans_me,"
            " ares_mc_me, ares_temp_bot, ares_oxygen_bot, ares_oceans_bot,"
            " ares_mc_bot)"
            " VALUES (" + ",".join(["%s"] * 24) + ") RETURNING id",
            (data.get('date_played'), data.get('game_title'), data.get('notes', ''),
             data.get('result', ''), data.get('level', ''),
             data.get('my_score', ''), data.get('bot_score', ''),
             spirit, adversary, level, scenario, imperium_civilisation(data),
             imperium_my_civilisation(data), *ark_nova_fields(data),
             scenario_number_value(data), *ares_fields(data))
        )
        # Returned so the form can attach a photo to the sitting it just made.
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'success': True, 'id': new_id})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

# The row itself carries a user_id and row-level security scopes it, so the
# endpoint does not have to be the boundary.
