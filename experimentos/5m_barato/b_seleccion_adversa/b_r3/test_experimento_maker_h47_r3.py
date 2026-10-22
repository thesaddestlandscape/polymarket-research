#!/usr/bin/env python3
"""Pruebas de experimento_maker_h47_r3 (variante R2/R3 de B) con cliente CLOB, libros y cadena FALSOS: sin red, sin dinero, ledger/KILL/lock en un directorio temporal.
Reutiliza los fixtures de test_experimento_maker_h47.py (el de B, sin tocarlo). NO ejecuta la variante contra el mercado.
Uso: /root/polymarket-research/.venv/bin/python -m pytest -q experimentos/5m_barato/b_seleccion_adversa/b_r3/test_experimento_maker_h47_r3.py
Cubren: regla falsa => ni una orden (seco y real), regla verdadera => la MISMA puja que B, repegado/cancelacion al pasar a falso, fail-closed (sin 15m, cruzado, viejo,
vol30 incompleto, excepcion), bordes (3c, 26 acc, hora 4), restauracion de objetivo_h35, defensa en profundidad en post(), ledger propio (hermano de los demas),
escalon A/regla invalida/sha de B cambiado => no arranca, equivalencia con B cuando la regla es siempre verdadera."""
import json
import random
import sys
import time
from pathlib import Path

import pytest

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
sys.path.insert(0, "/root/polymarket-research-dev")
import experimento_maker_h47_r3 as V   # noqa: E402
import test_experimento_maker_h47 as T  # noqa: E402  (fixtures de B: Cli, lib_falso, mk_falso, ctx_de, eventos...)

H, X, RR = V.H, V.X, V.RR
CREADOS_R3 = []


@pytest.fixture(autouse=True)
def _limpia_r3():
    orig = H.objetivo_h35
    yield
    assert H.objetivo_h35 is orig, "objetivo_h35 de B debe quedar restaurado"
    for ex in CREADOS_R3:
        ex._cerrado = True
    CREADOS_R3.clear()
    X.saldo_onchain = lambda w: T.ONCHAIN["pusd"]


def nuevo_r3(nombre, real=False, regla="R3", **kw):
    X.LEDGER = T.TMP / f"{nombre}.jsonl"
    X.KILL_FICHERO = T.TMP / f"{nombre}.KILL"
    X.LOCK = T.TMP / f"{nombre}.lock"
    X._CACHE = None
    X.cliente_dedicado = (lambda: (T.Cli(), "0xabc")) if real else (lambda: (_ for _ in ()).throw(AssertionError("seco: no hay cliente")))
    X.ASENTAR_S = 0.05
    T.ONCHAIN["pusd"] = 19.59
    ex = V.Exp47R3(real, kw.pop("escalon", "B"), kw.pop("n_max", None), 60.0, 5, 1.0, ("eth", "sol", "xrp"), kw.pop("presupuesto", 12.0), 5, regla)
    CREADOS_R3.append(ex)
    return ex


def ctx15(ex, coin="eth", bid5=0.20, ask5=0.22, bid15=0.21, ask15=0.23, vol=30.0, vol_antes_de_conectar=False):
    """Contexto con libro 5m (T.ctx_de) y libro 15m falso del mismo lado; `vol` acciones casadas hace 5 s; libro conectado antes de la apertura."""
    c = T.ctx_de(ex, coin, bid5, ask5)
    now = time.time()
    c.mk["ini"] = now - 100
    c.t_inicio = now - 120 if not vol_antes_de_conectar else now - 10
    c.lib15 = T.lib_falso(bid15, ask15, "tU15", "tD15")
    c.tok15 = {c.up: "tU15", c.dn: "tD15"}
    if vol:
        c.lib.trades[c.up].append((now - 5, now - 5, 0.21, vol, "BUY"))
    return c


def ev(tipo=None):
    """Eventos del ledger actual; [] si todavia no existe (nada que registrar)."""
    return T.eventos(tipo) if X.LEDGER.exists() else []


def decidir(ex, c, t=200.0):
    c.mk["fin"] = time.time() + t
    ex.decidir(c, t, time.time())


def posts(ex):
    return ev("puja_post")


def test_regla_verdadera_pone_la_misma_puja_que_b_y_deja_rasgos_en_el_ledger():
    ex = nuevo_r3("v1")
    c = ctx15(ex, bid15=0.21)                                        # ETH k=2: objetivo 0,18; 21-18 = 3c => R2 ok; vol 30 >= 26; hora actual >= 4 (se fuerza)
    V.hora_utc = lambda now: 12
    decidir(ex, c)
    p = posts(ex)
    assert len(p) == 1 and p[0]["precio"] == 0.18 and p[0]["linea_r3"] == "B_R3"
    r3 = p[0]["r3"]
    assert r3["ok"] is True and r3["b15"] == 0.21 and r3["lvl15m"] == 30 and r3["vol30"] == 30.0 and r3["hora"] == 12 and r3["regla"] == "R3"
    dec = ev("r3_decision")
    assert len(dec) == 1 and dec[0]["precio"] == 0.18 and dec[0]["r3"]["b15"] == 0.21
    ex_b = T.nuevo("v1_b", real=False)                               # B sin regla, mismo libro
    cb = T.ctx_de(ex_b, "eth", 0.20, 0.22)
    cb.mk["fin"] = time.time() + 200
    ex_b.decidir(cb, 200.0, time.time())
    assert ev("puja_post")[-1]["precio"] == 0.18


