#!/usr/bin/env python3
"""attach_ms.py S -- une a las unidades de poblacion (datos/units, dias con registro ms) los rasgos del libro WS (q) del token 5m del lado,
del token 15m del mismo lado/coin (bid 15m), spread, tamanos top, profundidad en ticks de la puja bajo el top, vol30 por WS y desviacion Binance-Chainlink.
Todo en t_obs = ts - 4 s (misma regla que build_units). Salida datos/ms_units.pkl."""
import sys, os, glob, json
S = sys.argv[1]; sys.path.insert(0, S); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
from datetime import date, timedelta
from npbt import load_bt_np, px_np
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); MS = '/root/polymarket-research-datalogs/sa_ms/'
LAG = 4.0; out = []
def cl_series(days):
    T = {a: [] for a in ('ETH', 'SOL', 'XRP')}; P = {a: [] for a in T}
    for d in days:
        f = f'/root/polymarket-research/data/prices/chainlink_{d}.csv'
        if not os.path.exists(f): continue
        c = pd.read_csv(f, usecols=['timestamp_utc', 'asset', 'price_usd', 'source']); c = c[(c.source == 'chainlink') & c.asset.isin(T)]
        ts = pd.to_datetime(c.timestamp_utc, utc=True).astype('int64').values / 1e9
        for a in T: m = (c.asset == a).values; T[a].append(ts[m]); P[a].append(c.price_usd.values[m])
    return {a: (np.concatenate(T[a]), np.concatenate(P[a])) for a in T}
for f in sorted(glob.glob(B + '/datos/units/units_*.pkl')):
    d = f[-14:-4]
    if not os.path.exists(MS + f'ms_{d}.npz'): continue
    U = pd.read_pickle(f); z = np.load(MS + f'ms_{d}.npz', allow_pickle=True)
    toks = z['tokens']; tmap = z['tmap']
    meta = pd.DataFrame(tmap, columns=['act', 'marco', 'mid', 'fin', 'lado']); meta['finE'] = pd.to_datetime(meta.fin, utc=True).astype('int64') // 10**9; meta['mid'] = meta.mid.astype(np.int64)
    qk = z['q_k']; qt = z['q_t'] + int(z['t0']); qv = [z['q_v%d' % j] for j in range(4)]
    # indices por token (q ordenado por k,t)
    bounds = np.searchsorted(qk, np.arange(len(toks) + 1)); tk5 = {(r.mid, r.lado): i for i, r in enumerate(meta.itertuples()) if r.marco == '5min'}
    tk15 = {(r.act, r.finE, r.lado): i for i, r in enumerate(meta.itertuples()) if r.marco == '15min'}
    def at(i, t_ms):   # ultimo estado q del token i con t <= t_ms
        a, b = bounds[i], bounds[i + 1]
        j = np.searchsorted(qt[a:b], t_ms, side='right') - 1
        return (a + j) if j >= 0 else -1
    n = len(U); cols = {k: np.full(n, np.nan) for k in ['bb', 'ba', 'bs', 'as_', 'qage', 'bb30', 'bb5', 'b15', 'b15_30', 'b15_5', 'a15', 'vol30ws', 'cl_dev']}
    tobs = U.ts.values - LAG; sg = np.where(U.lado_c.values == 'YES', 1, -1)
    has5 = np.zeros(n, bool)
    for r in range(n):
        u = U.iloc[r] if False else None
    mids = U.mkt.values.astype(np.int64); lc = U.lado_c.values; act = U.act.values; fin = U.fin.values
    for r in range(n):
        i5 = tk5.get((mids[r], lc[r]))
        if i5 is None: continue
        tm = tobs[r] * 1000
        j = at(i5, tm)
        if j < 0: continue
        has5[r] = True
        cols['bb'][r], cols['ba'][r], cols['bs'][r], cols['as_'][r] = qv[0][j], qv[1][j], qv[2][j], qv[3][j]; cols['qage'][r] = (tm - qt[j]) / 1000
        for nm, dt in (('bb30', 30), ('bb5', 5)):
            j2 = at(i5, tm - dt * 1000)
            if j2 >= 0: cols[nm][r] = qv[0][j2]
        f15 = int(np.ceil(fin[r] / 900.0) * 900); i15 = tk15.get((act[r], f15, lc[r]))
        if i15 is not None:
            j3 = at(i15, tm)
            if j3 >= 0:
                cols['b15'][r] = qv[0][j3]; cols['a15'][r] = qv[1][j3]
                for nm, dt in (('b15_30', 30), ('b15_5', 5)):
                    j4 = at(i15, tm - dt * 1000)
                    if j4 >= 0: cols[nm][r] = qv[0][j4]
    # vol30 por WS: trades t de ambos tokens del mercado, por evento
    tt = z['t_t'] + int(z['t0']); tk_ = z['t_k']; tsz = z['t_sz']
    mk_of_tok = {i: (r.mid) for i, r in enumerate(meta.itertuples()) if r.marco == '5min'}
    mkt_arr = np.array([mk_of_tok.get(k, -1) for k in tk_]); o = np.lexsort((tt, mkt_arr)); mkt_s, t_s, sz_s = mkt_arr[o], tt[o], tsz[o]
    cs = np.concatenate([[0], np.cumsum(sz_s)]); key = mkt_s.astype(np.float64) * 1e13 + t_s
    kq = mids.astype(np.float64) * 1e13
    i1 = np.searchsorted(key, kq + tobs * 1000, side='right'); i0 = np.searchsorted(key, kq + (tobs - 30) * 1000, side='right'); cols['vol30ws'] = cs[i1] - cs[i0]
    # Binance - Chainlink
    dd = [x for x in [(date.fromisoformat(d) - timedelta(1)).isoformat(), d, (date.fromisoformat(d) + timedelta(1)).isoformat()] if '2026-10-08' <= x <= '2026-10-22']
    bt = load_bt_np(dd); cl = cl_series(dd)
    for a in ('ETH', 'SOL', 'XRP'):
        m = act == a
        if not m.any(): continue
        sb = px_np(bt[a], tobs[m], stale=60); ct, cp = cl[a]; ic = np.searchsorted(ct, tobs[m], side='right') - 1; sc = np.where(ic >= 0, cp[np.clip(ic, 0, None)], np.nan)
        cols['cl_dev'][m] = sg[m] * (sb / sc - 1) * 1e4
    V = U.copy()
    for k, v in cols.items(): V[k] = v
    V['has5'] = has5; out.append(V); print(d, 'unidades', n, 'con libro 5m', has5.mean().round(3), 'con 15m', np.isfinite(cols['b15']).mean().round(3), flush=True)
V = pd.concat(out, ignore_index=True)
V['spread'] = V.ba - V.bb; V['depth_ticks'] = (V.bb - V.pc) / 0.01; V['imb'] = V.bs / (V.bs + V.as_); V['lbs'] = np.log1p(V.bs)
V['dbb30'] = V.bb - V.bb30; V['dbb5'] = V.bb - V.bb5; V['d15_30'] = V.b15 - V.b15_30; V['d15_5'] = V.b15 - V.b15_5; V['lvl15'] = V.b15 - V.pc; V['gap15'] = V.b15 - V.bb
V.to_pickle(B + '/datos/ms_units.pkl'); print(len(V), 'filas guardadas')
