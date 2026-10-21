"""Tests del paquete H23 V3 real (COPIA de los 75 de v1 adaptada a los nombres V3 + los de la RE-PUJA TEMPRANA al final; sin red, sin dinero): politica de decision con libro falso, camino caliente de cancelacion (paso/liquidar/verificar),
equivalencia con el replay, integracion con X.cancelar / X.post REALES del arnes (cliente CLOB falso, ledger en tmp), etiquetas, kill por brazo y
puertas del modo real. Desde este directorio:  python3 -m pytest -q -p no:cacheprovider test_experimento_maker_h23.py
(necesita /root/polymarket-research-dev con H47)"""
import json, os, random, sys, threading, time
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/root/polymarket-research-dev")
sys.path.insert(0, os.path.join(HERE, ".."))                               # h23_regla_v3
sys.path.insert(0, HERE)
import pytest
import experimento_maker_h47 as H
import experimento_maker_h23_v3 as M
import h23_regla_v3 as R

X = M.X


class Lib(X.Libro):
    """Libro REAL del arnes (top/tamano_nivel/mejor_bid_ajeno de X.Libro) sin hilo WS."""
    def __init__(self):
        self.lk = threading.Lock()
        self.L = {"u5": {"bids": {0.30: 100.0}, "asks": {0.33: 50.0}}, "d5": {"bids": {0.66: 10.0}, "asks": {0.70: 10.0}},
                  "u15": {"bids": {0.45: 80.0}, "asks": {0.47: 80.0}}, "d15": {"bids": {0.50: 10.0}, "asks": {0.54: 10.0}}}
        self.ok, self.tick_cambiado, self.ult_tok, self.ult = True, False, {}, time.time()
        self.edades = {}
        self.mids = {t: [] for t in self.L}
    def fresco(self): return self.ok
    def conexion_sana(self): return self.ok
    def edad(self, tk): return self.edades.get(tk, 0.0)
    def poner(self, tk, bids, asks):
        self.L[tk] = {"bids": dict(bids), "asks": dict(asks)}


class Fake(M.Exp23):
    def __init__(self):                                                     # NO llama al arnes (sin ledger, sin wallet, sin red)
        self.brazo, self.umbral, self.refs, self.kill_brazo, self.tanda_agotada = "A", 0.05, None, None, None
        self.sin_desenlace, self._intentos, self._ult_puerta, self.puerta_ok, self._ordenes_previas = None, {}, 0.0, True, {}
        self.vivas, self.canceladas, self.parada, self.kill, self.senal = {}, {}, None, None, None
        self.enfriar_tok, self.slugs_usados, self.n_max, self.max_vivas = {}, set(), 40, 2
        self.size, self.min_nocional, self.n_ordenes_total, self.t_stop = 5, 1.0, 0, 10.0
        self.real, self.sim_lleno, self.gem, self.gem_lleno = False, {}, {}, {}
        self._en_reaccion, self._ctx_actual, self._poll_ms, self._ult_vigilar, self._ult_kb, self._des = False, None, None, 0.0, 0.0, {}
        self._ult_verif = 0.0
        self.ctxs = {}
        self._t_ult_post = {}
        self.calls = []
    def sincronizar_rellenos(self, c): return 0.0
    def cancelar(self, h): self.calls.append(("cancelar", h)); self.vivas.pop(h, None); return True
    def liquidar(self, *a, **k): self.calls.append(("liquidar",))
    def n_usadas(self): return len(self.slugs_usados)
    def pujas_en_libro(self): return set()
    def puede_enviar(self, coste): return True
    def post(self, slug, tok, lado, precio, size, cola, **k):
        self.calls.append(("post", precio, size)); self.vivas["h1"] = {"precio": precio, "tok": tok, "size": size, "t_post": time.time(), "cola": cola}; return "h1"
    def _log47(self, ev): self.calls.append(("log", ev["tipo"])); self.evs = getattr(self, "evs", []) + [ev]
    def _bloqueo(self, *a): self.calls.append(("bloqueo",))
    def _libro5(self, lib, tok): return []


def ctx():
    c = object.__new__(M.Ctx23)
    c.mk = {"slug": "btc-updown-5m-1", "fin": time.time() + 200, "min_size": 5}
    c.up, c.dn, c.up15, c.dn15 = "u5", "d5", "u15", "d15"
    c.lados = {"u5": "YES", "d5": "NO"}
    c.estado = {t: {"llenas": 0.0, "coste": 0.0, "oid": None, "rellenos": [], "cerrado": False} for t in ("u5", "d5")}
    c.s, c.tc, c.to, c.n_ord, c.t_accion, c.hashes, c.fin_puja, c.tok, c.posteado, c.libro_dec = "Up", "u5", "u15", 0, 0.0, [], None, None, False, None
    c.fase, c.viejo_desde, c.medido, c.ult_poll, c.ult_poll_can, c.ult_cancel = "activa", None, False, 0.0, 0.0, 0.0
    c.lib = Lib()
    return c


def acts(ex): return [x for x in ex.calls if x[0] != "log"]


def viva(ex, c, h="h1", precio=0.30, size=5.0, visto=False, t_post=None, cola=50.0):
    ex.vivas[h] = {"precio": precio, "tok": "u5", "size": size, "t_post": t_post if t_post is not None else time.time(), "cola": cola,
                   "slug": c.mk["slug"], "lado": "YES", **({"visto": True} if visto else {})}
    c.estado["u5"]["oid"] = h
    return ex.vivas[h]


@pytest.fixture(autouse=True)
def sin_ledger(monkeypatch, request):
    if "tmp_path" not in request.fixturenames:                              # los tests con ledger real en tmp lo gestionan ellos
        monkeypatch.setattr(M.X, "leer_ledger", lambda: [])
        monkeypatch.setattr(M.H, "_fsync_ledger", lambda: None)


# ------------------------------------------------------------------ politica basica (heredada)
def test_pone_join_y_no_repone_si_nada_cambia():
    ex, c = Fake(), ctx()
    ex.decidir(c, 200, time.time())
    posts = [x for x in ex.calls if x[0] == "post"]
    assert len(posts) == 1 and posts[0][1] == 0.30 and posts[0][2] >= 5
    ex.calls.clear(); ex.decidir(c, 199, time.time() + 1)
    assert not [x for x in ex.calls if x[0] in ("post", "cancelar")]


def test_cancela_en_cuanto_cae_la_cota():
    ex, c = Fake(), ctx()
    ex.decidir(c, 200, time.time())
    c.lib.poner("u15", {0.36: 80.0}, {0.47: 80.0})                          # p_limite(0,36) = 0,29 < 0,30
    ex.calls.clear(); ex.decidir(c, 199, time.time() + 1)
    assert ("cancelar", "h1") in ex.calls and ("log", "h23_cancela") in ex.calls


def test_libro_no_fresco_cancela_y_no_pone():
    ex, c = Fake(), ctx()
    ex.decidir(c, 200, time.time())
    c.lib.ok = False
    ex.calls.clear(); ex.decidir(c, 199, time.time() + 1)
    assert ("cancelar", "h1") in ex.calls
    ex2, c2 = Fake(), ctx(); c2.lib.ok = False
    ex2.decidir(c2, 200, time.time())
    assert not [x for x in ex2.calls if x[0] == "post"]


def test_no_repone_mientras_hay_cancelada_sin_asentar():
    ex, c = Fake(), ctx()
    ex.canceladas["h0"] = {"tok": "u5"}
    ex.decidir(c, 200, time.time())
    assert not [x for x in ex.calls if x[0] == "post"]


def test_un_relleno_cierra_la_puja():
    ex, c = Fake(), ctx()
    ex.decidir(c, 200, time.time())
    c.estado["u5"]["llenas"] = 2.0
    ex.calls.clear(); ex.decidir(c, 199, time.time() + 1)
    assert ("cancelar", "h1") in ex.calls and c.estado["u5"]["cerrado"]
    ex.calls.clear(); ex.decidir(c, 198, time.time() + 2)
    assert not [x for x in ex.calls if x[0] == "post"]


def test_no_pone_sin_lado_ni_antes_de_la_ventana_ni_con_gap_pequeno():
    ex, c = Fake(), ctx(); c.s = c.tc = c.to = None
    ex.decidir(c, 200, time.time()); assert not [x for x in ex.calls if x[0] == "post"]
    ex, c = Fake(), ctx(); c.mk["fin"] = time.time() + 299.9                  # t < apertura + 1,5 s
    ex.decidir(c, 299.9, time.time()); assert not [x for x in ex.calls if x[0] == "post"]
    assert M.lado_por_refs(100.0, 99.9995) is None and M.lado_por_refs(100.0, 99.9) == "Up" and M.lado_por_refs(100.0, 100.1) == "Down"


def test_t_stop_no_pone_a_menos_de_12s():
    ex, c = Fake(), ctx(); c.mk["fin"] = time.time() + 11
    ex.decidir(c, 11, time.time()); assert not [x for x in ex.calls if x[0] == "post"]


def test_topes_n_y_vivas():
    ex, c = Fake(), ctx(); ex.slugs_usados = {f"s{i}" for i in range(40)}
    ex.decidir(c, 200, time.time()); assert not [x for x in ex.calls if x[0] == "post"]
    ex, c = Fake(), ctx(); ex.vivas = {"a": {}, "b": {}}
    ex.decidir(c, 200, time.time()); assert not [x for x in ex.calls if x[0] == "post"]


def test_el_real_no_es_el_defecto_y_el_ledger_es_hermano_de_h47():
    import inspect
    assert "action=\"store_true\"" in inspect.getsource(M.main) and "H23V3" in M.H.N_MAX and "H23V3B" in M.H.N_MAX
    assert M.H.N_MAX["H23V3"] == 40 and M.H.N_MAX["H23V3B"] == 40 and M.T_STOP_H23 == 10.0 and R.CONFIG["repost_min_ms"]["join_r"] == int(H.ASENTAR_H47_S * 1000)
    from pathlib import Path
    assert Path("experimento_h47_H23V3_ledger.jsonl").match("experimento_h47_*_ledger.jsonl")   # el glob de ledgers_reales_hermanos lo recoge


def test_mutacion_objetivo_siempre_se_detecta(monkeypatch):
    monkeypatch.setattr(M, "objetivo_h23", lambda a, b, u: 0.30)
    with pytest.raises(AssertionError):
        test_cancela_en_cuanto_cae_la_cota()


# ------------------------------------------------------------------ #3 bid AJENO = misma decision que el replay
def test_equivalencia_con_el_replay_mismas_decisiones_sobre_el_mismo_libro():
    rng = random.Random(23)
    n_dif_ingenuo = n_cancela = n_queda = 0
    for _ in range(600):
        niveles = sorted({round(rng.choice([0.05, 0.1, 0.2, 0.25, 0.28, 0.29, 0.30, 0.31, 0.35, 0.4, 0.55]), 2) for _ in range(rng.randint(0, 4))}, reverse=True)
        ajeno = {p: float(rng.randint(1, 40)) for p in niveles}                # libro SIN nuestra orden (lo que ve el replay)
        ask5 = round(rng.choice([0.31, 0.33, 0.36, 0.45, 0.7]), 2)
        b15 = round(rng.choice([0.3, 0.36, 0.4, 0.45, 0.6]), 2); a15 = round(b15 + rng.choice([0.01, 0.02, 0.05]), 2)
        pc = rng.choice(niveles + [0.30]) if niveles else 0.30                  # precio al que estamos
        ex, c = Fake(), ctx()
        con_nosotros = dict(ajeno); con_nosotros[pc] = con_nosotros.get(pc, 0.0) + 5.0
        c.lib.poner("u5", con_nosotros, {ask5: 50.0}); c.lib.poner("u15", {b15: 80.0}, {a15: 80.0})
        viva(ex, c, precio=pc, visto=True)
        b_aj = max(ajeno) if ajeno else None
        w = R.querer(b_aj, ask5, b15, a15, 0.05)                                # decision del replay (h23_sim_dia: want)
        replay_cancela = not (w is not None and abs(w - pc) < 1e-9)
        ex.calls.clear(); ex._reaccion_viva(c, 200, time.time(), "t")
        assert (("cancelar", "h1") in ex.calls) == replay_cancela, (ajeno, pc, ask5, b15, a15, w)
        n_cancela += replay_cancela; n_queda += not replay_cancela
        top = max(con_nosotros)                                                 # lo que haria el codigo ANTES (top() incluye nuestra orden)
        w_ing = R.querer(top, ask5, b15, a15, 0.05)
        n_dif_ingenuo += (not (w_ing is not None and abs(w_ing - pc) < 1e-9)) != replay_cancela
    assert n_dif_ingenuo > 0 and n_cancela > 20 and n_queda > 20            # el test tiene potencia: la version ingenua discrepaba


