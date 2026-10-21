"""Test del parche F2 (brazo sombra H59) con libro simulado. NO arranca F2, no abre WS, no firma, no envia: Par se construye con stubs
(armero y enviador falsos que cuentan llamadas). Carga el modulo parcheado desde el texto (REPO -> raiz del repo).
Ejecutar: cd experimentos/5m_barato/h59_colchon && nice -n 19 python3 -m pytest -q test_f2_h59_parche.py"""
import difflib
import hashlib
import shutil
import subprocess
import sys
import threading
import types
from collections import Counter
from pathlib import Path

import pytest

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import h59_regla as R  # noqa: E402

SRC = (AQUI / "f2_5m_barato_dryrun.h59.py").read_text()
BASE = R.REPO / "f2_5m_barato_dryrun.py"
assert "REPO = Path(__file__).resolve().parent\n" in SRC
mod = types.ModuleType("f2_h59_cargado")
mod.__file__ = str(BASE)
sys.path.insert(0, str(R.REPO))
exec(compile(SRC, mod.__file__, "exec"), mod.__dict__)        # noqa: S102  (test: carga el parche tal cual)


class Lib:
    def __init__(self):
        self.top, self.lib, self.ult_tk = {}, {}, {}
    def fresco(self, tk, max_edad_ms=3000):
        return True


class Armero:
    """Cuenta tomar() (consume) y listas() (solo lee)."""
    def __init__(self):
        self.tomadas, self.listadas = [], []
    def tomar(self, clave):
        self.tomadas.append(clave)
        return "firma"
    def listas(self, clave):
        self.listadas.append(clave)
        return 3


class Env:
    def __init__(self):
        self.enviadas = []
    def enviar(self, clave, signed, tipo, t_evento, inline=False, meta=None):
        self.enviadas.append((clave, meta["regla"]))
        return object()


@pytest.fixture(autouse=True)
def entorno(tmp_path):
    mod.OUT = tmp_path
    mod._H59_VISTO.clear()
    yield


def par(mo="BTC"):
    P = mod.Par.__new__(mod.Par)
    P.mo, P.cie, P.s = mo, 1792369800, "Up"
    P.m5, P.m15 = {"id": "M5"}, {"id": "M15"}
    P.tc, P.to = "tc", "to"
    P.motivos, P.v4, P.v7_ult, P.v7_hecho, P.v7_intentos = Counter(), {"activo": False, "ult": None, "n": 0}, -10 ** 12, set(), Counter()
    P.t_ini, P.t_fin = (P.cie - 300) * 1000 + 1500, (P.cie - 10) * 1000
    P.lock, P.lib = threading.Lock(), Lib()
    t_rx = P.t_ini + 500 - 5
    P.lib.top = {"tc": (t_rx, .38, 30, .40, 50), "to": (t_rx, .50, 50, .52, 50)}
    P.lib.lib = {"tc": {"asks": {.40: 50}}}
    P.lib.ult_tk = {"tc": t_rx}
    agenda = []
    P.arm, P.env = Armero(), Env()
    P.ctx = types.SimpleNamespace(agenda=types.SimpleNamespace(en=lambda t, fn: agenda.append((t, fn))), armero=P.arm, env=P.env, inline=False)
    return P, agenda


def correr(mo="BTC"):
    logs = []
    mod.log = lambda ev: logs.append(ev)
    P, agenda = par(mo)
    t = P.t_ini + 500
    P.al_cambiar("tc", t, P.lib.top["tc"])
    return P, agenda, logs, t


def disparar(agenda, hasta=None):
    """Ejecuta la agenda en orden de tiempo (como el hilo real), opcionalmente solo lo vencido a `hasta`."""
    for tt, fn in sorted(agenda, key=lambda x: x[0]):
        if hasta is None or tt <= hasta:
            fn()


def cambia(P, t, bid, bsz, ask, asz):
    """Un cambio del top del 5m s a la hora de RECEPCION t (lo que hace el WS: actualiza libro y llama al callback)."""
    P.lib.top["tc"] = (t, bid, bsz, ask, asz)
    P.lib.ult_tk["tc"] = t
    P.al_cambiar("tc", t, P.lib.top["tc"])


