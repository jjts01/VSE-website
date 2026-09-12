"""Knowledge hub: pillars, guides, event-type landing pages, tools, glossary, news.
Registers pages into the generator's P dict."""
import json, re, html as H

SITE = "https://www.virtualstudio.events/"
DATE = "2026-09-12"

PILLARS = [
 dict(key='pre-production', slug='pillar-pre-production.html', name='Pre-production & planning', num='01',
      title='Virtual Event Pre-Production & Planning Guides | Virtual Studio Events',
      desc='How to plan a virtual or hybrid event: run orders, speaker preparation, rehearsals, redundancy planning, budgets and accessibility — from working broadcast engineers.',
      h1='Pre-production: <span class="em">where shows are won.</span>',
      lede='Every flawless live event was boring in the gallery because the work happened weeks earlier. These guides cover the planning that makes show day calm.',
      blurb='Run orders, speaker prep, rehearsals, redundancy, budgets and accessibility.'),
 dict(key='infrastructure', slug='pillar-infrastructure.html', name='Streaming infrastructure', num='02',
      title='Live Streaming Infrastructure Explained: Internet, Encoders, Cloud Galleries | Virtual Studio Events',
      desc='Plain-English engineering guides to live streaming infrastructure: connectivity and bonding, encoders and bitrates, cloud production on AWS, remote contribution, audio and CDNs.',
      h1='Infrastructure: <span class="em">the bit nobody sees.</span>',
      lede='Bandwidth, encoders, cloud galleries, contribution links and delivery — the plumbing behind a stream that never drops, explained without the jargon.',
      blurb='Connectivity, encoders, cloud production, remote contribution, audio and delivery.'),
 dict(key='set-design', slug='pillar-set-design.html', name='Sets, studios & on-screen look', num='03',
      title='Set Design, Studio Lighting & On-Screen Graphics for Streaming | Virtual Studio Events',
      desc='How to design sets for camera, choose between LED walls, green screen and cyc, light for broadcast, brand your stream with graphics and get presenters looking their best.',
      h1='Sets &amp; studios: <span class="em">designing for the lens.</span>',
      lede='A room that looks great to the audience in it can look flat on a stream. These guides are about building for the camera first.',
      blurb='Set building, backdrops, lighting, graphics and presenting to camera.'),
 dict(key='live-production', slug='pillar-live-production.html', name='Live production', num='04',
      title='Live Event Production: Gallery Roles, Show Calling & Recovery | Virtual Studio Events',
      desc='Inside the production gallery: crew roles, show calling and comms, running live Q&A and polls, hybrid room-plus-stream delivery, simulcasting and what to do when it goes wrong.',
      h1='Live production: <span class="em">standby… go.</span>',
      lede='What actually happens on show day — who does what, how the calls are made, and how professionals recover when something breaks on air.',
      blurb='Gallery roles, comms, live interaction, hybrid delivery and recovery playbooks.'),
 dict(key='platforms', slug='pillar-platforms.html', name='Platforms & registration', num='05',
      title='Virtual Event Platforms: Comparison, Features, Registration & GDPR | Virtual Studio Events',
      desc='Choosing and running a virtual event platform: feature checklists, Teams vs Zoom vs YouTube vs dedicated platforms, registration flows, attendee data and GDPR, engagement tools.',
      h1='Platforms: <span class="em">the venue is software.</span>',
      lede='Independent, platform-agnostic guidance on where your audience watches, how they register, and what to do with the data — from a team that runs shows on all of them.',
      blurb='Platform comparison, feature checklists, registration, data and engagement.'),
 dict(key='analytics', slug='pillar-analytics.html', name='Analytics, ROI & after the show', num='06',
      title='Virtual Event Analytics, ROI & Post-Event Content | Virtual Studio Events',
      desc='Which virtual event metrics matter, how to measure ROI, how to turn a live event into on-demand and social content, and how to write the post-event report leadership will read.',
      h1='After the show: <span class="em">proving it worked.</span>',
      lede='The stream ends; the value doesn\'t have to. Metrics that matter, ROI models, on-demand strategy and the report that gets next year\'s budget approved.',
      blurb='Metrics, ROI, on-demand and repurposing, post-event reporting.'),
]
PILLAR_BY_KEY = {p['key']: p for p in PILLARS}

