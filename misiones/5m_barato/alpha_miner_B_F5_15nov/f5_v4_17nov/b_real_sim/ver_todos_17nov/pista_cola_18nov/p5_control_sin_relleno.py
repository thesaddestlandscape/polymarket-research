#!/usr/bin/env python3
"""p5_control_sin_relleno.py v2 (ADENDA_02 punto 3; RE-B-COLA-CANCELA, MECANISMO, NO EV). CONTROL COMPARABLE de M3/p4: rellenos vs NO rellenos con la MISMA metrica y ventanas identicas.
Para cada puja de B 20-23 Oct con L2 del nivel (cola_vs_cruce/mk, ETH/SOL/XRP hasta 22-Oct ~16:15Z; BTC: B no opero BTC y no existe L2 5m posterior, ver ADENDA_02):
  ancla tc = t_ini + dt. RELLENO: dt = real_tm3 - t_ini (casado observado; tomador_202.pkl). NO RELLENO: dt muestreado (K por puja) de la distribucion EMPIRICA de dt de los rellenos
  con dt <= vida de la puja (vida = min(t_cancel_int,t_fuera)-t_ini): misma duracion de vida y mismo anclaje relativo a la colocacion.
Metrica identica a p4: F50 = R1 (V1: tau=300 ms, theta=50 %, masa cancelada sin imprimir) dispara con te en [tc-1000, tc-20-53]; F90 con L=60+147 (cota prereg).
Comparacion por estratos (coin x cola>0) y LR = F(rellenos)/F(no rellenos) con IC90 bootstrap por dia. Uso: p5_control_sin_relleno.py [max_ficheros] [K]"""
import json, gzip, bisect, os, sys, random, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)); MK = '/root/polymarket-research-datalogs/cola_vs_cruce/mk/'
TOKM = json.load(open('/root/polymarket-research-datalogs/cola_vs_cruce/tokens.json'))
OB = pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str})
TF = pd.read_pickle(H + '/../tomador_202.pkl')[['oid', 'real_tm3']]
MAXF = int(sys.argv[1]) if len(sys.argv) > 1 else 10**9; K = int(sys.argv[2]) if len(sys.argv) > 2 else 5
random.seed(18112026)
def parse(fn):
    lv = {'Y': {}, 'N': {}}; bk = {'Y': {}, 'N': {}}; TR = {'Y': [], 'N': []}
    def rec(s_, p, t, z):
        e = lv[s_].setdefault(p, ([], [])); e[0].append(t); e[1].append(z)
    try:
        with gzip.open(fn, 'rt', errors='replace') as f:
            for ln in f:
                c = ln.rstrip('\n').split(',')
                if len(c) < 4 or c[0] not in lv: continue
                s_, ty = c[0], c[1]
                try:
                    if ty == 'B':
                        t = int(c[2]); new = {}
                        for it in c[3].split(';'):
                            if ':' in it: p, z = it.split(':'); new[round(float(p), 2)] = float(z)
                        for p in set(bk[s_]) | set(new):
                            if abs(bk[s_].get(p, 0) - new.get(p, 0)) > 1e-9: rec(s_, p, t, new.get(p, 0.0))
                        bk[s_] = new
                    elif ty == 'd':
                        t = int(c[2]); p = round(float(c[3]), 2); z = float(c[4]); o = bk[s_].get(p, 0.0)
                        if z > 0: bk[s_][p] = z
                        else: bk[s_].pop(p, None)
                        if abs(z - o) > 1e-9: rec(s_, p, t, z)
                    elif ty == 'T': TR[s_].append((int(c[2]), c[3], round(float(c[4]), 2), float(c[5])))
                except (ValueError, IndexError): continue
    except (EOFError, OSError): pass
    return lv, TR
