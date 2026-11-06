#!/usr/bin/env python3
"""TOXICIDAD thru1 (06-Nov, reverse-engineer, EXPLORATORIO, DEV, 0 ordenes). Diseno DISENO_T.md (sha 36e49c0c). Base passC5d.py (engine SIN tocar). Uso: python3 -I passT.py DIA -> out/RT_<D>.pkl, out/SEGT_<D>.pkl
(todas las colocaciones, cancelacion a +60 ms cuando la politica se apaga y REPOSICION cuando vuelve), cinta re-sincronizada = esc_dec2.py.
Variantes (fijadas ANTES de ver C3): G0; AVO_<S><c> = cotizar solo si p_S <= umbral de cobertura c (umbral fijado en dias de entrenamiento);
INV_<S>70 = cotizar solo si p_S > umbral70 (inversion); PLA_<S>70_<seed> = puntuacion de OTRO token (misma moneda, lado y nivel, mismo T, relleno hacia
delante/atras), mismo umbral (placebo con la misma persistencia temporal). Uso: python3 -I passC3.py DIA -> out/RC3_<D>.pkl, out/SC3_<D>.pkl"""
import sys, os, json, time, gc, numpy as np, pandas as pd
T0 = time.time()
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = H + 'out/'
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
sys.path.insert(0, P2 + 'escalera_B'); import engine as G
PB = P2 + 'precursores_barrido/out/'
d = sys.argv[1]
if os.path.exists(OUT + f'RT_{d}.pkl'): print('ya', d); sys.exit(0)
tape = pd.read_pickle(PB + f'tape_{d}.pkl'); bad = {tuple(x) for x in json.load(open(PB + f'bad_{d}.json'))['bad']}
E = G.DayEng(d, 'chain', tape, bad); D = E.D
tp = tape.assign(k=tape.token_id.map(D.tokidx)); tp = tp[tp.k.notna()].copy(); tp['k'] = tp.k.astype(int)
tp['pr3'] = tp.price.round(3); ev = tp.groupby(['k', 'tx']).agg(t=('t_ws_ms', 'min'), pmin=('price', 'min'), npr=('pr3', 'nunique')).reset_index(); tp = tp.drop(columns=['pr3'])
tm = np.empty(len(ev), np.int64); evk = ev.k.values; evt = ev.t.values.astype(np.int64); evp = ev.pmin.values
for i in range(len(ev)):
    k = evk[i]; t = evt[i]; pm = evp[i]
    a, b = D.qb[k], D.qb[k + 1]; qt = D.qt[a:b]; v0 = D.v0[a:b]
    i0 = np.searchsorted(qt, t - 400, side='left'); i1 = np.searchsorted(qt, t, side='right'); tm[i] = t - 63
    if i1 > i0 and i0 > 0:
        lo = v0[i0 - 1:i1] <= pm + G.TOLP; w = np.where(lo[1:] & ~lo[:-1])[0]
        if len(w): tm[i] = int(qt[i0 + w[0]])
ev['tm'] = tm
tp = tp.merge(ev[['k', 'tx', 'tm']], on=['k', 'tx'], how='left'); tp['t_ws_ms'] = tp.tm.astype(np.int64)
E.tape = G.Tape('chain', D, tp.drop(columns=['k', 'tm'])); KEY = {}
for _k, _t, _pm, _np in zip(ev.k.values, ev.tm.values, ev.pmin.values, ev.npr.values): KEY.setdefault((int(_k), int(_t)), []).append((float(_pm), int(_np)))
del tp, tape, ev; gc.collect()
ks = [k for k in E.ks if E.sane(k) == 'ok' and G.capt_outcome(E, k) is not None]
FE = {k: E.feats(k) for k in ks}
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/q11/barrido_multi'); import bfeat
def load_x_lean(dias, t_from):   # = passA.load_x_lean (solo t, px)
    acc = {}
    for dd in dias:
        f = bfeat.xfile(dd)
        if not f: continue
        for ch in pd.read_csv(f, header=None, usecols=[2, 3, 7], names=['sym', 'px', 'recv'], dtype={'sym': 'category', 'px': 'float64', 'recv': 'int64'}, chunksize=1500000):
            ch = ch[ch.recv.values >= t_from]
            for sym, g_ in ch.groupby('sym', observed=True): acc.setdefault(str(sym)[:-4], []).append((g_.recv.values, g_.px.values))
    out = {}
    for sym, L_ in acc.items():
        t = np.concatenate([x[0] for x in L_]); o = np.argsort(t, kind='stable'); out[sym] = (t[o], np.concatenate([x[1] for x in L_])[o])
    return out
