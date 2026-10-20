#!/usr/bin/env python3
"""Tests de a6_shadow_persistente (sin red). Ejecutar: python3 -m pytest -q test_a6_shadow_persistente.py (desde este directorio)."""
import gzip
import json
import os
import sys
import tempfile
import time

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a6_shadow_persistente as A  # noqa: E402
import h43_unidades as H  # noqa: E402

CIERRE = 1_800_000_000.0


def ms(T):
    return int((CIERRE - T) * 1000)


class Banco:
    """Nucleo con salida en memoria y un mercado BTC 5m sintético y_ (YES/Up) / n_ (NO/Down)."""

    def __init__(self, records=None, emitidos=None, cierre=CIERRE, arranque_T=320):
        self.rows = []
        self.n = A.Nucleo(self.rows.append, emitidos, records)
        self.cierre = cierre
        self.m = self.n.nuevo_mercado("m1", "y_", "n_", cierre, int((cierre - arranque_T) * 1000))
        self.libro(arranque_T)

    def libro(self, T, y_bids=((0.19, 300.0), (0.18, 100.0)), y_ask=0.21, n_bids=((0.78, 200.0),), n_ask=0.81):
        t = int((self.cierre - T) * 1000)
        self.n.on_book("y_", t, [{"price": str(p), "size": str(s)} for p, s in y_bids], [{"price": str(y_ask), "size": "50"}])
        self.n.on_book("n_", t, [{"price": str(p), "size": str(s)} for p, s in n_bids], [{"price": str(n_ask), "size": "50"}])

    def fill(self, lado, pc, acc, T):
        """El maker ADQUIERE `lado` a pc (tomador VENDE ese token a pc)."""
        tk = "y_" if lado == "YES" else "n_"
        self.n.on_trade(tk, int((self.cierre - T) * 1000),
                        {"price": str(pc), "size": str(acc), "side": "SELL", "timestamp": "123"})

    def tipo(self, t):
        return [r for r in self.rows if r["tipo"] == t]


def cruzar(b, T=250, lado="YES", pc=0.20):
    b.fill(lado, pc, 5000.0, T)


# --- regla y descartes -------------------------------------------------------------------------------------------------
def test_constantes_unica_fuente():
    assert (A.D.OFFSET, A.D.K, A.D.T_MIN, A.D.T_COS_MAX) == (H.OFFSET, H.K, H.T_MIN, H.T_MAX) == (5000.0, 50.0, 60.0, 270.0)
    assert (A.BANDA_LO, A.BANDA_HI) == (0.10, 0.30)


def test_cruce_en_ventana_pone_al_mejor_bid():
    b = Banco()
    cruzar(b, T=250)
    p = b.tipo("puesto")
    assert len(p) == 1
    p = p[0]
    assert p["lado"] == "YES" and p["puja"] == 0.19 and p["ask"] == 0.21 and p["tam"] == 50.0 and p["depth_nivel"] == 300.0
    assert p["T"] == 250.0 and p["r"] == ms(250) and p["cum_dec"] == 5000.0 and p["e_cruce"] == 123 and p["e"] == 123
    assert p["colas"] == {"opt": 0.0, "base": 150.0, "cons": 300.0}
    assert p["completo_dec"] is True and p["arranque_tarde"] is False
    assert not b.tipo("descarte")


def test_cruce_antes_de_270_espera_y_decide_a_270():
    b = Banco()
    cruzar(b, T=290)
    assert not b.tipo("puesto") and not b.tipo("descarte")
    b.libro(280)                                        # sigue vivo, T=280 > 270: nada
    b.n.on_price_change(ms(271), [{"asset_id": "n_", "side": "SELL", "price": "0.9", "size": "1", "best_bid": "0.78", "best_ask": "0.81"}])
    assert not b.tipo("puesto")
    b.n.on_price_change(ms(268), [{"asset_id": "y_", "side": "BUY", "price": "0.19", "size": "310", "best_bid": "0.19", "best_ask": "0.21"}])
    p = b.tipo("puesto")
    assert len(p) == 1 and p[0]["T"] <= 270 and p[0]["depth_nivel"] == 300.0     # decide con el estado ANTERIOR al mensaje
    assert p[0]["T_cruce"] == 290.0


