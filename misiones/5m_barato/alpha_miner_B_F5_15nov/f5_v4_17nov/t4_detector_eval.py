#!/usr/bin/env python3
"""t4_detector_eval.py [--grid] [--params W,C,rho,nmin,H] -- evalua el detector rapido (suelo_causal.lo_crudo/estado_lo) contra el p5 de 10 min (cache/clases_D.npz 'cls', causal) sobre los dias con cache/seg_D.npz.
VERDAD (SOLO validacion, mira hacia delante y atras): por bin de 10 s, f = filas con d<30 ms / filas, n>=100: 'lo' si f>=0,30; 'hi' si f<=0,01; si no 'amb'/'unk'. Regimen = tramo de bins lo|hi (>=3 bins seguidos); transicion T* = inicio del primer bin tras el ultimo bin del regimen anterior (cota CONSERVADORA del retraso: incluye zona ambigua).
Metricas por detector (estado lo/nolo por segundo): retraso lo->hi (1er segundo >= T* en nolo), hi->lo (1er segundo >= T* en lo), segundos 'lo' con verdad hi pasado T*+retraso... = lo-en-hi; episodios; perdida de cobertura (verdad lo con estado nolo);
EUR de la poblacion F5 (prints ALL3 + BTC, t=r_ex-83 ms) con estado lo y verdad hi (exposicion) y en la ventana de deteccion. Salida: T4_detector.txt/.json. GRID: seleccion en dias <= 2026-10-25, hold-out > 25-Oct."""
import os, sys, json, glob, itertools, numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import suelo_causal as SC
C4 = HERE + '/cache/'; EXPC = '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/exp1/cache/'
DIAS = sorted(os.path.basename(p)[4:14] for p in glob.glob(C4 + 'seg_2026-*.npz') if os.path.exists(C4 + 'clases_' + os.path.basename(p)[4:14] + '.npz'))
NL30 = SC.nbandas_bajo(30)
def verdad(S):
    """-> (v (8640,) int8: 1 lo, 0 hi, -1 amb/unk), con tramos >=3 bins."""
    n = S.reshape(8640, 10, -1).sum((1)).sum(1); l = S[:, :NL30].reshape(8640, 10, -1).sum(1).sum(1); f = l / np.maximum(n, 1)
    v = np.full(8640, -1, np.int8); v[(n >= 100) & (f >= 0.30)] = 1; v[(n >= 100) & (f <= 0.01)] = 0
    for val in (0, 1):                                              # quita tramos de <3 bins
        m = v == val; d = np.diff(np.concatenate([[0], m.astype(int), [0]])); a, b = np.where(d == 1)[0], np.where(d == -1)[0]
        for x, y in zip(a, b):
            if y - x < 3: v[x:y] = -1
    return v
def transiciones(v):
    """lista (T*_bin, tipo) tipo 'lohi'|'hilo': entre tramos consecutivos de regimen distinto; T* = bin siguiente al ultimo bin del regimen anterior."""
    idx = np.where(v >= 0)[0]; out = []
    for a, b in zip(idx[:-1], idx[1:]):
        if v[a] != v[b]: out.append((a + 1, 'lohi' if v[a] == 1 else 'hilo', b))
    return out
def estado_rapido(S, p): return SC.estado_lo(SC.lo_crudo(S, p), p)
def estado_p5(cls): return np.repeat(cls == 'lo', 10)
def eval_dia(S, cls, v, p=None, pob=None, day0=0):
    st = estado_p5(cls) if p is None else estado_rapido(S, p); vs = np.repeat(v, 10); R = dict(ret_lohi=[], ret_hilo=[], sin_det=0)
    for T, tipo, b in transiciones(v):
        t0 = T * 10; t1 = b * 10                                           # t1 = inicio del primer bin del nuevo regimen conocido
        seg = st[t0:min(t0 + 3600, 86400)]; w = np.where(~seg)[0] if tipo == 'lohi' else np.where(seg)[0]
        (R['ret_lohi'] if tipo == 'lohi' else R['ret_hilo']).append(int(w[0]) if len(w) else 3600)
    hi = vs == 0; lo = vs == 1
    R['seg_hi'] = int(hi.sum()); R['seg_lo'] = int(lo.sum()); R['lo_en_hi'] = int((st & hi).sum()); R['nolo_en_lo'] = int((~st & lo).sum())
    ep = np.diff(np.concatenate([[0], (st & hi).astype(int)])); R['episodios_lo_en_hi'] = int((ep == 1).sum())
    R['transiciones'] = len(transiciones(v)); R['st'] = st; R['vs'] = vs
    return R
def carga_pob(d):
    ps = []
    for pk in (EXPC + f'{d}_pob_add3.pkl.gz', C4 + f'btc_pob_{d}.pkl.gz'):
        if os.path.exists(pk):
            try: X = pd.read_pickle(pk, compression='gzip')[['r_ex', 'coste', 'pnl']]; ps.append(X)
            except Exception: pass
    return pd.concat(ps, ignore_index=True) if ps else None
