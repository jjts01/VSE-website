const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ---- preloader ---- */
const loader=document.getElementById('loader'),pctEl=loader.querySelector('.pct');
let pct=0;
const pi=setInterval(()=>{
  pct=Math.min(100,pct+Math.ceil(Math.random()*14));
  pctEl.textContent=pct+'%';
  if(pct>=100){clearInterval(pi);setTimeout(()=>loader.classList.add('done'),250)}
},reduced?10:90);

/* ---- scroll progress + nav ---- */
const prog=document.getElementById('progress'),nav=document.getElementById('nav');
addEventListener('scroll',()=>{
  const h=document.documentElement;
  prog.style.width=(h.scrollTop/(h.scrollHeight-h.clientHeight)*100)+'%';
  nav.classList.toggle('scrolled',h.scrollTop>40);
},{passive:true});

/* ---- reveals ---- */
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.15});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

/* ---- image parallax ---- */
if(!reduced){
  addEventListener('scroll',()=>{
    document.querySelectorAll('.plx').forEach(img=>{
      const r=img.parentElement.getBoundingClientRect();
      if(r.bottom<0||r.top>innerHeight)return;
      const p=(r.top+r.height/2-innerHeight/2)/innerHeight;
      img.style.transform=`translateY(${p*-26}px)`;
    });
  },{passive:true});
}

/* ---- hero: "the gallery is live" — LED wall that follows the cursor ---- */
const cv=document.getElementById('lights');
if(cv){
const ctx=cv.getContext('2d');
let W,H,dots=[];
function build(){
  W=cv.width=cv.offsetWidth*devicePixelRatio;H=cv.height=cv.offsetHeight*devicePixelRatio;
  dots=[];const gap=34*devicePixelRatio;
  for(let x=gap/2;x<W;x+=gap)for(let y=gap/2;y<H;y+=gap)
    dots.push({x,y,b:0,hue:Math.random()<.6?182:225,tw:Math.random()*Math.PI*2});
}
build();addEventListener('resize',build);
let hx=-9999,hy=-9999;
cv.parentElement.addEventListener('mousemove',e=>{
  const r=cv.getBoundingClientRect();
  hx=(e.clientX-r.left)*devicePixelRatio;hy=(e.clientY-r.top)*devicePixelRatio;
});
cv.parentElement.addEventListener('mouseleave',()=>{hx=hy=-9999});
let t=0;
(function draw(){
  t+=.02;ctx.clearRect(0,0,W,H);
  const R=240*devicePixelRatio;
  for(const d of dots){
    const dist=Math.hypot(d.x-hx,d.y-hy);
    const target=dist<R?(1-dist/R):0;
    d.b+=(target-d.b)*.08;
    const base=.05+.04*Math.sin(t+d.tw);
    const a=Math.min(1,base+d.b*.9);
    const size=(1+d.b*2.2)*devicePixelRatio;
    ctx.beginPath();
    ctx.fillStyle=`hsla(${d.hue},${d.hue===182?38:30}%,${66+d.b*18}%,${a})`;
    ctx.arc(d.x,d.y,size,0,7);
    ctx.fill();
  }
  if(!reduced)requestAnimationFrame(draw);
})();
}
