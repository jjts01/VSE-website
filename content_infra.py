GUIDES = [
dict(slug='guide-internet-connectivity.html', pillar='infrastructure',
 title='Internet for Live Streaming Events: Bandwidth, Bonding & Backup Explained | Virtual Studio Events',
 desc='How much upload bandwidth a live stream needs, why venue Wi-Fi fails, wired vs bonded cellular, how to test a line, and the redundancy setup broadcast crews use.',
 h1='Connectivity: <span class="em">the stream is only as good as the line.</span>', h1_plain='Connectivity: the stream is only as good as the line',
 lede='How much bandwidth you really need, why "the venue has fast Wi-Fi" is the most dangerous sentence in events, and how professionals build a connection that doesn\'t drop.',
 related=['guide-encoders-bitrates.html','guide-risk-redundancy.html','guide-cloud-production.html'],
 body='''
<p>Every live stream is a river of data leaving the building, and it only takes one narrow point for the whole thing to stutter. This guide explains what the stream needs, how to find out what the venue can actually give you, and how to build a connection with no single point of failure.</p>
<h2>How much upload do you need?</h2>
<p>Streaming is about <strong>upload</strong>, the direction most connections are weakest in. A 1080p stream at a typical 5–6 Mbps needs a stable line with headroom of roughly twice that (10–12 Mbps of <em>consistent</em> upload) because the encoder's output fluctuates and other traffic on the line competes. Add a second destination or a backup stream and it doubles. Remote contributors coming <em>in</em> use download, which is usually plentiful. Use our <a href="tools.html">bandwidth calculator</a> for a number that includes headroom.</p>
<h2>Why venue Wi-Fi fails</h2>
<p>Wi-Fi shares a radio channel with every phone in the room. The connection that tested at 80 Mbps at 8 a.m. in an empty hall is fighting 400 devices by 10 a.m. Guest networks also commonly throttle per device, block the ports and protocols streaming uses, and drop sessions after a fixed time. Wi-Fi is fine for a laptop reading email; it is never the primary path for a stream that matters.</p>
<h2>Wired, dedicated, tested</h2>
<p>The professional standard is a <strong>wired Ethernet connection dedicated to the stream</strong>, ideally on its own VLAN or physical circuit separate from the venue's guest and office traffic. Ask the venue three questions: what's the upload speed on a wired port near the gallery position? Is it shared with guest Wi-Fi? Can they confirm outbound ports 1935 (RTMP), 443 and the SRT/UDP ranges are open? Then <strong>test it from the actual gallery position</strong>, at the time of day the event happens, with the encoder you'll use. A speed test from the venue manager's office at 3 p.m. on a Tuesday tells you nothing.</p>
<h2>Bonded cellular: the second path</h2>
<p>A bonded cellular encoder (LiveU, Teradek and similar) combines several 4G/5G SIMs from different networks into one reliable link. It's how news crews go live from anywhere. For events it's the backup path, and in venues with poor fixed lines, sometimes the primary. Budget a few hundred pounds per job; test it in the room, because basements and steel-framed buildings kill mobile signal.</p>
<h2>Automatic failover</h2>
<p>Having two paths only helps if the switch between them is instant. Modern encoders and bonding units can fail over between wired and cellular automatically, and streaming protocols like SRT tolerate packet loss far better than old RTMP. Ask your production team how failover works on their setup and how long the audience would see a glitch. The right answer is "a second or two, and they probably won't notice".</p>
<h2>Latency and what it means for interaction</h2>
<p>Standard streaming delivers video 15–45 seconds behind real time; low-latency modes get to 3–8 seconds. That delay is fine for a broadcast, awkward for live Q&amp;A (the audience is answering a question you asked half a minute ago) and unusable for two-way conversation. Design your interaction around the latency you'll actually have. Our <a href="guide-cdn-players.html">delivery guide</a> explains the trade-offs.</p>
<h2>The checklist</h2>
<ul><li>Dedicated wired line, tested from the gallery position, at the right time of day.</li><li>Upload at least 2× your total stream bitrate, sustained.</li><li>Ports and protocols confirmed open with venue IT.</li><li>Bonded cellular backup, tested in the room.</li><li>Automatic failover confirmed and rehearsed.</li><li>Remote contributors briefed on <em>their</em> connections.</li></ul>
<div class="callout"><p>If a venue can't answer the questions above, assume the worst and bring your own connectivity.</p></div>
'''),

dict(slug='guide-encoders-bitrates.html', pillar='infrastructure',
 title='Encoders, Bitrates & Resolutions for Live Streaming Explained | Virtual Studio Events',
 desc='What a streaming encoder does, hardware vs software encoders, RTMP vs SRT, choosing bitrate and resolution, keyframes and profiles. The settings broadcast engineers actually use.',
 h1='Encoders and bitrates: <span class="em">the settings that matter.</span>', h1_plain='Encoders and bitrates: the settings that matter',
 lede='What the encoder does, the difference between RTMP and SRT, and the resolution and bitrate choices that decide how your stream looks.',
 related=['guide-internet-connectivity.html','guide-cdn-players.html','guide-cloud-production.html'],
 body='''
<p>The encoder is the box (or software) that takes the finished programme picture and sound and compresses it into a stream the internet can carry. Its settings decide how your event looks on a phone and how likely it is to buffer. Here's what each one does, and what we set.</p>
<h2>Hardware or software?</h2>
<p><strong>Software encoders</strong> (vMix, OBS, Wirecast) run on a production PC and are flexible, cheap and integrated with the vision mix. The same machine can switch cameras, play graphics and encode. <strong>Hardware encoders</strong> (dedicated boxes from Teradek, LiveU, AJA, Blackmagic and others) do one job with great reliability and no operating system updates to worry about. Our standard on anything important: software encoding for the primary programme, a hardware encoder as the independent backup taking the same programme feed.</p>
<h2>RTMP vs SRT</h2>
<p><strong>RTMP</strong> is the veteran protocol most platforms accept. It's simple, but it handles packet loss badly. A dropped packet becomes a stall. <strong>SRT</strong> was built for unreliable networks: it retransmits lost packets within a latency window you set, encrypts by default and copes with jitter. Use SRT wherever the destination supports it, especially for contribution links between sites and into cloud galleries; fall back to RTMP where you must (many social platforms).</p>
<h2>Resolution: 1080p is the default, not 4K</h2>
<p>1080p at 25 or 30 frames per second is the sweet spot for events: sharp on a laptop, efficient on a phone, achievable on ordinary venue lines. 4K quadruples the bitrate for a benefit almost no viewer sees on a stream, and most platforms will downscale it anyway. 720p is a sensible choice when the line is marginal. A stable 720p beats a stuttering 1080p every time. Frame rate: 25 (UK) or 30 fps for presentations; 50/60 only for fast motion like sport.</p>
<h2>Bitrate: enough, with headroom</h2>
<p>Typical settings we use: 1080p at 4.5–6 Mbps for talking heads and slides; up to 8 Mbps for busy, moving content; 720p at 2.5–4 Mbps. Higher isn't better if the line can't sustain it. Use a constant bitrate (CBR) for the live encode (it's predictable for the network) and keep the total of all your streams under half the tested upload.</p>
<h2>Keyframes, profiles and audio</h2>
<p>Set the keyframe interval to 2 seconds (most platforms require it), H.264 High profile, and AAC audio at 128–192 kbps, 48 kHz, stereo. Audio at too low a bitrate is far more noticeable than a slightly softer picture. If your platform supports HEVC (H.265) you gain quality per megabit, but check device compatibility before you rely on it.</p>
<h2>Recording alongside the stream</h2>
<p>Always record the programme locally at a higher quality than the stream (an ISO or programme recording at 20–50 Mbps) so the on-demand version and the highlight edit aren't built from the compressed stream. Record on two devices if the content matters.</p>
<h2>The settings card we tape to the encoder</h2>
<table><tr><th>Setting</th><th>Presentations / talking heads</th><th>Motion-heavy content</th></tr>
<tr><td>Resolution / frame rate</td><td>1920×1080 @ 25</td><td>1920×1080 @ 50</td></tr>
<tr><td>Video bitrate (CBR)</td><td>5 Mbps</td><td>8 Mbps</td></tr>
<tr><td>Keyframe interval</td><td>2 s</td><td>2 s</td></tr>
<tr><td>Profile</td><td>H.264 High</td><td>H.264 High</td></tr>
<tr><td>Audio</td><td>AAC 160 kbps 48 kHz</td><td>AAC 192 kbps 48 kHz</td></tr>
<tr><td>Protocol</td><td>SRT (RTMP fallback)</td><td>SRT (RTMP fallback)</td></tr></table>
'''),

dict(slug='guide-cloud-production.html', pillar='infrastructure',
 title='Cloud Production Galleries: How Remote Live Production on AWS Works | Virtual Studio Events',
 desc='How cloud-based live production works: vMix on AWS, remote operators, contribution links, latency, security, cost versus on-site kit, and when a cloud gallery is the right choice.',
 h1='Cloud galleries: <span class="em">the studio that lives in a data centre.</span>', h1_plain='Cloud galleries: the studio that lives in a data centre',
 lede='How we run entire broadcasts from machines in the cloud, why it costs less than trucking kit around, and when you still want a human in the room.',
 related=['guide-remote-contribution.html','guide-encoders-bitrates.html','guide-live-streaming-cost.html'],
 body='''
<p>Some of the shows we're proudest of had no production kit on site at all. The vision mixing, graphics, playback and encoding happened on powerful virtual machines in an AWS data centre, operated by an engineer at a desk two hundred miles away. This is cloud production, and it's become one of the most cost-effective ways to deliver a professional virtual event.</p>
<h2>What a cloud gallery actually is</h2>
<p>A GPU-equipped virtual machine (we use AWS instances) running production software, vMix in our case, exactly as it would run on a physical production PC. Sources come in over the internet: remote speakers via broadcast-quality calling, on-site cameras via SRT from a small encoder, pre-recorded content uploaded in advance. The operator connects to the machine over a low-latency remote desktop and drives the show. The programme output streams straight out of the data centre to the platform on a connection far faster than any venue line.</p>
<h2>Why it works so well</h2>
<p><strong>The bandwidth problem inverts.</strong> Instead of pushing a heavy programme stream out of a venue, you only need to get individual sources <em>in</em>, and the data centre has effectively unlimited outbound capacity. <strong>Scaling is instant:</strong> a second machine for a second room is a few clicks, not a van. <strong>Crew can be anywhere:</strong> the best operator for your show doesn't need to be within travelling distance. <strong>Cost:</strong> instance hours are cheap compared with hiring, transporting and insuring physical production systems.</p>
<h2>Where the humans are</h2>
<p>Fully virtual events with remote speakers need nobody on site. Hybrid events still need people in the room (camera operators, a sound engineer, a floor manager) but the <em>gallery</em> can be in the cloud, with a compact "contribution kit" (a camera or two, an audio feed and an SRT encoder) sending the room to it. We've run multi-camera hybrid conferences this way with two people on site instead of six.</p>
<h2>Latency and interaction</h2>
<p>Remote desktop control adds a few frames; contribution links add a few hundred milliseconds. For a presenter in the room talking to a remote guest on a screen, the delay is comparable to a good video call and audiences don't notice. Where it matters. A live Q&amp;A with the room. We design the interaction around it, as in any hybrid show.</p>
<h2>Security</h2>
<p>Machines are created for the event and destroyed afterwards. Access is by named user, over encrypted connections, with SRT streams encrypted end to end. No client content persists in the cloud beyond the event unless you ask us to keep it. For regulated clients we document the whole chain.</p>
<h2>When you still want kit on site</h2>
<p>Very large in-room audiences where the room screens are the priority; venues with no usable internet at all (though bonded cellular often solves that); shows with heavy on-site graphics interaction with an LED wall. In those cases the cloud gallery becomes a superb backup path rather than the primary.</p>
<h2>What it costs</h2>
<p>A cloud gallery for a show day typically runs a few hundred pounds in infrastructure plus the operator's day rate, often a third to a half of an equivalent on-site production. Our <a href="guide-live-streaming-cost.html">cost guide</a> puts it in context.</p>
<div class="callout"><p>We've been running cloud galleries since 2020 and built our own AWS routing and infrastructure for it. <a href="services.html">Ask us</a> about it for your next show.</p></div>
'''),

dict(slug='guide-remote-contribution.html', pillar='infrastructure',
 title='Remote Contribution for Live Events: SRT, NDI, vMix Call, Teams & Zoom Feeds | Virtual Studio Events',
 desc='The ways remote speakers and remote sites get into a live production: broadcast calling, SRT contribution, NDI on a LAN, and bringing Teams or Zoom into a broadcast properly.',
 h1='Remote contribution: <span class="em">getting the guest into the gallery.</span>', h1_plain='Remote contribution: getting the guest into the gallery',
 lede='Video calls, broadcast links and everything between. How remote speakers and remote venues arrive in a professional production, and which method suits which situation.',
 related=['guide-speaker-prep.html','guide-cloud-production.html','guide-encoders-bitrates.html','guide-stream-audio.html'],
 body='''
<p>"Can the CEO just join on Teams?" She can, but how her picture and sound get from her laptop into your broadcast decides whether she looks like a keynote or a customer-service call. These are the contribution methods we use, from simplest to most robust.</p>
<h2>Broadcast calling (vMix Call and similar)</h2>
<p>Purpose-built for production: the guest opens a link in a browser, and their video and audio arrive in the vision mixer as a clean, separate source with a return feed of the programme. No app to install, individual control of each guest's audio, and the operator can see and manage every caller. This is our default for remote speakers on virtual and hybrid events. Quality depends on the guest's connection and kit. See <a href="guide-speaker-prep.html">speaker prep</a>.</p>
<h2>SRT contribution</h2>
<p>For a remote <em>venue</em> or a high-value guest, a small hardware encoder at their end sends an SRT stream to the gallery: broadcast-grade picture and sound, encrypted, tolerant of imperfect networks, with sub-second latency. It's how we bring a second site into a multi-location conference, or a keynote speaker with a local camera crew into the main show. Needs a decent upload at the far end and someone to plug it in.</p>
<h2>NDI on a local network</h2>
<p>Within one building, NDI carries high-quality video over ordinary Ethernet. Cameras, laptops, graphics machines and the production PC all see each other on the LAN. It's the backbone of most modern galleries and the reason a single Ethernet cable can replace a bundle of SDI. It doesn't cross the public internet without extra tools, so it's a local solution.</p>
<h2>Bringing Teams, Zoom or Meet into a broadcast</h2>
<p>Sometimes the client's audience or the guest simply lives on a conferencing platform. Done properly, the meeting is joined by a dedicated production machine, and each participant's video is pulled out as an isolated source (the platforms' NDI outputs or a capture workflow), so the vision mixer can frame and cut between them like any other camera. Done badly, someone screen-records the gallery view with its grey borders and mute icons. The difference is entirely in the setup, and it's worth an hour of rehearsal.</p>
<h2>The phone as last resort</h2>
<p>Every remote speaker gets a dial-in number. If the video link fails, their voice over a holding slide with their name keeps the show moving. It's a cheap insurance policy that we've cashed in more than once.</p>
<h2>Choosing the method</h2>
<table><tr><th>Situation</th><th>Method</th></tr>
<tr><td>Remote presenter from home or office</td><td>Broadcast calling with a tested kit brief</td></tr>
<tr><td>Second venue or filmed remote keynote</td><td>SRT from a hardware encoder</td></tr>
<tr><td>Sources within one building</td><td>NDI over the LAN</td></tr>
<tr><td>Audience or guests already on Teams/Zoom</td><td>Isolated capture from a dedicated machine</td></tr>
<tr><td>Everything failed</td><td>Phone dial-in over a holding slide</td></tr></table>
<h2>Returns: what the guest sees and hears</h2>
<p>A remote speaker needs to see the programme (or at least the presenter) and hear the show <em>without hearing themselves</em>. That's a mix-minus return (programme audio minus their own voice) and it's the single most common thing missing from amateur setups. It's covered in detail in <a href="guide-stream-audio.html">stream audio</a>.</p>
'''),

dict(slug='guide-stream-audio.html', pillar='infrastructure',
 title='Audio for Live Streaming: Mix-Minus, Audio Splits & Levels Explained | Virtual Studio Events',
 desc='Why stream audio needs its own mix, how mix-minus stops remote speakers hearing themselves, getting a clean split from venue PA, levels and loudness, and the mistakes that ruin streams.',
 h1='Stream audio: <span class="em">the 80% nobody budgets for.</span>', h1_plain='Stream audio: the 80% nobody budgets for',
 lede='Viewers forgive a soft picture and never forgive bad sound. How professional stream audio is built, and the three mistakes that account for most complaints.',
 related=['guide-remote-contribution.html','guide-hybrid-event-checklist.html','guide-encoders-bitrates.html'],
 body='''
<p>Ask a hundred viewers why they left a stream and picture quality will barely feature. Audio will: too quiet, echoing, one speaker inaudible, a remote guest sounding like they're in a tunnel. Audio is most of the perceived quality of a stream, and it's usually the least-planned part of the production.</p>
<h2>The stream needs its own mix</h2>
<p>The mix that sounds right in a room (through a PA, with the room's own acoustics) is wrong for a stream. Room PA feeds are equalised for the space and carry every reverberation. The stream needs a dedicated mix: direct microphone feeds, VT audio, remote guests and any music, balanced for headphones and laptop speakers. On bigger shows that's a separate sound engineer with their own desk listening on the stream, not in the room.</p>
<h2>Audio splits from the venue</h2>
<p>When a venue's AV team runs the room, the stream takes an <strong>audio split</strong>: a copy of each microphone (or at minimum a clean pre-fade mix) delivered on a stage box or via Dante to the stream desk. Agree it in writing before the day: which sources, what connector, who provides the cable, and whether it's pre- or post-fader. "We'll give you a feed from the desk" is not specific enough.</p>
<h2>Mix-minus: why remote guests hear themselves</h2>
<p>A remote speaker needs to hear the show to take part in it. If you send them the full programme mix, that mix contains their own voice, delayed by the round trip, and they'll hear themselves echo a second later, which makes speaking almost impossible. <strong>Mix-minus</strong> is a return feed of everything <em>except</em> that person's own microphone. Every remote contributor needs their own mix-minus. Broadcast calling tools handle it automatically; DIY setups routing a Teams call into a mixer usually don't, and that's the echo you've heard on so many webinars.</p>
<h2>Levels and loudness</h2>
<p>Aim for consistent loudness across every source: the presenter, the pre-recorded video, the remote guest and the music bed should all sit at the same perceived level so viewers aren't reaching for the volume control. A limiter on the stream output prevents the sudden peak that distorts. Where we can, we normalise pre-recorded content in advance to a target loudness rather than fixing it live.</p>
<h2>Microphones: the right type in the right place</h2>
<p>Lavalier (clip-on) mics for presenters who move; headsets for anyone who turns their head a lot; handhelds for audience questions and as an emergency backup on stage; a boundary or gooseneck for a seated panel if lavs aren't possible. Fresh batteries at every break. And a rule: nobody on the stream is ever on a laptop microphone.</p>
<h2>The three mistakes that account for most complaints</h2>
<ol><li><strong>Feeding the room PA mix to the stream</strong> (reverberant, uneven, unusable.</li><li><strong>No mix-minus for remote guests</strong>) echo, and a speaker who stops mid-sentence.</li><li><strong>Nobody listening on the stream</strong>: problems that are obvious to a viewer go unnoticed for twenty minutes in a gallery monitoring the room.</li></ol>
<div class="callout"><p>Put a competent person on headphones, listening only to the stream, for the whole show. It's the cheapest quality improvement available.</p></div>
'''),

dict(slug='guide-cdn-players.html', pillar='infrastructure',
 title='CDNs, Video Players & Stream Latency Explained for Event Organisers | Virtual Studio Events',
 desc='What happens to your stream after the encoder: content delivery networks, adaptive bitrate, HLS and low-latency modes, player choices, geo-restrictions and corporate networks.',
 h1='Delivery: <span class="em">from the encoder to ten thousand screens.</span>', h1_plain='Delivery: from the encoder to ten thousand screens',
 lede='CDNs, adaptive bitrate, latency modes and players: what happens between your gallery and the viewer, and the decisions that affect whether it works on their network.',
 related=['guide-encoders-bitrates.html','guide-internet-connectivity.html','guide-platform-comparison.html'],
 body='''
<p>Your encoder sends one stream. Ten thousand people watch it, on phones on 4G, on laptops through corporate firewalls, on a boardroom TV. The machinery that makes that possible is the content delivery network and the player, and a few decisions here decide whether "it worked for us in the gallery" also means it worked for the audience.</p>
<h2>The CDN</h2>
<p>A content delivery network takes the single stream from the platform's ingest point, converts it into small chunks, and copies them to servers around the world so each viewer fetches from somewhere close. YouTube, Vimeo, Microsoft, Zoom and every dedicated event platform run or rent one. You rarely choose the CDN directly, but its behaviour (how many viewers it can serve, how it copes with corporate networks) is part of choosing the platform.</p>
<h2>Adaptive bitrate</h2>
<p>The platform transcodes your stream into a ladder of qualities (1080p, 720p, 480p, 360p) and the viewer's player switches between them as their connection changes. This is why you send one good 1080p stream and let the platform make the smaller versions, and why sending a bad stream can't be fixed downstream. The rungs of the ladder come from your source; garbage in, garbage in at every size.</p>
<h2>Latency: the trade-off you have to choose</h2>
<p>Standard HLS delivery is 15–45 seconds behind live. Robust, cacheable, works everywhere. Low-latency HLS and similar modes get to 3–8 seconds at some cost in resilience. WebRTC-based delivery reaches under a second for genuine two-way interaction but scales less cheaply. Choose based on what the audience needs to do: watch (standard is fine), react to live polls (low latency helps), converse (you need a video call, not a stream). Don't pay for latency you won't use.</p>
<h2>Players and where they live</h2>
<p>The player is the bit of software on the viewer's screen. It might be YouTube's, embedded in your platform; the platform's own; or a player embedded on your website. Considerations: does it support captions and accessibility controls; does it work on the devices your audience uses; does it fall back gracefully when the stream drops; and can you brand it. Test it on a phone, a locked-down corporate laptop and a smart TV before you commit.</p>
<h2>Corporate networks: the silent killer</h2>
<p>Many organisations block YouTube, throttle video, or route everything through a proxy that breaks streaming protocols. If your audience is inside a company, ask their IT team to test the exact player and stream type in advance, and have an alternative delivery path (a different platform or a direct HLS link) ready. This is the single most common reason a perfectly good stream "doesn't work for half the audience".</p>
<h2>Geo-restrictions and privacy</h2>
<p>Some content must not be visible outside certain territories or to the public. Platforms offer geo-restriction, password protection, SSO integration and tokenised links; unlisted YouTube links offer almost nothing. Decide the access model with the client and check the platform actually enforces it.</p>
<h2>Redundant delivery</h2>
<p>For events that matter we stream to two destinations at once. The primary platform and a standby (typically an unlisted stream on a second service). If the platform fails, the standby link goes to attendees by email within minutes. It costs almost nothing and has saved shows.</p>
'''),
]
