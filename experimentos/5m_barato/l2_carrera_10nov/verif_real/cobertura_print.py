import sys, glob, numpy as np, pandas as pd
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'; sys.path.insert(0, P2 + 'escalera_B'); import engine as G
H = __file__.rsplit('/', 1)[0] + '/'
R = pd.read_pickle(H + 'out/R_all.pkl'); R = R[R.real_fill == 1]
res = []
for d, g in R.groupby('dia'):
    D = G.DayEng(d, 'ws').D
    for r in g.itertuples():
        k = int(r.k); L = r.L; row = dict(oid=r.oid, dia=d)
        for X in (250, 1000, 3000):
            pr = D.prints(k, L, r.t_ini, r.t_fuera + X); row[f'c{X}'] = bool([x for x in pr if x[3] == 1]); row[f'a{X}'] = bool(pr)
        # a la cinta: ts de mismo hash que el propio print (anchor) -> distancia a t_fuera
        row['own_vs_fuera'] = r.t_own_print - r.t_fuera; row['own_vs_ini'] = r.t_own_print - r.t_ini; row['src'] = r.own_src
        res.append(row)
X = pd.DataFrame(res); print('n', len(X)); print(X[[c for c in X if c[0] in 'ca' and c[1:].isdigit()]].mean().round(3).to_dict())
print('anclas ws_match', int((X.src == 'ws_match').sum()), 'bloque', int((X.src == 'bloque').sum()))
print('own print - t_fuera (ms) ws_match:', X[X.src == 'ws_match'].own_vs_fuera.describe(percentiles=[.05,.5,.95]).round(0).to_dict())
print('own print - t_ini (ms):', X[X.src == 'ws_match'].own_vs_ini.describe(percentiles=[.05,.5,.95]).round(0).to_dict())
