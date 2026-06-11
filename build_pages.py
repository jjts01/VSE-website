#!/usr/bin/env python3
"""Generates the static pages with shared chrome. Run: python3 build_pages.py"""
import html

SWIRL = '''<div class="swirl" aria-hidden="true"><svg viewBox="0 0 1000 1000" fill="none">
<g class="ring1" stroke="rgba(255,255,255,.13)" stroke-linecap="round">
<circle cx="500" cy="500" r="470" stroke-width="10" stroke-dasharray="640 260 90 320 420 1223"/>
<circle cx="500" cy="500" r="420" stroke-width="22" stroke-dasharray="380 420 700 1139" transform="rotate(70 500 500)"/>
<circle cx="500" cy="500" r="365" stroke-width="6" stroke-dasharray="14 26 14 26 14 26 760 1413" transform="rotate(160 500 500)"/>
</g>
<g class="ring2" stroke="rgba(106,151,153,.30)" stroke-linecap="round">
<circle cx="500" cy="500" r="305" stroke-width="16" stroke-dasharray="420 330 560 607" transform="rotate(-40 500 500)"/>
<circle cx="500" cy="500" r="245" stroke-width="8" stroke-dasharray="10 22 10 22 10 22 480 963" transform="rotate(120 500 500)"/>
<circle cx="500" cy="500" r="185" stroke-width="26" stroke-dasharray="300 240 380 242" transform="rotate(20 500 500)"/>
</g></svg></div>'''

NAV_ITEMS = [("services.html","Services"),("studios.html","Studios"),("work.html","Work"),("about.html","About"),("contact.html","Contact")]

def page(slug, title, desc, hero_kicker, hero_h1, hero_lede, body):
    cur = ' aria-current="page"'
    nav = "\n".join(f'    <li><a href="{h}"{cur if h==slug else ""}>{t}</a></li>' for h,t in NAV_ITEMS)
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#212b54">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="icon" type="image/png" href="assets/img/icon-white.png">
<link rel="canonical" href="https://www.virtualstudio.events/{'' if slug=='index.html' else slug}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="https://www.virtualstudio.events/assets/img/hero-manchester.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/main.css">
</head>
<body>
<div id="loader"><img src="assets/img/logo-stacked-white.png" alt=""><div class="pct">0%</div></div>
<div id="progress"></div>
<nav id="nav">
  <a class="logo" href="index.html"><img src="assets/img/logo-long-white.png" alt="Virtual Studio Events"></a>
  <ul>
{nav}
  </ul>
  <a class="cta-btn" href="contact.html">Start a project</a>
</nav>
<header class="page-hero" id="top">
  {SWIRL}
  <div class="wrap">
    <span class="kicker"><span class="live-dot"></span> {hero_kicker}</span>
    <h1>{hero_h1}</h1>
    <p class="lede">{hero_lede}</p>
  </div>
</header>
{body}
<section class="contact" id="contact">
  <div class="wrap reveal">
    <span class="eyebrow">Let's get started</span>
    <h2>Bring us the show <span class="em">you can't afford to drop.</span></h2>
    <p>A date and an ambition is plenty. We'll engineer the rest — from "can we?" to "standby… go."</p>
    <div class="contact-links">
      <a class="cta-btn" href="mailto:enquiries@virtualstudio.events">Email the studio</a>
      <a class="ghost-btn" href="tel:+442035986555">+44 020 359 86555</a>
      <a class="ghost-btn" href="https://wa.me/message/BOOOL7EHUXW4O1">WhatsApp ↗</a>
    </div>
  </div>
</section>
<footer>
  <img src="assets/img/logo-stacked-white.png" alt="VSE">
  <span>Live, hybrid &amp; broadcast event production · United Kingdom</span>
  <span>© 2026 Virtual Studio Events Limited · Studio partner: <a href="https://granary.digital/">Granary Digital</a></span>
</footer>
<script src="assets/js/main.js"></script>
</body>
</html>'''

P = {}

P['services.html'] = page('services.html',
 'Services — Virtual Studio Events','Senior crew, streaming engineering, production management, editing, hybrid events and podcast production for live events.',
 'What we do','One crew, <span class="em">the whole show.</span>',
 'From a single remote vMix operator to full technical delivery of a multi-day conference — scale us up or down to fit the show.',
 '''<section class="content-sec"><div class="wrap reveal"><div class="detail-list">
