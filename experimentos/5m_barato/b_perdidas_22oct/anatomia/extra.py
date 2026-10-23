#!/usr/bin/env python3
"""extra.py -- pruebas complementarias (solo lectura): seleccion adversa rellenas vs no rellenas por tramo (Fisher), tasa base Up
de TODOS los 5m ETH/SOL/XRP 20-22 Oct (twap60 oficial), forward de la hipotesis spread<=0,02 (declarada 22-Oct 08:57Z en
b_seleccion_adversa/INFORME.md §E), salida condicionada a Binance post-relleno (exploratoria, contrastar con H40), concentracion por cierre."""
import numpy as np, pandas as pd, csv, collections
from scipy.stats import fisher_exact, norm
D = pd.read_csv('pos_anotado.csv'); U = pd.read_csv('pujas.csv')
print('=== 1. Seleccion adversa: acierto rellenas vs NO rellenas (pujas.csv, unidad puja mercado-lado, desenlace gamma)')
U = U.sort_values('fin').reset_index(drop=True); U['tramo'] = pd.cut(np.arange(len(U)), [-1, 91, 183, 400], labels=['1', '2', '3']).astype(str)
U['t22'] = np.where(U.dia == '2026-10-22', '22-Oct', '20-21 Oct')
for dim in ['tramo', 't22', 'coin']:
    for v, g in U.groupby(dim):
        f = g[g.relleno]; nf = g[~g.relleno]
        a, b, c, d = int(f.gana.sum()), int((1 - f.gana).sum()), int(nf.gana.sum()), int((1 - nf.gana).sum())
        print(f'{dim}={v}: rellenas {a}/{a+b}={a/(a+b):.3f} (precio post {f.p_post.mean():.3f})  no rellenas {c}/{c+d}={c/(c+d):.3f} (precio {nf.p_post.mean():.3f})  Fisher p={fisher_exact([[a,b],[c,d]])[1]:.4f}')
# interaccion: brecha tramo 3 vs tramos 1-2 (bootstrap por puja)
r = np.random.default_rng(3)
def gap(g): return g[~g.relleno].gana.mean() - g[g.relleno].gana.mean()
g3 = U[U.tramo == '3']; g12 = U[U.tramo != '3']; obs = gap(g3) - gap(g12)
pl = []
lab = (U.tramo == '3').values
for _ in range(5000):
    p = r.permutation(lab); pl.append(gap(U[p]) - gap(U[~p]))
print(f'brecha (no rell - rell) tramo3 {gap(g3):+.3f} vs tramos1-2 {gap(g12):+.3f}; diferencia {obs:+.3f}, p perm (tramo barajado) {(np.abs(pl) >= abs(obs)).mean():.3f}')
print('\n=== 2. Tasa base Up de TODOS los 5m ETH/SOL/XRP (twap60 oficial cierre>=apertura), por dia')
TW = collections.defaultdict(dict)
for Dd in ['2026-10-20', '2026-10-21', '2026-10-22']:
    with open(f'/root/polymarket-research/data/prices/polybolt_{Dd}.csv') as f:
        rd = csv.reader(f); next(rd)
        for ts, a, can, v, ems, sn, s in rd:
            if can == 'twap60' and s == 'chainlink' and a in ('ETH', 'SOL', 'XRP'):
                e = int(ems) // 1000
                if e % 300 == 0: TW[a][e] = float(v)
rows = []
for a, m in TW.items():
    for e, v in m.items():
        if e + 300 in m: rows.append(dict(coin=a, e=e, up=float(m[e + 300] >= v), dia=pd.to_datetime(e, unit='s').strftime('%Y-%m-%d'), h=pd.to_datetime(e, unit='s').hour))
