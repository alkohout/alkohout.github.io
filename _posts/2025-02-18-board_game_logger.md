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
	        <p><strong>Code Snippet: Adding a played game to the database</strong></p>
          	<figure class="img-right" style="max-width: 35%">
	              <img src="/assets/images/boardgame_log.png"
	                   alt="Board game log screenshot">
	              <figcaption>
			Screenshot of the board game logger.
		      </figcaption>
	        </figure>
       		<div class="code">
	              {% highlight python %}
       		      {% include boardgame_log.py %}
       		      {% endhighlight %}
       		</div>
       		<div class="code">
	              {% highlight html %}
       		      {% include boardgame_log.html %}
       		      {% endhighlight %}
       		</div>

          <h3>Comprehensive Analysis</h3>
		<p>
		The application provides detailed statistics, highlighting top played games and game counts by week, month, and year. 
		Users can access averages and identify the most played games over various time frames.
		</p>
	        <p><strong>Code Snippet: Played board game statistics</strong></p>
          	<figure class="img-right" style="max-width: 35%">
	              <img src="/assets/images/boardgame_stats.png"
	                   alt="Board game log screenshot">
	              <figcaption>
			Screenshot of the board game logger.
		      </figcaption>
	        </figure>
       		<div class="code">
	              {% highlight html %}

<div class="form-container">
    <h2>Games played</h2>
    <table style="border-collapse: separate; border-spacing: 20px 0;">
      <tr>
        <th style="padding: 10px; text-align: left;"></th>
        <th style="padding: 10px; text-align: left;">Week</th>
        <th style="padding: 10px; text-align: left;">Month</th>
        <th style="padding: 10px; text-align: left;">Year</th>
      </tr>
      <tr>
        <td style="padding: 10px;">Current</td>
        <td style="padding: 10px;">{{games_this_week}}</td>
        <td style="padding: 10px;">{{games_this_month}}</td>
        <td style="padding: 10px;">{{games_this_year}}</td>
      </tr>
      <tr>
        <td style="padding: 10px;">Previous</td>
        <td style="padding: 10px;">{{games_last_week}}</td>
        <td style="padding: 10px;">{{games_last_month}}</td>
        <td style="padding: 10px;">{{games_last_year}}</td>
      </tr>
      <tr>
        <td style="padding: 10px;">Average</td>
        <td style="padding: 10px;">{{weekly_avg}}</td>
        <td style="padding: 10px;">{{monthly_avg}}</td>
        <td style="padding: 10px;">{{yearly_avg}}</td>
      </tr>
    </table>

    <h2>Most Played Games</h2>
    <table style="border-collapse: separate; border-spacing: 20px 0;">
      <tr>
        <th style="padding: 10px; text-align: left;"></th>
        <th style="padding: 10px; text-align: left;">Game</th>
        <th style="padding: 10px; text-align: left;">Plays</th>
      </tr>
      <tr>
        <td style="padding: 10px;">Current Week</td>
        <td style="padding: 10px;">{{most_played_game_week}}</td>
        <td style="padding: 10px;">{{week_play_count}}</td>
      </tr>
      <tr>
        <td style="padding: 10px;">Previous Week</td>
        <td style="padding: 10px;">{{most_played_game_last_week}}</td>
        <td style="padding: 10px;">{{last_week_play_count}}</td>
      </tr>
      <tr>
        <td style="padding: 10px;">Current Month</td>
        <td style="padding: 10px;">{{most_played_game_month}}</td>
        <td style="padding: 10px;">{{month_play_count}}</td>
      </tr>
      <tr>
        <td style="padding: 10px;">Previous Month</td>
        <td style="padding: 10px;">{{most_played_game_last_month}}</td>
        <td style="padding: 10px;">{{last_month_play_count}}</td>
      </tr>
      <tr>
        <td style="padding: 10px;">Current Year</td>
        <td style="padding: 10px;">{{most_played_game_year}}</td>
        <td style="padding: 10px;">{{year_play_count}}</td>
      </tr>
      <tr>
        <td style="padding: 10px;">Previous Year</td>
        <td style="padding: 10px;">{{most_played_game_last_year}}</td>
        <td style="padding: 10px;">{{last_year_play_count}}</td>
      </tr>
    </table>

    <h3>Top 5</h3>
    <ul id="top_games">
        {% for game, count in top_games %}
            <li>{{ game }} - {{ count }} </li>
        {% endfor %}
    </ul>
</div>

       		      {% endhighlight %}
       		</div>

          <h3>Advanced Search Functionality</h3>
		<p>
		With powerful search capabilities, users can find game data by title or other criteria. 
		Specialized routes cater to game-specific tracking, such as the "Sleeping Gods" and "Imperium" games.
		</p>

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


