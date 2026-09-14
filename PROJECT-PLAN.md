# VSE website — project plan

> **Auto-generated.** `build_pages.py` rewrites this file on every build, so the
> numbers below are always the real state of the repo. Only the roadmap section is
> hand-maintained — edit it between the MANUAL markers and it survives rebuilds.
> Strategy, conventions and infrastructure live in **CLAUDE.md**.

**Last build:** 2026-09-14 · **Last commit:** 14 September 2026 · **Commits:** 61

## Where the project stands

| Metric | Value |
|---|---|
| Pages published | 75 |
| Knowledge-hub guides | 32 across 6 pillars |
| Platform capabilities listed | 71 |
| Words of original content | ~30,878 |
| Images / videos in repo | 15 / 12 |

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
| 2026-09-14 | `4828f7b` | Correct the record: Search Console, Bing, GA4 and Clarity are all set up |
| 2026-09-14 | `bc6c24b` | Declare both routes to each demo as separate breadcrumb trails |
| 2026-09-12 | `cd401a1` | Document the three nav states and the mobile menu scroll requirement |
| 2026-09-12 | `e8a91cf` | Use the icon mark in the nav on phone portrait |
| 2026-09-12 | `32bf0a0` | Let the open mobile menu scroll |
| 2026-09-12 | `efc38fb` | Fix the nav squashing the logo and clipping the CTA on tablet |
| 2026-09-12 | `88ab9e3` | Drop the crisis framing from the 2020 story |
| 2026-09-12 | `f5c3c67` | Put the context back around the 2020 date, sitewide |
| 2026-09-12 | `98d1ad6` | Sync .txt, search index and video in CI; submit to IndexNow on deploy |
| 2026-09-12 | `66977ed` | Tidy the new copy against house style; document the demo scenarios and IndexNow |
| 2026-09-12 | `36898e5` | Stamp the cache-busting version on every asset reference centrally |
| 2026-09-12 | `daf1681` | Demo switcher between the four demos, and four real brand scenarios |

## How this file stays current

`build_pages.py` calls `plan.py` as its final step. Every build re-counts pages,
re-reads prices from `content_platform.py`, re-counts guides from `content_hub.py`
and re-reads the git log. To record a decision or a new task, edit only the
roadmap between the MANUAL markers — the rest is derived and will be overwritten.