<article class="detail"><span class="num">01 — Crew &amp; engineering</span><h3>Senior, show-hardened crew. White-label welcome.</h3>
<p>Video engineers, vision mixers, playback and graphics operators who've sat in every kind of gallery. Most of our work is for other production companies — we wear your lanyard, look after your client and make your show look effortless.</p>
<ul><li>Video engineering &amp; vision mixing</li><li>Playback, graphics &amp; screens</li><li>Show-day operators and prep days</li></ul></article>
<article class="detail"><span class="num">02 — Streaming &amp; vMix</span><h3>On site or fully remote, every frame delivered.</h3>
<p>vMix systems, encoders and multi-destination streaming, run by engineers who built the workflow. We design and operate cloud production galleries on AWS — remote machines, low-latency routing and bulletproof redundancy.</p>
<ul><li>Remote vMix operation &amp; cloud galleries</li><li>Multi-destination encoding &amp; delivery</li><li>Teams / Zoom / Meet integration</li></ul></article>
<article class="detail"><span class="num">03 — Production management</span><h3>A Video HOD who owns the technical side.</h3>
<p>Pre-production, specs, supplier wrangling and a calm voice on comms. Our production managers and heads of department carry the technical risk of your show so you can stay with the creative.</p>
<ul><li>Video HOD &amp; technical direction</li><li>Pre-production &amp; system design</li><li>Production management day rates</li></ul></article>
<article class="detail"><span class="num">04 — Editing &amp; post</span><h3>Fast post, from the people who shot it.</h3>
<p>Show opens, sizzle reels, highlight edits and same-day session turnarounds. Because we were in the gallery, the edit starts before the show ends.</p>
<ul><li>Highlights &amp; sizzle reels</li><li>Session edits &amp; speaker cutdowns</li><li>Graphics &amp; motion</li></ul></article>
<article class="detail"><span class="num">05 — Hybrid &amp; virtual events</span><h3>The capability we built our name on.</h3>
<p>Interactive event platforms with agendas, Q&amp;A, chat and breakouts; remote contribution; audiences in the room and online, seamlessly together. Born in 2020, refined on every show since.</p>
<ul><li>Event platform &amp; registration</li><li>Remote speaker contribution</li><li>Hybrid room + stream design</li></ul></article>
<article class="detail"><span class="num">06 — Podcast production</span><h3>End-to-end podcasts for brands.</h3>
<p>Recording (in studio or remote), editing, artwork and managed hosting with monthly distribution — an ongoing service, not a one-off.</p>
<ul><li>Studio &amp; remote recording</li><li>Edit, mix &amp; artwork</li><li>Managed hosting &amp; distribution</li></ul></article>
</div></div></section>''')

P['studios.html'] = page('studios.html',
 'Studios — Virtual Studio Events','A UK-wide network of broadcast-spec partner studios in Manchester, Norwich, Fareham and Chichester.',
 'Studio network','A studio network, <span class="em">not a single room.</span>',
 'Trusted partner studios across the UK — every one meeting our minimum broadcast spec — or we bring the studio to your premises.',
 '''<section class="content-sec"><div class="wrap reveal">
<div class="gallery">
<div class="img-frame"><img src="assets/img/hero-manchester.jpg" alt="Manchester studio with VSE branding" loading="lazy"></div>
<div class="img-frame"><img src="assets/img/fareham-pink.jpg" alt="Fareham studio set, pink lighting" loading="lazy"></div>
<div class="img-frame"><img src="assets/img/norwich-day.jpg" alt="Norwich studio, daylight set" loading="lazy"></div>
<div class="img-frame"><img src="assets/img/fareham-set.jpg" alt="Fareham studio interview set" loading="lazy"></div>
<div class="img-frame"><img src="assets/img/norwich-blue.jpg" alt="Norwich studio, blue neon" loading="lazy"></div>
<div class="img-frame"><img src="assets/img/fareham-blue.jpg" alt="Fareham studio in blue" loading="lazy"></div>
</div>
<div class="content-sec prose">
<p><strong>Manchester · Norwich · Fareham · Chichester</strong> — plus our studio partner <a href="https://granary.digital/"><strong>Granary Digital</strong></a>. Every partner studio meets a minimum specification for broadcast-quality content: proper lighting, acoustics, gallery space and connectivity.</p>
<p>Need it closer to home? We build pop-up studios at your premises — set, lighting, cameras and a connected gallery, anywhere in the UK.</p>
</div></div></section>''')

P['work.html'] = page('work.html',
 'Work — Virtual Studio Events','Case studies: a 75,000-viewer awards show, national retail townhalls, charity events and white-label production.',
 'Selected work','Shows we were trusted <span class="em">not to drop.</span>',
 "A few of the productions we can talk about — much of our best work ships under our clients' names.",
 '''<section class="content-sec"><div class="wrap">
