---
layout: post
title: "Food–Body Connection"
date: 2025-12-24
categories:
  - projects 
tags:
  - SQL
  - Machine Learning
  - FastAPI
  - Claude AI
permalink: /projects/food_body_connection/
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Food–Body Connection</title>
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
      <span class="project-title">Food–Body Connection</span>
    </div>

    <nav>
      <ul>
        <li><a href="https://alkohout.github.io/projects/food_body_connection/">Home</a></li>
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
<section id="home" class="topics">
<div class="topic-list">

  <!-- Overview -->
  <div class="topic inverse">
   <div class="topic inverse">
    <h1>Food–Body Connection</h1>
    <figure class="img-left" style="max-width: 15%">
        <a href="https://alkohout.github.io/food_body_connection/" target="_blank" rel="noopener noreferrer">
          <img src="/assets/images/background_iphone.png"
               alt="ICON">
        </a>
    </figure>
    <p>
      Food–Body Connection is a full‑stack health analytics application designed to help users
      identify potential food or environmental allergens associated with adverse symptoms.
      Users log exposures and symptoms over time, and the system applies statistical analysis
    </p>
    <p>
      The goal is <strong>decision support — not diagnosis</strong>. The application highlights
      candidate trigger foods to investigate further and provides structured insights that can
      be discussed with healthcare professionals.
    </p>
   </div>
  </div>

  <!-- What the App Does -->
  <div class="topic inverse">
    <h2>What the app does</h2>
    <ul>
      <li>Logs allergen exposure events with quantities and timestamps</li>
      <li>Logs symptom events with severity and timing</li>
      <li>Allows logged entries to be reviewed, edited, or deleted after the fact</li>
      <li>Tracks twice-daily check-ins covering mood, sleep, fatigue, gut health, stress, and more</li>
      <li>Logs medications and active regimens with dose and date tracking</li>
      <li>Prescribes and logs strength training sessions, adjusting load to logged symptoms</li>
      <li>Accepts uploaded health documents (PDF, DOCX, text) for contextual AI analysis</li>
      <li>Stores structured health data in a relational PostgreSQL database with field-level encryption</li>
      <li>Aligns exposure and symptom events using time‑aware windows</li>
      <li>Analyzes relationships between allergens and symptoms</li>
      <li>Generates personalized AI-powered reports highlighting potential trigger foods</li>
      <li>Supports elimination diets and long‑term tracking strategies</li>
      <li>Installable as a Progressive Web App for offline access</li>
    </ul>
  </div>

  <!-- Analysis & Modeling -->
  <div class="topic inverse">
    <h2>Statistical & machine‑learning analysis</h2>
    <p>
      The system is designed for real‑world health data: frequent exposures, rare symptoms,
      delayed responses, and small sample sizes. Models prioritize interpretability and
      robustness over raw predictive power.
    </p>

    <h3>Logistic Regression</h3>
    <ul>
      <li>Estimates the probability that an allergen is associated with symptom occurrence</li>
      <li>Produces interpretable odds ratios for each allergen</li>
      <li>Uses regularization and class weighting to handle imbalance</li>
      <li>Evaluated using ROC AUC, symptom recall, and bootstrapped confidence intervals</li>
    </ul>

    <h3>Fisher Exact Test</h3>
    <ul>
      <li>Exact statistical test for association in small or sparse datasets</li>
      <li>Confirms associations suggested by regression models</li>
      <li>Reports p‑values for allergen–symptom relationships</li>
    </ul>

    <h3>Ordinal Logistic Regression (Dose–Response)</h3>
    <ul>
      <li>Models the relationship between exposure volume and symptom severity</li>
      <li>Preserves ordinal symptom intensity information</li>
      <li>Produces odds ratios with confidence intervals for exposure dose</li>
      <li>Supports sensitivity analysis across different post‑exposure time windows</li>
    </ul>

    <h3>Cyclical Headache Forecast</h3>
    <ul>
      <li>Estimates the probability of a symptom day for each day of a recurring cycle</li>
      <li>Uses the empirical per-cycle-day hit rate across all completed cycles</li>
      <li>Smooths circularly across adjacent cycle days, since a handful of cycles makes any single day far too noisy</li>
      <li>Projects forward as three coarse likelihood bands — enough to rank days, not to quote a percentage</li>
    </ul>

    <h3>Medication Change Analysis</h3>
    <ul>
      <li>Rebuilds total daily dose as a step function to locate the points where it changed</li>
      <li>Compares symptom rates in equal-length windows before and after a change</li>
      <li>Reports a rate ratio with an exact Poisson confidence interval</li>
      <li>Observational and uncontrolled — the plot states plainly that it shows no causation</li>
    </ul>

    <h3>AI‑Powered Summary & Chat</h3>
    <ul>
      <li>Generates natural‑language health summaries using Claude (Anthropic API)</li>
      <li>Provides a conversational chat interface grounded in the user's own tracking data</li>
      <li>Queries logged training sets and aggregates training volume through structured tool calls</li>
      <li>Incorporates uploaded health documents as additional context for responses</li>
      <li>Clearly scoped to data interpretation — not medical diagnosis</li>
    </ul>
  </div>

  <!-- Technology Stack -->
  <div class="topic inverse">
    <h2>Technology stack</h2>
    <p>
      The application is deployed as a cloud‑based system with a static frontend and a secure
      API backend.
    </p>
    <ul>
      <li><strong>Backend:</strong> FastAPI (Python)</li>
      <li><strong>Database:</strong> PostgreSQL on NEON</li>
      <li><strong>ORM:</strong> SQLAlchemy</li>
      <li><strong>Authentication:</strong> JWT‑based authentication with password reset flow</li>
      <li><strong>AI:</strong> Claude (Anthropic API) for health summaries and chat</li>
      <li><strong>Analysis:</strong> Statistical modeling and supervised machine learning</li>
      <li><strong>Data security:</strong> Field-level encryption on all sensitive health data</li>
      <li><strong>Frontend:</strong> Static Progressive Web App hosted on <a href="https://github.com/alkohout/food_body_connection" target="_blank" rel="noopener noreferrer">GitHub Pages</a></li>
    </ul>
  </div>

  <!-- Architecture -->
  <div class="topic inverse">
    <h2>System architecture</h2>
    <p>
      Static Frontend (<a href="https://github.com/alkohout/food_body_connection" target="_blank" rel="noopener noreferrer">GitHub Pages</a>) → HTTPS (JWT‑authenticated API calls) →
      FastAPI Backend (Oracle) → PostgreSQL Database (NEON)
    </p>
    <p>
      The backend exposes REST endpoints for data logging, triggering analyses,
      and returning metrics and plots for visualization.
    </p>
  </div>

  <!-- Database -->
  <div class="topic inverse">
    <h2>Database design</h2>
    <p>
      The relational schema tracks users, allergens, symptoms, exposure events,
      symptom events, medications, check-ins, training sessions, and uploaded
      documents over time.
      All timestamps are stored in UTC, sensitive fields are encrypted at rest,
      and all health data is scoped per user.
    </p>
    <ul>
      <li><strong>Users:</strong> Account and authentication data</li>
      <li><strong>Allergens:</strong> User‑defined exposure categories</li>
      <li><strong>Units:</strong> Measurement units and conversions</li>
      <li><strong>Allergen logs:</strong> Timestamped exposure events</li>
      <li><strong>Symptoms:</strong> User‑defined symptom definitions with optional grouping</li>
      <li><strong>Symptom logs:</strong> Timestamped symptom events with severity</li>
      <li><strong>Medications:</strong> User‑defined medication names</li>
      <li><strong>Medication regimens:</strong> Dose, unit, and active date range per medication</li>
      <li><strong>Daily check-ins:</strong> Twice-daily structured wellbeing records (morning / evening)</li>
      <li><strong>Exercises:</strong> Per-user exercise library with equipment, target area, and form cues</li>
      <li><strong>Workout sessions:</strong> Dated training sessions with duration, RPE, and a morning-after soreness score</li>
      <li><strong>Set logs:</strong> Individual sets with reps, load, band, hold time, side, RPE, and pain</li>
      <li><strong>Training profile:</strong> Programme selection, goals, constraints, and owned equipment</li>
      <li><strong>Practice items:</strong> User-defined routines that bookend each session</li>
      <li><strong>User documents:</strong> Uploaded health documents with extracted text for AI context</li>
      <li><strong>Password reset tokens:</strong> Secure, expiring tokens for account recovery</li>
    </ul>
  </div>

  <!-- Daily Check-ins -->
  <div class="topic inverse">
    <h2>Daily check-ins & wellbeing tracking</h2>
    <p>
      Users complete structured morning and evening check-ins to build a continuous picture of
      their wellbeing alongside allergen and symptom data.
    </p>
    <ul>
      <li><strong>General variables:</strong> mood, sleep quality, fatigue, gut health, stress</li>
      <li><strong>Extended variables:</strong> headache, overnight headache, brain fog, tinnitus, visual disturbance, training intensity, illness status</li>
      <li>Check-in trends are visualized over time and can be cross-referenced with allergen and symptom events</li>
      <li>Medication and check-in data can both be included in the unified time series view</li>
    </ul>
  </div>

  <!-- Training -->
  <div class="topic inverse">
    <h2>Training programme</h2>
    <p>
      The training feature turns the same health record into a prescriptive strength programme.
      It decides what to train today, what load to use, and when to hold back — reading the
      symptoms and check-ins already logged elsewhere in the app.
    </p>
    <p>
      The progression rules are <strong>deterministic by design</strong>. A rule that reads the
      previous session's morning-after soreness score and refuses to add load is a guarantee;
      the same instruction written into a prompt is only a suggestion. The AI layer explains the
      plan and answers questions about it — it does not choose loads.
    </p>

    <h3>Programmes and phases</h3>
    <ul>
      <li>Selectable programmes, each with their own exercises, session themes, and baseline tests</li>
      <li>Three progressive phases per programme, from tolerance work through to heavier loading</li>
      <li>Advancement requires both time in the phase and quiet symptoms, so a good week cannot promote someone whose joints are complaining</li>
      <li>Rotating A/B/C session days, so every area is trained two or three times a week rather than once</li>
      <li>A submaximal baseline assessment sets starting loads, holds, and rep targets — no one-rep maxes</li>
      <li>User-defined practice routines bookend each session, separate from the programme itself</li>
    </ul>

    <h3>How a session is prescribed</h3>
    <ul>
      <li><strong>Double progression:</strong> reps or hold time build to the top of a range before load is added</li>
      <li><strong>Symptom-led back-off:</strong> load holds or drops when the morning-after score is high, and only for the body areas actually affected</li>
      <li><strong>Side-specific adjustment:</strong> on unilateral work only the sore side eases off, so the good side keeps training</li>
      <li><strong>Instability handling:</strong> standing single-leg work is dropped outright — not merely trimmed — when a joint is giving way</li>
      <li><strong>Stall detection:</strong> an exercise that fails the same target three sessions running is swapped for an easier version of the same movement</li>
      <li><strong>Equipment substitution:</strong> exercises are matched to the kit the user owns, and loads are rounded to weights that can actually be built from their plates</li>
      <li><strong>Session modes:</strong> a logged headache or fatigue suggests a reduced or gentle session — a shorter list rather than smaller numbers — which the user can override</li>
      <li><strong>Spacing:</strong> strength days are kept apart, with practice and maintenance work filling the days between</li>
    </ul>

    <h3>Logging and feedback</h3>
    <ul>
      <li>A guided session runner walks through each prescribed exercise in order</li>
      <li>Sets record reps, weight, band resistance, hold time, side, RPE, and pain</li>
      <li>Off-plan sets can be logged separately without disturbing the programme</li>
      <li>A morning-after soreness score is collected the day after each session, and is what decides whether load goes up</li>
      <li>Pre-session check-ins surface only the symptoms that change what the session may contain</li>
    </ul>

    <h3>Connection to the wider record</h3>
    <p>
      Training is not a separate app bolted on. Because it shares one database with the allergen,
      symptom, medication, and check-in logs, a symptom recorded in the morning reaches that
      afternoon's session, training intensity appears alongside every other check-in variable in
      the time series, and the AI chat can answer questions that cross the boundary — such as
      whether joint pain tracks training volume.
    </p>
  </div>

  <!-- Visualizations -->
  <div class="topic inverse">
    <h2>Visualizations</h2>
    <p>The dashboard renders a range of interactive and static plots generated by the backend:</p>
    <ul>
      <li>Allergen importance ranking</li>
      <li>Symptom grouping and EDA</li>
      <li>Time series for allergens, symptoms, check-in variables, and medications</li>
      <li>Symptom calendar heatmap</li>
      <li>Check-in trend plots</li>
      <li>Triptan usage and monthly analysis</li>
      <li>Headache likelihood forecast calendar</li>
      <li>Medication change before/after comparison</li>
      <li>Risk visualizations</li>
      <li>Dose–response analysis with event series overlays</li>
      <li>Model performance metrics page</li>
    </ul>
  </div>

  <!-- Limitations -->
  <div class="topic inverse">
    <h2>Limitations & caveats</h2>
    <ul>
      <li>Correlation does not imply causation</li>
      <li>Confounders (stress, sleep, illness) are not yet modeled</li>
      <li>Small sample sizes increase uncertainty</li>
      <li>Outputs are not intended for medical diagnosis</li>
    </ul>
  </div>

  <!-- Future Work -->
  <div class="topic inverse">
    <h2>Future development</h2>

	<p><strong>Planned Analysis Enhancements</strong></p>
	<ul>
	  <li>Identify and analyze recurring patterns in symptom occurrence</li>
	  <li>Enable analysis across user‑selected date ranges</li>
	  <li>Support logging of multiple allergens and symptoms within a single event</li>
	</ul>

	<p><strong>Data Management Improvements</strong></p>
	<ul>
	  <li>Introduce a dedicated Food table with automatic allergen assignment</li>
	  <li>Provide access to raw data for greater transparency and control</li>
	</ul>

	<p><strong>Reporting & Sharing</strong></p>
	<ul>
	  <li> Enable optional email delivery of generated reports</li>
	</ul>

	<p><strong>Architecture & Scalability</strong></p>
	<ul>
	  <li>Migrate to an alternative system architecture to support long‑term growth and scalability</li>
	</ul>

  </div>

  <!-- CTA -->
  <div class="topic inverse">
    <h2>Try the app</h2>
    <p>
      The Food–Body Connection app allows users to log foods and symptoms
      and receive personalised analytical reports.
    </p>
    <a href="https://alkohout.github.io/food_body_connection/"
       class="cta-button">
       Launch App
    </a>
  </div>

</div>
</section>
</main>

<footer>
  <p>&copy; {{ site.time | date: "%Y" }} {{ site.title }}</p>
</footer>

</body>
</html>
