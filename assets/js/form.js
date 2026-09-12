/* VSE enquiry form: validation, UTM passthrough, spam traps, success/error states.
   If VSE_FORM_ENDPOINT is empty the form falls back to a pre-filled mailto so it
   still works for the visitor while the backend is being provisioned. */
(function () {
  'use strict';
  const ENDPOINT = window.VSE_FORM_ENDPOINT || '';
  const form = document.getElementById('enquiryForm');
  if (!form) return;

  const statusEl = document.getElementById('formStatus');
  const successEl = document.getElementById('formSuccess');
  const btn = document.getElementById('submitBtn');
  const started = document.getElementById('startedAt');
  if (started) started.value = String(Date.now());

  const emailOk = v => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v);

  function fieldWrap(el) { return el.closest('.field') || el.closest('.chk'); }
  function setInvalid(el, bad) {
    const w = fieldWrap(el); if (!w) return;
    w.classList.toggle('invalid', bad);
    el.setAttribute('aria-invalid', bad ? 'true' : 'false');
    const err = w.querySelector('.err');
    if (err) err.style.display = bad ? 'block' : '';
  }

  function validate(report) {
    let firstBad = null;
    const checks = [
      ['name', el => el.value.trim().length >= 2],
      ['email', el => emailOk(el.value.trim())],
      ['message', el => el.value.trim().length >= 10],
      ['consent', el => el.checked]
    ];
    checks.forEach(([n, ok]) => {
      const el = form.elements[n]; if (!el) return;
      const bad = !ok(el);
      if (report) setInvalid(el, bad);
      if (bad && !firstBad) firstBad = el;
    });
    return firstBad;
  }

  // live-clear errors as the user fixes them
  form.addEventListener('input', e => {
    const w = fieldWrap(e.target);
    if (w && w.classList.contains('invalid')) validate(true);
  });
  form.addEventListener('change', e => {
    if (e.target.name === 'consent') validate(true);
  });

  function showStatus(kind, html) {
    if (!statusEl) return;
    statusEl.className = 'form-status on ' + kind;
    statusEl.innerHTML = html;
  }

  function payload() {
    const fd = new FormData(form);
    const data = {};
    fd.forEach((v, k) => { data[k] = typeof v === 'string' ? v.trim() : v; });
    data.consent = !!form.elements.consent.checked;
    data.utm = (window.vseUtm && window.vseUtm()) || {};
    data.page = location.href;
    data.elapsed_ms = Date.now() - Number(started ? started.value : Date.now());
    return data;
  }

  function mailtoFallback(d) {
    const lines = [
      'Name: ' + (d.name || ''), 'Email: ' + (d.email || ''),
      'Organisation: ' + (d.organisation || ''), 'Phone: ' + (d.phone || ''),
      'Event type: ' + (d.event_type || ''), 'Event date: ' + (d.event_date || ''),
      'Budget: ' + (d.budget || ''), 'Location: ' + (d.location || ''),
      '', d.message || ''
    ];
    if (d.utm && d.utm.utm_source) lines.push('', '— via ' + d.utm.utm_source + ' / ' + (d.utm.utm_campaign || ''));
    return 'mailto:enquiries@virtualstudio.events?subject=' +
      encodeURIComponent('Enquiry from ' + (d.name || 'the website')) +
      '&body=' + encodeURIComponent(lines.join('\n'));
  }

  function succeed(viaMail) {
    form.style.display = 'none';
    if (successEl) {
      successEl.classList.add('on');
      if (viaMail) {
        const m = document.getElementById('successMsg');
        if (m) m.innerHTML = 'Your email client should have opened with the details filled in — press send and it\'s with us. If nothing happened, email <a href="mailto:enquiries@virtualstudio.events">enquiries@virtualstudio.events</a> directly.';
      }
      successEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
    if (window.gtag) window.gtag('event', 'generate_lead', { method: viaMail ? 'mailto' : 'form' });
  }

  form.addEventListener('submit', async e => {
    e.preventDefault();
    const bad = validate(true);
    if (bad) {
      showStatus('bad', 'Please check the highlighted fields and try again.');
      bad.focus();
      bad.scrollIntoView({ behavior: 'smooth', block: 'center' });
      return;
    }
    // spam traps: hidden field filled, or submitted implausibly fast
    const d = payload();
    if (d.website) { succeed(false); return; }          // silently accept bots
    if (d.elapsed_ms < 2500) { showStatus('bad', 'That was quick — give it another moment and press send again.'); return; }

    if (statusEl) statusEl.className = 'form-status';
    btn.setAttribute('aria-busy', 'true');

    if (!ENDPOINT) {
      window.location.href = mailtoFallback(d);
      btn.removeAttribute('aria-busy');
      setTimeout(() => succeed(true), 600);
      return;
    }

    try {
      const ctl = new AbortController();
      const timer = setTimeout(() => ctl.abort(), 15000);
      const res = await fetch(ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(d),
        signal: ctl.signal
      });
      clearTimeout(timer);
      if (res.ok) { succeed(false); return; }
      let msg = 'Something went wrong at our end.';
      if (res.status === 429) msg = 'That\'s a few enquiries in quick succession — please wait a minute and try again.';
      else if (res.status === 400) { try { const j = await res.json(); if (j && j.error) msg = j.error; } catch (err) {} }
      showStatus('bad', msg + ' You can also email <a href="mailto:enquiries@virtualstudio.events">enquiries@virtualstudio.events</a> or call <a href="tel:+442035986555">+44 020 359 86555</a>.');
    } catch (err) {
      showStatus('bad', 'We couldn\'t reach the server — your connection or ours. ' +
        '<a href="' + mailtoFallback(d) + '">Send it by email instead</a>, or call <a href="tel:+442035986555">+44 020 359 86555</a>.');
    } finally {
      btn.removeAttribute('aria-busy');
    }
  });
})();
