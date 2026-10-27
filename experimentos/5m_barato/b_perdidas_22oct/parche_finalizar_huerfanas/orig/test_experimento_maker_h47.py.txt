#!/usr/bin/env python3
"""Pruebas de experimento_maker_h47 con cliente CLOB, libro y cadena FALSOS (sin red, sin dinero, ledger/KILL/lock en un directorio temporal).
Uso: /root/polymarket-research/.venv/bin/python -m pytest -q test_experimento_maker_h47.py
Cubren (pase de casos límite de CLAUDE.md): reglas H35 en bordes (banda, tick, subcéntimo, k), tamaño/nocional mínimo, escalera A, relleno
CONS (sim_uno), suelo de saldo, saldo ilegible, dinero que no cuadra, N fijo y persistente tras reinicio, máx. vivas, una sola cara, repegado
(cancelar -> leer -> volver a pujar), relleno parcial cierra la puja, hash != orderID -> kill, parada que no envía, kill que cancela, reinicio a
mitad (orden del ledger se cancela por hash), ensayo en seco sin cliente, WS viejo / tick cambiado, tope de órdenes, escalón A sin riesgo de relleno."""
import gc
import json
import os
import sys
import tempfile
import threading
import time
import types
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, "/root/polymarket-research")
import experimento_pares_cola_15m as X          # noqa: E402
import experimento_maker_h47 as H               # noqa: E402
import pares_contabilidad as C                  # noqa: E402

DEF_ASENTAR, DEF_ASENTAR_MIN = H.ASENTAR_H47_S, H.ASENTAR_MIN_REAL_S      # valores del módulo ANTES de acortarlos para los tests
DEF_PRESUPUESTO = H.PRESUPUESTO_UTIL                                       # 5.0 (decisión de Javi 19-Oct); los tests de dinero usan un presupuesto ancho (12) salvo los propios del tope
H.ASENTAR_H47_S = H.ASENTAR_MIN_REAL_S = 0.05                              # los tests usan esperas de ms; test_asentar_* prueba los reales
TMP = Path(tempfile.mkdtemp(prefix="test_h47_"))
C.T_VERIF_S = 0.6
H.PRESUPUESTO_UTIL = 12.0
H.ESPERA_LECTURAS_S = 0.0
H.ESPERA_REINTENTO_S = 0.0                                                  # la verificación del saldo de arranque no duerme en los tests
X.ESPERA_INEXISTENTE_S = 0.0
ONCHAIN = {"pusd": 19.59}
CREADOS = []


class Cli:
    def __init__(self):
        self.ordenes = {}
        self.n = 0
        self.cancel_ok = True
        self.post_oid = None            # fuerza un orderID distinto del hash
        self.posts = []
        self.cancels = []
        self.cancel_all_n = 0

    def get_tick_size(self, tok):
        return "0.01"

    def create_order(self, args):
        self.n += 1
        return {"h": f"0xh{self.n}", "args": args}

    def post_order(self, signed, tipo, post_only=True):
        assert post_only is True
        h = signed["h"]
        a = signed["args"]
        self.posts.append((h, a.price, a.size))
        oid = self.post_oid or h
        self.ordenes[oid] = {"size_matched": 0.0, "status": "LIVE"}
        return {"orderID": oid, "success": True}

    def get_order(self, h):
        o = self.ordenes.get(h)
        return None if o is None else {"size_matched": str(o["size_matched"]), "status": o["status"]}

    def cancel_order(self, payload):
        h = payload.orderID
        self.cancels.append(h)
        if self.cancel_ok and h in self.ordenes:
            if self.ordenes[h]["status"] == "LIVE":
                self.ordenes[h]["status"] = "CANCELED"
            return {"canceled": [h]}
        return {"canceled": [], "not_canceled": {h: "x"}}

    def cancel_all(self):
        self.cancel_all_n += 1
        for o in self.ordenes.values():
            if o["status"] == "LIVE":
                o["status"] = "CANCELED"
        return {"canceled": []}

    def get_open_orders(self, *a, **k):
        return [{"id": h} for h, o in self.ordenes.items() if o["status"] == "LIVE"]

    def get_trades(self, *a, **k):
        return []


X.saldo_onchain = lambda w: ONCHAIN["pusd"]
BLQ = {"n": 1000, "dt": 0.0}                                                # bloque falso: número monótono y hora = ahora − dt


def _bloque_falso(w):
    """H.saldo_con_bloque de los tests: el saldo sale de X.saldo_onchain (así `lecturas(...)` sigue valiendo) y el bloque avanza solo."""
    v = X.saldo_onchain(w)
    if v is None:
        return None
    BLQ["n"] += 1
    return v, BLQ["n"], time.time() - BLQ["dt"]


H.saldo_con_bloque = _bloque_falso
X.acciones_onchain = lambda w, toks: {t: 0.0 for t in toks}
H.Exp47._hash = lambda self, signed, tok: signed["h"]


def lib_falso(bid=0.20, ask=0.22, tok_up="tU", tok_dn="tD"):
    lib = object.__new__(X.Libro)
    lib.lk = threading.Lock()
    lib.L = {tok_up: {"bids": {bid: 50.0, round(bid - 0.01, 2): 80.0}, "asks": {ask: 40.0}},
             tok_dn: {"bids": {round(1 - ask, 2): 40.0}, "asks": {round(1 - bid, 2): 50.0}}}
    lib.ult = lib.ult_msg = time.time()
    lib.tick_cambiado = False
    lib.error = None
    lib.mids = {tok_up: [], tok_dn: []}
    lib.registrar_trades = True
    lib.trades = {tok_up: [], tok_dn: []}
    lib.trades_trecv = {tok_up: [], tok_dn: []}
    lib.parar = False
    lib.hilo = types.SimpleNamespace(is_alive=lambda: True)
    return lib


def poner_libro(lib, tok, bids, asks):
    with lib.lk:
        lib.L[tok] = {"bids": dict(bids), "asks": dict(asks)}
    lib.ult = lib.ult_msg = time.time()


def mk_falso(coin="eth", fin_en=200.0, slug=None):
    ini = int(time.time())
    return {"slug": slug or f"{coin}-updown-5m-{ini}", "id": "1", "fin": time.time() + fin_en, "toks": {"Up": "tU", "Down": "tD"},
            "coin": coin, "ini": ini, "min_size": 5}


def nuevo(nombre, real=True, escalon="B", **kw):
    X.LEDGER = TMP / f"{nombre}.jsonl"
    X.KILL_FICHERO = TMP / f"{nombre}.KILL"
    X.LOCK = TMP / f"{nombre}.lock"
    X._CACHE = None
    X.cliente_dedicado = (lambda: (Cli(), "0xabc")) if real else (lambda: (_ for _ in ()).throw(AssertionError("seco: no hay cliente")))
    X.ASENTAR_S = 0.05
    ONCHAIN["pusd"] = 19.59
    ex = H.Exp47(real, escalon, kw.pop("n_max", None), kw.pop("t_stop", 60.0), kw.pop("size", 5), kw.pop("min_nocional", 1.0),
                 kw.pop("monedas", ("eth", "sol", "xrp")), kw.pop("presupuesto", 12.0), kw.pop("max_vivas", 5))
    CREADOS.append(ex)
    return ex


def ctx_de(ex, coin="eth", bid=0.20, ask=0.22, **kw):
    lib = lib_falso(bid, ask)
    c = H.Ctx(coin, mk_falso(coin, **kw), lib, H.K_POR_MONEDA[coin])
    c.fase = "activa"
    ex.ctxs[c.mk["slug"]] = c
    return c


@pytest.fixture(autouse=True)
def _limpia():
    yield
    for ex in CREADOS:
        ex._cerrado = True
    CREADOS.clear()
    X.saldo_onchain = lambda w: ONCHAIN["pusd"]


def eventos(tipo=None, real=None):
    out = []
    for ln in X.LEDGER.read_text().splitlines():
        try:
            e = json.loads(ln)
        except ValueError:                                                      # líneas corruptas puestas a propósito (tests de suelo ilegible)
            continue
        if (tipo is None or e.get("tipo") == tipo) and (real is None or e.get("real") == real):
            out.append(e)
    return out


def esperar_asentar():
    time.sleep(0.12)


# ---------------------------------------------------------------- reglas puras
def test_banda_y_objetivo_en_bordes():
    assert not H.en_banda(0.11, 0.13) and H.en_banda(0.12, 0.14) and H.en_banda(0.30, 0.32) and not H.en_banda(0.31, 0.33)
    assert not H.en_banda(0.20, 0.20) and not H.en_banda(0.20, 0.19)           # libro cruzado / bloqueado
    assert H.objetivo_h35(0.12, 0.14, 1) == 0.11 and H.objetivo_h35(0.12, 0.14, 2) == 0.10
    assert H.objetivo_h35(0.13, 0.15, 2) == 0.11
    assert H.objetivo_h35(0.30, 0.32, 1) == 0.29 and H.objetivo_h35(0.30, 0.32, 2) == 0.28
    assert H.objetivo_h35(0.11, 0.13, 2) is None                                # 0,09 < 0,10
    assert H.objetivo_h35(0.105, 0.13, 1) == 0.10                               # top fuera de rejilla: céntimo inferior
    assert H.objetivo_h35(0.105, 0.13, 2) is None
    assert H.objetivo_h35(0.20, 0.205, 1) == 0.19


def test_tamano_y_nocional_minimo():
    assert H.tamano_orden(0.15, 5, 1.0) == 7 and H.tamano_orden(0.10, 5, 1.0) == 10 and H.tamano_orden(0.30, 5, 1.0) == 5
    assert H.tamano_orden(0.15, 5, 0.0) == 5
    assert H.tamano_orden(0.05, 5, 1.0) is None                                  # ceil(20) > 10: no se envía
    assert H.tamano_orden(0.2, 11, 1.0) is None and H.tamano_orden(0.2, 4, 1.0) is None
    assert H.tamano_orden(0.17, 5, 1.0) == 6                                     # 6 * 0,17 = 1,02


def test_escalera_a():
    assert [H.precio_a(i) for i in range(4)] == [0.02, 0.01, 0.03, 0.02]


def test_sim_uno_cons():
    lib = lib_falso()
    t0 = time.time()
    o = {"tok": "tU", "precio": 0.20, "size": 5.0, "t_post": t0, "cola": 30.0}

    def trade(tk, tx, p, sz, sd):
        lib.trades[tk].append((tx, tx, p, sz, sd))
        lib.trades_trecv[tk].append(tx)
    trade("tU", t0 + 0.01, 0.19, 99, "SELL")                    # antes del alta (+70 ms): no cuenta
    assert H.sim_uno(lib, {"tU": "tD", "tD": "tU"}, o, 0.0) == 0.0
    trade("tU", t0 + 0.2, 0.20, 20, "SELL")                     # a nuestro nivel, no supera la cola 30
    assert H.sim_uno(lib, {"tU": "tD", "tD": "tU"}, o, 0.0) == 0.0
    trade("tU", t0 + 0.3, 0.20, 12, "SELL")                     # 32 > 30: parcial 2
    f = H.sim_uno(lib, {"tU": "tD", "tD": "tU"}, o, 0.0)
    assert abs(f - 2.0) < 1e-9
    trade("tD", t0 + 0.4, 0.82, 1, "BUY")                       # equivalente 0,18 < 0,20: atraviesa -> entera
    assert H.sim_uno(lib, {"tU": "tD", "tD": "tU"}, o, f) == 5.0
    o3 = {"tok": "tU", "precio": 0.20, "size": 5.0, "t_post": t0 + 0.6, "cola": 0.0, "t_cancel": t0 + 0.7}
    lib2 = lib_falso()
    lib2.trades["tU"].append((t0 + 1.0, t0 + 1.0, 0.19, 5, "SELL"))
    lib2.trades_trecv["tU"].append(t0 + 1.0)
    assert H.sim_uno(lib2, {"tU": "tD", "tD": "tU"}, o3, 0.0) == 0.0


# ---------------------------------------------------------------- dinero
def test_suelo_de_saldo_y_saldo_ilegible():
    ex = nuevo("suelo")
    assert abs(ex.saldo_min - 7.59) < 1e-9                                      # 19,59 verificado − 12 útiles
    assert ex.puede_enviar(1.5)                                                 # 19,59 - 1,5 >= 7,59
    ex.vivas["x"] = {"tok": "tU", "precio": 0.2, "size": 5.0}
    ex.vivas["y"] = {"tok": "tU", "precio": 0.2, "size": 5.0}
    assert ex.puede_enviar(1.0) and abs(ex.comprometido() - 2.0) < 1e-9
    ex.vivas.update({f"z{i}": {"tok": "tU", "precio": 0.3, "size": 10.0} for i in range(3)})
    assert ex.puede_enviar(1.0)                                                 # comprometido 11 + 1 -> 7,59 justo en el suelo
    assert not ex.puede_enviar(1.01)                                            # 7,58 < 7,59
    assert eventos("bloqueo_suelo_saldo")[-1]["minimo"] == ex.saldo_min
    ex.vivas.clear()
    X.saldo_onchain = lambda w: None
    ex._on_cache = (0.0, None)
    assert not ex.puede_enviar(1.0)                                             # fail-closed
    assert not ex.puede_enviar(3.5)                                             # tope por orden


def test_dinero_que_no_cuadra_mata():
    ex = nuevo("cuadre")
    ONCHAIN["pusd"] = 15.0                                                      # salieron 4,59 sin ninguna orden
    ex._on_cache = (0.0, None)
    assert not ex.puede_enviar(1.0)
    assert ex.kill and "no cuadra" in ex.kill and X.KILL_FICHERO.exists()


def test_parada_por_saldo_bajo_y_por_ilegible():
    ex = nuevo("parada")
    ONCHAIN["pusd"] = 7.0                                                       # < suelo 7,59
    ex._on_cache = (0.0, None)
    t = time.time()
    ex.vigilar_saldo(t)
    assert ex.parada is None and ex.saldo_bajo_desde is not None
    ex._on_cache = (0.0, None)
    ex.vigilar_saldo(t + H.ESPERA_SALDO_BAJO_S + 1)
    assert ex.parada and "7.00" in ex.parada
    ex2 = nuevo("parada2")
    X.saldo_onchain = lambda w: None
    ex2._on_cache = (0.0, None)
    ex2.vigilar_saldo(t)
    assert ex2.parada is None
    ex2._on_cache = (0.0, None)
    ex2.vigilar_saldo(t + H.SALDO_ILEGIBLE_MAX_S + 1)
    assert ex2.parada and "ilegible" in ex2.parada


def test_parametros_peligrosos_se_rechazan():
    with pytest.raises(SystemExit):
        nuevo("p1", presupuesto=12.5)                                           # en real nunca más de 12 útiles
    with pytest.raises(SystemExit):
        nuevo("p1b", presupuesto=0.0)
    with pytest.raises(SystemExit):
        nuevo("p1c", presupuesto=-1.0)
    nuevo("p1d", presupuesto=6.0)                                               # menos presupuesto sí se admite
    with pytest.raises(SystemExit):
        nuevo("p2", n_max=501)
    with pytest.raises(SystemExit):
        nuevo("p3", escalon="A", n_max=41)
    with pytest.raises(SystemExit):
        nuevo("p4", max_vivas=6)
    with pytest.raises(SystemExit):
        nuevo("p5", size=11)


