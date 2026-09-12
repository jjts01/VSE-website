#!/usr/bin/env python3
"""Thin out formulaic em dashes, using only transforms that are safe on any prose.

The em dash is not banned. What reads as machine-made is density and sameness:
every aside, every afterthought, every label pinned on with the same mark. This
pass makes the changes that cannot break a sentence, and leaves the judgement
calls to be finished by hand.

  A — aside — B   ->  A (aside) B        parentheses never break a sentence
  ... — and/but   ->  comma              comma + conjunction is correct
  label: — text   ->  colon
  clause — clause ->  full stop
  ... — list      ->  colon
  anything else   ->  comma, but never in front of an independent clause
"""
import re, glob, os, sys

VERB = (r"\b(?:seen|done|been|made|said|found|built|heard|left|meant|kept|told|gone|"
        r"taken|given|known|thought|brought|caught|bought|sold|held|won|lost|paid|"
        r"is|are|was|were|isn't|aren't|has|have|had|will|won't|would|can|can't|could|"
        r"should|does|doesn't|do|don't|didn't|shows?|means?|gets?|goes?|comes?|reads?|costs?|"
        r"takes?|makes?|needs?|works?|happens?|matters?|counts?|helps?|keeps?|leaves?|gives?|"
        r"sits?|runs?|looks?|feels?|wants?|buys?|pays?|starts?|ends?|turns?|puts?|adds?|"
        r"saves?|lets?|tends?|stops?|breaks?|fails?|arrives?|lands?|wins?|beats?|expects?|"
        r"assumes?|traces?|lives?|dies?|flows?|sends?|holds?|knows?|sees?|says?|calls?|"
        r"becomes?|remains?|stays?|appears?|seems?|joins?|builds?|reaches?|changes?|"
        r"explains?|covers?|handles?|requires?|allows?|includes?|uses?|offers?|provides?|"
        r"delivers?|records?|streams?|sends?|drops?|rises?|falls?|opens?|closes?|feeds?|"
        r"pushes|push|pulls?|describes?|applies|apply|answers?|asks?|tells?|writes?|"
        r"sets?|sits|meets?|misses|miss|hides?|scales?|doubles?|halves?|traces|trace|"
        r"be|been|being|lets|let|kills?|beats|beat|wants|want|suits?|fits?|lasts?)\b")
SUBJ = (r"(?:it|they|we|you|he|she|that|this|these|those|there|the|a|an|his|her|its|their|"
        r"our|your|most|every|each|both|one|two|three|some|any|no|nothing|everything|"
        r"anyone|nobody|someone|people|clients?|audiences?|[A-Z][a-z]+)\b")
CONJ = re.compile(r"^(?:and|but|yet|or|so|nor|then)\b", re.I)
# a dependent or prepositional opener: a comma is always right in front of these
DEP  = re.compile(r"^(?:with|without|plus|including|from|plain|for|in|on|at|by|plus|to|as|like|"
                  r"after|before|until|while|where|which|who|whose|when|though|although|"
                  r"because|since|unless|even|often|usually|always|never|just|only|\w+ing|\w+ed)\b", re.I)

tags   = lambda t: re.sub(r'<[^>]+>', '', t)
clause = lambda t: bool(re.match(SUBJ, t, re.I) and re.search(VERB, t[:160], re.I))
verby  = lambda t: bool(re.search(VERB, t[:160], re.I))

DASH = re.compile(r'(?<!>)\s*(?:—|&mdash;)\s*(?!<)')
# a matched pair on one line; the aside may itself contain markup
PAIR = re.compile(r'(\S)\s*(?:—|&mdash;)\s*((?:(?!—|&mdash;|;|\. ).){3,120}?)\s*(?:—|&mdash;)\s*(?=\w|<)')

def fix_pairs(line):
    def sub(m):
        head, inner = m.group(1), m.group(2).strip()
        bare = tags(inner).strip()
        if not re.search(r'\w', bare):     # markup only: an empty table cell, not an aside
            return m.group(0)
        # a short, comma-free noun phrase sits fine between commas and keeps the
        # sentence lighter than brackets would
        if ',' not in bare and not verby(bare) and len(bare.split()) <= 4:
            return f"{head}, {inner}, "
        rest = m.string[m.end():]
        # a subordinate clause that was interrupted, or an apposed list, needs a
        # comma after the bracket closes; a bare subject-verb interruption doesn't
        sub = re.match(r'\s*(?:if|when|while|unless|although|though|because|after|'
                       r'before|once|since)\b', tags(m.string[:m.start()]).strip(), re.I)
        need = bool(sub) or (',' in bare and not verby(tags(rest).lstrip()[:30]))
        return f"{head} ({inner}){',' if need else ''} "
    prev = None
    while prev != line:                     # handle more than one pair per line
        prev, line = line, PAIR.sub(sub, line)
    return line

def classify(left, right):
    r  = tags(right).lstrip()
    lt = tags(left).rstrip()
    n  = len(r.split())

    if CONJ.match(r):
        return ', ', False
    if re.search(r'</strong>\s*$|</b>\s*$', left.rstrip()):
        return ': ', False
    if lt and lt[0].isupper() and 0 < len(lt.split()) <= 5 and not verby(lt):
        return ': ', False
    if DEP.match(r):
        return ', ', False
    # a list in apposition takes a colon, whatever the shape of the left side
    if ',' in r[:100] and not verby(r):
        return ': ', False
    if clause(r) and n >= 3:
        # never end a sentence with a full stop when the question mark is still
        # to come: the dash was holding open a single question
        rest = re.split(r'(?<=[.?!])\s', r, 1)[0]
        if rest.rstrip().endswith('?') and not lt.rstrip().endswith('?'):
            return ', ', False
        return ('. ', True) if verby(lt) else (': ', False)
    return ', ', False

def fix_line(line):
    if '—' not in line and '&mdash;' not in line:
        return line
    line = fix_pairs(line)
    out, pos = [], 0
    for m in DASH.finditer(line):
        left, right = line[pos:m.start()], line[m.end():]
        out.append(left)
        rep, cap = classify(left, right)
        out.append(rep)
        if cap:
            mm = re.match(r'(\s*(?:<[^>]+>)*)([a-z])', right)
            if mm:
                out.append(mm.group(1) + mm.group(2).upper())
                pos = m.end() + mm.end()
            else:
                pos = m.end()
        else:
            pos = m.end()
    out.append(line[pos:])
    s = ''.join(out)
    s = re.sub(r',\s*,', ',', s)
    s = re.sub(r'\s+([,.;:)])', r'\1', s)
    s = re.sub(r'\(\s+', '(', s)
    s = re.sub(r'([,:;])\s*\1+', r'\1', s)
    s = re.sub(r'\.\s*\.', '.', s)
    s = re.sub(r'(?<=[.,:;])  +', ' ', s)
    return s

if __name__ == '__main__':
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)
    n = 0
    for p in [f for f in sorted(glob.glob('content_*.py')) + ['build_pages.py', 'index.html']
              if os.path.exists(f)]:
        src = open(p, encoding='utf-8').read()
        before = src.count('—') + src.count('&mdash;')
        res = '\n'.join(fix_line(l) for l in src.split('\n'))
        after = res.count('—') + res.count('&mdash;')
        if res != src:
            n += before - after
            if '--dry' not in sys.argv:
                open(p, 'w', encoding='utf-8').write(res)
            print(f"{os.path.basename(p):<24} {before:>4} -> {after}")
    print(f"\n{n} removed")
