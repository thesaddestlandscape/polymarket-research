"""Pruebas del diagnóstico de calibración H26 (objeto comparable: primeras K acciones de la población). Datos sintéticos, sin red."""
import gzip
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import analisis_5m_maker_banda_calibracion_objeto as C  # noqa: E402


def pob(rows):
    """rows: (dia, mkt, lado_c, T, acc, coste, gana, cola, act)."""
    return pd.DataFrame(rows, columns=["dia", "mkt", "lado_c", "T", "acc", "coste", "gana", "cola", "act"])


def test_primeras_k_orden_temporal_y_prorrata():
    # T desc = más temprano primero: 3 acc a 0,30 (T=250), luego 10 acc a 0,10 (T=200). K=5 -> 3 al 0,30 + 2 al 0,10 (prorrata).
    P = pob([("d", "m", "YES", 200, 10, 1.0, 1, "solo", "BTC"),
             ("d", "m", "YES", 250, 3, 0.9, 1, "solo", "BTC")])
    U = C.primeras_k(P, 5)
    assert len(U) == 1
    r = U.iloc[0]
    assert r.acc_k == pytest.approx(5.0)
    assert r.coste_k == pytest.approx(0.9 + 0.2)
    assert r.pnl_k == pytest.approx(5.0 - 1.1)                     # gana: cada acción paga 1


def test_primeras_k_perdedora_y_unidad_corta():
    P = pob([("d", "m", "NO", 250, 2, 0.5, 0, "solo", "ETH")])
    U = C.primeras_k(P, 5)
    r = U.iloc[0]
    assert r.acc_k == pytest.approx(2.0) and r.pnl_k == pytest.approx(-0.5)   # menos de K acciones: se toma entera, no se rellena


def test_primeras_k_unidades_independientes_y_todo():
    P = pob([("d", "m1", "YES", 250, 4, 0.8, 1, "solo", "BTC"), ("d", "m1", "NO", 250, 4, 0.8, 0, "solo", "BTC"),
             ("d2", "m1", "YES", 250, 4, 0.8, 0, "solo", "BTC")])
    assert len(C.primeras_k(P, 5)) == 3                              # dia, mkt, lado distintos
    big = C.primeras_k(P, 1e12)
    assert big.acc_k.sum() == pytest.approx(12.0)


def test_primeras_k_empates_estable():
    P = pob([("d", "m", "YES", 250, 5, 1.0, 1, "solo", "BTC"), ("d", "m", "YES", 250, 5, 2.0, 1, "solo", "BTC")])
    U = C.primeras_k(P, 5)
    assert U.iloc[0].coste_k == pytest.approx(1.0)                   # gana el primero del fichero (orden estable)


def test_ev_pool_y_medio_distintos():
    pnl, c = np.array([1.0, -1.0]), np.array([1.0, 9.0])
    assert C.ev_pool(pnl, c) == pytest.approx(0.0)
    assert C.ev_medio(pnl, c) == pytest.approx((1.0 - 1 / 9) / 2)
    assert C.ev_pool([], []) != C.ev_pool([], [])                   # nan, no 0


def test_tabla_2x2_categorias():
    uni = pd.DataFrame({"dia": ["d"] * 4, "mkt": ["a", "a", "b", "b"], "lado": ["YES", "NO", "YES", "NO"]})
    pobU = pd.DataFrame({"dia": ["d", "d"], "mkt": ["a", "b"], "lado": ["YES", "NO"], "pnl_p": [1.0, 1.0], "coste_p": [1.0, 1.0]})
    sim = pd.DataFrame({"dia": ["d", "d"], "mkt": ["a", "b"], "lado": ["YES", "YES"], "norders": [3, 2], "lleno": [5.0, 0.0]})
    A = C.tabla_2x2(uni, pobU, sim).set_index(["mkt", "lado"])
    assert A.loc[("a", "YES"), "sim"] == "rellena" and bool(A.loc[("a", "YES"), "pop"])
    assert A.loc[("b", "YES"), "sim"] == "cotiza_sin_relleno" and not bool(A.loc[("b", "YES"), "pop"])
    assert A.loc[("a", "NO"), "sim"] == "nunca_cotiza"               # sin fila del simulador = nunca cotizó (no es 'sin relleno')
    assert bool(A.loc[("b", "NO"), "pop"]) and A.loc[("b", "NO"), "sim"] == "nunca_cotiza"
    assert len(A) == 4


def test_veredicto_objeto_haz_y_nan():
    assert C.veredicto_objeto(-0.03, -0.04, -0.05)["estado"] == "PASA_OBJETO_COMPARABLE"
    assert C.veredicto_objeto(0.068, -0.040, -0.050)["estado"] == "NO_REPRODUCE_OBJETO_COMPARABLE"   # el caso real de la población completa
    assert C.veredicto_objeto(float("nan"), 0.0, 0.0)["estado"] == "SIN_DATOS"
    assert C.veredicto_objeto(-0.1, -0.04, -0.05)["post_hoc"] is True


def test_informe_fixture_minima(tmp_path):
    d = "2026-10-05"
    cab = "dia,motor,act,mkt,lado,tramo,completo,norders,ncap,lleno,coste,precio_m,rebate,t_libro_s,cap_s,t_fill_s,des,pnl\n"
    filas = []
    for motor in ("JOIN|C0|CONS|5", "JOIN|C0|OPT|5", "JOIN|C0|CONS|25", "JOIN|C0|CONS|50"):
        filas.append(f"{d},{motor},BTC,m1,YES,0,1,2,0,5.0,1.0,0.2,0.0,1.0,1.0,200.0,YES,4.0\n")
    with gzip.open(tmp_path / f"unidades_{d}.csv.gz", "wt") as fh:
        fh.write(cab + "".join(filas))
    pc = "mkt,lado_c,act,T,pc,acc,coste,cola,des,pnl\n"
    with gzip.open(tmp_path / f"pob_fills_{d}.csv.gz", "wt") as fh:
        fh.write(pc + "m1,YES,BTC,250.0,0.2,10.0,2.0,final,YES,8.0\nm2,NO,ETH,250.0,0.2,10.0,2.0,solo,YES,-2.0\n")
    with gzip.open(tmp_path / f"universo_{d}.csv.gz", "wt") as fh:
        fh.write("m1\nm2\n")
    txt, res = C.informe(tmp_path, [d])
    assert "2x2" in txt and "PASA_OBJETO_COMPARABLE" in txt or "NO_REPRODUCE_OBJETO_COMPARABLE" in txt
    assert res["celdas_JOIN|C0|CONS|5"]["pob|rellena"] == 1
    assert res["celdas_JOIN|C0|CONS|5"]["pob|nunca_cotiza"] == 1
