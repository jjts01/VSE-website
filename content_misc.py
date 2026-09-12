FAQS = [
 ("What's the difference between a virtual and a hybrid event?","A virtual event happens entirely online. Speakers and audience all join remotely. A hybrid event has a physical room with a live audience and an online audience watching the same show, with both able to take part."),
 ("How far in advance should we book production?","For a straightforward stream, two weeks is comfortable. For a multi-day hybrid conference, six to eight weeks gives time for platform builds, rehearsals and proper redundancy planning."),
 ("How much does a virtual event cost?","A produced webinar starts around £750+VAT; a single-room town hall or conference £2,000–£5,000; a hybrid conference or awards show £5,000–£15,000+. Our <a href=\"guide-live-streaming-cost.html\">cost guide</a> and <a href=\"tools.html#budget\">budget estimator</a> give a tailored range."),
 ("Can you work with our existing AV supplier or venue?","Yes. Much of our work is alongside other suppliers and in-house teams. We slot in for the streaming, vision or platform layer, or take the whole technical delivery."),
 ("Which virtual event platform should we use?","It depends on your audience and what they need to do. Internal events usually belong in Teams; public reach on YouTube and LinkedIn; multi-track conferences on a dedicated platform. Our <a href=\"guide-platform-comparison.html\">comparison guide</a> walks through it."),
 ("What internet connection does a live stream need?","A dedicated wired connection with sustained upload of at least twice your total stream bitrate (typically 10–12 Mbps for one 1080p stream) plus a bonded cellular backup. Venue Wi-Fi is never the primary path."),
 ("Do you travel outside the UK?","Yes. We're UK-based with a studio in Chichester and partners nationwide, and we deliver shows across Europe and worldwide, or run them remotely from our cloud galleries."),
 ("Do you work white-label for other production companies?","Yes. A large share of our work is crew, engineering and cloud galleries delivered under other agencies' names. Ask about trade rates."),
]

