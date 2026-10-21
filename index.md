---
layout: default
title: ""
body_class: home
---
<section class="hero">
  <div class="hero-photo" style="--hero-image: url('{{ '/assets/gallery/2025_ovro_milkyway_re.jpg' | relative_url }}');" role="img" aria-label="Radio dishes under the Milky Way at Owens Valley Radio Observatory"></div>

  <div class="hero-content">
    <p class="hero-eyebrow"><span class="accent">Physics</span>, KAIST <span class="sep">/</span> Daejeon, Korea</p>
    <h1 class="hero-name">MinSu Ko</h1>
    <p class="hero-korean">고민수</p>

    <p class="hero-lead">
      I build instruments for <span class="accent">observational cosmology</span> and <span class="accent">particle physics</span>:
      radio receivers for CO line-intensity mapping and quantum-noise-limited amplifiers for axion searches.
    </p>

    <p class="hero-status"><span class="status-dot" aria-hidden="true"></span>Master–Doctoral Integrated Program (2nd year), ObsCAL, KAIST</p>

    <div class="hero-actions">
      <a class="btn btn-solid" href="mailto:komin0310@kaist.ac.kr">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1Zm9 7.2L4.2 7H4v.6l8 5.3 8-5.3V7h-.2L12 12.2Z" fill="currentColor"/></svg>
        komin0310@kaist.ac.kr
      </a>
      <a class="btn btn-ghost" href="{{ '/cv.html' | relative_url }}">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h8l6 6v13a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1Zm7 1.5V9h5.5L13 3.5ZM8 13v1.5h8V13H8Zm0 3.5V18h8v-1.5H8Z" fill="currentColor"/></svg>
        Curriculum vitae
      </a>
      <div class="hero-social">
        <a class="scholar" href="https://scholar.google.com/citations?user=H4vZJ-QAAAAJ&hl=ko" target="_blank" rel="noopener noreferrer">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 3 1 9l11 6 9-4.9V17h2V9L12 3Zm-7 10.2v4.3C5 19.4 8.1 21 12 21s7-1.6 7-3.5v-4.3l-7 3.8-7-3.8Z"/></svg>
          Google Scholar
        </a>
        <a class="researchgate" href="https://www.researchgate.net/profile/Minsu-Ko-3?ev=hdr_xprf" target="_blank" rel="noopener noreferrer">
          <svg viewBox="0 0 24 24" aria-hidden="true"><rect width="24" height="24" rx="5" fill="currentColor"/><text x="3.6" y="17.5" font-family="Georgia, 'Times New Roman', serif" font-size="14" fill="#0e1219">R</text><text x="13.2" y="11" font-family="Georgia, 'Times New Roman', serif" font-size="8.5" fill="#0e1219">G</text></svg>
          ResearchGate
        </a>
      </div>
    </div>
  </div>

  <p class="hero-credit">Owens Valley Radio Observatory, 2025</p>
</section>

<section class="home-section">
  <div class="home-inner">
    <p class="section-eyebrow">Current projects</p>
    <div class="project-grid">
      <article class="project-card">
        <span class="project-index">01</span>
        <p class="project-tag">COMAP-EoR</p>
        <h3>12–20 GHz receiver for CO line-intensity mapping</h3>
        <p>Developing a Ku-band receiver targeting carbon monoxide emission at <em>z</em> &gt; 4.8, toward mapping the Epoch of Reionization.</p>
      </article>
      <article class="project-card">
        <span class="project-index">02</span>
        <p class="project-tag">Axion haloscope</p>
        <h3>Wideband quantum-noise-limited readout</h3>
        <p>Readout chains based on Josephson parametric amplifiers that widen the scan range of axion dark-matter searches.</p>
      </article>
    </div>

    <p class="section-eyebrow">Interests</p>
    <ul class="interest-chips">
      <li>Experimental cosmology &amp; faint-signal astronomy</li>
      <li>Beyond Standard Model experiments</li>
      <li>Radio astronomy instrumentation</li>
      <li>Superconducting quantum-limited amplifiers</li>
    </ul>
  </div>
</section>

<script>
  // 스크롤하면 상단 배너에 배경이 생기도록
  (function () {
    var header = document.querySelector('header');
    var update = function () { header.classList.toggle('scrolled', window.scrollY > 24); };
    window.addEventListener('scroll', update, { passive: true });
    update();
  })();
</script>
