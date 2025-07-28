
@app.route('/sleeping_gods', methods=['GET', 'POST'])
def sleeping_gods():

    if request.method == 'POST':

        # Get other form data
        location_raw = request.form.get('location', '').strip()
        location = int(location_raw) if location_raw else 0
        part = request.form.get('part', '')
        required_keyword = request.form.get('required_keyword', '')
        gained_keyword = request.form.get('gained_keyword', '')
        visited = '1' if request.form.get('visited') == '1' else '0'
        notes = request.form.get('notes', '')
        combat = '1' if request.form.get('combat') == '1' else '0'
        combat_level_raw = request.form.get('combat_level', '').strip()
        combat_level = int(combat_level_raw) if combat_level_raw else 0
        gained = request.form.get('gained', '')
        req_coins_raw = request.form.get('req_coins', '').strip()
        req_coins = int(req_coins_raw) if req_coins_raw else 0
        req_meat_raw = request.form.get('req_meat', '').strip()
        req_meat = int(req_meat_raw) if req_meat_raw else 0
        req_veg_raw = request.form.get('req_veg', '').strip()
        req_veg = int(req_veg_raw) if req_veg_raw else 0
        req_grain_raw = request.form.get('req_grain', '').strip()
        req_grain = int(req_grain_raw) if req_grain_raw else 0
        req_wood_raw = request.form.get('req_wood', '').strip()
        req_wood = int(req_wood_raw) if req_wood_raw else 0
        req_artifacts_raw = request.form.get('req_artifacts', '').strip()
        req_artifacts = int(req_artifacts_raw) if req_artifacts_raw else 0
        gain_coins_raw = request.form.get('gain_coins', '').strip()
        gain_coins = int(gain_coins_raw) if gain_coins_raw else 0
        gain_meat_raw = request.form.get('gain_meat', '').strip()
        gain_meat = int(gain_meat_raw) if gain_meat_raw else 0
        gain_veg_raw = request.form.get('gain_veg', '').strip()
        gain_veg = int(gain_veg_raw) if gain_veg_raw else 0
        gain_grain_raw = request.form.get('gain_grain', '').strip()
        gain_grain = int(gain_grain_raw) if gain_grain_raw else 0
        gain_wood_raw = request.form.get('gain_wood', '').strip()
        gain_wood = int(gain_wood_raw) if gain_wood_raw else 0
        gain_artifacts_raw = request.form.get('gain_artifacts', '').strip()
        gain_artifacts = int(gain_artifacts_raw) if gain_artifacts_raw else 0
        gain_xp_raw = request.form.get('gain_xp', '').strip()
        gain_xp = int(gain_xp_raw) if gain_xp_raw else 0
        gain_adventure_raw = request.form.get('gain_adventure', '').strip()
        gain_adventure = int(gain_adventure_raw) if gain_adventure_raw else 0
        gain_ship_damage_raw = request.form.get('gain_ship_damage', '').strip()
        gain_ship_damage = int(gain_ship_damage_raw) if gain_ship_damage_raw else 0
        gain_ship_repair_raw = request.form.get('gain_ship_repair', '').strip()
        gain_ship_repair = int(gain_ship_repair_raw) if gain_ship_repair_raw else 0
        gain_crew_damage_raw = request.form.get('gain_crew_damage', '').strip()
        gain_crew_damage = int(gain_crew_damage_raw) if gain_crew_damage_raw else 0
        gain_crew_health_raw = request.form.get('gain_crew_health', '').strip()
        gain_crew_health = int(gain_crew_health_raw) if gain_crew_health_raw else 0
        gain_low_morale_raw = request.form.get('gain_low_morale', '').strip()
        gain_low_morale = int(gain_low_morale_raw) if gain_low_morale_raw else 0
        gain_fright_raw = request.form.get('gain_fright', '').strip()
        gain_fright = int(gain_fright_raw) if gain_fright_raw else 0
        gain_venom_raw = request.form.get('gain_venom', '').strip()
        gain_venom = int(gain_venom_raw) if gain_venom_raw else 0
        gain_weakness_raw = request.form.get('gain_weakness', '').strip()
        gain_weakness = int(gain_weakness_raw) if gain_weakness_raw else 0
        gain_madness_raw = request.form.get('gain_madness', '').strip()
        gain_madness = int(gain_madness_raw) if gain_madness_raw else 0
        remove_low_morale_raw = request.form.get('remove_low_morale', '').strip()
        remove_low_morale = int(remove_low_morale_raw) if remove_low_morale_raw else 0
        remove_fright_raw = request.form.get('remove_fright', '').strip()
        remove_fright = int(remove_fright_raw) if remove_fright_raw else 0
        remove_venom_raw = request.form.get('remove_venom', '').strip()
        remove_venom = int(remove_venom_raw) if remove_venom_raw else 0
        remove_weakness_raw = request.form.get('remove_weakness', '').strip()
        remove_weakness = int(remove_weakness_raw) if remove_weakness_raw else 0
        remove_madness_raw = request.form.get('remove_madness', '').strip()
        remove_madness = int(remove_madness_raw) if remove_madness_raw else 0
        gain_totem = request.form.get('gain_totem', '')
        challenge = request.form.get('challenge', '')
        challenge_level_raw = request.form.get('challenge_level', '').strip()
        challenge_level = int(challenge_level_raw) if challenge_level_raw else 0

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO sleeping_gods (location, part, required_keyword, gained_keyword, visited, notes, combat, combat_level, gained, req_coins, req_meat, req_veg, req_grain, req_wood, req_artifacts, gain_coins, gain_meat, gain_veg, gain_grain, gain_wood, gain_artifacts, gain_xp, gain_ship_damage, gain_ship_repair, gain_crew_damage, gain_crew_health, gain_low_morale, gain_fright, gain_venom, gain_weakness, gain_madness, remove_low_morale, remove_fright, remove_venom, remove_weakness, remove_madness, gain_totem, challenge, challenge_level, gain_adventure) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (location, part, required_keyword, gained_keyword, visited, notes, combat, combat_level, gained, req_coins, req_meat, req_veg, req_grain, req_wood, req_artifacts, gain_coins, gain_meat, gain_veg, gain_grain, gain_wood, gain_artifacts, gain_xp, gain_ship_damage, gain_ship_repair, gain_crew_damage, gain_crew_health, gain_low_morale, gain_fright, gain_venom, gain_weakness, gain_madness, remove_low_morale, remove_fright, remove_venom, remove_weakness, remove_madness, gain_totem, challenge, challenge_level, gain_adventure)
        )
        conn.commit()

        cur.close()
        conn.close()

    return render_template(
        'sleeping_gods.html',
    )

