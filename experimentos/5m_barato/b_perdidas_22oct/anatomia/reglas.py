#!/usr/bin/env python3
"""reglas.py -- (a) rasgo de tendencia previa (Chainlink, recepcion) 15/60 min firmado hacia nuestro lado; (b) walk-forward honesto:
elegir celdas de veto con 20-21 Oct (pos 1-109) y medirlas en 22-Oct (66 pos), sin re-elegir; (c) contabilidad de cada veto candidato:
perdidas evitadas, ganancias renunciadas, neto (todo en EUR, PnL on-chain). Solo lectura."""
import numpy as np, pandas as pd, csv, datetime as dt
from scipy.stats import fisher_exact
D = pd.read_csv('pos_anotado.csv')
cl = {}
for Dd in ['2026-10-20', '2026-10-21', '2026-10-22']:
    with open(f'/root/polymarket-research/data/prices/chainlink_{Dd}.csv') as f:
        rd = csv.reader(f); next(rd)
        for ts, a, p, w, s in rd:
            if s == 'chainlink' and a in ('ETH', 'SOL', 'XRP'): cl.setdefault(a, []).append((dt.datetime.fromisoformat(ts).timestamp(), float(p)))
cl = {a: (np.array([x[0] for x in v]), np.array([x[1] for x in v])) for a, v in cl.items()}
for a in cl: o = np.argsort(cl[a][0]); cl[a] = (cl[a][0][o], cl[a][1][o])
def px(a, t):
    i = np.searchsorted(cl[a][0], t, side='right') - 1; return cl[a][1][i] if i >= 0 and t - cl[a][0][i] < 30 else np.nan
s = np.where(D.lado == 'YES', 1, -1)
D['tr15'] = s * np.array([(px(c, t) / px(c, t - 900) - 1) * 1e4 for c, t in zip(D.coin, D.t_fill)])
D['tr60'] = s * np.array([(px(c, t) / px(c, t - 3600) - 1) * 1e4 for c, t in zip(D.coin, D.t_fill)])
for col in ['tr15', 'tr60']:
    D[col + 'b'] = pd.qcut(D[col], 4).astype(str)
    print(f'--- {col} (bps firmado hacia nuestro lado; + = la tendencia nos favorece)')
    t = D.groupby(col + 'b').agg(n=('pnl', 'size'), hit=('gana', 'mean'), precio=('precio', 'mean'), pnl=('pnl', 'sum'), c=('coste', 'sum')); t['EV'] = t.pnl / t.c
    t['dias'] = D.groupby(col + 'b').apply(lambda g: '/'.join(f"{g[g.dia == d].pnl.sum() / g[g.dia == d].coste.sum():+.2f}" if (g.dia == d).any() else 'na' for d in sorted(D.dia.unique())), include_groups=False)
    print(t.round(3).to_string())
    print('spearman con gana', round(D[[col, 'gana']].corr(method='spearman').iloc[0, 1], 3))
D.to_csv('pos_anotado2.csv', index=False)
# (b) walk-forward
DIMS = ['coin', 'lado', 'hb', 'pb', 'Tb', 'acc_b', 'distb', 'pre30b', 'bnpre30b', 'btcpre30b', 'volb', 'repb', 'sprb', 'fvgb', 'tr15b', 'tr60b']
tr = D[D.dia < '2026-10-22']; te = D[D.dia == '2026-10-22']
cells = []
for dim in DIMS:
    for v, g in tr.groupby(dim):
        if len(g) >= 15: cells.append((dim, v, len(g), g.pnl.sum() / g.coste.sum(), g.pnl.sum()))
C = pd.DataFrame(cells, columns=['dim', 'v', 'n_tr', 'EV_tr', 'pnl_tr']).sort_values('EV_tr')
print(f'\n=== Walk-forward: {len(C)} celdas con n>=15 en 20-21 Oct (n={len(tr)}); se eligen las 5 de peor EV y se miden en 22-Oct (n={len(te)}) sin re-elegir')
for _, r in C.head(5).iterrows():
    m = te[r.dim].astype(str) == str(r.v); g = te[m]; rest = te[~m]
    print(f"{r.dim}={r.v}: train n={r.n_tr} EV {r.EV_tr:+.3f} | 22-Oct veto n={len(g)} pnl {g.pnl.sum():+.2f} EV {g.pnl.sum()/max(g.coste.sum(),1e-9):+.3f}  resto n={len(rest)} EV {rest.pnl.sum()/rest.coste.sum():+.3f}")
print('(placebo: 5 celdas al azar con n>=15 en train, mismo test, 2000 sorteos)')
rng = np.random.default_rng(5); deltas = []
for _ in range(2000):
    pick = C.sample(5, random_state=int(rng.integers(1e9)))
    deltas.append(np.mean([-te[te[r.dim].astype(str) == str(r.v)].pnl.sum() for _, r in pick.iterrows()]))
real = np.mean([-te[te[r.dim].astype(str) == str(r.v)].pnl.sum() for _, r in C.head(5).iterrows()])
print(f'EUR evitado medio por veto en 22-Oct: elegidas {real:+.2f} vs placebo media {np.mean(deltas):+.2f} p95 {np.percentile(deltas,95):+.2f}; P(placebo>=elegidas)={(np.array(deltas)>=real).mean():.3f}')
# (c) contabilidad de vetos candidatos (in-sample 175, y por dia)
def acct(name, m):
    g = D[m]; L = g[g.gana == 0]; W = g[g.gana == 1]
    by = '/'.join(f"{-g[g.dia == d].pnl.sum():+.1f}" for d in sorted(D.dia.unique()))
    print(f"{name}: veta n={len(g)} ({len(g)/len(D):.0%}, {g.coste.sum():.1f} EUR coste) | perdidas evitadas {-L.pnl.sum():+.2f} | ganancias renunciadas {W.pnl.sum():.2f} ({len(W)} ganadoras) | NETO {-g.pnl.sum():+.2f} EUR | neto por dia {by} | EV resto {D[~m].pnl.sum()/D[~m].coste.sum():+.3f} (n={int((~m).sum())})")
print('\n=== Contabilidad de vetos (IN-SAMPLE, 175 posiciones; neto = -pnl de lo vetado)')
acct('V1 hora 08-11 UTC', D.hb == '08-11')
acct('V2 precio >=0,25', D.precio >= 0.25)
acct('V3 spread al pujar >0,02', D.spread_post > 0.021)
acct('V4 XRP', D.coin == 'XRP')
acct('V5 Binance 30 s previo en contra (-4,-1] bps', (D.bn_pre30 > -4) & (D.bn_pre30 <= -1))
acct('V6 lado Up', D.lado == 'YES')
acct('V7 tendencia 60 min en contra (cuartil inferior tr60)', D.tr60 <= D.tr60.quantile(.25))
acct('V8 tendencia 15 min en contra (cuartil inferior tr15)', D.tr15 <= D.tr15.quantile(.25))
acct('V1|V3', (D.hb == '08-11') | (D.spread_post > 0.021))
