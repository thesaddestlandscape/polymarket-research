#!/usr/bin/env python3
"""a1_cal.py OFF : re-medido de A1/F5 (tamano del ask propio 100 ms antes del relleno) sobre los rellenos VIRTUALES calibrados (tabla_cal_offN). Regla y gate congelados de mitigar_as_25oct/PREREG_A1.md con K=1."""
import sys, json
import numpy as np, pandas as pd
from scipy import stats
OFF = int(sys.argv[1]); LAGCOL = sys.argv[2] if len(sys.argv) > 2 else 'f5'
import os
CD = os.environ.get('CALIB_DL', '/root/polymarket-research-datalogs/calibracion_etiqueta/'); D = os.environ.get('CALIB_OUT') or __file__.rsplit('/', 2)[0] + '/datos/'
rng = np.random.default_rng(20261026)
T = pd.read_parquet(CD + 'tabla_cal_off%d.parquet' % OFF)
T = T[(T.censurada == 0) & T.coin.isin(['ETH', 'SOL', 'XRP'])]
cov = {'vidas': int(len(T)), 'rellenas': int(T.relleno_pes.sum()), 'rellenas_sin_desenlace': int(((T.relleno_pes == 1) & T.gana.isna()).sum()), 'rellenas_sin_F5': int(((T.relleno_pes == 1) & T[LAGCOL].isna()).sum())}
F = T[(T.relleno_pes == 1) & T.gana.notna()].copy(); F['c'] = 5.0 * F.bl; F['pnl'] = F.pnl_5acc_si_relleno.astype(float)
F['dia'] = pd.to_datetime(F.t0_recv_ms, unit='ms', utc=True).dt.strftime('%Y-%m-%d')
F = F[F[LAGCOL].notna()]
dias = sorted(F.dia.unique()); TEST = [d for d in dias if d >= '2026-10-09']
def ev(x): return float(x.pnl.sum() / x.c.sum()) if len(x) and x.c.sum() > 0 else np.nan
def run(inv=False):
    out = []; rows = []
    for d in TEST:
        tr = F[(F.dia < d) & (F.dia >= '2026-10-06')]; te = F[F.dia == d]
        if tr.dia.nunique() < 3 or len(te) == 0: continue
        q = np.quantile(tr[LAGCOL], [1 / 3, 2 / 3]); bins = np.digitize(tr[LAGCOL], q)
        evs = [ev(tr[bins == k]) for k in range(3)]; k = int(np.nanargmax(evs) if inv else np.nanargmin(evs))
        flag = np.digitize(te[LAGCOL], q) == k; f = te.c[flag].sum() / te.c.sum()
        ex = f * te.pnl.sum() - te.pnl[flag].sum()
        out.append((d, ex, f, k)); rows.append(te.assign(flag=flag, f_d=f))
    return out, pd.concat(rows)
res, R = run(); ex = np.array([e for _, e, _, _ in res])
inv, _ = run(True); exi = np.array([e for _, e, _, _ in inv])
n = len(ex); tot = ex.sum(); se = ex.std(ddof=1) / np.sqrt(n); tq = stats.t.ppf(0.95, n - 1)
ic = (ex.mean() - tq * se, ex.mean() + tq * se); p = float(stats.t.sf(ex.mean() / se, n - 1))
cl = (R.pnl * (R.flag.astype(float) * -1 + R.f_d)).groupby(R.cierre).sum().values   # exceso = f*pnl - pnl_marcados
bs = np.array([cl[rng.integers(0, len(cl), len(cl))].sum() for _ in range(2000)]); icc = (float(np.percentile(bs, 5)), float(np.percentile(bs, 95)))
# EV retenido vs total por dias
dd = []
for d, g in R.groupby('dia'): dd.append(ev(g[~g.flag]) - ev(g))
dd = np.array(dd); ret_ic = (dd.mean() - tq * dd.std(ddof=1) / np.sqrt(len(dd)), dd.mean() + tq * dd.std(ddof=1) / np.sqrt(len(dd)))
gate = {'exceso>0': tot > 0, 'IC90_dias_inf>0': ic[0] > 0, 'p<0.05': p < 0.05, 'sin_2mejores>0': tot - np.sort(ex)[-2:].sum() > 0, 'inversion<0': exi.sum() < 0, 'dias+>=10': int((ex > 0).sum()) >= 10,
        'IC90_cierre_inf>0': icc[0] > 0, 'EVret>EVtot_IC>0': ret_ic[0] > 0}
sol = {'OFF': OFF, 'lag': LAGCOL, 'cobertura': cov, 'n_rellenas_evaluadas': int(len(R)), 'dias_test': n, 'exceso_total': float(tot), 'exceso_por_dia': {d: float(e) for d, e, _, _ in res}, 'f_eur_media': float(np.mean([f for _, _, f, _ in res])),
       'IC90_dias': [float(ic[0]), float(ic[1])], 'p_unilateral_dias': p, 'sin_mejor': float(tot - ex.max()), 'sin_2mejores': float(tot - np.sort(ex)[-2:].sum()), 'dias_pos': int((ex > 0).sum()), 'IC90_cierre': icc,
       'inversion_exceso': float(exi.sum()), 'EV_total': ev(R), 'EV_retenido': ev(R[~R.flag]), 'EV_marcado': ev(R[R.flag]), 'dif_EVret_menos_tot_IC90_dias': [float(ret_ic[0]), float(ret_ic[1])], 'gate': {k: bool(v) for k, v in gate.items()}, 'PASA': bool(all(gate.values())),
       'por_moneda': {c: {'n': int(len(g)), 'exceso': float(sum((g[g.dia == d].c[g[g.dia == d].flag].sum() / g[g.dia == d].c.sum()) * g[g.dia == d].pnl.sum() - g[g.dia == d].pnl[g[g.dia == d].flag].sum() for d in g.dia.unique()))} for c, g in R.groupby('coin')}}
json.dump(sol, open(D + 'a1cal_off%d_%s.json' % (OFF, LAGCOL), 'w'), indent=1, default=float); print(json.dumps(sol, indent=1, default=float))