OB = OB.merge(TF, on='oid', how='left'); OB['k'] = OB.tok.map(lambda t: tuple(TOKM[t][:3]) if t in TOKM else None)
OB['fillb'] = OB.fill > 0
DTF = sorted((OB[OB.fillb & OB.real_tm3.notna()].real_tm3 - OB[OB.fillb & OB.real_tm3.notna()].t_ini * 1000).clip(lower=0))   # ms
cov = {'pujas': int(len(OB)), 'rellenos': int(OB.fillb.sum()), 'rellenos_con_tm3': int(OB.fillb.sum() - OB[OB.fillb].real_tm3.isna().sum()), 'sin_L2_token': int(OB.k.isna().sum())}
rows = []; nf = 0
for k, g in OB[OB.k.notna()].groupby('k'):
    if nf >= MAXF: break
    act, mid, lado = k; fn = f'{MK}{act}_{mid}.gz'
    if not os.path.exists(fn): cov['sin_fichero'] = cov.get('sin_fichero', 0) + len(g); continue
    nf += 1; lv, TR = parse(fn); me = 'Y' if lado == 'YES' else 'N'; ot = 'N' if me == 'Y' else 'Y'
    for r in g.itertuples():
        L = round(r.precio, 2); ser = lv[me].get(L)
        if ser is None: cov['sin_nivel_en_L2'] = cov.get('sin_nivel_en_L2', 0) + 1; continue
        hr, hs = ser; t0 = int(r.t_ini * 1000); life = int(np.nanmin([r.t_cancel_int, r.t_fuera]) * 1000) - t0     # v2.1: 58 rellenos sin t_cancel_int (NaN) -> vida = t_fuera
        pr = sorted([(t, z) for (t, sd, p, z) in TR[me] if sd == 'SELL' and p == L] + [(t, z) for (t, sd, p, z) in TR[ot] if sd == 'BUY' and abs(p - (1 - L)) < 1e-6])
        prt = [t for t, z in pr]; pcs = np.concatenate([[0], np.cumsum([z for t, z in pr])])
        def q(t):
            i = bisect.bisect_right(hr, t) - 1; return hs[i] if i >= 0 else None
        def printed(a, b): return pcs[bisect.bisect_right(prt, b)] - pcs[bisect.bisect_right(prt, a)]
        def fire(tc, dl, tau=300, th=.5):
            cs = {tc - 1000, dl} | {t for t in hr if tc - 1000 - tau <= t <= dl} | {t + tau for t in hr if tc - 1000 - tau <= t <= dl}
            for te in sorted(x for x in cs if tc - 1000 <= x <= dl):
                qa, qb = q(te - tau), q(te)
                if qa and qb is not None and qa > 0 and max(0.0, qa - qb - printed(te - tau, te)) >= th * qa - 1e-9: return te
            return None
        if r.fillb:
            if not (r.real_tm3 == r.real_tm3): continue
            anchors = [int(r.real_tm3)]
        else:
            ok = [d for d in DTF if d <= life]
            if not ok: cov['vida_menor_que_todo_dt'] = cov.get('vida_menor_que_todo_dt', 0) + 1; continue
            anchors = [t0 + random.choice(ok) for _ in range(K)]
        for tc in anchors:
            rows.append(dict(oid=r.oid, coin=r.coin, dia=r.dia, fillb=bool(r.fillb), cola_pos=bool(r.cola > 0), dt=tc - t0, vida=life,
                             F50=fire(tc, tc - 20 - 53) is not None, F90=fire(tc, tc - 20 - 207) is not None, q150=q(tc - 150), w=1.0 / len(anchors)))
O = pd.DataFrame(rows); cov['ficheros_leidos'] = nf; cov['filas_ancla'] = int(len(O)); res = {'cobertura': cov}
def tab(x):
    a, b = x[x.fillb], x[~x.fillb]
    if len(a) < 5 or len(b) < 5: return {'n_fill': int(len(a)), 'n_nofill_pujas': int(b.oid.nunique()), 'nota': 'INSUFFICIENT'}
    o = {'n_fill': int(len(a)), 'n_nofill_pujas': int(b.oid.nunique()), 'n_nofill_anclas': int(len(b))}
    for m in ('F50', 'F90'):
        fa, fb = float(a[m].mean()), float(np.average(b[m], weights=b.w)); o[m] = dict(fill=round(fa, 4), nofill=round(fb, 4), LR=round(fa / fb, 2) if fb > 0 else None)
    # IC90 por dia (bootstrap de dias) del LR F50
    ds = sorted(x.dia.unique()); lr = []
    rg = np.random.default_rng(3)
    for _ in range(1000):
        dd = rg.choice(ds, len(ds)); A = pd.concat([a[a.dia == d] for d in dd]); B = pd.concat([b[b.dia == d] for d in dd])
        if len(A) and len(B) and np.average(B.F50, weights=B.w) > 0: lr.append(A.F50.mean() / np.average(B.F50, weights=B.w))
    o['LR_F50_ic90_dias'] = [round(float(v), 2) for v in np.percentile(lr, [5, 95])] if len(lr) > 50 else None
    return o
if len(O):
    res['global'] = tab(O); res['por_coin'] = {c: tab(g) for c, g in O.groupby('coin')}; res['por_cola'] = {str(c): tab(g) for c, g in O.groupby('cola_pos')}
    res['balance_dt_ms_mediana'] = dict(fill=float(O[O.fillb].dt.median()), nofill=float(O[~O.fillb].dt.median()))
res['nota'] = 'Ventanas identicas, ancla relativa a la colocacion y vida condicionada. LR~F(fill)/F(nofill): si ~1 la regla R1 no discrimina rellenos de no rellenos. MECANISMO, no EV. tc de relleno = real_tm3 (casado observado).'
O.to_pickle(H + '/out/p5_control_sin_relleno.pkl'); json.dump(res, open(H + '/out/p5_control_sin_relleno.json', 'w'), indent=1, default=str); print(json.dumps(res, indent=1, default=str))
