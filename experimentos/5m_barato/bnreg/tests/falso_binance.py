"""Servidor WS falso de Binance (dev). Hilo propio con su bucle. aggTrade con `a` contiguo por simbolo (continua entre conexiones, como Binance) y bookTicker sin `e`."""
import asyncio
import json
import threading
import time

from websockets.asyncio.server import serve

SIMB = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "DOGEUSDT", "BNBUSDT"]


class FalsoBinance:
    def __init__(self, periodo=0.01):
        self.periodo = periodo
        self.ids = {s: 100 for s in SIMB}
        self.conexiones = 0
        self.vivas = set()
        self.silencio = False
        self.basura = False        # True: intercala mensajes no JSON / sin `data` dict / listas
        self.saltar_ids = 0        # >0: el proximo aggTrade de BTC salta ese numero de ids (para probar `faltantes`)
        self.enviados = []         # (T, sym, p, q, m) de cada aggTrade enviado
        self.loop = None
        self.srv = None
        self.port = None
        self._lis = threading.Event()

    async def _handler(self, ws):
        self.conexiones += 1
        self.vivas.add(ws)
        i = 0
        try:
            while True:
                await asyncio.sleep(self.periodo)
                if self.silencio:
                    continue
                s = SIMB[i % 6]
                i += 1
                if self.basura and i % 5 == 0:
                    await ws.send(["esto no es json", '{"data": 5}', '[1, 2]', '{"stream": "x"}', 'null'][(i // 5) % 5])
                ahora = int(time.time() * 1000)
                if i % 2:
                    if self.saltar_ids and s == "BTCUSDT":
                        self.ids[s] += self.saltar_ids
                        self.saltar_ids = 0
                    self.ids[s] += 1
                    p, q, m = f"{100 + (i % 7) * 0.01:.2f}", f"{0.001 * (1 + i % 5):.3f}", bool(i % 3 == 0)
                    self.enviados.append((ahora - 2, s, p, q, int(m)))
                    msg = {"stream": s.lower() + "@aggTrade", "data": {"e": "aggTrade", "E": ahora - 1, "s": s, "a": self.ids[s], "p": p, "q": q, "f": 1, "l": 1, "T": ahora - 2, "m": m}}
                else:
                    msg = {"stream": s.lower() + "@bookTicker", "data": {"u": i, "s": s, "b": f"{99.9 + (i % 5) * 0.01:.2f}", "B": "1.5", "a": f"{100.1 + (i % 5) * 0.01:.2f}", "A": "2.5"}}
                await ws.send(json.dumps(msg))
        except Exception:
            pass
        finally:
            self.vivas.discard(ws)

    def _run(self, port):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        async def main():
            self.srv = await serve(self._handler, "127.0.0.1", port)
            self.port = self.srv.sockets[0].getsockname()[1]
            self._lis.set()
            await self.srv.wait_closed()
        try:
            self.loop.run_until_complete(main())
        except Exception:
            pass

    def start(self, port=0):
        self._lis.clear()
        threading.Thread(target=self._run, args=(port,), daemon=True).start()
        assert self._lis.wait(5), "servidor falso no arranca"
        return f"ws://127.0.0.1:{self.port}/stream"

    def drop(self):
        """Cierra todas las conexiones vivas (el servidor sigue aceptando)."""
        async def _d():
            for ws in list(self.vivas):
                await ws.close()
        asyncio.run_coroutine_threadsafe(_d(), self.loop).result(5)

    def stop(self):
        async def _s():
            self.srv.close()
            for ws in list(self.vivas):
                await ws.close()
        asyncio.run_coroutine_threadsafe(_s(), self.loop).result(5)
