#!/usr/bin/env python3
"""
fetch_chainlink_prices.py — Captura continua de precios Chainlink vía el
websocket público de Polymarket (RTDS), solo lectura.

Motivo (20-Jul, investigación de las 13 roturas de garantía en
nested_arb_sim.csv): la fuente de resolución OFICIAL de los mercados
Up/Down de Polymarket es Chainlink (`resolutionSource` en gamma-api, p.ej.
https://data.chain.link/streams/btc-usd), NO Binance/Kraken (que es lo que
usa fetch_binance_klines.py). nested_arb_scanner.py estima o_inner/o_outer
con nuestros propios klines Binance/Kraken -- cuando el gap real entre
ambas aperturas es pequeño, el ruido normal Binance-vs-Chainlink basta
para invertir el orden percibido, hacer que se compre el combo equivocado,
y romper una garantía que en teoría es matemáticamente segura. Las 13
roturas medidas tenían el patrón exacto de este fallo (las 13 con AMBAS
patas perdiendo a la vez, imposible bajo el teorema si o_inner/o_outer son
correctos). Ver memoria idea_nested_arb_garantia_causa_chainlink_20jul.

Petición explícita de Javi (20-Jul): trackear Chainlink SIEMPRE, como
parte del pipeline diario -- no solo para arreglar nested_arb, sino para
tener presente la fuente de resolución oficial en general.

Fuente: Real-Time Data Socket de Polymarket (wss://ws-live-data.polymarket.com),
topic "crypto_prices_chainlink", sin autenticación. Mismo feed que Polymarket
expone también en Binance (crypto_prices_binance) -- este script solo pide
Chainlink porque Binance ya lo cubre fetch_binance_klines.py.

Salida: data/prices/chainlink_YYYY-MM-DD.csv (rota a medianoche UTC),
columnas timestamp_utc,asset,price_usd,ws_timestamp_ms,source -- mismo
espíritu que data/prices/YYYY-MM-DD.csv pero de una fuente distinta, no
se fusiona con ese fichero (evita mezclar/confundir qué precio viene de
dónde; cualquier consumidor que quiera Chainlink específicamente lee este
fichero explícitamente).

Corre en screen propio (igual que pfinish):
  screen -dmS chainlink bash -c "cd /root/polymarket-research && .venv/bin/python fetch_chainlink_prices.py >> logs/chainlink.log 2>&1"
"""

import asyncio
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

import websockets

REPO = Path(__file__).resolve().parent
DIR_PRICES = REPO / "data" / "prices"

WS_URL = "wss://ws-live-data.polymarket.com"
SIMBOLOS = ["btc/usd", "eth/usd", "sol/usd", "xrp/usd"]
PING_INTERVAL_S = 5
RECONNECT_ESPERA_S = 5

_SYMBOL_A_ASSET = {s: s.split("/")[0].upper() for s in SIMBOLOS}


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _archivo_hoy() -> Path:
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return DIR_PRICES / f"chainlink_{fecha}.csv"


def _escribir_tick(writer_state: dict, asset: str, price: float, ws_ts_ms: int) -> None:
    archivo = _archivo_hoy()
    if writer_state.get("path") != archivo:
        # Rotación de día (o primer tick): (re)abre el fichero, cabecera si es nuevo.
        if writer_state.get("f"):
            writer_state["f"].close()
        nuevo = not archivo.exists()
        f = open(archivo, "a", newline="", encoding="utf-8")
        w = csv.writer(f)
        if nuevo:
            w.writerow(["timestamp_utc", "asset", "price_usd", "ws_timestamp_ms", "source"])
        writer_state.update(path=archivo, f=f, w=w)
    ts = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
    writer_state["w"].writerow([ts, asset, price, ws_ts_ms, "chainlink"])
    writer_state["f"].flush()


async def _mantener_ping(ws):
    try:
        while True:
            await asyncio.sleep(PING_INTERVAL_S)
            await ws.send("PING")
    except (asyncio.CancelledError, websockets.exceptions.ConnectionClosed):
        pass


async def _correr_una_conexion(writer_state: dict) -> None:
    async with websockets.connect(WS_URL, open_timeout=10, close_timeout=5) as ws:
        # El campo "filters" documentado no funciona en la práctica (probado
        # 20-Jul: con o sin él, con string u objeto, la suscripción se queda
        # muda) -- se suscribe al topic entero (trae BTC/ETH/SOL/XRP/BNB/DOGE/...)
        # y se filtra por símbolo del lado cliente en el bucle de abajo.
        sub = {
            "action": "subscribe",
            "subscriptions": [
                {"topic": "crypto_prices_chainlink", "type": "update"},
            ],
        }
        await ws.send(json.dumps(sub))
        _log(f"Conectado a {WS_URL}, suscrito a {SIMBOLOS}")
        ping_task = asyncio.create_task(_mantener_ping(ws))
        n_ticks = 0
        try:
            async for raw in ws:
                try:
                    msg = json.loads(raw)
                except (json.JSONDecodeError, TypeError):
                    continue
                if msg.get("topic") != "crypto_prices_chainlink":
                    continue
                payload = msg.get("payload") or {}
                symbol = payload.get("symbol")
                asset = _SYMBOL_A_ASSET.get(symbol)
                if not asset:
                    continue
                try:
                    price = float(payload.get("value"))
                except (TypeError, ValueError):
                    continue
                ws_ts_ms = payload.get("timestamp") or msg.get("timestamp")
                _escribir_tick(writer_state, asset, price, ws_ts_ms)
                n_ticks += 1
                if n_ticks % 500 == 0:
                    _log(f"{n_ticks} ticks recibidos en esta conexión")
        finally:
            ping_task.cancel()


async def main() -> None:
    DIR_PRICES.mkdir(parents=True, exist_ok=True)
    writer_state: dict = {}
    while True:
        try:
            await _correr_una_conexion(writer_state)
        except (websockets.exceptions.ConnectionClosed, OSError, asyncio.TimeoutError) as e:
            _log(f"Conexión perdida ({type(e).__name__}: {e}) — reintentando en {RECONNECT_ESPERA_S}s")
        except Exception as e:
            _log(f"Error inesperado ({type(e).__name__}: {e}) — reintentando en {RECONNECT_ESPERA_S}s")
        await asyncio.sleep(RECONNECT_ESPERA_S)


if __name__ == "__main__":
    asyncio.run(main())