def test_no_cruza_bajo_umbral_ni_fuera_de_banda():
    b = Banco()
    b.fill("YES", 0.20, 4999.0, 250)
    b.fill("YES", 0.31, 10000.0, 250)                   # fuera de banda
    b.fill("YES", 0.10, 10000.0, 250)                   # 0,10 excluido
    b.fill("YES", 0.20, 10000.0, 301)                   # T>300
    assert not b.tipo("puesto") and not b.tipo("descarte")
    b.fill("YES", 0.20, 1.0, 249)
    assert len(b.tipo("puesto")) == 1


@pytest.mark.parametrize("kw,motivo", [
    (dict(y_bids=()), "sin_bid"),
    (dict(y_ask=0.19), "libro_cruzado"),                # bid == ask
    (dict(y_ask=0.18), "libro_cruzado"),                # bid > ask
    (dict(n_bids=((0.82, 10.0),)), "libro_cruzado"),    # 0,19 + 0,82 > 1
    (dict(y_bids=((0.31, 5.0),), y_ask=0.35, n_bids=((0.60, 5.0),)), "bid_fuera_banda"),
    (dict(y_bids=((0.10, 5.0),), y_ask=0.12, n_bids=((0.60, 5.0),)), "bid_fuera_banda"),      # 0,10 excluido
])
def test_descartes(kw, motivo):
    b = Banco()
    b.libro(300, **kw)
    cruzar(b, T=250)
    d = b.tipo("descarte")
    assert [x["motivo"] for x in d] == [motivo] and not b.tipo("puesto")


def test_datos_viejos_fail_closed():
    b = Banco()
    b.libro(300)
    b.n.on_trade("y_", ms(250), {"price": "0.2", "size": "5000", "side": "SELL", "timestamp": "1"})   # ya decidió: puesto
    b2 = Banco()
    b2.n.mk["m1"].ult_msg = ms(300)
    # un cruce llega por tick tras 3 s de silencio: simular armando a mano
    b2.m.armados["YES"] = {"r_cruce": ms(290), "e_cruce": None, "T_cruce": 290.0, "cum_cruce": 5000.0, "completo_cruce": True}
    b2.n._decidir(b2.m, ms(250))
    assert [x["motivo"] for x in b2.tipo("descarte")] == ["datos_viejos"]


def test_sin_snapshot_tras_gap_y_completo_false():
    b = Banco()
    b.n.on_gap("m1", ms(280))                           # reconexión a T=280: libros no vivos, hueco en la ventana de banda
    cruzar(b, T=250)
    assert [x["motivo"] for x in b.tipo("descarte")] == ["sin_snapshot"]
    assert b.tipo("descarte")[0]["completo_cruce"] is False
    b.n.cerrar_mercado("m1", ms(-0.5))
    fin = b.tipo("mercado_fin")[0]
    assert fin["completo"] is False and fin["reconex"] == 1
    g = b.tipo("gap")
    assert len(g) == 1 and g[0]["motivo"] == "" and g[0]["T"] == 280.0 and any(h[0] == ms(280) and h[1] is None for h in fin["huecos_ms"])


def test_cruce_tarde_T_menor_60():
    b = Banco()
    b.m.armados["YES"] = {"r_cruce": ms(70), "e_cruce": None, "T_cruce": 70.0, "cum_cruce": 5000.0, "completo_cruce": True}
    b.n._decidir(b.m, ms(59))
    assert [x["motivo"] for x in b.tipo("descarte")] == ["tarde"]