# ---------------------------------------------------------------- flujo de una puja
def test_flujo_colocar_repegar_relleno_parcial_cierra():
    ex = nuevo("flujo", n_max=3)
    c = ctx_de(ex, "eth", 0.20, 0.22)                                           # k=2 -> 0,18; 0,18*5 = 0,9 < 1 -> 6 acc
    ahora = time.time()
    ex.decidir(c, 200.0, ahora)
    assert len(ex.cli.posts) == 1 and ex.cli.posts[0][1:] == (0.18, 6.0)
    h1 = ex.cli.posts[0][0]
    ip = eventos("intencion_post", True)
    assert len(ip) == 1 and ip[0]["lado"] == "YES" and ip[0]["precio"] == 0.18 and ip[0]["size"] == 6.0
    assert c.tok == "tU" and ex.n_usadas() == 1
    pp = eventos("puja_post")[0]
    assert pp["objetivo_h35"] == 0.18 and pp["cola"] == 0.0 and pp["libro"]["bids"][0][0] == 0.20 and pp["variante"] == "H35"
    assert eventos("post_lat") and h1 in ex.gem
    # el top sube: objetivo 0,19 -> cancela y lee
    poner_libro(c.lib, "tU", {0.21: 50.0, 0.20: 10.0}, {0.23: 40.0})
    time.sleep(H.MIN_ENTRE_ACCIONES_S + 0.02)
    ex.decidir(c, 199.0, time.time())
    assert ex.cli.ordenes[h1]["status"] == "CANCELED" and h1 in ex.canceladas and ex.vivas.get(h1) is None
    assert eventos("repega") and eventos("cancel_lat")
    # no repone hasta asentar
    ex.decidir(c, 198.9, time.time())
    assert len(ex.cli.posts) == 1
    esperar_asentar()
    ex.liquidar_todo(c.estado, c.lib, 198.0)
    assert not ex.canceladas
    ex.decidir(c, 198.0, time.time())
    assert len(ex.cli.posts) == 2 and ex.cli.posts[1][1] == 0.19
    h2 = ex.cli.posts[1][0]
    # relleno parcial de h2: la puja se cierra y se cancela el resto, sin nuevas órdenes
    ex.cli.ordenes[h2]["size_matched"] = 2.0
    ex.liquidar_todo(c.estado, c.lib, 190.0)
    assert c.estado["tU"]["llenas"] == 2.0
    ex.decidir(c, 190.0, time.time())
    assert c.estado["tU"]["cerrado"] and ex.cli.ordenes[h2]["status"] == "CANCELED"
    esperar_asentar()
    ex.liquidar_todo(c.estado, c.lib, 189.0)
    ex.decidir(c, 189.0, time.time())
    assert len(ex.cli.posts) == 2 and ex.kill is None
    o = ex.ordenes()[h2]
    assert abs(o.lo - 2.0) < 1e-9 and abs(o.hi - 6.0) < 1e-9                    # hasta verificar cuenta su tamaño
    time.sleep(C.T_VERIF_S + 0.6)
    assert ex.verificar() == 0
    assert abs(ex.ordenes()[h2].hi - 2.0) < 1e-9


def test_banda_perdida_cancela_y_no_repone():
    ex = nuevo("banda")
    c = ctx_de(ex, "sol", 0.20, 0.22)
    ex.decidir(c, 200.0, time.time())
    assert len(ex.cli.posts) == 1
    poner_libro(c.lib, "tU", {0.36: 50.0}, {0.38: 40.0})
    time.sleep(H.MIN_ENTRE_ACCIONES_S + 0.02)
    ex.decidir(c, 190.0, time.time())
    assert eventos("cancela_banda") and not ex.vivas
    esperar_asentar()
    ex.liquidar_todo(c.estado, c.lib, 189.0)
    ex.decidir(c, 189.0, time.time())
    assert len(ex.cli.posts) == 1
    poner_libro(c.lib, "tU", {0.25: 50.0}, {0.27: 40.0})                         # vuelve a la banda: sol k=1 -> 0,24
    time.sleep(H.MIN_ENTRE_ACCIONES_S + 0.02)
    ex.decidir(c, 180.0, time.time())
    assert len(ex.cli.posts) == 2 and ex.cli.posts[1][1] == 0.24


def test_una_sola_cara_y_n_fijo_y_max_vivas():
    ex = nuevo("n", n_max=2, max_vivas=1)
    c1 = ctx_de(ex, "eth")
    c2 = ctx_de(ex, "sol")
    c3 = ctx_de(ex, "xrp")
    ex.decidir(c1, 200.0, time.time())
    assert len(ex.cli.posts) == 1
    ex.decidir(c2, 200.0, time.time())                                          # máx. 1 viva: bloquea la 2ª puja
    assert len(ex.cli.posts) == 1
    ex.cli.ordenes[ex.cli.posts[0][0]]["size_matched"] = 6.0
    ex.liquidar_todo(c1.estado, c1.lib, 190.0)
    c1.estado["tU"]["cerrado"] = True                                           # puja 1 cerrada -> libera la viva
    ex.decidir(c2, 199.0, time.time())
    assert len(ex.cli.posts) == 2 and ex.n_usadas() == 2
    ex.cli.ordenes[ex.cli.posts[1][0]]["size_matched"] = 5.0
    ex.liquidar_todo(c2.estado, c2.lib, 190.0)
    c2.estado["tU"]["cerrado"] = True
    ex.decidir(c3, 199.0, time.time())                                          # N=2 alcanzado: la 3ª no se envía
    assert len(ex.cli.posts) == 2
    # una sola cara: con las dos caras en banda solo se elige una (la primera) y el token contrario nunca se puja
    assert all(p[0] for p in ex.cli.posts) and {e["lado"] for e in eventos("intencion_post", True)} == {"YES"}


def test_n_persistente_tras_reinicio_y_orden_viva_se_cancela():
    ex = nuevo("reinicio", n_max=1)
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())
    h = ex.cli.posts[0][0]
    assert ex.n_usadas() == 1
    ex._cerrado = True                                                          # el proceso muere con la orden viva
    cli_viejo = ex.cli
    del ex
    X._CACHE = None
    X.LOCK = TMP / "reinicio2.lock"
    X.cliente_dedicado = lambda: (cli_viejo, "0xabc")
    ex2 = H.Exp47(True, "B", 1, 60.0, 5, 1.0, ("eth", "sol", "xrp"), 12.0, 5)
    CREADOS.append(ex2)
    assert ex2.n_usadas() == 1                                                  # N persistente: no se reinicia
    assert cli_viejo.ordenes[h]["status"] == "CANCELED"                         # lo propio que pudo quedar vivo se cancela al arrancar
    c2 = ctx_de(ex2, "sol")
    ex2.decidir(c2, 200.0, time.time())
    assert len(cli_viejo.posts) == 1                                            # N=1 agotado


def test_hash_distinto_mata_y_no_envia_mas():
    ex = nuevo("hash")
    ex.cli.post_oid = "0xOTRO"
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())
    assert ex.kill and "hash calculado" in ex.kill and X.KILL_FICHERO.exists()
    assert ex.cli.cancel_all_n >= 1 and ex.hash_ok is False                     # identidad no fiable: se cancela todo y no se envía más
    n = len(ex.cli.posts)
    ex.decidir(c, 199.0, time.time())
    assert len(ex.cli.posts) == n


def test_parada_no_envia_y_kill_cierra_cancelando():
    ex = nuevo("kill")
    c = ctx_de(ex, "eth")
    ex.parada = "prueba"
    ex.decidir(c, 200.0, time.time())
    assert not ex.cli.posts
    ex.parada = None
    ex.decidir(c, 200.0, time.time())
    assert len(ex.cli.posts) == 1
    ex.kill = "fallo de maquinaria"
    ex.paso(c)
    assert c.fase == "asentando"
    ex.paso(c)
    assert not ex.vivas and ex.cli.ordenes[ex.cli.posts[0][0]]["status"] == "CANCELED"
    esperar_asentar()
    ex.paso(c)
    assert c.fase == "espera_fin"
    c.mk["fin"] = time.time() - H.FIN_ESPERA_S - 1
    ex.paso(c)
    assert c.fase == "fin" and eventos("puja_fin")
    assert eventos("puja_fin")[0]["relleno_real"] is False


def test_cancelacion_no_confirmada_mata():
    ex = nuevo("cnc")
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())
    ex.cli.cancel_ok = False
    ex.cli.ordenes[ex.cli.posts[0][0]]["status"] = "LIVE"
    poner_libro(c.lib, "tU", {0.30: 50.0}, {0.32: 40.0})
    time.sleep(H.MIN_ENTRE_ACCIONES_S + 0.02)
    ex.decidir(c, 190.0, time.time())
    assert ex.kill and "cancelación no confirmada" in ex.kill


def test_ws_viejo_y_tick_cambiado_cierran():
    ex = nuevo("ws")
    c = ctx_de(ex, "eth")
    c.lib.tick_cambiado = True
    ex.paso(c)
    assert c.fase == "asentando" and c.motivo_cierre == "tick_cambiado"
    c2 = ctx_de(ex, "sol")
    c2.lib.ult_msg = time.time() - 60
    ex.paso(c2)
    assert c2.fase == "activa"                                                  # primero espera
    c2.viejo_desde = time.time() - 10
    ex.paso(c2)
    assert c2.fase == "asentando" and c2.motivo_cierre == "ws_viejo"
    c3 = ctx_de(ex, "xrp", fin_en=50.0)                                         # T <= t_stop
    ex.paso(c3)
    assert c3.motivo_cierre == "t_stop" and not ex.cli.posts


def test_tope_de_ordenes_por_puja():
    ex = nuevo("tope")
    c = ctx_de(ex, "eth")
    c.n_ord = H.MAX_ORDENES_PUJA
    ex.decidir(c, 200.0, time.time())
    assert not ex.cli.posts and c.estado["tU"]["cerrado"] and c.fin_puja == "tope_ordenes"


def test_escalon_a_precio_bajo_y_nunca_si_puede_rellenarse():
    ex = nuevo("a", escalon="A")
    c = ctx_de(ex, "eth", 0.04, 0.06)                                           # fuera de banda H35
    ex.decidir(c, 200.0, time.time())
    assert not ex.cli.posts
    poner_libro(c.lib, "tU", {0.20: 50.0}, {0.22: 40.0})
    ex.decidir(c, 200.0, time.time())
    assert ex.cli.posts[0][1:] == (0.02, 5.0)                                   # 0,02 * 5 = 0,10 $: sin subir el tamaño
    poner_libro(c.lib, "tU", {0.21: 50.0}, {0.23: 40.0})                         # la regla B repegaría -> A cancela y baja a 0,01
    time.sleep(H.MIN_ENTRE_ACCIONES_S + 0.02)
    ex.decidir(c, 199.0, time.time())
    esperar_asentar()
    ex.liquidar_todo(c.estado, c.lib, 198.0)
    ex.decidir(c, 198.0, time.time())
    assert [p[1] for p in ex.cli.posts] == [0.02, 0.01]
    assert max(p[1] for p in ex.cli.posts) <= 0.03


def test_mercado_con_min_size_mayor_bloquea():
    ex = nuevo("minsize")
    c = ctx_de(ex, "eth")
    c.mk["min_size"] = 8
    ex.decidir(c, 200.0, time.time())
    assert not ex.cli.posts or ex.cli.posts[0][2] >= 8


# ---------------------------------------------------------------- ensayo en seco
def test_ensayo_en_seco_no_toca_cliente_ni_dinero():
    ex = nuevo("seco", real=False)
    assert ex.cli is None and ex.funder is None
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())
    ev = eventos("intencion_post")
    assert len(ev) == 1 and ev[0]["real"] is False and ev[0]["oid"].startswith("seco-")
    h = ev[0]["oid"]
    # un print por debajo de nuestro precio (0,18) en el token contrario: acuñación, atraviesa -> relleno entero simulado
    t = time.time() + 0.3
    c.lib.trades["tD"].append((t, t, 0.85, 3, "BUY"))
    c.lib.trades_trecv["tD"].append(t)
    time.sleep(0.4)
    ex.simular(c)
    assert ex.sim_lleno.get(h, 0) > 0
    ex.liquidar_todo(c.estado, c.lib, 190.0)
    assert c.estado["tU"]["llenas"] > 0 and not ex.real
    assert ex.peor_total() == 0.0


def test_rutas_seco_y_real_separadas_y_rearmar_exige_confirmacion():
    H.configurar_rutas(False, "B")
    assert "seco" in str(X.LEDGER) and "seco" in str(X.LOCK) and "seco" in str(X.KILL_FICHERO)
    H.configurar_rutas(True, "A")
    assert str(X.LEDGER).endswith("experimento_h47_A_ledger.jsonl") and str(X.LOCK).endswith("experimento_h47.lock")
    H.configurar_rutas(True, "B", 90.0)
    assert str(X.LEDGER).endswith("experimento_h47_B_t90_ledger.jsonl")         # H35b: ledger aparte, mismo lock y .KILL
    H.configurar_rutas(True, "B")
    assert str(X.KILL_FICHERO).endswith("experimento_h47.KILL")              # compartido con A: un kill bloquea ambos
    with pytest.raises(SystemExit):
        H.main(["--rearmar-kill", "x"])
    with pytest.raises(SystemExit):
        H.main(["--monedas", "btc"])
    nuevo("rutas_fin")


def test_finalizar_markout_missing_tras_cierre():
    ex = nuevo("markout", real=False)
    c = ctx_de(ex, "eth", fin_en=100.0)
    c.tok = "tU"
    c.hashes = ["seco-1"]
    t0 = time.time()
    c.lib.mids["tU"] = [(t0 - 1, 0.20), (t0 + 6, 0.22)]
    c.estado["tU"]["rellenos"] = [{"oid": "seco-1", "acc": 5.0, "precio": 0.18, "t_deteccion": t0 + 1, "mid0": 0.2}]
    c.mk["fin"] = t0 + 40                                                       # +30 s cabe, +120 s pasa del cierre
    ex.finalizar(c)
    r = eventos("puja_fin")[0]["rellenos"][0]
    assert r["mid_5s"] == 0.22 and abs(r["markout_5s"] - (0.22 - 0.18) / 0.18) < 1e-9
    assert r["mid_30s"] is not None and r["mid_120s"] is None and r["markout_120s"] is None


# ---------------------------------------------------------------- API a medias, rechazos, datos viejos, contabilidad incremental
def test_post_resultado_desconocido_mata_y_cancela_por_hash():
    ex = nuevo("desconocido")
    c = ctx_de(ex, "eth")

    def roto(signed, tipo, post_only=True):
        raise RuntimeError("timeout de red")
    ex.cli.post_order = roto
    ex.decidir(c, 200.0, time.time())
    assert ex.kill and "resultado desconocido" in ex.kill and X.KILL_FICHERO.exists()
    assert eventos("intencion_post", True) and ex.cli.cancels                  # se cancela por hash la orden que pudo crearse
    o = ex.ordenes()[eventos("intencion_post", True)[0]["oid"]]
    assert o.hi == o.tamano                                                     # cuenta hasta su tamaño hasta verificarse


def test_rechazo_4xx_limpio_no_mata_y_5_seguidos_paran():
    import httpx
    from py_clob_client_v2.exceptions import PolyApiException
    ex = nuevo("rechazo", escalon="A")
    c = ctx_de(ex, "eth")

    def rechaza(signed, tipo, post_only=True):
        raise PolyApiException(httpx.Response(400, json={"error": "order below minimum notional"}))
    ex.cli.post_order = rechaza
    ex.decidir(c, 200.0, time.time())
    n1 = len(eventos("intencion_post", True))
    ex.decidir(c, 200.0, time.time())
    assert len(eventos("intencion_post", True)) == n1 == 1                      # enfriamiento tras el rechazo: no martillea
    for i in range(4):
        ex.enfriar_tok.clear()
        c.t_accion = 0.0
        ex.decidir(c, 200.0, time.time())
    assert ex.kill is None and ex.parada and "5 rechazos" in ex.parada
    o = list(ex.ordenes().values())[0]
    assert o.hi == 0.0 and o.rechazada                                          # la orden no se creó: sin exposición
    assert ex.n_usadas() == 1                                                   # un mercado: N cuenta el mercado una vez


def test_libro_no_fresco_tras_firmar_no_envia():
    ex = nuevo("viejo")
    c = ctx_de(ex, "eth")
    orig = ex.cli.create_order

    def firma_y_envejece(args):
        r = orig(args)
        c.lib.ult_msg = time.time() - 60
        return r
    ex.cli.create_order = firma_y_envejece
    ex.decidir(c, 200.0, time.time())
    assert not ex.cli.posts and not eventos("intencion_post", True) and eventos("post_abortado_tras_firma")
    assert ex.n_usadas() == 0 and ex.kill is None                               # nada enviado: no consume N


def test_ordenes_incremental_igual_que_plegar_completo():
    ex = nuevo("incr")
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())
    h = ex.cli.posts[0][0]
    ex.ordenes()
    ex.cli.ordenes[h]["size_matched"] = 3.0
    ex.liquidar_todo(c.estado, c.lib, 190.0)
    poner_libro(c.lib, "tU", {0.30: 50.0}, {0.32: 40.0})
    ex.cancelar(h)
    time.sleep(0.2)
    ex.liquidar_todo(c.estado, c.lib, 189.0)
    inc, full = ex.ordenes(), C.plegar(X.leer_ledger())
    assert set(inc) == set(full)
    for k in full:
        a, b = inc[k], full[k]
        assert (a.lo, a.hi, a.abierta, a.alias, a.rechazada, a.t_fuera) == (b.lo, b.hi, b.abierta, b.alias, b.rechazada, b.t_fuera)
    assert C.peor_total(inc) == C.peor_total(full) and C.exposicion_maxima(inc) == C.exposicion_maxima(full)


def test_cada_orden_real_lleva_tamano_precio_y_lado_en_su_intencion():
    ex = nuevo("intencion")
    c = ctx_de(ex, "xrp", 0.15, 0.17)                                           # xrp k=1 -> 0,14; 5 * 0,14 = 0,70 -> 8 acc
    ex.decidir(c, 200.0, time.time())
    ip = eventos("intencion_post", True)[0]
    assert (ip["precio"], ip["size"], ip["lado"], ip["slug"]) == (0.14, 8.0, "YES", c.mk["slug"]) and ip["tok"] == "tU"


