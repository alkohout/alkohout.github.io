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
          <figure class="img-right" style="max-width: 30%">
              <img src="/assets/images/wave_decay.png"
                   alt="Wave decay plots">
              <figcaption>Figure 1: Wave decay in the marginal ice zone during a calm wave event and a large wave event. Each plot shows the significant wave heights as a function of distance from the ice edge from the WIIOS units (blue markers) and an exponential fit to the calm condition units and and linear fit to the large wave event (red line). </figcaption>
          </figure>
	  This understanding has become increasingly important as climate change leads to more frequent and intense wave events in polar regions, potentially accelerating ice break-up and affecting maritime operations. 
	  Traditional approaches to studying wave decay in sea ice have relied on linear wave theory, but recent observations suggest this may not fully capture the complexity of wave-ice interactions, particularly during large wave events.
          Analysis of wave decay in sea ice focuses on understanding the evolution of the full wave spectrum propagating through the ice. 
          Linear theory assumes that as a wave propagates through ice, the power at each wave number decays without transfer of energy between wave numbers. 
          This implies that the significant wave height, which is proportional to the square root of the total wave energy, will always decay exponentially with distance from the sea ice edge. 
          Our SIPEX data set confirms previous observations that, during calm conditions, the significant wave height decays exponentially with distance. 
          However, during three large wave events, we found that significant wave heights did not decay exponentially, enabling large waves to persist deep into the pack ice.
	  See Figure 1 for an example of these two cases.
          To demonstrate the consistency of this, for our whole data record, we calculated the decay rate of the significant wave height between wave buoys, dHs/dx, where Hs is the significant wave height and x the distance between buoys. 
	  We present this data in the form of a boxplot, where we observe that the magnitude of dHs/dx increases almost perfectly linearly with Hs until Hs reaches 3 m, as we would expect for exponentially decaying waves as show in the calm plot in Figure 1. 
          <figure class="img-left" style="max-width: 20%">
              <img src="/assets/images/wave_decay_boxplot.png"
                   alt="Wave decay plots">
              <figcaption>Figure 2: Decay rates of waves for given significant wave heights. 
		Data are binned in 1-m boxes. 
		The red dot is the median. 
		Box height shows the range within which 50% of the data lie. 
		The whiskers give the range of data, excluding outliers (blue markers) and single data points. 
	       </figcaption>
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
          <figure class="img-right" style="max-width: 30%">
              <img src="/assets/images/cascade.png"
                   alt="Wave decay plots">
              <figcaption>Figure 3: 
		The power spectral densities during a storm-generated wave event (a) and during calm seas (b). 
		For each event, the red dashed lines show the output of the unit closest to the ice edge and the yellow furthest from the ice edge.
		The shaded regions give the 90% confidence intervals
	      </figcaption>
          </figure>
          Thus, our observations suggest that nonlinear energy transfer may need
          to be considered when modelling the decay of large waves (Hs > 3 m) through sea ice and that small amplitude wave theory cannot simply be extrapolated to large amplitude waves.
          
          To verify these findings we conducted a much larger experiment during PIPERS.
	  We again studied the decay rates and display the data in boxplots. This time however, the larger dataset allowed us to break the data into long and short peak wave periods and high and low ice concentrations. 
	  This showed that generally during this experiment, the total wave energy decayed exponentially through the ice with the rate of decay dependent on ice concentration. 
          These results suggest that the conclusion from the SIPEX-II dataset, that large waves decay linearly, was likely an artefact of analysing a small dataset and comparing data experiencing differing ice conditions. 
          <figure class="img-left" style="max-width: 20%">
              <img src="/assets/images/kohout_etal_20.jpg"
                   alt="Wave decay plots">
              <figcaption>Figure 4: 
		Decay rates of WIIOS in ice concentrations <80% (blue squares) and WIIOS in ice concentrations >80% (green circles). 
		(a) Data from WIIOS with peak periods <14 s.
		(b) Data from WIIOS with peak periods >14 s. 
		Data are binned in 1 m boxes. 
		The markers are the median within each box. 
		The shaded boxes show the range within which 50% of the data lie. 
		The number of data points within each box is displayed above/below the box. 
		The black lines show the least-squares regression line of best fit to the median values within each box.
	      </figcaption>
          </figure>
          For example, it is possible that during SIPEX-II, the large wave events predominantly occurred when low ice concentrations were present, thereby reducing the decay rates and leading to an appearance of linear wave decay. 
	  </p>
	  <p>
          <figure class="img-right" style="max-width: 20%">
              <img src="/assets/images/Kohout_etal_2014.jpg"
                   alt="Trends in sea ice extent and significant wave heights">
              <figcaption>Figure 5: 
		A comparison between the trends in sea ice extent and significant wave height between 1997 and 2009. 
		The observed trend in the location of the ice edge (red) and the simulated trend in the significant wave height (blue) are shown as functions of longitude. 
		a, Averaged trends for the ice decay season (September to February). 
		b, The averaged trends during the ice growth season (March to August). 
		The Pearson coefficient (r) is given at the top right of each panel (n = 288 for each). 
		Antarctica is represented by the grey shaded region. 
		We note that the scale for trend in Hs increases downwards.
	      </figcaption>
          </figure>
          <p>
	  Building on our experimental findings, we investigate the broader implications of wave breakup on sea ice extent. 
	  We propose that increasing significant wave heights in the Southern Ocean enhance sea ice breakup, leading to a retreat of the sea-ice edge. 
	  Conversely, decreasing wave heights would likely cause the ice edge to expand.
	  To test this relationship, we analyzed model-derived significant wave height estimates alongside satellite sea-ice observations from 1997-2009, defining the sea-ice edge at 15% ice concentration. 
	  We divided the data into biannual seasons: growth (March-August) and decay (September-February) as shown in Figure 5.
	  Both seasonal analyses revealed that trends in sea-ice extent inversely correlate with significant wave height trends, with Pearson correlation coefficients of -0.70 during decay season and -0.79 during growth season. 
	  Our analysis indicates that a 2-meter increase in significant wave height over a decade corresponds to a 2° latitudinal retreat in ice extent (Extended Data Fig. 4).
	  Geographically, the most substantial wave height increases occurred in the Amundsen–Bellingshausen Sea, coinciding with documented sea-ice retreat, while the Western Ross Sea experienced the largest decreases in wave height, aligning with known ice expansion. 
	  These 1997-2009 trends in wave height are consistent with observed longer-term patterns. 
	  Our findings suggest sea ice vulnerability to changing storm patterns. 
	  Recent decades have witnessed a southward shift in storm tracks, decreasing mid-latitude cyclones while increasing high-latitude cyclones. 
	  This shift has not been uniformly zonal; recent trends in surface pressure and winds show zonally asymmetric changes, creating variability in atmospheric forcing on sea ice.
	  Future projections indicate increasing wave heights throughout Arctic and Antarctic sea-ice edges, potentially accelerating sea-ice retreat.
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