def test_regla_falsa_no_pone_ninguna_orden_seco_y_real():
    for real in (False, True):
        ex = nuevo_r3(f"f{int(real)}", real=real)
        c = ctx15(ex, bid15=0.22)                                    # 22-18 = 4c > 3c
        V.hora_utc = lambda now: 12
        decidir(ex, c)
        assert posts(ex) == [] and ev("r3_decision") == []
        assert not any(e["tipo"] == "intencion_post" for e in ev())
        if real:
            assert ex.cli.posts == []


def test_real_regla_verdadera_envia_una_orden_y_falsa_ninguna():
    ex = nuevo_r3("rv", real=True)
    c = ctx15(ex, bid15=0.21)
    V.hora_utc = lambda now: 12
    decidir(ex, c)
    assert len(ex.cli.posts) == 1 and ex.cli.posts[0][1] == 0.18


def test_borde_3c_exacto_y_vol30_26_y_hora_4():
    V.hora_utc = lambda now: 4
    ex = nuevo_r3("b1")
    c = ctx15(ex, bid15=0.21, vol=26.0)
    decidir(ex, c)
    assert len(posts(ex)) == 1                                       # 3c, 26 acc, hora 4: todo en el borde, pasa
    ex = nuevo_r3("b2")
    c = ctx15(ex, bid15=0.21, vol=25.99)
    decidir(ex, c)
    assert posts(ex) == []
    ex = nuevo_r3("b3")
    V.hora_utc = lambda now: 3
    c = ctx15(ex, bid15=0.21, vol=40.0)
    decidir(ex, c)
    assert posts(ex) == []
    ex = nuevo_r3("b4", regla="R2")                                  # R2 no mira volumen ni hora
    c = ctx15(ex, bid15=0.21, vol=0.0)
    decidir(ex, c)
    assert len(posts(ex)) == 1


def test_fail_closed_sin_15m_cruzado_viejo_y_ventana_incompleta():
    V.hora_utc = lambda now: 12
    ex = nuevo_r3("c1")
    c = ctx15(ex)
    c.lib15 = None
    decidir(ex, c)
    assert posts(ex) == []
    ex = nuevo_r3("c2")
    c = ctx15(ex, bid15=0.21, ask15=0.20)                            # cruzado
    decidir(ex, c)
    assert posts(ex) == []
    ex = nuevo_r3("c3")
    c = ctx15(ex)
    c.lib15.ult_msg = time.time() - 30                               # conexion del 15m muerta
    decidir(ex, c)
    assert posts(ex) == []
    ex = nuevo_r3("c4")
    c = ctx15(ex, vol_antes_de_conectar=True)                        # el libro se conecto 10 s antes: la ventana de 30 s no esta cubierta
    decidir(ex, c)
    assert posts(ex) == []
    ex = nuevo_r3("c5", regla="R2")
    c = ctx15(ex, vol_antes_de_conectar=True)
    decidir(ex, c)
    assert len(posts(ex)) == 1, "R2 no usa vol30"


def test_excepcion_al_evaluar_no_mata_ni_cotiza():
    V.hora_utc = lambda now: 12
    ex = nuevo_r3("e1")
    c = ctx15(ex)

    def boom(tk):
        raise RuntimeError("x")
    c.lib15.top = boom
    decidir(ex, c)
    assert posts(ex) == [] and ex._r3_err == 1 and not ex.kill


def test_pasar_a_falso_con_puja_viva_la_cancela_con_rasgos():
    V.hora_utc = lambda now: 12
    ex = nuevo_r3("k1")
    c = ctx15(ex, bid15=0.21)
    decidir(ex, c)
    assert len(posts(ex)) == 1
    time.sleep(0.15)
    T.poner_libro(c.lib15, "tU15", {0.25: 100.0}, {0.27: 100.0})     # el 15m sube: 25-18 = 7c
    decidir(ex, c)
    canc = ev("cancela_banda")
    assert len(canc) == 1 and canc[0]["r3"]["motivo"] == "r2_nivel15" and canc[0]["r3"]["ok"] is False


def test_objetivo_h35_se_restaura_aunque_decidir_de_b_lance(monkeypatch):
    ex = nuevo_r3("x1")
    c = ctx15(ex)
    orig = H.objetivo_h35

    def lanza(self, c, T_, a):
        raise RuntimeError("boom")
    monkeypatch.setattr(H.Exp47, "decidir", lanza)
    with pytest.raises(RuntimeError):
        decidir(ex, c)
    assert H.objetivo_h35 is orig


