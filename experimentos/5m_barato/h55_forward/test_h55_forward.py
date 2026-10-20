"""Tests del vigia H55/H53/H54 (fixture sintetica, sin red, sin tocar datalogs reales). Ejecutar: python3 -m pytest -q test_h55_forward.py"""
import csv, gzip, json, os, sys, tempfile
from datetime import datetime, timezone
from pathlib import Path
TMP = Path(tempfile.mkdtemp(prefix="h55fx_"))
os.environ.update({"M5B_DL": str(TMP / "DL"), "M5B_PRICES": str(TMP / "prices"), "M5B_SALIDA": str(TMP / "DL" / "ent")})
(TMP / "DL").mkdir(); (TMP / "prices").mkdir()
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pytest
import numpy as np
import m5b_anidado_regla as R, m5b_anidado_dia as D, m5b_anidado_stats as S

DIA, C = "2026-10-19", 1792368000 + 900
T0 = (C - 300) * 1000 + 1500


def iso(c): return datetime.fromtimestamp(c, timezone.utc).isoformat()


def fixture(gana_sl="YES"):
    toks = {("5min", "YES"): "t5Y", ("5min", "NO"): "t5N", ("15min", "YES"): "t15Y", ("15min", "NO"): "t15N"}
    L = []
    for (mc, sd), tk in toks.items():
        L.append(f"k,0,{tk},BTC,{mc},{'M5' if mc == '5min' else 'M15'},{iso(C)},{sd}")
    q = lambda rx, tk, b, a, bs, as_: f"q,{rx-20},{tk},{b},{a},{bs},{as_},{rx}"
    L += [q(T0 - 1000, "t15Y", .80, .82, 50, 50), q(T0 + 500, "t5Y", .60, .70, 30, 100),
          q(T0 + 800, "t5Y", .60, .70, 30, 100), q(T0 + 900, "t15Y", .80, .82, 50, 50)]
    L.append(f"t,{T0+680},t5Y,0.59,SELL,10,{T0+700}")          # venta del token s a 0,59: atraviesa nuestro bid 0,60
    d = TMP / "DL"
    with gzip.open(d / f"maker_ms_{DIA}_1.csv.gz", "wt") as fh: fh.write("\n".join(L) + "\n")
    with open(TMP / "prices" / f"polybolt_{DIA}.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["canal", "asset", "event_ts_ms", "value", "source"])
        w.writerow(["twap60", "BTC", (C - 900) * 1000, 100.0, "chainlink"]); w.writerow(["twap60", "BTC", (C - 300) * 1000, 99.0, "chainlink"])
    json.dump({"M5": gana_sl}, open(TMP / "des.json", "w")); os.environ["M5B_DES"] = str(TMP / "des.json")


def test_regla_fronteras():
    a, b = np.array([.5, .95, .96, .49]), np.array([.55, 1.0, 1.0, .6])
    assert list(R.senal("H55", a, b, a - .01, b + .01)) == [R.margen(.55, .5) >= -.05, R.margen(1.0, .95) >= -.05, False, False]
    assert not R.senal("H55", .6, .6, .6, .5)                 # libro cruzado (bid15 > ask15)
    assert not R.senal("H53", np.nan, .5, .4, .6)             # dato ausente no es senal
    assert R.senal("H53", .3, .34, .29, .35) and not R.senal("V4", .3, .34, .29, .35)
    assert R.senal("H55", .7, .8, .69, .81) == R.senal("H55", np.array([.7]), np.array([.8]), np.array([.69]), np.array([.81]))[0]


def test_pnl_y_llegada():
    assert R.llegada_tomador(.71, 9, .70, 5) == (0.0, None) and R.llegada_tomador(.70, 3, .70, 5) == (3.0, .70)
    p, c = R.pnl_tomador(5, .7, True); assert abs(p - 5 * (.3 - R.fee(.7))) < 1e-12 and abs(c - 5 * (.7 + R.fee(.7))) < 1e-12
    assert R.pnl_tomador(5, .7, None)[0] is None and R.pnl_tomador(0, None, True) == (0.0, 0.0)
    assert R.combinado_una_via(5, 1000, 950, True) == "maker" and R.combinado_una_via(5, 1100, 1000, True) == "tomador"
    assert R.combinado_una_via(0, None, None, False) == "nada" and R.combinado_una_via(5, 10, None, False) == "maker"


def test_dia_fixture_idempotente():
    fixture()
    now = datetime(2026, 10, 20, 1, tzinfo=timezone.utc).timestamp()
    m = D.procesar_dia(DIA, ahora=now)
    assert m["completo"] and m["cierres_con_fila"] == 1
    fo = D.SALIDA / f"entradas_{DIA}.csv.gz"
    rows = list(csv.DictReader(gzip.open(fo, "rt"))); r = rows[0]
    assert r["lado"] == "Up" and int(r["h55_t"]) == T0 + 500 and float(r["h55_precio"]) == .7 and float(r["h55_acc"]) == 5
    assert r["h53_t"] == r["h55_t"] == r["v4_t"] and float(r["mk_lleno"]) == 5 and float(r["mk_coste"]) == 3.0
    h1 = open(fo, "rb").read()
    D.procesar_dia(DIA, ahora=now)                                  # reintento: no duplica
    D.procesar_dia(DIA, forzar=True, ahora=now)                     # recalculo: mismo contenido y 1 sola fila por cierre
    assert len(list(csv.DictReader(gzip.open(fo, "rt")))) == 1
    ok, par, dc, dp = S.cargar(); assert dc == [DIA] and len(ok) == 1
    des = S.desenlace_por_m5(ok)
    o55, c = S.brazo_tomador(ok, "h55", des); assert len(o55) == 1 and abs(o55[0]["pnl"] - 5 * (.3 - R.fee(.7))) < 1e-9
    om, _ = S.brazo_maker(ok, des); assert abs(om[0]["pnl"] - (5 - 3.0 + .2 * R.fee(.6) * 5)) < 1e-9
    oc, cc = S.brazo_combinado(ok, des); assert cc["tomador"] == 1 and oc[0]["via"] == "tomador"       # maker relleno > t+60 ms
    # desenlace ausente = pendiente, nunca 0
    assert S.brazo_tomador(ok, "h55", {})[1]["pendiente_desenlace"] == 1


def test_dia_parcial_no_cuenta():
    fixture()
    D.procesar_dia(DIA, forzar=True, ahora=datetime(2026, 10, 19, 12, tzinfo=timezone.utc).timestamp())
    ok, par, dc, dp = S.cargar(); assert dc == [] and dp == [DIA] and ok == [] and len(par) == 1


def test_estadistica_y_kill():
    ops = [dict(dia=f"2026-10-{19+i//3}", cierre=i, pnl=p, coste=1.0, precio=.92, gana=p > 0, acc=5) for i, p in enumerate([.1, -.9, .1, .1, -.9, .2, .05, .1, -.05])]
    r = S.resumen(ops, "x", 3)
    assert r["n"] == 9 and abs(r["ev_pond_por_eur"] - sum(o["pnl"] for o in ops) / 9) < 1e-3 and len(r["perdidas_con_precio_ge_090"]) == 3
    assert S.veredicto_h55(r)["kill_disparado"]                    # >=2 perdidas con ask>=0,90 en 10 dias
    d = S.dif_emparejada(ops, ops[:6], "t"); assert d["n_cierres"] == 9 and d["ic90_por_cierre"][0] <= d["dif"] <= d["ic90_por_cierre"][1]
    assert S.boot_ratio([(1, 1), (2, 1)]) is None                  # <3 grupos: sin IC inventado


def test_congelacion():
    cfg = {"version": 9, "x": 1}
    S.manifiesto(TMP / "m", "t", cfg, [Path(R.__file__)])
    S.manifiesto(TMP / "m", "t", cfg, [Path(R.__file__)], dia="2026-10-19")      # mismo hash: ok
    with pytest.raises(SystemExit): S.manifiesto(TMP / "m", "t", dict(cfg, x=2), [Path(R.__file__)])


def test_solo_lectura_no_envia():
    for m in (R, D, S):
        src = Path(m.__file__).read_text()
        assert "ejecutor_rapido" not in src and "py_clob_client" not in src and "requests.post" not in src
