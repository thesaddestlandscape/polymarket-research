#!/usr/bin/env python3
"""f3_real.py <modelo> <phi> [T] - (d) PREREG_DFUERTE: modelo CONGELADO (entrenado <=2026-08-17) sobre precios reales (pop 17-22 Oct, baratas 5-14 Oct). p_con = precio pagado (aprox. declarada)."""
import sys, os, pickle, hashlib, numpy as np, pandas as pd, warnings
warnings.filterwarnings('ignore')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..', 'scripts'))
assert hashlib.sha256(open(os.path.join(HERE, '..', 'PREREG_DFUERTE.md'), 'rb').read()).hexdigest().startswith('5efad7c6')
import dfuerte_lib as DL, r3_precios as R3
OUT = '/root/polymarket-research-datalogs/regimen_5m/dfuerte'; MOD = sys.argv[1]; PHI = float(sys.argv[2]); TSEL = int(sys.argv[3]) if len(sys.argv) > 3 else 180
kind, fams, m, CUT = pickle.load(open(f'{OUT}/frozen_models_T{TSEL}.pkl', 'rb'))[MOD]; cq = lambda f: CUT['q%d' % round(f * 100)]
W = pd.read_pickle(f'{OUT}/windows_reciente.pkl')[['coin', 'tmin', 'o'] + DL.FEATS].drop_duplicates(['coin', 'tmin'])
def cols(fams): return list(dict.fromkeys(['lpc'] + sum([DL.FAM[f] for f in fams], [])))
def prep(P):
    P = P.drop(columns=[c for c in DL.FEATS if c in P.columns]).merge(W, on=['coin', 'tmin'], how='left')
    P = P[P.o.notna() & (P.rpre.abs() >= R3.THR)].copy(); P['con'] = P.rpre >= R3.THR
    P['pcon'] = np.where(P.con, P.pc_, 1 - P.pc_); P = P[(P.pcon > 0.02) & (P.pcon < 0.98)].copy(); P['lpc'] = np.log(P.pcon / (1 - P.pcon))
    P['s_hat'] = m.predict_proba(P[cols(fams)].values.astype(float))[:, 1] - P.pcon.values; return P
def rep(P, label):
    print(f'\n=== {label}: unidades |rpre|>=7,7 con rasgos {len(P)}, CON {int(P.con.sum())}, dias {P.dia.nunique()}, cierres {P.cierre.nunique()}, PnL CON {P.pnl_u[P.con].sum():+.1f} EUR, coste CON {P.cost_u[P.con].sum():.0f} ===')
    for nm, mk in [(f'DETECTOR phi={t:.2f}', P.con & (P.s_hat <= cq(t))) for t in sorted({0.10, 0.25, 0.50, PHI})] + [('INVERSION 1-phi*', P.con & (P.s_hat >= cq(1 - PHI))), ('R-TEND R1 (CON&TREND)', P.con & (P.R == 'TREND')), ('INCONDICIONAL CON', P.con)]:
        mk = mk.values; n = int(mk.sum())
        if n < 20: print(f'  {nm:28s} n {n} (<20)'); continue
        dp = -P.pnl_u[mk].sum(); lo, hi = R3.ic_cierre(P, mk); pl = R3.placebo(P, P.con, mk & P.con.values, 300); evs = P.pnl_u[mk].sum() / P.cost_u[mk].sum()
        print(f'  {nm:28s} n {n:5d} coste {P.cost_u[mk].sum():7.0f} EV salt {evs:+.3f} dPnL {dp:+8.1f} IC90cierre ({lo:+.1f},{hi:+.1f}) placebo media {pl.mean():+.1f} p {(pl>=dp).mean():.3f}  EXCESO {dp-pl.mean():+.1f}')
    g = P.groupby('dia').apply(lambda x: pd.Series({'dP_det': -x.pnl_u[x.con & (x.s_hat <= cq(PHI))].sum(), 'dP_R1': -x.pnl_u[x.con & (x.R == 'TREND')].sum(), 'dP_inc': -x.pnl_u[x.con].sum(), 'n_det': int((x.con & (x.s_hat <= cq(PHI))).sum())}), include_groups=False)
    print(g.round(1).to_string())
pop = prep(R3.load_pop()); rep(pop, 'S_C pop 17-22 Oct'); rep(pop[pop.dia >= '2026-10-20'], 'S_C pop TEST 20-22 Oct')
rep(prep(R3.load_barat()), 'S_C baratas 5-14 Oct (banda 0,10-0,20, normalizado 5 acc)')