# ---------------- guides (imported from per-pillar modules) ----------------
from content_prepro import GUIDES as G1
from content_infra import GUIDES as G2
from content_sets import GUIDES as G3
from content_live import GUIDES as G4
from content_platforms import GUIDES as G5
from content_analytics import GUIDES as G6
GUIDES = G1 + G2 + G3 + G4 + G5 + G6
GUIDE_BY_SLUG = {g['slug']: g for g in GUIDES}

AUTHOR = '''<div class="author"><div class="av">VSE</div><p><b>Written by the Virtual Studio Events production team</b>James Jones and Ben O'Dwyer have 40+ years combined in live event production and have run broadcasts for the BBC, ITV, Waitrose, Morrisons, John Lewis and the UK's leading production companies since 2020.</p></div>'''

def slugify(t):
    return re.sub(r'[^a-z0-9]+','-',t.lower()).strip('-')

def add_ids(body):
    """give h2s ids and return (body, toc list)"""
    toc=[]
    def rep(m):
        txt=re.sub('<[^>]+>','',m.group(1)); i=slugify(txt); toc.append((i,txt))
        return f'<h2 id="{i}">{m.group(1)}</h2>'
    body=re.sub(r'<h2>(.*?)</h2>',rep,body)
    return body,toc

def guide_page(page, crumb, g):
    p=PILLAR_BY_KEY[g['pillar']]
    body,toc=add_ids(g['body'])
    rel=[GUIDE_BY_SLUG[s] for s in g.get('related',[]) if s in GUIDE_BY_SLUG]
    words=len(re.sub('<[^>]+>',' ',body).split())
    mins=max(3,round(words/220))
    schema='<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"Article","headline":g['h1_plain'],"description":g['desc'],"author":{"@type":"Organization","name":"Virtual Studio Events"},"publisher":{"@type":"Organization","name":"Virtual Studio Events","logo":{"@type":"ImageObject","url":SITE+"assets/img/logo-stacked-white.png"}},"mainEntityOfPage":SITE+g['slug'],"datePublished":"2026-06-11","dateModified":DATE,"wordCount":words,"articleSection":p['name']})+'</script>'
    side='<aside class="side">'
    if toc: side+='<div class="side-box toc"><h4>In this guide</h4><ul>'+''.join(f'<li><a href="#{i}">{t}</a></li>' for i,t in toc)+'</ul></div>'
    if rel: side+='<div class="side-box"><h4>Related guides</h4><ul>'+''.join(f'<li><a href="{r["slug"]}">{r["h1_plain"]}</a></li>' for r in rel)+'</ul></div>'
    side+=f'<div class="side-box"><h4>Need it done?</h4><p style="font-size:.92rem;color:var(--ink-dim);margin-bottom:14px">We deliver this for the UK\'s leading brands and production companies.</p><a class="cta-btn" href="contact.html" style="display:inline-block">Talk to us</a></div></aside>'
    content=f'''<section class="content-sec"><div class="wrap"><div class="guide-wrap"><article class="guide-body reveal">{body}{AUTHOR}</article>{side}</div></div></section>'''
    crumbs=[('index.html','Home'),('resources.html','Resources'),(p['slug'],p['name']),(g['slug'],g['h1_plain'])]
    return page(g['slug'],g['title'],g['desc'],p['name'],g['h1'],g['lede'],content,crumbs=crumbs,extra_head=schema,
                hero_extra=f'<div class="guide-meta">{mins} min read · Updated September 2026</div>')

def guide_list(guides):
    out='<div class="guide-list">'
    for i,g in enumerate(guides,1):
        out+=f'<a href="{g["slug"]}"><span class="n">{i:02d}</span><div><h3>{g["h1_plain"]}</h3><p>{g["lede"]}</p></div><span class="ar">→</span></a>'
    return out+'</div>'

