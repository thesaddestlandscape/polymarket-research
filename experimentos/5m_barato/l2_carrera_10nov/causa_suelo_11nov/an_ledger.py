import json, collections, numpy as np, datetime
f = '/root/polymarket-research-datalogs/experimento_h47_B_ledger.jsonl'
tipos = collections.Counter(); tok = {}; lat = []
for ln in open(f):
    try: e = json.loads(ln)
    except Exception: continue
    tipos[e.get('tipo')] += 1
    if e.get('tipo') in ('intencion_post', 'post_ok') and e.get('tok'): tok[e.get('oid')] = e['tok']
    if e.get('tipo') == 'post_lat': lat.append(e)
print(tipos.most_common(15)); print(len(lat), lat[0])
seen = set(); rows = []
for e in sorted(lat, key=lambda e: e['t_call0']):
    t = tok.get(e['oid']); primera = t not in seen if t else None
    if t: seen.add(t)
    rows.append((datetime.datetime.utcfromtimestamp(e['t_call0']).strftime('%m-%d'), e['ms'], primera))
import itertools
for d, g in itertools.groupby(rows, key=lambda r: r[0]):
    g = list(g); a = np.array([x[1] for x in g]); p = np.array([x[2] is True for x in g]); 
    s = f"{d} n={len(g)} p50={np.median(a):.0f} p10={np.percentile(a,10):.0f} p90={np.percentile(a,90):.0f}"
    if p.any() and (~p).any(): s += f" | primera-del-token n={p.sum()} p50={np.median(a[p]):.0f} ; resto n={(~p).sum()} p50={np.median(a[~p]):.0f}"
    print(s)
