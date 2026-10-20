"""M3: profundidad real del nivel 1 a t0+215 ms (extracto BTC, filas q, RECEPCION) para la variante tomador con colchon. Solo lectura."""
import sys, csv, glob, gzip, json, math, random, collections
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/v4_comprar_lo_bueno/r3')
import numpy as np
from simlib import O, DES, kmap
OOS = 1791288000000
def fee(p): return 0.07 * p * (1 - p)
EVs = collections.defaultdict(list)
for f in sorted(glob.glob('/root/polymarket-research-datalogs/vigia_5m_barato/eventos_2026-10-*.csv')):
    for r in csv.DictReader(open(f)):
        if r['regla'] != 'B1_5m' or r['es_primero'] != '1' or r['moneda'] != 'BTC' or int(r['t_deteccion']) < OOS: continue
        EVs[f[-14:-4]].append(r)
RES = []
for D, evs in sorted(EVs.items()):
    try: km = kmap(D)
    except FileNotFoundError: print(D, 'sin extracto'); continue
    want = {}
    for r in evs:
        C = int(r['cierre']); sl = 'YES' if r['lado'] == 'Up' else 'NO'
        k = km.get(('5min', C, sl))
        if k: want[(str(C), k[0])] = r
    Q = collections.defaultdict(list); G = set(c for c, _ in want); TK = set(t for _, t in want)
    with gzip.open(O + f'rows_{D}.csv.gz', 'rt') as fh:
        for ln in fh:
            if ',q,' not in ln[:16]: continue
            c = ln.rstrip('\n').split(',')
            if c[0] in G and c[3] in TK and (c[0], c[3]) in want:
                try: Q[(c[0], c[3])].append((int(c[8]) if c[8] else int(c[2]), float(c[5]) if c[5] not in ('', 'None') else math.nan, float(c[7]) if c[7] not in ('', 'None') else 0.0))
                except (ValueError, IndexError): pass
    for key, r in want.items():
        q = sorted(Q.get(key, []))
        te = int(r['t_deteccion']) + 215
        i = max([j for j, x in enumerate(q) if x[0] <= te], default=None)
        if i is None: continue
        ask, asz = q[i][1], q[i][2]
        sl = 'YES' if r['lado'] == 'Up' else 'NO'; g = 1.0 if DES.get(r['market_compra']) == sl else 0.0
        RES.append(dict(dia=D, cl=r['L215_clase'], plim=float(r['p_limite']), ask=ask, asz=asz, g=g, vig_acc=float(r['L215_acciones'] or 0), vig_p=r['L215_precio']))
    print(D, len(want), 'eventos', flush=True)
json.dump(RES, open('/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_captura_maker/m3_prof.json', 'w'))
def st(rows):
    if not rows: return 'n=0'
    byd = collections.defaultdict(lambda: [0, 0])
    for d, p, c in rows: byd[d][0] += p; byd[d][1] += c
    ds = list(byd); random.seed(1); bs = []
    for _ in range(2000):
        s = [random.choice(ds) for _ in ds]; c = sum(byd[x][1] for x in s); bs.append(sum(byd[x][0] for x in s) / c)
    top = sorted(ds, key=lambda x: -byd[x][0])[:2]; c2 = sum(byd[x][1] for x in ds if x not in top)
    P = sum(p for _, p, _ in rows); Cc = sum(c for _, _, c in rows)
    return f'n={len(rows)} dias={len(ds)} PnL={P:+.2f} coste={Cc:.2f} EVpond={P/Cc:+.3f} IC90d=({np.percentile(bs,5):+.2f},{np.percentile(bs,95):+.2f}) sin2={(sum(byd[x][0] for x in ds if x not in top)/c2) if c2 else float("nan"):+.3f}'
print('chequeo A (vigia vs extracto):', sum(1 for e in RES if e['cl'].startswith('A') and e['ask'] <= e['plim'] + 1e-9), '/', sum(1 for e in RES if e['cl'].startswith('A')))
for k in (0.0, 0.01, 0.02, 0.03):
    rows = []; nparc = 0; gan = 0
    for e in RES:
        lim = e['plim'] + k
        if math.isnan(e['ask']) or e['ask'] > lim + 1e-9: continue
        need = max(5.0, 2.0 / e['ask']); a = min(need, e['asz'])
        if a < 5.0 - 1e-9: nparc += 1
        if a <= 0: continue
        rows.append((e['dia'], a * e['g'] - a * e['ask'] - a * fee(e['ask']), a * e['ask'])); gan += e['g']
    print(f'k=+{k:.2f} (solo nivel 1 con su tamaño real) ganadoras={gan:.0f} parciales<5acc={nparc} | {st(rows)}')