GLOSSARY = [
 ("Adaptive bitrate (ABR)","Delivery technique where the platform makes several quality versions of a stream and the viewer's player switches between them as their connection changes."),
 ("Audio split","A copy of each microphone or a clean mix taken from the room's sound desk and delivered to the stream mixer, so the stream gets its own balance rather than the PA feed."),
 ("Bitrate","The amount of data per second in a stream, usually in megabits per second (Mbps). Higher means better quality and more bandwidth needed."),
 ("Bonded cellular","An encoder that combines several 4G/5G SIMs into one reliable connection; the standard backup (or field primary) path for live streaming."),
 ("Breakout room","A smaller virtual session split off from the main event for workshops or discussion, controlled by a producer or host."),
 ("Bug","A small persistent on-screen logo, usually in a corner of the frame."),
 ("Captions (live/closed)","Text of the spoken audio displayed on screen, generated live by a human captioner or automated speech recognition, and correctable afterwards for on-demand."),
 ("CBR / VBR","Constant vs variable bitrate. CBR is predictable for networks and preferred for live encoding; VBR saves data for recordings."),
 ("CDN","Content delivery network: the distributed servers that copy a stream around the world so each viewer fetches it from somewhere nearby."),
 ("Chroma key","Replacing a green or blue backdrop with another image in the vision mixer; 'green screen'."),
 ("Cloud gallery","A production gallery running on virtual machines in a data centre (we use AWS), operated remotely, with sources arriving over the internet."),
 ("Comms / talkback","The intercom system crew use to talk during a show, usually split into production, technical and floor channels."),
 ("Confidence monitor","A screen positioned for the presenter showing their slides, notes or the programme, out of the camera's view."),
 ("Contribution","Getting a source (a remote speaker, a second venue) into the production, as opposed to distribution which is getting the programme out to viewers."),
 ("Cyclorama (cyc)","A seamless curved backdrop, usually white, that can be lit any colour and gives a clean infinite background on camera."),
 ("Dante","A standard for carrying many channels of audio over an ordinary network cable; common for audio splits between desks."),
 ("Dress rehearsal","A full run of the show in real time with presenters, following the run order, typically the day before or the morning of the event."),
 ("Encoder","Hardware or software that compresses the programme picture and sound into a stream for the internet."),
 ("Failover","Automatic switching to a backup path (second connection, second encoder) when the primary fails."),
 ("Floor manager","The crew member in the room who cues presenters and relays between the stage and the gallery."),
 ("Frame rate","Frames per second in the video; 25 or 30 for presentations, 50 or 60 for fast motion."),
 ("Gallery","The production control room, physical or cloud, where the show is mixed, called and encoded."),
 ("Green room","A holding area (physical or virtual) where speakers wait, are tested and briefed before going on."),
 ("H.264 / HEVC","Video compression standards. H.264 is universal; HEVC (H.265) gives better quality per megabit but isn't supported everywhere."),
 ("HLS","HTTP Live Streaming. The most common delivery format, splitting the stream into small chunks; standard latency 15–45 seconds, low-latency variants a few seconds."),
 ("Holding slide / loop","A branded graphic (often with music and a countdown) shown before the show, in breaks and during technical problems so the screen is never black."),
 ("Hybrid event","An event with both an in-room audience and an online audience watching and taking part in the same show."),
 ("ISO recording","An isolated recording of a single source (one camera, one remote guest) separate from the mixed programme, used for re-editing."),
 ("Keyframe interval","How often the encoder sends a full frame rather than changes; platforms typically require every 2 seconds."),
 ("Latency","The delay between something happening live and the viewer seeing it; from under a second (WebRTC) to 45 seconds (standard HLS)."),
 ("LED wall","A backdrop made of LED panels displaying live content behind presenters, used instead of a physical set or green screen."),
 ("Line check","A quick test of every source and route before the show, without performing."),
 ("Lower third","A graphic in the lower part of the frame giving a speaker's name and role; also called a name strap or super."),
 ("Mix-minus","A return audio feed for a remote contributor that contains everything except their own voice, preventing echo."),
 ("Moiré","Shimmering patterns on camera caused by fine stripes or checks in clothing or set, or by LED pixel pitch interacting with the sensor."),
 ("NDI","Network Device Interface: a standard for sending high-quality video between devices over an ordinary local network."),
 ("PA feed","Audio taken from the room's public-address mix; usually unsuitable for a stream because it's equalised for the room and carries reverberation."),
 ("Playback","Pre-recorded video or audio played into the show on cue, typically from the production system."),
 ("Programme (PGM)","The final mixed output of the show. The pictures and sound the audience sees."),
 ("Redundancy","Duplicate paths and kit (encoders, connections, power) so a single failure doesn't take the show off air."),
 ("Restreaming","Sending one stream to a cloud service that fans it out to several platforms at once (simulcast)."),
 ("RTMP","An older protocol for sending streams to platforms; universally supported but handles packet loss poorly."),
 ("Run order","The minute-by-minute document listing every item in the show with its source, audio, graphics, presenter and timing; the crew's script."),
 ("Safe area","The part of the frame guaranteed to be visible on every device; graphics are kept inside it."),
 ("Show caller","The person (usually the producer) who reads the run order and gives the cues on comms."),
 ("Simulcast","Streaming the same show to several platforms simultaneously."),
 ("SRT","Secure Reliable Transport: a modern streaming protocol that recovers lost packets and encrypts by default; preferred for contribution links."),
 ("Standby","The warning call given before a cue ('standby VT'); the cue itself is executed on 'go'."),
 ("Sting","A short animated graphic with sound used to open a show or bridge between segments."),
 ("Tech run","A rehearsal of every technical path (sources, routes, stream), without presenters performing."),
 ("Teleprompter","A display in front of the lens showing the script, letting the presenter read while looking at the camera."),
 ("Town hall","An all-staff meeting or leadership broadcast, typically internal, with Q&A."),
 ("Transcoding","Converting a stream into other resolutions and bitrates (the ABR ladder), done by the platform."),
 ("UPS","Uninterruptible power supply: a battery that keeps critical kit running through a power cut."),
 ("vMix","Production software that combines vision mixing, playback, graphics, remote calling and encoding on one machine; our house system."),
 ("vMix Call","vMix's browser-based broadcast calling for remote guests, with individual audio control and a programme return."),
 ("Vision mixer","The person (or device) that switches between cameras and sources to make the programme."),
 ("VT","Short for videotape; in practice any pre-recorded video item played into the show."),
 ("WebRTC","A real-time video technology with sub-second latency, used for two-way interaction and some low-latency players."),
 ("White label","Production delivered under another company's name; a large part of the trade side of the events industry."),
]

