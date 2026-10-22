#!/usr/bin/env python3
"""Pruebas de r3_regla / r3_shadow / r3_desenlaces / r3_vigia: SIN red, SIN dinero, SIN claves; tiempo controlado (nada duerme).
Uso: /root/polymarket-research/.venv/bin/python -m pytest -q experimentos/5m_barato/b_seleccion_adversa/r3_shadow/test_r3_shadow.py
Cubren: gemelo identico a B (reglas y constantes y sim_uno), bordes de R2/R3 (0,03 en milesimas, 26 acc, hora 4), fail-closed (sin bid15, 15m cruzado, WS viejo,
ventana incompleta), ciclo de puja (post/repega/asentado/stop), relleno que atraviesa, parcial a la cola, un relleno cierra la puja, reconexion (huecos),
idempotencia de claves, reinicio desde el log (incluido gzip truncado), mensajes duplicados/desordenados y seguridad (sin simbolos de ordenes/claves)."""
import gzip
import json
import random
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import pytest

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import r3_regla as R  # noqa: E402
import r3_shadow as S  # noqa: E402

INI = int(datetime(2026, 10, 23, 12, 0, 0, tzinfo=timezone.utc).timestamp())        # hora UTC 12 (>= 4), multiplo de 300
INI_NOCHE = int(datetime(2026, 10, 23, 2, 0, 0, tzinfo=timezone.utc).timestamp())    # hora UTC 2 (< 4)
UP, DN, U15, D15 = "tU", "tD", "tU15", "tD15"


def mk(coin="eth", ini=INI, t_ms=None):
    nuc_rows = []
    nuc = R.Nucleo(nuc_rows.append)
    mk5 = {"slug": f"{coin}-updown-5m-{ini}", "id": "5", "up": UP, "down": DN}
    mk15 = {"slug": f"{coin}-updown-15m-{ini // 900 * 900}", "id": "15", "up": U15, "down": D15}
    m = nuc.nuevo(coin, ini, mk5, mk15, int((ini - 20) * 1000) if t_ms is None else t_ms)
    return nuc, m, nuc_rows


def book(tok, bids, asks):
    return {"event_type": "book", "asset_id": tok, "bids": [{"price": str(p), "size": str(s)} for p, s in bids], "asks": [{"price": str(p), "size": str(s)} for p, s in asks]}


def pc(tok, price, size, side):
    return {"event_type": "price_change", "price_changes": [{"asset_id": tok, "price": str(price), "size": str(size), "side": side}]}


def trade(tok, price, size, side, ts=None):
    d = {"event_type": "last_trade_price", "asset_id": tok, "price": str(price), "size": str(size), "side": side}
    if ts is not None:
        d["timestamp"] = str(int(ts * 1000))
    return d


def libros(m, t, bid5=0.20, ask5=0.22, bid15=0.22, ask15=0.24):
    """Snapshots de los 4 tokens: 5m YES con top (bid5, ask5), NO su complemento; 15m YES con (bid15, ask15)."""
    m.on_msg(book(UP, [(bid5, 50), (round(bid5 - 0.01, 2), 80)], [(ask5, 40)]), t)
    m.on_msg(book(DN, [(round(1 - ask5, 2), 40)], [(round(1 - bid5, 2), 50)]), t)
    m.on_msg(book(U15, [(bid15, 100)], [(ask15, 100)]), t)
    m.on_msg(book(D15, [(round(1 - ask15, 2), 100)], [(round(1 - bid15, 2), 100)]), t)


def correr(nuc, m, t0, t1, paso=0.1, hasta=None):
    t = t0
    while t <= t1 + 1e-9:
        m.vivo(t)
        nuc.tick(t)
        t = round(t + paso, 6)
    return t


def tr(m, pol, esc="cons_x"):
    return next(x for x in m.traders if x.pol == pol and x.esc == esc)


def filas(rows, tipo=None, **kw):
    return [r for r in rows if (tipo is None or r["tipo"] == tipo) and all(r.get(k) == v for k, v in kw.items())]


def llenar_vol(m, t, total=30.0, n=3):
    for i in range(n):
        m.on_msg(trade(UP, 0.21, total / n, "BUY", ts=t + 0.001 * i), t + 0.001 * i)


def preparar_vol(m, t_ini):
    """Libros conectados 20 s antes de abrir y 30 acc casadas en el 5m justo tras la apertura (antes de abrir no hay operaciones)."""
    libros(m, INI - 20)
    llenar_vol(m, INI + 1)


