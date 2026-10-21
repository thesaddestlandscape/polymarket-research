"""Tests del envoltorio de integridad `vigia_5m_barato_h59_robusto.py` (hallazgos 6-10 del code-review de H59) y de que el vigia congelado sigue intacto.
Fixture sintetica reutilizada de test_h59.py (mismo TMP/entorno; sin red, sin tocar datalogs reales ni produccion).
Ejecutar: cd experimentos/5m_barato/h59_colchon && nice -n 19 python3 -m pytest -q test_h59.py test_h59_robusto.py"""
import csv
import gzip
import hashlib
import json
import os
import shutil
import threading
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

import test_h59 as T                                   # fija el entorno (M5B_DL, M5B_PRICES, H59_SALIDA) y la fixture
import vigia_5m_barato_h59_forward as VG
import vigia_5m_barato_h59_robusto as ROB

DIA, TMP = T.DIA, T.TMP
AHORA = T.AHORA_COMPLETO
AQUI = Path(__file__).resolve().parent
N = 8                                                   # cierres de la fixture + el escenario "tardio"
TARDIO = {91: dict(q15=[(-1000, .50, .52)], q5=[(500, .38, .40, 30, 50), (297000, .38, .40, 30, 50)])}      # cierre 24:00Z con fila q a C-3 s


def fx(extra=None, tardio=True):
    ex = dict(TARDIO) if tardio else {}
    ex.update(extra or {})
    T.fixture(ex)


@pytest.fixture(autouse=True)
def limpio():
    for p in (ROB.SAL, TMP / "DL" / "ent55"):
        if p.exists():
            for f in p.glob("*"):
                f.unlink() if f.is_file() else shutil.rmtree(f, ignore_errors=True)
    yield


def meta(dia=DIA):
    return json.loads((ROB.SAL / f"entradas_{dia}.meta.json").read_text())


def filas_csv(dia=DIA):
    with gzip.open(ROB.SAL / f"entradas_{dia}.csv.gz", "rt") as fh:
        return list(csv.DictReader(fh))


# ------------------------------------------------------------------------------------------------ congelacion intacta
def test_los_ficheros_congelados_siguen_byte_a_byte_y_el_hash_es_el_preregistrado():
    pre = json.loads((AQUI / "preregistro.json").read_text())
    for f in ("h59_lectura.py", "h59_regla.py", "h59_stats.py", "vigia_5m_barato_h59_forward.py"):
        assert hashlib.sha256((AQUI / f).read_bytes()).hexdigest()[:16] == pre["sha256_16_ficheros"][f], f
    assert VG.hash_codigo() == pre["hash_congelacion"] == "ea3789bafdc70764"


def test_el_envoltorio_no_envia_ni_firma():
    s = (AQUI / "vigia_5m_barato_h59_robusto.py").read_text()
    for prohibido in ("ejecutor_rapido", "py_clob_client", "requests.post", "post_order", "create_order", "live/.env", "load_dotenv", "private_key", "Enviador"):
        assert prohibido not in s, prohibido
    assert "if telegram:" in s


# ------------------------------------------------------------------------------------------------ equivalencia con el vigia congelado
def test_misma_salida_que_el_vigia_congelado_cuando_los_datos_estan_completos():
    fx()
    VG.procesar(DIA, forzar=True, ahora=AHORA)
    a = gzip.decompress((VG.SAL / f"entradas_{DIA}.csv.gz").read_bytes())
    ROB.procesar(DIA, forzar=True, ahora=AHORA, cierres_esperados=N)
    b = gzip.decompress((ROB.SAL / f"entradas_{DIA}.csv.gz").read_bytes())
    assert a == b and len(filas_csv()) == N and meta()["duplicados"] == 0


