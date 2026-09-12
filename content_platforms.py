GUIDES = [
dict(slug='guide-virtual-event-platform.html', pillar='platforms',
 title='Choosing a Virtual Event Platform: The Feature Checklist That Matters | Virtual Studio Events',
 desc='Which virtual event platform features matter — registration, embedded streaming, Q&A, breakouts, analytics, production back-end — which are fluff, the questions to ask vendors, and when you don\'t need a platform at all.',
 h1='Choosing a virtual event platform: <span class="em">what actually matters.</span>', h1_plain='Choosing a virtual event platform: what actually matters',
 lede='Twelve features worth paying for, the ones that are marketing fluff — and when you don\'t need a platform at all.',
 related=['guide-platform-comparison.html','guide-registration-data-gdpr.html','guide-engagement-features.html'],
 body='''
<h2>First: do you need one?</h2>
<p>If your event is one session, one audience, watch-only — you don't need an event platform. A well-produced stream into YouTube, LinkedIn or Teams will reach more people with less friction. Platforms earn their cost when you need registration, multiple sessions, structured interaction or sponsor visibility. Be honest about which of those you actually need before you start demos.</p>
<h2>Features that matter</h2>
<ol><li><strong>Registration that exports clean data</strong> — custom fields, confirmation emails you control, a CSV that doesn't need repairing.</li>
<li><strong>An agenda that handles time zones</strong> and personal schedules.</li>
<li><strong>Reliable embedded streaming</strong> — test it on a corporate network; many block consumer video.</li>
<li><strong>Moderated Q&amp;A with upvoting</strong> and a moderator view that's actually usable live.</li>
<li><strong>Polls whose results can be displayed into the show</strong>, not just inside the platform.</li>
<li><strong>Breakout rooms a producer can open, close and move people between.</strong></li>
<li><strong>Per-session analytics</strong>: who watched what, for how long, exportable.</li>
<li><strong>Branding control</strong> beyond a logo upload — colours, fonts, layouts.</li>
<li><strong>A production back-end your crew can drive</strong>: speaker green rooms, source switching, screen-share management, or clean RTMP/SRT ingest for an external gallery.</li>
<li><strong>Captions and accessibility</strong>: keyboard navigation, screen-reader support, caption display controls.</li>
<li><strong>Single sign-on and access control</strong> for internal events.</li>
<li><strong>On-demand hosting</strong> after the event, with the same analytics.</li></ol>
<h2>Features that are usually fluff</h2>
<p>3D lobbies and avatars (novelty wears off in minutes; accessibility suffers), gamification badges, AI matchmaking on events under a few hundred attendees, virtual exhibition halls nobody visits, and "metaverse" anything. If a demo spends its first ten minutes on these, ask to see the moderator's Q&amp;A view instead.</p>
<h2>Questions to ask any vendor</h2>
<ul><li>What happens when a viewer's connection drops — does the player recover on its own?</li><li>What's the real concurrency limit, with proof from a past event?</li><li>Can we get every piece of attendee data out afterwards, in full?</li><li>What does support look like <em>during</em> the live event — a human on a channel, or a ticket queue?</li><li>Where is data stored and processed (see <a href="guide-registration-data-gdpr.html">GDPR</a>)?</li><li>Can an external production gallery send you a broadcast feed, and at what latency?</li></ul>
<h2>Our position</h2>
<p>We're platform-agnostic. We build bespoke event platforms when the brief demands it, and we'll happily run your show into Teams, Zoom or a third-party platform when that's the right answer. The platform is the venue — the show is what we're there for. The <a href="guide-platform-comparison.html">comparison guide</a> puts the common options side by side.</p>
'''),

dict(slug='guide-platform-comparison.html', pillar='platforms',
 title='Teams vs Zoom vs YouTube vs Vimeo vs Dedicated Event Platforms: Which for Your Virtual Event? | Virtual Studio Events',
 desc='An independent comparison of the main ways to deliver a virtual event — Microsoft Teams, Zoom Webinars/Events, YouTube Live, Vimeo, LinkedIn Live and dedicated event platforms — by audience, interaction, control, cost and production fit.',
 h1='Teams, Zoom, YouTube, Vimeo or a dedicated platform? <span class="em">An honest comparison.</span>', h1_plain='Teams, Zoom, YouTube, Vimeo or a dedicated platform? An honest comparison',
 lede='The common delivery options compared by what matters to organisers: who can watch, what they can do, how much control you have, what it costs and how well it plays with a production gallery.',
 related=['guide-virtual-event-platform.html','guide-cdn-players.html','guide-multi-platform-streaming.html'],
 body='''
<p>This is a comparison by <em>category</em>, because specific features change every quarter and vendors' pricing pages are their own. We run shows on all of these, and the right answer depends on your audience and what you need them to do — not on which is "best".</p>
<h2>Microsoft Teams (meetings, webinars, town halls)</h2>
<p><strong>Best for:</strong> internal corporate events where everyone already lives in Microsoft 365. <strong>Strengths:</strong> zero friction for staff; SSO; attendance reporting; town-hall mode scales to large internal audiences. <strong>Limits:</strong> the look is Teams; production control is limited unless you bring an external broadcast feed in; external audiences find it clunky. <strong>Production fit:</strong> good when a gallery feeds a broadcast-quality programme into it as a single source.</p>
<h2>Zoom (webinars and events)</h2>
<p><strong>Best for:</strong> mixed internal/external audiences that need reliable interaction. <strong>Strengths:</strong> everyone knows how to use it; strong Q&amp;A and polls; breakout rooms; decent analytics. <strong>Limits:</strong> branding is basic; the "webinar look" is hard to shake; large-scale streaming is via its own player or simulcast out. <strong>Production fit:</strong> good — a gallery can inject a produced feed, or pull participants out as isolated sources.</p>
<h2>YouTube Live</h2>
<p><strong>Best for:</strong> public reach, discoverability and free hosting of the on-demand version. <strong>Strengths:</strong> unlimited scale; excellent player on every device; free; automatic captions. <strong>Limits:</strong> no registration; minimal interaction beyond chat; blocked on many corporate networks; ads and recommendations you don't control; rights enforcement on music. <strong>Production fit:</strong> excellent — it's built to receive a broadcast feed.</p>
<h2>Vimeo (and similar professional video hosts)</h2>
<p><strong>Best for:</strong> branded, ad-free public or semi-private streams on your own website. <strong>Strengths:</strong> clean embeddable player; privacy controls; good on-demand tooling; reliable. <strong>Limits:</strong> interaction is light; registration needs another tool; costs scale with tier. <strong>Production fit:</strong> excellent.</p>
<h2>LinkedIn Live</h2>
<p><strong>Best for:</strong> B2B thought-leadership events where the audience is already scrolling. <strong>Strengths:</strong> reach into the professional network; comments as a social signal. <strong>Limits:</strong> needs eligibility and scheduling; little control; not a place for a four-hour conference. <strong>Production fit:</strong> good as a simulcast destination, rarely as the primary.</p>
<h2>Dedicated event platforms</h2>
<p><strong>Best for:</strong> multi-session conferences, events with sponsors, and anything needing registration, agendas, networking and detailed analytics in one place. <strong>Strengths:</strong> everything in one branded environment; the data model is built around events. <strong>Limits:</strong> cost; attendees have to learn a new interface; quality varies enormously between vendors; some have weak streaming under the hood. <strong>Production fit:</strong> varies — check they accept an external broadcast feed at decent latency.</p>
<h2>Side by side</h2>
<table><tr><th></th><th>Teams</th><th>Zoom</th><th>YouTube</th><th>Vimeo</th><th>LinkedIn</th><th>Dedicated</th></tr>
<tr><td>Audience</td><td>Internal</td><td>Mixed</td><td>Public</td><td>Public/private</td><td>Public B2B</td><td>Registered</td></tr>
<tr><td>Registration</td><td>Basic</td><td>Good</td><td>None</td><td>Add-on</td><td>None</td><td>Strong</td></tr>
<tr><td>Interaction</td><td>Good</td><td>Strong</td><td>Chat</td><td>Light</td><td>Comments</td><td>Strong</td></tr>
<tr><td>Branding</td><td>Low</td><td>Low–med</td><td>Low</td><td>High</td><td>Low</td><td>High</td></tr>
<tr><td>Scale</td><td>Large</td><td>Large</td><td>Unlimited</td><td>Large</td><td>Large</td><td>Varies</td></tr>
<tr><td>Corporate network risk</td><td>Low</td><td>Low</td><td>High</td><td>Med</td><td>Med</td><td>Varies</td></tr>
<tr><td>Cost</td><td>Included</td><td>£–££</td><td>Free</td><td>££</td><td>Free</td><td>£££</td></tr></table>
<h2>How we'd decide</h2>
<p>Internal all-hands: Teams, with a produced feed. Public thought-leadership: a produced stream to LinkedIn and YouTube simultaneously. Customer conference with sponsors and tracks: a dedicated platform, chosen with the <a href="guide-virtual-event-platform.html">feature checklist</a>, fed by an external gallery. Branded launch on your own site: Vimeo-class embed. And in every case, a <a href="guide-cdn-players.html">standby destination</a> ready in case the primary fails.</p>
'''),

dict(slug='guide-registration-data-gdpr.html', pillar='platforms',
 title='Virtual Event Registration, Attendee Data & GDPR: A Practical Guide | Virtual Studio Events',
 desc='Designing virtual event registration that converts, what attendee data to collect and why, consent and privacy notices, data processors and international transfers, recordings, and deleting data afterwards.',
 h1='Registration and data: <span class="em">collect less, use it better.</span>', h1_plain='Registration and data: collect less, use it better',
 lede='Registration flows that don\'t lose people, the attendee data that\'s worth having, and the GDPR questions organisers should be able to answer before a platform goes live.',
 related=['guide-virtual-event-platform.html','guide-event-metrics.html','guide-post-event-report.html'],
 body='''
<p>Registration is the first thing your audience experiences and the last thing most organisers design. It's also where personal data enters the system, which makes it the point where privacy obligations start. This guide covers both — the conversion and the compliance — in practical terms. It's general information from a production team, not legal advice.</p>
<h2>Registration that converts</h2>
<p>Every extra field loses registrants. Ask for what you'll actually use: name, email, organisation, and one or two questions that shape the event (role, topic of interest). Put the rest in a post-event survey. Confirm instantly by email with a calendar file, the join link, and what to expect. Send reminders the day before and an hour before; the hour-before email is the single biggest driver of attendance.</p>
<h2>Data you'll want afterwards</h2>
<p>Registered vs attended (the no-show rate tells you about your reminders); session-level attendance and watch time; questions asked and polls answered (with names, if consented); on-demand views in the following weeks. Make sure the platform can export all of it, per attendee, before you sign — see the <a href="guide-virtual-event-platform.html">feature checklist</a>.</p>
<h2>The GDPR basics for an event</h2>
<p><strong>Lawful basis.</strong> Running the event someone registered for is usually covered by contract or legitimate interests; using their details for marketing afterwards generally needs consent (a clearly labelled, unticked box) or a documented legitimate-interests assessment for existing customers. Don't bury marketing consent in the registration terms.</p>
<p><strong>Privacy notice.</strong> Link to it at registration. It should say what you collect, why, who processes it (the platform, the production company, the CRM), how long you keep it and how to opt out.</p>
<p><strong>Processors.</strong> The platform and any production partner handling attendee data are processors; you need a data-processing agreement with each. Ask where they store data and whether it leaves the UK/EEA — many platforms are US-hosted and rely on transfer mechanisms you should at least know the name of.</p>
<p><strong>Recordings.</strong> Recording attendees (their video, their questions with names, their chat) is processing personal data. Tell people the session is recorded before they join, and decide whether Q&amp;A on the on-demand version shows names.</p>
<p><strong>Retention.</strong> Decide when registration data is deleted from the platform — after the follow-up campaign, say — and actually delete it. Export what you need to your own systems first.</p>
<h2>Internal events</h2>
<p>Employee events are still personal data, and the attendance report your leadership wants ("who didn't watch the all-hands?") has implications. Be transparent with staff about what's tracked and why.</p>
<h2>A short pre-launch checklist</h2>
<ul><li>Registration form: minimum fields, clear marketing consent, privacy notice linked.</li><li>Processing agreements with platform and production partners in place.</li><li>Data location and transfers understood.</li><li>Recording notice on the join page and at the top of the show.</li><li>Export and deletion plan written down with dates.</li></ul>
<div class="callout"><p>The organisations that handle this well aren't the ones with the longest terms and conditions — they're the ones who collect less and can explain every field.</p></div>
'''),

dict(slug='guide-engagement-features.html', pillar='platforms',
 title='Virtual Event Engagement: Features That Actually Work (And What to Measure) | Virtual Studio Events',
 desc='Which engagement features move the numbers at virtual events — Q&A, polls, chat, reactions, breakouts, networking, gamification — with the production requirements and the metrics to judge each one.',
 h1='Engagement features: <span class="em">what works, what\'s theatre.</span>', h1_plain='Engagement features: what works, what\'s theatre',
 lede='Every platform sells "engagement". Here\'s which features actually change how long people watch and what they do afterwards — and what each one demands from the production.',
 related=['guide-live-interaction.html','guide-event-metrics.html','guide-virtual-event-platform.html'],
 body='''
<p>Engagement isn't a feature; it's a behaviour. The question for each tool is whether it changes what the audience does — watch longer, ask something, come back on demand, follow up — and whether your production can support it properly. Here's our field experience, feature by feature.</p>
<h2>Q&amp;A — works, when staffed</h2>
<p>The highest-value feature on every platform. Watch time rises measurably when the audience believes questions will be answered. It needs a moderator and a workflow (<a href="guide-live-interaction.html">how to run it</a>). Measure: questions submitted per 100 attendees, share answered on air, and watch time of askers vs non-askers.</p>
<h2>Polls — work, with latency handled</h2>
<p>A well-timed poll re-engages a drifting audience and produces content for the presenter. Badly timed (closed before the delayed stream shows it) it frustrates. Two or three per hour, results shown on screen. Measure: response rate per poll; drop-off before vs after.</p>
<h2>Reactions and emoji — cheap and real</h2>
<p>Low effort, genuinely liked, and a live signal for presenters that someone is out there. Surface them on screen occasionally. Measure: reactions per minute as a proxy for attention.</p>
<h2>Chat — works for community, not for information</h2>
<p>Great with a host in it; noise without one. Keep questions out of it. Measure: active participants (not messages), and whether practical problems get solved there.</p>
<h2>Breakout rooms — work for small groups with a purpose</h2>
<p>Workshops, training, roundtables: yes, with a facilitator per room and a task. "Networking breakouts" with strangers and no structure: people leave. Measure: room occupancy over time (do they stay?), and post-event feedback.</p>
<h2>Networking and matchmaking — rarely works</h2>
<p>Below several hundred attendees, the pool is too small; above it, the platforms' matchmaking is usually shallow. Where it works it's tightly facilitated: pre-booked meetings, speed-networking with a host. Measure: meetings actually completed, not "connections made".</p>
<h2>Gamification — theatre, mostly</h2>
<p>Points for visiting sponsor booths produce booth visits and nothing else. It can work for internal training with a real prize. Measure: whether the behaviour persists when the points stop.</p>
<h2>Downloads and resources — under-used</h2>
<p>Slides, a one-page summary, a template — offered on screen at the right moment — drive follow-up more than any interactive widget. Measure: downloads per attendee.</p>
<h2>What we'd build for a typical corporate event</h2>
<p>Moderated Q&amp;A with on-screen questions; two or three polls per hour with results on screen; reactions surfaced by the presenter; a hosted chat; resources offered at the end of each session; and no gamification. Production requirements: a moderator, poll graphics in the run order, and presenters briefed to acknowledge the online audience by name. Then measure it properly — the <a href="guide-event-metrics.html">metrics guide</a> shows how.</p>
'''),
]
