#!/usr/bin/env python3
"""Builds search-index.json from the generated pages. Run after build_pages.py."""
import glob, json, re, os

SKIP = {'404.html'}
def text_of(h):
    m = re.search(r'<main id="main">(.*?)</main>', h, re.S)
    src = m.group(1) if m else h
    src = re.sub(r'<(script|style|svg)[^>]*>.*?</\1>', ' ', src, flags=re.S)
    return re.sub(r'\s+', ' ', re.sub('<[^>]+>', ' ', src)).strip()

def build():
    items = []
    for f in sorted(glob.glob('*.html')):
        if f in SKIP: continue
        h = open(f).read()
        title = re.search(r'<title>(.*?)</title>', h, re.S)
        desc = re.search(r'<meta name="description" content="(.*?)"', h, re.S)
        h1 = re.search(r'<h1>(.*?)</h1>', h, re.S)
        t = re.sub('<[^>]+>', '', h1.group(1)).strip() if h1 else (title.group(1).split('|')[0].strip() if title else f)
        d = (desc.group(1) if desc else '')[:190]
        body = text_of(h)
        # keyword pool: headings + first chunk of body
        heads = ' '.join(re.sub('<[^>]+>', ' ', x) for x in re.findall(r'<h[23][^>]*>(.*?)</h[23]>', h, re.S))
        items.append({'u': f, 't': t, 'd': d, 'k': (heads + ' ' + body[:900]).lower()[:1400]})
    json.dump(items, open('search-index.json', 'w'), separators=(',', ':'), ensure_ascii=False)
    return len(items), os.path.getsize('search-index.json')

if __name__ == '__main__':
    n, s = build()
    print(f'search-index.json: {n} pages, {s//1024}KB')
