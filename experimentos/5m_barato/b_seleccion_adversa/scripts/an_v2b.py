#!/usr/bin/env python3
"""an_v2b.py [NPERM] -- (1) barrido en POBLACION con rasgos de libro (ms_units.pkl, 17-21 Oct, disc 17-19 / hold 20-21); (2) regla lvl15 (bid15 - puja) en el simulador con libro real,
sola y combinada con R1, por dia y por moneda; (3) cuentas en EUR/ano."""
import sys, os, glob; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
from scanlib import *; from sa_common import *
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); NP = int(sys.argv[1]) if len(sys.argv) > 1 else 300
U = pd.read_pickle(B + '/datos/ms_units.pkl').rename(columns={'p': 'pn'}); U = U[U.has5].copy(); U['hb'] = U.hora // 4
feats = ['spread', 'depth_ticks', 'imb', 'lbs', 'dbb5', 'dbb30', 'd15_5', 'd15_30', 'lvl15', 'gap15', 'vol30ws', 'vol30', 'cl_dev', 'qage', 'gap_last', 'dp30', 'dp60', 'd_open', 'flow60', 'fv_gap', 'z', 'b10', 'T', 'pc']
for f in feats: U[f] = U[f].astype(float)
dn = U.dia.str[-2:].astype(int); dis = (dn <= 19).values
print('POBLACION 17-21 Oct con libro: unidades', len(U), 'EUR', round(U.c.sum()), 'EV %.3f' % (U.pn.sum() / U.c.sum()), '| disc %.3f hold %.3f' % (U.pn[dis].sum() / U.c[dis].sum(), U.pn[~dis].sum() / U.c[~dis].sum()))
print('cobertura 15m %.3f; vol30ws vs vol30 on-chain: corr log %.3f ; acuerdo del umbral 26: %.3f' % (U.b15.notna().mean(), np.corrcoef(np.log1p(U.vol30ws.fillna(0)), np.log1p(U.vol30))[0, 1], ((U.vol30ws >= 26) == (U.vol30 >= 26)).mean()))
Td, Th = U[dis].reset_index(drop=True), U[~dis].reset_index(drop=True)
rules = build_rules(U, feats, dis, {'act': ['ETH', 'SOL', 'XRP'], 'hb': [0, 1, 2, 3, 4, 5]})
res = maxstat(Td, rules, nperm=NP, seed=9); eh = stats(masks(Th, rules), Th.pn.values, Th.c.values)
out = pd.DataFrame(dict(regla=[r[0] for r in rules], evg_d=res['eg'], evb_d=res['eb'], t_d=res['t'], ng_d=res['ng'], p_fw=res['p_fw'], valid=res['valid'], evg_h=eh[0], evb_h=eh[1], t_h=eh[2], ng_h=eh[3], nb_h=eh[4]))
out.to_csv(B + '/datos/scan_pop_libro_reglas.csv', index=False); pd.set_option('display.width', 250)
print('max-null q95', round(np.quantile(res['mx'], .95), 2)); print(out[out.valid].sort_values('t_d', ascending=False).head(14).round(3).to_string()); print('p_fw<0.10:', int(((out.p_fw < .10) & out.valid).sum()), 'de', int(out.valid.sum()))
for nm, m in (('lvl15<=0.03', U.lvl15 <= 0.03), ('lvl15 NaN', U.lvl15.isna()), ('lvl15>0.03', U.lvl15 > 0.03)):
    for per, pm in (('disc', dis), ('hold', ~dis)):
        s = U[m.values & pm]; print('poblacion', nm, per, fmt(day_boot(s, 'pn', 'c', 'dia')))
# (2) simulador con libro real
exec(open(os.path.dirname(os.path.abspath(__file__)) + '/an_v2.py').read().split('R0, kf0 = run()')[0].split('Z = [np.load')[0].replace('NP = int(sys.argv[1]) if len(sys.argv) > 1 else 200', ''))
Z = [np.load(f, allow_pickle=True) for f in sorted(glob.glob(B + '/datos/simv2/simv2_*.npz'))]
D = {k: np.concatenate([z[k] for z in Z]) for k in Z[0].files}; M = len(D['mkt']); TKV = 295 - 5 * np.arange(47); EPS = 1e-9
hour = ((D['fin'][:, None] - TKV[None, :]) // 3600 % 24).astype(int); lvl = D['b15'] - D['p']; steps = np.ones(47, bool)
def run(gate=None):
    p = D['p']; valid = np.isfinite(p) & steps[None, :]
    if gate is not None: valid = valid & gate
    fill = valid & (D['minpc'] < p - EPS); kf = fill.argmax(1); fd = fill.any(1); qd = valid.any(1); ar = np.arange(M)
    return pd.DataFrame(dict(dia=D['dia'], act=D['act'], quoted=qd, filled=fd, p=np.where(fd, p[ar, kf], np.nan), win=D['win'].astype(bool), pq=np.where(qd, p[ar, valid.argmax(1)], np.nan)))
def evs(R, m=None):
    f = R[R.filled] if m is None else R[R.filled & m]
    return day_boot(pd.DataFrame(dict(dia=f.dia.values, p=5 * (f.win.values.astype(float) - f.p.values), c=5 * f.p.values))) if len(f) else dict(ev=np.nan, lo=np.nan, hi=np.nan, ev_sin2=np.nan, dpos=0, dias=0, n=0, eur=0)
print('\n== SIMULADOR con libro real: regla lvl15 (cotizar solo si bid15 - puja <= x) sola y con R1; dias 17-21 / disc / hold / por dia')
dnn = np.array([int(x[-2:]) for x in D['dia']])
for nm, g in (('base', None), ('lvl15<=0.03', lvl <= 0.03), ('lvl15<=0.05', lvl <= 0.05), ('lvl15<=0.10', lvl <= 0.10), ('lvl15<=0.03 & R1', (lvl <= 0.03) & (D['sh30'] >= 26) & (hour >= 4)), ('lvl15<=0.05 & R1', (lvl <= 0.05) & (D['sh30'] >= 26) & (hour >= 4)),
              ('lvl15<=0.03 | lvl15 NaN', (lvl <= 0.03) | ~np.isfinite(lvl)), ('lvl15<=0 (15m no mayor)', lvl <= 0.0)):
    R = run(g); a = evs(R); q = R[R.quoted]; ad = evs(R, R.dia.str[-2:].astype(int) <= 19); ah = evs(R, R.dia.str[-2:].astype(int) > 19)
    pdv = {d[-2:]: round(evs(R, R.dia == d)['ev'], 3) for d in sorted(set(D['dia']))}
    print('%-26s n=%4d fr %.2f EV %+.3f IC90d(%+.3f,%+.3f) sin2 %+.3f | disc %+.3f hold %+.3f | por dia %s | EV_cotizadas %+.3f' % (nm, a['n'], R.filled.sum() / max(len(q), 1), a['ev'], a['lo'], a['hi'], a['ev_sin2'], ad['ev'], ah['ev'], pdv, (q.win.astype(float) - q.pq).sum() / max(q.pq.sum(), 1e-9)))
R = run(lvl <= 0.03)
for a_ in ('ETH', 'SOL', 'XRP'): print('  lvl15<=0.03', a_, fmt(evs(R, R.act == a_)))
