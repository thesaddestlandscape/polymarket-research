#!/usr/bin/env python3
"""t4b_eval.py --grid | --params W,C,rho,nmin,H [--tag X]  (17-Nov, tarea 2 de Javi; corrige t4_detector_eval.py: el retraso se CENSURA al fin del regimen y se reporta la tasa de deteccion).
Detector rapido = suelo_causal.lo_crudo/estado_lo (causal: segundo t usa solo segundos [t-W,t-1] completos, reloj RX). Baseline = clase 'lo' pura del p5 de 10 min v4 (cache/clases_D.npz, ya causal).
VERDAD (SOLO validacion, mira atras y adelante, no es un detector): por bin de 10 s f = filas d<30 ms / filas con n>=100: lo si f>=0,30; hi si f<=0,01; si no ambiguo; tramos <3 bins se anulan.
Transicion = entre tramos lo|hi consecutivos; T* = bin siguiente al ultimo bin del regimen anterior (cota conservadora: incluye zona ambigua). Ventana de deteccion = [T*, fin del regimen nuevo) con tope 3600 s.
 retraso lo->hi: 1er segundo de la ventana con estado 'nolo' (no detectado = ninguno). retraso hi->lo: 1er segundo con estado 'lo'.
 lo_en_hi = segundos con estado lo y verdad hi (exposicion peligrosa); nolo_en_lo = segundos con estado nolo y verdad lo (oportunidad perdida por fail-closed). Episodios = rachas contiguas.
EUR: poblacion F5 (ADD3 ETH/SOL/XRP en exp1/cache + BTC en cache/btc_pob), regla vigente = tipo B (bid_p60 >= q+0,0099) y F5_p60 <= C0 (tercil bajo, cortes TRAIN congelados) y cat_p60==0; t = r_ex-83 ms (como SPEC).
 Compuerta: operar solo con estado lo. Celdas estado x verdad. 0 ordenes, nada en data/. GRID en dias <= 2026-10-25 (calibracion), resto = hold-out; criterio declarado ANTES: min (lo_en_hi_s + nolo_en_lo_s) sobre dev."""
import os, sys, json, glob, itertools, numpy as np, pandas as pd
from scipy import stats
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import suelo_causal as SC
C4 = HERE + '/cache/'; EXPC = '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/exp1/cache/'; C0 = 3.526360511779785
NL30 = SC.nbandas_bajo(30); CORTE = '2026-10-25'
DIAS = sorted(os.path.basename(p)[4:14] for p in glob.glob(C4 + 'seg_2026-*.npz') if os.path.exists(C4 + 'clases_' + os.path.basename(p)[4:14] + '.npz'))
def verdad(S):
    n = S.reshape(8640, 10, -1).sum(1).sum(1); l = S[:, :NL30].reshape(8640, 10, -1).sum(1).sum(1); f = l / np.maximum(n, 1)
    v = np.full(8640, -1, np.int8); v[(n >= 100) & (f >= 0.30)] = 1; v[(n >= 100) & (f <= 0.01)] = 0
    for val in (0, 1):
        m = v == val; d = np.diff(np.concatenate([[0], m.astype(int), [0]])); a, b = np.where(d == 1)[0], np.where(d == -1)[0]
        for x, y in zip(a, b):
            if y - x < 3: v[x:y] = -1
    return v
def tramos(v):
    """lista de (ini_bin, fin_bin_excl, reg) de tramos de regimen (reg 1 lo, 0 hi)."""
    out = []; i = 0
    while i < len(v):
        if v[i] < 0: i += 1; continue
        j = i
        while j < len(v) and v[j] == v[i]: j += 1
        out.append((i, j, int(v[i]))); i = j
    return out
def transiciones(v):
    tr = tramos(v); out = []
    for k in range(len(tr) - 1):
        a, b = tr[k], tr[k + 1]
        if a[2] != b[2]: out.append(dict(T=a[1] * 10, tipo='lohi' if a[2] == 1 else 'hilo', fin=(tr[k + 2][0] * 10 if k + 2 < len(tr) else 86400)))   # nuevo regimen dura hasta el inicio del tramo siguiente (cota)
    return out
class Dia:
    def __init__(s, d):
        s.d = d; s.S = np.load(C4 + f'seg_{d}.npz')['S']; s.cls = np.load(C4 + f'clases_{d}.npz', allow_pickle=True)['cls'].astype(str)
        s.v = verdad(s.S); s.vs = np.repeat(s.v, 10); s.tr = transiciones(s.v); s.st_p5 = np.repeat(s.cls == 'lo', 10)
def runs(x):
    d = np.diff(np.concatenate([[0], x.astype(int), [0]])); return int((d == 1).sum())
