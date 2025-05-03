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

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Waves in Ice - WIIOS</title>
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
                    <h2>Real-Time Spectral Analysis for Wave Motion Processing in Ice</h2>
                    <p>As part of the Waves in Ice Observation System (WIIOS) project, I developed a C-based signal processing system to analyze wave motion data in sea ice environments. This project was a unique challenge, as my formal programming training was limited to Fortran basics from my mathematics degree. I independently learned C to build this system from the ground up. Due to the constrained memory on the sensors, only essential libraries were included, requiring me to write all algorithms from scratch. As a result, the code deviates from conventional formatting standards. Please note that this software was initially developed for personal use and not intended for public sharing. I am currently working on refining the code with AI assistance to make it accessible in a polished, shareable format. Below, I outline the core components of the system, accompanied by relevant code snippets.</p>
                    
                    <h3>Data Acquisition & Preprocessing</h3>
                    <p>[GitHub Links: <a href="https://github.com/alkohout/waves-in-ice/blob/main/3.27/src/main.c">main.c</a>, <a href="https://github.com/alkohout/waves-in-ice/blob/main/3.27/src/sc_misc.c">sc_misc.c</a>, <a href="https://github.com/alkohout/waves-in-ice/blob/main/3.27/src/signal_conditioning.c">signal_conditioning.c</a>]</p>
                    <ul>
                        <li>Captured 640-second burst samples at 64 Hz using IMU and Kistler accelerometers.</li>
                        <li>Designed a digital filtering pipeline, including:
                            <ul>
                                <li>A low-pass 2nd-order Butterworth filter (0.5 Hz cutoff).</li>
                                <li>Downsampling to 2 Hz for efficient processing.</li>
                                <li>High-pass filtering to derive displacement data.</li>
                            </ul>
                        </li>
                    </ul>
                    <p><strong>Code Snippet: Downsampling Implementation</strong></p>
                    <div class="code">
                        {% highlight c %}
                        {% include decimate.c %}
                        {% endhighlight %}
                    </div>

                    <h3>Spectral Analysis</h3>
                    <p>[GitHub Links: <a href="https://github.com/alkohout/waves-in-ice/blob/main/3.27/src/process.c">process.c</a>, <a href="https://github.com/alkohout/waves-in-ice/blob/main/3.27/src/nr_four.c">nr_four.c</a>, <a href="https://github.com/alkohout/waves-in-ice/blob/main/3.27/src/direction.c">direction.c</a>]</p>
                    <ul>
                        <li>Applied Welch’s method for power spectral density estimation using:
                            <ul>
                                <li>256-second data segments with 50% overlap.</li>
                                <li>10% cosine windowing to reduce spectral leakage.</li>
                                <li>Detrending algorithms for each segment to remove noise.</li>
                                <li>Calculation of spectral moments for wave characterization.</li>
                            </ul>
                        </li>
                    </ul>

                    <h3>Automated Quality Control System</h3>
                    <p>[GitHub Link: <a href="https://github.com/alkohout/waves-in-ice/blob/main/3.27/src/qc.c">qc.c</a>]</p>
                    <ul>
                        <li>Developed validation mechanisms, including statistical tests.</li>
                        <li>Implemented spike detection to identify anomalies.</li>
                        <li>Monitored consecutive data changes to ensure consistency.</li>
                    </ul>

                    <h3>Real-Time Processing Constraints</h3>
                    <ul>
                        <li>Utilized a dual-core Edison processor for computations.</li>
                        <li>Managed operations within a 1 GB RAM limitation.</li>
                        <li>Optimized data storage on a 32 GB SD card.</li>
                    </ul>

                    <h3>Technical Skills Highlighted</h3>
                    <ul>
                        <li>Advanced digital signal processing techniques.</li>
                        <li>Real-time programming for embedded systems.</li>
                        <li>Statistical analysis and data validation methods.</li>
                        <li>Sensor integration and memory optimization.</li>
                    </ul>

                    <p>This project demonstrates a blend of advanced programming proficiency and deep mathematical understanding of spectral analysis and signal processing, tailored to the unique challenges of studying wave dynamics in Antarctic sea ice.</p>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; {{ site.time | date: "%Y" }} {{ site.title }}</p>
    </footer>
</body>
</html>