def pillar_page(page, p):
    gs=[g for g in GUIDES if g['pillar']==p['key']]
    intro=p.get('intro','')
    body=f'''<section class="content-sec"><div class="wrap reveal">{intro}{guide_list(gs)}
<div style="margin-top:70px"><span class="eyebrow">Explore the other pillars</span><div class="pillar-grid" style="margin-top:30px">'''+''.join(f'<a class="pillar-card" href="{q["slug"]}"><span class="num">{q["num"]}</span><h3>{q["name"]}</h3><p>{q["blurb"]}</p></a>' for q in PILLARS if q['key']!=p['key'])+'</div></div></div></section>'
    crumbs=[('index.html','Home'),('resources.html','Resources'),(p['slug'],p['name'])]
    return page(p['slug'],p['title'],p['desc'],'Knowledge hub · '+p['num'],p['h1'],p['lede'],body,crumbs=crumbs)

# ---------------- event-type landing pages ----------------
from content_events import EVENTS, EVENT_FAQ_SCHEMA
def event_page(page, e):
    faqs=e.get('faqs',[])
    faq_html='' if not faqs else '<div style="margin-top:80px"><span class="eyebrow">Common questions</span><h2 class="big">'+e['faq_title']+'</h2><div class="rate-table">'+''.join(f'<div class="rate-row"><h4>{q}</h4><p>{a}</p><span></span></div>' for q,a in faqs)+'</div></div>'
    rel=[GUIDE_BY_SLUG[s] for s in e.get('related',[]) if s in GUIDE_BY_SLUG]
    rel_html='' if not rel else '<div style="margin-top:80px"><span class="eyebrow">Plan it properly</span><h2 class="big">Guides for this kind of event</h2>'+guide_list(rel)+'</div>'
    body=f'''<section class="content-sec"><div class="wrap reveal"><div class="two-col"><div class="prose">{e['intro']}</div><div class="img-frame"><img src="assets/img/{e['img']}" alt="{e['img_alt']}" loading="lazy"></div></div>
<div style="margin-top:80px"><span class="eyebrow">What we deliver</span><h2 class="big">{e['deliver_title']}</h2><div class="detail-list">'''+''.join(f'<div class="detail"><span class="num">{n}</span><h3>{t}</h3><p>{d}</p></div>' for n,t,d in e['deliverables'])+f'''</div></div>{rel_html}{faq_html}</div></section>'''
    extra='' if not faqs else EVENT_FAQ_SCHEMA(faqs)
    crumbs=[('index.html','Home'),('event-types.html','Event types'),(e['slug'],e['name'])]
    return page(e['slug'],e['title'],e['desc'],e['kicker'],e['h1'],e['lede'],body,crumbs=crumbs,extra_head=extra)

def event_index(page):
    body='<section class="content-sec"><div class="wrap reveal"><div class="pillar-grid">'+''.join(f'<a class="pillar-card" href="{e["slug"]}"><span class="num">{e["kicker"]}</span><h3>{e["name"]}</h3><p>{e["card"]}</p></a>' for e in EVENTS)+'</div></div></section>'
    return page('event-types.html','Virtual, Hybrid & Live Event Production by Event Type | Virtual Studio Events',
        'Production for every format: virtual and hybrid conferences, town halls and all-hands, awards shows, webinars, product launches and AGMs — delivered by broadcast-grade crew UK-wide.',
        'Event types','Whatever the format, <span class="em">we\'ve run it.</span>',
        'Pick the kind of event you\'re planning. Each page explains what a broadcast-grade delivery looks like, what it costs, and the guides to read first.',
        body, crumbs=[('index.html','Home'),('event-types.html','Event types')])

