"""Enviador.enviar(inline=True): mismo hilo, Future ya resuelto, idempotencia y veto de riesgo intactos (dry-run, sin red).
Uso: .venv/bin/python -m pytest -q tests/test_ejecutor_rapido_enviador_inline.py"""
import json
import sys
import threading
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import ejecutor_rapido as er  # noqa: E402


class _R:
    def __init__(self, ok=True):
        self.ok = ok

    def puede(self):
        return self.ok, "ok" if self.ok else "vetado"


def test_inline_mismo_hilo_resuelto_e_idempotente(tmp_path):
    led = tmp_path / "l.jsonl"
    env = er.Enviador(None, led, _R(), dry_run=True, hilos=1)
    hilo = []
    orig = env._log
    env._log = lambda ev: (hilo.append(threading.current_thread().name), orig(ev))
    fut = env.enviar("k1", None, "FOK", er.ahora_ms(), meta={"x": 1}, inline=True)
    assert fut.done()
    r = fut.result()
    assert r["fase"] == "respuesta" and r["res"] == {"dry_run": True} and r["ms_decision_a_envio"] < 5
    assert hilo == [threading.current_thread().name]                  # respuesta registrada desde el hilo llamador
    assert env.enviar("k1", None, "FOK", er.ahora_ms(), inline=True) is None   # idempotencia
    env.vaciar_ledger()
    fases = [json.loads(ln)["fase"] for ln in open(led)]
    assert fases == ["intencion", "respuesta"]


def test_inline_respeta_veto_de_riesgo(tmp_path):
    env = er.Enviador(None, tmp_path / "l.jsonl", _R(ok=False), dry_run=True, hilos=1)
    assert env.enviar("k2", None, "FOK", er.ahora_ms(), inline=True) is None


def test_inline_excepcion_queda_en_el_future(tmp_path):
    env = er.Enviador(None, tmp_path / "l.jsonl", _R(), dry_run=True, hilos=1)
    llamadas = {"n": 0}

    def puede():
        llamadas["n"] += 1
        if llamadas["n"] == 2:                                      # el re-chequeo dentro de _post revienta
            raise RuntimeError("boom")
        return True, "ok"
    env.riesgo.puede = puede
    fut = env.enviar("k3", None, "FOK", er.ahora_ms(), inline=True)  # no propaga al llamador
    assert fut.done() and isinstance(fut.exception(), RuntimeError)


def test_por_defecto_sigue_usando_el_pool(tmp_path):
    env = er.Enviador(None, tmp_path / "l.jsonl", _R(), dry_run=True, hilos=1)
    fut = env.enviar("k4", None, "FOK", er.ahora_ms())
    r = fut.result(5)
    assert r["fase"] == "respuesta"
