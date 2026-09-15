#!/usr/bin/env python3
"""ballenas_cross_check.py — 15-Sep, módulo LIGERO (sin dependencias
pesadas, mismo criterio que candidata9_gate_bucket.py/wallet_mirror_gate_
bucket.py) para que CUALQUIER familia (SNIPER/DISPERSO/WALLET_MIRROR/
CANDIDATA9_BOT_CONSENSO) consulte el cruce sistemático con ballenas como
REFUERZO de confianza -- petición explícita Javi: "me parece bien como
refuerzo, pero no como veto".

Única fuente de verdad: data/shadow/ballenas_hitrate_por_bucket.json,
regenerado a diario por analisis_ballenas_hitrate_por_bucket.py. Este
módulo solo LEE -- nunca escribe, nunca decide, nunca degrada un
veredicto. El caller decide qué hacer con la información (loguearla,
mostrarla en un informe, o en el futuro ponderarla si se acumula
suficiente experiencia revisándola).
"""
import json
import math
from pathlib import Path

REPO = Path(__file__).resolve().parent
GATE_PATH = REPO / "data" / "shadow" / "ballenas_hitrate_por_bucket.json"
STEP = 0.05

# bot_wallets/candidata9/wallet_mirror usan "5min"/"15min"/"60min"/"240min";
# ballenas_timing_history.csv usa "5m"/"15m"/"60m"/"240m"/"weekly".
_MARCO_A_BALLENAS = {"5min": "5m", "15min": "15m", "60min": "60m", "240min": "240m"}

_cache: dict = {"mtime": None, "datos": {}}


def _bucket(p: float) -> float:
    return round(math.floor(p / STEP + 1e-9) * STEP, 4)


def _cargar() -> dict:
    try:
        st = GATE_PATH.stat()
    except OSError:
        return {}
    if _cache["mtime"] != st.st_mtime:
        try:
            _cache["datos"] = json.loads(GATE_PATH.read_text(encoding="utf-8"))
            _cache["mtime"] = st.st_mtime
        except Exception:
            return {}
    return _cache["datos"]


def consultar(activo: str, marco: str, py: float, direccion: str | None = None) -> dict:
    """Devuelve {"hit_rate_yes", "n", "breakeven_yes", "coincide"} para
    (activo, marco, micro-bucket de py en perspectiva YES).

    "coincide" (solo si se pasa `direccion`, "BUY_YES"/"BUY_NO") compara
    el hit-rate de ballenas contra el BREAKEVEN implícito del precio
    (≈py, no un 50% fijo) -- comparar contra 50% sería un error: a
    py=0.27 lo normal en un mercado bien calibrado es que YES gane ~27%
    de las veces, así que "hit_rate_yes=0.26<0.5" no dice nada sobre si
    hay edge, solo confirma el precio. Lo que sí importa es si el
    hit-rate real de ballenas en esa zona SUPERA el breakeven de esa
    misma zona (igual que wilson90lo>ask_medio en el resto del proyecto).
    BUY_YES coincide si hit_rate_yes>py; BUY_NO coincide si
    hit_rate_yes<py (equivalente a que NO gane más de lo que su propio
    precio implica). Puramente informativo, el caller decide si eso pesa
    algo -- nunca bloquea nada por sí solo. Sin datos suficientes ->
    {"hit_rate_yes": None, "n": 0, "breakeven_yes": None, "coincide":
    None} (fail-neutral, nunca fail-closed)."""
    marco_ballenas = _MARCO_A_BALLENAS.get(marco, marco)
    datos = _cargar()
    b = _bucket(py)
    clave = f"{activo}#{marco_ballenas}#{b:.2f}"
    info = datos.get(clave)
    if not info:
        return {"hit_rate_yes": None, "n": 0, "breakeven_yes": None, "coincide": None}
    hit_rate_yes = info.get("hit_rate_yes")
    n = info.get("n", 0)
    coincide = None
    if direccion is not None and hit_rate_yes is not None:
        if direccion == "BUY_YES":
            coincide = hit_rate_yes > py
        elif direccion == "BUY_NO":
            coincide = hit_rate_yes < py
    return {"hit_rate_yes": hit_rate_yes, "n": n, "breakeven_yes": round(py, 4), "coincide": coincide}
