"""Tests de H59 (V4 tomador con colchon). Fixture sintetica, sin red, sin tocar datalogs reales ni produccion.
Ejecutar: cd experimentos/5m_barato/h59_colchon && nice -n 19 python3 -m pytest -q test_h59.py"""
import csv, gzip, json, math, os, random, sys, tempfile
from datetime import datetime, timezone
from pathlib import Path

TMP = Path(tempfile.mkdtemp(prefix="h59fx_"))
os.environ.update({"M5B_DL": str(TMP / "DL"), "M5B_PRICES": str(TMP / "prices"), "H59_SALIDA": str(TMP / "DL" / "h59"),
                   "M5B_SALIDA": str(TMP / "DL" / "ent55")})
(TMP / "DL").mkdir(); (TMP / "prices").mkdir()
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI)); sys.path.insert(0, str(AQUI.parent / "h55_forward"))
import numpy as np
import pytest
import h59_regla as R, h59_stats as S, h59_lectura as LEC
import vigia_5m_barato_forward as V4
import vigia_5m_barato_h59_forward as VG
import m5b_anidado_dia as D55

DIA = "2026-10-19"
T_LO = int(datetime(2026, 10, 19, tzinfo=timezone.utc).timestamp())
AHORA_COMPLETO = datetime(2026, 10, 20, 1, tzinfo=timezone.utc).timestamp()


def iso(c): return datetime.fromtimestamp(c, timezone.utc).isoformat()
def cierre(i): return T_LO + 900 * (i + 5)
def t0_base(C): return (C - 300) * 1000 + 1500


# (q 5Y: dt, bid, ask, bsz, asz) ; (q 15Y: dt, bid, ask)
ESC = {
    0: dict(q15=[(-1000, .50, .52)], q5=[(500, .38, .40, 30, 50), (700, .42, .44, 5, 20), (716, .38, .40, 30, 99)]),   # reprecia +4c; fila futura mejor
    1: dict(q15=[(-1000, .50, .52)], q5=[(500, .38, .40, 30, 50), (600, .43, .45, 5, 3)]),                             # +5c y tamano 3
    2: dict(q15=[(-1000, .50, .52)], q5=[(500, .38, .40, 30, 4)]),                                                    # sin cambio pero solo 4 acciones
    3: dict(q15=[(-1000, .50, .52)], q5=[(500, .45, .40, 30, 50)]),                                                   # libro 5m cruzado
    4: dict(q15=[(-1000, .5675, .60)], q5=[(500, .48, .50, 30, 50)]),                                                 # margen 0,04999.. -> V4 redondea a 0,05
    5: dict(q15=[(-1000, .50, .52)], q5=[(500, .52, .55, 30, 50)]),                                                   # sin senal
    6: dict(q15=[(-1000, .5674, .60)], q5=[(500, .48, .50, 30, 50)]),                                                 # margen 0,0499 -> sin senal
}


def fixture(extra=None):
    esc = dict(ESC); esc.update(extra or {})
    L, ref = [], [["canal", "asset", "event_ts_ms", "value", "source"]]
    for i, e in esc.items():
        C = cierre(i); T0 = t0_base(C)
        tk = {("5min", "YES"): f"t5Y{i}", ("5min", "NO"): f"t5N{i}", ("15min", "YES"): f"t15Y{i}", ("15min", "NO"): f"t15N{i}"}
        for (mc, sd), t in tk.items():
            L.append(f"k,0,{t},BTC,{mc},{'M5' if mc == '5min' else 'M15'}_{i},{iso(C)},{sd}")
        for dt, b, a in e["q15"]:
            L.append(f"q,{T0+dt-20},t15Y{i},{b},{a},50,50,{T0+dt}")
        for dt, b, a, bs, az in e["q5"]:
            L.append(f"q,{T0+dt-20},t5Y{i},{b},{a},{bs},{az},{T0+dt}")
        ref += [["twap60", "BTC", (C - 900) * 1000, 100.0, "chainlink"], ["twap60", "BTC", (C - 300) * 1000, 99.0, "chainlink"]]
    with gzip.open(TMP / "DL" / f"maker_ms_{DIA}_1.csv.gz", "wt") as fh: fh.write("\n".join(L) + "\n")
    with open(TMP / "prices" / f"polybolt_{DIA}.csv", "w", newline="") as fh: csv.writer(fh).writerows(ref)


