#!/usr/bin/env python3
"""candidata9_gate_bucket.py — 08-Sep, módulo LIGERO (sin dependencias
pesadas -- solo json/math/pathlib) que expone el gate de micro-bucket de
CANDIDATA9_BOT_CONSENSO (candidata9_10_gate_bucket.json) con la MISMA
firma que wallet_mirror_gate_bucket.py/resolution_sniper_naive_gate_
bucket.py, para poder registrarse en live_trade.py::
_GATES_EXTERNOS_POR_ESTRATEGIA sin crear un import circular.

Por qué un módulo aparte y no reusar la función ya escrita en
candidata9_bot_consenso_reactivo_fase0.py: ese módulo importa
wallet_mirror_tracker (para _fillability_mirror), que a su vez importa
live_trade -- si live_trade.py importara candidata9_bot_consenso_
reactivo_fase0.py directamente, el ciclo live_trade → fase0 →
wallet_mirror_tracker → live_trade rompería el arranque del proceso.
Mismo motivo por el que wallet_mirror_gate_bucket.py vive aislado de
wallet_mirror_tracker.py pese a evaluar exactamente los mismos datos.

Única fuente de verdad para el precio: candidata9_10_gate_bucket.json,
regenerado por analisis_candidata9_10_gate_bucket_26ago.py (cron/vigía ya
existente, ver vigia_candidata9_10_gate_bucket_26ago.py). Este módulo
solo LEE -- nunca escribe, nunca decide qué es bueno_confirmado, solo
expone el veredicto ya calculado con la firma que live_trade.py espera.
"""
import json
import math
from pathlib import Path

REPO = Path(__file__).resolve().parent
GATE_PATH = REPO / "data" / "shadow" / "candidata9_10_gate_bucket.json"
GATE_STEP = 0.05

_gate_cache: dict = {"mtime": None, "datos": {}}


def _gate_veredicto_dict(activo: str, marco: str, precio: float) -> dict:
    """Consulta EN CALIENTE candidata9_10_gate_bucket.json -- única fuente
    de verdad, autoaprendiente (mismo patrón que gate_bucket_propio.py en
    cripto). Cachea por mtime, no relee el fichero en cada llamada. Fail-
    closed: sin fichero/clave/bucket -> {"veredicto": "sin_concluir"},
    nunca "permitir por defecto"."""
    try:
        st = GATE_PATH.stat()
    except OSError:
        return {"veredicto": "sin_concluir", "detalle": {"origen": "sin_fichero"}}
    if _gate_cache["mtime"] != st.st_mtime:
        try:
            _gate_cache["datos"] = json.loads(GATE_PATH.read_text(encoding="utf-8"))
            _gate_cache["mtime"] = st.st_mtime
        except Exception:
            return {"veredicto": "sin_concluir", "detalle": {"origen": "fichero_ilegible"}}
    clave = f"CANDIDATA9_BOT_CONSENSO#{activo}#{marco}"
    tabla = _gate_cache["datos"].get(clave)
    if not tabla:
        return {"veredicto": "sin_concluir", "detalle": {"origen": "sin_clave", "clave": clave}}
    bucket_key = f"{math.floor(precio / GATE_STEP + 1e-9) * GATE_STEP:.2f}"
    info = tabla.get(bucket_key)
    if not info:
        return {"veredicto": "sin_concluir", "detalle": {"origen": "sin_bucket", "bucket": bucket_key}}
    return info


def evaluar(activo: str, marco: str, precio: float) -> dict:
    """Alias directo, para llamadores que ya tienen (activo, marco, precio)
    resueltos (candidata9_bot_consenso_reactivo_fase0.py/executor)."""
    return _gate_veredicto_dict(activo, marco, precio)


def evaluar_para_recheck(subtype: str, direction: str, py: float, contexto: dict) -> dict:
    """Firma uniforme que live_trade.py::_ejecutar_orden_polymarket usa en
    el re-chequeo post-requote y en el multi-lectura de justo antes de
    firmar (registrado en _GATES_EXTERNOS_POR_ESTRATEGIA) -- mismo patrón
    que wallet_mirror_gate_bucket.py::evaluar_para_recheck (ver su
    docstring). `py` llega en perspectiva YES -- se convierte al precio
    del lado que de verdad estamos comprando (el gate opera sobre el ask
    del lado mayoritario, no sobre YES a secas)."""
    partes = subtype.split("#")
    if len(partes) != 2:
        return {"veredicto": "sin_concluir", "detalle": {"origen": "subtype_invalido"}}
    activo, marco = partes
    ask = py if direction == "BUY_YES" else round(1.0 - py, 6)
    return _gate_veredicto_dict(activo, marco, ask)
