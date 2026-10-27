#!/usr/bin/env python3
"""e1c_eval.py -- PREREG_E1C (sha 9b064af9...). Evalua las politicas de cancelacion sobre senales.csv.gz (contrafactual sustractivo sobre ordenes reales de B).
Salida: datos/e1c_resultados.txt, datos/e1c_tabla.csv, datos/e1c_rellenos.csv. Solo lectura."""
import os, sys, hashlib, warnings, numpy as np, pandas as pd
warnings.filterwarnings('ignore')
AQ = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.join(AQ, '..', '..'); D = os.path.join(AQ, '..', 'datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_E1C.md'), 'rb').read()).hexdigest().startswith('9b064af90b24')
OUT = '/root/polymarket-research-datalogs/e1_cancelacion_ms/'
rng = np.random.default_rng(7); out = []
def P(*a): out.append(' '.join(str(x) for x in a)); print(*a)
S = pd.read_csv(os.environ.get('E1C_CK', OUT + 'senales_parcial.jsonl').replace('_parcial.jsonl', '.csv.gz'))
C = pd.read_csv(os.path.join(BASE, 'cola_posicion', 'datos', 'b_cola.csv'))[['oid', 'pnl', 'coste', 'gana', 'pc']]
P('ordenes', len(S), S.estado.value_counts().to_dict())
X = S[S.estado == 'ok'].merge(C, on='oid', how='left')
F = X[X.relleno == 1].copy(); N = X[X.relleno == 0].copy()
P('rellenas ok', len(F), 'sin pnl', int(F.pnl.isna().sum()), '| no rellenas ok', len(N))
F = F[F.pnl.notna()].copy()
F['banda'] = np.where(F.q <= 200, '0,10-0,20', '0,20-0,30'); F['hp'] = F.gana - F.pc
F = F.merge(pd.read_csv(os.path.join(BASE, 'cola_posicion', 'datos', 'b_l2.csv'))[['oid', 'print_exacto']], on='oid', how='left')
P('print localizado por talla exacta (1/2) vs aproximado (0):', F.print_exacto.value_counts().to_dict())
P(f'BASE sin cancelar: n={len(F)} pnl={F.pnl.sum():.2f} coste={F.coste.sum():.2f} EV€={F.pnl.sum()/F.coste.sum():+.4f} | por dia:',
  F.groupby('dia').apply(lambda d: f'{len(d)}/{d.pnl.sum():+.2f}/{d.pnl.sum()/d.coste.sum():+.3f}').to_dict())
FAM = {'BN': 'BN_', 'KNIFE5': ('KN_', 'GAP_'), 'L15': 'L15_', 'TRADE': 'TR_', 'DEPTH': ('DP_', 'SOLO', 'AH_'), 'EDAD': 'ED_'}
cols = [c for c in S.columns if c.split('_')[0] in ('BN', 'KN', 'GAP', 'L15', 'TR', 'DP', 'SOLO', 'AH', 'ED') or c == 'SOLO']
fam_of = lambda c: next(f for f, p in FAM.items() if c.startswith(p))
def avoided(df, col, lead=90):
    v = df[col].values; return (v >= 0) & (v <= df['end'].values - lead)
def met(df, av):
    k = df[~av]; a = df[av]
    return dict(n=len(df), n_ev=int(av.sum()), dPnL=-a.pnl.sum(), EVret=(k.pnl.sum() / k.coste.sum()) if len(k) else np.nan,
                ret=k.coste.sum() / df.coste.sum(), gan_perd=int((a.gana == 1).sum()), eur_gan_perd=a[a.gana == 1].pnl.sum(),
                hp_ev=a.hp.mean() if len(a) else np.nan, hp_ret=k.hp.mean() if len(k) else np.nan)
def placebo(df, av, nrep=5000):
    obs = -df[av].pnl.sum(); grp = [g.pnl.values for _, g in df.assign(av=av).groupby('dia')]; ks = [int(x.av.sum()) for _, x in df.assign(av=av).groupby('dia')]
    sims = np.zeros(nrep)
    for i in range(nrep):
        s = 0.0
        for v, k in zip(grp, ks):
            if k: s -= v[rng.choice(len(v), k, replace=False)].sum()
        sims[i] = s
    return obs, float((sims >= obs - 1e-12).mean()), float(sims.std()), float(sims.mean())
def boot_cierre(df, av, nb=2000):
    d = df.assign(x=np.where(av, -df.pnl, 0.0)).groupby('fin').x.sum().values
    return np.quantile([rng.choice(d, len(d)).sum() for _ in range(nb)], [0.05, 0.95])
# rate de disparo en vidas NO rellenas (coste de oportunidad no modelado)
def rate_N(col): v = N[col].values; return float((v >= 0).mean())
TR = F[F.dia.isin(['2026-10-20', '2026-10-21'])]; TE = F[F.dia == '2026-10-22']
rows = []
for c in cols:
    for nm, df in (('TRAIN', TR), ('TEST', TE), ('TODO', F)):
        av = avoided(df, c); m = met(df, av); m.update(cfg=c, fam=fam_of(c), part=nm, miss_bn=int((df[c] == -2).sum()), tasa_N=rate_N(c)); rows.append(m)
T = pd.DataFrame(rows)
# F7 combos: OR de mejores (TRAIN)
best = {}
for fam in FAM:
    t = T[(T.fam == fam) & (T.part == 'TRAIN')].sort_values('dPnL', ascending=False); best[fam] = t.iloc[0].cfg
P('elegidas en TRAIN (max dPnL):', best)
def orcol(cs, name):
    for df in (F, N):
        v = np.full(len(df), -1.0)
        for c in cs:
            x = df[c].values; v = np.where((x >= 0) & ((v < 0) | (x < v)), x, v)
        df[name] = v
    return name