NEWS = [
 dict(date='September 2026 · Pricing briefing', title='What virtual and hybrid events actually cost in 2026: the benchmark',
  body='We re-benchmarked our pricing against every published UK rate card and platform pricing guide we could find. Production: single-camera streams from £499–£1,000 a day, multi-camera business productions £895–£3,500, hybrid conferences £5,000–£15,000, multi-stage broadcast events £15,000–£50,000+, specialist crew £450–£750 a day. Platforms: self-serve tools £1k–£5k a year, mid-market platforms $10k–$50k per event or year, enterprise suites $25k–$500k+. Our <a href="guide-live-streaming-cost.html">cost guide</a> now carries the full comparison with sources, and our <a href="platform-packages.html">packages</a> have been repriced against it, including platform-only and participation-only licences for agencies.',
  src=[('Concept LIVE (live streaming cost UK','https://conceptlive.co.uk/live-streaming-cost'),('Gass Productions) hybrid event cost UK','https://gassproductions.co.uk/hybrid-event-cost-uk/'),('Life Inside (platform comparison 2026','https://www.lifeinside.io/insights/virtual-event-platform-comparison'),('Vendr), ON24 pricing','https://www.vendr.com/marketplace/on24')]),
 dict(date='September 2026 · Industry briefing', title='The virtual events market has more than kept its pandemic gains, and it\'s still growing',
  body='Industry estimates put the global virtual events market at roughly $237bn in 2025, up from around $194bn in 2024, with forecasts of it more than doubling by 2029, while a Zoom survey found roughly 37% of event budgets now go to virtual and hybrid formats. For organisers the message is that virtual and hybrid are permanent line items rather than a pandemic workaround, and that budget scrutiny is rising accordingly, which is why we\'ve published our <a href="guide-measuring-roi.html">ROI model</a> and <a href="guide-live-streaming-cost.html">honest cost guide</a>.',
  src=[('Digital Samba (The Future of Virtual Events','https://www.digitalsamba.com/blog/the-future-of-virtual-events'),('Technologies4you), Hybrid events in 2026','https://technologies4you.com/hybrid-events-in-2026-emerging-trends-and-how-virtual-platforms-are-adapting/')]),
 dict(date='September 2026 · Industry briefing', title='AI is arriving in the gallery: auto-tracking cameras, live captions and automated highlight clipping',
  body='Production briefs in 2026 are increasingly asking for AI-assisted production. PTZ cameras that track presenters, real-time captioning, and automated clipping that produces social cuts within hours of a live event. Alongside shoppable or interactive overlays on the stream. Our view from the gallery: auto-clipping and captioning are genuinely useful and we use them; auto-tracking cameras still need a human watching the framing. See our guides on <a href="guide-on-demand-repurposing.html">same-day content</a> and <a href="guide-accessibility.html">captioning</a>.',
  src=[('GASS Productions (Virtual & hybrid event trends 2026','https://gassproductions.co.uk/hybrid-virtual-events-2025-trends/'),('Verbit), 5 event technology trends','https://verbit.ai/resources/5-event-technology-trends-reshaping-events/')]),
 dict(date='September 2026 · Industry briefing', title='Accessibility is now a baseline requirement, not an add-on',
  body='Multilingual captioning, screen-reader compatibility and responsive design are being treated as baseline requirements across the industry in 2026 rather than optional extras, driven by procurement expectations and regulation. If your production supplier can\'t talk fluently about live captions, BSL on stream and accessible platforms, that\'s now a gap. Our <a href="guide-accessibility.html">accessibility guide</a> covers what good looks like and what it costs.',
  src=[('Eventplanner.net: Event industry trends for 2026','https://www.eventplanner.net/news/11089_event-industry-trends-for-2026-a-bold-new-era-of-innovation-and-impact.html')]),
 dict(date='September 2026 · Industry briefing', title='Event professionals are the most optimistic they\'ve been in five years',
  body='A recent global survey found 85% of event professionals optimistic about the industry\'s prospects in 2026 (the highest reading in five years) with the wider events industry projected to reach $1.55 trillion by 2028 on the back of event technology and hybrid formats. The strategic shift being described is towards software as the operational backbone of events rather than a marketing gimmick: organisation over novelty. That matches what we see in briefs: fewer 3D lobbies, more questions about <a href="guide-registration-data-gdpr.html">registration data</a> and <a href="guide-event-metrics.html">measurement</a>.',
  src=[('Eventplanner.net: Event industry trends for 2026','https://www.eventplanner.net/news/11089_event-industry-trends-for-2026-a-bold-new-era-of-innovation-and-impact.html'),('Cadmium: Event technology trends','https://www.gocadmium.com/resources/event-technology-what-are-the-top-trends-in-2025')]),
 dict(date='September 2026 · From the studio', title='New website and knowledge hub launched',
  body='We\'ve rebuilt virtualstudio.events from the ground up and published our production knowledge base: 32 guides across pre-production, streaming infrastructure, set design, live production, platforms and analytics, plus free tools, templates and a glossary. It\'s the material we hand to clients before every show, now open to everyone. Start at the <a href="resources.html">resources hub</a>.', src=[]),
]

