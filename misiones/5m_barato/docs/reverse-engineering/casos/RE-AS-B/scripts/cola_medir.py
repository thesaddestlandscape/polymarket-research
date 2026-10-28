#!/usr/bin/env python3
"""cola_medir.py -- Tarea B (RE-AS-B): EV ponderado por euros por COLA al colocar, ledger H47-B real (fills.json + ledger) y vida_puja_virtual 24/25/26-Oct. DESCRIPTIVO; n<40 no decide. python3 -I."""
import sys, json, collections, numpy as np, pandas as pd
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__))); import cola_lib as C
rng = np.random.default_rng(C.SEED); HERE = __import__('os').path.dirname(__import__('os').path.abspath(__file__))
# ---- 1) LEDGER H47-B real
F = json.load(open(HERE + '/../e02real_fills.json')); cola = {}
for l in open('/root/polymarket-research-datalogs/experimento_h47_B_ledger.jsonl'):
    if '"post_ok"' in l:
        d = json.loads(l)
        if d.get('tipo') == 'post_ok': cola[d['oid']] = d.get('cola')
F = [f for f in F if f.get('ok') and f.get('gana') is not None]; F.sort(key=lambda f: (f['bloque'], f['logidx_fill'])); seen = set(); U = []
for f in F:
    k = (f['mercado'], f['outcome'])
    if k in seen: continue
    seen.add(k); U.append(f)
L = pd.DataFrame([dict(coin=f['mercado'].split('-')[0].upper(), b=f['precio'], cola=cola.get(f['oid']), pnl=f['size'] * (f['gana'] - f['precio']), cost=f['size'] * f['precio'],
                       cierre=int(f['mercado'].split('-')[-1]) + 300, dia=f['fecha'][:10]) for f in U])
print('== LEDGER H47-B real: unidades (mercado-lado, primer relleno) %d, con cola en ledger %d, Σpnl %+.2f' % (len(L), L.cola.notna().sum(), L.pnl.sum()))
L = L[L.cola.notna()].copy(); L['rej'] = pd.cut(L.cola, C.REJ_EDGES, labels=C.REJ_LAB); L['tri'] = pd.cut(L.cola, C.TRI_EDGES, labels=C.TRI_LAB); L['bk'] = pd.cut(L.b, C.BK_EDGES, labels=C.BK_LAB)
def informe(Q, tag):
    print('\n== %s' % tag); print(C.linea('TODOS', Q, rng))
    for c in ('tri', 'rej'):
        print(' -- por cola (%s)' % c)
        for k, h in Q.groupby(c, observed=True): print(C.linea('cola ' + str(k), h, rng))
    print(' -- por moneda x cola (tri)')
    for (m, k), h in Q.groupby(['coin', 'tri'], observed=True): print(C.linea('%s cola %s' % (m, k), h, rng))
    print(' -- por bucket de precio x cola (tri)')
    for (m, k), h in Q.groupby(['bk', 'tri'], observed=True): print(C.linea('%s cola %s' % (m, k), h, rng))
    cel = [(k, h) for k, h in Q.groupby(['coin', 'bk', 'tri'], observed=True)]
    print(' -- moneda x bucket x cola(tri): %d celdas con datos, %d con n>=40' % (len(cel), sum(len(h) >= 40 for _, h in cel)))
    for k, h in sorted(cel, key=lambda z: -len(z[1]))[:8]: print(C.linea('%s|%s|%s' % k, h, rng))
informe(L, 'LEDGER H47-B real, 20-23 Oct (post_ok.cola al colocar)')
# ---- 2) VIRTUAL
X = C.cargar_vpv(['2026-10-24', '2026-10-25', '2026-10-26']); print('\n[vpv] vidas %d; cobertura gana (re-unida con cache actual) por dia: %s' % (len(X), X.groupby('dia').gana.apply(lambda s: round(s.notna().mean(), 4)).to_dict()))
for col, tcol, nm in (('relleno_pes', 't_relleno_pes_ms', 'pes'), ('relleno_opt', 't_relleno_opt_ms', 'opt')):
    for modo in ('primer_relleno', 'primera_colocada'):
        Q = C.unidades(X, modo, col, tcol).copy(); Q['coin'] = Q.coin
        informe(Q, 'VIRTUAL relleno %s, unidad %s (Q0 = cola al colocar) 24-26 Oct' % (nm, modo))
        if nm == 'pes' and modo == 'primer_relleno':
            for d, h in Q.groupby('dia'): print(C.linea('[por dia] ' + d, h, rng))
            print(' -- dias x cola(tri)')
            for (d, k), h in Q.groupby(['dia', 'tri'], observed=True): print(C.linea('%s cola %s' % (d, k), h, rng))
