#!/usr/bin/env python3
"""
fetch_polymarket_activity_ws.py — Captura continua del firehose de trades
reales de Polymarket vía RTDS (wss://ws-live-data.polymarket.com), topic
"activity" type "trades". Solo lectura.

Origen (28-Jul): al revisar el repo moondevonyt/Hyperliquid-Data-Layer-API
(que cobra por una "Polymarket Whales API" describiéndola como "persistent
WebSocket a wss://ws-live-data.polymarket.com, cada trade ≥$1000"), Javi
pidió NO suscribirse a ningún servicio de pago sino intentar replicarlo
gratis. Confirmado con sondeo manual (probe_rtds*.py, scratchpad de la
sesión): el topic real es "activity"/"trades" (no documentado en
docs.polymarket.com/market-data/websocket/rtds, que solo lista precios y
comentarios) — sin autenticación, mismo endpoint que ya usa
fetch_chainlink_prices.py para precios Chainlink. Payload real por trade:
proxyWallet, pseudonym, side, size, price, outcome, conditionId,
eventSlug, slug, title, timestamp, transactionHash — exactamente lo que
Moon Dev cobra por dar.

NO reemplaza `ballenas_observer.py` (cron horario, ballenas_timing_
history.csv) todavía -- eso sería un cambio de pipeline core que merece
su propia sesión dedicada de revisión/comparación, no un swap silencioso.
Esto es una captura NUEVA e independiente, puramente aditiva: fichero
propio, para comparar más adelante fidelidad/latencia contra el método
de polling actual antes de proponer ningún reemplazo.

Filtra dos categorías (ambas se guardan, columna `categoria`):
  - "updown_tracked": trades en nuestros mercados Up/Down de
    BTC/ETH/SOL/XRP/DOGE/BNB (5m/15m/1h) -- el universo que ya operamos.
  - "whale": cualquier trade (de cualquier mercado) con usd_value >=
    WHALE_USD_MIN (1000, mismo suelo que usa el servicio de pago).
  Un trade puede cumplir ambas a la vez (columnas booleanas separadas).

Salida: data/shadow/polymarket_activity_YYYY-MM-DD.csv (rota a
medianoche UTC). Puramente shadow/observacional, NO toca dinero ni
ninguna decisión todavía.

Corre en screen propio (mismo patrón que chainlink/pfinish):
  screen -dmS polyactivity bash -c "cd /root/polymarket-research && .venv/bin/python fetch_polymarket_activity_ws.py >> logs/polymarket_activity.log 2>&1"
"""

import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import asyncio
import websockets

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"

WS_URL = "wss://ws-live-data.polymarket.com"
PING_INTERVAL_S = 5
RECONNECT_ESPERA_S = 5
WHALE_USD_MIN = 1000.0

ACTIVOS_TRACKEADOS = {"BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"}
_RE_UPDOWN_SLUG = re.compile(r"^([a-z]+)-updown-(\d+)(m|h)-\d+$")

COLUMNS = [
    "timestamp_utc", "ws_timestamp", "condition_id", "event_slug", "market_slug",
    "title", "activo", "marco", "categoria_updown_tracked", "categoria_whale",
    "wallet", "pseudonym", "outcome", "side", "price", "size", "usd_value",
    "transaction_hash",
]


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _archivo_hoy() -> Path:
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return DIR_SHADOW / f"polymarket_activity_{fecha}.csv"


def _parse_updown(event_slug: str):
    """('BTC','5min') a partir de 'btc-updown-5m-1785237000', o (None,None)."""
    m = _RE_UPDOWN_SLUG.match(event_slug or "")
    if not m:
        return None, None
    activo = m.group(1).upper()
    if activo not in ACTIVOS_TRACKEADOS:
        return None, None
    n, unidad = m.group(2), m.group(3)
    marco = f"{n}min" if unidad == "m" else f"{int(n)*60}min"
    return activo, marco


def _escribir_fila(fila: dict) -> None:
    archivo = _archivo_hoy()
    with open(archivo, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        if f.tell() == 0:
            w.writeheader()
        w.writerow(fila)


async def _mantener_ping(ws):
    try:
        while True:
            await asyncio.sleep(PING_INTERVAL_S)
            await ws.send("PING")
    except (asyncio.CancelledError, websockets.exceptions.ConnectionClosed):
        pass


async def _correr_una_conexion() -> None:
    async with websockets.connect(WS_URL, open_timeout=10, close_timeout=5) as ws:
        sub = {
            "action": "subscribe",
            "subscriptions": [{"topic": "activity", "type": "trades"}],
        }
        await ws.send(json.dumps(sub))
        _log(f"Conectado a {WS_URL}, suscrito a activity/trades")
        ping_task = asyncio.create_task(_mantener_ping(ws))
        n_total = n_guardados = 0
        try:
            async for raw in ws:
                if not raw:
                    continue
                try:
                    msg = json.loads(raw)
                except (json.JSONDecodeError, TypeError):
                    continue
                payload = msg.get("payload")
                if not isinstance(payload, dict) or "proxyWallet" not in payload:
                    continue
                n_total += 1
                try:
                    price = float(payload.get("price", 0) or 0)
                    size = float(payload.get("size", 0) or 0)
                except (TypeError, ValueError):
                    continue
                usd_value = round(price * size, 4)
                event_slug = payload.get("eventSlug", "")
                activo, marco = _parse_updown(event_slug)
                es_tracked = activo is not None
                es_whale = usd_value >= WHALE_USD_MIN
                if not es_tracked and not es_whale:
                    continue  # fail-cheap: no guardar el ruido de trades pequeños fuera de nuestro universo
                fila = {
                    "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
                    "ws_timestamp": payload.get("timestamp"),
                    "condition_id": payload.get("conditionId", ""),
                    "event_slug": event_slug,
                    "market_slug": payload.get("slug", ""),
                    "title": payload.get("title", ""),
                    "activo": activo or "",
                    "marco": marco or "",
                    "categoria_updown_tracked": int(es_tracked),
                    "categoria_whale": int(es_whale),
                    "wallet": payload.get("proxyWallet", ""),
                    "pseudonym": payload.get("pseudonym", ""),
                    "outcome": payload.get("outcome", ""),
                    "side": payload.get("side", ""),
                    "price": price,
                    "size": size,
                    "usd_value": usd_value,
                    "transaction_hash": payload.get("transactionHash", ""),
                }
                _escribir_fila(fila)
                n_guardados += 1
                if n_total % 1000 == 0:
                    _log(f"{n_total} trades vistos, {n_guardados} guardados (tracked o whale) en esta conexión")
        finally:
            ping_task.cancel()


async def main() -> None:
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    while True:
        try:
            await _correr_una_conexion()
        except (websockets.exceptions.ConnectionClosed, OSError, asyncio.TimeoutError) as e:
            _log(f"Conexión perdida ({type(e).__name__}: {e}) — reintentando en {RECONNECT_ESPERA_S}s")
        except Exception as e:
            _log(f"Error inesperado ({type(e).__name__}: {e}) — reintentando en {RECONNECT_ESPERA_S}s")
        await asyncio.sleep(RECONNECT_ESPERA_S)


if __name__ == "__main__":
    asyncio.run(main())