day0 = int(pd.Timestamp(d, tz='UTC').timestamp()) * 1000
XS = load_x_lean([(pd.Timestamp(d) - pd.Timedelta(days=1)).strftime('%Y-%m-%d'), d], day0 - 3 * 3600 * 1000)
def bnr(coin, times, w):
    A_ = XS.get(coin)
    if A_ is None: return np.full(len(times), np.nan)
    t, p = A_; j1 = np.searchsorted(t, times, side='right') - 1; j0 = np.searchsorted(t, times - w, side='right') - 1
    ok = (j1 >= 0) & (j0 >= 0) & (t[np.maximum(j1, 0)] > times - 15000)
    return np.where(ok, (p[np.maximum(j1, 0)] / p[np.maximum(j0, 0)] - 1) * 1e4, np.nan)
JUMP = {}
for coin, (t, p) in XS.items():   # saltos de 1 s >=3 bps, hora = recepcion del tick
    r1 = bnr(coin, t, 1000); JUMP[coin] = {'up': t[r1 >= 3], 'dn': t[r1 <= -3]}
def first_after(arr, t0, t1):
    i = np.searchsorted(arr, t0, side='left'); return int(arr[i]) if i < len(arr) and arr[i] <= t1 else None
def run_var(k, L, g, can, Gm, fin, cancel_fn):
    n = len(g); hard = (fin - G.TMIN) * 1000 + 60; falsos = np.where(~Gm)[0]; i = 0; rem = 5.0; out = []; si = 0
    while i < n and rem > 1e-9:
        if not can[i]: i += 1; continue
        t = int(g[i]); t_arr = t + G.LAT_POST; pos = np.searchsorted(falsos, i + 1); j = falsos[pos] if pos < len(falsos) else n
        t_end = min(int(g[j]) + 60 if j < n else hard, hard); canc = 0
        if cancel_fn is not None and t_end > t_arr:
            tc = cancel_fn(t_arr, t_end)
            if tc is not None and tc < t_end: t_end = max(tc, t_arr); canc = 1
        if t_end > t_arr:
            q, tf, _ = E.run_segment(k, L, t_arr, t_end, rem, 'BASE')
            out.append((si, t, t_arr, t_end, float(q), int(tf) if q > 1e-9 else -1, canc)); si += 1
            if q > 1e-9: rem -= q
        i = max(i + 1, int(np.searchsorted(g, t_end)))
    return out
def ftype(k, L, tf):
    it = KEY.get((int(k), int(tf)))
    if not it: return 'nomatch'
    thr = [(pm < L - G.TOLP, npr) for pm, npr in it]
    if any(a and b >= 2 for a, b in thr): return 'nivel'
    if any(a for a, b in thr): return 'thru1'
    return 'cola'