def test_post_directo_con_regla_en_falso_se_bloquea_defensa_en_profundidad():
    ex = nuevo_r3("d1", real=True)
    c = ctx15(ex)
    ex._r3_ultimo = {"slug": c.mk["slug"], "ok": False, "motivo": "r2_nivel15"}
    assert ex.post(c.mk["slug"], c.up, "YES", 0.18, 5.0, 0.0) is None
    assert ex.cli.posts == [] and ev("r3_bloqueo_post")
    ex._r3_ultimo = None
    assert ex.post(c.mk["slug"], c.up, "YES", 0.18, 5.0, 0.0) is None and ex.cli.posts == []


def test_token_distinto_del_libro_no_cotiza():
    V.hora_utc = lambda now: 12
    ex = nuevo_r3("t1")
    c = ctx15(ex)
    orig_top = c.lib.top
    c.lib.top = lambda tk: ((0.19, 10.0), (0.22, 10.0)) if tk == c.up else orig_top(tk)      # el libro 'cambia' bajo los pies de la regla
    n = {"i": 0}

    def top_inestable(tk):
        n["i"] += 1
        return ((0.20, 50.0), (0.22, 40.0)) if n["i"] <= 2 else ((0.19, 50.0), (0.22, 40.0))
    c.lib.top = top_inestable
    decidir(ex, c)
    assert posts(ex) == []


def test_escalon_a_regla_invalida_y_sha_de_b_cambiado_no_arrancan(monkeypatch):
    with pytest.raises(SystemExit):
        nuevo_r3("s1", escalon="A")
    with pytest.raises(SystemExit):
        nuevo_r3("s2", regla="R9")
    with pytest.raises(SystemExit):
        nuevo_r3("s3", n_max=501)
    monkeypatch.setattr(V, "B_SHA_REVISADO", "0" * 64)
    with pytest.raises(SystemExit):
        V.verificar_sha_b()
    with pytest.raises(SystemExit):
        V.main(["--regla", "R3"])


def test_sha_actual_de_b_coincide_con_el_revisado():
    assert V.sha_b() == V.B_SHA_REVISADO


def test_ledger_propio_es_hermano_de_los_demas():
    H.configurar_rutas(False, V.ESCALON_LEDGER, 60.0)
    assert X.LEDGER.name == "experimento_h47_seco_B_R3_ledger.jsonl"
    H.configurar_rutas(True, V.ESCALON_LEDGER, 60.0)
    assert X.LEDGER.name == "experimento_h47_B_R3_ledger.jsonl" and X.LOCK.name == "experimento_h47.lock" and X.KILL_FICHERO.name == "experimento_h47.KILL"
    d = T.TMP / "hermanos"
    d.mkdir(exist_ok=True)
    X.LEDGER = d / "experimento_h47_B_R3_ledger.jsonl"
    for n in ("experimento_h47_B_ledger.jsonl", "experimento_h47_A_ledger.jsonl", "experimento_h47_seco_B_ledger.jsonl", "experimento_h47_B_R3_ledger.jsonl"):
        (d / n).write_text("")
    nombres = {p.name for p in H.ledgers_reales_hermanos()}
    assert "experimento_h47_B_ledger.jsonl" in nombres and "experimento_h47_A_ledger.jsonl" in nombres and "experimento_h47_seco_B_ledger.jsonl" not in nombres
    assert "experimento_h47_B_R3_ledger.jsonl" not in nombres                                 # el propio no es hermano de si mismo
    X.LEDGER = d / "experimento_h47_B_ledger.jsonl"                                           # y B (si reiniciara) vera el de la variante
    assert "experimento_h47_B_R3_ledger.jsonl" in {p.name for p in H.ledgers_reales_hermanos()}


def test_equivalente_a_b_cuando_la_regla_es_siempre_verdadera(monkeypatch):
    monkeypatch.setattr(RR, "regla", lambda pol, f: (True, None))
    rnd = random.Random(11)
    for i in range(12):
        bid = round(rnd.choice([0.12, 0.15, 0.2, 0.25, 0.3]) + rnd.choice([0, 0, 0.005]), 3)
        ask = round(bid + rnd.choice([0.01, 0.02, 0.05]), 3)
        coin = rnd.choice(["eth", "sol", "xrp"])
        ex = nuevo_r3(f"q{i}")
        c = ctx15(ex, coin, bid, ask, bid15=0.4, ask15=0.42)
        decidir(ex, c)
        p_r3 = [e["precio"] for e in ev("puja_post")]
        exb = T.nuevo(f"qb{i}", real=False)
        cb = T.ctx_de(exb, coin, bid, ask)
        cb.mk["fin"] = time.time() + 200
        exb.decidir(cb, 200.0, time.time())
        p_b = [e["precio"] for e in ev("puja_post")]
        assert p_r3 == p_b, (bid, ask, coin)


def test_seguridad_estatica_sin_secretos_ni_cambios_a_b():
    import re
    codigo = Path(V.__file__).read_text()
    codigo = re.sub(r'""".*?"""', "", codigo, flags=re.S)
    assert not re.search(r"\.env|private_key|PRIVATE_KEY|api_secret|seed", codigo)
    assert Path(H.__file__).resolve() == Path("/root/polymarket-research-dev/experimento_maker_h47.py")
    assert "experimento_maker_h47.py" not in re.findall(r"open\([^)]*\)", codigo)
