"""Contact/enquiry form and privacy notice."""

# Shared cache-busting version. A fixed ?v=1 meant the form script never
# updated in browsers that had seen the page before.
try:
    from build_pages import CSSV as _CSSV
except Exception:
    _CSSV = 'v=1'

# The Lambda Function URL. Verified end-to-end on 12 September 2026: validation,
# spam traps and SES delivery all confirmed from the live origin.
# If this is ever blanked, the form still works - it validates fully and falls
# back to a pre-filled mailto, so it never looks broken to a visitor.
# Note: CORS is configured on the function URL, never in the Lambda response.
# Sending it from both places duplicates Access-Control-Allow-Origin and the
# browser rejects the reply while the mail still sends.
FORM_ENDPOINT = "https://5vyyyazykmpyo3liwlnxzcxznq0xcose.lambda-url.eu-west-2.on.aws/"

CONTACT_BODY = """
<section class="content-sec"><div class="wrap reveal">
<div class="two-col" style="align-items:start">
  <div>
    <div class="form-card">
      <form id="enquiryForm" novalidate>
        <div class="form-grid">
          <label class="field"><span>Your name *</span><input name="name" required autocomplete="name" maxlength="80"><em class="err">Please tell us your name.</em></label>
          <label class="field"><span>Work email *</span><input name="email" type="email" required autocomplete="email" maxlength="120"><em class="err">We need a valid email to reply to.</em></label>
          <label class="field"><span>Organisation</span><input name="organisation" autocomplete="organization" maxlength="100"></label>
          <label class="field"><span>Phone</span><input name="phone" type="tel" autocomplete="tel" maxlength="40"></label>
          <label class="field"><span>What are you planning?</span>
            <select name="event_type">
              <option value="">Not sure yet</option>
              <option>Virtual conference</option><option>Hybrid conference</option>
              <option>Town hall / all-hands</option><option>Awards show</option>
              <option>Webinar</option><option>Product launch</option>
              <option>AGM / investor event</option><option>Podcast</option>
              <option>Crew hire (white-label)</option><option>Studio hire</option>
              <option>Platform only</option><option>Something else</option>
            </select></label>
          <label class="field"><span>Event date</span><input name="event_date" type="date"></label>
          <label class="field"><span>Budget guide</span>
            <select name="budget">
              <option value="">Prefer not to say</option>
              <option>Under &pound;2,000</option><option>&pound;2,000&ndash;&pound;7,500</option>
              <option>&pound;7,500&ndash;&pound;15,000</option><option>&pound;15,000&ndash;&pound;30,000</option>
              <option>&pound;30,000+</option><option>Annual programme</option>
            </select></label>
          <label class="field"><span>Where are you?</span><input name="location" placeholder="London, remote, our studio&hellip;" maxlength="80"></label>
          <label class="field full"><span>Tell us about the show *</span><textarea name="message" required maxlength="4000" placeholder="Format, audience size, room or online, what success looks like. A couple of sentences is plenty."></textarea><em class="err">A sentence or two about the event, please.</em></label>
        </div>
        <label class="chk" style="margin-top:18px;display:block;font-size:.86rem;color:var(--ink-dim)">
          <input type="checkbox" name="consent" required> I'm happy for VSE to use these details to reply to my enquiry. *
          <em class="err" style="display:none">Please tick to let us reply.</em>
        </label>
        <div class="hp" aria-hidden="true"><label>Leave this blank<input name="website" tabindex="-1" autocomplete="off"></label></div>
        <input type="hidden" name="started_at" id="startedAt">
        <div class="form-actions">
          <button type="submit" class="cta-btn btn-submit" id="submitBtn">Send enquiry<span class="spin" aria-hidden="true"></span></button>
          <span class="form-note" style="margin:0">Same-day response, every enquiry.</span>
        </div>
        <div class="form-status" id="formStatus" role="status" aria-live="polite"></div>
      </form>
      <div class="form-success" id="formSuccess" role="status" aria-live="polite">
        <div class="tick"><svg viewBox="0 0 24 24"><path d="m5 13 4.5 4.5L19 7"/></svg></div>
        <h3>Thanks, that's with us.</h3>
        <p id="successMsg">We read every enquiry ourselves and reply the same working day. If it's urgent, call <a href="tel:+442035986555">+44 020 359 86555</a>.</p>
        <a class="ghost-btn" href="resources.html">Read the knowledge hub while you wait</a>
      </div>
    </div>
    <p class="form-note">We'll only use your details to answer this enquiry. No lists, no newsletters unless you ask. See our <a href="privacy.html" style="color:var(--accent2)">privacy notice</a>.</p>
  </div>
  <div>
    <div class="media-band reveal" style="aspect-ratio:4/3;margin-bottom:24px"><img src="assets/img/gen/studio-door.jpg" alt="The door to the VSE studio, light spilling into the corridor" loading="lazy"></div>
    <div class="contact-card" style="text-align:left">
      <h3>Prefer to talk?</h3>
      <p style="color:var(--ink-dim);font-size:.92rem;margin:10px 0 6px">Email <a href="mailto:enquiries@virtualstudio.events">enquiries@virtualstudio.events</a></p>
      <p style="color:var(--ink-dim);font-size:.92rem;margin:0 0 14px">Call <a href="tel:+442035986555">+44 020 359 86555</a></p>
      <div class="copy-wrap" style="justify-content:flex-start"><button class="copy-btn" type="button" data-copy="#contactDetails">Copy contact details</button></div>
      <div id="contactDetails" class="hp">Virtual Studio Events Limited
enquiries@virtualstudio.events
+44 020 359 86555
Chichester, West Sussex, United Kingdom
virtualstudio.events</div>
    </div>
    <div class="side-box" style="margin-top:22px">
      <h4>What happens next</h4>
      <ul style="list-style:none">
        <li style="padding:7px 0;border-top:1px solid var(--line)">We reply the same working day: a person, not an autoresponder.</li>
        <li style="padding:7px 0;border-top:1px solid var(--line)">A 20-minute call to understand the show and the risks.</li>
        <li style="padding:7px 0;border-top:1px solid var(--line)">An itemised proposal: crew, kit, redundancy, platform, deliverables.</li>
      </ul>
    </div>
    <div class="side-box">
      <h4>Already know the numbers?</h4>
      <p style="font-size:.9rem;color:var(--ink-dim);margin-bottom:12px">Get an indicative budget in 60 seconds before you write to us.</p>
      <a class="ghost-btn" href="tools.html#budget">Budget estimator &rarr;</a>
    </div>
  </div>
</div>
</div></section>
"""

