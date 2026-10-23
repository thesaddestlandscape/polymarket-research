"""Tests de v9v3_lib: reglas de veto (orden, empates, latencia), placebo (calibracion, estructura de grupo), IC y aritmetica de neto/Delta."""
import os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
import v9v3_lib as L


def test_veto_steps_primero_empate_y_gap():
    grp = np.array(['a', 'a', 'a', 'a', 'b', 'c', 'c'])
    k = np.array([5, 5, 6, 7, 3, 1, 9])
    # dk=2: grupo a (k1=5): 5 y 5 no se vetan (empate), 6 no (k<7), 7 si; b unico; c: 1 no, 9 si
    assert L.veto_steps(grp, k, 2).tolist() == [False, False, False, True, False, False, True]
    # dk=1: 6 y 7 se vetan
    assert L.veto_steps(grp, k, 1).tolist() == [False, False, True, True, False, False, True]


def test_veto_time_latencia_y_primero():
    grp = np.array(['a', 'a', 'a', 'b', 'b'])
    t = np.array([100.0, 100.4, 103.0, 50.0, 50.0])
    assert L.veto_time(grp, t, 1.0).tolist() == [False, False, True, False, False]   # 0,4 s < L: pasa; empate exacto en b: no se veta
    assert L.veto_time(grp, t, 0.3).tolist() == [False, True, True, False, False]
    assert L.veto_time(grp, t, 5.0).tolist() == [False, False, False, False, False]


def test_veto_independiente_del_orden_de_filas():
    grp = np.array(['a', 'a', 'a']); t = np.array([103.0, 100.0, 100.4])
    assert L.veto_time(grp, t, 1.0).tolist() == [True, False, False]                  # el primero es el de menor t, no el de la fila 0


def test_neto_y_delta_aritmetica():
    df = pd.DataFrame(dict(dia=['d1', 'd1', 'd2', 'd2'], cierre=[1, 2, 3, 4], pnl=[-1.0, 2.0, -1.0, -1.0], cost=[1.0, 1.0, 1.0, 1.0], veto=[True, False, True, False], g=['x', 'y', 'x', 'y']))
    t = L.summarize('t', df, 'g', np.random.default_rng(1), reps=50)
    assert abs(t['net'] - 2.0) < 1e-12                                                # -(pnl vetado) = 1 + 1
    assert abs(t['ev_v'] - (-1.0)) < 1e-12 and abs(t['ev_r'] - 0.5) < 1e-12 and abs(t['delta'] - 1.5) < 1e-12
    assert t['nv'] == 2 and t['n'] == 4 and abs(t['share_cost_kept'] - 0.5) < 1e-12


def test_placebo_calibrado_bajo_nulo():
    # pnl iid: el neto real de una regla que vetea al azar el mismo numero por grupo debe quedar dentro de la distribucion placebo (p ~ uniforme)
    rng = np.random.default_rng(7); ps = []
    for rep in range(60):
        n = 600; g = np.repeat(np.arange(200), 3); pnl = rng.normal(-0.2, 1.0, n)
        veto = np.zeros(n, bool)
        for gi in range(200):
            idx = np.arange(gi * 3, gi * 3 + 3); veto[rng.choice(idx, 1)] = True
        nv = pd.Series(veto).groupby(g).transform('sum').values
        pl = L.placebo(pnl, g, nv, 400, rng); net = -pnl[veto].sum()
        ps.append((np.sum(pl >= net) + 1) / 401)
    ps = np.array(ps)
    assert 0.3 < ps.mean() < 0.7 and (ps < 0.05).mean() < 0.15


def test_placebo_detecta_regla_con_habilidad():
    # el primero de cada grupo pierde, los demas ganan: vetar el primero debe ser significativo (p pequeno); no vetar nada da p no definido (neto 0)
    rng = np.random.default_rng(3); g = np.repeat(np.arange(300), 3); pnl = np.tile([-1.0, 0.1, 0.1], 300) + rng.normal(0, .05, 900)
    veto = np.tile([True, False, False], 300); nv = pd.Series(veto).groupby(g).transform('sum').values
    pl = L.placebo(pnl, g, nv, 500, rng); net = -pnl[veto].sum()
    assert (np.sum(pl >= net) + 1) / 501 < 0.01


def test_placebo_conserva_el_numero_vetado_por_grupo():
    g = np.array([0, 0, 0, 1, 1, 2]); nv = np.array([2, 2, 2, 1, 1, 0]); pnl = np.array([1.0, 2.0, 4.0, 8.0, 16.0, 32.0])
    pl = L.placebo(pnl, g, nv, 2000, np.random.default_rng(0))
    # grupo 0 veta 2 de {1,2,4}: -(3|5|6); grupo 1 veta 1 de {8,16}: -(8|16); grupo 2 no entra (nv=0)
    assert set(np.round(pl).astype(int)) <= {-(a + b) for a in (3, 5, 6) for b in (8, 16)}
    assert abs(pl.mean() - (-(14 / 3 * 1 + 12))) < 0.6                                  # media exacta: 2*(7/3) + 12 = 16.67


def test_bootstrap_ic_contiene_media_y_es_determinista():
    rng1 = np.random.default_rng(5); rng2 = np.random.default_rng(5)
    a = np.array([[1.0, 2.0, 0.5, 2.0]] * 10 + [[-1.0, 2.0, 1.0, 2.0]] * 3)           # (pv, cv, pr, cr) por unidad de remuestreo
    r1 = L.boot(a, rng1, reps=400); r2 = L.boot(a, rng2, reps=400)
    assert r1 == r2 and r1[0] < r1[1]


def test_dia_sin_vetados_no_cuenta_como_cero():
    df = pd.DataFrame(dict(dia=['d1', 'd1', 'd2'], cierre=[1, 2, 3], pnl=[1.0, -1.0, 1.0], cost=[1.0, 1.0, 1.0], veto=[False, True, False], g=['a', 'b', 'c']))
    t = L.summarize('t', df, 'g', np.random.default_rng(1), reps=20)
    assert t['por_dia']['d2']['delta'] is None                                          # sin vetados: Delta indefinido (missing), no 0