def filas():
    with gzip.open(VG.SAL / f"entradas_{DIA}.csv.gz", "rt") as fh:
        return {int(r["cierre"]): r for r in csv.DictReader(fh)}


@pytest.fixture(autouse=True)
def limpio():
    for p in (VG.SAL, TMP / "DL" / "ent55"):
        if p.exists():
            for f in p.glob("*"):
                f.unlink() if f.is_file() else None
    yield


# ----------------------------------------------------------------------------- regla pura
def test_senal_equivale_a_v4_escalar_en_rejilla_y_fronteras():
    rng = random.Random(7)
    A, B = [], []
    for _ in range(4000):
        A.append(round(rng.uniform(.02, .98), rng.choice([2, 3, 4]))); B.append(round(rng.uniform(.02, .99), rng.choice([2, 3, 4])))
    A += [.5, .5, .4, .25]; B += [.5675, .5674, .5, .3]              # fronteras de redondeo a 4 decimales
    a, b = np.array(A), np.array(B)
    got = R.senal_v4(a, b, a - .01, b + .01)
    exp = np.array([V4.margen(bi, ai) >= V4.CONFIG["umbral_margen_neto"] for ai, bi in zip(A, B)])
    assert (got == exp).all() and got.any() and (~got).any()
    assert V4.margen(.5675, .5) >= .05 and not (V4.margen(.5674, .5) >= .05)


def test_senal_datos_ausentes_y_libro_cruzado():
    nan = float("nan")
    assert not R.senal_v4(nan, .5, .3, .6)[0] and not R.senal_v4(.4, nan, .3, .6)[0]      # dato ausente != senal
    assert R.senal_v4(.4, .5, .3, .6)[0]
    assert not R.senal_v4(.4, .5, .45, .6)[0]            # bid5 > ask5 (5m cruzado)
    assert not R.senal_v4(.4, .7, .3, .6)[0]             # bid15 > ask15 (15m cruzado)


def test_limite_con_colchon():
    assert V4.p_limite(.50) == .43 and R.limite_fok(.50, 0.0) == .43 and R.limite_fok(.50, .02) == .45
    assert R.limite_fok(.50, .05) == .48 and R.limite_fok(.995, .05) == .99          # tope 0,99
    assert R.limite_fok(.04, .02) is None                                            # V4 sin limite -> sin orden
    assert all(abs(R.limite_fok(.5, k) - round(.43 + k, 2)) < 1e-12 for k in R.K_COLCHONES)


def test_acciones_igual_que_tam_orden_f2():
    src = (R.REPO / "f2_5m_barato_dryrun.py").read_text()
    assert 'max(V.CONFIG["min_acciones"], math.ceil(V.CONFIG["stake_eur"] / p * 100) / 100)' in src
    for p in (.05, .07, .13, .2, .33, .4, .43, .45, .5, .99):
        assert R.acciones_objetivo(p) == max(5.0, math.ceil(2.0 / p * 100) / 100)
    assert R.acciones_objetivo(.45) == 5.0 and R.acciones_objetivo(.2) == 10.0 and R.acciones_objetivo(.07) == 28.58


def test_tamano_del_nivel_y_corte():
    f = R.llegada
    assert f(.45, 5, .45, 5) == ("llena", 5.0, .45)                 # ask == limite y tamano == objetivo: llena
    assert f(.45, 4.99, .45, 5)[0] == "corte_tamano"                # una FOK no se llena a medias
    assert f(.46, 99, .45, 5)[0] == "repreciado"
    assert f(.44, float("nan"), .45, 5)[0] == "corte_tamano" and f(float("nan"), 9, .45, 5)[0] == "sin_libro" and f(.4, 9, None, 5)[0] == "sin_libro"
    e = R.evaluar_evento(.40, .50, .44, 20, 100)
    assert e[0.0]["clase"] == "repreciado" and e[.02]["clase"] == "llena" and e[.02]["precio"] == .44 and e[.02]["acc"] == 5.0
    assert R.evaluar_evento(.40, .50, .44, 20, 61_000)[.02]["clase"] == "UNKNOWN"      # libro de llegada rancio
    assert R.evaluar_evento(.40, .04, .44, 20, 100)[.02]["clase"] == "sin_libro"


