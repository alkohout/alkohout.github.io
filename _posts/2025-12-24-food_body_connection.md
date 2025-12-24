---
layout: post
title: "Food Data Connection"
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
    <title>Food Data Connection</title>
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
          <span class="project-title">Food Body Connection</span>
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
        <div class="topic inverse">
	<h1>Food–Body Connection</h1>
	<p>
	I developed a full-stack health analytics application that allows users to log foods they eat and symptoms they experience. 
	The system stores the data in a relational database, performs analytical processing to identify potential trigger relationships, 
	and generates a personalized report highlighting patterns between diet and symptoms.
</p>
        </div>
	<div class="topic inverse">
	  <h2>What the app does</h2>
	  <ul>
	    <li>Allows users to log foods, quantities, and timestamps</li>
	    <li>Allows users to log symptoms and symptom intensity over time</li>
	    <li>Stores structured health data in a PostgreSQL database (AWS RDS)</li>
	    <li>Analyzes relationships between foods and symptoms</li>
	    <li>Generates a personalized report highlighting potential trigger foods</li>
	  </ul>
	</div>
	<div class="topic inverse">
	  <h2>Technology stack</h2>
	  <ul>
	    <li><strong>Backend:</strong> FastAPI (Python)</li>
	    <li><strong>Database:</strong> PostgreSQL on AWS RDS</li>
	    <li><strong>ORM:</strong> SQLAlchemy</li>
	    <li><strong>Authentication:</strong> JWT-based user authentication</li>
	    <li><strong>Analysis:</strong> Statistical analysis & machine learning techniques</li>
	    <li><strong>Frontend:</strong> Static frontend hosted on GitHub Pages</li>
	  </ul>
	</div>

	<div class="topic inverse">
	  <h2>Why this project matters</h2>
	  <p>
	  Food-related symptom triggers are often difficult to identify due to delayed effects, overlapping foods, 
	  and noisy real-world data. This project explores how structured data collection and analysis can help 
	  surface meaningful patterns that are not obvious through manual tracking alone.
	  </p>
	</div>

	<div class="topic inverse">
	  <h2>Future development</h2>
	  <ul>
	    <li>Improved statistical modeling of delayed symptom onset</li>
	    <li>Visualization of symptom and food timelines</li>
	    <li>Personalized model tuning per user</li>
	    <li>Expanded food categorization and allergen grouping</li>
	  </ul>
	</div>
	<div class="topic inverse">
	  <h2>Try the app</h2>
	  <p>
	    The Food–Body Connection app allows users to log foods and symptoms and receive personalized analytical reports.
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