# ------------------------------------------------------------------------------------------------ (1) sin prefirmas ni envio de H59
def test_h59_no_consume_prefirmas_ni_envia_y_dispara_una_vez_solo_btc():
    P, agenda, logs, t = correr("BTC")
    assert len(P.arm.tomadas) == 1 and P.arm.tomadas[0][1] == .43                    # SOLO la de V4 (p_limite(0,50)=0,43); nada a 0,45 (H59)
    assert [r for _, r in P.env.enviadas] == ["v4"]                                  # el enviador no ve ninguna orden H59
    disparar(agenda, hasta=t + 50)                                                   # hilo de la agenda: evento base
    ev = [e for e in logs if e["tipo"] == "h59_evento"]
    assert len(ev) == 1 and [e["tipo"] for e in logs].count("v4_evento") == 1
    assert ev[0]["limites"] == {"0.00": .43, "0.01": .44, "0.02": .45, "0.03": .46, "0.05": .48} and ev[0]["ask5_sz_t0"] == 50
    assert ev[0]["prefirmas_listas_k0.02"] == 3 and P.arm.listadas == [("tc", .45, R.acciones_objetivo(.45), "BUY")]
    assert len(P.arm.tomadas) == 1                                                    # listas() no consume
    assert any(a[0] == t + 215 for a in agenda)                                       # llegada acotada a t0+215 ms
    cambia(P, t + 50, .38, 30, .40, 51)                                               # cambio de tamano: misma senal activa, n no sube
    assert len([e for e in logs if e["tipo"] == "h59_evento"]) == 1
    P2, ag2, logs2, _ = correr("ETH")
    disparar(ag2)
    assert not [e for e in logs2 if e["tipo"] == "h59_evento"] and [e for e in logs2 if e["tipo"] == "v4_evento"]


# ------------------------------------------------------------------------------------------------ (2) llegada por RECEPCION
def test_llegada_usa_el_ultimo_top_recibido_hasta_t0_mas_215_aunque_el_callback_llegue_tarde():
    P, agenda, logs, t = correr("BTC")
    cambia(P, t + 100, .42, 5, .44, 20)                                               # a tiempo (+100 ms): reprecia +4c
    cambia(P, t + 300, .38, 30, .40, 99)                                              # DESPUES del limite (+300 ms): no debe contar
    P.lib.lib["tc"]["asks"] = {.40: 99}
    disparar(agenda)                                                                  # el callback corre cuando el libro ya es el de +300
    r = [e for e in logs if e["tipo"] == "h59_relleno"][0]
    assert r["ask_llegada"] == .44 and r["asz_llegada"] == 20 and r["t_recv_estado"] == t + 100 and r["hay_top_posterior"] is True
    assert r["edad_llegada_ms"] == 115 and r["retraso_callback_ms"] >= 0
    assert r["k0.00"]["clase"] == "repreciado" and r["k0.02"]["clase"] == "llena" and r["k0.02"]["precio"] == .44
    assert r["k0.02"]["l2"]["clase"] == "no_exacto_libro_tocado_tras_limite"          # el L2 de ahora ya no es el de la llegada: no se usa
    assert r["regla_sha256"] == hashlib.sha256((AQUI / "h59_regla.py").read_bytes()).hexdigest()


def test_tamano_del_nivel_1_corta_la_fok_y_l2_exacto_si_nadie_toco_el_libro():
    P, agenda, logs, t = correr("BTC")
    cambia(P, t + 10, .42, 5, .45, 3)                                                 # cabe en el limite pero solo 3 acciones
    P.lib.lib["tc"]["asks"] = {.45: 3, .50: 100}
    disparar(agenda)
    r = [e for e in logs if e["tipo"] == "h59_relleno"][0]
    assert r["k0.02"]["clase"] == "corte_tamano" and r["k0.02"]["l2"]["clase"] == "parcial" and r["hay_top_posterior"] is False


def test_sin_cambios_tras_t0_el_estado_es_el_de_la_senal():
    P, agenda, logs, t = correr("BTC")
    disparar(agenda)
    r = [e for e in logs if e["tipo"] == "h59_relleno"][0]
    assert r["ask_llegada"] == .40 and r["asz_llegada"] == 50 and r["k0.02"]["clase"] == "llena" and r["k0.02"]["l2"]["clase"] == "llena"


# ------------------------------------------------------------------------------------------------ (3) libro mutable + evento base antes
def test_l2_copia_el_dict_vivo_y_reintenta_si_el_ws_lo_muta():
    class Mut:
        def __init__(self, fallos):
            self.fallos, self.d = fallos, {.45: 10}
        def keys(self):
            if self.fallos:
                self.fallos -= 1
                raise RuntimeError("dictionary changed size during iteration")
            return self.d.keys()
        def __getitem__(self, k):
            return self.d[k]
    lib = Lib()
    lib.ult_tk = {"tc": 100}
    lib.lib = {"tc": {"asks": Mut(2)}}
    assert mod._h59_l2(lib, "tc", 200, .45, 5.0, (100, .4, 1, .45, 10))["clase"] == "llena"       # 2 fallos, 3er intento bien
    lib.lib = {"tc": {"asks": Mut(9)}}
    assert mod._h59_l2(lib, "tc", 200, .45, 5.0, (100, .4, 1, .45, 10))["clase"] == "no_exacto_copia_inestable"


def test_un_fallo_en_la_llegada_deja_el_evento_base_y_un_error_explicito(monkeypatch):
    P, agenda, logs, t = correr("BTC")
    monkeypatch.setattr(mod.H59, "evaluar_evento", lambda *a, **k: (_ for _ in ()).throw(ValueError("boom")))
    disparar(agenda)
    tipos = [e["tipo"] for e in logs if e["tipo"].startswith("h59")]
    assert tipos == ["h59_evento", "h59_relleno_error"] and "boom" in [e for e in logs if e["tipo"] == "h59_relleno_error"][0]["error"]