# ---------------------------------------------------------------- gemelo identico a B (si el modulo de B cambia, esto falla)
def _importar_b():
    sys.path.insert(0, "/root/polymarket-research-dev")
    sys.path.insert(0, "/root/polymarket-research")
    try:
        import experimento_maker_h47 as H
        import experimento_pares_cola_15m as X
        return H, X
    except Exception as e:                      # pragma: no cover
        pytest.skip(f"B no importable: {e}")


def test_gemelo_identico_a_b():
    H, X = _importar_b()
    for b in [i / 1000 for i in range(80, 340)] + [0.105, 0.2049, 0.3]:
        for a in (b + 0.001, b + 0.01, b + 0.02, b + 0.15, b - 0.01, b):
            assert R.en_banda(b, a) == H.en_banda(b, a), (b, a)
            for k in (1, 2):
                assert R.objetivo_h35(b, a, k) == H.objetivo_h35(b, a, k), (b, a, k)
        assert R.en_rejilla(b) == H.en_rejilla(b)
    for p in [i / 100 for i in range(1, 100)]:
        for sb in (4, 5, 7, 10, 11):
            assert R.tamano_orden(p, sb, 1.0) == H.tamano_orden(p, sb, 1.0)
            assert R.tamano_orden(p, sb, 0.0) == H.tamano_orden(p, sb, 0.0)
    assert R.K_POR_MONEDA == H.K_POR_MONEDA and R.T_STOP == H.T_STOP_DEF and R.T_INI == H.T_INI
    assert R.LAT_POST_S == X.LAT_POST_S and R.LAT_CANCEL_S == X.LAT_CANCEL_S and R.WS_MAX_S == X.WS_MAX_S
    tb = sys.modules.get("test_experimento_maker_h47")           # si el test de B se importo en la misma sesion, acorto ASENTAR_* para sus pruebas: se compara con el valor ORIGINAL
    asentar = getattr(tb, "DEF_ASENTAR", H.ASENTAR_H47_S)
    asentar_min = getattr(tb, "DEF_ASENTAR_MIN", H.ASENTAR_MIN_REAL_S)
    assert R.ASENTAR_S == asentar == asentar_min, "B asienta una cancelacion en ASENTAR_H47_S"
    assert R.POLL_S == H.POLL_S and R.MIN_ENTRE_ACCIONES_S == H.MIN_ENTRE_ACCIONES_S and R.REQUOTE_INVALIDO_S == H.REQUOTE_INVALIDO_S
    assert (R.SIZE_MIN, R.SIZE_MAX) == (H.SIZE_MIN, H.SIZE_MAX)


def test_sim_orden_igual_que_sim_uno_de_b_en_flujos_aleatorios():
    H, X = _importar_b()
    rnd = random.Random(7)
    par = {"tU": "tD", "tD": "tU"}
    for _ in range(200):
        lib = R.Libro(["tU", "tD"])
        t0 = 1000.0
        q = round(rnd.choice([0.15, 0.2, 0.25]), 2)
        cola = rnd.choice([0.0, 10.0, 30.0])
        for i in range(rnd.randint(0, 12)):
            tk = rnd.choice(["tU", "tD"])
            p = round(rnd.choice([0.14, 0.15, 0.19, 0.2, 0.21, 0.8, 0.81, 0.85]), 2)
            tx = t0 + rnd.uniform(-0.1, 2.0)
            lib.trades[tk].append((tx, tx, p, float(rnd.randint(1, 20)), rnd.choice(["BUY", "SELL"])))
            lib.trades_r[tk].append(tx)
        for tk in lib.trades:                                   # recepcion monotona (como en vivo)
            lib.trades[tk].sort(); lib.trades_r[tk] = [x[0] for x in lib.trades[tk]]
        o1 = {"tok": "tU", "precio": q, "size": 5.0, "t_post": t0, "cola": cola}
        o2 = dict(o1)
        if rnd.random() < 0.5:
            o1["t_cancel"] = o2["t_cancel"] = t0 + rnd.uniform(0.0, 1.5)
        f1 = H.sim_uno(lib, par, o1, 0.0)
        f2 = R.sim_orden(lib, par, o2, 0.0, "x")
        assert abs(f1 - f2) < 1e-9


# ---------------------------------------------------------------- regla R2 / R3 en bordes
def F(**kw):
    f = {"fresco": True, "b15m": 330, "cruzado15": False, "objm": 300, "vol30": 30.0, "hora": 12}
    f.update(kw)
    return f