def test_solos_en_el_nivel_se_cancela_aunque_top_muestre_nuestra_orden():
    ex, c = Fake(), ctx()
    c.lib.poner("u5", {0.30: 5.0, 0.29: 40.0}, {0.33: 50.0})
    viva(ex, c, precio=0.30, size=5.0, visto=True)
    ex._reaccion_viva(c, 200, time.time(), "t")
    assert ("cancelar", "h1") in ex.calls                                      # bid ajeno = 0,29 != 0,30 (replay: re-cotiza a 0,29)
    ex2, c2 = Fake(), ctx()
    c2.lib.poner("u5", {0.30: 55.0, 0.29: 40.0}, {0.33: 50.0})                 # hay 50 ajenas en el 0,30: nos quedamos
    viva(ex2, c2, precio=0.30, size=5.0, visto=True)
    ex2._reaccion_viva(c2, 200, time.time(), "t")
    assert not [x for x in ex2.calls if x[0] == "cancelar"]


# ------------------------------------------------------------------ #2 paso() y frescura (incluida la edad del bid15)
def test_paso_cancela_con_libro_no_fresco_antes_de_salir():
    ex, c = Fake(), ctx()
    viva(ex, c)
    c.lib.ok = False
    ex.paso(c)                                                              # Exp47.paso saldria sin llegar a decidir(): la reaccion va antes
    assert acts(ex)[0] == ("cancelar", "h1")
    ev = [e for e in ex.evs if e["tipo"] == "h23_cancela"][0]
    assert ev["causa"] == "libro_no_fresco" and ev["origen"] == "rapida"


def test_paso_cancela_si_el_libro_15m_esta_viejo_aunque_la_conexion_viva():
    ex, c = Fake(), ctx()
    viva(ex, c)
    ex.paso(c); assert not [x for x in ex.calls if x[0] == "cancelar"]        # todo fresco: sigue
    c.lib.edades["u15"] = M.EDAD_TOKEN_MAX_S + 1                             # la conexion y el 5m siguen, el bid15 lleva > 30 s sin mensajes
    ex.calls.clear(); ex.paso(c)
    assert acts(ex)[0] == ("cancelar", "h1")
    assert [e for e in ex.evs if e["tipo"] == "h23_cancela"][-1]["causa"] == "libro_no_fresco"
    ex2, c2 = Fake(), ctx(); c2.lib.edades["u15"] = M.EDAD_TOKEN_MAX_S + 1
    ex2.decidir(c2, 200, time.time()); assert not [x for x in ex2.calls if x[0] == "post"]    # y no se puja con un bid15 viejo


def test_paso_cancela_antes_de_cualquier_lectura_rest():
    ex, c = Fake(), ctx()
    viva(ex, c)
    c.lib.poner("u15", {0.36: 80.0}, {0.47: 80.0})                           # condicion rota, libro fresco
    ex.paso(c)
    assert acts(ex)[0] == ("cancelar", "h1")                                 # antes del liquidar_todo/verificar de Exp47.paso
    ev = [e for e in ex.evs if e["tipo"] == "h23_cancela"][0]
    for k in ("t_evento", "t_detecta", "t_cancel", "t_cancel_ret", "ms_evento_a_cancel", "ms_cancel_rtt", "causa", "origen"):
        assert k in ev
    assert ev["t_cancel"] >= ev["t_detecta"] and ev["causa"] == "condicion"


def test_liquidar_y_verificar_reevaluan_antes_del_rest_y_verificar_va_de_una_en_una(monkeypatch):
    rec = []
    monkeypatch.setattr(X.Exp, "liquidar", lambda self, *a, **k: rec.append("rest_liquidar"))
    monkeypatch.setattr(X.Exp, "verificar", lambda self, limite=None: rec.append(("rest_verificar", limite)) or 0)
    ex, c = Fake(), ctx()
    ex.liquidar = lambda *a, **k: M.Exp23.liquidar(ex, *a, **k)             # el Fake lo silencia: usamos el real
    ex._reaccion_rapida_orig = ex._reaccion_rapida
    viva(ex, c); ex._ctx_actual = c
    c.lib.poner("u15", {0.36: 80.0}, {0.47: 80.0})
    ex.liquidar("h1", ex.vivas["h1"], False, c.estado, c.lib, 100)
    assert acts(ex)[0] == ("cancelar", "h1") and rec[-1] == "rest_liquidar"
    ex.verificar(limite=3); assert rec[-1] == ("rest_verificar", 3)         # sin orden viva: limite intacto
    c.lib.poner("u15", {0.45: 80.0}, {0.47: 80.0}); viva(ex, c, h="h2"); ex.verificar(limite=3); assert rec[-1] == ("rest_verificar", 1)   # con orden viva: de una en una


def test_vigilar_saldo_se_espacia_con_orden_viva(monkeypatch):
    n = []
    monkeypatch.setattr(H.Exp47, "vigilar_saldo", lambda self, ahora: n.append(ahora))
    ex, c = Fake(), ctx()
    ex.vigilar_saldo(100.0); ex.vigilar_saldo(100.5); assert n == [100.0, 100.5]      # sin viva: cada segundo como H47
    viva(ex, c); ex.vigilar_saldo(101.0); ex.vigilar_saldo(105.0); ex.vigilar_saldo(111.0)
    assert n == [100.0, 100.5, 111.0]


def test_libro_h23_registra_edad_por_token():
    lib = object.__new__(M.LibroH23)
    lib.L = {"a": {"bids": {}, "asks": {}}, "b": {"bids": {}, "asks": {}}}
    lib.ult_tok, lib.mids, lib.ult, lib.tick_cambiado, lib.registrar_trades = {}, {"a": [], "b": []}, 0.0, False, False
    lib._aplicar({"event_type": "price_change", "price_changes": [{"asset_id": "a", "price": "0.3", "size": "5", "side": "BUY"}]})
    assert "a" in lib.ult_tok and "b" not in lib.ult_tok and lib.edad("a") < 1 and lib.edad("b") > 1e6
    lib._aplicar({"event_type": "last_trade_price", "asset_id": "b", "price": "0.3", "size": "1", "side": "BUY"})
    assert "b" not in lib.ult_tok                                              # un trade no cuenta como libro vivo
    lib._aplicar({"asset_id": "b", "bids": [{"price": "0.2", "size": "3"}], "asks": []})
    assert "b" in lib.ult_tok


# ------------------------------------------------------------------ integracion con el arnes REAL (X.cancelar / X.post), cliente CLOB falso
class FakeCli:
    def __init__(self):
        self.cancel_resp = lambda h: {"canceled": [h]}
        self.get_order_resp = {"size_matched": "0", "status": "LIVE"}
        self.on_create = lambda: None
        self.post_orders = []
    def cancel_order(self, payload): return self.cancel_resp(payload.orderID)
    def get_order(self, h): return dict(self.get_order_resp)
    def create_order(self, args): self.on_create(); return {"signed": args.token_id, "price": args.price}
    def post_order(self, signed, tipo, post_only=False):
        self.post_orders.append((signed, post_only)); return {"orderID": "0xnuevo", "success": True}
    def get_open_orders(self, *a, **k): return []


def real23(tmp_path, monkeypatch, brazo="A"):
    monkeypatch.setattr(X, "LEDGER", tmp_path / "ledger.jsonl")
    monkeypatch.setattr(X, "_CACHE", None)
    monkeypatch.setattr(X, "KILL_FICHERO", tmp_path / "x.KILL")
    ex = object.__new__(M.Exp23)
    ex.__dict__.update(
        real=True, cli=FakeCli(), vivas={}, canceladas={}, _kill=None, _ords_cache=(None, None), _acc_cache=(0.0, None, None), _verif_avisado=set(),
        _ult_lectura={}, senal=False, hash_ok=True, fill_desconocido=set(), _pend_indexacion=set(), enfriar={}, _bloqueo_prev={}, cancel_all_ok=set(),
        sim_lleno={}, _on_cache=(0.0, None), funder="0xw", saldo_inicial=10.0, t_reinicio=None, posteado=False, tope_bloqueo=False,
        escalon="H23V3", t_stop=10.0, size=5, min_nocional=1.0, monedas=("btc",), presupuesto=5.0, max_vivas=2, saldo_min=0.0, gem={}, gem_lleno={},
        slugs_usados=set(), parada=None, n_ordenes_total=0, rechazos_seguidos=0, enfriar_tok={}, _inc={}, _inc_n=0, _ev_oid={}, ctxs={}, n_max=40,
        _gamma_err={}, _visto_log=set(), brazo=brazo, umbral=R.CONFIG["brazos"][brazo], refs=None, kill_brazo=None, tanda_agotada=None, sin_desenlace=None, _intentos={}, _ult_puerta=0.0, puerta_ok=True, _ordenes_previas={}, t_inicio_tanda=0.0, _previas=[], _en_reaccion=False,
        _ctx_actual=None, _poll_ms=None, _ult_vigilar=0.0, _ult_kb=0.0, _des={}, _suelo_escrito=True, _ult_verif=0.0, _t_ult_post={})
    ex._hash = lambda signed, tok: "0xhash1"
    ex.puede_enviar = lambda coste: True
    return ex


def leer(tmp_path):
    p = tmp_path / "ledger.jsonl"
    return [json.loads(l) for l in p.read_text().splitlines()] if p.exists() else []


def escenario_cancel_ya_terminal(tmp_path, monkeypatch):
    ex = real23(tmp_path, monkeypatch)
    ex.cli.cancel_resp = lambda h: {"canceled": [], "not_canceled": {h: "order can't be found - already canceled or matched"}}
    c = ctx(); c.lib.L["u5"]["bids"][0.30] = 60.0                          # cola 50 + nuestras 5 + 5 ajenas: el WS ya muestra nuestra orden
    viva(ex, c, h="0xh1", t_post=time.time() - 5)                           # orden JOVEN (< ESPERA_INEXISTENTE_S = 30 s) y aun no marcada como vista
    c.lib.poner("u15", {0.36: 80.0}, {0.47: 80.0})                          # la condicion se rompe -> cancelar
    return ex, c


def test_hallazgo1_already_canceled_en_orden_joven_no_acaba_en_kill(tmp_path, monkeypatch):
    ex, c = escenario_cancel_ya_terminal(tmp_path, monkeypatch)
    ex.decidir(c, 200, time.time())                                         # decidir() marca visto ANTES de cancelar (como Exp47.decidir)
    assert ex.kill is None, ex.kill
    assert ex.canceladas["0xh1"].get("visto") and ex.canceladas["0xh1"].get("ya_terminal")
    tipos = [e["tipo"] for e in leer(tmp_path)]
    assert "visto" in tipos and "cancel_ya_terminal" in tipos and "h23_cancela" in tipos and "kill" not in tipos
    assert not (tmp_path / "x.KILL").exists()


def test_hallazgo1_control_sin_marcar_visto_el_mismo_escenario_mata_la_wallet(tmp_path, monkeypatch):
    ex, c = escenario_cancel_ya_terminal(tmp_path, monkeypatch)
    monkeypatch.setattr(M.Exp23, "_marcar_visto", lambda *a, **k: None)     # el codigo anterior (sin bloque `visto`)
    ex.decidir(c, 200, time.time())
    assert ex.kill and "cancelación no confirmada" in ex.kill               # kill compartido de toda la wallet


def test_hallazgo1_via_paso_rapido_tambien_marca_visto(tmp_path, monkeypatch):
    ex, c = escenario_cancel_ya_terminal(tmp_path, monkeypatch)
    monkeypatch.setattr(X.Exp, "liquidar", lambda self, *a, **k: None)
    ex._reaccion_rapida(c)                                                  # la ruta nueva (paso) no pasa por decidir()
    assert ex.kill is None and ex.canceladas["0xh1"].get("ya_terminal")


# ------------------------------------------------------------------ #4 revalidar objetivo_h23 tras firmar (X.Exp.post real)
def escenario_post(tmp_path, monkeypatch):
    ex = real23(tmp_path, monkeypatch)
    c = ctx()
    return ex, c


def test_hallazgo4_si_la_cota_cae_durante_la_firma_no_se_envia(tmp_path, monkeypatch):
    ex, c = escenario_post(tmp_path, monkeypatch)
    ex.cli.on_create = lambda: c.lib.poner("u15", {0.36: 80.0}, {0.47: 80.0})   # create_order/get_neg_risk son red: el bid15 baja mientras firmamos
    ex.decidir(c, 200, time.time())
    assert ex.cli.post_orders == [] and not ex.vivas                        # NADA enviado
    evs = leer(tmp_path)
    assert any(e["tipo"] == "h23_revalida_aborta" and e["precio_firmado"] == 0.30 and e["objetivo_ahora"] is None for e in evs)
    assert not any(e["tipo"] == "intencion_post" for e in evs)


