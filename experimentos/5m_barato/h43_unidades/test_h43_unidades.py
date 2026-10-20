"""Tests de h43_unidades (A1 H43 R5K). Sinteticos (siempre) + regresion contra los datos reales (si estan en disco).
Ejecutar: nice -n 19 python3 -m pytest -q test_h43_unidades.py"""
import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import h43_unidades as H

# fila: (ts, li, mkt, lado, acc, coste, T, pc, maker)
def fila(ts, mkt, lado, acc, T, pc=0.2, li=0):
    return (ts, li, mkt, lado, acc, acc * pc, T, pc, "w")

DES = {"M1": "YES", "M2": "NO", "M3": "YES"}
FIN = 1_000_000_200  # multiplo de 300


def mercado(mkt, lado, tramos):
    """tramos: [(acc, T)] en orden temporal; ts = FIN - T."""
    return [fila(FIN - T, mkt, lado, acc, T, li=i) for i, (acc, T) in enumerate(tramos)]


def test_cosechable_toma_50_primeras_acc_en_ventana_tras_cruzar():
    rows = mercado("M1", "YES", [(4900, 280), (200, 200), (30, 150), (40, 100)])   # cruza 5000 con 100 (aporta 100)
    U, sd = H.unidades_cosechables(rows, DES)
    u = U[("M1", "YES")]
    # el relleno que cruza aporta 100 (>50) -> unidad completa con solo 50 acc del relleno que cruza
    assert u["completa"] and abs(u["acc"] - 50.0) < 1e-9 and not sd
    assert abs(u["c"] - 50 * 0.2) < 1e-9 and abs(u["p"] - 50 * 0.8) < 1e-9     # YES gana: (1-0,2)*50


def test_fills_fuera_de_ventana_no_consumen_cupo_cosechable_pero_si_posicional():
    # cruce con T=280 (>270): no cuenta. Las 50 acc siguientes con T<=270 SI en cosechable; en posicional la ventana
    # [5000,5050) cae en fills fuera de ventana -> unidad vacia o distinta (C1).
    rows = mercado("M1", "YES", [(4990, 290), (60, 280), (30, 200), (40, 100)])
    Uc, _ = H.unidades_cosechables(rows, DES)
    Up = H.unidades_posicionales(rows, DES)
    assert abs(Uc[("M1", "YES")]["acc"] - 50.0) < 1e-9 and Uc[("M1", "YES")]["completa"]
    assert ("M1", "YES") not in Up                         # la ventana posicional [5000,5050) esta en T=280


def test_fronteras_T_60_excluido_270_incluido():
    rows = mercado("M1", "YES", [(5000, 290), (20, 270), (20, 60), (20, 61)])
    U, _ = H.unidades_cosechables(rows, DES)
    u = U[("M1", "YES")]
    assert abs(u["acc"] - 40.0) < 1e-9 and not u["completa"]   # 270 y 61 cuentan, 60 no
    # la incompleta NO entra en cifras
    us, _, _ = [dict(u, fichero="x")], 0, 0
    assert [x for x in us if x["completa"]] == []


def test_fill_con_T_mayor_270_no_cuenta_aunque_este_en_banda():
    rows = mercado("M1", "YES", [(5000, 290), (50, 280)])        # T=280 > 270 (el registro congelado usa 270, no 300)
    U, _ = H.unidades_cosechables(rows, DES)
    assert U == {}


def test_sin_desenlace_se_excluye_y_se_cuenta_no_es_cero():
    rows = mercado("MX", "YES", [(5000, 290), (60, 200)])
    U, sd = H.unidades_cosechables(rows, DES)
    assert U == {} and sd == {("MX", "YES")}


def test_ventana_de_cruce_prorrata_exacta():
    rows = mercado("M2", "NO", [(4980, 290), (40, 200), (30, 100)])   # cruce: 20 por encima + 30 siguientes
    U, _ = H.unidades_cosechables(rows, DES)
    u = U[("M2", "NO")]
    assert abs(u["acc"] - 50.0) < 1e-9 and u["completa"]


def test_dia_de_cierre_no_el_de_fichero():
    u = {"fin": 1_000_000_200, "c": 10.0, "p": 1.0, "fichero": "1999-01-01"}
    import datetime
    esperado = datetime.datetime.fromtimestamp(1_000_000_200, datetime.timezone.utc).strftime("%Y-%m-%d")
    assert H.dia_cierre(u) == esperado != u["fichero"]


def test_cifras_ponderado_por_usdc_no_media_de_cocientes():
    us = [{"fin": 300 * i, "c": c, "p": p} for i, (c, p) in enumerate([(100.0, -50.0), (1.0, 1.0), (1.0, 1.0)])]
    r = H.cifras(us)
    assert abs(r["EV_ponderado"] - (-48.0 / 102.0)) < 1e-3          # ponderado
    assert abs(r["EV_media_unidad"] - ((-0.5 + 1 + 1) / 3)) < 1e-3  # media de cocientes: muy distinta
    assert H.cifras([]) is None


def test_ic90_exige_3_clusters():
    assert H._ic90({1: [1.0, 0.1], 2: [1.0, 0.1]}) is None