# ------------------------------------------------------------------------------------------------ (6) COMPLETE solo con evidencia
def test_complete_exige_96_cierres_y_datos_hasta_el_final_del_dia():
    fx()
    m = ROB.procesar(DIA, forzar=True, ahora=AHORA, cierres_esperados=N)
    assert m["estado"] == "COMPLETE" and m["completo"] and m["motivos"] == [] and m["wrapper_sha256"] == ROB.sha_wrapper()
    m = ROB.procesar(DIA, forzar=True, ahora=AHORA)                                  # 96 reales: la fixture solo tiene 8
    assert m["estado"] == "PARTIAL" and any(x.startswith("cierres_con_mercado_8_de_96") for x in m["motivos"])
    fx(tardio=False)
    m = ROB.procesar(DIA, forzar=True, ahora=AHORA, cierres_esperados=7)
    assert m["estado"] == "PARTIAL" and "datos_no_llegan_al_fin_del_dia" in m["motivos"]      # el feed acaba temprano: no es un dia completo
    m = ROB.procesar(DIA, forzar=True, ahora=datetime(2026, 10, 19, 12, tzinfo=timezone.utc).timestamp(), cierres_esperados=7)
    assert m["estado"] == "PARTIAL" and "dia_no_terminado" in m["motivos"]


def test_fichero_truncado_o_abierto_queda_registrado_y_sin_datos_al_final_es_parcial():
    fx()
    f = TMP / "DL" / f"maker_ms_{DIA}_1.csv.gz"
    raw = f.read_bytes()
    f.write_bytes(raw[:-12])                                                         # gz cortado (proceso matado) + mtime reciente = abierto
    m = ROB.procesar(DIA, forzar=True, ahora=time.time() + 1, cierres_esperados=N)
    assert m["ficheros_truncados"] == [f.name] and m["ficheros_abiertos"] == [f.name]
    f.write_bytes(raw)


def test_ya_procesado_se_revalida_con_tamano_y_mtime_de_los_ficheros_del_dia():
    fx()
    m1 = ROB.procesar(DIA, forzar=True, ahora=AHORA, cierres_esperados=N)
    m2 = ROB.procesar(DIA, ahora=AHORA, cierres_esperados=N)
    assert m2["generado_utc"] == m1["generado_utc"]                                  # nada cambio: no recalcula
    # un fichero del dia D cambia (se completo despues): hay que recalcular aunque el meta diga COMPLETE
    f = TMP / "DL" / f"maker_ms_{DIA}_1.csv.gz"
    os.utime(f, ns=(1, f.stat().st_mtime_ns + 5_000_000_000))
    m3 = ROB.procesar(DIA, ahora=AHORA, cierres_esperados=N)
    assert m3["generado_utc"] != m1["generado_utc"]
    # un fichero NUEVO del dia D tambien invalida
    shutil.copy(f, TMP / "DL" / f"maker_ms_{DIA}_2.csv.gz")
    try:
        m4 = ROB.procesar(DIA, ahora=AHORA, cierres_esperados=N)
        assert m4["generado_utc"] != m3["generado_utc"] and len(m4["ficheros_ms"]) == 2
    finally:
        (TMP / "DL" / f"maker_ms_{DIA}_2.csv.gz").unlink()
    # el crecimiento de un fichero de D+1 NO invalida
    sig = (datetime.fromisoformat(DIA) + timedelta(days=1)).date().isoformat()
    g = TMP / "DL" / f"maker_ms_{sig}_9.csv.gz"
    with gzip.open(g, "wt") as fh:
        fh.write("tipo,t_ms,id\n")
    ROB.procesar(DIA, forzar=True, ahora=AHORA, cierres_esperados=N)
    ult = meta()["generado_utc"]
    with gzip.open(g, "wt") as fh:
        fh.write("tipo,t_ms,id\nh,1,2\n")
    assert ROB.procesar(DIA, ahora=AHORA, cierres_esperados=N)["generado_utc"] == ult
    g.unlink()


