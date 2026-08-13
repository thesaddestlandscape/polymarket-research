#!/usr/bin/env python3
"""
gbmlate_fade_depth_fase0.py — FASE 0 (SOLO OBSERVACIÓN) del hallazgo de
hoy (12-Ago, petición Javi: "vamos con el 1"): dentro de la familia
GBM_LATE_15M (base/ESPACIO_ATR/TARDIO/PYCONFIRMADO/MULTIHORIZONTE), el
subconjunto donde el libro del lado ORIGINAL tiene profundidad real
(ratio_vs_stake>=5x, "fillable") acierta PEOR que el azar — verificado
en GBM_LATE_15M_ESPACIO_ATR#XRP#15min: n=302, hit=36.4%, pnl=-0.573€/trade
(vs hit=79.4% en el 78.7% con libro vacío, que domina el shadow agregado
pero nunca sería ejecutable). Simulando con el precio complementario
(1-precio_original), fadear esa misma población daría hit=63.6%,
pnl_medio=+0.232€/trade (n=302, total +70.14€) — pero esa simulación
asume que el lado CONTRARIO también tiene profundidad ejecutable, dato
que hoy NO se mide en ningún sitio (libro_snapshots.csv solo registra el
lado que la estrategia decidió comprar). Ver
idea_gbmlate15m_espacioatr_xrp_arquetipo_a_confirmado_12ago (memoria)
para el análisis completo.

⚠️ TWAP (12-Ago, petición Javi de revisar): el hallazgo de arriba se
recalculó filtrando `prediction_timestamp < 2026-08-07` (TWAP_FECHA_
CAMBIO, `shadow_postmortem.es_pre_twap`, "15min"/"5min" SÍ están en
TWAP_MARCOS_AFECTADOS) tras confirmar que el 88% de la muestra original
(2008/2272) era pre-TWAP. El efecto SOBREVIVE y se refuerza con datos
limpios post-TWAP: fillable n=31 hit=12.9% pnl=-1.402€/trade, fade
simulado n=31 hit=87.1% pnl=+0.675€/trade — n todavía por debajo del
n≥40 estándar del proyecto, de ahí este observador. Este script en sí
NO necesita filtrar TWAP: solo escribe datos DESDE HOY (12-Ago, ya
post-cambio), así que todo lo que acumule será automáticamente post-TWAP
-- el filtro solo hacía falta para el análisis retrospectivo sobre
results.csv/predictions_*.csv histórico. Cualquier análisis FUTURO que
cruce este CSV con results.csv histórico para ampliar el hallazgo
(mezclar con datos previos a hoy) debe seguir aplicando `es_pre_twap()`.

Mecanismo (mismo patrón exacto que favorito_confirmado_senal_contraria_
fase0.py y p22_cola_posicion_fase0.py — reusa `lt._consultar_profundidad_
libro`, solo lectura, nunca ordena):
  1. Vigila data/live/libro_snapshots.csv por filas NUEVAS de cualquier
     estrategia GBM_LATE_15M*/GBM_LATE_5M (familia completa 15min+5min,
     no solo ESPACIO_ATR/XRP — recoger amplio para poder desagregar por
     activo/marco/subfamilia después, CLAUDE.md pt.17; ampliado 12-Ago a
     5min, petición Javi "hazlo para 5 minutos también") con
     motivo=candidato_evaluacion Y ratio_vs_stake>=RATIO_OBJETIVO
     (exactamente la población "fillable" que ya se demostró adversa —
     la inversa de lo que vigila P22/favorito_contraria, que buscan
     libros VACÍOS que mejoran).
  2. Para cada evento nuevo, consulta el libro público del lado
     CONTRARIO (el token que NO recomienda la estrategia) cada
     POLL_INTERVAL_S durante VENTANA_S — no hace falta seguir el lado
     propio (ya sabemos que está fillable, es la condición de entrada).
  3. Persiste en data/shadow/gbmlate_fade_depth_fase0.csv: identidad de
     la señal, ratio/precio del lado original, y la serie temporal de
     ratio/ask del lado contrario. Un análisis posterior cruza con
     outcome_real (results.csv) para responder: cuando el modelo dice
     "compra X" y el libro dice "aquí hay contrapartida real", el lado
     contrario (fadear) ¿tenía TAMBIÉN profundidad ejecutable, o el
     precio barato del contrario esconde el mismo problema de libro
     vacío que el resto del proyecto?

NO coloca, cancela ni modifica ninguna orden real, no llama a ninguna
función de ejecución de live_trade.py, no toca pares_permitidos_live ni
candidatos_evaluacion_live — puramente observacional, mismo criterio de
riesgo que el resto de la familia *_fase0.py.

Se fusiona en observadores_fase0.py (screen "observadores") como los
demás — NUNCA lanzar una screen suelta para este script.
"""
import csv
import json
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
LIBRO_SNAPSHOTS = REPO / "data" / "live" / "libro_snapshots.csv"
OUT = DIR_SHADOW / "gbmlate_fade_depth_fase0.csv"

