"""Test del parche F2 (brazo sombra H59) con libro simulado. NO arranca F2, no abre WS, no firma, no envia: Par se construye con stubs y
`_decidir` (el unico punto que toca el Enviador DRY-RUN) se sustituye. Carga el modulo parcheado desde el texto (REPO -> raiz del repo).
Ejecutar: cd experimentos/5m_barato/h59_colchon && python3 -m pytest -q test_f2_h59_parche.py"""
import sys
import threading
import types
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import h59_regla as R  # noqa: E402

SRC = (AQUI / "f2_5m_barato_dryrun.h59.py").read_text()
assert "REPO = Path(__file__).resolve().parent\n" in SRC
mod = types.ModuleType("f2_h59_cargado")
mod.__file__ = str(R.REPO / "f2_5m_barato_dryrun.py")
sys.path.insert(0, str(R.REPO))
exec(compile(SRC, mod.__file__, "exec"), mod.__dict__)        # noqa: S102  (test: carga el parche tal cual)


class Lib:
    def __init__(self):
        self.top, self.lib = {}, {}
    def fresco(self, tk, max_edad_ms=3000):
        return True


def par(mo="BTC"):
    P = mod.Par.__new__(mod.Par)
    P.mo, P.cie, P.s = mo, 1792369800, "Up"
    P.m5, P.m15 = {"id": "M5"}, {"id": "M15"}
    P.tc, P.to = "tc", "to"
    P.motivos, P.v4, P.v7_ult, P.v7_hecho, P.v7_intentos = Counter(), {"activo": False, "ult": None, "n": 0}, -10 ** 12, set(), Counter()
    P.t_ini, P.t_fin = (P.cie - 300) * 1000 + 1500, (P.cie - 10) * 1000
    P.lock, P.lib = threading.Lock(), Lib()
    P.lib.top = {"tc": (0, .38, 30, .40, 50), "to": (0, .50, 50, .52, 50)}
    P.lib.lib = {"tc": {"asks": {.40: 50}}}
    agenda = []
    P.ctx = types.SimpleNamespace(agenda=types.SimpleNamespace(en=lambda t, fn: agenda.append((t, fn))))
    P.llamadas = []
    P._decidir = lambda regla, t, p, extra: (P.llamadas.append((regla, t, p, extra)) or {"enviador": True})
    return P, agenda


def correr(mo="BTC"):
    logs = []
    mod.log = lambda ev: logs.append(ev)
    P, agenda = par(mo)
    t = P.t_ini + 500
    P.al_cambiar("tc", t, P.lib.top["tc"])
    return P, agenda, logs, t


def test_h59_dispara_una_vez_por_cierre_y_solo_btc():
    P, agenda, logs, t = correr("BTC")
    ev = [e for e in logs if e["tipo"] == "h59_evento"]
    assert len(ev) == 1 and [e["tipo"] for e in logs].count("v4_evento") == 1
    assert ev[0]["limites"] == {"0.00": .43, "0.01": .44, "0.02": .45, "0.03": .46, "0.05": .48} and ev[0]["ask5_sz_t0"] == 50
    assert P.llamadas[-1] == ("H59", t, .45, {"n": 1}) and any(r[0] == "v4" for r in P.llamadas)
    assert any(a[0] == t + 215 for a in agenda)                                    # llegada a +215 ms
    P.lib.top["tc"] = (0, .38, 30, .40, 51)                                        # cambio de tamano, misma senal: sigue activo, n no sube
    P.al_cambiar("tc", t + 50, P.lib.top["tc"])
    assert len([e for e in logs if e["tipo"] == "h59_evento"]) == 1
    P2, ag2, logs2, _ = correr("ETH")
    assert not [e for e in logs2 if e["tipo"] == "h59_evento"] and [e for e in logs2 if e["tipo"] == "v4_evento"]


def test_h59_relleno_usa_el_libro_en_la_llegada_y_el_tamano():
    P, agenda, logs, t = correr("BTC")
    P.lib.top["tc"] = (0, .42, 5, .44, 20)                                         # +4c a la llegada, 20 acciones
    P.lib.lib["tc"]["asks"] = {.44: 20, .50: 100}
    for tt, fn in agenda:
        if tt == t + 215:
            fn()
    r = [e for e in logs if e["tipo"] == "h59_relleno"][0]
    assert r["fresco"] and r["k0.00"]["clase"] == "repreciado" and r["k0.02"]["clase"] == "llena" and r["k0.02"]["precio"] == .44
    assert r["k0.02"]["l2"]["clase"] == "llena" and r["k0.02"]["l2"]["acciones"] == 5.0
    P2, ag2, logs2, t2 = correr("BTC")
    P2.lib.top["tc"] = (0, .42, 5, .45, 3)                                         # cabe en el limite pero solo 3 acciones: la FOK muere
    P2.lib.lib["tc"]["asks"] = {.45: 3}
    [fn() for tt, fn in ag2 if tt == t2 + 215]
    r2 = [e for e in logs2 if e["tipo"] == "h59_relleno"][0]
    assert r2["k0.02"]["clase"] == "corte_tamano" and r2["k0.02"]["l2"]["clase"] == "parcial"      # el L2 sombra muestra el parcial; el gate usa el nivel 1


def test_parche_no_toca_nada_mas_y_no_envia():
    base = (R.REPO / "f2_5m_barato_dryrun.py").read_text().splitlines()
    nuevo = SRC.splitlines()
    import difflib
    borradas = [l for l in difflib.unified_diff(base, nuevo, lineterm="", n=0) if l.startswith("-") and not l.startswith("---")]
    assert borradas == []                                                          # el parche solo AÑADE lineas
    anadidas = "\n".join(l for l in difflib.unified_diff(base, nuevo, lineterm="", n=0) if l.startswith("+") and not l.startswith("+++"))
    for prohibido in ("enviar(", "post_order", "create_order", "dry_run=False", "sign(", "requests.post"):
        assert prohibido not in anadidas
