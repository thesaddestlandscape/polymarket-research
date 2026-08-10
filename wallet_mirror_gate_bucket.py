"""
wallet_mirror_gate_bucket.py — consumidor del gate por micro-bucket de
precio real de Wallet Mirror (P24), mismo patrón que gate_bucket_propio.py
pero para data/shadow/wallet_mirror_gate_bucket.json (generado por
analisis_wallet_mirror_gate_bucket_10ago.py).

Solo lectura: expone evaluar() para que un futuro FASE 2 (si se aprueba
explícitamente, ver project_p24_checklist_conexion_completo_10ago) pueda
consultar el veredicto de una tupla WALLET_MIRROR#tipo#activo#marco#grande
sin volver a calcular nada. Hoy WALLET_MIRROR no está en pares_permitidos_
live y nada llama a evaluar() todavía -- este módulo es infraestructura
preparada, no un veto activo.
"""
import json
import math
from pathlib import Path

DATA_PATH = Path("data/shadow/wallet_mirror_gate_bucket.json")
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


def evaluar(tipo: str, activo: str, marco: str, ask: float, jugada_grande: bool) -> dict:
    """{"veredicto": "malo_confirmado"|"bueno_confirmado"|"sin_concluir",
    "detalle": {...}|None}."""
    b = round(math.floor(ask / STEP + 1e-9) * STEP, 4)
    b_str = f"{b:.2f}"
    grande_str = "1" if jugada_grande else "0"
    clave_str = f"{tipo}#{activo}#{marco}#{grande_str}"

    tabla = _cargar().get(clave_str, {})
    detalle = tabla.get(b_str)
    if detalle is not None:
        return {"veredicto": detalle.get("veredicto", "sin_concluir"), "detalle": detalle}
    return {"veredicto": "sin_concluir", "detalle": None}
