#!/usr/bin/env python3
"""Red-team R2 (DISENO_RT.md): ordenes REALES de B (20-23 Oct, verdad on-chain por order_hash, ordenes_b.parquet) pasadas por el MISMO fill_segment
de la escalera G (cinta WS de capt.Day: prints propios incluidos -> OPT queda contaminado por auto-print; STRICT no). Uso: python3 -I rt_b.py > out/rt_b.log"""
import sys, numpy as np, pandas as pd, warnings; warnings.filterwarnings('ignore')
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
sys.path.insert(0, P2 + 'escalera_B'); import engine as G
O = pd.read_parquet('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.parquet')
rows = []
for d, od in O.groupby('dia'):
    E = G.DayEng(d, 'ws', None, None); D = E.D
    for r in od.itertuples():
        k = D.tokidx.get(str(r.tok))
        if k is None: rows.append((r.oid, 'sin_token') + (np.nan,) * 8); continue
        t0 = int(r.t_ini * 1000); t1 = int(r.t_fin * 1000); L = round(float(r.precio), 2); rem = float(r.size)
        bk = D.book(k, t0)
        pt, pp, ps = E.tape.get(k, L, t0, t1)
        strict = float(len(np.where(pp < L - G.TOLP)[0]) > 0)
        touch = float(len(np.where(np.abs(pp - L) <= G.TOLP)[0]) > 0)
        qb, _, why = E.run_segment(k, L, t0, t1, rem, 'BASE')
        # ask propio <= L durante la vida (libro no cruzado) en el libro grabado (que INCLUYE la orden de B)
        a, b = D.qb[k], D.qb[k + 1]; qt = D.qt[a:b]; i0 = np.searchsorted(qt, t0, side='right'); i1 = np.searchsorted(qt, t1, side='right')
        v0 = D.v0[a + i0:a + i1]; v1 = D.v1[a + i0:a + i1]
        cross = float(((v1 <= L + G.EPS) & (v1 > v0 + G.EPS)).any())
        bid_below = float((v0 < L - G.EPS).any())
        rows.append((r.oid, 'ok', strict, touch, float(qb > 1e-9), cross, bid_below, bk[0] if bk else np.nan, bk[1] if bk else np.nan, why))
    del E, D
S = pd.DataFrame(rows, columns=['oid', 'st', 'sim_strict', 'print_en_L', 'sim_base', 'ask_le_L', 'bid_bajo_L', 'bid_ini', 'ask_ini', 'why'])
X = O.merge(S, on='oid'); X = X[X.st == 'ok'].copy()
X['offc'] = np.clip(np.round((X.bid_ini - X.precio) * 100), -1, 3).fillna(-9).astype(int)
X['banda'] = pd.cut(X.precio, [0, 0.15, 0.20, 0.25, 0.30], labels=['<.15', '.15-.20', '.20-.25', '.25-.30'])
print('ordenes B con libro:', len(X), 'de', len(O), '| rellenos reales', int(X.fill.sum()))
def rate(x, c): return f'{x[c].mean():.3f}'
print('\n== Tasa de relleno por ORDEN: real vs simulada (STRICT = solo travesia; BASE = escalera G; "print en L" = cota con auto-print)')
for col in ('offc', 'banda', 'coin', 'dia'):
    for v, x in X.groupby(col, observed=True):
        print(f' {col}={v}: n {len(x)} real {rate(x, "fill")} | STRICT {rate(x, "sim_strict")} BASE {rate(x, "sim_base")} | print en L {rate(x, "print_en_L")}')
print(f' TOTAL: n {len(X)} real {rate(X, "fill")} | STRICT {rate(X, "sim_strict")} BASE {rate(X, "sim_base")} | print en L {rate(X, "print_en_L")}')
P = X.groupby('puja').agg(real=('fill', 'max'), st=('sim_strict', 'max'), ba=('sim_base', 'max'))
print(f' POR PUJA (n {len(P)}): real {P.real.mean():.3f} STRICT {P.st.mean():.3f} BASE {P.ba.mean():.3f}')
print('\n== Matriz real x BASE (ordenes) y EV de los rellenos reales segun el sim los vea o no (EV = sum pnl / sum coste, maker sin rebate)')
print(pd.crosstab(X.fill, X.sim_base).to_string())
F = X[X.fill == 1]
for lab, m in (('real y BASE lo ve', F.sim_base == 1), ('real y BASE NO lo ve', F.sim_base == 0), ('real, hubo travesia', F.sim_strict == 1), ('real, SIN travesia (solo toque/sin print)', F.sim_strict == 0)):
    z = F[m]; print(f' {lab}: n {len(z)} pnl {z.pnl.sum():+.2f} coste {z.coste.sum():.2f} EV {z.pnl.sum() / z.coste.sum() if z.coste.sum() > 0 else np.nan:+.3f} acierto {z.gana_lado.mean():.3f} precio medio {z.precio.mean():.3f}')
# bootstrap por cierre de la diferencia de EV (con travesia - sin travesia)
rng = np.random.default_rng(3); F = F.assign(tr=F.sim_strict == 1)
g = F.groupby(['cie', 'tr']).agg(p=('pnl', 'sum'), c=('coste', 'sum')).unstack(fill_value=0.0); n = len(g); B = []
for _ in range(4000):
    i = rng.integers(0, n, n); s = g.iloc[i].sum()
    if s[('c', True)] > 0 and s[('c', False)] > 0: B.append(s[('p', True)] / s[('c', True)] - s[('p', False)] / s[('c', False)])
print(f' dif EV (travesia - sin travesia) IC90 por cierre ({np.quantile(B, .05):+.3f},{np.quantile(B, .95):+.3f}), cierres {n}')
print('\n== Falsos positivos del sim (BASE rellena, real no):', int(((X.sim_base == 1) & (X.fill == 0)).sum()), '| de ellos con travesia', int(((X.sim_strict == 1) & (X.fill == 0)).sum()))
print('FIN')
