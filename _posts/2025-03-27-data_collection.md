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
// Modified script section with debugging
<script>
    // Debug: Log initial setup
    console.log("Starting map initialization...");

    // Initialize the map
    var map = L.map('map').setView([-70, 160], 4);
    console.log("Map initialized");

    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);
    console.log("Base map tiles added");

    // Debug: Log buoys data
    var buoys = {{ site.data.wave_ice_buoy_info | jsonify }};
    console.log("Buoys data:", buoys);

    // Modified loadCSV function with error handling
    async function loadCSV(url) {
        console.log("Attempting to load CSV from:", url);
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.text();
            console.log("CSV data received:", data.substring(0, 200) + "..."); // Show first 200 chars

            const lines = data.trim().split('\n');
            const headers = lines[0].split(',').map(h => h.trim().toLowerCase());
            console.log("CSV headers:", headers);

            const latIndex = headers.indexOf('latitude (decimal degrees)');
            const lngIndex = headers.indexOf('longitude (decimal degrees)');

            console.log("Column indices - Lat:", latIndex, "Lng:", lngIndex);

            if (latIndex === -1 || lngIndex === -1) {
                throw new Error('CSV missing required columns');
            }

            const positions = lines.slice(1).map(line => {
                const values = line.split(',');
                return {
                    lat: parseFloat(values[latIndex]),
                    lng: parseFloat(values[lngIndex])
                };
            });

            console.log("Parsed positions:", positions.slice(0, 3)); // Show first 3 positions
            return positions;
        } catch (error) {
            console.error("Error loading CSV:", error);
            throw error;
        }
    }

    // Modified buoy processing with better error handling
    buoys.forEach(async function(buoy) {
        console.log("Processing buoy:", buoy.id);
        try {
            const positions = await loadCSV(buoy.plot_url);
            
            if (!positions || positions.length === 0) {
                console.warn("No positions found for buoy:", buoy.id);
                return;
            }

            console.log(`Creating path for buoy ${buoy.id} with ${positions.length} positions`);

            // Create path
            const path = L.polyline(positions, {
                color: 'blue',
                weight: 2,
                opacity: 0.7
            }).addTo(map);

            // Create marker
            const marker = L.marker([positions[0].lat, positions[0].lng])
                .addTo(map)
                .bindPopup(`<strong>Buoy:</strong> ${buoy.id}`);

            // Add hover events
            marker.on('mouseover', function() {
                console.log(`Hover started on buoy ${buoy.id}`);
                let tooltipContent = `<strong>Buoy ID: ${buoy.id}</strong><br/>Positions:<br/>`;
                positions.slice(0, 5).forEach((pos, idx) => {
                    tooltipContent += `${idx}: (${pos.lat.toFixed(2)}, ${pos.lng.toFixed(2)})<br/>`;
                });
                marker.bindTooltip(tooltipContent).openTooltip();
                path.setStyle({color: 'red', weight: 3});
            });

            marker.on('mouseout', function() {
                console.log(`Hover ended on buoy ${buoy.id}`);
                path.setStyle({color: 'blue', weight: 2});
                marker.closeTooltip();
            });

        } catch (error) {
            console.error(`Error processing buoy ${buoy.id}:`, error);
        }
    });
</script>

</body>

</html>

