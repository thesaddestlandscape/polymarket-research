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
import threading
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

# Lectura INCREMENTAL (24-Sep, mismo patrón que fetch_libro_ambos_lados.
# _universo_activo): predictions_HOY.csv pesa ~520MB a media tarde y se
# releía ENTERO cada 20s desde cada hilo de momentum_ibs_ballena_executor
# (py-spy 24-Sep: 1861/2199 muestras del proceso ejeclive, dinero real).
# shadow_predict.py solo APENDIZA a este fichero (ningún proceso lo reescribe),
# así que basta con recordar el offset en bytes y parsear lo añadido. El índice
# es una unión mercado->decisiones que solo crece: resultado idéntico al de la
# relectura completa. Reset si cambia la fecha/inodo o el fichero encoge.
# Bloques de 8MB (RAM acotada en la lectura en frío) y corte SOLO por b"\n".
_BLOQUE_BYTES = 8 * 1024 * 1024
_lock = threading.Lock()
_inc = {"fecha": None, "ino": None, "offset": 0, "cab": None, "index": {}}


def _leer_nuevas(path: Path, fecha: str) -> None:
    """Llamar con _lock tomado. Si algo lanza, el offset no avanza y el
    tramo se reintenta entero en la siguiente llamada."""
    st = path.stat()
    if _inc["fecha"] != fecha or _inc["ino"] != st.st_ino or st.st_size < _inc["offset"]:
        _inc.update({"fecha": fecha, "ino": st.st_ino, "offset": 0, "cab": None, "index": {}})
    if st.st_size == _inc["offset"]:
        return
    cab = _inc["cab"]
    nuevos: dict[str, set] = {}
    consumido = 0
    resto = b""
    with open(path, "rb") as f:
        f.seek(_inc["offset"])
        pendiente = st.st_size - _inc["offset"]
        while pendiente > 0:
            trozo = f.read(min(_BLOQUE_BYTES, pendiente))
            if not trozo:
                break
            pendiente -= len(trozo)
            partes = (resto + trozo).split(b"\n")
            resto = partes.pop()
            consumido += sum(len(x) + 1 for x in partes)
            lineas = [x.rstrip(b"\r").decode("utf-8", errors="replace") for x in partes]
            if cab is None and lineas:
                cab = next(csv.reader([lineas[0]]))
                lineas = lineas[1:]
            if cab is None:
                continue
            i_s, i_m, i_d = cab.index("strategy"), cab.index("market_id"), cab.index("decision")
            for vals in csv.reader(lineas):
                if len(vals) <= max(i_s, i_m, i_d):
                    continue
                if vals[i_s] not in GBM_STRATEGIES:
                    continue
                mid, dec = vals[i_m], vals[i_d]
                # "SKIP" (estrategia disparó pero decidió no operar) NO es una
                # dirección real -- results.csv (base del análisis retrospectivo
                # del 19-Ago) nunca lo incluye, así que aquí tampoco cuenta.
                if not mid or dec not in ("BUY_YES", "BUY_NO"):
                    continue
                nuevos.setdefault(mid, set()).add(dec)
    _inc["cab"] = cab
    idx = _inc["index"]
    for mid, decs in nuevos.items():
        # set NUEVO (no mutar en sitio): otros hilos pueden estar iterando el
        # set que devolvió index.get() en evaluar() fuera del cerrojo.
        idx[mid] = idx.get(mid, set()) | decs
    _inc["offset"] += consumido


def _archivo_hoy() -> tuple[Path, str]:
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return DIR_SHADOW / f"predictions_{fecha}.csv", fecha


def _index_actualizado() -> dict:
    path, fecha = _archivo_hoy()
    if _cache["fecha"] == fecha and time.time() - _cache["ts"] < CACHE_TTL_S:
        return _cache["index"]
    with _lock:
        ahora = time.time()
        if _cache["fecha"] == fecha and ahora - _cache["ts"] < CACHE_TTL_S:
            return _cache["index"]  # otro hilo acaba de refrescar
        try:
            _leer_nuevas(path, fecha)
        except Exception:
            # OSError = fichero de hoy aún no existe; cualquier otro = fail-open
            # (puramente informacional). ts se actualiza también aquí: sin eso un
            # error persistente haría que CADA evaluar() de cada hilo reintentase
            # bajo el cerrojo, saltándose el TTL (/code-review 24-Sep).
            _cache["ts"] = ahora
            return _cache["index"]
        _cache["ts"] = ahora
        _cache["fecha"] = fecha
        _cache["index"] = _inc["index"]
        return _cache["index"]


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
