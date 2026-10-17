#!/usr/bin/env python3
"""multivenue_ms_fase0.py -- 17-Oct (Javi: "tiene que haber una forma de que esa señal no llegue tarde"). Solo captura.

H26-MS (DECISION_LOG 17-Oct 11:20Z): el movimiento de Binance que precede a los rellenos maker adversos llega
50-100 ms antes de que recibamos el relleno: tarde para cancelar. Medido el mismo día desde este VPS (Helsinki;
el VPS cerca del CLOB está descartado): Binance spot y perp nos llegan con ~140 ms de retraso sobre su propio sello
(servidores en Tokio), Kraken ~27 ms, Bitstamp ~31 ms, Coinbase ~63 ms, Bybit ~96 ms. Si estas bolsas se mueven a la
vez que Binance, ven el mismo movimiento ~80-115 ms ANTES desde aquí. Este grabador guarda, con hora de RECEPCIÓN en
ms, el mejor bid/ask (Q) y las operaciones (T) de las 6 monedas, para medir quién nos avisa antes y repetir H26-MS
con la fuente más temprana. (Antecedente: leadlag_venues_llegada.py, capturas cortas del 07-Oct, solo trades BTC.)

UN PROCESO POR BOLSA (el supervisor lanza `--bolsa X` y lo relanza si muere): cada uno sella la recepción en su
propio bucle, sin que la ráfaga de una bolsa retrase el sello de otra; escritor en hilo aparte (texto + gzip).
Salida: /mnt/HC_Volume_106538179/multivenue_ms/multivenue_ms_YYYY-MM-DD_<proceso>_<pid>[_e<n>].csv.gz (proceso = bolsa; binance_perp_t = trades del perp)
Filas (8 columnas): bolsa,tipo,simbolo,sello_ms,recepcion_ms,c1,c2,c3
   Q = mejor bid/ask: c1=bid, c2=ask             T = operación: c1=precio, c2=tamaño, c3=lado según la bolsa
   G = hueco de la bolsa: c1=motivo (conexion/caida/pausa/fin)
 Notas de fuente: sello_ms vacío en Q de binance_spot (su bookTicker no lleva hora) y en Q de kraken (ticker sin
 hora); vale la hora de RECEPCIÓN. Coinbase: su canal ticker solo emite con operaciones (Q de coinbase = bid/ask en
 cada operación, no en cada recotización) y c3 es su campo `side` (según su documentación, el lado del tomador; sin
 verificar). Bybit: libro de nivel 1 mantenido con snapshot+deltas. Bitstamp: order_book solo de BTC y ETH (100
 niveles por mensaje); del resto, solo operaciones.
Espacio: presupuesto PRESUPUESTO_GB para toda la familia (se borran los más antiguos; se protegen solo el fichero
abierto y las últimas 24 h); pausa (cierra la conexión) con el volumen < MIN_LIBRE_GB o con el INTERRUPTOR.
Fallo del escritor 8 veces seguidas o error grave -> el proceso de la bolsa sale y el supervisor lo relanza.
SIGTERM: cierra el gzip bien antes de salir.
"""
import argparse
import asyncio
import gzip
import json
import os
import queue
import signal
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

VOL = "/mnt/HC_Volume_106538179"
DIR = Path(VOL) / "multivenue_ms"
INTERRUPTOR = Path("/root/polymarket-research-datalogs/MULTIVENUE_OFF")
PRESUPUESTO_GB = 15.0
MIN_LIBRE_GB = 10.0
MAXQ = 50000
MON6 = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]


def _log(msg, bolsa="supervisor"):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] [{bolsa}] {msg}", flush=True)


def _ms():
    return int(time.time() * 1000)


def _iso_ms(s):
    return int(datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp() * 1000)


# ---------------- parsers: (msg, recepción) -> filas ----------------
def _p_binance(bolsa):
    def p(m, r):
        d = m.get("data") or {}
        s = (d.get("s") or "").replace("USDT", "")
        if d.get("e") == "aggTrade":
            return [(bolsa, "T", s, d["T"], r, d["p"], d["q"], "SELL" if d.get("m") else "BUY")]
        if "b" in d and "a" in d and "u" in d:
            return [(bolsa, "Q", s, d.get("T") or d.get("E") or "", r, d["b"], d["a"], "")]
        return []
    return p


def _p_coinbase(m, r):
    if m.get("type") != "ticker":
        return []
    s = (m.get("product_id") or "").replace("-USD", "")
    t = _iso_ms(m["time"]) if m.get("time") else ""
    filas = [("coinbase", "Q", s, t, r, m["best_bid"], m["best_ask"], "")]
    if m.get("price") and m.get("last_size"):
        filas.append(("coinbase", "T", s, t, r, m["price"], m["last_size"], (m.get("side") or "").upper()))
    return filas


