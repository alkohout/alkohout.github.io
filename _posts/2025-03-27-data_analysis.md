---
layout: post
title: "Data Anaylsis"
date: 2025-02-09
categories:
  - projects 
tags:
  - sea ice
  - waves
  - climate
  - antarctica
permalink: /projects/waves-in-ice/data_analysis/
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Analysis</title>
    <link rel="stylesheet" href="/assets/css/style.css"> 
    <!-- MathJax v3 -->
    <script>
    MathJax = {
        tex: {
            inlineMath: [['$', '$'], ['\$$', '\$$']],
            displayMath: [['$$', '$$'], ['\$$', '\$$']]
        }
    };
    </script>
    <script type="text/javascript" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>
    <!-- Site Visit Counter -->
    <script data-goatcounter="https://kohoutal.goatcounter.com/count"
       async src="//gc.zgo.at/count.js">
    </script>
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
          <h1>Wave decay</h1>
          <p>
	  The interaction between ocean waves and sea ice is a fundamental process that influences both the dynamics of the ice cover and the characteristics of the wave field. 
	  Understanding how waves decay as they propagate through sea ice is crucial for improving our ability to model and predict ice-ocean interactions, particularly in the marginal ice zone (MIZ) where wave-ice interactions are most pronounced. 
	  This understanding has become increasingly important as climate change leads to more frequent and intense wave events in polar regions, potentially accelerating ice break-up and affecting maritime operations. 
	  Traditional approaches to studying wave decay in sea ice have relied on linear wave theory, but recent observations suggest this may not fully capture the complexity of wave-ice interactions, particularly during large wave events.
          Analysis of wave decay in sea ice focuses on understanding the evolution of the full wave spectrum propagating through the ice. 
          Linear theory assumes that as a wave propagates through ice, the power at each wave number decays without transfer of energy between wave numbers. 
          This implies that the significant wave height, which is proportional to the square root of the total wave energy, will always decay exponentially with distance from the sea ice edge. 
          Our SIPEX data set confirms previous observations that, during calm conditions, the significant wave height decays exponentially with distance. 
          However, during three large wave events, we found that significant wave heights did not decay exponentially, enabling large waves to persist deep into the pack ice.
          <figure class="fig-left">
              <img src="/assets/images/wave_decay.png"
                   alt="Wave decay plots">
              <figcaption>Figure 1: Wave decay in the marginal ice zone during a calm wave event and a large wave event</figcaption>
          </figure>
          To demonstrate this, for our whole data record, we calculated the decay rate of the significant wave height between wave buoys, dHs/dx, where Hs is the significant wave height and x the distance between buoys. 
	  We present this data in the form of a boxplot, where we observe that the magnitude of dHs/dx increases almost perfectly linearly with Hs until Hs reaches 3 m, as we would expect for exponentially decaying waves as show in the calm plot in Figure 1. 
          <figure class="fig-left">
              <img src="/assets/images/wave_decay_boxplot.png"
                   alt="Wave decay plots">
              <figcaption>Figure 2: Wave decay in the marginal ice zone during a calm wave event and a large wave event</figcaption>
          </figure>
          For waves larger than 3 m, dHs/dx flattens and can be treated as being independent of Hs, as demonstrated in the large wave event plot in Figure 1. 
          This showed that existing linear theory appears to be only valid for waves with Hs < 3 m. 
          The empirical model derived from the data was 
          </p>
	  $$
	  \frac{dH_s}{dx} =
	  \begin{cases}
	  -5.35 \times 10^{-6}H_s, & H_s \le 3\,\mathrm{m} \\
	  -16.05 \times 10^{-6}, & H_s \ge 3\,\mathrm{m}
	  \end{cases}
	  $$
          <p>
          where $-5.35 \times 10^{-6}$ is the attenuation coefficient. 
          The constant attenuation for waves with significant wave height greater than 3 m implies a more gradual decay of wave height with propagation distance, allowing large waves to penetrate considerably farther into the ice. 
          Because the ice in the MIZ was all first-year ice, we are unable to determine how equation (1) will differ in thicker ice or in a combination of first-year and multi-year ice.
          The wave spectra during large wave events indicate that the spectral peak of the energy distribution may shift to longer periods with increasing distance from the ice edge. 
          This is standard for waves in the open ocean, where nonlinear interactions create an inverse energy cascade, moving energy and the spectral peak to longer periods.
          Thus, our observations suggest that nonlinear energy transfer may need
          to be considered when modelling the decay of large waves (Hs > 3 m) through sea ice and that small amplitude wave theory cannot simply be extrapolated to large amplitude waves.
          
          To improve our understanding of the wave attenuation processes found during SIPEXII, we conducted a much larger experiment during PIPERS.
          The large dataset is broken into long and short peak wave periods and high and low ice concentrations, showing that generally during this experiment, the total wave energy decayed exponentially through the ice with the rate of decay dependent on ice concentration. 
          These results suggest that the conclusion from the SIPEXII dataset, that large waves decay linearly, was an artefact of analysing a small dataset in different ice conditions. 
          For example, it is possible that during SIPEX-II, the large wave events predominantly occurred when low ice concentrations were present, thereby reducing the decay rates and leading to an appearance of linear wave decay. 
          </p>
        </div>
       </div>
    </section>
    </main>
    <footer>
        <p>&copy; {{ site.time | date: "%Y" }} {{ site.title }}</p>
    </footer>
</body>
</html>

