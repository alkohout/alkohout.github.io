---
layout: post
title: "Board Game Logger"
date: 2025-02-16
categories:
  - project 
tags:
  - board games 
  - SQL 
  - python
permalink: /projects/board_game_logger/
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Board Game Logger</title>
    <link rel="stylesheet" href="/assets/css/style.css"> 
    <!-- Site Visit Counter -->
    <script data-goatcounter="https://kohoutal.goatcounter.com/count"
       async src="//gc.zgo.at/count.js">
    </script>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="https://alkohout.github.io">Alison Kohout</a></li>
            </ul>
        </nav>
    </header>

    <main>
    <section class="topics">
      <div class="topic-list">
        <div class="topic inverse">
          <h2>Board Game Logger</h2>
          <h3>Overview</h3>
		<p>
		The SQL Logger is a dynamic web application developed using Flask and PostgreSQL, designed to track and analyze board game data. 
		This project showcases my skills in web development and database management, offering valuable insights into gameplay trends.
		</p>

          <h3>Data Entry and Management</h3>
		<p>
		Users can seamlessly input game details including date played, game title, notes, results, and various scores. 
		This data is securely stored and managed using a PostgreSQL database.
		</p>
          	<figure class="img-centre" >
		      <p>
		      </p>
	              <img src="/assets/images/boardgame_log.png"
	                   alt="Board game log screenshot">
	              <figcaption>
			Screenshot of the board game logger.
		      </figcaption>
	        </figure>
	        <p><strong>Code Snippet: Adding a played game to the database</strong></p>
       		<div class="code">
		     <div class="python">
                     {% highlight python %}
                     {% include boardgame_log.py %}
                     {% endhighlight %}
       		     </div>
       		</div>
       		<div class="code">
		     <div class="html">
                     {% highlight html %}
                     {% include boardgame_log.html %}
                     {% endhighlight %}
       		     </div>
       		</div>

          <h3>Comprehensive Analysis</h3>
		<p>
		The application provides detailed statistics, highlighting top played games and game counts by week, month, and year. 
		Users can access averages and identify the most played games over various time frames.
		</p>
          	<figure class="img-centre">
	              <img src="/assets/images/boardgame_stats.png"
	                   alt="Board game log screenshot">
	              <figcaption>
			Screenshot of the board game logger.
		      </figcaption>
	        </figure>
	        <p><strong>Code Snippet: Played board game statistics</strong></p>
       		<div class="code">
		     <div class="html">
                     {% highlight python %}
                     {% include boardgame_stats.py %}
                     {% endhighlight %}
       		     </div>
       		</div>
       		<div class="code">
		     <div class="html">
                     {% highlight html %}
                     {% include boardgame_stats.html %}
                     {% endhighlight %}
       		     </div>
       		</div>


          <h3>Advanced Search Functionality</h3>
		<p>
		With powerful search capabilities, users can find game data by title or other criteria. 
		Specialized routes cater to game-specific tracking, such as the "Sleeping Gods" and "Imperium" games.
		</p>
          	<figure class="img-centre" >
		      <p>
		      </p>
	              <img src="/assets/images/boardgame_extra.png"
	                   alt="Board game log screenshot">
	              <figcaption>
			Screenshot of the board game search capability.
		      </figcaption>
	        </figure>
          	<figure class="img-centre" >
		      <p>
		      </p>
	              <img src="/assets/images/boardgame_search.png"
	                   alt="Board game log screenshot">
	              <figcaption>
			Screenshot of an example search result.
		      </figcaption>
	        </figure>
	        <h6><strong>Code Snippet: Searching the database </strong></h6>
       		<div class="code">
		     <div class="python">
                     {% highlight python %}
                     {% include boardgame_search.py %}
                     {% endhighlight %}
       		     </div>
       		</div>
       		<div class="code">
		     <div class="html">
                     {% highlight html %}
                     {% include boardgame_extra.html %}
                     {% endhighlight %}
       		     </div>
       		</div>
          	<figure class="img-centre" >
	              <img src="/assets/images/boardgame_overview.png"
	                   alt="Board game log screenshot">
	              <figcaption>
			A screenshot of an overview of games played.
		      </figcaption>
	        </figure>
	        <h6><strong>Code Snippet: View an overview of the games played </strong></h6>
       		<div class="code">
		     <div class="python">
                     {% highlight python %}
                     {% include boardgame_overview.py %}
                     {% endhighlight %}
       		     </div>
       		</div>
       		<div class="code">
		     <div class="html">
                     {% highlight html %}
                     {% include boardgame_overview.html %}
                     {% endhighlight %}
       		     </div>
       		</div>
          	<figure class="img-centre" >
	              <img src="/assets/images/boardgame_all_sortBname.png"
	                   alt="Board game log screenshot">
	              <figcaption>
			A screenshot of a list of all games played sorted by name. Clicking on the header will reorder accordingly.
		      </figcaption>
	        </figure>
          	<figure class="img-centre" >
	              <img src="/assets/images/boardgame_all_sortBrank.png"
	                   alt="Board game log screenshot">
	              <figcaption>
			A screenshot of a list of all games played sorted by ranking. Clicking on the header will reorder accordingly.
		      </figcaption>
	        </figure>
	        <br>
	        <h6><strong>Code Snippet: View all games sorted by rank or name. </strong></h6>
       		<div class="code">
		     <div class="html">
                     {% highlight html %}
                     {% include boardgame_all_games.html %}
                     {% endhighlight %}
       		     </div>
       		</div>

          <h3>Interactive Updates</h3>
		<p>
		Users can update game notes and scores dynamically, allowing for current data and insights. 
		The application supports data updates and deletions through secure endpoints.
		</p>

          <h3>Special Features for Enthusiasts</h3>
		<p>
		The project includes targeted features for "Sleeping Gods," including totem tracking and resource management, as well as detailed win/loss statistics for the "Imperium" game—appealing to dedicated gamers.
		</p>

          <h3>Database Interaction</h3>
		<p>
		Utilizes psycopg2 for efficient and secure database connections, ensuring seamless data handling and user experiences.
		</p>

        </div>
      </div>
    </section>
    </main>
    <footer>
        <p>&copy; {{ site.time | date: "%Y" }} {{ site.title }}</p>
    </footer>

</body>
</html>