<article class="card reveal"><div class="card-img"><img class="plx" src="assets/img/hero-manchester.jpg" alt="VSE broadcast studio"></div>
<div><span class="card-tag">Awards · 2020</span><h3>The 75,000-viewer awards show</h3><p>Our first contract: a full awards production streamed live to seventy-five thousand people — vision mixing, graphics, audio and delivery, end to end. The show that proved the model.</p></div></article>
<article class="card reveal"><div class="card-img"><img class="plx" src="assets/img/asda-live.jpg" alt="Live show floor"></div>
<div><span class="card-tag">Retail townhalls</span><h3>National retail, live to every store</h3><p>Studio townhalls and supplier conferences for the UK's biggest retailers — Waitrose, Morrisons, ASDA and John Lewis among them — interactive Q&amp;A, polls and tens of thousands of colleagues watching live.</p></div></article>
<article class="card reveal"><div class="card-img"><img class="plx" src="assets/img/platform-waitrose.jpg" alt="VSE event platform"></div>
<div><span class="card-tag">Platform</span><h3>Branded event platforms</h3><p>Registration, agendas, breakouts and live Q&amp;A under the client's brand — the connective tissue of every hybrid event we run, designed and developed per event.</p></div></article>
<article class="card reveal"><div class="card-img"><img class="plx" src="assets/img/fareham-pink.jpg" alt="Studio set"></div>
<div><span class="card-tag">White-label</span><h3>The crew behind the crew</h3><p>Video HODs, vMix operators and streaming engineers embedded in other companies' productions — trusted in front of their clients, invisible in the credits. Ask us about this work; our partners will vouch for what we can't show.</p></div></article>
</div></section>''')

P['about.html'] = page('about.html',
 'About — Virtual Studio Events',"Founded in 2020 by James Jones and Ben O'Dwyer. 40+ years of combined live event experience.",
 'The studio','Built in a crisis. <span class="em">Proven on every show since.</span>',
 "Founded in March 2020 by James Jones and Ben O'Dwyer — 40+ years of combined live event experience.",
 '''<section class="content-sec"><div class="wrap reveal"><div class="two-col">
<div class="prose">
<p>Virtual Studio Events started by streaming an awards show to <strong>75,000 people</strong> when the world shut down. While venues were dark, we built the platform, the cloud galleries and the remote workflows that kept our clients' audiences connected.</p>
<p>When live came back, we kept the lot. Today the same go-big-or-go-home crew delivers the technical layer of live, hybrid and broadcast events for the UK's leading production companies, agencies, charities and brands — in the gallery, in the studio, and in the cloud.</p>
<p><strong>James Jones</strong> and <strong>Ben O'Dwyer</strong> lead every project personally. No account managers, no hand-offs — the people you brief are the people on comms.</p>
</div>
<div class="img-frame"><img src="assets/img/fareham-blue.jpg" alt="Fareham studio in blue" loading="lazy"></div>
</div>
<div class="stat-row">
<div class="stat"><b>75<small>K</small></b><span>Peak live audience</span></div>
<div class="stat"><b>40<small>+</small></b><span>Years combined experience</span></div>
<div class="stat"><b>500<small>+</small></b><span>Jobs delivered since 2020</span></div>
<div class="stat"><b>UK</b><span>Studio network, runs worldwide</span></div>
</div></div></section>''')

P['contact.html'] = page('contact.html',
 'Contact — Virtual Studio Events','Start a project with Virtual Studio Events. Same-day response on every enquiry.',
 'Say hello','Got a show <span class="em">coming up?</span>',
 "Tell us the date and the ambition — we'll handle the rest. Same-day response on every enquiry.",
 '''<section class="content-sec"><div class="wrap reveal"><div class="contact-grid">
<div class="contact-card"><h3>Email</h3><p><a href="mailto:enquiries@virtualstudio.events">enquiries@virtualstudio.events</a></p></div>
<div class="contact-card"><h3>Phone</h3><p><a href="tel:+442035986555">+44 020 359 86555</a></p></div>
<div class="contact-card"><h3>WhatsApp</h3><p><a href="https://wa.me/message/BOOOL7EHUXW4O1">Message us directly ↗</a></p></div>
</div></div></section>''')

for name, content in P.items():
    open(name,'w').write(content)
    print('wrote', name)