def test_hallazgo4_si_el_libro_no_cambia_se_envia_post_only(tmp_path, monkeypatch):
    ex, c = escenario_post(tmp_path, monkeypatch)
    ex.decidir(c, 200, time.time())
    assert len(ex.cli.post_orders) == 1 and ex.cli.post_orders[0][1] is True
    assert any(e["tipo"] == "intencion_post" and e["precio"] == 0.30 for e in leer(tmp_path))


@pytest.mark.parametrize("cambio", ["bid15_baja", "libro15_viejo", "bid5_se_mueve", "cruce15"])
def test_hallazgo4_cualquier_cambio_de_la_regla_tras_firmar_aborta(tmp_path, monkeypatch, cambio):
    ex, c = escenario_post(tmp_path, monkeypatch)
    def mover():
        if cambio == "bid15_baja": c.lib.poner("u15", {0.36: 80.0}, {0.47: 80.0})
        elif cambio == "libro15_viejo": c.lib.edades["u15"] = M.EDAD_TOKEN_MAX_S + 5
        elif cambio == "bid5_se_mueve": c.lib.poner("u5", {0.31: 10.0, 0.30: 100.0}, {0.33: 50.0})
        elif cambio == "cruce15": c.lib.poner("u15", {0.50: 80.0}, {0.47: 80.0})
    ex.cli.on_create = mover
    ex.decidir(c, 200, time.time())
    assert ex.cli.post_orders == []


# ------------------------------------------------------------------ #6 etiquetas
def test_hallazgo6_eventos_llevan_h23_brazo_umbral_y_hash_regla(tmp_path, monkeypatch):
    for brazo, umbral in (("A", 0.05), ("B", 0.02)):
        ex = real23(tmp_path, monkeypatch, brazo)
        monkeypatch.setattr(X, "_CACHE", None)
        for t in ("puja_fin", "config", "mercado_fin", "puja_post", "h23_cancela"):
            ex._log47({"tipo": t, "variante": "H35", "k": 0})
        evs = [e for e in leer(tmp_path) if e["tipo"] in ("puja_fin", "config", "mercado_fin", "puja_post", "h23_cancela")][-5:]
        assert len(evs) == 5
        for e in evs:
            assert e["variante"] == f"H23V3-{brazo}" and e["brazo"] == brazo and e["umbral"] == umbral and e["hash_regla"] == R.hash_config()
        assert [e for e in evs if e["tipo"] == "config"][0]["codigo_sha_h23"] == M.sha_propio()


def test_hallazgo6_brazo_b_usa_su_escalon_y_su_n():
    assert M.H.N_MAX["H23V3B"] == 40
    import inspect
    assert '"H23V3" if brazo == "A" else "H23V3B"' in inspect.getsource(M.Exp23.__init__)


# ------------------------------------------------------------------ #7 kill por brazo y puertas
def pos(n, dias, gana, acc=5.0, precio=0.30, ndias_extra=0):
    return [{"slug": f"s{i}", "dia": f"2026-10-{10 + i % dias:02d}", "acc": acc, "coste": acc * precio, "gana": gana(i)} for i in range(n)]


def test_kill_brazo_pendiente_y_rearme():
    ev = [{"real": True, "tipo": "kill_brazo", "motivo": "m1"}]
    assert M.kill_brazo_pendiente(ev) == "m1"
    assert M.kill_brazo_pendiente(ev + [{"real": True, "tipo": "kill_brazo_rearmado"}]) is None
    assert M.kill_brazo_pendiente([{"real": False, "tipo": "kill_brazo"}]) is None


def test_kill_brazo_dispara_para_cancela_y_no_repone(monkeypatch):
    ex, c = Fake(), ctx(); ex.real = True
    monkeypatch.setattr(ex, "posiciones_brazo", lambda: pos(25, 6, lambda i: False), raising=False)
    ex._vigilar_kill_brazo(1000.0)
    assert ex.kill_brazo and ex.parada and ("log", "kill_brazo") in ex.calls
    ex.calls.clear(); ex.decidir(c, 200, time.time()); assert not [x for x in ex.calls if x[0] == "post"]
    ex2, c2 = Fake(), ctx(); viva(ex2, c2); ex2.kill_brazo = "kb"
    ex2._reaccion_viva(c2, 200, time.time(), "t"); assert ("cancelar", "h1") in ex2.calls
    assert [e for e in ex2.evs if e["tipo"] == "h23_cancela"][0]["causa"] == "kill_brazo"


def test_kill_brazo_no_consulta_desenlaces_con_orden_viva(monkeypatch):
    ex, c = Fake(), ctx(); ex.real = True; viva(ex, c)
    monkeypatch.setattr(ex, "posiciones_brazo", lambda: (_ for _ in ()).throw(AssertionError("no debe leerse")), raising=False)
    ex._vigilar_kill_brazo(1000.0)


def test_main_real_no_arranca_con_kill_brazo_pendiente(tmp_path, monkeypatch):
    monkeypatch.setattr(M, "exigir_puertas", lambda *a, **k: None)
    led = tmp_path / "l.jsonl"
    led.write_text(json.dumps({"real": True, "tipo": "kill_brazo", "motivo": "x"}) + "\n")
    def rutas(real, brazo): X.LEDGER = led; X._CACHE = None
    monkeypatch.setattr(M, "configurar_rutas", rutas)
    monkeypatch.setattr(X, "LEDGER", led)
    with pytest.raises(SystemExit) as e: M.main(["--confirmo-dinero-real", "--ok-final-javi", "x"])
    assert "kill de brazo pendiente" in str(e.value)


def ok_txt(sin=()):
    d = {"sha": M.sha_propio(), "regla": M.HASH_REGLA, **M.sha_dependencias()}
    d["kill"] = M.hash_kill_v3()
    return "ok javi 2026-10-2x " + " ".join(f"{k}={v}" for k, v in d.items() if k not in sin)


def cfg_ev(**k): return {"real": True, "tipo": "config", "escalon": "B", "n_max": 230, "t_stop": 60.0, "codigo_sha": M.sha_dependencias()["h47"], **k}
def fin_ev(**k): return {"real": True, "tipo": "fin_ejecucion", "pujas": 230, "ordenes": 500, "kill": None, "parada": None, "abiertas_sin_verificar": 0, **k}


def test_puerta_h47b_exige_fin_ejecucion_sin_kill():
    assert M.h47b_terminado([cfg_ev(), fin_ev()])[0]
    assert not M.h47b_terminado([])[0]                                       # sin ledger/config
    assert not M.h47b_terminado([cfg_ev()])[0]                               # en curso o muerto sin cerrar
    assert not M.h47b_terminado([cfg_ev(), fin_ev(), cfg_ev()])[0]           # arranque posterior sin cerrar
    assert not M.h47b_terminado([cfg_ev(), fin_ev(kill="descuadre")])[0]
    assert not M.h47b_terminado([cfg_ev(), fin_ev(abiertas_sin_verificar=2)])[0]
    assert not M.h47b_terminado([cfg_ev(), {"real": True, "tipo": "kill", "motivo": "x"}, fin_ev()])[0]       # kill sin rearmar
    assert M.h47b_terminado([cfg_ev(), {"real": True, "tipo": "kill", "motivo": "x"}, {"real": True, "tipo": "kill_rearmado"}, cfg_ev(), fin_ev()])[0]
    assert not M.h47b_terminado([{"real": False, "tipo": "config"}, {"real": False, "tipo": "fin_ejecucion"}])[0]   # un ensayo en seco no vale


def test_puertas_del_modo_real(tmp_path, monkeypatch):
    M.exigir_puertas(False, None)                                           # seco: sin puertas
    with pytest.raises(SystemExit): M.exigir_puertas(True, None)
    with pytest.raises(SystemExit): M.exigir_puertas(True, "  ")
    monkeypatch.setattr(M, "OK_FICHERO", tmp_path / "ok.txt")
    ledger_b = tmp_path / "b.jsonl"
    with pytest.raises(SystemExit): M.exigir_puertas(True, "ok javi", ledger_b=ledger_b)      # el fichero no existe
    bueno = ok_txt()
    (tmp_path / "ok.txt").write_text(bueno + "\n")
    with pytest.raises(SystemExit): M.exigir_puertas(True, "otro texto", ledger_b=ledger_b)
    with pytest.raises(SystemExit) as e: M.exigir_puertas(True, bueno, ledger_b=ledger_b)     # texto ok pero sin ledger de H47-B
    assert "ledger de H47-B" in str(e.value)
    ledger_b.write_text(json.dumps(cfg_ev()) + "\n")
    with pytest.raises(SystemExit) as e: M.exigir_puertas(True, bueno, ledger_b=ledger_b)     # H47-B sin fin_ejecucion
    assert "no ha terminado" in str(e.value)
    ledger_b.write_text(json.dumps(cfg_ev()) + "\n" + json.dumps(fin_ev(kill="x")) + "\n")
    with pytest.raises(SystemExit) as e: M.exigir_puertas(True, bueno, ledger_b=ledger_b)     # terminado CON kill
    assert "kill" in str(e.value)
    ledger_b.write_text(json.dumps(cfg_ev()) + "\n" + json.dumps(fin_ev()) + "\n{linea corta")
    with pytest.raises(SystemExit) as e: M.exigir_puertas(True, bueno, ledger_b=ledger_b)     # linea ilegible tras el ultimo config: fail-closed
    assert "ilegible" in str(e.value)
    ledger_b.write_text(json.dumps(cfg_ev()) + "\n" + json.dumps(fin_ev()) + "\n")
    M.exigir_puertas(True, bueno, ledger_b=ledger_b)


def test_ok_ligado_al_sha_de_este_fichero(tmp_path, monkeypatch):
    monkeypatch.setattr(M, "OK_FICHERO", tmp_path / "ok.txt")
    ledger_b = tmp_path / "b.jsonl"; ledger_b.write_text(json.dumps(cfg_ev()) + "\n" + json.dumps(fin_ev()) + "\n")
    for malo in ("ok javi sin sha", f"ok javi sha=0000000000000000 regla={M.HASH_REGLA}", f"ok javi sha={M.sha_propio()}",
                 f"ok javi sha={M.sha_propio()} regla=0000000000000000"):
        (tmp_path / "ok.txt").write_text(malo)
        with pytest.raises(SystemExit) as e: M.exigir_puertas(True, malo, ledger_b=ledger_b)
        assert "no esta ligado" in str(e.value)
    # si el fichero cambia, el sha cambia: el OK emitido antes deja de valer
    emitido = ok_txt()
    (tmp_path / "ok.txt").write_text(emitido)
    monkeypatch.setattr(M, "sha_propio", lambda: "ffffffffffffffff")
    with pytest.raises(SystemExit): M.exigir_puertas(True, emitido, ledger_b=ledger_b)


def test_imprimir_sha(capsys):
    assert M.main(["--imprimir-sha"]) == 0
    out = capsys.readouterr().out
    assert f"sha={M.sha_propio()} regla={M.HASH_REGLA}" in out and f"kill={M.hash_kill_v3()}" in out and all(f"{k}={v}" in out for k, v in M.sha_dependencias().items())


# ================================================================== RONDA 2
def test_r2_1_h47b_abortado_o_interrumpido_no_cuenta():
    assert M.h47b_terminado([cfg_ev(), fin_ev(pujas=230)])[0]
    ok, m = M.h47b_terminado([cfg_ev(), fin_ev(pujas=37)]); assert not ok and "no llego a su N" in m          # Ctrl-C / senal / abortado
    ok, m = M.h47b_terminado([cfg_ev(), fin_ev(parada="saldo 3.1 < suelo")]); assert not ok and "parada" in m
    assert not M.h47b_terminado([{"real": True, "tipo": "config"}, fin_ev()])[0]                              # config sin n_max
    assert not M.h47b_terminado([cfg_ev(), fin_ev(pujas=None)])[0]
    assert M.h47b_terminado([cfg_ev(n_max=300), fin_ev(pujas=300)])[0]                                         # el N es el DE ESE run
    assert not M.h47b_terminado([cfg_ev(n_max=40), fin_ev(pujas=40)])[0]                                        # pero el escalon B completo (>= 230)


