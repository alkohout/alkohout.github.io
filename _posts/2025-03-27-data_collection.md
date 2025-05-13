---
layout: post
title: "Data Collection"
date: 2025-02-09
categories:
  - projects 
tags:
  - sea ice
  - waves
  - climate
  - antarctica
permalink: /projects/waves-in-ice/data_collection/
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Waves - in - ice</title>
    <link rel="stylesheet" href="/assets/css/style.css"> 
    <!-- Load Leaflet CSS -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />

    <style>
      /* Map container styling */
      #map {
        height: 600px;
        width: 100%;
        margin: 1em 0;
      }
      .download-link {
        display: inline-block;
        margin-top: 5px;
        padding: 4px 8px;
        background-color: #007bff;
        color: white;
        border-radius: 4px;
        text-decoration: none;
      }
    </style>

</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="https://alkohout.github.io">Alison Kohout</a></li>
                <li><a href="https://alkohout.github.io/projects/waves-in-ice/">Home</a></li>
                <li><a href="https://alkohout.github.io/projects/waves-in-ice/WIIOS/">Sensor Design</a></li>
                <li><a href="https://alkohout.github.io/projects/waves-in-ice/data_collection/">Data Collection</a></li>
                <li><a href="https://alkohout.github.io/projects/waves-in-ice/data_analysis/">Data Analysis</a></li>
                <li><a href="https://alkohout.github.io/projects/waves-in-ice/publications/">Publications</a></li>
            </ul>
        </nav>
    </header>

    <main>
    <section id="home" class="topics">
       <div class="topic-list">
        <div class="topic inverse">
	<div id="map"></div>

        </div>
       </div>
    </section>
    <section id="home" class="topics">
       <div class="topic-list">
        <div class="topic inverse">
          <h1>Data collection</h1>
        </div>
       </div>
    </section>
    </main>
    <footer>
        <p>&copy; {{ site.time | date: "%Y" }} {{ site.title }}</p>
    </footer>
    <!-- Leaflet JS -->
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script>
      // Initialize the map
      var map = L.map('map').setView([-70, 160], 4);

      // Add OpenStreetMap tiles
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
      }).addTo(map);

      // Buoy data from Jekyll data file
      var buoys = {{ site.data.wave_ice_buoy_info | jsonify }};

      // Function to load and parse CSV data
      function loadCSV(url) {
        return fetch(url)
          .then(response => response.text())
          .then(data => {
            const lines = data.trim().split('\n');
            const headers = lines[0].split(',').map(header => header.trim().toLowerCase()); // Normalize headers to lowercase
            const latIndex = headers.indexOf('latitude (decimal degrees)'); // Adjust header name as needed
            const lngIndex = headers.indexOf('longitude (decimal degrees)'); // Adjust header name as needed
    
            if (latIndex === -1 || lngIndex === -1) {
              throw new Error('CSV does not contain the expected "latitude" or "longitude" columns');
            }
    
            return lines.slice(1).map(line => {
              const values = line.split(',');
              return {
                lat: parseFloat(values[latIndex]),
                lng: parseFloat(values[lngIndex])
              };
            });
          });
      }
    
      // Add markers and paths for each buoy
      buoys.forEach(function(buoy) {
        var positions;
        loadCSV(buoy.positions_url)
          .then(data => {
            positions = data;
    
            // Create and show polyline for the buoy's path
            var path = L.polyline(positions, {
              color: 'blue',
              weight: 2,
              opacity: 0.7,
              smoothFactor: 1
            }).addTo(map);
    
            // Create and add marker for the buoy
            var marker = L.marker([positions[0].lat, positions[0].lng]).addTo(map);
            marker.bindPopup(`<strong>Buoy ID:</strong> ${buoy.id}`);
          })
          .catch(error => console.error('Error loading positions:', error));
      });
    </script>

</body>

</html>

