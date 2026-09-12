#!/usr/bin/env python3
"""Regenerates PROJECT-PLAN.md from the actual state of the repo.

Called automatically at the end of build_pages.py, so the plan can never drift
from reality: every build re-counts the pages, re-reads the prices out of the
content modules, and re-reads the git history for the changelog.

Hand-written sections are preserved between <!-- MANUAL:START --> and
<!-- MANUAL:END --> markers. Everything else is regenerated.
"""
import os, re, glob, subprocess, datetime

PLAN = 'PROJECT-PLAN.md'
MANUAL_START = '<!-- MANUAL:START -->'
MANUAL_END = '<!-- MANUAL:END -->'

DEFAULT_MANUAL = """### Now (this quarter)

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
"""

def sh(cmd, default=''):
    try:
        return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return default

def categorise():
    """Group the built pages into sections."""
    pages = sorted(os.path.basename(p) for p in glob.glob('*.html'))
    buckets = {
        'Core': [], 'VSE Platform': [], 'Interactive demos': [], 'Event-type landing pages': [],
        'Knowledge pillars': [], 'Guides': [], 'Reference & tools': [],
    }
    for p in pages:
        if p.startswith('demo-'): buckets['Interactive demos'].append(p)
        elif p.startswith('platform') or p in ('pipeline.html', 'demos.html'): buckets['VSE Platform'].append(p)
        elif p.startswith('event-'): buckets['Event-type landing pages'].append(p)
        elif p.startswith('pillar-'): buckets['Knowledge pillars'].append(p)
        elif p.startswith('guide-'): buckets['Guides'].append(p)
        elif p in ('glossary.html', 'tools.html', 'templates.html', 'news.html', 'resources.html'):
            buckets['Reference & tools'].append(p)
        else: buckets['Core'].append(p)
    return pages, buckets

def content_words():
    """Rough word count of the <main> content across guides, events and reference pages."""
    total = 0
    for f in glob.glob('guide-*.html') + glob.glob('event-*.html') + glob.glob('platform*.html') + ['glossary.html', 'news.html']:
        try:
            h = open(f).read()
            m = re.search(r'<main id="main">(.*?)</main>', h, re.S)
            if m: total += len(re.sub('<[^>]+>', ' ', m.group(1)).split())
        except Exception:
            pass
    return total

def prices():
    try:
        import content_platform as cp
        rows = [(p[0], p[2]) for p in cp.PACKAGES]
        rows += [(p[0], p[2]) for p in getattr(cp, 'PLATFORM_ONLY', [])]
        return rows
    except Exception:
        return []

def feature_count():
    try:
        import content_platform as cp
        return sum(len(fs) for _, fs in getattr(cp, 'FEATURE_MATRIX', []))
    except Exception:
        return 0

def guide_count():
    try:
        import content_hub as ch
        return len(ch.GUIDES), len(ch.PILLARS)
    except Exception:
        return 0, 0

def build():
    today = datetime.date.today().isoformat()
    pages, buckets = categorise()
    guides, pillars = guide_count()
    words = content_words()
    feats = feature_count()
    imgs = len(glob.glob('assets/img/*'))
    vids = len(glob.glob('assets/video/*'))
    commits = sh("git log --oneline -12 --pretty=format:'%h|%ad|%s' --date=short")
    total_commits = sh("git rev-list --count HEAD", '?')
    last = sh("git log -1 --pretty=format:'%ad' --date=format:'%d %B %Y'", today)

    # preserve the manual roadmap
    manual = DEFAULT_MANUAL
    if os.path.exists(PLAN):
        old = open(PLAN).read()
        if MANUAL_START in old and MANUAL_END in old:
            manual = old.split(MANUAL_START)[1].split(MANUAL_END)[0].strip('\n')

    inv = '\n'.join(
        f'| {k} | {len(v)} | {", ".join(v[:4])}{" …" if len(v) > 4 else ""} |'
        for k, v in buckets.items() if v)

    price_rows = '\n'.join(f'| {n} | {p} |' for n, p in prices()) or '| _(not found)_ | |'

    changelog = '\n'.join(
        f'| {c.split("|")[1]} | `{c.split("|")[0]}` | {c.split("|")[2]} |'
        for c in commits.split('\n') if c.count('|') >= 2)

    out = f"""# VSE website — project plan

> **Auto-generated.** `build_pages.py` rewrites this file on every build, so the
> numbers below are always the real state of the repo. Only the roadmap section is
> hand-maintained — edit it between the MANUAL markers and it survives rebuilds.
> Strategy, conventions and infrastructure live in **CLAUDE.md**.

**Last build:** {today} · **Last commit:** {last} · **Commits:** {total_commits}

## Where the project stands

| Metric | Value |
|---|---|
| Pages published | {len(pages)} |
| Knowledge-hub guides | {guides} across {pillars} pillars |
| Platform capabilities listed | {feats} |
| Words of original content | ~{words:,} |
| Images / videos in repo | {imgs} / {vids} |

## Site inventory

| Section | Pages | Examples |
|---|---|---|
{inv}

## Published pricing

| Package | Price |
|---|---|
{price_rows}

Benchmarked September 2026 — see `Website assets/Market pricing research - Sept 2026.md` in Dropbox for sources.

## Roadmap

{MANUAL_START}
{manual}
{MANUAL_END}

## Recent changes

| Date | Commit | Change |
|---|---|---|
{changelog}

## How this file stays current

`build_pages.py` calls `plan.py` as its final step. Every build re-counts pages,
re-reads prices from `content_platform.py`, re-counts guides from `content_hub.py`
and re-reads the git log. To record a decision or a new task, edit only the
roadmap between the MANUAL markers — the rest is derived and will be overwritten.
"""
    open(PLAN, 'w').write(out)
    return len(pages), guides, words

if __name__ == '__main__':
    p, g, w = build()
    print(f'PROJECT-PLAN.md updated: {p} pages, {g} guides, ~{w:,} words')
