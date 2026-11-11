#!/usr/bin/env python3
"""passT_v3.py STAMP ENG DIA  (STAMP in {v2,v3}; ENG in {orig,dd}) -- passT_v2 (modo 'causal', SIN editar) con (a) sello v3 de la cinta (stamp_v3.py) y (b) motor engine_v3 con/sin dedupe de cola.
v2 = regla vieja (caida L1 buscada por RX en [t_rx-400,t_rx], sello EX; t_ev; t_rx-63) -- solo regresion (STAMP=v2 ENG=orig reproduce out_v2/RT_causal); v3 = firma exacta unica -> ex(fila)-1; si no, t_ev - c_epoca - 1.
ENG=orig = engine.fill_segment original (engine_v3.fill_segment_v3 dedupe=False); dd = dedupe. Salida: out_v3/RT_<STAMP><ENG>_<D>.pkl, SEGT_..., TAPEDIAG_....json. Docstring original de passT_v2:
passT_v2.py MODO DIA -- passT (passT_copia/passT.py, SIN editar) parametrizado por RELOJ. MODO in {legacy, causal, rx} (engine_clock.MODOS, CONTRATO_RELOJES.md).
Salida: out_v2/RT_<modo>_<D>.pkl, SEGT_<modo>_<D>.pkl, TAPEDIAG_<modo>_<D>.json. 'legacy' reproduce el passT original (regresion); 'causal' = conocimiento en RECEPCION + mecanica de relleno en EXCHANGE.
Sello de tiempo de cada print de la cinta (tm): legacy = caida L1 (q_t EXCHANGE) en [t_rx-400, t_rx] o t_rx-63; causal = caida L1 buscada por RECEPCION en [t_rx-400, t_rx], devuelta con su sello EXCHANGE,
o t_ev del tx (libro5_tx, exchange) o t_rx-63; rx = caida L1 en recepcion o t_rx (sin constante). 0 ordenes; solo lectura."""
import sys, os, json, time, gc, numpy as np, pandas as pd
T0 = time.time()
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = os.environ.get('PASST_OUT', H + 'out_v3/'); os.makedirs(OUT, exist_ok=True); sys.path.insert(0, H)
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
sys.path.insert(0, P2 + 'escalera_B'); import engine as G; import engine_clock as EC; import engine_v3 as E3; import stamp_v3 as ST; import glob
PB = P2 + 'precursores_barrido/out/'
STAMP, ENG, d = sys.argv[1], sys.argv[2], sys.argv[3]
assert STAMP in ('v2', 'v3') and ENG in ('orig', 'dd'), (STAMP, ENG); modo = 'causal'
TAG = f'{STAMP}{ENG}_{d}'
if os.path.exists(OUT + f'RT_{TAG}.pkl'): print('ya', TAG); sys.exit(0)
tape = pd.read_pickle(PB + f'tape_{d}.pkl'); bad = {tuple(x) for x in json.load(open(PB + f'bad_{d}.json'))['bad']}
E = E3.DayEngV3(d, 'chain', tape, bad, modo=modo, dedupe=(ENG == 'dd')); D = E.D; K = E.K
# t_ev (EXCHANGE) del tx desde libro5_tx (cols t_ev, token, tx, recv). Solo se usa en modo causal como fallback del sello de relleno.
TXD = '/mnt/HC_Volume_106538179/libro5_tx/'; fr = []
for dd_ in [(pd.Timestamp(d) + pd.Timedelta(days=i)).strftime('%Y-%m-%d') for i in (-1, 0, 1)]:
    for f_ in sorted(glob.glob(TXD + f'libro5_tx_{dd_}_*.csv.gz')): fr.append(pd.read_csv(f_, header=None, names=['t_ev', 'token', 'tx', 'recv'], dtype={'token': str, 'tx': str}))
TEV = pd.concat(fr, ignore_index=True).groupby('tx').t_ev.min() if fr else pd.Series(dtype='int64'); del fr
tp = tape.assign(k=tape.token_id.map(D.tokidx)); tp = tp[tp.k.notna()].copy(); tp['k'] = tp.k.astype(int)
tp['pr3'] = tp.price.round(3); ev = tp.groupby(['k', 'tx']).agg(t=('t_ws_ms', 'min'), pmin=('price', 'min'), pmax=('pr3', 'max'), S=('sh', 'sum'), npr=('pr3', 'nunique')).reset_index(); tp = tp.drop(columns=['pr3'])
evk = ev.k.values; evt = ev.t.values.astype(np.int64); evp = ev.pmin.values
tev_ = ev.tx.map(TEV).values; RXB = np.full(len(ev), -1, np.int64); BR = dict(drop=0, tev=0, const63=0, rxprint=0, sig=0, amb=0, nosig=0, guard=0, sinev=0)
RAMA = np.empty(len(ev), object); C_EPOCA = None
if STAMP == 'v2':
    tm = np.empty(len(ev), np.int64)
    for i in range(len(ev)):
        k = evk[i]; t = evt[i]; pm = evp[i]                       # t = RECEPCION del print (libro5_tx)
        a, b = K.qb[k], K.qb[k + 1]; qt = K.qt[a:b]; v0 = K.v0[a:b]
        i0 = np.searchsorted(qt, t - 400, side='left'); i1 = np.searchsorted(qt, t, side='right'); hit = False
        if i1 > i0 and i0 > 0:
            lo = v0[i0 - 1:i1] <= pm + G.TOLP; w = np.where(lo[1:] & ~lo[:-1])[0]
            if len(w):
                j = i0 + w[0]; hit = True; BR['drop'] += 1; tm[i] = int(K.otro(a + j)); RXB[i] = int(qt[j]); RAMA[i] = 'drop'
        if not hit:
            if np.isfinite(tev_[i]): tm[i] = int(tev_[i]); BR['tev'] += 1; RAMA[i] = 'tev'
            else: tm[i] = t - 63; BR['const63'] += 1; RAMA[i] = 'const63'
