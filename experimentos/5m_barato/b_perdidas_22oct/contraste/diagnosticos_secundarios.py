#!/usr/bin/env python3
"""diagnosticos_secundarios.py -- POST-HOC / SECUNDARIOS (no cambian el veredicto del prereg). Explican POR QUE V9 y V3 no pasan:
 (1) dentro de los grupos con >=2 rellenos, EV del 1.o vs los posteriores (por instrumento); (2) V3 puerta de mercado (variante secundaria del prereg) con placebo;
 (3) EV de rellenos por tramo de spread (I3, I4b); (4) V9 en I4 restringido a makers multi-moneda recurrentes (sensibilidad).
Mismos inputs que contraste_v9_v3.py (solo lectura). Salida: diagnosticos_secundarios.txt"""
import os, sys, glob
os.environ.setdefault('PYTHONDONTWRITEBYTECODE', '1'); sys.dont_write_bytecode = True
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); R = '/root/polymarket-research/experimentos/5m_barato'
SA = R + '/b_seleccion_adversa'; AN = R + '/b_perdidas_22oct/anatomia'
sys.path.insert(0, SA + '/scripts'); sys.path.insert(0, HERE)
import sa_sim, v9v3_lib as lib
OUT = []
def P(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); OUT.append(s)
rng = np.random.default_rng(20261022 + 99)
def first_vs_later(name, df, grp, order_col):
    d = df.copy(); d['g'] = grp; sz = d.groupby('g').g.transform('size'); d = d[sz >= 2].copy()
    d['o'] = d.groupby('g')[order_col].rank(method='first'); first = d[d.o == 1]; later = d[d.o > 1]; mid = d[d.o == 2]
    f = lambda x: x.pnl.sum() / x.cost.sum()
    # IC90 por cierre de (EV_primero - EV_posteriores)
    a = pd.DataFrame(dict(c=d.cierre, pv=np.where(d.o > 1, d.pnl, 0), cv=np.where(d.o > 1, d.cost, 0), pr=np.where(d.o == 1, d.pnl, 0), cr=np.where(d.o == 1, d.cost, 0))).groupby('c').sum().values
    lo, hi, _, _ = lib.boot(a, rng, reps=1000)
    P(f"{name}: grupos con >=2 rellenos {d.g.nunique()} | 1.o: n={len(first)} EV {f(first):+.3f} | posteriores: n={len(later)} EV {f(later):+.3f} | EV(1.o)-EV(posteriores) {f(first)-f(later):+.3f} IC90 por cierre ({lo:+.3f},{hi:+.3f}) [ + = el 1.o es MEJOR; V9 solo ayuda si <0 ]")
    return f(first), f(later)
# ---- I2
D2 = sa_sim.load(SA + '/datos/sim'); Rr = sa_sim.run(D2, delta=sa_sim.dB(D2), mode='cons'); Rr['side'] = D2['side']
f2 = Rr[Rr.filled].copy(); f2['pnl'] = 5 * (f2.win.astype(float) - f2.p); f2['cost'] = 5 * f2.p; f2['cierre'] = f2.fin.astype(np.int64)
first_vs_later('I2 cinta', f2, (f2.cierre.astype(str) + '_' + f2.side.astype(str)).values, 'k')
sz = f2.groupby([f2.cierre, f2.side]).cierre.transform('size'); s1 = f2[sz == 1]
P(f"   rellenos en grupo unitario (1 sola moneda del cierre-lado): n={len(s1)} EV {s1.pnl.sum()/s1.cost.sum():+.3f} | en grupos >=2: n={int((sz>=2).sum())} EV {f2[sz>=2].pnl.sum()/f2[sz>=2].cost.sum():+.3f}")
# ---- I3
zs = sorted(glob.glob(SA + '/datos/simv2/simv2_*.npz')); Z = [np.load(f, allow_pickle=True) for f in zs]; D3 = {k: np.concatenate([z[k] for z in Z]) for k in Z[0].files}; M = len(D3['mkt'])
spr = np.round(D3['ba'].astype(float) - D3['bb'].astype(float), 2); p3 = D3['p']; valid0 = np.isfinite(p3); win3 = D3['win'].astype(bool); ar = np.arange(M)
fill = valid0 & (D3['minpc'] < p3 - 1e-9); kf = fill.argmax(1); filled = fill.any(1); ix = np.flatnonzero(filled)
F3 = pd.DataFrame(dict(dia=D3['dia'][ix], act=D3['act'][ix], cierre=D3['fin'][ix].astype(np.int64), side=D3['side'][ix], k=kf[ix], p=p3[ix, kf[ix]], win=win3[ix], spread=spr[ix, kf[ix]]))
F3['pnl'] = 5 * (F3.win.astype(float) - F3.p); F3['cost'] = 5 * F3.p
first_vs_later('I3 simv2', F3, (F3.cierre.astype(str) + '_' + F3.side.astype(str)).values, 'k')
# (2) V3 puerta de mercado: particion por spread en la 1.a cotizacion valida, con placebo estricto por (dia,moneda)
fv = valid0.argmax(1); spf = spr[ar, fv]; mk_veto = (spf > 0.025) & valid0.any(1)
F3['mveto'] = mk_veto[ix]; F3['grp3'] = F3.dia + '_' + F3.act
t = lib.summarize('I3m', F3[['dia', 'cierre', 'pnl', 'cost', 'grp3']].assign(veto=F3.mveto.values), 'grp3', rng)
P(f"I3 V3 puerta de MERCADO (particion de rellenos por spread en la 1.a cotizacion >0,02): n={t['n']} vetados={t['nv']} ({t['share_veto']:.1%}) EV_ret {t['ev_r']:+.3f} EV_vet {t['ev_v']:+.3f} Delta {t['delta']:+.3f} IC90 dia ({t['ic90_dia_delta'][0]:+.3f},{t['ic90_dia_delta'][1]:+.3f}) cierre ({t['ic90_cierre_delta'][0]:+.3f},{t['ic90_cierre_delta'][1]:+.3f}) neto {t['net']:+.1f} placebo {t['placebo_estricto']['media']:+.1f} p={t['placebo_estricto']['p']:.3f} dias Delta>0 {t['dias_delta_pos']}/{t['dias']}")
P('   por dia: ' + ' '.join(f"{k[-5:]}:D{('na' if v['delta'] is None else format(v['delta'], '+.2f'))}/net{v['net']:+.1f}/v{v['nv']}" for k, v in t['por_dia'].items()))
# re-sim del mercado con placebo (barajar el vector de veto de mercado dentro de dia-moneda)
def pnl_sel(sel):
    fl = valid0 & sel[:, None] & (D3['minpc'] < p3 - 1e-9); k_ = fl.argmax(1); f_ = fl.any(1); return float((5 * (win3[f_].astype(float) - p3[ar, k_][f_])).sum())