def test_concat_traslada_mercado_que_cruza_medianoche(monkeypatch):
    # prueba de MECANICA: en datos reales la banda T<=300 hace casi imposible que un 5m tenga fills en dos ficheros
    # (medido 05-18 Oct: 0 mercados trasladados; concat y por-fichero dan cifras identicas)
    import datetime
    d1, d2 = "2026-10-10", "2026-10-11"
    mid = datetime.datetime(2026, 10, 11, tzinfo=datetime.timezone.utc).timestamp()
    fin = mid + 300                                     # mercado 00:05: fills en dos ficheros
    f1 = [fila(fin - 280, "M1", "YES", 4960, 280, li=0), fila(fin - 270, "M1", "YES", 30, 270, li=1)]   # antes de las 00:00
    f2 = [fila(fin - 200, "M1", "YES", 30, 200, li=0), fila(fin - 100, "M1", "YES", 40, 100, li=1)]     # despues
    ficheros = {d1: f1, d2: f2}
    monkeypatch.setattr(H, "ruta_banda", lambda d: d if d in ficheros else None)
    monkeypatch.setattr(H, "leer_banda", lambda p: list(ficheros[p]))
    des = {"M1": "YES"}
    us, _, cob = H.construir([d1, d2], des=des, concat=False)
    assert [u for u in us if u["completa"]] == []        # por fichero: el cum se reinicia, nunca llega a 5000 en d2
    us, _, cob = H.construir([d1, d2], des=des, concat=True)
    comp = [u for u in us if u["completa"]]
    assert len(comp) == 1 and comp[0]["fichero"] == d2 and H.dia_cierre(comp[0]) == d2
    assert cob["_mercados_trasladados_de_fichero"] == 1


# ---- regresion contra datos reales (se salta si el volumen no esta montado) ----
DIAS_IN = ["2026-10-%02d" % d for d in range(5, 17)]
real = pytest.mark.skipif(not all(H.ruta_banda(d) for d in DIAS_IN + ["2026-10-17"]) or not os.path.exists(H.DES_CACHES[0]),
                          reason="bandas pass1 no disponibles")


@real
def test_regresion_in_sample_06_16_oct_reproduce_a7():
    """a7_cierre_final.json (auditoria 19-Oct): n=985, 963 cierres, coste 9.073, EV ponderado +0,201."""
    us, sd, _ = H.construir(DIAS_IN + ["2026-10-17"])
    r = H.cifras(H.periodo([u for u in us if u["completa"]], *H.IN_SAMPLE))
    assert (r["n"], r["cierres"]) == (985, 963) and sd == 0
    assert abs(r["coste_usdc"] - 9073.24) < 1.0 and abs(r["EV_ponderado"] - 0.2013) < 0.001
    assert r["IC90_cierre"][0] > 0.05 and r["dias_positivos"] == 9


@real
def test_regresion_forward_17_oct():
    """Definicion unica: n=61, EV ponderado -0,190 (por fichero -0,275 = vigia)."""
    us, _, _ = H.construir(["2026-10-16", "2026-10-17", "2026-10-18"] if H.ruta_banda("2026-10-18") else ["2026-10-16", "2026-10-17"])
    comp = [u for u in us if u["completa"]]
    r = H.cifras(H.periodo(comp, "2026-10-17", "2026-10-17"))
    assert r["n"] == 61 and abs(r["EV_ponderado"] - (-0.1904)) < 0.001
    rf = H.cifras(H.periodo(comp, "2026-10-17", "2026-10-17", clave=lambda u: u["fichero"]), clave_dia=lambda u: u["fichero"])
    assert abs(rf["EV_ponderado"] - (-0.275)) < 0.01             # por fichero, el vigia


@real
def test_regresion_unidades_por_fichero_10_12_14_oct_cosechable_completas():
    """Auditoria 19-Oct (validador 17-Oct): 89 / 78 / 71 unidades en 10 / 12 / 14-Oct (por fichero, cosechables completas)."""
    us, _, _ = H.construir(["2026-10-10", "2026-10-12", "2026-10-14"])
    n = {d: sum(1 for u in us if u["completa"] and u["fichero"] == d) for d in ("2026-10-10", "2026-10-12", "2026-10-14")}
    assert n == {"2026-10-10": 89, "2026-10-12": 78, "2026-10-14": 71}


@real
def test_posicional_reproduce_el_vigia_congelado_17_oct():
    """La definicion posicional implementada aqui da lo que publico el vigia (data/shadow/vigia_5m_barato_r5k.json del 19-Oct):
    17-Oct 61 unidades, coste 551,98, EV -0,2753; la unica diferencia con la definicion unica es 1 unidad incompleta (C1/C3)."""
    us, _, _ = H.construir(["2026-10-17"], posicional=True)
    r = H.cifras(us, clave_dia=lambda u: u["fichero"])
    assert r["n"] == 61 and abs(r["coste_usdc"] - 551.98) < 0.05 and abs(r["EV_ponderado"] - (-0.2753)) < 0.001
    uc, _, _ = H.construir(["2026-10-17"])
    assert sum(1 for u in uc if not u["completa"]) == 1
