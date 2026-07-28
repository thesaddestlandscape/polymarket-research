"""
ballenas_banda_fina_gate.py — gate de entrada por micro-banda calibrada
(ballenas_observer.py::ballenas_timing_state_fino.json, paso 0.05) para
tuplas LIVE. Petición explícita Javi 28-Jul: "diseña el filtro de entrada
por bucket para todas las tuplas que estan operando en live" + "atendiendo
a los objetivos y la mision del proyecto" — responde a Stage 0 del plan
escalonado (project_plan_escalonado_200k_23jul): cerrar el gap modelo↔
realidad ANTES de escalar. El fichero fino ya lo calcula ballenas_observer.py
cada ciclo (paso 0.05, z-score, n_wallets, top1_share, restante_min de las
ganadoras) pero declara explícitamente "no lo consume ningún ejecutor
todavía" -- este módulo es ese consumidor, importable desde
shadow_predict.py y los ejecutores de ballenas sin duplicar lógica.

FASE 0 (esta implementación): SOLO OBSERVACIONAL. `evaluar()` siempre
devuelve permitido=True -- nunca bloquea una señal real todavía. Se limita
a calcular y exponer el veredicto que el gate DARÍA, para loguearlo como
feature y medir con datos reales (n, hit, pnl) si vetar de verdad evitaría
pérdidas antes de activarlo — mismo patrón que el resto del proyecto
(instrumentar observacional primero, aplicar después con aprobación
explícita + /code-review, CLAUDE.md "código que toca dinero"). Activar el
bloqueo real es un cambio de código de seguridad live y NO se hace en este
commit.

Diseño del veredicto:
- Sin fichero / sin combo (activo,marco) / combo no significativo (menos de
  N_MIN_INFORMATIVO trades de ballenas en alguna banda con z suficiente):
  "sin_banda_calibrada" -- sin evidencia, no se vetaría.
- py cae DENTRO de una banda_significativa: si restante_min actual >=
  rest_lo_min de esa banda (percentil 25 del timing de las ganadoras
  históricas), "banda_ok" -- llegamos con tiempo real, no solo comprando
  la confirmación después de que ya pasó. Si no, "banda_tardia" -- se
  vetaría en fase 1.
- py fuera de TODAS las bandas significativas: "fuera_de_bandas" -- sin
  evidencia en ese precio exacto, no se vetaría (mismo fail-open que
  veto_ballenas: este gate solo puede reducir una señal ya aprobada por el
  resto de la lógica, nunca inventar una nueva).
"""
import json
from pathlib import Path

FINO_PATH = Path("data/shadow/ballenas_timing_state_fino.json")
MARCO_MAP = {"15min": "15m", "60min": "60m", "5min": "5m", "240min": "240m"}

_cache = {"mtime": None, "data": {}}


def _cargar_fino() -> dict:
    try:
        mtime = FINO_PATH.stat().st_mtime
    except OSError:
        return {}
    if _cache["mtime"] != mtime:
        try:
            _cache["data"] = json.loads(FINO_PATH.read_text(encoding="utf-8"))
            _cache["mtime"] = mtime
        except Exception:
            pass  # se queda con la última copia válida conocida (mejor que nada)
    return _cache["data"]


def evaluar(activo: str, marco: str, py: float, restante_min: float | None) -> dict:
    """Devuelve {"permitido": bool, "vetaria_fase1": bool, "motivo": str,
    "banda": {...} | None}. `permitido` es SIEMPRE True en fase 0 (ver
    docstring del módulo) -- `vetaria_fase1` es el veredicto real para
    medir con datos, sin aplicarlo todavía."""
    marco_ball = MARCO_MAP.get(marco, marco)
    data = _cargar_fino()
    info = data.get(f"{activo}#{marco_ball}")
    if not info or not info.get("significativo"):
        return {"permitido": True, "vetaria_fase1": False, "motivo": "sin_banda_calibrada", "banda": None}

    for b in info.get("bandas_significativas") or []:
        if b["banda_lo"] <= py < b["banda_hi"]:
            rest_min_req = b.get("rest_lo_min")
            if rest_min_req is None:
                return {"permitido": True, "vetaria_fase1": False, "motivo": "banda_sin_timing", "banda": b}
            if restante_min is None:
                return {"permitido": True, "vetaria_fase1": False, "motivo": "sin_restante_min", "banda": b}
            if restante_min < rest_min_req:
                return {"permitido": True, "vetaria_fase1": True,
                        "motivo": f"banda_tardia py={py:.3f} restante={restante_min:.2f}<{rest_min_req:.2f}",
                        "banda": b}
            return {"permitido": True, "vetaria_fase1": False,
                    "motivo": f"banda_ok py={py:.3f} rest_lo={rest_min_req:.2f}", "banda": b}

    return {"permitido": True, "vetaria_fase1": False, "motivo": "fuera_de_bandas_significativas", "banda": None}
