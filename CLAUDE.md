# CLAUDE.md — Virtual Studio Events website & platform

**Read this first in any session touching virtualstudio.events.** It is the canonical brief: strategy, conventions and coordinates. `PROJECT-PLAN.md` alongside it is the living plan and changelog — it is **rewritten automatically by `build_pages.py` on every build**, so never hand-edit the sections marked auto-generated.

---

## 1. Who and what

Virtual Studio Events Limited (VSE) — UK live, hybrid and virtual event production company. Founded March 2020 by **James Jones** and **Ben O'Dwyer** (40+ years combined live event experience). Studio in **Chichester, West Sussex**, partner studios in Manchester, Norwich and Fareham, cloud galleries on AWS. Studio partner: Granary Digital.

- Site: https://www.virtualstudio.events
- Contact: enquiries@virtualstudio.events · +44 020 359 86555
- Repo: `jjts01/VSE-website` (GitHub, private)

## 2. Strategy — the one thing to understand

The 2020 site sold a "virtual events platform". The invoice data (571 lines, 2020–2026) showed the actual business is **senior technical crew and production delivery sold largely to other production companies**: 2024–26 revenue was ~£84k crew & engineering, ~£57k production management/HOD/technical delivery, ~£29k editing. Top clients are Apple Peel Productions, Reach Charity, Pure Communications, Universal Live, Production Bureau — trade, not end-clients.

So the site is positioned on three layers, in this order of commercial weight:

1. **Production company** — broadcast-grade crew, streaming engineering, studios. White-label for agencies; end-to-end for brands.
2. **VSE Platform** — an all-in-one event platform (registration, live participation, networking, agenda/on-demand, analytics) with a real production gallery behind it. The differentiator: platforms have no crew, production companies have no data; VSE has both under one contract.
3. **Knowledge authority** — 32+ guides, tools, templates, glossary and a sourced news page, to win organic search and be the reference people cite.

**Target audiences** (given by James): production companies needing crew; brands/corporates needing full event production; companies needing hybrid/virtual events. **Geography: UK-wide.** Named competitors to watch: Fresh Productions, MOD Streaming, Gass Productions, Concept LIVE.

**Voice:** plain, confident, specific. Gallery language ("standby… go"). Serif-italic accent words inside display headings. Never hype, never "solutions". Numbers and honest trade-offs beat adjectives — the honesty *is* the marketing.

## 3. Commercial position (benchmarked September 2026)

Full research with sources: Dropbox → `Website assets/Market pricing research - Sept 2026.md`.

| | Price | Note |
|---|---|---|
| Broadcast package | from £1,750/event | Produced stream into existing tools |
| Engage package | from £7,500/event | + registration, agenda, full participation |
| Enterprise programme | from £30,000/year | 5+ events, networking/expo, white-label, SSO |
| Platform-only (agencies) | from £1,500/event · £12,000/yr | No VSE crew |
| Engage-only | from £350/event · £2,400/yr | Participation layer for any show |

Market context: UK production runs £499–£1,000 (single camera) → £895–£3,500 (multi-camera) → **£5k–£15k/day (hybrid conference)** → £15k–£50k+ (multi-stage); specialist crew £450–£750/day. Platform licences alone run £1k–£5k/yr (self-serve) → **$10k–$50k per event/year (mid-market)** → $25k–$500k+ (ON24/Bizzabo/Cvent). **The bundle is the story**: an Enterprise programme including crew undercuts platform-only licences.

**Claims discipline.** Security wording is deliberately "built on ISO 27001 / SOC 2-certified infrastructure, controls *aligned to* ISO 27001" — do not upgrade to "we are certified" unless VSE actually is. Prices on the site are recommendations benchmarked to market; James redlines them.

## 4. Architecture

Static site, no framework. Python generates every page.

