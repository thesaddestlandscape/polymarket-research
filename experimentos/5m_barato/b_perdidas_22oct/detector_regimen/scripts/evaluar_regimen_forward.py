#!/usr/bin/env python3
"""evaluar_regimen_forward.py - GATE de la regla candidata 'rpre-skip condicionada a regimen' sobre la POBLACION etiquetada por L1b (pob_DIA) unida a las etiquetas de regimen (etiquetar_regimen.py).
Solo lectura. Reglas congeladas (3; Bonferroni x3): R0 = saltar CON>=7,7 (h_w1==1); R1 = R0 & R==TREND; R2 = R0 & R in {TREND,MIXTO}.
Metrica = PnL TOTAL: dP = -Sum pnl(saltadas) (EUR, pnl sin rebate). Gate (todo a la vez, por regla): >=10 dias forward (dia >= 2026-10-23), >=300 unidades saltadas, dP>0 con IC90 por cierre inferior >0,
placebo (mismo numero de saltos al azar dentro de dia x moneda x cubo de precio 0,05 entre h_w1==1) p<0,05/3, dP>0 en >=60 % de los dias, dP sin los 2 mejores dias >0, y EV/EUR retenido > EV/EUR base.
Uso: python3 -I evaluar_regimen_forward.py [--desde 2026-10-23]"""
import os, sys, glob, argparse, numpy as np, pandas as pd
POB = os.environ.get('L1B_POB', '/root/polymarket-research-datalogs/etiquetado_pasivo_B/poblacion'); ET = os.environ.get('REG_ET', '/root/polymarket-research-datalogs/regimen_5m/etiquetas')
RNG = np.random.default_rng(7)
def cargar(desde):
    P = pd.concat([pd.read_csv(f, dtype={'mid': str}) for f in sorted(glob.glob(f'{POB}/pob_*.csv.gz'))], ignore_index=True)
    P = P[P.gana_lado.notna() & P.pnl.notna() & (P.dia >= desde)].copy()
    E = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(f'{ET}/regimen_*.csv.gz'))], ignore_index=True)[['coin', 'tmin', 'R', 'D', 'COH']]
    P['tmin'] = (P.fin_s // 60 - 5).astype(int); P = P.merge(E, on=['coin', 'tmin'], how='left'); return P
def evalua(P, nombre, regla, nb=2000, npl=1000):
    base = P.pnl.sum(); h = P.h_w1 == 1; m = regla(P) & h; n = int(m.sum())
    if n < 20: return f'{nombre}: n saltadas {n} (<20)'
    dP = -P.pnl[m].sum(); g = P.assign(s=np.where(m, P.pnl, 0.0)).groupby('cierre' if 'cierre' in P else 'fin_s').s.sum().values
    bs = np.array([-g[RNG.integers(0, len(g), len(g))].sum() for _ in range(nb)]); lo = np.percentile(bs, 5)
    strat = (P.dia.astype(str) + P.coin + (P.precio * 20).astype(int).astype(str)).astype('category').cat.codes.values
    el = np.nonzero(h.values)[0]; cnt = pd.Series(m.values[el]).groupby(strat[el]).sum(); idx = pd.Series(el).groupby(strat[el]).apply(list)
    pl = np.empty(npl)
    for i in range(npl):
        t = 0.0
        for s_, k in cnt.items():
            if k: t += P.pnl.values[RNG.choice(idx[s_], int(k), replace=False)].sum()
        pl[i] = -t
    p = (pl >= dP).mean(); dd = P.assign(s=np.where(m, -P.pnl, 0.0)).groupby('dia').s.sum()
    ret = (base - P.pnl[m].sum()) / (P.coste.sum() - P.coste[m].sum()); b0 = base / P.coste.sum()
    ok = dict(dias=P.dia.nunique() >= 10, n=n >= 300, ic=lo > 0, placebo=p < 0.05 / 3, pos=(dd > 0).mean() >= 0.6, sin2=dd.sort_values().iloc[:-2].sum() > 0, ev=ret > b0)
    return f'{nombre}: dias {P.dia.nunique()} n saltadas {n} coste {P.coste[m].sum():.0f} dP {dP:+.1f} EUR IC90cierre inf {lo:+.1f} placebo p {p:.3f} dias dP>0 {(dd>0).mean():.2f} sin2mejores {dd.sort_values().iloc[:-2].sum():+.1f} EV ret {ret:+.4f} vs base {b0:+.4f} -> ' + ('GATE OK' if all(ok.values()) else 'NO (' + ','.join(k for k, v in ok.items() if not v) + ')')
if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--desde', default='2026-10-23'); a = ap.parse_args(); P = cargar(a.desde)
    print(f'unidades {len(P)} dias {P.dia.nunique()} (desde {a.desde}); etiqueta R presente {P.R.notna().mean():.3f}')
    if P.dia.nunique() == 0: print('NO EVALUABLE'); sys.exit(0)
    for nm, rg in (('R0 incondicional', lambda D: D.h_w1 == 1), ('R1 TREND', lambda D: D.R == 'TREND'), ('R2 TREND|MIXTO', lambda D: D.R.isin(['TREND', 'MIXTO']))): print(evalua(P, nm, rg))
