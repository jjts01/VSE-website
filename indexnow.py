#!/usr/bin/env python3
"""Submit the site's URLs to IndexNow.

IndexNow tells Bing, Yandex, Seznam, Naver and the other participating engines
that a page has changed, instead of waiting for them to crawl round to it.
Google does not participate, so this sits alongside the sitemap rather than
replacing it.

Usage:
    python3 indexnow.py              # submit every URL in sitemap.xml
    python3 indexnow.py a.html b.html   # submit only these
"""
import json, os, re, sys, urllib.request, urllib.error

HOST = 'www.virtualstudio.events'
SITE = f'https://{HOST}/'
ENDPOINT = 'https://api.indexnow.org/IndexNow'
ROOT = os.path.dirname(os.path.abspath(__file__))


def load_key():
    path = os.path.join(ROOT, '.indexnow-key')
    if os.path.exists(path):
        return open(path).read().strip()
    # fall back to whichever <32-hex>.txt sits in the repo root
    for f in os.listdir(ROOT):
        if re.fullmatch(r'[0-9a-f]{8,128}\.txt', f):
            return f[:-4]
    raise SystemExit('No IndexNow key found. Expected .indexnow-key or <key>.txt in the repo root.')


def urls_from_sitemap():
    xml = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
    return re.findall(r'<loc>([^<]+)</loc>', xml)


def submit(urls, key):
    payload = {
        'host': HOST,
        'key': key,
        'keyLocation': f'{SITE}{key}.txt',
        'urlList': urls,
    }
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode(),
        headers={'Content-Type': 'application/json; charset=utf-8'},
        method='POST')
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode()[:200]
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:300]
    except Exception as e:
        return None, str(e)


if __name__ == '__main__':
    key = load_key()
    if len(sys.argv) > 1:
        urls = [u if u.startswith('http') else SITE + u.lstrip('/') for u in sys.argv[1:]]
    else:
        urls = urls_from_sitemap()
    # IndexNow accepts up to 10,000 URLs per request
    status, body = submit(urls[:10000], key)
    print(f'{len(urls)} URLs -> HTTP {status}')
    if body:
        print(body)
    # 200 accepted, 202 accepted but key still being validated
    sys.exit(0 if status in (200, 202) else 1)