# ------------------------------------------------------------------------------------------------ (7) k, en el fichero del dia anterior
def test_mercado_con_la_linea_k_en_el_fichero_del_dia_anterior_no_se_pierde_en_silencio():
    fx()
    f = TMP / "DL" / f"maker_ms_{DIA}_1.csv.gz"
    with gzip.open(f, "rt") as fh:
        lineas = fh.read().splitlines()
    ks = [l for l in lineas if l.startswith("k,") and ",M5_0," in l or l.startswith("k,") and ",M15_0," in l]
    assert len(ks) == 4
    with gzip.open(f, "wt") as fh:
        fh.write("\n".join(l for l in lineas if l not in ks) + "\n")
    prev = (datetime.fromisoformat(DIA) - timedelta(days=1)).date().isoformat()
    p = TMP / "DL" / f"maker_ms_{prev}_1.csv.gz"
    with gzip.open(p, "wt") as fh:
        fh.write("\n".join(ks) + "\n")
    os.utime(p, (1, 1))                                                              # mas antiguo: se lee primero
    try:
        m = ROB.procesar(DIA, forzar=True, ahora=AHORA, cierres_esperados=N)
        assert m["usado_dia_previo"] is True and m["cierres_en_registro"] == N and m["estado"] == "COMPLETE"
        assert str(T.cierre(0)) in {r["cierre"] for r in filas_csv()}               # el cierre 0 sigue en la salida
        m2 = ROB.procesar(DIA, forzar=True, ahora=AHORA, cierres_esperados=N + 5)    # faltan mercados de verdad: PARTIAL con el motivo a la vista
        assert m2["estado"] == "PARTIAL" and any("cierres_con_mercado" in x for x in m2["motivos"])
    finally:
        p.unlink()
        fx()


# ------------------------------------------------------------------------------------------------ (8)/(9) informe
def _dos_dias(monkeypatch, dia2="2026-10-18", estado2="PARTIAL"):
    """Dia 19 COMPLETE (verificado) + dia 18 con las mismas filas pero PARTIAL/otro estado."""
    fx()
    ROB.procesar(DIA, forzar=True, ahora=AHORA, cierres_esperados=N)
    rows = filas_csv()
    with gzip.open(ROB.SAL / f"entradas_{dia2}.csv.gz", "wt", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=VG.CAMPOS, restval="")
        w.writeheader()
        w.writerows({**r, "dia": dia2, "cierre": int(r["cierre"]) - 86400} for r in rows)
    m = {**meta(), "dia": dia2, "estado": estado2, "completo": estado2 == "COMPLETE", "motivos": ["cierres_con_mercado_8_de_96"] if estado2 == "PARTIAL" else []}
    (ROB.SAL / f"entradas_{dia2}.meta.json").write_text(json.dumps(m))
    monkeypatch.setitem(VG.CONFIG, "congelado_utc", "2026-10-17T00:00:00+00:00")
    monkeypatch.setattr(VG, "hash_codigo", lambda: "x")
    monkeypatch.setattr(VG, "manifiesto", lambda dia=None: "x")


def _estandar(monkeypatch):
    monkeypatch.setattr(ROB, "DL_STD", os.environ["M5B_DL"])
    monkeypatch.setattr(ROB, "PRICES_STD", os.environ["M5B_PRICES"])
    monkeypatch.setattr(ROB, "SAL_STD", os.environ["H59_SALIDA"])
    monkeypatch.delenv("M5B_DES", raising=False)


DES = {"M5_0": "YES", "M5_4": "NO", "M5_91": "YES"}


def test_el_gate_solo_cuenta_dias_complete_y_con_desenlaces_oficiales_completos(monkeypatch):
    _dos_dias(monkeypatch)
    _estandar(monkeypatch)
    rep = ROB.informe(des=dict(DES))
    c = rep["cobertura"]
    assert c["dias_completos"] == [DIA] and c["dias_parciales"] == ["2026-10-18"] and c["disparos_oos"] == 5          # 5 senales del dia COMPLETE
    assert c["disparos_oos_en_dias_no_completos_excluidos_del_gate"] == 5 and c["motivos_parciales"]["2026-10-18"]
    assert rep["principal"]["n"] == 3 and rep["veredicto"]["veredicto"] == "PENDIENTE" and c["pendientes_desenlace"] == 0
    # desenlace oficial ausente en una llena del OOS: el gate NO se evalua (nunca "0" ni "excluida")
    rep = ROB.informe(des={"M5_0": "YES", "M5_4": "NO"})
    assert rep["veredicto"]["veredicto"] == "PENDIENTE_DESENLACES" and rep["veredicto"]["gate_bloqueado_por_pendientes"] and rep["cobertura"]["pendientes_desenlace"] >= 1
    txt = (ROB.SAL / "informe.txt").read_text()
    assert "dias COMPLETE 1" in txt and "parcial 2026-10-18" in txt


