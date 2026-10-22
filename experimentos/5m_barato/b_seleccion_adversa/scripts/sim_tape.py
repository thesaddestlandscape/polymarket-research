#!/usr/bin/env python3
"""sim_tape.py S OUTDIR DIA [DIA...] -- simulador de pujas tipo B sobre la CINTA on-chain (sin libro), con contrafactico de NO rellenadas.
Por mercado (ETH/SOL/XRP 5m): lado barato fijado la 1a vez que q_last<=0.31 (o >=0.69 -> el otro lado); pasos cada 5 s con T in (60,300];
en cada paso se cotiza p = floor_cent(q_last_lado - delta*0.01) si p en [0.10,0.30]; relleno en el paso si hay una operacion del lado con
pc < p (conservador 'cons') o pc <= p ('opt') con hora de casado (ts-2.4) en (t+0.1, t+5.1]. Informacion de decision: solo operaciones con
casado <= t (nada posterior). Rasgos Binance: bookTicker por recepcion (precio mid, rejilla 1 s). Guarda npz por dia con matrices M x K."""
import sys, os
os.environ.setdefault('PYTHONDONTWRITEBYTECODE', '1')
S, OUT = sys.argv[1], sys.argv[2]; DAYS = sys.argv[3:]
sys.path.insert(0, S); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
from datetime import date, timedelta
from math import erf
from npbt import load_bt_np, px_np
from fills_loader import all_fills, COINS
K = 47; TK = 295 - 5 * np.arange(K)         # T restante al cotizar: 295..65 (paso 5 s)
DELTAS = (0, 1, 2, 3); CAS = 2.4
def phi(x): return 0.5 * (1 + np.vectorize(erf)(x / np.sqrt(2)))
for d in DAYS:
    of = f'{OUT}/sim_{d}.npz'
    if os.path.exists(of): print(d, 'ya'); continue
    F = all_fills(d, S); F['tc'] = F.ts - CAS
    dd = [x for x in [(date.fromisoformat(d) - timedelta(1)).isoformat(), d, (date.fromisoformat(d) + timedelta(1)).isoformat()] if '2026-10-08' <= x <= '2026-10-21']
    bt = load_bt_np(dd); base = int(pd.Timestamp(d).timestamp()) - 7200; g0 = base
    grid = np.arange(g0, g0 + 86400 + 4 * 3600).astype(float); G = {}
    for a in COINS:
        mid = px_np(bt[a], grid, stale=600); lr = np.log(mid); r10 = np.r_[np.full(10, np.nan), lr[10:] - lr[:-10]]
        G[a] = (mid, pd.Series(r10 ** 2).rolling(1800, min_periods=600).mean().values / 10.0)
    def at(arr, t): return arr[np.clip((np.floor(t) - g0).astype(np.int64), 0, len(grid) - 1)]
    rec = {k: [] for k in ['dia', 'act', 'mkt', 'fin', 'win', 'side']}
    mats = {k: [] for k in ['q', 'ok', 'minpc', 'dp10', 'dp30', 'dp60', 'dopen', 'hi60', 'v30', 'sh30', 'flow60', 'z', 'ret10', 'sig', 'lastage']}
    F = F[F.des.notna()].sort_values(['mkt', 'tc'])
    mk = F.mkt.values; cuts = np.flatnonzero(np.r_[True, mk[1:] != mk[:-1], True])
    for ci in range(len(cuts) - 1):
        sl = slice(cuts[ci], cuts[ci + 1]); f = F.iloc[sl]
        fin = float(f.fin.iloc[0]); st = fin - 300; act = f.act.iloc[0]; des = f.des.iloc[0]
        tc = f.tc.values; pyes = f.pyes.values; pc = f.pc.values; lc = f.lado_c.values == 'YES'; shs = f.sh.values; fl = f.flow_yes.values
        tk = fin - TK                                    # instante de cotizar
        idx = np.searchsorted(tc, tk, side='right') - 1  # ultima operacion con casado <= tk
        def qat(t, sgn):
            i = np.searchsorted(tc, t, side='right') - 1; p = np.where(i >= 0, pyes[np.clip(i, 0, None)], np.nan)
            return np.where(sgn > 0, p, 1 - p)
        qy = qat(tk, 1)
        cheap = np.where(qy <= 0.31, 1, np.where(qy >= 0.69, -1, 0))   # +1: YES barato, -1: NO barato
        if not (cheap != 0).any(): continue
        sgn = cheap[np.argmax(cheap != 0)]               # lado fijado la primera vez
        q = qat(tk, sgn); q10 = qat(tk - 10, sgn); q30 = qat(tk - 30, sgn); q60 = qat(tk - 60, sgn)
        io = np.searchsorted(tc, st, side='left'); qo = np.nan
        if io < len(tc): qo = pyes[io] if sgn > 0 else 1 - pyes[io]
        side_f = (lc == (sgn > 0))                      # operaciones del lado elegido (el maker puja ese lado)
        tcs = tc[side_f]; pcs = pc[side_f]
        minpc = np.full(K, np.inf); hi60 = np.full(K, np.nan); v30 = np.zeros(K); sh30 = np.zeros(K); flow60 = np.full(K, np.nan); lastage = np.full(K, np.nan)
        qall = pyes if sgn > 0 else 1 - pyes
        for k in range(K):
            a, b = np.searchsorted(tcs, [tk[k] + 0.1, tk[k] + 5.1], side='right')
            if b > a: minpc[k] = pcs[a:b].min()
            a2, b2 = np.searchsorted(tc, [tk[k] - 60, tk[k]], side='right')
            if b2 > a2:
                hi60[k] = qall[a2:b2].max(); s60 = shs[a2:b2].sum(); flow60[k] = (fl[a2:b2].sum() * sgn) / max(s60, 1e-9)   # >0: tomadores compran nuestro lado
                a3 = np.searchsorted(tc, tk[k] - 30, side='right'); v30[k] = b2 - a3; sh30[k] = shs[a3:b2].sum()
            if idx[k] >= 0: lastage[k] = tk[k] - tc[idx[k]]
        mid, s2 = G[act]; S_now = at(mid, tk); S_10 = at(mid, tk - 10)
        ref = np.nanmean(at(mid, np.arange(st - 62, st - 2)))
        var = at(s2, tk); zv = np.log(S_now / ref) / np.sqrt(var * TK)
        win = (des == 'YES') == (sgn > 0)
        rec['dia'].append(d); rec['act'].append(act); rec['mkt'].append(f.mkt.iloc[0]); rec['fin'].append(fin); rec['win'].append(win); rec['side'].append(sgn)
        mats['q'].append(q); mats['minpc'].append(minpc); mats['dp10'].append(q - q10); mats['dp30'].append(q - q30); mats['dp60'].append(q - q60)
        mats['dopen'].append(q - qo); mats['hi60'].append(hi60 - q); mats['v30'].append(v30); mats['sh30'].append(sh30); mats['flow60'].append(flow60)
        mats['z'].append(sgn * zv); mats['ret10'].append(sgn * np.log(S_now / S_10) * 1e4); mats['sig'].append(np.sqrt(var) * 1e4)
        mats['lastage'].append(lastage); mats['ok'].append(np.isfinite(q))
    np.savez_compressed(of, **{k: np.array(v) for k, v in rec.items()}, **{k: np.array(v) for k, v in mats.items()}, TK=TK)
    print(d, 'mercados', len(rec['mkt']), flush=True)
    del F, bt; import gc; gc.collect()
print('ok')