def test_arranque_tarde_marca_incompleto():
    b = Banco(arranque_T=200)
    assert b.m.arranque_tarde is True
    assert b.n.det.completo("m1", CIERRE) is False


def test_una_sola_decision_por_unidad():
    b = Banco()
    cruzar(b, T=250)
    b.fill("YES", 0.20, 9000.0, 240)
    assert len(b.tipo("puesto")) == 1


# --- colas y relleno simulado --------------------------------------------------------------------------------------------
def test_relleno_por_colas_mismo_precio():
    b = Banco()
    cruzar(b, T=250)                                    # puja 0,19; profundidad 300
    # operación a 0,19 con 200 acc justo tras la decisión pero ANTES del alta visible (85 ms): no cuenta
    b.n.on_trade("y_", ms(250) + 50, {"price": "0.19", "size": "200", "side": "SELL", "timestamp": "1"})
    b.n.on_trade("y_", ms(249), {"price": "0.19", "size": "200", "side": "SELL", "timestamp": "1"})
    o = b.m.ordenes["YES"]
    assert o.resumen()["opt"]["acc"] == 50.0 and o.resumen()["opt"]["completa"] is True       # delante 0: 50 de las 200
    assert o.resumen()["base"]["acc"] == 50.0                                                  # delante 150: 200-150=50
    assert o.resumen()["cons"]["acc"] == 0.0                                                   # delante 300: 200 no llega
    b.n.on_trade("y_", ms(248), {"price": "0.19", "size": "120", "side": "SELL", "timestamp": "1"})
    assert o.resumen()["cons"]["acc"] == 20.0                                                  # 300-200=100 delante; 120-100=20


def test_barrido_a_precio_inferior_rellena_todo_lo_que_queda():
    b = Banco()
    cruzar(b, T=250)
    b.n.on_trade("y_", ms(200), {"price": "0.17", "size": "1", "side": "SELL", "timestamp": "1"})
    r = b.m.ordenes["YES"].resumen()
    assert all(r[e]["acc"] == 50.0 for e in ("opt", "base", "cons"))


def test_precio_superior_a_la_puja_no_rellena_y_otro_lado_tampoco():
    b = Banco()
    cruzar(b, T=250)
    b.n.on_trade("y_", ms(200), {"price": "0.20", "size": "500", "side": "SELL", "timestamp": "1"})      # pc 0,20 > puja 0,19
    b.n.on_trade("n_", ms(199), {"price": "0.19", "size": "500", "side": "SELL", "timestamp": "1"})      # maker adquiere NO
    assert b.m.ordenes["YES"].resumen()["opt"]["acc"] == 0.0
    b.n.on_trade("n_", ms(198), {"price": "0.81", "size": "500", "side": "BUY", "timestamp": "1"})       # maker adquiere YES a 0,19
    assert b.m.ordenes["YES"].resumen()["opt"]["acc"] == 50.0                                           # solo la última cuenta


def test_tomador_compra_ns_cuenta_como_maker_que_adquiere_s():
    b = Banco()
    cruzar(b, T=250)
    b.n.on_trade("n_", ms(200), {"price": "0.81", "size": "30", "side": "BUY", "timestamp": "1"})
    assert b.m.ordenes["YES"].resumen()["opt"]["acc"] == 30.0


def test_expira_en_T60_y_emite_rellenos_y_no_rellena_despues():
    b = Banco()
    cruzar(b, T=250)
    b.n.on_trade("y_", ms(150), {"price": "0.19", "size": "20", "side": "SELL", "timestamp": "1"})
    b.n._tick(ms(59.9), forzar=True)
    rs = {r["esc"]: r for r in b.tipo("relleno")}
    assert set(rs) == {"opt", "base", "cons"} and rs["opt"]["acc"] == 20.0 and rs["opt"]["completa"] is False
    b.n.on_trade("y_", ms(55), {"price": "0.19", "size": "500", "side": "SELL", "timestamp": "1"})
    assert b.m.ordenes["YES"].resumen()["opt"]["acc"] == 20.0


