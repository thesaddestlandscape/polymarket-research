#!/usr/bin/env python3
"""rf5_k6.py -- ESPEC E6 (ADENDA_RF5_K6_CALMA_v2): reserva de alfa K1-K4 / K6, gate de K6 y comprobaciones estructurales (particion exhaustiva, Calma∩F3=0, K6 sin Calma == K1, dias evaluables). Funciones PURAS sobre ordenes de la simulacion;
la politica K6 (K1 + Calma-T1) la produce el hook de Calma del juez v4 (PENDIENTE: ver cola). Ninguna cifra Calma del forward viejo cuenta. 0 ordenes, 0 red."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/")
import numpy as np, pandas as pd

def alfas(k1_ev_positivo, mirada=1):
    """UMBRALES p VINCULANTES (Pocock-LD, ADENDA_RF5_INTERINA_24nov sec.6 D1; unica fuente: rf5_fronteras.UMBRAL). mirada 1 = 6.o dia valido, mirada 2 = FINAL (10.o). K1-K4 0,02834 | 0,02171; K6 0,00709 | 0,00470 (0,03543 | 0,02792 si K1 = COMBINADA_EV_POSITIVO).
    La mirada de 20 dias esta SUPRIMIDA: ya no hay alfa a mitad."""
    import rf5_fronteras as FR
    return dict(K1_K4=FR.umbral_p('K1_K4', mirada), K6=FR.umbral_p('K6', mirada, 0.05 if k1_ev_positivo else 0.01), nota='K6 con alfa 0,05 solo si K1 = COMBINADA_EV_POSITIVO (grafo Bretz firmado)')

def dias_k6(dias_validos_rf5, dias_calma_ok, max_no_evaluable=0.20):
    """dias de K6 = interseccion de evaluables; NO_EVALUABLE fijado por el manifest de entradas ANTES del EV; > 20 % de los dias validos RF5 => K6 INSUFFICIENT."""
    dv = sorted(set(dias_validos_rf5)); ev = [d for d in dv if d in set(dias_calma_ok)]; no_ev = [d for d in dv if d not in set(dias_calma_ok)]
    frac = (len(no_ev) / len(dv)) if dv else 1.0
    return dict(dias=ev, no_evaluables=no_ev, frac_no_evaluable=frac, estado=('INSUFFICIENT' if (not dv or frac > max_no_evaluable) else 'OK'))

REGLAS = ('F3', 'V5', 'V6', 'Calma', 'ninguna')
def particion_exhaustiva(O):
    """O: una fila por orden con primera_regla in REGLAS (la PRIMERA que cancela/veta) y columnas bool 'tambien_F3','tambien_V5','tambien_V6','tambien_Calma', n=1, coste, pnl. Devuelve la tabla por regla y comprueba que n, coste y pnl SUMAN el total (ValueError si no)."""
    mal = set(O.primera_regla.unique()) - set(REGLAS)
    if mal: raise ValueError(f'primera_regla desconocida {mal}')
    g = O.groupby('primera_regla').agg(n=('coste', 'size'), coste=('coste', 'sum'), pnl=('pnl', 'sum')).reindex(list(REGLAS)).fillna(0.0)
    if int(g.n.sum()) != len(O) or not np.isclose(g.coste.sum(), O.coste.sum(), atol=1e-9) or not np.isclose(g.pnl.sum(), O.pnl.sum(), atol=1e-9): raise ValueError('la particion no suma el total')
    return g

def calma_inter_f3_cero(O):
    """Calma ∩ F3 = 0: ninguna orden vetada por F3 puede tener a Calma como regla que cancela (el veto de entrada de F3 precede). Devuelve el n de violaciones (debe ser 0)."""
    return int(((O.primera_regla == 'Calma') & O.f3_veto.astype(bool)).sum())

def k6_sin_calma_igual_k1(O6, O1, cols=('dia', 'mid', 'k', 'n_ord', 'q', 'cost', 'pnl')):
    """K6 con Calma desactivada == K1 BIT A BIT sobre las columnas clave (mismas filas y orden)."""
    a = O6[list(cols)].sort_values(list(cols[:4])).reset_index(drop=True); b = O1[list(cols)].sort_values(list(cols[:4])).reset_index(drop=True)
    return a.equals(b)

def gate_k6(delta_pareado, placebo_p, alfa_k6, ev_k6, ic_dias, ic_cierres, lc111, lc147, sin2mejores, loo):
    """gate de K6 (ADENDA K6 v2 B): EV incondicional >0 con IC90 dias y cierre (inf >0); Delta(K6-K1) pareado IC90 dias y cierre inf >0; Delta > placebo con p <= alfa_K6; positivo con L 111 y 147; sin 2 mejores dias >0; LOO (K6-F3, K6-V5, K6-V6) positivos.
    delta_pareado = dict(delta, ic90_dias=[lo,hi], ic90_cierres=[lo,hi]); ic_* = [lo,hi]; loo = {capa: ic90_dias}. Devuelve (veredicto, condiciones); DESCRIPTIVA si alfa es 0,01 y no se cumple, nunca confirma por debajo."""
    c = dict(ev_pos=ev_k6 > 0, ev_ic_dias=ic_dias[0] > 0, ev_ic_cierres=ic_cierres[0] > 0, delta_pos=delta_pareado['delta'] > 0, delta_ic_dias=delta_pareado['ic90_dias'][0] > 0, delta_ic_cierres=delta_pareado['ic90_cierres'][0] > 0,
             placebo=(placebo_p is not None and placebo_p <= alfa_k6), lc111=lc111 > 0, lc147=lc147 > 0, sin2=sin2mejores > 0, loo=all(v[0] > 0 for v in loo.values()))
    c = {k: bool(v) for k, v in c.items()}; return ('K6_CONFIRMADA_PENDIENTE_SENS' if all(c.values()) else 'K6_DESCRIPTIVA'), c
