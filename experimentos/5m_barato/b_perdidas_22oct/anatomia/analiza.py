#!/usr/bin/env python3
"""analiza.py -- anatomia de perdidas de B real (pos.csv / pujas.csv de build.py). Solo lectura. Salida: stdout (-> analiza.txt).
EV ponderado por EUR = sum pnl / sum coste. IC90 bootstrap por CIERRE (posiciones del mismo cierre = 1 apuesta) y por bloque dia-hora.
Celda vs resto: diferencia de EV ponderado; p familiar = max-estadistico (|t|) permutando desenlaces (pnl) entre posiciones dentro de dia,
sobre TODAS las celdas con n>=15 de las dimensiones PRE-relleno (accionables). Las dimensiones POST-relleno son descriptivas."""
import numpy as np, pandas as pd, sys
from scipy.stats import norm
pd.set_option('display.width', 250)
D = pd.read_csv('pos.csv').sort_values('t_fill').reset_index(drop=True); U = pd.read_csv('pujas.csv')
D['orden'] = np.arange(len(D))
D['tercio'] = pd.cut(D.orden, [-1, 58, 116, 200], labels=['1:pos1-59', '2:pos60-117', '3:pos118-175']).astype(str)
D['pb'] = (np.floor(D.precio / 0.05 + 1e-9) * 0.05).round(2).astype(str)
D['hb'] = (D.hora // 4 * 4).map(lambda h: f'{h:02d}-{h+3:02d}')
D['Tb'] = pd.cut(D.T_rest, [60, 120, 180, 240, 301]).astype(str)
D['acc_b'] = pd.cut(D.acc, [0, 4.99, 5.01, 100], labels=['<5', '=5', '>5']).astype(str)
D['distb'] = pd.cut(D.dist_ref_bps, [-99, -8, -6, -4, 0]).astype(str)
D['pre30b'] = pd.cut(D.mov_pre30_cl, [-99, -4, -1, 1, 99]).astype(str)
D['bnpre30b'] = pd.cut(D.bn_pre30, [-99, -4, -1, 1, 99]).astype(str)
D['btcpre30b'] = pd.cut(D.btc_pre30, [-99, -3, 0, 3, 99]).astype(str)
D['volb'] = pd.cut(D.vol60_bps, [0, 2.5, 3.3, 4.2, 99]).astype(str)
D['repb'] = pd.cut(D.n_ordenes, [0, 1, 4, 10, 1e9]).astype(str)
D['espb'] = pd.cut(D.espera_s, [-1, 2, 10, 60, 1e9]).astype(str)
D['colab'] = pd.cut(D.cola_fill, [-1, 20, 60, 150, 1e9]).astype(str)
D['sprb'] = pd.cut(D.spread_post, [-1, 0.021, 0.041, 1]).astype(str)
# FV naive: P(lado) = Phi(dist / (vol60 * sqrt(T/60)))  (sin calibrar: SOBRECONFIADO, solo para ordenar)
D['fv'] = norm.cdf(D.dist_ref_bps / (D.vol60_bps * np.sqrt(D.T_rest / 60)).clip(lower=0.1))
D['fv_gap'] = D.fv - D.precio
D['fvgb'] = pd.cut(D.fv_gap, [-1, -0.1, -0.03, 0.03, 1]).astype(str)
D['postb'] = pd.cut(D.mov_post30_cl, [-99, -3, 0, 3, 99]).astype(str)
D['bnpostb'] = pd.cut(D.bn_post30, [-99, -3, 0, 3, 99]).astype(str)
D['mo5b'] = pd.cut(D.mo5, [-9, -0.2, 0, 0.2, 9]).astype(str)
PRE = ['coin', 'lado', 'hb', 'dia', 'tercio', 'pb', 'Tb', 'acc_b', 'distb', 'pre30b', 'bnpre30b', 'btcpre30b', 'volb', 'repb', 'sprb', 'fvgb', 'en_ledger']
POSTD = ['espb', 'colab', 'postb', 'bnpostb', 'mo5b', 'tras_cancel']
def ev(df): return df.pnl.sum() / df.coste.sum() if len(df) else np.nan
def boot(df, key, nb=4000, seed=1):
    g = df.groupby(key)[['pnl', 'coste']].sum()
    if len(g) < 3: return (np.nan, np.nan)
    r = np.random.default_rng(seed); i = r.integers(0, len(g), (nb, len(g)))
    e = g.pnl.values[i].sum(1) / g.coste.values[i].sum(1); return tuple(np.quantile(e, [.05, .95]))
D['blk'] = D.dia + '_' + D.hora.astype(str)
def row(df, name):
    s2 = df.sort_values('pnl', ascending=False).iloc[2:]
    lo, hi = boot(df, 'fin'); blo, bhi = boot(df, 'blk')
    pd_ = df.groupby('dia').apply(lambda g: ev(g), include_groups=False)
    return dict(celda=name, n=len(df), gan=int(df.gana.sum()), hit=df.gana.mean(), precio=df.coste.sum() / df.acc.sum(), eur=df.coste.sum(), pnl=df.pnl.sum(), EV=ev(df),
                ic_cierre=f'({lo:+.2f},{hi:+.2f})', ic_blk=f'({blo:+.2f},{bhi:+.2f})', EV_sin2=ev(s2), dias='/'.join(f'{v:+.2f}' for v in pd_.values), n_dias=len(pd_))
print(f"=== B real (H47-B), posiciones on-chain con tanda_B: n={len(D)}, ganadas {int(D.gana.sum())}, {D.dia.min()}..{D.dia.max()}, fills {pd.to_datetime(D.t_fill.min(),unit='s')}..{pd.to_datetime(D.t_fill.max(),unit='s')}")
tot = row(D, 'TOTAL'); print(pd.DataFrame([tot]).round(3).to_string(index=False))
out = []
for dim in PRE + POSTD:
    for v, g in D.groupby(dim):
        r = row(g, f'{dim}={v}'); r['dim'] = dim; r['post'] = dim in POSTD; out.append(r)
C = pd.DataFrame(out)
# max-estadistico: diferencia EV celda - resto, permutando pnl/coste/gana juntos dentro de dia (las posiciones conservan su precio: permutamos el desenlace)
def diffs(win, M):
    pnl = D.acc.values * win - D.coste.values; c = D.coste.values; out = []
    for m in M:
        a = pnl[m].sum() / c[m].sum(); b = pnl[~m].sum() / c[~m].sum(); out.append(a - b)
    return np.array(out)
cand = C[(~C.post) & (C.n >= 15) & (C.n <= len(D) - 15)].copy()
M = np.array([(D[c.split('=', 1)[0]].astype(str) == c.split('=', 1)[1]).values for c in cand.celda])
obs = diffs(D.gana.values, M)
# estandarizar por la sd de la permutacion de cada celda
r = np.random.default_rng(7); NP = 3000; perm = np.zeros((NP, len(M)))
dias = D.dia.values; idx_by = {d: np.where(dias == d)[0] for d in np.unique(dias)}
for k in range(NP):
    w = D.gana.values.copy()
    for d, ix in idx_by.items(): w[ix] = w[r.permutation(ix)]
    perm[k] = diffs(w, M)
sd = perm.std(0); z = obs / sd; zmax = np.abs(perm / sd).max(1)
cand['diff_vs_resto'] = obs; cand['z'] = z; cand['p_marg'] = [(np.abs(perm[:, j] / sd[j]) >= abs(z[j])).mean() for j in range(len(z))]
cand['p_familiar'] = [(zmax >= abs(zz)).mean() for zz in z]
o = np.argsort(cand.p_marg.values); m = len(o); bh = np.zeros(m); prev = 1
for rank, j in enumerate(o[::-1]):
    k = m - rank; prev = min(prev, cand.p_marg.values[j] * m / k); bh[j] = prev
cand['q_BH'] = bh
C = C.merge(cand[['celda', 'diff_vs_resto', 'z', 'p_marg', 'p_familiar', 'q_BH']], on='celda', how='left')
cols = ['celda', 'n', 'gan', 'hit', 'precio', 'eur', 'pnl', 'EV', 'ic_cierre', 'ic_blk', 'EV_sin2', 'dias', 'diff_vs_resto', 'p_marg', 'p_familiar', 'q_BH']
for dim in PRE + POSTD:
    print(f'\n--- {dim}' + (' (POST-relleno, descriptivo, NO accionable)' if dim in POSTD else ''))
    print(C[C.dim == dim][cols].round(3).to_string(index=False))
print(f'\nFamilia max-estadistico: {len(cand)} celdas pre-relleno con 15<=n<=n-15; permutaciones {NP} dentro de dia.')
print(cand.sort_values('p_marg')[['celda', 'n', 'EV', 'diff_vs_resto', 'p_marg', 'p_familiar', 'q_BH']].head(12).round(3).to_string(index=False))
# placebo: cuantas celdas con p_marg<0.05 cabe esperar por azar (numero esperado = 0.05*m) y distribucion en permutaciones
pm = np.array([[(np.abs(perm[:, j] / sd[j]) >= abs(perm[k, j] / sd[j])).mean() for j in range(len(M))] for k in range(0, NP, 30)])
print(f'Placebo: celdas con p_marg<0.05 observadas {int((cand.p_marg < .05).sum())}; en {pm.shape[0]} permutaciones: media {np.mean((pm < .05).sum(1)):.2f}, p95 {np.percentile((pm < .05).sum(1), 95):.0f}')
# seleccion adversa: rellenas vs no rellenas
print('\n--- Contrafactico: pujas rellenas vs NO rellenas (acierto del lado pujado; pujas.csv)')
U['tercio_t'] = pd.cut(U.fin.rank(method='first'), 3, labels=['1', '2', '3']).astype(str)
for dim in ['coin', 'dia', 'tercio_t']:
    t = U.groupby([dim, 'relleno']).agg(n=('gana', 'size'), hit=('gana', 'mean'), p_post=('p_post', 'mean')).unstack(); print(t.round(3).to_string())
# FV calibracion
print('\n--- FV naive (Phi(dist/(vol60*sqrt(T/60))), sin calibrar) por cuartil: hit vs precio vs fv')
D['fvq'] = pd.qcut(D.fv, 4)
print(D.groupby('fvq', observed=True).agg(n=('gana', 'size'), hit=('gana', 'mean'), precio=('precio', 'mean'), fv=('fv', 'mean'), EV=('pnl', 'sum'), c=('coste', 'sum')).assign(EV=lambda x: x.EV / x.c).round(3).to_string())
D.to_csv('pos_anotado.csv', index=False)