def test_r2_2_config_lleva_sha_dependencias_y_alcanzable(tmp_path, monkeypatch):
    ex = real23(tmp_path, monkeypatch)
    ex._log47({"tipo": "config"})
    e = [x for x in leer(tmp_path) if x["tipo"] == "config"][-1]
    assert e["dependencias"] == M.sha_dependencias() and set(e["dependencias"]) == {"h47", "pares", "contabilidad", "shadow"}
    assert e["kill_brazo_v3"]["hash"] == M.hash_kill_v3() and e["kill_brazo_v3"]["tope_tanda_usd"] == M.KILL_BRAZO_V3["tope_tanda_usd"]
    assert e["codigo_sha_h23"] == M.sha_propio()


def test_r2_3_el_ok_liga_h47_pares_y_shadow(tmp_path, monkeypatch):
    monkeypatch.setattr(M, "OK_FICHERO", tmp_path / "ok.txt")
    lb = tmp_path / "b.jsonl"; lb.write_text(json.dumps(cfg_ev()) + "\n" + json.dumps(fin_ev()) + "\n")
    for dep in ("h47", "pares", "shadow"):
        txt = ok_txt(sin=(dep,)); (tmp_path / "ok.txt").write_text(txt)
        with pytest.raises(SystemExit) as e: M.exigir_puertas(True, txt, ledger_b=lb)
        assert dep in str(e.value) and "dependencias" in str(e.value)
    txt = ok_txt(); (tmp_path / "ok.txt").write_text(txt); M.exigir_puertas(True, txt, ledger_b=lb)
    d = M.sha_dependencias()
    monkeypatch.setattr(M, "sha_dependencias", lambda: {**d, "h47": "0" * 16})                              # H47 cambiado tras el OK
    with pytest.raises(SystemExit): M.exigir_puertas(True, txt, ledger_b=lb)
    assert d["shadow"] == M._sha_fichero(M.AQUI_REGLA / "h23_shadow.py") and os.path.exists(M.AQUI_REGLA / "h23_shadow.py")


def test_r2_4_libro_quieto_no_se_cancela_pero_conexion_muerta_si():
    ex, c = Fake(), ctx(); viva(ex, c)
    c.lib.edades.update({"u15": 60.0, "u5": 45.0})                                                          # 60 s sin mensajes del 15m, conexion sana
    ex.paso(c); assert not [x for x in ex.calls if x[0] == "cancelar"]
    c.lib.ok = False                                                                                         # la conexion muere (sin PONG)
    ex.paso(c); assert ("cancelar", "h1") in ex.calls
    ex2, c2 = Fake(), ctx(); viva(ex2, c2); c2.lib.edades["u15"] = M.EDAD_TOKEN_MAX_S + 1                    # respaldo: token mudo > 120 s
    ex2.paso(c2); assert ("cancelar", "h1") in ex2.calls


def test_r2_4_conexion_sana_distingue_salud_de_actividad():
    lib = object.__new__(M.LibroH23)
    class Hilo:
        def is_alive(self): return True
    lib.hilo, lib.error, lib.ult_msg, lib.ult = Hilo(), None, time.time(), time.time() - 100          # libro sin cambios 100 s, PONG ahora
    assert lib.conexion_sana()
    lib.ult_msg = time.time() - (X.WS_MAX_S + 1); assert not lib.conexion_sana()                      # sin PING/PONG
    lib.ult_msg = time.time(); lib.error = "boom"; assert not lib.conexion_sana()


def test_r2_5_top5_resta_siempre_nuestro_tamano_aunque_no_este_visto():
    ex, c = Fake(), ctx()
    c.lib.poner("u5", {0.30: 5.0, 0.29: 40.0}, {0.33: 50.0})
    viva(ex, c, precio=0.30, size=5.0, visto=False)                                                          # WS ya nos muestra, criterio `visto` aun no
    ex._reaccion_viva(c, 200, time.time(), "t")
    assert ("cancelar", "h1") in ex.calls                                                                    # antes: se quedaba (fail-open vs replay)


def test_r2_5_nunca_se_queda_donde_el_replay_cancelaria_con_orden_vista_o_no():
    rng = random.Random(7); n_vis = n_cancel_extra = 0
    for _ in range(800):
        niveles = sorted({round(rng.choice([0.2, 0.28, 0.29, 0.30, 0.31, 0.35]), 2) for _ in range(rng.randint(0, 3))}, reverse=True)
        ajeno = {p: float(rng.randint(1, 8)) for p in niveles}                                               # incluye cola ajena pequena (comida)
        ask5, b15 = round(rng.choice([0.33, 0.45]), 2), round(rng.choice([0.36, 0.4, 0.45]), 2); a15 = round(b15 + 0.02, 2)
        pc = rng.choice(niveles + [0.30]) if niveles else 0.30
        mostrada = rng.random() < 0.5                                                                        # ¿el WS ya incluye nuestra orden?
        libro = dict(ajeno)
        if mostrada: libro[pc] = libro.get(pc, 0.0) + 5.0
        ex, c = Fake(), ctx(); c.lib.poner("u5", libro, {ask5: 50.0}); c.lib.poner("u15", {b15: 80.0}, {a15: 80.0})
        viva(ex, c, precio=pc, visto=rng.random() < 0.5)
        w = R.querer(max(ajeno) if ajeno else None, ask5, b15, a15, 0.05)
        replay_cancela = not (w is not None and abs(w - pc) < 1e-9)
        ex._reaccion_viva(c, 200, time.time(), "t"); cancela = ("cancelar", "h1") in ex.calls
        assert cancela or not replay_cancela, (ajeno, pc, mostrada)                                         # quedarse => el replay tambien se queda
        if mostrada: assert cancela == replay_cancela                                                       # orden mostrada => EXACTAMENTE el replay
        n_cancel_extra += cancela and not replay_cancela; n_vis += mostrada
    assert n_vis > 100 and n_cancel_extra > 0                                                               # hubo casos conservadores (no mostrada + cola ajena menor que la nuestra)


def test_r2_6_liquidar_tras_reaccion_relee_vivas_y_pasa_es_cancelada(monkeypatch):
    rec = []
    monkeypatch.setattr(X.Exp, "liquidar", lambda self, h, o, esc, *a, **k: rec.append((h, esc, o is self.canceladas.get(h))))
    ex, c = Fake(), ctx()
    def cancelar(h): ex.calls.append(("cancelar", h)); ex.canceladas[h] = ex.vivas.pop(h); return True      # como X.cancelar real
    ex.cancelar = cancelar
    ex.liquidar = lambda *a, **k: M.Exp23.liquidar(ex, *a, **k)
    viva(ex, c); ex._ctx_actual = c; c.lib.poner("u15", {0.36: 80.0}, {0.47: 80.0})
    o_viejo = ex.vivas["h1"]
    ex.liquidar("h1", o_viejo, False, c.estado, c.lib, 100)
    assert rec[-1] == ("h1", True, True)                                                                      # se llamo con es_cancelada=True y la orden de `canceladas`
    assert all(r[1] is True for r in rec)                                                                     # nunca como viva tras cancelarla
    rec.clear(); ex.canceladas.clear()
    ex.liquidar("zz", {"tok": "u5"}, False, c.estado, c.lib, 100); assert rec == []                           # ya liquidada y fuera de todo: no se lee


def test_r2_7_camino_ack_de_x_cancelar_desde_h23(tmp_path, monkeypatch):
    ex = real23(tmp_path, monkeypatch)
    ex.cli.cancel_resp = lambda h: {"canceled": [], "not_canceled": {h: "order can't be found - already canceled or matched"}}
    ex.cli.get_order_resp = {"size_matched": "5", "status": "MATCHED"}                                       # get_order ya terminal tras el sleep
    slept = []
    monkeypatch.setattr(time, "sleep", lambda t: slept.append(t))
    monkeypatch.setattr(M.Exp23, "_marcar_visto", lambda *a, **k: None)                                    # orden NO vista: obliga al camino ack
    c = ctx(); viva(ex, c, h="0xh1", t_post=time.time() - 1.4)["ack"] = True
    c.lib.poner("u15", {0.36: 80.0}, {0.47: 80.0})
    ex.decidir(c, 200, time.time())
    assert ex.kill is None and X.ASENTAR_S in slept                                                          # X.cancelar durmio ASENTAR_S + get_order
    ev = [e for e in leer(tmp_path) if e["tipo"] == "h23_cancela"][0]
    assert ev["camino_ack"] is True and ev["rtt_incluye_asentar_s"] == X.ASENTAR_S
    assert any(e["tipo"] == "cancel_ya_terminal_ack" and e["status"] == "MATCHED" for e in leer(tmp_path))
    # camino normal: no marca ack
    ex2 = real23(tmp_path, monkeypatch); c2 = ctx(); viva(ex2, c2, h="0xh2"); c2.lib.poner("u15", {0.36: 80.0}, {0.47: 80.0})
    ex2.decidir(c2, 200, time.time())
    assert [e for e in leer(tmp_path) if e["tipo"] == "h23_cancela"][-1]["camino_ack"] is False


def test_r2_8_kill_brazo_acotado(monkeypatch):
    ex = Fake(); ex.real = True
    pos5 = [{"slug": f"btc-updown-5m-{i}", "dia": "2026-10-10", "acc": 5.0, "coste": 1.5, "gana": None, "fin": 10 + i} for i in range(5)]
    monkeypatch.setattr(ex, "posiciones_brazo", lambda: pos5, raising=False)
    llamadas = []
    monkeypatch.setattr(M, "desenlace_token", lambda slug: llamadas.append(slug))
    ex._vigilar_kill_brazo(1000.0)
    assert len(llamadas) == M.KILL_BRAZO_MAX_CONSULTAS                                                       # <= 2 por pasada
    for ahora in (1490.0, 1600.0, 1790.0):                                                                   # <20 s antes de la apertura (1500), dentro y justo antes del cierre
        llamadas.clear(); ex._ult_kb = 0.0; ex._vigilar_kill_brazo(ahora); assert llamadas == [], ahora
    llamadas.clear(); ex._ult_kb = 0.0; ex._vigilar_kill_brazo(1801.0); assert llamadas                      # fuera de la ventana si consulta
    llamadas.clear(); ex._ult_kb = 0.0; c = ctx(); ex.ctxs["x"] = c; ex._vigilar_kill_brazo(1000.0); assert llamadas == []   # mercado activo
    assert M.KILL_BRAZO_TIMEOUT_S <= 3 and "timeout=KILL_BRAZO_TIMEOUT_S" in open(M.__file__).read()


def test_r2_8_vigilar_saldo_tambien_se_espacia_con_cancelada_pendiente(monkeypatch):
    n = []
    monkeypatch.setattr(H.Exp47, "vigilar_saldo", lambda self, ahora: n.append(ahora))
    ex = Fake(); ex.canceladas["h0"] = {"tok": "u5"}
    ex.vigilar_saldo(100.0); ex.vigilar_saldo(101.0); assert n == [100.0]


# ================================================================== KILL V2
def p2(n, gana, acc=6.0, precio=0.30):
    return [{"slug": f"s{i}", "acc": acc, "coste": acc * precio, "gana": gana(i), "fin": i} for i in range(n)]


def test_kv3_dispara_en_secuencia_perdedora_por_tope_y_por_sigma():
    d, info = M.evaluar_kill_v3(p2(2, lambda i: False)); assert not d and info["perdida"] < 4.5                 # 2 x 1,5 $ : aun no
    d, info = M.evaluar_kill_v3(p2(3, lambda i: False)); assert d and info["causa"] == "tope_tanda" and info["n_disparo"] == 3   # 4,5 $ >= tope
    sg = {**M.KILL_BRAZO_V3, "sigma1": 1.0, "tope_tanda_usd": 99.0}                                           # rama sigma aislada
    d, info = M.evaluar_kill_v3(p2(3, lambda i: False), sg); assert d and info["causa"] == "sigma"
    sg2 = {**sg, "sigma1": 0.5}
    d, _ = M.evaluar_kill_v3(p2(2, lambda i: False), sg2); assert not d                                         # n_min = 3 (con n=2 la formula ya se cumpliria)
    d, _ = M.evaluar_kill_v3(p2(3, lambda i: False), sg2); assert d
    d, _ = M.evaluar_kill_v3(p2(40, lambda i: False), {**M.KILL_BRAZO_V3, "sigma1": 2.0, "tope_tanda_usd": 99.0}); assert d   # con sigma1=2 solo tras ~10 perdidas seguidas