CXBL = (150, 300, 1000, 3000); CXJL = (150, 1000)
VN = ['G0', 'GEO6', 'NJ3', 'NJ3A', 'CALM3', 'GEO6NJ3'] + [f'CXB{l}' for l in CXBL] + [f'CXJ{l}' for l in CXJL] + [f'PNJ3A_{s}' for s in range(1, 20)] + [f'PCXB300_{s}' for s in range(1, 6)]
FILLS = []; SEGF = []
for k in ks:
    g, bid, ask, b15, vol, hora = FE[k]; fin = int(D.fin[k]); gana = G.capt_outcome(E, k); coin = D.act[k]; lado = D.lado[k]; sgn = 1.0 if lado == 'YES' else -1.0
    tq = g - 300; b300 = E.quotes(k, tq)[0]; b3300 = E.quotes(k, g - 3300)[0]
    with np.errstate(invalid='ignore'):
        r3 = sgn * bnr(coin, tq, 3000); dbid3 = b300 - b3300
    J = JUMP.get(coin, {'up': np.array([], np.int64), 'dn': np.array([], np.int64)}); jadv = J['dn'] if lado == 'YES' else J['up']
    ja3 = (np.searchsorted(jadv, tq, side='right') - np.searchsorted(jadv, tq - 3000, side='right')) > 0
    a_, b_ = D.qb[k], D.qb[k + 1]; qt = D.qt[a_:b_]; v0 = D.v0[a_:b_]
    for L in G.LEVELS:
        Gm = G.gate_vec('G', L, b15, vol, hora); base = Gm & np.isfinite(ask) & (ask > L + G.EPS)
        with np.errstate(invalid='ignore'):
            bl = b300 - L; geo6 = np.isfinite(b300) & (bl >= 0.06 - 1e-6); nj3 = ~(np.abs(r3) >= 3); nj3a = ~(r3 <= -3)
            calm = (np.abs(dbid3) < 1e-9) & (np.abs(r3) < 3); arm_cxb = np.isfinite(b300) & (bl >= 0.01 - 1e-6)
        below = v0 < L - G.TOLP; qbel = qt[below]
        def cxb(l):
            def f(t0, t1):
                ix = np.searchsorted(qt, t0, side='right') - 1
                if ix >= 0 and below[ix]: return t0 + l
                tb = first_after(qbel, t0 + 1, t1); return None if tb is None else tb + l
            return f
        def cxj(l):
            def f(t0, t1):
                tb = first_after(jadv, t0, t1); return None if tb is None else tb + l
            return f
        rng = np.random.default_rng(k * 131 + int(L * 100))
        specs = {'G0': (base, None), 'GEO6': (base & geo6, None), 'NJ3': (base & nj3, None), 'NJ3A': (base & nj3a, None), 'CALM3': (base & calm, None), 'GEO6NJ3': (base & geo6 & nj3, None)}
        for l in CXBL: specs[f'CXB{l}'] = (base & arm_cxb, cxb(l))
        for l in CXJL: specs[f'CXJ{l}'] = (base & ~ja3, cxj(l))
        for s in range(1, 20):
            sh = int(rng.integers(120, len(g) - 120)) if len(g) > 240 else 0; specs[f'PNJ3A_{s}'] = (base & np.roll(nj3a, sh), None)
        c300 = cxb(300)
        for s in range(1, 6):
            rs = np.random.default_rng(s * 7919 + k * 31 + int(L * 100))
            def pf(t0, t1, rs=rs):
                tc = c300(t0, t1); u = rs.random()
                return None if (tc is None or tc >= t1) else int(t0 + u * (t1 - t0))
            specs[f'PCXB300_{s}'] = (base & arm_cxb, pf)
        for name in VN:
            can, cf = specs[name]
            for (si, t, t_arr, t_end, q, tf, canc) in run_var(k, L, g, can, Gm, fin, cf):
                ft = ftype(k, L, tf) if q > 1e-9 else ''
                if q > 1e-9: FILLS.append((name, d, coin, lado, fin, k, L, q, tf, (fin * 1000 - tf) / 1000.0, gana, si, t, ft, canc))
                if name == 'G0':
                    ig = int(np.searchsorted(g, t))
                    SEGF.append((d, coin, lado, fin, k, L, si, t, (fin * 1000 - t) / 1000.0, float(bl[ig]), float(r3[ig]), float(dbid3[ig]), bool(ja3[ig]), q, tf, ft, t_end - t_arr, gana))
R = pd.DataFrame(FILLS, columns=['var', 'dia', 'act', 'lado', 'fin', 'k', 'L', 'q', 'tf', 'T', 'gana', 'seg', 't_dec', 'ftype', 'canc'])
R['cost'] = R.q * R.L; R['pnl'] = R.q * (R.gana - R.L) + R.q * 0.2 * 0.07 * R.L * (1 - R.L)
S = pd.DataFrame(SEGF, columns=['dia', 'act', 'lado', 'fin', 'k', 'L', 'seg', 't_dec', 'T', 'bidL', 'r3', 'dbid3', 'ja3', 'q', 'tf', 'ftype', 'vida_ms', 'gana'])
S.to_pickle(OUT + f'SEGT_{d}.pkl'); R.to_pickle(OUT + f'RT_{d}.pkl.tmp'); os.replace(OUT + f'RT_{d}.pkl.tmp', OUT + f'RT_{d}.pkl')
print('ok', d, 'tokens', len(ks), {v: (len(x), round(float(x.pnl.sum()), 1)) for v, x in R.groupby('var', sort=False) if not v.startswith('P')}, 'binance', {c: len(v[0]) for c, v in XS.items()}, round(time.time() - T0, 1), 's', flush=True)