def test_r2_borde_en_milesimas():
    assert R.regla("R2", F(b15m=330, objm=300)) == (True, None)           # 0,03 exacto: pasa
    assert R.regla("R2", F(b15m=331, objm=300)) == (False, "r2_nivel15")
    assert R.regla("R2", F(b15m=250, objm=300))[0]                       # 15m por debajo de la puja: pasa
    assert R.regla("R2", F(b15m=360, objm=330))[0]                       # 0.36-0.33 en float seria 0.0299999 o 0.0300001: con enteros es exacto


def test_r2_fail_closed():
    assert R.regla("R2", F(b15m=None)) == (False, "sin_b15")
    assert R.regla("R2", F(cruzado15=True)) == (False, "b15_cruzado")
    assert R.regla("R2", F(fresco=False)) == (False, "ws_viejo")
    assert R.regla("BASE", F(b15m=None, fresco=False))[0]                  # BASE nunca depende de la regla


def test_r3_bordes():
    assert R.regla("R3", F(vol30=26.0))[0] and R.regla("R3", F(vol30=25.99)) == (False, "r3_vol30")
    assert R.regla("R3", F(hora=4))[0] and R.regla("R3", F(hora=3)) == (False, "r3_hora")
    assert R.regla("R3", F(vol30=None)) == (False, "vol30_sin_ventana")
    assert R.regla("R3", F(b15m=400)) == (False, "r2_nivel15")             # R3 incluye R2


# ---------------------------------------------------------------- ciclo de pujas
def test_base_cotiza_y_r2_r3_segun_regla():
    nuc, m, rows = mk("eth")
    preparar_vol(m, INI)
    libros(m, INI + 3, bid5=0.20, ask5=0.22, bid15=0.22)            # objetivo ETH k=2 -> 0,18; bid15-obj = 4c > 3c -> R2 no
    correr(nuc, m, INI + 3, INI + 4)
    assert tr(m, "BASE").orden and tr(m, "BASE").orden["precio"] == 0.18
    assert tr(m, "R2").orden is None and tr(m, "R3").orden is None
    assert any(r["motivo"] == "r2_nivel15" for r in filas(rows, "dec", pol="R3", acc="no_cotiza"))
    libros(m, INI + 5, bid5=0.20, ask5=0.22, bid15=0.21)            # 3c -> R2 y R3 (vol30 30 >= 26, hora 12)
    correr(nuc, m, INI + 5, INI + 6.2)
    assert tr(m, "R2").orden["precio"] == 0.18 and tr(m, "R3").orden["precio"] == 0.18
    p = filas(rows, "dec", pol="R3", esc="cons_x", acc="post")[0]
    assert p["b15"] == 0.21 and p["lvl15m"] == 30 and p["vol30"] == 30.0 and p["hora"] == 12 and p["r3"] is True


def test_r3_sin_volumen_ni_hora_no_cotiza_pero_r2_si():
    nuc, m, rows = mk("sol")                                       # SOL k=1: top 0,20 -> objetivo 0,19
    libros(m, INI - 20, bid5=0.20, ask5=0.22, bid15=0.21)
    llenar_vol(m, INI + 2, total=20.0)                            # 20 < 26
    correr(nuc, m, INI + 3, INI + 4)
    assert tr(m, "R2").orden and tr(m, "BASE").orden and tr(m, "R3").orden is None
    assert filas(rows, "dec", pol="R3", acc="no_cotiza")[-1]["motivo"] == "r3_vol30"
    nuc2, m2, rows2 = mk("sol", ini=INI_NOCHE)
    libros(m2, INI_NOCHE - 20, bid5=0.20, ask5=0.22, bid15=0.21)
    llenar_vol(m2, INI_NOCHE + 2, total=40.0)
    correr(nuc2, m2, INI_NOCHE + 3, INI_NOCHE + 4)
    assert tr(m2, "R2").orden and tr(m2, "R3").orden is None
    assert filas(rows2, "dec", pol="R3", acc="no_cotiza")[-1]["motivo"] == "r3_hora"


def test_ventana_vol30_incompleta_si_el_libro_se_conecta_tarde():
    nuc, m, rows = mk("xrp", t_ms=int((INI + 60) * 1000))
    libros(m, INI + 60, bid5=0.20, ask5=0.22, bid15=0.21)           # conectado a ini+60: ventana (ini+40...) empieza antes de la conexion
    assert m.vol30(INI + 70) is None                                # t_conexion=ini+60 > max(now-30, ini)=ini+40
    assert m.vol30(INI + 95) == 0.0                                 # ya hay 30 s completos
    assert m.arranque_tarde is True


