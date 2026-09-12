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

NAV_ITEMS = [("platform.html","Platform"),("services.html","Services"),("event-types.html","Event types"),("work.html","Work"),("resources.html","Resources"),("news.html","News"),("contact.html","Contact")]
SITE = "https://www.virtualstudio.events/"
TRACKING = """<!-- Microsoft Clarity -->
<script type="text/javascript">(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window, document, "clarity", "script", "yh85iv2y4g");</script>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-1SVVZ8ZEVK"></script>
<script>window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag('js', new Date());gtag('config', 'G-1SVVZ8ZEVK');</script>"""
CSSV = "v=13"

ORG_SCHEMA = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"ProfessionalService","name":"Virtual Studio Events","legalName":"Virtual Studio Events Limited","url":"https://www.virtualstudio.events/","logo":"https://www.virtualstudio.events/assets/img/logo-stacked-white.png","image":"https://www.virtualstudio.events/assets/img/hero-manchester.jpg","address":{"@type":"PostalAddress","addressLocality":"Chichester","addressRegion":"West Sussex","addressCountry":"GB"},"priceRange":"££","foundingDate":"2020-03","founders":[{"@type":"Person","name":"James Jones"},{"@type":"Person","name":"Ben O\'Dwyer"}],"description":"Broadcast-grade live, hybrid and virtual event production: senior technical crew, streaming engineering, editing and full production delivery.","email":"enquiries@virtualstudio.events","telephone":"+442035986555","areaServed":"GB","sameAs":[]}</script>'

FOOTER_COLS = [
 ("Platform",[("platform.html","Overview"),("platform-register.html","Register"),("platform-engage.html","Engage"),("platform-connect.html","Connect"),("platform-stage.html","Stage"),("platform-broadcast.html","Broadcast"),("platform-insight.html","Insight"),("demos.html","Live demos"),("platform-features.html","Full feature list"),("pipeline.html","The pipeline"),("platform-packages.html","Packages")]),
 ("Services",[("services.html","Crew & engineering"),("services.html","Streaming & vMix"),("services.html","Production management"),("studios.html","Studio hire"),("work.html","Case studies")]),
 ("Event types",[("event-virtual-conference.html","Virtual conferences"),("event-hybrid-conference.html","Hybrid conferences"),("event-town-hall.html","Town halls & all-hands"),("event-awards-show.html","Awards shows"),("event-webinar.html","Webinars"),("event-product-launch.html","Product launches")]),
 ("Resources",[("resources.html","Knowledge hub"),("pillar-pre-production.html","Pre-production"),("pillar-infrastructure.html","Streaming infrastructure"),("pillar-live-production.html","Live production"),("pillar-analytics.html","Analytics & ROI"),("glossary.html","Glossary"),("tools.html","Free tools & templates")]),
 ("Company",[("about.html","About"),("news.html","News & insights"),("contact.html","Contact"),("mailto:enquiries@virtualstudio.events","enquiries@virtualstudio.events")]),
]

def breadcrumb_html(trail):
    """trail: list of (href,label); last item is current page"""
    items=[]; ld=[]
    for i,(href,label) in enumerate(trail):
        last = i==len(trail)-1
        items.append(f'<span aria-current="page">{label}</span>' if last else f'<a href="{href}">{label}</a>')
        ld.append({"@type":"ListItem","position":i+1,"name":label,"item":SITE+href if href!='index.html' else SITE})
    import json
    schema='<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":ld})+'</script>'
    return '<nav class="crumbs" aria-label="Breadcrumb">'+' <span>/</span> '.join(items)+'</nav>'+schema

