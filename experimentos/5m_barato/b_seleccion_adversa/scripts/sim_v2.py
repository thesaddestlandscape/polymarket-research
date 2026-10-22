#!/usr/bin/env python3
"""sim_v2.py S OUTDIR DIA... -- simulador de B con LIBRO REAL (registro ms, q) para dias con ms_DIA.npz:
precio de puja = objetivo_h35 (top bid - k ticks, k: ETH 2, SOL/XRP 1; en banda (0,11;0,30], < ask), lado = primera cara cuyo top entra en banda (pegajoso),
repeg cada 5 s, T 295..65, relleno 'cons' = operacion en cinta on-chain del lado con pc < p (casado = ts-2,4) en (t+0,1; t+5,1].
Guarda M x K: p, bb, ba, bs, as, b15 y sus cambios, minpc (lado), minpc_opp (lado contrario), rasgos de cinta/Binance como sim_tape."""
import sys, os
S, OUT = sys.argv[1], sys.argv[2]; DAYS = sys.argv[3:]
sys.path.insert(0, S); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
from datetime import date, timedelta
from npbt import load_bt_np, px_np
from fills_loader import all_fills, COINS
K = 47; TK = 295 - 5 * np.arange(K); CAS = 2.4; MS = '/root/polymarket-research-datalogs/sa_ms/'
for d in DAYS:
    of = f'{OUT}/simv2_{d}.npz'
    if os.path.exists(of): print(d, 'ya'); continue
    z = np.load(MS + f'ms_{d}.npz', allow_pickle=True); toks = z['tokens']
    meta = pd.DataFrame(z['tmap'], columns=['act', 'marco', 'mid', 'fin', 'lado']); meta['finE'] = pd.to_datetime(meta.fin, utc=True).astype('int64') // 10**9; meta['mid'] = meta.mid.astype(np.int64)
    qk, qt = z['q_k'], z['q_t'] + int(z['t0']); qv = [z['q_v%d' % j] for j in range(4)]; bounds = np.searchsorted(qk, np.arange(len(toks) + 1))
    t5 = {(r.mid, r.lado): i for i, r in enumerate(meta.itertuples()) if r.marco == '5min'}
    t15 = {(r.act, r.finE, r.lado): i for i, r in enumerate(meta.itertuples()) if r.marco == '15min'}
    def book(i, tms):   # (bb, ba, bs, as) en cada t (ms) para el token i; NaN si no hay
        a, b = bounds[i], bounds[i + 1]
        j = np.searchsorted(qt[a:b], tms, side='right') - 1; ok = j >= 0; jj = np.where(ok, a + j, 0)
        return [np.where(ok, v[jj], np.nan) for v in qv]
    F = all_fills(d, S); F['tc'] = F.ts - CAS
    dd = [x for x in [(date.fromisoformat(d) - timedelta(1)).isoformat(), d, (date.fromisoformat(d) + timedelta(1)).isoformat()] if '2026-10-08' <= x <= '2026-10-22']
    bt = load_bt_np(dd); g0 = int(pd.Timestamp(d).timestamp()) - 7200; grid = np.arange(g0, g0 + 86400 + 4 * 3600).astype(float); G = {}
    for a in COINS:
        mid = px_np(bt[a], grid, stale=600); lr = np.log(mid); r10 = np.r_[np.full(10, np.nan), lr[10:] - lr[:-10]]
        G[a] = (mid, pd.Series(r10 ** 2).rolling(1800, min_periods=600).mean().values / 10.0)
    def at(arr, t): return arr[np.clip((np.floor(t) - g0).astype(np.int64), 0, len(grid) - 1)]
    F = F[F.des.notna()].sort_values(['mkt', 'tc']); mk = F.mkt.values; cuts = np.flatnonzero(np.r_[True, mk[1:] != mk[:-1], True])
    names = ['p', 'bb', 'ba', 'bs', 'as_', 'b15', 'b15_30', 'b15_5', 'a15', 'minpc', 'minpc_opp', 'dp10', 'dp30', 'sh30', 'flow60', 'z', 'ret10', 'sig', 'lastage', 'bb30', 'bb5']
    M = {k: [] for k in names}; rec = {k: [] for k in ['dia', 'act', 'mkt', 'fin', 'win', 'side']}
    for ci in range(len(cuts) - 1):
        f = F.iloc[cuts[ci]:cuts[ci + 1]]; mid_ = int(f.mkt.iloc[0]); act = f.act.iloc[0]; fin = float(f.fin.iloc[0]); des = f.des.iloc[0]
        iy, in_ = t5.get((mid_, 'YES')), t5.get((mid_, 'NO'))
        if iy is None or in_ is None: continue
        tk = fin - TK; tms = tk * 1000
        by = book(iy, tms); bn = book(in_, tms)
        def band(bb): return np.isfinite(bb) & (bb > 0.11 + 1e-9) & (bb <= 0.30 + 1e-9)
        cy, cn = band(by[0]), band(bn[0])
        if not (cy | cn).any(): continue
        first = np.argmax(cy | cn); sgn = 1 if cy[first] else -1; bk = by if sgn > 0 else bn
        bb, ba, bs, as_ = bk
        kk = 2 if act == 'ETH' else 1
        b = np.round(np.nan_to_num(bb, nan=0) * 1000).astype(int); a_ = np.round(np.nan_to_num(ba, nan=9) * 1000).astype(int)
        o = np.where(b % 10 == 0, b - kk * 10, (b // 10 - (kk - 1)) * 10)
        ok = band(bb) & (o >= 100) & (o <= 300) & (o < b) & (o < a_); p = np.where(ok, o / 1000.0, np.nan)
        # 15m del mismo lado
        f15 = int(np.ceil(fin / 900.0) * 900); i15 = t15.get((act, f15, 'YES' if sgn > 0 else 'NO'))
        if i15 is not None:
            b15 = book(i15, tms); b15_30 = book(i15, tms - 30000)[0]; b15_5 = book(i15, tms - 5000)[0]; bb15, a15 = b15[0], b15[1]
        else: bb15 = b15_30 = b15_5 = a15 = np.full(K, np.nan)
        bb30 = book(iy if sgn > 0 else in_, tms - 30000)[0]; bb5 = book(iy if sgn > 0 else in_, tms - 5000)[0]
        tc = f.tc.values; pyes = f.pyes.values; pc = f.pc.values; lc = f.lado_c.values == 'YES'; shs = f.sh.values; fl = f.flow_yes.values
        qall = pyes if sgn > 0 else 1 - pyes
        sidem = lc == (sgn > 0); tcs, pcs = tc[sidem], pc[sidem]; tco, pco = tc[~sidem], pc[~sidem]
        minpc = np.full(K, np.inf); minpo = np.full(K, np.inf); sh30 = np.zeros(K); flow60 = np.full(K, np.nan); lastage = np.full(K, np.nan)
        idx = np.searchsorted(tc, tk, side='right') - 1
        for k in range(K):
            a1, b1 = np.searchsorted(tcs, [tk[k] + 0.1, tk[k] + 5.1], side='right')
            if b1 > a1: minpc[k] = pcs[a1:b1].min()
            a1, b1 = np.searchsorted(tco, [tk[k] + 0.1, tk[k] + 5.1], side='right')
            if b1 > a1: minpo[k] = pco[a1:b1].min()
            a2, b2 = np.searchsorted(tc, [tk[k] - 60, tk[k]], side='right')
            if b2 > a2:
                flow60[k] = (fl[a2:b2].sum() * sgn) / max(shs[a2:b2].sum(), 1e-9); a3 = np.searchsorted(tc, tk[k] - 30, side='right'); sh30[k] = shs[a3:b2].sum()
            if idx[k] >= 0: lastage[k] = tk[k] - tc[idx[k]]
        def qat(t):
            i = np.searchsorted(tc, t, side='right') - 1; q = np.where(i >= 0, pyes[np.clip(i, 0, None)], np.nan); return q if sgn > 0 else 1 - q
        q0 = qat(tk); dp10 = q0 - qat(tk - 10); dp30 = q0 - qat(tk - 30)
        mid, s2 = G[act]; S_now = at(mid, tk); S_10 = at(mid, tk - 10); st = fin - 300
        ref = np.nanmean(at(mid, np.arange(st - 62, st - 2))); var = at(s2, tk); zv = np.log(S_now / ref) / np.sqrt(var * TK)
        vals = dict(p=p, bb=bb, ba=ba, bs=bs, as_=as_, b15=bb15, b15_30=b15_30, b15_5=b15_5, a15=a15, minpc=minpc, minpc_opp=minpo, dp10=dp10, dp30=dp30, sh30=sh30, flow60=flow60,
                    z=sgn * zv, ret10=sgn * np.log(S_now / S_10) * 1e4, sig=np.sqrt(var) * 1e4, lastage=lastage, bb30=bb30, bb5=bb5)
        for k_ in names: M[k_].append(vals[k_])
        rec['dia'].append(d); rec['act'].append(act); rec['mkt'].append(mid_); rec['fin'].append(fin); rec['win'].append((des == 'YES') == (sgn > 0)); rec['side'].append(sgn)
    np.savez_compressed(of, **{k: np.array(v) for k, v in rec.items()}, **{k: np.array(v) for k, v in M.items()})
    print(d, 'mercados', len(rec['mkt']), flush=True)
