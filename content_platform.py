"""VSE Platform: product overview, modules, pipeline, packages, integrations, demos."""
import json, re

SITE="https://www.virtualstudio.events/"

MODULES = [
 dict(img='gen/mod-register.jpg', img_alt='Phone showing a check-in code beside a blank badge and badge printer', key='register', slug='platform-register.html', name='Register', tag='Registration, ticketing & check-in',
  title='Event Registration, Ticketing & Check-in Software | VSE Platform',
  desc='Branded event registration with ticket types, payments, invitations, approval workflows, SSO, waitlists, calendar sync, QR check-in and badge printing for virtual, hybrid and live events.',
  h1='Register: <span class="em">from invite to badge in one flow.</span>',
  lede='Branded registration pages, ticketing and payments, approvals, SSO for internal events, QR check-in and on-site badge printing, with every attendee record flowing straight into the live event and the analytics afterwards.',
  demo='demo-registration.html', demo_label='Try the registration & check-in demo',
  features=[
   ('Branded registration pages','Your domain, your brand, your fields. Multi-step forms with conditional questions, custom ticket types and session selection at sign-up.'),
   ('Ticketing & payments','Free, paid, early-bird and promo-coded tickets; card and invoice payment; VAT handling; automatic receipts and refunds.'),
   ('Invitations & approvals','Invite-only lists, approval queues for gated events, waitlists that auto-promote, and capacity per session.'),
   ('SSO & internal events','SAML/OIDC single sign-on so employees join a town hall with one click: no registration form at all.'),
   ('Confirmations & reminders','Calendar files, personalised join links, the hour-before reminder that lifts attendance, and SMS on request.'),
   ('QR check-in & badges','Scan-to-check-in on any phone for hybrid events, on-site badge printing, session scanning for CPD and attendance.'),
   ('Data that leaves cleanly','Every field exportable, synced to your CRM in real time, retention rules you set. GDPR by design.'),
   ('Event website & email campaigns','A branded event site built from your registration data (agenda, speakers, sponsors), plus invitation, reminder and follow-up email campaigns with open and click tracking.'),
   ('Surveys & certificates','Pre- and post-event surveys, session feedback, and automatic CPD or attendance certificates issued from the check-in record.'),
   ('Multi-language & multi-currency',"Registration and confirmations in the attendee's language; ticketing in GBP, EUR, USD and more with local VAT handling."),
  ],
  related=['guide-registration-data-gdpr.html','guide-virtual-event-platform.html']),
 dict(vid='audience', img='gen/mod-engage.jpg', img_alt='Audience in a darkened auditorium holding up glowing phones', key='engage', slug='platform-engage.html', name='Engage', tag='Live audience participation',
  title='Live Audience Participation Platform: Q&A, Polls, Quizzes, Reactions | VSE Platform',
  desc='Branded live audience participation for virtual, hybrid and in-room events: moderated Q&A with upvoting, polls and quizzes with on-screen results, reactions, word clouds, live chat, captions and translation.',
  h1='Engage: <span class="em">the audience in the show, not just watching it.</span>',
  lede='A branded participation layer that works on any phone or laptop, in the room or online: moderated Q&A, polls, quizzes with leaderboards, reactions, word clouds, chat, with results rendered into the broadcast graphics by the gallery.',
  demo='demo-audience.html', demo_label='Try the live participation demo',
  features=[
   ('Moderated Q&A','Questions submitted from any device, upvoted by the audience, curated by a moderator, pushed to the presenter\'s screen and rendered on air as a graphic.'),
   ('Polls & quizzes','Multiple choice, ratings, ranking and open text; timed quizzes with live leaderboards; results animated into the stream, not just the app.'),
   ('Reactions & word clouds','Emoji reactions that float across the broadcast, word clouds that build live from audience answers.'),
   ('Live chat & moderation','Hosted chat with profanity filters, slow mode, pre-moderation for public events and message pinning.'),
   ('Captions & translation','Automated or human live captions and real-time translation into the languages your audience chooses, on their own device.'),
   ('In-room & online together','One participation layer for both audiences: the room joins by QR code, online joins from the player. Same polls, same Q&A, fair interleaving.'),
   ('Presenter & moderator views','A presenter tablet with the curated question queue; a moderator console for approving, merging and scheduling; gallery triggers for the graphics.'),
   ('Broadcast-ready outputs','Poll results, questions, word clouds and leaderboards published as graphics sources for vMix, OBS and hardware mixers, so any gallery can put them on air.'),
   ('Scales to 50,000+','Load-tested for town halls with tens of thousands of participants, rate-limited and moderated for public events.'),
  ],
  related=['guide-live-interaction.html','guide-engagement-features.html','guide-accessibility.html']),
 dict(img='gen/mod-connect.jpg', img_alt='Two people meeting at an exhibition stand', key='connect', slug='platform-connect.html', name='Connect', tag='Networking, expo & sponsors',
  title='Virtual Event Networking, Expo Booths & Sponsor Platform | VSE Platform',
  desc='Networking and commercial features for virtual and hybrid events: 1:1 meeting scheduling, AI matchmaking, hosted roundtables, virtual expo booths with lead capture, sponsor visibility and ROI reporting.',
  h1='Connect: <span class="em">the conversations around the content.</span>',
  lede='1:1 meeting booking, matchmaking, hosted roundtables, exhibitor booths with lead capture, and sponsor placements that report their own ROI: the commercial layer that pays for the event.',
  demo='demo-event-hub.html', demo_label='See networking in the event hub demo',
  features=[
   ('1:1 meetings','Attendees browse profiles, request meetings, and join video calls from their agenda. Time-zone aware, with no-show tracking.'),
   ('Matchmaking','Interest-based suggestions for who to meet, and speed-networking rounds hosted by a facilitator. The format that actually works.'),
   ('Roundtables & lounges','Small-group video tables with topics and hosts; producers can open, close and move people.'),
   ('Expo booths','Exhibitor pages with video, downloads, live chat, meeting booking and a "leave your details" button that becomes a scanned lead.'),
   ('Lead capture & retrieval','In-room badge scanning and online booth interactions unified into one lead list per exhibitor, exportable or synced to their CRM.'),
   ('Sponsor placements','Logo walls, session sponsorships, sponsored breaks and push notifications: every placement with an impressions and clicks report.'),
   ('Community after the event','Keep the network open for 30 days: on-demand content, continued messaging, and a reason to come back next year.'),
   ('Smart badges & contactless leads',"NFC/QR smart badges for hybrid events: tap to connect, tap to leave details at a booth, every tap a lead in the exhibitor's list."),
   ('Exhibitor self-serve portal','Exhibitors build their own booth, upload content, invite staff and download their leads: no organiser admin.'),
  ],
  related=['guide-engagement-features.html','guide-measuring-roi.html']),
 dict(img='gen/mod-stage.jpg', img_alt='Grid of on-demand video thumbnails with a play button', key='stage', slug='platform-stage.html', name='Stage', tag='Agenda, sessions & content',
  title='Event Agenda, Sessions, Breakouts & On-Demand Content Platform | VSE Platform',
  desc='The attendee experience: personalised multi-track agendas, session rooms with embedded broadcast streams, breakouts, speaker portal and green room, resource library and an on-demand hub with the same analytics after the event.',
  h1='Stage: <span class="em">where the audience watches, and comes back.</span>',
  lede='Multi-track agendas with personal schedules, session rooms with the broadcast embedded at low latency, breakouts, a speaker portal with green room, resource downloads and an on-demand library that keeps the event working for months.',
  demo='demo-event-hub.html', demo_label='Try the attendee event hub demo',
  features=[
   ('Multi-track agenda','Tracks, time zones, personal schedules with reminders, session capacity and add-to-calendar.'),
   ('Session rooms','Broadcast stream embedded with low-latency delivery, captions, Q&A and polls beside the picture, and resources for the session.'),
   ('Breakouts & workshops','Producer-controlled breakout rooms, hosted workshops, and a way back to the main stage on cue.'),
   ('Speaker portal & green room','Speakers upload bios and slides, run their tech check, wait in a virtual green room and go live on the producer\'s cue.'),
   ('Resource library','Slides, transcripts, documents and links per session, downloadable and tracked.'),
   ('On-demand hub','Chaptered recordings published within hours, gated or open, with the same engagement and analytics as live.'),
   ('Mobile app','iOS and Android app for hybrid attendees: agenda, room finder, participation, networking and notifications.'),
   ('AI chapters, summaries & clips','Every session automatically chaptered, summarised and cut into suggested highlight clips minutes after it ends, reviewed by our editors before publishing.'),
   ('Live translation & multi-language','Captions and translation into the languages your audience chooses, on their own device, plus multi-language agendas and interfaces.'),
   ('Attendee AI assistant',"A branded assistant that answers 'where is the ROI session?' and 'what did I miss?' from the event's own data."),
  ],
  related=['guide-on-demand-repurposing.html','guide-speaker-prep.html']),
 dict(vid='global-network', img='gen/mod-broadcast.jpg', img_alt='Global network of streaming signal paths across a dark globe', key='broadcast', slug='platform-broadcast.html', name='Broadcast', tag='Production & streaming',
  title='Broadcast-Grade Production Integrated With Your Event Platform | VSE Platform',
  desc='The difference between a platform and a show: VSE studios, cloud galleries, remote contribution, redundant streaming and broadcast graphics feeding the platform, produced by the crew behind the BBC, ITV and Waitrose events.',
  h1='Broadcast: <span class="em">a platform is a venue. This is the show.</span>',
  lede='Every other platform hands you a webcam grid. Ours is fed by a production gallery, studio or cloud, with vision mixing, broadcast graphics, remote contribution on managed links and redundant delivery. The engagement data flows back into the pictures.',
  demo='demo-audience.html', demo_label='See gallery graphics in the participation demo',
  features=[
   ('Studio or cloud gallery','Produced from our Chichester studio, a partner studio, your venue or a cloud gallery on AWS: same crew, same standard.'),
   ('Remote contribution','Speakers join on broadcast-quality links from the speaker portal, tested in advance, with mix-minus returns and dial-in fallbacks.'),
   ('Broadcast graphics','Lower thirds, stings, sponsor idents and, uniquely, live poll results, Q&A and word clouds from Engage rendered into the programme.'),
   ('Redundant delivery','Dual encoders, wired plus bonded cellular, low-latency delivery into the platform and a standby destination.'),
   ('Hybrid room integration','Stream audio mix from the room, cameras framed for screens, remote guests on the room screens, one technical lead owning the join.'),
   ('Simulcast','The same programme to LinkedIn, YouTube and your website at once, with cleared music and unified comments.'),
   ('Rehearsed, every time','Tech run, dress rehearsal and failure drills are part of the package, not an extra.'),
   ('Global multi-CDN delivery','Streams delivered through multiple content delivery networks with automatic failover, so a viewer in Singapore gets the same start time and quality as one in Slough.'),
   ('Any ingest, any latency','RTMP and SRT ingest from any gallery; standard, low-latency and sub-second delivery modes chosen per session.'),
  ],
  related=['guide-cloud-production.html','guide-hybrid-event-checklist.html','guide-risk-redundancy.html']),
 dict(img='gen/pillar-analytics.jpg', img_alt='Abstract event analytics curve visualisation', key='insight', slug='platform-insight.html', name='Insight', tag='Analytics, reporting & integrations',
  title='Event Analytics, Engagement Reporting & CRM Integration | VSE Platform',
  desc='Live and post-event analytics: concurrent viewers, attendance curves against the run order, engagement per session, lead scoring, sponsor reports, exports and real-time sync to HubSpot, Salesforce, Marketo and Dynamics.',
  h1='Insight: <span class="em">the report that gets next year approved.</span>',
  lede='A live dashboard during the show and a post-event report the morning after: attendance curves against the run order, engagement per session, leads scored by behaviour, sponsor ROI, synced to your CRM and marketing automation in real time.',
  demo='demo-analytics.html', demo_label='Try the live analytics dashboard demo',
  features=[
   ('Live dashboard','Concurrent viewers, joins and drop-offs, engagement rates and stream health while the show is on air, on the producer\'s screen and yours.'),
   ('Attendance curve vs run order','The one chart that changes next year\'s agenda: who was watching at every item.'),
   ('Per-attendee engagement','Sessions watched, minutes, questions asked, polls answered, resources downloaded, meetings held, scored into an engagement index.'),
   ('Lead scoring & routing','Behaviour-based scoring pushed to sales with the context of what each lead did.'),
   ('Sponsor & exhibitor reports','Impressions, clicks, booth visits, leads and meetings per sponsor, in a report they can forward to their board.'),
   ('Integrations','HubSpot, Salesforce, Marketo, Dynamics, Mailchimp, Slack and Teams notifications, webhooks and a REST API for everything else.'),
   ('Post-event report','Generated the morning after in the structure from our guides: one-page summary, results against targets, recommendations.'),
   ('AI session summaries & insight reports','Automatic summaries of every session, sentiment from Q&A and chat, and a draft post-event report you edit rather than write.'),
   ('Attribution & pipeline',"Attendees matched to CRM opportunities so the event's influenced pipeline is reported, not guessed."),
  ],
  related=['guide-event-metrics.html','guide-measuring-roi.html','guide-post-event-report.html']),
 dict(img='gen/mod-brand.jpg', img_alt='Glowing padlock in a secure data centre corridor', key='brand', slug='platform-brand.html', name='Brand & trust', tag='White-label, security & accessibility',
  title='White-Label Event Platform: Branding, Security, GDPR & Accessibility | VSE Platform',
  desc='A fully white-label event platform on your domain, with enterprise security (SSO, roles, audit logs, UK/EU data residency), GDPR tooling, WCAG 2.1 AA accessibility, captions and BSL, for brands and for agencies reselling under their own name.',
  h1='Brand &amp; trust: <span class="em">your name on it, our standards under it.</span>',
  lede='Your domain, your design system, your emails, or your agency\'s. Underneath: single sign-on, role-based access, audit logs, UK/EU data residency, GDPR tooling and WCAG 2.1 AA accessibility.',
  demo='demo-audience.html', demo_label='Switch brands live in the participation demo',
  features=[
   ('Full white-label','Custom domain, fonts, colours, layouts, email templates and app icon. No "powered by" unless you want it.'),
   ('Agency reseller mode','Production companies run client events under their own brand with separate workspaces, billing and permissions. A large part of our business.'),
   ('Security','SAML/OIDC SSO, MFA, role-based access, audit logs, encrypted at rest and in transit, penetration tested.'),
   ('Data residency & GDPR','UK/EU hosting, data-processing agreement as standard, consent capture, retention rules, subject-access and deletion tooling.'),
   ('Accessibility','WCAG 2.1 AA interface, keyboard and screen-reader support, caption controls, BSL picture-in-picture on the stream.'),
   ('Reliability','Redundant streaming, standby destinations, and a human on a channel during your event: not a ticket queue.'),
   ('Content ownership','Your recordings, your data, exported in full whenever you ask. Deleted when you say so.'),
   ('UK/EU data residency, by default','Platform and attendee data hosted on AWS in London and Frankfurt. VSE is a UK-owned company. Your data is not exposed to US CLOUD Act requests via a US parent.'),
   ('Infrastructure certifications & DPA',"Built on ISO 27001 / SOC 2-certified AWS infrastructure with VSE's own controls aligned to ISO 27001; data-processing agreement, sub-processor list and security questionnaire answers available on request."),
   ('Availability & support','99.9% platform availability target, multi-CDN delivery, and 24/7 event-day support with a producer on a channel: not a ticket queue.'),
  ],
  related=['guide-registration-data-gdpr.html','guide-accessibility.html']),
]
MOD_BY_KEY={m['key']:m for m in MODULES}

