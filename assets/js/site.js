/* VSE site chrome: theme, consent-gated analytics, search, copy, UTM, floating CTA.
   Loads on every page. Analytics do not fire until consent is given. */
(function () {
  'use strict';
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => [...(r || document).querySelectorAll(s)];
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };

  /* ---------------- theme ---------------- */
  const THEME_KEY = 'vse-theme';
  function applyTheme(t) {
    document.documentElement.setAttribute('data-theme', t);
    const btn = $('#themeBtn');
    if (btn) {
      btn.setAttribute('aria-label', t === 'light' ? 'Switch to dark theme' : 'Switch to light theme');
      btn.setAttribute('aria-pressed', t === 'light');
    }
    const meta = $('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', t === 'light' ? '#f4f6fa' : '#212b54');
  }
  applyTheme(store.get(THEME_KEY) || 'dark');   // dark is the brand default; light is opt-in
  document.addEventListener('click', e => {
    const b = e.target.closest('#themeBtn');
    if (!b) return;
    const next = document.documentElement.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    store.set(THEME_KEY, next); applyTheme(next);
  });

  /* ---------------- UTM capture ---------------- */
  const UTM_KEY = 'vse-utm';
  (function captureUtm() {
    const p = new URLSearchParams(location.search);
    const keys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'fbclid', 'msclkid'];
    const found = {};
    keys.forEach(k => { const v = p.get(k); if (v) found[k] = v.slice(0, 120); });
    if (Object.keys(found).length) {
      found.landing = location.pathname;
      found.referrer = (document.referrer || '').slice(0, 200);
      found.ts = new Date().toISOString();
      store.set(UTM_KEY, JSON.stringify(found));
    }
  })();
  window.vseUtm = function () { try { return JSON.parse(store.get(UTM_KEY) || '{}'); } catch (e) { return {}; } };
  function sendStoredUtm() {
    const u = window.vseUtm();
    if (u.utm_source && window.gtag) {
      window.gtag('event', 'campaign_attributed', { campaign_source: u.utm_source, campaign_medium: u.utm_medium || '', campaign_name: u.utm_campaign || '' });
    }
  }

  /* ---------------- consent-gated analytics ----------------
     Two modes, one switch.

     ADVANCED_CONSENT = false  (current behaviour, most conservative)
       Nothing loads until the visitor accepts. Anyone who ignores the banner
       is invisible to both GA4 and Clarity, which is almost certainly why
       analytics volume looks low.

     ADVANCED_CONSENT = true   (Google Consent Mode v2, "advanced")
       GA4 loads immediately with analytics_storage denied. It writes and reads
       no cookies in that state, so PECR's storage rule is not engaged, but it
       does send cookieless pings to Google (timestamp, user agent, referrer,
       consent state, no identifier) which Google uses to model the sessions it
       cannot observe. On accept, consent is updated and normal collection
       starts. This recovers the non-consenting majority for GA4 and makes the
       accept rate measurable.

     Clarity is unaffected by the switch: it needs _clck/_clsk to function at
     all, so it stays fully gated in both modes.

     The trade-off in advanced mode is that data about non-consenting visitors
     reaches Google, which is a judgement for James rather than a default. */
  const ADVANCED_CONSENT = false;

  const CONSENT_KEY = 'vse-consent';
  const GA_ID = 'G-1SVVZ8ZEVK', CLARITY_ID = 'yh85iv2y4g';
  let gaLoaded = false, clarityLoaded = false;

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };

  // Declare the consent state before gtag.js loads, so it is never guessed.
  gtag('consent', 'default', {
    ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied',
    analytics_storage: 'denied',
    functionality_storage: 'granted', security_storage: 'granted',
    wait_for_update: 500
  });

  function loadGA() {
    if (gaLoaded) return; gaLoaded = true;
    const s = document.createElement('script');
    s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    gtag('js', new Date());
    gtag('config', GA_ID);          // GA4 anonymises IPs by default
  }

  function loadClarity() {
    if (clarityLoaded) return; clarityLoaded = true;
    (function (c, l, a, r, i, t, y) {
      c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
      t = l.createElement(r); t.async = 1; t.src = 'https://www.clarity.ms/tag/' + i;
      y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
    })(window, document, 'clarity', 'script', CLARITY_ID);
  }

  function grantAnalytics() {
    gtag('consent', 'update', { analytics_storage: 'granted' });
    loadGA();
    loadClarity();
    sendStoredUtm();
  }

  function showBar() {
    const b = $('#cookieBar');
    if (b) { b.classList.add('on'); gtag('event', 'consent_banner_shown'); }
  }
  function hideBar() { const b = $('#cookieBar'); if (b) b.classList.remove('on'); }

  const consent = store.get(CONSENT_KEY);
  if (consent === 'all') {
    grantAnalytics();
  } else {
    // In advanced mode GA4 loads now, cookieless, so the visit is counted even
    // if the banner is never touched. In conservative mode nothing loads.
    if (ADVANCED_CONSENT) loadGA();
    if (consent !== 'essential') setTimeout(showBar, 400);
  }

  document.addEventListener('click', e => {
    if (e.target.closest('#cookieAccept')) {
      store.set(CONSENT_KEY, 'all'); hideBar();
      grantAnalytics(); gtag('event', 'consent_accepted');
    }
    if (e.target.closest('#cookieReject')) {
      store.set(CONSENT_KEY, 'essential'); hideBar();
      gtag('event', 'consent_rejected');
    }
    if (e.target.closest('.cookie-settings')) { store.set(CONSENT_KEY, ''); showBar(); }
  });

  /* ---------------- site search ---------------- */
  let idx = null, idxLoading = false;
  function loadIndex() {
    if (idx || idxLoading) return Promise.resolve(idx);
    idxLoading = true;
    return fetch('search-index.json').then(r => r.json()).then(d => { idx = d; return d; }).catch(() => { idx = []; return idx; });
  }
  function openSearch() {
    const o = $('#searchOverlay'); if (!o) return;
    o.classList.add('on'); document.body.style.overflow = 'hidden';
    loadIndex(); const i = $('#searchInput'); if (i) { i.value = ''; i.focus(); }
    $('#searchResults').innerHTML = '<a href="resources.html"><b>Browse the knowledge hub</b><span>32 guides across six pillars</span></a>';
  }
  function closeSearch() { const o = $('#searchOverlay'); if (!o) return; o.classList.remove('on'); document.body.style.overflow = ''; }

  function score(item, terms) {
    let s = 0;
    const t = (item.t || '').toLowerCase(), d = (item.d || '').toLowerCase(), k = (item.k || '').toLowerCase();
    terms.forEach(q => {
      if (t.startsWith(q)) s += 60;
      if (t.includes(q)) s += 30;
      if (k.includes(q)) s += 12;
      if (d.includes(q)) s += 6;
    });
    return s;
  }
  function esc(s) { return (s || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])); }
  function mark(text, terms) {
    let out = esc(text);
    terms.forEach(q => { if (q.length > 1) out = out.replace(new RegExp('(' + q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'), '<em>$1</em>'); });
    return out;
  }
  function runSearch(q) {
    const box = $('#searchResults'); if (!box) return;
    const terms = q.toLowerCase().split(/\s+/).filter(Boolean);
    if (!terms.length || !idx) { box.innerHTML = ''; return; }
    const hits = idx.map(it => ({ it, s: score(it, terms) })).filter(x => x.s > 0).sort((a, b) => b.s - a.s).slice(0, 8);
    box.innerHTML = hits.length
      ? hits.map(h => `<a href="${h.it.u}"><b>${mark(h.it.t, terms)}</b><span>${mark((h.it.d || '').slice(0, 110), terms)}</span></a>`).join('')
      : `<a href="contact.html"><b>No matches for “${esc(q)}”</b><span>Ask us directly — we answer every enquiry the same day.</span></a>`;
  }
  document.addEventListener('click', e => {
    if (e.target.closest('#searchBtn')) { e.preventDefault(); openSearch(); }
    const o = $('#searchOverlay');
    if (o && o.classList.contains('on') && e.target === o) closeSearch();
  });
  document.addEventListener('input', e => { if (e.target.id === 'searchInput') runSearch(e.target.value.trim()); });
  document.addEventListener('keydown', e => {
    const o = $('#searchOverlay'), open = o && o.classList.contains('on');
    if ((e.key === 'k' || e.key === 'K') && (e.metaKey || e.ctrlKey)) { e.preventDefault(); open ? closeSearch() : openSearch(); return; }
    if (e.key === '/' && !open && !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) { e.preventDefault(); openSearch(); return; }
    if (!open) return;
    if (e.key === 'Escape') closeSearch();
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp' || e.key === 'Enter') {
      const links = $$('#searchResults a'); if (!links.length) return;
      let i = links.findIndex(l => l.classList.contains('sel'));
      if (e.key === 'Enter') { e.preventDefault(); (links[i] || links[0]).click(); return; }
      e.preventDefault();
      links.forEach(l => l.classList.remove('sel'));
      i = e.key === 'ArrowDown' ? (i + 1) % links.length : (i <= 0 ? links.length - 1 : i - 1);
      links[i].classList.add('sel'); links[i].scrollIntoView({ block: 'nearest' });
    }
  });

  /* ---------------- copy buttons ---------------- */
  document.addEventListener('click', e => {
    const b = e.target.closest('.copy-btn'); if (!b) return;
    const sel = b.getAttribute('data-copy');
    const src = sel ? $(sel) : b.closest('.tool, .guide-body, .contact-card');
    if (!src) return;
    const text = src.tagName === 'TABLE'
      ? [...src.rows].map(r => [...r.cells].map(c => c.innerText.trim()).join('\t')).join('\n')
      : (src.innerText || '').trim();
    const done = () => { const o = b.textContent; b.textContent = 'Copied'; b.classList.add('done'); setTimeout(() => { b.textContent = o; b.classList.remove('done'); }, 1800); };
    if (navigator.clipboard) navigator.clipboard.writeText(text).then(done).catch(() => {});
    else { const ta = document.createElement('textarea'); ta.value = text; document.body.appendChild(ta); ta.select(); try { document.execCommand('copy'); done(); } catch (err) {} ta.remove(); }
  });

  /* ---------------- floating contact button ---------------- */
  (function fab() {
    const f = $('.fab'); if (!f) return;
    if (/contact\.html$/.test(location.pathname)) { f.remove(); return; }
    const onScroll = () => { f.classList.toggle('on', scrollY > 620); };
    addEventListener('scroll', onScroll, { passive: true }); onScroll();
  })();
})();
