#!/usr/bin/env python3
"""Medicion (solo lectura, WS publico del CLOB) de RAM/CPU/slow-consumer: una conexion por moneda como libro_estado_ws (suscripcion
en trozos de 20 cada 0,25 s, PING de texto cada 10 s). modo 'horizonte' = 5m con inicio <= +2 h; 'todo' = todos los 5m vigentes.
Uso: carga_ws_5m.py <dir_universo_5m> <horizonte|todo> <segundos>"""
import asyncio, json, os, resource, sys, time, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "stage"))
import universo_5m_io as U
import websockets

WS = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
dirp, modo, dur = sys.argv[1], sys.argv[2], float(sys.argv[3])
ahora = time.time()
mk, _ = U.leer(ahora, dirp)
por = collections.defaultdict(list)
for r in sorted(mk.values(), key=lambda r: r["_cierre"]):
    if r["marco"] != "5m" or r["_cierre"] <= ahora:
        continue
    if modo == "horizonte" and r["_cierre"] - 300 > ahora + 7200:
        continue
    por[r["activo"]] += [r["token_up"], r["token_down"]]
st = {"msgs": 0, "bytes": 0, "cierres": [], "libros": 0, "price_change": 0, "por_conn": collections.Counter()}
t_fin = time.time() + dur


async def conn(a, toks):
    try:
        async with websockets.connect(WS, ping_interval=20, ping_timeout=20, open_timeout=10, max_queue=None) as ws:
            cola = list(toks[20:])
            await ws.send(json.dumps({"type": "market", "assets_ids": toks[:20]}))
            t_sub = t_ping = time.time()
            while time.time() < t_fin:
                if cola and time.time() - t_sub >= 0.25:
                    await ws.send(json.dumps({"assets_ids": cola[:20], "operation": "subscribe"}))
                    cola = cola[20:]
                    t_sub = time.time()
                if time.time() - t_ping >= 10:
                    await ws.send("PING")
                    t_ping = time.time()
                try:
                    raw = await asyncio.wait_for(ws.recv(), 0.5)
                except asyncio.TimeoutError:
                    continue
                if raw == "PONG":
                    continue
                st["msgs"] += 1
                st["bytes"] += len(raw)
                st["por_conn"][a] += 1
                st["libros"] += raw.count('"event_type":"book"') + raw.count('"event_type": "book"')
                st["price_change"] += raw.count("price_change")
    except Exception as e:
        st["cierres"].append((a, round(time.time() - (t_fin - dur), 1), type(e).__name__, str(e)[:80]))


async def main():
    t0, c0 = time.time(), resource.getrusage(resource.RUSAGE_SELF)
    await asyncio.gather(*[conn(a, t) for a, t in por.items()])
    c1 = resource.getrusage(resource.RUSAGE_SELF)
    cpu = (c1.ru_utime + c1.ru_stime) - (c0.ru_utime + c0.ru_stime)
    print(json.dumps({"modo": modo, "conexiones": len(por), "tokens_por_moneda": {a: len(t) for a, t in por.items()},
                      "segundos": round(time.time() - t0, 1), "msgs": st["msgs"], "msgs_s": round(st["msgs"] / dur, 1),
                      "KB_s": round(st["bytes"] / 1024 / dur, 1), "libros_iniciales": st["libros"],
                      "cpu_s": round(cpu, 2), "cpu_pct_de_1_core": round(100 * cpu / dur, 2),
                      "maxrss_MB": round(c1.ru_maxrss / 1024, 1), "cierres_inesperados": st["cierres"]}))
asyncio.run(main())