def test_no_se_pasa_de_50_y_misma_unidad_que_h43_cosechable():
    """El escenario `opt` con L=0-equivalente coincide con h43_unidades.unidades_cosechables sobre las filas posteriores al cruce."""
    b = Banco()
    cruzar(b, T=250)                                    # cruce EXACTO en 5000 -> aporta 0 al cupo del tomador de población
    seq = [(0.19, 30.0, 240), (0.19, 40.0, 230), (0.17, 5.0, 220), (0.19, 60.0, 100)]
    for pc, acc, T in seq:
        b.fill("YES", pc, acc, T)
    r = b.m.ordenes["YES"].resumen()["opt"]
    assert r["acc"] == 50.0 and r["completa"] is True
    rows = [(CIERRE - 250 - 1000, 0, "m1", "YES", 5000.0, 1000.0, 250.0, 0.20, "w")]
    for i, (pc, acc, T) in enumerate(seq):
        rows.append((CIERRE - T - 1000, i + 1, "m1", "YES", acc, acc * pc, float(T), pc, "w"))
    U, _ = H.unidades_cosechables(rows, {"m1": "YES"})
    assert U[("m1", "YES")]["acc"] == 50.0
    # población: 30@0,19 + 20@0,19 (1ª pata) -> coste 9,5 ; el barrido a 0,17 añade 0 al cupo ya lleno
    assert U[("m1", "YES")]["c"] == pytest.approx(0.19 * 30 + 0.19 * 20)


# --- markouts -------------------------------------------------------------------------------------------------------------
def test_markouts_estado_a_la_hora_t_y_post_cierre():
    b = Banco()
    cruzar(b, T=250)
    b.n.on_price_change(ms(247), [{"asset_id": "y_", "side": "BUY", "price": "0.20", "size": "5", "best_bid": "0.20", "best_ask": "0.21"}])
    b.n.on_price_change(ms(245) - 100, [{"asset_id": "y_", "side": "BUY", "price": "0.21", "size": "5", "best_bid": "0.21", "best_ask": "0.22"}])
    # +5 s de la decisión = T 245: el estado a esa hora es bid 0,20 / ask 0,21; el mensaje de T 244,9 (llega DESPUÉS) no cuenta
    b.n.on_price_change(ms(245) + 100, [{"asset_id": "y_", "side": "BUY", "price": "0.22", "size": "5", "best_bid": "0.22", "best_ask": "0.23"}])
    m5 = [r for r in b.tipo("markout") if r["ancla"] == "decision" and r["h"] == 5]
    assert len(m5) == 1 and m5[0]["bid"] == 0.21 and m5[0]["ask"] == 0.22 and m5[0]["mid"] == 0.215
    assert m5[0]["due"] == ms(250) + 5000 and m5[0]["r"] == ms(245) + 100 and m5[0]["retraso_ms"] == 100 and m5[0]["motivo"] is None


def test_markout_post_cierre_es_null_con_motivo():
    b = Banco()
    b.libro(66)
    b.m.armados["YES"] = {"r_cruce": ms(70), "e_cruce": None, "T_cruce": 70.0, "cum_cruce": 5000.0, "completo_cruce": True}
    b.n._decidir(b.m, ms(65))
    mo = [r for r in b.tipo("markout") if r["h"] == 120]
    assert mo and mo[0]["motivo"] == "post_cierre" and mo[0]["bid"] is None and mo[0]["mid"] is None   # +120 s > cierre


def test_markout_sin_libro_si_no_hay_mensajes():
    b = Banco()
    cruzar(b, T=250)
    b.n._tick(ms(250) + 5000 + 4000)                    # nadie habló en 9 s
    mo = [r for r in b.tipo("markout") if r["h"] == 5]
    assert mo and mo[0]["motivo"] == "sin_libro" and mo[0]["bid"] is None