PIPELINE = [
 ('01','Brief & design','We take the objective, audience and format and turn it into a production plan, a platform configuration and a run order.', ['guide-virtual-event-production.html','guide-live-streaming-cost.html'], 'register'),
 ('02','Registration & promotion','Branded registration goes live; invitations, reminders and CRM sync run automatically; the audience builds.', ['guide-registration-data-gdpr.html'], 'register'),
 ('03','Content & speakers','Speakers onboard through the portal, upload slides, run tech checks. Graphics and pre-records are produced.', ['guide-speaker-prep.html','guide-graphics-lower-thirds.html'], 'stage'),
 ('04','Studio, set & rehearsal','Set designed for camera, studio or venue rigged, tech run and dress rehearsal with failure drills.', ['guide-set-design-for-camera.html','guide-rehearsals.html'], 'broadcast'),
 ('05','Live','The gallery runs the show into the platform; Engage drives participation; the live dashboard shows what\'s working.', ['guide-show-calling-comms.html','guide-live-interaction.html'], 'engage'),
 ('06','On-demand & content','Chaptered recordings published same day; highlights and social cuts within 48 hours; the network stays open.', ['guide-on-demand-repurposing.html'], 'stage'),
 ('07','Insight & next event','The post-event report, leads routed to sales, sponsor reports delivered, and the plan for next time.', ['guide-post-event-report.html','guide-measuring-roi.html'], 'insight'),
]