@app.route('/search_sleeping_gods_location', methods=['GET'])
def search_sleeping_gods_location():
    location = request.args.get('term', '0')
    conn = get_db_connection()
    cur = conn.cursor()

    # Search  
    cur.execute("""
        SELECT id,* FROM sleeping_gods  
        WHERE location = %s 
    """, (location,))
    results = cur.fetchall()
    cur.close()
    conn.close()

    # Convert the results to a list of dictionaries
    data = [
        {       
	    'id': row[0],
	    'location': row[1],
	    'part': row[2],
	    'required_keyword': row[3],
	    'gained_keyword': row[4],
	    'visited': row[5],
	    'notes': row[6],
	    'combat': row[7],
	    'combat_level': row[8],
	    'gained': row[9],
	    'lost': row[10],
	    'req_coins': row[11],
	    'req_meat': row[12],
	    'req_veg': row[13],
	    'req_grain': row[14],
	    'req_artifacts': row[15],
	    'gain_coins': row[16],
	    'gain_meat': row[17],
	    'gain_veg': row[18],
	    'gain_grain': row[19],
	    'gain_artifacts': row[20],
	    'req_wood': row[21],
	    'gain_wood': row[22],
	    'gain_xp': row[23],
	    'gain_ship_damage': row[24],
	    'gain_ship_repair': row[25],
	    'gain_crew_damage': row[26],
	    'gain_crew_health': row[27],
	    'gain_low_morale': row[28],
	    'gain_fright': row[29],
	    'gain_venom': row[30],
	    'gain_weakness': row[31],
	    'gain_madness': row[32],
	    'remove_low_morale': row[33],
	    'remove_fright': row[34],
	    'remove_venom': row[35],
	    'remove_weakness': row[36],
	    'remove_madness': row[37],
	    'totem': row[38],
	    'challenge': row[39],
	    'challenge_level': row[40],
	    'gain_totem': row[41],
	    'gain_adventure': row[42],
        }
        for row in results
    ]

    return jsonify(data)

@app.route('/search_sleeping_gods_notes', methods=['GET'])
def search_sleeping_gods_notes():
    keyword = request.args.get('term', '0')
    conn = get_db_connection()
    cur = conn.cursor()

    # Search  
    cur.execute("""
        SELECT id,* FROM sleeping_gods  
        WHERE notes ILIKE %s 
           OR required_keyword ILIKE %s
           OR gained_keyword ILIKE %s
	   OR gained ILIKE %s
	   OR lost ILIKE %s
    """, (f"%{keyword}%", f"%{keyword}%",f"%{keyword}%",f"%{keyword}%",f"%{keyword}%"))
    results = cur.fetchall()
    cur.close()
    conn.close()

    # Convert the results to a list of dictionaries
    data = [
        {       
	    'id': row[0],
	    'location': row[1],
	    'part': row[2],
	    'required_keyword': row[3],
	    'gained_keyword': row[4],
	    'visited': row[5],
	    'notes': row[6],
	    'combat': row[7],
	    'combat_level': row[8],
	    'gained': row[9],
	    'lost': row[10],
	    'req_coins': row[11],
	    'req_meat': row[12],
	    'req_veg': row[13],
	    'req_grain': row[14],
	    'req_artifacts': row[15],
	    'gain_coins': row[16],
	    'gain_meat': row[17],
	    'gain_veg': row[18],
	    'gain_grain': row[19],
	    'gain_artifacts': row[20],
	    'req_wood': row[21],
	    'gain_wood': row[22],
	    'gain_xp': row[23],
	    'gain_ship_damage': row[24],
	    'gain_ship_repair': row[25],
	    'gain_crew_damage': row[26],
	    'gain_crew_health': row[27],
	    'gain_low_morale': row[28],
	    'gain_fright': row[29],
	    'gain_venom': row[30],
	    'gain_weakness': row[31],
	    'gain_madness': row[32],
	    'remove_low_morale': row[33],
	    'remove_fright': row[34],
	    'remove_venom': row[35],
	    'remove_weakness': row[36],
	    'remove_madness': row[37],
	    'totem': row[38],
	    'challenge': row[39],
	    'challenge_level': row[40],
	    'gain_totem': row[41],
	    'gain_adventure': row[42],
        }
        for row in results
    ]

    return jsonify(data)

