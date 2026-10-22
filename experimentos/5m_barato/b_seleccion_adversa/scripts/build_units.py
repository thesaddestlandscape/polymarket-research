#!/usr/bin/env python3
"""build_units.py S OUT  -- poblacion makers ETH/SOL/XRP 5m, celda pc in (0,10;0,30], T in (60;300] s (09-21 Oct), SIN nosotros.
Unidad = primeras 5 acciones por (maker, mercado, lado) [misma definicion que b_lecciones_wallets/scripts/first5.py].
Rasgos PREVIOS al primer relleno de la unidad, solo con informacion de bloques con ts_b <= ts - LAG (LAG=4 s; la hora de casado
es bloque-2,4 s +-1,5 s, asi que todo lo usado se caso >= ~1 s antes que nuestro relleno; nada sub-segundo):
  precio del lado (ultimo trade), cambios 5/30/60 s, maximo 60 s, precio a la apertura, actividad, flujo tomador neto,
  cuota de flujo de tomadoras 'informadas' (score de DIAS ANTERIORES), FV Binance (z con sigma realizada 30 min, todo Binance),
  y diagnosticos NO observables (score de la tomadora del propio relleno).
Entrada: pop_D.pkl (S, de b_lecciones_wallets/scripts/pop.py), fills_D.parquet (wallets_18oct) / alt_DD.csv + gmap (S)."""
import sys, os, json, gc
import numpy as np, pandas as pd
from datetime import date, timedelta
S = sys.argv[1]; OUT = sys.argv[2]
sys.path.insert(0, S)
from npbt import load_bt_np, px_np
from math import erf
EX = '0xe111180000d2663c0091e4f400237545b87b996b'; US = '0x659a40ff9920febc5a66836213040924343d297f'
CA = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/'
DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
LAG = 4.0
COINS = ('ETH', 'SOL', 'XRP')
def all_fills(d):
    if d <= '2026-10-18':
        F = pd.read_parquet(CA + f'fills_{d}.parquet', columns=['tx', 'is_tk', 'maker', 'taker', 'side', 'act', 'mkt', 'lado', 'fin', 'ts', 'maker_amt', 'taker_amt'])
        F = F[(F.is_tk == 0) & F.act.isin(COINS)].drop(columns=['is_tk'])
        F['mkt'] = F.mkt.astype(np.int64); F['des'] = F.mkt.astype(str).map(DES)
    else:
        gm = json.load(open(S + ('/gmap19.json' if d == '2026-10-19' else '/gmap.json')))
        tok = {}
        for slug, v in gm.items():
            st = int(slug.rsplit('-', 1)[1]); coin = slug.split('-')[0].upper()
            for t, l in zip(v['toks'], ('YES', 'NO')): tok[t] = (coin, int(v['id']), st + 300, l, v['des'])
        cols = ['tipo', 'bloque', 'ts', 'tx', 'li', 'oh', 'maker', 'taker', 'side', 'tok', 'maker_amt', 'taker_amt', 'fee']
        F = pd.read_csv(S + f'/alt_{d[8:]}.csv', header=None, names=cols, dtype={'tok': str, 'tx': str, 'maker': str, 'taker': str},
                        usecols=['tipo', 'ts', 'tx', 'maker', 'taker', 'side', 'tok', 'maker_amt', 'taker_amt'])
        F = F[(F.tipo == 'F') & (F.taker.str.lower() != EX) & F.tok.isin(tok.keys())].copy()
        F['maker'] = F.maker.str.lower(); F['taker'] = F.taker.str.lower()
        for i, c in enumerate(['act', 'mkt', 'fin', 'lado', 'des']): F[c] = F.tok.map(lambda t, i=i: tok[t][i])
        F = F.drop(columns=['tipo', 'tok'])
        F = F[F.act.isin(COINS)]
    v = F.side.values == 1
    F['sh'] = np.where(v, F.maker_amt, F.taker_amt); usd = np.where(v, F.taker_amt, F.maker_amt)
    F = F[F.sh > 0].copy(); usd = usd[F.index.isin(F.index)] if False else np.where(F.side.values == 1, F.taker_amt, F.maker_amt)
    ptok = usd / F.sh.values
    F['lado_c'] = np.where(F.side.values == 1, np.where(F.lado == 'YES', 'NO', 'YES'), F.lado)
    F['pyes'] = np.where(F.lado.values == 'YES', ptok, 1 - ptok)            # precio del YES implicado por el relleno
    pc = np.where(F.lado_c.values == 'YES', F.pyes.values, 1 - F.pyes.values)
    F['pc'] = pc; F['coste_m'] = F.sh.values * pc
    # flujo del TOMADOR hacia YES (acciones): el tomador toma la exposicion contraria a la del maker
    F['flow_yes'] = np.where(F.lado_c.values == 'NO', F.sh.values, -F.sh.values)
    F['pnl_m'] = np.where(F.des.isna(), np.nan, np.where(F.lado_c == F.des, F.sh, 0) - F.coste_m)
    F['ts'] = F.ts.astype(float)
    return F[['tx', 'maker', 'taker', 'act', 'mkt', 'fin', 'ts', 'sh', 'pyes', 'pc', 'coste_m', 'flow_yes', 'pnl_m', 'des', 'lado_c']]