PRIVACY_BODY = """
<section class="content-sec"><div class="wrap reveal"><div class="guide-body" style="max-width:74ch">
<p><strong>Virtual Studio Events Limited</strong> ("VSE", "we") is the data controller for this website and for enquiries sent through it. This notice explains what we collect and why. It is written to be read, not to be survived.</p>

<h2>What we collect</h2>
<p><strong>When you send an enquiry:</strong> your name, email address and message, plus anything optional you choose to add (organisation, phone, event type, date, budget guide, location). We also record which page you arrived from and any campaign tags in the link you followed, so we know which of our content is useful.</p>
<p><strong>When you browse:</strong> nothing identifying, unless you accept analytics cookies. Our web server and content delivery network keep short-lived technical logs (IP address, browser type, pages requested) for security and troubleshooting.</p>

<h2>Cookies and analytics</h2>
<p>Essential storage keeps your theme choice and your cookie preference. It is not used to track you and cannot be switched off without breaking the site.</p>
<p>Analytics cookies load <strong>only if you accept them</strong>. We use Google Analytics 4 (with IP anonymisation) and Microsoft Clarity, which records anonymised interaction patterns so we can see where pages confuse people. Decline and neither loads at all. You can change your mind at any time using the <a href="#" class="cookie-settings">cookie settings</a> link.</p>

<h2>Why we're allowed to use it</h2>
<p>For enquiries: to take steps at your request before entering a contract, and our legitimate interest in responding to people who contact us. For analytics: your consent. We do not use your enquiry details for marketing unless you separately ask us to.</p>

<h2>Who else sees it</h2>
<p>Our enquiry email is hosted by our mail provider, and enquiries are delivered through Amazon Web Services (SES) in the UK/EU region. The website is hosted on AWS in London. Analytics data, if you consent, goes to Google and Microsoft under their own terms. We do not sell data and we do not share enquiry details with anyone who isn't working on your event.</p>

<h2>How long we keep it</h2>
<p>Enquiries that become projects are retained for the life of the working relationship plus six years for tax and contractual records. Enquiries that don't lead anywhere are deleted within 24 months. Analytics data follows the providers' retention settings (GA4: 14 months).</p>

<h2>Your rights</h2>
<p>You can ask us for a copy of what we hold, ask us to correct or delete it, object to processing, or withdraw consent at any time. Email <a href="mailto:enquiries@virtualstudio.events">enquiries@virtualstudio.events</a> and we'll respond within one month. If you're unhappy with how we've handled it you can complain to the Information Commissioner's Office at <a href="https://ico.org.uk" rel="noopener">ico.org.uk</a>.</p>

<h2>Security</h2>
<p>The site is served over HTTPS with HSTS. Enquiries are transmitted over encrypted connections and delivered to a mailbox protected by multi-factor authentication. We keep the number of people with access small.</p>

<h2>Changes</h2>
<p>If we change this notice materially we'll update the date below. This version: <strong>September 2026</strong>.</p>
<p style="color:var(--ink-dim);font-size:.9rem">Virtual Studio Events Limited, Chichester, West Sussex, United Kingdom. Enquiries: <a href="mailto:enquiries@virtualstudio.events">enquiries@virtualstudio.events</a></p>
</div></div></section>
"""


def register(P, page):
    P['contact.html'] = page(
        'contact.html',
        'Contact Us | Virtual Studio Events: UK Event Production Company',
        'Talk to us about live, hybrid or virtual event production, crew hire, studio booking or the VSE Platform. Same-day response on every enquiry, UK-wide delivery.',
        'Say hello', 'Got a show <span class="em">coming up?</span>',
        "Tell us the date and the ambition. We'll handle the rest. Same-day response on every enquiry.",
        CONTACT_BODY,
        crumbs=[('index.html', 'Home'), ('contact.html', 'Contact')],
        extra_head='<script defer src="assets/js/form.js?'+_CSSV+'"></script>')

    P['privacy.html'] = page(
        'privacy.html',
        'Privacy Notice | Virtual Studio Events',
        'How Virtual Studio Events collects and uses personal data from website enquiries and analytics, your rights under UK GDPR, retention periods and how to contact us.',
        'Legal', 'Privacy notice: <span class="em">the short, readable version.</span>',
        'What we collect, why, how long we keep it, and how to make us stop.',
        PRIVACY_BODY,
        crumbs=[('index.html', 'Home'), ('privacy.html', 'Privacy')])
