"""
kelly_precio_gate.py — consumidor del gate de corrección de Kelly por
precio de entrada (ver analisis_kelly_precio_gate_29jul.py para la
metodología: Wilson+shuffle+split-half+BH-FDR sobre results.csv,
agrupado por familia de arquetipo x bucket de precio 0.10).

Mismo patrón fail-open que gate_bucket_propio.py: si el fichero no existe,
la familia no tiene datos, o el bucket no está "confirmado", devuelve
factor=1.0 (no-op) -- nunca inventa una corrección sin evidencia.

Petición Javi 29-Jul: atacar primero GBM_LATE_15M#0.30-0.40 (infra-
dimensionada 1.1x-2.3x, n=1837-7234, el bucket con más evidencia de todo
el barrido). live_stake.py::_kelly_precio_factor() es el único caller.
"""
import json
import math
from pathlib import Path

DATA_PATH = Path("data/shadow/kelly_precio_gate.json")
STEP = 0.10

_cache = {"mtime": None, "data": {}}


def _familia(strategy: str) -> str:
    """Debe coincidir EXACTO con _familia() de analisis_kelly_precio_gate_29jul.py
    -- si se cambia el agrupamiento ahí, cambiar aquí también."""
    if strategy.startswith("GBM_LATE"):
        return "GBM_LATE_15M_FAMILIA"
    if strategy.startswith("FAVORITO_CONFIRMADO"):
        return "FAVORITO_CONFIRMADO_FAMILIA"
    if strategy.startswith("BALLENAS"):
        return "BALLENAS_FAMILIA"
    if strategy.startswith("UPDOWN_GBM"):
        return "UPDOWN_GBM_FAMILIA"
    return strategy


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


def evaluar(strategy: str, precio_decision: float) -> dict | None:
    """precio_decision = precio en la perspectiva de la DECISIÓN (ya
    flipado a 1-precio_yes si es BUY_NO -- el caller es responsable de
    resolver esto, igual que gate_bucket_propio.evaluar()).

    Devuelve None si no hay evidencia (fail-open, factor=1.0 para el
    caller), o {"veredicto", "ratio_correccion", "bucket", "familia", "n"}
    si el bucket está en el gate (confirmado o no)."""
    familias = _cargar().get("familias", {})
    familia = _familia(strategy)
    tabla = familias.get(familia)
    if not tabla:
        return None
    b = round(math.floor(precio_decision / STEP) * STEP, 4)
    entrada = tabla.get(f"{b:.2f}")
    if entrada is None:
        return None
    return {
        "veredicto": entrada.get("veredicto", "sin_concluir"),
        "ratio_correccion": entrada.get("ratio_correccion"),
        "bucket": f"{b:.2f}",
        "familia": familia,
        "n": entrada.get("n"),
    }
