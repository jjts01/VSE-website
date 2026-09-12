# VSE website — project plan

> **Auto-generated.** `build_pages.py` rewrites this file on every build, so the
> numbers below are always the real state of the repo. Only the roadmap section is
> hand-maintained — edit it between the MANUAL markers and it survives rebuilds.
> Strategy, conventions and infrastructure live in **CLAUDE.md**.

**Last build:** 2026-09-12 · **Last commit:** 12 September 2026 · **Commits:** 50

## Where the project stands

| Metric | Value |
|---|---|
| Pages published | 75 |
| Knowledge-hub guides | 32 across 6 pillars |
| Platform capabilities listed | 71 |
| Words of original content | ~30,868 |
| Images / videos in repo | 13 / 12 |

## Site inventory

| Section | Pages | Examples |
|---|---|---|
| Core | 8 | 404.html, about.html, contact.html, index.html … |
| VSE Platform | 12 | demos.html, pipeline.html, platform-brand.html, platform-broadcast.html … |
| Interactive demos | 4 | demo-analytics.html, demo-audience.html, demo-event-hub.html, demo-registration.html |
| Event-type landing pages | 8 | event-agm-investor.html, event-awards-show.html, event-hybrid-conference.html, event-product-launch.html … |
| Knowledge pillars | 6 | pillar-analytics.html, pillar-infrastructure.html, pillar-live-production.html, pillar-platforms.html … |
| Guides | 32 | guide-accessibility.html, guide-cdn-players.html, guide-cloud-production.html, guide-encoders-bitrates.html … |
| Reference & tools | 5 | glossary.html, news.html, resources.html, templates.html … |

## Published pricing

| Package | Price |
|---|---|
| Broadcast | from £1,750 +VAT per event |
| Engage | from £7,500 +VAT per event |
| Enterprise programme | from £30,000 +VAT per year |
| Platform licence (agencies & in-house teams) | from £1,500 +VAT per event · £12,000 +VAT per year |
| Engage only | from £350 +VAT per event · £2,400 +VAT per year |

Benchmarked September 2026 — see `Website assets/Market pricing research - Sept 2026.md` in Dropbox for sources.

## Roadmap

<!-- MANUAL:START -->
### Now (this quarter)

- [ ] **Confirm the video loops actually play in a real browser.** Six generated loops (hero, platform, gallery, awards, global-network, audience) are deployed as MP4 (H.264, faststart) + WebM (VP9), with poster images and reduced-motion handling. Files serve correctly (200/206, right MIME, Accept-Ranges) and the markup is valid, but the automated browser used to verify would not decode either codec (readyState stayed 0), so playback is unverified. The poster frames render correctly as a fallback, so nothing looks broken either way. Check on a normal machine; if they don't play, the posters can simply stay.

- [ ] **Deploy workflow needs two lines added** (the PAT used for pushes lacks `workflow` scope, so `.github/workflows/deploy.yml` can't be updated from here; `assets/video/` and `search-index.json` are currently uploaded to S3 by hand). Add to the "Sync assets" step:
      `aws s3 sync assets/video s3://${{ secrets.S3_BUCKET }}/assets/video --content-type "video/mp4" --cache-control "public,max-age=2592000"`
      `aws s3 sync assets/video s3://${{ secrets.S3_BUCKET }}/assets/video --exclude "*" --include "*.webm" --content-type "video/webm" --cache-control "public,max-age=2592000"`
      and to the "Sync pages" step add `--include "search-index.json"`.
- [ ] **Contact form backend** — run `infra/contact-form.yaml` (see `Website assets/SETUP - contact form and SES DNS.md`), then send me the Function URL to paste into `FORM_ENDPOINT`.
- [ ] **SES DNS records** — add the verification TXT and three DKIM CNAMEs at Fasthosts (same setup doc).
- [ ] ~~Deploy workflow is missing the video sync line.~~ The PAT used for pushes lacks `workflow` scope, so `.github/workflows/deploy.yml` could not be updated. Videos are currently uploaded to S3 by hand. Add this line after the `*.png` sync line in the "Sync assets" step:
      `aws s3 sync assets/video s3://${{ secrets.S3_BUCKET }}/assets/video --content-type "video/mp4" --cache-control "public,max-age=2592000"`

- [ ] Verify domain in Google Search Console and submit the sitemap
- [ ] Create a Google Business Profile for the Chichester studio
- [ ] Recover client logo files from the old WordPress host and restore the logo marquee
- [ ] Rotate the GitHub PAT and AWS keys shared during setup; scope the deploy user down to sync + invalidate
- [ ] Confirm the bare domain forwards to www
- [ ] James to redline the published package prices against real margins

### Next

- [ ] Contact form backed by Lambda + SES (currently mailto only)
- [ ] Showreel video in the homepage hero (needs the Showreel folder made available offline in Dropbox)
- [ ] Real case studies with named clients, once permissions are cleared
- [ ] Add `cloudfront:CreateResponseHeadersPolicy` to the deploy user, then ship a full Content-Security-Policy (allow-list clarity.ms and googletagmanager.com)
- [ ] Monthly cadence: one new guide or news item, informed by the competitor briefing

### Someday

- [ ] Git-based CMS (Decap/Tina) so non-technical edits don't need a build
- [ ] Case-study schema and a filterable work index
- [ ] Reseller portal for agency partners
<!-- MANUAL:END -->

## Recent changes

| Date | Commit | Change |
|---|---|---|
| 2026-09-12 | `daf1681` | Demo switcher between the four demos, and four real brand scenarios |
| 2026-09-12 | `f2de199` | Fix conflicting experience claims; add IndexNow key and submitter |
| 2026-09-12 | `4d55e83` | Record the function URL CORS and permission learnings in CLAUDE.md |
| 2026-09-12 | `28d56b3` | Switch the enquiry form to the live endpoint |
| 2026-09-12 | `f1d933a` | Keep both origins in the template so a redeploy doesn't drop the apex domain |
| 2026-09-12 | `103987a` | Stop the Lambda sending its own CORS headers: the function URL already does |
| 2026-09-12 | `ae4b7bc` | Footer base link tap targets; record the theme-audit learnings in CLAUDE.md |
| 2026-09-12 | `6d6df8e` | Give footer links a 24px tap target |
| 2026-09-12 | `bfcc246` | Make the event-hub demo's placeholder actions inert spans, not href=# links |
| 2026-09-12 | `72975d8` | Fix three label rules where the new colour was overridden by the old one |
| 2026-09-12 | `d9c3614` | Darken the phone LIVE badge to match the broadcast one |
| 2026-09-12 | `4059cb4` | Clear the last small-label contrast misses |

## How this file stays current

`build_pages.py` calls `plan.py` as its final step. Every build re-counts pages,
re-reads prices from `content_platform.py`, re-counts guides from `content_hub.py`
and re-reads the git log. To record a decision or a new task, edit only the
roadmap between the MANUAL markers — the rest is derived and will be overwritten.
