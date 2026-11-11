#!/usr/bin/env python3
"""passT_cxb_v3.py STAMP ENG DIA  (STAMP in {v2,v3}; ENG in {orig,dd}) -- passT_v2 (modo 'causal', SIN editar) con (a) sello v3 de la cinta (stamp_v3.py) y (b) motor engine_v3 con/sin dedupe de cola.
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
if os.path.exists(OUT + f'CX_{TAG}.pkl'): print('ya', TAG); sys.exit(0)
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

# ======================= PASO 4-6: familia CXB-true / F5 con MOTOR (re-armado, cola, rem). Variantes declaradas ANTES de mirar resultados (ver PASS_T_V3_RESULTADOS_11nov.md §variantes).
C0, C1 = 3.526360511779785, 4.717426776885986                     # cortes F5 congelados (PREREG_FWD_V2, TRAIN 06-08 Oct); F5 = log1p(tamano del ask nivel 1 del token propio)
SA2 = '/root/polymarket-research-datalogs/sa_ms2/'
def sza_rx(d):
    """tamano del ask (q_v3) alineado con la vista RX (K): misma filtracion/orden que relojes.Day2(clock='rx') -> lexsort((rx, qk)). Se verifica contra K.v0."""
    z = np.load(SA2 + f'ms2_{d}.npz', allow_pickle=True); qk = z['q_k']; rx = z['q_t_rx']; v3 = z['q_v3']; v0 = z['q_v0']; ok = rx >= 0
    if (~ok).any(): qk = qk[ok]; rx = rx[ok]; v3 = v3[ok]; v0 = v0[ok]
    o = np.lexsort((rx, qk)).astype(np.int32); v3 = v3[o].astype(np.float32); v0 = v0[o]; del o, z
    return v3, v0
SZA, V0CHK = sza_rx(d)
assert len(SZA) == len(K.v0) and np.array_equal(np.nan_to_num(V0CHK.astype(np.float64), nan=-9), np.nan_to_num(np.asarray(K.v0, np.float64), nan=-9)), 'sza no alineado con K'
del V0CHK
S_PLC = 20
TESTED = ['CXB60', 'CXB100', 'CXB150', 'TOP60', 'CXB60r', 'F5A', 'F5B', 'F5A_CXB60', 'F5A_CXB100', 'F5A_CXB150']
CTRL = ['G0', 'GEO1', 'GEO1_F5A']
VN = CTRL + TESTED + [f'P_{v}_{s}' for v in TESTED for s in range(1, S_PLC + 1)]
FILLS = []; AGG = {}
def cfn(qt, arr, l):
    qbel = qt[arr]
    def f(t0, t1):
        ix = np.searchsorted(qt, t0, side='right') - 1
        if ix >= 0 and arr[ix]: return t0 + l
        tb = first_after(qbel, t0 + 1, t1); return None if tb is None else tb + l
    return f
for k in ks:
    g, bid, ask, b15, vol, hora = FE[k]; fin = int(D.fin[k]); gana = G.capt_outcome(E, k); coin = D.act[k]; lado = D.lado[k]
    a_, b_ = K.qb[k], K.qb[k + 1]; qt = K.qt[a_:b_]; v0 = K.v0[a_:b_]; sz = SZA[a_:b_]
    tq = g - 300; b300 = E.quotes(k, tq)[0]
    jx = np.searchsorted(qt, g, side='right') - 1; f5g = np.where(jx >= 0, np.log1p(np.where(np.isfinite(sz[np.maximum(jx, 0)]), sz[np.maximum(jx, 0)], np.nan)), np.nan)   # F5 en el instante de decision (RX)
    f5hi = np.isfinite(f5g) & (f5g <= C1); f5lo = np.isfinite(f5g) & (f5g <= C0)                              # 'permitido' = fuera del tercil ALTO / solo tercil BAJO
    for L in G.LEVELS:
        Gm = G.gate_vec('G', L, b15, vol, hora); base = Gm & np.isfinite(ask) & (ask > L + G.EPS)
        with np.errstate(invalid='ignore'):
            bl = b300 - L; arm = np.isfinite(b300) & (bl >= 0.01 - 1e-6); armr = arm & np.isfinite(bid) & (bid >= L + 0.01 - 1e-6)
        below = v0 < L - G.TOLP; topc = v0 <= L + G.TOLP
        c = {l: cfn(qt, below, l) for l in (60, 100, 150)}; ctop = cfn(qt, topc, 60)
        spec = {'G0': (base, Gm, None), 'GEO1': (base & arm, Gm, None), 'GEO1_F5A': (base & arm & f5hi, Gm & f5hi, None),
                'CXB60': (base & arm, Gm, c[60]), 'CXB100': (base & arm, Gm, c[100]), 'CXB150': (base & arm, Gm, c[150]), 'TOP60': (base & arm, Gm, ctop), 'CXB60r': (base & armr, Gm, c[60]),
                'F5A': (base & f5hi, Gm & f5hi, None), 'F5B': (base & f5lo, Gm & f5lo, None),
                'F5A_CXB60': (base & arm & f5hi, Gm & f5hi, c[60]), 'F5A_CXB100': (base & arm & f5hi, Gm & f5hi, c[100]), 'F5A_CXB150': (base & arm & f5hi, Gm & f5hi, c[150])}
        def plc(name, s):
            rs = np.random.default_rng(s * 7919 + k * 31 + int(L * 100) + hash(name) % 1000 * 0)     # semilla independiente de hash(): determinista
            can0, Gm0, cf0 = spec[name]; n_ = len(g); sh = int(rs.integers(120, n_ - 120)) if n_ > 240 else 0
            if name.startswith('F5'):                                                                         # placebo del filtro F5: mascara rodada (mismo ciclo de trabajo, sin relacion con el libro)
                m_hi = np.roll(f5hi, sh); m_lo = np.roll(f5lo, sh); m = m_lo if name == 'F5B' else m_hi
                can_p = base & (arm if 'CXB' in name else True) & m; Gm_p = Gm & m
            else: can_p, Gm_p = can0, Gm0
            if cf0 is None: return can_p, Gm_p, None
            def pf(t0, t1):                                                                                  # placebo de cancelacion: misma cobertura (se cancela solo si la regla real dispararia), instante uniforme en el segmento
                tc = cf0(t0, t1); u = rs.random()
                return None if (tc is None or tc >= t1) else int(t0 + u * (t1 - t0))
            return can_p, Gm_p, pf
        for name in VN:
            if name.startswith('P_'): _, v, s = name.split('_', 1)[0], name[2:].rsplit('_', 1)[0], int(name.rsplit('_', 1)[1]); can, Gmx, cf = plc(v, s)
            else: can, Gmx, cf = spec[name]
            ag = AGG.setdefault((name, coin, L), [0, 0, 0.0, 0.0, 0.0, 0.0]); real = not name.startswith('P_')
            for (si, t, t_arr, t_end, q, tf, canc) in run_var(k, L, g, can, Gmx, fin, cf):
                ag[0] += 1; ag[1] += canc
                if q > 1e-9:
                    pnl = q * (gana - L) + q * 0.2 * 0.07 * L * (1 - L); ag[2] += 1; ag[3] += q * L; ag[4] += pnl
                    if real: FILLS.append((name, d, coin, lado, fin, k, L, q, tf, gana, si, t, canc, (fin * 1000 - tf) / 1000.0, float(f5g[int(np.searchsorted(g, t))]), pnl, q * L))
R = pd.DataFrame(FILLS, columns=['var', 'dia', 'act', 'lado', 'fin', 'k', 'L', 'q', 'tf', 'gana', 'seg', 't_dec', 'canc', 'T', 'f5_dec', 'pnl', 'cost'])
A = pd.DataFrame([(n, d, c, L, *v) for (n, c, L), v in AGG.items()], columns=['var', 'dia', 'act', 'L', 'n_seg', 'n_canc', 'n_fill', 'cost', 'pnl', 'dummy']).drop(columns=['dummy'])
A['cost'] = [v[3] for v in AGG.values()]; A['pnl'] = [v[4] for v in AGG.values()]
pd.to_pickle(dict(R=R, A=A, ramas=BR, c_epoca=C_EPOCA), OUT + f'CX_{TAG}.pkl.tmp'); os.replace(OUT + f'CX_{TAG}.pkl.tmp', OUT + f'CX_{TAG}.pkl')
print('ok CX', TAG, {v: (int(x.n_fill.sum()), round(float(x.pnl.sum()), 1)) for v, x in A.groupby('var', sort=False) if not v.startswith('P_')}, round(time.time() - T0, 1), 's', flush=True)