def test_sin_bid15_o_15m_cruzado_no_cotiza_r2():
    nuc, m, rows = mk("eth")
    m.on_msg(book(UP, [(0.20, 50)], [(0.22, 40)]), INI - 20)
    m.on_msg(book(DN, [(0.78, 40)], [(0.80, 50)]), INI - 20)       # sin snapshot del 15m
    correr(nuc, m, INI + 3, INI + 4)
    assert tr(m, "BASE").orden and tr(m, "R2").orden is None
    assert filas(rows, "dec", pol="R2", acc="no_cotiza")[-1]["motivo"] == "sin_b15"
    m.on_msg(book(U15, [(0.22, 10)], [(0.21, 10)]), INI + 5)        # cruzado (bid > ask)
    m.on_msg(book(D15, [(0.78, 10)], [(0.80, 10)]), INI + 5)
    correr(nuc, m, INI + 5, INI + 6)
    assert tr(m, "R2").orden is None and filas(rows, "dec", pol="R2", acc="no_cotiza")[-1]["motivo"] == "b15_cruzado"


def test_relleno_por_operacion_que_atraviesa_cierra_la_puja_y_no_repuja():
    nuc, m, rows = mk("eth")
    preparar_vol(m, INI)
    libros(m, INI + 3, bid5=0.20, ask5=0.22, bid15=0.21)
    correr(nuc, m, INI + 3, INI + 4)
    o = tr(m, "R3").orden
    assert o and o["precio"] == 0.18
    size = o["size"]
    t_post = o["t_post"]
    m.on_msg(trade(UP, 0.17, 20, "SELL", ts=t_post + 0.5), t_post + 0.5)         # venta tomadora por debajo de 0,18 -> llena entera
    correr(nuc, m, INI + 4.1, INI + 7)
    t = tr(m, "R3")
    assert t.cerrado and t.llenas == size and t.orden is None
    fl = filas(rows, "fill", pol="R3", esc="cons_x")
    assert len(fl) == 1 and fl[0]["acc"] == size and fl[0]["precio"] == 0.18 and fl[0]["feat_post"]["r3"] is True
    n_post = t.n_post
    correr(nuc, m, INI + 7.1, INI + 12)
    assert t.n_post == n_post, "un relleno cierra la puja: no hay mas posts"


def test_relleno_por_acunacion_compra_tomadora_del_contrario():
    nuc, m, rows = mk("eth")
    preparar_vol(m, INI)
    libros(m, INI + 3, bid5=0.20, ask5=0.22, bid15=0.21)
    correr(nuc, m, INI + 3, INI + 4)
    t_post = tr(m, "BASE").orden["t_post"]
    m.on_msg(trade(DN, 0.84, 9, "BUY", ts=t_post + 0.3), t_post + 0.3)           # equivalente 0,16 < 0,18
    correr(nuc, m, INI + 4.1, INI + 7)
    assert tr(m, "BASE").llenas > 0


def test_parcial_a_la_cola_solo_con_volumen_sobre_la_cola():
    nuc, m, rows = mk("eth")
    preparar_vol(m, INI)
    libros(m, INI + 3, bid5=0.20, ask5=0.22, bid15=0.21)
    m.on_msg(pc(UP, 0.18, 30, "BUY"), INI + 3)                      # ya hay 30 acc en 0,18 (cola)
    correr(nuc, m, INI + 3.5, INI + 4.5)
    o_cons, o_opt = tr(m, "BASE", "cons_x").orden, tr(m, "BASE", "opt_x").orden
    assert o_cons["cola"] == 30.0 and o_opt["cola"] == 0.0
    t_post = o_cons["t_post"]
    m.on_msg(trade(UP, 0.18, 20, "SELL", ts=t_post + 0.3), t_post + 0.3)          # 20 < cola 30: cons no llena; opt (cola 0) llena 5
    correr(nuc, m, INI + 4.6, INI + 6.5)
    assert tr(m, "BASE", "cons_x").llenas == 0.0 and tr(m, "BASE", "opt_x").llenas == o_opt["size"]


