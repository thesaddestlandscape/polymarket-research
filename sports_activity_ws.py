#!/usr/bin/env python3
"""
sports_activity_ws.py — Captura continua en tiempo real de TODOS los
trades de mercados sports/esports vía RTDS (mismo endpoint público que
fetch_polymarket_activity_ws.py, pero conexión propia e independiente).

Origen (18-Ago, mismo patrón ya aplicado en weather el mismo día): el
firehose compartido de cripto (fetch_polymarket_activity_ws.py,
data/*/polymarket_activity_*.csv) SOLO guarda trades tracked-cripto o
whale-tier (usd_value>=1000) -- la inmensa mayoría de la actividad
sports/esports (trades pequeños) nunca llega a ese fichero, y por eso
sports_wallet_edge_tracker.py (18-Ago, primera pasada) solo pudo
descubrir wallets a partir de 86.545 trades whale-tier, perdiéndose
cualquier especialista de tamaño moderado. Además ese fichero no guarda
`outcomeIndex` (solo el texto `outcome`, ambiguo en mercados head-to-head
como UFC/esports donde el outcome es el NOMBRE del contendiente, no
Yes/No) -- este captura el outcomeIndex crudo del payload, sin esa
ambigüedad.

Reutiliza clasificar() de sports_wallet_edge_tracker.py (mismo import
directo, cero duplicación de las 24 categorías + auto-descubrimiento de
ligas de fútbol por slug).

Salida: data/sports/activity_ws_YYYY-MM-DD.csv (rota a medianoche UTC).
Puramente de captura -- no decide ni ejecuta nada.

Corre en screen propia:
  screen -dmS sports-ws bash -c "cd /root/polymarket-research && .venv/bin/python sports_activity_ws.py >> logs/sports_activity_ws.log 2>&1"
"""
import asyncio
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import websockets

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from sports_wallet_edge_tracker import clasificar  # noqa: E402

DIR_SPORTS = REPO / "data" / "sports"
DIR_SPORTS.mkdir(parents=True, exist_ok=True)

WS_URL = "wss://ws-live-data.polymarket.com"
PING_INTERVAL_S = 5
RECONNECT_ESPERA_S = 5
RECV_TIMEOUT_S = 30  # mismo fix ya conocido (chainlink/polyactivity/weather) -- sin esto, una
# conexión muerta en silencio bloquea el bucle para siempre.

COLUMNS = [
    "timestamp_utc", "ws_timestamp", "condition_id", "event_slug", "market_slug",
    "title", "categoria", "wallet", "pseudonym", "outcome", "outcome_index",
    "side", "price", "size", "usd_value", "transaction_hash",
]


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _archivo_hoy() -> Path:
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return DIR_SPORTS / f"activity_ws_{fecha}.csv"


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
        sub = {"action": "subscribe", "subscriptions": [{"topic": "activity", "type": "trades"}]}
        await ws.send(json.dumps(sub))
        _log(f"Conectado a {WS_URL}, suscrito a activity/trades")
        ping_task = asyncio.create_task(_mantener_ping(ws))
        n_total = n_guardados = 0
        try:
            while True:
                raw = await asyncio.wait_for(ws.recv(), timeout=RECV_TIMEOUT_S)
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
                title = payload.get("title", "")
                categoria = clasificar(title, payload.get("eventSlug", ""))
                if categoria is None:
                    continue  # fuera de nuestro universo (cripto/weather/politica/etc.)
                try:
                    price = float(payload.get("price", 0) or 0)
                    size = float(payload.get("size", 0) or 0)
                except (TypeError, ValueError):
                    continue
                try:
                    outcome_index = int(payload.get("outcomeIndex"))
                except (TypeError, ValueError):
                    outcome_index = ""
                fila = {
                    "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
                    "ws_timestamp": payload.get("timestamp"),
                    "condition_id": payload.get("conditionId", ""),
                    "event_slug": payload.get("eventSlug", ""),
                    "market_slug": payload.get("slug", ""),
                    "title": title, "categoria": categoria,
                    "wallet": payload.get("proxyWallet", ""),
                    "pseudonym": payload.get("pseudonym", ""),
                    "outcome": payload.get("outcome", ""), "outcome_index": outcome_index,
                    "side": payload.get("side", ""), "price": price, "size": size,
                    "usd_value": round(price * size, 4),
                    "transaction_hash": payload.get("transactionHash", ""),
                }
                _escribir_fila(fila)
                n_guardados += 1
                if n_total % 5000 == 0:
                    _log(f"{n_total} trades vistos (todos los mercados), "
                         f"{n_guardados} de sports/esports guardados en esta conexión")
        finally:
            ping_task.cancel()


async def main() -> None:
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