@app.route('/search_sleeping_gods_keyword', methods=['GET'])
def search_sleeping_gods_keyword():
    keyword = request.args.get('term', '')
    conn = get_db_connection()
    cur = conn.cursor()

    # Search  
    cur.execute("""
        SELECT id,* FROM sleeping_gods  
        WHERE required_keyword ILIKE %s OR
              gained_keyword ILIKE %s 
    """, (f"%{keyword}%", f"%{keyword}%"))
    results = cur.fetchall()
    cur.close()
    conn.close()

    # Convert the results to a list of dictionaries
    data = [
        {       
	    'id': row[0],
	    'location': row[1],
	    'part': row[2],
	    'required_keyword': row[3],
	    'gained_keyword': row[4],
	    'visited': row[5],
	    'notes': row[6],
	    'combat': row[7],
	    'combat_level': row[8],
	    'gained': row[9],
	    'lost': row[10],
	    'req_coins': row[11],
	    'req_meat': row[12],
	    'req_veg': row[13],
	    'req_grain': row[14],
	    'req_artifacts': row[15],
	    'gain_coins': row[16],
	    'gain_meat': row[17],
	    'gain_veg': row[18],
	    'gain_grain': row[19],
	    'gain_artifacts': row[20],
	    'req_wood': row[21],
	    'gain_wood': row[22],
	    'gain_xp': row[23],
	    'gain_ship_damage': row[24],
	    'gain_ship_repair': row[25],
	    'gain_crew_damage': row[26],
	    'gain_crew_health': row[27],
	    'gain_low_morale': row[28],
	    'gain_fright': row[29],
	    'gain_venom': row[30],
	    'gain_weakness': row[31],
	    'gain_madness': row[32],
	    'remove_low_morale': row[33],
	    'remove_fright': row[34],
	    'remove_venom': row[35],
	    'remove_weakness': row[36],
	    'remove_madness': row[37],
	    'totem': row[38],
	    'challenge': row[39],
	    'challenge_level': row[40],
	    'gain_totem': row[41],
	    'gain_adventure': row[42],
        }
        for row in results
    ]

    return jsonify(data)

@app.route('/delete_sleeping_gods_row', methods=['POST'])
def delete_sleeping_gods_row():
    data = request.get_json(force=True)
    row_id = data.get('id')
    if not row_id:
        return jsonify({'success': False, 'error': 'id missing'}), 400

    try:
        with get_db_connection() as conn, conn.cursor() as cur:
            cur.execute("DELETE FROM sleeping_gods WHERE id = %s", (row_id,))
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/reset_visited_sleeping_gods', methods=['POST'])
def reset_visited_sleeping_gods():
    try:
        # Connect to your database
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Update all records to set visited to 0
        cursor.execute('UPDATE sleeping_gods SET visited = FALSE')
        
        # Commit the changes
        conn.commit()
        
        # Close the connection
        cursor.close()
        conn.close()
        
        return jsonify({'success': True})

    except Exception as e:
        print(e)  # For debugging
        return jsonify({'success': False, 'error': str(e)})

@app.route('/sleeping_gods_totems_update', methods=['POST'])
def sleeping_gods_totems_update():
    try:
        data = request.get_json()
        totem_id = data['totemId']
        is_found = data['isFound']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE sleeping_gods_totems SET found = %s WHERE id = %s", (bool(is_found), totem_id))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        print(f"Error updating totem checklist: {e}")
        return jsonify({'success': False, 'message': str(e)}), 500  #Return error message

@app.route('/sleeping_gods_totems')
def sleeping_gods_totems():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, totem, found FROM sleeping_gods_totems ORDER BY id") 
    rows = cur.fetchall()
    cur.close()
    conn.close()

    totems = [{'id': row[0], 'totem': row[1], 'found': row[2]} for row in rows]
    return render_template('sleeping_gods_totems.html', totems=totems)
