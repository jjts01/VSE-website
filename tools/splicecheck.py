#!/usr/bin/env python3
"""Flag comma splices and other punctuation damage introduced while thinning em dashes.
A splice is worse writing than the dash it replaced, so nothing ships until this is clean."""
import re, glob, os, sys, html
SUBJ = (r"(?:(?:it|they|we|you|he|she|there)(?:'(?:ve|ll|d|re|s|m))?|"
        r"the|a|an|his|her|its|their|our|your|most|every|each|one|people|clients?|audiences?)")
VERB = (r"(?:seen|done|been|got|had|made|said|found|run|built|"
        r"is|are|was|were|isn't|aren't|has|have|will|won't|would|can|can't|does|"
        r"doesn't|do|don't|didn't|shows?|means?|gets?|goes?|comes?|costs?|takes?|makes?|"
        r"needs?|works?|happens?|matters?|keeps?|gives?|runs?|looks?|feels?|starts?|"
        r"ends?|changes?|explains?|covers?|requires?|allows?|includes?|uses?|offers?|"
        r"provides?|delivers?|sends?|becomes?|remains?|seems?|reaches?|traces?)")
PATS = [
 ("comma splice", re.compile(rf",\s+{SUBJ}\s+{VERB}\b", re.I)),
 ("double punct",  re.compile(r"[,;:]\s*[,;:]|\(\s*\)|\s+[,.;:]")),
 ("colon+conj",    re.compile(r":\s+(?:and|but|yet|or|so|nor)\b", re.I)),
  ("lower after .", re.compile(r"(?<![A-Z0-9])\.\s+[a-z]{2,}")),
]
TAG=re.compile(r'<[^>]+>')
def prose(l):
    s=re.sub(r'style="[^"]*"', ' ', l)
    s=TAG.sub('', s)                 # no space: tags must not fake a gap before punctuation
    return html.unescape(s)

# python statements and inline scripts are not prose
CODE = re.compile(r'^\s*(?:_?\w+\s*=|def |import |from |for |if |print|return|P\[|#|\(function)')
ABBR = re.compile(r'\b(?:a\.m|p\.m|e\.g|i\.e|vs|etc|Mr|Mrs|Ltd|No|approx)\.$', re.I)
n=0
for p in sorted(glob.glob('content_*.py'))+['build_pages.py','index.html']:
    if not os.path.exists(p): continue
    for i,raw in enumerate(open(p,encoding='utf-8'),1):
        if CODE.match(raw) and not any(k in raw for k in ('<p>','lede=','desc=','card=')):
            continue
        t=prose(raw)
        if len(t.strip())<12: continue
        for name,rx in PATS:
            for m in rx.finditer(t):
                if name == "lower after ." and ABBR.search(t[:m.start()+1]): continue
                # "Because X, Y is Z" is a correct subordinate clause, not a splice
                if name == "comma splice" and re.search(
                        r'\b(?:because|when|while|although|though|if|unless|since|after|'
                        r'before|once|as|where|whereas|until)\b[^,]{0,120}$',
                        t[:m.start()], re.I): continue
                n+=1
                print(f"{os.path.basename(p)}:{i} [{name}] …{' '.join(t[max(0,m.start()-75):m.start()+85].split())}…")
print(f"\n{n} to check")