POLL_INTERVAL_S = 5.0
VENTANA_S = 30.0
RATIO_OBJETIVO = 5.0       # mismo umbral "fillable" que veto_profundidad/analisis_fills.py
CICLO_TAIL_S = 3.0
MAX_HILOS_CONCURRENTES = 8
FAMILIAS_PREFIJO = ("GBM_LATE_15M", "GBM_LATE_5M")  # 15M: base+ESPACIO_ATR+TARDIO+PYCONFIRMADO+MULTIHORIZONTE. 5M: solo base (12-Ago, petición Javi: "hazlo para 5 minutos también")

COLUMNS = [
    "evento_timestamp_utc", "market_id", "strategy", "subtype", "direction",
    "precio_original", "stake_eur", "ratio_original",
    "precio_contrario", "muestras_json",  # [[t_offset_s, ratio_contrario, ask_contrario], ...]
    "ratio_contrario_inicial", "ratio_contrario_max", "ratio_contrario_min",
]


def _es_evento_relevante(fila: dict) -> bool:
    if fila.get("motivo") != "candidato_evaluacion":
        return False
    if not str(fila.get("strategy", "")).startswith(FAMILIAS_PREFIJO):
        return False
    try:
        return float(fila.get("ratio_vs_stake") or 0.0) >= RATIO_OBJETIVO
    except (TypeError, ValueError):
        return False


_lock_out = threading.Lock()
_vistos = set()
_sem = threading.Semaphore(MAX_HILOS_CONCURRENTES)
_libro_pos = 0
_libro_header: list[str] | None = None


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _iniciar_tail_libro() -> None:
    global _libro_pos, _libro_header
    if not LIBRO_SNAPSHOTS.exists():
        return
    with open(LIBRO_SNAPSHOTS, encoding="utf-8") as f:
        primera = f.readline()
        if primera:
            _libro_header = next(csv.reader([primera]))
    _libro_pos = LIBRO_SNAPSHOTS.stat().st_size


def _leer_filas_nuevas() -> list:
    global _libro_pos, _libro_header
    if not LIBRO_SNAPSHOTS.exists() or _libro_header is None:
        return []
    tam = LIBRO_SNAPSHOTS.stat().st_size
    if tam < _libro_pos:
        _libro_pos = 0
        _libro_header = None
        return []
    if tam == _libro_pos:
        return []
    with open(LIBRO_SNAPSHOTS, encoding="utf-8") as f:
        f.seek(_libro_pos)
        nuevas = f.readlines()
        _libro_pos = f.tell()
    if not nuevas:
        return []
    return list(csv.DictReader(nuevas, fieldnames=_libro_header))


def _cargar_vistos_previos() -> set:
    if not OUT.exists():
        return set()
    with open(OUT, encoding="utf-8") as f:
        return {(r["evento_timestamp_utc"], r["market_id"]) for r in csv.DictReader(f)}


def _escribir_fila(fila: dict) -> None:
    with _lock_out:
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)


