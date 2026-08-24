"""
wallet_mirror_gate_bucket.py — consumidor del gate por micro-bucket de
precio real de Wallet Mirror (P24), mismo patrón que gate_bucket_propio.py
pero para data/shadow/wallet_mirror_gate_bucket.json (generado por
analisis_wallet_mirror_gate_bucket_10ago.py).

Solo lectura: expone evaluar() para consultar el veredicto de una tupla
WALLET_MIRROR#tipo#activo#marco#grande sin volver a calcular nada.

24-Ago (docstring desactualizada corregida): WALLET_MIRROR SÍ está en
pares_permitidos_live desde el 10/11/12-Ago (6 tuplas BTC#5/15/60min) y
wallet_mirror_executor_dryrun.py SÍ llama a evaluar() en el camino real
de ejecución (fail-closed, exige bueno_confirmado) -- este módulo dejó
de ser "infraestructura preparada" hace semanas, es veto activo sobre
dinero real.
"""
import json
import math
from pathlib import Path

_REPO = Path(__file__).resolve().parent
DATA_PATH = _REPO / "data/shadow/wallet_mirror_gate_bucket.json"
# 24-Ago (petición explícita Javi, mismo mecanismo que gate_bucket_propio.py
# desde el 05-Ago: "asegúrate que el mecanismo autoaprendiente tenga un
# backup que lo proteja siempre"): este gate no tenía NINGÚN cortacircuitos
# de emergencia -- WALLET_MIRROR pasó a mover dinero real el 10/11/12-Ago
# sin que nadie añadiera esta pieza. Fichero propio (no comparte namespace
# con gate_bucket_propio_override.json -- el formato de clave es distinto,
# tipo#activo#marco#grande#bucket, no strategy#activo#marco#decision#bucket).
OVERRIDE_PATH = _REPO / "data/live/wallet_mirror_gate_bucket_override.json"
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
    """Mismo patrón exacto que gate_bucket_propio.py::_cargar_override() --
    SIEMPRE gana sobre cualquier otro veredicto, incluido bueno_confirmado.
    Un fichero corrupto/inaccesible se trata como override vacío (no
    bloquea nada por error de lectura)."""
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


def bucket(ask: float) -> float:
    """Único punto de verdad del bucketing (STEP=0.05) -- mismo motivo que
    gate_bucket_propio.py::bucket() (24-Ago, /code-review): cualquier
    vigía externo que necesite reconstruir la MISMA clave exacta debe
    importar esto, no reimplementar la fórmula a mano."""
    return round(math.floor(ask / STEP + 1e-9) * STEP, 4)


def clave(tipo: str, activo: str, marco: str, jugada_grande: bool) -> str:
    """Única fuente de verdad del formato de clave (sin el sufijo de
    bucket) -- mismo motivo que bucket()."""
    return f"{tipo}#{activo}#{marco}#{'1' if jugada_grande else '0'}"


def evaluar(tipo: str, activo: str, marco: str, ask: float, jugada_grande: bool) -> dict:
    """{"veredicto": "malo_confirmado"|"bueno_confirmado"|"sin_concluir",
    "detalle": {...}|None}.

    Cortacircuitos de emergencia -- SIEMPRE se comprueba primero, gana
    sobre cualquier otro veredicto (incluido bueno_confirmado propio)."""
    clave_str = clave(tipo, activo, marco, jugada_grande)
    b_str = f"{bucket(ask):.2f}"
    override = _cargar_override()
    ov = override.get(f"{clave_str}#{b_str}") or override.get(clave_str)
    if ov is not None:
        return {
            "veredicto": "malo_confirmado",
            "detalle": {"origen": "override_emergencia", "motivo": ov.get("motivo", "sin motivo registrado"),
                        "desde": ov.get("desde")},
        }
    return evaluar_sin_override(tipo, activo, marco, ask, jugada_grande)


def evaluar_sin_override(tipo: str, activo: str, marco: str, ask: float, jugada_grande: bool) -> dict:
    """MISMA lógica que evaluar() pero SIN consultar el override de
    emergencia -- exclusivamente para el vigía de reapertura (24-Ago,
    /code-review, mismo hallazgo real que en gate_bucket_propio.py: con
    el override todavía escrito, evaluar() SIEMPRE devuelve
    malo_confirmado, sea cual sea el estado real de la tabla -- la
    condición de reapertura nunca se cumpliría)."""
    clave_str = clave(tipo, activo, marco, jugada_grande)
    b_str = f"{bucket(ask):.2f}"
    tabla = _cargar().get(clave_str, {})
    detalle = tabla.get(b_str)
    if detalle is not None:
        return {"veredicto": detalle.get("veredicto", "sin_concluir"), "detalle": detalle}
    return {"veredicto": "sin_concluir", "detalle": None}
