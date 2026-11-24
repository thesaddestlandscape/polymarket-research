"""test_rf5_nulo_run.py -- piezas puras del nulo por re-simulacion y salvaguardas (sin motor: no construye E)."""
import os, sys
import numpy as np, pandas as pd, pytest
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
os.environ.setdefault('RF5_OUT', '/tmp/rf5_test_nulo_run/'); os.makedirs('/tmp/rf5_test_nulo_run/', exist_ok=True)
import rf5_nulo_run as NR, rf5_nulo as NU

def _R(pol, dia, pnl, cost, q=1.0, bloq=0): return dict(pol=pol, dia=dia, pnl=pnl, cost=cost, q=q, bloq=bloq)

def test_unidades_dia_solo_rellenos_y_nan_es_cero():
    R = pd.DataFrame([_R('b', 'd', 1.0, 2.0), _R('b', 'd', 5.0, 9.0, q=0.0), _R('b', 'd', np.nan, np.nan)]); assert NR.unidades_dia(R) == (1.0, 2.0) and NR.unidades_dia(None) == (0.0, 0.0) and NR.unidades_dia(R.iloc[0:0]) == (0.0, 0.0)

def test_delta_dia_y_Tobs_max_sobre_dias():
    dias = ['d1', 'd2', 'd3', 'd4']; rows = []
    for i, d in enumerate(dias): rows += [_R('base', d, 1.0, 10.0), _R('F3', d, 1.0 + 0.5 + 0.1 * i, 10.0), _R('F1', d, 1.0 - 0.2, 10.0)]
    R = pd.DataFrame(rows); o = NR.Tobs_max('A', R[R.pol == 'base'], R, ('F1', 'F3')); assert o['dias'] == dias
    assert np.allclose(o['por_politica']['F3']['delta_dias'], [0.05, 0.06, 0.07, 0.08]) and np.allclose(o['por_politica']['F1']['delta_dias'], [-0.02] * 4)
    assert o['Tmax'] == o['por_politica']['F3']['T'] and np.isnan(o['por_politica']['F1']['T'])                       # varianza 0 => T indefinido (NaN), el max ignora NaN

def test_corre_bloqueado_sin_autorizacion_y_con_pocos_dias(monkeypatch):
    monkeypatch.delenv('RF5_NULO_AUTORIZADO', raising=False)
    with pytest.raises(SystemExit, match='BLOQUEADO'): NR.main(['corre', 'K', '2026-11-24'])
    monkeypatch.setenv('RF5_NULO_AUTORIZADO', '1')
    with pytest.raises(SystemExit, match='BLOQUEADO'): NR.main(['corre', 'K', '2026-11-24'])

def test_ensayo_se_niega_en_dia_ciego():
    with pytest.raises(SystemExit): NR.main(['ensayo', '2026-11-18', 'K'])

def test_permuta_asignacion_biyectiva_por_moneda_y_coherente_con_permuta_pares():
    M = pd.DataFrame(dict(coin=['eth'] * 4 + ['sol'] * 3, mid=[f'm{i}' for i in range(7)], f_up=np.arange(7.0), f_dn=np.arange(7.0) + 10)); a = NU.permuta_asignacion(M, NU.rng_perm('2026-12-01', 3)); assert set(a) == set(M.mid) and sorted(a.values()) == sorted(M.mid)
    assert all((a[m][1:] in ('0', '1', '2', '3')) == (m in ('m0', 'm1', 'm2', 'm3')) for m in a)                          # nunca cruza de moneda
    p = NU.permuta_pares(M, NU.rng_perm('2026-12-01', 3)); assert all(p[m] == (float(M.f_up[int(a[m][1:])]), float(M.f_dn[int(a[m][1:])])) for m in p)            # el PAR viaja junto y coincide con la asignacion
    assert NU.permuta_asignacion(M, NU.rng_perm('2026-12-01', 3)) == a                                                      # determinista por (dia, j)

def test_igual_ignora_solo_la_etiqueta_pol():
    import rf5_nulo_run as R
    A = pd.DataFrame(dict(pol=['F1_SET'] * 3, px=[0.1, 0.2, np.nan], n=[1, 2, 3])); B = A.assign(pol='F1')
    assert R.igual(A, B) is True and R.difiere(A, B) == {}
    assert R.igual(A, B.assign(px=[0.1, 0.2, 0.3])) is False and 'px' in R.difiere(A, B.assign(px=[0.1, 0.2, 0.3]))   # NaN != 0.3 se detecta
    assert R.igual(A, B.iloc[::-1]) is False                                                                          # el orden de filas cuenta