# ------------------------------------------------------------------------------------------------ (4) una ruta, sha256
def test_la_regla_se_importa_de_una_sola_ruta_con_sha256_y_el_brazo_se_desactiva_si_no_coincide(monkeypatch):
    assert mod.H59_RUTA == AQUI / "h59_regla.py" and not (R.REPO / "h59_regla.py").exists()
    assert mod.H59_SHA256 == hashlib.sha256((AQUI / "h59_regla.py").read_bytes()).hexdigest() and mod.H59_ACTIVO is True
    P, agenda, logs, t = correr("BTC")
    disparar(agenda)
    assert all(e["regla_sha256"] == mod.H59_SHA256 for e in logs if e["tipo"] in ("h59_evento", "h59_relleno"))
    assert logs[[e["tipo"] for e in logs].index("h59_evento")]["regla_ruta"] == str(AQUI / "h59_regla.py")
    monkeypatch.setattr(mod, "H59_ACTIVO", False)                                    # sha distinto / modulo ausente: fail-closed del brazo
    P2, ag2, logs2, _ = correr("BTC")
    disparar(ag2)
    assert not [e for e in logs2 if e["tipo"].startswith("h59")] and [e for e in logs2 if e["tipo"] == "v4_evento"]


# ------------------------------------------------------------------------------------------------ (5) reinicio a mitad de cierre
def test_reinicio_no_duplica_el_evento_y_lo_perdido_se_declara(monkeypatch):
    P, agenda, logs, t = correr("BTC")
    disparar(agenda, hasta=t + 50)                                                    # evento base emitido; el proceso "muere" antes de la llegada
    mod._H59_VISTO.clear()                                                            # proceso nuevo: sin memoria, solo el disco
    logs2 = []
    mod.log = lambda ev: logs2.append(ev)
    with monkeypatch.context() as m:
        m.setattr(mod.time, "time", lambda: P.cie + 60)                              # 'ahora' = justo tras ese cierre (F2 se reinicia en minutos)
        mod._h59_reconciliar()
    assert logs2[-1]["tipo"] == "h59_relleno_perdido_reinicio" and logs2[-1]["marcas"] == [f"E|BTC|{P.cie}"]
    mod._H59_VISTO.clear()
    logs3 = []
    mod.log = lambda ev: logs3.append(ev)
    P3, ag3 = par("BTC")
    P3.al_cambiar("tc", t, P3.lib.top["tc"])                                          # el 2.o F2 ve la misma senal del mismo cierre
    disparar(ag3)
    tipos = [e["tipo"] for e in logs3 if e["tipo"].startswith("h59")]
    assert tipos == ["h59_evento_duplicado_omitido"]                                  # ni evento duplicado ni llegada
    assert (mod.OUT / f"h59_marcas_{mod.utc_dia(P.cie)}.txt").read_text().split() == [f"E|BTC|{P.cie}"]


def test_reconciliar_ignora_cierres_completos(monkeypatch):
    P, agenda, logs, t = correr("BTC")
    disparar(agenda)                                                                  # E y R
    mod._H59_VISTO.clear()
    logs2 = []
    mod.log = lambda ev: logs2.append(ev)
    with monkeypatch.context() as m:
        m.setattr(mod.time, "time", lambda: P.cie + 60)
        mod._h59_reconciliar()
    assert not logs2


# ------------------------------------------------------------------------------------------------ el parche
def test_parche_solo_anade_no_envia_y_reproduce_el_fichero(tmp_path):
    base = BASE.read_text().splitlines()
    nuevo = SRC.splitlines()
    borradas = [l for l in difflib.unified_diff(base, nuevo, lineterm="", n=0) if l.startswith("-") and not l.startswith("---")]
    assert borradas == []                                                             # el parche solo AÑADE lineas
    anadidas = "\n".join(l for l in difflib.unified_diff(base, nuevo, lineterm="", n=0) if l.startswith("+") and not l.startswith("+++"))
    for prohibido in ("post_order", "create_order", "dry_run=False", "sign(", "requests.post", "self._decidir(\"H59\"", "H59_RUTA.write"):
        assert prohibido not in anadidas
    assert "env.enviar" not in anadidas and "arm.tomar" not in anadidas and ".tomar(" not in anadidas
    (tmp_path / "f2_5m_barato_dryrun.py").write_text(BASE.read_text())
    r = subprocess.run(["patch", "-p1", "--no-backup-if-mismatch", "-i", str(AQUI / "f2_h59.patch")], cwd=tmp_path, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    assert (tmp_path / "f2_5m_barato_dryrun.py").read_text() == SRC                   # el .patch y la copia parcheada coinciden
