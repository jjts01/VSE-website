GUIDES = [
dict(slug='guide-hybrid-event-checklist.html', pillar='live-production',
 title='Hybrid Event Technical Checklist: 20 Questions Before Show Day | Virtual Studio Events',
 desc='The hybrid event checklist used by broadcast engineers: audio splits, remote speakers, room cameras, connectivity, streaming redundancy, platform integration and who owns the gaps.',
 h1='The hybrid event <span class="em">technical checklist.</span>', h1_plain='The hybrid event technical checklist',
 lede='Hybrid is where events fail. A great room show with an unwatchable stream, or vice versa. Settle these before show day.',
 related=['guide-stream-audio.html','guide-internet-connectivity.html','guide-remote-contribution.html','guide-gallery-roles.html'],
 body='''
<p><strong>The golden rule:</strong> the online audience is not an afterthought. It's usually the bigger audience. Design the show for both rooms from day one, and appoint one person who owns the join between them.</p>
<h2>Audio</h2>
<ol><li>Will the stream take a dedicated mix, not the room PA feed?</li><li>Who provides the audio split, on what connector, pre- or post-fader?</li><li>Do remote speakers get mix-minus returns so they don't hear themselves?</li><li>Is there a handheld backup mic on stage and fresh batteries at every break?</li></ol>
<p>Audio is 80% of perceived stream quality. Settle it first. <a href="guide-stream-audio.html">Stream audio in depth</a>.</p>
<h2>Cameras and vision</h2>
<ol start="5"><li>How many cameras cover the stage, and is at least one framed for screens rather than the back of the room?</li><li>Are slides fed to the stream as a clean source rather than a camera pointed at a projector?</li><li>Who mixes the stream, and is it a different person from whoever mixes the room screens?</li><li>Are the stage lighting states designed for camera as well as the room?</li></ol>
<h2>Remote contribution</h2>
<ol start="9"><li>How do remote speakers join, a managed broadcast link or a consumer video call?</li><li>Have they been tested on the actual hardware and connection?</li><li>Where does a remote speaker appear in the room, and can they see and hear the room?</li><li>What is the fallback if their link fails?</li></ol>
<h2>Connectivity</h2>
<ol start="13"><li>Is there dedicated wired internet for the stream, separate from guest Wi-Fi?</li><li>What's the backup path (bonded cellular, second circuit) and has it been tested in the room?</li><li>Has someone speed-tested the line from the position the encoder will sit?</li></ol>
<h2>The platform layer</h2>
<ol start="16"><li>Where does the online audience watch, and can they interact, Q&amp;A, polls, chat?</li><li>Do questions from the platform reach the moderator on stage, and how?</li><li>Has the player been tested on the audience's corporate network?</li></ol>
<h2>People</h2>
<ol start="19"><li>Who is the single technical point of contact across venue AV, streaming and platform?</li><li>Who calls the show for the stream, and how do they talk to the room's stage manager?</li></ol>
<p>On hybrid shows the most common failure isn't equipment. It's three suppliers each assuming another one owns the gap. That's the job we're most often hired to do: own the gap.</p>
<div class="callout"><p>Print this, take it to the production meeting, and don't leave until every question has a name next to it.</p></div>
'''),

dict(slug='guide-gallery-roles.html', pillar='live-production',
 title='Who\'s Who in a Live Production Gallery: Crew Roles for Virtual & Hybrid Events | Virtual Studio Events',
 desc='The roles in a broadcast gallery explained (producer, director, vision mixer, vMix operator, graphics, sound, streaming engineer, floor manager, speaker wrangler) and how many people a given event needs.',
 h1='Who\'s who in the gallery: <span class="em">crew roles explained.</span>', h1_plain='Who\'s who in the gallery: crew roles explained',
 lede='What each person in a production crew actually does, which roles can be combined, and the crew sizes that fit different events.',
 related=['guide-show-calling-comms.html','guide-hybrid-event-checklist.html','guide-live-streaming-cost.html'],
 body='''
<p>Quotes for event production are mostly people. Understanding what each person does (and which jobs genuinely can't be combined) is the fastest way to judge whether a crew list is right for your show, over-specified, or dangerously thin.</p>
<h2>The roles</h2>
<p><strong>Producer.</strong> Owns the show. Calls the run order, watches the clock, makes the decisions when things change. On a virtual event the producer is usually also the show caller, the voice on comms that everyone follows.</p>
<p><strong>Director / vision mixer.</strong> Chooses the pictures: which camera, when to cut, when the graphic comes in. On smaller shows the vision mixer and the producer are the same person; on larger ones they must be separate, because you can't call the show and cut it at the same time under pressure.</p>
<p><strong>vMix / production operator.</strong> Drives the production system (cameras, playback, remote callers, graphics, encoding), often all from one machine. On many virtual events this person is director, vision mixer, graphics and streaming engineer rolled into one, which is fine for a single-stream show and not fine for a multi-room conference.</p>
<p><strong>Graphics operator.</strong> Fires lower thirds, slides, polls and stings on cue. Splits out from the vMix operator when the graphics load is heavy.</p>
<p><strong>Sound engineer.</strong> Mixes the stream audio, manages remote returns (mix-minus) and radio mics. Under-hired, over-needed.</p>
<p><strong>Streaming / broadcast engineer.</strong> Owns the encoders, connectivity, failover and the destination platforms. Watches the stream health, not the pictures.</p>
<p><strong>Video HOD / technical director.</strong> The senior technical lead on complex shows: designs the system, signs off the plan, owns the interfaces with venue and other suppliers.</p>
<p><strong>Floor manager.</strong> The gallery's person in the room: cues presenters, manages the stage, relays what the audience can't see.</p>
<p><strong>Speaker wrangler / green room host.</strong> Tests, briefs and babysits remote contributors so nobody in the gallery has to.</p>
<p><strong>Platform moderator.</strong> Runs Q&amp;A, chat and polls on the platform; feeds questions to the stage.</p>
<p><strong>Camera operators.</strong> One per manned camera; robotic or locked-off cameras need none.</p>
<h2>Which combinations work</h2>
<p>Producer + show caller: yes. vMix operator + graphics on a simple show: yes. Streaming engineer + sound engineer: usually a mistake. Both need full attention when things wobble. Producer + vision mixer on anything over an hour with more than three sources: no. Floor manager + speaker wrangler: only if all speakers are in the room.</p>
<h2>Crew sizes by event</h2>
<table><tr><th>Event</th><th>Typical crew</th><th>Roles</th></tr>
<tr><td>Webinar, one presenter, slides</td><td>1–2</td><td>vMix operator (+ producer/wrangler)</td></tr>
<tr><td>Virtual town hall, remote panel</td><td>3</td><td>Producer, vMix operator, speaker wrangler</td></tr>
<tr><td>Single-room hybrid conference</td><td>4–6</td><td>Producer, vision mixer, sound, streaming, floor manager, camera</td></tr>
<tr><td>Multi-track hybrid conference</td><td>8–15</td><td>Above per room, plus HOD, graphics, moderators</td></tr>
<tr><td>Awards show, streamed</td><td>6–10</td><td>Producer, director, vision mixer, graphics, sound, streaming, floor, cameras</td></tr></table>
<h2>Reading a crew list</h2>
<p>Red flags: one person listed for vision, sound and streaming on a show with remote guests; no floor manager on a hybrid event; no rehearsal day on a multi-camera show. Green flags: a named technical lead, a separate sound engineer, and a rehearsal in the schedule. The crew is what you're paying for; make sure it's the right crew.</p>
'''),

dict(slug='guide-show-calling-comms.html', pillar='live-production',
 title='Show Calling & Comms for Live Events: Talkback, Standard Cues & Protocol | Virtual Studio Events',
 desc='How a live event is called: comms channels and talkback, the standard vocabulary (standby, go, cut), calling remote and hybrid shows, discipline on comms and what to do when the caller is lost.',
 h1='Show calling: <span class="em">the voice everyone follows.</span>', h1_plain='Show calling: the voice everyone follows',
 lede='How professional crews talk during a live show. The channels, the standard calls, and the discipline that keeps a gallery calm when the run order goes sideways.',
 related=['guide-run-order.html','guide-gallery-roles.html','guide-when-it-goes-wrong.html'],
 body='''
<p>Comms is the nervous system of a live show. Everyone in the crew is on a talkback channel, and one voice (the show caller) turns the run order into cues that fire on time. Get the language and discipline right and a complex show feels effortless; get it wrong and every transition is a negotiation.</p>
<h2>Channels</h2>
<p>Small shows run one open channel. Larger ones split: a production channel (caller, vision, graphics, playback), a technical channel (streaming, sound, engineering) and a floor channel (floor manager, cameras, stage). The caller can talk to all; departments keep their own chatter off the production channel. Remote crew join the same channels over IP intercom. Our <a href="guide-cloud-production.html">cloud galleries</a> run comms this way every show.</p>
<h2>The standard vocabulary</h2>
<p><strong>"Standby [item]"</strong>: warn, 10–30 seconds before, naming the item number from the run order. <strong>"Go"</strong>: execute, and only the word "go" executes anything. <strong>"Cut"</strong>, <strong>"Take 2"</strong>, <strong>"Roll VT"</strong>, <strong>"Graphic in / graphic out"</strong>, <strong>"Fade to holding"</strong>: short, unambiguous, agreed in advance. Nobody says "yeah do it now" on comms. Counts are given into VTs and out of breaks: "coming out of VT in 10… 5, 4, 3, 2, 1, go cam 1".</p>
<h2>Calling from the run order</h2>
<p>The caller reads ahead. While item 14 is on air they are standing by item 15 and checking item 16 is ready. Every cue names the item number so anyone can find their place: "standby item 15, lower third Sarah, cam 2." When timings drift the caller announces the new plan once, clearly: "we're running four late, we'll lose the second poll, item 22 is out."</p>
<h2>Calling hybrid and remote</h2>
<p>Hybrid shows have two rhythms (the room's and the stream's) and the caller sits between them. The floor manager cues the stage; the caller cues the pictures and graphics; and they talk to each other constantly. Remote speakers are cued by the speaker wrangler on a separate line so they never hear the gallery. When the caller is remote (cloud gallery) the floor manager becomes their eyes; agree a shorthand for what the room is doing.</p>
<h2>Discipline</h2>
<ul><li>Only the caller calls. Everyone else confirms ("cam 2 ready") or reports ("stream health good", "Sarah's link dropped").</li><li>Report problems in one line, with what you're doing about it: "primary encoder down, on backup, stream stable."</li><li>No chat during a live segment. Save the joke for the break.</li><li>Use names, not "you".</li><li>If comms fails, the pre-agreed fallback is the printed run order and hand signals from the floor.</li></ul>
<h2>What it sounds like</h2>
<p><em>"Standby item 12, VT sizzle, 90 seconds, embedded audio, mics down. Graphics standby holding for the end. Coming to VT in 5, 4, 3, 2, 1: roll VT, mics down. Good. Sarah, you're back on cam 1 after this, wrap in 90. Standby cam 1, standby lower third Sarah. Out of VT in 10… 5, 4, 3, 2, 1, cam 1, mics up, graphic in."</em></p>
<div class="callout"><p>Rehearse comms as part of the dress run. A show that's been called through once already is half the stress of one that hasn't.</p></div>
'''),

dict(slug='guide-live-interaction.html', pillar='live-production',
 title='Running Live Q&A, Polls & Chat at Virtual Events Without Chaos | Virtual Studio Events',
 desc='How to manage audience interaction at virtual and hybrid events: moderation workflow, getting questions to the stage, polls that work with stream latency, chat etiquette, and staffing.',
 h1='Live interaction: <span class="em">Q&amp;A, polls and chat without the chaos.</span>', h1_plain='Live interaction: Q&A, polls and chat without the chaos',
 lede='Interaction is why people choose live over on-demand. It\'s also where most virtual events look messiest. The workflow that keeps it sharp.',
 related=['guide-engagement-features.html','guide-cdn-players.html','guide-gallery-roles.html'],
 body='''
<p>Every audience-interaction feature is a promise: ask and you'll be heard, vote and you'll see the result. Break the promise (a question that vanishes, a poll that never gets read out), and the audience disengages for the rest of the show. Interaction needs its own workflow and its own staffing, like any other part of the production.</p>
<h2>Q&amp;A: the moderation pipeline</h2>
<p>Questions arrive on the platform. A <strong>moderator</strong> (a named person, not "someone in the gallery") reads them as they come in, merges duplicates, flags the good ones and discards the unusable. The flagged questions go to the <strong>presenter or host</strong> on a tablet or confidence monitor, already prioritised, so they can pick the next one without reading fifty. Nothing reaches the stage unfiltered. For hybrid shows, the moderator also holds the roving mic queue in the room so in-person and online questions interleave fairly.</p>
<h2>Make questions visible</h2>
<p>When a question is answered, put it on screen as a graphic. Name (if permitted) and question text. It tells the asker they were heard, tells everyone else the feature works, and it looks like television. Pre-build the graphic template so the moderator can populate it in seconds.</p>
<h2>Polls and latency</h2>
<p>Streams are delayed 5–40 seconds behind the room. If the presenter says "vote now" and closes the poll 20 seconds later, half the online audience never saw it open. Give polls a generous window (90 seconds minimum), launch them on the platform slightly <em>before</em> the presenter mentions them, and show results on the stream as a graphic rather than asking the presenter to read a screen the audience can't see. Our <a href="guide-cdn-players.html">delivery guide</a> explains the latency options.</p>
<h2>Chat: decide what it's for</h2>
<p>Open chat is great for community and dreadful for signal. Set expectations on screen at the top ("chat is for reactions; questions go in the Q&amp;A tab"), have a host in the chat welcoming people and answering practical questions ("can't hear? try refreshing"), and give the moderator the power to hide messages. For large public events, pre-moderation or slow mode.</p>
<h2>The presenter's part</h2>
<p>Presenters must acknowledge the online audience by name and at regular intervals ("great question from Priya watching in Leeds") or the stream becomes a window onto someone else's meeting. Brief them to leave gaps for questions and to trust the moderator's list rather than scanning a screen live.</p>
<h2>Staffing</h2>
<p>Under 200 attendees: one moderator can run Q&amp;A, polls and chat. 200–1,000: a moderator plus a chat host. Over 1,000, or public: two moderators and a chat host, with the platform's automated filters on. It's a modest cost, and it's the difference between interaction that feels curated and interaction that feels like a free-for-all.</p>
<h2>Before the show</h2>
<ul><li>Pre-load polls with correct options and agreed timings in the run order.</li><li>Seed two or three questions so the Q&amp;A tab isn't empty when it opens.</li><li>Agree the profanity and personal-data rules for what goes on screen.</li><li>Rehearse the handoff from moderator to presenter.</li></ul>
'''),

dict(slug='guide-when-it-goes-wrong.html', pillar='live-production',
 title='When a Live Stream Goes Wrong: The Recovery Playbook | Virtual Studio Events',
 desc='What professional crews do in the first 60 seconds of a live failure: holding graphics, failover, calm comms, the presenter\'s script, when to stop and restart, and the post-mortem afterwards.',
 h1='When it goes wrong live: <span class="em">the first sixty seconds.</span>', h1_plain='When it goes wrong live: the first sixty seconds',
 lede='Something will break on air eventually. The difference between a blip and a disaster is what the crew does in the first minute, and whether they\'ve rehearsed it.',
 related=['guide-risk-redundancy.html','guide-rehearsals.html','guide-show-calling-comms.html'],
 body='''
<p>Across more than five hundred shows we've had encoders die, keynotes drop off mid-sentence, venue power trip and platforms fall over. Almost none of those became something the audience remembers, because the response was already written down. This is that playbook.</p>
<h2>Second 0: cover the picture</h2>
<p>Whatever has failed, the audience must never see black, a frozen frame or a gallery desktop. The first call is always "fade to holding". The branded "back in a moment" graphic with the music bed. It buys time and it looks intentional. Every show has this graphic loaded on a hot key; if yours doesn't, that's the first thing to fix.</p>
<h2>Seconds 0–15: diagnose out loud, once</h2>
<p>One person reports on comms in one sentence: what's broken and what they're doing. "Primary encoder dropped, switching to backup." "Sarah's link is gone, wrangler redialling." The caller acknowledges and everyone else stays silent unless they have information. Panic on comms is contagious; a calm voice is too.</p>
<h2>Seconds 15–45: execute the rehearsed response</h2>
<p>Each likely failure has a pre-agreed response from the <a href="guide-risk-redundancy.html">risk register</a>: encoder → backup encoder; internet → bonded cellular; remote speaker → holding graphic with their name while the wrangler reconnects, or the presenter takes the next item; platform → standby link emailed to attendees; playback file → skip to the next item and return to it. Because it's been drilled in rehearsal, this is a cue like any other, not an improvisation.</p>
<h2>Seconds 45–60: brief the presenter</h2>
<p>The presenter is told, via the floor manager or an earpiece, exactly what to say and do: "Sarah's line dropped; say we'll come back to her and introduce the next speaker." Presenters who know the plan handle it gracefully; the audience hears "we've lost Sarah for a moment. Let's bring in James and come back to her" and thinks nothing of it. Give every presenter a line for this in the prep session.</p>
<h2>When to stop and restart</h2>
<p>Rarely. Stopping the stream logs the audience out of players and dumps the recording; restarting means many won't find their way back. Stay live on holding for up to a few minutes while you fix. Beyond that, tell the audience plainly on screen what's happening and when to return, and email them. Honesty keeps more viewers than silence.</p>
<h2>Afterwards: the post-mortem</h2>
<p>Within 24 hours, while it's fresh: what failed, what the response was, how long the audience was affected, what would have prevented it. Written down, without blame, and turned into a change to the checklist or the kit. The crews that never seem to have problems are the ones who've had them all before and wrote them down.</p>
<h2>The kit that makes recovery possible</h2>
<ul><li>Holding graphic on a hot key, with music.</li><li>Backup encoder and backup connection, already running.</li><li>A standby stream destination and the email ready to send.</li><li>Dial-in numbers for every remote speaker.</li><li>Printed run order in case the screens go.</li><li>A rehearsed failure drill in the dress run.</li></ul>
<div class="callout"><p>Ask your production company what they'd do if the primary encoder died mid-keynote. If the answer takes more than one sentence, keep asking.</p></div>
'''),

dict(slug='guide-multi-platform-streaming.html', pillar='live-production',
 title='Simulcasting: Streaming a Live Event to Multiple Platforms at Once | Virtual Studio Events',
 desc='How to stream one event to YouTube, LinkedIn, Facebook, a website player and an event platform simultaneously: restreaming services vs multiple encoders, per-platform requirements, chat and analytics.',
 h1='Simulcasting: <span class="em">one show, every platform.</span>', h1_plain='Simulcasting: one show, every platform',
 lede='Streaming to LinkedIn, YouTube, your website and the event platform at the same time: how it\'s done, what each destination wants, and what it does to your interaction and analytics.',
 related=['guide-encoders-bitrates.html','guide-cdn-players.html','guide-platform-comparison.html'],
 body='''
<p>Public-facing events increasingly want to meet the audience where it already is: on LinkedIn for the professional crowd, YouTube for reach, the company website for control, plus the registered-attendee platform. Sending one production to all of them at once is simulcasting, and it's straightforward if you plan for the differences between destinations.</p>
<h2>Two ways to do it</h2>
<p><strong>A restreaming service</strong> takes one stream from your encoder and fans it out to every destination from the cloud. One upload from the venue, one point of failure, easy to manage. <strong>Multiple encoders</strong> (or multiple outputs from the production software) send independent streams to each platform. More upload bandwidth needed, but no third-party dependency and per-destination control of quality. We generally use a restreamer for social destinations and a direct, independent stream to the primary platform, so the primary doesn't share the social channels' risk.</p>
<h2>What each destination expects</h2>
<p>Platforms differ in accepted resolutions, bitrates, keyframe intervals, aspect ratios and whether they need a scheduled event created in advance with its own stream key. Some require the stream to start minutes before "going live" to warm up; some auto-end after a period of silence. Build a destination sheet with the settings and keys for each, and test every one in the tech run. A stream key pasted wrong is the classic simulcast failure.</p>
<h2>Content and rights</h2>
<p>Music is the trap. Licensed music that's fine on your own platform will get a stream muted or taken down on social platforms with automated rights detection. Use cleared library music for anything simulcast, and keep the awards-show playout of a chart hit for the room only.</p>
<h2>Interaction across platforms</h2>
<p>Each destination has its own comments and chat. Either aggregate them (many restreamers and moderation tools pull all comments into one view for the moderator) or decide that interaction only lives on the primary platform and say so on screen. Polls and Q&amp;A almost always stay on the primary platform; social viewers are told where to go if they want to take part.</p>
<h2>Analytics</h2>
<p>You'll get separate numbers from every platform, measured differently. Agree in advance how you'll combine them (peak concurrent across platforms, total unique viewers where the platform provides it, watch time), and note that social platforms count a "view" after a few seconds. The <a href="guide-event-metrics.html">metrics guide</a> covers how to report honestly.</p>
<h2>Bandwidth</h2>
<p>Direct multi-encoder simulcasting multiplies your upload requirement by the number of destinations. A restreamer keeps it at one stream. Either way, run the <a href="tools.html">bandwidth calculator</a> with the real number of outputs.</p>
<h2>Checklist</h2>
<ul><li>Destination sheet: settings, stream keys, scheduled events, go-live lead times.</li><li>Music cleared for every platform.</li><li>Every destination tested in the tech run, watched on a phone.</li><li>Moderation plan for each platform's comments.</li><li>Analytics definitions agreed before the show.</li></ul>
'''),
]
