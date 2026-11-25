#!/usr/bin/env python3
"""t4d_a2.py (1d-A (i)): detector adoptado con evidencia ampliada (suma de cuentas por segundo y banda de varias fuentes del WS: base + g0 q 5min fuera de banda + g1 prints 5min + g2 q m15_registro). VERDAD fija = la de la base (D.vs), para comparar manzanas con manzanas.
Mide lo-en-hi, nolo-en-lo, retraso lo->hi/hi->lo y EUR de la regla F5 (poblacion, t=r_ex-83) en nolo con verdad lo / lo con verdad hi, dev <= 25-Oct y hold-out. Con y sin memoria causal N. Solo dias con seg2."""
import os, sys, glob, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import suelo_causal as SC, t4b_eval as T, t4d_a as A
dias = [d for d in T.DIAS if os.path.exists(HERE + f'/cache/seg2_{d}.npz')]; DAYS = [T.Dia(d) for d in dias]; Z = {D.d: np.load(HERE + f'/cache/seg2_{D.d}.npz')['Z'] for D in DAYS}; POB = {D.d: T.carga_pob(D.d) for D in DAYS}
dev = [D for D in DAYS if D.d <= T.CORTE]; ho = [D for D in DAYS if D.d > T.CORTE]; L = [f'# T4d-A(i) evidencia ampliada; dias con seg2: {len(DAYS)} (dev {len(dev)}, hold-out {len(ho)}); verdad = base d<30']
FUENT = (('base (q 5min en banda)', ()), ('+g0 q 5min fuera de banda', (0,)), ('+g0+g1 (y prints)', (0, 1)), ('+g2 (q m15/60m)', (2,)), ('+g0+g1+g2 (todas)', (0, 1, 2)))
for pnm, P in (('W12 C30 rho.07 nmin5', SC.ParamsDetector(12, 30, 0.07, 5, 1)), ('W12 C30 rho.07 nmin10', SC.ParamsDetector(12, 30, 0.07, 10, 1)), ('W12 C30 rho.07 nmin20', SC.ParamsDetector(12, 30, 0.07, 20, 1))):
    for fn, gs in FUENT:
        for N in (0, 60):
            sts = {}
            for D in DAYS:
                S = D.S.astype(np.int64)
                for g in gs: S = S + Z[D.d][g]
                n, c = A.ventana(S, P); sts[D.d] = A.estado_mem(n, c, P, N) if N else SC.estado_lo(SC.lo_crudo(S, P), P)
            line = []
            for nm, grp in (('DEV', dev), ('HO', ho)):
                Ag = T.agrega([T.metricas_dia(D, sts[D.d]) for D in grp]); cel = {}
                for D in grp:
                    X = POB[D.d]
                    if X is None or len(X) == 0: continue
                    for k, v in T.celdas_eur(D, X, sts[D.d]).items(): a = cel.setdefault(k, [0, 0., 0.]); a[0] += v['n']; a[1] += v['coste']; a[2] += v['pnl']
                line.append(f"{nm}: lo_en_hi {Ag['lo_en_hi']} s/{Ag['ep_lo_en_hi']} ep, nolo_en_lo {Ag['nolo_en_lo']} s ({100 * Ag['nolo_en_lo'] / max(Ag['seg_lo'], 1):.2f} %), lohi miss {Ag['lohi_miss']}/{Ag['lohi_n']} p50/p90 {T.pq(Ag['lohi'], 50)}/{T.pq(Ag['lohi'], 90)}, hilo p50/p90 {T.pq(Ag['hilo'], 50)}/{T.pq(Ag['hilo'], 90)}, cancel/dia {np.mean([(np.diff(sts[D.d].astype(int)) == -1).sum() for D in grp]):.0f}; EUR nolo&lo {cel['nolo_lo'][1]:.0f} (n={cel['nolo_lo'][0]}, pnl {cel['nolo_lo'][2]:+.0f}), lo&hi {cel['lo_hi'][1]:.0f} (n={cel['lo_hi'][0]}, pnl {cel['lo_hi'][2]:+.0f})")
            L.append(f'[{pnm}] {fn:<28} N={N:>2}  ' + ' || '.join(line))
open(HERE + '/T4d_A2.txt', 'w').write('\n'.join(L) + '\n'); print('\n'.join(x[:760] for x in L))
