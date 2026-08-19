#!/usr/bin/env python3
"""
resolution_sniper_naive_executor_dryrun.py — P34 FASE 1, 19-Ago.

Continuación directa de resolution_sniper_naive_depth_fase0.py: el gate
riguroso completo (analisis_gate_riguroso_resolution_sniper_naive_depth_19ago.py,
n=472 con outcome_real resuelto) confirmó que apostar CON la dirección
implícita de Chainlink en offset 0-3s post-cierre, CON profundidad real
verificada (ratio>=5x), da 6/6 combos GATE OK en 5min — BTC/ETH/SOL/XRP/
DOGE/BNB, pnl/tr +0.51€ a +0.96€ (stake 1.05€), wilson90lo muy por encima
del ask_medio, p_shuffle=0.0000-0.0025, split-half consistente. 15min NO
tiene aún muestra suficiente con profundidad confirmada -- excluido aquí.

Mismo hueco que P24 (wallet_mirror) señaló el 03-Ago: medir profundidad
en el INSTANTE DE DETECCIÓN no basta -- hace falta saber cuánto se
degrada la oportunidad entre "la detectamos" y "la hubiéramos podido
ejecutar de verdad" (tras el resto del pipeline de decisión: circuit
breakers, cálculo de stake). Este script añade exactamente ese tramo,
mismo patrón que wallet_mirror_executor_dryrun.py (P24 FASE 1):
  1. Se engancha a resolution_sniper_fade_depth_fase0.py::observar_ventana
     (mismo hilo, mismo reloj, NINGÚN hilo/proceso/screen nuevo -- criterio
     de presupuesto de CPU ya aplicado hoy mismo en esa fusión, py-spy
     encontró 85 hilos vivos en observadores_fase0.py).
  2. Cuando el combo (activo,marco) es uno de los 6 confirmados en 5min Y
     la profundidad en el instante de detección ya es fillable (ratio>=5x)
     Y el ask está en la banda accionable -- espera DECISION_LATENCY_S
     (simula el tiempo real que tardaría live_guard.puede_operar_live +
     live_stake.calcular_stake + circuit breakers antes de poder enviar
     una orden) y vuelve a consultar el libro completo (ambos ask, no solo
     profundidad al ask viejo -- el precio también pudo moverse).
  3. Registra ambas mediciones + el delta en
     data/shadow/resolution_sniper_naive_executor_dryrun.csv.

Seguridad -- por qué esto es DRY_RUN real, no una promesa (mismo criterio
que wallet_mirror_executor_dryrun.py):
  1. `DRY_RUN=True` -- nunca se evalúa el tramo de envío real (que ni
     siquiera existe en este fichero: no importa la función de envío de
     live_trade.py, solo `_consultar_profundidad_libro`, de solo lectura).
  2. Tupla sintética "RESOLUTION_SNIPER_NAIVE#{activo}#5min#BUY_{dir}"
     NUNCA puede estar en `pares_permitidos_live` (no es una estrategia
     que shadow_predict.py/live_trade.py reconozcan) -- verificado
     explícitamente, no asumido.
  3. Promoción real (FASE 2) exigiría: (a) n>=40 en ESTE csv (mide
     degradación con latencia real, distinto del n ya confirmado en el
     gate de detección), (b) /code-review adversarial antes de tocar
     cualquier camino de envío, (c) decisión explícita de Javi para
     añadir la tupla a pares_permitidos_live. Ninguno de los tres ha
     pasado todavía -- ver idea_resolution_sniper_naive_edge_19ago.

NO coloca, cancela ni modifica ninguna orden real.
"""
import csv
import time
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "resolution_sniper_naive_executor_dryrun.csv"

DRY_RUN = True  # guardián #1 -- nunca cambiar sin los 3 pasos del docstring

# Los únicos 6 combos con gate riguroso OK + profundidad real confirmada
# hoy (19-Ago). 15min excluido -- sin muestra suficiente con profundidad.
COMBOS_CONFIRMADOS = {("BTC", "5min"), ("ETH", "5min"), ("SOL", "5min"),
                      ("XRP", "5min"), ("DOGE", "5min"), ("BNB", "5min")}

RATIO_FILLABLE_MIN = 5.0
ASK_MIN, ASK_MAX = 0.05, 0.95
DECISION_LATENCY_S = 0.3  # latencia realista simulada del resto del pipeline

COLUMNS = [
    "timestamp_utc", "activo", "marco", "slug", "market_id", "condition_id",
    "ts_end", "offset_s",
    "direccion_implicita", "ask_deteccion", "ratio_deteccion",
    "ask_decision", "ratio_decision", "delta_ask", "delta_ratio",
    "sigue_fillable_decision",
]


def _log(msg: str):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _guardar(fila: dict):
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(COLUMNS)
        w.writerow([fila.get(c, "") for c in COLUMNS])


def evaluar(asset: str, marco: str, slug: str, market_id: str, condition_id: str,
            ts_end: int, offset: int, direccion_impl: str, ask_impl,
            token_impl: str, ratio_deteccion, libro_fn, token_yes: str, token_no: str):
    """Se llama desde resolution_sniper_fade_depth_fase0.py::observar_ventana
    justo después de medir la profundidad de detección. Solo actúa sobre los
    6 combos confirmados y cuando la detección YA era fillable -- si no lo
    era en detección, no puede mejorar esperando (mismo hallazgo que P22,
    refutado 04-Ago: esperar no rescata señales, degrada)."""
    if (asset, marco) not in COMBOS_CONFIRMADOS:
        return
    if ratio_deteccion is None or ratio_deteccion < RATIO_FILLABLE_MIN:
        return
    if ask_impl is None or not (ASK_MIN <= ask_impl <= ASK_MAX):
        return

    time.sleep(DECISION_LATENCY_S)

    ask_yes2, ask_no2, _, _ = libro_fn(token_yes, token_no)
    ask_decision = ask_yes2 if direccion_impl == "Up" else ask_no2
    depth2 = lt._consultar_profundidad_libro(None, token_impl, ask_decision or ask_impl, 1.05)
    ratio_decision = depth2.get("ratio_vs_stake")

    delta_ask = (ask_decision - ask_impl) if ask_decision is not None else ""
    delta_ratio = (ratio_decision - ratio_deteccion) if ratio_decision is not None else ""
    sigue_fillable = bool(ratio_decision is not None and ratio_decision >= RATIO_FILLABLE_MIN)

    fila = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
        "activo": asset, "marco": marco, "slug": slug,
        "market_id": market_id, "condition_id": condition_id,
        "ts_end": ts_end, "offset_s": offset,
        "direccion_implicita": direccion_impl,
        "ask_deteccion": ask_impl, "ratio_deteccion": ratio_deteccion,
        "ask_decision": ask_decision if ask_decision is not None else "",
        "ratio_decision": ratio_decision if ratio_decision is not None else "",
        "delta_ask": delta_ask, "delta_ratio": delta_ratio,
        "sigue_fillable_decision": sigue_fillable,
    }
    _guardar(fila)
    _log(f"[{asset}#{marco}] ts_end={ts_end} offset={offset} dir={direccion_impl} "
         f"deteccion={ask_impl}(ratio={ratio_deteccion}) "
         f"decision={ask_decision}(ratio={ratio_decision}) "
         f"sigue_fillable={sigue_fillable}")