def page(slug, title, desc, hero_kicker, hero_h1, hero_lede, body, crumbs=None, extra_head='', hero_extra=''):
    cur = ' aria-current="page"'
    nav = "\n".join(f'    <li><a href="{h}"{cur if h==slug else ""}>{t}</a></li>' for h,t in NAV_ITEMS)
    url = SITE + ('' if slug=='index.html' else slug)
    crumb = breadcrumb_html(crumbs) if crumbs else ''
    cols = "".join(f'<div><h4>{h}</h4><ul>'+"".join(f'<li><a href="{u}">{l}</a></li>' for u,l in links)+'</ul></div>' for h,links in FOOTER_COLS)
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#212b54">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="icon" type="image/png" href="assets/img/icon-white.png">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="https://www.virtualstudio.events/assets/img/gen/hero-studio-wide.jpg">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Virtual Studio Events">
<meta name="twitter:card" content="summary_large_image">
{TRACKING}
<link rel="preload" href="assets/fonts/milliard-extrabold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/milliard-book.woff2" as="font" type="font/woff2" crossorigin>
{ORG_SCHEMA}
{extra_head}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/main.css?{CSSV}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div id="loader"><img src="assets/img/logo-stacked-white.png" alt=""><div class="pct">0%</div></div>
<div id="progress"></div>
<nav id="nav">
  <a class="logo" href="index.html"><img src="assets/img/logo-long-white.png" alt="Virtual Studio Events"></a>
  <ul id="menu">
{nav}
    <li class="m-only"><a href="studios.html">Studios</a></li>
    <li class="m-only"><a href="demos.html">Demos</a></li>
    <li class="m-only"><a href="about.html">About</a></li>
  </ul>
  <a class="cta-btn" href="contact.html">Start a project</a>
  <button class="menu-btn" id="menuBtn" aria-label="Open menu" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
</nav>
<header class="page-hero" id="top">
  {SWIRL}
  <div class="wrap">
    {crumb}
    <span class="kicker"><span class="live-dot"></span> {hero_kicker}</span>
    <h1>{hero_h1}</h1>
    <p class="lede">{hero_lede}</p>
    {hero_extra}
  </div>
</header>
<main id="main">
{body}
</main>
<section class="contact" id="contact">
  <div class="wrap reveal">
    <span class="eyebrow">Let's get started</span>
    <h2>Bring us the show <span class="em">you can't afford to drop.</span></h2>
    <p>A date and an ambition is plenty. We'll engineer the rest — from "can we?" to "standby… go."</p>
    <div class="contact-links">
      <a class="cta-btn" href="mailto:enquiries@virtualstudio.events">Email the studio</a>
      <a class="ghost-btn" href="tel:+442035986555">+44 020 359 86555</a>
    </div>
  </div>
</section>
<footer>
  <div class="foot-grid">
    <div class="foot-brand"><img src="assets/img/logo-stacked-white.png" alt="Virtual Studio Events"><p>Live, hybrid &amp; broadcast event production. Chichester studio, UK-wide crew, cloud galleries worldwide.</p></div>
    {cols}
  </div>
  <div class="foot-base"><span>© 2026 Virtual Studio Events Limited · Studio partner: <a href="https://granary.digital/">Granary Digital</a></span><span><a href="sitemap.xml">Sitemap</a></span></div>
