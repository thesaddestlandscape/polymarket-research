#!/usr/bin/env python3
"""t5_ident.py D : PUERTA I2 del PREREG_TRANSFERENCIA (E-RE-CB-03). Inferencia de ordenes ajenas desde el L2 agregado (libro5_ms,
lado bid, episodios de nivel 0->s en un solo evento y solo decrementos hasta 0). (a) recuperacion del alta/fin de las ordenes REALES
de B; (b) no degeneracion del subconjunto identificable de OTROS makers (>=2 order_hash rellenados a p en el episodio). Solo lectura."""
import sys, gzip, json, collections, numpy as np, pandas as pd
D = sys.argv[1]; DL = '/root/polymarket-research-datalogs/calibracion_etiqueta/'; V = DL + 'v3_l2/'
BW = '0x659a40ff9920febc5a66836213040924343d297f'
ser = collections.defaultdict(list)   # (tok, p_milesimas) -> [(recep_ms, size)]
gaps = collections.defaultdict(list)  # tok -> [recep_ms] (baja/pausa/arranque: estado desconocido)
last = {}                             # (tok,p) -> size actual (para snapshots)
rows = []
for line in gzip.open(V + 'l2_%s.csv.gz' % D, 'rt', errors='replace'):
    c = line.rstrip('\n').split(',')
    if len(c) < 8: continue
    try: rows.append((int(c[7]), c))
    except ValueError: continue
rows.sort(key=lambda x: x[0])
for _, c in rows:
    ty = c[0]
    if ty == 'G':
        tks = [k for k in {k[0] for k in last}] if c[2] == '*' else [c[2]]
        for tk in tks:
            gaps[tk].append(int(c[6]))
            for k in [k for k in last if k[0] == tk]: ser[k].append((int(c[6]), np.nan)); del last[k]
    elif ty == 'B':
        tk = c[2]; t = int(c[6]); lv = {}
        for it in c[3].split(';'):
            if ':' in it: p, s = it.split(':'); lv[int(round(float(p) * 1000))] = float(s)
        for k in [k for k in last if k[0] == tk and k[1] not in lv]: ser[k].append((t, 0.0)); last[k] = 0.0
        for p, s in lv.items():
            if last.get((tk, p)) != s: ser[(tk, p)].append((t, s)); last[(tk, p)] = s
    elif ty == 'd' and c[3] == 'B':
        tk = c[2]; p = int(round(float(c[4]) * 1000)); s = float(c[5]); t = int(c[6])
        if last.get((tk, p)) != s: ser[(tk, p)].append((t, s)); last[(tk, p)] = s

def episodios(L):
    """-> lista (t_ini, t_fin, s0, unico): nivel 0->s0; unico = sin incrementos hasta volver a 0; NaN (hueco) invalida."""
    out = []; ini = None; prev = 0.0; uni = True; s0 = 0
    for t, s in L:
        if s != s:  # hueco
            ini = None; prev = np.nan; continue
        if ini is None:
            if (prev == 0.0) and s > 0: ini = t; s0 = s; uni = True
            prev = s; continue
        if s > prev + 1e-9: uni = False
        if s <= 1e-9: out.append((ini, t, s0, uni)); ini = None
        prev = s
    return out
EP = {k: episodios(v) for k, v in ser.items()}
res = {'dia': D, 'niveles_bid': len(ser)}
# (a) ordenes reales de B
B = pd.read_parquet(DL + 'ordenes_b.parquet'); b = B[B.dia == D].copy()
a_rec = 0; a_alta = 0; a_solo = 0; dts = []
for r in b.itertuples():
    k = (r.tok, int(round(r.precio * 1000))); ti = r.t_ini * 1000; tf = r.t_fin * 1000; L = ser.get(k, [])
    # alta visible: incremento ~size en +-250 ms
    best = None; prev = 0.0
    for t, s in L:
        if s == s and prev == prev and abs((s - prev) - r.size) < 0.02 and (best is None or abs(t - ti) < abs(best - ti)): best = t
        prev = s if s == s else np.nan
    if best is not None: dts.append(best - ti)
    if best is not None and abs(best - ti) <= 250: a_alta += 1
    ok = [e for e in EP.get(k, []) if e[3] and abs(e[0] - ti) <= 250 and abs(e[1] - tf) <= 500]
    if ok: a_rec += 1
    if [e for e in EP.get(k, []) if abs(e[0] - ti) <= 250]: a_solo += 1
res['a'] = dict(n_ordenes_B=len(b), recuperadas_episodio=a_rec, frac=a_rec / max(len(b), 1), alta_visible_250ms=a_alta,
                nivel_vacio_al_alta=a_solo, dt_alta_ms_p10_50_90=[float(x) for x in np.percentile(dts, [10, 50, 90])] if dts else None, n_dt=len(dts))
# (b) otros makers
OC = pd.read_csv(V + 'oc_%s.csv.gz' % D, header=None, names='tipo,bloque,ts_est,tx,log_index,order_hash,maker,taker,side,token_id,maker_amt,taker_amt,fee'.split(','), dtype={'token_id': str})
OC = OC[(OC.side == 0) & (OC.maker.str.lower() != BW)].copy(); OC['p'] = (OC.maker_amt / OC.taker_amt * 1000).round().astype(int)
OC = OC[(OC.p > 110) & (OC.p <= 300)]
res['cota_positivos'] = dict(order_hash_ajenos_rellenados_bid_banda=int(OC.order_hash.nunique()), fills=len(OC), tokens=int(OC.token_id.nunique()))
g = {k: v for k, v in OC.groupby(['token_id', 'p'])}
Bown = collections.defaultdict(list)
for r in b.itertuples(): Bown[(r.tok, int(round(r.precio * 1000)))].append((r.t_ini * 1000 - 2000, r.t_fin * 1000 + 2000))
ne = 0; npos = 0; nneg = 0; nondeg = 0; tamano_ok = 0; nb = 0
for k, eps in EP.items():
    if not (110 < k[1] <= 300): continue
    f = g.get(k)
    for (t0, t1, s0, uni) in eps:
        if not uni: continue
        if any(not (t1 < a or t0 > z) for a, z in Bown.get(k, [])): nb += 1; continue
        ne += 1
        if f is None: nneg += 1; continue
        w = f[(f.ts_est * 1000 >= t0 - 1000) & (f.ts_est * 1000 <= t1 + 8000)]
        if len(w) == 0: nneg += 1; continue
        npos += 1; nh = w.order_hash.nunique()
        if nh >= 2: nondeg += 1
        if nh == 1 and abs(w.taker_amt.sum() - s0) < 0.05: tamano_ok += 1
res['b'] = dict(episodios_unicos_banda_sin_B=ne, solapados_con_B=nb, positivos=npos, negativos_cancelados=nneg,
                positivos_con_2_o_mas_order_hash=nondeg, frac_no_degenerado=nondeg / max(npos, 1), positivos_1hash_tamano_cuadra=tamano_ok)
json.dump(res, open('t5_ident_%s.json' % D, 'w'), indent=1); print(json.dumps(res, indent=1))