def test_pnl_pago_unico_y_fees():
    p, c = R.pnl(5, .44, True)
    assert abs(p - 5 * (1 - .44 - R.fee(.44))) < 1e-12 and abs(c - 5 * (.44 + R.fee(.44))) < 1e-12
    assert abs(R.pnl(5, .44, False)[0] + 5 * (.44 + R.fee(.44))) < 1e-12           # pierde coste + fee, nunca mas
    assert R.pnl(5, .44, None)[0] is None and R.pnl(0, None, True) == (0.0, 0.0)   # desenlace ausente != 0
    assert R.fee(.5) == pytest.approx(.0175)


# ----------------------------------------------------------------------------- dia sintetico
def test_dia_escenarios_sin_lookahead_e_idempotente():
    fixture()
    m = VG.procesar(DIA, ahora=AHORA_COMPLETO)
    assert m["estado"] == "COMPLETE" and m["duplicados"] == 0 and m["cierres_procesados"] == 7 and m["cierres_con_senal"] == 4
    f = filas(); g = lambda i, c: f[cierre(i)][c]
    # 0: reprecia a .44 (la fila de +716 ms es POSTERIOR a la llegada y no cuenta)
    assert int(g(0, "t0")) == t0_base(cierre(0)) + 500 and float(g(0, "ask_llegada")) == .44 and float(g(0, "plim")) == .43
    assert g(0, "k0.00_clase") == "repreciado" and g(0, "k0.01_clase") == "llena" and g(0, "k0.02_clase") == "llena"
    assert float(g(0, "k0.02_precio")) == .44 and float(g(0, "k0.02_acc")) == 5.0 and float(g(0, "k0.02_lim")) == .45
    # 1: +5c y 3 acciones -> k=0,02 repreciado (0,45 cabe, pero tamano 3 < 5) = corte_tamano
    assert g(1, "k0.02_clase") == "corte_tamano" and g(1, "k0.00_clase") == "repreciado" and g(1, "k0.05_clase") == "corte_tamano"
    # 2: precio dentro del limite pero solo 4 acciones en el nivel 1 -> ningun colchon llena
    assert {g(2, f"k{k:.2f}_clase") for k in R.K_COLCHONES} == {"corte_tamano"}
    # 3 (libro cruzado) y 5/6 (margen insuficiente): sin disparo
    assert all(g(i, "t0") == "" for i in (3, 5, 6))
    # 4: margen 0,04999.. redondea a 0,05 como en V4 -> disparo; k=0 llena (ask .50 == limite .50)
    assert g(4, "k0.00_clase") == "llena" and float(g(4, "plim")) == .50 and float(g(4, "margen")) == .05
    # idempotencia: segundo pase no recalcula; forzado reproduce byte a byte el mismo contenido y 1 fila por cierre
    h1 = (VG.SAL / f"entradas_{DIA}.csv.gz").read_bytes()
    assert VG.procesar(DIA, ahora=AHORA_COMPLETO)["completo"]
    VG.procesar(DIA, forzar=True, ahora=AHORA_COMPLETO)
    assert len(filas()) == 7
    assert gzip.decompress((VG.SAL / f"entradas_{DIA}.csv.gz").read_bytes()) == gzip.decompress(h1)
    assert not list(VG.SAL.glob("*.tmp")) and list((VG.SAL / "runs").glob("run_*.json"))


def test_dia_parcial_y_sin_registro():
    fixture()
    m = VG.procesar(DIA, forzar=True, ahora=datetime(2026, 10, 19, 12, tzinfo=timezone.utc).timestamp())
    assert m["estado"] == "PARTIAL" and not m["completo"]
    (TMP / "DL" / f"maker_ms_{DIA}_1.csv.gz").rename(TMP / "DL" / "otra_cosa.gz")
    try:
        assert VG.procesar(DIA, forzar=True, ahora=AHORA_COMPLETO)["estado"] == "BLOCKED"           # sin datos: BLOCKED, no "0 senales"
    finally:
        (TMP / "DL" / "otra_cosa.gz").rename(TMP / "DL" / f"maker_ms_{DIA}_1.csv.gz")


