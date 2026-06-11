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

NAV_ITEMS = [("services.html","Services"),("studios.html","Studios"),("work.html","Work"),("resources.html","Resources"),("about.html","About"),("contact.html","Contact")]

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
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.virtualstudio.events/{'' if slug=='index.html' else slug}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="assets/fonts/milliard-extrabold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/milliard-book.woff2" as="font" type="font/woff2" crossorigin>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Organization","name":"Virtual Studio Events","legalName":"Virtual Studio Events Limited","url":"https://www.virtualstudio.events/","logo":"https://www.virtualstudio.events/assets/img/logo-stacked-white.png","foundingDate":"2020-03","founders":[{{"@type":"Person","name":"James Jones"}},{{"@type":"Person","name":"Ben O'Dwyer"}}],"description":"Broadcast-grade live, hybrid and virtual event production: senior technical crew, streaming engineering, editing and full production delivery.","email":"enquiries@virtualstudio.events","telephone":"+442035986555","areaServed":"GB","sameAs":[]}}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/main.css?v=5">
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

    </div>
  </div>
</section>
<footer>
  <img src="assets/img/logo-stacked-white.png" alt="VSE">
  <span>Live, hybrid &amp; broadcast event production · United Kingdom</span>
  <span>© 2026 Virtual Studio Events Limited · Studio partner: <a href="https://granary.digital/">Granary Digital</a></span>
