#!/usr/bin/env python3
"""passT_cxb_l.py STAMP DIA  (STAMP in {v3,v3p}; motor v3 con dedupe) -- COPIA ACOTADA de passT_cxb_v3.py (no se edita el original): familia CXB-true con la CURVA de l (35/45/60/80/100/120/150 ms y mezcla empirica `EMP` del pool de anclas propias),
sin placebo ni F5 (declarado en L_REAL_Y_DRYRUN_CXB60_11nov.md). STAMP=v3p = sello PESIMISTA para el fallback (ramas amb/nosig/guard: tm adelantado en (p95 de d_ex de las firmas unicas del dia - c_epoca) ms, hasta ~56 ms: el relleno
cae ANTES en el modelo, la cancelacion llega 'tarde' mas veces). Salida out_l/CXL_<STAMP>_<D>.pkl. HOLD (>=10-Nov) no se lee. 0 ordenes. Docstring del original:
passT_cxb_v3.py STAMP ENG DIA  (STAMP in {v2,v3}; ENG in {orig,dd}) -- passT_v2 (modo 'causal', SIN editar) con (a) sello v3 de la cinta (stamp_v3.py) y (b) motor engine_v3 con/sin dedupe de cola.
v2 = regla vieja (caida L1 buscada por RX en [t_rx-400,t_rx], sello EX; t_ev; t_rx-63) -- solo regresion (STAMP=v2 ENG=orig reproduce out_v2/RT_causal); v3 = firma exacta unica -> ex(fila)-1; si no, t_ev - c_epoca - 1.
ENG=orig = engine.fill_segment original (engine_v3.fill_segment_v3 dedupe=False); dd = dedupe. Salida: out_v3/RT_<STAMP><ENG>_<D>.pkl, SEGT_..., TAPEDIAG_....json. Docstring original de passT_v2:
passT_v2.py MODO DIA -- passT (passT_copia/passT.py, SIN editar) parametrizado por RELOJ. MODO in {legacy, causal, rx} (engine_clock.MODOS, CONTRATO_RELOJES.md).
Salida: out_v2/RT_<modo>_<D>.pkl, SEGT_<modo>_<D>.pkl, TAPEDIAG_<modo>_<D>.json. 'legacy' reproduce el passT original (regresion); 'causal' = conocimiento en RECEPCION + mecanica de relleno en EXCHANGE.
Sello de tiempo de cada print de la cinta (tm): legacy = caida L1 (q_t EXCHANGE) en [t_rx-400, t_rx] o t_rx-63; causal = caida L1 buscada por RECEPCION en [t_rx-400, t_rx], devuelta con su sello EXCHANGE,
o t_ev del tx (libro5_tx, exchange) o t_rx-63; rx = caida L1 en recepcion o t_rx (sin constante). 0 ordenes; solo lectura."""
import sys, os, json, time, gc, numpy as np, pandas as pd
T0 = time.time()
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'; OUT = os.environ.get('PASST_OUT', H + 'l_real_11nov/out_l/'); os.makedirs(OUT, exist_ok=True); sys.path.insert(0, H)
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
sys.path.insert(0, P2 + 'escalera_B'); import engine as G; import engine_clock as EC; import engine_v3 as E3; import stamp_v3 as ST; import glob
PB = P2 + 'precursores_barrido/out/'
STAMP, d = sys.argv[1], sys.argv[2]; ENG = 'dd'
assert STAMP in ('v3', 'v3p'), STAMP; modo = 'causal'; assert d <= '2026-11-09', 'HOLD'
TAG = f'{STAMP}_{d}'
if os.path.exists(OUT + f'CXL_{TAG}.pkl'): print('ya', TAG); sys.exit(0)
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
    sinev = RAMA == 'sinev'
    DHI = None
    if STAMP == 'v3p':
        okd = (RAMA == 'sig') & np.isfinite(DEX); DHI = int(np.percentile(DEX[okd], 95)) if okd.sum() >= 200 else 76
        fb = np.isin(RAMA, ['amb', 'nosig', 'guard']); tm = np.where(fb, tm - max(DHI - C_EPOCA, 0), tm)
    tm = np.where(sinev, evt - 63, tm)
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

