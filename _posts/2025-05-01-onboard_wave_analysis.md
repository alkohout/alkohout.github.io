---
layout: post
title: "WIIOS"
date: 2025-02-09
categories:
  - projects 
tags:
  - sea ice
  - waves
  - climate
  - antarctica
permalink: /projects/waves-in-ice/WIIOS/wave_analysis/
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Waves - in - ice</title>
    <link rel="stylesheet" href="/assets/css/style.css"> 
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
        <section class="topics">
            <div class="topic-list">
                <div class="topic inverse">
                    <h3>Implementation of Real-Time Spectral Analysis for Wave Motion Processing</h3>
                    <p>I developed a C-based signal processing system for analyzing wave motion data with the following key components:</p>
                    
                    <h5>Data Acquisition & Preprocessing: {% include github-link.html href="https://github.com/alkohout/waves-in-ice/blob/main/3.27/src/sc_misc.c" %}{% include github-link.html href="https://github.com/alkohout/waves-in-ice/blob/main/3.27/src/signal_conditioning.c" %}</h5>
                    <ul>
                        <li>Implemented 640-second burst sampling at 64Hz from IMU and Kistler accelerometer</li>
                        <li>Designed digital filtering system using:
                            <ul>
                                <li>Low-pass 2nd order Butterworth filter (0.5Hz cutoff)</li>
                                <li>Downsampling to 2Hz</li>
                                <li>High-pass filtering for displacement calculations</li>
                            </ul>
                        </li>
                    </ul>

                    <h5>Spectral Analysis Core:</h5>
                    <ul>
                        <li>Implemented Welch's method for power spectral density estimation:</li>
                        <li>256-second segments with 50% overlap</li>
                        <li>10% cosine windowing</li>
                        <li>Detrending algorithms for each segment</li>
                        <li>Spectral moment calculations</li>
                    </ul>

                    <h5>Automated Quality Control System: <a href="https://github.com/alkohout/waves-in-ice/blob/main/3.27/src/qc.c">(github)</a></h5>
                    <ul>
                        <li>Statistical validation tests</li>
                        <li>Spike detection algorithms</li>
                        <li>Consecutive data change monitoring</li>
                    </ul>

                    <h5>Real-time Processing:</h5>
                    <ul>
                        <li>Dual-core Edison processor</li>
                        <li>1GB RAM limitation</li>
                        <li>32GB SD storage management</li>
                    </ul>

                    <h5>Technical Skills Demonstrated:</h5>
                    <ul>
                        <li>Digital Signal Processing</li>
                        <li>Real-time embedded systems programming</li>
                        <li>Statistical analysis</li>
                        <li>Data validation algorithms</li>
                        <li>Sensor integration</li>
                        <li>Memory optimization</li>
                    </ul>

                    <p>This implementation showcases both advanced programming skills and mathematical expertise in spectral analysis and signal processing.</p>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; {{ site.time | date: "%Y" }} {{ site.title }}</p>
    </footer>
</body>
</html>
