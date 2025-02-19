---
layout: post
title: "Waves - in - Ice"
date: 2025-02-09
categories:
  - coding
tags:
  - sea ice
  - waves
  - climate
  - antarctica
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Waves - in - ice</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
        }
        .waves-post {
            background-image: url('/assets/images/background.jpg');
            background-size: cover;
            background-attachment: scroll;
            background-repeat: no-repeat;
	    /*
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
	    */
            min-height: 100vh; /* Ensures background covers full viewport */
            background-position: bottom center;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: left;
            color: #333; /* Text color for contrast */
        }
        .waves-content {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
            max-width: 800px;
            margin: 40px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        h1, h2, h3 {
            color: #005f99;
        }
        a {
            color: #0066cc;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

<div class="waves-post">
    <div class="waves-content">
        <h1>Buoy development</h1>
	<p> We developed wave-in-ice sensors from the ground up, addressing the lack of available off-the-shelf solutions. This innovative concept emerged from extensive discussions with Martin Doble, whose expertise was invaluable in supporting hull design and wave data analysis. P.A.S. crafted the hardware, software, and live GUI, while I engineered the onboard wave analysis, ensuring precise and reliable data collection. [Reference] [GitHub Link]. 
        <a href="https://github.com/alkohout/waves-in-ice.git" target="_blank" class="btn">View Code on GitHub</a>
    </div>
</div>

</body>
</html>