def phi(x): return 0.5 * (1 + np.vectorize(erf)(x / np.sqrt(2)))
days = sys.argv[3:] or [(date(2026, 10, 9) + timedelta(i)).isoformat() for i in range(13)]
TK = None   # score acumulado de tomadoras con dias ANTERIORES: taker -> (pnl_t, cost_t, n)
for d in days:
    of = OUT + f'/units_{d}.pkl'
    F = all_fills(d)
    # --- stats de tomadoras de este dia (para dias posteriores)
    G = F[F.pnl_m.notna()]
    tk_day = pd.DataFrame({'taker': G.taker.values, 'pnl_t': -G.pnl_m.values, 'cost_t': (G.sh - G.coste_m).values}).groupby('taker').agg(pnl_t=('pnl_t', 'sum'), cost_t=('cost_t', 'sum'), n=('pnl_t', 'size'))
    if os.path.exists(of):
        TK = tk_day if TK is None else TK.add(tk_day, fill_value=0); print(d, 'ya hecho'); continue
    score = {} if TK is None else (TK[(TK.n >= 30) & (TK.cost_t >= 50)].eval('pnl_t/cost_t')).to_dict()
    F['inf'] = F.taker.map(score)            # NaN = sin historial suficiente
    # --- serie por mercado, ordenada (clave combinada)
    F = F.sort_values(['mkt', 'ts']).reset_index(drop=True)
    base = int(pd.Timestamp(d).timestamp()) - 7200
    mk_ids = {m: i for i, m in enumerate(F.mkt.unique())}
    F['mi'] = F.mkt.map(mk_ids).astype(np.int64)
    key = F.mi.values * 1e6 + (F.ts.values - base)
    cum_sh = np.concatenate([[0], np.cumsum(F.sh.values)]); cum_fl = np.concatenate([[0], np.cumsum(F.flow_yes.values)])
    infv = np.where(F.inf.values > 0.0, F.sh.values, 0.0); knv = np.where(F.inf.notna().values, F.sh.values, 0.0)
    cum_inf = np.concatenate([[0], np.cumsum(infv)]); cum_kn = np.concatenate([[0], np.cumsum(knv)])
    # numero de tx distintas: aproximado por filas con ts distinto
    newblk = np.r_[True, (np.diff(key) != 0)]; cum_blk = np.concatenate([[0], np.cumsum(newblk)])
    pyes = F.pyes.values; mi_arr = F.mi.values
    # --- unidades (primeras 5 acc) desde pop_D.pkl
    P = pd.read_pickle(S + f'/pop_{d}.pkl'); P = P[P.maker != US]
    P = P.sort_values(['maker', 'mkt', 'lado_c', 'ts'])
    P['cum'] = P.groupby(['maker', 'mkt', 'lado_c']).sh.cumsum(); P['prev'] = P.cum - P.sh
    P = P[P.prev < 5].copy(); take = np.minimum(P.sh, 5 - P.prev); f = take / P.sh
    P['coste_m'] = P.coste_m * f; P['pnl_m'] = P.pnl_m * f; P['sh'] = take
    U = P.groupby(['dia', 'maker', 'mkt', 'lado_c', 'act']).agg(c=('coste_m', 'sum'), p=('pnl_m', 'sum'), sh=('sh', 'sum'), T=('T', 'first'), pc=('pc', 'first'),
        fin=('fin', 'first'), gana=('gana', 'first'), ts=('ts', 'first'), taker=('taker', 'first'), b10=('bn_pre10x', 'first'), nf=('sh', 'size')).reset_index()
    U['mkt'] = U.mkt.astype(np.int64)
    U = U[U.mkt.isin(mk_ids)].copy()
    U['mi'] = U.mkt.map(mk_ids).astype(np.int64)
    sgn = np.where(U.lado_c.values == 'YES', 1.0, -1.0)
    t_obs = U.ts.values - LAG
    def idx_le(t):   # ultimo indice con key <= (mi, t) dentro del mismo mercado, -1 si no hay
        k = U.mi.values * 1e6 + (t - base); i = np.searchsorted(key, k, side='right') - 1
        ok = (i >= 0) & (mi_arr[np.clip(i, 0, None)] == U.mi.values); return np.where(ok, i, -1)
    def side_px(t):
        i = idx_le(t); p = np.where(i >= 0, pyes[np.clip(i, 0, None)], np.nan)
        return np.where(sgn > 0, p, 1 - p)
    def wsum(cum, t0, t1):
        i0 = idx_le(t0); i1 = idx_le(t1)
        lo = np.where(i0 >= 0, i0 + 1, np.searchsorted(key, U.mi.values * 1e6, side='left'))   # inicio del mercado si no hay nada antes
        hi = np.where(i1 >= 0, i1 + 1, lo)
        hi = np.maximum(hi, lo)
        return cum[hi] - cum[lo]
    p_now = side_px(t_obs)
    U['p_last'] = p_now
    U['gap_last'] = U.pc.values - p_now                       # <0: el precio bajo hasta nosotros
    for W in (5, 30, 60):
        U[f'dp{W}'] = p_now - side_px(t_obs - W)
    # maximo/minimo del lado en [t_obs-60, t_obs]
    i1 = idx_le(t_obs); i0 = idx_le(t_obs - 60)
    hi60 = np.full(len(U), np.nan); lo60 = np.full(len(U), np.nan)
    for j in range(len(U)):
        a, b = i0[j] + 1 if i0[j] >= 0 else None, i1[j]
        if b < 0: continue
        if a is None:
            a = np.searchsorted(key, U.mi.values[j] * 1e6, side='left')
        seg = pyes[a:b + 1] if b >= a else pyes[b:b + 1]
        s = seg if sgn[j] > 0 else 1 - seg
        hi60[j] = s.max(); lo60[j] = s.min()
    U['hi60'] = hi60 - U.pc.values; U['rng60'] = hi60 - lo60
    # precio a la apertura (primer trade con T<=300)
    st = U.fin.values - 300.0
    kst = U.mi.values * 1e6 + (st - base); io = np.searchsorted(key, kst, side='left')
    ok = (io < len(key)) & (mi_arr[np.clip(io, 0, len(key) - 1)] == U.mi.values) & (io <= np.where(i1 >= 0, i1, -1))
    po = np.where(ok, pyes[np.clip(io, 0, len(key) - 1)], np.nan)
    U['d_open'] = np.where(sgn > 0, po, 1 - po) - U.pc.values  # >0: el lado valia mas al abrir
    U['vol30'] = wsum(cum_sh, t_obs - 30, t_obs); U['blk30'] = wsum(cum_blk, t_obs - 30, t_obs)
    U['vol_all'] = wsum(cum_sh, st - 1, t_obs)
    fl = wsum(cum_fl, t_obs - 60, t_obs) * sgn; v60 = wsum(cum_sh, t_obs - 60, t_obs)
    U['flow60'] = np.where(v60 > 0, fl / np.maximum(v60, 1e-9), np.nan)     # >0: tomadores compraban NUESTRO lado
    kn = wsum(cum_kn, t_obs - 120, t_obs); iv = wsum(cum_inf, t_obs - 120, t_obs)
    U['inf120'] = np.where(kn > 0, iv / np.maximum(kn, 1e-9), np.nan)
    U['tk_score'] = U.taker.map(score)        # DIAGNOSTICO (no observable antes del relleno)
    # --- FV Binance
    dd = [x for x in [(date.fromisoformat(d) - timedelta(1)).isoformat(), d, (date.fromisoformat(d) + timedelta(1)).isoformat()] if '2026-10-08' <= x <= '2026-10-21']
    bt = load_bt_np(dd)
    fv = np.full(len(U), np.nan); zz = np.full(len(U), np.nan); sig = np.full(len(U), np.nan)
    for a in COINS:
        m = U.act.values == a
        if not m.any(): continue
        ts_, ms_ = bt[a]
        g0 = int(base); grid = np.arange(g0, g0 + 86400 + 4 * 3600)
        mid = px_np(bt[a], grid.astype(float), stale=600)
        lr = np.log(mid)
        r10 = lr[10:] - lr[:-10]; r10 = np.r_[np.full(10, np.nan), r10]
        s2 = pd.Series(r10 ** 2).rolling(1800, min_periods=600).mean().values / 10.0   # var por segundo
        def at(arr, t):
            i = np.clip((np.floor(t) - g0).astype(np.int64), 0, len(grid) - 1); return arr[i]
        ref = np.array([np.nanmean(at(mid, np.arange(s - 62, s - 2))) for s in st[m]])
        S_now = at(mid, t_obs[m]); var = at(s2, t_obs[m]); Tm = U.fin.values[m] - t_obs[m]
        z = np.log(S_now / ref) / np.sqrt(var * Tm)
        py = phi(z); fv[m] = np.where(sgn[m] > 0, py, 1 - py); zz[m] = z * sgn[m]; sig[m] = np.sqrt(var) * 1e4
    U['fv'] = fv; U['fv_gap'] = fv - U.pc.values; U['z'] = zz; U['sig_bps_s'] = sig
    U['hora'] = pd.to_datetime(U.ts - 2.4, unit='s').dt.hour
    U.drop(columns=['mi']).to_pickle(of)
    print(d, 'unidades', len(U), 'cob p_last', round(np.isfinite(p_now).mean(), 3), 'fv', round(np.isfinite(fv).mean(), 3), 'inf120', round(U.inf120.notna().mean(), 3),
          'EV', round(U.p.sum() / U.c.sum(), 4), flush=True)
    TK = tk_day if TK is None else TK.add(tk_day, fill_value=0)
    del F, P, U, bt; gc.collect()
print('ok')
