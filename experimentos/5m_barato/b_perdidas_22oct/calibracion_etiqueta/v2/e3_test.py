#!/usr/bin/env python3
"""e3_test.py: evaluacion en TEST (22-23 Oct) con parametros/plantillas FIJADOS en TUNE (datos_tune_sel.json). Capa 1 + Capa G + placebos + K1..K6 (PREREG_V2)."""
import sys, json, numpy as np, pandas as pd
sys.path.insert(0, '.'); from v2lib import *
S = json.load(open('datos_tune_sel.json')); sel = S['sel']; E_, F_, G_ = int(sel['e']), sel['f'], sel['g']; RHO = {int(k): v for k, v in S['rho'].items()}; TPL = S['plantillas']
B = pd.read_parquet(DL + 'ordenes_b.parquet'); B = B[B.dia.isin(['2026-10-22', '2026-10-23'])].copy().reset_index(drop=True)
B['ti'] = B.t_ini * 1000; B['tf'] = B.t_fin * 1000; B['Qv'] = B.cola.fillna(0.0)
rng_rows = []; L1 = []; PJ = []; cobertura = dict(plantillas=len(TPL), ord_virtuales=0, ord_sin_libro=0, ord_fuera_cierre=0)
SHIFTS = {'G': 0, 'PL+90': 90_000, 'PL-90': -90_000}
for dia in ('2026-10-22', '2026-10-23'):
    D = Dia(dia); g = B[B.dia == dia]
    for r in g.itertuples():   # Capa 1
        c = D.consumos(r.tok, r.precio, r.ti, r.tf + E_); fl = lleno(c, r.ti, r.tf, E_, F_, G_, r.size, r.Qv) is not None
        L1.append(dict(oid=r.oid, puja=r.puja, dia=dia, fill=r.fill, v=int(fl), score=sum(x[1] for x in c if r.ti <= x[0] <= r.tf + E_) / r.size, coste=r.coste, pnl=r.pnl, slug=r.slug))
    for puja, gp in g.groupby('puja'):
        r0 = gp.sort_values('ti').iloc[0]; t0 = r0.ti; tk = r0.tok; cie = r0.cie * 1000
        out = {'puja': puja, 'dia': dia, 'slug': r0.slug, 'real': int(gp.fill_puja.max()), 'gana': float(r0.gana_lado) if r0.gana_lado == r0.gana_lado else np.nan}
        for nm, sh in SHIFTS.items():
            nf = 0; n_o = 0; n_ofill = 0; cost = 0.0; pnl = 0.0
            for tpl in TPL:
                anyf = False
                for off_ms, vida, off_c in tpl:
                    ti = t0 + off_ms
                    if ti > cie - 2000: 
                        if nm == 'G': cobertura['ord_fuera_cierre'] += 1
                        continue
                    tf = min(ti + vida, cie - 2000); bq = bid_at(D, tk, ti - 100)
                    if bq is None:
                        if nm == 'G': cobertura['ord_sin_libro'] += 1
                        continue
                    p = round(bq[0] - off_c / 100.0, 2)
                    if p <= 0: continue
                    if nm == 'G': cobertura['ord_virtuales'] += 1
                    c = [(t - sh, sz, sw) for (t, sz, sw) in D.consumos(tk, p, ti + sh, tf + E_ + sh)]
                    n_o += 1
                    if lleno(c, ti, tf, E_, F_, G_, 5.0, (RHO.get(off_c) or 1.0) * bq[1]) is not None:
                        n_ofill += 1; anyf = True
                        if out['gana'] == out['gana']: cost += 5 * p; pnl += 5 * (out['gana'] - p)
                nf += anyf
            out['P_' + nm] = nf / len(TPL); out['Po_' + nm] = n_ofill / max(n_o, 1); out['n_o_' + nm] = n_o
            out['cost_' + nm] = cost / len(TPL); out['pnl_' + nm] = pnl / len(TPL)
        PJ.append(out)
    print(dia, 'listo', flush=True)
L1 = pd.DataFrame(L1); PJ = pd.DataFrame(PJ); L1.to_csv(DL + 'v2/test_capa1.csv', index=False); PJ.to_csv(DL + 'v2/test_capaG.csv', index=False)
json.dump(dict(cobertura=cobertura), open('datos_test_cob.json', 'w'))
print(json.dumps(cobertura)); print(PJ.groupby('dia')[['real', 'P_G', 'P_PL+90', 'P_PL-90', 'Po_G']].mean().round(3))
