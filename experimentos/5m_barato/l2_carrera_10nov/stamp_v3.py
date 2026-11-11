#!/usr/bin/env python3
"""stamp_v3.py -- sello de cada print de la cinta on-chain en la FILA DE CONSUMO EXACTA del libro (firma token+precio+tamano unida por hash de tx a libro5_tx). Funciones puras, probadas en test_v3.py.
Relojes (CONTRATO_RELOJES.md): TODO EXCHANGE (t_ev del print = EX; filas q = EX). Se devuelve ademas el RX de la fila (solo para etiquetar 'cuando lo supimos', nunca para decidir aqui).
Firma (como causalidad_187ms/emparejado.py, que SE REUSA sin editar): event = (token k, tx) con p = pmax, S = suma de acciones del tx; ventana SIMETRICA +-W alrededor de t_ev (EX):
  npr==1 : 'dec'  = bid==p antes y despues y szb baja EXACTAMENTE S (+-TOLS)  |  'clr' = bid==p antes, bid<p despues y szb previo == S
  npr>=2 : una sola fila que salta de bid>=pmax a bid<=pmin (barrido)
Sello: exactamente 1 firma exacta y d_ex = t_ev - ex(fila) dentro de [GUARD_LO, GUARD_HI]  ->  tm = ex(fila) - 1 ms   (rama 'sig')
       2+ firmas (ambiguo) | 0 firmas (sin firma) | unica fuera de guardia              ->  tm = t_ev - c_epoca - 1 ms  (ramas 'amb', 'nosig', 'guard'); c_epoca = p50 de d_ex de las firmas unicas npr==1 del dia
       sin t_ev (tx sin fila en libro5_tx)                                              ->  rama 'sinev' (el llamador decide; legacy t_rx-63)."""
import numpy as np
W = 1500; TOLP = 0.0049; TOLS = 0.015; GUARD_LO, GUARD_HI = -50, 300


def sig_rows(B, Z, i0, i1, a, p, S, npr, pmin):
    """Indices absolutos (en los arrays B,Z del token, rows a..) de filas firma EXACTAS en [i0,i1), i>a. Misma logica que emparejado.sig_rows (solo exactas)."""
    i0 = max(i0, a + 1)
    if i1 <= i0: return np.array([], int)
    bp = B[i0 - 1:i1 - 1]; bc = B[i0:i1]; zp = Z[i0 - 1:i1 - 1]; zc = Z[i0:i1]
    if npr == 1:
        atp = np.abs(bp - p) < TOLP
        dec = atp & (np.abs(bc - p) < TOLP) & (np.abs((zp - zc) - S) <= TOLS)
        clr = atp & (bc < p - TOLP) & (np.abs(zp - S) <= TOLS)
        exact = dec | clr
    else:
        exact = (bp >= p - TOLP) & (bc <= pmin + TOLP)
    return np.where(exact)[0] + i0


def match_event(EX, B, Z, a, b, tev, p, S, npr, pmin):
    """EX/B/Z arrays del dia; token en [a,b); tev EX (ms, misma base que EX). Devuelve (n_exact, fila_unica_o_-1, d_ex_o_None). n_exact = firmas exactas en +-W."""
    e = EX[a:b]
    i0 = a + int(np.searchsorted(e, tev - W, 'left')); i1 = a + int(np.searchsorted(e, tev + W, 'right'))
    rows = sig_rows(B, Z, i0, i1, a, p, S, npr, pmin)
    n = len(rows)
    if n == 1: return 1, int(rows[0]), int(tev - EX[rows[0]])
    return n, -1, None


def epoch_const(d_ex_unique_npr1, default=20):
    """c_epoca = p50 de d_ex de las firmas unicas (npr==1, dentro de guardia) del dia; si <200 firmas se usa `default` (20 ms, medido 15 dias: p50 18-21)."""
    x = np.asarray([v for v in d_ex_unique_npr1 if GUARD_LO <= v <= GUARD_HI], float)
    return (int(round(float(np.median(x)))) if len(x) >= 200 else default)


def stamp_events(EX, B, Z, qb, ev_k, ev_tev, ev_p, ev_pmin, ev_S, ev_npr, default_c=20):
    """Bucle por evento. EX/B/Z: arrays q ordenados por (token, EX) en la MISMA base de tiempo que ev_tev; qb: limites por token. Devuelve (tm, rama, row, d_ex, c_epoca):
    tm int64 (EX), rama in {'sig','amb','nosig','guard','sinev'}, row = indice absoluto de la fila de consumo (o -1)."""
    n = len(ev_k); tm = np.zeros(n, np.int64); rama = np.empty(n, object); row = np.full(n, -1, np.int64); dex = np.full(n, np.nan); nex = np.zeros(n, np.int32)
    for i in range(n):
        if ev_tev[i] < 0: rama[i] = 'sinev'; continue
        k = int(ev_k[i]); a, b = int(qb[k]), int(qb[k + 1])
        if b - a < 3: rama[i] = 'nosig'; nex[i] = 0; continue
        ne, r, d = match_event(EX, B, Z, a, b, int(ev_tev[i]), float(ev_p[i]), float(ev_S[i]), int(ev_npr[i]), float(ev_pmin[i]))
        nex[i] = ne
        if ne == 1 and GUARD_LO <= d <= GUARD_HI: rama[i] = 'sig'; row[i] = r; dex[i] = d
        elif ne == 1: rama[i] = 'guard'
        elif ne >= 2: rama[i] = 'amb'
        else: rama[i] = 'nosig'
    ok = (rama == 'sig') & (np.asarray(ev_npr) == 1)
    c = epoch_const(dex[ok], default_c)
    for i in range(n):
        if rama[i] == 'sig': tm[i] = int(EX[row[i]]) - 1
        elif rama[i] != 'sinev': tm[i] = int(ev_tev[i]) - c - 1
    return tm, rama, row, dex, c, nex