# ================================================================ 2ª tanda: aplicación de los 10 hallazgos de la 1ª /code-review (19-Oct)
def _cancelar_y_asentar(ex, c, T=199.0):
    """El top sube -> repega: cancela la viva, espera ASENTAR y la liquida (queda fuera de vivas y canceladas)."""
    poner_libro(c.lib, "tU", {0.21: 50.0, 0.20: 10.0}, {0.23: 40.0})
    time.sleep(H.MIN_ENTRE_ACCIONES_S + 0.02)
    ex.decidir(c, T, time.time())
    esperar_asentar()
    ex.liquidar_todo(c.estado, c.lib, T - 1)


# ---- #1 ASENTAR_S igual al del harness, nunca por debajo en real
def test_asentar_defecto_igual_al_harness_y_real_no_baja(monkeypatch):
    assert DEF_ASENTAR == 1.5 and DEF_ASENTAR_MIN == 1.5 and DEF_ASENTAR >= 1.5
    monkeypatch.setattr(X, "ASENTAR_S", 0.05)
    monkeypatch.setattr(H, "ASENTAR_MIN_REAL_S", DEF_ASENTAR_MIN)
    monkeypatch.setattr(H, "ASENTAR_H47_S", 0.35)                       # el valor del código anterior
    with pytest.raises(SystemExit):
        nuevo("asentar_bajo")                                           # real: se niega
    nuevo("asentar_seco_ok", real=False)                                # seco: sin dinero, se permite
    monkeypatch.setattr(H, "ASENTAR_H47_S", DEF_ASENTAR)
    nuevo("asentar_ok")
    assert X.ASENTAR_S == 1.5                                           # el harness lee la constante del módulo X


def test_relleno_dentro_de_la_ventana_de_asentar_se_registra_y_no_se_repuja(monkeypatch):
    monkeypatch.setattr(H, "ASENTAR_H47_S", 0.4)
    monkeypatch.setattr(H, "ASENTAR_MIN_REAL_S", 0.4)
    monkeypatch.setattr(X, "ASENTAR_S", 0.4)
    ex = nuevo("asentar_ventana")
    assert X.ASENTAR_S == 0.4
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())
    h = ex.cli.posts[0][0]
    poner_libro(c.lib, "tU", {0.21: 50.0, 0.20: 10.0}, {0.23: 40.0})
    time.sleep(H.MIN_ENTRE_ACCIONES_S + 0.02)
    ex.decidir(c, 199.0, time.time())                                   # repega: cancela h
    assert h in ex.canceladas
    time.sleep(0.15)
    ex.liquidar_todo(c.estado, c.lib, 198.0)                            # lectura con f=0: aún NO asentada
    assert h in ex.canceladas
    ex.cli.ordenes[h]["size_matched"] = 2.0                             # el casado de ms antes del cancel aparece ~1 s después
    time.sleep(0.12)
    ex.liquidar_todo(c.estado, c.lib, 197.0)
    assert c.estado["tU"]["llenas"] == 2.0
    ex.decidir(c, 197.0, time.time())
    time.sleep(0.4)
    ex.liquidar_todo(c.estado, c.lib, 196.0)
    ex.decidir(c, 196.0, time.time())
    assert len(ex.cli.posts) == 1 and c.estado["tU"]["cerrado"]         # un relleno cierra la puja: no se repuja el mismo bid


def test_relectura_rapida_de_canceladas_solo_al_cumplirse_asentar(monkeypatch):
    monkeypatch.setattr(H, "ASENTAR_H47_S", 5.0)
    monkeypatch.setattr(X, "ASENTAR_S", 5.0)
    ex = nuevo("relectura")
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())
    h = ex.cli.posts[0][0]
    poner_libro(c.lib, "tU", {0.21: 50.0}, {0.23: 40.0})
    time.sleep(H.MIN_ENTRE_ACCIONES_S + 0.02)
    ex.decidir(c, 199.0, time.time())
    assert h in ex.canceladas
    llamadas = []
    orig = ex.cli.get_order
    ex.cli.get_order = lambda hh: (llamadas.append(hh), orig(hh))[1]
    c.ult_poll, c.ult_poll_can = time.time(), 0.0                       # POLL_S aún no toca; la relectura rápida sí
    ex.paso(c)
    assert not llamadas and h in ex.canceladas                          # sin martillear la API antes de cumplirse ASENTAR_S (5 s)


# ---- #2 rellenos vistos fuera de liquidar() (verificar, finalizar) se reincorporan a la medición
def test_relleno_tardio_por_verificar_cierra_la_puja_y_entra_en_puja_fin():
    ex = nuevo("tardio")
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())
    h = ex.cli.posts[0][0]
    _cancelar_y_asentar(ex, c)
    assert h not in ex.canceladas and c.estado["tU"]["llenas"] == 0.0
    ex.cli.ordenes[h]["size_matched"] = 3.0                             # se refleja tarde (p. ej. ~30 s después)
    time.sleep(C.T_VERIF_S + 0.7)
    ex.verificar()
    assert c.estado["tU"]["llenas"] == 0.0                              # aún no incorporado a la medición
    ex.decidir(c, 150.0, time.time())
    assert c.estado["tU"]["llenas"] == 3.0 and c.estado["tU"]["cerrado"] and eventos("relleno_tardio")
    assert len(ex.cli.posts) == 1                                       # no se repuja tras el relleno tardío
    ex.finalizar(c)
    r = eventos("puja_fin")[0]
    assert r["relleno_real"] is True and r["llenas_en_vuelo"] == 0.0 and r["llenas_detectadas"] == 3.0 and r["rellenos_tardios"] == 1
    assert r["rellenos"][0]["tardio"] and r["rellenos"][0]["markout_5s"] is None     # sin markout inventado (missing, no 0)
    assert r["relleno_cota_inferior"] is False


def test_finalizar_verifica_y_ve_relleno_que_solo_la_verificacion_conoce():
    ex = nuevo("tardio_fin")
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())
    h = ex.cli.posts[0][0]
    _cancelar_y_asentar(ex, c)
    ex.cli.ordenes[h]["size_matched"] = 4.0
    time.sleep(C.T_VERIF_S + 0.7)
    ex.finalizar(c)                                                     # sin verificar() previo: finalizar lo hace él
    r = eventos("puja_fin")[0]
    assert r["relleno_real"] is True and r["llenas_detectadas"] == 4.0 and r["llenas_en_vuelo"] == 0.0


def test_puja_fin_marca_cota_inferior_si_hay_ordenes_sin_verificar():
    ex = nuevo("sinverif")
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())
    ex.finalizar(c)                                                     # la orden sigue viva en el libro falso: nada verificable
    r = eventos("puja_fin")[0]
    assert r["relleno_cota_inferior"] is True and r["ordenes_sin_verificar"]


def test_trades_con_mas_relleno_que_las_lecturas_se_marca_no_se_suma():
    ex = nuevo("trades_mas")
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())
    h = ex.cli.posts[0][0]
    _cancelar_y_asentar(ex, c)
    ex.cli.get_trades = lambda *a, **k: [{"id": "t1", "status": "MATCHED", "match_time": "1", "taker_order_id": h, "size": "3",
                                          "price": "0.18", "side": "BUY", "maker_orders": []}]
    time.sleep(C.T_VERIF_S + 0.7)
    ex.finalizar(c)
    r = eventos("puja_fin")[0]
    assert r["llenas_detectadas"] == 0.0 and r["relleno_solo_trades"] == [h] and r["relleno_real"] is True   # marcado, no sumado
    assert ex.ordenes()[h].lo == 0.0                                    # la contabilidad no sube por /trades


# ---- #3 el gemelo CONS usa el t_post de la RESPUESTA del POST, no el instante previo a firmar
def test_gemelo_usa_t_post_de_la_respuesta_no_t0():
    ex = nuevo("gem_tpost")
    c = ctx_de(ex, "eth")
    orig = ex.cli.create_order

    def firma_lenta(args):
        time.sleep(0.3)                                                 # firma + neg_risk + POST: la orden aún no está en el libro
        return orig(args)
    ex.cli.create_order = firma_lenta
    t0 = time.time()
    ex.decidir(c, 200.0, t0)
    h = ex.cli.posts[0][0]
    g = ex.gem[h]
    assert g["t_post"] == ex.vivas[h]["t_post"] and g["t_post"] >= t0 + 0.3 and g["t_call0"] <= t0 + 0.05
    assert eventos("post_lat")[0]["t_post_gemelo"] == g["t_post"]
    # una operación que ATRAVIESA nuestro precio (0,18) a t0+0,15 s: antes de que la orden estuviera en el libro -> no cuenta
    t = t0 + 0.15
    c.lib.trades["tU"].append((t, t, 0.10, 99, "SELL"))
    c.lib.trades_trecv["tU"].append(t)
    ex.simular(c)
    assert ex.gem_lleno.get(h, 0.0) == 0.0 and not eventos("gemelo_relleno")
    t2 = g["t_post"] + 0.2                                              # y una posterior al alta sí
    c.lib.trades["tU"].append((t2, t2, 0.10, 99, "SELL"))
    c.lib.trades_trecv["tU"].append(t2)
    ex.simular(c)
    assert ex.gem_lleno[h] == 6.0 and eventos("gemelo_relleno")


# ---- #10 'visto': criterio nivel o plazo, también en seco, con el motivo registrado
def test_visto_por_nivel_en_real_y_por_plazo_tambien_en_seco():
    ex = nuevo("visto_real")
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())
    h = ex.cli.posts[0][0]
    ex.decidir(c, 200.0, time.time())
    assert not eventos("visto")                                         # el nivel 0,18 no muestra nada aún y no ha pasado el plazo
    with c.lib.lk:
        c.lib.L["tU"]["bids"][0.18] = 6.0                                # nuestro resto aparece en el nivel (cola 0 + 6)
    ex.decidir(c, 199.9, time.time())
    v = eventos("visto")
    assert len(v) == 1 and v[0]["oid"] == h and v[0]["criterio"] == "nivel" and v[0]["simulado"] is False
    exs = nuevo("visto_seco", real=False)
    cs = ctx_de(exs, "eth")
    exs.decidir(cs, 200.0, time.time())
    hs = eventos("intencion_post")[0]["oid"]
    exs.decidir(cs, 200.0, time.time())
    assert not eventos("visto")
    exs.vivas[hs]["t_post"] -= H.X.VISTO_MAX_S + 0.5                     # pasa el plazo POST + VISTO_MAX_S
    exs.decidir(cs, 199.0, time.time())
    v = eventos("visto")
    assert len(v) == 1 and v[0]["criterio"] == "plazo" and v[0]["simulado"] is True


# ---- #4 excepción repetida en 'asentando': no bucle infinito
def test_excepcion_repetida_en_asentando_abandona_el_mercado_y_run_termina(monkeypatch):
    monkeypatch.setattr(H, "sim_uno", lambda *a, **k: (_ for _ in ()).throw(KeyError("tU")))
    ex = nuevo("exc_loop")
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())                                   # una orden real viva
    h = ex.cli.posts[0][0]
    ex.parada = "no lanzar mercados nuevos (prueba)"
    t = threading.Thread(target=ex.run, kwargs={"duracion_max_s": 60}, daemon=True)
    t.start()
    t.join(30)
    assert not t.is_alive(), "run() no termina: bucle infinito de excepciones"
    assert len(eventos("excepcion")) <= H.MAX_EXC_CTX                   # ledger acotado, no ~10 líneas/s
    assert len(eventos("mercado_abandonado")) == 1 and c.fase == "fin"
    assert ex.kill and "excepción" in ex.kill and X.KILL_FICHERO.exists()
    assert ex.cli.ordenes[h]["status"] == "CANCELED"                    # lo vivo se cancela (kill + cerrar_salida)
    assert eventos("fin_ejecucion")


def test_excepcion_en_activa_pasa_a_asentando_con_kill():
    ex = nuevo("exc_activa")
    c = ctx_de(ex, "eth")
    c.lib = None                                                        # fuerza una excepción en paso()
    ex.paso_seguro(c)
    assert ex.kill and c.fase == "asentando" and c.n_exc == 1 and len(eventos("excepcion")) == 1


# ---- #7 el contexto de un mercado terminado se libera
def test_ctx_terminado_se_sustituye_por_centinela_y_se_poda(monkeypatch):
    ex = nuevo("centinela")
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())
    h = ex.cli.posts[0][0]
    assert h in ex.gem
    ex.kill = "prueba"
    for _ in range(10):
        ex.paso_seguro(c)
        if c.fase == "espera_fin":
            break
        time.sleep(0.06)
    c.mk["fin"] = time.time() - H.FIN_ESPERA_S - 1
    ex.paso_seguro(c)
    assert c.fase == "fin" and ex.ctxs[c.mk["slug"]] == "terminado" and h not in ex.gem and h not in ex.gem_lleno
    assert not any(isinstance(v, H.Ctx) for v in ex.ctxs.values())
    # poda de centinelas viejos y de errores de gamma antiguos; no se recrea el mercado terminado
    ex2 = nuevo("centinela2")
    ahora = time.time()
    ex2.ctxs["eth-updown-5m-100"] = "terminado"
    ex2._gamma_err["eth-updown-5m-100"] = 5.0
    llamadas = []
    monkeypatch.setattr(H, "mercado_5m", lambda coin, ini: (llamadas.append((coin, ini)), None)[1])
    ex2.lanzar_mercados(ahora)
    assert "eth-updown-5m-100" not in ex2.ctxs and "eth-updown-5m-100" not in ex2._gamma_err


# ---- #5 enfriamiento por token (un 4xx en ETH YES no bloquea los YES de SOL/XRP)
def _ctx_tokens(ex, coin, tu, td, bid=0.20, ask=0.22):
    lib = lib_falso(bid, ask, tu, td)
    mk = mk_falso(coin)
    mk["toks"] = {"Up": tu, "Down": td}
    c = H.Ctx(coin, mk, lib, H.K_POR_MONEDA[coin])
    c.fase = "activa"
    ex.ctxs[mk["slug"]] = c
    return c


def test_enfriamiento_por_token_no_por_lado():
    import httpx
    from py_clob_client_v2.exceptions import PolyApiException
    ex = nuevo("enf_tok", n_max=5, max_vivas=5)
    c_eth = _ctx_tokens(ex, "eth", "eU", "eD")
    c_sol = _ctx_tokens(ex, "sol", "sU", "sD")
    orig = ex.cli.post_order

    def rechaza_eth(signed, tipo, post_only=True):
        if signed["args"].token_id == "eU":
            raise PolyApiException(httpx.Response(400, json={"error": "order below minimum notional"}))
        return orig(signed, tipo, post_only=post_only)
    ex.cli.post_order = rechaza_eth
    ex.decidir(c_eth, 200.0, time.time())
    assert eventos("post_rechazada") and ex.enfriar_tok.get("eU", 0) > time.time() + 5
    assert "YES" not in ex.enfriar                                      # el valor por lado del harness no queda armado
    ex.decidir(c_sol, 200.0, time.time())                               # SOL YES no está bloqueado
    assert len(ex.cli.posts) == 1 and ex.cli.posts[0][1] == 0.19
    n = len(eventos("intencion_post", True))
    ex.decidir(c_eth, 200.0, time.time())                               # pero ETH sigue en su enfriamiento
    assert len(eventos("intencion_post", True)) == n


# ---- #6 topes en disco: total (todos los escalones reales) y no reentrar en una puja ya operada
def test_tope_total_se_reconstruye_del_ledger_y_de_otros_escalones(monkeypatch):
    (TMP / "fam1").mkdir(exist_ok=True)
    lin = lambda oid, real=True, alias=None, tipo="intencion_post": json.dumps(
        dict({"tipo": tipo, "oid": oid, "real": real, "slug": "eth-updown-5m-1", "ts": "2026-10-19T10:00:00.000+00:00"},
             **({"alias_de": alias} if alias else {})))
    (TMP / "fam1" / "experimento_h47_A_ledger.jsonl").write_text("\n".join([lin("a1"), lin("a2"), lin("a2", alias="a2x"), lin("a3"),
                                                                           lin("a1"), lin("s", real=False)]) + "\n")
    (TMP / "fam1" / "experimento_h47_seco_B_ledger.jsonl").write_text(lin("z1", real=False) + "\n")   # seco: no cuenta
    ex = nuevo("fam1/experimento_h47_B_ledger")
    assert ex.n_ordenes_total == 3                                      # a1, a2, a3 (alias y duplicados no cuentan; el seco tampoco)
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())
    ex.decidir(c, 200.0, time.time())
    assert ex.n_ordenes_total == 4 and len(ex.cli.posts) == 1
    # reinicio: el contador sigue en 4, no en 0
    ex._cerrado = True
    X._CACHE = None
    X.LOCK = TMP / "fam1" / "otro.lock"
    cli_viejo = ex.cli
    X.cliente_dedicado = lambda: (cli_viejo, "0xabc")
    ex2 = H.Exp47(True, "B", 230, 60.0, 5, 1.0, ("eth", "sol", "xrp"), 12.0, 5)
    CREADOS.append(ex2)
    assert ex2.n_ordenes_total == 4
    monkeypatch.setattr(H, "MAX_ORDENES_TOTAL", 4)
    c2 = ctx_de(ex2, "sol")
    ex2.decidir(c2, 200.0, time.time())
    assert len(cli_viejo.posts) == 1 and ex2.parada and "tope total" in ex2.parada      # no envía y para