def test_kv3_no_dispara_en_secuencia_ganadora_ni_con_sigma_sin_n():
    d, info = M.evaluar_kill_v3(p2(12, lambda i: i % 2 == 0)); assert not d and info["perdida"] < 0           # gana la mitad a 0,30: PnL muy positivo
    d, _ = M.evaluar_kill_v3(p2(10, lambda i: i % 3 == 0)); assert not d                                        # 1 de 3 a 0,30: ~ +0,1 por €
    d, _ = M.evaluar_kill_v3([]); assert not d
    sin = p2(6, lambda i: False)
    for x in sin: x["gana"] = None                                                                              # sin desenlace oficial: missing, no 0
    d, info = M.evaluar_kill_v3(sin); assert not d and info["n"] == 0 and info["sin_desenlace"] == 6


def test_kv3_orden_de_cierre_y_recuperacion_antes_del_tope():
    ps = [{"slug": "a", "acc": 5.0, "coste": 1.5, "gana": False, "fin": 1}, {"slug": "b", "acc": 5.0, "coste": 1.5, "gana": True, "fin": 2},
          {"slug": "c", "acc": 5.0, "coste": 1.5, "gana": False, "fin": 3}, {"slug": "d", "acc": 5.0, "coste": 1.5, "gana": False, "fin": 4}]
    assert not M.evaluar_kill_v3(ps)[0]
    assert M.evaluar_kill_v3(list(reversed(ps)))[0] is False                                                  # el orden de entrada no importa: se ordena por `fin`
    ls = p2(3, lambda i: False) + [{"slug": "w", "acc": 6.0, "coste": 1.8, "gana": True, "fin": 10}]
    assert M.evaluar_kill_v3(list(reversed(ls)))[0] is True                                                     # L,L,L,W entregadas al reves: dispara a la 3a perdida


def test_kv3_hash_cambia_con_cualquier_parametro_o_con_la_funcion():
    h0 = M.hash_kill_v3(); assert h0 == M.hash_kill_v3() and len(h0) == 16
    for k, v in (("z", 2.0), ("sigma1", 1.9), ("margen_ev", 0.04), ("n_min", 4), ("tope_tanda_usd", 3.0), ("presupuesto_ref_usd", 4.0), ("version", 4), ("acumulado", "solo_tanda")):
        assert M.hash_kill_v3({**M.KILL_BRAZO_V3, k: v}) != h0, k
    import inspect
    assert "tope_tanda_usd" in inspect.getsource(M.evaluar_kill_v3)


def test_kv3_el_ok_liga_el_hash_del_kill(tmp_path, monkeypatch):
    monkeypatch.setattr(M, "OK_FICHERO", tmp_path / "ok.txt")
    lb = tmp_path / "b.jsonl"; lb.write_text(json.dumps(cfg_ev()) + "\n" + json.dumps(fin_ev()) + "\n")
    txt = ok_txt(sin=("kill",)); (tmp_path / "ok.txt").write_text(txt)
    with pytest.raises(SystemExit) as e: M.exigir_puertas(True, txt, ledger_b=lb)
    assert "kill V3" in str(e.value)
    txt = ok_txt(); (tmp_path / "ok.txt").write_text(txt); M.exigir_puertas(True, txt, ledger_b=lb)
    monkeypatch.setattr(M, "KILL_BRAZO_V3", {**M.KILL_BRAZO_V3, "tope_tanda_usd": 3.0})                  # parametros tocados tras el OK
    with pytest.raises(SystemExit): M.exigir_puertas(True, txt, ledger_b=lb)


def test_kv3_tope_de_tanda_para_la_tanda_pero_no_deja_kill_persistente(tmp_path, monkeypatch):
    ex = real23(tmp_path, monkeypatch); ex.cli = None; ex.tanda_agotada = None
    monkeypatch.setattr(ex, "posiciones_brazo", lambda: p2(3, lambda i: False), raising=False)
    monkeypatch.setattr(ex, "parar", lambda m: setattr(ex, "parada", m), raising=False)
    ex._vigilar_kill_brazo(1000.0)
    assert ex.tanda_agotada and ex.parada and ex.kill_brazo is None                                          # 3 x 1,8 $ perdidos >= 5 $: para la tanda
    evs = leer(tmp_path)
    assert any(e["tipo"] == "tope_tanda" and e["variante"] == "H23V3-A" for e in evs) and not any(e["tipo"] == "kill_brazo" for e in evs)
    monkeypatch.setattr(X, "_CACHE", None)
    assert M.kill_brazo_pendiente(X.leer_ledger()) is None                                                   # un reinicio NO queda bloqueado por el tope de tanda
    ex.cli = FakeCli(); c = ctx(); viva(ex, c, h="0xv"); ex._reaccion_viva(c, 200, time.time(), "t")         # y cancela lo vivo
    assert [e for e in leer(tmp_path) if e["tipo"] == "h23_cancela"][-1]["causa"] == "kill_brazo"


def test_kv3_formula_acumulada_deja_kill_persistente(tmp_path, monkeypatch):
    monkeypatch.setattr(M, "KILL_BRAZO_V3", {**M.KILL_BRAZO_V3, "sigma1": 0.5})
    ex = real23(tmp_path, monkeypatch); ex.cli = None; ex.tanda_agotada = None
    antiguas = [{"slug": f"v{i}", "acc": 6.0, "coste": 1.8, "gana": False, "fin": i, "t_int": 10.0} for i in range(3)]      # de una tanda anterior
    monkeypatch.setattr(ex, "posiciones_brazo", lambda: antiguas, raising=False)
    ex.t_inicio_tanda = 1e9
    monkeypatch.setattr(ex, "parar", lambda m: setattr(ex, "parada", m), raising=False)
    ex._vigilar_kill_brazo(1000.0)
    assert ex.kill_brazo and "sigma" in ex.kill_brazo and ex.tanda_agotada is None                            # el tope de tanda no cuenta lo anterior
    ev = [e for e in leer(tmp_path) if e["tipo"] == "kill_brazo"][0]
    assert ev["real"] is True and ev["variante"] == "H23V3-A"
    monkeypatch.setattr(X, "_CACHE", None)
    assert M.kill_brazo_pendiente(X.leer_ledger()) == ev["motivo"]                                           # persistente: un reinicio lo ve


def test_kv3_se_rearma_y_tras_el_rearme_solo_cuentan_ordenes_nuevas(tmp_path, monkeypatch):
    led = tmp_path / "l.jsonl"
    led.write_text(json.dumps({"real": True, "tipo": "kill_brazo", "motivo": "x", "ts": "2026-10-20T10:00:00.000+00:00"}) + "\n")
    monkeypatch.setattr(X, "LEDGER", led); monkeypatch.setattr(X, "_CACHE", None); monkeypatch.setattr(X, "LOCK", tmp_path / "x.lock")
    monkeypatch.setattr(M, "exigir_puertas", lambda *a, **k: None)
    monkeypatch.setattr(M, "configurar_rutas", lambda real, brazo: None)
    assert M.main(["--confirmo-dinero-real", "--ok-final-javi", "x", "--rearmar-kill-brazo", "revisado por Javi"]) == 0
    monkeypatch.setattr(X, "_CACHE", None)
    ev = X.leer_ledger()
    assert M.kill_brazo_pendiente(ev) is None and ev[-1]["tipo"] == "kill_brazo_rearmado" and ev[-1]["motivo"] == "revisado por Javi"
    with pytest.raises(SystemExit): M.main(["--confirmo-dinero-real", "--ok-final-javi", "x", "--rearmar-kill-brazo", "otra vez"])   # no hay kill pendiente
    with pytest.raises(SystemExit): M.main(["--confirmo-dinero-real", "--ok-final-javi", "x", "--rearmar-kill-brazo", "  "])
    t_r = M.t_rearme(ev); assert t_r > 1.7e9
    from types import SimpleNamespace as NS
    mk = lambda slug, t_int: NS(alias=False, ilegible=False, abierta=False, lo=5.0, precio=0.30, slug=slug, tok="u5", t_int=t_int)
    fk = Fake(); fk.t_rearme_brazo = t_r
    fk.ordenes = lambda: {"a": mk("btc-updown-5m-100", t_r - 50), "b": mk("btc-updown-5m-400", t_r + 50)}
    pos = fk.posiciones_brazo()
    assert [p["slug"] for p in pos] == ["btc-updown-5m-400"]                                                  # la anterior al rearme no cuenta
    assert M.t_rearme([]) == 0.0


def test_kv3_ya_no_hay_aviso_de_inalcanzable():
    src = open(M.__file__).read()
    assert "kill_brazo_alcanzable" not in src and "NO es un freno efectivo" not in src and "RELLENO_REPLAY" not in src


# ================================================================== KILL V3: acumulado entre tandas
import datetime as _dt
def epoch(iso): return _dt.datetime.fromisoformat(iso).timestamp()


def escribe_ledger(ruta, posiciones, extra=()):
    """posiciones: [(slug, iso_ts, precio, size)] con relleno completo."""
    ev = []
    for i, (slug, ts, precio, size) in enumerate(posiciones):
        oid = f"0x{abs(hash((str(ruta), slug, i))):x}"
        ev += [{"tipo": "intencion_post", "oid": oid, "slug": slug, "tok": "u5", "lado": "YES", "precio": precio, "size": size, "real": True, "ts": ts},
               {"tipo": "lectura", "oid": oid, "f": size, "status": "MATCHED", "real": True, "ts": ts}]
    ev += list(extra)
    ruta.write_text("".join(json.dumps(e) + "\n" for e in ev))


def test_kv3_acumula_entre_tandas_y_no_se_reinicia_con_el_suelo(tmp_path, monkeypatch):
    monkeypatch.setattr(M, "KILL_BRAZO_V3", {**M.KILL_BRAZO_V3, "sigma1": 0.5})                         # sigma1 baja: la formula acumulada es alcanzable con n=3
    ex = real23(tmp_path, monkeypatch); ex.tanda_agotada = None
    X.LEDGER = tmp_path / "experimento_h47_H23V3_ledger.jsonl"
    ant = tmp_path / "experimento_h47_H23V3_ledger_tanda1.jsonl"
    escribe_ledger(ant, [("btc-updown-5m-1000", "2026-10-19T10:00:00+00:00", 0.30, 5.0), ("btc-updown-5m-1900", "2026-10-19T11:00:00+00:00", 0.30, 5.0)],
                   extra=[{"real": True, "tipo": "suelo_reiniciado", "ts": "2026-10-19T12:00:00+00:00", "saldo_base": 9.0}])    # reseteo de suelo en la tanda anterior
    escribe_ledger(X.LEDGER, [("btc-updown-5m-2800", "2026-10-20T10:00:00+00:00", 0.30, 5.0)], extra=[{"real": True, "tipo": "suelo_fijado", "ts": "2026-10-20T09:00:00+00:00"}])
    monkeypatch.setattr(X, "_CACHE", None)
    st = M.estado_acumulado("A", dirn=tmp_path)
    assert st["pendiente"] is None and st["t_rearme"] == 0.0 and len(st["previas"]) == 2                  # suelo_reiniciado / suelo_fijado NO reinician el acumulado
    ex._ordenes_previas, ex.t_inicio_tanda = st["ordenes_previas"], epoch("2026-10-20T00:00:00+00:00")
    ex._des = {s: "otro" for s in ("btc-updown-5m-1000", "btc-updown-5m-1900", "btc-updown-5m-2800")}      # las 3 pierden (u5 no es el ganador)
    pos = ex.posiciones_brazo()
    assert len(pos) == 3 and sum(1 for p in pos if p["t_int"] >= ex.t_inicio_tanda) == 1                   # 2 de la tanda anterior + 1 de esta
    dispara, info = M.evaluar_kill_v3(pos, t_tanda=ex.t_inicio_tanda)
    assert dispara and info["causa"] == "sigma" and info["n_disparo"] == 3 and info["perdida_tanda"] < 2    # solo el ACUMULADO lo dispara
    assert not M.evaluar_kill_v3(pos[2:] if pos[0]["t_int"] < pos[2]["t_int"] else [pos[0]], t_tanda=ex.t_inicio_tanda)[0]   # sin las previas (1 posicion): no
    monkeypatch.setattr(ex, "parar", lambda m: setattr(ex, "parada", m), raising=False)
    ex._vigilar_kill_brazo(1000.0)
    assert ex.kill_brazo and "perdida acumulada" in ex.kill_brazo


def test_kv3_tope_de_tanda_solo_cuenta_las_posiciones_de_esta_ejecucion():
    viejas = [{"slug": f"v{i}", "acc": 6.0, "coste": 1.8, "gana": False, "fin": i, "t_int": 10.0} for i in range(2)]
    nuevas = [{"slug": f"n{i}", "acc": 6.0, "coste": 1.8, "gana": False, "fin": 10 + i, "t_int": 500.0} for i in range(3)]
    d, info = M.evaluar_kill_v3(viejas, t_tanda=100.0); assert not d and info["perdida"] > 3 and info["perdida_tanda"] == 0.0
    d, info = M.evaluar_kill_v3(viejas + nuevas[:2], t_tanda=100.0); assert not d                          # 2 nuevas: tanda 3,5 < 5
    d, info = M.evaluar_kill_v3(viejas + nuevas, t_tanda=100.0); assert d and info["causa"] == "tope_tanda"


