#!/usr/bin/env python3
"""Paso 11. (A) Modelo de SELECCION de cierres de R1/R2 (logistica, entrenada 09-12 Oct, holdout 13-18) con rasgos causales en NUESTRO disparo A (primer instante m>=-0,05 & dm>=0,01):
 ask5, bid15, T, asz5, bsz15, m, dm, |gap| bp, hora UTC. EV de nuestra entrada A (limite=ask, +215 ms, nivel 1) en todos los disparos vs en el top 30 % predicho vs en cierres realmente operados por rivales (holdout).
(B) BOLSILLO 'favorito anidado' que R1 gana 10/10 dias (precio 0,7-1,0): 4 variantes FIJADAS antes: F1 ask5 in [.70,.95] & m>=-.05; F2 idem & m>=0; F3 ask5 in [.50,.95] & m>=-.05; F4 F1 & dm>=.01. 1a entrada por cierre, +215 ms. Bonferroni x4."""
import glob, numpy as np, pandas as pd
O = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/r3_out/'
fee = lambda p: 0.07 * p * (1 - p)
F = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(O + 'feat_*.csv.gz'))], ignore_index=True).drop_duplicates(['cierre', 't']).sort_values(['cierre', 't'])
F['gana'] = F.gana.astype(bool); F['dm'] = F.db15_1s - F.da5_1s; F['T'] = F.cierre - F.t / 1000
F['hora'] = (F.cierre % 86400) / 3600.0
Rv = pd.read_csv(O + 'p1_fills.csv.gz', usecols=['cierre', 'w', 'placebo', 'gap_bp']); Rv = Rv[(Rv.placebo == 0) & Rv.w.isin(['R1_9783', 'R2_e38c'])]
rset = set(Rv.cierre); gap = Rv.drop_duplicates('cierre').set_index('cierre').gap_bp.abs()
rng = np.random.default_rng(21)
def prim(mask):
    d = F[mask].groupby('cierre').head(1).copy(); d['ejec'] = d.acc_e215 > 0; d['p'] = d.ask_e215
    d['coste'] = np.where(d.ejec, d.acc_e215 * (d.p + fee(d.p)), 0.0); d['pnl'] = np.where(d.ejec, d.acc_e215 * (d.gana.astype(float) - d.p - fee(d.p)), 0.0); d['riv'] = d.cierre.isin(rset); return d
def boot(x, key, q):
    g = x.groupby(key)[['pnl', 'coste']].sum().values
    if len(g) < 3: return (np.nan, np.nan)
    ix = rng.integers(0, len(g), (4000, len(g))); r = g[ix, 0].sum(1) / np.maximum(g[ix, 1].sum(1), 1e-9); return tuple(np.percentile(r, [q, 100 - q]).round(3))
def rep(x, nom):
    e = x[x.ejec]
    if e.coste.sum() <= 0: print(f'  {nom:36s} n=0'); return
    by = e.groupby('dia')[['pnl', 'coste']].sum(); top = by.pnl.sort_values(ascending=False).index[:2]; y = e[~e.dia.isin(top)]
    print(f'  {nom:36s} disp={len(x):3d} ejec={len(e):3d} dias={e.dia.nunique():2d} coste={e.coste.sum():6.1f} EV={e.pnl.sum()/e.coste.sum():+.3f} acierto={e.gana.mean():.2f} IC90cierre={boot(e,"cierre",5)} Bonf4inf={boot(e,"cierre",1.25)[0]} IC90dia={boot(e,"dia",5)} sin2mejores={(y.pnl.sum()/y.coste.sum() if y.coste.sum()>0 else np.nan):+.3f} dias+={(by.pnl>0).sum()}/{len(by)}')
# ---------------- (A)
A = prim((F.m >= -0.05) & (F.dm >= 0.01)); A['gap'] = A.cierre.map(gap)
# gap de cierres sin rival: no disponible -> se usa solo como rasgo si existe; aqui se omite (cobertura parcial)
X = ['ask5', 'bid15', 'T', 'asz5', 'bsz15', 'm', 'dm', 'hora']
def prep(d): 
    Z = d[X].copy(); Z['asz5'] = np.log1p(Z.asz5); Z['bsz15'] = np.log1p(Z.bsz15); Z['hs'] = np.sin(2 * np.pi * Z.hora / 24); Z['hc'] = np.cos(2 * np.pi * Z.hora / 24); Z = Z.drop(columns='hora'); return Z
tr = A[(A.dia >= '2026-10-09') & (A.dia <= '2026-10-12')]; te = A[A.dia >= '2026-10-13']
Zt = prep(tr); mu, sd = Zt.mean(), Zt.std() + 1e-9
def fit(Z, y, lam=1.0):
    Z = np.c_[np.ones(len(Z)), ((Z - mu) / sd).values]; w = np.zeros(Z.shape[1])
    for _ in range(50):
        p = 1 / (1 + np.exp(-Z @ w)); g = Z.T @ (p - y) + lam * w * np.r_[0, np.ones(Z.shape[1] - 1)]; H = (Z.T * (p * (1 - p))) @ Z + lam * np.eye(Z.shape[1]); w -= np.linalg.solve(H, g)
    return w
w = fit(Zt, tr.riv.values.astype(float))
def score(d): Z = np.c_[np.ones(len(d)), ((prep(d) - mu) / sd).values]; return Z @ w
def auc(x, y):
    d = pd.DataFrame({'x': x, 'y': y}); n1 = d.y.sum(); n0 = len(d) - n1; return (d.x.rank()[d.y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0) if n1 and n0 else np.nan
te = te.copy(); te['s'] = score(te)
print('(A) entrenamiento 09-12:', len(tr), 'disparos', int(tr.riv.sum()), 'rival | holdout 13-18:', len(te), 'disparos', int(te.riv.sum()), 'rival | AUC holdout', round(auc(te.s, te.riv.astype(int)), 3), '| coef', dict(zip(['c'] + list(prep(tr).columns), w.round(2))))
rep(te, 'A holdout: TODOS los disparos')
rep(te[te.s >= te.s.quantile(0.7)], 'A holdout: top 30 % predicho rival')
rep(te[te.s < te.s.quantile(0.7)], 'A holdout: resto 70 %')
rep(te[te.riv], 'A holdout: cierres que SI opero rival')
rep(te[~te.riv], 'A holdout: cierres que NO opero rival')
# ---------------- (B)
print('\n(B) bolsillo favorito anidado (4 variantes fijadas):')
V = {'F1 ask[.70,.95] m>=-.05': (F.ask5 >= .70) & (F.ask5 <= .95) & (F.m >= -.05), 'F2 ask[.70,.95] m>=0': (F.ask5 >= .70) & (F.ask5 <= .95) & (F.m >= 0),
     'F3 ask[.50,.95] m>=-.05': (F.ask5 >= .50) & (F.ask5 <= .95) & (F.m >= -.05), 'F4 F1 & dm>=.01': (F.ask5 >= .70) & (F.ask5 <= .95) & (F.m >= -.05) & (F.dm >= .01)}
for k, mk in V.items():
    d = prim(mk); print('---', k)
    rep(d, 'TODO 06-18'); rep(d[d.dia <= '2026-10-12'], 'DESC 06-12'); rep(d[d.dia >= '2026-10-13'], 'TEST 13-18')