# ======================= CURVA DE l: familia CXB-true (mismo criterio y re-armado que passT_cxb_v3: CXB = base & arm, cancelar al ver bid<L, efectiva t_rx + l). Controles G0, GEO1.
def sza_dummy(): return None
LS = [35, 45, 60, 80, 100, 120, 150]
AN = json.load(open(H + 'l_real_11nov/out/anclas_l_real.json')); POOL = np.array([int(round(x)) for x in AN['pool_empirico_l']['valores']], np.int64); PROC = 3     # PROC: d_proc declarado (rx disparo -> envio DELETE), NO medido
VN = ['G0', 'GEO1'] + [f'CXB{l}' for l in LS] + ['CXBEMP']
FILLS = []; AGG = {}
def cfn(qt, arr, l):
    qbel = qt[arr]
    def f(t0, t1):
        ix = np.searchsorted(qt, t0, side='right') - 1
        if ix >= 0 and arr[ix]: return t0 + l
        tb = first_after(qbel, t0 + 1, t1); return None if tb is None else tb + l
    return f
def cfn_emp(qt, arr, rs):
    qbel = qt[arr]
    def f(t0, t1):
        ix = np.searchsorted(qt, t0, side='right') - 1
        if ix >= 0 and arr[ix]: tb = t0
        else:
            tb = first_after(qbel, t0 + 1, t1)
            if tb is None: return None
        return int(tb + PROC + POOL[int(rs.integers(len(POOL)))])
    return f
for k in ks:
    g, bid, ask, b15, vol, hora = FE[k]; fin = int(D.fin[k]); gana = G.capt_outcome(E, k); coin = D.act[k]; lado = D.lado[k]
    a_, b_ = K.qb[k], K.qb[k + 1]; qt = K.qt[a_:b_]; v0 = K.v0[a_:b_]
    tq = g - 300; b300 = E.quotes(k, tq)[0]
    for L in G.LEVELS:
        Gm = G.gate_vec('G', L, b15, vol, hora); base = Gm & np.isfinite(ask) & (ask > L + G.EPS)
        with np.errstate(invalid='ignore'): arm = np.isfinite(b300) & ((b300 - L) >= 0.01 - 1e-6)
        below = v0 < L - G.TOLP
        spec = {'G0': (base, None), 'GEO1': (base & arm, None)}
        for l in LS: spec[f'CXB{l}'] = (base & arm, cfn(qt, below, l))
        spec['CXBEMP'] = (base & arm, cfn_emp(qt, below, np.random.default_rng(k * 131 + int(round(L * 100)))))
        for name in VN:
            can, cf = spec[name]
            ag = AGG.setdefault((name, coin, L), [0, 0, 0.0, 0.0, 0.0])
            for (si, t, t_arr, t_end, q, tf, canc) in run_var(k, L, g, can, Gm, fin, cf):
                ag[0] += 1; ag[1] += canc
                if q > 1e-9:
                    pnl = q * (gana - L) + q * 0.2 * 0.07 * L * (1 - L); ag[2] += 1; ag[3] += q * L; ag[4] += pnl
                    FILLS.append((name, d, coin, lado, fin, k, L, q, tf, gana, si, t, canc, pnl, q * L))
R = pd.DataFrame(FILLS, columns=['var', 'dia', 'act', 'lado', 'fin', 'k', 'L', 'q', 'tf', 'gana', 'seg', 't_dec', 'canc', 'pnl', 'cost'])
A = pd.DataFrame([(n, d, c, L, v[0], v[1], v[2], v[3], v[4]) for (n, c, L), v in AGG.items()], columns=['var', 'dia', 'act', 'L', 'n_seg', 'n_canc', 'n_fill', 'cost', 'pnl'])
pd.to_pickle(dict(R=R, A=A, ramas=BR, c_epoca=C_EPOCA, dhi=(DHI if STAMP != 'v2' else None), pool_n=len(POOL), proc=PROC), OUT + f'CXL_{TAG}.pkl.tmp'); os.replace(OUT + f'CXL_{TAG}.pkl.tmp', OUT + f'CXL_{TAG}.pkl')
print('ok CXL', TAG, {v: (int(x.n_fill.sum()), round(float(x.pnl.sum()), 1)) for v, x in A.groupby('var', sort=False)}, round(time.time() - T0, 1), 's', flush=True)