def test_tope_total_cuenta_tambien_posts_rechazados_o_cortados():
    ex = nuevo("tope_total_rech", escalon="A")
    c = ctx_de(ex, "eth")
    ex.cli.post_order = lambda *a, **k: (_ for _ in ()).throw(RuntimeError("timeout"))
    ex.decidir(c, 200.0, time.time())
    assert ex.n_ordenes_total == 1                                      # intención escrita aunque el POST se corte


def test_reinicio_no_reentra_en_una_puja_ya_operada(monkeypatch):
    ex = nuevo("noreentra")
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())
    slug = c.mk["slug"]
    ex._cerrado = True
    X._CACHE = None
    X.LOCK = TMP / "noreentra2.lock"
    cli_viejo = ex.cli
    X.cliente_dedicado = lambda: (cli_viejo, "0xabc")
    ex2 = H.Exp47(True, "B", 230, 60.0, 5, 1.0, ("eth", "sol", "xrp"), 12.0, 5)
    CREADOS.append(ex2)
    monkeypatch.setattr(X, "Libro", lambda *a, **k: (_ for _ in ()).throw(AssertionError("no debe abrir WS de un mercado ya operado")))
    mk = mk_falso("eth", slug=slug)
    assert ex2.crear_ctx("eth", mk) is None
    ev = eventos("mercado_ya_operado_no_reentra")
    assert ev and ev[-1]["slug"] == slug and ev[-1]["n_ordenes_previas"] == 1


# ---- #8 el tope de vivas cuenta vivas + canceladas del libro, no solo pujas en fase 'activa'
def test_max_vivas_cuenta_ordenes_en_libro_aunque_el_mercado_este_asentando():
    ex = nuevo("vivas8", max_vivas=1)
    c1 = _ctx_tokens(ex, "eth", "eU", "eD")
    c2 = _ctx_tokens(ex, "sol", "sU", "sD")
    ex.decidir(c1, 200.0, time.time())
    assert len(ex.cli.posts) == 1
    ex.cerrar_ctx(c1, "t_stop")                                         # asentando: su orden sigue viva hasta cancelarse
    assert c1.fase == "asentando" and ex.vivas
    ex.decidir(c2, 200.0, time.time())
    assert len(ex.cli.posts) == 1                                       # bloqueada: ya hay 1 orden en el libro
    # y una orden CANCELADA sin confirmar también ocupa plaza (incluso para el repegado de otra puja)
    ex.vivas.clear()
    ex.canceladas["x"] = {"tok": "eU", "precio": 0.2, "size": 5.0, "slug": c1.mk["slug"]}
    ex.decidir(c2, 200.0, time.time())
    assert len(ex.cli.posts) == 1
    ex.canceladas.clear()
    c1.estado["eU"]["cerrado"] = True
    ex.decidir(c2, 200.0, time.time())
    assert len(ex.cli.posts) == 2


def test_max_vivas_cuenta_general_aplica_tambien_a_pujas_ya_abiertas_y_pujas_activas_sin_orden():
    ex = nuevo("vivas8b", max_vivas=1)
    c1 = _ctx_tokens(ex, "eth", "eU", "eD")
    c2 = _ctx_tokens(ex, "sol", "sU", "sD")
    ex.decidir(c1, 200.0, time.time())
    assert len(ex.cli.posts) == 1
    ex.slugs_usados.add(c2.mk["slug"])                                  # c2 ya tuvo una orden (no es su primera puja): solo vale el tope general
    ex.decidir(c2, 200.0, time.time())
    assert len(ex.cli.posts) == 1
    # puja activa sin orden en el libro (repegando): sigue ocupando plaza para una puja NUEVA
    h = ex.cli.posts[0][0]
    ex.cancelar(h)
    ex.canceladas.clear()
    assert not ex.vivas and not ex.canceladas and c1.posteado and not c1.estado["eU"]["cerrado"]
    c3 = _ctx_tokens(ex, "xrp", "xU", "xD")
    ex.decidir(c3, 200.0, time.time())
    assert len(ex.cli.posts) == 1


# ---- #9 las copias de H47 NO pueden divergir del harness: pruebas diferenciales (aleatorias, con semilla) contra el código original
def test_sim_uno_igual_que_simular_rellenos_del_harness_en_flujos_aleatorios():
    import random
    rng = random.Random(1947)
    ex = nuevo("dif_sim", real=False)
    par = {"tU": "tD", "tD": "tU"}
    for caso in range(300):
        lib = lib_falso()
        t0 = time.time()
        precio = rng.choice([0.18, 0.20, 0.25])
        o = {"tok": "tU", "precio": precio, "size": float(rng.choice([5, 6, 8])), "t_post": t0, "cola": rng.choice([0.0, 10.0, 30.0]),
             "vol_sim": 0.0, "slug": "s", "lado": "YES"}
        if rng.random() < 0.5:
            o["t_cancel"] = t0 + rng.uniform(0.3, 1.5)
        o_h = {k: (dict(v) if isinstance(v, dict) else v) for k, v in o.items()}       # copia para el harness
        ex.vivas = {"seco-x": o_h}
        ex.canceladas = {}
        ex.sim_lleno = {}
        ex._par = par
        f_uno = 0.0
        for tanda in range(2):                                                 # dos tandas: el estado incremental (i_sim, vol_sim) también cuenta
            for _ in range(rng.randint(0, 8)):
                tk = rng.choice(["tU", "tD"])
                tx = t0 + rng.uniform(-0.1, 2.0) + tanda * 0.01
                p = round(rng.choice([0.10, 0.17, 0.18, 0.19, 0.20, 0.21, 0.25, 0.80, 0.82, 0.84]), 2)
                lib.trades[tk].append((tx, tx, p, float(rng.randint(1, 20)), rng.choice(["BUY", "SELL"])))
                lib.trades_trecv[tk].append(tx)
            ex.simular_rellenos(lib)
            f_uno = H.sim_uno(lib, par, o, f_uno)
            assert abs(f_uno - ex.sim_lleno.get("seco-x", 0.0)) < 1e-9, (caso, tanda, o, o_h)


def test_cuadre_igual_que_capital_fuera_del_harness():
    ex = nuevo("dif_cuadre")
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())                                    # una orden real: exposición 6 * 0,18 = 1,08
    assert len(ex.cli.posts) == 1
    cand = {"size": 5.0, "precio": 0.2}
    for on in (19.59, 19.0, 18.6, 18.46, 18.4, 12.0, 0.0, 25.0):
        ex._kill = None
        r1 = ex.cuadre(on)
        k1 = ex.kill
        ex._kill = None
        ex._on_cache = (time.time(), on)                                 # capital_fuera lee la caché de 2 s
        r2 = ex.capital_fuera(cand)
        k2 = ex.kill
        assert r1 == (r2 is not None), (on, r1, r2)
        assert bool(k1) == bool(k2), (on, k1, k2)
    ex._kill = None


def test_en_seco_el_tope_total_no_acumula_de_ensayo_en_ensayo():
    ex = nuevo("seco_acum", real=False)
    c = ctx_de(ex, "eth")
    ex.decidir(c, 200.0, time.time())
    assert ex.n_ordenes_total == 1
    ex._cerrado = True
    X._CACHE = None
    X.LOCK = TMP / "seco_acum2.lock"
    ex2 = H.Exp47(False, "B", None, 60.0, 5, 1.0, ("eth", "sol", "xrp"), 12.0, 5)
    CREADOS.append(ex2)
    assert ex2.n_ordenes_total == 0 and ex2.n_usadas() == 1                 # N sí persiste (como en real); el tope de órdenes es por proceso en seco


# ---------------------------------------------------------------- suelo dinámico (opción b de Javi, 19-Oct): saldo verificado − presupuesto útil
# 2ª /code-review medium (19-Oct): #1 alza de saldo a mitad, #2 suelo corrupto fail-closed + fsync, #3 saldo mínimo de arranque, #4 bloque,
# #5 suelo al enviar la 1ª orden, #6 última lectura y tolerancia sin acumulación, #7 reseteo auditado, #8 ledgers hermanos, #9 tests.
def lecturas(*vals):
    """X.saldo_onchain que devuelve `vals` en orden (la 1ª la consume el saldo_inicial del harness) y después el saldo de ONCHAIN."""
    it = iter(vals)
    return lambda w: next(it, ONCHAIN["pusd"])


def primera_orden(ex, coin="eth"):
    """Provoca el primer POST real (la compuerta de dinero + _post_real) sobre un mercado falso."""
    PRIMERA["n"] += 1
    c = ctx_de(ex, coin, slug=f"{coin}-updown-5m-{8000000 + PRIMERA['n']}")    # slug propio: un reinicio no reentra en una puja ya operada
    ex.decidir(c, 200.0, time.time())
    return c


PRIMERA = {"n": 0}


def liquidar(ex):
    """Deja el ledger como tras un cierre limpio: órdenes fuera del libro y verificadas (hi == lo) y nada vivo en el exchange falso."""
    from datetime import datetime, timedelta, timezone
    ahora = datetime.now(timezone.utc)
    lineas = []
    for oid in list(ex.ordenes()):
        lineas.append(json.dumps({"tipo": "fuera_libro", "oid": oid, "real": True, "ts": (ahora - timedelta(seconds=30)).isoformat(timespec="milliseconds")}))
        lineas.append(json.dumps({"tipo": "verificada", "oid": oid, "real": True, "f": 0.0, "ts": (ahora - timedelta(seconds=20)).isoformat(timespec="milliseconds")}))
    with open(X.LEDGER, "a") as f:
        f.write("\n".join(lineas) + "\n")
    for o in ex.cli.ordenes.values():
        o["status"] = "CANCELED"
    X._CACHE = None
    ex._cerrado = True


def envejecer(ex, seg):
    """Retrasa `seg` segundos el inicio del alza pendiente (conserva su bloque)."""
    p = ex._alza_pend
    ex._alza_pend = (p[0], p[1] - seg) + tuple(p[2:])


def reinicio(saldo, nombre, ledger=None, presupuesto=12.0):
    """Nuevo proceso sobre el MISMO ledger (reinicio), con ese saldo on-chain."""
    ONCHAIN["pusd"] = saldo
    X._CACHE = None
    X.LOCK = TMP / f"{nombre}.lock"
    X.cliente_dedicado = lambda: (Cli(), "0xabc")
    e = H.Exp47(True, "B", 230, 60.0, 5, 1.0, ("eth", "sol", "xrp"), presupuesto, 5)
    CREADOS.append(e)
    return e


def test_presupuesto_util_es_5_por_decision_de_javi_y_tope_duro_en_real(monkeypatch):
    assert DEF_PRESUPUESTO == 5.0
    monkeypatch.setattr(H, "PRESUPUESTO_UTIL", DEF_PRESUPUESTO)
    for malo in (5.01, 12.0, float("nan"), float("inf"), 0.0, -1.0):
        with pytest.raises(SystemExit):
            nuevo("tope5", presupuesto=malo)
    for malo in (float("nan"), float("inf"), 0.0, -1.0):
        with pytest.raises(SystemExit):
            nuevo("tope5seco0", real=False, presupuesto=malo)                   # ni siquiera en seco valen NaN/inf/<=0
    ex = nuevo("tope5ok", presupuesto=5.0)
    assert abs(ex.saldo_min - 14.59) < 1e-9                                     # 19,59 − 5
    ex2 = nuevo("tope5seco", real=False, presupuesto=50.0)                      # el tope solo aplica en real
    assert ex2.saldo_min == 0.0
    vistos = {}

    class Falso:
        n_max = 1
        kill = None

        def __init__(self, *a):
            vistos["args"] = a

        def n_usadas(self):
            return 0

        def run(self, duracion_max_s=None):
            return None
    monkeypatch.setattr(H, "Exp47", Falso)
    monkeypatch.setattr(H, "configurar_rutas", lambda *a, **k: None)
    assert H.main([]) == 0 and vistos["args"][7] == 5.0                         # defecto de la CLI
    assert H.main(["--presupuesto-util", "7"]) == 0 and vistos["args"][7] == 7.0
    with pytest.raises(SystemExit):
        H.main(["--saldo-min", "12"])                                           # argparse: --saldo-min ya no existe


def test_suelo_es_saldo_verificado_menos_presupuesto_y_se_escribe_al_enviar_la_primera_orden(monkeypatch):
    fs = []
    monkeypatch.setattr(H, "_fsync_ledger", lambda: fs.append(len(X.leer_ledger())))
    ex = nuevo("sd1")
    assert ex.saldo_verificado == 19.59 and abs(ex.saldo_min - 7.59) < 1e-9 and ex.bloque_saldo is not None
    assert eventos("suelo_fijado", True) == [] and fs == []                     # #5: el arranque solo CALCULA (memoria + aviso), no fija
    calc = eventos("suelo_calculado", True)[-1]
    assert abs(calc["suelo"] - 7.59) < 1e-9 and calc["bloque"] == ex.bloque_saldo
    primera_orden(ex)
    assert len(ex.cli.posts) == 1
    ev = eventos("suelo_fijado", True)
    assert len(ev) == 1 and ev[0]["wallet"] == "0xabc" and abs(ev[0]["suelo"] - 7.59) < 1e-9 and ev[0]["presupuesto"] == 12.0
    assert ev[0]["suelos_previos"] == [] and ev[0]["bloque"] == ex.bloque_saldo
    tipos = [e["tipo"] for e in eventos()]
    assert tipos.index("suelo_fijado") < tipos.index("intencion_post")          # antes de la orden, no después
    assert len(fs) == 1 and fs[0] == tipos.index("suelo_fijado") + 1            # fsync justo tras escribirlo, antes de la intención
    primera_orden(ex, "sol")
    assert len(eventos("suelo_fijado", True)) == 1                              # una sola vez por ejecución
    X.saldo_onchain = lambda w: 40.0                                            # otra wallet con más saldo: el suelo sigue al saldo, no es fijo
    assert abs(nuevo("sd1b").saldo_min - 28.0) < 1e-9
    X.saldo_onchain = lambda w: 20.0
    assert abs(nuevo("sd1d", presupuesto=6.0).saldo_min - 14.0) < 1e-9


def test_fsync_ledger_hace_os_fsync_del_fichero_del_ledger(monkeypatch):
    ex = nuevo("fsync_real")
    vistos = []
    monkeypatch.setattr(H.os, "fsync", lambda fd: vistos.append(os.readlink(f"/proc/self/fd/{fd}")))
    H._fsync_ledger()
    assert vistos == [str(X.LEDGER)]
    vistos.clear()
    primera_orden(ex)                                                           # el suelo_fijado se sincroniza ANTES de la intención
    assert vistos and all(v == str(X.LEDGER) for v in vistos) and len(vistos) >= 2     # suelo_fijado + intencion_post (esta, la del harness)


def test_suelo_escrito_nunca_redondea_hacia_abajo(monkeypatch):
    X.saldo_onchain = lecturas(19.59, 19.5900004, 19.5900004)
    ex = nuevo("sd_ceil")
    primera_orden(ex)
    ev = eventos("suelo_fijado", True)[-1]
    assert ev["suelo"] >= ex.saldo_min - 1e-12 and abs(ev["suelo"] - ex.saldo_min) < 2e-6
    X.saldo_onchain = lambda w: ONCHAIN["pusd"]


def test_fsync_del_suelo_que_falla_mata_y_no_envia(monkeypatch):
    def malo():
        raise OSError("disco")
    monkeypatch.setattr(H, "_fsync_ledger", malo)
    ex = nuevo("sd1f")
    primera_orden(ex)
    assert ex.cli.posts == [] and not eventos("intencion_post", True)
    assert ex.kill and "suelo_fijado" in ex.kill and X.KILL_FICHERO.exists()