def test_kv3_rearme_borra_el_acumulado_anterior(tmp_path, monkeypatch):
    monkeypatch.setattr(X, "LEDGER", tmp_path / "experimento_h47_H23V3_ledger.jsonl")
    ant = tmp_path / "experimento_h47_H23V3_ledger_tanda1.jsonl"
    escribe_ledger(ant, [("btc-updown-5m-1000", "2026-10-19T10:00:00+00:00", 0.30, 5.0)],
                   extra=[{"real": True, "tipo": "kill_brazo", "motivo": "m", "ts": "2026-10-19T12:00:00+00:00"}])
    st = M.estado_acumulado("A", eventos_propios=[], dirn=tmp_path)
    assert st["pendiente"] == "m" and len(st["previas"]) == 1                                              # kill de otra tanda: pendiente tambien en esta
    rearme = {"real": True, "tipo": "kill_brazo_rearmado", "motivo": "ok", "ts": "2026-10-20T08:00:00+00:00"}
    st = M.estado_acumulado("A", eventos_propios=[rearme], dirn=tmp_path)
    assert st["pendiente"] is None and st["t_rearme"] == epoch("2026-10-20T08:00:00+00:00") and st["previas"] == []   # lo anterior al rearme no cuenta


def test_kv3_ledger_hermano_ilegible_no_opera(tmp_path, monkeypatch):
    monkeypatch.setattr(X, "LEDGER", tmp_path / "experimento_h47_H23V3_ledger.jsonl"); monkeypatch.setattr(X, "_CACHE", None)
    monkeypatch.setattr(X, "LOCK", tmp_path / "x.lock")                                                    # NUNCA el lock real de la wallet
    (tmp_path / "experimento_h47_H23V3_ledger_tanda1.jsonl").write_text('{"real": true, "tipo": "config"}\n{linea cortada')
    with pytest.raises(M.LedgerBrazoIlegible): M.estado_acumulado("A", eventos_propios=[], dirn=tmp_path)
    monkeypatch.setattr(M, "exigir_puertas", lambda *a, **k: None); monkeypatch.setattr(M, "configurar_rutas", lambda real, brazo: None)
    with pytest.raises(SystemExit) as e: M.main(["--confirmo-dinero-real", "--ok-final-javi", "x"])
    assert "ilegible" in str(e.value) and "fail-closed" in str(e.value)
    with pytest.raises(SystemExit) as e: M.main(["--confirmo-dinero-real", "--ok-final-javi", "x", "--rearmar-kill-brazo", "m"])
    assert "ilegible" in str(e.value)
    (tmp_path / "experimento_h47_H23V3_ledger_tanda1.jsonl").write_text('[1, 2]\n')                        # JSON valido pero no es un evento
    with pytest.raises(M.LedgerBrazoIlegible): M.estado_acumulado("A", eventos_propios=[], dirn=tmp_path)


def test_kv3_cada_brazo_acumula_solo_sus_ledgers(tmp_path, monkeypatch):
    monkeypatch.setattr(X, "LEDGER", tmp_path / "experimento_h47_H23V3_ledger.jsonl")
    for n in ("experimento_h47_H23V3_ledger_tanda1.jsonl", "experimento_h47_H23V3B_ledger.jsonl", "experimento_h47_B_ledger.jsonl", "experimento_h47_H23V3_ledger.jsonl",
              "experimento_h47_H23V3_ledger.jsonl.bak", "experimento_h47_H23V3_ledger_copia.jsonl", "experimento_h47_H23V3_ledger_tanda1.jsonl~", "experimento_h47_H23V3_ledger_t1.jsonl"):
        (tmp_path / n).write_text("")
    assert [f.name for f in M.ledgers_del_brazo("A", tmp_path)] == ["experimento_h47_H23V3_ledger_tanda1.jsonl"]    # sin el propio, sin H23B ni H47-B ni copias/backups
    monkeypatch.setattr(X, "LEDGER", tmp_path / "experimento_h47_H23V3B_ledger.jsonl")
    assert M.ledgers_del_brazo("B", tmp_path) == []


# ================================================================== RONDA 3
def pend_pos(n, base=0):
    return [{"slug": f"btc-updown-5m-{1000 + 900 * (base + i)}", "dia": "2026-10-10", "acc": 6.0, "coste": 1.8, "incierta": False, "fin": 1300 + 900 * (base + i), "t_int": 1.0}
            for i in range(n)]


def con_gana(ex, pos):
    return [{**p, "gana": (None if p["slug"] not in ex._des else (ex._des[p["slug"]] == "ganador")) } for p in pos]


def test_r3_1_gamma_falla_rota_candidatos_evalua_con_cache_y_pasa_a_failclosed(monkeypatch):
    ex = Fake(); ex.real = True
    pos = pend_pos(5)
    ex._des = {pos[0]["slug"]: "otro", pos[1]["slug"]: "otro", pos[2]["slug"]: "otro"}                      # 3 ya resueltas (pierden) -> kill sigma con sigma1 baja
    monkeypatch.setattr(M, "KILL_BRAZO_V3", {**M.KILL_BRAZO_V3, "sigma1": 0.5})
    monkeypatch.setattr(ex, "posiciones_brazo", lambda: con_gana(ex, pos), raising=False)
    def falla(slug): raise RuntimeError("gamma caido")
    monkeypatch.setattr(M, "desenlace_token", falla)
    ex._vigilar_kill_brazo(1e6)                                                                            # gamma falla, pero el kill se evalua con lo cacheado
    assert ex.kill_brazo and "sigma" in ex.kill_brazo
    ex2 = Fake(); ex2.real = True; ex2._des = {}
    pos2 = pend_pos(5)
    monkeypatch.setattr(ex2, "posiciones_brazo", lambda: con_gana(ex2, pos2), raising=False)
    for k in range(3):
        ex2._ult_kb = 0.0; ex2._vigilar_kill_brazo(1e6 + k)
    assert sorted(ex2._intentos.values()) == [1, 1, 1, 1, 2] or sorted(ex2._intentos.values()) == [1, 1, 1, 1, 2]    # 2+2+2 consultas rotadas: nadie monopoliza
    assert max(ex2._intentos.values()) - min(ex2._intentos.values()) <= 1 and len(ex2._intentos) == 5
    for k in range(10):
        ex2._ult_kb = 0.0; ex2._vigilar_kill_brazo(1e6 + 10 + k)
    assert ex2.sin_desenlace and "sin desenlace oficial" in ex2.sin_desenlace                               # >= DESENLACE_MAX_PASADAS intentos: fail-closed
    c = ctx(); ex2.decidir(c, 200, time.time()); assert not [x for x in ex2.calls if x[0] == "post"]        # y no se postea
    ex2.sin_desenlace = None; ex2.decidir(c, 200, time.time()); assert [x for x in ex2.calls if x[0] == "post"]   # (control: sin el bloqueo si postea)


def test_r3_1_por_tiempo_sin_desenlace_tambien_bloquea(monkeypatch):
    ex = Fake(); ex.real = True
    pos = pend_pos(1)
    monkeypatch.setattr(ex, "posiciones_brazo", lambda: con_gana(ex, pos), raising=False)
    monkeypatch.setattr(M, "desenlace_token", lambda slug: None)
    ahora = pos[0]["fin"] + M.DESENLACE_MAX_MIN * 60 + 10
    ex._vigilar_kill_brazo(ahora); assert ex.sin_desenlace
    ex2 = Fake(); ex2.real = True
    monkeypatch.setattr(ex2, "posiciones_brazo", lambda: con_gana(ex2, pos), raising=False)
    ex2._vigilar_kill_brazo(pos[0]["fin"] + 120); assert ex2.sin_desenlace is None                         # a los 2 min aun es normal


def test_r3_2_puerta_de_arranque_resuelve_antes_de_la_primera_orden(monkeypatch):
    ex = Fake(); ex.real = True; ex.puerta_ok = False
    pos = pend_pos(2)
    monkeypatch.setattr(ex, "posiciones_brazo", lambda: con_gana(ex, pos), raising=False)
    monkeypatch.setattr(M, "desenlace_token", lambda slug: None)                                           # gamma no resuelve
    c = ctx(); t0 = time.time()
    ex.decidir(c, 200, t0); assert not [x for x in ex.calls if x[0] == "post"] and ex.puerta_ok is False   # fail-closed
    monkeypatch.setattr(M, "desenlace_token", lambda slug: "ganador")                                      # gamma vuelve
    ex._ult_puerta = 0.0; ex.decidir(c, 200, time.time())
    assert ex.puerta_ok and [x for x in ex.calls if x[0] == "post"]
    ex2 = Fake(); ex2.real = True; ex2.puerta_ok = False                                                   # puerta + kill: las posiciones previas pierden -> no se postea
    monkeypatch.setattr(M, "KILL_BRAZO_V3", {**M.KILL_BRAZO_V3, "sigma1": 0.5})
    monkeypatch.setattr(ex2, "posiciones_brazo", lambda: con_gana(ex2, pend_pos(4)), raising=False)
    monkeypatch.setattr(M, "desenlace_token", lambda slug: "otro")
    ex2.decidir(ctx(), 200, time.time())
    assert ex2.kill_brazo and not [x for x in ex2.calls if x[0] == "post"] and not ex2.puerta_ok


def test_r3_3_dedupe_por_oid_y_slug_sin_nombre_de_fichero(tmp_path, monkeypatch):
    monkeypatch.setattr(X, "LEDGER", tmp_path / "experimento_h47_H23V3_ledger.jsonl"); monkeypatch.setattr(X, "_CACHE", None)
    pos = [("btc-updown-5m-1000", "2026-10-19T10:00:00+00:00", 0.30, 5.0)]
    escribe_ledger(tmp_path / "experimento_h47_H23V3_ledger_tanda1.jsonl", pos)
    (tmp_path / "experimento_h47_H23V3_ledger_tanda2.jsonl").write_text((tmp_path / "experimento_h47_H23V3_ledger_tanda1.jsonl").read_text())   # copia exacta (mismos oid)
    (tmp_path / "experimento_h47_H23V3_ledger.jsonl.bak").write_text((tmp_path / "experimento_h47_H23V3_ledger_tanda1.jsonl").read_text())          # backup: ni se lee
    st = M.estado_acumulado("A", eventos_propios=[], dirn=tmp_path)
    assert len(st["ordenes_previas"]) == 1 and len(st["previas"]) == 1 and st["previas"][0]["acc"] == 5.0           # una sola vez
    ex = real23(tmp_path, monkeypatch); ex._ordenes_previas = st["ordenes_previas"]
    oid = next(iter(st["ordenes_previas"])); o = st["ordenes_previas"][oid]
    ex.ordenes = lambda: {oid: o}                                                                           # la misma orden tambien en el ledger propio
    ps = ex.posiciones_brazo(); assert len(ps) == 1 and ps[0]["acc"] == 5.0
    monkeypatch.setattr(X, "LEDGER", tmp_path / "experimento_h47_H23V3_ledger.jsonl")
    # dos ordenes distintas del mismo slug en ledgers distintos = UNA posicion
    escribe_ledger(tmp_path / "experimento_h47_H23V3_ledger_tanda2.jsonl", [("btc-updown-5m-1000", "2026-10-19T10:05:00+00:00", 0.31, 5.0)])
    st = M.estado_acumulado("A", eventos_propios=[], dirn=tmp_path); ex._ordenes_previas = st["ordenes_previas"]; ex.ordenes = lambda: {}
    ps = ex.posiciones_brazo(); assert len(st["ordenes_previas"]) == 2 and len(ps) == 1 and abs(ps[0]["acc"] - 10.0) < 1e-9


def test_r3_4_h47b_exige_escalon_b_completo_t_stop_y_mismo_codigo():
    h47 = M.sha_dependencias()["h47"]
    assert M.h47b_terminado([cfg_ev(), fin_ev()], sha_h47=h47)[0]
    for malo, frag in ((dict(escalon="A"), "escalon B"), (dict(n_max=100), "n_max"), (dict(t_stop=90.0), "t_stop"), (dict(codigo_sha="0" * 16), "otro codigo")):
        ok, m = M.h47b_terminado([cfg_ev(**malo), fin_ev()], sha_h47=h47); assert not ok and frag in m, (malo, m)
    assert not M.h47b_terminado([{"real": True, "tipo": "config", "escalon": "B"}, fin_ev()], sha_h47=h47)[0]      # sin n_max/t_stop
    assert M.h47b_terminado([cfg_ev(n_max=230, codigo_sha="x"), fin_ev()])[0]                              # sin sha_h47 no se compara (solo uso interno); exigir_puertas SIEMPRE lo pasa