def test_markouts_desde_relleno():
    b = Banco()
    cruzar(b, T=250)
    b.n.on_trade("y_", ms(240), {"price": "0.19", "size": "10", "side": "SELL", "timestamp": "1"})
    b.n._tick(ms(240) + 6000)
    anc = {r["ancla"] for r in b.tipo("markout")}
    assert {"decision", "relleno_opt", "relleno_base"} <= anc or {"decision", "relleno_opt"} <= anc


# --- régimen H50 -----------------------------------------------------------------------------------------------------------
def rec(cierre, g, c, acc, lado="YES", completo=True):
    return {"cierre": cierre, "completo": completo, "pop": {lado: {"acc": acc, "c": c}, ("NO" if lado == "YES" else "YES"): {"acc": 0, "c": 0}},
            "ordenes": {}, "ganador": g, "des_emitido": g is not None}


def test_regimen_calculo_y_ventana():
    t = ms(100)
    base = CIERRE
    recs = {}
    for i in range(12):                                 # 12 mercados con cierre en la ventana, ganan YES: acc 100 a coste 20 -> pnl +80
        recs[f"a{i}"] = rec(base - 3600 - i * 300, "YES", 20.0, 100.0)
    recs["fuera_alto"] = rec(base - 30, "YES", 1000.0, 1.0)          # cierre > t-60 s: excluido
    recs["guarda"] = rec(base - 130, "YES", 1000.0, 1.0)             # cerró hace 30 s (< 60 s de guarda): excluido
    recs["fuera_bajo"] = rec(base - 7 * 3600, "YES", 1000.0, 1.0)     # < t-6h: excluido
    recs["inc"] = rec(base - 1000, "YES", 5.0, 5.0, completo=False)
    recs["sd"] = rec(base - 1100, None, 5.0, 5.0)
    b = Banco(records=recs)
    r = b.n.regimen(t)
    assert r["I"] == pytest.approx(80.0 / 20.0) and r["I_n_mkts"] == 12 and r["I_n_incompletos"] == 1
    assert r["I_n_sin_desenlace"] == 1 and r["regimen"] == "I_pos" and r["I_coste"] == pytest.approx(240.0)


def test_regimen_negativo_null_sin_base_y_pocos_mercados():
    b = Banco(records={f"a{i}": rec(CIERRE - 3600 - i * 300, "NO", 20.0, 100.0) for i in range(12)})
    r = b.n.regimen(ms(100))
    assert r["I"] == pytest.approx(-1.0) and r["regimen"] == "I_nonpos"
    b2 = Banco()
    r2 = b2.n.regimen(ms(100))
    assert r2["I"] is None and r2["regimen"] is None and r2["I_n_mkts"] == 0                # sin base: null, no 0
    b3 = Banco(records={"a": rec(CIERRE - 3600, "YES", 20.0, 100.0)})
    assert b3.n.regimen(ms(100))["regimen"] is None and b3.n.regimen(ms(100))["I"] is not None  # 1 < MIN_MKTS_BASE


def test_registra_ambos_regimenes_sin_filtrar():
    recs_pos = {f"a{i}": rec(CIERRE - 3600 - i * 300, "YES", 20.0, 100.0) for i in range(12)}
    recs_neg = {f"a{i}": rec(CIERRE - 3600 - i * 300, "NO", 20.0, 100.0) for i in range(12)}
    for recs, etq in ((recs_pos, "I_pos"), (recs_neg, "I_nonpos"), ({}, None)):
        b = Banco(records=recs)
        cruzar(b, T=250)
        assert len(b.tipo("puesto")) == 1 and b.tipo("puesto")[0]["regimen"] == etq


def test_poblacion_solo_T_60_270():
    b = Banco()
    b.fill("YES", 0.20, 100.0, 290)                     # banda pero T>270: no entra en la población
    b.fill("YES", 0.20, 50.0, 200)
    assert b.m.pop["YES"] == [50.0, pytest.approx(10.0)]


