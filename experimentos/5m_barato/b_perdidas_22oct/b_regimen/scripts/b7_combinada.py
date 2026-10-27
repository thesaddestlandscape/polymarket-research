#!/usr/bin/env python3
"""b7_combinada.py -- H-C EXPLORATORIA (ADENDA 3): reglas sin ajuste (R0 = CON, N2 = AR2h<=-0,10) combinadas; metrica EXCESO_EV. K adicional 3 (union, interseccion, CON|AR2h<=0)."""
import sys, os, numpy as np, pandas as pd
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/q_techo/scripts')
from qlib import perm_cierre, clus, boot_ratio, COINS
T = pd.read_pickle('/mnt/HC_Volume_106538179/agentes_datos/b_regimen/tab_reg.pkl').reset_index(drop=True)
OUT = []
def P(*a):
    s = ' '.join(str(x) for x in a); OUT.append(s); print(s, flush=True)
def rep(nom, X, skip):
    c, p = X.c.values, X.p.values; r = ~skip; cl = clus(X)
    ret = c[r].sum() / c.sum(); evr = p[r].sum() / c[r].sum(); eva = p.sum() / c.sum(); pp, nm, _ = perm_cierre(X, skip)
    cs = c[skip].sum(); dnul = ((p.sum() + nm) / (c.sum() - cs)) - eva; lo, hi = boot_ratio(p * r, c * r, cl)
    dd = pd.Series(-p * skip).groupby(X.dia.values).sum(); ex = -(p[skip].sum()) - nm
    ddn = pd.Series(0.0)
    P(f'{nom}: skip EUR {cs:.0f} ({1-ret:.2f}) | EV_all {eva:+.4f} EV_ret {evr:+.4f} [{lo:+.3f},{hi:+.3f}] | dEV {evr-eva:+.4f} EXCESO_EV {evr-eva-dnul:+.4f} p_perm {pp:.4f} | dPnL {-p[skip].sum():+.0f} (exceso dPnL sobre nulo {ex:+.0f})')
for pn, X in (('P1 09-16', T[T.dia <= '2026-10-16'].reset_index(drop=True)), ('P2 17-21', T[T.dia >= '2026-10-17'].reset_index(drop=True))):
    P(f'#### {pn}'); con = (X.cls == 'CON').values; n2 = (X.AR2h <= -0.10).values & X.AR2h.notna().values; ar0 = (X.AR2h <= 0.0).values & X.AR2h.notna().values
    rep('R0 (CON)', X, con); rep('N2 (AR2h<=-0,10)', X, n2); rep('UNION R0 u N2', X, con | n2); rep('INTERSECCION R0 y N2', X, con & n2); rep('CON solo si AR2h<=0', X, con & ar0)
    for a in COINS:
        m = (X.act == a).values; Xa = X[m].reset_index(drop=True); ca = con[m]; na = n2[m]
        P(f'   {a}: EV_all {Xa.p.sum()/Xa.c.sum():+.3f} | EV_ret R0 {Xa.p.values[~ca].sum()/Xa.c.values[~ca].sum():+.3f} | EV_ret N2 {Xa.p.values[~na].sum()/Xa.c.values[~na].sum():+.3f} | EV_ret union {Xa.p.values[~(ca|na)].sum()/Xa.c.values[~(ca|na)].sum():+.3f}')
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos', 'b7_resultados.txt'), 'w').write('\n'.join(OUT))