def metricas_dia(D, st):
    R = dict(lohi=[], hilo=[], lohi_miss=0, hilo_miss=0, lohi_n=0, hilo_n=0)
    for t in D.tr:
        a = t['T']; b = min(t['fin'], a + 3600); seg = st[a:b]; w = np.where(~seg)[0] if t['tipo'] == 'lohi' else np.where(seg)[0]
        R[t['tipo'] + '_n'] += 1
        if len(w): R[t['tipo']].append(int(w[0]))
        else: R[t['tipo'] + '_miss'] += 1
    hi = D.vs == 0; lo = D.vs == 1
    R.update(seg_hi=int(hi.sum()), seg_lo=int(lo.sum()), lo_en_hi=int((st & hi).sum()), nolo_en_lo=int((~st & lo).sum()), ep_lo_en_hi=runs(st & hi), ep_nolo_en_lo=runs(~st & lo), seg_lo_det=int((st & lo).sum())); return R
def agrega(rs):
    A = dict(lohi=[], hilo=[]);
    for r in rs:
        A['lohi'] += r['lohi']; A['hilo'] += r['hilo']
    for k in ('lohi_miss', 'hilo_miss', 'lohi_n', 'hilo_n', 'seg_hi', 'seg_lo', 'lo_en_hi', 'nolo_en_lo', 'ep_lo_en_hi', 'ep_nolo_en_lo', 'seg_lo_det'): A[k] = sum(r[k] for r in rs)
    A['dias'] = len(rs); return A
def pq(x, q): return float(np.percentile(x, q)) if len(x) else None
def linea(nm, A):
    f = lambda k: f"{k} n={A[k + '_n']} detectadas {A[k + '_n'] - A[k + '_miss']} ({100 * (A[k + '_n'] - A[k + '_miss']) / max(A[k + '_n'], 1):.0f} %) retraso p50/p90 {pq(A[k], 50)}/{pq(A[k], 90)} s"
    return (f"{nm:<24} {f('lohi')} | {f('hilo')} | lo-en-hi {A['lo_en_hi']} s de {A['seg_hi']} ({100 * A['lo_en_hi'] / max(A['seg_hi'], 1):.2f} %), {A['ep_lo_en_hi']} episodios ({A['ep_lo_en_hi'] / A['dias']:.2f}/dia) | nolo-en-lo {A['nolo_en_lo']} s de {A['seg_lo']} ({100 * A['nolo_en_lo'] / max(A['seg_lo'], 1):.2f} %), {A['ep_nolo_en_lo']} episodios ({A['ep_nolo_en_lo'] / A['dias']:.2f}/dia)")
def carga_pob(d):
    ps = []
    for pk in (EXPC + f'{d}_pob_add3.pkl.gz', C4 + f'btc_pob_{d}.pkl.gz'):
        if os.path.exists(pk):
            try: ps.append(pd.read_pickle(pk, compression='gzip')[['r_ex', 'q', 'F5_p60', 'bid_p60', 'cat_p60', 'coste', 'pnl', 'coin']])
            except Exception: pass
    if not ps: return None
    X = pd.concat(ps, ignore_index=True); m = (X.cat_p60 == 0) & np.isfinite(X.F5_p60) & (X.F5_p60 <= C0) & np.isfinite(X.bid_p60) & ((X.bid_p60 - X.q) >= 0.0099 - 1e-12)
    return X[m]
