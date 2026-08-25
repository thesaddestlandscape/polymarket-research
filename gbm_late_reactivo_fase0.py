#!/usr/bin/env python3
"""gbm_late_reactivo_fase0.py -- FASE 0 (solo medición, NUNCA orden real),
25-Ago. Mide si Arquetipo A (GBM_LATE) tiene una ventana de profundidad
real capturable en los primeros cientos de milisegundos tras el tick de
Binance que cruza el umbral de edge, algo que el sondeo actual a 2s
(`gbm_late_15min_executor.py::POLL_INTERVAL_S=2.0`) no puede ver.

Contexto (ver idea_arquetipo_a_palancas_probadas_25ago en memoria): FAK/
orden parcial ya descartado (99.9% de vetos con profundidad LITERALMENTE
CERO en 4 familias -- no hay nada que un fill parcial pudiera rescatar).
El websocket de FUTUROS de Binance (fstream.binance.com, usado para
liquidaciones) está bloqueado para esta VPS -- pero el de SPOT
(stream.binance.com:9443, el precio que usa GBM_LATE) está CONFIRMADO
funcionando sin bloqueo (307 msj/10s, verificado 30-Jul). Este script
construye el consumidor de ese websocket spot que nunca se había hecho.

Diseño (experimento de medición, no réplica exacta del modelo GBM):
para cada mercado GBM_LATE#15min activo (6 monedas), toma como
referencia el primer tick de precio visto tras el inicio de la ventana
de 15min (mismo rol que `ref` en shadow_predict.py::_s_gbm_late). En
cada tick nuevo, si el movimiento acumulado desde esa referencia supera
GBM_LATE_DRIFT_VENT_MIN_PCT (0.03%, mismo umbral real que usa el modelo)
y no se ha disparado ya para ese mercado, consulta INMEDIATAMENTE el
libro real de Polymarket (mismo `_consultar_profundidad_libro` que usan
los ejecutores live) y registra la latencia tick->consulta y la
profundidad encontrada.

NO calcula d_gbm/sigma_h/p_up completos -- el objetivo es solo medir
profundidad en el INSTANTE del cruce, comparable contra el baseline ya
conocido (99.9% profundidad=0 con sondeo a 2s).

NO coloca, cancela ni modifica ninguna orden real. Se fusiona en
observadores_fase0.py (screen "observadores") si funciona bien standalone.
"""
import asyncio
import csv
import fcntl
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import websockets

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import live_trade as lt  # noqa: E402
from resolution_sniper_observer import mercado_slot, token_ids  # noqa: E402

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "gbm_late_reactivo_fase0.csv"
OUT_LOCK = DIR_SHADOW / "gbm_late_reactivo_fase0.csv.lock"

ASSETS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
SYMBOLS = {"BTC": "btcusdt", "ETH": "ethusdt", "SOL": "solusdt",
           "XRP": "xrpusdt", "DOGE": "dogeusdt", "BNB": "bnbusdt"}
MARCO_TAG = "15m"
DUR_S = 900
DRIFT_MIN_PCT = 0.03  # mismo umbral que GBM_LATE_DRIFT_VENT_MIN_PCT en shadow_predict.py
STAKE_REF_EUR = 1.05

WS_URL = "wss://stream.binance.com:9443/stream?streams=" + "/".join(
    f"{s}@aggTrade" for s in SYMBOLS.values())

COLUMNS = [
    "timestamp_utc", "activo", "market_id", "condition_id", "ts_end",
    "ts_tick_binance_ms", "ts_consulta_libro_ms", "latencia_ms",
    "precio_ref", "precio_tick", "drift_pct",
    "mejor_ask", "profundidad_eur", "ratio_vs_stake", "n_niveles",
]