TOOLS_BODY = '''
<section class="content-sec"><div class="wrap reveal">
<span class="eyebrow">Tool 01</span><h2 class="big" id="bandwidth">Streaming bandwidth calculator</h2>
<p class="prose" style="margin-top:14px">Work out the sustained upload speed your venue line actually needs, including headroom and a backup path. Based on the <a href="guide-encoders-bitrates.html" style="color:var(--accent2)">encoder settings we use</a>.</p>
<div class="tool" id="bwtool">
<div class="grid2">
<div><label for="bw-quality">Stream quality</label><select id="bw-quality"><option value="2.5">720p · talking heads (2.5 Mbps)</option><option value="4">720p · motion (4 Mbps)</option><option value="5" selected>1080p · talking heads / slides (5 Mbps)</option><option value="8">1080p · motion-heavy (8 Mbps)</option><option value="16">4K (16 Mbps, rarely worth it)</option></select></div>
<div><label for="bw-streams">Number of simultaneous outputs</label><input type="number" id="bw-streams" min="1" max="10" value="1"><div class="note">Each destination streamed directly counts as one. A restreamer counts as one total.</div></div>
<div><label for="bw-backup">Backup stream to a standby destination?</label><select id="bw-backup"><option value="1" selected>Yes (recommended)</option><option value="0">No</option></select></div>
<div><label for="bw-remote">Remote contributors joining (download)</label><input type="number" id="bw-remote" min="0" max="30" value="2"></div>
<div><label for="bw-other">Other traffic on the same line</label><select id="bw-other"><option value="0" selected>None, dedicated line</option><option value="10">Light (a few laptops)</option><option value="30">Heavy (shared with guests)</option></select></div>
</div>
<div class="result"><b id="bw-result">—</b><span id="bw-detail"></span></div>
<div class="note">Headroom of 2× is applied to the encode total because encoder output fluctuates and lines rarely deliver their headline speed. Test the line from the gallery position, wired, at the time of day of the event. Read the <a href="guide-internet-connectivity.html" style="color:var(--accent2)">connectivity guide</a>.</div>
</div>

<div style="margin-top:110px"><span class="eyebrow">Tool 02</span><h2 class="big" id="budget">Virtual event budget estimator</h2>
<p class="prose" style="margin-top:14px">A realistic UK production budget range for 2026, built from the day rates and packages in our <a href="guide-live-streaming-cost.html" style="color:var(--accent2)">cost guide</a>. Excludes VAT, venue hire and catering.</p>
<div class="tool" id="budgettool">
<div class="grid2">
<div><label for="b-format">Event format</label><select id="b-format"><option value="webinar">Webinar / single presenter</option><option value="townhall" selected>Town hall / single-room conference</option><option value="hybrid">Hybrid conference (room + stream)</option><option value="awards">Awards show</option><option value="launch">Product launch / keynote</option><option value="multi">Multi-track conference</option></select></div>
<div><label for="b-days">Show days</label><input type="number" id="b-days" min="1" max="5" value="1"></div>
<div><label for="b-cams">Cameras</label><input type="range" id="b-cams" min="1" max="6" value="2"><div class="note">Cameras: <span id="b-cams-v">2</span></div></div>
<div><label for="b-remote">Remote speakers</label><input type="range" id="b-remote" min="0" max="20" value="3"><div class="note">Speakers: <span id="b-remote-v">3</span></div></div>
<div><label for="b-platform">Platform</label><select id="b-platform"><option value="0">Existing (Teams/Zoom/YouTube)</option><option value="2500" selected>VSE Platform per-event licence</option><option value="4000">Third-party mid-market platform (typical per-event)</option><option value="8000">Bespoke branded platform build</option></select></div>
<div><label for="b-studio">Location</label><select id="b-studio"><option value="studio" selected>Our studio (Chichester / partner)</option><option value="venue">Your venue / office</option><option value="cloud">Fully remote (cloud gallery)</option></select></div>
<div><label for="b-extras">Extras</label>
<div class="note" style="margin-top:0"><label style="display:inline;text-transform:none;letter-spacing:0;font-size:.95rem"><input type="checkbox" id="b-captions"> Human live captions</label><br><label style="display:inline;text-transform:none;letter-spacing:0;font-size:.95rem"><input type="checkbox" id="b-rehearsal" checked> Rehearsal day</label><br><label style="display:inline;text-transform:none;letter-spacing:0;font-size:.95rem"><input type="checkbox" id="b-edit" checked> Highlights &amp; on-demand edit</label><br><label style="display:inline;text-transform:none;letter-spacing:0;font-size:.95rem"><input type="checkbox" id="b-led"> LED wall</label></div></div>
</div>
<div class="result"><b id="b-result">—</b><span id="b-detail"></span></div>
<table id="b-table"></table>
<div class="note">Indicative only: every event is quoted individually. Trade and white-label rates for production companies differ. <a href="contact.html" style="color:var(--accent2)">Send us the brief</a> for a real number within a working day.</div>
</div></div>
</div></section>
'''