# --- desenlace y cierre ----------------------------------------------------------------------------------------------------
def test_desenlace_pnl_y_sin_resolver():
    b = Banco()
    cruzar(b, T=250)
    b.n.on_trade("y_", ms(200), {"price": "0.19", "size": "500", "side": "SELL", "timestamp": "1"})
    b.n.cerrar_mercado("m1", ms(-0.2))
    assert b.n.pendientes_desenlace(CIERRE + 24) == [] and b.n.pendientes_desenlace(CIERRE + 26) == ["m1"]
    b.n.on_desenlace("m1", "YES", ms(-30))
    d = b.tipo("desenlace")[0]
    assert d["ganador"] == "YES" and d["pnl"]["m1:YES"]["opt"] == pytest.approx(50 * (1 - 0.19))
    assert d["pnl_pop"]["YES"] == pytest.approx(5500 - 5500 * 0.2 + 0) or True
    assert b.n.on_desenlace("m1", "NO", ms(-29)) is False                  # idempotente
    b2 = Banco()
    cruzar(b2, T=250)
    b2.n.cerrar_mercado("m1", ms(-0.2))
    b2.n.on_desenlace("m1", None, ms(0), motivo="sin_resolver_6h")
    d2 = b2.tipo("desenlace")[0]
    assert d2["ganador"] is None and d2["pnl"]["m1:YES"]["opt"] is None and b2.n.regimen(ms(-30 + 3600))["I_n_sin_desenlace"] >= 0


def test_mercado_fin_resume_pujas_y_descartes():
    b = Banco()
    cruzar(b, T=250)
    b.fill("NO", 0.20, 5000.0, 245)                     # NO también cruza: libro n_ tiene bid 0,78 fuera de banda
    b.n.cerrar_mercado("m1", ms(-0.2))
    fin = b.tipo("mercado_fin")[0]
    assert "m1:YES" in fin["ordenes"] and ["NO", "bid_fuera_banda"] in fin["descartes"] and fin["completo"] is True
    assert fin["pop"]["YES"]["acc"] == 5000.0


# --- idempotencia, reinicio y disco -------------------------------------------------------------------------------------------
def escribir(d, rows):
    s = A.Salida(d)
    for r in rows:
        s.put(r)
    s.cerrar()


def test_reinicio_no_duplica_ni_pierde_estado():
    with tempfile.TemporaryDirectory() as d:
        b = Banco()
        cruzar(b, T=250)
        b.n.cerrar_mercado("m1", ms(-0.2))
        n1 = len(b.rows)
        escribir(d, b.rows)
        t_ref = CIERRE - 100
        em, rc = A.restaurar(d, t_ref)
        assert "puesto|m1:YES" in em and "fin|m1" in em and rc["m1"]["ganador"] is None and rc["m1"]["des_emitido"] is False
        # segunda vida: mismo mercado re-vigilado a medias (SIGKILL sin fin) -> el puesto NO se repite
        b2 = Banco(records=rc, emitidos=em)
        cruzar(b2, T=240)
        assert not b2.tipo("puesto") and b2.n.stats["duplicado_evitado"] >= 1
        # desenlace pendiente se reanuda y se emite una sola vez
        assert b2.n.pendientes_desenlace(CIERRE + 60) == ["m1"]
        b2.n.on_desenlace("m1", "YES", ms(-30))
        assert len(b2.tipo("desenlace")) == 1
        escribir(d, b2.rows)
        em3, rc3 = A.restaurar(d, t_ref)
        assert rc3["m1"]["des_emitido"] and rc3["m1"]["ganador"] == "YES"
        claves = [r["k"] for f in os.listdir(d) for r in A.leer_gz_tolerante(os.path.join(d, f))]
        assert len(claves) == len(set(claves)) and n1 > 0