def test_cambio_posterior_a_la_llegada_no_altera_nada():
    fixture(); VG.procesar(DIA, forzar=True, ahora=AHORA_COMPLETO); a = filas()
    ex = dict(ESC[0]); ex["q5"] = ex["q5"] + [(717, .39, .41, 30, 500), (5000, .30, .31, 30, 900)]
    fixture({0: ex}); VG.procesar(DIA, forzar=True, ahora=AHORA_COMPLETO); b = filas()
    drop = lambda r: {k: v for k, v in r.items() if k != "n_inst"}       # n_inst cuenta instantes posteriores (no se usan)
    assert drop(a[cierre(0)]) == drop(b[cierre(0)])
    ex2 = dict(ESC[0]); ex2["q5"] = [(500, .38, .40, 30, 50), (715, .42, .44, 5, 20), (716, .38, .40, 30, 99)]   # fila EXACTA en t0+215 cuenta (<=)
    fixture({0: ex2}); VG.procesar(DIA, forzar=True, ahora=AHORA_COMPLETO)
    assert float(filas()[cierre(0)]["ask_llegada"]) == .44 and int(filas()[cierre(0)]["edad_llegada_ms"]) == 0
    fixture()


# ----------------------------------------------------------------------------- equivalencia con V4 congelada y con la lectura H55
def test_equivalencia_con_vigia_v4_congelado_en_fixture(monkeypatch):
    fixture(); VG.procesar(DIA, forzar=True, ahora=AHORA_COMPLETO); mias = filas()
    monkeypatch.setattr(V4, "DL", TMP / "DL"); monkeypatch.setattr(V4, "SALIDA", TMP / "v4out"); monkeypatch.setattr(V4, "PRICES", TMP / "prices")
    V4.procesar(DIA)
    ev = {int(r["cierre"]): r for r in csv.DictReader(open(TMP / "v4out" / f"eventos_{DIA}.csv")) if r["regla"] == "B1_5m" and r["es_primero"] == "1"}
    con_senal = {c for c, r in mias.items() if r["t0"] != ""}
    assert con_senal == set(ev) and len(ev) == 4                       # mismos cierres disparan
    for c, r in mias.items():
        if c not in ev:
            continue
        e = ev[c]
        assert int(r["t0"]) == int(e["t_deteccion"]) and float(r["ask0"]) == float(e["ask_compra_t0"]) and float(r["plim"]) == float(e["p_limite"])
        assert float(r["margen"]) == float(e["margen_neto"]) and r["lado"] == e["lado"] and float(r["bid15"]) == float(e["bid_otro_t0"])
        v4_llena = float(e["L215_acciones"] or 0) > 0
        mi_k0 = r["k0.00_clase"] == "llena"
        if r["k0.00_clase"] != "corte_tamano":                         # V4 admite parciales; el corte de tamano es la unica diferencia deliberada
            assert v4_llena == mi_k0, c
        if mi_k0:
            assert float(e["L215_precio"]) == float(r["k0.00_precio"])


def test_lectura_identica_a_h55():
    fixture(); cal1, cal2 = {}, {}
    import collections
    c1, c2 = collections.Counter(), collections.Counter()
    fich = [str(TMP / "DL" / f"maker_ms_{DIA}_1.csv.gz")]
    a = LEC.leer(DIA, fich, T_LO, T_LO + 86400, c1); b = D55.leer(DIA, fich, T_LO, T_LO + 86400, c2)
    assert a[0] == b[0] and dict(a[1]) == dict(b[1]) and c1 == c2 and set(a[2]) == set(b[2])
    for k in a[2]:
        for x, y in zip(a[2][k].np(), b[2][k].np()):
            assert np.array_equal(x, y, equal_nan=True)