base = pnl_sel(np.ones(M, bool)); real = pnl_sel(~mk_veto) - base
gi = pd.Series(range(M)).groupby([D3['dia'], D3['act']]).apply(lambda s: s.values).tolist(); pl = np.empty(2000)
for r in range(2000):
    perm = np.arange(M)
    for g_ in gi: perm[g_] = rng.permutation(g_)
    pl[r] = pnl_sel(~mk_veto[perm]) - base
P(f"   re-sim puerta de mercado: cambio de PnL {real:+.1f} EUR; placebo (veto de mercado barajado por dia-moneda) media {pl.mean():+.1f} p95 {np.quantile(pl,.95):+.1f}; p={(np.sum(pl>=real-1e-9)+1)/2001:.4f}; vetados {int(mk_veto.sum())}/{int(valid0.any(1).sum())} mercados")
# (3) EV por tramo de spread
def tramos(name, df, col):
    b = pd.cut(df[col], [-.001, .0151, .0251, .0351, 1.0], labels=['<=0,01', '0,02', '0,03', '>=0,04'])
    g = df.groupby(b, observed=True).agg(n=('pnl', 'size'), pnl=('pnl', 'sum'), c=('cost', 'sum'), dias=('dia', 'nunique')); g['EV'] = g.pnl / g.c
    P(f"{name} EV por spread: " + ' | '.join(f"{i}: n={int(r.n)} EV {r.EV:+.3f}" for i, r in g.iterrows()))
tramos('I3 (spread en el paso de relleno)', F3, 'spread')
MU = pd.read_pickle(SA + '/datos/ms_units.pkl')[['dia', 'c', 'p', 'spread', 'fin']].rename(columns={'c': 'cost', 'p': 'pnl'}).dropna(subset=['spread']); MU['spread'] = MU.spread.round(2)
tramos('I4b (spread en el relleno)', MU, 'spread')
# (4) I4 V9 en makers multi-moneda recurrentes
uf = sorted(glob.glob(SA + '/datos/units/units_*.pkl')); U = pd.concat([pd.read_pickle(f)[['dia', 'maker', 'mkt', 'lado_c', 'c', 'p', 'fin', 'ts']] for f in uf], ignore_index=True).rename(columns={'c': 'cost', 'p': 'pnl'})
U['cierre'] = U.fin.astype(np.int64); U['grp'] = U.maker + '_' + U.cierre.astype(str) + '_' + U.lado_c
first_vs_later('I4 poblacion', U, U.grp.values, 'ts')
nmulti = U[U.groupby('grp').grp.transform('size') >= 2].groupby('maker').grp.nunique()
for thr in (20, 100):
    mk = set(nmulti[nmulti >= thr].index); Us = U[U.maker.isin(mk)].copy(); veto = lib.veto_time(Us.grp.values, Us.ts.values, 3.0)
    t = lib.summarize('I4s', Us[['dia', 'cierre', 'pnl', 'cost', 'grp']].assign(veto=veto), 'grp', rng, reps=500)
    P(f"I4 V9 L=3 s solo makers con >={thr} grupos multi-moneda ({len(mk)} makers, n={t['n']}): EV_ret {t['ev_r']:+.3f} EV_vet {t['ev_v']:+.3f} Delta {t['delta']:+.3f} IC90 dia ({t['ic90_dia_delta'][0]:+.3f},{t['ic90_dia_delta'][1]:+.3f}) cierre ({t['ic90_cierre_delta'][0]:+.3f},{t['ic90_cierre_delta'][1]:+.3f}) neto {t['net']:+.1f} placebo estricto {t['placebo_estricto']['media']:+.1f} p={t['placebo_estricto']['p']:.3f}")
# ---- I1
B1 = pd.read_csv(AN + '/pos_anotado2.csv'); B1['cierre'] = B1.fin.astype(np.int64); B1 = B1.rename(columns={'coste': 'cost'})
first_vs_later('I1 B real', B1, (B1.cierre.astype(str) + '_' + B1.lado).values, 't_fill')
open(HERE + '/diagnosticos_secundarios.txt', 'w').write('\n'.join(OUT) + '\n')