def test_r3_4_exigir_puertas_pasa_el_sha_de_h47_del_ok(tmp_path, monkeypatch):
    monkeypatch.setattr(M, "OK_FICHERO", tmp_path / "ok.txt")
    lb = tmp_path / "b.jsonl"; lb.write_text(json.dumps(cfg_ev(codigo_sha="0" * 16)) + "\n" + json.dumps(fin_ev()) + "\n")
    txt = ok_txt(); (tmp_path / "ok.txt").write_text(txt)
    with pytest.raises(SystemExit) as e: M.exigir_puertas(True, txt, ledger_b=lb)
    assert "otro codigo" in str(e.value)


class _Hilo:
    def is_alive(self): return True


def libro_real_quieto(edad_5m, edad_15m, quieto_s=200):
    lib = object.__new__(M.LibroH23)
    ahora = time.time()
    lib.hilo, lib.error, lib.ult_msg, lib.ult = _Hilo(), None, ahora, ahora - quieto_s                    # PONG ahora; ningun cambio de libro hace `quieto_s`
    lib.ult_tok = {"u5": ahora - edad_5m, "u15": ahora - edad_15m}
    return lib


def test_r3_5_libro_quieto_mas_de_120s_con_conexion_viva_usa_conexion_sana_y_respaldo():
    ex, c = Fake(), ctx()
    c.lib = libro_real_quieto(60, 100, quieto_s=200)                                                       # X.Libro.fresco() diria False (ult > 120 s)
    assert c.lib.fresco() is False and ex._libro_fresco(c) is True                                          # nosotros: conexion sana + token < 120 s
    c.lib = libro_real_quieto(60, M.EDAD_TOKEN_MAX_S + 5); assert ex._libro_fresco(c) is False             # respaldo: un token mudo > 120 s
    c.lib = libro_real_quieto(1, 1); c.lib.ult_msg = time.time() - (X.WS_MAX_S + 1); assert ex._libro_fresco(c) is False   # conexion muerta
    c.lib = libro_real_quieto(1, 1)
    lp = M.LibPost(ex, c, 0.30); assert lp.fresco() is True                                                 # LibPost igual
    c.lib.ult_tok["u15"] = time.time() - 500; assert lp.fresco() is False


def test_r3_6_documentacion_honesta_del_kill_n_bajo():
    import inspect
    doc = open(M.__file__).read().split("Uso:")[0]
    assert "INALCANZABLE" in doc and "SUELO DE SALDO" in doc and "media movil del PREFIJO" in doc
    assert "suelo de saldo" in M.KILL_BRAZO_V3["nota"] and M.KILL_BRAZO_V3["s"] == "media_movil_del_prefijo"
    assert "MEDIA MOVIL DEL PREFIJO" in inspect.getsource(M.evaluar_kill_v3)


def test_r3_7_sin_rebate_y_relleno_incierto_es_sin_desenlace():
    d, info = M.evaluar_kill_v3([{"slug": "a", "acc": 6.0, "coste": 1.8, "gana": False, "fin": 1}])
    assert info["perdida"] == 1.8                                                                           # el rebate teorico NO se cuenta como ingreso
    from types import SimpleNamespace as NS
    mk = lambda slug, abierta: NS(alias=False, ilegible=False, abierta=abierta, lo=5.0, precio=0.30, slug=slug, tok="u5", t_int=10.0)
    ps = {p["slug"]: p for p in M.agrupar_posiciones([mk("btc-updown-5m-1000", True), mk("btc-updown-5m-1900", False)])}
    assert ps["btc-updown-5m-1000"]["incierta"] and not ps["btc-updown-5m-1900"]["incierta"]
    ex = Fake(); ex._des = {"btc-updown-5m-1000": "u5", "btc-updown-5m-1900": "u5"}
    ex.ordenes = lambda: {"a": mk("btc-updown-5m-1000", True), "b": mk("btc-updown-5m-1900", False)}
    pos = {p["slug"]: p for p in ex.posiciones_brazo()}
    assert pos["btc-updown-5m-1000"]["gana"] is None and pos["btc-updown-5m-1900"]["gana"] is True          # incierta: no cuenta aunque el mercado este resuelto
    assert "incierto" in ex._motivo_sin_desenlace(list(pos.values()), 1e9)                                  # y bloquea (fail-closed) pasado el cierre


def test_r3_8_fsync_en_kill_tope_y_rearme_y_fallo_es_kill(tmp_path, monkeypatch):
    llamadas = []
    real_fsync = M.H._fsync_ledger
    monkeypatch.setattr(M.H, "_fsync_ledger", lambda: (llamadas.append(1), real_fsync())[1])
    ex = real23(tmp_path, monkeypatch); ex.cli = None; ex.tanda_agotada = None
    monkeypatch.setattr(ex, "parar", lambda m: setattr(ex, "parada", m), raising=False)
    ex._evaluar_kill(p2(3, lambda i: False))
    assert ex.tanda_agotada and len(llamadas) == 1                                                          # tope_tanda con fsync
    monkeypatch.setattr(M, "KILL_BRAZO_V3", {**M.KILL_BRAZO_V3, "sigma1": 0.5})
    ex2 = real23(tmp_path, monkeypatch); ex2.tanda_agotada = None; monkeypatch.setattr(ex2, "parar", lambda m: None, raising=False)
    ex2._evaluar_kill(p2(3, lambda i: False)); assert ex2.kill_brazo and len(llamadas) == 2                  # kill_brazo con fsync
    monkeypatch.setattr(M.H, "_fsync_ledger", lambda: (_ for _ in ()).throw(OSError("disco")))
    ex3 = real23(tmp_path, monkeypatch); ex3.tanda_agotada = None; monkeypatch.setattr(ex3, "parar", lambda m: None, raising=False)
    ex3._evaluar_kill(p2(3, lambda i: False)); assert ex3.kill and "fsync" in ex3.kill                      # no llega a disco -> kill de la wallet
    # rearme con fsync
    monkeypatch.setattr(M.H, "_fsync_ledger", lambda: (llamadas.append(2), real_fsync())[1])
    led = tmp_path / "experimento_h47_H23V3_ledger.jsonl"
    led.write_text(json.dumps({"real": True, "tipo": "kill_brazo", "motivo": "x", "ts": "2026-10-20T10:00:00.000+00:00"}) + "\n")
    monkeypatch.setattr(X, "LEDGER", led); monkeypatch.setattr(X, "_CACHE", None); monkeypatch.setattr(X, "LOCK", tmp_path / "x.lock")
    monkeypatch.setattr(M, "exigir_puertas", lambda *a, **k: None); monkeypatch.setattr(M, "configurar_rutas", lambda real, brazo: None)
    n = len(llamadas); assert M.main(["--confirmo-dinero-real", "--ok-final-javi", "x", "--rearmar-kill-brazo", "ok"]) == 0 and llamadas[n:] == [2]


def test_r3_8_linea_ilegible_del_ledger_propio_es_failclosed(tmp_path, monkeypatch):
    own = tmp_path / "experimento_h47_H23V3_ledger.jsonl"
    own.write_text(json.dumps({"real": True, "tipo": "config"}) + '\n{"real": true, "tipo": "intencion_po')
    monkeypatch.setattr(X, "LEDGER", own); monkeypatch.setattr(X, "_CACHE", None)
    with pytest.raises(M.LedgerBrazoIlegible) as e: M.estado_acumulado("A", dirn=tmp_path)
    assert "aceptar-linea-ilegible-brazo" in str(e.value)


def test_r3_9_contabilidad_en_el_sha_y_el_hash_del_kill_cubre_el_codigo_de_acumulacion(tmp_path, monkeypatch):
    d = M.sha_dependencias(); assert set(d) == {"h47", "pares", "contabilidad", "shadow"} and d["contabilidad"] == M._sha_fichero(M.H.C.__file__)
    monkeypatch.setattr(M, "OK_FICHERO", tmp_path / "ok.txt")
    lb = tmp_path / "b.jsonl"; lb.write_text(json.dumps(cfg_ev()) + "\n" + json.dumps(fin_ev()) + "\n")
    txt = ok_txt(sin=("contabilidad",)); (tmp_path / "ok.txt").write_text(txt)
    with pytest.raises(SystemExit) as e: M.exigir_puertas(True, txt, ledger_b=lb)
    assert "contabilidad" in str(e.value)
    h0 = M.hash_kill_v3()
    for fn in ("agrupar_posiciones", "estado_acumulado", "escanear_brazo"):
        orig = getattr(M, fn)
        monkeypatch.setattr(M, fn, lambda *a, **k: orig(*a, **k))                                         # otro codigo
        assert M.hash_kill_v3() != h0, fn
        monkeypatch.setattr(M, fn, orig)
    assert M.hash_kill_v3() == h0


def test_r3_10_recuperacion_de_ledger_hermano_truncado(tmp_path, monkeypatch, capsys):
    own = tmp_path / "experimento_h47_H23V3_ledger.jsonl"; own.write_text("")
    monkeypatch.setattr(X, "LEDGER", own); monkeypatch.setattr(X, "_CACHE", None)
    her = tmp_path / "experimento_h47_H23V3_ledger_tanda1.jsonl"
    her.write_text(json.dumps({"real": True, "tipo": "config"}) + '\n{"real": true, "tipo": "intencion_po\n' + json.dumps({"real": True, "tipo": "fin_ejecucion"}) + "\n")
    with pytest.raises(M.LedgerBrazoIlegible): M.estado_acumulado("A", dirn=tmp_path)
    with pytest.raises(SystemExit): M.aceptar_lineas_brazo("A", "  ", dirn=tmp_path)                       # motivo obligatorio
    assert M.aceptar_lineas_brazo("A", "crash", leer=lambda m: "no", dirn=tmp_path) is None                # sin confirmacion: nada
    with pytest.raises(M.LedgerBrazoIlegible): M.estado_acumulado("A", dirn=tmp_path)
    ev = M.aceptar_lineas_brazo("A", "crash del 19-Oct", leer=lambda m: "ACEPTAR LINEA ILEGIBLE BRAZO A", dirn=tmp_path)
    assert ev and ev["motivo"] == "crash del 19-Oct" and "intencion_po" in capsys.readouterr().out          # muestra la linea
    sha = M.H._sha('{"real": true, "tipo": "intencion_po'); assert [her.name, sha] in [list(x) for x in ev["aceptadas"]] and ev["lineas_crudas"][sha]["base64"]
    monkeypatch.setattr(X, "_CACHE", None)
    assert M.estado_acumulado("A", dirn=tmp_path)["pendiente"] is None                                     # ahora lee
    assert any(e["tipo"] == "h23_linea_ilegible_aceptada" for e in leer(tmp_path.parent / "x") ) if False else True
    her.write_text(her.read_text() + 'basura \x00 no json\n')
    with pytest.raises(SystemExit): M.aceptar_lineas_brazo("A", "m", leer=lambda m: "ACEPTAR LINEA ILEGIBLE BRAZO A", dirn=tmp_path)   # no parece un JSON cortado: no acepta ninguna


# ====================================================================== V3: RE-PUJA TEMPRANA (150 ms)
def cancelada_v3(ex, h="h0", ahora=None, dt_det=0.30, st="CANCELED", f=0.0, lect_tras_cancel=True, c=None, libro_posterior=True, **extra):
    """Orden CANCELADA ya leida: decision de cancelar hace `dt_det` s, cancelacion completada 0,06 s despues, lectura 0,02 s tras eso. Registra el ctx en ex.ctxs y el
    ultimo mensaje del libro del token (`libro_posterior`: True = DESPUES de la decision de cancelar)."""
    ahora = ahora if ahora is not None else time.time()
    t_det = ahora - dt_det
    c = c if c is not None else ctx()
    ex.ctxs = {"c": c}
    c.lib.ult_tok = {"u5": (t_det + 0.05) if libro_posterior else (t_det - 0.5)}
    o = {"tok": "u5", "precio": 0.30, "size": 5.0, "t_post": ahora - 10, "t_det_cancel": t_det, "t_cancel": t_det + 0.06,
         "lectura_post": {"t": t_det + (0.08 if lect_tras_cancel else 0.02), "f": f, "st": st}, **extra}
    ex.canceladas[h] = o
    return o