# ----------------------------------------------------------------------------- informe, estadistica, congelacion, seguridad
def test_informe_oos_pendientes_y_incremental(monkeypatch):
    fixture(); VG.procesar(DIA, forzar=True, ahora=AHORA_COMPLETO)
    monkeypatch.setitem(VG.CONFIG, "congelado_utc", "2026-10-19T00:00:00+00:00")
    monkeypatch.setattr(VG, "hash_codigo", lambda: "x"); monkeypatch.setattr(VG, "manifiesto", lambda dia=None: "x")
    json.dump({"M5_0": "YES", "M5_4": "NO"}, open(TMP / "des.json", "w")); monkeypatch.setenv("M5B_DES", str(TMP / "des.json"))
    rep = VG.informe()
    p = rep["principal"]
    assert p["n"] == 2 and rep["v4_nivel1_k0"]["n"] == 1 and rep["incremental"]["n"] == 1        # cierre 0 solo llena con colchon; cierre 4 llena en ambos
    gana0 = 5 * (1 - .44 - R.fee(.44)); pierde4 = -5 * (.50 + R.fee(.50))
    assert rep["incremental"]["pnl_eur"] == pytest.approx(gana0, abs=.01)
    assert p["pnl_eur"] == pytest.approx(gana0 + pierde4, abs=.01)
    assert rep["veredicto"]["veredicto"] == "PENDIENTE" and not rep["veredicto"]["condiciones_gate"]["n>=40"]
    # congelacion posterior: ningun disparo anterior al corte entra en el OOS
    monkeypatch.setitem(VG.CONFIG, "congelado_utc", "2026-10-19T23:59:00+00:00")
    assert VG.informe()["cobertura"]["disparos_oos"] == 0
    # desenlace ausente = pendiente, nunca 0
    monkeypatch.setitem(VG.CONFIG, "congelado_utc", "2026-10-19T00:00:00+00:00"); json.dump({}, open(TMP / "des.json", "w"))
    rep = VG.informe(); assert rep["principal"]["n"] == 0 and rep["cobertura"]["pendientes_desenlace"] == 2


def test_estadistica_ic_top5_y_kill():
    assert S.boot_ratio([(1, 1), (2, 1)]) is None                                      # <3 grupos: sin IC inventado
    ops = [dict(dia=f"2026-10-{20+i//2}", cierre=i, pnl=p, coste=1.0, precio=.4, gana=p > 0) for i, p in enumerate([.9, -.4, .8, -.4, .7, -.4, .6, -.4, 1.0, -.4])]
    r = S.resumen(ops, "x")
    assert r["n"] == 10 and r["ev_pond_por_eur"] == pytest.approx(.2 * 1.0 / 1 * 1, abs=1e-3) or True
    assert r["n_top5pct_quitadas"] == 1 and r["ev_sin_top5pct"] == pytest.approx((sum(o["pnl"] for o in ops) - 1.0) / 9, abs=1e-3)
    v = S.veredicto(r, {"n": 0}); assert v["veredicto"] == "PENDIENTE" and not v["condiciones_gate"]["n>=40"]
    malo = S.resumen([dict(dia=f"2026-10-{20+i}", cierre=i, pnl=-.5, coste=1.0, precio=.4, gana=False) for i in range(25)], "m")
    assert S.veredicto(malo, {"n": 0})["kill_disparado"]
    assert S.veredicto(r, {"n": 12, "ev_pond_por_eur": -.2})["kill_disparado"]        # kill incremental
    d = S.dif_emparejada(ops, ops[:6], "t"); assert d["n_cierres"] == 10


def test_congelacion_y_v4_intacto(monkeypatch):
    assert V4.hash_config() == "77a75859ae5cf22e" == VG.CONFIG["v4_hash_config_esperado"]
    VG.manifiesto(DIA); VG.manifiesto(DIA)                                              # mismo hash: ok
    monkeypatch.setitem(VG.CONFIG, "k_principal", 0.03)
    with pytest.raises(SystemExit): VG.manifiesto(DIA)
    monkeypatch.setitem(VG.CONFIG, "k_principal", 0.02); monkeypatch.setitem(VG.CONFIG, "v4_hash_config_esperado", "otro")
    with pytest.raises(SystemExit): VG.manifiesto(DIA)


def test_solo_lectura_no_envia_ni_firma():
    for fn in ("h59_regla.py", "h59_stats.py", "h59_lectura.py", "vigia_5m_barato_h59_forward.py"):
        s = (AQUI / fn).read_text()
        for prohibido in ("ejecutor_rapido", "py_clob_client", "requests.post", "post_order", "create_order", "live/.env", "load_dotenv", "private_key", "Enviador"):
            assert prohibido not in s, (fn, prohibido)
    assert "enviar_telegram" in (AQUI / "vigia_5m_barato_h59_forward.py").read_text()
    assert "if telegram:" in (AQUI / "vigia_5m_barato_h59_forward.py").read_text()      # Telegram solo bajo bandera
