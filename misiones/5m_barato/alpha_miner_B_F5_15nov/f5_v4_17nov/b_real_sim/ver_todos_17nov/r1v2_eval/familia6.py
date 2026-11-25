#!/usr/bin/env python3
"""familia6.py -- R1v2 FASE B (pendiente 6): max-statistic de la familia de 6 (V1 primaria c=0,02 mu_ucb; V2 c=0; V3 c=0,05; V4 mu_hat<-c c=0,02; V5 CXJ150; V6 E1b S1) con placebo C11 e inversion C4.
Estadistico = DeltaPnL (EUR, ordenes del 1.er relleno mercado-lado; positivo = perdida evitada) de cancelar las ordenes con >=1 punto que dispara Y efectivo (t + t_proc + L_cancel + 20 <= tf).
APROXIMACION DECLARADA: el DeltaPnL de placebo/inversion se calcula sobre la TABLA de puntos del replay base (post-hoc, sin re-armado: las ordenes posteriores del mismo mercado no se quitan); el EV primario sale del replay integrado
(replay_variantes). Placebo: se permutan los flags de disparo ENTRE puntos (orden,t) dentro de dia x moneda x suelo x nivel x tramo de T, con UNA permutacion conjunta para las 6 variantes (preserva el solape V5/V6),
K=1000, semilla 20261119, sin ventanas +-30 s. Inversion: el MISMO numero de ordenes canceladas por dia pero las de MAYOR puntuacion (solo V1-V4, que tienen puntuacion). p_max: max-statistic (variantes_b.p_max_permutacion).
V1-V4 = regla primaria (alta/repegado + gatillo F5, columnas es_alta/gate_f5); estratos del placebo incluyen suelo (lo/hi/indet de la tabla firmada) y es_alta.
Pts: DataFrame con dia, coin, suelo, nivel, tramoT, es_alta, gate_f5, ord (codigo int de orden), t, tf (NaN sin relleno), score_ucb, score_mu, fire_V5, fire_V6. Ord: pnl por codigo de orden (0 sin relleno)."""
import os, sys
import numpy as np, pandas as pd
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import variantes_b as VB
NOMBRES = ('V1', 'V2', 'V3', 'V4', 'V5', 'V6'); REGLAS = {'V1': ('score_ucb', 0.02), 'V2': ('score_ucb', 0.0), 'V3': ('score_ucb', 0.05), 'V4': ('score_mu', 0.02)}
K_PLACEBO = 1000; SEED = 20261119; STRATA = ('dia', 'coin', 'suelo', 'nivel', 'tramoT', 'es_alta')

def fire_matrix(P):
    """(n_puntos, 6) bool. V1-V4: puntuacion < -c (NaN -> False: no se cancela por rasgo no evaluable); V5/V6: flags de salto adverso."""
    cols = []; alta = P.es_alta.values.astype(bool); gate = P.gate_f5.values.astype(bool)
    for v in NOMBRES[:4]:      # V1-V4 = la regla PRIMARIA del hook: solo en alta/repegado (primer punto de cada orden), gatillo F5 (inval/alto) O regla E1; NaN de la regla -> no dispara por ella
        col, c = REGLAS[v]; s = P[col].values.astype(float); cols.append(alta & (gate | np.where(np.isnan(s), False, s < -c)))
    cols.append(P.fire_V5.values.astype(bool)); cols.append(P.fire_V6.values.astype(bool)); return np.stack(cols, axis=1)

def eff_mask(P, t_proc, l_cancel=VB.L_CANCEL['primaria']):
    tf = P.tf.values.astype(float); return np.isfinite(tf) & (P.t.values + t_proc + l_cancel <= tf - VB.MARGEN_CASADO_MS)

def eff_matrix(P, t_proc, l_cancel=VB.L_CANCEL['primaria']):
    """(n, 6) bool: V1-V4 no armar en el alta = no hay orden, sin latencia de cancelacion -> efectivo en todo punto de alta; V5/V6 (cancelacion en vida o no armar) usan eff_mask."""
    e = eff_mask(P, t_proc, l_cancel); a = P.es_alta.values.astype(bool); return np.stack([a, a, a, a, e | a, e | a], axis=1)

