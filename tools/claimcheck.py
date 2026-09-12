#!/usr/bin/env python3
"""List every experience, duration and founding claim on the site, so conflicts
between them are visible in one place.

The site once said "thirty years" in homepage copy and "40+ years combined" in
the stat block three lines below it, and claimed a 2020 founding date without
saying why 2020 mattered. Numbers about the company are a credibility surface:
they need to agree with each other, and a date needs its context or it just
reads as "new".
"""
import re, glob, html, collections

PATTERNS = [
    ('years',    re.compile(r'\b(?:\d+\s*\+?|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|twenty|thirty|forty|fifty)[\s-]+years?\b', re.I)),
    ('decades',  re.compile(r'\b(?:a|two|three|four|several|many)?\s*decades?\b', re.I)),
    ('since',    re.compile(r'\bsince\s+(?:19|20)\d{2}\b', re.I)),
    ('year',     re.compile(r'\b(?:in|from|founded|established|started)\s+(?:19|20)\d{2}\b', re.I)),
    ('founding', re.compile(r'\b(?:founded|established|set up|started out|born)\b', re.I)),
    ('shows',    re.compile(r'\b\d[\d,]*\+?\s+(?:shows?|jobs?|events?|productions?)\s+delivered\b', re.I)),
]
CONTEXT = re.compile(r'pandemic|lockdown|shut down|shutdown|venues were dark|crisis|covid', re.I)
# claims inside sourced market commentary are about the industry, not about VSE
THIRD_PARTY = re.compile(r'survey|industry estimates|projected|forecast|market at|respondents|report(?:s|ed)? that|according to', re.I)
OURS = re.compile(r"\b(?:we|we've|we're|our|us|VSE|Virtual Studio Events|James Jones|Ben O'Dwyer)\b", re.I)
TAG = re.compile(r'<[^>]+>')

def prose(f):
    s = open(f, encoding='utf-8').read()
    s = re.sub(r'<(script|style|nav|footer|head)\b.*?</\1>', '', s, flags=re.S)
    return ' '.join(html.unescape(TAG.sub(' ', s)).split())

if __name__ == '__main__':
    found = collections.defaultdict(list)
    for f in sorted(glob.glob('*.html')):
        t = prose(f)
        for name, rx in PATTERNS:
            for m in rx.finditer(t):
                frag = t[max(0, m.start() - 90):m.start() + 110]
                # a date is "in context" if the page explains it anywhere the
                # reader will see, not only in the sentence it sits in
                in_ctx = bool(CONTEXT.search(t))
                # skip claims that belong to a cited third party
                if THIRD_PARTY.search(frag) and not OURS.search(frag):
                    continue
                found[name].append((f, m.group(0).strip(), frag, in_ctx))

    for name, _ in PATTERNS:
        hits = found[name]
        if not hits:
            continue
        # collapse identical claims that repeat across pages
        seen = collections.Counter(h[1].lower() for h in hits)
        print(f'\n=== {name} ({len(hits)} across the site) ===')
        for claim, n in seen.most_common():
            ex = next(h for h in hits if h[1].lower() == claim)
            ctx = 'in context' if ex[3] else 'NO CONTEXT'
            print(f'  {n:>3}x  "{ex[1]}"  [{ctx}]  {ex[0]}')
            if name in ('since', 'year', 'founding') and not ex[3]:
                print(f'         …{ex[2][:150]}…')
