"""Tests del paquete H23 real (sin red, sin dinero): politica de decision con libro falso, puertas del modo real y propiedades del subclase.
Desde este directorio:  python3 -m pytest -q -p no:cacheprovider test_experimento_maker_h23.py   (necesita /root/polymarket-research-dev con H47)"""
import os, sys, time
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/root/polymarket-research-dev")
sys.path.insert(0, os.path.join(HERE, ".."))                               # h23_regla
sys.path.insert(0, HERE)
import pytest
import experimento_maker_h47 as H
import experimento_maker_h23 as M
import h23_regla as R


class Lib:
    def __init__(self):
        self.t = {"u5": ((0.30, 100.0), (0.33, 50.0)), "d5": ((0.66, 10.0), (0.70, 10.0)), "u15": ((0.45, 80.0), (0.47, 80.0)), "d15": ((0.50, 10.0), (0.54, 10.0))}
        self.ok, self.tick_cambiado = True, False
    def top(self, tk): return self.t[tk]
    def fresco(self): return self.ok
    def tamano_nivel(self, tk, p): return 100.0
    def mejor_bid_ajeno(self, tk): return None


class Fake(M.Exp23):
    def __init__(self):                                                     # NO llama al arnes (sin ledger, sin wallet, sin red)
        self.brazo, self.umbral, self.refs = "A", 0.05, None
        self.vivas, self.canceladas, self.parada, self.kill, self.senal = {}, {}, None, None, None
        self.enfriar_tok, self.slugs_usados, self.n_max, self.max_vivas = {}, set(), 40, 2
        self.size, self.min_nocional, self.n_ordenes_total, self.t_stop = 5, 1.0, 0, 10.0
        self.calls = []
    def sincronizar_rellenos(self, c): return 0.0
    def cancelar(self, h): self.calls.append(("cancelar", h)); self.vivas.pop(h, None); return True
    def liquidar(self, *a, **k): self.calls.append(("liquidar",))
    def n_usadas(self): return len(self.slugs_usados)
    def pujas_en_libro(self): return set()
    def puede_enviar(self, coste): return True
    def post(self, slug, tok, lado, precio, size, cola, **k):
        self.calls.append(("post", precio, size)); self.vivas["h1"] = {"precio": precio, "tok": tok, "size": size}; return "h1"
    def _log47(self, ev): self.calls.append(("log", ev["tipo"]))
    def _bloqueo(self, *a): self.calls.append(("bloqueo",))
    def _libro5(self, lib, tok): return []


def ctx():
    c = object.__new__(M.Ctx23)
    c.mk = {"slug": "btc-updown-5m-1", "fin": time.time() + 200, "min_size": 5}
    c.up, c.dn, c.up15, c.dn15 = "u5", "d5", "u15", "d15"
    c.lados = {"u5": "YES", "d5": "NO"}
    c.estado = {t: {"llenas": 0.0, "coste": 0.0, "oid": None, "rellenos": [], "cerrado": False} for t in ("u5", "d5")}
    c.s, c.tc, c.to, c.n_ord, c.t_accion, c.hashes, c.fin_puja, c.tok, c.posteado, c.libro_dec = "Up", "u5", "u15", 0, 0.0, [], None, None, False, None
    c.lib = Lib()
    return c


@pytest.fixture(autouse=True)
def sin_ledger(monkeypatch):
    monkeypatch.setattr(M.X, "leer_ledger", lambda: [])


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
    c.lib.t["u15"] = ((0.36, 80.0), (0.47, 80.0))                           # p_limite(0,36) = 0,29 < 0,30
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


def test_puertas_del_modo_real(tmp_path, monkeypatch):
    M.exigir_puertas(False, None)                                           # seco: sin puertas
    with pytest.raises(SystemExit): M.exigir_puertas(True, None)
    with pytest.raises(SystemExit): M.exigir_puertas(True, "  ")
    monkeypatch.setattr(M, "OK_FICHERO", tmp_path / "ok.txt")
    with pytest.raises(SystemExit): M.exigir_puertas(True, "ok javi")      # el fichero no existe
    (tmp_path / "ok.txt").write_text("ok javi 2026-10-2x\n")
    with pytest.raises(SystemExit): M.exigir_puertas(True, "otro texto")
    M.exigir_puertas(True, "ok javi 2026-10-2x")


def test_el_real_no_es_el_defecto_y_el_ledger_es_hermano_de_h47():
    import inspect
    assert "action=\"store_true\"" in inspect.getsource(M.main) and "H23" in M.H.N_MAX
    assert M.H.N_MAX["H23"] == 40 and M.T_STOP_H23 == 10.0 and R.CONFIG["repost_min_ms"]["join_r"] == int(H.ASENTAR_H47_S * 1000)
    from pathlib import Path
    assert Path("experimento_h47_H23_ledger.jsonl").match("experimento_h47_*_ledger.jsonl")   # el glob de ledgers_reales_hermanos lo recoge


def test_mutacion_objetivo_siempre_se_detecta(monkeypatch):
    monkeypatch.setattr(M, "objetivo_h23", lambda a, b, u: 0.30)
    with pytest.raises(AssertionError):
        test_cancela_en_cuanto_cae_la_cota()
