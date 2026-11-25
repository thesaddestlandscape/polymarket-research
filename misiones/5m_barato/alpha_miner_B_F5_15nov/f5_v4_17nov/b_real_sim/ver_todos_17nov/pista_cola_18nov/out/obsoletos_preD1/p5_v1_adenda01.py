#!/usr/bin/env python3
"""p5_control_sin_relleno.py (ADENDA_01 fix 7; RE-B-COLA-CANCELA, MECANISMO, NO EV). CONTROL de M3: tasa de disparo de R1 (V1: masa cancelada sin imprimir
en (te-300,te] >= 50 % de Q(te-300) en NUESTRO nivel) durante la vida de las pujas de B 20-23 Oct que NO se rellenaron (ordenes_b.csv, fill==0),
con L2 por nivel de cola_vs_cruce/mk (ETH/SOL/XRP hasta 22-Oct 16:15Z; BTC sin L2). Mismo reloj/L2/parser que p4_m3_b.py (copiado, p4 no se toca).
Ventana de evaluacion = [t_ini, t_cancel_int] (el nivel cae por NUESTRA cancelacion despues de t_cancel_int; el sube por nuestra colocacion no es caida).
Comparable a p4 (rellenos): P(R1 dispara en el ultimo ~0,93 s antes del casado). Aqui se da por puja y por segmento de 1 s. Uso: p5_control_sin_relleno.py [max_pujas]"""
import json, gzip, bisect, os, sys, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)); MK = '/root/polymarket-research-datalogs/cola_vs_cruce/mk/'
TOKM = json.load(open('/root/polymarket-research-datalogs/cola_vs_cruce/tokens.json'))
OB = pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str})
MAXN = int(sys.argv[1]) if len(sys.argv) > 1 else 10**9
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
NF = OB[OB.fill == 0].copy(); NF['k'] = NF.tok.map(lambda t: tuple(TOKM[t][:3]) if t in TOKM else None)
cov = {'pujas_no_rellenadas': int(len(NF)), 'sin_L2_token': int(NF.k.isna().sum())}
cache = {}; rows = []; n = 0
for k, g in NF[NF.k.notna()].groupby('k'):
    act, mid, lado = k; fn = f'{MK}{act}_{mid}.gz'
    if not os.path.exists(fn): cov['sin_fichero'] = cov.get('sin_fichero', 0) + len(g); continue
    lv, TR = parse(fn); me = 'Y' if lado == 'YES' else 'N'; ot = 'N' if me == 'Y' else 'Y'
    for r in g.itertuples():
        if n >= MAXN: break
        n += 1; L = round(r.precio, 2); ser = lv[me].get(L)
        if ser is None: cov['sin_nivel_en_L2'] = cov.get('sin_nivel_en_L2', 0) + 1; continue
        hr, hs = ser
        pr = sorted([(t, z) for (t, sd, p, z) in TR[me] if sd == 'SELL' and p == L] + [(t, z) for (t, sd, p, z) in TR[ot] if sd == 'BUY' and abs(p - (1 - L)) < 1e-6])
        prt = [t for t, z in pr]; pcs = np.concatenate([[0], np.cumsum([z for t, z in pr])])
        def q(t):
            i = bisect.bisect_right(hr, t) - 1; return hs[i] if i >= 0 else None
        def printed(a, b): return pcs[bisect.bisect_right(prt, b)] - pcs[bisect.bisect_right(prt, a)]
        t0 = int(r.t_ini * 1000); t1 = int(min(r.t_cancel_int, r.t_fuera) * 1000)
        if t1 - t0 < 1000: cov['vida_lt_1s'] = cov.get('vida_lt_1s', 0) + 1; continue
        tau, th = 300, .5
        cs = sorted({x for x in [t0, t1] + [t_ for t_ in hr if t0 - tau <= t_ <= t1] + [t_ + tau for t_ in hr if t0 - tau <= t_ <= t1] if t0 <= x <= t1})
        fired = []
        for te in cs:
            qa, qb = q(te - tau), q(te)
            if qa and qb is not None and qa > 0 and max(0.0, qa - qb - printed(te - tau, te)) >= th * qa - 1e-9: fired.append(te)
        nb = int((t1 - t0) // 1000); bins = {(te - t0) // 1000 for te in fired if (te - t0) // 1000 < nb}
        rows.append(dict(oid=r.oid, coin=r.coin, dia=r.dia, L=L, cola=r.cola, vida_s=(t1 - t0) / 1000, disp=bool(fired), nbins=nb, bins_disp=len(bins)))
O = pd.DataFrame(rows); cov['evaluadas'] = int(len(O)); res = {'cobertura': cov}
if len(O):
    res['global'] = dict(n=int(len(O)), frac_pujas_con_disparo=round(float(O.disp.mean()), 4), frac_segmentos_1s_con_disparo=round(float(O.bins_disp.sum() / O.nbins.sum()), 4),
                         vida_s_mediana=round(float(O.vida_s.median()), 2), dias=O.dia.value_counts().to_dict())
    res['por_coin'] = {k: dict(n=int(len(g)), frac_pujas=round(float(g.disp.mean()), 4), frac_seg_1s=round(float(g.bins_disp.sum() / g.nbins.sum()), 4)) for k, g in O.groupby('coin')}
    res['por_dia'] = {k: dict(n=int(len(g)), frac_pujas=round(float(g.disp.mean()), 4), frac_seg_1s=round(float(g.bins_disp.sum() / g.nbins.sum()), 4)) for k, g in O.groupby('dia')}
    res['con_cola_gt0'] = dict(n=int((O.cola > 0).sum()), frac_seg_1s=round(float(O[O.cola > 0].bins_disp.sum() / O[O.cola > 0].nbins.sum()), 4))
res['nota'] = ('Comparar con p4_m3_b.json (rellenos): F50 = fraccion de casados con R1 disparado en [tc-1000, tc-73]. Aqui frac_segmentos_1s = P(R1 dispara en un segmento de 1 s '
               'de la vida de una puja NO rellenada). LR ~ F50 / frac_seg_1s. MECANISMO, no EV; ETH/SOL/XRP hasta 22-Oct 16:15Z (sin BTC).')
O.to_pickle(H + '/out/p5_control_sin_relleno.pkl'); json.dump(res, open(H + '/out/p5_control_sin_relleno.json', 'w'), indent=1, default=str); print(json.dumps(res, indent=1, default=str))
