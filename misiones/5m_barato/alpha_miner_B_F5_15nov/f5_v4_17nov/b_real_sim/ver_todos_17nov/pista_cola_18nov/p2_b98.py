#!/usr/bin/env python3
"""p2_b98.py (RE-B-COLA-CANCELA, MECANISMO): masa delante cancelada EXACTA por relleno de B 20-23 Oct.
cancelada = cola al colocar (tomador_202.cola) - sum taker_amt de fills on-chain side=0 en (tok,L) de OTROS makers antes del nuestro
(bloque anterior, o mismo bloque con log_index menor) y con bloque > t_ini + {1,4 ; 3,8} s. Proxy M3 (cota ex post, NO M3)."""
import pandas as pd, numpy as np, json, os
H = os.path.dirname(os.path.abspath(__file__)) + '/../'; OWN = '0x659a40ff9920febc5a66836213040924343d297f'
T = pd.read_pickle(H + 'tomador_202.pkl'); M = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '/out/b202_onchain.csv.gz', dtype={'token_id': str, 'maker': str, 'tx': str})
M = M[(M.tipo == 'F') & (M.side == 0)].copy(); M['token_id'] = M.token_id.astype(str); M['maker'] = M.maker.str.lower()
M['p'] = (M.maker_amt / M.taker_amt).round(2); G = {k: g for k, g in M.groupby(['token_id', 'p'])}
T['cl'] = T.causa.str.split('(').str[0]; out = []
for r in T.itertuples():
    g = G.get((str(r.tok), round(r.L, 2)))
    if g is None: out.append(dict(oid=r.oid, ok=False)); continue
    own = g[(g.tx == r.tx) & (g.maker == OWN)]
    if own.empty: out.append(dict(oid=r.oid, ok=False)); continue
    ts0, li0, b0 = own.ts_est.iloc[0], own.log_index.min(), own.bloque.iloc[0]
    oth = g[(g.maker != OWN) & ((g.bloque < b0) | ((g.bloque == b0) & (g.log_index < li0)))]
    d = {}
    for nm, off in (('lo', 1.4), ('hi', 3.8)):
        pr = oth[oth.ts_est > r.t_ini / 1000 + off].taker_amt.sum(); d['prev_' + nm] = pr
        d['canc_' + nm] = max(0.0, r.cola - pr) if r.cola == r.cola else np.nan
    d['prev_mismo_tx'] = oth[oth.tx == r.tx].taker_amt.sum()
    pnl = r.real_q * ((1.0 if r.gana == 1 else 0.0) - r.L); cost = r.real_q * r.L
    out.append(dict(oid=r.oid, ok=True, cl=r.cl, coin=r.coin, dia=r.dia, cola=r.cola, n_mk=r.n_mk, pnl=pnl, cost=cost, **d))
O = pd.DataFrame(out); O.to_pickle(os.path.dirname(os.path.abspath(__file__)) + '/out/p2_b98.pkl')
res = {'n': len(O), 'unidos': int(O.ok.sum())}
O = O[O.ok]
for nm, s in (('clase1', O.cl == '1_propio_solo'), ('resto', O.cl != '1_propio_solo'), ('n_mk1', O.n_mk == 1), ('n_mk2+', O.n_mk >= 2)):
    x = O[s]; xc = x[x.cola > 0]; r_ = dict(n=len(x), cola_gt0=len(xc))
    for b in ('lo', 'hi'):
        fr = xc['canc_' + b] / xc.cola
        r_[b] = dict(frac_canc_gt0=round(float((xc['canc_' + b] > 1e-6).mean()), 3), frac_canc_ge50=round(float((fr >= .5).mean()), 3),
                     mediana_frac=round(float(fr.median()), 3), mediana_cola=float(xc.cola.median()), mediana_prev=float(xc['prev_' + b].median()))
    res[nm] = r_
# cota ex post M3 (NO M3: el disparo ex ante no es observable sin L2 20-23 Oct): rellenos con >=50% de la cola delante cancelada
for b in ('lo', 'hi'):
    xc = O[O.cola > 0]; s = (xc['canc_' + b] / xc.cola) >= .5
    res['proxyM3_' + b] = dict(n_marcados=int(s.sum()), pnl_marcados=round(float(xc[s].pnl.sum()), 2), coste_marcados=round(float(xc[s].cost.sum()), 2),
        ev_eur_marcados=round(float(xc[s].pnl.sum() / xc[s].cost.sum()), 3), n_resto=int((~s).sum()), ev_eur_resto=round(float(xc[~s].pnl.sum() / xc[~s].cost.sum()), 3),
        buenos_perdidos_eur=round(float(xc[s & (xc.pnl > 0)].pnl.sum()), 2), malos_evitados_eur=round(float(-xc[s & (xc.pnl < 0)].pnl.sum()), 2),
        por_dia={k: [int(len(v)), round(float(v.pnl.sum()), 2)] for k, v in xc[s].groupby('dia')})
print(json.dumps(res, indent=1, default=str))
