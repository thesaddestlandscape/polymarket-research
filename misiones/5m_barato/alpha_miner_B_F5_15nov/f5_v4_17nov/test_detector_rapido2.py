"""Tests adicionales del detector rapido (17-Nov, tarea 3): perturbacion del futuro sobre datos REALES, determinismo, hi->lo sintetico, parametros elegidos. python3 -I -m pytest -q test_detector_rapido2.py"""
import os, sys, numpy as np, pytest
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import suelo_causal as S
from test_detector_rapido import filas_seg, a_matriz
PSEL = S.ParamsDetector(W=5, C=30, rho=0.05, nmin=10, H=1)
def _estado(M, p): return S.estado_lo(S.lo_crudo(M, p), p)
@pytest.mark.parametrize('p', [PSEL, S.ParamsDetector(2, 30, 0.05, 20, 2), S.ParamsDetector(3, 36, 0.1, 40, 5)])
def test_futuro_real_no_cambia_pasado(p):
    f = os.path.join(HERE, 'cache', 'seg_2026-10-15.npz')
    if not os.path.exists(f): pytest.skip('sin cache seg')
    M = np.load(f)['S']; base = _estado(M, p); rng = np.random.default_rng(7)
    for t in (3600, 20000, 43210, 70000):
        M2 = M.copy(); M2[t:] = rng.integers(0, 500, M2[t:].shape); M2[t:, 5:] = 0                      # futuro (segundos >= t) arbitrario
        e2 = _estado(M2, p); assert (e2[:t + 1] == base[:t + 1]).all(), t                                  # estado[t] usa solo segundos < t
def test_determinismo():
    M = a_matriz(sorted(filas_seg(0, 300, 19, 60, 11) + filas_seg(300, 600, 40, 60, 12)), 600)
    a = _estado(M, PSEL); b = _estado(M.copy(), PSEL); assert (a == b).all() and a.tobytes() == b.tobytes()
def test_hi_a_lo_y_lo_a_hi_sinteticos():
    M = a_matriz(sorted(filas_seg(0, 200, 40, 80, 1) + filas_seg(200, 400, 19, 80, 2) + filas_seg(400, 600, 40, 80, 3)), 600); e = _estado(M, PSEL)
    assert not e[:60].any() and not e[150:200].any()                       # hi -> nolo (fail-closed)
    assert e[210:400].all() or e[215:400].all()                             # lo detectado <= ~10 s tras el cambio
    r_hilo = int(np.argmax(e[200:])); assert r_hilo <= 15, r_hilo           # retraso hi->lo en s
    assert not e[410:600].any() or int(np.argmax(~e[400:])) <= 10           # lo->hi en <= ~10 s
def test_poco_trafico_failclosed():
    M = a_matriz(sorted(filas_seg(0, 300, 19, 0.3, 21)), 300); assert not _estado(M, PSEL).any()
