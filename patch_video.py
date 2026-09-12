"""Wire the generated video loops into hero, pillars, modules and event pages."""

def vid_tag(name, poster, alt, cls='media-band reveal'):
    return (f'<div class="{cls}">'
            f'<video autoplay muted loop playsinline preload="none" '
            f'poster="assets/img/gen/poster-{name}.jpg" aria-label="{alt}">'
            f'<source src="assets/video/{name}.mp4" type="video/mp4"></video></div>')

# ---------- pillars: live-production gets the gallery loop ----------
h = open('content_hub.py').read()
old = """    banner=f'<div class="media-band reveal"><img src="assets/img/{p["img"]}" alt="{p["img_alt"]}" loading="lazy"></div>' if p.get('img') else ''"""
new = """    if p.get('vid'):
        banner=('<div class="media-band reveal"><video autoplay muted loop playsinline preload="none" poster="assets/img/gen/poster-'
                +p['vid']+'.jpg" aria-label="'+p['img_alt']+'"><source src="assets/video/'+p['vid']+'.mp4" type="video/mp4"></video></div>')
    elif p.get('img'):
        banner=f'<div class="media-band reveal"><img src="assets/img/{p["img"]}" alt="{p["img_alt"]}" loading="lazy"></div>'
    else:
        banner=''"""
assert old in h
h = h.replace(old, new, 1)
h = h.replace("dict(img='gen/pillar-live-production.jpg',", "dict(vid='gallery', img='gen/pillar-live-production.jpg',", 1)
open('content_hub.py', 'w').write(h)

# ---------- platform modules: broadcast + engage get loops ----------
p = open('content_platform.py').read()
old = """    banner=f'<div class="media-band reveal"><img src="assets/img/{m["img"]}" alt="{m["img_alt"]}" loading="lazy"></div>' if m.get('img') else ''"""
new = """    if m.get('vid'):
        banner=('<div class="media-band reveal"><video autoplay muted loop playsinline preload="none" poster="assets/img/gen/poster-'
                +m['vid']+'.jpg" aria-label="'+m['img_alt']+'"><source src="assets/video/'+m['vid']+'.mp4" type="video/mp4"></video></div>')
    elif m.get('img'):
        banner=f'<div class="media-band reveal"><img src="assets/img/{m["img"]}" alt="{m["img_alt"]}" loading="lazy"></div>'
    else:
        banner=''"""
assert old in p
p = p.replace(old, new, 1)
p = p.replace("dict(img='gen/mod-broadcast.jpg',", "dict(vid='global-network', img='gen/mod-broadcast.jpg',", 1)
p = p.replace("dict(img='gen/mod-engage.jpg',", "dict(vid='audience', img='gen/mod-engage.jpg',", 1)

# platform overview hero -> arcs loop
p = p.replace('<div class="media-band reveal"><img src="assets/img/gen/platform-hero.jpg" alt="Abstract broadcast technology visual" loading="lazy"></div>',
              vid_tag('platform-arcs', 'platform-arcs', 'Abstract rotating broadcast technology visual'), 1)
open('content_platform.py', 'w').write(p)

# ---------- event pages: awards gets a loop ----------
e = open('content_events.py').read()
e = e.replace("img='gen/ev-awards-show.jpg',", "vid='awards', img='gen/ev-awards-show.jpg',", 1)
old = """<div class="img-frame"><img src="assets/img/{e['img']}" alt="{e['img_alt']}" loading="lazy"></div>"""
new = """{vidblock}"""
assert old in e
e = e.replace(old, new, 1)
old2 = "def event_page(page, e):"
new2 = """def event_page(page, e):
    if e.get('vid'):
        vidblock=('<div class="img-frame"><video autoplay muted loop playsinline preload="none" poster="assets/img/gen/poster-'
                  +e['vid']+'.jpg" aria-label="'+e['img_alt']+'"><source src="assets/video/'+e['vid']+'.mp4" type="video/mp4"></video></div>')
    else:
        vidblock='<div class="img-frame"><img src="assets/img/'+e['img']+'" alt="'+e['img_alt']+'" loading="lazy"></div>'"""
e = e.replace(old2, new2, 1)
open('content_events.py', 'w').write(e)

# ---------- homepage hero video ----------
idx = open('index.html').read()
if 'hero-video' not in idx:
    old3 = '<canvas id="lights"></canvas>'
    new3 = ('<video class="hero-video" autoplay muted loop playsinline preload="none" '
            'poster="assets/img/gen/poster-hero-studio.jpg" aria-hidden="true">'
            '<source src="assets/video/hero-studio.mp4" type="video/mp4"></video>\n  '
            '<canvas id="lights"></canvas>')
    assert old3 in idx
    idx = idx.replace(old3, new3, 1)
    open('index.html', 'w').write(idx)

# ---------- reduced motion: pause every decorative video ----------
js = open('assets/js/main.js').read()
if 'pauseDecorativeVideo' not in js:
    js += """

/* ---- decorative video: respect reduced motion, pause when off-screen ---- */
(function pauseDecorativeVideo(){
  const vids=[...document.querySelectorAll('.hero-video, .media-band video, .img-frame video')];
  if(!vids.length) return;
  if(matchMedia('(prefers-reduced-motion: reduce)').matches){
    vids.forEach(v=>{v.removeAttribute('autoplay');v.pause();});
    return;
  }
  const io=new IntersectionObserver(es=>es.forEach(e=>{
    const v=e.target;
    if(e.isIntersecting){ if(v.paused) v.play().catch(()=>{}); } else { v.pause(); }
  }),{threshold:.1});
  vids.forEach(v=>io.observe(v));
})();
"""
    open('assets/js/main.js', 'w').write(js)

# ---------- css + cache bust ----------
css = open('assets/css/main.css').read()
if '.img-frame video' not in css:
    css += """
.img-frame video{width:100%;height:100%;object-fit:cover;display:block}
"""
    open('assets/css/main.css', 'w').write(css)

b = open('build_pages.py').read()
b = b.replace('CSSV = "v=13"', 'CSSV = "v=14"')
open('build_pages.py', 'w').write(b)
print('video patch applied')
