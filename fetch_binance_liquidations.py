#!/usr/bin/env python3
"""
fetch_binance_liquidations.py — Captura continua del stream público de
liquidaciones de Binance Futures (wss://fstream.binance.com/ws/!forceOrder@arr,
sin autenticación, sin API key). Solo lectura.

Origen (28-Jul, backlog ítem B — idea_moondev_10_hallazgos_priorizados_28jul):
de todas las señales de order-flow que una fuente externa (repo Moon Dev)
midió en su propio dataset, SOLO liquidaciones predijo dirección con
consistencia (58.8% en 187 señales); CVD y MACD dieron 51-52% (coinflip).
Nuestro `ORDER_FLOW_5M` (s_order_flow_5m en shadow_predict.py) usa
taker_buy/sell de klines de Binance -- básicamente el mismo mecanismo que
su CVD ya refutado. Este capturador da la señal DISTINTA (liquidaciones
reales, no volumen de trading normal) para construir estrategias nuevas en
15min/60min (marcos donde HOY no existe ninguna estrategia de order-flow,
ORDER_FLOW_5M solo cubre 5min).

Mantiene en memoria una ventana rodante de liquidaciones recientes (hasta
LOOKBACK_MAX_MIN) por activo, y escribe cada ~10s un JSON agregado con
totales long/short en varias ventanas (2/5/15/60min) -- mismo espíritu que
`totals.json` del servicio de pago de Moon Dev, pero gratis y con nuestros
propios activos. shadow_predict.py (proceso NO persistente, se relanza
cada ciclo) lee este fichero en vez de mantener su propia conexión
websocket.

Salida: data/shadow/liquidaciones_binance_state.json (sobrescrito, no CSV
-- es estado agregado, no histórico fila-a-fila; el histórico crudo se
puede añadir después si hace falta granularidad para análisis retrospectivo).
Puramente shadow/observacional, NO toca dinero ni ninguna decisión todavía
directamente -- alimentará s_liquidaciones_15m/60m (próximo paso).

Corre en screen propio (mismo patrón que chainlink/pfinish):
  screen -dmS liqs bash -c "cd /root/polymarket-research && .venv/bin/python fetch_binance_liquidations.py >> logs/binance_liquidations.log 2>&1"
"""

import json
import time
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

import asyncio
import websockets

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
STATE_PATH = DIR_SHADOW / "liquidaciones_binance_state.json"

WS_URL = "wss://fstream.binance.com/ws/!forceOrder@arr"
RECONNECT_ESPERA_S = 5
ESCRITURA_INTERVALO_S = 10
LOOKBACK_MAX_MIN = 65  # cubre la ventana más larga (60min) con margen

ACTIVOS_TRACKEADOS = {"BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"}
VENTANAS_MIN = [2, 5, 15, 60]


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


# {activo: deque[(epoch_s, lado, usd)]}  lado: "long" (se liquidó un long -> venta forzada) / "short"
_eventos: dict[str, deque] = {a: deque() for a in ACTIVOS_TRACKEADOS}


def _symbol_a_activo(symbol: str) -> str | None:
    for a in ACTIVOS_TRACKEADOS:
        if symbol == f"{a}USDT":
            return a
    return None


def _procesar_evento(msg: dict) -> None:
    o = msg.get("o") or {}
    symbol = o.get("s", "")
    activo = _symbol_a_activo(symbol)
    if not activo:
        return
    # side="SELL" en el evento = se liquidó una posición LARGA (venta forzada
    # empuja el precio hacia abajo); side="BUY" = se liquidó una posición
    # CORTA (compra forzada empuja el precio hacia arriba). Convención
    # documentada de Binance Futures forceOrder.
    side = o.get("S", "")
    lado = "long" if side == "SELL" else ("short" if side == "BUY" else None)
    if lado is None:
        return
    try:
        precio = float(o.get("ap") or o.get("p") or 0)
        cantidad = float(o.get("q") or 0)
    except (TypeError, ValueError):
        return
    usd = precio * cantidad
    if usd <= 0:
        return
    ahora = time.time()
    _eventos[activo].append((ahora, lado, usd))
    _purgar(activo, ahora)


def _purgar(activo: str, ahora: float) -> None:
    limite = ahora - LOOKBACK_MAX_MIN * 60
    dq = _eventos[activo]
    while dq and dq[0][0] < limite:
        dq.popleft()


def _agregar_estado() -> dict:
    ahora = time.time()
    estado = {"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    for activo in sorted(ACTIVOS_TRACKEADOS):
        _purgar(activo, ahora)
        dq = _eventos[activo]
        por_ventana = {}
        for vmin in VENTANAS_MIN:
            limite = ahora - vmin * 60
            usd_long = usd_short = 0.0
            n = 0
            for ts, lado, usd in dq:
                if ts < limite:
                    continue
                n += 1
                if lado == "long":
                    usd_long += usd
                else:
                    usd_short += usd
            total = usd_long + usd_short
            # imbalance > 0 => dominan liquidaciones LONG (venta forzada,
            # sesgo bajista) -- mismo signo que delta_ratio de ORDER_FLOW_5M
            # (negativo=venta) para que ambas features se interpreten igual.
            imbalance = round((usd_short - usd_long) / total, 4) if total > 0 else None
            por_ventana[f"{vmin}min"] = {
                "usd_long": round(usd_long, 2),
                "usd_short": round(usd_short, 2),
                "n": n,
                "imbalance": imbalance,
            }
        estado[activo] = por_ventana
    return estado


def _escribir_estado() -> None:
    estado = _agregar_estado()
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(estado, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(STATE_PATH)


async def _mantener_ping(ws):
    try:
        while True:
            await asyncio.sleep(180)
            await ws.ping()
    except (asyncio.CancelledError, websockets.exceptions.ConnectionClosed):
        pass


async def _escritor_periodico():
    while True:
        await asyncio.sleep(ESCRITURA_INTERVALO_S)
        try:
            _escribir_estado()
        except Exception as e:
            _log(f"Error escribiendo estado: {type(e).__name__}: {e}")


async def _correr_una_conexion() -> None:
    async with websockets.connect(WS_URL, open_timeout=10, close_timeout=5) as ws:
        _log(f"Conectado a {WS_URL}")
        ping_task = asyncio.create_task(_mantener_ping(ws))
        n_total = 0
        try:
            async for raw in ws:
                try:
                    msg = json.loads(raw)
                except (json.JSONDecodeError, TypeError):
                    continue
                if msg.get("e") != "forceOrder":
                    continue
                _procesar_evento(msg)
                n_total += 1
                if n_total % 50 == 0:
                    _log(f"{n_total} liquidaciones vistas en esta conexión")
        finally:
            ping_task.cancel()


async def main() -> None:
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    escritor = asyncio.create_task(_escritor_periodico())
    try:
        while True:
            try:
                await _correr_una_conexion()
            except (websockets.exceptions.ConnectionClosed, OSError, asyncio.TimeoutError) as e:
                _log(f"Conexión perdida ({type(e).__name__}: {e}) — reintentando en {RECONNECT_ESPERA_S}s")
            except Exception as e:
                _log(f"Error inesperado ({type(e).__name__}: {e}) — reintentando en {RECONNECT_ESPERA_S}s")
            await asyncio.sleep(RECONNECT_ESPERA_S)
    finally:
        escritor.cancel()


if __name__ == "__main__":
    asyncio.run(main())
