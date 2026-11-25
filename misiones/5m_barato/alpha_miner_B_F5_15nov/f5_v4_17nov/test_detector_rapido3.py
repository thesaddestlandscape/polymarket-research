"""Tests 1c: parametros de la meseta (W12 C30 rho0.07 nmin5), permanencia X/Y causal. python3 -I -m pytest -q test_detector_rapido3.py"""
import os, sys, numpy as np, pytest
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import suelo_causal as S
from test_detector_rapido import filas_seg, a_matriz
PM = S.ParamsDetector(12, 30, 0.07, 5, 1)
def estado_xy(crudo, X, Y):
    """entra tras X crudos True seguidos; sale tras Y crudos False seguidos (Y=1: inmediata)."""
    n = len(crudo); st = np.zeros(n, bool); s = False; a = b = 0
    for i, c in enumerate(crudo):
        a = a + 1 if c else 0; b = 0 if c else b + 1
        if not s and a >= X: s = True
        elif s and b >= Y: s = False
        st[i] = s
    return st

def test_meseta_futuro_real_no_cambia_pasado():
    f = os.path.join(HERE, 'cache', 'seg_2026-10-21.npz')
    if not os.path.exists(f): pytest.skip('sin cache')
    M = np.load(f)['S']; base = S.estado_lo(S.lo_crudo(M, PM), PM); rng = np.random.default_rng(3)
    for t in (5000, 30000, 61000):
        M2 = M.copy(); M2[t:] = rng.integers(0, 300, M2[t:].shape); assert (S.estado_lo(S.lo_crudo(M2, PM), PM)[:t + 1] == base[:t + 1]).all()
def test_xy_causal_y_deterministico():
    rng = np.random.default_rng(1); c = rng.random(2000) < 0.6; e = estado_xy(c, 3, 5); assert (e == estado_xy(c.copy(), 3, 5)).all()
    c2 = c.copy(); c2[1200:] = ~c2[1200:]; assert (estado_xy(c2, 3, 5)[:1200] == e[:1200]).all()
def test_xy_entrada_salida():
    c = np.array([0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], bool); e = estado_xy(c, 3, 2)
    assert list(e[:4]) == [False, False, False, True] and e[4] and e[5] and not e[6]      # entra con 3 seguidos; sale tras 2 False; Y=1 = inmediata
    assert list(estado_xy(c, 1, 1)) == list(c)
def test_meseta_sintetico_lo_hi_failclosed():
    M = a_matriz(sorted(filas_seg(0, 200, 19, 80, 1) + filas_seg(200, 400, 40, 80, 2) + filas_seg(400, 500, 19, 0.05, 3)), 500); e = S.estado_lo(S.lo_crudo(M, PM), PM)
    assert e[100:200].all() and not e[230:400].any() and not e[420:500].any()                # lo -> nolo en hi; poco trafico = nolo