def _seguir_evento(fila_ev: dict) -> None:
    """Hilo por evento fillable: consulta el libro del lado CONTRARIO
    cada POLL_INTERVAL_S durante VENTANA_S. Solo lectura."""
    try:
        market_id = fila_ev["market_id"]
        strategy = fila_ev["strategy"]
        subtype = fila_ev["subtype"]
        direction = fila_ev["direction"]
        precio_original = float(fila_ev["precio_plan"])
        stake_eur = float(fila_ev["stake_eur"])
        ratio_original = float(fila_ev.get("ratio_vs_stake") or 0.0)

        yes_token, no_token, _cid = lt._get_token_ids(market_id)
        token_contrario = no_token if direction == "BUY_YES" else yes_token
        precio_contrario = round(max(0.01, min(0.99, 1.0 - precio_original)), 6)

        muestras = []
        ratios_contrario = []
        t0 = time.monotonic()

        while time.monotonic() - t0 < VENTANA_S:
            t_offset = round(time.monotonic() - t0, 1)
            try:
                prof_contrario = lt._consultar_profundidad_libro(
                    None, token_contrario, precio_contrario, stake_eur)
            except Exception:
                prof_contrario = {"ok": False}

            ratio_c = prof_contrario.get("ratio_vs_stake") if prof_contrario.get("ok") else None
            ask_c = prof_contrario.get("mejor_ask") if prof_contrario.get("ok") else None
            muestras.append([t_offset, ratio_c, ask_c])
            if ratio_c is not None:
                ratios_contrario.append(ratio_c)

            time.sleep(POLL_INTERVAL_S)

        _escribir_fila({
            "evento_timestamp_utc": fila_ev["timestamp_utc"],
            "market_id": market_id, "strategy": strategy, "subtype": subtype,
            "direction": direction,
            "precio_original": precio_original, "stake_eur": stake_eur,
            "ratio_original": ratio_original,
            "precio_contrario": precio_contrario,
            "muestras_json": json.dumps(muestras, separators=(",", ":")),
            "ratio_contrario_inicial": ratios_contrario[0] if ratios_contrario else "",
            "ratio_contrario_max": max(ratios_contrario) if ratios_contrario else "",
            "ratio_contrario_min": min(ratios_contrario) if ratios_contrario else "",
        })
        rc0 = ratios_contrario[0] if ratios_contrario else None
        _log(f"[{market_id}] {strategy}#{subtype} {direction} ratio_original={ratio_original:.1f} "
             f"-- ratio_contrario_inicial={rc0}")
    except Exception as e:
        _log(f"error siguiendo evento {fila_ev.get('market_id')}: {e}")
    finally:
        _sem.release()


def _marcar_backlog_como_visto() -> set:
    vistos = set()
    if LIBRO_SNAPSHOTS.exists():
        with open(LIBRO_SNAPSHOTS, encoding="utf-8") as f:
            for fila in csv.DictReader(f):
                if _es_evento_relevante(fila):
                    vistos.add((fila["timestamp_utc"], fila["market_id"]))
    return vistos


def main() -> None:
    global _vistos
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    ya_procesados = _cargar_vistos_previos()
    backlog = _marcar_backlog_como_visto()
    _vistos = ya_procesados | backlog
    _iniciar_tail_libro()
    _log(f"arrancado -- {len(ya_procesados)} eventos ya en {OUT.name}, "
         f"{len(backlog)} en el backlog histórico marcados como vistos (no se procesan) -- "
         f"solo se sigue lo que ocurra desde ahora (tail incremental desde byte {_libro_pos})")

    while True:
        try:
            for fila in _leer_filas_nuevas():
                if not _es_evento_relevante(fila):
                    continue
                clave = (fila["timestamp_utc"], fila["market_id"])
                if clave in _vistos:
                    continue
                _vistos.add(clave)
                if _sem.acquire(blocking=False):
                    threading.Thread(target=_seguir_evento, args=(fila,), daemon=True).start()
                else:
                    _log(f"[{fila['market_id']}] descartado -- {MAX_HILOS_CONCURRENTES} hilos ya en curso")
        except Exception as e:
            _log(f"error en ciclo principal: {e}")
        time.sleep(CICLO_TAIL_S)


if __name__ == "__main__":
    main()
