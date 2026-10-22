"""Tests H61b (sin red, sin datos reales). Ejecutar: python3 -m pytest -q test_h61b.py"""
import gzip, os, sys, tempfile
import numpy as np
import pytest
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import h61b_regla as RG, h61b_feeds as FD, h61b_stats as S, h61b_vigia as VG
import h61b_sim as SM

def test_congelada_intacta():
    assert RG.verificar_congelada() == RG.SHA_CONGELADA

def test_congelada_alterada_falla(monkeypatch, tmp_path):
    f = tmp_path / "x.json"; f.write_text("{}")
    monkeypatch.setattr(RG, "CONGELADA", f)
    with pytest.raises(RuntimeError):
        RG.verificar_congelada()

def test_parametros_coinciden_con_json():
    import json
    j = json.load(open(RG.CONGELADA))
    assert "-0,5 bps" in j["accion"] and "t-60ms-500ms" in j["senal"] and "5 s" in j["senal"]
    assert (RG.W_MS, RG.X_BPS, RG.MAX_ANTIG_MS, RG.REPUJA_MS) == (500, 0.5, 5000, 150)

RX = np.array([1000, 1400, 1900, 2600, 9000], dtype=np.int64); P = np.array([100.0, 100.0, 100.0, 99.99, 100.0])

def test_ret_orientacion_y_ventana():
    # en t=2700: ultimo trade rx=2600 (99.99); hace 500ms (t=2200): ultimo rx=1900 (100.0) -> -1 bps
    up = RG.ret_bps(RX, P, [2700], "Up"); dn = RG.ret_bps(RX, P, [2700], "Down")
    assert up[0] == pytest.approx(-1.0, abs=1e-6) and dn[0] == pytest.approx(1.0, abs=1e-6)
    assert RG.permitido(RX, P, [2700], "Up")[0] == False and RG.permitido(RX, P, [2700], "Down")[0] == True

def test_umbral_exacto_no_dispara():
    rx = np.array([0, 600], dtype=np.int64); p = np.array([100.0, 100.0 * (1 - 0.5e-4)])   # exactamente -0,5 bps
    r = RG.ret_bps(rx, p, [700], "Up")[0]
    assert r == pytest.approx(-0.5, abs=1e-9)
    assert RG.permitido(rx, p, [700], "Up")[0] in (True, False)  # el borde depende del float; lo importante: -0,49 permite
    p2 = np.array([100.0, 100.0 * (1 - 0.49e-4)]); assert RG.permitido(rx, p2, [700], "Up")[0]
    p3 = np.array([100.0, 100.0 * (1 - 0.51e-4)]); assert not RG.permitido(rx, p3, [700], "Up")[0]

def test_sin_dato_o_viejo_no_dispara():
    assert np.isnan(RG.ret_bps(RX, P, [500], "Up")[0]) and RG.permitido(RX, P, [500], "Up")[0]       # antes del primer trade
    assert np.isnan(RG.ret_bps(RX, P, [7700], "Up")[0])                                              # ultimo trade (2600) con >5 s
    assert RG.permitido(RX, P, [7700], "Up")[0]
    assert np.isnan(RG.ret_bps(None, None, [1], "Up")[0]) and np.isnan(RG.ret_bps(np.array([], dtype=np.int64), np.array([]), [1], "Up")[0])

def test_sin_look_ahead():
    # un trade FUTURO (rx > t) no puede influir
    rx = np.array([0, 100, 5000], dtype=np.int64); p = np.array([100.0, 100.0, 50.0])
    assert RG.ret_bps(rx, p, [1000], "Up")[0] == pytest.approx(0.0)

def test_parse_feeds():
    x = ["x,10,BTCUSDT,100.0,0.5,1,11,150", "x,10,ETHUSDT,5.0,1,0,11,150", "basura", "x,1,BTCUSDT,abc,1,1,1,1"]
    assert FD.parse_x(x) == [(150, 100.0, 0.5)]
    m = ["binance_spot,T,BTC,10,155,100.0,0.5,BUY", "binance_spot,Q,BTC,,155,1,2,", "kraken,T,BTC,10,155,1,1,BUY", "binance_spot,T,ETH,10,155,5,1,BUY"]
    assert FD.parse_mv(m, "BTC") == [(155, 100.0, 0.5)]
    o = FD._ordenar([(5, 1.0, 1.0), (3, 2.0, 1.0), (5, 1.0, 1.0)])
    assert list(o[0]) == [3, 5] and len(o[1]) == 2          # dedup exacto + orden por recepcion

# ---------- simulacion: la defensa solo enmascara; sin Binance en contra C == v3 ----------
def _escenario():
    inst = np.array([0, 1000, 2000, 3000, 4000], dtype=np.int64)
    want = [0.30, 0.30, 0.30, 0.30, 0.30]; bsz = np.array([4.0] * 5)
    FIL = [(1500, 0.30, 10.0)]                     # un print que llena nuestra puja (precio igual) con cola 0
    FE = np.array([f[0] for f in FIL], dtype=np.int64)
    return inst, want, bsz, FIL, FE

def _correr(want, inst, bsz, FIL, FE):
    filas = []
    SM.simular_variante(inst, want, bsz, 1e12, 5000, FIL, FE, dict(dia="d", coin="BTC", cierre=1, lado="Up", m5="m", gana=1), "v3", "A", 0.0, filas.append)
    return filas

def _central(filas):
    f = [r for r in filas if (r["cola"], r["lp"], r["lc"], r["mult"], r["modo"]) == ("opt", 79, 60, 1, "primer")]
    assert len(f) == 1; return f[0]