</footer>
<script src="assets/js/main.js?{CSSV}"></script>
</body>
</html>"""

P = {}

P['services.html'] = page('services.html',
 'Event Crew Hire & Technical Production Services UK | Virtual Studio Events','Hire senior video engineers, vMix operators, streaming engineers and production managers UK-wide. White-label crew for production companies; full technical delivery for brands.',
 'What we do','One crew, <span class="em">the whole show.</span>',
 'From a single remote vMix operator to full technical delivery of a multi-day conference — scale us up or down to fit the show.',
 '''<section class="content-sec"><div class="wrap reveal"><div class="demo-cta"><div><span class="eyebrow">New</span><h3>VSE Platform: registration, participation, networking and analytics under the same roof as the crew</h3><p>Every service below now plugs into the platform — or buy the platform on its own.</p></div><a class="cta-btn" href="platform.html">See the platform →</a></div><div class="detail-list" style="margin-top:40px">
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
 'Broadcast & Live Streaming Studio Hire UK | Virtual Studio Events','Broadcast-spec studio hire in Chichester plus a UK partner network in Manchester, Norwich and Fareham. Pre-lit, connected and crewed for live streaming and filming.',
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
<div class="img-frame"><img src="assets/img/gen/hero-studio-wide.jpg" alt="Broadcast studio with a lit cyclorama and camera pedestal" loading="lazy"></div>
<div class="img-frame"><img src="assets/img/gen/pillar-set-design.jpg" alt="Studio set lit in teal and navy" loading="lazy"></div>
<div class="img-frame"><img src="assets/img/gen/audio-desk.jpg" alt="Audio mixing desk in a production gallery" loading="lazy"></div>
</div>
<div class="content-sec prose">
<p><strong>Manchester · Norwich · Fareham · Chichester</strong> — plus our studio partner <a href="https://granary.digital/"><strong>Granary Digital</strong></a>. Every partner studio meets a minimum specification for broadcast-quality content: proper lighting, acoustics, gallery space and connectivity.</p>
<p>Need it closer to home? We build pop-up studios at your premises — set, lighting, cameras and a connected gallery, anywhere in the UK.</p>
</div></div></section>''')

P['work.html'] = page('work.html',
 'Event Production Case Studies | Virtual Studio Events','A 75,000-viewer live awards show, national retail townhalls for Waitrose and Morrisons, hybrid conferences and white-label crew work — see how we deliver.',
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
 'About Virtual Studio Events | UK Event Production Experts',"Founded in 2020 by James Jones and Ben O'Dwyer — 40+ years of combined live event experience delivering broadcast-grade production for the UK's biggest brands.",
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
 'Contact Us | Virtual Studio Events — UK Event Production Company','Talk to us about live, hybrid or virtual event production, crew hire or studio booking. Same-day response on every enquiry, UK-wide delivery.',
 'Say hello','Got a show <span class="em">coming up?</span>',
 "Tell us the date and the ambition — we'll handle the rest. Same-day response on every enquiry.",
 '''<section class="content-sec"><div class="wrap reveal"><div class="contact-grid">
<div class="contact-card"><h3>Email</h3><p><a href="mailto:enquiries@virtualstudio.events">enquiries@virtualstudio.events</a></p></div>
<div class="contact-card"><h3>Phone</h3><p><a href="tel:+442035986555">+44 020 359 86555</a></p></div>
</div></div></section>''')



# ---- knowledge hub, landing pages, tools, news, glossary ----
from content_hub import register
register(P, page, breadcrumb_html)
from content_platform import register as register_platform
register_platform(P, page)

for name, content in P.items():
    open(name,'w').write(content)
    print('wrote', name)

# sitemap
urls = ['index.html'] + [k for k in P.keys()]
xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls:
    loc = SITE + ('' if u=='index.html' else u)
    xml += f'<url><loc>{loc}</loc><lastmod>2026-09-12</lastmod></url>\n'
xml += '</urlset>\n'
open('sitemap.xml','w').write(xml)
print('sitemap:', len(urls), 'urls')

# ---- keep hand-built index.html chrome in sync ----
import re as _re
idx = open('index.html').read()
sample = P['services.html']
nav_new = _re.search(r'<nav id="nav">.*?</nav>', sample, _re.S).group(0).replace(' aria-current="page"','')
foot_new = _re.search(r'<footer>.*?</footer>', sample, _re.S).group(0)
idx = _re.sub(r'<nav id="nav">.*?</nav>', lambda m: nav_new, idx, flags=_re.S)
idx = _re.sub(r'<footer>.*?</footer>', lambda m: foot_new, idx, flags=_re.S)
idx = _re.sub(r'main\.css\?v=\d+', 'main.css?'+CSSV, idx); idx = _re.sub(r'main\.js\?v=\d+', 'main.js?'+CSSV, idx)
idx = idx.replace('assets/img/hero-manchester.jpg"', 'assets/img/gen/hero-studio-wide.jpg"')
if 'clarity.ms' not in idx:
    idx = idx.replace('<meta name="twitter:card" content="summary_large_image">','<meta name="twitter:card" content="summary_large_image">\n'+TRACKING,1)
open('index.html','w').write(idx)
nf = open('404.html').read()
if 'clarity.ms' not in nf:
    nf = nf.replace('<link rel="stylesheet"', TRACKING+'\n<link rel="stylesheet"',1)
    open('404.html','w').write(nf)
print('index chrome synced + tracking')

# ---- keep PROJECT-PLAN.md in sync with reality on every build ----
try:
    import plan as _plan
    _p, _g, _w = _plan.build()
    print(f'PROJECT-PLAN.md updated: {_p} pages, {_g} guides, ~{_w:,} words')
except Exception as _e:
    print('plan update skipped:', _e)
