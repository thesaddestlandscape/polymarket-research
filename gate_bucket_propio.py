"""
gate_bucket_propio.py — gate de entrada por micro-bucket de precio,
construido desde NUESTRO PROPIO histórico de PnL (results.csv), no desde
timing de ballenas. Petición explícita Javi 28-Jul, tras refutar
retrospectivamente que reusar el timing de ballenas para gatear
FAVORITO_CONFIRMADO/GBM_LATE_15M no transfiere (ver
ballenas_banda_fina_gate.py y project_gate_banda_fina_ballenas_28jul).

Datos: data/shadow/gate_bucket_propio.json, generado por
analisis_gate_bucket_propio_28jul.py (shuffle test + split-half
cronológico, n>=15 -- ver ese fichero para la metodología completa).
Solo los buckets "malo_confirmado"/"bueno_confirmado" tienen evidencia
suficiente; todo lo demás es "sin_concluir" y no se toca (fail-open).
"""
import json
from pathlib import Path

DATA_PATH = Path("data/shadow/gate_bucket_propio.json")
STEP = 0.05

_cache = {"mtime": None, "data": {}}


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


def evaluar(tupla_str: str, py: float) -> dict:
    """{"veredicto": "malo_confirmado"|"bueno_confirmado"|"sin_concluir",
    "detalle": {...}|None}. No decide permitido/vetado -- eso lo hace el
    caller (fase 0: solo loguea; fase 1: veta si malo_confirmado)."""
    import math
    b = round(math.floor(py / STEP) * STEP, 4)
    tabla = _cargar().get(tupla_str, {})
    detalle = tabla.get(f"{b:.2f}")
    if detalle is None:
        return {"veredicto": "sin_concluir", "detalle": None}
    return {"veredicto": detalle.get("veredicto", "sin_concluir"), "detalle": detalle}
