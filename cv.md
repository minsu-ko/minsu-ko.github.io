---
layout: cv
title: CV
---

<!--
  - 아래 헤딩(##)의 {#anchor} id 는 왼쪽 사이드바 링크와 연결됩니다.
  - Publications / Presentations / Honors / Teachings 는 _data/*.yml 파일만 고치면 됩니다.
-->

## Basics {#basics}

<div class="basics-grid">
  <div class="basic-row">
    <span class="basic-label">Name</span>
    <span class="basic-value">MinSu Ko (고민수)</span>
  </div>
  <div class="basic-row">
    <span class="basic-label">Position</span>
    <span class="basic-value">Student, Master-Doctoral Program</span>
  </div>
  <div class="basic-row">
    <span class="basic-label">Affiliation</span>
    <span class="basic-value">Dept. of Physics, Korea Advanced Institute of Sci. and Tech.</span>
  </div>
  <div class="basic-row">
    <span class="basic-label">Email</span>
    <span class="basic-value"><a href="mailto:komin0310@kaist.ac.kr">komin0310@kaist.ac.kr</a></span>
  </div>
  <div class="basic-row">
    <span class="basic-label">Working On</span>
    <span class="basic-value">Development of a 12–20 GHz radio astronomical receiver for high z CO line-intensity mapping</span>
  </div>
</div>

## Education {#education}

<div class="education-item">
  <div class="education-header">
    <span class="degree">Ph.D. in Physics (expected Feb, 2031) </span>
    <span class="edu-date">Feb, 2025 – Present</span>
  </div>
  <div class="edu-institution">Korea Advanced Institute of Sci. and Tech. (KAIST), Department of Physics</div>
  <div class="thesis-title">Project: “Development of 12-20 GHz receiver for CO line-intensity mapping on z=4.8-8.6” (Advisor: Junhan Kim)</div>
</div>

<div class="education-item">
  <div class="education-header">
    <span class="degree">B.S. in Physics</span>
    <span class="edu-date">Mar, 2020 – Feb, 2025</span>
  </div>
  <div class="edu-institution">Korea Advanced Institute of Sci. and Tech. (KAIST), Department of Physics</div>
  <div class="edu-details">
    • Advanced Major in Physics, Individually Designed Major (Electrical engineering, Nuclear engineering)
  </div>
  <div class="thesis-title">Thesis: “Characterization of Josephson Parametric Amplifiers for Wideband Axion Search at CAPP” (Advisor: Yannis K. Semertzidis)</div>
</div>

## Employment & Experience {#employment}

<div class="employment-item grid">
  <!-- 왼쪽 정보 칸 -->
  <div class="employment-info">
    <div class="job-title">Ph.D. candidate</div>
    <div class="job-institution">
      Observational Cosmology and Astrophysics Lab. (ObsCAL), KAIST
    </div>
    <div class="edu-details">
      • Cross-correlation analysis of line-intensity mapping data.
    </div>
    <div class="edu-details">
      • Corrugated feed & waveguide components optimization.
    </div>
  </div>

  <!-- 오른쪽 메타 칸 -->
  <div class="employment-meta">
    <div class="job-date">Feb, 2025 – Present</div>
    <div class="job-location">Daejeon, South Korea</div>
  </div>
</div>

<div class="employment-item grid">
  <div class="employment-info">
    <div class="job-title">Student Assistant</div>
    <div class="job-institution">
      Center for Axion and Precision Physics Research, Institute for Basic Science (IBS/CAPP)
    </div>
    <div class="edu-details">
      • Experimental verification of Josephson parametric amplifiers.
    </div>
    <div class="edu-details">
      • Dry dilution fridge, cryocooler operation & maintenance.
    </div>
  </div>
  
  <div class="employment-meta">
    <div class="job-date">Jan, 2023 – Dec, 2024</div>
    <div class="job-location">Daejeon, South Korea</div>
  </div>
</div>

## Publications {#publications}

{% include cv-publications.html %}

## Presentations {#presentations}

{% include cv-presentations.html type="oral" %}

{% include cv-presentations.html type="poster" %}

## Honors {#honors}

{% include cv-simple-list.html items=site.data.honors %}

## Teachings {#teachings}

{% include cv-simple-list.html items=site.data.teachings %}