combos = [orcol([best['BN'], best['DEPTH']], 'CB_BN+DP'), orcol([best['KNIFE5'], best['DEPTH']], 'CB_KN+DP'), orcol([best['BN'], best['KNIFE5'], best['DEPTH']], 'CB_BN+KN+DP')]
TR = F[F.dia.isin(['2026-10-20', '2026-10-21'])]; TE = F[F.dia == '2026-10-22']
rows = []
for c in combos:
    for nm, df in (('TRAIN', TR), ('TEST', TE), ('TODO', F)):
        av = avoided(df, c); m = met(df, av); m.update(cfg=c, fam='COMBO', part=nm, miss_bn=0, tasa_N=rate_N(c)); rows.append(m)
T = pd.concat([T, pd.DataFrame(rows)]); T.round(4).to_csv(os.path.join(D, 'e1c_tabla.csv'), index=False)
tc = T[(T.fam == 'COMBO') & (T.part == 'TRAIN')].sort_values('dPnL', ascending=False); best['COMBO'] = tc.iloc[0].cfg
P('\nTODAS las configs (TRAIN | TEST | TODO): dPnL, n_evitados, EVret, tasa disparo en vidas NO rellenas')
pv = T.pivot_table(index='cfg', columns='part', values=['dPnL', 'n_ev'], aggfunc='first')
for c in pv.index:
    r = pv.loc[c]; P(f'  {c:14s} TRAIN {r[("dPnL","TRAIN")]:+6.2f} ({int(r[("n_ev","TRAIN")])}) | TEST {r[("dPnL","TEST")]:+6.2f} ({int(r[("n_ev","TEST")])}) | TODO {r[("dPnL","TODO")]:+6.2f} ({int(r[("n_ev","TODO")])}) | tasaN {T[(T.cfg==c)].tasa_N.iloc[0]:.2f}')
Kt = 7; alfa = 0.10 / Kt
P(f'\nGATE en TEST (22-Oct) por familia, K_test={Kt}, alfa={alfa:.4f}')
fills_out = F[['oid', 'act', 'dia', 'fin', 'q', 'pc', 'pnl', 'coste', 'gana', 'end', 'vida']].copy()
for fam, c in best.items():
    av = avoided(TE, c); m = met(TE, av); obs, p, se, mu = placebo(TE, av); lo, hi = boot_cierre(TE, av)
    avA = avoided(F, c); dd = F.assign(x=np.where(avA, -F.pnl, 0.0)); pdia = dd.groupby('dia').x.sum().sort_values(); pcie = dd.groupby('fin').x.sum().sort_values()
    sin2d = pdia.iloc[:-2].sum(); sin2c = pcie.iloc[:-2].sum(); mA = met(F, avA)
    ok = (obs > 0) and (p < alfa) and (lo > 0) and (sin2d > 0) and (sin2c > 0) and (mA['ret'] >= 0.40)
    mde = (2.19 + 0.84) * se
    P(f'  {fam:7s} {c:14s} TEST dPnL {obs:+.2f} (evita {m["n_ev"]}/{m["n"]}; placebo media {mu:+.2f} se {se:.2f} p={p:.3f}; IC90 cierre {lo:+.2f},{hi:+.2f}) '
      f'EVret {m["EVret"]:+.3f} ret {m["ret"]:.2f} ganadores perdidos {m["gan_perd"]} ({m["eur_gan_perd"]:+.2f} EUR) hp_evit {m["hp_ev"]:+.3f} hp_ret {m["hp_ret"]:+.3f} | '
      f'TODO dPnL {mA["dPnL"]:+.2f} EVret {mA["EVret"]:+.3f} sin2dias {sin2d:+.2f} sin2cierres {sin2c:+.2f} | MDE {mde:.2f} | GATE {"PASA" if ok else "FALLA"}')
    fills_out[c] = avA.astype(int)
    # sensibilidad de latencia: lead requerido
    s = ' '.join(f'{L}ms:{-F[avoided(F, c, L)].pnl.sum():+.2f}({int(avoided(F, c, L).sum())})' for L in (90, 150, 250, 400, 1000))
    P(f'          lead requerido (TODO) {s}')
    Fx = F[F.print_exacto >= 1]; ax = avoided(Fx, c); ox, px, sx, mx_ = placebo(Fx, ax, 2000)
    rTR = F[F.dia == '2026-10-22']; rTE = F[F.dia != '2026-10-22']; ar = avoided(rTE, c); orr, pr_, sr, mr = placebo(rTE, ar, 2000)
    P(f'          solo print exacto (TODO): dPnL {ox:+.2f} evita {int(ax.sum())}/{len(Fx)} placebo p={px:.3f} | EXTRA no prereg, test=20-21: dPnL {orr:+.2f} evita {int(ar.sum())} p={pr_:.3f}')
fills_out.to_csv(os.path.join(D, 'e1c_rellenos.csv'), index=False)
P('\nDesglose moneda x banda (TODO) de las elegidas: base n/pnl/EV | evitados n/pnl | EVret')
for fam, c in best.items():
    av = avoided(F, c); dd = F.assign(av=av)
    for (a, b), g in dd.groupby(['act', 'banda']):
        k = g[~g.av]; P(f'  {c:14s} {a} {b}: base {len(g)}/{g.pnl.sum():+.2f}/{g.pnl.sum()/g.coste.sum():+.3f} | evit {int(g.av.sum())}/{g[g.av].pnl.sum():+.2f} | EVret {k.pnl.sum()/max(k.coste.sum(),1e-9):+.3f}')
P('\nSelección adversa: hit-p rellenas base', round(F.hp.mean(), 4), 'n', len(F))
open(os.path.join(D, 'e1c_resultados.txt'), 'w').write('\n'.join(out) + '\n')