def celdas_eur(D, X, st):
    """-> dict con coste/pnl/n por (estado lo|nolo) x (verdad lo|hi|amb)."""
    day0 = int(pd.Timestamp(D.d + 'T00:00:00Z').value // 10**6); s = (X.r_ex.values.astype(np.int64) - 83 - day0) // 1000; ok = (s >= 0) & (s < 86400); s = np.clip(s, 0, 86399)
    ve = np.where(D.vs[s] == 1, 'lo', np.where(D.vs[s] == 0, 'hi', 'amb')); es = np.where(st[s], 'lo', 'nolo'); c = X.coste.values.astype(float); p = X.pnl.values.astype(float); out = {}
    for e in ('lo', 'nolo'):
        for v in ('lo', 'hi', 'amb'):
            m = ok & (es == e) & (ve == v); out[f'{e}_{v}'] = dict(n=int(m.sum()), coste=float(c[m].sum()), pnl=float(p[m].sum()))
    out['total'] = dict(n=int(ok.sum()), coste=float(c[ok].sum()), pnl=float(p[ok].sum())); return out
def t_ic(x):
    x = np.asarray(x, float); n = len(x)
    if n < 3: return None
    se = x.std(ddof=1) / np.sqrt(n); return float(x.mean() - stats.t.ppf(0.95, n - 1) * se), float(x.mean() + stats.t.ppf(0.95, n - 1) * se), float(x.mean())
def eur(dias, st_fn, tag):
    """por dia: pnl de la regla F5 con compuerta (solo estado lo) y celdas. Devuelve filas por dia."""
    rows = []
    for D in dias:
        X = carga_pob(D.d)
        if X is None or len(X) == 0: continue
        rows.append((D.d, celdas_eur(D, X, st_fn(D))))
    return rows
def informe_eur(rows_p5, rows_fast, nm_f):
    L = []; dd = [d for d, _ in rows_p5]
    def S(rows, k, f): return np.array([r[k][f] for _, r in rows], float)
    for nm, rows in (('p5 10 min', rows_p5), (nm_f, rows_fast)):
        tot = {k: sum(r[k]['coste'] for _, r in rows) for k in rows[0][1]}; pn = {k: sum(r[k]['pnl'] for _, r in rows) for k in rows[0][1]}; nn = {k: sum(r[k]['n'] for _, r in rows) for k in rows[0][1]}
        L.append(f"{nm:<24} regla F5 ({len(rows)} dias con poblacion; n total {nn['total']}, coste {tot['total']:.0f}, pnl {pn['total']:+.0f}); celdas estado_verdad: " + ' | '.join(f"{k} n={nn[k]} coste {tot[k]:.0f} pnl {pn[k]:+.0f} EV {pn[k] / tot[k] if tot[k] else float('nan'):+.3f}" for k in rows[0][1] if k != 'total'))
    gp = lambda rows: np.array([sum(r[k]['pnl'] for k in ('lo_lo', 'lo_hi', 'lo_amb')) for _, r in rows]); gc = lambda rows: np.array([sum(r[k]['coste'] for k in ('lo_lo', 'lo_hi', 'lo_amb')) for _, r in rows])
    dp = gp(rows_fast) - gp(rows_p5); ic = t_ic(dp)
    L.append(f"COMPUERTA (operar solo con estado lo): pnl p5 {gp(rows_p5).sum():+.0f} (coste {gc(rows_p5).sum():.0f}, EV {gp(rows_p5).sum() / gc(rows_p5).sum():+.4f}) vs rapido {gp(rows_fast).sum():+.0f} (coste {gc(rows_fast).sum():.0f}, EV {gp(rows_fast).sum() / gc(rows_fast).sum():+.4f}); diferencia por dia (rapido - p5) media {dp.mean():+.1f} EUR/dia, IC90 dias {None if ic is None else (round(ic[0], 1), round(ic[1], 1))}, dias+ {(dp > 0).sum()}/{len(dp)}, sin 2 mejores {np.sort(dp)[:-2].mean():+.1f}")
    return L
def grid(dias):
    rows = []
    for W, C, rho, nmin, H in itertools.product((1, 2, 3, 5), (26, 30, 36), (0.02, 0.05, 0.1, 0.2), (10, 20, 40), (1, 2, 3, 5)):
        p = SC.ParamsDetector(W, C, rho, nmin, H); A = agrega([metricas_dia(D, SC.estado_lo(SC.lo_crudo(D.S, p), p)) for D in dias])
        rows.append(dict(p=repr(p), W=W, C=C, rho=rho, nmin=nmin, H=H, score=A['lo_en_hi'] + A['nolo_en_lo'], lo_en_hi=A['lo_en_hi'], nolo_en_lo=A['nolo_en_lo'], lohi_miss=A['lohi_miss'], lohi_n=A['lohi_n'], lohi_p50=pq(A['lohi'], 50), lohi_p90=pq(A['lohi'], 90), hilo_p50=pq(A['hilo'], 50), hilo_p90=pq(A['hilo'], 90), ep_lo_en_hi=A['ep_lo_en_hi']))
    return sorted(rows, key=lambda r: (r['score'], r['H'], r['W']))
if __name__ == '__main__':
    arg = lambda k, d=None: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    DAYS = [Dia(d) for d in DIAS]; dev = [D for D in DAYS if D.d <= CORTE]; ho = [D for D in DAYS if D.d > CORTE]
    if '--grid' in sys.argv:
        g = grid(dev); json.dump(g, open(HERE + '/T4b_grid_dev.json', 'w'), indent=0); print('dev dias', len(dev), 'configs', len(g)); [print(r) for r in g[:8]]; sys.exit(0)
    ps = arg('--params').split(','); p = SC.ParamsDetector(int(ps[0]), int(ps[1]), float(ps[2]), int(ps[3]), int(ps[4])); tag = arg('--tag', 'sel')
    st_f = lambda D: SC.estado_lo(SC.lo_crudo(D.S, p), p); st_p = lambda D: D.st_p5; L = [f'# T4b detector rapido {p!r}; dias seg {len(DAYS)} ({DAYS[0].d}..{DAYS[-1].d}); dev (calibracion) {len(dev)} dias <= {CORTE}, hold-out {len(ho)} dias']
    for nm, grp in (('DEV', dev), ('HOLD-OUT', ho), ('TODOS', DAYS)):
        L.append(f'## {nm} ({len(grp)} dias)'); L.append(linea('p5 10 min (v4)', agrega([metricas_dia(D, st_p(D)) for D in grp]))); L.append(linea(repr(p), agrega([metricas_dia(D, st_f(D)) for D in grp])))
        rp, rf = eur(grp, st_p, 'p5'), eur(grp, st_f, 'f'); L += informe_eur(rp, rf, repr(p))
    open(HERE + f'/T4b_{tag}.txt', 'w').write('\n'.join(L) + '\n'); print('\n'.join(x[:1500] for x in L))
