/* VSE free tools: bandwidth calculator, budget estimator, template downloads */
(function(){
  const $=id=>document.getElementById(id);

  /* ---- bandwidth ---- */
  if($('bwtool')){
    const calc=()=>{
      const q=+$('bw-quality').value, n=+$('bw-streams').value||1, b=+$('bw-backup').value, r=+$('bw-remote').value||0, o=+$('bw-other').value;
      const encode=q*n + (b?Math.min(q,5):0);
      const up=Math.ceil(encode*2 + o);
      const down=Math.ceil(r*3 + 5);
      $('bw-result').textContent=up+' Mbps upload';
      $('bw-detail').textContent=`Encode total ${encode.toFixed(1)} Mbps × 2 headroom${o?` + ${o} Mbps other traffic`:''}. Plus ~${down} Mbps download for ${r} remote contributor${r===1?'':'s'} and returns. Backup path (bonded cellular) should sustain at least ${Math.ceil(q*2)} Mbps.`;
    };
    ['bw-quality','bw-streams','bw-backup','bw-remote','bw-other'].forEach(id=>$(id).addEventListener('input',calc));
    calc();
  }

  /* ---- budget ---- */
  if($('budgettool')){
    const gbp=n=>'£'+(Math.round(n/50)*50).toLocaleString('en-GB');
    const calc=()=>{
      const f=$('b-format').value, days=+$('b-days').value||1, cams=+$('b-cams').value, rem=+$('b-remote').value;
      $('b-cams-v').textContent=cams; $('b-remote-v').textContent=rem;
      const rows=[];
      // core crew per show day by format
      const crew={webinar:[['vMix operator / streaming engineer',495]],
        townhall:[['Producer / show caller',595],['vMix operator',495],['Sound engineer (stream mix)',450]],
        hybrid:[['Video HOD / technical director',650],['Vision mixer',495],['Streaming engineer',495],['Sound engineer',450],['Floor manager',400]],
        awards:[['Producer / show caller',595],['Vision mixer',495],['Graphics operator',450],['Streaming engineer',495],['Sound engineer',450],['Floor manager',400]],
        launch:[['Video HOD / technical director',650],['Vision mixer',495],['Graphics operator',450],['Streaming engineer',495],['Sound engineer',450]],
        multi:[['Video HOD / technical director',650],['Producer',595],['vMix operators × tracks (3)',1485],['Streaming engineer',495],['Sound engineer',450],['Platform moderators × 2',700]]}[f];
      let crewTotal=0; crew.forEach(([n,c])=>{crewTotal+=c*days; rows.push([n+(days>1?` × ${days} days`:''),c*days]);});
      // cameras
      const camOps=Math.max(0,cams-1); if(camOps){rows.push([`Camera operators × ${camOps}`,camOps*400*days]);}
      rows.push([`Cameras & lenses × ${cams}`,cams*150*days]);
      // production system
      rows.push([$('b-studio').value==='cloud'?'Cloud gallery (AWS instances + routing)':'vMix production system + backup encoder',($('b-studio').value==='cloud'?350:640)*days]);
      // connectivity
      rows.push(['Bonded cellular backup + redundancy',$('b-studio').value==='cloud'?150:450]);
      // remote speakers
      if(rem){rows.push([`Remote speaker checks & green room (${rem})`,Math.min(rem,20)*45 + (rem>4?400*days:0)]);}
      // studio / location
      if($('b-studio').value==='studio') rows.push(['Studio hire, lit set, pre-rig',(f==='webinar'?395:795)*days]);
      if($('b-studio').value==='venue') rows.push(['Load-in, travel & on-site logistics',350+120*cams]);
      // graphics
      rows.push(['Graphics package (stings, lower thirds, holding loop)',{webinar:350,townhall:600,hybrid:900,awards:1800,launch:1800,multi:1200}[f]]);
      // platform
      const plat=+$('b-platform').value; if(plat) rows.push(['Platform licence / build',plat]);
      // extras
      if($('b-captions').checked) rows.push(['Human live captioning',300*4*days]);
      if($('b-rehearsal').checked) rows.push(['Rehearsal day (crew)',Math.round(crewTotal/days*0.6)]);
      if($('b-edit').checked) rows.push(['Highlights & on-demand edit',{webinar:350,townhall:600,hybrid:900,awards:1200,launch:1400,multi:1500}[f]]);
      if($('b-led').checked) rows.push(['LED wall hire, processing & content',3500*days]);
      const total=rows.reduce((a,r)=>a+r[1],0);
      $('b-result').textContent=gbp(total*0.85)+' – '+gbp(total*1.15);
      $('b-detail').textContent=`Central estimate ${gbp(total)} +VAT for ${days} show day${days>1?'s':''}. Range reflects venue conditions, content volume and rehearsal scope.`;
      $('b-table').innerHTML='<tr><th>Line</th><th style="text-align:right">Est.</th></tr>'+rows.map(r=>`<tr><td>${r[0]}</td><td style="text-align:right">${gbp(r[1])}</td></tr>`).join('');
    };
    ['b-format','b-days','b-cams','b-remote','b-platform','b-studio','b-captions','b-rehearsal','b-edit','b-led'].forEach(id=>$(id).addEventListener('input',calc));
    calc();
  }

  /* ---- template downloads ---- */
  const dl=(name,text,type)=>{const blob=new Blob([text],{type});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;document.body.appendChild(a);a.click();a.remove();};
  if($('dl-runorder')) $('dl-runorder').addEventListener('click',()=>{
    const rows=[...document.querySelectorAll('#run-order ~ .tool table tr, .tool table tr')].slice(0,11).map(tr=>[...tr.children].map(td=>'"'+td.textContent.replace(/"/g,'""')+'"').join(','));
    dl('VSE-run-order-template.csv',rows.join('\n'),'text/csv');
  });
  if($('dl-techspec')) $('dl-techspec').addEventListener('click',()=>{
    const el=document.querySelector('#tech-spec ~ .tool .guide-body')||document.querySelectorAll('.tool .guide-body')[0];
    dl('VSE-technical-spec-template.txt','VIRTUAL STUDIO EVENTS — TECHNICAL SPECIFICATION TEMPLATE\n\n'+el.innerText,'text/plain');
  });
  if($('dl-report')) $('dl-report').addEventListener('click',()=>{
    const el=document.querySelectorAll('.tool .guide-body')[1];
    dl('VSE-post-event-report-template.txt','VIRTUAL STUDIO EVENTS — POST-EVENT REPORT TEMPLATE\n\n'+el.innerText,'text/plain');
  });
})();