PACKAGES = [
 ('Broadcast','Produced webinars, town halls and streams into the tools you already use.','from £1,750 +VAT per event',
  ['Studio or cloud gallery production with broadcast graphics','Engage: moderated Q&A, polls, reactions','Delivery into Teams, Zoom, YouTube, LinkedIn or your site','Redundant encoding and standby destination','Live dashboard and post-event report','Same-day on-demand edit']),
 ('Engage','Conferences, awards and launches that need registration and a branded experience.','from £7,500 +VAT per event',
  ['Everything in Broadcast','Register: branded registration, ticketing, reminders','Stage: multi-track agenda, session rooms, on-demand hub','Engage: quizzes, word clouds, captions and translation','Speaker portal and green room','Insight: engagement scoring, CRM sync, AI session summaries']),
 ('Enterprise programme','A year of events, hybrid flagships, and agencies reselling under their own brand.','from £30,000 +VAT per year',
  ['Everything in Engage, across 5+ events','Connect: networking, expo, sponsors, lead capture','Mobile app, hybrid check-in and badge printing','Full white-label and reseller workspaces','SSO, UK/EU data residency, audit logs, SLA','Named producer and account team']),
]
PLATFORM_ONLY = [
 ('Platform licence (agencies & in-house teams)',"Register + Stage + Engage + Insight without VSE crew, bring your own production, or ours by the day.",'from £1,500 +VAT per event · £12,000 +VAT per year',
  ['Branded registration, agenda, session rooms, on-demand','Full participation layer with broadcast-ready graphics outputs','RTMP/SRT ingest from any gallery','Analytics, exports and integrations','Reseller workspaces and white-label']),
 ('Engage only',"The branded participation layer for any show. Yours, a venue's, or a Teams call.",'from £350 +VAT per event · £2,400 +VAT per year',
  ['Q&A, polls, quizzes, reactions, word clouds, chat','Room join by QR, online join from any player','Moderator console and presenter view','Graphics outputs for vMix, OBS and hardware mixers','Results and attendance exports']),
]
INTEGRATIONS = [
 ('CRM & marketing','HubSpot, Salesforce, Microsoft Dynamics, Marketo, Pardot, Mailchimp: attendee records and engagement scores synced in real time.'),
 ('Collaboration','Microsoft Teams, Zoom, Google Meet and Slack, produced feeds into your meetings, notifications into your channels.'),
 ('Streaming destinations','YouTube, LinkedIn Live, Vimeo, Facebook, your own website player: simulcast from one programme.'),
 ('Identity','SAML 2.0 and OIDC single sign-on with Entra ID, Okta, Google Workspace; SCIM provisioning for internal events.'),
 ('Payments & finance','Stripe and invoice payment, VAT handling, Xero and QuickBooks exports.'),
 ('Accessibility services','Human captioners, BSL interpreters and translation partners plugged into the stream and the platform.'),
 ('Automation & data','Webhooks, a REST API, Zapier and Make for everything else; scheduled exports to your warehouse.'),
 ('Delivery & hosting','Global multi-CDN delivery for viewers anywhere; platform and data hosted on AWS in London and Frankfurt with UK/EU residency by default.'),
]

