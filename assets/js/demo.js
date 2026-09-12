/* VSE Platform demos — fully client-side, simulated audience, no storage */
(function(){
const $=(s,r)=>(r||document).querySelector(s), $$=(s,r)=>[...(r||document).querySelectorAll(s)];
const rnd=(a,b)=>Math.floor(Math.random()*(b-a+1))+a, pick=a=>a[rnd(0,a.length-1)];
const NAMES=['Priya S.','Tom W.','Aisha K.','Ben O.','Marta L.','Dev P.','Chloe R.','Sam H.','Ravi N.','Jess M.','Omar F.','Lucy T.','Kwame A.','Hannah B.','Leo G.','Nadia E.'];

/* ---------- brand switcher ---------- */
const BRANDS={
 vse:{name:'Virtual Studio Events',bg:'#212b54',accent:'#6a9799',accent2:'#9fc4c5',panel:'#2b3663'},
 retail:{name:'Northfield Retail',bg:'#1f1a2e',accent:'#e0603a',accent2:'#f3a683',panel:'#2c2540'},
 charity:{name:'Reach Together',bg:'#14322b',accent:'#f2b544',accent2:'#f8d58a',panel:'#1d4438'},
 tech:{name:'Helix Software',bg:'#0f172a',accent:'#38bdf8',accent2:'#7dd3fc',panel:'#1e293b'}};
function setBrand(k){const b=BRANDS[k]; const r=document.documentElement.style;
 r.setProperty('--demo-bg',b.bg); r.setProperty('--demo-accent',b.accent); r.setProperty('--demo-accent2',b.accent2); r.setProperty('--demo-panel',b.panel);
 $$('.brand-name').forEach(e=>e.textContent=b.name); $$('.brandbar button').forEach(x=>x.classList.toggle('on',x.dataset.brand===k));}
$$('.brandbar button').forEach(b=>b.addEventListener('click',()=>setBrand(b.dataset.brand))); if($('.brandbar')) setBrand('vse');

/* ---------- Demo 01: audience participation ---------- */
if($('#engage-demo')){
 let aud=1214, votes=0, qcount=0, reacts=0, recent=[];
 const POLLS=[{q:'Which format will you run most in 2027?',o:['Virtual','Hybrid','In-person','Not sure']},{q:'Biggest risk on your last event?',o:['Internet','Speakers','Platform','Budget']},{q:'How do you measure success?',o:['Attendance','Engagement','Leads','Feedback']}];
 const QUIZ=[{q:"What's the recommended keyframe interval for live streaming?",o:['1 second','2 seconds','5 seconds','10 seconds'],a:1},{q:'What does mix-minus remove from a remote guest\'s return feed?',o:['Music','The presenter','Their own voice','Room noise'],a:2},{q:'Standard HLS latency is roughly…',o:['0.5 s','3 s','15–45 s','2 minutes'],a:2}];
 let pi=0, poll=POLLS[0], counts=[0,0,0,0], myVote=null, qi=0, quizAns=null, board={};
 const QS=[{t:'How do you keep remote speakers looking as good as the studio presenters?',u:42,by:'Aisha K.'},{t:'What redundancy do you actually run on the internet line?',u:37,by:'Tom W.'},{t:'Is 4K ever worth the bandwidth for a conference?',u:21,by:'Dev P.'},{t:'Do you recommend human or automated captions for internal events?',u:18,by:'Chloe R.'}];
 const qs=QS.map(q=>({...q,mine:false,answered:false,voted:false}));
 const CHAT=['Great audio today 👌','Can we get the slides afterwards?','Hello from Leeds!','The hybrid checklist guide is gold','Watching from the warehouse canteen 🙋','Question submitted!'];
 const tabs=$$('#engage-demo .tabs button'); tabs.forEach(t=>t.addEventListener('click',()=>{tabs.forEach(x=>x.classList.remove('on'));t.classList.add('on');$$('#engage-demo .pane').forEach(p=>p.classList.toggle('hidden',p.dataset.pane!==t.dataset.tab));}));
 const fmt=n=>n.toLocaleString('en-GB');
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
 renderPoll(); renderQA(); renderQuiz(); renderBC(); ['Priya S.','Tom W.'].forEach(n=>chat(n,pick(CHAT)));
}

/* ---------- Demo 02: registration ---------- */
if($('#reg-demo')){
 const go=n=>{$$('.reg-step').forEach(s=>s.classList.toggle('hidden',s.dataset.step!==String(n))); $$('.reg-steps span').forEach(s=>s.classList.toggle('on',+s.dataset.step<=n)); window.scrollTo({top:$('#reg-demo').offsetTop-90,behavior:'smooth'});};
 const log=m=>{const l=$('#reg-events'); l.insertAdjacentHTML('beforeend',`<li>${m}</li>`); l.scrollTop=l.scrollHeight;};
 const total=()=>{const t=$('input[name=tk]:checked'); let p=+t.dataset.price; const promo=$('#promo').value.trim().toUpperCase(); if(promo==='EARLYBIRD'&&p)p=Math.round(p*.8); $('#tk-total').textContent='Total: £'+p+(promo==='EARLYBIRD'&&p?' (20% early bird)':'');};
 $$('input[name=tk]').forEach(i=>i.addEventListener('change',()=>{total(); log('Ticket selected: '+i.value+' · capacity checked');})); $('#promo').addEventListener('input',()=>{total(); if($('#promo').value.toUpperCase()==='EARLYBIRD')log('Promo code EARLYBIRD validated — 20% off');});
 $$('[data-next]').forEach(b=>b.addEventListener('click',()=>{const n=+b.dataset.next;
  if(n===3){const f=$('#r-first').value||'Guest', l=$('#r-last').value||'', t=$('input[name=tk]:checked').value; $('#c-name').textContent=f; $('#c-sum').textContent=t+' · Annual Conference 2027 · 14 May'; $('#c-email').textContent=$('#r-email').value; $('#b-name').textContent=f+' '+l; $('#b-org').textContent=$('#r-org').value; $('#b-type').textContent=t; drawQR($('#qr'),f+l+Date.now());
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
 total();
}

/* ---------- Demo 03: event hub ---------- */
if($('#hub-demo')){
 const AG=[['09:00','A','Doors, holding loop & welcome',''],['09:30','A','Keynote: Events that survive contact with reality','Sarah Okafor'],['10:15','B','Registration data & GDPR without the fear','Marta L.'],['10:15','C','Workshop: writing a run order the gallery can use','James Jones'],['11:00','A','Panel: hybrid — owning the join','Ben O\'Dwyer, Aisha K., Tom W.'],['11:45','B','Platform comparison: Teams, Zoom, YouTube or dedicated?','Dev P.'],['12:30','A','Lunch · expo & 1:1 meetings',''],['13:30','A','Case study: a 75,000-viewer awards show','James Jones'],['14:15','C','Workshop: lighting for camera in 45 minutes','Chloe R.'],['15:00','A','Measuring ROI: a model finance accepts','Ben O\'Dwyer'],['15:45','A','Closing & on-demand launch','Sarah Okafor']];
 const mine=new Set([1,4,7]);
 const views=$$('.hub-nav button'); views.forEach(b=>b.addEventListener('click',()=>{views.forEach(x=>x.classList.remove('on')); b.classList.add('on'); $$('.hub-view').forEach(v=>v.classList.toggle('hidden',v.dataset.view!==b.dataset.view));}));
 let track='all'; $$('.track-tabs button').forEach(b=>b.addEventListener('click',()=>{$$('.track-tabs button').forEach(x=>x.classList.remove('on')); b.classList.add('on'); track=b.dataset.track; renderAg();}));
 function renderAg(){$('#agenda-list').innerHTML=AG.filter(a=>track==='all'||a[1]===track).map((a,i)=>{const idx=AG.indexOf(a); const live=a[0]==='09:30'; return `<div class="ag ${live?'live':''}"><span class="t">${a[0]}</span><div><b>${a[2]}</b>${a[3]?`<span>${a[3]}</span>`:''}<em>Track ${a[1]}${live?' · LIVE NOW':''}</em></div><button data-i="${idx}" class="${mine.has(idx)?'on':''}">${mine.has(idx)?'✓ In my schedule':'+ Add'}</button></div>`;}).join('');
  $$('#agenda-list button').forEach(b=>b.addEventListener('click',()=>{const i=+b.dataset.i; mine.has(i)?mine.delete(i):mine.add(i); renderAg();}));}
 renderAg();
 const SP=[['Sarah Okafor','Head of Events, Northfield Retail','Keynote'],['James Jones','Co-founder, Virtual Studio Events','Run orders · Awards case study'],["Ben O'Dwyer",'Co-founder, Virtual Studio Events','Hybrid panel · ROI'],['Aisha K.','Broadcast engineer','Hybrid panel'],['Marta L.','Data protection lead','GDPR'],['Dev P.','Platform consultant','Platform comparison'],['Chloe R.','Lighting director','Lighting workshop'],['Tom W.','Venue AV manager','Hybrid panel']];
 $('#speaker-cards').innerHTML=SP.map(s=>`<div class="hcard"><div class="av">${s[0].split(' ').map(x=>x[0]).join('')}</div><b>${s[0]}</b><span>${s[1]}</span><em>${s[2]}</em><button class="ghost-btn">Request meeting</button></div>`).join('');
 const EX=[['Granary Digital','Studio partner · Podcast & broadcast studios','Gold'],['StreamKit','Bonded cellular encoders','Silver'],['CaptionWorks','Human live captioning & BSL','Silver'],['Helix Software','Event CRM integration','Bronze'],['Lumen Hire','LED walls & lighting','Bronze'],['Northfield Retail','Headline sponsor','Headline']];
 $('#expo-cards').innerHTML=EX.map(e=>`<div class="hcard booth"><em class="tier">${e[2]}</em><b>${e[0]}</b><span>${e[1]}</span><div class="booth-acts"><button class="ghost-btn lead">Leave my details</button><button class="ghost-btn">Video</button><button class="ghost-btn">Chat</button></div></div>`).join('');
 $$('.booth .lead').forEach(b=>b.addEventListener('click',()=>{b.textContent='✓ Details shared — lead captured'; b.disabled=true;}));
 const PEOPLE=[['Aisha K.','Broadcast engineer · Leeds','hybrid production'],['Dev P.','Platform consultant · London','platforms & data'],['Nadia E.','Internal comms lead · Manchester','hybrid production'],['Omar F.','Events manager · Bristol','platforms & data'],['Hannah B.','Marketing ops · Remote','platforms & data']];
 $('#net-people').innerHTML=PEOPLE.map((p,i)=>`<div class="person"><div class="av">${p[0].split(' ').map(x=>x[0]).join('')}</div><div><b>${p[0]}</b><span>${p[1]}</span><em>Matched: ${p[2]}</em></div><button class="ghost-btn" data-p="${i}">Request 1:1</button></div>`).join('');
 $$('#net-people button').forEach(b=>b.addEventListener('click',()=>{const p=PEOPLE[+b.dataset.p]; b.textContent='Requested'; b.disabled=true; setTimeout(()=>{b.textContent='✓ Accepted'; const m=$('#net-meetings'); if(m.querySelector('.hint'))m.innerHTML=''; m.insertAdjacentHTML('beforeend',`<div class="rt"><b>${p[0]}</b><span>12:${rnd(30,55)} · 15 min · video</span><button class="ghost-btn">Join</button></div>`);},1500);}));
 const VOD=[['Keynote: Events that survive contact with reality','47:12','1,980 views'],['Panel: hybrid — owning the join','44:05','1,120 views'],['Case study: a 75,000-viewer awards show','38:40','1,640 views'],['Measuring ROI: a model finance accepts','41:22','870 views'],['Highlights reel','1:30','3,210 views'],['Workshop: run orders','52:10','610 views']];
 $('#vod-cards').innerHTML=VOD.map(v=>`<div class="hcard vod"><div class="thumb"><span>▶</span></div><b>${v[0]}</b><span>${v[1]} · ${v[2]} · captions · chapters</span></div>`).join('');
 const QA=[['Aisha K.','How do you keep remote speakers looking as good as the studio?',42],['Tom W.','What redundancy do you run on the internet line?',37],['Dev P.','Is 4K ever worth it for a conference?',21]];
 $('#sess-qa').innerHTML='<div class="sq-list">'+QA.map(q=>`<div class="qa"><p>${q[1]}</p><div><span>${q[0]}</span><button>▲ ${q[2]}</button></div></div>`).join('')+'</div><form class="sq-form"><input placeholder="Ask a question…"><button type="submit">Ask</button></form>';
 $('.sq-form').addEventListener('submit',e=>{e.preventDefault(); const i=$('.sq-form input'); if(!i.value.trim())return; $('.sq-list').insertAdjacentHTML('afterbegin',`<div class="qa"><p>${i.value}</p><div><span>You</span><button>▲ 1</button></div></div>`); i.value='';});
 $$('.sess-side .tabs button').forEach(b=>b.addEventListener('click',()=>{$$('.sess-side .tabs button').forEach(x=>x.classList.remove('on')); b.classList.add('on'); const k=b.dataset.stab; $('#sess-qa').style.display=k==='qa'?'':'none';}));
}

/* ---------- Demo 04: analytics ---------- */
if($('#dash-demo')){
 const RO=[['09:00','Welcome',0.35],['09:30','Keynote',0.95],['10:15','Track sessions',0.72],['11:00','Hybrid panel',0.88],['11:45','Platforms',0.6],['12:30','Lunch/expo',0.3],['13:30','Awards case study',0.82],['14:15','Workshops',0.55],['15:00','ROI',0.7],['15:45','Close',0.5],['16:30','End',0.1]];
 const peak=1610; let t=0, speed=1, series=[], uniq=new Set(), leads=0, q=[['How do you keep remote speakers looking as good as the studio?',42],['What redundancy do you run on the internet line?',37],['Is 4K ever worth the bandwidth?',21],['Human or automated captions for internal events?',18],['Can polls run in the room and online at once?',12]];
 const sponsors=[['Northfield Retail',0,0,0],['Granary Digital',0,0,0],['StreamKit',0,0,0],['CaptionWorks',0,0,0]];
 const cv=$('#curve'), ctx=cv.getContext('2d');
 $$('.dash-ctl [data-speed]').forEach(b=>b.addEventListener('click',()=>{$$('.dash-ctl [data-speed]').forEach(x=>x.classList.remove('on')); b.classList.add('on'); speed=+b.dataset.speed;}));
 $('#ro-strip').innerHTML=RO.slice(0,-1).map(r=>`<span>${r[0]}<br>${r[1]}</span>`).join('');
 const log=m=>{const l=$('#ev-log'); l.insertAdjacentHTML('afterbegin',`<div><span>${tstr()}</span>${m}</div>`); if(l.children.length>14)l.lastChild.remove();};
 const tstr=()=>{const m=540+t; return String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0');};
 function target(){const m=540+t; for(let i=0;i<RO.length-1;i++){const a=RO[i],b=RO[i+1]; const am=+a[0].slice(0,2)*60+ +a[0].slice(3), bm=+b[0].slice(0,2)*60+ +b[0].slice(3); if(m>=am&&m<bm){const p=(m-am)/(bm-am); return (a[2]+(b[2]-a[2])*p)*peak;}} return 0;}
 function draw(){const W=cv.width,H=cv.height; ctx.clearRect(0,0,W,H); ctx.strokeStyle='rgba(255,255,255,.08)'; for(let i=1;i<4;i++){ctx.beginPath();ctx.moveTo(0,H*i/4);ctx.lineTo(W,H*i/4);ctx.stroke();}
  ctx.strokeStyle='rgba(255,255,255,.12)'; RO.slice(0,-1).forEach(r=>{const m=+r[0].slice(0,2)*60+ +r[0].slice(3)-540; const x=m/450*W; ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H);ctx.stroke();});
  if(series.length<2)return; const acc=getComputedStyle(document.documentElement).getPropertyValue('--demo-accent')||'#6a9799';
  ctx.beginPath(); series.forEach((v,i)=>{const x=i/450*W, y=H-v/(peak*1.1)*H; i?ctx.lineTo(x,y):ctx.moveTo(x,y);}); ctx.lineTo(series.length/450*W,H); ctx.lineTo(0,H); ctx.closePath(); ctx.fillStyle=acc.trim()+'33'; ctx.fill();
  ctx.beginPath(); series.forEach((v,i)=>{const x=i/450*W, y=H-v/(peak*1.1)*H; i?ctx.lineTo(x,y):ctx.moveTo(x,y);}); ctx.strokeStyle=acc.trim(); ctx.lineWidth=2.5; ctx.stroke();}
 let watch=0;
 function tick(){if(t>=450)return; t++; const tv=target(); const v=Math.max(0,Math.round(tv+rnd(-25,25))); series.push(v); for(let i=0;i<Math.round(v/20);i++)uniq.add(rnd(1,2140)); watch+= v/1000;
  if(Math.random()<.04)leads+=rnd(1,3); sponsors.forEach(s=>{s[1]+=Math.round(v/40); if(Math.random()<.15)s[2]++; if(Math.random()<.04)s[3]++;});
  if(t%15===0&&Math.random()<.5){const i=rnd(0,q.length-1); q[i][1]+=rnd(1,4);}
  const evs={5:'Stream started · both encoders healthy',30:'Keynote on air · concurrent climbing',52:'Poll 1 launched · 61% response in 90s',75:'Peak concurrent so far',120:'Hybrid panel · 4 remote guests live',135:'Primary encoder failover → backup (audience impact: none)',136:'Primary encoder restored',210:'Lunch · expo traffic up · 38 booth leads',270:'Awards case study · reactions 2.1/min',330:'Workshops · breakout rooms opened (3)',405:'On-demand hub published · 4 sessions chaptered',449:'Stream ended · recordings saved · report ready'};
  if(evs[t])log(evs[t]); if(t===135){$('#k-health').textContent='Failover';$('#k-health').className='warn';$('#k-health-d').textContent='on backup encoder';} if(t===136){$('#k-health').textContent='Good';$('#k-health').className='ok';$('#k-health-d').textContent='both encoders up';}
  $('#k-conc').textContent=v.toLocaleString(); $('#k-conc-d').textContent='peak '+Math.max(...series).toLocaleString()+' · '+tstr(); $('#k-uniq').textContent=uniq.size.toLocaleString(); $('#k-watch').textContent=Math.round(watch/Math.max(1,uniq.size)*60)+'m'; $('#k-eng').textContent=Math.round(30+t/450*42); $('#k-leads').textContent=leads; $('#k-leads-d').textContent=Math.round(leads*.62)+' MQL · synced to CRM';
  if(t%3===0){draw(); $('#eng-bars').innerHTML=RO.slice(0,-1).filter(r=>+r[0].slice(0,2)*60+ +r[0].slice(3)-540<=t).map(r=>`<div class="bc-bar"><span>${r[1]}</span><i style="width:${r[2]*100}%"></i><em>${Math.round(r[2]*100)}</em></div>`).join('');
   $('#top-q').innerHTML=[...q].sort((a,b)=>b[1]-a[1]).map(x=>`<li>${x[0]} <b>▲${x[1]}</b></li>`).join('');
   $('#sponsor-tbl').innerHTML='<tr><th>Sponsor</th><th>Impr.</th><th>Clicks</th><th>Leads</th></tr>'+sponsors.map(s=>`<tr><td>${s[0]}</td><td>${s[1].toLocaleString()}</td><td>${s[2]}</td><td>${s[3]}</td></tr>`).join('');}}
 setInterval(()=>{for(let i=0;i<speed;i++)tick();},400);
 $('#dash-report').addEventListener('click',()=>{const pk=Math.max(0,...series); $('#report').classList.remove('hidden');
  $('#report-body').innerHTML=`<p><strong>Objective:</strong> reach the whole membership live or on demand and generate qualified conversations for the sales team.</p><p><strong>Result:</strong> ${uniq.size.toLocaleString()} unique attendees of 2,140 registered (${Math.round(uniq.size/2140*100)}% attendance), peak concurrent ${pk.toLocaleString()}, average watch time ${$('#k-watch').textContent}, ${leads} leads scored (${Math.round(leads*.62)} MQL). Stream health: one automatic encoder failover at 11:15 with no audience impact.</p><p><strong>What worked:</strong> keynote and hybrid panel held the audience (engagement ${RO[1][2]*100}/${RO[3][2]*100}); polls averaged 58% response; expo produced ${sponsors.reduce((a,s)=>a+s[3],0)} booth leads.</p><p><strong>What didn't:</strong> the 11:45 platforms session lost 30% of the audience; lunch ran long on the stream (holding loop 55 min).</p><p><strong>Recommendations:</strong> move the platforms session after lunch (agenda owner, March); shorten the lunch stream break to 40 min with a sponsored segment (production); human captions for the keynote (finance, £1,200).</p><p class="hint">Generated from Insight data. Edit, attach the attendance curve, send.</p>`; $('#report').scrollIntoView({behavior:'smooth'});});
 log('Dashboard connected · waiting for stream'); draw();
}
})();
