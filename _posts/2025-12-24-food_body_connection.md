---
layout: post
title: "Food–Body Connection"
date: 2025-12-24
categories:
  - projects 
tags:
  - AWS RDS 
  - SQL
  - Machine Learning
  - FastAPI
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
    <figure class="img-centre" style="max-width: 30%">
        <img src="/assets/images/background_iphone.png"
             alt="ICON">
    </figure>
    <h1>Food–Body Connection</h1>
    <p>
      Food–Body Connection is a full‑stack health analytics application designed to help users
      identify potential food or environmental allergens associated with adverse symptoms.
      Users log exposures and symptoms over time, and the system applies statistical analysis
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
      <li>Stores structured health data in a relational PostgreSQL database</li>
      <li>Aligns exposure and symptom events using time‑aware windows</li>
      <li>Analyzes relationships between allergens and symptoms</li>
      <li>Generates personalized reports highlighting potential trigger foods</li>
      <li>Supports elimination diets and long‑term tracking strategies</li>
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
      <li><strong>Database:</strong> PostgreSQL on AWS RDS</li>
      <li><strong>ORM:</strong> SQLAlchemy</li>
      <li><strong>Authentication:</strong> JWT‑based authentication</li>
      <li><strong>Analysis:</strong> Statistical modeling and supervised machine learning</li>
      <li><strong>Frontend:</strong> Static site hosted on <a href="https://github.com/alkohout/food_body_connection" target="_blank" rel="noopener noreferrer">GitHub Pages</a></li>
    </ul>
  </div>

  <!-- Architecture -->
  <div class="topic inverse">
    <h2>System architecture</h2>
    <p>
      Static Frontend (<a href="https://github.com/alkohout/food_body_connection" target="_blank" rel="noopener noreferrer">GitHub Pages</a>) → HTTPS (JWT‑authenticated API calls) →
      FastAPI Backend (AWS) → PostgreSQL Database (AWS RDS)
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
      and symptom events over time. All timestamps are stored in UTC, and
      allergens and symptoms are scoped per user.
    </p>
    <ul>
      <li><strong>Users:</strong> Account and authentication data</li>
      <li><strong>Allergens:</strong> User‑defined exposure categories</li>
      <li><strong>Units:</strong> Measurement units and conversions</li>
      <li><strong>Allergen logs:</strong> Timestamped exposure events</li>
      <li><strong>Symptoms:</strong> User‑defined symptom definitions</li>
      <li><strong>Symptom logs:</strong> Timestamped symptom events with severity</li>
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
    <figure class="img-right" style="max-width: 10%">
        <img src="/assets/images/QR.png"
             alt="QR code">
    </figure>
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