</footer>
<script src="assets/js/main.js?v=5"></script>
</body>
</html>'''

P = {}

P['services.html'] = page('services.html',
 'Event Crew Hire & Technical Production Services UK | Virtual Studio Events','Hire senior video engineers, vMix operators, streaming engineers and production managers UK-wide. White-label crew for production companies; full technical delivery for brands.',
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


def article_schema(slug,title,desc):
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{title}","description":"{desc}","author":{{"@type":"Organization","name":"Virtual Studio Events"}},"publisher":{{"@type":"Organization","name":"Virtual Studio Events","logo":{{"@type":"ImageObject","url":"https://www.virtualstudio.events/assets/img/logo-stacked-white.png"}}}},"mainEntityOfPage":"https://www.virtualstudio.events/{slug}","datePublished":"2026-06-11","dateModified":"2026-06-11"}}</script>'

P['resources.html'] = page('resources.html',
 'Virtual & Hybrid Event Resources, Guides & FAQs | Virtual Studio Events','Free guides on planning virtual events, hybrid event technical checklists, live streaming costs and choosing an event platform — from working production engineers.',
 'Resources','Everything we wish <span class="em">clients knew.</span>',
 'Plain-English guides from the people in the gallery — how to plan it, what it costs, and what to ask before you book anyone (including us).',
 """<section class="content-sec"><div class="wrap reveal"><div class="detail-list">
<a class="detail" href="guide-virtual-event-production.html"><span class="num">Guide 01</span><h3>How to plan a virtual event: the production guide</h3><p>Formats, run orders, rehearsals, redundancy — the practical checklist we run on every show, written for organisers.</p></a>
<a class="detail" href="guide-hybrid-event-checklist.html"><span class="num">Guide 02</span><h3>The hybrid event technical checklist</h3><p>Room + stream is where events fail. The 20 questions to settle before show day, from audio splits to remote speakers.</p></a>
<a class="detail" href="guide-live-streaming-cost.html"><span class="num">Guide 03</span><h3>How much does live streaming an event cost?</h3><p>Honest UK numbers: what drives the price of a stream, from a single-camera webinar to a multi-studio broadcast.</p></a>
<a class="detail" href="guide-virtual-event-platform.html"><span class="num">Guide 04</span><h3>Choosing a virtual event platform: what actually matters</h3><p>Registration, Q&amp;A, breakouts, analytics — the feature checklist, and when you don't need a platform at all.</p></a>
</div>
<div style="margin-top:110px">
<span class="eyebrow">Quick answers</span>
<h2 class="big">Frequently asked questions</h2>
<div class="rate-table" itemscope>
<div class="rate-row"><h4>What's the difference between a virtual and a hybrid event?</h4><p>A virtual event happens entirely online — speakers and audience all join remotely. A hybrid event has a physical room with a live audience and an online audience watching the same show, with both able to take part.</p><span></span></div>
<div class="rate-row"><h4>How far in advance should we book production?</h4><p>For a straightforward stream, two weeks is comfortable. For a multi-day hybrid conference, six to eight weeks gives time for platform builds, rehearsals and proper redundancy planning.</p><span></span></div>
<div class="rate-row"><h4>Can you work with our existing AV supplier or venue?</h4><p>Yes — much of our work is alongside other suppliers and in-house teams. We slot in for the streaming, vision or platform layer, or take the whole technical delivery.</p><span></span></div>
<div class="rate-row"><h4>Do you travel outside the UK?</h4><p>Yes. We're UK-based with a studio network across the south and partners nationwide, and we deliver shows across Europe and worldwide — or run them remotely from our cloud galleries.</p><span></span></div>
</div></div>
</div></section>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What's the difference between a virtual and a hybrid event?","acceptedAnswer":{"@type":"Answer","text":"A virtual event happens entirely online - speakers and audience all join remotely. A hybrid event has a physical room with a live audience and an online audience watching the same show, with both able to take part."}},{"@type":"Question","name":"How far in advance should we book production?","acceptedAnswer":{"@type":"Answer","text":"For a straightforward stream, two weeks is comfortable. For a multi-day hybrid conference, six to eight weeks gives time for platform builds, rehearsals and proper redundancy planning."}},{"@type":"Question","name":"Can you work with our existing AV supplier or venue?","acceptedAnswer":{"@type":"Answer","text":"Yes - much of our work is alongside other suppliers and in-house teams. We slot in for the streaming, vision or platform layer, or take the whole technical delivery."}},{"@type":"Question","name":"Do you travel outside the UK?","acceptedAnswer":{"@type":"Answer","text":"Yes. We are UK-based with a studio network across the south and partners nationwide, and we deliver shows across Europe and worldwide - or run them remotely from our cloud galleries."}}]}</script>""")


GUIDE_FOOT = """<div class="rate-note" style="margin-top:60px">Need this done rather than read about? <a href="contact.html" style="color:var(--accent2)">Talk to our production team</a> — same-day response.</div>"""

P['guide-virtual-event-production.html'] = page('guide-virtual-event-production.html',
 'How to Plan a Virtual Event: Production Guide (2026) | Virtual Studio Events','Step-by-step virtual event production guide from working broadcast engineers: format, run order, rehearsals, redundancy, platforms and crew.',
 'Guide 01','How to plan a virtual event: <span class="em">the production guide.</span>',
 'The practical checklist we run on every show — written for the person whose name is on the invite.',
 """<section class="content-sec"><div class="wrap reveal"><div class="prose">
<p><strong>Start with the audience, not the tech.</strong> Before anything else, answer three questions: who is watching, where are they watching (desk, phone, a screen in an office?), and what must they be able to do — just watch, or ask questions, vote and network? Every production decision flows from those answers.</p>
<p><strong>Choose the format.</strong> A town hall is not a conference is not an awards show. Single-session events suit a broadcast approach: one stream, strong presenter, tight run order. Multi-track conferences need a platform with agendas and breakouts. Awards shows live or die on pace — pre-record the risky bits, keep the live moments live.</p>
<p><strong>Build a real run order.</strong> Every minute accounted for: who is on, what is on screen, which microphone, what plays next. The run order is the single document that lets a gallery anticipate rather than react. If your production company doesn't ask for one, worry.</p>
<p><strong>Rehearse the failure, not just the show.</strong> A proper technical rehearsal tests remote speakers on the actual kit they'll use on the day — same laptop, same room, same connection. It also tests what happens when things break: backup presenter link, holding slides, a second internet path. We run every show with redundant encoders and a second connection because one of them will eventually be needed.</p>
<p><strong>Pre-record strategically.</strong> Anything that cannot be allowed to fail — the CEO's keynote, the awards montage — consider pre-recording with a live Q&amp;A after. Audiences accept polished pre-records; they don't accept frozen keynotes.</p>
<p><strong>Crew it properly.</strong> Minimum viable crew for a professional virtual event: a vision mixer/vMix operator, a producer calling the show, and someone dedicated to speaker wrangling. One person cannot do all three well — and on show day, "well" is the only acceptable standard.</p>
<p><strong>Measure what mattered.</strong> Peak concurrent viewers, average watch time, Q&amp;A volume, drop-off points. Set up analytics before the event; decide afterwards what you'll change next time.</p>
</div>""" + GUIDE_FOOT + """</div></section>""" )

P['guide-hybrid-event-checklist.html'] = page('guide-hybrid-event-checklist.html',
 'Hybrid Event Technical Checklist: 20 Questions | Virtual Studio Events','The hybrid event checklist used by broadcast engineers: audio splits, remote speakers, room cameras, streaming redundancy and platform integration.',
 'Guide 02','The hybrid event <span class="em">technical checklist.</span>',
 'Hybrid is where events fail — a great room show with an unwatchable stream, or vice versa. Settle these before show day.',
 """<section class="content-sec"><div class="wrap reveal"><div class="prose">
<p><strong>The golden rule:</strong> the online audience is not an afterthought — it's usually the bigger audience. Design the show for both rooms from day one.</p>
<p><strong>Audio.</strong> Will the stream take a dedicated mix (not the room PA feed)? Who provides the audio split? Are remote speakers' returns mix-minus so they don't hear themselves? Audio is 80% of perceived stream quality — settle it first.</p>
<p><strong>Cameras and vision.</strong> How many cameras cover the stage, and is at least one shot framed for screens rather than the back of the room? Are slides fed to the stream as a clean source rather than a camera pointed at a projector? Who mixes the stream — and is that a different person from whoever mixes the room screens?</p>
<p><strong>Remote contribution.</strong> How do remote speakers join — a managed broadcast link or a consumer video call? Have they been tested on the actual hardware? What happens in the room when a remote speaker presents: where do they appear, and can they see and hear the room properly?</p>
<p><strong>Connectivity.</strong> Is there dedicated, wired internet for the stream — separate from venue guest Wi-Fi? What's the backup path (bonded 4G/5G, second circuit)? Has someone actually speed-tested the line from the position the encoder will sit?</p>
<p><strong>The platform layer.</strong> Where does the online audience watch, and can they interact — Q&amp;A, polls, chat? Do questions from the platform reach the moderator on stage? Is registration data captured somewhere useful?</p>
<p><strong>People.</strong> Who is the single technical point of contact across venue AV, streaming and platform? On hybrid shows the most common failure isn't equipment — it's three suppliers each assuming another one owns the gap. That's the job we're most often hired to do: own the gap.</p>
</div>""" + GUIDE_FOOT + """</div></section>""")

P['guide-live-streaming-cost.html'] = page('guide-live-streaming-cost.html',
 'How Much Does Live Streaming an Event Cost? UK Guide 2026 | Virtual Studio Events','Honest UK pricing for event live streaming: what drives cost, typical budgets from single-camera webinars to multi-camera hybrid broadcasts.',
 'Guide 03','What does live streaming <span class="em">actually cost?</span>',
 'Honest UK numbers and what drives them — so you can budget before you ask anyone for a quote.',
 """<section class="content-sec"><div class="wrap reveal"><div class="prose">
<p>Streaming costs scale with four things: <strong>cameras, hours, destinations and risk</strong>. Here's how that plays out in practice in the UK market in 2026 (all figures exclude VAT and assume a single day).</p>
<p><strong>Simple webinar or boardroom stream — roughly £750–£1,500.</strong> One camera, slides, a streaming engineer with an encoder, one destination (Teams, YouTube, LinkedIn). The cost is mostly the engineer's day and the kit.</p>
<p><strong>Single-room conference or town hall — roughly £2,000–£5,000.</strong> Two to three cameras, vision mixing, a dedicated stream audio mix, graphics and lower-thirds, redundant encoding, possibly a remote speaker or two. Crew of two to three.</p>
<p><strong>Hybrid conference or awards show — £5,000–£15,000+.</strong> Multi-camera, full graphics package, platform with registration and Q&amp;A, remote contributors managed on broadcast links, rehearsal day, redundant everything. The platform and the rehearsal day are the items people forget to budget.</p>
<p><strong>What moves the number up:</strong> multiple sessions or rooms streamed simultaneously, pre-records and edit work, custom platform builds, international remote speakers needing managed links and out-of-hours rehearsals, and same-day highlight edits.</p>
<p><strong>What moves it down:</strong> a venue with good in-house AV that provides a clean audio split and camera feeds; flexible timings; using our cloud galleries instead of physical kit on site; and remote operation — a remote vMix operator runs from a fraction of the on-site cost.</p>
<p><strong>The cheapest insurance you can buy</strong> is redundancy: a second encoder and a bonded backup connection typically add a few hundred pounds — against the cost of your event going dark in front of your whole company.</p>
</div>""" + GUIDE_FOOT + """</div></section>""")

P['guide-virtual-event-platform.html'] = page('guide-virtual-event-platform.html',
 'Choosing a Virtual Event Platform: Feature Checklist | Virtual Studio Events','Which virtual event platform features matter: registration, Q&A, breakouts, analytics — and when you don\'t need a platform at all.',
 'Guide 04','Choosing a virtual event platform: <span class="em">what actually matters.</span>',
 'Twelve features worth paying for, the ones that are marketing fluff — and when you don\'t need a platform at all.',
 """<section class="content-sec"><div class="wrap reveal"><div class="prose">
<p><strong>First: do you need one?</strong> If your event is one session, one audience, watch-only — you don't need an event platform. A well-produced stream into YouTube, LinkedIn or Teams will reach more people with less friction. Platforms earn their cost when you need registration, multiple sessions, interaction or sponsor visibility.</p>
<p><strong>Features that matter:</strong> registration that exports clean data; an agenda that handles time zones; reliable embedded streaming (test it on a corporate network — many block consumer video); moderated Q&amp;A with upvoting; polls that display into the live show; breakout rooms that a producer can open and close; per-session analytics; branding control; and crucially, a production back-end your crew can drive — speaker green rooms, source switching, screen-share management.</p>
<p><strong>Features that are usually fluff:</strong> 3D lobbies and avatars (novelty wears off in minutes and accessibility suffers), gamification badges, AI matchmaking on events under a few hundred attendees, and "metaverse" anything.</p>
<p><strong>The questions to ask any platform vendor:</strong> What happens when a viewer's connection drops — does the player recover on its own? What's the real concurrency limit, with proof? Can we get the attendee data out, in full, afterwards? What does support look like during the live event — a human on a channel, or a ticket queue?</p>
<p><strong>Our position:</strong> we're platform-agnostic. We build bespoke event platforms when the brief demands it, and we'll happily run your show into Teams, Zoom, or a third-party platform when that's the right answer. The platform is the venue — the show is what we're there for.</p>
</div>""" + GUIDE_FOOT + """</div></section>""")

P['contact.html'] = page('contact.html',
 'Contact Us | Virtual Studio Events — UK Event Production Company','Talk to us about live, hybrid or virtual event production, crew hire or studio booking. Same-day response on every enquiry, UK-wide delivery.',
 'Say hello','Got a show <span class="em">coming up?</span>',
 "Tell us the date and the ambition — we'll handle the rest. Same-day response on every enquiry.",
 '''<section class="content-sec"><div class="wrap reveal"><div class="contact-grid">
<div class="contact-card"><h3>Email</h3><p><a href="mailto:enquiries@virtualstudio.events">enquiries@virtualstudio.events</a></p></div>
<div class="contact-card"><h3>Phone</h3><p><a href="tel:+442035986555">+44 020 359 86555</a></p></div>
</div></div></section>''')

for name, content in P.items():
    open(name,'w').write(content)
    print('wrote', name)