B = pd.DataFrame(rows); B = B[B.e >= 1792496400]
print(B.groupby(['dia']).up.agg(['size', 'mean']).round(3).to_string()); print(B.groupby(['coin']).up.agg(['size', 'mean']).round(3).to_string())
print('B: acierto Up', D[D.lado == 'YES'].gana.mean().round(3), 'n', (D.lado == 'YES').sum(), ' Down', D[D.lado == 'NO'].gana.mean().round(3), 'n', (D.lado == 'NO').sum())
print('B lado por dia (n, acierto):'); print(D.groupby(['dia', 'lado']).gana.agg(['size', 'mean']).round(3).unstack().to_string())
print('\n=== 3. Forward de spread<=0,02 al pujar (hipotesis declarada con 209 pujas, corte 22-Oct 08:57Z)')
cut = pd.Timestamp('2026-10-22T08:57Z').timestamp()
for nm, g in [('antes del corte (descubrimiento)', D[D.t_fill < cut]), ('DESPUES del corte (forward)', D[D.t_fill >= cut])]:
    for v, h in g.groupby(g.spread_post <= 0.021):
        print(f'{nm} spread<=0,02={v}: n={len(h)} gan={int(h.gana.sum())} eur={h.coste.sum():.2f} pnl={h.pnl.sum():+.2f} EV={h.pnl.sum()/h.coste.sum():+.3f}')
print('\n=== 4. Salida condicionada post-relleno (EXPLORATORIA; H40 REJECTED 36/36 con n grande). Venta al mid_30s - x, comision 0,07*p*(1-p)*acc')
F = D[D.mo30.notna()].copy(); F['mid30'] = F.precio * (1 + F.mo30)
for col, th in [('bn_post30', -3), ('bn_post30', -1), ('mov_post30_cl', -3), ('mov_post10_cl', -2), ('bn_post5', -2)]:
    for x in (0.01, 0.02):
        s = F[F[col] <= th]; bid = (s.mid30 - x).clip(lower=0); fee = 0.07 * bid * (1 - bid) * s.acc
        venta = (bid * s.acc - fee); hold = s.acc * s.gana
        print(f'{col}<={th} spread/2={x}: n={len(s)} ganadoras vendidas={int(s.gana.sum())} mid30 medio={s.mid30.mean():.3f} -> vender {venta.sum():+.2f} vs mantener {hold.sum():+.2f}: delta {venta.sum()-hold.sum():+.2f} EUR; esperado por mid (sum acc*mid30) {(s.acc*s.mid30).sum():.2f}')
print(f'(sobre {len(F)} de {len(D)} posiciones con mid_30s en el ledger; faltan {len(D)-len(F)})')
print('\n=== 5. Concentracion: cierres con >=2 posiciones (misma apuesta)')
c = D.groupby('fin').agg(n=('pnl', 'size'), g=('gana', 'sum'), pnl=('pnl', 'sum'))
print('cierres', len(c), 'con >=2 pos', int((c.n >= 2).sum()), 'pos en ellos', int(c[c.n >= 2].n.sum()), 'todas perdidas en cierres multi', int(((c.n >= 2) & (c.g == 0)).sum()), 'pnl cierres multi', round(c[c.n >= 2].pnl.sum(), 2))
print('top5 posiciones pnl', D.pnl.nlargest(5).round(2).tolist(), 'suma', round(D.pnl.nlargest(5).sum(), 2), '| perdida media', round(D[D.gana == 0].pnl.mean(), 3), 'ganancia media', round(D[D.gana == 1].pnl.mean(), 3))
print('breakeven hit = precio medio', round(D.coste.sum() / D.acc.sum(), 3), 'hit real', round(D.gana.mean(), 3))
# P(hit<=37/175 | p=precio) y binomial por dia
from scipy.stats import binom
for dname, g in D.groupby('dia'):
    pexp = (g.coste / g.acc).mean(); print(dname, f'hit {g.gana.mean():.3f} vs precio {pexp:.3f} n={len(g)} P(hit<=obs | p=precio)={binom.cdf(int(g.gana.sum()), len(g), pexp):.3f}')
