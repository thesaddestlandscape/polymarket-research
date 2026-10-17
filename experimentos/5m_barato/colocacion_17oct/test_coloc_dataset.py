"""Pruebas del constructor de dataset de colocación (fixture mínimo, sin tocar datos reales).
Ejecutar:  python3 -m pytest -q experimentos/5m_barato/colocacion_17oct/test_coloc_dataset.py
Cubren: regresión (la primera orden creada de cada unidad == motor de línea base de H35), causalidad de los rasgos (truncar el futuro no
cambia ningún rasgo anterior), relleno CONS (barrida / cola desconocida), unicidad de claves, reanudación idempotente y bloqueo horario."""
import gzip
import json
import math
import sys
from pathlib import Path

import numpy as np

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import coloc_dataset as C  # noqa: E402
H, S = C.H, C.S

DIA = "2026-10-14"
DIA0 = 1791936000000                 # 2026-10-14 00:00:00Z
FIN = DIA0 + 300_000                 # cierra a las 00:05
Y, N = "tokY", "tokN"


def kfilas():
    iso = "2026-10-14 00:05:00+00:00"
    return [f"k,{DIA0},{Y},BTC,5min,1001,{iso},YES", f"k,{DIA0},{N},BTC,5min,1001,{iso},NO"]


def q(t, tk, bid, ask, bsz=100.0, asz=50.0):
    return f"q,{t},{tk},{bid},{ask},{bsz},{asz},{t}"


def tr(t, tk, p, side, sz):
    return f"t,{t},{tk},{p},{side},{sz},{t},"


def escenario():
    L = kfilas()
    base = DIA0 + 10_000
    L.append(q(base - 1, N, "0.78", "0.8"))
    L.append(q(base, Y, "0.2", "0.22"))
    L.append(tr(base + 2000, Y, "0.2", "SELL", 150.0))                 # supera la cola de JOIN (100) -> k=0 rellena 5 a 0,20
    L.append(q(base + 2500, Y, "0.2", "0.22", 40.0, 50.0))
    L.append(tr(base + 3000, Y, "0.18", "SELL", 30.0))                  # barre 0,19 (k=1 rellena) y toca 0,18 (k=2: cola desconocida = inf)
    L.append(q(base + 3600, Y, "0.19", "0.22", 80.0, 50.0))
    L.append(q(base + 6000, Y, "0.19", "0.21", 80.0, 50.0))
    L.append(q(base + 9000, Y, "0.17", "0.21", 80.0, 50.0))
    L.append(q(base + 12000, Y, "0.17", "0.2", 10.0, 5.0))
    L.append(tr(base + 15000, Y, "0.15", "SELL", 500.0))
    L.append(q(base + 30000, Y, "0.17", "0.2", 10.0, 5.0))
    return L


def escribe(tmp, lineas):
    f = tmp / "m5_registro_test.csv.gz"
    with gzip.open(f, "wt") as fh:
        fh.write("tipo,t_ms,id,c1,c2,c3,c4,c5\n")
        for ln in lineas:
            fh.write(ln + "\n")
    return f


def correr(f, spawn_ms=1000):
    engines = [H.EngD(0, "DEEP", 1, "CONS"), H.EngD(1, "DEEP", 2, "CONS"), H.EngD(2, "JOIN", 0, "CONS")]
    mo = C.procesar(f, engines, H.Ladders(), C.B15(), DIA0, None, None, None, spawn_ms)
    return mo, mo.filas_deep(DIA)


def test_primera_orden_igual_a_linea_base(tmp_path):
    mo, base = correr(escribe(tmp_path, escenario()))
    d = C.empaquetar(mo, {"1001": "YES"})
    assert not C.validar(d)
    primero = {}
    for i in range(len(d["mkt"])):
        primero.setdefault((str(d["mkt"][i]), int(d["lado_yes"][i])), i)
    i0 = primero[("1001", 1)]
    por = {(r["fam"], r["k"]): r for r in base if r["lado"] == "YES" and r["tramo"] == 0}
    for k, clave in ((0, ("JOIN", 0)), (1, ("DEEP", 1)), (2, ("DEEP", 2))):
        r = por.get(clave)
        if r is None:
            assert d[f"av{k}"][i0] == 0
            continue
        assert abs(d[f"lleno{k}"][i0] - r["lleno"]) < 1e-5, (k, d[f"lleno{k}"][i0], r["lleno"])
        assert abs(d[f"coste{k}"][i0] - r["coste"]) < 1e-5, (k, d[f"coste{k}"][i0], r["coste"])


