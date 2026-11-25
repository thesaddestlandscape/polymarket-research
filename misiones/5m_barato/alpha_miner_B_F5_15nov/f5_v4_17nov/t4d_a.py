#!/usr/bin/env python3
"""t4d_a.py (paso 1d-A, 17-Nov). Detector adoptado W12 C30 rho0,07 nmin5 H1 (salida inmediata). (1) EUR de la oportunidad lo perdida (regla F5: tipo B, tercil bajo p60, cat ok; poblacion ajena; t=r_ex-83 ms).
(2) MEMORIA CAUSAL: si el ultimo estado fue lo con evidencia fuerte (fraccion d<30 >= 3*rho en el ultimo segundo con crudo True) y NO hay evidencia de hi (evidencia de hi = ventana con n >= NH=3 filas y fraccion < rho), mantiene lo hasta N s desde el ultimo crudo True. Cualquier evidencia de hi => nolo inmediato.
Uso: python3 -I t4d_a.py  -> T4d_A.txt/json. Sin lookahead: el segundo t usa solo [t-W,t-1]."""
import os, sys, json, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import suelo_causal as SC, t4b_eval as T, t4c_eval as C
P = SC.ParamsDetector(12, 30, 0.07, 5, 1); NH = 3; NS = (0, 5, 10, 20, 30, 60, 120, 300)
def ventana(S, p):
    X = np.vstack([np.zeros((p.W, SC.NBAND), np.int64), S.astype(np.int64)]); nl = SC.nbandas_bajo(p.C)
    tot = np.cumsum(np.concatenate([[0], X.sum(1)])); low = np.cumsum(np.concatenate([[0], X[:, :nl].sum(1)])); t = np.arange(S.shape[0]) + p.W
    return tot[t] - tot[t - p.W], low[t] - low[t - p.W]
def estado_mem(n, c, p, N, nh=NH):
    ns = len(n); st = np.zeros(ns, bool); crudo = (n >= p.nmin) & (c >= p.rho * np.maximum(n, 1)); hi = (n >= nh) & (c < p.rho * n); last = -10**9; fuerte = False; prev = False
    for t in range(ns):
        if crudo[t]: last = t; fuerte = c[t] >= 3 * p.rho * n[t]; s = True
        elif N > 0 and prev and fuerte and not hi[t] and t - last <= N: s = True
        else: s = False
        st[t] = s; prev = s
    return st
if __name__ == '__main__':
    DAYS = [T.Dia(d) for d in T.DIAS]; dev = [D for D in DAYS if D.d <= T.CORTE]; ho = [D for D in DAYS if D.d > T.CORTE]; NC = {D.d: ventana(D.S, P) for D in DAYS}; POB = {D.d: T.carga_pob(D.d) for D in DAYS}
    L = [f'# T4d-A detector {P!r}; memoria causal N (s) con decaimiento por fuerza de evidencia; NH={NH}; dev {len(dev)} / hold-out {len(ho)} dias'] ; out = {}
    for N in NS:
        sts = {D.d: estado_mem(*NC[D.d], P, N) for D in DAYS}; line = []
        for nm, g in (('DEV', dev), ('HO', ho), ('TODOS', DAYS)):
            A = T.agrega([T.metricas_dia(D, sts[D.d]) for D in g]); cel = {}; nd = 0
            for D in g:
                X = POB[D.d]
                if X is None or len(X) == 0: continue
                nd += 1; ce = T.celdas_eur(D, X, sts[D.d])
                for k, v in ce.items():
                    a = cel.setdefault(k, [0, 0., 0.]); a[0] += v['n']; a[1] += v['coste']; a[2] += v['pnl']
            out[f'N{N}_{nm}'] = dict(A={k: v for k, v in A.items() if not isinstance(v, list)}, cel=cel)
            line.append(f"{nm}: lo_en_hi {A['lo_en_hi']} s ({A['ep_lo_en_hi']} ep) nolo_en_lo {A['nolo_en_lo']} s ({100 * A['nolo_en_lo'] / A['seg_lo']:.2f} %) lohi miss {A['lohi_miss']}/{A['lohi_n']} p90 {T.pq(A['lohi'], 90)} | EUR nolo&verdad_lo n={cel['nolo_lo'][0]} {cel['nolo_lo'][1]:.0f} EUR pnl {cel['nolo_lo'][2]:+.0f} ; lo&verdad_hi n={cel['lo_hi'][0]} {cel['lo_hi'][1]:.0f} EUR pnl {cel['lo_hi'][2]:+.0f} ({nd} dias con poblacion)")
        L.append(f'N={N:>3}  ' + '\n        '.join(line))
    json.dump(out, open(HERE + '/T4d_A.json', 'w')); open(HERE + '/T4d_A.txt', 'w').write('\n'.join(L) + '\n'); print('\n'.join(x[:700] for x in L))
