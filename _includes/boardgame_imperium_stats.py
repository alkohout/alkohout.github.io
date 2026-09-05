
# Win/loss per civilisation, grouped by expansion.
#
# The imperium view reads `games` with security_invoker, so it applies
# row-level security as whoever is asking — the owner gate that used to sit
# here was the only thing making this the owner's alone.

@app.route('/api/imperium_stats')
def api_imperium_stats():
    conn = get_db_connection()
    cur = conn.cursor()
    # One pass over the plays; the per-civilisation tally happens here rather
    # than in the 56 separate count queries the old page used.
    cur.execute("SELECT level, result, civilisation FROM imperium")
    plays = [{'level': r[0], 'result': r[1], 'civilisation': r[2]}
             for r in cur.fetchall()]
    cur.close()
    conn.close()

    # The recorded deck if there is one, otherwise read the old free text.
    # Resolved once per play so a play can never be counted under two decks.
    for p in plays:
        p['civ'] = imperium_civ_of(p)
        p['res'] = (p['result'] or '').lower()

    expansions = []
    for expansion, name, stars in IMPERIUM_CIVS:
        mine = [p for p in plays if p['civ'] == name]
        if not expansions or expansions[-1]['expansion'] != expansion:
            expansions.append({'expansion': expansion, 'civilisations': []})
        expansions[-1]['civilisations'].append({
            'name': name, 'stars': stars,
            'won': sum(1 for p in mine if 'won' in p['res']),
            'lost': sum(1 for p in mine if 'lost' in p['res']),
            # A game left set up is logged more than once, so a row is a
            # sitting. Finished games are the ones carrying a result.
            'games': sum(1 for p in mine if 'won' in p['res'] or 'lost' in p['res']),
            'plays': len(mine),
            # How many still rely on the free text. Zero once backfilled, and
            # worth seeing if it ever climbs again.
            'from_text': sum(1 for p in mine if not p['civilisation']),
        })

    # Text that names no known deck: a new expansion, a typo, or a play with no
    # opponent recorded at all.
    unmatched = sorted({(p['level'] or '').strip() for p in plays
                        if (p['level'] or '').strip() and not p['civ']})

    finished = sum(1 for p in plays if 'won' in p['res'] or 'lost' in p['res'])
    return jsonify({'expansions': expansions, 'unmatched_levels': unmatched,
                    'total_plays': len(plays),
                    'total_games': finished,
                    'recorded': sum(1 for p in plays if p['civilisation']),
                    'from_text': sum(1 for p in plays
                                     if p['civ'] and not p['civilisation'])})