def test_repega_espera_asentado_y_stop():
    nuc, m, rows = mk("sol")
    preparar_vol(m, INI)
    libros(m, INI + 3, bid5=0.20, ask5=0.22, bid15=0.21)
    correr(nuc, m, INI + 3, INI + 4)
    assert tr(m, "BASE").orden["precio"] == 0.19
    m.on_msg(pc(UP, 0.21, 10, "BUY"), INI + 4)                      # el top sube a 0,21 -> objetivo 0,20
    m.on_msg(pc(UP, 0.22, 5, "SELL"), INI + 4)
    correr(nuc, m, INI + 4.1, INI + 4.5)
    b = tr(m, "BASE")
    assert b.orden is None and len(b.pend) == 1, "cancelada, pendiente de asentar"
    correr(nuc, m, INI + 4.6, INI + 5.3)
    assert b.orden is None, "no se repuja antes de ASENTAR_S"
    correr(nuc, m, INI + 5.4, INI + 6.5)
    assert b.orden and b.orden["precio"] == 0.2 and b.n_post == 2
    correr(nuc, m, INI + 7, m.fin - 61)
    assert b.orden
    correr(nuc, m, m.fin - 60.5, m.fin - 56)
    assert b.orden is None and b.parado and not b.pend
    assert filas(rows, "mkt_fin")[0]["completo"] is True and filas(rows, "mkt_fin")[0]["parada"] is None


def test_banda_y_bordes_de_precio():
    for bid, ask, esperado in ((0.11, 0.13, None), (0.12, 0.14, 0.10), (0.30, 0.32, 0.28), (0.31, 0.33, None)):
        nuc, m, rows = mk("eth")
        libros(m, INI - 20, bid5=bid, ask5=ask, bid15=bid + 0.01)
        correr(nuc, m, INI + 3, INI + 4)
        o = tr(m, "BASE").orden
        assert (o["precio"] if o else None) == esperado, (bid, ask)


def test_ws_viejo_para_las_politicas_y_marca_incompleto():
    nuc, m, rows = mk("eth")
    preparar_vol(m, INI)
    libros(m, INI + 3, bid5=0.20, ask5=0.22, bid15=0.21)
    correr(nuc, m, INI + 3, INI + 4)
    assert tr(m, "BASE").orden
    t = INI + 4.1
    while t < INI + 12:                                            # sin mensajes ni PONG
        nuc.tick(t)
        t += 0.1
    assert m.parar_motivo == "ws_viejo" and tr(m, "BASE").parado
    correr(nuc, m, INI + 12, m.fin - 56)
    assert filas(rows, "mkt_fin")[0]["completo"] is False and filas(rows, "mkt_fin")[0]["parada"] == "ws_viejo"


def test_tick_cambiado_para_como_b():
    nuc, m, rows = mk("eth")
    preparar_vol(m, INI)
    libros(m, INI + 3)
    correr(nuc, m, INI + 3, INI + 4)
    assert tr(m, "BASE").orden
    m.on_msg({"event_type": "tick_size_change", "asset_id": UP}, INI + 4.05)
    correr(nuc, m, INI + 4.1, INI + 4.5)
    assert tr(m, "BASE").orden is None and m.parar_motivo == "tick_cambiado"


def test_reconexion_invalida_libro_y_marca_hueco():
    nuc, m, rows = mk("eth")
    preparar_vol(m, INI)
    libros(m, INI + 3, bid5=0.20, ask5=0.22, bid15=0.21)
    correr(nuc, m, INI + 3, INI + 4)
    m.reconectado(INI + 4.2)
    assert not m.libro_valido(UP) and m.vol30(INI + 4.3) is None
    correr(nuc, m, INI + 4.2, INI + 7)                              # libro invalido > 2 s -> cancela
    assert tr(m, "BASE").orden is None
    libros(m, INI + 7.1, bid5=0.20, ask5=0.22, bid15=0.21)
    correr(nuc, m, INI + 7.2, m.fin - 56)
    assert filas(rows, "mkt_fin")[0]["completo"] is False and filas(rows, "mkt_fin")[0]["huecos"] == 1


def test_mensajes_duplicados_y_desordenados_no_rompen():
    nuc, m, rows = mk("eth")
    preparar_vol(m, INI)
    libros(m, INI + 3, bid5=0.20, ask5=0.22, bid15=0.21)
    for _ in range(3):                                              # snapshot repetido
        m.on_msg(book(UP, [(0.20, 50)], [(0.22, 40)]), INI + 3.5)
    m.on_msg(trade(UP, 0.30, 1, "SELL", ts=INI + 100), INI + 3.6)    # timestamp de exchange futuro
    m.on_msg(trade(UP, 0.30, 1, "SELL", ts=INI - 100), INI + 3.7)    # y pasado
    m.on_msg({"event_type": "last_trade_price", "asset_id": UP, "price": "x"}, INI + 3.8)    # basura
    m.on_msg({"foo": 1}, INI + 3.9)
    correr(nuc, m, INI + 4, INI + 6)
    assert tr(m, "BASE").orden and nuc.stats.get("error_trader", 0) == 0