def module_page(page, m):
    from content_hub import GUIDE_BY_SLUG, guide_list
    feats=''.join(f'<div class="detail"><span class="num">{i:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(m['features'],1))
    others=''.join(f'<a class="pillar-card" href="{o["slug"]}"><span class="num">{o["name"]}</span><h3>{o["tag"]}</h3><p>{o["lede"][:110]}…</p></a>' for o in MODULES if o['key']!=m['key'])
    rel=[GUIDE_BY_SLUG[s] for s in m.get('related',[]) if s in GUIDE_BY_SLUG]
    if m.get('vid'):
        banner=('<div class="media-band reveal"><video autoplay muted loop playsinline preload="metadata" poster="assets/img/gen/poster-'
                +m['vid']+'.jpg" aria-label="'+m['img_alt']+'"><source src="assets/video/'+m['vid']+'.webm" type="video/webm"><source src="assets/video/'+m['vid']+'.mp4" type="video/mp4"></video></div>')
    elif m.get('img'):
        banner=f'<div class="media-band reveal"><img src="assets/img/{m["img"]}" alt="{m["img_alt"]}" loading="lazy"></div>'
    else:
        banner=''
    body=f'''<section class="content-sec"><div class="wrap reveal">{banner}
<div class="demo-cta"><div><span class="eyebrow">Interactive demo</span><h3>{m['demo_label']}</h3><p>Runs in your browser, no sign-up. Switch the brand live.</p></div><a class="cta-btn" href="{m['demo']}">Open demo →</a></div>
<div style="margin-top:80px"><span class="eyebrow">Capabilities</span><h2 class="big">What {m['name']} does</h2><div class="detail-list">{feats}</div></div>
{('<div style="margin-top:90px"><span class="eyebrow">Read the thinking behind it</span><h2 class="big">Guides</h2>'+guide_list(rel)+'</div>') if rel else ''}
<div style="margin-top:90px"><span class="eyebrow">The rest of the platform</span><div class="pillar-grid" style="margin-top:30px">{others}</div></div>
</div></section>'''
    schema='<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"SoftwareApplication","name":f"VSE Platform: {m['name']}","applicationCategory":"BusinessApplication","operatingSystem":"Web, iOS, Android","description":m['desc'],"provider":{"@type":"Organization","name":"Virtual Studio Events"},"offers":{"@type":"Offer","priceCurrency":"GBP","price":"2000","description":"Per-event pricing from £2,000; programme pricing available"}})+'</script>'
    return page(m['slug'],m['title'],m['desc'],'VSE Platform · '+m['name'],m['h1'],m['lede'],body,crumbs=[('index.html','Home'),('platform.html','Platform'),(m['slug'],m['name'])],extra_head=schema)

def platform_overview(page):
    mods=''.join(f'<a class="pillar-card" href="{m["slug"]}"><span class="num">{m["name"]}</span><h3>{m["tag"]}</h3><p>{m["features"][0][1][:120]}…</p><span class="cnt">{len(m["features"])} capabilities →</span></a>' for m in MODULES)
    pipe=''.join(f'<a class="pipe-step" href="{MOD_BY_KEY[k]["slug"]}"><span class="num">{n}</span><h3>{t}</h3><p>{d}</p><span class="cnt">{MOD_BY_KEY[k]["name"]} →</span></a>' for n,t,d,g,k in PIPELINE)
    demos='''<div class="pillar-grid" style="margin-top:34px">
<a class="pillar-card" href="demo-audience.html"><span class="num">Demo 01</span><h3>Live audience participation</h3><p>Phone + presenter + broadcast graphic, side by side. Vote, ask, react, with a simulated audience of 1,200.</p></a>
<a class="pillar-card" href="demo-registration.html"><span class="num">Demo 02</span><h3>Registration &amp; check-in</h3><p>Branded ticket flow, confirmation with QR, and the check-in scanner view.</p></a>
<a class="pillar-card" href="demo-event-hub.html"><span class="num">Demo 03</span><h3>Attendee event hub</h3><p>Agenda, session room with stream, speakers, expo, networking and 1:1 booking.</p></a>
<a class="pillar-card" href="demo-analytics.html"><span class="num">Demo 04</span><h3>Live analytics dashboard</h3><p>Concurrent viewers against the run order, engagement, leads and sponsor ROI, updating live.</p></a></div>'''
    pk=''.join(f'<div class="pkg"><span class="num">{n}</span><h3>{p}</h3><p>{d}</p><ul>'+''.join(f'<li>{x}</li>' for x in items)+'</ul><a class="ghost-btn" href="contact.html">Talk to us</a></div>' for n,p,d,items in [(p[2],p[0],p[1],p[3]) for p in PACKAGES])
    body=f'''<section class="content-sec"><div class="wrap reveal">
<div class="media-band reveal"><video autoplay muted loop playsinline preload="metadata" poster="assets/img/gen/poster-platform-arcs.jpg" aria-label="Abstract rotating broadcast technology visual"><source src="assets/video/platform-arcs.webm" type="video/webm"><source src="assets/video/platform-arcs.mp4" type="video/mp4"></video></div>
<span class="eyebrow">Seven modules · one roof</span><h2 class="big">Registration to ROI, produced like a broadcast</h2>
<p style="color:var(--ink-dim);max-width:64ch;margin-top:16px">Most event platforms are software that hopes you have a production team. Most production companies hand you a stream and no data. VSE Platform is both: the registration, participation, networking and analytics layers of a modern event platform, fed by a real broadcast gallery and delivered by the crew.</p>
<div class="pillar-grid">{mods}</div>
<div style="margin-top:100px"><span class="eyebrow">The full pipeline</span><h2 class="big">How an event moves through the system</h2><div class="pipeline">{pipe}</div><div style="margin-top:24px;display:flex;gap:12px;flex-wrap:wrap"><a class="ghost-btn" href="pipeline.html">See the pipeline in detail →</a><a class="ghost-btn" href="platform-features.html">Full feature list →</a></div></div>
<div style="margin-top:100px"><span class="eyebrow">Try it</span><h2 class="big">Working demos, no sign-up</h2>{demos}</div>
<div style="margin-top:100px"><span class="eyebrow">Packages</span><h2 class="big">Priced per event, or as a programme</h2><div class="pkg-grid">{pk}</div><p class="rate-note">All packages include production crew; platform-only licences are available to production companies under reseller terms. See <a href="platform-packages.html" style="color:var(--accent2)">packages and integrations</a>.</p></div>
</div></section>'''
    schema='<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"SoftwareApplication","name":"VSE Platform","applicationCategory":"BusinessApplication","operatingSystem":"Web, iOS, Android","description":"All-in-one virtual, hybrid and live event platform with integrated broadcast production: registration, audience participation, networking, agenda and on-demand, analytics and integrations.","provider":{"@type":"Organization","name":"Virtual Studio Events"},"offers":{"@type":"AggregateOffer","priceCurrency":"GBP","lowPrice":"2000","highPrice":"60000"},"featureList":"Registration & ticketing, live Q&A and polls, networking and expo, multi-track agenda, broadcast production, analytics and CRM integration, white-label"})+'</script>'
    return page('platform.html','VSE Platform: All-in-One Virtual & Hybrid Event Platform With Broadcast Production',
      'The event platform with a production gallery built in: registration and ticketing, branded live audience participation, networking and expo, agenda and on-demand, analytics and CRM sync, delivered by broadcast crew. Try the live demos.',
      'VSE Platform','Everything an event needs, <span class="em">under one roof.</span>',
      'Registration, participation, networking, agenda, broadcast production, analytics and integrations: one platform, one crew, one point of accountability. Working demos below.',
      body,crumbs=[('index.html','Home'),('platform.html','Platform')],extra_head=schema)

def pipeline_page(page):
    from content_hub import GUIDE_BY_SLUG
    steps=''
    for n,t,d,gs,k in PIPELINE:
        m=MOD_BY_KEY[k]
        links=''.join(f'<li><a href="{s}">{GUIDE_BY_SLUG[s]["h1_plain"]}</a></li>' for s in gs if s in GUIDE_BY_SLUG)
        steps+=f'<div class="pipe-row"><div class="pipe-num">{n}</div><div><h3>{t}</h3><p>{d}</p><div class="pipe-meta"><span>Module: <a href="{m["slug"]}">{m["name"]}</a></span><ul>{links}</ul></div></div></div>'
    body=f'''<section class="content-sec"><div class="wrap reveal"><div class="prose"><p>An event isn't a day; it's a pipeline that starts with a brief and ends with a report and a better plan for next time. Every stage below is owned by a named person on our team, supported by a module of the platform, and documented in the guides, so nothing falls between suppliers.</p></div><div class="pipe-list">{steps}</div>
<div class="callout" style="margin-top:60px"><p><strong>One point of accountability.</strong> Registration, content, studio, live show, on-demand and analytics are one contract and one producer. When something goes wrong at 10:04 on show day, there is exactly one phone number.</p></div></div></section>'''
    return page('pipeline.html','The Full Event Pipeline: Brief to Registration to Live to Analytics | VSE Platform',
      'How a virtual or hybrid event moves through VSE Platform end to end: brief and design, registration, speakers and content, studio and rehearsal, live production, on-demand and post-event insight: one team, one contract.',
      'The pipeline','Brief to report, <span class="em">nothing between the cracks.</span>',
      'The seven stages every event passes through, who owns each, which module supports it and what to read before you get there.',
      body,crumbs=[('index.html','Home'),('platform.html','Platform'),('pipeline.html','Pipeline')])

def packages_page(page):
    pk=''.join(f'<div class="pkg"><span class="num">{p[2]}</span><h3>{p[0]}</h3><p>{p[1]}</p><ul>'+''.join(f'<li>{x}</li>' for x in p[3])+'</ul><a class="cta-btn" href="contact.html">Get a quote</a></div>' for p in PACKAGES)
    ints=''.join(f'<div class="detail"><h3>{t}</h3><p>{d}</p></div>' for t,d in INTEGRATIONS)
    body=f'''<section class="content-sec"><div class="wrap reveal"><span class="eyebrow">Packages</span><h2 class="big">Three ways to buy</h2><div class="pkg-grid">{pk}</div>
<div style="margin-top:70px"><span class="eyebrow">Platform without the crew</span><h2 class="big">For agencies and in-house teams</h2><div class="pkg-grid" style="grid-template-columns:1fr 1fr">'''+''.join(f'<div class="pkg"><span class="num">{p[2]}</span><h3>{p[0]}</h3><p>{p[1]}</p><ul>'+''.join(f'<li>{x}</li>' for x in p[3])+'</ul><a class="ghost-btn" href="contact.html">Ask about reseller terms</a></div>' for p in PLATFORM_ONLY)+'''</div></div>
<div class="callout" style="margin-top:60px"><p><strong>How we priced this (September 2026).</strong> Platform-only licences in the market run from about £1k–£5k a year for self-serve webinar tools to <strong>$10k–$50k per event or year</strong> for mid-market platforms (Hubilo, vFairs, Swapcard, RingCentral Events, Zuddl) and $25k–$500k+ for ON24, Bizzabo and Cvent. UK broadcast production runs £499–£1,000 for a single-camera stream, £895–£3,500 for multi-camera business productions, <strong>£5k–£15k a day for hybrid conferences</strong> with redundancy, and £15k–£50k+ for multi-stage events; specialist crew cost £450–£750 a day. Our packages bundle both layers. An Enterprise programme with production included costs less than many platform-only licences. Sources and the full benchmark are in our <a href="guide-live-streaming-cost.html">cost guide</a>.</p></div>
<p class="rate-note">Every package includes production crew and a rehearsal. Prices are per event and exclude VAT, venue hire and third-party services (human captioners, BSL). Programme pricing covers a year of events with a named producer. Production companies: ask about reseller terms and platform-only licences.</p>
<div style="margin-top:100px"><span class="eyebrow">Integrations</span><h2 class="big">It plugs into what you already run</h2><div class="detail-list">{ints}</div></div>
<div style="margin-top:100px"><span class="eyebrow">Compare</span><h2 class="big">Platform, production company, or both?</h2>
<div class="guide-body"><table><tr><th></th><th>Typical event platform</th><th>Typical production company</th><th>VSE Platform</th></tr>
<tr><td>Registration &amp; ticketing</td><td>Yes</td><td>No</td><td>Yes</td></tr>
<tr><td>Audience participation</td><td>In-app only</td><td>Sometimes, unbranded</td><td>Branded, rendered into the broadcast</td></tr>
<tr><td>Broadcast production</td><td>Webcam grid</td><td>Yes</td><td>Yes: studio or cloud gallery</td></tr>
<tr><td>Hybrid room integration</td><td>Rarely</td><td>Yes</td><td>Yes, one technical lead</td></tr>
<tr><td>Networking &amp; expo</td><td>Yes</td><td>No</td><td>Yes</td></tr>
<tr><td>Analytics &amp; CRM sync</td><td>Yes</td><td>Viewer count</td><td>Yes, plus the run-order curve</td></tr>
<tr><td>Redundancy &amp; rehearsal</td><td>Your problem</td><td>Yes</td><td>Included</td></tr>
<tr><td>Support during the show</td><td>Ticket queue</td><td>The crew</td><td>The crew, plus a producer</td></tr>
<tr><td>Accountability</td><td>Split</td><td>Split</td><td>One contract</td></tr></table></div></div></div></section>'''
    return page('platform-packages.html','VSE Platform Packages, Pricing & Integrations | Virtual Studio Events',
      'VSE Platform packages: Broadcast from £1,750, Engage from £7,500, Enterprise programmes from £30,000 a year with production crew included, plus platform-only licences from £1,500 per event for agencies, plus integrations with HubSpot, Salesforce, Teams, Zoom, YouTube, SSO providers and payments.',
      'Packages & integrations','Buy the show, the platform, <span class="em">or the whole roof.</span>',
      'Per-event packages with crew included, programme pricing for a year of events, reseller terms for agencies, and the integrations that make it fit your stack.',
      body,crumbs=[('index.html','Home'),('platform.html','Platform'),('platform-packages.html','Packages')])


FEATURE_MATRIX = [
 ('Registration & ticketing',['Branded registration pages on your domain','Multi-step forms with conditional questions','Free, paid, early-bird and promo-coded tickets','Card and invoice payment, VAT, refunds','Invite-only lists, approvals, waitlists, capacity','SAML/OIDC single sign-on for internal events','Calendar files, personalised join links, SMS reminders','QR check-in, badge printing, session scanning','Event website builder','Email campaigns with open/click tracking','Surveys and CPD/attendance certificates','Multi-language, multi-currency']),
 ('Live participation',['Moderated Q&A with upvoting and merging','Polls: multiple choice, rating, ranking, open text','Quizzes with live leaderboards','Reactions and word clouds','Hosted chat with filters, slow mode, pinning','Live captions (human or automated) and translation','Room join by QR, online join from any player','Presenter view, moderator console, gallery triggers','Broadcast-ready graphics outputs for vMix/OBS/hardware','Scales to 50,000+ participants']),
 ('Networking & commercial',['Attendee profiles and 1:1 meeting booking','Interest-based matchmaking, speed networking','Hosted roundtables and lounges','Virtual expo booths with video, downloads, chat','Lead capture and retrieval, online and on-site','Smart badges (NFC/QR) for contactless connections','Exhibitor self-serve portal','Sponsor placements with impressions and click reports','Post-event community for 30 days']),
 ('Agenda, sessions & content',['Multi-track agenda, personal schedules, time zones','Session rooms with embedded low-latency stream','Breakouts and hosted workshops','Speaker portal, tech checks, virtual green room','Resource library per session','On-demand hub with the same analytics as live','AI chapters, summaries and suggested clips','Attendee AI assistant','iOS and Android app for hybrid attendees','Multi-language interfaces']),
 ('Broadcast production',['Studio (Chichester and partners) or cloud gallery on AWS','Remote contribution on managed links with mix-minus','Broadcast graphics with live participation data on air','Dual encoders, wired plus bonded cellular','Global multi-CDN delivery with failover','RTMP and SRT ingest; standard, low-latency and sub-second modes','Hybrid room integration with one technical lead','Simulcast to LinkedIn, YouTube, website and platform','Tech run, dress rehearsal and failure drills included']),
 ('Analytics & integrations',['Live dashboard: concurrent, joins, drop-off, stream health','Attendance curve against the run order','Per-attendee engagement index','Lead scoring and routing with behaviour context','Sponsor and exhibitor ROI reports','AI session summaries and draft post-event report','CRM attribution to opportunities and pipeline','HubSpot, Salesforce, Dynamics, Marketo, Pardot, Mailchimp','Teams, Zoom, Google Meet, Slack','Webhooks, REST API, Zapier, Make, warehouse exports']),
 ('Security, data & trust',['Full white-label: domain, design, email, app icon','Agency reseller workspaces and permissions','SSO (SAML/OIDC), MFA, role-based access, audit logs','Encryption in transit and at rest; penetration tested','UK/EU data residency by default (AWS London/Frankfurt)','UK-owned: no US parent, no CLOUD Act exposure','DPA, sub-processor list, security questionnaire responses','Built on ISO 27001 / SOC 2-certified infrastructure','WCAG 2.1 AA interface, captions, BSL on stream','99.9% availability target, 24/7 event-day support','Recordings and data exported in full, deleted on instruction']),
]

def features_page(page):
    grid=''.join('<div class="detail"><h3>'+cat+'</h3><ul class="feat-list">'+''.join(f'<li>{f}</li>' for f in fs)+'</ul></div>' for cat,fs in FEATURE_MATRIX)
    n=sum(len(fs) for _,fs in FEATURE_MATRIX)
    body=f"""<section class="content-sec"><div class="wrap reveal"><span class="eyebrow">{n} capabilities · seven areas</span><h2 class="big">The full list, in one place</h2><p style="color:var(--ink-dim);max-width:62ch;margin-top:16px">Everything the major platforms talk about, plus the production layer they don't have. If something you need isn't here, ask. Most of what we build starts as a client question.</p><div class="detail-list">{grid}</div>
<div style="margin-top:80px"><span class="eyebrow">Delivery &amp; data</span><h2 class="big">Global delivery, data that stays home</h2><div class="guide-body"><p>Viewers are served through <strong>multiple global content delivery networks</strong> with automatic failover, so audiences in Asia-Pacific, the Americas and Europe get the same start time and quality. The platform itself, and every attendee record, lives in <strong>AWS regions in London and Frankfurt</strong>: UK/EU residency by default, with US or APAC residency available for programmes that need it. Virtual Studio Events is a UK-owned company with no US parent, which matters increasingly to procurement teams assessing CLOUD Act exposure.</p><p>Security: single sign-on, MFA, role-based access and audit logs; encryption in transit and at rest; regular penetration testing; infrastructure certified to ISO 27001 and SOC 2 with VSE's own controls aligned to ISO 27001. A data-processing agreement, sub-processor list and completed security questionnaires are available on request. Accessibility to WCAG 2.1 AA, with captions and BSL on the stream. Availability target 99.9%, and (the part no certificate covers) a producer on a channel for the whole of your event.</p></div></div>
<div class="demo-cta" style="margin-top:60px"><div><span class="eyebrow">See it</span><h3>Four working demos, no sign-up</h3><p>Participation, registration, the attendee hub and the analytics dashboard, with a live brand switcher.</p></div><a class="cta-btn" href="demos.html">Try the demos →</a></div></div></section>"""
    return page('platform-features.html','VSE Platform Full Feature List: Registration, Engagement, Networking, Broadcast, Analytics, Security',
      'The complete VSE Platform feature list: registration and ticketing, live participation, networking and expo, agenda and on-demand, broadcast production, analytics and integrations, security with UK/EU data residency and global multi-CDN delivery.',
      'Feature list','Everything, <span class="em">itemised.</span>',
      'The complete capability list across all seven modules, with the delivery and data-residency detail procurement teams ask for.',
      body,crumbs=[('index.html','Home'),('platform.html','Platform'),('platform-features.html','Features')])

# ---------------- demos ----------------
DEMO_HEAD='<script defer src="assets/js/demo.js?v=1"></script>'
BRANDBAR='''<div class="brandbar"><span>Brand:</span><button type="button" data-brand="vse" class="on">Virtual Studio Events</button><button type="button" data-brand="retail">Northfield Retail</button><button type="button" data-brand="charity">Reach Together</button><button type="button" data-brand="tech">Helix Software</button><span class="note">— white-label switches colours, logo and copy live</span></div>'''

def demo_page(page, slug, title, desc, kicker, h1, lede, body, back):
    return page(slug,title,desc,kicker,h1,lede,body,crumbs=[('index.html','Home'),('platform.html','Platform'),(back[0],back[1]),(slug,'Demo')],extra_head=DEMO_HEAD+'<meta name="robots" content="index,follow">')

def demo_audience(page):
    body=BRANDBAR+'''<section class="content-sec" style="padding-top:40px"><div class="wrap">
<div class="demo-grid" id="engage-demo">
 <div class="phone"><div class="phone-top"><span class="dot"></span><b class="brand-name">Virtual Studio Events</b><span class="live">LIVE</span></div>
  <div class="tabs"><button class="on" data-tab="poll">Poll</button><button data-tab="qa">Q&amp;A</button><button data-tab="react">React</button><button data-tab="quiz">Quiz</button><button data-tab="chat">Chat</button></div>
  <div class="pane" data-pane="poll"><h4 id="poll-q">Which format will you run most in 2027?</h4><div id="poll-opts"></div><p class="hint" id="poll-hint">Tap to vote. Results update live for everyone.</p></div>
  <div class="pane hidden" data-pane="qa"><form id="qa-form"><input id="qa-input" placeholder="Ask the panel a question…" maxlength="140"><button type="submit">Ask</button></form><div id="qa-list"></div></div>
  <div class="pane hidden" data-pane="react"><p class="hint">Send a reaction. It floats across the broadcast.</p><div class="react-row"><button data-r="👏">👏</button><button data-r="🔥">🔥</button><button data-r="❤️">❤️</button><button data-r="💡">💡</button><button data-r="🎉">🎉</button></div><p class="hint" id="react-count">0 reactions in the last minute</p></div>
  <div class="pane hidden" data-pane="quiz"><h4 id="quiz-q">Quiz · Q1: What's the recommended keyframe interval for live streaming?</h4><div id="quiz-opts"></div><div id="quiz-board"></div></div>
  <div class="pane hidden" data-pane="chat"><div id="chat-list"></div><form id="chat-form"><input id="chat-input" placeholder="Say something…" maxlength="120"><button type="submit">Send</button></form></div>
  <div class="phone-foot"><span id="aud-count">1,214 watching</span><span>Captions: EN ▾</span></div>
 </div>
 <div class="stage-col">
  <div class="broadcast"><div class="bc-img"></div><div class="bc-graphic" id="bc-graphic"><div class="bc-brand brand-name">Virtual Studio Events</div><div id="bc-content"><div class="bc-title">Live poll</div><div id="bc-poll"></div></div></div><div class="bc-lower"><b>Sarah Okafor</b><span>Head of Events · <span class="brand-name">Virtual Studio Events</span></span></div><div id="react-layer"></div><span class="bc-live">● LIVE · 1,214</span></div>
  <div class="console"><div class="console-head"><b>Moderator console</b><span>what the gallery and presenter see</span></div>
   <div class="console-grid">
    <div><h5>Question queue</h5><div id="mod-queue"></div></div>
    <div><h5>Show on broadcast</h5><div class="mod-btns"><button data-show="poll">Poll results</button><button data-show="qa">Top question</button><button data-show="cloud">Word cloud</button><button data-show="quiz">Quiz leaderboard</button><button data-show="none">Clear graphic</button></div>
     <h5 style="margin-top:18px">Launch</h5><div class="mod-btns"><button id="new-poll">New poll</button><button id="next-quiz">Next quiz question</button></div>
     <h5 style="margin-top:18px">Live stats</h5><div class="stat-mini"><span id="st-votes">0 votes</span><span id="st-q">0 questions</span><span id="st-react">0 reactions</span></div></div>
   </div></div>
 </div>
</div>
<div class="prose" style="margin-top:60px"><p><strong>What you\'re looking at.</strong> The phone is what every attendee sees, in the room by QR code or online beside the player. The broadcast frame is the programme output with Engage results rendered by the gallery as a graphic, not a screenshot of the app. The console is the moderator\'s view: curate questions, decide what goes on air, launch the next poll. A simulated audience of 1,200 is voting, asking and reacting around you. Switch the brand at the top to see the white-label.</p></div>
</div></section>'''
    return demo_page(page,'demo-audience.html','Live Branded Audience Participation Demo: Q&A, Polls, Reactions, Quiz | VSE Platform',
      'Try VSE Engage in your browser: vote in a live poll, ask and upvote questions, send reactions and play a quiz, and see the moderator console and the results rendered into the broadcast graphics. Switch brands live.',
      'Demo 01 · Engage','Live participation, <span class="em">three screens at once.</span>',
      'The attendee\'s phone, the broadcast output and the moderator console: all live, all in your browser, with a simulated audience of 1,200.',body,('platform-engage.html','Engage'))

def demo_registration(page):
    body=BRANDBAR+'''<section class="content-sec" style="padding-top:40px"><div class="wrap">
<div class="reg-wrap" id="reg-demo">
 <div class="reg-steps"><span class="on" data-step="1">1 · Tickets</span><span data-step="2">2 · Details</span><span data-step="3">3 · Confirmed</span><span data-step="4">4 · Check-in</span></div>
 <div class="reg-card">
  <div class="reg-hero"><span class="reg-brand brand-name">Virtual Studio Events</span><h3 class="reg-title">Annual Conference 2027 · Hybrid</h3><p>14 May 2027 · London &amp; online · 09:00–16:30 BST</p></div>
  <div class="reg-step" data-step="1"><h4>Choose your ticket</h4><div class="tickets">
   <label class="ticket"><input type="radio" name="tk" value="Online pass" data-price="0" checked><div><b>Online pass</b><span>Live stream, participation, on-demand for 30 days</span></div><em>Free</em></label>
   <label class="ticket"><input type="radio" name="tk" value="In-person" data-price="195"><div><b>In-person</b><span>Venue, lunch, networking, plus everything online</span></div><em>£195</em></label>
   <label class="ticket"><input type="radio" name="tk" value="VIP" data-price="495"><div><b>VIP &amp; speaker dinner</b><span>Front section, speaker dinner, 1:1 meeting priority</span></div><em>£495</em></label>
  </div><label class="fld">Promo code<input id="promo" placeholder="EARLYBIRD"></label><div class="reg-actions"><span id="tk-total">Total: £0</span><button class="cta-btn" data-next="2">Continue →</button></div></div>
  <div class="reg-step hidden" data-step="2"><h4>Your details</h4><div class="grid2"><label class="fld">First name<input id="r-first" value="Priya"></label><label class="fld">Last name<input id="r-last" value="Shah"></label><label class="fld">Work email<input id="r-email" value="priya@example.com"></label><label class="fld">Organisation<input id="r-org" value="Example Ltd"></label><label class="fld">Role<select id="r-role"><option>Events</option><option>Marketing</option><option>Internal comms</option><option>Production</option></select></label><label class="fld">Sessions of interest<select id="r-track"><option>Hybrid production</option><option>Platforms &amp; data</option><option>Set &amp; studio</option></select></label></div>
   <label class="chk"><input type="checkbox" id="r-consent"> Keep me updated about future events (optional)</label><label class="chk"><input type="checkbox" checked disabled> I accept the privacy notice, recorded sessions, data retained 90 days</label>
   <div class="reg-actions"><button class="ghost-btn" data-next="1">← Back</button><button class="cta-btn" data-next="3">Register</button></div></div>
  <div class="reg-step hidden" data-step="3"><div class="confirm"><h4>You\'re in, <span id="c-name">Priya</span>.</h4><p id="c-sum">Online pass · Annual Conference 2027</p><div class="qr" id="qr"></div><p class="hint">Your personal QR code: scan it at the venue or open your join link online. A calendar file and reminders are on their way to <span id="c-email">priya@example.com</span>.</p><div class="badge"><div class="badge-brand brand-name">Virtual Studio Events</div><b id="b-name">Priya Shah</b><span id="b-org">Example Ltd</span><em id="b-type">Online pass</em></div></div><div class="reg-actions"><button class="cta-btn" data-next="4">Simulate venue check-in →</button></div></div>
  <div class="reg-step hidden" data-step="4"><h4>Check-in scanner (staff view)</h4><div class="scanner"><div class="scan-frame" id="scan-frame"><div class="scan-line"></div></div><div id="scan-result" class="scan-result">Point at a badge QR… <button id="scan-btn" class="ghost-btn">Simulate scan</button></div></div><div class="checkin-log" id="checkin-log"></div><div class="reg-actions"><button class="ghost-btn" data-next="1">Start again</button></div></div>
 </div>
 <aside class="reg-side"><h5>Behind the form</h5><ul id="reg-events"><li>Registration page rendered in brand</li></ul></aside>
</div>
<div class="prose" style="margin-top:60px"><p><strong>What you\'re looking at.</strong> A branded registration flow with ticket types and promo codes, the confirmation with a personal QR and printable badge, and the staff check-in view for hybrid events. The panel on the right shows what happens behind the scenes at each step: CRM sync, reminders scheduled, capacity updated. Switch the brand at the top.</p></div>
</div></section>'''
    return demo_page(page,'demo-registration.html','Event Registration, Ticketing & QR Check-in Demo | VSE Platform',
      'Try VSE Register in your browser: choose a ticket, apply a promo code, register, receive a personal QR and badge, then simulate the venue check-in scanner, with the behind-the-scenes CRM and reminder events shown live.',
      'Demo 02 · Register','From ticket to badge <span class="em">in four steps.</span>',
      'Choose a ticket, register, get your QR and badge, then see the staff check-in view, with everything that happens behind the scenes listed live.',body,('platform-register.html','Register'))

def demo_event_hub(page):
    body=BRANDBAR+'''<section class="content-sec" style="padding-top:40px"><div class="wrap">
<div class="hub" id="hub-demo">
 <div class="hub-nav"><b class="brand-name">Virtual Studio Events</b><button class="on" data-view="agenda">Agenda</button><button data-view="session">Main stage</button><button data-view="speakers">Speakers</button><button data-view="expo">Expo</button><button data-view="network">Networking</button><button data-view="ondemand">On-demand</button><span class="hub-user">Priya S.</span></div>
 <div class="hub-view" data-view="agenda"><div class="hub-head"><h4>Thursday 14 May</h4><div class="track-tabs"><button class="on" data-track="all">All tracks</button><button data-track="A">Main stage</button><button data-track="B">Platforms &amp; data</button><button data-track="C">Workshops</button></div></div><div id="agenda-list"></div></div>
 <div class="hub-view hidden" data-view="session"><div class="sess-grid"><div><div class="player"><div class="player-img"></div><span class="bc-live">● LIVE</span><div class="player-lower"><b>Keynote: Events that survive contact with reality</b><span>Main stage · 09:30–10:15</span></div><div class="cc">Captions: "…and the run order is the document that lets the gallery anticipate…"</div></div><div class="sess-meta"><span>1,214 watching</span><span>Latency: 3s</span><a href="#">Slides ↓</a><a href="#">Transcript ↓</a><a href="#">Add to calendar</a></div></div><div class="sess-side"><div class="tabs"><button class="on" data-stab="qa">Q&amp;A</button><button data-stab="poll">Poll</button><button data-stab="chat">Chat</button></div><div id="sess-qa"></div></div></div></div>
 <div class="hub-view hidden" data-view="speakers"><div class="cards" id="speaker-cards"></div></div>
 <div class="hub-view hidden" data-view="expo"><div class="cards" id="expo-cards"></div></div>
 <div class="hub-view hidden" data-view="network"><div class="net-grid"><div><h4>People to meet</h4><p class="hint">Matched on your interests: hybrid production, platforms &amp; data</p><div id="net-people"></div></div><div><h4>Your meetings</h4><div id="net-meetings"><p class="hint">No meetings booked yet.</p></div><h4 style="margin-top:24px">Roundtables now</h4><div class="rt"><b>Measuring event ROI</b><span>6 seats · hosted by Ben O\'Dwyer</span><button class="ghost-btn">Join</button></div><div class="rt"><b>Hybrid room + stream</b><span>4 seats · hosted by James Jones</span><button class="ghost-btn">Join</button></div></div></div></div>
 <div class="hub-view hidden" data-view="ondemand"><div class="cards" id="vod-cards"></div></div>
</div>
<div class="prose" style="margin-top:60px"><p><strong>What you\'re looking at.</strong> The attendee\'s event hub: Stage and Connect working together. A multi-track agenda with a personal schedule, a session room with the broadcast, captions, Q&amp;A and resources beside it, speaker profiles, exhibitor booths with lead capture, networking with 1:1 meeting requests and hosted roundtables, and the on-demand library. Every tap is an engagement event feeding Insight.</p></div>
</div></section>'''
    return demo_page(page,'demo-event-hub.html','Attendee Event Hub Demo: Agenda, Session Room, Expo & Networking | VSE Platform',
      'Try the VSE attendee experience: a multi-track agenda with personal schedule, a session room with embedded stream and captions, speaker profiles, expo booths with lead capture, 1:1 meeting booking and roundtables, and the on-demand library.',
      'Demo 03 · Stage + Connect','The attendee\'s <span class="em">whole event, one tab.</span>',
      'Agenda, main stage, speakers, expo, networking and on-demand: the branded hub every attendee gets, live in your browser.',body,('platform-stage.html','Stage'))

def demo_analytics(page):
    body=BRANDBAR+'''<section class="content-sec" style="padding-top:40px"><div class="wrap">
<div class="dash" id="dash-demo">
 <div class="dash-head"><div><b class="brand-name">Virtual Studio Events</b> · Annual Conference 2027 · <span class="bc-live">● LIVE</span></div><div class="dash-ctl"><button class="on" data-speed="1">Live</button><button data-speed="8">Fast-forward</button><button id="dash-report" class="ghost-btn">Generate post-event report</button></div></div>
 <div class="kpis"><div class="kpi"><span>Concurrent</span><b id="k-conc">0</b><em id="k-conc-d"></em></div><div class="kpi"><span>Unique attendees</span><b id="k-uniq">0</b><em>of 2,140 registered</em></div><div class="kpi"><span>Avg watch time</span><b id="k-watch">0m</b><em>target 55m</em></div><div class="kpi"><span>Engagement index</span><b id="k-eng">0</b><em>questions · polls · reactions</em></div><div class="kpi"><span>Leads scored</span><b id="k-leads">0</b><em id="k-leads-d">synced to CRM</em></div><div class="kpi"><span>Stream health</span><b id="k-health" class="ok">Good</b><em id="k-health-d">both encoders up</em></div></div>
 <div class="dash-grid"><div class="panel"><h5>Concurrent viewers vs run order</h5><canvas id="curve" width="900" height="300"></canvas><div class="runorder" id="ro-strip"></div></div>
  <div class="panel"><h5>Engagement by session</h5><div id="eng-bars"></div></div>
  <div class="panel"><h5>Top questions (upvotes)</h5><ol id="top-q"></ol></div>
  <div class="panel"><h5>Sponsor performance</h5><table id="sponsor-tbl"><tr><th>Sponsor</th><th>Impr.</th><th>Clicks</th><th>Leads</th></tr></table></div>
  <div class="panel"><h5>Live event log</h5><div id="ev-log" class="ev-log"></div></div></div>
 <div class="report hidden" id="report"><h4>Post-event report, draft</h4><div id="report-body"></div></div>
</div>
<div class="prose" style="margin-top:60px"><p><strong>What you\'re looking at.</strong> Insight during the show: concurrent viewers plotted against the run order (the chart that changes next year\'s agenda), engagement per session, the questions the audience cares about, sponsor impressions and leads, stream health from the gallery, and a live event log. Press fast-forward to run the whole day, then generate the post-event report.</p></div>
</div></section>'''
    return demo_page(page,'demo-analytics.html','Live Event Analytics Dashboard Demo: Attendance Curve, Engagement, Leads | VSE Platform',
      'Try VSE Insight: a live event dashboard with concurrent viewers plotted against the run order, engagement per session, top questions, sponsor performance, stream health and a generated post-event report.',
      'Demo 04 · Insight','The dashboard <span class="em">the producer and the CMO share.</span>',
      'Concurrent viewers against the run order, engagement, leads and sponsor ROI updating live, then a post-event report generated in one click.',body,('platform-insight.html','Insight'))

def demos_index(page):
    body='''<section class="content-sec"><div class="wrap reveal"><div class="pillar-grid">
<a class="pillar-card" href="demo-audience.html"><span class="num">Demo 01 · Engage</span><h3>Live audience participation</h3><p>Phone, broadcast graphic and moderator console side by side with a simulated audience.</p></a>
<a class="pillar-card" href="demo-registration.html"><span class="num">Demo 02 · Register</span><h3>Registration &amp; check-in</h3><p>Tickets, promo codes, confirmation with QR and badge, staff scanner.</p></a>
<a class="pillar-card" href="demo-event-hub.html"><span class="num">Demo 03 · Stage + Connect</span><h3>Attendee event hub</h3><p>Agenda, session room, speakers, expo, networking, on-demand.</p></a>
<a class="pillar-card" href="demo-analytics.html"><span class="num">Demo 04 · Insight</span><h3>Live analytics dashboard</h3><p>Attendance curve vs run order, engagement, leads, sponsors, report.</p></a>
</div><div class="callout" style="margin-top:60px"><p>These demos run entirely in your browser with simulated data, nothing is stored and there\'s no sign-up. Want to see it with your brand and your agenda? <a href="contact.html">Book a guided demo</a>.</p></div></div></section>'''
    return page('demos.html','Interactive Event Platform Demos: Participation, Registration, Event Hub, Analytics | VSE Platform',
      'Four working demos of VSE Platform in your browser: live branded audience participation, registration and QR check-in, the attendee event hub, and the live analytics dashboard. No sign-up.',
      'Demos','See it working, <span class="em">no sign-up.</span>',
      'Four working demos, each one a module of the platform. Switch the brand live on every one.',
      body,crumbs=[('index.html','Home'),('platform.html','Platform'),('demos.html','Demos')])

def register(P, page):
    P['platform.html']=platform_overview(page)
    for m in MODULES: P[m['slug']]=module_page(page,m)
    P['pipeline.html']=pipeline_page(page)
    P['platform-packages.html']=packages_page(page)
    P['platform-features.html']=features_page(page)
    P['demos.html']=demos_index(page)
    P['demo-audience.html']=demo_audience(page)
    P['demo-registration.html']=demo_registration(page)
    P['demo-event-hub.html']=demo_event_hub(page)
    P['demo-analytics.html']=demo_analytics(page)
