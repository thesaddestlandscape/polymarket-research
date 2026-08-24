"""
gate_bucket_kelly.py — consumidor de solo lectura de
data/shadow/gate_bucket_kelly.json (analisis_gate_bucket_kelly_24ago.py),
mismo patrón exacto que gate_bucket_propio.py pero para g(f) (Kelly) en
vez de pnl_neto lineal.

25-Ago (Javi: "vamos con el hallazgo 1 a resolver" -- conectar el gate
que llevaba desde el 24-Ago solo observacional): el análisis ya
confirmó, con rigor completo (Wilson/bootstrap+shuffle+split-half+BH-FDR),
payout inverso REAL en micro-buckets de tuplas YA EN VIVO
(BALLENAS_TARDIAS#{ETH,DOGE}#5min#BUY_YES[0.00,0.05)) -- PnL lineal
positivo, crecimiento compuesto negativo. Sin este módulo, ese hallazgo
no tenía ningún efecto sobre dinero real.

Clave/bucket: IDÉNTICO formato que gate_bucket_propio.py (STRATEGY#
subtype#DECISION, bucket grid 0.05 sobre precio_yes_mercado RAW) -- así
ambos gates hablan de la MISMA celda sin traducción.
"""
import json
import math
from pathlib import Path

_REPO = Path(__file__).resolve().parent
DATA_PATH = _REPO / "data/shadow/gate_bucket_kelly.json"
# Cortacircuitos de emergencia -- mismo mecanismo que gate_bucket_propio.py/
# wallet_mirror_gate_bucket.py (petición Javi 05-Ago/24-Ago: "el mecanismo
# autoaprendiente tiene que tener un backup que lo proteja siempre").
OVERRIDE_PATH = _REPO / "data/live/gate_bucket_kelly_override.json"
STEP = 0.05

_cache = {"mtime": None, "data": {}}
_cache_override = {"mtime": None, "data": {}}


def _cargar() -> dict:
    try:
        mtime = DATA_PATH.stat().st_mtime
    except OSError:
        return {}
    if _cache["mtime"] != mtime:
        try:
            _cache["data"] = json.loads(DATA_PATH.read_text(encoding="utf-8"))
            _cache["mtime"] = mtime
        except Exception:
            pass
    return _cache["data"]


def _cargar_override() -> dict:
    try:
        mtime = OVERRIDE_PATH.stat().st_mtime
    except OSError:
        return {}
    if _cache_override["mtime"] != mtime:
        try:
            _cache_override["data"] = json.loads(OVERRIDE_PATH.read_text(encoding="utf-8"))
            _cache_override["mtime"] = mtime
        except Exception:
            pass
    return _cache_override["data"]


def bucket(py: float) -> float:
    """Mismo bucketing exacto que gate_bucket_propio.py::bucket() (STEP=0.05,
    +1e-9 contra el mismo bug de precisión de coma flotante en múltiplos
    exactos de STEP)."""
    return round(math.floor(py / STEP + 1e-9) * STEP, 4)


def evaluar(tupla_str: str, py: float) -> dict:
    """{"veredicto": "malo_confirmado"|"sin_concluir", "detalle": {...}|None}.
    Solo tiene DOS estados (a diferencia de gate_bucket_propio) -- este
    gate no promueve "bueno_confirmado" propio, solo AÑADE un veto encima
    del que ya decide gate_bucket_propio; su ausencia de opinión nunca
    bloquea nada (fail-open a sin_concluir, el caller decide qué hacer).
    Cortacircuitos de emergencia -- SIEMPRE se comprueba primero."""
    b_str = f"{bucket(py):.2f}"
    override = _cargar_override()
    ov = override.get(f"{tupla_str}#{b_str}") or override.get(tupla_str)
    if ov is not None:
        return {
            "veredicto": "malo_confirmado",
            "detalle": {"origen": "override_emergencia", "motivo": ov.get("motivo", "sin motivo registrado"),
                        "desde": ov.get("desde")},
        }
    return evaluar_sin_override(tupla_str, py)


def evaluar_sin_override(tupla_str: str, py: float) -> dict:
    """MISMA lógica que evaluar() pero SIN el override -- exclusivamente
    para un futuro vigía de reapertura (mismo motivo que gate_bucket_
    propio.py/wallet_mirror_gate_bucket.py: con el override todavía
    escrito, evaluar() SIEMPRE devuelve malo_confirmado)."""
    b_str = f"{bucket(py):.2f}"
    tabla = _cargar().get(tupla_str, {})
    detalle = tabla.get(b_str)
    if detalle is not None and detalle.get("veredicto") == "malo_confirmado":
        return {"veredicto": "malo_confirmado", "detalle": detalle}
    return {"veredicto": "sin_concluir", "detalle": detalle}
