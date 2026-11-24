"""test_rf5_k6_dia.py -- piezas del juez Calma v4 que no necesitan motor: particion por primera regla (suma exacta), Calma∩F3 = 0, salto de dias no COMPLETE, calendario ciego."""
import os, sys, types
import pandas as pd, pytest
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
os.environ.setdefault('RF5_OUT', '/tmp/rf5_test_k6dia/'); os.makedirs('/tmp/rf5_test_k6dia/', exist_ok=True)
import rf5_k6_dia as KD

def test_particion_cuenta_por_primera_regla_y_suma():
    R = pd.DataFrame(dict(mid=['a', 'b', 'c', 'd'], n_ord=[0, 0, 0, 1], k=[1, 2, 3, 4])); HK = types.SimpleNamespace(quien={('a', 0): 'V5+CALMA', ('b', 0): 'CALMA', ('c', 0): 'V6'})
    p = KD.particion(R, HK); assert p['V5'] == 1 and p['CALMA'] == 1 and p['V6'] == 1 and p['ninguna'] == 1 and p['total'] == 4 and p['suma_ok']

def test_calma_inter_f3_cuenta_ordenes_en_lados_vetados():
    R = pd.DataFrame(dict(mid=['a', 'b'], n_ord=[0, 0], k=[1, 2])); assert KD.calma_inter_f3(R, types.SimpleNamespace(vetado={('a', 1): False, ('b', 2): False})) == 0
    assert KD.calma_inter_f3(R, types.SimpleNamespace(vetado={('a', 1): True})) == 1

def test_procesa_salta_dia_no_complete(monkeypatch):
    monkeypatch.setattr(KD.RR, 'lee_dia', lambda d: {'status': 'INCOMPLETE'}); assert KD.procesa('2026-11-19') == 'SALTADO'
    monkeypatch.setattr(KD.RR, 'lee_dia', lambda d: None); assert KD.procesa('2026-11-19') == 'SALTADO'

def test_run_k6_sin_t_proc_o_sin_binance_falla_cerrado(monkeypatch):
    monkeypatch.setattr(KD.RR, 't_proc', lambda: None)
    with pytest.raises(RuntimeError, match='BLOCKED_T_PROC'): KD.run_K6('2026-11-24')
    monkeypatch.setattr(KD.RR, 't_proc', lambda: 1.0); monkeypatch.setattr(KD.FB, 'carga_binance', lambda d: {})
    with pytest.raises(RuntimeError, match='DATA_BLOCKED'): KD.run_K6('2026-11-24')
