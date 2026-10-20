#!/usr/bin/env python3
"""Paso 6: combinacion preregistrable = MAKER H23 primario (join en bid 5m lado s, margen>=-0,05, cancela 60 ms, rebate 20 %) + TOMADOR V4b (m>=0,02, 1er instante por cierre, +215 ms, nivel 1).
Regla de exclusion por cierre (una sola via por evento): si el maker se rellena como tarde 60 ms despues del disparo del tomador, cuenta el maker y el tomador NO compra;
si no, compra el tomador (el maker se cancela en el disparo, sin relleno posible despues de t+60). Datos: mk_D (sim_dia3) y feat_D, BTC 06-18 Oct, desenlace oficial."""
import glob, numpy as np, pandas as pd
O = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/r3_out/'
fee = lambda p: 0.07 * p * (1 - p)
M = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(O + 'mk_*.csv')) if __import__('os').path.getsize(f) > 0])
M = M[(M['var'] == 'join') & (M.mq == -0.05) & (M.clk == 'rx') & (M.lc == 60)].drop_duplicates(['dia', 'cierre'])
M['gana'] = M.gana.astype(float); M['pnl_m'] = M.lleno * M.gana - M.coste + M.rebate; M['coste_m'] = M.coste
F = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(O + 'feat_*.csv.gz'))], ignore_index=True).drop_duplicates(['cierre', 't']).sort_values(['cierre', 't'])
T = F[F.m >= 0.02 - 1e-9].groupby('cierre').head(1).copy()
T['ej'] = T.acc_e215 > 0; T['p'] = T.ask_e215
T['coste_t'] = np.where(T.ej, T.acc_e215 * (T.p + fee(T.p)), 0.0); T['pnl_t'] = np.where(T.ej, T.acc_e215 * (T.gana.astype(float) - T.p - fee(T.p)), 0.0)
X = M[['dia', 'cierre', 'lleno', 't_relleno', 'pnl_m', 'coste_m', 'gana']].merge(T[['cierre', 't', 'ej', 'pnl_t', 'coste_t']], on='cierre', how='outer')
X['dia'] = X.dia.fillna(X.cierre.map(F.drop_duplicates('cierre').set_index('cierre').dia))
mf = X.lleno.fillna(0) > 0; tg = X.t.notna()
mk_vale = mf & (~tg | (X.t_relleno <= X.t + 60))
X['pnl'] = np.where(mk_vale, X.pnl_m, np.where(tg & X.ej.fillna(False), X.pnl_t, 0.0)); X['coste'] = np.where(mk_vale, X.coste_m, np.where(tg & X.ej.fillna(False), X.coste_t, 0.0))
X['via'] = np.where(mk_vale, 'maker', np.where(tg & X.ej.fillna(False), 'tomador', 'nada'))
rng = np.random.default_rng(9)
def boot(d, key, q=5):
    g = d.groupby(key)[['pnl', 'coste']].sum().values
    if len(g) < 3: return (np.nan, np.nan)
    ix = rng.integers(0, len(g), (4000, len(g))); r = g[ix, 0].sum(1) / np.maximum(g[ix, 1].sum(1), 1e-9); return tuple(np.percentile(r, [q, 100 - q]).round(3))
def rep(d, nom):
    d = d[d.coste > 0]
    if not len(d): print(f'  {nom}: n=0'); return
    by = d.groupby('dia')[['pnl', 'coste']].sum(); top = by.pnl.sort_values(ascending=False).index[:2]; y = d[~d.dia.isin(top)]
    print(f'  {nom:26s} n={len(d):3d} dias={d.dia.nunique():2d} coste={d.coste.sum():6.1f} PnL={d.pnl.sum():+7.2f} EV={d.pnl.sum()/d.coste.sum():+.3f} IC90cierre={boot(d,"cierre")} IC90dia={boot(d,"dia")} sin2mejores={(y.pnl.sum()/y.coste.sum() if y.coste.sum()>0 else np.nan):+.3f} dias+={(by.pnl>0).sum()}/{len(by)}')
print('cierres con maker relleno', int(mf.sum()), '| con disparo tomador m>=0,02', int(tg.sum()), '| ambos', int((mf & tg).sum()))
for nm, sel in (('TODO 06-18', X.dia > ''), ('DESC 06-12', X.dia <= '2026-10-12'), ('TEST 13-18', X.dia >= '2026-10-13')):
    print('==', nm); x = X[sel]
    rep(x.assign(pnl=x.pnl_m.fillna(0), coste=x.coste_m.fillna(0)), 'solo MAKER H23')
    rep(x.assign(pnl=x.pnl_t.fillna(0), coste=x.coste_t.fillna(0)), 'solo TOMADOR V4b(0,02)')
    rep(x, 'COMBINADO (una via)'); print('   vias:', x.via.value_counts().to_dict())
    rep(x[x.via == 'tomador'], '  incremento tomador')