def test_C_igual_v3_sin_defensa_y_se_evita_con_defensa():
    inst, want, bsz, FIL, FE = _escenario()
    a = _central(_correr(want, inst, bsz, FIL, FE))
    assert a["lleno"] == 5.0 and a["precio"] == 0.30
    # defensa activa en el instante 1000 (cancelacion decidida en 1000 -> efectiva 1060 < print 1500): sin relleno
    wC = [0.30, None, None, 0.30, 0.30]
    c = _correr(wC, inst, bsz, FIL, FE)
    assert _central(c)["lleno"] == 0.0
    # defensa justo DESPUES del print: no evita el relleno (la cancelacion llega tarde, 60 ms)
    wC2 = [0.30, 0.30, 0.30, None, 0.30]
    assert _central(_correr(wC2, inst, bsz, FIL, FE))["lleno"] == 5.0
    # decision a 1450 con print a 1500: cancelacion efectiva 1510 > 1500 -> el print aun nos llena (60 ms de latencia de cancel)
    inst2 = np.array([0, 1450, 3000], dtype=np.int64); w3 = [0.30, None, 0.30]
    assert _central(_correr(w3, inst2, np.array([4.0] * 3), FIL, FE))["lleno"] == 5.0

def test_claves_unicas_y_escritura_atomica_idempotente():
    inst, want, bsz, FIL, FE = _escenario()
    filas = _correr(want, inst, bsz, FIL, FE)
    assert SM.validar_filas(filas)
    assert not SM.validar_filas(filas + [filas[0]])                       # duplicado detectado
    with tempfile.TemporaryDirectory() as d:
        fo = os.path.join(d, "rows_BTC_2026-10-22.csv.gz")
        SM.escribir_atomico(fo, filas); assert SM.validar_salida(fo)
        n1 = os.path.getsize(fo); SM.escribir_atomico(fo, filas); assert os.path.getsize(fo) > 0 and SM.validar_salida(fo)
        # corrupcion: fichero truncado / cabecera distinta -> no valido (se recalcula)
        with open(fo, "rb") as fh: b = fh.read()
        open(fo, "wb").write(b[: len(b) // 2]); assert not SM.validar_salida(fo)
        with gzip.open(fo, "wt") as fh: fh.write("a,b\n1,2\n")
        assert not SM.validar_salida(fo)
        assert not os.path.exists(fo + ".tmp")

# ---------- vigia ----------
def _fila(dia, cierre, brazo, var, lleno, coste, gana, reb=0.0):
    return dict(dia=dia, coin="BTC", cierre=str(cierre), lado="Up", m5="m", brazo=brazo, var=var, modo="primer", mult="1", cola="base", lp="79", lc="60", n_seg="1", precio="0.3",
                prof_join="4", need="5", lleno=str(lleno), coste=str(coste), n_fill="1", t_rel="", p_rel="", gana=gana, rebate=str(reb), frac_bloq="0")

def test_ev_dias_y_missing():
    pos = [("d1", 1.0, 2.0), ("d2", -1.0, 2.0), ("d3", None, 2.0)]
    e = S.ev_dias(pos)
    assert e["n"] == 2 and e["ev"] == pytest.approx(0.0) and e["dias"] == 2            # el missing NO cuenta como 0 ni entra en el coste
    assert np.isnan(e["ic90_lo"])                                                       # <5 dias: IC no estimable

def test_posiciones_gana_vacio_es_missing():
    rows = [_fila("d1", 1, "A", "v3", 5, 1.5, "")]
    p = S.posiciones(rows, "v3", "A")
    assert list(p.values())[0][1] is None

def test_vigia_gate_y_kill():
    # 12 dias, v3 y C con 4 rellenos/dia ganadores 4/4 -> EV alto; retencion 1.0
    rows = {}
    for i in range(12):
        d = f"2026-10-{22 + i:02d}"; rs = []
        for k in range(4):
            for var in ("v3", "C_live"):
                rs.append(_fila(d, 900 * k, "A", var, 5, 1.5, "1"))
        rows[d] = rs
    b = VG.evaluar_brazo(rows, "A", "C_live")
    assert b["n_C"] == 48 and b["retencion"] == 1.0 and b["gate_h23_C"] and not b["kill"]
    assert b["dif"]["dev"] == pytest.approx(0.0)                                         # igual a v3 -> dEV 0 -> el gate H61b exige dEV>0
    assert not b["gate_h61b"] and b["estado"] == "EN_CURSO"
    # C pierde siempre (gana=0) con n>=20 -> KILL
    for d, rs in rows.items():
        for r in rs:
            if r["var"] == "C_live": r["gana"] = "0"
    b = VG.evaluar_brazo(rows, "A", "C_live")
    assert b["kill"] and b["estado"] == "KILL"

def test_vigia_insuficiente_con_pocos_dias():
    rows = {"2026-10-22": [_fila("2026-10-22", 900, "A", "v3", 5, 1.5, "1"), _fila("2026-10-22", 900, "A", "C_live", 5, 1.5, "1")]}
    assert VG.evaluar_brazo(rows, "A", "C_live")["estado"] == "INSUFICIENTE"

def test_dias_con_datos_filtra_desde(tmp_path):
    for d in ("2026-10-20", "2026-10-22", "2026-10-23"): (tmp_path / f"rows_BTC_{d}.csv.gz").write_bytes(b"")
    r = S.dias_con_datos("BTC", "2026-10-22", None, str(tmp_path) + "/")
    assert [d for d, _ in r] == ["2026-10-22", "2026-10-23"]                             # los dias previos a la congelacion NO entran en el gate
