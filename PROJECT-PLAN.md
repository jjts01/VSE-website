# VSE website — project plan

> **Auto-generated.** `build_pages.py` rewrites this file on every build, so the
> numbers below are always the real state of the repo. Only the roadmap section is
> hand-maintained — edit it between the MANUAL markers and it survives rebuilds.
> Strategy, conventions and infrastructure live in **CLAUDE.md**.

**Last build:** 2026-09-12 · **Last commit:** 12 September 2026 · **Commits:** 24

## Where the project stands

| Metric | Value |
|---|---|
| Pages published | 74 |
| Knowledge-hub guides | 32 across 6 pillars |
| Platform capabilities listed | 71 |
| Words of original content | ~31,160 |
| Images / videos in repo | 12 / 6 |

## Site inventory

| Section | Pages | Examples |
|---|---|---|
| Core | 7 | 404.html, about.html, contact.html, index.html … |
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

- [ ] **Deploy workflow is missing the video sync line.** The PAT used for pushes lacks `workflow` scope, so `.github/workflows/deploy.yml` could not be updated. Videos are currently uploaded to S3 by hand. Add this line after the `*.png` sync line in the "Sync assets" step:
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
| 2026-09-12 | `20ca3a0` | Deploy: sync assets/video with video/mp4 content-type |
| 2026-09-12 | `7694891` | Six generated video loops (hero, platform, gallery, awards, global network, audience) with posters and reduced-motion handling |
| 2026-09-12 | `4b92c30` | Add CLAUDE.md brief and self-updating PROJECT-PLAN.md; 24 generated brand images across event types, pillars, platform modules and studios |
| 2026-09-12 | `6248fd7` | Tracking on 404 page |
| 2026-09-12 | `97bae60` | Add Microsoft Clarity and Google Analytics (GA4) tags to every page |
| 2026-09-12 | `8ce2b11` | Packages meta pricing |
| 2026-09-12 | `0c63172` | Market-benchmarked pricing (Sept 2026), platform-only and Engage-only tiers, full feature matrix page, global CDN + UK/EU residency + AI + security features, cost guide benchmarks with sources, news item |
| 2026-09-12 | `2ed0260` | Hub meeting card layout |
| 2026-09-12 | `a7dd62b` | Fix demo background image paths |
| 2026-09-12 | `ad8463f` | VSE Platform: overview, 7 modules, pipeline, packages/integrations, 4 working demos (participation, registration, event hub, analytics); nav/footer/homepage integration |
| 2026-09-12 | `79d17c8` | Fix breadcrumb inheriting header nav styles |
| 2026-09-12 | `761882f` | Knowledge hub: 6 pillars, 32 guides, 7 event-type landing pages, tools, templates, glossary, news; mobile nav; footer sitemap; breadcrumbs; auto sitemap |

## How this file stays current

`build_pages.py` calls `plan.py` as its final step. Every build re-counts pages,
re-reads prices from `content_platform.py`, re-counts guides from `content_hub.py`
and re-reads the git log. To record a decision or a new task, edit only the
roadmap between the MANUAL markers — the rest is derived and will be overwritten.
