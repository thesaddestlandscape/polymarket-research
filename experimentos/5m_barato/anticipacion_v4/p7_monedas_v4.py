"""Eventos V4 del vigia (regla B1_5m, primer evento por cierre, m>=0,05) por MONEDA, con ejecucion L215 del propio vigia (clase A/D = ejecutable) y desenlace oficial.
Solo lectura de DL/vigia_5m_barato/eventos_D.csv. EV ponderado por EUR; IC90 por cierre. Descriptivo (multimoneda tal como se congelo v4)."""
import csv, glob, json, collections, numpy as np
DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
fee = lambda p: 0.07 * p * (1 - p)
R = collections.defaultdict(list); allc = collections.Counter(); sin = 0
for f in sorted(glob.glob('/root/polymarket-research-datalogs/vigia_5m_barato/eventos_*.csv')):
    dia = f[-14:-4]
    for r in csv.DictReader(open(f)):
        if r['regla'] != 'B1_5m' or r['es_primero'] != '1': continue
        allc[r['moneda']] += 1
        out = DES.get(r['market_compra'])
        if out is None: sin += 1; continue
        sl = 'YES' if r['lado'] == 'Up' else 'NO'
        cl = r['L215_clase']; p = r['L215_precio']; a = r['L215_acciones']
        if cl in ('A_sigue_barato', 'D_otro_nivel_barato') and p and a and float(a) > 0:
            p = float(p); a = float(a); R[r['moneda']].append((dia, r['cierre'], a * (p + fee(p)), a * ((out == sl) - p - fee(p)), float(r['ask_compra_t0'] or 0), float(r['margen_neto'] or 0)))
print('eventos primeros B1_5m por moneda', dict(allc), '| sin desenlace', sin)
rng = np.random.default_rng(1)
for m, v in sorted(R.items()):
    c = np.array([x[2] for x in v]); pn = np.array([x[3] for x in v]); cl = [x[1] for x in v]; dias = [x[0] for x in v]
    g = {}
    for k, a, b in zip(cl, c, pn): g.setdefault(k, [0, 0]); g[k][0] += b; g[k][1] += a
    G = np.array(list(g.values())); ix = rng.integers(0, len(G), (3000, len(G))); r = G[ix, 0].sum(1) / np.maximum(G[ix, 1].sum(1), 1e-9)
    byd = {}
    for d_, a, b in zip(dias, c, pn): byd.setdefault(d_, 0); byd[d_] += b
    print(f'{m:5s} ejecutables L215 n={len(v):3d} dias={len(set(dias)):2d} coste={c.sum():7.1f} PnL={pn.sum():+7.2f} EV={pn.sum()/c.sum():+.3f} IC90cierre=({np.percentile(r,5):+.2f},{np.percentile(r,95):+.2f}) dias+={sum(1 for x in byd.values() if x>0)}/{len(byd)}')