def test_arranque_abortado_no_sube_el_suelo_sin_ratchet_por_arranques():
    ex = nuevo("sd5")
    primera_orden(ex)                                                           # suelo 7,59 escrito
    ex._cerrado = True
    for i, saldo in enumerate((40.0, 60.0, 80.0)):                              # arranques que salen sin enviar nada
        reinicio(saldo, f"sd5_{i}")._cerrado = True
    e = reinicio(19.59, "sd5_fin")
    assert abs(e.saldo_min - 7.59) < 1e-9                                       # los 28/48/68 calculados y no enviados no cuentan
    assert [round(x["suelo"], 2) for x in eventos("suelo_fijado", True)] == [7.59]


def test_sin_saldo_verificable_en_el_arranque_no_hay_suelo_ni_se_envia_nada():
    casos = {"sd2a": (19.59, None, None, None, None, None, None, None),        # RPC caído tras el saldo inicial
             "sd2b": (19.59, 19.59, None, 19.59, None, 19.59, None),           # una lectura de cada par falla siempre
             "sd2c": (19.59, 19.59, 12.0, 19.59, 12.0, 19.59, 12.0)}           # las lecturas nunca coinciden
    for nombre, seq in casos.items():
        X.saldo_onchain = lecturas(*seq)
        ex = nuevo(nombre)
        assert ex.saldo_min is None, nombre                                     # tres rondas sin coincidencia: NO hay suelo
        assert eventos("suelo_no_fijado", True)
        X.saldo_onchain = lambda w: 19.59                                       # aunque el saldo ya sea legible, sin suelo no se envía
        ex._on_cache = (0.0, None)
        assert not ex.puede_enviar(1.0)
        c = ctx_de(ex, "eth")
        ex.decidir(c, 200.0, time.time())
        assert ex.cli.posts == [] and not eventos("intencion_post", True)
        ex.vigilar_saldo(time.time())
        assert ex.parada and "sin fijar" in ex.parada
        ex.parada = None
        ex.ctxs.clear()                                                         # run() solo con la parada de arranque, sin mercados sintéticos
        t = threading.Thread(target=lambda: ex.run(duracion_max_s=0.01), daemon=True)
        t.start()
        t.join(timeout=15)
        assert not t.is_alive() and ex.cli.posts == []
        assert "sin fijar" in (ex.parada or "")
    X.saldo_onchain = lambda w: ONCHAIN["pusd"]


def test_saldo_de_arranque_menor_que_presupuesto_mas_margen_no_opera_en_vez_de_suelo_cero():
    for saldo, opera in ((1.0, False), (9.0, False), (12.99, False), (13.0, True), (13.5, True)):
        X.saldo_onchain = lambda w, v=saldo: v
        ex = nuevo(f"sd3_{saldo}")
        if opera:
            assert abs(ex.saldo_min - (saldo - 12.0)) < 1e-9 and ex.saldo_min >= H.SALDO_ARRANQUE_MARGEN - 1e-9, saldo
        else:
            assert ex.saldo_min is None and "presupuesto" in eventos("suelo_no_fijado", True)[-1]["motivo"], saldo
            ex._on_cache = (0.0, None)
            assert not ex.puede_enviar(1.0)                                     # None no es 0.0: no se evalúa como «falsy»
            primera_orden(ex)
            assert ex.cli.posts == []
    X.saldo_onchain = lambda w: ONCHAIN["pusd"]


def test_tolerancia_de_verificacion_exacta_y_ultima_lectura_no_el_maximo():
    X.saldo_onchain = lecturas(19.59, 19.59, 19.64)                             # diferencia = tolerancia exacta (0,05): coincide en la ronda 1
    ex = nuevo("sd3a")
    assert ex.saldo_verificado == 19.64 and abs(ex.saldo_min - 7.64) < 1e-9
    X.saldo_onchain = lecturas(19.59, 19.59, 19.6401, 19.59, 19.59)             # 0,0501: la ronda 1 NO coincide; la 2 sí
    ex = nuevo("sd3b")
    assert ex.saldo_verificado == 19.59                                         # si la ronda 1 hubiera valido saldría 19,6401
    X.saldo_onchain = lecturas(19.59, 19.62, 19.59)                             # #6: se usa la ÚLTIMA lectura verificada, no max(a, b)
    ex = nuevo("sd3c")
    assert ex.saldo_verificado == 19.59 and abs(ex.saldo_min - 7.59) < 1e-9
    X.saldo_onchain = lecturas(19.59, 19.59, 15.0, 19.59, 19.62)                # ronda 1 no coincide; ronda 2 sí
    assert nuevo("sd3d").saldo_verificado == 19.62
    X.saldo_onchain = lambda w: ONCHAIN["pusd"]


def test_lecturas_verificadas_exige_bloque_reciente_y_monotono():
    ahora = 10000.0
    ok = lambda a, b: H.lecturas_verificadas(a, b, ahora)
    assert ok((19.59, 100, ahora - 5), (19.59, 101, ahora - 3))
    assert not ok((19.59, 100, ahora - 5), (19.59, 100, ahora - 5))             # 3ª #6: el MISMO bloque no vale, hace falta uno mayor
    assert not ok((19.59, 101, ahora - 5), (19.59, 100, ahora - 3))             # el bloque retrocede: nodo distinto/atrasado
    assert ok((19.59, 100, ahora - 60.0), (19.59, 101, ahora - 60.0))           # justo en el límite de edad
    assert not ok((19.59, 100, ahora - 60.5), (19.59, 101, ahora - 3))          # 1ª lectura de un bloque viejo
    assert not ok((19.59, 100, ahora - 5), (19.59, 101, ahora - 61.0))          # 2ª lectura de un bloque viejo
    assert ok((19.59, 100, ahora + 30.0), (19.59, 101, ahora + 30.0))           # adelanto tolerado hasta 30 s
    assert not ok((19.59, 100, ahora + 31.0), (19.59, 101, ahora + 31.0))
    assert not ok(None, (19.59, 101, ahora)) and not ok((19.59, 100, ahora), None)
    assert not ok((19.59, 100, ahora), (19.70, 101, ahora))                     # saldos distintos


def test_bloque_viejo_o_que_retrocede_en_el_arranque_no_da_suelo():
    BLQ["dt"] = 300.0                                                           # el nodo devuelve siempre un bloque de hace 5 min
    try:
        ex = nuevo("sd4a")
    finally:
        BLQ["dt"] = 0.0
    assert ex.saldo_min is None and eventos("suelo_no_fijado", True)
    n = {"i": 0}

    def retrocede(w):
        n["i"] += 1
        return 19.59, 5000 - n["i"], time.time()                               # cada lectura es de un bloque ANTERIOR a la previa
    orig = H.saldo_con_bloque
    H.saldo_con_bloque = retrocede
    try:
        assert nuevo("sd4b").saldo_min is None
    finally:
        H.saldo_con_bloque = orig
    assert nuevo("sd4c").saldo_min is not None                                  # control: con bloques sanos sí hay suelo


def test_el_suelo_nunca_baja_en_un_reinicio_pero_sube_con_el_saldo_y_la_tolerancia_no_acumula():
    ex = nuevo("sd6")
    primera_orden(ex)
    assert abs(ex.saldo_min - 7.59) < 1e-9
    ex._cerrado = True
    e2 = reinicio(19.0, "sd6b")                     # 0,59 pUSD están en acciones sin redimir: 19,0 − 12 = 7,0 < 7,59: el suelo previo manda
    assert abs(e2.saldo_min - 7.59) < 1e-9
    primera_orden(e2)
    assert eventos("suelo_fijado", True)[-1]["suelos_previos"] == [7.59]
    e2._cerrado = True
    e3 = reinicio(30.0, "sd6c")                     # redención o depósito: el suelo sube con el saldo (30 − 12)
    assert abs(e3.saldo_min - 18.0) < 1e-9
    primera_orden(e3)
    e3._cerrado = True
    assert abs(reinicio(20.0, "sd6d").saldo_min - 18.0) < 1e-9                  # el máximo previo (18) se mantiene aunque el saldo sea menor
    # tolerancia: +0,05 sobre el máximo previo es ruido (se queda en 18); +0,0501 ya es una subida real
    assert abs(reinicio(30.05, "sd6e").saldo_min - 18.0) < 1e-9
    assert abs(reinicio(30.0501, "sd6f").saldo_min - 18.0501) < 1e-9
    # sin acumulación: 10 arranques con ruido de +0,04 sobre el MÁXIMO ya fijado no empujan el suelo
    for i in range(10):
        e = reinicio(30.04, f"sd6g{i}")
        primera_orden(e)
        e._cerrado = True
        assert abs(e.saldo_min - 18.0) < 1e-9


def ev_suelo(wallet, suelo, real=True, tipo="suelo_fijado", ts="2026-10-19T10:00:00.000+00:00", **kw):
    d = {"tipo": tipo, "wallet": wallet, "suelo": suelo, "real": real, "ts": ts}
    d.update(kw)
    return json.dumps(d)


def test_suelo_previo_de_otra_wallet_o_de_seco_se_ignora_y_los_de_otros_escalones_y_pares_cuentan():
    (TMP / "fam2").mkdir(exist_ok=True)
    (TMP / "fam2" / "experimento_h47_A_ledger.jsonl").write_text("\n".join([ev_suelo("0xabc", 9.0), ev_suelo("0xOTRA", 99.0),
                                                                           ev_suelo("0xabc", 50.0, False)]) + "\n")
    (TMP / "fam2" / "experimento_h47_seco_B_ledger.jsonl").write_text(ev_suelo("0xabc", 77.0) + "\n")          # seco: no cuenta
    (TMP / "fam2" / "experimento_pares_dedicada_seco_btc_ledger.jsonl").write_text(ev_suelo("0xabc", 88.0) + "\n")   # seco de pares: no cuenta
    ex = nuevo("fam2/experimento_h47_B_ledger")
    assert abs(ex.saldo_min - 9.0) < 1e-9                                       # max(19,59 − 12 = 7,59; A: 9,0)
    (TMP / "fam3").mkdir(exist_ok=True)
    (TMP / "fam3" / "experimento_pares_dedicada_ledger.jsonl").write_text(ev_suelo("0xabc", 10.0) + "\n")        # misma wallet, ledger de pares
    ex = nuevo("fam3/experimento_h47_B_ledger")
    assert abs(ex.saldo_min - 10.0) < 1e-9


def test_helper_ledgers_reales_hermanos_y_tope_de_ordenes_incluye_pares():
    d = TMP / "fam4"
    d.mkdir(exist_ok=True)
    lin = lambda oid, real=True: json.dumps({"tipo": "intencion_post", "oid": oid, "real": real, "slug": "eth-updown-5m-1",
                                             "ts": "2026-10-19T10:00:00.000+00:00"})
    (d / "experimento_h47_A_ledger.jsonl").write_text(lin("a1") + "\n")
    (d / "experimento_h47_seco_B_ledger.jsonl").write_text(lin("z", False) + "\n")
    (d / "experimento_pares_dedicada_ledger.jsonl").write_text("\n".join([lin("p1"), lin("p2"), lin("p3", False)]) + "\n")
    (d / "experimento_pares_dedicada_seco_btc_ledger.jsonl").write_text(lin("q1") + "\n")
    (d / "experimento_pares_cola_15m_ledger.jsonl").write_text(lin("c1") + "\n")          # otra wallet: no cuenta
    ex = nuevo("fam4/experimento_h47_B_ledger")
    assert sorted(f.name for f in H.ledgers_reales_hermanos()) == ["experimento_h47_A_ledger.jsonl", "experimento_pares_dedicada_ledger.jsonl"]
    assert ex.n_ordenes_total == 3                                              # a1 + p1 + p2 (reales); p3 es de ensayo
    X.LEDGER = d / "experimento_h47_A_ledger.jsonl"                             # visto desde A, B... el propio nunca se cuenta dos veces
    assert [f.name for f in H.ledgers_reales_hermanos()] == ["experimento_h47_B_ledger.jsonl", "experimento_pares_dedicada_ledger.jsonl"]


MALAS = {
    "truncada": '{"tipo": "suelo_fijado", "wallet": "0xabc", "su',
    "prefijo_corto": '{"tipo": "suel',
    "suelo_no_numerico": ev_suelo("0xabc", "abc"),
    "suelo_nulo": ev_suelo("0xabc", None),
    "suelo_nan": ev_suelo("0xabc", float("nan")),
    "suelo_negativo": ev_suelo("0xabc", -3.0),
    "sin_wallet": json.dumps({"tipo": "suelo_fijado", "suelo": 9.0, "real": True, "ts": "2026-10-19T10:00:00.000+00:00"}),
    "ts_corrupto": ev_suelo("0xabc", 9.0, ts="ayer"),
    "basura_binaria": "\x00\x00\x01{{{",
}


@pytest.mark.parametrize("clave", sorted(MALAS))
@pytest.mark.parametrize("donde", ["propio", "hermano"])
def test_suelo_previo_corrupto_o_ilegible_es_fail_closed(clave, donde):
    d = TMP / f"mal_{donde}_{clave}"
    d.mkdir(exist_ok=True)
    (d / ("experimento_h47_B_ledger.jsonl" if donde == "propio" else "experimento_h47_A_ledger.jsonl")).write_text(
        ev_suelo("0xabc", 3.0) + "\n" + MALAS[clave] + "\n")
    ex = nuevo(f"mal_{donde}_{clave}/experimento_h47_B_ledger")
    assert ex.saldo_min is None, (donde, clave)                                 # antes se ignoraba en silencio (fail-open)
    mot = eventos("suelo_no_fijado", True)[-1]["motivo"]
    assert "ilegible" in mot or "corrupta" in mot, mot
    assert not ex.puede_enviar(1.0)
    primera_orden(ex)
    assert ex.cli.posts == [] and not eventos("intencion_post", True)
    ex.vigilar_saldo(time.time())
    assert ex.parada and "sin fijar" in ex.parada


def test_ledger_hermano_que_no_se_puede_leer_es_fail_closed():
    d = TMP / "mal_dir"
    d.mkdir(exist_ok=True)
    (d / "experimento_h47_A_ledger.jsonl").mkdir(exist_ok=True)                 # existe pero no se puede leer como fichero
    ex = nuevo("mal_dir/experimento_h47_B_ledger")
    assert ex.saldo_min is None and "no se puede leer" in eventos("suelo_no_fijado", True)[-1]["motivo"]
    assert ex.n_ordenes_total == H.MAX_ORDENES_TOTAL            # 3ª #10: cuenta no fiable -> tope agotado, no «solo el ledger propio»
    primera_orden(ex)
    assert ex.cli.posts == []


def test_ledger_valido_de_otra_wallet_o_seco_con_basura_no_bloquea():
    d = TMP / "ok_otros"
    d.mkdir(exist_ok=True)
    (d / "experimento_h47_A_ledger.jsonl").write_text(ev_suelo("0xOTRA", 99.0) + "\n" + ev_suelo("0xabc", 4.0, False) + "\n\n")
    (d / "experimento_h47_seco_B_ledger.jsonl").write_text("basura\n")         # los ledgers de ensayo no se leen
    ex = nuevo("ok_otros/experimento_h47_B_ledger")
    assert abs(ex.saldo_min - 7.59) < 1e-9


def test_alza_de_saldo_a_mitad_de_ejecucion_sube_el_suelo_y_acota_el_gasto():
    """#1: sin esto, un depósito/redención a mitad dejaba gastar (saldo nuevo − suelo viejo) > presupuesto."""
    ex = nuevo("alza")                                                          # saldo 19,59, suelo 7,59, presupuesto 12
    primera_orden(ex)
    assert abs(ex.saldo_min - 7.59) < 1e-9 and ex.hwm == 19.59
    ONCHAIN["pusd"] = 30.0                                                      # +10,41 (depósito o redención): máximo nuevo 30
    ex._on_cache = (0.0, None)
    assert not ex.puede_enviar(1.0)                                             # alza SIN confirmar: no se envía
    assert ex._alza_pend is not None and ex.saldo_min < 8
    assert eventos("bloqueo_alza_saldo_sin_confirmar")
    ex._on_cache = (0.0, None)
    assert not ex.puede_enviar(1.0) and ex.hwm == 19.59                         # una 2ª lectura ANTES de 2 s tampoco confirma
    envejecer(ex, H.ALZA_CONFIRMA_S + 0.1)                                      # han pasado > 2 s
    ex._on_cache = (0.0, None)
    assert ex.puede_enviar(1.0)                                                 # confirmada: el suelo sube a 30 − 12 = 18
    assert abs(ex.saldo_min - 18.0) < 1e-9 and ex.hwm == 30.0
    su = eventos("suelo_subido", True)
    assert len(su) == 1 and abs(su[0]["suelo"] - 18.0) < 1e-9                   # persistido (para un reinicio)
    ex.vivas["x"] = {"tok": "tU", "precio": 0.3, "size": 10.0}                  # 3 $ comprometidos
    ex.vivas["y"] = {"tok": "tU", "precio": 0.3, "size": 10.0}
    ex.vivas["z"] = {"tok": "tU", "precio": 0.3, "size": 10.0}
    ex.vivas["w"] = {"tok": "tU", "precio": 0.3, "size": 10.0}                  # 12 $ comprometidos = exactamente el presupuesto desde el pico
    assert not ex.puede_enviar(1.0)                                             # con el suelo viejo (7,59) aún se habrían podido gastar 10 más
    ex.vivas.clear()
    # reinicio tras el alza: el suelo subido se conserva aunque el saldo vuelva a 20
    ex._cerrado = True
    assert abs(reinicio(20.0, "alza2").saldo_min - 18.0) < 1e-9


