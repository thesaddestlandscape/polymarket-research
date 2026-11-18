#!/usr/bin/env python3
"""v7_resumen.py -- metricas de las variantes DEM/COLA/C150 (out/V5_DEM_*.pkl) frente a la base v3d_BASE del MISMO fichero. Solo calculo. -> v7_resumen.json"""
import glob, json, os, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; FLOOR = 1e-3
R = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H + 'out/V5_DEM_*_2026-10-2?.pkl'))], ignore_index=True); assert R.dia.nunique() == 4
T = pd.read_pickle(H + 'tomador_202.pkl')[['oid', 'causa', 'estructura']]; R = R.merge(T, on='oid', how='left'); R['cl'] = R.causa.fillna('').str.split('(').str[0]
rf = R.real_fill.values == 1; g = R.gana.values.astype(float); L = R.L.values; qr = R.real_q.values
def ev(q, m): c = (q[m] * L[m]).sum(); return round(float((q[m] * (g[m] - L[m])).sum() / c), 4) if c > 0 else None
VARS = ['v3d_BASE', 'DEMr', 'DEMe', 'DEMall', 'DEMr_p30', 'DEMr_m30', 'C150', 'COLA', 'COLA_C150', 'DEMr_COLA_C150', 'DEMr_COLA', 'DEMr_COLA_p30', 'DEMr_COLA_m30']
b = R['v3d_BASE_f_q'].values >= FLOOR; out = {}
for v in VARS:
    q = R[f'{v}_f_q'].values; s = q >= FLOOR; tp = s & rf; fp = s & ~rf; fn = ~s & rf; tf = R[f'{v}_f_tf'].values
    near = tp & np.isfinite(R.real_tm3.values) & (np.abs(tf - R.real_tm3.values) <= 50)
    out[v] = dict(sim=int(s.sum()), TP=int(tp.sum()), FP=int(fp.sum()), FN=int(fn.sum()), prec=round(tp.sum() / max(s.sum(), 1), 3), rec=round(tp.sum() / rf.sum(), 3),
                  dTP=int(tp.sum() - (b & rf).sum()), dFP=int(fp.sum() - (b & ~rf).sum()), TP_50ms=int(near.sum()),
                  nuevos_TP_por_clase=pd.Series(R.cl.values[tp & ~b]).value_counts().to_dict(), TP_perdidos=int((b & rf & ~s).sum()),
                  TP_por_dia=pd.Series(R.dia.values[tp]).value_counts().sort_index().to_dict(),
                  EV_TP_motor=ev(q, tp), EV_TP_real=ev(qr, tp), EV_FP_motor=ev(q, fp), EV_FN_real=ev(qr, fn), pnl_FP=round(float((q[fp] * (g[fp] - L[fp])).sum()), 2),
                  EV_sim_total=ev(q, s), EV_real_total=ev(qr, rf))
json.dump(out, open(H + 'v7_resumen.json', 'w'), indent=1, default=str)
for v, o in out.items(): print(f"{v:16s} sim {o['sim']:3d} TP {o['TP']:3d} FP {o['FP']:3d} prec {o['prec']:.3f} rec {o['rec']:.3f} dTP {o['dTP']:+d} dFP {o['dFP']:+d} TP50 {o['TP_50ms']:3d} EVtp {o['EV_TP_real']} EVfp {o['EV_FP_motor']} EVfn {o['EV_FN_real']} EVsim {o['EV_sim_total']} nuevos {o['nuevos_TP_por_clase']}")
