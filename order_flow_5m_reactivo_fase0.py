#!/usr/bin/env python3
"""
order_flow_5m_reactivo_fase0.py -- FASE 0, observador de baja latencia
dedicado para ORDER_FLOW_5M#{ETH,XRP,DOGE,BNB,SOL}#BUY_NO (27-Ago noche,
petición explícita Javi: "a qué tenemos que conectar esta estrategia para
sacarle todo el jugo").

Por qué hace falta: ORDER_FLOW_5M solo genera predicciones dentro del
ciclo principal de shadow_predict.py (~100-130s), y su fill-ability real
hoy solo se mide vía el poll genérico de candidatos_evaluacion_live
(~20s, motivo candidato_evaluacion en libro_snapshots.csv) -- barrido de
esta misma noche dio n=18-36 señales fillable por moneda tras 6+ semanas
acumulando (n_total 39-126). Un observador dedicado, con poll cada ~15s
SOBRE KLINES (no requiere esperar al ciclo lento de predict), puede
generar mucho más n útil por semana.

Diseño (mismo patrón P24/Candidata9/10/GBM_LATE_reactivo -- segunda
consulta de libro 3s después de la detección, registra predicción formal
SOLO si sigue fillable): en vez de reimplementar la lógica de umbral
delta_ratio/DELTA_MIN/DELTA_MAX/blacklist horario (riesgo real de drift
si se duplica a mano), este script llama DIRECTAMENTE a
`shadow_predict.s_order_flow_5m(market, ctx)` con klines frescos
(fetch_binance_klines.fetch_binance, mismo formato) y el `question` REAL
del mercado actual (gamma-api, vía mercado_slot -- nunca reconstruido a
mano, evita cualquier desajuste de parseo con _parse_updown_tipo). Fuente
única de verdad: si algún día cambia el umbral en shadow_predict.py, este
observador lo hereda automáticamente sin tocar nada aquí.

NO coloca, cancela ni modifica ninguna orden real. STRATEGY sintética
("ORDER_FLOW_5M_REACTIVO"), nunca puede estar en pares_permitidos_live
directamente -- se promociona como el resto (gate_bucket_propio +
checklist + decisión de Javi).

Se fusiona en observadores_fase0.py (screen "observadores") -- NUNCA
lanzar una screen suelta para este script.
"""
import csv
import fcntl
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from fetch_binance_klines import fetch_binance  # noqa: E402
from resolution_sniper_observer import mercado_slot, token_ids  # noqa: E402
from gbm_late_reactivo_fase0 import _libro_unico  # noqa: E402 -- reusa la misma
# consulta de libro de una sola llamada, mismo shape que _consultar_profundidad_libro
from shadow_predict import (  # noqa: E402
    s_order_flow_5m, ORDER_FLOW_BLACKLIST_HOURS, ORDER_FLOW_PAIR_BLACKLIST,
)

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "order_flow_5m_reactivo_fase0.csv"
OUT_LOCK = DIR_SHADOW / "order_flow_5m_reactivo_fase0.csv.lock"
PREDICTIONS_LOCK_PATH = DIR_SHADOW / ".predictions_lock"

STRATEGY = "ORDER_FLOW_5M_REACTIVO"  # sintética, nunca en pares_permitidos_live directamente
ACTIVOS = ["ETH", "SOL", "XRP", "DOGE", "BNB"]  # BTC ya en ORDER_FLOW_PAIR_BLACKLIST
DUR_S = 300  # 5min
SEGUNDA_CONSULTA_ESPERA_S = 3.0
POLL_S = 3  # 27-Ago noche (petición Javi: "¿no es mejor milisegundos para
# reaccionar a una posición volátil?"): medido en vivo -- la vela EN
# FORMACIÓN de Binance ya se actualiza en tiempo casi real vía REST
# (delta_ratio de ETH cambió 0.322->0.343->0.327 en solo 13s de poll a
# 3s). No hace falta reescribir a websocket (como gbm_late_reactivo_
# fase0.py) para tener ese frescor -- ahí SÍ compensaba porque el trigger
# es un evento de un solo tick (cruce de precio); aquí el trigger es un
# agregado de 5min que evoluciona de forma continua, no una ráfaga
# puntual. Sondear cada 3s en vez de 15s ya captura ese frescor con una
# fracción del coste de ingeniería. 5 activos * 1 llamada/3s ~= 100
# llamadas/min a klines REST, muy por debajo del límite de Binance.
RATIO_MIN = 5.0
STAKE_REF_EUR = 1.05

COLUMNS = [
    "timestamp_utc", "activo", "market_id", "condition_id", "delta_ratio",
    "py_deteccion", "ratio_deteccion", "ask_deteccion",
    "ratio_decision", "ask_decision", "degradacion_ask_pct",
    "sigue_fillable_en_decision", "registrada_prediccion",
]


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _guardar(fila: dict) -> None:
    lock_f = open(OUT_LOCK, "w")
    fcntl.flock(lock_f, fcntl.LOCK_EX)
    try:
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)
    finally:
        fcntl.flock(lock_f, fcntl.LOCK_UN)