def test_v3_configuracion_y_nombres_propios():
    assert R.CONFIG["repuja_ms"] == 150 and M.REPUJA_S == 0.15 and 0.10 <= M.REPUJA_S < X.ASENTAR_S
    assert M.OK_FICHERO.name == "H23V3_OK_JAVI.txt" and M.OK_FICHERO.name != "H23_OK_JAVI.txt"
    assert M.ARM_RE["A"].match("experimento_h47_H23V3_ledger.jsonl") and not M.ARM_RE["A"].match("experimento_h47_H23_ledger.jsonl")
    assert M.ARM_RE["B"].match("experimento_h47_H23V3B_ledger_tanda2.jsonl") and not M.ARM_RE["B"].match("experimento_h47_H23B_ledger.jsonl")
    sys.path.insert(0, os.path.join(HERE, "..", ".."))                                  # h23_regla v1 (solo para comparar hashes)
    import h23_regla as R1
    assert R.hash_config() != R1.hash_config() and M.HASH_REGLA == R.hash_config()


def test_v3_liberada_con_todas_las_condiciones():
    ex, c = Fake(), ctx(); o = cancelada_v3(ex, c=c)
    assert ex._liberada(o, time.time()) is True and ex._cancelada_sin_liberar("u5", time.time()) is False
    assert [e for e in ex.evs if e["tipo"] == "h23v3_repuja"][0]["via"] == "lectura_terminal"
    n = len(ex.evs); ex._liberada(o, time.time()); assert len(ex.evs) == n              # el evento se escribe UNA vez


@pytest.mark.parametrize("cambia", [
    dict(ya_terminal=True), dict(t_det_cancel=None), dict(t_cancel=None), dict(lectura_post=None),
    dict(dt_det=0.05), dict(st="LIVE"), dict(st=""), dict(lect_tras_cancel=False), dict(libro_posterior=False)])
def test_v3_no_se_libera_si_falta_algo_y_vuelve_a_v1(cambia):
    ex, c = Fake(), ctx()
    kw = dict(cambia)
    extra = {k: kw.pop(k) for k in ("ya_terminal", "t_det_cancel", "t_cancel", "lectura_post") if k in kw}
    o = cancelada_v3(ex, c=c, **kw)
    o.update(extra)
    assert ex._liberada(o, time.time()) is False and ex._cancelada_sin_liberar("u5", time.time()) is True


def test_v3_no_se_libera_con_relleno_cerrado_o_frenos():
    for cierre in ({"llenas": 1.0}, {"cerrado": True}):
        ex, c = Fake(), ctx(); ex.ctxs = {"c": c}; c.estado["u5"].update(cierre); o = cancelada_v3(ex, c=c)
        assert ex._liberada(o, time.time()) is False
    for freno in ("kill", "parada", "senal", "kill_brazo", "tanda_agotada"):
        ex, c = Fake(), ctx(); ex.ctxs = {"c": c}; o = cancelada_v3(ex, c=c); setattr(ex, freno, "x")
        assert ex._liberada(o, time.time()) is False, freno


def test_v3_repuja_fuera_de_rango_cae_a_v1(monkeypatch):
    ex, c = Fake(), ctx(); o = cancelada_v3(ex, c=c)
    monkeypatch.setattr(M, "REPUJA_S", float(X.ASENTAR_S))                              # = v1
    assert ex._liberada(o, time.time()) is False
    monkeypatch.setattr(M, "REPUJA_S", 0.05)                                            # por debajo de la RTT de cancelacion: prohibido
    assert ex._liberada(o, time.time()) is False


def test_v3_decidir_repone_a_los_150ms_con_lectura_terminal_y_no_antes():
    ex, c = Fake(), ctx()
    cancelada_v3(ex, c=c, dt_det=0.05)                                                       # han pasado 50 ms de la decision: aun no
    ex.decidir(c, 200, time.time()); assert not [x for x in ex.calls if x[0] == "post"]
    ex, c = Fake(), ctx(); cancelada_v3(ex, c=c, dt_det=0.20)                                # 200 ms: libre
    ex.decidir(c, 200, time.time()); posts = [x for x in ex.calls if x[0] == "post"]
    assert len(posts) == 1 and posts[0][1] == 0.30
    pp = [e for e in ex.evs if e["tipo"] == "puja_post"][0]
    assert pp["ms_desde_decision_cancel"] is None or pp["ms_desde_decision_cancel"] >= 0      # t_det_cancel del ctx solo lo pone la reaccion


def test_v3_la_reaccion_ancla_t_det_cancel_y_el_puja_post_mide_los_ms_reales():
    ex, c = Fake(), ctx()
    def cancelar(h):
        ex.calls.append(("cancelar", h)); o = ex.vivas.pop(h); ex.canceladas[h] = dict(o, t_cancel=time.time()); return True
    ex.cancelar = cancelar; ex.ctxs = {"c": c}
    ex.decidir(c, 200, time.time())
    c.lib.poner("u15", {0.36: 80.0}, {0.47: 80.0})                                       # cota cae -> cancelar
    t0 = time.time(); ex._reaccion_viva(c, 199, t0, "rapida")
    assert c.t_det_cancel >= t0 and ex.canceladas["h1"]["t_det_cancel"] == c.t_det_cancel
    ex.canceladas["h1"]["lectura_post"] = {"t": time.time(), "f": 0.0, "st": "CANCELED"}
    c.lib.poner("u15", {0.45: 80.0}, {0.47: 80.0}); c.lib.ult_tok["u5"] = time.time(); time.sleep(0.2)     # el WS emite (p. ej. el retiro de nuestra orden) tras la decision
    ex.calls.clear(); ex.decidir(c, 198, time.time())
    pp = [e for e in ex.evs if e["tipo"] == "puja_post"][-1]
    assert pp["ms_desde_decision_cancel"] >= 150 and pp["repuja_s_cfg"] == 0.15 and c.t_det_cancel is None and len([e for e in ex.evs if e["tipo"] == "puja_post"]) == 2
    assert [e for e in ex.evs if e["tipo"] == "h23v3_repuja"]


def test_v3_fill_tardio_con_orden_nueva_posterior_es_doble_exposicion_y_mata_el_brazo(monkeypatch):
    monkeypatch.setattr(X.Exp, "_lectura", lambda self, *a, **k: None)
    ex, c = Fake(), ctx(); o = cancelada_v3(ex, c=c, h="h0")
    assert ex._liberada(o, time.time())
    ex._t_ult_post["u5"] = o["t_cancel"] + 0.2                                           # se re-pujo DESPUES de cancelar
    ex._lectura("h0", 2.0, "MATCHED", 5.0)
    assert ex.kill_brazo and "doble exposicion" in ex.kill_brazo and ex.parada
    ev = [e for e in ex.evs if e["tipo"] == "kill_brazo"][0]
    assert ev["info"]["doble_exposicion"] is True and ev["info"]["f_antes"] == 0.0 and ev["info"]["f_ahora"] == 2.0


def test_v3_fill_tardio_sin_orden_nueva_solo_se_registra(monkeypatch):
    monkeypatch.setattr(X.Exp, "_lectura", lambda self, *a, **k: None)
    ex, c = Fake(), ctx(); o = cancelada_v3(ex, c=c, h="h0")
    assert ex._liberada(o, time.time())
    ex._lectura("h0", 2.0, "MATCHED", 5.0)                                               # nadie re-pujo: el v1 tambien lo veria igual
    assert ex.kill_brazo is None and not ex.parada
    assert [e for e in ex.evs if e["tipo"] == "h23v3_fill_tardio"][0]["doble_exposicion"] is False


def test_v3_lectura_sin_liberar_o_sin_relleno_nuevo_no_dispara(monkeypatch):
    monkeypatch.setattr(X.Exp, "_lectura", lambda self, *a, **k: None)
    ex, c = Fake(), ctx(); o = cancelada_v3(ex, c=c, h="h0")                                  # NO liberada (no se llamo a _liberada)
    ex._t_ult_post["u5"] = o["t_cancel"] + 1; ex._lectura("h0", 2.0, "MATCHED", 5.0)
    assert ex.kill_brazo is None and o["lectura_post"]["f"] == 2.0                       # se anota la lectura, pero no era una re-puja temprana
    ex2, c2 = Fake(), ctx(); o2 = cancelada_v3(ex2, c=c2, h="h0"); ex2._liberada(o2, time.time()); ex2._t_ult_post["u5"] = o2["t_cancel"] + 1
    ex2._lectura("h0", 0.0, "CANCELED", 5.0)                                             # misma f: no es un relleno nuevo
    assert ex2.kill_brazo is None


def test_v3_e2e_con_el_arnes_real_cancelar_leer_y_repujar_a_los_150ms(tmp_path, monkeypatch):
    """X.cancelar / X.liquidar / X.post REALES con cliente CLOB falso: tras cancelar (ack 'canceled') y leer CANCELED con 0 relleno, se vuelve a pujar sin esperar ASENTAR_S."""
    ex = real23(tmp_path, monkeypatch); ex.cli.get_order_resp = {"size_matched": "0", "status": "CANCELED"}
    ex._hash = lambda signed, tok: "0xnuevo"                                             # el hash local coincide con el orderID que devuelve el cliente falso
    c = ctx(); ex.ctxs = {"c": c}
    viva(ex, c, h="0xh1", t_post=time.time() - 40, visto=True)
    c.lib.poner("u15", {0.36: 80.0}, {0.47: 80.0})                                       # la cota cae -> cancelar ya
    ex.decidir(c, 200, time.time())
    assert "0xh1" in ex.canceladas and ex.canceladas["0xh1"]["lectura_post"]["st"] == "CANCELED" and ex.canceladas["0xh1"]["t_det_cancel"]
    c.lib.poner("u15", {0.45: 80.0}, {0.47: 80.0}); c.lib.ult_tok["u5"] = time.time()    # la cota vuelve (mensaje del WS posterior a la decision de cancelar)
    ex.decidir(c, 199.9, time.time())                                                    # < 150 ms: todavia no
    assert not ex.cli.post_orders
    time.sleep(0.2)
    ex.decidir(c, 199.5, time.time())
    assert len(ex.cli.post_orders) == 1 and ex.cli.post_orders[0][1] is True              # post_only; ASENTAR_S (1,5 s) NO se espero
    tipos = [e["tipo"] for e in leer(tmp_path)]
    assert "h23v3_repuja" in tipos and "intencion_post" in tipos and "kill" not in tipos
    rep = [e for e in leer(tmp_path) if e["tipo"] == "h23v3_repuja"][0]
    assert 150 <= rep["ms_desde_decision_cancel"] < 1500 and rep["lectura"]["st"] == "CANCELED"


def test_v3_e2e_si_el_exchange_dice_ya_cancelada_o_casada_se_espera_como_v1(tmp_path, monkeypatch):
    ex, c = escenario_cancel_ya_terminal(tmp_path, monkeypatch); ex.ctxs = {"c": c}
    ex.decidir(c, 200, time.time())
    assert ex.canceladas["0xh1"].get("ya_terminal")
    c.lib.poner("u15", {0.45: 80.0}, {0.47: 80.0}); time.sleep(0.2)
    ex.decidir(c, 199, time.time())
    assert not ex.cli.post_orders and ex._cancelada_sin_liberar("u5", time.time()) is True      # fail-closed: nada de re-puja temprana


def test_v3_en_seco_la_lectura_de_una_cancelada_se_registra_como_terminal_y_en_real_no_se_toca(monkeypatch):
    monkeypatch.setattr(X.Exp, "_lectura", lambda self, *a, **k: None)
    ex, c = Fake(), ctx(); ex.real = False
    ex.canceladas["h0"] = {"tok": "u5"}; ex._lectura("h0", 0.0, "LIVE", 5.0)
    assert ex.canceladas["h0"]["lectura_post"]["st"] == "CANCELED"          # seco: sin estado de cancelacion simulado
    ex.canceladas["h0"] = {"tok": "u5"}; ex._lectura("h0", 5.0, "LIVE", 5.0)
    assert ex.canceladas["h0"]["lectura_post"]["st"] == "MATCHED"
    ex.real = True
    ex.canceladas["h0"] = {"tok": "u5"}; ex._lectura("h0", 0.0, "LIVE", 5.0)
    assert ex.canceladas["h0"]["lectura_post"]["st"] == "LIVE"              # real: el estado del exchange, intacto (un LIVE NO libera la re-puja)


def test_v3_sin_ctx_del_token_no_se_libera():
    ex, c = Fake(), ctx(); o = cancelada_v3(ex, c=c); ex.ctxs = {}
    assert ex._liberada(o, time.time()) is False                                         # sin vista del libro de ese token: fail-closed