def test_idempotencia_de_claves_y_reinicio_desde_el_log(tmp_path):
    out = S.Salida(tmp_path)
    emitidos = set()
    nuc = R.Nucleo(out.put, emitidos)
    mk5 = {"slug": f"eth-updown-5m-{INI}", "id": "5", "up": UP, "down": DN}
    mk15 = {"slug": f"eth-updown-15m-{INI // 900 * 900}", "id": "15", "up": U15, "down": D15}
    nuc.nuevo("eth", INI, mk5, mk15, int((INI - 20) * 1000))
    assert nuc.emit({"k": "x|1", "tipo": "latido", "r": INI * 1000}) is True
    assert nuc.emit({"k": "x|1", "tipo": "latido", "r": INI * 1000}) is False and nuc.stats["duplicado_evitado"] == 1
    out.cerrar()
    f = next(tmp_path.glob("r3_shadow_*.jsonl.gz"))
    # gzip truncado al final (proceso muerto a mitad): las filas anteriores se leen
    with open(f, "ab") as fh:
        fh.write(gzip.compress(b'{"k":"y|1","tipo":"x","pad":"' + bytes(random.Random(1).randbytes(400)).hex().encode() + b'"}\n')[:-60])
    em, vistos, term = S.restaurar(tmp_path, INI + 10)
    assert f"mkt|eth-updown-5m-{INI}" in em and "x|1" in em and "y|1" not in em
    assert vistos == {f"eth-updown-5m-{INI}"} and term == set()


def test_cerrar_es_idempotente_y_podar():
    nuc, m, rows = mk("eth")
    nuc.cerrar(m, INI + 100)
    nuc.cerrar(m, INI + 101)
    assert len(filas(rows, "mkt_fin")) == 1 and len(filas(rows, "fin_t")) == len(R.POLITICAS) * len(R.ESCENARIOS)
    nuc.podar(m.fin + 500)
    assert m.slug not in nuc.mercados


def test_smp_cada_5s_con_flags():
    nuc, m, rows = mk("eth")
    preparar_vol(m, INI)
    libros(m, INI + 3, bid5=0.20, ask5=0.22, bid15=0.21)
    correr(nuc, m, INI + 3, INI + 20)
    s = filas(rows, "smp")
    assert 3 <= len(s) <= 4 and all(x["r2"] is True and x["r3"] is True and x["lvl15m"] == 30 for x in s)


# ---------------------------------------------------------------- seguridad: dry-run puro
def test_seguridad_sin_simbolos_de_ordenes_claves_ni_produccion():
    prohibido = re.compile(r"create_order|post_order|cancel_order|ClobClient|py_clob_client|private_key|PRIVATE_KEY|api_secret|\.env|secrets|signer|sign_order|"
                           r"live_trade|live_switch|import experimento_|from experimento_|requests\.post|\.post\(")
    for nombre in ("r3_regla.py", "r3_shadow.py", "r3_desenlaces.py", "r3_vigia.py"):
        p = AQUI / nombre
        if not p.exists():
            continue
        # se ignoran docstrings y comentarios: solo codigo
        codigo = "\n".join(l for l in p.read_text().splitlines() if not l.strip().startswith("#"))
        codigo = re.sub(r'""".*?"""', "", codigo, flags=re.S)
        assert not prohibido.search(codigo), f"{nombre}: simbolo prohibido {prohibido.search(codigo).group(0)}"


def test_salida_defecto_fuera_de_git_y_humo_prohibido_con_ella():
    assert S.SALIDA_DEFECTO.startswith("/root/polymarket-research-datalogs/")
    with pytest.raises(SystemExit):
        sys.argv = ["x", "--minutos", "1"]
        S.main()


# ---------------------------------------------------------------- resolvedor y vigia (datos sinteticos)
import r3_desenlaces as D  # noqa: E402
import r3_vigia as V  # noqa: E402


