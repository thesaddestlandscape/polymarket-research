#!/usr/bin/env python3
"""fetch_binance_bookticker.py -- (24-Sep, Javi: "hay que ver la forma de adelantarse aunque sea en
milisegundos en BTC y ETH"). Solo captura, no decide nada.

A3 midió que en BTC/ETH el mercado de Polymarket ya ha incorporado el salto cuando nos llega
Chainlink por RTDS (~1,4 s tras la hora del oráculo): sus market makers van más rápido. La única
forma de adelantarse es ver el precio ANTES de que Chainlink lo publique: Chainlink agrega
precios de bolsas; Binance bookTicker (mejor bid/ask, la señal más rápida que publica) debería
llevarle ventaja. Este fetcher guarda el mid de bookTicker de las 6 monedas, muestreado cada
100 ms (solo si cambió) con la hora de evento de Binance y la de recepción, para medir después:
  (1) lead de Binance sobre Chainlink (hora de oráculo y de recepción RTDS),
  (2) lead de Binance sobre los trades de Polymarket (polymarket_activity) en BTC/ETH.
Salida: /root/polymarket-research-datalogs/binance_bookticker_YYYY-MM-DD.csv (fuera del repo).
Hilo de fetchers_fase0.py (async main).
"""
import asyncio
import csv
import json
import time
from datetime import datetime, timezone
from pathlib import Path

import websockets

DIR = Path("/root/polymarket-research-datalogs")
SIMBOLOS = {"BTCUSDT": "BTC", "ETHUSDT": "ETH", "SOLUSDT": "SOL", "XRPUSDT": "XRP",
            "DOGEUSDT": "DOGE", "BNBUSDT": "BNB"}
WS_URL = "wss://stream.binance.com:9443/stream?streams=" + "/".join(f"{s.lower()}@bookTicker" for s in SIMBOLOS)
MUESTREO_S = 0.1
CAMPOS = ["ts_recepcion_ms", "activo", "bid", "ask", "mid", "bid_qty", "ask_qty", "update_id"]
_ultimo = {}      # activo -> fila más reciente recibida
_escrito = {}     # activo -> mid escrito por última vez


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


async def _escritor():
    while True:
        await asyncio.sleep(MUESTREO_S)
        filas = [f for a, f in list(_ultimo.items()) if _escrito.get(a) != f["mid"]]
        if not filas:
            continue
        p = DIR / f"binance_bookticker_{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.csv"
        nuevo = not p.exists()
        try:
            with open(p, "a", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=CAMPOS)
                if nuevo:
                    w.writeheader()
                for f in filas:
                    w.writerow(f)
                    _escrito[f["activo"]] = f["mid"]
        except OSError as e:
            _log(f"error escribiendo: {e}")


async def main():
    _log(f"fetch_binance_bookticker arrancado ({len(SIMBOLOS)} símbolos, muestreo {MUESTREO_S}s)")
    asyncio.create_task(_escritor())
    while True:
        try:
            async with websockets.connect(WS_URL, ping_interval=20, ping_timeout=20) as ws:
                _log("conectado a Binance bookTicker")
                async for raw in ws:
                    try:
                        d = json.loads(raw).get("data") or {}
                        a = SIMBOLOS.get(d.get("s"))
                        if not a:
                            continue
                        bid, ask = float(d["b"]), float(d["a"])
                        _ultimo[a] = {"ts_recepcion_ms": int(time.time() * 1000), "activo": a, "bid": bid,
                                      "ask": ask, "mid": (bid + ask) / 2, "bid_qty": d.get("B"),
                                      "ask_qty": d.get("A"), "update_id": d.get("u")}
                    except (ValueError, KeyError, TypeError):
                        continue
        except Exception as e:
            _log(f"conexión perdida ({type(e).__name__}: {e}), reconectando en 5 s")
            await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())