else:
    tev_abs = np.where(np.isfinite(tev_), np.nan_to_num(tev_, nan=-1.0), -1.0).astype(np.int64)
    tm, RAMA, ROW, DEX, C_EPOCA, NEX = ST.stamp_events(D.qt, D.v0, D.v2, D.qb, evk, tev_abs, ev.pmax.values, evp, ev.S.values, ev.npr.values)
    sinev = RAMA == 'sinev'; tm = np.where(sinev, evt - 63, tm)
    for r_ in RAMA: BR[r_] += 1
    for i in np.where(RAMA == 'sig')[0]:
        o = int(D.otro(int(ROW[i]))); RXB[i] = o
ev['tm'] = tm; ev['rxb'] = RXB; ev['rama'] = RAMA
tp = tp.merge(ev[['k', 'tx', 'tm']], on=['k', 'tx'], how='left'); tp['t_ws_ms'] = tp.tm.astype(np.int64)
EVX = {(int(k_), int(m_)): (int(r_), int(t_), str(a_)) for k_, m_, r_, t_, a_ in zip(ev.k.values, ev.tm.values, ev.rxb.values, ev.t.values, ev.rama.values)}   # (k, tm) -> (rx fila, rx print, rama)
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
    a_, b_ = K.qb[k], K.qb[k + 1]; qt = K.qt[a_:b_]; v0 = K.v0[a_:b_]      # conocimiento (disparos de cancelacion por el libro) = vista K
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
                if q > 1e-9: FILLS.append((name, d, coin, lado, fin, k, L, q, tf, (fin * 1000 - tf) / 1000.0, gana, si, t, ft, canc) + EVX.get((int(k), int(tf)), (-1, -1, 'nomatch')))
                if name == 'G0':
                    ig = int(np.searchsorted(g, t))
                    SEGF.append((d, coin, lado, fin, k, L, si, t, (fin * 1000 - t) / 1000.0, float(bl[ig]), float(r3[ig]), float(dbid3[ig]), bool(ja3[ig]), q, tf, ft, t_end - t_arr, gana))
R = pd.DataFrame(FILLS, columns=['var', 'dia', 'act', 'lado', 'fin', 'k', 'L', 'q', 'tf', 'T', 'gana', 'seg', 't_dec', 'ftype', 'canc', 'tf_rxb', 'tf_rxp', 'rama'])
R['cost'] = R.q * R.L; R['pnl'] = R.q * (R.gana - R.L) + R.q * 0.2 * 0.07 * R.L * (1 - R.L)
S = pd.DataFrame(SEGF, columns=['dia', 'act', 'lado', 'fin', 'k', 'L', 'seg', 't_dec', 'T', 'bidL', 'r3', 'dbid3', 'ja3', 'q', 'tf', 'ftype', 'vida_ms', 'gana'])
S.to_pickle(OUT + f'SEGT_{TAG}.pkl'); json.dump(dict(stamp=STAMP, eng=ENG, dia=d, c_epoca=C_EPOCA, paired_dedupe=int(E.diag.get('paired', 0)), ramas_tm=BR, clock_fill=E.clock_fill, clock_know=E.clock_know, n_sin_rx_q=int(getattr(K, 'n_sin_rx', 0))), open(OUT + f'TAPEDIAG_{TAG}.json', 'w'))
R.to_pickle(OUT + f'RT_{TAG}.pkl.tmp'); os.replace(OUT + f'RT_{TAG}.pkl.tmp', OUT + f'RT_{TAG}.pkl')
print('ok', TAG, 'ramas_tm', BR, 'tokens', len(ks), {v: (len(x), round(float(x.pnl.sum()), 1)) for v, x in R.groupby('var', sort=False) if not v.startswith('P')}, 'binance', {c: len(v[0]) for c, v in XS.items()}, round(time.time() - T0, 1), 's', flush=True)
