#!/usr/bin/env python3
"""Tests de brecha_nivel_v3.py (funciones puras, datos sinteticos): calibra_composicion, sim_con_delta, escalones aditivos. python3 -I test_brecha.py"""
import os, sys, numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import brecha_nivel_v3 as B

def test_calibra():
    assert abs(B.calibra_composicion(None, -0.2, 20.0, 0.0, cost_tp_sim=10.0) - (-0.2 / 3)) < 1e-12          # rho = 2
    assert abs(B.calibra_composicion(None, -0.2, 0.0, 0.5, cost_tp_sim=10.0) - (-0.2)) < 1e-12               # sin FN: no cambia
    assert abs(B.calibra_composicion(None, 0.1, 10.0, 0.1, cost_tp_sim=10.0) - 0.1) < 1e-12                  # FN igual de buenos: sin efecto

def mk():
    return pd.DataFrame(dict(q_s=[5.0, 5.0, 5.0, 0.0, 5.0], q_r=[5.0, 0.0, 0.0, 5.0, 5.0], L=[0.15] * 5, gana=[0.0, 0.0, 1.0, 0.0, 1.0], v3d_BASE_f_tf=[1000.0, 1100.0, 1030.0, -1.0, 2000.0],
                             tcs=[0.9, 0.9, 0.9, 0.9, np.nan], dia=['d'] * 5, cl=list('abcde')))

def test_delta():
    R = mk(); q, an = B.sim_con_delta(R, 40)             # tcs*1000+40 = 940: tf 1000>940 anula (fila 0), 1100 anula (1), 1030 anula (2); fila 4 sin tcs no se anula; fila 3 no tenia relleno
    assert list(an) == [True, True, True, False, False] and list(q) == [0, 0, 0, 0, 5.0], (list(an), list(q))
    q, an = B.sim_con_delta(R, 150); assert list(an) == [False, True, False, False, False]                # 1100 > 900+150? 1100 > 1050 si; 1000 y 1030 no
    q, an = B.sim_con_delta(R, 1e9); assert not an.any()

def test_escalones_aditivos():
    R = mk(); R['q_s'] = R.q_s.astype(float); R['c_s'] = R.q_s * R.L; R['c_r'] = R.q_r * R.L; R['p_s'] = B.pnl_of(R.q_s, R.L, R.gana); R['p_r'] = B.pnl_of(R.q_r, R.L, R.gana)
    R['cls'] = np.where((R.q_s > 0) & (R.q_r > 0), 'TP', np.where(R.q_s > 0, 'FP', np.where(R.q_r > 0, 'FN', 'TN')))
    E = B.escalones(R); assert abs((E['paso_quitar_FP'] + E['paso_cantidad_real'] + E['paso_anadir_FN']) - E['gap_total']) < 1e-3, E

if __name__ == '__main__':
    test_calibra(); test_delta(); test_escalones_aditivos(); print('TODOS OK (brecha)')
