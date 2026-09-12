#!/usr/bin/env python3
"""Scan site copy for the writing tells catalogued in Wikipedia's 'Signs of AI writing'.
Reports per-file, per-line hits so they can be rewritten by hand."""
import re, sys, glob, os, html, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- the checks -------------------------------------------------------------
VOCAB = r"""delve|delving|crucial|pivotal|tapestry|testament|vibrant|meticulous(?:ly)?|
intricate|intricacies|interplay|underscor\w+|showcas\w+|foster\w*|leverag\w+|seamless(?:ly)?|
robust|realm|bespoke|holistic|transformative|cutting[- ]edge|state[- ]of[- ]the[- ]art|
unlock\w*|empower\w*|harness\w*|elevat(?:e|es|ed|ing)|garner\w*|bolster\w*|boasts|
myriad|plethora|nuanced|multifaceted|unwavering|enduring|profound(?:ly)?|
dynamic\s+(?:landscape|world|environment)|ever[- ]evolving|ever[- ]changing|
navigat(?:e|es|ing)\s+the|rich\s+history|deep\s+dive|game[- ]?changer|
paradigm|synerg\w+|ecosystem\s+of|treasure\s+trove|stands?\s+as\s+a|
serves?\s+as\s+a|plays?\s+a\s+(?:pivotal|crucial|vital|key)\s+role|
at\s+the\s+heart\s+of|at\s+its\s+core|in\s+today'?s\s+\w+\s+landscape|
in\s+an\s+era\s+(?:of|where)|the\s+world\s+of|when\s+it\s+comes\s+to"""
VOCAB = re.compile('|'.join(p.strip() for p in VOCAB.split('|')), re.I | re.X)

CHECKS = [
 ("em-dash",        re.compile(r'—|&mdash;')),
 ("not-just-X",     re.compile(r"\b(?:not\s+(?:only|just|merely|simply)\b[^.]{0,90}?\bbut\b"
                               r"|isn'?t\s+just\b|aren'?t\s+just\b|it'?s\s+not\s+(?:about\s+)?\w+[^.]{0,60}?,?\s+it'?s\b"
                               r"|doesn'?t\s+just\b|more\s+than\s+just\b)", re.I)),
 ("not-X-but-Y",    re.compile(r"\bnot\s+(?:a|an|the)?\s*\w+[^.,;]{0,40},\s+but\s+", re.I)),
 ("trailing -ing",  re.compile(r",\s+(?:ensuring|allowing|enabling|making\s+it|reflecting|"
                               r"highlighting|underscoring|demonstrating|showcasing|cementing|"
                               r"solidifying|helping\s+to|providing|offering|creating|driving|"
                               r"delivering|positioning|establishing|contributing)\b", re.I)),
 ("ai-vocab",       VOCAB),
 ("rule-of-three",  re.compile(r"\b\w+,\s+\w+,?\s+and\s+\w+\b(?=[\s.,;])")),
 ("whether-you",    re.compile(r"\bwhether\s+you'?(?:re|ve)\b|\bfrom\s+\w+\s+to\s+\w+,\s", re.I)),
 ("curly-quote",    re.compile(r"[‘’“”]")),
 ("challenges-fmt", re.compile(r"\bdespite\s+(?:its|these|the)\b", re.I)),
 ("vague-attrib",   re.compile(r"\b(?:many|some|most)\s+(?:experts|producers|clients|"
                               r"organisations|companies|teams|professionals)\s+(?:say|believe|agree|find)", re.I)),
]

TAG   = re.compile(r'<[^>]+>')
STYLE = re.compile(r'style="[^"]*"')
URLS  = re.compile(r'https?://\S+|assets/\S+|[\w-]+\.(?:html|css|js|jpg|png|webp|mp4|svg)')

def prose(line):
    """Strip markup so we only judge the words a visitor actually reads."""
    s = STYLE.sub(' ', line)
    s = TAG.sub(' ', s)
    s = URLS.sub(' ', s)
    s = html.unescape(s.replace('&mdash;', '—'))
    return s

def scan(paths):
    hits = collections.defaultdict(list)
    counts = collections.Counter()
    for p in paths:
        for n, raw in enumerate(open(p, encoding='utf-8'), 1):
            text = prose(raw)
            if len(text.strip()) < 12:
                continue
            for name, rx in CHECKS:
                for m in rx.finditer(text):
                    counts[name] += 1
                    hits[name].append((os.path.basename(p), n, m.group(0).strip()[:60],
                                       text.strip()[max(0, m.start()-70):m.start()+90]))
    return counts, hits

if __name__ == '__main__':
    files = sorted(glob.glob(os.path.join(ROOT, 'content_*.py'))) + \
            [os.path.join(ROOT, f) for f in ('build_pages.py', 'index.html') if os.path.exists(os.path.join(ROOT, f))]
    counts, hits = scan(files)
    total = sum(counts.values())
    print(f"{total} hits across {len(files)} files\n")
    for name, _ in CHECKS:
        print(f"{counts[name]:>5}  {name}")
    if len(sys.argv) > 1:
        want = sys.argv[1]
        print(f"\n--- {want} ---")
        for f, n, m, ctx in hits[want]:
            print(f"{f}:{n}  [{m}]\n      …{' '.join(ctx.split())}…")
