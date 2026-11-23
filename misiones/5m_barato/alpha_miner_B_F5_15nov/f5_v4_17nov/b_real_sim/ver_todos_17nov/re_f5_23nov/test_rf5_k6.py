"""test_rf5_k6.py -- ESPEC E6 (puras): reserva de alfa, dias evaluables, particion exhaustiva/conservacion, Calma∩F3=0, K6 sin Calma == K1, gate."""
import os, sys
import numpy as np, pandas as pd, pytest
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import rf5_k6 as K6

def test_reserva_de_alfa_fwer_y_mirada2():
    a = K6.alfas(False); assert a['K1_K4'] == 0.04 and a['K6'] == 0.01 and a['K1_K4'] + a['K6'] <= 0.05
    assert K6.alfas(True)['K6'] == 0.05 and K6.alfas(False, 2)['K1_K4'] == 0.02 and K6.alfas(False, 2)['K6'] == 0.005 and K6.alfas(True, 2)['K6'] == 0.025

def test_dias_evaluables_interseccion_e_insufficient_por_20pct():
    r = K6.dias_k6(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']); assert r['estado'] == 'OK' and r['no_evaluables'] == ['i', 'j'] and r['frac_no_evaluable'] == 0.2          # 20 % exacto no supera
    r = K6.dias_k6(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], ['a', 'b', 'c', 'd', 'e', 'f', 'g']); assert r['estado'] == 'INSUFFICIENT' and K6.dias_k6([], [])['estado'] == 'INSUFFICIENT'

def _ordenes(n=20):
    rng = np.random.default_rng(0); pr = rng.choice(K6.REGLAS, n); return pd.DataFrame(dict(primera_regla=pr, coste=rng.uniform(1, 3, n), pnl=rng.normal(0, 1, n), f3_veto=(pr == 'F3'), dia='d', mid=[f'm{i}' for i in range(n)], k=1, n_ord=1, q=1.0, cost=1.0))

def test_particion_exhaustiva_suma_el_total_y_rechaza_regla_desconocida():
    O = _ordenes(); g = K6.particion_exhaustiva(O); assert g.n.sum() == len(O) and np.isclose(g.pnl.sum(), O.pnl.sum()) and np.isclose(g.coste.sum(), O.coste.sum())
    with pytest.raises(ValueError): K6.particion_exhaustiva(O.assign(primera_regla='Otra'))

def test_calma_inter_f3_es_cero_y_detecta_violaciones():
    O = _ordenes(); assert K6.calma_inter_f3_cero(O) == 0
    O2 = O.copy(); i = O2.index[O2.primera_regla == 'F3'][0]; O2.loc[i, 'primera_regla'] = 'Calma'; assert K6.calma_inter_f3_cero(O2) == 1

def test_k6_sin_calma_igual_k1_bit_a_bit():
    O = _ordenes(); assert K6.k6_sin_calma_igual_k1(O.sample(frac=1, random_state=1), O)
    O2 = O.copy(); O2.loc[O2.index[3], 'pnl'] += 1e-12; assert not K6.k6_sin_calma_igual_k1(O2, O)

def test_gate_k6_condiciones():
    ok = dict(delta_pareado=dict(delta=.05, ic90_dias=[.01, .1], ic90_cierres=[.01, .1]), placebo_p=.004, alfa_k6=.01, ev_k6=.04, ic_dias=[.01, .1], ic_cierres=[.01, .1], lc111=.02, lc147=.01, sin2mejores=.01, loo={'F3': [.01, .1], 'V5': [.01, .1], 'V6': [.01, .1]})
    assert K6.gate_k6(**ok)[0] == 'K6_CONFIRMADA_PENDIENTE_SENS'
    assert K6.gate_k6(**dict(ok, placebo_p=.02))[0] == 'K6_DESCRIPTIVA'                                      # alfa 0,01 no cumplido
    assert K6.gate_k6(**dict(ok, placebo_p=.02, alfa_k6=.05))[0] == 'K6_CONFIRMADA_PENDIENTE_SENS'          # con K1 confirmada el umbral es 0,05
    assert K6.gate_k6(**dict(ok, loo={'F3': [-.01, .1], 'V5': [.01, .1], 'V6': [.01, .1]}))[0] == 'K6_DESCRIPTIVA' and K6.gate_k6(**dict(ok, placebo_p=None))[0] == 'K6_DESCRIPTIVA'
