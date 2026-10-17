# Lector WS mínimo del CLOB (mercado), sin procesar nada: sello de recepción y volcado de last_trade_price.
import asyncio, json, sys, time, websockets
toks = open(sys.argv[1]).read().split()
out = open(sys.argv[2], "w")
async def main():
    async with websockets.connect("wss://ws-subscriptions-clob.polymarket.com/ws/market", ping_interval=20,
                                  max_queue=None, open_timeout=10) as ws:
        await ws.send(json.dumps({"type": "market", "assets_ids": toks}))
        t0, t_ping = time.time(), time.time()
        while time.time() - t0 < float(sys.argv[3]):
            if time.time() - t_ping > 9:
                await ws.send("PING"); t_ping = time.time()
            try:
                raw = await asyncio.wait_for(ws.recv(), 2)
            except asyncio.TimeoutError:
                continue
            r = int(time.time() * 1000)
            if raw == "PONG": continue
            for e in (json.loads(raw) if raw[:1] == "[" else [json.loads(raw)]):
                if isinstance(e, dict) and e.get("event_type") == "last_trade_price":
                    out.write(f"{e.get('asset_id')},{e.get('timestamp')},{e.get('price')},{e.get('size')},{r}\n")
asyncio.run(main())
out.close()
