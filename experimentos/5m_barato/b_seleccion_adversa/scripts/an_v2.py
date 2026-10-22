#!/usr/bin/env python3
"""an_v2.py [NPERM] -- simulador con libro real (dias 17-21 Oct): fidelidad vs B real, AS, descomposicion, barrido de reglas con rasgos de libro/15m/R1
(descubrimiento 17-19, holdout 20-21), disenos que cambian el modelo (confirmacion previa, cancelar por bid 15m, scalp/cobertura con lado contrario)."""
import sys, os, glob; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
from scanlib import *; from sa_common import *
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); NP = int(sys.argv[1]) if len(sys.argv) > 1 else 200
TKV = 295 - 5 * np.arange(47); EPS = 1e-9
Z = [np.load(f, allow_pickle=True) for f in sorted(glob.glob(B + '/datos/simv2/simv2_*.npz'))]
D = {k: np.concatenate([z[k] for z in Z]) for k in Z[0].files}
M = len(D['mkt']); hour = ((D['fin'][:, None] - TKV[None, :]) // 3600 % 24).astype(int)
D['spread'] = D['ba'] - D['bb']; D['imb'] = D['bs'] / (D['bs'] + D['as_']); D['dbb5'] = D['bb'] - D['bb5']; D['dbb30'] = D['bb'] - D['bb30']
D['d15_5'] = D['b15'] - D['b15_5']; D['d15_30'] = D['b15'] - D['b15_30']; D['lvl15'] = D['b15'] - D['p']; D['gap15'] = D['b15'] - D['bb']; D['lbs'] = np.log1p(D['bs']); D['depth_t'] = (D['bb'] - D['p']) / 0.01
dn = np.array([int(x[-2:]) for x in D['dia']]); dis = dn <= 19
steps = np.ones(47, bool)
def run(gate=None, sel=None, mode='cons', parr=None):
    p = D['p'] if parr is None else parr; valid = np.isfinite(p) & steps[None, :]
    if gate is not None: valid = valid & gate
    if sel is not None: valid = valid & sel[:, None]
    fill = valid & (D['minpc'] < p - EPS); kf = fill.argmax(1); filled = fill.any(1); quoted = valid.any(1); ar = np.arange(M)
    pf = np.where(filled, p[ar, kf], np.nan); pq = np.where(quoted, p[ar, valid.argmax(1)], np.nan)
    D['_p'] = p
    R = pd.DataFrame(dict(dia=D['dia'], act=D['act'], quoted=quoted, filled=filled, p=pf, pq=pq, k=np.where(filled, kf, -1), win=D['win'].astype(bool)))
    return R, kf
def ev_(R, sel=None):
    f = R[R.filled] if sel is None else R[R.filled & sel]
    if not len(f): return dict(ev=np.nan, lo=np.nan, hi=np.nan, ev_sin2=np.nan, dias=0, dpos=0, n=0, eur=0.0)
    return day_boot(pd.DataFrame(dict(dia=f.dia.values, p=5 * (f.win.values.astype(float) - f.p.values), c=5 * f.p.values)))
R0, kf0 = run()
q = R0[R0.quoted]; f = R0[R0.filled]; u = q[~q.filled]
print('== FIDELIDAD (libro real, dias 17-21 Oct) mercados', M, 'cotizados', len(q), 'rellenos', len(f), 'tasa %.3f' % (len(f) / len(q)), '| B real: 72 % rellena')
print('acierto relleno %.3f (B real 21.9)  no rellenadas %.3f (B real 37.1)  precio relleno %.3f (B real 0.215)' % (f.win.mean(), u.win.mean(), f.p.mean()))
r = ev_(R0); print('EV rellenado', fmt(r)); allq = (q.win.astype(float) - q.pq).sum() / q.pq.sum(); print('EV de todas las cotizadas (sin seleccion) %+.3f  => AS = %.3f por EUR' % (allq, allq - r['ev']))
ar = np.arange(M); ix = np.flatnonzero(R0.filled.values); k = kf0[ix]
FT = R0.iloc[ix].copy().reset_index(drop=True)
for nm in ['p', 'bb', 'ba', 'bs', 'as_', 'spread', 'imb', 'lbs', 'dbb5', 'dbb30', 'd15_5', 'd15_30', 'lvl15', 'gap15', 'depth_t', 'dp10', 'dp30', 'sh30', 'flow60', 'z', 'ret10', 'sig', 'lastage', 'minpc']: FT['f_' + nm] = D[nm][ix, k]
FT['T'] = TKV[k]; FT['hora'] = hour[ix, k]; FT['pn'] = 5 * (FT.win.astype(float) - FT.p); FT['c'] = 5 * FT.p; FT['overshoot'] = FT.p - FT.f_minpc; FT['dia'] = FT.dia
FT['hb'] = FT.hora // 4
print('overshoot: <=3.5c n=%d EV %.3f | >3.5c n=%d EV %.3f' % ((FT.overshoot <= 0.035).sum(), FT.pn[FT.overshoot <= .035].sum() / FT.c[FT.overshoot <= .035].sum(), (FT.overshoot > .035).sum(), FT.pn[FT.overshoot > .035].sum() / FT.c[FT.overshoot > .035].sum()))
print('por moneda:', {a: round(g.pn.sum() / g.c.sum(), 3) for a, g in FT.groupby('act')}, 'n', FT.act.value_counts().to_dict())
print('top bid size bs (acc) mediana de rellenos', FT.f_bs.median(), 'spread mediana', FT.f_spread.median(), 'depth_t media', FT.f_depth_t.mean())
# ---- barrido de reglas (rasgos al paso de relleno), discovery 17-19 vs holdout 20-21
feats = ['f_bs', 'f_as_', 'f_spread', 'f_imb', 'f_lbs', 'f_dbb5', 'f_dbb30', 'f_d15_5', 'f_d15_30', 'f_lvl15', 'f_gap15', 'f_depth_t', 'f_dp10', 'f_dp30', 'f_sh30', 'f_flow60', 'f_z', 'f_ret10', 'f_sig', 'f_lastage', 'T', 'p']
dsm = (FT.dia.str[-2:].astype(int) <= 19).values
for c in feats: FT[c] = FT[c].astype(float).fillna(FT[c].median())
rules = build_rules(FT, feats, dsm, {'act': ['ETH', 'SOL', 'XRP'], 'hb': [0, 1, 2, 3, 4, 5]})
Td, Th = FT[dsm].reset_index(drop=True), FT[~dsm].reset_index(drop=True)
res = maxstat(Td, rules, nperm=NP, seed=5); eh = stats(masks(Th, rules), Th.pn.values, Th.c.values)
out = pd.DataFrame(dict(regla=[r[0] for r in rules], evg_d=res['eg'], evb_d=res['eb'], t_d=res['t'], ng_d=res['ng'], p_fw=res['p_fw'], valid=res['valid'], evg_h=eh[0], evb_h=eh[1], t_h=eh[2], ng_h=eh[3], nb_h=eh[4]))
out.to_csv(B + '/datos/scan_v2_reglas.csv', index=False)
pd.set_option('display.width', 250)
print('N disc/hold', len(Td), len(Th), 'EV disc %.3f hold %.3f' % (Td.pn.sum() / Td.c.sum(), Th.pn.sum() / Th.c.sum()), 'max-null q95', round(np.quantile(res['mx'], .95), 2))
print(out[out.valid].sort_values('t_d', ascending=False).head(16).round(3).to_string()); print('p_fw<0.10:', int(((out.p_fw < .10) & out.valid).sum()), 'de', int(out.valid.sum()))

print('\n== PROFUNDIDAD DE LA PUJA con libro real: k ticks bajo el top (k=0 = unirse al top) para todas las monedas igual')
bI = np.round(np.nan_to_num(D['bb'], nan=0) * 1000).astype(int); aI = np.round(np.nan_to_num(D['ba'], nan=9) * 1000).astype(int)
for kk in (0, 1, 2, 3, 4, 6):
    o = (bI // 10) * 10 if kk == 0 else np.where(bI % 10 == 0, bI - kk * 10, (bI // 10 - (kk - 1)) * 10)
    okk = np.isfinite(D['bb']) & (bI > 110) & (bI <= 300) & (o >= 100) & (o <= 300) & (o <= bI) & (o < aI) & ((o < bI) | (kk == 0))
    parr = np.where(okk, o / 1000.0, np.nan); R, _ = run(parr=parr); a = ev_(R); qq = R[R.quoted]
    print('k=%d quoted %d fills %d (%.2f) acierto relleno %.3f precio %.3f | EV %+.3f IC90d(%+.3f,%+.3f) disc/hold %+.3f/%+.3f' % (kk, len(qq), R.filled.sum(), R.filled.sum() / max(len(qq), 1), R[R.filled].win.mean(), R[R.filled].p.mean(), a['ev'], a['lo'], a['hi'], ev_(R, R.dia.str[-2:].astype(int) <= 19)['ev'], ev_(R, R.dia.str[-2:].astype(int) > 19)['ev']))
# ---- disenos que cambian el modelo
print('\n== DISENOS (re-simulacion con puerta; EV de lo rellenado; todos los dias 17-21 / disc / hold)')
def show(nm, gate=None):
    R, _ = run(gate=gate); a = ev_(R); ad = ev_(R, (R.dia.str[-2:].astype(int) <= 19)); ah = ev_(R, (R.dia.str[-2:].astype(int) > 19))
    print('%-34s n=%5d EV %+.3f IC90d(%+.3f,%+.3f) | disc %+.3f n=%d | hold %+.3f n=%d | fr %.2f' % (nm, a['n'], a['ev'], a['lo'], a['hi'], ad['ev'], ad['n'], ah['ev'], ah['n'], R.filled.sum() / max(R.quoted.sum(), 1)))
show('base B-like libro real')
show('R1 (sh30>=26 & hora>=4)', (D['sh30'] >= 26) & (hour >= 4))
show('confirmacion: bid sube vs 5 s', D['dbb5'] > 0)
show('confirmacion: bid no baja 5 s', D['dbb5'] >= 0)
show('confirmacion: bid no baja 30 s', D['dbb30'] >= 0)
show('cancelar si bid15 baja 5 s', ~(D['d15_5'] < 0))
show('cancelar si bid15 baja 30 s', ~(D['d15_30'] < 0))
show('top bid size >= 100', D['bs'] >= 100)
show('top bid size >= 300', D['bs'] >= 300)
show('spread <= 0.01', D['spread'] <= 0.0101)
show('spread >= 0.02', D['spread'] >= 0.0199)
show('imb >= 0.5', D['imb'] >= 0.5)
show('R1 + top>=100 + bid15 no baja', (D['sh30'] >= 26) & (hour >= 4) & (D['bs'] >= 100) & ~(D['d15_5'] < 0))
# scalp / cobertura: tras rellenar a p, oferta de venta a p+m == puja en el lado contrario a 1-p-m; relleno si minpc_opp < 1-p-m en pasos posteriores
print('\n== SCALP/COBERTURA (lado contrario a 1-p-m tras el relleno), base B-like')
R, kf = run(); ixf = np.flatnonzero(R.filled.values)
for m_ in (0.01, 0.02, 0.03, 0.05):
    ok = 0; tot = 0; pn = 0.0; cs = 0.0; pn_base = 0.0; rows = []
    for i in ixf:
        k0 = kf[i]; p_ = D['p'][i, k0]; p2 = 1 - p_ - m_; lock = np.any(D['minpc_opp'][i, k0 + 1:] < p2 - EPS)   # rellena la pata contraria mas tarde
        a = 5 * (float(D['win'][i]) - p_); rows.append((D['dia'][i], 5 * m_ if lock else a, 5 * p_, lock, a))
    X = pd.DataFrame(rows, columns=['dia', 'p', 'c', 'lock', 'a'])
    r2 = day_boot(X[['dia', 'p', 'c']]); print('m=%.2f P(cobertura rellena)=%.3f EV %s | base %+.3f' % (m_, X.lock.mean(), fmt(r2), X.a.sum() / X.c.sum()))