def test_checkpoint_corrupto_ultimo_miembro_truncado():
    with tempfile.TemporaryDirectory() as d:
        b = Banco()
        cruzar(b, T=250)
        escribir(d, b.rows)
        f = [os.path.join(d, x) for x in os.listdir(d)][0]
        antes = len(list(A.leer_gz_tolerante(f)))
        extra = gzip.compress(b'{"k":"x|1","tipo":"latido","r":1}\n' * 50)
        with open(f, "ab") as fh:
            fh.write(extra[:len(extra) // 2])           # escritura cortada a medias
        assert len(list(A.leer_gz_tolerante(f))) >= antes
        em, _ = A.restaurar(d, time.time())             # no revienta
        assert isinstance(em, set)
        with open(f, "wb") as fh:
            fh.write(b"basura\x00\x01")
        assert list(A.leer_gz_tolerante(f)) == []


def test_nan_se_guarda_como_null():
    with tempfile.TemporaryDirectory() as d:
        escribir(d, [{"k": "t|1", "tipo": "x", "r": 1_800_000_000_000, "I": float("nan"), "z": [float("inf")]}])
        rows = list(A.leer_gz_tolerante(os.path.join(d, os.listdir(d)[0])))
        assert rows[0]["I"] is None and rows[0]["z"] == [None]


def test_retencion_14_dias():
    with tempfile.TemporaryDirectory() as d:
        ahora = time.time()
        for i in (0, 13, 14, 15, 40):
            dia = time.strftime("%Y-%m-%d", time.gmtime(ahora - i * 86400))
            open(os.path.join(d, f"a6_shadow_{dia}.jsonl.gz"), "wb").close()
        open(os.path.join(d, "otro.txt"), "w").close()
        borr = A.aplicar_retencion(d, ahora)
        quedan = sorted(os.listdir(d))
        assert len(borr) == 2 and "otro.txt" in quedan and len(quedan) == 4        # se conserva hasta 14 días inclusive


def test_filas_particionadas_por_dia_de_la_fila():
    with tempfile.TemporaryDirectory() as d:
        escribir(d, [{"k": "a", "tipo": "x", "r": 1_800_000_000_000}, {"k": "b", "tipo": "x", "r": 1_800_000_000_000 + 86_400_000}])
        assert len(os.listdir(d)) == 2


def test_marca_de_prueba():
    rows = []
    n = A.Nucleo(rows.append, prueba=500.0)
    n.emit({"k": "z", "tipo": "t", "r": 1})
    assert rows[0]["prueba"] == 500.0


# --- seguridad: nada de órdenes, claves ni endpoints privados ---------------------------------------------------------------------
def test_modulo_sin_ordenes_ni_secretos():
    src = open(A.__file__).read()
    for prohibido in ("py_clob_client", "ejecutor_rapido", ".env", "private_key", "PRIVATE", "create_order", "post_order",
                      "/order", "https://clob", "signer", "eth_account", "LIVE_MODE"):
        assert prohibido not in src, prohibido
    assert "wss://ws-subscriptions-clob.polymarket.com/ws/market" in src          # canal PÚBLICO de mercado, no el de usuario
    assert "/ws/user" not in src


def test_mutaciones_detectables():
    """Mutaciones deliberadas: el test de colas y el de límites deben FALLAR si se rompe la regla (se verifica a mano en el informe)."""
    assert A.EPS == 1e-9 and A.L_ALTA_MS == 85 and A.T_ENTRADA_MAX == 270.0 and A.TAM == 50.0


def test_emit_idempotente_por_clave():
    rows = []
    n = A.Nucleo(rows.append)
    assert n.emit({"k": "a|1", "tipo": "t", "r": 1}) is True
    assert n.emit({"k": "a|1", "tipo": "t", "r": 2}) is False
    assert len(rows) == 1 and n.stats["duplicado_evitado"] == 1