def _p_kraken(m, r):
    if m.get("channel") == "ticker" and m.get("data"):
        return [("kraken", "Q", x["symbol"].replace("/USD", ""), "", r, x["bid"], x["ask"], "") for x in m["data"]]
    if m.get("channel") == "trade" and m.get("data"):
        return [("kraken", "T", x["symbol"].replace("/USD", ""), _iso_ms(x["timestamp"]), r, x["price"], x["qty"],
                 (x.get("side") or "").upper()) for x in m["data"]]
    return []


def _p_bitstamp(m, r):
    ch, d = m.get("channel") or "", m.get("data") or {}
    if m.get("event") == "data" and ch.startswith("order_book_") and d.get("bids") and d.get("asks"):
        s = ch.replace("order_book_", "").replace("usd", "").upper()
        return [("bitstamp", "Q", s, int(d["microtimestamp"]) // 1000, r, d["bids"][0][0], d["asks"][0][0], "")]
    if m.get("event") == "trade" and ch.startswith("live_trades_"):
        s = ch.replace("live_trades_", "").replace("usd", "").upper()
        return [("bitstamp", "T", s, int(d["microtimestamp"]) // 1000, r, d["price"], d["amount"],
                 "BUY" if d.get("type") == 0 else "SELL")]
    return []


_BYBIT_TOP = {}   # símbolo -> {"b": precio|None, "a": precio|None} (libro de nivel 1: snapshot + deltas)


def _p_bybit(m, r):
    top, d = m.get("topic") or "", m.get("data")
    if top.startswith("orderbook.1.") and isinstance(d, dict):
        s = d["s"].replace("USDT", "")
        est = _BYBIT_TOP.setdefault(s, {"b": None, "a": None})
        if m.get("type") == "snapshot":
            est["b"] = est["a"] = None
        for lado in ("b", "a"):
            for precio, tam in d.get(lado) or []:
                if float(tam) == 0:
                    if est[lado] == precio:
                        est[lado] = None
                else:
                    est[lado] = precio
        if est["b"] and est["a"]:
            return [("bybit", "Q", s, m.get("ts"), r, est["b"], est["a"], "")]
        return []
    if top.startswith("publicTrade.") and isinstance(d, list):
        return [("bybit", "T", x["s"].replace("USDT", ""), x["T"], r, x["p"], x["v"], (x.get("S") or "").upper())
                for x in d]
    return []


_BN = "/".join([f"{c.lower()}usdt@bookTicker/{c.lower()}usdt@aggTrade" for c in MON6])
_SIN_BNB = [c for c in MON6 if c != "BNB"]
BOLSAS = {
    "binance_spot": ("wss://stream.binance.com:9443/stream?streams=" + _BN, [], _p_binance("binance_spot")),
    # futuros: el bookTicker sigue en la raíz, pero los aggTrade se movieron a /market/ (medido 17-Oct: 0 por la raíz)
    "binance_perp": ("wss://fstream.binance.com/stream?streams=" + "/".join(f"{c.lower()}usdt@bookTicker" for c in MON6),
                     [], _p_binance("binance_perp")),
    "binance_perp_t": ("wss://fstream.binance.com/market/stream?streams=" + "/".join(f"{c.lower()}usdt@aggTrade" for c in MON6),
                       [], _p_binance("binance_perp")),
    "coinbase": ("wss://ws-feed.exchange.coinbase.com",
                 [{"type": "subscribe", "channels": [{"name": "ticker", "product_ids": [f"{c}-USD" for c in _SIN_BNB]}]}],
                 _p_coinbase),
    "kraken": ("wss://ws.kraken.com/v2",
               [{"method": "subscribe", "params": {"channel": "ticker", "event_trigger": "bbo",
                                                   "symbol": [f"{c}/USD" for c in _SIN_BNB]}},
                {"method": "subscribe", "params": {"channel": "trade", "symbol": [f"{c}/USD" for c in _SIN_BNB]}}],
               _p_kraken),
    "bitstamp": ("wss://ws.bitstamp.net",
                 [{"event": "bts:subscribe", "data": {"channel": f"order_book_{c.lower()}usd"}} for c in ("BTC", "ETH")]
                 + [{"event": "bts:subscribe", "data": {"channel": f"live_trades_{c.lower()}usd"}} for c in _SIN_BNB],
                 _p_bitstamp),
    "bybit": ("wss://stream.bybit.com/v5/public/spot",
              [{"op": "subscribe", "args": [f"orderbook.1.{c}USDT" for c in MON6]},     # máx. 10 temas por mensaje
               {"op": "subscribe", "args": [f"publicTrade.{c}USDT" for c in MON6]}],
              _p_bybit),
}


# ---------------- proceso de UNA bolsa ----------------
class _Grabador:
    def __init__(self, bolsa):
        self.bolsa = bolsa
        self.q = queue.Queue(maxsize=MAXQ)
        self.activo = True
        self.descartes = 0
        self.errores_parser = 0
        self.fin = threading.Event()
        self.cerrado = threading.Event()
        threading.Thread(target=self._escritor, daemon=True, name="escritor").start()

    def put(self, filas):
        if not self.activo or not filas:
            return
        try:
            self.q.put_nowait(filas)
        except queue.Full:
            self.descartes += len(filas)

    def _libre(self):
        st = os.statvfs(DIR)
        return st.f_bavail * st.f_frsize / 1e9

    def _presupuesto(self, actual):
        fs = []
        for p in DIR.glob("multivenue_ms_*.csv.gz"):
            try:
                st = p.stat()
            except OSError:
                continue
            fs.append((st.st_mtime, st.st_size, p))
        total = sum(x[1] for x in fs) / 1e9
        reciente = time.time() - 86400                  # se protegen solo el abierto y las últimas 24 h
        for mt, tam, p in sorted(fs):
            if total <= PRESUPUESTO_GB:
                break
            if p.name == actual or mt >= reciente:
                continue
            try:
                p.unlink()
                _log(f"presupuesto {PRESUPUESTO_GB} GB superado: borrado {p.name}", self.bolsa)
            except FileNotFoundError:
                pass                                      # ya no está: cuenta igual
            except OSError:
                continue
            total -= tam / 1e9

    def _abrir(self, dia, n):
        while True:
            suf = f"{self.bolsa}_{os.getpid()}" + (f"_e{n}" if n else "")
            ruta = DIR / f"multivenue_ms_{dia}_{suf}.csv.gz"
            try:
                f = gzip.open(ruta, "xt", encoding="utf-8", compresslevel=3)
                f.write("bolsa,tipo,simbolo,sello_ms,recepcion_ms,c1,c2,c3\n")
                return f, n, ruta.name
            except FileExistsError:
                n += 1

    def _escritor(self):
        f, dia, n, nombre, fallos = None, None, 0, None, 0
        t_flush = t_chk = t_pres = 0.0
        aplica_presupuesto = self.bolsa == next(iter(BOLSAS))   # una sola bolsa recorta el directorio común

        def linea(x):
            return ",".join("" if v is None else str(v) for v in x) + "\n"

        while True:
            try:
                if self.fin.is_set():
                    if f is not None:
                        limite = time.time() + 2.0
                        try:
                            while time.time() < limite:
                                f.write("".join(linea(x) for x in self.q.get_nowait()))
                        except queue.Empty:
                            pass
                        f.write(linea((self.bolsa, "G", "*", "", _ms(), _ms(), "fin", "")))
                        f.close()
                    self.cerrado.set()
                    return
                if time.time() - t_chk > 10:
                    t_chk = time.time()
                    try:                                  # errores de espacio/listado NO son fallos de escritura
                        if aplica_presupuesto and time.time() - t_pres > 60:
                            t_pres = time.time()
                            self._presupuesto(nombre)
                        pausa = INTERRUPTOR.exists() or self._libre() < MIN_LIBRE_GB
                    except OSError as e:
                        _log(f"comprobación de espacio: {type(e).__name__}: {e}", self.bolsa)
                        pausa = not self.activo
                    if pausa == self.activo:
                        self.activo = not pausa
                        _log(f"grabación {'REANUDADA' if self.activo else 'EN PAUSA (interruptor o volumen bajo)'}",
                             self.bolsa)
                    if self.descartes or self.errores_parser:
                        _log(f"últimos 10 s: {self.descartes} filas descartadas (cola llena), "
                             f"{self.errores_parser} mensajes ilegibles", self.bolsa)
                        self.descartes = self.errores_parser = 0
                try:
                    filas = self.q.get(timeout=1.0)
                except queue.Empty:
                    filas = None
                if not self.activo:
                    if f is not None:
                        f.write(linea((self.bolsa, "G", "*", "", _ms(), _ms(), "pausa", "")))
                        f.close()
                        f = None
                    continue
                if filas is not None:
                    hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
                    if f is None or hoy != dia:
                        if f is not None:
                            f.close()
                        f, n, nombre = self._abrir(hoy, 0 if hoy != dia else n)
                        dia = hoy
                    f.write("".join(linea(x) for x in filas))
                if f is not None and time.time() - t_flush > 5:
                    f.flush()
                    t_flush = time.time()
                    fallos = 0
            except Exception as e:
                fallos += 1
                _log(f"escritor: {type(e).__name__}: {e} (fallo {fallos}/8)", self.bolsa)
                try:
                    if f is not None:
                        f.close()
                except Exception:
                    pass
                f, n = None, n + 1
                if fallos >= 8:
                    _log("escritor muerto tras 8 fallos: el proceso sale y el supervisor lo relanza", self.bolsa)
                    os._exit(3)
                self.fin.wait(min(60, 5 * 2 ** (fallos - 1)))   # SIGTERM/SIGHUP lo despierta

    async def _vigilar(self, ws):
        """Ping de aplicación de Bybit y cierre de la conexión al entrar en pausa (fuera del bucle de lectura)."""
        t_ping = time.time()
        while True:
            await asyncio.sleep(1)
            if not self.activo:
                await ws.close()
                return
            if self.bolsa == "bybit" and time.time() - t_ping > 20:
                await ws.send(json.dumps({"op": "ping"}))
                t_ping = time.time()

    async def correr(self, url, subs, parser):
        import websockets
        espera = 2
        while True:
            if not self.activo:                          # en pausa no se mantiene la conexión (ni su CPU)
                await asyncio.sleep(5)
                continue
            try:
                async with websockets.connect(url, open_timeout=10, ping_interval=20, ping_timeout=20,
                                              max_queue=4096, max_size=2 ** 23) as ws:
                    for s in subs:
                        await ws.send(json.dumps(s))
                    self.put([(self.bolsa, "G", "*", "", _ms(), _ms(), "conexion", "")])
                    _log("conectado", self.bolsa)
                    vigia = asyncio.create_task(self._vigilar(ws))
                    try:
                        async for raw in ws:
                            r = _ms()                     # sello de recepción, lo primero
                            try:
                                filas = parser(json.loads(raw), r)
                            except Exception:
                                self.errores_parser += 1
                                continue
                            self.put(filas)
                            espera = 2
                    finally:
                        vigia.cancel()
            except Exception as e:
                self.put([(self.bolsa, "G", "*", "", _ms(), _ms(), "caida", "")])
                _log(f"caída {type(e).__name__}: {str(e)[:120]}; reconecta en {espera} s", self.bolsa)
                await asyncio.sleep(espera)
                espera = min(60, espera * 2)


def _hijo(bolsa):
    if not os.path.ismount(VOL):
        _log(f"{VOL} no está montado: no se graba en el disco raíz", bolsa)
        sys.exit(1)
    DIR.mkdir(parents=True, exist_ok=True)
    g = _Grabador(bolsa)

    def al_terminar(signum, frame):
        g.fin.set()
        g.cerrado.wait(5)
        os._exit(0)
    for sg in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):   # screen -X quit manda SIGHUP
        signal.signal(sg, al_terminar)
    url, subs, parser = BOLSAS[bolsa]
    asyncio.run(g.correr(url, subs, parser))


# ---------------- supervisor ----------------
def _supervisor():
    if not os.path.ismount(VOL):
        _log(f"{VOL} no está montado: no se graba en el disco raíz")
        sys.exit(1)
    hijos, espera, proximo = {}, {b: 2 for b in BOLSAS}, {b: 0.0 for b in BOLSAS}
    terminar = threading.Event()

    def al_terminar(signum, frame):
        terminar.set()
    for sg in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
        signal.signal(sg, al_terminar)
    _log(f"multivenue_ms_fase0 arrancado: un proceso por bolsa ({', '.join(BOLSAS)}) -> {DIR}")
    while not terminar.is_set():
        for b in BOLSAS:
            p = hijos.get(b)
            if p is not None and p.poll() is not None:
                _log(f"{b} salió (rc={p.returncode}); se relanza en {espera[b]} s")
                proximo[b] = time.time() + espera[b]
                espera[b] = min(300, espera[b] * 2)
                hijos[b] = p = None
            if p is None and time.time() >= proximo[b]:
                hijos[b] = subprocess.Popen([sys.executable, os.path.abspath(__file__), "--bolsa", b])
                hijos[b].t0 = time.time()
            elif p is not None and time.time() - getattr(p, "t0", 0) > 600:
                espera[b] = 2                             # lleva 10 min vivo: se olvida el backoff
        terminar.wait(5)
    vivos = [p for p in hijos.values() if p is not None]
    for p in vivos:
        if p.poll() is None:
            p.terminate()
    for p in vivos:
        try:
            p.wait(8)
        except subprocess.TimeoutExpired:
            p.kill()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--bolsa", choices=list(BOLSAS))
    a = ap.parse_args()
    if a.bolsa:
        _hijo(a.bolsa)
    else:
        _supervisor()