def _registrar_prediccion(condition_id: str, activo: str, py: float) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    archivo = DIR_SHADOW / f"predictions_{ts[:10]}.csv"
    subtype = f"{activo}#5min"
    decision = "BUY_NO"
    prob_yes = max(0.03, py - 0.03)
    edge = prob_yes - py
    features = json.dumps({
        "py_entrada": round(py, 4), "ejecutor_baja_latencia": True,
        "fase0_solo_observacion": True, "order_flow_5m_reactivo": True,
    }, separators=(",", ":"))
    try:
        with open(PREDICTIONS_LOCK_PATH, "w") as lock_f:
            fcntl.flock(lock_f, fcntl.LOCK_EX)
            try:
                nuevo = not archivo.exists()
                with open(archivo, "a", newline="", encoding="utf-8") as f:
                    w = csv.writer(f)
                    if nuevo:
                        w.writerow([
                            "timestamp_utc", "strategy", "market_id", "question", "end_date",
                            "horas_a_vencimiento", "precio_yes_mercado", "prob_yes_modelo",
                            "edge_bruto", "edge_neto", "edge_direccional", "decision", "razon",
                            "subtype", "apuesta", "features",
                        ])
                    w.writerow([
                        ts, STRATEGY, condition_id, "", "",
                        "0.02", f"{py:.4f}", f"{prob_yes:.4f}",
                        f"{edge:.4f}", f"{edge:.4f}", f"{edge:.4f}", decision,
                        "order_flow_5m_reactivo", subtype, str(STAKE_REF_EUR), features,
                    ])
            finally:
                fcntl.flock(lock_f, fcntl.LOCK_UN)
    except Exception as e:
        _log(f"aviso: no se pudo registrar predicción: {e}")


def _procesar_activo(activo: str, vistos: set) -> None:
    hora_utc = datetime.now(timezone.utc).hour
    if hora_utc in ORDER_FLOW_BLACKLIST_HOURS or activo in ORDER_FLOW_PAIR_BLACKLIST:
        return

    ahora = time.time()
    ts_end = (int(ahora) // DUR_S + 1) * DUR_S
    ts_start = ts_end - DUR_S

    dedup_key = f"{activo}|{ts_start}"
    if dedup_key in vistos:
        return

    klines = fetch_binance(activo, with_flow=True)
    if not klines or len(klines) < 5:
        return

    slug, mkt = mercado_slot(activo, "5m", ts_start)
    if not mkt:
        return
    token_yes, token_no = token_ids(mkt)
    if not token_yes or not token_no:
        return

    # precio actual (proxy real-time, mkt cacheado puede estar rancio) --
    # mid del libro YES, una sola consulta.
    fill_yes, _, _ = _libro_unico(token_yes, 0.5, STAKE_REF_EUR)
    if not fill_yes.get("ok") or fill_yes.get("mejor_ask") is None:
        return
    py = fill_yes["mejor_ask"]

    horas_restantes = (ts_end - ahora) / 3600.0
    market = {
        "question": mkt.get("question", ""), "_precio_yes": py, "_horas": horas_restantes,
        "condition_id": mkt.get("conditionId") or mkt.get("condition_id", ""),
        "spread": mkt.get("spread"), "liquidity": mkt.get("liquidity"),
    }
    ctx = {"klines_raw": {activo: klines}}

    resultado = s_order_flow_5m(market, ctx)
    if resultado is None:
        return

    vistos.add(dedup_key)
    condition_id = mkt.get("conditionId") or mkt.get("condition_id", "")
    market_id = mkt.get("id", "")
    delta_ratio = resultado["features"].get("delta_ratio")

    # detección: consulta libro lado NO (BUY_NO es la única dirección de ORDER_FLOW_5M)
    fill_det, _, _ = _libro_unico(token_no, 1 - py, STAKE_REF_EUR)
    ask_det = fill_det.get("mejor_ask")
    ratio_det = fill_det.get("ratio_vs_stake") if fill_det.get("ok") else None

    time.sleep(SEGUNDA_CONSULTA_ESPERA_S)

    fill_dec, _, _ = _libro_unico(token_no, 1 - py, STAKE_REF_EUR)
    ask_dec = fill_dec.get("mejor_ask")
    ratio_dec = fill_dec.get("ratio_vs_stake") if fill_dec.get("ok") else None

    degradacion = None
    if ask_det is not None and ask_dec is not None and ask_det > 0:
        degradacion = round((ask_dec - ask_det) / ask_det * 100, 2)

    sigue_fillable = bool(ratio_dec is not None and ratio_dec >= RATIO_MIN)
    py_ref = (1 - ask_dec) if ask_dec is not None else py

    registrada = False
    if sigue_fillable:
        _registrar_prediccion(condition_id, activo, py_ref)
        registrada = True

    _log(f"[{activo}] TRIGGER delta={delta_ratio} py={py:.3f} ask_det={ask_det} "
         f"ratio_det={ratio_det} -> ask_dec={ask_dec} ratio_dec={ratio_dec} "
         f"degradacion={degradacion}% registrada={registrada}")

    _guardar({
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "activo": activo, "market_id": market_id, "condition_id": condition_id,
        "delta_ratio": delta_ratio, "py_deteccion": py,
        "ratio_deteccion": ratio_det, "ask_deteccion": ask_det,
        "ratio_decision": ratio_dec, "ask_decision": ask_dec,
        "degradacion_ask_pct": degradacion,
        "sigue_fillable_en_decision": int(sigue_fillable), "registrada_prediccion": int(registrada),
    })


def main() -> None:
    vistos = set()
    _log(f"arrancado -- vigilando ORDER_FLOW_5M reactivo en {ACTIVOS}")
    while True:
        try:
            # limpiar vistos de slots ya cerrados (evita crecer sin límite)
            ahora = time.time()
            ts_end_actual = (int(ahora) // DUR_S + 1) * DUR_S
            ts_start_actual = ts_end_actual - DUR_S
            vistos = {v for v in vistos if v.endswith(f"|{ts_start_actual}")}

            for activo in ACTIVOS:
                try:
                    _procesar_activo(activo, vistos)
                except Exception as e:
                    _log(f"error procesando {activo}: {type(e).__name__}: {e}")
        except Exception as e:
            _log(f"error en ciclo: {e}")
        time.sleep(POLL_S)


if __name__ == "__main__":
    main()