def sembrar(d, dias, fills_por_dia=40, completos=864, sesgo=0.1, seed=3, sin_desenlace=0):
    """Escribe en `d` un log sintetico: por dia, `completos` mkt_fin completos y fills BASE/R2/R3 (cons_x y cons_r) con desenlace oficial.
    Los fills con flag R3=true ganan con prob 0.30+sesgo, los demas 0.20 (precio 0.20 => EV ~ +0.5 vs -0.0)."""
    rnd = random.Random(seed)
    out = S.Salida(d)
    outd = S.Salida(d, prefijo="r3_desenlaces")
    n = 0
    for k, dia in enumerate(dias):
        base = int(datetime.fromisoformat(dia).replace(tzinfo=timezone.utc).timestamp())
        for i in range(completos):
            ini = base + 300 * (i % 288)
            coin = ("eth", "sol", "xrp")[i // 288 % 3]
            slug = f"{coin}-updown-5m-{ini}"
            out.put({"k": f"mkt_fin|{slug}|{dia}", "tipo": "mkt_fin", "r": (ini + 300) * 1000, "slug": slug, "coin": coin, "cierre": ini + 300, "completo": True, "huecos": 0,
                     "arranque_tarde": False})
            if i < fills_por_dia:
                r3 = i % 3 == 0
                gana = rnd.random() < (0.30 + sesgo if r3 else 0.20)
                if n < sin_desenlace:
                    n += 1
                else:
                    outd.put({"k": f"des|{slug}|{dia}", "tipo": "des", "r": (ini + 300) * 1000, "slug": slug, "cierre": ini + 300, "ganador": "YES" if gana else "NO"})
                for pol in ("BASE", "R2", "R3"):
                    if pol == "R3" and not r3:
                        continue
                    if pol == "R2" and not r3:
                        continue
                    for esc in ("cons_x", "cons_r", "opt_x"):
                        out.put({"k": f"fill|{slug}|{pol}|{esc}|{dia}", "tipo": "fill", "r": (ini + 200) * 1000, "slug": slug, "coin": coin, "pol": pol, "esc": esc, "lado": "YES",
                                 "precio": 0.20, "size": 5.0, "acc": 5.0, "n_orden": 1, "t1": (ini + 200) * 1000, "T1": 100.0,
                                 "feat_post": {"r2": r3, "r3": r3}})
    out.cerrar()
    outd.cerrar()


def test_vigia_acumulando_con_pocos_dias_y_cobertura(tmp_path):
    sembrar(tmp_path, ["2026-10-23", "2026-10-24"])
    res = V.informe(tmp_path, desde="2026-10-22", ledger="/nonexistent")
    assert res["dias_validos"] == 2 and res["reglas"]["R3"]["veredicto"] == "ACUMULANDO"
    assert res["cobertura"]["2026-10-23"]["completos"] == 864 and res["cobertura"]["2026-10-23"]["valido"]
    assert res["reglas"]["R3"]["escenarios"]["cons_x"]["dif"]["dif"] is not None


def test_vigia_dia_con_poca_cobertura_no_cuenta(tmp_path):
    sembrar(tmp_path, ["2026-10-23"], completos=500)                # 500/864 = 0,58 < 0,80
    res = V.informe(tmp_path, desde="2026-10-22", ledger="/nonexistent")
    assert res["dias_validos"] == 0 and res["cobertura"]["2026-10-23"]["valido"] is False
    assert res["fills_excluidos"].get("dia_no_valido", 0) > 0
    assert res["reglas"]["R3"]["escenarios"]["cons_x"]["dif"]["dif"] is None


def test_vigia_confirmada_con_efecto_grande_y_sesgo_mas_dias(tmp_path):
    dias = [f"2026-10-{d}" for d in range(23, 31)] + ["2026-11-01", "2026-11-02", "2026-11-03"]
    sembrar(tmp_path, dias, fills_por_dia=300, sesgo=0.25)          # 11 dias, 100 fills true/dia, 200 false/dia
    res = V.informe(tmp_path, desde="2026-10-22", ledger="/nonexistent")
    assert res["dias_validos"] == 11
    assert res["reglas"]["R3"]["veredicto"] == "CONFIRMADA", res["reglas"]["R3"]["motivos"]
    # sin efecto: no confirma
    d2 = tmp_path / "b"
    sembrar(d2, dias, fills_por_dia=300, sesgo=-0.10, seed=5)       # el flag true gana igual que el resto (0.20)
    res2 = V.informe(d2, desde="2026-10-22", ledger="/nonexistent")
    assert res2["reglas"]["R3"]["veredicto"] != "CONFIRMADA"


def test_vigia_missing_no_es_cero_fills_sin_desenlace_se_excluyen(tmp_path):
    sembrar(tmp_path, ["2026-10-23"], sin_desenlace=10)
    res = V.informe(tmp_path, desde="2026-10-22", ledger="/nonexistent")
    assert res["fills_excluidos"]["sin_desenlace"] > 0
    assert res["cobertura"]["2026-10-23"]["fills_sin_desenlace"] > 0


def test_veredicto_fail_closed_con_datos_ausentes():
    vacio = {"dif": {"n_true": 0, "n_false": 0, "dif": None, "ic90": [None, None], "ic95": [None, None], "dif_sin2": None}, "ev": {"ev": None, "ic95": [None, None], "ev_sin2": None}}
    v, _ = V.veredicto_regla(30, {"cons_x": vacio, "cons_r": vacio})
    assert v != "CONFIRMADA"


def test_desenlaces_idempotente_y_abandona_a_las_6h(tmp_path, monkeypatch):
    ahora = datetime.now(timezone.utc)
    ini = int(ahora.timestamp()) // 300 * 300 - 900
    viejo = ini - 8 * 3600
    out = S.Salida(tmp_path)
    for i, slug_ini in enumerate((ini, viejo)):
        slug = f"eth-updown-5m-{slug_ini}"
        out.put({"k": f"mkt_fin|{slug}", "tipo": "mkt_fin", "r": (slug_ini + 300) * 1000, "slug": slug, "coin": "eth", "cierre": slug_ini + 300, "completo": True})
    out.cerrar()
    llamadas = []
    monkeypatch.setattr(D, "desenlaces_gamma", lambda slugs: (llamadas.append(list(slugs)) or ({f"eth-updown-5m-{ini}": "YES"}, 0, 1)))
    assert D.main(["--dir", str(tmp_path), "--dias", "2"]) == 0
    assert D.main(["--dir", str(tmp_path), "--dias", "2"]) == 0                  # 2a pasada: nada nuevo
    filas = [r for f in tmp_path.glob("r3_desenlaces_*.jsonl.gz") for r in S.leer_gz_tolerante(f)]
    assert sorted((r["slug"].rsplit("-", 1)[1], r["ganador"]) for r in filas) == sorted([(str(ini), "YES"), (str(viejo), None)])
    assert len(filas) == 2 and len(llamadas) == 1, "no se vuelve a consultar lo ya resuelto/abandonado"


def test_cron_script_sintaxis():
    import subprocess
    assert subprocess.run(["bash", "-n", str(AQUI / "r3_cron.sh")]).returncode == 0


def test_b_real_empareja_por_flag_y_mide_acuerdo_de_relleno(tmp_path):
    slug = f"eth-updown-5m-{INI}"
    led = tmp_path / "led.jsonl"
    lineas = [{"real": True, "escalon": "B", "tipo": "puja_post", "slug": slug, "lado": "YES", "t_dec": INI + 10.0, "precio": 0.18},
              {"real": True, "escalon": "B", "tipo": "puja_fin", "slug": slug, "lado": "YES", "coin": "eth", "k": 2, "n_ordenes": 1, "fin_puja": "relleno",
               "rellenos": [{"acc": 5.0, "precio": 0.18}]}]
    led.write_text("\n".join(json.dumps(x) for x in lineas) + "\n")
    smp = [{"tipo": "smp", "slug": slug, "lado": "YES", "r": int((INI + 12) * 1000), "r2": True, "r3": False}]
    des = {slug: {"ganador": "YES"}}
    fin = {slug: {"completo": True}}
    fills = [{"slug": slug, "lado": "YES", "pol": "BASE", "esc": "cons_x"}]
    fint = [{"slug": slug, "lado": "YES", "pol": "BASE", "esc": "cons_x", "n_post": 1}]
    out = V.b_real(str(led), smp, [], des, fin, fills, fint)
    assert out["disponible"] and out["por_flag"]["R2=true,R3=false"]["rellenos"] == 1
    assert abs(out["por_flag"]["R2=true,R3=false"]["pnl"] - (5.0 - 0.9)) < 1e-9
    assert out["acuerdo_relleno_real_vs_simulado"]["cons_x"] == {"real_si__sim_si": 1}
    assert out["acuerdo_relleno_real_vs_simulado"]["cons_r"] == {"real_si__sim_no": 1}
    assert V.b_real(str(tmp_path / "no_existe.jsonl"), [], [], {}) == {"disponible": False}
