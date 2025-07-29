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
      <div class="header-content">
        <div class="brand">
          <a href="https://alkohout.github.io" class="home-link">
            <img src="/assets/images/kohout.jpeg" alt="Alison Kohout" class="profile-img">
          </a>
          <span class="project-title">Board Game Logger Project</span>
        </div>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#data_entry">Data Entry</a></li>
                <li><a href="#analysis">Analysis</a></li>
                <li><a href="#search">Search</a></li>
                <li><a href="#special_features">Special Features</a></li>
            </ul>
        </nav>
        <div class="contact-links"> 
          <a href="mailto:kohoutal@gmail.com" aria-label="Email"> 
            <img src="/assets/images/mail_white.svg" alt="Email" class="contact-icon">
          </a>
          <a href="https://linkedin.com/in/alisonkohout" target="_blank" aria-label="LinkedIn">
            <img src="/assets/images/linkedin-White.png" alt="LinkedIn" class="contact-icon">
          </a>
          <a href="https://github.com/alkohout/" target="_blank" aria-label="GitHub">
            <img src="/assets/images/github-mark-white.png" alt="GitHub" class="contact-icon">
          </a>
        </div>
      </div>
    </header>

    <main>
    <section class="topics" id="home">
      <div class="topic-list">
        <div class="topic inverse">
          <h3>Overview</h3>
		<p>
		Seeking to enhance the efficiency of logging my board games, I developed a comprehensive data system that tracks gameplay and reveals performance patterns.

		By leveraging AI prompting techniques, I identified Flask and PostgreSQL as suitable technologies for building a functional local web application. 
		I then successfully implemented this solution despite having no previous web development background and only recently encountering SQL.

		This achievement demonstrates my capacity to rapidly acquire new technical skills and tackle intricate challenges. 
		More importantly, it marked an exciting and pivotal realization for me: with AI assistance complementing my abilities, my only limit is my imagination.
		</p>
<p>
        <a href="https://github.com/yourusername/board-game-logger" target="_blank">View the project on GitHub →</a>
      </p>
	</div>
      </div>
    </section>

    <section class="topics" id="data_entry">
      <div class="topic-list">
        <div class="topic inverse">
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
			Background image credited to © Ryan Laukat / Red Raven Games.
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
	</div>
      </div>
    </section>

    <section class="topics" id="analysis">
      <div class="topic-list">
        <div class="topic inverse">
          <h3>Comprehensive Analysis</h3>
		<p>
		The application provides detailed statistics, highlighting top played games and game counts by week, month, and year. 
		Users can access averages and identify the most played games over various time frames.
		</p>
          	<figure class="img-centre">
	              <img src="/assets/images/boardgame_stats.png"
	                   alt="Board game log screenshot">
	              <figcaption>
			Screenshot of basic board game statistics.
			Background image credited to © Ryan Laukat / Red Raven Games.
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

	</div>
      </div>
    </section>

    <section class="topics" id="search">
      <div class="topic-list">
        <div class="topic inverse">
          <h3>Advanced Search Functionality</h3>
		<p>
		With powerful search capabilities, users can find game data by title or other criteria. 
		Specialized routes cater to game-specific tracking, such as the Sleeping Gods and Imperium games.
		</p>
          	<figure class="img-centre" >
		      <p>
		      </p>
	              <img src="/assets/images/boardgame_extra.png"
	                   alt="Board game log screenshot">
	              <figcaption>
			Screenshot of the board game search capability.
			Background image credited to © Ryan Laukat / Red Raven Games.
		      </figcaption>
	        </figure>
          	<figure class="img-centre" >
		      <p>
		      </p>
	              <img src="/assets/images/boardgame_search.png"
	                   alt="Board game log screenshot">
	              <figcaption>
			Screenshot of an example search result.
			Background image credited to © Ryan Laukat / Red Raven Games.
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
	</div>
      </div>
    </section>

    <section class="topics" id="special_features">
      <div class="topic-list">
        <div class="topic inverse">

          <h3>Special Features for Enthusiasts</h3>
		<p>
		The project includes targeted features for Sleeping Gods, including totem tracking and resource management, as well as detailed win/loss statistics for the Imperium game—appealing to dedicated gamers.
		</p>
          	<figure class="img-centre" >
	              <img src="/assets/images/boardgame_sleepinggods_log.png"
	                   alt="Board game log screenshot">
	              <figcaption>
			A screenshot of all the logged details for the board game Sleeping Gods. Sleeping Gods is an adventure game about exploring a world.
			Keeping notes as you play is an essential aspect of the game.
			Background image credited to © Ryan Laukat / Red Raven Games.
		      </figcaption>
	        </figure>
          	<figure class="img-centre" >
	              <img src="/assets/images/boardgame_sleepinggods_search.png"
	                   alt="Board game log screenshot">
	              <figcaption>
			A screenshot of the search options specifically developed for the board game Sleeping Gods. 
			This is an essential tool for the adventure board game to help you make decisions about where to go and what to do.
			Background image credited to © Ryan Laukat / Red Raven Games.
		      </figcaption>
	        </figure>
	        <h6><strong>Code Snippet: Tracking games in Sleeping Gods </strong></h6>
       		<div class="code">
		     <div class="python">
                     {% highlight python %}
                     {% include boardgame_sleepinggods.py %}
                     {% endhighlight %}
       		     </div>
       		</div>
       		<div class="code">
		     <div class="html">
                     {% highlight html %}
                     {% include boardgame_sleepinggods.html %}
                     {% endhighlight %}
       		     </div>
       		</div>
          	<figure class="img-centre" >
	              <img src="/assets/images/boardgame_imperium_stats.png"
	                   alt="Board game log screenshot">
	              <figcaption>
			A screenshot of a list of win/loss statistics for Imperium. This page helps me decide which civilisation pair to attempt next.
		      </figcaption>
	        </figure>
	        <h6><strong>Code Snippet: Win / loss statistics for the board game Imperium </strong></h6>
       		<div class="code">
		     <div class="python">
                     {% highlight python %}
                     {% include boardgame_imperium_stats.py %}
                     {% endhighlight %}
       		     </div>
       		</div>
       		<div class="code">
		     <div class="html">
                     {% highlight html %}
                     {% include boardgame_imperium_stats.html %}
                     {% endhighlight %}
       		     </div>
       		</div>

        </div>
      </div>
    </section>
    </main>
    <footer>
        <p>&copy; {{ site.time | date: "%Y" }} {{ site.title }}</p>
    </footer>

</body>
</html>



