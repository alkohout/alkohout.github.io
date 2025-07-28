
@app.route('/imperium')
def imperium():
    conn = get_db_connection()
    cur = conn.cursor()

    #// Abbasids ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Abbasids%' AND result ILIKE '%lost%'
    """)
    abba_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Abbasids%' AND result ILIKE '%won%'
    """)
    abba_won=cur.fetchone()[0]

    #// Aksumites ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Aksumites%' AND result ILIKE '%lost%'
    """)
    aksu_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Aksumites%' AND result ILIKE '%won%'
    """)
    aksu_won=cur.fetchone()[0]

    #// Arthurians ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Arthurians%' AND result ILIKE '%lost%'
    """)
    arth_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Arthurians%' AND result ILIKE '%won%'
    """)
    arth_won=cur.fetchone()[0]

    #// Atlanteans ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Atlant%' AND result ILIKE '%lost%'
    """)
    atlant_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Atlant%' AND result ILIKE '%won%'
    """)
    atlant_won=cur.fetchone()[0]

    #// Carthaginians ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Carthag%' AND result ILIKE '%lost%'
    """)
    carthag_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Carthag%' AND result ILIKE '%won%'
    """)
    carthag_won=cur.fetchone()[0]

    #// Celts ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%celt%' AND result ILIKE '%lost%'
    """)
    celts_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Celt%' AND result ILIKE '%won%'
    """)
    celts_won=cur.fetchone()[0]

    #// Cultists ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%cult%' AND result ILIKE '%lost%'
    """)
    cult_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%cult%' AND result ILIKE '%won%'
    """)
    cult_won=cur.fetchone()[0]

    #// Egyptians ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Egyptians%' AND result ILIKE '%lost%'
    """)
    egyp_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Egyptians%' AND result ILIKE '%won%'
    """)
    egyp_won=cur.fetchone()[0]

    #// Greeks ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Greek%' AND result ILIKE '%lost%'
    """)
    greek_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Greek%' AND result ILIKE '%won%'
    """)
    greek_won=cur.fetchone()[0]

    #// Macedonian ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Macedonian%' AND result ILIKE '%lost%'
    """)
    mace_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Macedonian%' AND result ILIKE '%won%'
    """)
    mace_won=cur.fetchone()[0]

    #// Mauryans ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Mauryans%' AND result ILIKE '%lost%'
    """)
    mau_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Mauryans%' AND result ILIKE '%won%'
    """)
    mau_won=cur.fetchone()[0]

    #// Minoans ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Minoans%' AND result ILIKE '%lost%'
    """)
    min_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Minoans%' AND result ILIKE '%won%'
    """)
    min_won=cur.fetchone()[0]

    #// Olmecs ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Olmecs%' AND result ILIKE '%lost%'
    """)
    olm_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Olmecs%' AND result ILIKE '%won%'
    """)
    olm_won=cur.fetchone()[0]

    #// Persians ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Persian%' AND result ILIKE '%lost%'
    """)
    persian_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Persian%' AND result ILIKE '%won%'
    """)
    persian_won=cur.fetchone()[0]

    #// Qin ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Qin%' AND result ILIKE '%lost%'
    """)
    qin_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Qin%' AND result ILIKE '%won%'
    """)
    qin_won=cur.fetchone()[0]

    #// Scythians ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Scythians%' AND result ILIKE '%lost%'
    """)
    scy_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Scythians%' AND result ILIKE '%won%'
    """)
    scy_won=cur.fetchone()[0]

    #// Utopians ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Utopians%' AND result ILIKE '%lost%'
    """)
    uto_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Utopians%' AND result ILIKE '%won%'
    """)
    uto_won=cur.fetchone()[0]

    #// Vikings ////////////////////////////////////////////////////
    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Viking%' AND result ILIKE '%lost%'
    """)
    vik_lost=cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*) 
        FROM imperium 
        WHERE level ILIKE '%Viking%' AND result ILIKE '%won%'
    """)
    vik_won=cur.fetchone()[0]

    return render_template(
        'imperium.html',
	abba_lost=abba_lost,
	abba_won=abba_won,
	aksu_lost=aksu_lost,
	aksu_won=aksu_won,
	arth_lost=arth_lost,
	arth_won=arth_won,
	atlant_lost=atlant_lost,
	atlant_won=atlant_won,
	carthag_lost=carthag_lost,
	carthag_won=carthag_won,
	celts_lost=celts_lost,
	celts_won=celts_won,
	cult_lost=cult_lost,
	cult_won=cult_won,
	egyp_lost=egyp_lost,
	egyp_won=egyp_won,
	greek_lost=greek_lost,
	greek_won=greek_won,
	mace_lost=mace_lost,
	mace_won=mace_won,
	mau_lost=mau_lost,
	mau_won=mau_won,
	min_lost=min_lost,
	min_won=min_won,
	olm_lost=olm_lost,
	olm_won=olm_won,
	persian_lost=persian_lost,
	persian_won=persian_won,
	qin_lost=qin_lost,
	qin_won=qin_won,
	scy_lost=scy_lost,
	scy_won=scy_won,
	uto_lost=uto_lost,
	uto_won=uto_won,
	vik_lost=vik_lost,
	vik_won=vik_won
    )
