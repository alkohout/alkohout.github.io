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
        <img src="/assets/images/background_iphone.png"
             alt="ICON">
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
      <li>Tracks twice-daily check-ins covering mood, sleep, fatigue, gut health, stress, and more</li>
      <li>Logs medications and active regimens with dose and date tracking</li>
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

    <h3>AI‑Powered Summary & Chat</h3>
    <ul>
      <li>Generates natural‑language health summaries using Claude (Anthropic API)</li>
      <li>Provides a conversational chat interface grounded in the user's own tracking data</li>
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
      FastAPI Backend (AWS) → PostgreSQL Database (NEON)
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
      symptom events, medications, check-ins, and uploaded documents over time.
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
	  <li>Add an editable data view allowing users to modify or delete logged entries</li>
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
