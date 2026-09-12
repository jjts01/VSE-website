/* VSE Platform demos — fully client-side, simulated audience, no storage */
(function(){
const $=(s,r)=>(r||document).querySelector(s), $$=(s,r)=>[...(r||document).querySelectorAll(s)];
const rnd=(a,b)=>Math.floor(Math.random()*(b-a+1))+a, pick=a=>a[rnd(0,a.length-1)];
const NAMES=['Priya S.','Tom W.','Aisha K.','Ben O.','Marta L.','Dev P.','Chloe R.','Sam H.','Ravi N.','Jess M.','Omar F.','Lucy T.','Kwame A.','Hannah B.','Leo G.','Nadia E.'];

/* ---------- brand scenarios ----------
   Four different customers, not four colourways. Each carries its own sector,
   audience size, agenda, questions, tickets, sponsors and visual language, so
   the white-label claim is demonstrated rather than asserted. The three
   non-VSE scenarios mirror the three audiences the business actually sells to:
   a production company buying crew, a corporate running an all-hands, and a
   membership body running a hybrid conference. */
const SCENARIOS={
 vse:{
  name:'Virtual Studio Events', sector:'Event production',
  event:'Annual Conference 2027', when:'14 May 2027 · London & online · 09:00–16:30 BST',
  short:'Annual Conference 2027', size:1214, registered:2140, peak:1610,
  bg:'#212b54', accent:'#6a9799', accent2:'#9fc4c5', panel:'#2b3663',
  radius:'18px', font:'var(--display)', labelCase:'uppercase', labelSpace:'.22em',
  host:{name:'Sarah Okafor', role:'Head of Events'},
  objective:'reach the whole membership live or on demand and generate qualified conversations for the sales team',
  polls:[{q:'Which format will you run most in 2027?',o:['Virtual','Hybrid','In-person','Not sure']},
         {q:'Biggest risk on your last event?',o:['Internet','Speakers','Platform','Budget']},
         {q:'How do you measure success?',o:['Attendance','Engagement','Leads','Feedback']}],
  quiz:[{q:"What's the recommended keyframe interval for live streaming?",o:['1 second','2 seconds','5 seconds','10 seconds'],a:1},
        {q:"What does mix-minus remove from a remote guest's return feed?",o:['Music','The presenter','Their own voice','Room noise'],a:2},
        {q:'Standard HLS latency is roughly…',o:['0.5 s','3 s','15–45 s','2 minutes'],a:2}],
  questions:[{t:'How do you keep remote speakers looking as good as the studio presenters?',u:42,by:'Aisha K.'},
             {t:'What redundancy do you actually run on the internet line?',u:37,by:'Tom W.'},
             {t:'Is 4K ever worth the bandwidth for a conference?',u:21,by:'Dev P.'},
             {t:'Do you recommend human or automated captions for internal events?',u:18,by:'Chloe R.'}],
  chat:['Great audio today 👌','Can we get the slides afterwards?','Hello from Leeds!','The hybrid checklist guide is gold','Watching from the warehouse canteen 🙋','Question submitted!'],
  tickets:[{v:'Online pass',d:'Live stream, participation, on-demand for 30 days',p:0,label:'Free'},
           {v:'In-person',d:'Venue, lunch, networking, plus everything online',p:195,label:'£195'},
           {v:'VIP & speaker dinner',d:'Front section, speaker dinner, 1:1 meeting priority',p:495,label:'£495'}],
  roles:['Events','Marketing','Internal comms','Production'],
  tracks:['Hybrid production','Platforms & data','Set & studio'],
  trackNames:{A:'Main stage',B:'Platforms & data',C:'Workshops'},
  agenda:[['09:00','A','Doors, holding loop & welcome',''],['09:30','A','Keynote: Events that survive contact with reality','Sarah Okafor'],['10:15','B','Registration data & GDPR without the fear','Marta L.'],['10:15','C','Workshop: writing a run order the gallery can use','James Jones'],['11:00','A','Panel: hybrid — owning the join',"Ben O'Dwyer, Aisha K."],['11:45','B','Platform comparison: Teams, Zoom, YouTube or dedicated?','Dev P.'],['12:30','A','Lunch · expo & 1:1 meetings',''],['13:30','A','Case study: a 75,000-viewer awards show','James Jones'],['14:15','C','Workshop: lighting for camera in 45 minutes','Chloe R.'],['15:00','A','Measuring ROI: a model finance accepts',"Ben O'Dwyer"],['15:45','A','Closing & on-demand launch','Sarah Okafor']],
  speakers:[['Sarah Okafor','Head of Events, Virtual Studio Events','Keynote'],['James Jones','Co-founder, Virtual Studio Events','Run orders · Awards case study'],["Ben O'Dwyer",'Co-founder, Virtual Studio Events','Hybrid panel · ROI'],['Aisha K.','Broadcast engineer','Hybrid panel'],['Marta L.','Data protection lead','GDPR'],['Dev P.','Platform consultant','Platform comparison'],['Chloe R.','Lighting director','Lighting workshop'],['Tom W.','Venue AV manager','Hybrid panel']],
  expo:[['Granary Digital','Studio partner · Podcast & broadcast studios','Gold'],['StreamKit','Bonded cellular encoders','Silver'],['CaptionWorks','Human live captioning & BSL','Silver'],['Lumen Hire','LED walls & lighting','Bronze']],
  sponsors:['Granary Digital','StreamKit','CaptionWorks','Lumen Hire'],
  people:[['Aisha K.','Broadcast engineer · Leeds','hybrid production'],['Dev P.','Platform consultant · London','platforms & data'],['Nadia E.','Internal comms lead · Manchester','hybrid production'],['Omar F.','Events manager · Bristol','platforms & data']],
  roundtables:[['Measuring event ROI','6 seats · hosted by Ben O’Dwyer'],['Hybrid room + stream','4 seats · hosted by James Jones']],
  runOrder:[['09:00','Welcome',0.35],['09:30','Keynote',0.95],['10:15','Track sessions',0.72],['11:00','Hybrid panel',0.88],['11:45','Platforms',0.6],['12:30','Lunch/expo',0.3],['13:30','Awards case study',0.82],['14:15','Workshops',0.55],['15:00','ROI',0.7],['15:45','Close',0.5],['16:30','End',0.1]],
  weak:'${S.weak}'
 },

 apex:{
  name:'Apex Live', sector:'Production agency · white-label',
  event:'Meridian Awards 2027', when:'27 February 2027 · Old Billingsgate & online · 19:00–22:30 GMT',
  short:'Meridian Awards 2027', size:412, registered:520, peak:640,
  bg:'#121212', accent:'#c9a227', accent2:'#e8cf7a', panel:'#1e1e1e',
  radius:'2px', font:'"Helvetica Neue",Arial,sans-serif', labelCase:'uppercase', labelSpace:'.34em',
  host:{name:'Marcus Bell', role:'Executive Producer'},
  objective:'deliver a client awards show to a room and a remote audience with no visible seam, under the client’s brand',
  polls:[{q:'Which category are you here for?',o:['Innovation','Sustainability','Team of the year','All of them']},
         {q:'First time at the Meridians?',o:['First time','Been before','I won last year','Presenting']},
         {q:'Table drinks running low?',o:['All good','Nearly','Send help','Driving']}],
  quiz:[{q:'How many categories are being announced tonight?',o:['8','12','14','18'],a:2},
        {q:'Which city hosted the Meridians in 2026?',o:['Manchester','Glasgow','Bristol','London'],a:0},
        {q:'What year did the Meridian Awards start?',o:['2009','2013','2017','2021'],a:1}],
  questions:[{t:'Will the winner interviews be available to download for our press team?',u:31,by:'Rachel D.'},
             {t:'Can remote guests see the room camera during the announcements?',u:24,by:'Gio M.'},
             {t:'What time does the after-party stream cut off?',u:19,by:'Sam P.'},
             {t:'Is the nominee reel available in 9:16 for social?',u:14,by:'Bea C.'}],
  chat:['Table 14 ready 🥂','That VT was superb','Remote and loving it','Congratulations Innovation team!','Audio perfect from here','Who did the lighting? Stunning'],
  tickets:[{v:'Remote viewing',d:'Live broadcast, voting, winner reels on demand',p:0,label:'Free'},
           {v:'Single seat',d:'Drinks reception, dinner, ceremony, after-party',p:245,label:'£245'},
           {v:'Table of ten',d:'Reserved table, sponsor mention, photography package',p:2200,label:'£2,200'}],
  roles:['Agency','Client','Press','Nominee'],
  tracks:['Ceremony','Winner interviews','After-party'],
  trackNames:{A:'Main room',B:'Press room',C:'Green room'},
  agenda:[['18:30','A','Drinks reception · room camera live',''],['19:00','A','Ceremony opens · host welcome','Marcus Bell'],['19:15','A','Categories 1–5','Host'],['19:50','B','Winner interviews · press room','Rachel D.'],['20:10','A','Dinner service · sponsor reel',''],['20:45','A','Categories 6–10','Host'],['21:15','B','Winner interviews · press room','Rachel D.'],['21:30','A','Categories 11–14 & Grand Prix','Host'],['22:00','A','Closing remarks','Marcus Bell'],['22:10','C','After-party stream · DJ set','']],
  speakers:[['Marcus Bell','Executive Producer, Apex Live','Host'],['Rachel D.','Press lead','Winner interviews'],['Gio M.','Lighting designer','Room design'],['Bea C.','Social editor','Clips & 9:16'],['Sam P.','Floor manager','Room'],['Nina H.','Awards director, Meridian','Grand Prix']],
  expo:[['Meridian Group','Headline sponsor','Headline'],['Calder & Finch','Category sponsor · Innovation','Gold'],['Brightwater','Category sponsor · Sustainability','Gold'],['Studio Nine','Photography & content','Silver']],
  sponsors:['Meridian Group','Calder & Finch','Brightwater','Studio Nine'],
  people:[['Rachel D.','Press lead · London','winner interviews'],['Gio M.','Lighting designer · London','room design'],['Nina H.','Awards director · Leeds','ceremony'],['Bea C.','Social editor · Remote','clips']],
  roundtables:[['Sponsor activation review','5 seats · hosted by Marcus Bell'],['2028 categories','6 seats · hosted by Nina H.']],
  runOrder:[['18:30','Reception',0.28],['19:00','Ceremony opens',0.92],['19:15','Categories 1–5',0.88],['19:50','Interviews',0.54],['20:10','Dinner',0.42],['20:45','Categories 6–10',0.9],['21:15','Interviews',0.58],['21:30','Grand Prix',0.98],['22:00','Close',0.6],['22:10','After-party',0.22],['22:30','End',0.08]],
  weak:'the dinner-service stretch lost 40% of the remote audience'
 },

 northfield:{
  name:'Northfield Group', sector:'Retail · internal communications',
  event:'All-Hands · Q1 2027', when:'9 March 2027 · Every store, depot and office · 10:00–11:15 GMT',
  short:'Q1 All-Hands', size:3980, registered:6800, peak:5200,
  bg:'#14302a', accent:'#8fbf4a', accent2:'#c2e08a', panel:'#1c4038',
  radius:'24px', font:'"Trebuchet MS",Verdana,sans-serif', labelCase:'none', labelSpace:'.04em',
  host:{name:'Dan Whitfield', role:'Chief Executive'},
  objective:'reach every colleague including shift workers on the shop floor, and measure whether the quarter’s priorities actually landed',
  polls:[{q:'Where are you watching from today?',o:['Store','Depot','Head office','Home']},
         {q:'How clear are the Q1 priorities?',o:['Very clear','Mostly','Not yet','First I’ve heard']},
         {q:'What should we cover next time?',o:['Pay & benefits','Systems','Store standards','Growth plans']}],
  quiz:[{q:'How many new stores opened last quarter?',o:['4','9','14','21'],a:1},
        {q:'Which region grew fastest in Q4?',o:['North West','Midlands','Scotland','South East'],a:2},
        {q:'What is our colleague discount rising to?',o:['15%','20%','25%','30%'],a:2}],
  questions:[{t:'Will the new rota system roll out to depots at the same time as stores?',u:214,by:'Leanne  M.'},
             {t:'Can we get the recording with subtitles for colleagues on nights?',u:186,by:'Rob T.'},
             {t:'Is the colleague discount change permanent or a trial?',u:151,by:'Priya K.'},
             {t:'What happens to the Milton Keynes depot in the restructure?',u:129,by:'Dean H.'}],
  chat:['Morning from Store 214 👋','Break room is packed for this','Subtitles please!','Good news on the discount','Depot 3 watching on the big screen','Can you repeat the rota date?'],
  tickets:[{v:'Colleague (online)',d:'Live stream, Q&A, on-demand with subtitles',p:0,label:'Free'},
           {v:'Store screen',d:'One link per site for the break room screen',p:0,label:'Free'},
           {v:'Head office (in person)',d:'Atrium, breakfast from 09:15',p:0,label:'Free'}],
  roles:['Store','Depot','Head office','Field team'],
  tracks:['Company update','Q&A','Regional breakout'],
  trackNames:{A:'Main broadcast',B:'Regional breakout',C:'Manager briefing'},
  agenda:[['09:45','A','Holding loop · music & Q1 highlights',''],['10:00','A','Welcome & the quarter in numbers','Dan Whitfield'],['10:15','A','Trading update','Sal Ahmed'],['10:30','A','The new rota system, explained','Kate Lindsay'],['10:45','A','Live Q&A · questions from the floor','Dan Whitfield'],['11:05','A','Close & what happens next','Dan Whitfield'],['11:15','B','Regional breakouts · North, Midlands, South',''],['11:15','C','Manager briefing · cascade pack','Kate Lindsay']],
  speakers:[['Dan Whitfield','Chief Executive','Welcome · Q&A'],['Sal Ahmed','Chief Financial Officer','Trading update'],['Kate Lindsay','People Director','Rota system · Manager briefing'],['Marcus Reid','Retail Director','Regional breakout'],['Jo Fenton','Comms lead','Host']],
  expo:[['Colleague support','Wellbeing, pensions and the benefits hub','Info'],['Learning','Apprenticeships and management pathways','Info'],['Rota help desk','Live chat with the project team','Info'],['Suggestions','Send an idea straight to the exec team','Info']],
  sponsors:['Colleague support','Learning','Rota help desk','Suggestions'],
  people:[['Kate Lindsay','People Director · Head office','rota system'],['Marcus Reid','Retail Director · North','store standards'],['Jo Fenton','Comms lead · Head office','cascade pack'],['Leanne M.','Store manager · Store 214','rota system']],
  roundtables:[['Rota questions, live','12 seats · hosted by Kate Lindsay'],['Store standards','10 seats · hosted by Marcus Reid']],
  runOrder:[['09:45','Holding loop',0.22],['10:00','Welcome',0.96],['10:15','Trading update',0.9],['10:30','Rota system',0.98],['10:45','Live Q&A',0.86],['11:05','Close',0.64],['11:15','Breakouts',0.3],['11:30','End',0.06]],
  weak:'the trading update lost the shop-floor audience for four minutes around the slide-heavy section'
 },

 ilt:{
  name:'Institute of Logistics & Transport', sector:'Membership body · CPD',
  event:'Annual Conference & AGM 2027', when:'8 October 2027 · Birmingham & online · 09:30–17:00 BST',
  short:'Annual Conference & AGM', size:874, registered:1480, peak:1120,
  bg:'#2d1b2e', accent:'#b9705f', accent2:'#dda695', panel:'#3b2540',
  radius:'6px', font:'Georgia,"Times New Roman",serif', labelCase:'none', labelSpace:'.1em',
  host:{name:'Dr Helen Asante', role:'Director General'},
  objective:'deliver accredited CPD to members who cannot travel, and carry a quorate AGM vote online',
  polls:[{q:'What is your biggest operational pressure in 2027?',o:['Driver shortage','Fuel & energy','Warehouse capacity','Compliance']},
         {q:'How are you approaching fleet decarbonisation?',o:['Electric now','Trialling','Planning','No plan yet']},
         {q:'Are you claiming CPD hours for today?',o:['Yes, all day','Some sessions','Not sure how','No']}],
  quiz:[{q:'What is the current maximum daily driving time under GB rules?',o:['8 hours','9 hours','10 hours','11 hours'],a:1},
        {q:'What does a Category C+E licence permit?',o:['Rigid only','Rigid + trailer','Bus','Van only'],a:1},
        {q:'Which document must accompany a hazardous consignment?',o:['CMR note','Dangerous goods note','Bill of lading','Packing list'],a:1}],
  questions:[{t:'Will the AGM vote stay open for members in different time zones?',u:96,by:'Peter N.'},
             {t:'How many CPD hours does the full-day online ticket carry?',u:88,by:'Sandra O.'},
             {t:'Is the driver shortage panel being recorded for branch meetings?',u:64,by:'Ian F.'},
             {t:'Does the institute have a position on the new emissions timetable?',u:57,by:'Mo A.'}],
  chat:['Joining from the Dublin branch','CPD certificate question in the Q&A','Excellent panel','Can we see the slides on decarbonisation?','Voting now','Good morning from Aberdeen'],
  tickets:[{v:'Member · online',d:'All sessions, AGM vote, 6 CPD hours, on-demand',p:0,label:'Included'},
           {v:'Member · in person',d:'Birmingham venue, lunch, exhibition, AGM vote',p:165,label:'£165'},
           {v:'Non-member · online',d:'All sessions and on-demand, no AGM vote',p:95,label:'£95'}],
  roles:['Operations','Fleet','Warehouse','Compliance','Academic'],
  tracks:['Fleet & decarbonisation','Warehouse & automation','Policy & compliance'],
  trackNames:{A:'Plenary',B:'Fleet & decarbonisation',C:'Warehouse & automation'},
  agenda:[['09:30','A','Registration, exhibition & networking',''],['10:00','A','Opening address & state of the sector','Dr Helen Asante'],['10:45','B','Fleet decarbonisation: what actually works','Ian F.'],['10:45','C','Automation without the hype','Sandra O.'],['11:30','A','Panel: the driver shortage, five years on','Mo A., Peter N.'],['12:30','A','Lunch & exhibition',''],['13:30','A','Annual General Meeting & member vote','Dr Helen Asante'],['14:30','B','Compliance update: emissions timetable','Mo A.'],['14:30','C','Warehouse capacity and the last mile','Ian F.'],['15:30','A','Awards & fellowship presentations',''],['16:15','A','Closing keynote & CPD certificates','Dr Helen Asante']],
  speakers:[['Dr Helen Asante','Director General, ILT','Opening · AGM · Close'],['Ian F.','Fleet strategy lead','Decarbonisation · Last mile'],['Sandra O.','Head of automation research','Automation'],['Mo A.','Policy director','Compliance · Panel'],['Peter N.','Branch chair, Scotland','Panel'],['Ruth C.','Awards chair','Fellowships']],
  expo:[['Caledon Fleet','Electric HGV leasing','Gold'],['Warehouse Systems Group','Automation & robotics','Gold'],['Meridian Insurance','Fleet and cargo cover','Silver'],['CPD Academy','Accredited training','Silver']],
  sponsors:['Caledon Fleet','Warehouse Systems Group','Meridian Insurance','CPD Academy'],
  people:[['Peter N.','Branch chair · Aberdeen','policy & compliance'],['Sandra O.','Automation research · Coventry','warehouse & automation'],['Ian F.','Fleet strategy · Manchester','fleet & decarbonisation'],['Mo A.','Policy director · London','policy & compliance']],
  roundtables:[['Branch chairs meet-up','8 seats · hosted by Peter N.'],['CPD and accreditation','6 seats · hosted by Ruth C.']],
  runOrder:[['09:30','Registration',0.3],['10:00','Opening address',0.9],['10:45','Breakouts',0.68],['11:30','Driver shortage panel',0.86],['12:30','Lunch/exhibition',0.34],['13:30','AGM & vote',0.94],['14:30','Breakouts',0.62],['15:30','Awards',0.74],['16:15','Closing keynote',0.66],['17:00','End',0.1]],
  weak:'the afternoon breakouts lost a third of the online audience against the in-room sessions'
 }
};

/* Demos register a rebuild function so switching brand re-renders their content,
   not just their colours. */
const REBUILD=[];
let S=SCENARIOS.vse;
const fmt=n=>n.toLocaleString('en-GB');

function setBrand(k){
 S=SCENARIOS[k]||SCENARIOS.vse;
 const r=document.documentElement.style;
 r.setProperty('--demo-bg',S.bg); r.setProperty('--demo-accent',S.accent);
 r.setProperty('--demo-accent2',S.accent2); r.setProperty('--demo-panel',S.panel);
 r.setProperty('--demo-radius',S.radius); r.setProperty('--demo-font',S.font);
 r.setProperty('--demo-label-case',S.labelCase); r.setProperty('--demo-label-spacing',S.labelSpace);
 $$('.brand-name').forEach(e=>e.textContent=S.name);
 $$('.brand-event').forEach(e=>e.textContent=S.event);
 $$('.brand-when').forEach(e=>e.textContent=S.when);
 $$('.brand-sector').forEach(e=>e.textContent=S.sector);
 $$('.brandbar button').forEach(x=>x.classList.toggle('on',x.dataset.brand===k));
 const note=$('.brandbar .note');
 if(note) note.textContent='— ' + S.sector + ' · ' + fmt(S.registered) + ' registered';
 REBUILD.forEach(fn=>{try{fn();}catch(e){}});
}
$$('.brandbar button').forEach(b=>b.addEventListener('click',()=>setBrand(b.dataset.brand)));

/* ---------- Demo 01: audience participation ---------- */
if($('#engage-demo')){
 let aud=S.size, votes=0, qcount=0, reacts=0, recent=[];
 let POLLS=S.polls;
 let QUIZ=S.quiz;
 let pi=0, poll=POLLS[0], counts=[0,0,0,0], myVote=null, qi=0, quizAns=null, board={};
 let QS=S.questions;
 let qs=QS.map(q=>({...q,mine:false,answered:false,voted:false}));
 let CHAT=S.chat;
 const tabs=$$('#engage-demo .tabs button'); tabs.forEach(t=>t.addEventListener('click',()=>{tabs.forEach(x=>x.classList.remove('on'));t.classList.add('on');$$('#engage-demo .pane').forEach(p=>p.classList.toggle('hidden',p.dataset.pane!==t.dataset.tab));}));
 function renderPoll(){$('#poll-q').textContent=poll.q; const tot=counts.reduce((a,b)=>a+b,0)||1;
  $('#poll-opts').innerHTML=poll.o.map((o,i)=>`<button class="popt ${myVote===i?'mine':''}" data-i="${i}"><span>${o}</span><em>${Math.round(counts[i]/tot*100)}%</em><i style="width:${counts[i]/tot*100}%"></i></button>`).join('');
  $$('.popt').forEach(b=>b.addEventListener('click',()=>{if(myVote!==null)counts[myVote]--; myVote=+b.dataset.i; counts[myVote]++; votes++; $('#poll-hint').textContent='Thanks — your vote is in. Results are live on the broadcast.'; renderPoll(); renderBC();}));
  $('#st-votes').textContent=fmt(counts.reduce((a,b)=>a+b,0))+' votes';}
 function renderQA(){const sorted=[...qs].sort((a,b)=>b.u-a.u);
  $('#qa-list').innerHTML=sorted.map((q,i)=>`<div class="qa ${q.answered?'ans':''}"><p>${q.t}</p><div><span>${q.by}${q.mine?' (you)':''}</span><button data-q="${qs.indexOf(q)}" class="${q.voted?'v':''}">▲ ${q.u}</button>${q.answered?'<em>Answered</em>':''}</div></div>`).join('');
  $$('#qa-list button').forEach(b=>b.addEventListener('click',()=>{const q=qs[+b.dataset.q]; q.u+=q.voted?-1:1; q.voted=!q.voted; renderQA(); renderMod();}));
  $('#st-q').textContent=qs.length+' questions'; renderMod();}
 function renderMod(){const sorted=[...qs].sort((a,b)=>b.u-a.u).slice(0,5);
  $('#mod-queue').innerHTML=sorted.map(q=>`<div class="mq ${q.answered?'ans':''}"><span>▲${q.u}</span><p>${q.t}</p><button data-a="${qs.indexOf(q)}">${q.answered?'✓':'To presenter'}</button></div>`).join('');
  $$('#mod-queue button').forEach(b=>b.addEventListener('click',()=>{qs[+b.dataset.a].answered=true; bcMode='qa'; renderQA(); renderBC();}));}
 let bcMode='poll';
 function renderBC(){const c=$('#bc-content'); const tot=counts.reduce((a,b)=>a+b,0)||1;
  if(bcMode==='none'){c.innerHTML='';$('#bc-graphic').classList.add('off');return;} $('#bc-graphic').classList.remove('off');
  if(bcMode==='poll') c.innerHTML=`<div class="bc-title">Live poll · ${fmt(tot)} votes</div><div class="bc-q">${poll.q}</div>`+poll.o.map((o,i)=>`<div class="bc-bar"><span>${o}</span><i style="width:${counts[i]/tot*100}%"></i><em>${Math.round(counts[i]/tot*100)}%</em></div>`).join('');
  if(bcMode==='qa'){const q=[...qs].sort((a,b)=>b.u-a.u)[0]; c.innerHTML=`<div class="bc-title">Audience question</div><div class="bc-q">“${q.t}”</div><div class="bc-by">${q.by} · ▲${q.u}</div>`;}
  if(bcMode==='cloud'){const words=[['redundancy',9],['audio',8],['rehearsal',7],['captions',6],['budget',6],['hybrid',5],['platform',5],['latency',4],['speakers',4],['graphics',3],['lighting',3],['ROI',3]]; c.innerHTML='<div class="bc-title">One word: what keeps you up before an event?</div><div class="cloud">'+words.map(([w,s])=>`<span style="font-size:${.8+s*.16}rem;opacity:${.55+s*.05}">${w}</span>`).join('')+'</div>';}
  if(bcMode==='quiz'){const top=Object.entries(board).sort((a,b)=>b[1]-a[1]).slice(0,5); c.innerHTML='<div class="bc-title">Quiz leaderboard</div>'+top.map(([n,s],i)=>`<div class="bc-bar"><span>${i+1}. ${n}</span><i style="width:${s/30*100}%"></i><em>${s} pts</em></div>`).join('');}}
 function renderQuiz(){const q=QUIZ[qi]; $('#quiz-q').textContent=`Quiz · Q${qi+1}: ${q.q}`;
  $('#quiz-opts').innerHTML=q.o.map((o,i)=>`<button class="popt ${quizAns===i?(i===q.a?'mine':'wrong'):''} ${quizAns!==null&&i===q.a?'mine':''}" data-i="${i}"><span>${o}</span></button>`).join('');
  $$('#quiz-opts .popt').forEach(b=>b.addEventListener('click',()=>{if(quizAns!==null)return; quizAns=+b.dataset.i; if(quizAns===q.a){board['You']=(board['You']||0)+10;} renderQuiz(); renderBoard();}));
  renderBoard();}
 function renderBoard(){const top=Object.entries(board).sort((a,b)=>b[1]-a[1]).slice(0,5); $('#quiz-board').innerHTML='<h5>Leaderboard</h5>'+top.map(([n,s],i)=>`<div class="lb"><span>${i+1}. ${n}</span><b>${s}</b></div>`).join('');}
 function react(r){reacts++; recent.push(Date.now()); const l=$('#react-layer'); const e=document.createElement('span'); e.textContent=r; e.style.left=rnd(5,90)+'%'; l.appendChild(e); setTimeout(()=>e.remove(),2600); $('#st-react').textContent=fmt(reacts)+' reactions';}
 $$('.react-row button').forEach(b=>b.addEventListener('click',()=>react(b.dataset.r)));
 $('#qa-form').addEventListener('submit',e=>{e.preventDefault(); const v=$('#qa-input').value.trim(); if(!v)return; qs.push({t:v,u:1,by:'You',mine:true,answered:false,voted:true}); $('#qa-input').value=''; renderQA();});
 $('#chat-form').addEventListener('submit',e=>{e.preventDefault(); const v=$('#chat-input').value.trim(); if(!v)return; chat('You',v); $('#chat-input').value='';});
 function chat(n,m){const l=$('#chat-list'); l.insertAdjacentHTML('beforeend',`<div class="cm"><b>${n}</b>${m}</div>`); l.scrollTop=l.scrollHeight; if(l.children.length>30)l.firstChild.remove();}
 $$('.mod-btns [data-show]').forEach(b=>b.addEventListener('click',()=>{bcMode=b.dataset.show; renderBC();}));
 $('#new-poll').addEventListener('click',()=>{pi=(pi+1)%POLLS.length; poll=POLLS[pi]; counts=[0,0,0,0]; myVote=null; $('#poll-hint').textContent='New poll — tap to vote.'; bcMode='poll'; renderPoll(); renderBC(); tabs[0].click();});
 $('#next-quiz').addEventListener('click',()=>{qi=(qi+1)%QUIZ.length; quizAns=null; renderQuiz(); bcMode='quiz'; renderBC(); tabs[3].click();});
 /* simulated audience */
 ['Aisha K.','Tom W.','Dev P.','Marta L.','Sam H.'].forEach(n=>board[n]=rnd(10,30));
 setInterval(()=>{const i=rnd(0,3); counts[i]+=rnd(1,6); renderPoll(); if(bcMode==='poll')renderBC();},900);
 setInterval(()=>{const q=pick(qs); q.u+=1; renderQA(); if(bcMode==='qa')renderBC();},1800);
 setInterval(()=>{if(Math.random()<.7)react(pick(['👏','🔥','❤️','💡','🎉']));},700);
 setInterval(()=>{chat(pick(NAMES),pick(CHAT));},3200);
 setInterval(()=>{aud+=rnd(-12,15); $('#aud-count').textContent=fmt(aud)+' watching'; $('.bc-live').textContent='● LIVE · '+fmt(aud); recent=recent.filter(t=>Date.now()-t<60000); $('#react-count').textContent=recent.length+' reactions in the last minute';},1500);
 setTimeout(()=>{qs.push({t:'Can we run the same poll in the room and online at once?',u:3,by:'Lucy T.',mine:false,answered:false,voted:false}); renderQA();},6000);
 function applyScenario(){
  POLLS=S.polls; QUIZ=S.quiz; QS=S.questions; CHAT=S.chat;
  qs=QS.map(q=>({...q,mine:false,answered:false,voted:false}));
  pi=0; poll=POLLS[0]; counts=[0,0,0,0]; myVote=null; qi=0; quizAns=null;
  aud=S.size; board={};
  ['Aisha K.','Tom W.','Dev P.','Marta L.','Sam H.'].forEach(n=>board[n]=rnd(10,30));
  const lower=$('.bc-lower');
  if(lower){lower.querySelector('b').textContent=S.host.name;
   lower.querySelector('span').innerHTML=S.host.role+' · <span class="brand-name">'+S.name+'</span>';}
  const ac=$('#aud-count'); if(ac)ac.textContent=fmt(aud)+' watching';
  const bl=$('.bc-live'); if(bl)bl.textContent='● LIVE · '+fmt(aud);
  const cl=$('#chat-list'); if(cl)cl.innerHTML='';
  renderPoll(); renderQA(); renderQuiz(); renderBC();
  ['Priya S.','Tom W.'].forEach(n=>chat(n,pick(CHAT)));
 }
 REBUILD.push(applyScenario);
 applyScenario();
}

/* ---------- Demo 02: registration ---------- */
if($('#reg-demo')){
 const go=n=>{$$('.reg-step').forEach(s=>s.classList.toggle('hidden',s.dataset.step!==String(n))); $$('.reg-steps span').forEach(s=>s.classList.toggle('on',+s.dataset.step<=n)); window.scrollTo({top:$('#reg-demo').offsetTop-90,behavior:'smooth'});};
 const log=m=>{const l=$('#reg-events'); l.insertAdjacentHTML('beforeend',`<li>${m}</li>`); l.scrollTop=l.scrollHeight;};
 const total=()=>{const t=$('input[name=tk]:checked'); let p=+t.dataset.price; const promo=$('#promo').value.trim().toUpperCase(); if(promo==='EARLYBIRD'&&p)p=Math.round(p*.8); $('#tk-total').textContent='Total: £'+p+(promo==='EARLYBIRD'&&p?' (20% early bird)':'');};
 $$('input[name=tk]').forEach(i=>i.addEventListener('change',()=>{total(); log('Ticket selected: '+i.value+' · capacity checked');})); $('#promo').addEventListener('input',()=>{total(); if($('#promo').value.toUpperCase()==='EARLYBIRD')log('Promo code EARLYBIRD validated — 20% off');});
 $$('[data-next]').forEach(b=>b.addEventListener('click',()=>{const n=+b.dataset.next;
  if(n===3){const f=$('#r-first').value||'Guest', l=$('#r-last').value||'', t=$('input[name=tk]:checked').value; $('#c-name').textContent=f; $('#c-sum').textContent=t+' · '+S.event; $('#c-email').textContent=$('#r-email').value; $('#b-name').textContent=f+' '+l; $('#b-org').textContent=$('#r-org').value; $('#b-type').textContent=t; drawQR($('#qr'),f+l+Date.now());
   log('Attendee record created · ID att_'+rnd(10000,99999)); log('Synced to CRM (HubSpot) as contact + event membership'); log('Confirmation email sent with .ics and personal join link'); log('Reminders scheduled: 24h and 1h before'); if($('#r-consent').checked)log('Marketing consent recorded (opt-in, timestamped)'); log('Session interest "'+$('#r-track').value+'" saved to profile for agenda personalisation');}
  if(n===2)log('Form fields validated · privacy notice linked');
  go(n);}));
 $('#scan-btn').addEventListener('click',()=>{const f=$('#scan-frame'); f.classList.add('hit'); setTimeout(()=>f.classList.remove('hit'),900); const nm=$('#b-name').textContent, t=$('#b-type').textContent;
  $('#scan-result').innerHTML=`<b>✓ ${nm}</b> — ${t} · ${$('#b-org').textContent}<br><small>Checked in ${new Date().toLocaleTimeString('en-GB',{hour:'2-digit',minute:'2-digit'})} · badge printing…</small> <button id="scan-btn" class="ghost-btn">Scan another</button>`;
  $('#checkin-log').insertAdjacentHTML('afterbegin',`<div>${new Date().toLocaleTimeString('en-GB',{hour:'2-digit',minute:'2-digit',second:'2-digit'})} · ${nm} · ${t} · badge #${rnd(100,999)}</div>`); log('Check-in recorded · attendance status live in Insight · badge sent to printer');
  $('#scan-btn').addEventListener('click',()=>{const n=pick(NAMES); $('#checkin-log').insertAdjacentHTML('afterbegin',`<div>${new Date().toLocaleTimeString('en-GB')} · ${n} · In-person · badge #${rnd(100,999)}</div>`);});});
 function drawQR(el,seed){let h=0; for(const c of seed)h=(h*31+c.charCodeAt(0))>>>0; const n=21, cells=[]; for(let i=0;i<n*n;i++){h^=h<<13;h^=h>>>17;h^=h<<5;h>>>=0; cells.push((h&7)<3);}
  const finder=(x,y)=>{for(let i=0;i<7;i++)for(let j=0;j<7;j++){const on=(i===0||i===6||j===0||j===6||(i>1&&i<5&&j>1&&j<5)); cells[(y+i)*n+x+j]=on;}}; finder(0,0);finder(n-7,0);finder(0,n-7);
  el.innerHTML='<div class="qrgrid">'+cells.map(c=>`<i class="${c?'on':''}"></i>`).join('')+'</div><small>sample QR</small>';}
 function applyScenario(){
  const hero=$('.reg-hero');
  if(hero){hero.querySelector('.reg-title').textContent=S.event;
   hero.querySelector('p').textContent=S.when;}
  const tw=$('.tickets');
  if(tw) tw.innerHTML=S.tickets.map((t,i)=>
   `<label class="ticket"><input type="radio" name="tk" value="${t.v}" data-price="${t.p}" ${i===0?'checked':''}>`+
   `<div><b>${t.v}</b><span>${t.d}</span></div><em>${t.label}</em></label>`).join('');
  const role=$('#r-role'); if(role) role.innerHTML=S.roles.map(r=>`<option>${r}</option>`).join('');
  const track=$('#r-track'); if(track) track.innerHTML=S.tracks.map(r=>`<option>${r}</option>`).join('');
  $$('input[name=tk]').forEach(i=>i.addEventListener('change',()=>{
    total(); log('Ticket selected: '+i.value+' · capacity checked');}));
  const l=$('#reg-events');
  if(l) l.innerHTML='<li>Registration page rendered in '+S.name+' brand</li>';
  total();
 }
 REBUILD.push(applyScenario);
 applyScenario();
}

/* ---------- Demo 03: event hub ---------- */
if($('#hub-demo')){
 let AG=S.agenda;
 let mine=new Set([1,4,7]);
 const views=$$('.hub-nav button'); views.forEach(b=>b.addEventListener('click',()=>{views.forEach(x=>x.classList.remove('on')); b.classList.add('on'); $$('.hub-view').forEach(v=>v.classList.toggle('hidden',v.dataset.view!==b.dataset.view));}));
 let track='all'; $$('.track-tabs button').forEach(b=>b.addEventListener('click',()=>{$$('.track-tabs button').forEach(x=>x.classList.remove('on')); b.classList.add('on'); track=b.dataset.track; renderAg();}));
 function renderAg(){$('#agenda-list').innerHTML=AG.filter(a=>track==='all'||a[1]===track).map((a,i)=>{const idx=AG.indexOf(a); const live=idx===1; return `<div class="ag ${live?'live':''}"><span class="t">${a[0]}</span><div><b>${a[2]}</b>${a[3]?`<span>${a[3]}</span>`:''}<em>Track ${a[1]}${live?' · LIVE NOW':''}</em></div><button data-i="${idx}" class="${mine.has(idx)?'on':''}">${mine.has(idx)?'✓ In my schedule':'+ Add'}</button></div>`;}).join('');
  $$('#agenda-list button').forEach(b=>b.addEventListener('click',()=>{const i=+b.dataset.i; mine.has(i)?mine.delete(i):mine.add(i); renderAg();}));}
 renderAg();
 let SP=S.speakers;
 let EX=S.expo;
 let PEOPLE=S.people;
 let VOD=[];
 let QA=[];
 $$('.sess-side .tabs button').forEach(b=>b.addEventListener('click',()=>{$$('.sess-side .tabs button').forEach(x=>x.classList.remove('on')); b.classList.add('on'); const k=b.dataset.stab; $('#sess-qa').style.display=k==='qa'?'':'none';}));

 function applyScenario(){
  AG=S.agenda; SP=S.speakers; EX=S.expo; PEOPLE=S.people;
  mine=new Set([1, Math.min(4,AG.length-1)]);
  // agenda day + track tab labels
  const head=$('.hub-view[data-view="agenda"] h4');
  if(head) head.textContent=S.when.split('·')[0].trim();
  $$('.track-tabs button').forEach(b=>{const k=b.dataset.track;
    if(k!=='all'&&S.trackNames[k]) b.textContent=S.trackNames[k];});
  renderAg();

  $('#speaker-cards').innerHTML=SP.map(sp=>`<div class="hcard"><div class="av">${sp[0].split(' ').map(x=>x[0]).join('')}</div><b>${sp[0]}</b><span>${sp[1]}</span><em>${sp[2]}</em><button class="ghost-btn">Request meeting</button></div>`).join('');
  $('#expo-cards').innerHTML=EX.map(e=>`<div class="hcard booth"><em class="tier">${e[2]}</em><b>${e[0]}</b><span>${e[1]}</span><div class="booth-acts"><button class="ghost-btn lead">Leave my details</button><button class="ghost-btn">Video</button><button class="ghost-btn">Chat</button></div></div>`).join('');
  $$('.booth .lead').forEach(b=>b.addEventListener('click',()=>{b.textContent='✓ Details shared — lead captured'; b.disabled=true;}));

  $('#net-people').innerHTML=PEOPLE.map((pp,i)=>`<div class="person"><div class="av">${pp[0].split(' ').map(x=>x[0]).join('')}</div><div><b>${pp[0]}</b><span>${pp[1]}</span><em>Matched: ${pp[2]}</em></div><button class="ghost-btn" data-p="${i}">Request 1:1</button></div>`).join('');
  $$('#net-people button').forEach(b=>b.addEventListener('click',()=>{const pp=PEOPLE[+b.dataset.p]; b.textContent='Requested'; b.disabled=true; setTimeout(()=>{b.textContent='✓ Accepted'; const m=$('#net-meetings'); if(m.querySelector('.hint'))m.innerHTML=''; m.insertAdjacentHTML('beforeend',`<div class="rt"><b>${pp[0]}</b><span>12:${rnd(30,55)} · 15 min · video</span><button class="ghost-btn">Join</button></div>`);},1500);}));
  const hint=$('.net-grid .hint'); if(hint) hint.textContent='Matched on your interests: '+S.tracks.slice(0,2).join(', ').toLowerCase();
  const rts=$$('.net-grid .rt');
  S.roundtables.forEach((r,i)=>{ if(rts[i]){rts[i].querySelector('b').textContent=r[0]; rts[i].querySelector('span').textContent=r[1];} });

  // on-demand library, built from the agenda so it always matches the show
  const talks=AG.filter(a=>a[3]).slice(0,5);
  VOD=talks.map((a,i)=>[a[2], (30+i*4)+':'+String(rnd(10,59)).padStart(2,'0'), fmt(Math.round(S.size*(1.2-i*0.13)))+' views']);
  VOD.push(['Highlights reel','1:30',fmt(Math.round(S.size*2.4))+' views']);
  $('#vod-cards').innerHTML=VOD.map(v=>`<div class="hcard vod"><div class="thumb"><span>▶</span></div><b>${v[0]}</b><span>${v[1]} · ${v[2]} · captions · chapters</span></div>`).join('');

  // session room: title, watching count and the Q&A beside it
  const pl=$('.player-lower');
  if(pl && AG[1]){pl.querySelector('b').textContent=AG[1][2]; pl.querySelector('span').textContent=(S.trackNames.A||'Main stage')+' · '+AG[1][0];}
  const meta=$('.sess-meta span'); if(meta) meta.textContent=fmt(S.size)+' watching';
  QA=S.questions.slice(0,3).map(q=>[q.by,q.t,q.u]);
  $('#sess-qa').innerHTML='<div class="sq-list">'+QA.map(q=>`<div class="qa"><p>${q[1]}</p><div><span>${q[0]}</span><button>▲ ${q[2]}</button></div></div>`).join('')+'</div><form class="sq-form"><input placeholder="Ask a question…"><button type="submit">Ask</button></form>';
  $('.sq-form').addEventListener('submit',e=>{e.preventDefault(); const i=$('.sq-form input'); if(!i.value.trim())return; $('.sq-list').insertAdjacentHTML('afterbegin',`<div class="qa"><p>${i.value}</p><div><span>You</span><button>▲ 1</button></div></div>`); i.value='';});
 }
 REBUILD.push(applyScenario);
 applyScenario();
}

/* ---------- Demo 04: analytics ---------- */
if($('#dash-demo')){
 let RO=S.runOrder;
 let peak=S.peak, t=0, speed=1, series=[], uniq=new Set(), leads=0, q=[];
 let sponsors=[];
 const cv=$('#curve'), ctx=cv.getContext('2d');
 $$('.dash-ctl [data-speed]').forEach(b=>b.addEventListener('click',()=>{$$('.dash-ctl [data-speed]').forEach(x=>x.classList.remove('on')); b.classList.add('on'); speed=+b.dataset.speed;}));
 $('#ro-strip').innerHTML=RO.slice(0,-1).map(r=>`<span>${r[0]}<br>${r[1]}</span>`).join('');
 const log=m=>{const l=$('#ev-log'); l.insertAdjacentHTML('afterbegin',`<div><span>${tstr()}</span>${m}</div>`); if(l.children.length>14)l.lastChild.remove();};
 const tstr=()=>{const m=startMin+t; return String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0');};
 function target(){const m=startMin+t; for(let i=0;i<RO.length-1;i++){const a=RO[i],b=RO[i+1]; const am=+a[0].slice(0,2)*60+ +a[0].slice(3), bm=+b[0].slice(0,2)*60+ +b[0].slice(3); if(m>=am&&m<bm){const p=(m-am)/(bm-am); return (a[2]+(b[2]-a[2])*p)*peak;}} return 0;}
 function draw(){const W=cv.width,H=cv.height; ctx.clearRect(0,0,W,H); ctx.strokeStyle='rgba(255,255,255,.08)'; for(let i=1;i<4;i++){ctx.beginPath();ctx.moveTo(0,H*i/4);ctx.lineTo(W,H*i/4);ctx.stroke();}
  ctx.strokeStyle='rgba(255,255,255,.12)'; RO.slice(0,-1).forEach(r=>{const m=+r[0].slice(0,2)*60+ +r[0].slice(3)-startMin; const x=m/dayMin*W; ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H);ctx.stroke();});
  if(series.length<2)return; const acc=getComputedStyle(document.documentElement).getPropertyValue('--demo-accent')||'#6a9799';
  ctx.beginPath(); series.forEach((v,i)=>{const x=i/dayMin*W, y=H-v/(peak*1.1)*H; i?ctx.lineTo(x,y):ctx.moveTo(x,y);}); ctx.lineTo(series.length/dayMin*W,H); ctx.lineTo(0,H); ctx.closePath(); ctx.fillStyle=acc.trim()+'33'; ctx.fill();
  ctx.beginPath(); series.forEach((v,i)=>{const x=i/dayMin*W, y=H-v/(peak*1.1)*H; i?ctx.lineTo(x,y):ctx.moveTo(x,y);}); ctx.strokeStyle=acc.trim(); ctx.lineWidth=2.5; ctx.stroke();}
 let watch=0, startMin=540, dayMin=450, evs={}, failAt=0, fixAt=0;
 function tick(){if(t>=dayMin)return; t++; const tv=target(); const v=Math.max(0,Math.round(tv+rnd(-25,25))); series.push(v); for(let i=0;i<Math.round(v/20);i++)uniq.add(rnd(1,S.registered)); watch+= v/1000;
  if(Math.random()<.04)leads+=rnd(1,3); sponsors.forEach(s=>{s[1]+=Math.round(v/40); if(Math.random()<.15)s[2]++; if(Math.random()<.04)s[3]++;});
  if(t%15===0&&Math.random()<.5){const i=rnd(0,q.length-1); q[i][1]+=rnd(1,4);}
  if(evs[t])log(evs[t]); if(t===failAt){$('#k-health').textContent='Failover';$('#k-health').className='warn';$('#k-health-d').textContent='on backup encoder';} if(t===fixAt){$('#k-health').textContent='Good';$('#k-health').className='ok';$('#k-health-d').textContent='both encoders up';}
  $('#k-conc').textContent=v.toLocaleString(); $('#k-conc-d').textContent='peak '+Math.max(...series).toLocaleString()+' · '+tstr(); $('#k-uniq').textContent=uniq.size.toLocaleString(); $('#k-watch').textContent=Math.round(watch/Math.max(1,uniq.size)*60)+'m'; $('#k-eng').textContent=Math.round(30+t/dayMin*42); $('#k-leads').textContent=leads; $('#k-leads-d').textContent=Math.round(leads*.62)+' MQL · synced to CRM';
  if(t%3===0){draw(); $('#eng-bars').innerHTML=RO.slice(0,-1).filter(r=>+r[0].slice(0,2)*60+ +r[0].slice(3)-startMin<=t).map(r=>`<div class="bc-bar"><span>${r[1]}</span><i style="width:${r[2]*100}%"></i><em>${Math.round(r[2]*100)}</em></div>`).join('');
   $('#top-q').innerHTML=[...q].sort((a,b)=>b[1]-a[1]).map(x=>`<li>${x[0]} <b>▲${x[1]}</b></li>`).join('');
   $('#sponsor-tbl').innerHTML='<tr><th>Sponsor</th><th>Impr.</th><th>Clicks</th><th>Leads</th></tr>'+sponsors.map(s=>`<tr><td>${s[0]}</td><td>${s[1].toLocaleString()}</td><td>${s[2]}</td><td>${s[3]}</td></tr>`).join('');}}
 setInterval(()=>{for(let i=0;i<speed;i++)tick();},400);
 $('#dash-report').addEventListener('click',()=>{const pk=Math.max(0,...series); $('#report').classList.remove('hidden');
  $('#report-body').innerHTML=`<p><strong>Objective:</strong> ${S.objective}.</p><p><strong>Result:</strong> ${uniq.size.toLocaleString()} unique attendees of '+fmt(S.registered)+' registered (${Math.round(uniq.size/S.registered*100)}% attendance), peak concurrent ${pk.toLocaleString()}, average watch time ${$('#k-watch').textContent}, ${leads} leads scored (${Math.round(leads*.62)} MQL). Stream health: one automatic encoder failover at 11:15 with no audience impact.</p><p><strong>What worked:</strong> ${RO[1][1]} and ${RO[3][1]} held the audience (engagement ${Math.round(RO[1][2]*100)}/${Math.round(RO[3][2]*100)}); polls averaged 58% response; expo produced ${sponsors.reduce((a,s)=>a+s[3],0)} booth leads.</p><p><strong>What didn't:</strong> ${S.weak}; lunch ran long on the stream (holding loop 55 min).</p><p><strong>Recommendations:</strong> move the platforms session after lunch (agenda owner, March); shorten the lunch stream break to 40 min with a sponsored segment (production); human captions for the keynote (finance, £1,200).</p><p class="hint">Generated from Insight data. Edit, attach the attendance curve, send.</p>`; $('#report').scrollIntoView({behavior:'smooth'});});
 function applyScenario(){
  RO=S.runOrder; peak=S.peak;
  startMin=+RO[0][0].slice(0,2)*60 + +RO[0][0].slice(3);
  dayMin=(+RO[RO.length-1][0].slice(0,2)*60 + +RO[RO.length-1][0].slice(3)) - startMin;
  t=0; series=[]; uniq=new Set(); leads=0; watch=0;
  q=S.questions.map(x=>[x.t,x.u]);
  sponsors=S.sponsors.map(n=>[n,0,0,0]);
  evs=Object.fromEntries(Object.entries({
   '0.02':'Stream started · both encoders healthy',
   '0.10':RO[1][1]+' on air · concurrent climbing',
   '0.18':'Poll 1 launched · 61% response in 90s',
   '0.28':'Peak concurrent so far',
   '0.42':'Primary encoder failover → backup (audience impact: none)',
   '0.43':'Primary encoder restored',
   '0.58':'Expo traffic up · booth leads arriving',
   '0.74':RO[Math.min(RO.length-3,6)][1]+' · reactions climbing',
   '0.90':'On-demand hub published · sessions chaptered',
   '0.99':'Stream ended · recordings saved · report ready'
  }).map(([k,v])=>[Math.round(+k*dayMin),v]));
  failAt=Math.round(0.42*dayMin); fixAt=failAt+1;
  $('#ro-strip').innerHTML=RO.slice(0,-1).map(r=>`<span>${r[0]}<br>${r[1]}</span>`).join('');
  const reg=$('#k-uniq')&&$('#k-uniq').nextElementSibling; if(reg) reg.textContent='of '+fmt(S.registered)+' registered';
  const ev=$('.dash-head'); if(ev){const b=ev.querySelector('div'); if(b) b.innerHTML='<b class="brand-name">'+S.name+'</b> · <span class="brand-event">'+S.event+'</span> · <span class="bc-live">● LIVE</span>';}
  $('#ev-log').innerHTML=''; $('#report').classList.add('hidden');
  ['#k-conc','#k-uniq','#k-watch','#k-eng','#k-leads'].forEach(id=>{const e=$(id); if(e)e.textContent='0';});
  draw(); log('Dashboard connected · waiting for stream');
 }
 REBUILD.push(applyScenario);
 applyScenario();
}
 if($('.brandbar')) setBrand('vse');
})();
