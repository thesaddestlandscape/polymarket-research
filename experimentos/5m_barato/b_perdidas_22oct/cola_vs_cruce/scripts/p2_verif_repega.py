"""Verifica con libro5 cuanto tarda B real en repegar tras un cambio del top (ledger repega vs ultimo cambio del top bid del token)."""
import json, gzip, os, sys, numpy as np, pandas as pd, datetime as dt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util
C = '/root/polymarket-research-datalogs/cola_vs_cruce/'
T = pd.concat([pd.read_csv(f'datos/tok_2026-10-{d}.csv', dtype={'mid': str}) for d in (20, 21, 22)]).drop_duplicates(['act', 'mid', 'lado'])
mid = {(r.act, int(r.fin)): r.mid for r in T.itertuples()}
reps = []
for l in open('/root/polymarket-research-datalogs/experimento_h47_B_ledger.jsonl'):
    try: d = json.loads(l)
    except Exception: continue
    if d.get('tipo') in ('repega', 'cancela_banda') and d.get('real'):
        reps.append(d)
lag = []; nf = 0
cache = {}
for d in reps:
    coin, _, _, st = d['slug'].split('-'); act = coin.upper(); fin = int(st) + 300
    m = mid.get((act, fin))
    if m is None: continue
    p = C + f'mk/{act}_{m}.gz'
    if not os.path.exists(p): nf += 1; continue
    if p not in cache:
        tops = {'Y': [], 'N': []}; bids = {'Y': {}, 'N': {}}
        with gzip.open(p, 'rt', errors='replace') as f:
            try:
                for ln in f:
                    c = ln.rstrip('\n').split(',')
                    if c[1] == 'B':
                        b = {}
                        for x in (c[3] or '').split(';'):
                            if ':' in x:
                                a, z = x.split(':')
                                if float(z) > 0: b[round(float(a), 3)] = float(z)
                        bids[c[0]] = b
                    elif c[1] == 'd':
                        q = round(float(c[3]), 3); z = float(c[4])
                        if z > 0: bids[c[0]][q] = z
                        else: bids[c[0]].pop(q, None)
                    else: continue
                    tb = max(bids[c[0]]) if bids[c[0]] else -1
                    if not tops[c[0]] or tops[c[0]][-1][1] != tb: tops[c[0]].append((int(c[2]), tb))
            except (EOFError, OSError): pass
        cache = {p: tops}
    tops = cache[p]
    t = dt.datetime.fromisoformat(d['ts']).timestamp() * 1000
    # lado de la puja: el token cuyo top bid == d['bid'] justo antes
    best = None
    for L in 'YN':
        arr = tops[L]; ts = [x[0] for x in arr]; j = np.searchsorted(ts, t, 'right') - 1
        if j >= 0 and d.get('bid') is not None and abs(arr[j][1] - d['bid']) < 1e-6: best = (t - arr[j][0]); break
    if best is not None: lag.append(best)
lag = np.array(lag) / 1000
print('repegas', len(reps), 'emparejadas', len(lag), 'sin fichero', nf)
print('retraso repega - ultimo cambio del top (s): p10/p25/p50/p75/p90', np.percentile(lag, [10, 25, 50, 75, 90]).round(3), 'frac<0.5s', round((lag < 0.5).mean(), 3), 'frac>=1.5s', round((lag >= 1.5).mean(), 3))