_SYM_A_ACTIVO = {v: k for k, v in SYMBOLS.items()}


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _guardar(fila: dict) -> None:
    lock_f = open(OUT_LOCK, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if nuevo:
                w.writerow(COLUMNS)
            w.writerow([fila.get(c, "") for c in COLUMNS])
    finally:
        fcntl.flock(lock_f, fcntl.LOCK_UN)
        lock_f.close()


class _EstadoActivo:
    __slots__ = ("ts_end", "mkt", "ref", "disparado")

    def __init__(self):
        self.ts_end = None
        self.mkt = None
        self.ref = None
        self.disparado = False


async def _procesar_tick(activo: str, precio: float, ts_tick_ms: int, estado: dict) -> None:
    now = time.time()
    ts_end = (int(now) // DUR_S + 1) * DUR_S
    ts_start = ts_end - DUR_S

    e = estado.setdefault(activo, _EstadoActivo())
    if e.ts_end != ts_end:
        # nueva ventana -- resolver mercado (barato, cacheado por
        # mercado_slot) y resetear referencia/disparo
        slug, mkt = mercado_slot(activo, MARCO_TAG, ts_start)
        e.ts_end = ts_end
        e.mkt = mkt
        e.ref = precio
        e.disparado = False
        return

    if e.ref is None or e.ref <= 0:
        e.ref = precio
        return
    if e.disparado or not e.mkt:
        return

    drift_pct = (precio / e.ref - 1) * 100
    if abs(drift_pct) < DRIFT_MIN_PCT:
        return

    e.disparado = True  # dedup: solo el primer cruce por ventana
    token_yes, token_no = token_ids(e.mkt)
    if not token_yes:
        return
    token_id = token_yes if drift_pct > 0 else token_no
    ts_consulta_ms = int(time.time() * 1000)

    try:
        fill = lt._consultar_profundidad_libro(None, token_id, 0.5, STAKE_REF_EUR)
    except Exception as ex:
        _log(f"[{activo}] error consultando libro: {type(ex).__name__}: {ex}")
        return

    fila = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
        "activo": activo, "market_id": e.mkt.get("id", ""),
        "condition_id": e.mkt.get("conditionId", ""), "ts_end": ts_end,
        "ts_tick_binance_ms": ts_tick_ms, "ts_consulta_libro_ms": ts_consulta_ms,
        "latencia_ms": ts_consulta_ms - ts_tick_ms,
        "precio_ref": e.ref, "precio_tick": precio, "drift_pct": round(drift_pct, 4),
        "mejor_ask": fill.get("mejor_ask") if fill.get("ok") else "",
        "profundidad_eur": fill.get("profundidad_eur") if fill.get("ok") else "",
        "ratio_vs_stake": fill.get("ratio_vs_stake") if fill.get("ok") else "",
        "n_niveles": fill.get("n_niveles") if fill.get("ok") else "",
    }
    _guardar(fila)
    _log(f"[{activo}] TRIGGER drift={drift_pct:+.3f}% latencia={fila['latencia_ms']}ms "
         f"profundidad={fila['profundidad_eur']} ask={fila['mejor_ask']}")


async def _consumir_websocket() -> None:
    estado: dict = {}
    while True:
        try:
            async with websockets.connect(WS_URL, ping_interval=20, ping_timeout=20) as ws:
                _log(f"conectado a {WS_URL[:60]}...")
                async for raw in ws:
                    try:
                        msg = json.loads(raw)
                        data = msg.get("data", {})
                        sym = data.get("s", "").lower()
                        activo = _SYM_A_ACTIVO.get(sym)
                        if not activo:
                            continue
                        precio = float(data.get("p", 0))
                        ts_tick_ms = int(data.get("T", time.time() * 1000))
                        if precio <= 0:
                            continue
                        await _procesar_tick(activo, precio, ts_tick_ms, estado)
                    except Exception as ex:
                        _log(f"error procesando mensaje: {type(ex).__name__}: {ex}")
        except Exception as ex:
            _log(f"conexión perdida ({type(ex).__name__}: {ex}) — reconectando en 5s")
            await asyncio.sleep(5)


def main() -> None:
    _log(f"gbm_late_reactivo_fase0 arrancado -- activos={ASSETS} marco=15min "
         f"umbral_drift={DRIFT_MIN_PCT}%")
    asyncio.run(_consumir_websocket())


if __name__ == "__main__":
    main()
