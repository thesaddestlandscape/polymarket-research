#!/usr/bin/env python3
"""Paso 5: (a) ¿Que cierres eligen los rivales? AUC de rasgos causales en NUESTRO disparo A (m>=-0,05 & dm>=0,01, 1er instante por cierre) para la etiqueta
'R1 o R2 operaron ese cierre' (descriptivo). (b) Familia FIJADA ANTES de mirar (4 variantes): A & ask5>=X & T>=Y, X in {0,20; 0,30}, Y in {120; 200} s.
Se elige la mejor por EV en DESC (06-12, n>=15 ejecutables) y se evalua UNA vez en TEST (13-18). Bonferroni x4. Ejecucion: limite=ask5, +215 ms, nivel 1 (feat_D)."""
import glob, numpy as np, pandas as pd
O = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/r3_out/'
F = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(O + 'feat_*.csv.gz'))], ignore_index=True).drop_duplicates(['cierre', 't']).sort_values(['cierre', 't'])
F['gana'] = F.gana.astype(bool); F['dm'] = F.db15_1s - F.da5_1s; F['T'] = F.cierre - F.t / 1000
fee = lambda p: 0.07 * p * (1 - p)
Rv = pd.read_csv(O + 'p1_fills.csv.gz'); Rv = Rv[(Rv.placebo == 0) & Rv.w.isin(['R1_9783', 'R2_e38c'])]
rset = set(Rv.cierre); gap = Rv.drop_duplicates('cierre').set_index('cierre').gap_bp.abs()
rng = np.random.default_rng(3)
def prim(mask):
    d = F[mask].groupby('cierre').head(1).copy(); d['ejec'] = d.acc_e215 > 0; d['p'] = d.ask_e215
    d['coste'] = np.where(d.ejec, d.acc_e215 * (d.p + fee(d.p)), 0.0); d['pnl'] = np.where(d.ejec, d.acc_e215 * (d.gana.astype(float) - d.p - fee(d.p)), 0.0)
    d['riv'] = d.cierre.isin(rset); return d
def auc(x, y):
    d = pd.DataFrame({'x': x, 'y': y}).dropna(); n1 = d.y.sum(); n0 = len(d) - n1
    return (d.x.rank()[d.y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0) if n1 and n0 else np.nan
def boot(x, key, q):
    g = x.groupby(key)[['pnl', 'coste']].sum().values
    if len(g) < 3: return np.nan, np.nan
    ix = rng.integers(0, len(g), (4000, len(g))); r = g[ix, 0].sum(1) / np.maximum(g[ix, 1].sum(1), 1e-9); return tuple(np.percentile(r, [q, 100 - q]).round(3))
def rep(x, nom):
    e = x[x.ejec]
    if e.coste.sum() <= 0: print(f'  {nom}: n=0'); return np.nan
    ev = e.pnl.sum() / e.coste.sum(); by = e.groupby('dia')[['pnl', 'coste']].sum(); top = by.pnl.sort_values(ascending=False).index[:2]; y = e[~e.dia.isin(top)]
    print(f'  {nom:34s} disparos={len(x):3d} ejec={len(e):3d} dias={e.dia.nunique():2d} coste={e.coste.sum():6.1f} EV={ev:+.3f} acierto={e.gana.mean():.2f} IC90cierre={boot(e,"cierre",5)} Bonf4inf={boot(e,"cierre",1.25)[0]} IC90dia={boot(e,"dia",5)} sin2mejores={(y.pnl.sum()/y.coste.sum() if y.coste.sum()>0 else np.nan):+.3f} dias+={(by.pnl>0).sum()}/{len(by)}')
    return ev
A = prim((F.m >= -0.05) & (F.dm >= 0.01)); A['gap'] = A.cierre.map(gap)
print('(a) AUC rasgos del disparo A para etiqueta rival-opero-el-cierre (n=%d, rival=%d)' % (len(A), A.riv.sum()))
print({c: round(auc(A[c], A.riv), 3) for c in ['ask5', 'bid15', 'asz5', 'bsz15', 'T', 'm', 'dm', 'r250', 'r1000']})
print('   cobertura gap solo en cierres rival (no se usa)')
print(f'   pct disparos con ask5<=0,15: rival {(A[A.riv].ask5 <= .15).mean():.2f} / no-rival {(A[~A.riv].ask5 <= .15).mean():.2f} ; con T<120: {(A[A.riv]["T"] < 120).mean():.2f} / {(A[~A.riv]["T"] < 120).mean():.2f}')
print('\n(b) familia fijada: A & ask5>=X & T>=Y')
base = (F.m >= -0.05) & (F.dm >= 0.01); R = {}
desc = F.dia <= '2026-10-12'
for X in (0.20, 0.30):
    for Y in (120, 200):
        mk = base & (F.ask5 >= X) & (F['T'] >= Y); d = prim(mk)
        print(f'--- X={X} Y={Y}'); R[(X, Y)] = rep(d[d.dia <= '2026-10-12'], 'DESC 06-12'); rep(d[d.dia >= '2026-10-13'], 'TEST 13-18'); rep(d, 'TODO')
ok = {k: v for k, v in R.items() if v == v}
best = max(ok, key=ok.get) if ok else None
print('\nmejor en DESC:', best, ok.get(best))
if best:
    d = prim(base & (F.ask5 >= best[0]) & (F['T'] >= best[1])); print('TEST de la elegida (una sola vez):'); rep(d[d.dia >= '2026-10-13'], f'ELEGIDA {best} TEST')