def delta_pnl(fire, eff, ord_code, pnl_ord):
    """DeltaPnL (EUR) por variante: -sum pnl de las ordenes canceladas a tiempo. fire (n,nv) bool; ord_code (n,) int en [0, len(pnl_ord)); pnl_ord (n_ord,)."""
    fire = np.asarray(fire, bool); out = []
    for j in range(fire.shape[1]):
        c = np.bincount(ord_code[fire[:, j] & (eff[:, j] if np.ndim(eff) == 2 else eff)], minlength=len(pnl_ord)) > 0; out.append(float(-np.asarray(pnl_ord)[c].sum()))
    return np.array(out)

def strata_ix(P, cols=STRATA): return [np.asarray(ix) for ix in P.groupby(list(cols), sort=False).indices.values()]

def nulos_placebo(fire, eff, ord_code, pnl_ord, strata, K=K_PLACEBO, seed=SEED):
    """(K, nv): DeltaPnL bajo placebo C11 con permutacion conjunta de las filas de flags dentro de cada estrato."""
    rng = np.random.default_rng(seed); fire = np.asarray(fire, bool); out = np.zeros((K, fire.shape[1]))
    for k in range(K):
        F = fire.copy()
        for ix in strata:
            if len(ix) > 1: F[ix] = fire[ix[rng.permutation(len(ix))]]
        out[k] = delta_pnl(F, eff, ord_code, pnl_ord)
    return out

def cancel_inversion(score, fire, eff, oc, dia_pts, n_ord):
    """Inversion C4 a nivel de ORDEN: mismo numero de ordenes canceladas POR DIA que la regla real (ordenes con >=1 punto que dispara y es efectivo), pero se eligen las de MAYOR puntuacion
    (puntuacion de la orden = minimo de sus puntos efectivos; NaN al final) entre las ordenes cancelables (>=1 punto efectivo). Devuelve bool (n_ord,) de ordenes canceladas. score (n,), fire/eff (n,) bool."""
    sc = np.where(np.isnan(score), -np.inf, score);      # NaN = puntuacion MAS BAJA (nunca se elige como 'la de mayor puntuacion')
    real = np.bincount(oc[fire & eff], minlength=n_ord) > 0; el = np.bincount(oc[eff], minlength=n_ord) > 0
    minsc = np.full(n_ord, np.inf); np.minimum.at(minsc, oc[eff], sc[eff]); dia_o = np.empty(n_ord, object); dia_o[oc] = dia_pts; out = np.zeros(n_ord, bool)
    for d in set(dia_o[el].tolist()):
        cand = np.where(el & (dia_o == d))[0]; n = int(real[cand].sum()); out[cand[np.argsort(-minsc[cand], kind='stable')[:n]]] = True
    return out

def evalua_familia(P, Ord, t_proc, K=K_PLACEBO, seed=SEED, l_cancel=VB.L_CANCEL['primaria']):
    """dict: obs (DeltaPnL por variante), p_ajustado y p_max (max-statistic sobre el placebo), p95 del placebo por variante, criterio_placebo (obs > p95), inversion (DeltaPnL con los de MAYOR mu) y su criterio (<=0 y < obs)."""
    P = P.reset_index(drop=True); oc = P.ord.values.astype(int); pnl = np.asarray(Ord.pnl, float); eff = eff_matrix(P, t_proc, l_cancel); F = fire_matrix(P)
    obs = delta_pnl(F, eff, oc, pnl); nul = nulos_placebo(F, eff, oc, pnl, strata_ix(P), K, seed); pm = VB.p_max_permutacion(obs, nul); p95 = np.percentile(nul, 95, axis=0)
    inv = []
    for j, v in enumerate(NOMBRES):
        if v in REGLAS: c_ = cancel_inversion(P[REGLAS[v][0]].values.astype(float), F[:, j], eff[:, j], oc, P.dia.values, len(pnl)); inv.append(float(-pnl[c_].sum()))
        else: inv.append(float('nan'))
    inv = np.array(inv)
    return dict(variantes=list(NOMBRES), obs=obs.tolist(), p_ajustado=pm['p_ajustado'], p_max=pm['p_max'], p95_placebo=p95.tolist(), criterio_placebo=(obs > p95).tolist(), inversion=inv.tolist(),
                criterio_inversion=[bool(np.isfinite(i) and i <= 0 and i < o) for i, o in zip(inv, obs)], K=K, seed=seed, n_puntos=int(len(P)), n_ordenes=int(len(pnl)),
                frecuencia_disparo={v: float(F[:, j].mean()) for j, v in enumerate(NOMBRES)}, aproximacion='DeltaPnL post-hoc sobre la tabla de puntos del replay base (sin re-armado); el EV primario es el del replay integrado')
