import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
import markouts_desde_registro as M

def rec(t0, tardio=False):
    return {'slug': 'eth-updown-5m-1000', 'lado': 'YES', 'rellenos': [{'oid': 'x', 'acc': 5.0, 'precio': 0.20, 't_deteccion': t0, 'tardio': tardio}]}

def test_basico_y_missing_y_stale():
    xs = [(1000.0, 0.20), (1010.0, 0.30), (1100.0, 0.10)]       # fin = 1300
    f = M.calcular(rec(1003.0), xs)[0]
    assert f['mid_5s'] == 0.20 and abs(f['markout_5s']) < 1e-12        # a 1008: ultimo q = 1000
    assert f['mid_30s'] == 0.30 and abs(f['markout_30s'] - 0.5) < 1e-9  # a 1033: q=1010
    assert f['mid_120s'] == 0.10 and abs(f['markout_120s'] + 0.5) < 1e-9
    assert f['stale_30s'] is False and abs(f['edad_q_30s'] - 23.0) < 1e-9
    g = M.calcular(rec(1250.0), xs)[0]                                  # +120 pasa del cierre -> missing, no 0
    assert g['mid_120s'] is None and g['markout_120s'] is None and g['mid_30s'] == 0.10 and g['stale_30s'] is True
    assert M.calcular(rec(1003.0, tardio=True), xs)[0]['mid_5s'] is None
    assert M.calcular(rec(1003.0), [])[0]['markout_5s'] is None

if __name__ == '__main__':
    test_basico_y_missing_y_stale(); print('ok')