def test_alza_transitoria_no_sube_el_suelo_y_pequenas_alzas_se_ignoran():
    ex = nuevo("alza_t")
    primera_orden(ex)
    ONCHAIN["pusd"] = 40.0                                                      # una lectura alta aislada (RPC raro) ...
    ex._on_cache = (0.0, None)
    assert not ex.puede_enviar(1.0)
    ONCHAIN["pusd"] = 19.59                                                     # ... y la siguiente vuelve a la realidad
    ex._on_cache = (0.0, None)
    assert ex.puede_enviar(1.0) and ex._alza_pend is None
    assert abs(ex.saldo_min - 7.59) < 1e-9 and not eventos("suelo_subido", True)
    ONCHAIN["pusd"] = 19.59 + H.SALDO_TOL_VERIF                                 # +0,05 exacto: ruido, no es alza
    ex._on_cache = (0.0, None)
    assert ex.puede_enviar(1.0) and ex._alza_pend is None
    ONCHAIN["pusd"] = 40.0                                                      # dos lecturas altas: se toma la MENOR (35)
    ex._on_cache = (0.0, None)
    ex.puede_enviar(1.0)
    ONCHAIN["pusd"] = 35.0
    envejecer(ex, 3.0)
    ex._on_cache = (0.0, None)
    assert ex.puede_enviar(1.0) and ex.hwm == 35.0 and abs(ex.saldo_min - 23.0) < 1e-9


def test_vigilar_saldo_tambien_confirma_el_alza_y_el_suelo_subido_va_al_reinicio_aunque_no_se_envie():
    ex = nuevo("alza_v")                                                        # sin ninguna orden enviada aún: el alza solo se anota en memoria
    ONCHAIN["pusd"] = 30.0
    t = time.time()
    ex._on_cache = (0.0, None)
    ex.vigilar_saldo(t)
    ex._on_cache = (0.0, None)
    envejecer(ex, 3.0)
    ex.vigilar_saldo(t + 3.0)
    assert abs(ex.saldo_min - 18.0) < 1e-9 and not eventos("suelo_subido", True)
    primera_orden(ex)
    assert abs(eventos("suelo_fijado", True)[-1]["suelo"] - 18.0) < 1e-9        # al enviar se fija el suelo ya subido


def test_gasto_total_de_la_ejecucion_nunca_supera_el_presupuesto_con_alzas_y_ordenes():
    """Barrido: tras cada alza confirmada el comprometido máximo permitido desde el pico es <= presupuesto."""
    ex = nuevo("barrido", presupuesto=5.0 if False else 12.0)
    primera_orden(ex)
    for nuevo_saldo in (19.59, 25.0, 25.0, 31.0):
        ONCHAIN["pusd"] = nuevo_saldo
        for _ in range(2):
            ex._on_cache = (0.0, None)
            if ex._alza_pend:
                envejecer(ex, 3.0)
            ex.puede_enviar(0.5)
        ex.vivas.clear()
        ex.vivas["a"] = {"tok": "tU", "precio": 0.3, "size": 10.0}
        mx = 0.0
        for k in range(100):
            ex.vivas[f"k{k}"] = {"tok": "tU", "precio": 0.3, "size": 10.0}
            ex._on_cache = (0.0, None)
            if not ex.puede_enviar(0.5):
                break
            mx = ex.comprometido() + 0.5
        assert mx <= 12.0 + 1e-9, (nuevo_saldo, mx)
        assert ex.hwm - ex.saldo_min <= 12.0 + 1e-9


def test_reinicio_voluntario_del_suelo_exige_confirmacion_y_deja_evento():
    (TMP / "rs1").mkdir(exist_ok=True)
    ex = nuevo("rs1/experimento_h47_B_ledger")
    ONCHAIN["pusd"] = 40.0
    ex._cerrado = True
    e = reinicio(40.0, "rs1b")
    primera_orden(e)                                                            # suelo 28 fijado
    liquidar(e)
    # retirada voluntaria: el saldo baja a 20 -> el suelo previo (28) deja el saldo por debajo y no se opera
    e2 = reinicio(20.0, "rs1c")
    assert abs(e2.saldo_min - 28.0) < 1e-9 and e2.saldo_min > 20.0
    e2.vigilar_saldo(time.time())
    assert e2.cli.posts == []
    e2._cerrado = True
    n0 = len(eventos())
    assert H.reiniciar_suelo("0xabc", "retiro 20 pUSD", cli=Cli(), leer=lambda m: "no") is None       # confirmación equivocada: nada cambia
    assert len(eventos()) == n0
    with pytest.raises(SystemExit):
        H.reiniciar_suelo("0xabc", "  ", cli=Cli(), leer=lambda m: "REINICIAR SUELO 0xabc"[:0])        # sin motivo
    fs = []
    orig = H._fsync_ledger
    H._fsync_ledger = lambda: fs.append(1)
    try:
        ev = H.reiniciar_suelo("0xabc", "retiro 20 pUSD", cli=Cli(), leer=lambda m: "REINICIAR SUELO " + "0xabc"[-6:])
    finally:
        H._fsync_ledger = orig
    assert ev and fs == [1] and len(eventos("suelo_reiniciado", True)) == 1
    assert eventos("suelo_reiniciado", True)[0]["suelos_descartados"] == [28.0]       # solo el de la ejecución que SÍ envió (rs1 no envió)
    e3 = reinicio(20.0, "rs1d")
    assert abs(e3.saldo_min - 8.0) < 1e-9                                       # 20 − 12: los suelos previos ya no cuentan
    primera_orden(e3)
    e3._cerrado = True
    assert abs(reinicio(20.0, "rs1e").saldo_min - 8.0) < 1e-9                   # y los nuevos (posteriores al reseteo) sí
    assert abs(reinicio(30.0, "rs1f").saldo_min - 18.0) < 1e-9
    e4 = reinicio(15.0, "rs1g")
    e4._cerrado = True
    assert abs(e4.saldo_min - 8.0) < 1e-9                                       # el máximo posterior (8) manda sobre 15 − 12 = 3


def test_reinicio_del_suelo_acepta_las_lineas_ilegibles_que_se_listaron_y_solo_esas():
    d = TMP / "rs2"
    d.mkdir(exist_ok=True)
    (d / "experimento_h47_B_ledger.jsonl").write_text(ev_suelo("0xabc", 3.0) + "\n" + MALAS["truncada"] + "\n")
    ex = nuevo("rs2/experimento_h47_B_ledger")
    assert ex.saldo_min is None
    ex._cerrado = True
    assert H.reiniciar_suelo("0xabc", "linea truncada", cli=Cli(), leer=lambda m: "REINICIAR SUELO " + "0xabc"[-6:])
    e2 = reinicio(19.59, "rs2b")
    assert abs(e2.saldo_min - 7.59) < 1e-9                                      # la línea ya aceptada no bloquea
    e2._cerrado = True
    with open(X.LEDGER, "a") as f:
        f.write(MALAS["suelo_no_numerico"] + "\n")                              # corrupción NUEVA posterior al reseteo: vuelve a bloquear
    assert reinicio(19.59, "rs2c").saldo_min is None


def test_cli_reiniciar_suelo_solo_real_con_wallet_del_ledger_y_cliente_solo_para_consultar(monkeypatch):
    with pytest.raises(SystemExit):
        H.main(["--reiniciar-suelo", "x"])                                      # sin --confirmo-dinero-real
    d = TMP / "cli"
    d.mkdir(exist_ok=True)
    monkeypatch.setattr(H, "DATALOGS", d)
    monkeypatch.setattr(X, "cliente_dedicado", lambda: (_ for _ in ()).throw(AssertionError("sin wallet en el ledger no se crea cliente")))
    with pytest.raises(SystemExit):
        H.main(["--confirmo-dinero-real", "--escalon", "A", "--reiniciar-suelo", "x"])         # sin saldo_inicial en el ledger: no hay wallet
    X.LEDGER = d / "experimento_h47_A_ledger.jsonl"
    X._CACHE = None
    X.LEDGER.write_text(json.dumps({"tipo": "saldo_inicial", "wallet": "0xabc", "valor": 19.59, "real": True,
                                    "ts": "2026-10-19T10:00:00.000+00:00"}) + "\n")
    vistos = {}
    cli = Cli()
    monkeypatch.setattr(X, "cliente_dedicado", lambda: (cli, "0xOTRA"))
    with pytest.raises(SystemExit) as e:
        H.main(["--confirmo-dinero-real", "--escalon", "A", "--reiniciar-suelo", "retiro"])
    assert "no es la del ledger" in str(e.value)                                # cliente de otra wallet: no se hace nada
    del e
    gc.collect()
    monkeypatch.setattr(X, "cliente_dedicado", lambda: (cli, "0xABC"))
    monkeypatch.setattr(H, "reiniciar_suelo", lambda w, m, **k: vistos.update(w=w, m=m, **k) or {"tipo": "suelo_reiniciado"})
    assert H.main(["--confirmo-dinero-real", "--escalon", "A", "--reiniciar-suelo", "retiro", "--segundo-motivo", "otra"]) == 0
    assert vistos == {"w": "0xabc", "m": "retiro", "cli": cli, "motivo2": "otra"}


def test_en_seco_no_hay_suelo_ni_se_lee_saldo():
    X.saldo_onchain = lambda w: (_ for _ in ()).throw(AssertionError("seco: no se lee saldo"))
    H.saldo_con_bloque = lambda w: (_ for _ in ()).throw(AssertionError("seco: no se lee saldo"))
    try:
        ex = nuevo("sd7", real=False, presupuesto=50.0)                         # el tope de 5 solo aplica en real
        assert ex.saldo_min == 0.0 and ex.puede_enviar(2.5)
        primera_orden(ex)
        assert not eventos("suelo_fijado") and not eventos("suelo_calculado")
        ex.vigilar_saldo(time.time())
    finally:
        H.saldo_con_bloque = _bloque_falso
        X.saldo_onchain = lambda w: ONCHAIN["pusd"]


# ---------------------------------------------------------------- 3ª /code-review medium (19-Oct): 10 hallazgos
def sin_exp(monkeypatch):
    """main() sin ledger ni cliente: cualquier intento de construir un Exp47 (arranque real) falla el test."""
    monkeypatch.setattr(H, "configurar_rutas", lambda *a, **k: None)
    monkeypatch.setattr(H, "Exp47", lambda *a, **k: (_ for _ in ()).throw(AssertionError("arrancó un Exp47")))


def test_motivo_vacio_de_las_opciones_de_reseteo_no_arranca_un_real_normal(monkeypatch):
    sin_exp(monkeypatch)
    for flag in ("--reiniciar-suelo", "--aceptar-linea-ilegible", "--rearmar-kill"):
        for motivo in ("", "   "):
            with pytest.raises(SystemExit) as e:
                H.main(["--confirmo-dinero-real", flag, motivo])
            assert "no vacío" in str(e.value), (flag, motivo)           # antes: "" es falsy -> se saltaba la rama y arrancaba el real
    with pytest.raises(SystemExit) as e:
        H.main(["--confirmo-dinero-real", "--reiniciar-suelo", "x", "--aceptar-linea-ilegible", "y"])
    assert "excluyentes" in str(e.value)
    with pytest.raises(SystemExit) as e:
        H.main(["--reiniciar-suelo", "x"])                              # sin --confirmo-dinero-real
    assert "solo con --confirmo-dinero-real" in str(e.value)


def escenario_retirada(nombre, con_reset):
    """Saldo 40 (suelo 28), una orden de 0,9; luego Javi retira 20 pUSD (saldo 20) y reinicia (o no)."""
    X.saldo_onchain = lambda w: 40.0
    (TMP / nombre).mkdir(exist_ok=True)
    ex = nuevo(f"{nombre}/experimento_h47_B_ledger")      # nombre real: el lector compartido busca experimento_h47_*_ledger.jsonl
    X.saldo_onchain = lambda w: ONCHAIN["pusd"]
    ONCHAIN["pusd"] = 40.0
    primera_orden(ex)
    liquidar(ex)
    ONCHAIN["pusd"] = 20.0
    if con_reset:
        assert H.reiniciar_suelo("0xabc", "retiro 20", cli=Cli(), leer=lambda m: "REINICIAR SUELO " + "0xabc"[-6:])
    return reinicio(20.0, nombre + "_2")


def test_reseteo_rebasa_la_base_del_cuadre_y_solo_explican_las_ordenes_posteriores():
    sin = escenario_retirada("rb_a", False)
    assert sin.saldo_inicial == 40.0 and abs(sin.saldo_min - 28.0) < 1e-9
    assert not sin.cuadre(20.0) and sin.kill and "no cuadra" in sin.kill       # sin reseteo la retirada es un kill persistente
    con = escenario_retirada("rb_b", True)
    assert con.saldo_inicial == 20.0 and abs(con.saldo_min - 8.0) < 1e-9 and con.t_reinicio is not None
    assert con.cuadre(20.0) and con.kill is None
    primera_orden(con)
    assert con.cli.posts and con.kill is None                              # opera con normalidad tras el reseteo
    # la orden de ANTES del reseteo (0,9) ya está en el saldo base: no relaja el cuadre. Una salida de 0,5 sin explicar sigue matando.
    con2 = escenario_retirada("rb_c", True)
    assert not con2.cuadre(19.5) and con2.kill and "no cuadra" in con2.kill
    assert con2.cuadre(20.0 + 5.0)                                         # y un ingreso nunca mata


def test_reseteo_exige_saldo_verificable_y_deja_la_base_en_el_evento(monkeypatch):
    (TMP / "rb_d").mkdir(exist_ok=True)
    ex = nuevo("rb_d/experimento_h47_B_ledger")
    ex._cerrado = True
    monkeypatch.setattr(H, "saldo_con_bloque", lambda w: None)
    with pytest.raises(SystemExit) as e:
        H.reiniciar_suelo("0xabc", "retiro", cli=Cli(), leer=lambda m: "REINICIAR SUELO " + "0xabc"[-6:])
    assert "no se puede verificar" in str(e.value) and not eventos("suelo_reiniciado", True)
    monkeypatch.setattr(H, "saldo_con_bloque", _bloque_falso)
    ONCHAIN["pusd"] = 17.25
    ev = H.reiniciar_suelo("0xabc", "retiro", cli=Cli(), leer=lambda m: "REINICIAR SUELO " + "0xabc"[-6:])
    assert ev["saldo_base"] == 17.25 and eventos("suelo_reiniciado", True)[-1]["saldo_base"] == 17.25


def test_cli_reseteo_toma_ademas_el_lock_de_pares(monkeypatch):
    import fcntl
    d = TMP / "cli2"
    d.mkdir(exist_ok=True)
    monkeypatch.setattr(H, "DATALOGS", d)
    monkeypatch.setattr(H, "LOCK_PARES", d / "pares.lock")
    X.LEDGER = d / "experimento_h47_A_ledger.jsonl"
    X._CACHE = None
    X.LEDGER.write_text(json.dumps({"tipo": "saldo_inicial", "wallet": "0xabc", "valor": 19.59, "real": True,
                                    "ts": "2026-10-19T10:00:00.000+00:00"}) + "\n")
    monkeypatch.setattr(X, "cliente_dedicado", lambda: (Cli(), "0xabc"))
    monkeypatch.setattr(H, "reiniciar_suelo", lambda w, m, **k: {"tipo": "suelo_reiniciado"})
    monkeypatch.setattr(H, "aceptar_linea_ilegible", lambda w, m, **k: {"tipo": "linea_ilegible_aceptada"})
    ocupado = open(d / "pares.lock", "w")
    fcntl.flock(ocupado, fcntl.LOCK_EX | fcntl.LOCK_NB)                      # experimento_pares en marcha
    for flag in ("--reiniciar-suelo", "--aceptar-linea-ilegible"):
        with pytest.raises(SystemExit) as e:
            H.main(["--confirmo-dinero-real", "--escalon", "A", flag, "x"])
        assert "pares" in str(e.value), flag
        del e
        gc.collect()                                                            # suelta el lock X.LOCK que tomó el intento fallido
    ocupado.close()
    assert H.main(["--confirmo-dinero-real", "--escalon", "A", "--reiniciar-suelo", "x"]) == 0
    assert H.main(["--confirmo-dinero-real", "--escalon", "A", "--aceptar-linea-ilegible", "x"]) == 0


