#!/usr/bin/env python3
"""Paso 4 (descriptivo, P_INS 09-23 Oct sin el TRAIN 06-08): curva EV por tercil de F5 segun el rezago (100..5000 ms) en la poblacion (r_D + l_D), todo vs tipo B (q<=bid100-0,01). Solo lectura."""
import os, sys, json, numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from lib_ev import *
AQ = os.path.dirname(os.path.abspath(__file__)); DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/'
LAGS = (100, 150, 200, 250, 400, 700, 1000, 2000, 5000); out = []
for d in pd.date_range('2026-10-09', '2026-10-23').strftime('%F'):
    r = pd.read_pickle(DL + f'r_{d}.pkl'); l = pd.read_pickle(DL + f'l_{d}.pkl')
    assert len(r) == len(l) and (r.index == l.index).all(); assert np.nanmax(np.abs(r.F5.values - l.F5_100.values)) < 1e-4
    r = r[r.coin.isin(('ETH', 'SOL', 'XRP'))]; l = l.loc[r.index]
    X = pd.DataFrame({'dia': d, 'coin': r.coin.values, 'cl': r.fin.values, 'pnl': r.pnl.values, 'coste': r.coste.values, 'tipoB': ((r.bid.values - r.q.values) >= 0.0099) & np.isfinite(r.bid.values)})
    for L in LAGS: X[f'F{L}'] = l[f'F5_{L}'].values
    out.append(X)
X = pd.concat(out, ignore_index=True); txt = [f'# Curva de rezago, poblacion ETH/SOL/XRP 09-23 Oct (filas {len(X)}, dias {X.dia.nunique()}); tipo B = q<=bid(r-100ms)-0,01 (fracc {X.tipoB.mean():.2f})']
res = {}
for nm, S in (('todas', X), ('tipoB', X[X.tipoB])):
    txt.append(f'## {nm} (filas {len(S)})'); txt.append('lag | EV bajo / medio / alto (pooled) | frac coste b/m/a | bajo-alto por dia (IC90 inf; dias+) | G1 EV (DeltaEV) | G2 EV | % filas con F5 valido')
    for L in LAGS:
        t = ter(S[f'F{L}'].values); G = pd.DataFrame({'dia': S.dia.values, 'cl': S.cl.values, 'pnl': S.pnl.values, 'coste': S.coste.values, 'ter': t})
        e = {r: ev(G.pnl[G.ter.isin(RET[r])], G.coste[G.ter.isin(RET[r])]) for r in ('todo', 'bajo', 'medio', 'alto', 'G1', 'G2')}
        fr = {r: G.coste[G.ter.isin(RET[r])].sum() / G.coste.sum() for r in ('bajo', 'medio', 'alto')}
        pdia = G.groupby('dia').apply(lambda d: pd.Series({r: ev(d.pnl[d.ter.isin(RET[r])], d.coste[d.ter.isin(RET[r])]) for r in ('bajo', 'alto')}), include_groups=False)
        dba = pdia.bajo - pdia.alto; lo, p, m = t_ic(dba)
        txt.append(f"{L:5d} | {e['bajo']:+.3f} / {e['medio']:+.3f} / {e['alto']:+.3f} | {fr['bajo']:.2f}/{fr['medio']:.2f}/{fr['alto']:.2f} | {m:+.3f} ({lo:+.3f}; {int((dba>0).sum())}/{len(dba)}) | {e['G1']:+.3f} ({e['G1']-e['todo']:+.3f}) | {e['G2']:+.3f} | {np.isfinite(S[f'F{L}']).mean():.3f}")
        res[f'{nm}_{L}'] = dict(e, **{'fr_' + k: v for k, v in fr.items()}, bajo_alto_dia=m, ic_inf=lo, dias_pos=int((dba > 0).sum()))
open(AQ + '/curva_rezago_INS.txt', 'w').write('\n'.join(txt)); json.dump(res, open(AQ + '/curva_rezago_INS.json', 'w'), default=float, indent=1); print('\n'.join(txt))