def eur_ventanas(R, pob, d):
    """EUR de prints con estado lo y verdad hi (exposicion) y en la ventana de deteccion (entre T* y el 1er nolo)."""
    if pob is None or len(pob) == 0: return dict(n=0, coste=0., pnl=0., n_vent=0, coste_vent=0., pnl_vent=0., n_pob=0, coste_pob=0.)
    day0 = int(pd.Timestamp(d + 'T00:00:00Z').value // 10**6); s = ((pob.r_ex.values.astype(np.int64) - 83 - day0) // 1000); ok = (s >= 0) & (s < 86400); s = np.clip(s, 0, 86399)
    m = ok & R['st'][s] & (R['vs'][s] == 0); c = pob.coste.values.astype(float); p = pob.pnl.values.astype(float)
    mv = np.zeros(len(pob), bool)
    for T, tipo, b in R['trans']:
        if tipo != 'lohi': continue
        t0 = T * 10; w = np.where(~R['st'][t0:min(t0 + 3600, 86400)])[0]; t1 = t0 + (w[0] if len(w) else 3600); mv |= ok & (s >= t0) & (s < t1)
    return dict(n=int(m.sum()), coste=float(c[m].sum()), pnl=float(p[m].sum()), n_vent=int(mv.sum()), coste_vent=float(c[mv].sum()), pnl_vent=float(p[mv].sum()), n_pob=int(ok.sum()), coste_pob=float(c[ok].sum()))
def resume(lst):
    a = np.array(lst, float); return dict(n=len(a), mediana=float(np.median(a)) if len(a) else None, p90=float(np.percentile(a, 90)) if len(a) else None, max=float(a.max()) if len(a) else None)
def correr(p, dias, con_eur=False):
    T = dict(ret_lohi=[], ret_hilo=[], lo_en_hi=0, seg_hi=0, seg_lo=0, nolo_en_lo=0, ep=0, trans=0, eur=dict(n=0, coste=0., pnl=0., n_vent=0, coste_vent=0., pnl_vent=0., n_pob=0, coste_pob=0.), por_dia={})
    for d in dias:
        S = np.load(C4 + f'seg_{d}.npz')['S']; cls = np.load(C4 + f'clases_{d}.npz', allow_pickle=True)['cls'].astype(str); v = verdad(S); R = eval_dia(S, cls, v, p); R['trans'] = transiciones(v)
        T['ret_lohi'] += R['ret_lohi']; T['ret_hilo'] += R['ret_hilo']
        for k, kk in (('lo_en_hi', 'lo_en_hi'), ('seg_hi', 'seg_hi'), ('seg_lo', 'seg_lo'), ('nolo_en_lo', 'nolo_en_lo'), ('ep', 'episodios_lo_en_hi'), ('trans', 'transiciones')): T[k] += R[kk]
        T['por_dia'][d] = dict(trans=R['transiciones'], lo_en_hi=R['lo_en_hi'], seg_hi=R['seg_hi'], ep=R['episodios_lo_en_hi'], nolo_en_lo=R['nolo_en_lo'], seg_lo=R['seg_lo'])
        if con_eur:
            e = eur_ventanas(R, carga_pob(d), d)
            for k, x in e.items(): T['eur'][k] += x
            T['por_dia'][d]['eur_lo_en_hi'] = e['coste']
    return T
def linea(nombre, T):
    r1, r2 = resume(T['ret_lohi']), resume(T['ret_hilo']); f = lambda r: f"n={r['n']} med {r['mediana']:.0f}/p90 {r['p90']:.0f}/max {r['max']:.0f} s" if r['n'] else 'n=0'
    nd = len(T['por_dia']); e = T['eur']
    return (f"{nombre:<26} lo->hi: {f(r1)} | hi->lo: {f(r2)} | seg lo-en-hi {T['lo_en_hi']} de {T['seg_hi']} ({100 * T['lo_en_hi'] / max(T['seg_hi'], 1):.2f} %), episodios {T['ep']} ({T['ep'] / nd:.2f}/dia) | cobertura perdida {100 * T['nolo_en_lo'] / max(T['seg_lo'], 1):.2f} % de {T['seg_lo']} s lo"
            + (f" | EUR prints en lo-en-hi: n={e['n']} coste {e['coste']:.2f} pnl {e['pnl']:+.2f}; en ventana de deteccion lo->hi: n={e['n_vent']} coste {e['coste_vent']:.2f} pnl {e['pnl_vent']:+.2f} (poblacion n={e['n_pob']}, coste {e['coste_pob']:.0f})" if e['n_pob'] else ''))
if __name__ == '__main__':
    if '--grid' in sys.argv:
        dev = [d for d in DIAS if d <= '2026-10-25']; res = []
        for W, C, rho, nmin, H in itertools.product((1, 2, 3, 5), (26, 30, 36), (0.02, 0.05, 0.1, 0.2), (10, 20, 40), (1, 2, 3, 5)):
            p = SC.ParamsDetector(W, C, rho, nmin, H); T = correr(p, dev); r1, r2 = resume(T['ret_lohi']), resume(T['ret_hilo'])
            res.append(dict(p=repr(p), lohi_med=r1['mediana'], lohi_p90=r1['p90'], lohi_max=r1['max'], hilo_med=r2['mediana'], hilo_p90=r2['p90'], lo_en_hi=T['lo_en_hi'], ep=T['ep'], cob_perdida=T['nolo_en_lo'] / max(T['seg_lo'], 1), ntr=T['trans']))
        json.dump(res, open(HERE + '/T4_grid_dev.json', 'w'), indent=0); print('grid', len(res), 'dev dias', len(dev)); sys.exit(0)
    ps = [float(x) for x in sys.argv[sys.argv.index('--params') + 1].split(',')]; p = SC.ParamsDetector(int(ps[0]), int(ps[1]), ps[2], int(ps[3]), int(ps[4]))
    for nm, pp in (('p5 10 min (v4)', None), (repr(p), p)): print(linea(nm, correr(pp, DIAS, con_eur=True)))