```
build_pages.py      # chrome (head, nav, footer, tracking), core pages, sitemap,
                    # syncs nav/footer into hand-built index.html + 404.html,
                    # and REGENERATES PROJECT-PLAN.md on every run
content_hub.py      # knowledge-hub engine: pillars, guide template (TOC, related,
                    # Article schema, breadcrumbs), resources hub, glossary, news, tools
content_prepro.py content_infra.py content_sets.py
content_live.py content_platforms.py content_analytics.py   # the 32 guides, by pillar
content_events.py   # 7 event-type landing pages (+ FAQ schema)
content_platform.py # VSE Platform: 7 modules, pipeline, packages, features, 4 demos
content_misc.py     # FAQs, glossary, news items, tools & templates HTML
assets/css/main.css # single stylesheet; bump CSSV in build_pages.py when it changes
assets/js/main.js   # site behaviour (loader, reveals, mobile nav, hero canvas)
assets/js/tools.js  # bandwidth + budget calculators, template downloads
assets/js/demo.js   # the four platform demos
assets/img/ assets/fonts/
```

`index.html` and `404.html` are **hand-built** — the build script injects nav, footer, tracking and cache-busting into them rather than regenerating them.

### Workflow
1. Edit the relevant `content_*.py` (or `index.html` directly).
2. `python3 build_pages.py`
3. Bump `CSSV` in `build_pages.py` if CSS or JS changed (cache-busting).
4. Commit and push to `main` → GitHub Actions deploys to S3 + CloudFront and invalidates.

### Adding a guide
Append a dict to the relevant pillar's `GUIDES` list with `slug`, `pillar`, `title` (SEO), `desc`, `h1` (HTML, with a `<span class="em">` accent), `h1_plain`, `lede`, `related` (slugs), `body` (HTML using `<h2>` sections). Rebuild — it appears in the pillar page, resources hub, sitemap, footer and related-links automatically.

## 5. Infrastructure

