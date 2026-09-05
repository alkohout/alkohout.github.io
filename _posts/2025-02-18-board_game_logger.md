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
  - Claude AI
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
                <li><a href="#special_features">Game Trackers</a></li>
                <li><a href="#accounts">Accounts</a></li>
                <li><a href="#selector">Game Selector</a></li>
                <li><a href="#rules_assistant">Rules Assistant</a></li>
                <li><a href="#database_query">Ask the Database</a></li>
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

		The project has grown well beyond its origins. It is now a multi-user application with approved accounts and
		database-enforced data isolation, per-game trackers for six different games, a weighted game selector for picking what to play,
		an AI rules assistant grounded in uploaded rulebook PDFs and BoardGameGeek forum content, and a natural-language
		interface that writes and runs its own SQL against the log.
		The frontend has been rebuilt as a static site deployed on GitHub Pages, communicating with the Flask backend via API calls.
		</p>
<p>
        <a href="https://github.com/alkohout/board_game_logger" target="_blank">[GitHub →]</a>
        &nbsp;&nbsp;
        <a href="https://alkohout.github.io/board_game_logger/dashboard.html" target="_blank">[Dashboard →]</a>
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
	        <h6><strong>Code Snippet: Search endpoints, and the autocomplete that calls them </strong></h6>
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

          <h3>Per-Game Trackers</h3>
		<p>
		Some games keep score in ways a generic log cannot capture. Each of these has its own page, built around
		the thing that game is actually about. A tracker only appears in the menu once that account has logged a
		play of the game, so nobody is shown pages for games they do not own.
		</p>
          <ul>
            <li><strong>Sleeping Gods</strong> — locations visited, totems collected, and how each voyage ended</li>
            <li><strong>Imperium</strong> — win/loss by civilisation, across every deck faced</li>
            <li><strong>Spirit Island</strong> — win grids by spirit, adversary, adversary level, and scenario</li>
            <li><strong>Ark Nova</strong> — results by zoo map against starting appeal</li>
            <li><strong>Cascadia</strong> — the solo scenario ladder, showing which rung is next</li>
            <li><strong>Ares Expedition</strong> — how close each finished game got to a terraformed board, charted per difficulty</li>
          </ul>
          <p>
            A recurring detail in all of them: a sitting logged with no result is a game left set up, not a loss,
            and is excluded from win rates rather than dragging them down.
          </p>
		<p>
		The two oldest trackers are shown below as examples.
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

    <section class="topics" id="accounts">
      <div class="topic-list">
        <div class="topic inverse">
          <h3>Accounts and Data Isolation</h3>
          <p>
            What began as a single-user local tool is now a multi-user application, which changes the security
            question entirely: it is no longer enough for the app to only ask for its own rows — the database
            has to refuse to return anyone else's.
          </p>
          <ul>
            <li>Sign-up creates a <em>pending</em> account and emails the owner; nobody can log in until they are approved</li>
            <li>The response to a sign-up is identical whether or not the email already exists, so the form cannot be used to discover accounts</li>
            <li>Signed bearer tokens carry a version number, so changing a password invalidates every token already issued</li>
            <li>Repeated failed logins for an address are throttled</li>
            <li><strong>PostgreSQL row-level security</strong> scopes every table to the account making the request</li>
            <li>The app connects as a restricted role, not a superuser; a superuser connection would silently ignore those policies, so the riskiest endpoints check for one and refuse to run</li>
            <li>Views run with the caller's privileges, so a view over a secured table cannot leak around the policy on it</li>
            <li>An owner-only admin page approves, suspends, and removes accounts</li>
          </ul>
          <h6><strong>Code Snippet: The shared fetch layer every page uses</strong></h6>
          <div class="code">
            <div class="javascript">
            {% highlight javascript %}
            {% include boardgame_api.js %}
            {% endhighlight %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="topics" id="photos">
      <div class="topic-list">
        <div class="topic inverse">
          <h3>Table Photographs</h3>
          <p>
            Plays can carry photographs of the table, attached to the logged game and viewable from the games list.
          </p>
          <p>
            Images are served through the same authenticated API as everything else rather than from a public URL,
            which would have undone the isolation the rest of the app enforces. Because an <code>&lt;img&gt;</code> tag
            cannot send an authorization header, the page fetches each photo in JavaScript and renders it from a blob URL.
          </p>
        </div>
      </div>
    </section>

    <section class="topics" id="selector">
      <div class="topic-list">
        <div class="topic inverse">
          <h3>Weighted Game Selector</h3>
          <p>
            Deciding what to play is half the battle. The game selector lets each player rank up to
            three preferences — first, second, and third choice — and then picks a game at random
            using weighted probabilities (first choice carries three times the weight of third choice).
          </p>
          <ul>
            <li>Each player submits up to three ranked game preferences</li>
            <li>A weighted random draw selects the game for the night</li>
            <li>The pool can be cleared and rebuilt between sessions</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="topics" id="rules_assistant">
      <div class="topic-list">
        <div class="topic inverse">
          <h3>AI Rules Assistant</h3>
          <p>
            The rules assistant uses the Claude API (Anthropic) to answer rules questions in natural language,
            grounded in the actual rulebook rather than relying solely on general training knowledge.
          </p>
          <ul>
            <li>Upload a rulebook PDF once per game — stored in the database and reused for all future questions</li>
            <li>Multiple rulebooks per game, so an expansion can be asked about alongside the base game</li>
            <li>Text is extracted from each PDF on upload and sent instead of page images — roughly a third of the tokens, which is what keeps a game like Spirit Island inside the context limit</li>
            <li>Books that are genuinely scanned images extract no text, so those are sent as pages automatically</li>
            <li>Page images can also be requested deliberately, with the cost shown before the question is asked</li>
            <li>Optionally paste BoardGameGeek forum threads as supplemental context, which are also cached per game</li>
            <li>Ask any rules question and receive a direct, rulebook-grounded answer</li>
            <li>Particularly useful mid-game when flipping through a rulebook is impractical</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="topics" id="database_query">
      <div class="topic-list">
        <div class="topic inverse">
          <h3>Ask the Database</h3>
          <p>
            A question in plain English — "which spirit have I won with most?" — is sent to Claude, which writes a
            PostgreSQL query against the live schema. The query is run, the rows are shown, and a second call turns
            them into a sentence or two of plain English. The generated SQL is displayed alongside the answer, so
            the working can always be checked.
          </p>
          <p>
            Running model-written SQL against a real database is the interesting part of this feature, and it is
            defended in layers rather than by trusting the model:
          </p>
          <ul>
            <li>Only a single <code>SELECT</code> or <code>WITH</code> statement is accepted, and a banned-keyword check rejects the rest</li>
            <li>The query runs in a genuinely read-only Postgres transaction — enforced by the database, not by parsing the SQL</li>
            <li>It executes as a restricted role that can read game rows and nothing else: no user table, no rulebooks</li>
            <li>Row-level security still applies, so a generated query cannot reach another account's data</li>
            <li>A statement timeout and a row cap bound what any single question can cost</li>
            <li>If the app detects it is connected as a superuser — which would bypass those policies — the feature disables itself and says why</li>
            <li>Questions the schema cannot answer come back as an explicit refusal rather than a guess</li>
          </ul>
          <h6><strong>Code Snippet: Validating and running model-written SQL</strong></h6>
          <div class="code">
            <div class="python">
            {% highlight python %}
            {% include boardgame_ask_database.py %}
            {% endhighlight %}
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="topics" id="credit">
      <div class="topic-list">
        <div class="topic inverse">
          <h3>AI Cost Control</h3>
          <p>
            The AI features cost real money per question, so the app accounts for it rather than hoping for the best.
          </p>
          <ul>
            <li>Every AI call records its token usage and cost, in both USD and NZD</li>
            <li>Each account holds a credit balance, with recent usage and top-up history shown on its own page</li>
            <li>Top-ups run through Stripe Checkout; the amount is chosen from a server-side list, and only the signed webhook marks a purchase paid — a success redirect can be forged, a signature cannot</li>
            <li>The rules assistant estimates what sending a rulebook as page images will cost <em>before</em> the question is asked</li>
            <li>Where a locally hosted model is configured, it answers instead — at no per-question cost — falling back to Claude if it is unreachable</li>
          </ul>
        </div>
      </div>
    </section>

    </main>
    <footer>
        <p>&copy; {{ site.time | date: "%Y" }} {{ site.title }}</p>
    </footer>

</body>
</html>