def test_aceptar_linea_ilegible_conserva_los_suelos_validos_y_solo_acepta_esa_linea():
    d = TMP / "ai"
    d.mkdir(exist_ok=True)
    (d / "experimento_h47_B_ledger.jsonl").write_text(ev_suelo("0xabc", 9.0) + "\n" + MALAS["truncada"] + "\n")
    ex = nuevo("ai/experimento_h47_B_ledger")
    assert ex.saldo_min is None
    ex._cerrado = True
    n0 = len(eventos())
    assert H.aceptar_linea_ilegible("0xabc", "crash", cli=Cli(), leer=lambda m: "no") is None and len(eventos()) == n0
    with pytest.raises(SystemExit):
        H.aceptar_linea_ilegible("0xabc", " ", cli=Cli(), leer=lambda m: "x")
    fs = []
    orig = H._fsync_ledger
    H._fsync_ledger = lambda: fs.append(1)
    try:
        ev = H.aceptar_linea_ilegible("0xabc", "crash", cli=Cli(), leer=lambda m: "ACEPTAR LINEA ILEGIBLE " + "0xabc"[-6:])
    finally:
        H._fsync_ledger = orig
    assert ev and fs == [1] and len(eventos("linea_ilegible_aceptada", True)) == 1 and not eventos("suelo_reiniciado", True)
    e2 = reinicio(19.59, "ai2")
    assert abs(e2.saldo_min - 9.0) < 1e-9                                       # el suelo válido (9,0) SE CONSERVA (el reseteo lo habría perdido)
    assert H.aceptar_linea_ilegible("0xabc", "otra vez", cli=Cli(), leer=lambda m: "x") is None      # nada nuevo que aceptar
    e2._cerrado = True
    with open(X.LEDGER, "a") as f:
        f.write(MALAS["suelo_no_numerico"] + "\n")                              # corrupción NUEVA: vuelve a bloquear
    assert reinicio(19.59, "ai3").saldo_min is None


def test_aceptacion_de_otra_wallet_no_vale():
    d = TMP / "ai_o"
    d.mkdir(exist_ok=True)
    sha = H._sha(MALAS["truncada"])
    (d / "experimento_h47_B_ledger.jsonl").write_text(
        MALAS["truncada"] + "\n" + json.dumps({"tipo": "linea_ilegible_aceptada", "wallet": "0xOTRA", "real": True, "motivo": "x",
                                              "ilegibles_aceptadas": [["experimento_h47_B_ledger.jsonl", sha]],
                                              "ts": "2026-10-19T10:00:00.000+00:00"}) + "\n")
    assert nuevo("ai_o/experimento_h47_B_ledger").saldo_min is None


def test_lectura_de_saldo_en_ejecucion_exige_bloque_reciente_y_no_retrocede(monkeypatch):
    ex = nuevo("ej")
    visto = ex._bloque_visto
    assert visto == ex.bloque_saldo
    cache = lambda: setattr(ex, "_on_cache", (0.0, None))
    monkeypatch.setattr(H, "saldo_con_bloque", lambda w: (19.59, visto - 1 - H.BLOQUE_RETROCESO_TOL, time.time()))       # bloque ANTERIOR al último visto (fuera de tolerancia)
    cache()
    assert ex.saldo() is None and not ex.puede_enviar(1.0)
    assert eventos("lectura_saldo_rechazada")[-1]["motivo"] == "bloque_retrocede"
    monkeypatch.setattr(H, "saldo_con_bloque", lambda w: (19.59, visto + 5, time.time() - 300))  # nodo atrasado: bloque de hace 5 min
    cache()
    assert ex.saldo() is None and not ex.puede_enviar(1.0)
    assert eventos("lectura_saldo_rechazada")[-1]["motivo"] == "bloque_no_reciente"
    primera_orden(ex)
    assert ex.cli.posts == []                                                   # y no se envía nada con esas lecturas
    monkeypatch.setattr(H, "saldo_con_bloque", lambda w: (19.59, visto + 6, time.time()))
    cache()
    assert ex.saldo() == 19.59 and ex.puede_enviar(1.0) and ex._bloque_visto == visto + 6
    monkeypatch.setattr(H, "saldo_con_bloque", lambda w: (19.59, visto + 6, time.time()))       # mismo bloque que el último visto: vale
    cache()
    assert ex.saldo() == 19.59


def test_cuadre_y_vigilar_usan_la_lectura_con_bloque(monkeypatch):
    ex = nuevo("ej2")
    visto = ex._bloque_visto
    monkeypatch.setattr(H, "saldo_con_bloque", lambda w: (1.0, visto - 1 - H.BLOQUE_RETROCESO_TOL, time.time()))         # saldo falso (bajísimo) en un bloque retrocedido
    ex._on_cache = (0.0, None)
    ex.vigilar_saldo(time.time())
    assert ex.kill is None and ex.saldo_ilegible_desde is not None             # no se «cuadra» con él (habría sido un kill): se trata como ilegible


def test_arranque_con_el_mismo_bloque_dos_veces_no_da_suelo(monkeypatch):
    monkeypatch.setattr(H, "saldo_con_bloque", lambda w: (19.59, 777, time.time()))
    ex = nuevo("blq_igual")
    assert ex.saldo_min is None and eventos("suelo_no_fijado", True)


def test_suelo_subido_que_no_llega_a_disco_mata_y_no_cambia_el_estado(monkeypatch):
    ex = nuevo("alza_f")
    primera_orden(ex)
    ONCHAIN["pusd"] = 30.0
    ex._on_cache = (0.0, None)
    assert not ex.puede_enviar(1.0)
    envejecer(ex, 3.0)

    def malo():
        raise OSError("disco")
    monkeypatch.setattr(H, "_fsync_ledger", malo)
    ex._on_cache = (0.0, None)
    assert not ex.puede_enviar(1.0)                                             # antes devolvía True con el suelo ya subido en memoria
    assert ex.kill and "suelo_subido" in ex.kill
    assert abs(ex.saldo_min - 7.59) < 1e-9 and ex.hwm == 19.59 and ex._alza_pend is None


def test_tras_un_alza_confirmada_no_se_gasta_el_exceso_sobre_el_pico(monkeypatch):
    ex = nuevo("alza_p")
    primera_orden(ex)
    for k in range(3):
        ex.vivas[f"v{k}"] = {"tok": "tU", "precio": 0.3, "size": 10.0}
    falta = 11.5 - ex.comprometido()                                            # completa hasta 11,5 $ comprometidos (la 1ª orden ya cuenta)
    ex.vivas["v3"] = {"tok": "tU", "precio": falta / 10.0, "size": 10.0}
    assert abs(ex.comprometido() - 11.5) < 1e-9
    ONCHAIN["pusd"] = 30.0
    ex._on_cache = (0.0, None)
    assert not ex.puede_enviar(0.4)
    envejecer(ex, 3.0)
    ONCHAIN["pusd"] = 31.0                                                      # la 2ª lectura es mayor: el pico confirmado es el MENOR (30)
    ex._on_cache = (0.0, None)
    assert not ex.puede_enviar(1.0)                                             # min(31, 30) − 11,5 − 1 = 17,5 < 18 (con 31 daría 18,5 y pasaría)
    assert ex.hwm == 30.0 and abs(ex.saldo_min - 18.0) < 1e-9
    ONCHAIN["pusd"] = 30.0
    ex._on_cache = (0.0, None)
    assert ex.puede_enviar(0.4)                                                 # 30 − 11,5 − 0,4 = 18,1 >= 18


def test_alza_pendiente_caduca_y_una_lectura_ilegible_la_anula(monkeypatch):
    ex = nuevo("alza_c")
    primera_orden(ex)
    ONCHAIN["pusd"] = 30.0
    ex._on_cache = (0.0, None)
    assert not ex.puede_enviar(1.0)
    envejecer(ex, H.ALZA_CADUCA_S + 1.0)                                        # la confirmación llega demasiado tarde: NO vale
    ex._on_cache = (0.0, None)
    assert not ex.puede_enviar(1.0) and ex.hwm == 19.59 and ex._alza_pend is not None
    assert time.time() - ex._alza_pend[1] < 1.0                                 # empezó otra confirmación desde cero
    envejecer(ex, 3.0)
    ex._on_cache = (0.0, None)
    assert ex.puede_enviar(1.0) and ex.hwm == 30.0                              # y esa sí se confirma
    # lectura ilegible entre medias: anula el alza pendiente
    ex2 = nuevo("alza_c2")
    primera_orden(ex2)
    ONCHAIN["pusd"] = 30.0
    ex2._on_cache = (0.0, None)
    assert not ex2.puede_enviar(1.0)
    envejecer(ex2, 3.0)
    X.saldo_onchain = lambda w: None
    ex2._on_cache = (0.0, None)
    assert not ex2.puede_enviar(1.0) and ex2._alza_pend is None
    X.saldo_onchain = lambda w: ONCHAIN["pusd"]
    ex2._on_cache = (0.0, None)
    assert not ex2.puede_enviar(1.0) and ex2.hwm == 19.59                       # vuelve a empezar: no confirma de inmediato
    # la confirmación debe venir de un bloque MÁS NUEVO que el de la lectura que abrió el alza
    ex3 = nuevo("alza_c3")
    primera_orden(ex3)
    ONCHAIN["pusd"] = 30.0
    ex3._on_cache = (0.0, None)
    assert not ex3.puede_enviar(1.0)
    p = ex3._alza_pend
    ex3._alza_pend = (p[0], p[1] - 3.0, 10 ** 12)
    ex3._on_cache = (0.0, None)
    assert not ex3.puede_enviar(1.0) and ex3.hwm == 19.59


def test_un_solo_escaneo_de_ledgers_por_arranque(monkeypatch):
    import inspect
    n = {"v": 0}
    orig = H.escanear_ledgers_reales

    def contado(w):
        n["v"] += 1
        return orig(w)
    monkeypatch.setattr(H, "escanear_ledgers_reales", contado)
    ex = nuevo("uno")
    assert n["v"] == 1 and ex.saldo_min is not None
    assert inspect.isgeneratorfunction(H._lineas)                              # streaming, no read_bytes del ledger entero


# ---------------------------------------------------------------- 4ª /code-review medium (19-Oct): 3 medios + 4 bajos
RESET = lambda **k: H.reiniciar_suelo("0xabc", "retiro", leer=lambda m: "REINICIAR SUELO " + "0xabc"[-6:], **k)
ACEPTA = lambda **k: H.aceptar_linea_ilegible("0xabc", "crash", leer=lambda m: "ACEPTAR LINEA ILEGIBLE " + "0xabc"[-6:], **k)


def sin_efecto(fn, **k):
    """La operación se niega (SystemExit) y no deja NINGÚN evento nuevo en el ledger."""
    n0 = len(X.LEDGER.read_text().splitlines())
    with pytest.raises(SystemExit) as e:
        fn(**k)
    assert len(X.LEDGER.read_text().splitlines()) == n0
    return str(e.value)


@pytest.mark.parametrize("op", [RESET, ACEPTA], ids=["reiniciar", "aceptar"])
def test_precondiciones_comunes_de_reseteo_y_aceptacion(op, monkeypatch):
    """M1/M2: kill pendiente, orden sin cerrar en ledger, orden viva en el exchange, sin cliente o saldo sin verificar -> no hace nada."""
    d = TMP / f"pre_{id(op)}"
    d.mkdir(exist_ok=True)
    (d / "experimento_h47_B_ledger.jsonl").write_text(MALAS["truncada"] + "\n")           # hay algo que aceptar/reiniciar
    ex = nuevo(f"pre_{id(op)}/experimento_h47_B_ledger", n_max=None)
    ex._cerrado = True
    X.saldo_onchain = lambda w: ONCHAIN["pusd"]
    ex.saldo_min = 7.59                                                         # (sin suelo por la línea cortada: se fuerza para poder enviar)
    ex.hwm = 19.59
    primera_orden(ex)
    assert ex.cli.posts                                                         # hay una orden SIN cerrar en el ledger
    assert "sin cerrar" in sin_efecto(op, cli=Cli())
    liquidar(ex)
    viva = Cli()
    viva.ordenes["0xv"] = {"size_matched": 0.0, "status": "LIVE"}
    assert "viva" in sin_efecto(op, cli=viva)                                   # viva en el exchange
    assert "sin cliente" in sin_efecto(op, cli=None)

    class Roto(Cli):
        def get_open_orders(self, *a, **k):
            raise RuntimeError("500")
    assert "fail-closed" in sin_efecto(op, cli=Roto())
    monkeypatch.setattr(H, "saldo_con_bloque", lambda w: None)
    assert "verificar el saldo" in sin_efecto(op, cli=Cli())                    # saldo no verificable
    monkeypatch.setattr(H, "saldo_con_bloque", _bloque_falso)
    X.KILL_FICHERO.write_text("dinero que no cuadra: salieron 3 pUSD")
    assert "kill pendiente" in sin_efecto(op, cli=Cli())                        # kill (incl. dinero_no_cuadra) pendiente: hay que investigar
    X.KILL_FICHERO.unlink()
    (d / "experimento_pares_dedicada.KILL").write_text("x")
    assert "experimento_pares_dedicada.KILL" in sin_efecto(op, cli=Cli())      # y el kill de pares
    (d / "experimento_pares_dedicada.KILL").unlink()
    with open(X.LEDGER, "a") as f:
        f.write(json.dumps({"tipo": "kill", "motivo": "dinero que no cuadra: x", "real": True, "ts": "2026-10-19T10:00:00.000+00:00"}) + "\n")
    X._CACHE = None
    assert "kill pendiente" in sin_efecto(op, cli=Cli())                        # kill en el ledger sin kill_rearmado
    with open(X.LEDGER, "a") as f:
        f.write(json.dumps({"tipo": "kill_rearmado", "motivo": "visto", "real": True, "ts": "2026-10-19T10:00:01.000+00:00"}) + "\n")
    X._CACHE = None
    assert op(cli=Cli())                                                        # todo limpio: ahora sí


def test_ordenes_abiertas_en_ledgers_hermanos_bloquean(monkeypatch):
    d = TMP / "pre_h"
    d.mkdir(exist_ok=True)
    (d / "experimento_h47_A_ledger.jsonl").write_text(json.dumps({"tipo": "intencion_post", "oid": "a1", "real": True, "slug": "eth-updown-5m-1",
                                                                   "lado": "YES", "precio": 0.2, "size": 5, "tok": "t",
                                                                   "ts": "2026-10-19T10:00:00.000+00:00"}) + "\n")
    (d / "experimento_h47_B_ledger.jsonl").write_text("")
    ex = nuevo("pre_h/experimento_h47_B_ledger")
    ex._cerrado = True
    assert H.ordenes_abiertas_en_ledgers() == 1
    assert "sin cerrar" in sin_efecto(RESET, cli=Cli())


def test_aceptar_solo_lineas_que_parecen_json_cortado_y_guarda_la_cruda():
    import base64
    d = TMP / "ai2"
    d.mkdir(exist_ok=True)
    corta = '{"tipo": "suelo_fijado", "wallet": "0xabc", "su'
    (d / "experimento_h47_B_ledger.jsonl").write_text(ev_suelo("0xabc", 9.0) + "\n" + corta + "\n" + ev_suelo("0xabc", 10.0) + "\n")
    ex = nuevo("ai2/experimento_h47_B_ledger")
    ex._cerrado = True
    ev = ACEPTA(cli=Cli())                                                      # cortada EN MEDIO (el harness la cierra con «\n» y sigue)
    assert ev and ev["saldo_verificado"] == 19.59 and ev["bloque"]
    sha = H._sha(corta)
    assert [tuple(x) for x in ev["ilegibles_aceptadas"]] == [("experimento_h47_B_ledger.jsonl", sha)]
    guardado = eventos("linea_ilegible_aceptada", True)[-1]["lineas_crudas"][sha]
    assert guardado["fichero"] == "experimento_h47_B_ledger.jsonl" and base64.b64decode(guardado["base64"]).decode() == corta
    # NO cortadas: basura binaria o JSON completo pero inválido -> no se acepta ninguna (ni la cortada que hubiera)
    for i, mala in enumerate(("\x00\x01{{{", '{"tipo": "suelo_fijado", "suelo": }', "esto no es json", '{"tipo": "su\x00elo"')):
        dd = TMP / f"ai3_{i}"
        dd.mkdir(exist_ok=True)
        (dd / "experimento_h47_B_ledger.jsonl").write_text(corta + "\n" + mala + "\n" + ev_suelo("0xabc", 4.0) + "\n")
        e2 = nuevo(f"ai3_{i}/experimento_h47_B_ledger")
        e2._cerrado = True
        assert "NO parecen un JSON cortado" in sin_efecto(ACEPTA, cli=Cli()), mala
    assert H.parece_truncada(corta) and H.parece_truncada("{") and not H.parece_truncada("[1, 2")
    assert not H.parece_truncada('{"a": 1}') and not H.parece_truncada("{\x00") and not H.parece_truncada("{\ufffd")