# ---------------- resources hub ----------------
from content_misc import FAQS, GLOSSARY, NEWS, TOOLS_BODY, TEMPLATES_BODY
def resources_hub(page):
    featured=['guide-live-streaming-cost.html','guide-hybrid-event-checklist.html','guide-internet-connectivity.html','guide-event-metrics.html']
    fg=[GUIDE_BY_SLUG[s] for s in featured if s in GUIDE_BY_SLUG]
    faq_ld='<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub('<[^>]+>','',a)}} for q,a in FAQS]})+'</script>'
    body=f'''<section class="content-sec"><div class="wrap reveal">
<span class="eyebrow">Six pillars · {len(GUIDES)} guides</span><h2 class="big">The complete virtual &amp; hybrid event knowledge base</h2>
<div class="pillar-grid">'''+''.join(f'<a class="pillar-card" href="{p["slug"]}"><span class="num">{p["num"]}</span><h3>{p["name"]}</h3><p>{p["blurb"]}</p><span class="cnt">{sum(1 for g in GUIDES if g["pillar"]==p["key"])} guides →</span></a>' for p in PILLARS)+f'''</div>
<div style="margin-top:90px"><span class="eyebrow">Start here</span><h2 class="big">Most useful right now</h2>{guide_list(fg)}</div>
<div style="margin-top:90px"><span class="eyebrow">Tools &amp; templates</span><h2 class="big">Do the maths before you ask for a quote</h2>
<div class="pillar-grid" style="margin-top:34px">
<a class="pillar-card" href="tools.html"><span class="num">Calculator</span><h3>Streaming bandwidth calculator</h3><p>How much upload you really need, with headroom and backup paths.</p></a>
<a class="pillar-card" href="tools.html#budget"><span class="num">Estimator</span><h3>Virtual event budget estimator</h3><p>A realistic UK cost range from cameras, hours, remote speakers and platform.</p></a>
<a class="pillar-card" href="templates.html"><span class="num">Templates</span><h3>Run order, tech spec &amp; post-event report</h3><p>The documents we use on every show — download and adapt.</p></a>
</div></div>
<div style="margin-top:90px"><span class="eyebrow">Reference</span><div class="pillar-grid" style="margin-top:30px">
<a class="pillar-card" href="glossary.html"><span class="num">A–Z</span><h3>Virtual event glossary</h3><p>{len(GLOSSARY)} terms from bitrate to vision mixer, defined in one sentence each.</p></a>
<a class="pillar-card" href="news.html"><span class="num">Updated monthly</span><h3>News &amp; industry briefing</h3><p>What\'s changing in virtual and hybrid events, with sources.</p></a>
<a class="pillar-card" href="event-types.html"><span class="num">By format</span><h3>Production by event type</h3><p>Conferences, town halls, awards, webinars, launches and AGMs.</p></a>
</div></div>
<div style="margin-top:90px"><span class="eyebrow">Quick answers</span><h2 class="big">Frequently asked questions</h2><div class="rate-table">'''+''.join(f'<div class="rate-row"><h4>{q}</h4><p>{a}</p><span></span></div>' for q,a in FAQS)+'</div></div></div></section>'
    return page('resources.html','Virtual Event Resources: Guides, Tools, Templates & Glossary | Virtual Studio Events',
        f'The UK\'s most complete virtual and hybrid event knowledge base: {len(GUIDES)} expert guides across pre-production, streaming infrastructure, set design, live production, platforms and analytics, plus free tools and templates.',
        'Resources','Everything we wish <span class="em">clients knew.</span>',
        'Plain-English guides from the people in the gallery — how to plan it, what it costs, how the technology works, and how to prove it was worth it.',
        body, crumbs=[('index.html','Home'),('resources.html','Resources')], extra_head=faq_ld)