TEMPLATES_BODY = '''
<section class="content-sec"><div class="wrap reveal">
<span class="eyebrow">Template 01</span><h2 class="big" id="run-order">Live event run order</h2>
<p class="prose" style="margin-top:14px">The layout we use in the gallery. Download it as a CSV (opens in Excel or Google Sheets), then read <a href="guide-run-order.html" style="color:var(--accent2)">how to write one properly</a>.</p>
<div class="tool">
<table><tr><th>#</th><th>Time</th><th>Dur</th><th>Item</th><th>Source</th><th>Audio</th><th>Graphics</th><th>On</th><th>Notes</th></tr>
<tr><td>1</td><td>08:00</td><td>60</td><td>Crew call, tech run</td><td>All</td><td>All routes</td><td>Load pack</td><td>Crew</td><td>Test stream to private</td></tr>
<tr><td>2</td><td>09:30</td><td>30</td><td>Holding loop live, line checks</td><td>Holding</td><td>Music bed</td><td>Countdown</td><td>Remote speakers</td><td>Green room</td></tr>
<tr><td>3</td><td>10:00</td><td>0:10</td><td>Opening sting</td><td>Playback</td><td>Embedded</td><td>Sting</td><td>—</td><td>Mics down</td></tr>
<tr><td>4</td><td>10:00</td><td>3</td><td>Welcome</td><td>Cam 1</td><td>Lav 1</td><td>LT: Host</td><td>Host</td><td>Address lens</td></tr>
<tr><td>5</td><td>10:03</td><td>20</td><td>CEO keynote</td><td>Cam 2 / slides</td><td>Lav 2</td><td>LT: CEO, slides</td><td>CEO</td><td>Prompter · FIXED</td></tr>
<tr><td>6</td><td>10:23</td><td>2</td><td>Poll 1 launch</td><td>Cam 1</td><td>Lav 1</td><td>Poll overlay</td><td>Host</td><td>90s window</td></tr>
<tr><td>7</td><td>10:25</td><td>15</td><td>Remote panel</td><td>Call 1–3</td><td>Callers, mix-minus</td><td>LTs ×3</td><td>Panel</td><td>Flexible −5</td></tr>
<tr><td>8</td><td>10:40</td><td>10</td><td>Q&amp;A</td><td>Cam 1 + Q graphic</td><td>Lav 1</td><td>Question straps</td><td>Host, moderator</td><td>Buffer</td></tr>
<tr><td>9</td><td>10:50</td><td>1</td><td>Close &amp; next steps</td><td>Cam 1</td><td>Lav 1</td><td>Closing slide</td><td>Host</td><td>—</td></tr>
<tr><td>10</td><td>10:51</td><td> (</td><td>Stream stop, save recordings</td><td>), </td><td>—</td><td>—</td><td>Crew</td><td>Confirm ISO saved</td></tr></table>
<div style="margin-top:20px"><button class="cta-btn" id="dl-runorder" type="button">Download run order (CSV)</button></div>
</div>

<div style="margin-top:110px"><span class="eyebrow">Template 02</span><h2 class="big" id="tech-spec">Technical specification for venues and suppliers</h2>
<p class="prose" style="margin-top:14px">Send this to the venue and any AV supplier eight weeks out. If every line has an answer, show day is calm.</p>
<div class="tool"><div class="guide-body">
<h3>Connectivity</h3><ul><li>Wired Ethernet at gallery position; sustained upload ___ Mbps (tested date ___)</li><li>Dedicated VLAN / separate from guest Wi-Fi: Y / N</li><li>Outbound ports open: 1935 (RTMP), 443, SRT/UDP range ___</li><li>Bonded cellular tested in room: Y / N, signal ___</li></ul>
<h3>Audio</h3><ul><li>Audio split: per-mic / clean mix, connector ___, pre/post fader</li><li>Stream mix engineer position and desk</li><li>Mix-minus returns for remote contributors: ___</li><li>Radio mic frequencies and battery plan</li></ul>
<h3>Vision</h3><ul><li>Cameras (number, positions, manned/robotic) ___</li><li>Clean slide feed to gallery: source ___</li><li>Room screen feeds vs stream programme: separate? Y / N</li><li>LED / screen refresh rate and brightness for camera ___</li></ul>
<h3>Power &amp; space</h3><ul><li>Gallery position (m²), power circuits, UPS on critical kit</li><li>Cable routes and load-in times</li></ul>
<h3>People</h3><ul><li>Single technical point of contact: ___</li><li>Venue AV lead: ___ · Platform lead: ___ · Streaming lead: ___</li><li>Rehearsal window: ___</li></ul></div>
<div style="margin-top:20px"><button class="cta-btn" id="dl-techspec" type="button">Download tech spec (text)</button></div></div></div>

<div style="margin-top:110px"><span class="eyebrow">Template 03</span><h2 class="big" id="report">Post-event report structure</h2>
<p class="prose" style="margin-top:14px">The one-page-then-evidence structure from our <a href="guide-post-event-report.html" style="color:var(--accent2)">report guide</a>, with the metrics table pre-built.</p>
<div class="tool"><div class="guide-body">
<h3>Page 1: Summary</h3><p>Objective · Result vs target · What worked (3) · What didn't (3) · Recommendation and decisions needed</p>
<h3>Results against targets</h3>
<table><tr><th>Metric</th><th>Target</th><th>Actual</th><th>Last event</th></tr><tr><td>Registered / attended / rate</td><td></td><td></td><td></td></tr><tr><td>Peak concurrent</td><td></td><td></td><td></td></tr><tr><td>Average watch time</td><td></td><td></td><td></td></tr><tr><td>Completion %</td><td></td><td></td><td></td></tr><tr><td>Questions per 100 attendees</td><td></td><td></td><td></td></tr><tr><td>Poll response rate</td><td></td><td></td><td></td></tr><tr><td>On-demand views (30 days)</td><td></td><td></td><td></td></tr><tr><td>Outcome metric (leads / pulse / completions)</td><td></td><td></td><td></td></tr></table>
<h3>Attendance curve</h3><p>Concurrent viewers over time, annotated with the run order.</p>
<h3>Audience feedback · Technical notes · Costs &amp; ROI · Content &amp; follow-up · Recommendations (owner, date)</h3></div>
<div style="margin-top:20px"><button class="cta-btn" id="dl-report" type="button">Download report template (text)</button></div></div></div>
</div></section>
'''
