#!/usr/bin/env python3
"""
gbm_confluencia.py — FASE 1 (solo instrumentación, cero riesgo) del
hallazgo del 19-Ago: la familia GBM (edge direccional real, fill-ability
pésima 6-36%, arquetipo A) tiene edge que hoy no se puede cobrar
ejecutándola directamente. Cruce retrospectivo (results.csv, post-TWAP,
15.086 mercados con señal de ambas familias):

  GBM COINCIDE con la dirección de una señal arquetipo B (BALLENAS_*,
  FAVORITO_CONFIRMADO*): PnL/trade=+0.0156 (n=3854)
  GBM DISCREPA:                          PnL/trade=-0.1072 (n=4558)
  p_shuffle=0.0000, split-half robusto, 10/12 combos activo#marco en la
  misma dirección con n>=40.

Mecanismo dominante: NO es un boost cuando coincide, es un VETO cuando
discrepa. Candidatas directas a rescatar: FAVORITO_CONFIRMADO#{ETH,SOL}
#15min#BUY_YES, pausadas 28-Jul por payout inverso -- son los 2 combos
con mejor COINCIDE de toda la tabla (+0.163/+0.151).

Este módulo SOLO calcula la etiqueta `gbm_direccion_coincide` en el
instante de decisión de las estrategias arquetipo B, para que acumulen
n forward limpio -- NO toca prob_yes, NO cambia ninguna decisión ni
ejecución. Ver idea_gbm_confluencia_arquetipo_b_19ago en memoria.

Lee `data/shadow/predictions_YYYY-MM-DD.csv` (el fichero que
shadow_predict.py y los ejecutores de baja latencia YA escriben en
near-tiempo-real) buscando señales de la familia GBM en el MISMO
market_id -- no una llamada de red nueva, reusa lo que ya existe.

Cacheado por TTL fijo (no por mtime, a propósito -- ver
project_gbm_confluencia_ttl_no_mtime_19ago en memoria): shadow_predict.py
es el MISMO proceso que escribe este fichero, con el handle abierto
durante todo el ciclo -- un caché por mtime se invalidaría en cada
escritura propia del ciclo (docenas por market loop) y forzaría reparsear
el CSV entero (creciente, ~10-40MB/día) decenas de veces por ciclo,
mismo patrón de fondo que el incidente de box_builder_fase0 (19-Ago,
CSV de 295MB). Con TTL, se reparsea como mucho una vez por ventana,
independientemente de cuántas escrituras haya de por medio.
"""
import csv
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"

# Misma lista de 9 estrategias usada en el análisis retrospectivo del
# 19-Ago (excluye variantes wrapper como MULTIHORIZONTE_XXX si las hubiera
# -- ver ESTRATEGIAS en shadow_predict.py para la lista completa registrada).
GBM_STRATEGIES = frozenset({
    "GBM_LATE_15M", "GBM_LATE_15M_TARDIO", "GBM_LATE_15M_ESPACIO_ATR",
    "GBM_LATE_15M_PYCONFIRMADO", "GBM_LATE_15M_MULTIHORIZONTE",
    "GBM_LATE_5M", "GBM_LATE_60M", "UPDOWN_GBM", "UPDOWN_GBM_15M_TARDIO",
})

# 20s ~ cadencia del fast loop -- como mucho un reparseo por ciclo,
# independientemente de cuántas escrituras propias haga el ciclo de por medio.
CACHE_TTL_S = 20.0

_cache = {"ts": 0.0, "fecha": None, "index": {}}


def _archivo_hoy() -> tuple[Path, str]:
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return DIR_SHADOW / f"predictions_{fecha}.csv", fecha


def _index_actualizado() -> dict:
    ahora = time.time()
    _, fecha = _archivo_hoy()
    if _cache["fecha"] == fecha and ahora - _cache["ts"] < CACHE_TTL_S:
        return _cache["index"]
    path = DIR_SHADOW / f"predictions_{fecha}.csv"
    index: dict[str, set] = {}
    try:
        with open(path, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                s = r.get("strategy")
                if s not in GBM_STRATEGIES:
                    continue
                mid = r.get("market_id")
                dec = r.get("decision")
                # "SKIP" (estrategia disparó pero decidió no operar) NO es una
                # dirección real -- results.csv (base del análisis retrospectivo
                # del 19-Ago) nunca lo incluye, así que aquí tampoco cuenta.
                if not mid or dec not in ("BUY_YES", "BUY_NO"):
                    continue
                index.setdefault(mid, set()).add(dec)
    except OSError:
        return _cache["index"]  # fichero de hoy aún no existe -- fail-open al último caché
    except Exception:
        return _cache["index"]  # fail-open a la última versión cacheada, puramente informacional
    _cache["ts"] = ahora
    _cache["fecha"] = fecha
    _cache["index"] = index
    return index


def evaluar(market_id: str, decision_propia: str) -> dict:
    """{"gbm_direccion_coincide": "SI"|"NO"|"SIN_SENAL_GBM"|"GBM_CONTRADICTORIO",
        "gbm_decisiones": [...]}. Nunca lanza -- fail-open a SIN_SENAL_GBM."""
    if not market_id or not decision_propia:
        return {"gbm_direccion_coincide": "SIN_SENAL_GBM", "gbm_decisiones": []}
    try:
        index = _index_actualizado()
        decisiones = index.get(market_id)
    except Exception:
        return {"gbm_direccion_coincide": "SIN_SENAL_GBM", "gbm_decisiones": []}
    if not decisiones:
        return {"gbm_direccion_coincide": "SIN_SENAL_GBM", "gbm_decisiones": []}
    if len(decisiones) > 1:
        # GBM internamente contradictorio en este mercado (2+ subtipos en
        # direcciones distintas) -- excluido del análisis retrospectivo,
        # se etiqueta aparte, no se cuenta como SI ni NO.
        return {"gbm_direccion_coincide": "GBM_CONTRADICTORIO", "gbm_decisiones": sorted(decisiones)}
    (unica,) = decisiones
    coincide = "SI" if unica == decision_propia else "NO"
    return {"gbm_direccion_coincide": coincide, "gbm_decisiones": [unica]}
