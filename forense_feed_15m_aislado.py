#!/usr/bin/env python3
"""forense_feed_15m_aislado.py -- MISIÓN 15M V3, FASE 0 (07-Oct): ¿los 423 ms de P90 del feed BTC 15m son de Polymarket o
nuestros? Lector WS AISLADO y mínimo (mismo canal market que libro_estado_ws, mismos tokens BTC 15m vivos y siguientes),
corriendo A LA VEZ que producción. Por cada mensaje guarda solo: recepción (time.time ms, en cuanto llega), timestamp del
exchange, tipo, token, precio/lado/tamaño. Después se empareja con el registro de producción (maker_ms_*: filas q/t con la
misma hora del exchange y token) para medir el retraso que añade NUESTRO pipeline frente al que trae la red/servidor.
Solo lectura. Salida: datalogs/forense_feed/aislado_<ts>.csv.gz.  Uso: python3 forense_feed_15m_aislado.py --seg 900 [--moneda btc]
"""
import argparse
import asyncio
import gzip
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
import websockets

WS = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
OUT = Path("/root/polymarket-research-datalogs/forense_feed")


def tokens(moneda):
    ini = int(time.time() // 900 * 900)
    out = []
    for i0 in (ini, ini + 900):
        r = requests.get("https://gamma-api.polymarket.com/markets", params={"slug": f"{moneda}-updown-15m-{i0}"}, timeout=10).json()
        if r:
            out += json.loads(r[0]["clobTokenIds"])
    return out


async def main(seg, moneda, k):
    OUT.mkdir(parents=True, exist_ok=True)
    f = gzip.open(OUT / f"aislado_{moneda}_k{k}_{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H%M')}_{os.getpid()}.csv.gz", "wt")
    f.write("recv_ms,ts_ex,tipo,token,precio,lado,tam,n_bytes,conn\n")
    fin = time.time() + seg
    # 07-Oct: K conexiones en PARALELO a los mismos tokens (redundancia: ¿cuánto baja la cola con la primera llegada?)
    await asyncio.gather(*(lector(f, fin, moneda, c) for c in range(k)))
    f.close()


async def lector(f, fin, moneda, conn):
    while time.time() < fin:
        toks = tokens(moneda)
        ventana = int(time.time() // 900)
        try:
            async with websockets.connect(WS, ping_interval=None, max_queue=None, open_timeout=10) as ws:
                await ws.send(json.dumps({"type": "market", "assets_ids": toks}))
                t_ping = time.time()
                while time.time() < fin and int(time.time() // 900) == ventana:
                    if time.time() - t_ping >= 10:
                        await ws.send("PING")
                        t_ping = time.time()
                    try:
                        raw = await asyncio.wait_for(ws.recv(), timeout=1.0)
                    except asyncio.TimeoutError:
                        continue
                    rec = time.time() * 1000
                    if not raw or raw[0] not in "[{":
                        continue
                    d = json.loads(raw)
                    for m in (d if isinstance(d, list) else [d]):
                        et, ts = m.get("event_type"), m.get("timestamp")
                        if et == "price_change":
                            for pc in m.get("price_changes", []):
                                f.write(f"{rec:.1f},{ts},pc,{pc.get('asset_id')},{pc.get('price')},{pc.get('side')},{pc.get('size')},{len(raw)},{conn}\n")
                        elif et == "last_trade_price":
                            f.write(f"{rec:.1f},{ts},t,{m.get('asset_id')},{m.get('price')},{m.get('side')},{m.get('size')},{len(raw)},{conn}\n")
                        elif et == "book":
                            f.write(f"{rec:.1f},{ts},book,{m.get('asset_id')},,,,{len(raw)},{conn}\n")
        except Exception as e:
            print(f"reconecto: {type(e).__name__}: {e}", flush=True)
            await asyncio.sleep(1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--seg", type=int, default=900)
    ap.add_argument("--moneda", default="btc")
    ap.add_argument("--conexiones", type=int, default=1)
    a = ap.parse_args()
    asyncio.run(main(a.seg, a.moneda, a.conexiones))