def test_relleno_conservador(tmp_path):
    mo, _ = correr(escribe(tmp_path, escenario()))
    d = C.empaquetar(mo, {"1001": "YES"})
    i0 = 0
    assert d["av0"][i0] == 1 and d["av1"][i0] == 1 and d["av2"][i0] == 1
    assert d["lleno0"][i0] == 5.0 and abs(d["coste0"][i0] - 1.0) < 1e-6          # JOIN 0,20: 5 acc
    assert d["lleno1"][i0] == 5.0 and abs(d["coste1"][i0] - 0.95) < 1e-6         # k=1 0,19: barrida por debajo
    assert d["lleno2"][i0] == 0.0                                                  # k=2 0,18: cola desconocida infinita -> solo sweeps
    assert d["p0" + "0"][i0] == 200 and d["p01"][i0] == 190 and d["p02"][i0] == 180


def test_rasgos_causales(tmp_path):
    L = escenario()
    f1 = escribe(tmp_path, L)
    mo1, _ = correr(f1)
    d1 = C.empaquetar(mo1, {})
    # truncar el futuro tras la decisión 3 no puede cambiar los rasgos de las decisiones 0..2
    tq = d1["tq"]
    assert len(tq) >= 4
    corte = int(tq[3]) - 1
    L2 = [x for x in L if x.startswith("k,") or int(x.split(",")[1]) <= corte]
    tmp2 = tmp_path / "b"
    tmp2.mkdir()
    mo2, _ = correr(escribe(tmp2, L2))
    d2 = C.empaquetar(mo2, {})
    m = min(len(d2["tq"]), 3)
    assert m >= 2
    # tq de las primeras decisiones coincide y los rasgos son idénticos (con NaN iguales)
    n = m
    sel1 = [i for i in range(len(d1["tq"])) if d1["tq"][i] <= corte][:n]
    sel2 = list(range(n))
    assert [int(d1["tq"][i]) for i in sel1] == [int(d2["tq"][i]) for i in sel2]
    assert np.array_equal(d1["X"][sel1], d2["X"][sel2], equal_nan=True)


def test_rasgos_exactos_primera_decision(tmp_path):
    mo, _ = correr(escribe(tmp_path, escenario()))
    d = C.empaquetar(mo, {})
    x = d["X"][0]
    g = lambda n: x[C.FI[n]]                                                    # noqa: E731
    assert abs(g("bid") - 0.2) < 1e-6 and abs(g("ask") - 0.22) < 1e-6
    assert abs(g("spr") - 2.0) < 1e-6 and abs(g("T") - 290.0) < 1e-3
    assert g("c_BTC") == 1.0 and g("c_ETH") == 0.0 and g("lado_yes") == 1.0
    assert g("hit5") == 0.0 and g("lift30") == 0.0 and math.isnan(g("bn_r5"))
    assert abs(g("par_bid") - 0.78) < 1e-6
    # la segunda decisión (tras la venta de 150) ve el flujo vendedor y no más
    j = [i for i in range(len(d["tq"])) if d["tq"][i] > DIA0 + 10_000 + 2000][0]
    assert d["X"][j][C.FI["hit5"]] == 150.0


def test_unicidad_y_reanudacion(tmp_path):
    mo, _ = correr(escribe(tmp_path, escenario()))
    d = C.empaquetar(mo, {"1001": "YES"})
    assert C.validar(d) == []
    out = tmp_path / "out"
    out.mkdir()
    C.guardar_npz(out / f"dp_{DIA}.npz", d)
    meta = {"script_sha": C.sha_codigo(), "params_hash": C.params_hash(), "cobertura_des": 1.0, "decisiones": len(d["mkt"]),
            "sha_npz": S.sha_fichero(out / f"dp_{DIA}.npz")}
    (out / f"meta_{DIA}.json").write_text(json.dumps(meta))
    assert C.cache_valida(out, DIA) is not None
    # corrupción: el checkpoint se invalida y se recalcularía
    with open(out / f"dp_{DIA}.npz", "ab") as fh:
        fh.write(b"corrupto")
    assert C.cache_valida(out, DIA) is None
    # duplicados detectados
    d2 = {k: np.concatenate([v, v[:1]]) for k, v in d.items()}
    assert C.validar(d2)


def test_bloqueo_horario_y_modo_solo_lectura():
    # el módulo no importa nada de ejecución real ni de red de trading
    src = Path(C.__file__).read_text()
    for prohibido in ("py_clob_client", "ejecutor_rapido", ".env", "private_key", "post_order"):
        assert prohibido not in src


def test_desorden_ms_no_rompe(tmp_path):
    L = kfilas()
    base = DIA0 + 10_000
    L += [q(base, Y, "0.2", "0.22"), q(base + 2000, Y, "0.2", "0.23"), q(base + 1990, Y, "0.19", "0.23"), q(base + 4000, Y, "0.19", "0.23")]
    mo, _ = correr(escribe(tmp_path, L))
    d = C.empaquetar(mo, {})
    assert not C.validar(d)