def test_dia_procesado_por_el_vigia_congelado_a_pelo_no_entra_en_el_gate(monkeypatch):
    fx()
    VG.procesar(DIA, forzar=True, ahora=AHORA)                                       # sin wrapper_sha256
    monkeypatch.setitem(VG.CONFIG, "congelado_utc", "2026-10-17T00:00:00+00:00")
    monkeypatch.setattr(VG, "hash_codigo", lambda: "x")
    monkeypatch.setattr(VG, "manifiesto", lambda dia=None: "x")
    _estandar(monkeypatch)
    rep = ROB.informe(des=dict(DES))
    assert rep["cobertura"]["dias_sin_verificar_wrapper"] == [DIA] and rep["cobertura"]["dias_completos"] == [] and rep["cobertura"]["disparos_oos"] == 0


def test_entorno_sustituido_queda_escrito_y_el_veredicto_no_es_valido(monkeypatch):
    _dos_dias(monkeypatch)
    _estandar(monkeypatch)
    des = TMP / "des.json"
    des.write_text(json.dumps(DES))
    monkeypatch.setenv("M5B_DES", str(des))
    e = ROB.entorno_no_estandar()
    assert e["M5B_DES"]["sha256"] == hashlib.sha256(des.read_bytes()).hexdigest()[:16]
    rep = ROB.informe()
    assert rep["veredicto"]["veredicto"].startswith("NO_VALIDO_ENTORNO_SUSTITUIDO:") and "M5B_DES" in rep["entorno_no_estandar"]
    assert rep["fuente_desenlaces"].startswith("M5B_DES") and "AVISO ENTORNO SUSTITUIDO" in (ROB.SAL / "informe.txt").read_text()
    monkeypatch.setattr(ROB, "DL_STD", "/otra/ruta")                                 # M5B_DL distinto del estandar tambien se anota
    assert "M5B_DL" in ROB.entorno_no_estandar()
    monkeypatch.delenv("M5B_DES")
    _estandar(monkeypatch)
    assert ROB.entorno_no_estandar() == {}
    m = ROB.procesar(DIA, forzar=True, ahora=AHORA, cierres_esperados=N)
    assert m["entorno_no_estandar"] == {} and (list((ROB.SAL / "runs").glob("run_*.json")))


# ------------------------------------------------------------------------------------------------ (10) flock del manifiesto
def test_bloqueo_exclusivo_serializa_procesar_e_informe():
    orden = []
    liberar = threading.Event()

    def uno():
        with ROB.bloqueo():
            orden.append("A entra")
            liberar.wait(5)
            orden.append("A sale")

    def dos():
        with ROB.bloqueo():
            orden.append("B entra")

    ta = threading.Thread(target=uno)
    ta.start()
    while "A entra" not in orden:
        time.sleep(0.01)
    tb = threading.Thread(target=dos)
    tb.start()
    time.sleep(0.3)
    assert orden == ["A entra"]                                                      # B espera mientras A tiene el candado
    liberar.set()
    ta.join(5)
    tb.join(5)
    assert orden == ["A entra", "A sale", "B entra"]


def test_manifiesto_atomico_sin_tmp_huerfano_tras_procesar():
    fx()
    ROB.procesar(DIA, forzar=True, ahora=AHORA, cierres_esperados=N)
    ROB.procesar(DIA, forzar=True, ahora=AHORA, cierres_esperados=N)
    mf = json.loads((ROB.SAL / "manifiesto.json").read_text())
    assert mf["versiones"]["1"]["dias"].count(DIA) == 1 and not list(ROB.SAL.glob("*.tmp"))