def glossary_page(page):
    letters=sorted(set(t[0].upper() for t,_ in GLOSSARY))
    nav='<div class="gloss-nav">'+''.join(f'<a href="#g-{l}">{l}</a>' for l in letters)+'</div>'
    body='<section class="content-sec"><div class="wrap reveal">'+nav+'<dl class="gloss">'
    cur=''
    for t,d in sorted(GLOSSARY,key=lambda x:x[0].lower()):
        l=t[0].upper()
        if l!=cur: cur=l; body+=f'<h2 class="big" id="g-{l}" style="margin-top:60px;font-size:1.6rem">{l}</h2>'
        body+=f'<dt id="{slugify(t)}">{t}</dt><dd>{d}</dd>'
    body+='</dl></div></section>'
    ld='<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"DefinedTermSet","name":"Virtual Event Glossary","hasDefinedTerm":[{"@type":"DefinedTerm","name":t,"description":re.sub('<[^>]+>','',d)} for t,d in GLOSSARY]})+'</script>'
    return page('glossary.html',f'Virtual Event & Live Streaming Glossary: {len(GLOSSARY)} Terms Explained | Virtual Studio Events',
        'Every virtual event and live streaming term you\'ll meet in a production meeting — bitrate, mix-minus, SRT, vision mixer, cyc, lower third — defined in plain English.',
        'Glossary','Speak <span class="em">gallery.</span>',
        'The words your production company uses, defined in one plain sentence each. Bookmark it for your next tech meeting.',
        body, crumbs=[('index.html','Home'),('resources.html','Resources'),('glossary.html','Glossary')], extra_head=ld)

def news_page(page):
    body='<section class="content-sec"><div class="wrap reveal"><div class="prose"><p>A monthly briefing on what\'s changing in virtual, hybrid and live event production — market data, technology shifts and what they mean for your next show. Every claim links to its source.</p></div>'
    for n in NEWS:
        body+=f'<article class="news-item"><span class="date">{n["date"]}</span><h3>{n["title"]}</h3><p>{n["body"]}</p>'+('' if not n.get('src') else '<p class="src">Sources: '+' · '.join(f'<a href="{u}" rel="noopener">{t}</a>' for t,u in n['src'])+'</p>')+'</article>'
    body+='</div></section>'
    return page('news.html','Virtual Events News & Industry Briefing (September 2026) | Virtual Studio Events',
        'Monthly virtual and hybrid events industry briefing: market growth, AI in production, accessibility requirements, platform changes and what they mean for organisers. Sourced and updated.',
        'News & insights','What\'s changing, <span class="em">and why it matters.</span>',
        'A monthly, sourced briefing on the virtual and hybrid events industry — written for organisers who need the signal, not the noise.',
        body, crumbs=[('index.html','Home'),('news.html','News & insights')])

def tools_page(page):
    return page('tools.html','Free Virtual Event Tools: Bandwidth Calculator & Budget Estimator | Virtual Studio Events',
        'Free tools for planning a live stream or virtual event: a streaming bandwidth calculator with headroom and backup, and a UK virtual event budget estimator based on real production pricing.',
        'Free tools','Do the maths <span class="em">before the quote.</span>',
        'Two calculators we built for our own pre-production, opened up for everyone. No sign-up, no email capture.',
        TOOLS_BODY, crumbs=[('index.html','Home'),('resources.html','Resources'),('tools.html','Tools')],
        extra_head='<script defer src="assets/js/tools.js?v=1"></script>')

def templates_page(page):
    return page('templates.html','Free Event Templates: Run Order, Technical Spec & Post-Event Report | Virtual Studio Events',
        'Download the templates broadcast crews actually use: a live event run order, a technical specification for suppliers and venues, and a post-event report structure.',
        'Templates','The documents <span class="em">behind every show.</span>',
        'Copy them, adapt them, make them yours. Every one of these lives in our own pre-production folder.',
        TEMPLATES_BODY, crumbs=[('index.html','Home'),('resources.html','Resources'),('templates.html','Templates')],
        extra_head='<script defer src="assets/js/tools.js?v=1"></script>')

def register(P, page, breadcrumb_html):
    for g in GUIDES: P[g['slug']]=guide_page(page,breadcrumb_html,g)
    for p in PILLARS: P[p['slug']]=pillar_page(page,p)
    for e in EVENTS: P[e['slug']]=event_page(page,e)
    P['event-types.html']=event_index(page)
    P['resources.html']=resources_hub(page)
    P['glossary.html']=glossary_page(page)
    P['news.html']=news_page(page)
    P['tools.html']=tools_page(page)
    P['templates.html']=templates_page(page)