| Thing | Value |
|---|---|
| S3 bucket | `vse-website-prod` (eu-west-2), CloudFront-only access via OAC |
| CloudFront | `E2MF96XZ37SRTT` → `d3lv0o5sgzlfow.cloudfront.net` |
| ACM cert | us-east-1, covers apex + www, DNS-validated |
| DNS | **Fasthosts** (ns1/ns2.livedns.co.uk). `www` CNAME → CloudFront; apex via Fasthosts web forwarding. Leave the two `_acm-validations` CNAMEs in place forever — they auto-renew the cert |
| Deploy | GitHub Actions on push to `main`; secrets `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `S3_BUCKET`, `CLOUDFRONT_DIST_ID` |
| Analytics | GA4 `G-1SVVZ8ZEVK` + Microsoft Clarity `yh85iv2y4g`, injected into every page via `TRACKING` in `build_pages.py` |
| IndexNow | Key `a13191bf63d09046dad3b2be26c637ef`, file at site root, `indexnow.py` submits `sitemap.xml` on every deploy. Bing/Yandex/Seznam/Naver only, Google does not participate |
| Security headers | CloudFront managed policy `67f7725c-…` (HSTS, nosniff, X-Frame-Options, referrer-policy) |

## 6. Hard-won learnings — read before repeating a mistake

- **MIME types break the site silently.** `aws s3 sync` stamps `binary/octet-stream` unless told otherwise; Chrome then refuses the stylesheet and the page renders white while every other tool reports 200 OK. The Actions workflow now sets `--content-type` per asset class. Never remove that.
- **Always bump `CSSV`** after CSS/JS changes or browsers serve the old file against new HTML.
- **HTML is cached 5 minutes, assets 7 days** — a "stale" page right after deploy is normal and self-heals.
- **Git inside the mounted Dropbox folder fails** ("Operation not permitted" on lock files). Work in `/tmp/vse-website`, then `rsync` a copy to the outputs folder.
- **Fine-grained GitHub PATs need explicit repo access** plus Contents: Read **and write**. Several tokens in this project were read-only and pushes 403'd; classic tokens worked.
- **The AWS deploy user is scoped** — it can sync and invalidate but cannot create a custom CloudFront response-headers policy (needed for a full CSP). That is the one outstanding IAM gap.
- **If a CSP is ever added**, allow-list `clarity.ms` and `googletagmanager.com` in `script-src`/`connect-src` or analytics dies silently.
- **Auditing themes in an offscreen iframe gives false results.** Chrome throttles rendering there, so anything with `transition:color` never completes the theme flip and reads as its pre-flip value: it looks like invisible text. Inject `*{transition:none!important}` before measuring. This produced a false "contrast 1.0" report on half the site.
- **Check the CSS build number when auditing.** Several "failures" were the browser holding a cached stylesheet against new HTML. The audit records the `?v=` of each page it measures; if the numbers differ between pages, the results are stale, not real.
- **The demos stay dark in both themes.** Only the dark surfaces (`.phone`, `.hub`, `.dash`, `.reg-card`, `.player`, `.scan-frame`, `.sess-side`) are pinned. Locking the whole demo container also catches step pills and brand bars that sit on the page background and turns them white-on-white.
- **The wordmark is a white PNG.** Light mode swaps to `logo-long-colour.png` via `content:url()`. Any new placement of the logo needs the same treatment.
- **Small uppercase labels use `--label`, not `--accent`.** `--accent` is only ~3.6:1 on navy. When adding a new eyebrow/tag/step-number rule, use `--label`.
- **Never set CORS headers in the Lambda and on the function URL.** For non-preflight requests Lambda returns *both* sets, the browser sees two `Access-Control-Allow-Origin` headers and rejects the response with a bare "Failed to fetch" — while the function runs and the mail sends. A silent success that is indistinguishable from a hard failure. CORS lives on the function URL only; `infra/contact-form.yaml` is correct and must stay that way.
- **A Lambda function URL needs three things, not one.** `AuthType: NONE`, a resource policy granting `lambda:InvokeFunctionUrl`, *and* (since October 2025) a second statement granting `lambda:InvokeFunction` with `--invoked-via-function-url`. Miss any one and you get 403 with no request ID and no CORS headers.
- **Test a function URL with `aws lambda invoke` first.** It bypasses the URL and CORS entirely, so it separates "handler is broken" from "response is being rejected" in one command. `aws logs tail /aws/lambda/vse-contact-form --since 20m` shows what actually ran.
- **Every asset reference is version-stamped centrally** by `build_pages.py` as it writes each page. `form.js` and `demo.js` were both pinned at `?v=1` for weeks, so browsers ran a stale script against fresh markup and the brand switcher looked broken on the live site while working locally. Don't hard-code a `?v=` in a content module.
- **The demo brand switcher carries four whole scenarios**, not four palettes: sector, event, date, audience size, tickets, agenda, tracks, speakers, exhibitors, polls, quiz, Q&A, chat, roundtables, run order and post-event narrative, plus its own corner radius, display face and label treatment. They mirror the three audiences the business sells to, plus VSE. Adding a fifth means adding every key in `SCENARIOS` — `demo.js` checks nothing at runtime.
- **The nav has three states, and changing one breaks another.** Below 560px the icon mark (`logo-icon-white` / `logo-icon-colour`); 560–1150px the wordmark plus hamburger; above 1150px the full bar. The wordmark is 333px and deliberately cannot shrink (`nav .logo{flex:0 0 auto}`, `max-width:none` to beat the global `img{max-width:100%}`), because letting it shrink is what crushed it to a sliver on tablet landscape. Which then pushed the hamburger off a phone screen, hence the icon breakpoint. **Test 320, 390, 560, 768, 1024, 1180 and 1400 after touching nav CSS** — the three states interact and fixing one width commonly breaks another.
- **The open mobile menu must scroll itself.** It is `position:fixed;inset:0` while `body{overflow:hidden}`, so without `overflow-y:auto` on the list the last items are unreachable on any short screen: an iPhone SE, or any phone in landscape. `overscroll-behavior:contain` stops the scroll chaining to the locked body behind it.
- **This file's open items are a to-do list, not evidence.** An early note saying Search Console and analytics needed setting up survived in Open items long after James had done all of it, and got repeated back to him twice as though it were a finding. Anything in section 8 is unverified by definition: check it, or ask, before stating it as fact. Never present a stale note from this file as a discovery.
- **Keep the 2020 story factual, not dramatic.** "Built in a crisis" was cut for being alarmist. The register is plain statement of what happened: *every event moved online*, *a stream was the only way to hold an event at all*, *the first weeks of the 2020 lockdown*. James's own wording for the homepage is the reference: *"when the world shut down during the 2020 global pandemic"*. Avoid crisis, catastrophe, emergency and similar about the company. (Those words are fine in the guides when they describe a technical failure on air, which is what they actually mean there.)
- **Experience claims must agree, and dates need their context.** The site once said "thirty years" in copy and "40+ years combined" in the stat block three lines below. Fixing that by deleting every number and date went too far the other way: it stripped the context that makes 2020 a strength. **Whenever 2020 appears it is anchored to the pandemic** ("when the world shut down during the 2020 global pandemic", "born in the 2020 shutdown, when a stream was the only way to hold an event at all"). A bare founding date reads as "new"; the same date with the reason reads as rising to a moment. The coherent claim set is: 40+ years combined (the founders' careers), six years of VSE shows, 500+ shows since 2020, founded March 2020 in the pandemic. `tools/claimcheck.py` lists every experience, duration and founding claim on the site with whether its page explains the date, so conflicts are visible in one place. Run it after touching any company claim.
- Breadcrumbs are `<nav>` elements — they need `nav.crumbs{position:static}` or they inherit the fixed header styles and vanish.

## 6a. House style — applies to every word written for James, anywhere

Not only the website: proposals, emails, decks, LinkedIn posts, quotes, docs. The
test is whether a producer who has run a thousand shows would recognise it as
something a person wrote. Audited against Wikipedia's *Signs of AI writing*.

**Punctuation**

- **Em dashes: roughly one per 500 words, and never as a default connector.** This
  was the single strongest tell in the original site copy: 445 across 34,000
  words, about one every 77. Ask what the sentence actually wants. A colon
  introduces an explanation or a list. A full stop separates two thoughts that
  were welded together. Commas bracket a short aside. Parentheses hold a
  cross-reference. A comma in front of an independent clause is a splice, and a
  splice is worse than the dash it replaced.
- Straight quotes and apostrophes, never curly.
- Sentence case in headings. Never Title Case On Every Main Word.

**Words**

- Avoid unless literally accurate in the trade sense: *delve, crucial, pivotal,
  tapestry, testament, vibrant, meticulous, intricate, underscore, showcase,
  foster, leverage, seamless, robust, realm, holistic, transformative,
  cutting-edge, unlock, empower, harness, elevate, garner, bolster, boasts,
  myriad, ever-evolving, navigate the, at the heart of, in today's X landscape*.
  (*Bespoke* for a set build, *seamless* for a cyc, *robust* for a stream are
  fine. They are the words the trade uses.)
- No *not just X, but Y*. No *it's not A, it's B*. No *more than just*.
- No trailing *-ing* commentary: *..., ensuring a smooth experience*, *...,
  highlighting our commitment*, *..., cementing its place*.
- No rule-of-three adjective stacking. Three-item lists of **real things**,
  cameras, deliverables, cities, are fine and good.
- No vague attribution: *many experts say*, *it is widely regarded*. Name the
  source or drop the claim.

**Shape**

- No *Despite its challenges...* or *Looking ahead...* closing paragraph.
- No puffery about significance, legacy or broader industry trends. Say the
  specific thing: *two people on site instead of six*, *£295+VAT half day*,
  *15-45 seconds behind live*.
- Boldface sparingly, roughly one per 250 words, for genuine emphasis, never to
  mark every key phrase.
- British English, VAT stated, prices as `£1,750 +VAT`.
- Write from what VSE has actually done. Concrete beats impressive.

**Tools:** `tools/aicheck.py` scores any copy against the full catalogue of
tells, `tools/dedash.py` rewrites em dashes in bulk, `tools/splicecheck.py`
catches the damage a bulk rewrite can do. Run all three before shipping copy.
All three are currently clean.

## 6b. Structured data — what still earns a rich result

Current inventory across 75 pages: `ProfessionalService` ×74, `BreadcrumbList` ×73, `Article` ×32, `SoftwareApplication` ×8, `FAQPage` ×8, `DefinedTermSet` ×1. All parse cleanly.

- **Breadcrumbs are a presentation feature, not a ranking factor.** Desktop only. The gain is a readable path instead of a raw URL in the result, so a modest CTR effect at best. There is no "more breadcrumbs" lever: coverage is already complete everywhere it is meaningful, and the six pages without a trail (`index`, `404`, and the four top-level pages) are correct to have none. Google requires at least two `ListItem`s, each with `position`, `name` and `item`; `item` is optional on the last entry only. Follow the **typical user path, not the URL structure** — that is the rule most sites fail. `build_pages.py`'s `breadcrumb_html()` accepts a list of trails to declare several routes to one page; the demos use this (module path and demos-index path). The first trail is the one rendered.
- **`FAQPage` no longer does anything.** Google deprecated the FAQ rich result on 7 May 2026 and removed the documentation in June. The markup is valid schema.org and harmless to leave — unused structured data does not hurt Search — but it earns nothing. Don't add more of it expecting a result.
- **`HowTo` was deprecated earlier** (2023). Same position.
- **Still producing rich results:** `Article`, `Event`, `Product`, `Review`/`AggregateRating`, `LocalBusiness`, `VideoObject`. `Organization`/`Person` matter for entity recognition rather than a visible result.
- **`sameAs` on the ProfessionalService block is an empty array.** Filling it (LinkedIn, YouTube, Companies House) is the cheapest real win available in the schema: it is how Google ties the site to the entity.

## 7. Measurement — already in place

Confirmed by James, September 2026. **Do not re-raise these as gaps.**

| | Status |
|---|---|
| Google Search Console | Set up |
| Bing Webmaster Tools | Set up |
| Google Analytics 4 | Set up (`G-1SVVZ8ZEVK`) |
| Microsoft Clarity | Set up (`yh85iv2y4g`) |

**None of this is verifiable from the page source, so do not conclude it is missing.** Site verification is done by DNS TXT at Fasthosts, which is domain-wide and invisible in the HTML. GA4 and Clarity are deliberately consent-gated: `site.js` injects them only after the visitor accepts, so a fetch of the static HTML shows no analytics tags at all. Both absences are correct behaviour, not faults.

## 8. Open items

- Client logo image files (currently the logo marquee is removed; text client cloud carries the names). Originals are on the old WordPress host.
- `sameAs` on the ProfessionalService schema is an empty array — needs LinkedIn, YouTube, Companies House.
- Google Business Profile for the Chichester studio (status unconfirmed — **ask, don't assume**).
- Rotate credentials pasted in chat during setup (GitHub PATs, AWS keys).
- Bare domain `virtualstudio.events` → confirm Fasthosts web forwarding to `www` is live.
- Milliard is a commercial typeface (Rene Bieder) — confirm the licence covers web embedding.

## 9. Recurring automation

`vse-competitor-intel` — scheduled task, 1st of each month 08:00. Researches UK production competitors, platform pricing, feature gaps and SEO positions; writes `Website assets/Competitor intel/YYYY-MM competitor briefing.md` to Dropbox and compares against the previous month.

## 10. Where things live

- Repo / working copy: `/tmp/vse-website` in session; mirrored to the Cowork outputs folder.
- Dropbox: `Virtual Studio Event Dropbox/Virtual Studio Events/` — `Website assets/` (research, DNS notes, competitor intel), `Design elements/` (logos, Milliard font, backgrounds), `Studio Media/` (Chichester, Fareham, Norwich, Manchester photography), `Clients/`, `Showreel/`.
- Brand: navy `#212b54`, teal `#6a9799`, light teal `#9fc4c5`; Milliard (display + body), Instrument Serif italic for accent words.
