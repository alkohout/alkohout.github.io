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
    // Initialize the map centered around East Antarctica / Scott Base region
    var map = L.map('map').setView([-70, 160], 4);
    
    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);
    
    // Variable to store the current path layer
    var currentPath = null;
    var trackDataCache = {};  // Cache for storing loaded track data
    var globalBounds = null;  // Variable to store the overall bounds
    
    // Function to load and parse CSV data for a specific buoy
    async function loadTrackingData(buoyId) {
      try {
        const filename = `/assets/data/${buoyId}_data.csv`;
        const response = await fetch(filename);
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.text();
        const rows = data.split('\n').slice(1); // Skip header row
        const coordinates = rows.map(row => {
          const columns = row.split(',');
          return [parseFloat(columns[1]), parseFloat(columns[2])]; // Lat, Lon from columns 2 and 3
        }).filter(coord => !isNaN(coord[0]) && !isNaN(coord[1])); // Filter out any invalid coordinates
        
        return coordinates;
      } catch (error) {
        console.error(`Error loading tracking data for buoy ${buoyId}:`, error);
        return [];
      }
    }
    
    // Function to calculate global bounds
    async function calculateGlobalBounds(buoys) {
      let allCoordinates = [];
      
      // Load all tracks
      for (const buoy of buoys) {
        const trackData = await loadTrackingData(buoy.id);
        trackDataCache[buoy.id] = trackData;  // Cache the data
        allCoordinates = allCoordinates.concat(trackData);
      }
      
      if (allCoordinates.length === 0) return null;
      
      // Calculate bounds
      const bounds = L.latLngBounds(allCoordinates);
      return bounds;
    }
    
    // Buoy data from Jekyll data file
    var buoys = {{ site.data.wave_ice_buoy_info | jsonify }};
    
    // Initialize bounds and markers
    (async function initializeMap() {
      // Calculate global bounds first
      globalBounds = await calculateGlobalBounds(buoys);
      
      if (globalBounds) {
        // Set initial map view to show all tracks with padding
        map.fitBounds(globalBounds, {
          padding: [50, 50],
          maxZoom: 10
        });
      }
      
      // Add markers for each buoy
      buoys.forEach(function(buoy) {
        var marker = L.marker([buoy.lat, buoy.lng]).addTo(map);
    
        // Format deployment date/time nicely
        var deploymentDate = new Date(buoy.deployed);
        var deploymentStr = deploymentDate.toLocaleString(undefined, {
          year: 'numeric', month: 'short', day: 'numeric',
          hour: '2-digit', minute: '2-digit', timeZoneName: 'short'
        });
    
        // Popup content
        var popupContent = `
          <strong>Buoy ID:</strong> ${buoy.id}<br/>
          <strong>Voyage:</strong> ${buoy.voyage}<br/>
          <strong>Deployed:</strong> ${deploymentStr}<br/>
          <a href="${buoy.raw_data_url}" class="download-link" download>Download Raw Data</a>
          <a href="${buoy.plot_url}" class="download-link" download>Download Time Series plot</a>
        `;
    
        marker.bindPopup(popupContent);
    
        // Add mouseover and mouseout events for tracking visualization
        marker.on('mouseover', function(e) {
          const trackingData = trackDataCache[buoy.id];
          if (trackingData && trackingData.length > 0) {
            // Remove existing path if any
            if (currentPath) {
              map.removeLayer(currentPath);
            }
            // Create and add new path
            currentPath = L.polyline(trackingData, {
              color: 'red',
              weight: 3,
              opacity: 0.7
            }).addTo(map);
          }
        });
    
        marker.on('mouseout', function(e) {
          if (currentPath) {
            map.removeLayer(currentPath);
            currentPath = null;
          }
        });
    
        // Show tooltip on hover with basic info
        // marker.bindTooltip(`ID: ${buoy.id}<br>Voyage: ${buoy.voyage}<br>Deployed: ${deploymentStr}`, {sticky: true});
      });
    })();
    </script>

</body>

</html>

