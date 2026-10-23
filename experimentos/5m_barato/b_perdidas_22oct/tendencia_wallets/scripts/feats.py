#!/usr/bin/env python3
"""feats.py -- PREREG W1 (sha 303c2090...). Indicadores causales orientados al lado comprado.
Uso: feats.py  -> escribe ../datos/feats_pop.csv.gz, feats_b.csv.gz, feats_wal.csv.gz
t0: poblacion/wallets = ts_chain - 5 s ; B = t_det - 4 s (o primer_fill_chain - 5 s [flag])."""
import os, sys, glob, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); DAT = os.path.join(AQ, '..', 'datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'PREREG.md'), 'rb').read()).hexdigest().startswith('303c2090')
SAL = os.path.join(AQ, '..', '..', 'salida', 'datos'); CP = os.path.join(AQ, '..', '..', 'cola_posicion', 'datos'); PH = os.path.join(AQ, '..', '..', 'pares_huecos', 'datos')
SYM = {'ETH': 0, 'SOL': 1, 'XRP': 2}; BIG = 1 << 40
WALLETS = ['0xf074dc84', '0x0ab01745']

class Dia:
    def __init__(s, d):
        z = np.load(os.path.join(SAL, f'ms_{d}.npz'), allow_pickle=False)
        s.D0 = int(z['D0']); s.qr = z['qr'].astype(np.int64); s.qk = z['qk'].astype(np.int64); s.qv = z['qv']
        s.tr = z['tr'].astype(np.int64); s.tk = z['tk'].astype(np.int64); s.tv = z['tv']; s.xr = z['xr'].astype(np.int64); s.xk = z['xk'].astype(np.int64); s.xv = z['xv']
        # qr/tr/xr son offsets respecto a D0 (ms)
        s.qkey = s.qk * BIG + s.qr; s.tkey = s.tk * BIG + s.tr; s.xkey = s.xk * BIG + s.xr
        assert np.all(np.diff(s.qkey) >= 0) and np.all(np.diff(s.tkey) >= 0) and np.all(np.diff(s.xkey) >= 0)
        s.idx = {}
        for i, (act, marco, mid, fin, lado) in enumerate(z['tmap']):
            s.idx[(str(act), str(marco), int(pd.Timestamp(str(fin)).timestamp()), str(lado))] = i
        sg = np.where(np.char.startswith(z['tmap'][:, 4].astype(str), 'YES'), 1.0, -1.0)
        s.sgn_tok = sg; flag = s.tv[:, 1] * 2 - 1
        s.cs = np.concatenate([[0.0], np.cumsum(sg[s.tk] * flag * s.tv[:, 2].astype(np.float64))])
        s.tstart = np.searchsorted(s.tk, np.arange(len(sg) + 1))
    def ms(s, tsec): return (np.asarray(tsec, dtype=np.float64) * 1000).round().astype(np.int64) - s.D0
    def bn(s, sym, t):
        k = np.full(len(t), sym, dtype=np.int64); j = np.searchsorted(s.xkey, k * BIG + t, 'right') - 1
        ok = (j >= 0) & (s.xk[np.clip(j, 0, None)] == sym); return np.where(ok, s.xv[np.clip(j, 0, None)], np.nan)
    def top_mid(s, k, t):
        okk = k >= 0; kk = np.where(okk, k, 0); j = np.searchsorted(s.qkey, kk * BIG + t, 'right') - 1
        jc = np.clip(j, 0, None); ok = okk & (j >= 0) & (s.qk[jc] == kk); v = s.qv[jc]
        good = ok & (v[:, 0] > 0) & (v[:, 1] > 0) & (v[:, 1] < 1.0001) & (v[:, 0] < v[:, 1] + 1e-9)
        return np.where(good, (v[:, 0] + v[:, 1]) / 2, np.nan)
    def flow(s, kY, kN, t0, t1):
        out = np.full(len(t0), np.nan)
        for kk in (kY, kN):
            pass
        tot = np.zeros(len(t0)); ok = np.ones(len(t0), bool)
        for kk in (kY, kN):
            oo = kk >= 0; k2 = np.where(oo, kk, 0)
            a = np.searchsorted(s.tkey, k2 * BIG + t1, 'right'); b = np.searchsorted(s.tkey, k2 * BIG + t0, 'right')
            tot += np.where(oo, s.cs[a] - s.cs[b], 0.0); ok &= oo | True
        return tot

def feats_df(df, d):
    """df: act, fin(epoch s), lado ('YES'/'NO'), t0 (epoch s). Devuelve columnas de indicadores orientados al lado."""
    D = Dia(d); n = len(df); res = {c: np.full(n, np.nan) for c in ['r60', 'r300', 'r900', 'rop', 'rpre', 'b15', 'd15', 'f60', 'f180']}
    act = df.act.values; fin = df.fin.values.astype(np.int64); lado = df.lado.values; t0s = df.t0.values
    sg = np.where(lado == 'YES', 1.0, -1.0); t0 = D.ms(t0s)
    for a, sym in SYM.items():
        m = np.where(act == a)[0]
        if not len(m): continue
        t = t0[m]; P = D.bn(sym, t)
        def r(back_ms, base=None):
            tb = (t - back_ms) if base is None else base
            Q = D.bn(sym, tb); return (P / Q - 1) * 1e4
        for nm, bk in (('r60', 60000), ('r300', 300000), ('r900', 900000)): res[nm][m] = r(bk) * sg[m]
        op = D.ms(fin[m] - 300); Po = D.bn(sym, op); res['rop'][m] = (P / Po - 1) * 1e4 * sg[m]
        Pp = D.bn(sym, op - 900000); res['rpre'][m] = (Po / Pp - 1) * 1e4 * sg[m]
        # 15m
        f15 = ((fin[m] + 899) // 900) * 900
        k15 = np.array([D.idx.get((a, '15min', int(f), str(l)), -1) for f, l in zip(f15, lado[m])])
        mid = D.top_mid(k15, t); mid5 = D.top_mid(k15, t - 300000)
        res['b15'][m] = mid - 0.5; res['d15'][m] = mid - mid5
        kY = np.array([D.idx.get((a, '5min', int(f), 'YES'), -1) for f in fin[m]]); kN = np.array([D.idx.get((a, '5min', int(f), 'NO'), -1) for f in fin[m]])
        ok = (kY >= 0) & (kN >= 0)
        res['f60'][m] = np.where(ok, D.flow(kY, kN, t - 60000, t) * sg[m], np.nan); res['f180'][m] = np.where(ok, D.flow(kY, kN, t - 180000, t) * sg[m], np.nan)
    return pd.DataFrame(res, index=df.index)

def main():
    days = ['2026-10-17', '2026-10-18', '2026-10-19', '2026-10-20', '2026-10-21', '2026-10-22']
    pop = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(os.path.join(CP, 'pop_units_*.csv.gz')))], ignore_index=True)
    pop = pop[(pop.es_b == 0)].copy(); pop['t0'] = pop.ts - 5.0
    b = pd.read_csv(os.path.join(SAL, 'unidades_b.csv'))
    b['act'] = b.coin; b['lado'] = np.where(b.outcome == 'Up', 'YES', 'NO'); b['fin'] = b.fin_s.astype(np.int64)
    pc = pd.to_datetime(b.primer_fill_chain, utc=True).astype('int64') / 1e9 if False else (pd.to_datetime(b.primer_fill_chain, utc=True).astype('int64') // 10**9)
    b['t0_flag'] = b.t_det.isna(); b['t0'] = np.where(b.t_det.notna(), b.t_det - 4.0, pc - 5.0)
    w = pd.read_csv(os.path.join(PH, 'fills_alts.csv.gz'), usecols=['dia', 'ts', 'wallet', 'rol', 'side', 'act', 'fin', 'lado_ef', 'px', 'acc', 'mid', 'des'])
    w = w[(w.rol == 'M') & w.act.isin(SYM)].copy(); w['px_ef'] = np.where(w.side == 0, w.px, 1 - w.px); w = w[(w.px_ef >= 0.1) & (w.px_ef <= 0.9)]
    w['lado'] = w.lado_ef; w['t0'] = w.ts - 5.0; w['T'] = w.fin - w.ts
    outs = {'pop': [], 'b': [], 'wal': []}
    for d in days:
        for nm, df in (('pop', pop[pop.dia == d]), ('b', b[b.dia == d]), ('wal', w[w.dia == d])):
            if len(df) == 0: continue
            f = feats_df(df, d); outs[nm].append(pd.concat([df, f], axis=1)); print(d, nm, len(df), flush=True)
    for nm, L in outs.items():
        X = pd.concat(L, ignore_index=True); X.to_csv(os.path.join(DAT, f'feats_{nm}.csv.gz'), index=False); print(nm, len(X), X[['r60', 'r300', 'r900', 'rop', 'rpre', 'b15', 'd15', 'f60']].notna().mean().round(3).to_dict())
main()
