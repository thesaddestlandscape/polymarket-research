import csv, io, json, sys, time, requests, os
hdr = open('/root/polymarket-research/data/markets/2026-11-13.csv', errors='replace').readline().strip().split(',')
f = open('/root/polymarket-research/data/markets/2026-11-13.csv', 'rb'); f.seek(-4000000, 2); f.readline()
rows = list(csv.DictReader(io.StringIO(f.read().decode('utf8', 'replace')), fieldnames=hdr))
seen = {}; 
for r in rows:
    sl = r.get('slug') or ''
    k = '5m' if 'updown-5m' in sl else '15m' if 'updown-15m' in sl else '1h' if 'up-or-down' in sl else None
    if k: seen[r['market_id']] = (k, r['market_id'], sl, r['condition_id'])
by = {}
for v in seen.values(): by.setdefault(v[0], []).append(v)
print({k: len(v) for k, v in by.items()})
sel = [x for k in ('5m', '15m', '1h') for x in by.get(k, [])[-9:]]
def gamma(mid):
    j = requests.get(f'https://gamma-api.polymarket.com/markets/{mid}', timeout=10).json()
    tk = json.loads(j['clobTokenIds']) if isinstance(j['clobTokenIds'], str) else j['clobTokenIds']
    oc = json.loads(j['outcomes']) if isinstance(j['outcomes'], str) else j['outcomes']
    return tk, oc
ok = bad = 0; lat = []
for k, mid, sl, cid in sel:
    a = sl
    try: gt, go = gamma(mid)
    except Exception as ex: print('gamma falla', mid, ex); continue
    g = (gt[0], gt[1]) if str(go[0]).lower() in ('up', 'yes') else (gt[1], gt[0])
    t0 = time.time(); r = requests.get(f'https://clob.polymarket.com/markets/{cid}', timeout=8); lat.append(time.time() - t0)
    if r.status_code != 200: print('clob', r.status_code, cid[:12]); bad += 1; continue
    j = r.json(); tk = j.get('tokens') or []
    outs = [(x.get('outcome'), x.get('token_id')) for x in tk]
    yes = [t for o, t in outs if str(o).strip().lower() in ('yes', 'up')]; no = [t for o, t in outs if str(o).strip().lower() in ('no', 'down')]
    same = len(yes) == 1 and len(no) == 1 and (yes[0], no[0]) == (g[0], g[1]) and j.get('condition_id') == cid
    ok += same; bad += (not same)
    print(a, mid, 'outcomes', [o for o, _ in outs], 'igual_gamma', same, 'closed', j.get('closed'), 'active', j.get('active'), 'accepting', j.get('accepting_orders'))
print('OK', ok, 'MAL', bad, 'lat clob p50 %.0f ms' % (1000 * sorted(lat)[len(lat) // 2]) if lat else '')
# mercado inexistente
for c in ('0x' + '0' * 64, '0x' + 'ab' * 32):
    r = requests.get(f'https://clob.polymarket.com/markets/{c}', timeout=8); print('inexistente', r.status_code, r.text[:80])
# orden invertido? cuenta mercados donde gamma tokens[0] no es yes
