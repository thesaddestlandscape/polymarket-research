"""Tests del detector rapido (python3 -I -m pytest -q test_detector_rapido.py)."""
import os, sys, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import suelo_causal as S
def filas_seg(sec0, sec1, piso, rate, seed):
    rng = np.random.default_rng(seed); out = []
    for s in range(sec0, sec1):
        n = rng.poisson(rate); rx = s * 1000 + rng.integers(0, 1000, n); d = piso + np.floor(rng.exponential(8, n)).astype(int); out += list(zip(rx, rx - d))
    return out
def a_matriz(filas, ns, s0=0):
    M = np.zeros((ns, S.NBAND), np.int64)
    for rx, ex in filas:
        k = rx // 1000 - s0
        if 0 <= k < ns: M[k, S.banda_de(rx - ex)] += 1
    return M
P = S.ParamsDetector(W=2, C=30, rho=0.05, nmin=20, H=2)
def test_lo_hi_y_retraso():
    f = filas_seg(0, 100, 19, 100, 1) + filas_seg(100, 200, 40, 100, 2); L = S.DetectorRapidoLive(P); out = {}
    for rx, ex in sorted(f):
        for t in (60, 99, 101, 102, 103, 104, 150, 199): 
            pass
    # streaming cronologico con consultas
    f.sort(); i = 0; est = {}
    for t_s in range(1, 200):
        while i < len(f) and f[i][0] < t_s * 1000: L.update(*f[i]); i += 1
        est[t_s] = L.estado(t_s * 1000)
    assert est[50] == 'lo' and est[99] == 'lo' and est[150] == 'nolo'
    assert est[102] == 'nolo'                         # lo->nolo en <= W+1 s del cambio (ventana de 2 s ya sin filas bajas)
    assert est[3] in ('lo', 'nolo')
def test_failclosed():
    L = S.DetectorRapidoLive(P); assert L.estado(10_000) == 'nolo'                                  # sin datos -> no operar
    f = filas_seg(0, 60, 19, 3, 3); [L.update(*x) for x in sorted(f)]; assert L.estado(59_000) == 'nolo'    # trafico < nmin -> no operar
def test_sin_lookahead():
    f = sorted(filas_seg(0, 60, 19, 100, 4)); L1 = S.DetectorRapidoLive(P); L2 = S.DetectorRapidoLive(P)
    for x in f: L1.update(*x); L2.update(*x)
    fut = [(60_000 + k * 10, 60_000 + k * 10 - 45) for k in range(200)]; [L2.update(*x) for x in fut]      # filas con rx >= t (hi) no cambian estado(t)
    assert L1.estado(60_000) == L2.estado(60_000) == 'lo'
    mid = [(59_500, 59_500 - 45)] * 500; L3 = S.DetectorRapidoLive(P); [L3.update(*x) for x in f]; est0 = L3.estado(59_500); [L3.update(*x) for x in mid]; assert L3.estado(59_500) == est0   # segundo en curso no cuenta
def test_batch_igual_live():
    f = sorted(filas_seg(0, 80, 19, 100, 5) + filas_seg(80, 160, 40, 100, 6) + filas_seg(160, 240, 19, 100, 7)); M = a_matriz(f, 240)
    crudo = S.lo_crudo(M, P); est = S.estado_lo(crudo, P); L = S.DetectorRapidoLive(P); i = 0
    for t_s in range(0, 240):
        while i < len(f) and f[i][0] < t_s * 1000: L.update(*f[i]); i += 1
        assert (L.estado(t_s * 1000) == 'lo') == bool(est[t_s]), (t_s, L.estado(t_s * 1000), est[t_s])
def test_batch_borde_dia():
    f = sorted(filas_seg(0, 300, 19, 100, 8)); M = a_matriz(f, 300); full = S.estado_lo(S.lo_crudo(M, P), P)
    parte = np.concatenate([S.estado_lo(S.lo_crudo(M[:150], P), P)]); cr2 = S.lo_crudo(M[150:], P, prev=M[:150]); e2 = S.estado_lo(cr2, P, prev_crudo=S.lo_crudo(M[:150], P)); assert (np.concatenate([parte, e2]) == full).all()
