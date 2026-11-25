"""Tests de suelo_causal.py (ejecutar: python3 -I -m pytest -q test_suelo_causal.py)."""
import os, sys, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import suelo_causal as S
def filas(t0, t1, piso, n_por_s, seed):
    """filas (rx, ex) en [t0,t1) ms, d = piso + exp(10) (el p5 queda ~piso)."""
    rng = np.random.default_rng(seed); n = int((t1 - t0) / 1000 * n_por_s); rx = np.sort(rng.integers(t0, t1, n)); d = piso + np.floor(rng.exponential(6, n)).astype(int); return rx, rx - d
def carga(live, *tr):
    for rx, ex in tr:
        for a, b in zip(rx, ex): live.update(int(a), int(b))
def test_lo_hi_indet_mixta():
    T = 1_000_000_000
    for piso, esp in ((19, 'lo'), (40, 'hi'), (80, 'indet')):
        L = S.SueloCausalLive(); carga(L, filas(T - 600_000, T, piso, 2, 1)); assert L.clase(T) == esp, (piso, L.clase(T, True))
    L = S.SueloCausalLive(); carga(L, filas(T - 600_000, T - 300_000, 19, 2, 2), filas(T - 300_000, T, 40, 2, 3)); assert L.clase(T) == 'mixta'
    L = S.SueloCausalLive(); carga(L, filas(T - 600_000, T, 19, 0.1, 4)); assert L.clase(T) == 'indet'          # pocas filas: indet, no lo
    L = S.SueloCausalLive(); assert L.clase(T) == 'indet'
def test_sin_lookahead():
    T = 1_000_000_000; A = filas(T - 600_000, T, 19, 2, 5); L1 = S.SueloCausalLive(); carga(L1, A)
    F = filas(T, T + 600_000, 40, 5, 6); L2 = S.SueloCausalLive(); carga(L2, A, F)                                  # filas con rx >= t: no cambian clase(t)
    assert L1.clase(T) == L2.clase(T) == 'lo' and L1.clase(T, True)[1] == L2.clase(T, True)[1]
def test_bin_incompleto_no_cuenta():
    T = 1_000_000_000; Tb = (T // 10_000) * 10_000; A = filas(Tb - 600_000, Tb, 19, 2, 8); L = S.SueloCausalLive(); R = S.SueloCausalLive(); carga(L, A); carga(R, A); base = R.clase(Tb + 10_000, True)[1]
    rx = np.array([Tb + 5_000]); carga(L, (rx, rx - 70))
    assert L.clase(Tb + 9_999, True)[1] == R.clase(Tb + 9_999, True)[1]                                             # fila en el bin en curso: invisible
    assert L.clase(Tb + 10_000, True)[1]['tot_2'] == base['tot_2'] + 1                                              # bin ya completo: visible
def test_desorden_invariante():
    T = 1_000_000_000; rx, ex = filas(T - 600_000, T, 19, 2, 9); L1 = S.SueloCausalLive(); carga(L1, (rx, ex)); o = np.random.default_rng(1).permutation(len(rx)); L2 = S.SueloCausalLive(); carga(L2, (rx[o], ex[o]))
    assert L1.clase(T, True) == L2.clase(T, True)
def test_live_igual_batch_y_borde_de_dia():
    day0 = 1_794_000_000_000 // 86_400_000 * 86_400_000; rng = np.random.default_rng(3); H = np.zeros((S.NBINS_DIA, S.ND), np.int32); Hp = np.zeros((S.NBINS_DIA, S.ND), np.int32); ev = []
    def pon(Hx, base, piso, a, b):
        for t in range(a, b, 500):                                                                                        # una fila cada 0,5 s
            d = piso + int(rng.exponential(6)); rx = base + t; Hx[(rx - base) // S.BIN_MS, min(d, S.D_HI) - S.D_LO] += 1; ev.append((rx, rx - d))
    pon(Hp, day0 - 86_400_000, 19, 86_400_000 - 1_200_000, 86_400_000)                                                   # 20 min finales del dia anterior: lo
    pon(H, day0, 19, 0, 3_600_000); pon(H, day0, 40, 3_600_000, 7_200_000)                                               # lo la 1a hora, hi la 2a
    tb = S.tabla_clases(H, prev=Hp[-60:], nxt=None); L = S.SueloCausalLive(); CK = (60_000, 600_000, 3_000_000, 3_700_000, 3_900_000, 4_300_000); got = {}; ev.sort()      # streaming cronologico: se consulta en t con solo filas rx < t
    for t in CK:
        while ev and ev[0][0] < day0 + t: L.update(*ev.pop(0))
        got[t] = L.clase(day0 + t)
    for t in CK: assert tb['cls'][t // S.BIN_MS] == got[t], (t, tb['cls'][t // S.BIN_MS], got[t])                        # borde de dia; lo puro; 100 s tras flip lo->hi aun 'lo' (p5=suelo: lag conocido ~4,75 min); mixta; hi puro
    assert got[3_000_000] == 'lo' and got[4_300_000] == 'hi' and got[3_700_000] == 'lo' and got[3_900_000] == 'mixta' and got[60_000] == 'lo'
    tb0 = S.tabla_clases(H, prev=None, nxt=None); assert tb0['cls'][6] == 'indet'                                         # sin dia previo: indet (missing != lo)
def test_p5_formula_add3():
    h = np.zeros(S.ND, np.int64); h[20 - S.D_LO] = 5; h[30 - S.D_LO] = 95; assert S.p5_de(h) == (20.0, 100)                # 0,05*100=5: cum[20]=5 >= 5
    h[20 - S.D_LO] = 4; h[31 - S.D_LO] = 1; assert S.p5_de(h)[0] == 30.0