def test_reseteos_tercero_y_siguientes_exigen_segundo_motivo_y_confirmacion_reforzada():
    (TMP / "cnt").mkdir(exist_ok=True)
    ex = nuevo("cnt/experimento_h47_B_ledger")
    ex._cerrado = True
    for k in (1, 2):
        ev = RESET(cli=Cli())
        assert ev and ev["n_reinicio"] == k and "motivo2" not in ev
    assert "segundo-motivo" in sin_efecto(RESET, cli=Cli())                    # 3º: sin segundo motivo (o en blanco)
    assert "segundo-motivo" in sin_efecto(RESET, cli=Cli(), motivo2="  ")
    n0 = len(eventos())
    assert H.reiniciar_suelo("0xabc", "retiro", cli=Cli(), motivo2="de verdad",
                             leer=lambda m: "REINICIAR SUELO " + "0xabc"[-6:]) is None and len(eventos()) == n0   # confirmación NORMAL no vale
    ev = H.reiniciar_suelo("0xabc", "retiro", cli=Cli(), motivo2="de verdad", leer=lambda m: "REINICIAR SUELO " + "0xabc"[-6:] + " VEZ 3")
    assert ev["n_reinicio"] == 3 and ev["motivo2"] == "de verdad" and eventos("suelo_reiniciado", True)[-1]["motivo2"] == "de verdad"
    assert len(eventos("suelo_reiniciado", True)) == 3


def test_base_del_cuadre_tras_reseteo_vale_tambien_para_el_harness_de_pares(tmp_path):
    """M3: experimento_pares_dedicada (misma wallet) cuadra contra el MISMO saldo base, sin tocar la lógica de H47."""
    d = tmp_path / "m3"
    d.mkdir()
    X.LEDGER = d / "experimento_pares_dedicada_ledger.jsonl"
    X.KILL_FICHERO = d / "pares.KILL"
    X.LOCK = d / "pares.lock"
    X._CACHE = None
    X.cliente_dedicado = lambda: (Cli(), "0xabc")
    ONCHAIN["pusd"] = 19.59
    reset = lambda base, ts, w="0xabc", extra=None: json.dumps(dict({"tipo": "suelo_reiniciado", "wallet": w, "saldo_base": base, "real": True, "ts": ts},
                                                                    **(extra or {})))
    (d / "experimento_h47_A_ledger.jsonl").write_text("\n".join([
        reset(11.0, "2026-10-19T09:00:00.000+00:00"),                           # antiguo
        reset(12.5, "2026-10-19T10:00:00.000+00:00"),                           # el último válido
        reset(99.0, "2026-10-19T11:00:00.000+00:00", w="0xOTRA"),               # otra wallet
        reset("x", "2026-10-19T12:00:00.000+00:00"),                            # base no válida
        reset(-3.0, "2026-10-19T12:30:00.000+00:00"),
        reset(7.0, "2026-10-19T13:00:00.000"),                                  # ts sin zona
        json.dumps({"tipo": "suelo_reiniciado", "wallet": "0xabc", "saldo_base": 5.0, "real": False, "ts": "2026-10-19T14:00:00.000+00:00"}),
        "basura {suelo_reiniciado",
    ]) + "\n")
    (d / "experimento_h47_seco_B_ledger.jsonl").write_text(reset(1.0, "2026-10-19T15:00:00.000+00:00") + "\n")      # seco: no cuenta
    import reinicio_suelo_compartido as R
    ep, base = R.ultimo_reinicio(d, "0xABC")
    from datetime import datetime
    assert base == 12.5 and ep == datetime.fromisoformat("2026-10-19T10:00:00.000+00:00").timestamp()       # el más reciente VÁLIDO de la wallet
    assert R.ultimo_reinicio(d, "0xzzz") is None and R.ultimo_reinicio(d / "no_existe", "0xabc") is None
    ex = X.Exp(True)
    CREADOS.append(ex)
    ex._cerrado = True
    assert ex.saldo_inicial == 12.5 and ex.t_reinicio == ep                      # el harness (pares) parte de la base rebasada
    # órdenes ANTERIORES al reseteo no explican salidas posteriores
    ex.ordenes = lambda: C.plegar([{"tipo": "intencion_post", "oid": "p1", "real": True, "slug": "btc-updown-15m-1", "lado": "YES", "tok": "t",
                                    "precio": 0.5, "size": 100, "ts": "2026-10-19T09:30:00.000+00:00"}])
    ONCHAIN["pusd"] = 12.0
    ex._on_cache = (0.0, None)
    assert ex.capital_fuera({"size": 5, "precio": 0.2}) is None and ex.kill and "no cuadra" in ex.kill
    # sin reseteo: la base es el primer saldo y la orden antigua sí explica
    d2 = tmp_path / "m3b"
    d2.mkdir()
    X.LEDGER = d2 / "experimento_pares_dedicada_ledger.jsonl"
    X.KILL_FICHERO = d2 / "pares.KILL"
    X.LOCK = d2 / "pares.lock"
    X._CACHE = None
    ONCHAIN["pusd"] = 19.59
    ex2 = X.Exp(True)
    CREADOS.append(ex2)
    ex2._cerrado = True
    assert ex2.saldo_inicial == 19.59 and ex2.t_reinicio is None


def test_suelo_reiniciado_formato_antiguo_sin_saldo_base_tiene_recuperacion_explicita():
    d = TMP / "leg"
    d.mkdir(exist_ok=True)
    (d / "experimento_h47_A_ledger.jsonl").write_text(json.dumps({"tipo": "suelo_reiniciado", "wallet": "0xabc", "motivo": "viejo", "real": True,
                                                                   "ts": "2026-10-19T10:00:00.000+00:00"}) + "\n")
    ex = nuevo("leg/experimento_h47_B_ledger")
    ex._cerrado = True
    assert ex.saldo_min is None
    assert "formato antiguo" in eventos("suelo_no_fijado", True)[-1]["motivo"] and "--reiniciar-suelo" in eventos("suelo_no_fijado", True)[-1]["motivo"]
    ev = RESET(cli=Cli())                                                       # la recuperación no es circular: el reseteo nuevo lo supera...
    assert ev and ev["n_reinicio"] == 1                                         # ...y el antiguo no cuenta para el máximo de reseteos
    e2 = reinicio(19.59, "leg2")
    assert abs(e2.saldo_min - 7.59) < 1e-9                                      # ya se opera


def test_retroceso_de_bloque_con_tolerancia_sin_bajar_el_maximo_visto(monkeypatch):
    ex = nuevo("tol")
    visto = ex._bloque_visto
    T = H.BLOQUE_RETROCESO_TOL
    assert T == 3
    cache = lambda: setattr(ex, "_on_cache", (0.0, None))
    monkeypatch.setattr(H, "saldo_con_bloque", lambda w: (19.59, visto - T, time.time()))     # justo en la tolerancia: vale
    cache()
    assert ex.saldo() == 19.59 and ex._bloque_visto == visto                  # y el máximo visto NO baja
    monkeypatch.setattr(H, "saldo_con_bloque", lambda w: (19.59, visto - T - 1, time.time()))
    cache()
    assert ex.saldo() is None and eventos("lectura_saldo_rechazada")[-1]["motivo"] == "bloque_retrocede"
    assert H.lectura_valida((1.0, 100, 1000.0), 1000.0, 103) == (True, None)
    assert H.lectura_valida((1.0, 99, 1000.0), 1000.0, 103) == (False, "bloque_retrocede")


def test_suelo_subido_registra_el_bloque_de_la_lectura_que_confirma_el_alza():
    ex = nuevo("bloq_alza")
    primera_orden(ex)
    ONCHAIN["pusd"] = 30.0
    ex._on_cache = (0.0, None)
    assert not ex.puede_enviar(1.0)
    envejecer(ex, 3.0)
    ex._on_cache = (0.0, None)
    assert ex.puede_enviar(1.0)
    su = eventos("suelo_subido", True)[-1]
    assert su["bloque"] == ex._bloque_lectura and su["bloque"] != ex.bloque_saldo and su["bloque"] > ex.bloque_saldo


def test_reseteo_toma_los_locks_en_el_mismo_orden_que_el_arranque(monkeypatch):
    import fcntl
    d = TMP / "cli4"
    d.mkdir(exist_ok=True)
    monkeypatch.setattr(H, "DATALOGS", d)
    monkeypatch.setattr(H, "LOCK_PARES", d / "pares.lock")
    X.LEDGER = d / "experimento_h47_A_ledger.jsonl"
    X._CACHE = None
    X.LEDGER.write_text(json.dumps({"tipo": "saldo_inicial", "wallet": "0xabc", "valor": 19.59, "real": True,
                                    "ts": "2026-10-19T10:00:00.000+00:00"}) + "\n")
    monkeypatch.setattr(X, "cliente_dedicado", lambda: (Cli(), "0xabc"))
    monkeypatch.setattr(H, "reiniciar_suelo", lambda w, m, **k: {"tipo": "suelo_reiniciado"})
    orden = []
    real_flock = fcntl.flock
    monkeypatch.setattr(fcntl, "flock", lambda fd, op: (orden.append(Path(fd.name).name), real_flock(fd, op))[1])
    assert H.main(["--confirmo-dinero-real", "--escalon", "A", "--reiniciar-suelo", "x"]) == 0
    assert orden == ["pares.lock", "experimento_h47.lock"]                    # pares primero, luego el de H47 (como main -> tomar_lock_pares -> Exp)


def _preparar_rotacion(nombre, saldo_inicio=40.0):
    (TMP / nombre).mkdir(exist_ok=True)
    ex = nuevo(f"{nombre}/experimento_h47_B_ledger")
    ONCHAIN["pusd"] = saldo_inicio
    ex._cerrado = True
    e = reinicio(saldo_inicio, nombre + "b")
    primera_orden(e)                                    # fija el suelo (saldo_inicio − presupuesto de los tests)
    liquidar(e)
    return e


@pytest.fixture
def ledger_explica_el_gasto(monkeypatch):
    """El gasto de la tanda (saldo bajo el suelo) se da por explicado por el ledger; el test del cuadre lo desactiva."""
    monkeypatch.setattr(H.C, "exposicion_maxima", lambda ords: 999.0)


def test_rotar_tanda_rechaza_si_la_tanda_no_esta_agotada(ledger_explica_el_gasto):
    _preparar_rotacion("rt1")
    ONCHAIN["pusd"] = 40.0                              # mucho margen sobre el suelo: tanda viva
    n0 = len(eventos("suelo_reiniciado", True))
    with pytest.raises(SystemExit, match="NO está agotada"):
        H.rotar_tanda("0xabc", cli=Cli())
    assert len(eventos("suelo_reiniciado", True)) == n0


def test_rotar_tanda_rota_si_agotada_y_deja_evento_auditado_con_fsync(ledger_explica_el_gasto):
    e = _preparar_rotacion("rt2")
    suelo = e.saldo_min
    ONCHAIN["pusd"] = suelo + 0.4                       # agotada: saldo − suelo < 1,5
    assert ONCHAIN["pusd"] >= H.ROTACION_SALDO_DURO + H.PRESUPUESTO_UTIL
    fs = []
    orig = H._fsync_ledger
    H._fsync_ledger = lambda: fs.append(1)
    try:
        ev = H.rotar_tanda("0xabc", cli=Cli())
    finally:
        H._fsync_ledger = orig
    assert ev and fs == [1]
    ult = eventos("suelo_reiniciado", True)[-1]
    assert ult["origen"] == "rotar_tanda" and abs(ult["saldo_base"] - (suelo + 0.4)) < 1e-6 and ult["rotacion_n_24h"] == 1
    assert suelo in ult["suelos_descartados"] and "n_reinicio" not in ult
    e2 = reinicio(suelo + 0.4, "rt2c")                  # tras rotar, la tanda siguiente parte del saldo nuevo
    assert abs(e2.saldo_min - (suelo + 0.4 - H.PRESUPUESTO_UTIL)) < 1e-6


def test_rotar_tanda_no_rota_por_debajo_del_suelo_duro(ledger_explica_el_gasto):
    _preparar_rotacion("rt3", saldo_inicio=40.0)
    ONCHAIN["pusd"] = H.ROTACION_SALDO_DURO + H.PRESUPUESTO_UTIL - 0.5
    n0 = len(eventos("suelo_reiniciado", True))
    with pytest.raises(SystemExit):
        H.rotar_tanda("0xabc", cli=Cli())
    assert len(eventos("suelo_reiniciado", True)) == n0


def test_rotar_tanda_respeta_el_tope_en_24h_movil(monkeypatch, ledger_explica_el_gasto):
    e = _preparar_rotacion("rt4", saldo_inicio=80.0)
    ONCHAIN["pusd"] = e.saldo_min + 0.3
    monkeypatch.setattr(H, "ROTACION_MAX_DIA", 1)
    assert H.rotar_tanda("0xabc", cli=Cli())
    e2 = reinicio(ONCHAIN["pusd"], "rt4c")
    primera_orden(e2)
    liquidar(e2)
    ONCHAIN["pusd"] = e2.saldo_min + 0.3
    n0 = len(eventos("suelo_reiniciado", True))
    with pytest.raises(SystemExit, match="rotaciones en 24 h"):
        H.rotar_tanda("0xabc", cli=Cli())
    assert len(eventos("suelo_reiniciado", True)) == n0


def test_rotar_tanda_sin_cliente_o_con_orden_viva_es_fail_closed(ledger_explica_el_gasto):
    e = _preparar_rotacion("rt5")
    ONCHAIN["pusd"] = e.saldo_min + 0.3
    with pytest.raises(SystemExit):
        H.rotar_tanda("0xabc", cli=None)               # sin cliente no se pueden comprobar las órdenes del exchange
    c = Cli()
    c.get_open_orders = lambda *a, **k: [{"id": "x"}]
    with pytest.raises(SystemExit, match="viva"):
        H.rotar_tanda("0xabc", cli=c)


def test_rotar_tanda_no_rota_si_el_dinero_no_cuadra():
    """Review 20-Oct #2: una bajada de saldo que el ledger NO explica no es «tanda agotada»; no se rebasea."""
    e = _preparar_rotacion("rt6", saldo_inicio=80.0)
    # base del cuadre explícita (un reseteo auditado con saldo_base = 80) para que el test no dependa del saldo_inicial histórico del ledger
    from datetime import datetime, timezone
    with open(X.LEDGER, "a") as f:
        f.write(json.dumps({"tipo": "suelo_reiniciado", "wallet": "0xabc", "saldo_base": 80.0, "suelo": 0.0, "real": True,
                            "ts": datetime.now(timezone.utc).isoformat(timespec="milliseconds")}) + "\n")
    time.sleep(0.02)
    e = reinicio(80.0, "rt6c")
    primera_orden(e)
    liquidar(e)
    ONCHAIN["pusd"] = e.saldo_min - 8.0                 # sale de la wallet mucho más de lo que las órdenes del ledger pueden explicar
    n0 = len(eventos("suelo_reiniciado", True))
    with pytest.raises(SystemExit, match="no cuadra"):
        H.rotar_tanda("0xabc", cli=Cli())
    assert len(eventos("suelo_reiniciado", True)) == n0


def test_rotar_tanda_no_acepta_lineas_ilegibles(ledger_explica_el_gasto):
    """Review 20-Oct #1: una línea defectuosa en un ledger real bloquea la rotación (la ve un humano), nunca se da por vista."""
    e = _preparar_rotacion("rt7")
    ONCHAIN["pusd"] = e.saldo_min + 0.3
    with open(X.LEDGER, "a") as f:
        f.write('{"tipo": "suelo_fijado", "wallet": "0xabc", "suelo": 12.\n')           # JSON cortado
    n0 = len(eventos("suelo_reiniciado", True))
    with pytest.raises(SystemExit, match="ilegible|corrupta"):
        H.rotar_tanda("0xabc", cli=Cli())
    assert len(eventos("suelo_reiniciado", True)) == n0


def test_rotaciones_automaticas_no_consumen_el_tope_de_reseteos_manuales(ledger_explica_el_gasto):
    """Review 20-Oct #4: n_reinicios cuenta todo, pero REINICIOS_MAX solo mira los manuales (n_rotaciones se descuenta)."""
    e = _preparar_rotacion("rt8", saldo_inicio=80.0)
    ONCHAIN["pusd"] = e.saldo_min + 0.3
    assert H.rotar_tanda("0xabc", cli=Cli())
    r = H.escanear_ledgers_reales("0xabc")
    assert r["n_reinicios"] == 1 and r["n_rotaciones"] == 1
