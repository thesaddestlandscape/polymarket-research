#!/usr/bin/env python3
"""leadlag_venues_llegada.py -- MISIÓN DEFINITIVA 15m §5/§20 (07-Oct): ¿qué fuente de precio de BTC llega ANTES a
NUESTRA máquina (Helsinki)? Para el maker que cancela importa la primera llegada de la información, no dónde nace.
Captura N segundos de operaciones de BTC por WS en 7 mercados a la vez (solo lectura, público):
  binance (spot aggTrade, Tokio), binancef (futuros aggTrade), coinbase (matches), kraken (trade v2), bybit (spot
  publicTrade), okx (trades), bitstamp (live_trades).
Guarda (venue, t_fuente_ms, t_recepcion_ms, precio, cantidad) en datalogs/leadlag_venues_<ts>.csv.gz y analiza:
  1. recepción − hora de la fuente por venue (P50/P90/P99): latencia de cable + interna.
  2. LEAD-LAG con NUESTRO reloj: eventos de Binance spot (|ret| >= 2 bps en 500 ms) -> cuántos ms antes/después cruza
     cada venue el mismo umbral en la misma dirección (mediana, % que llega antes que Binance).
  3. Correlación cruzada de retornos en rejilla de 25 ms (recepción) frente a Binance: lag de máxima correlación.
Uso: (ulimit -v 2000000; python3 leadlag_venues_llegada.py --seg 1200)
"""
import argparse
import asyncio
import collections
import gzip
import json
import time
from datetime import datetime, timezone

import numpy as np

OUT_DIR = "/root/polymarket-research-datalogs"
FILAS = []


def iso_ms(s):
    return int(datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp() * 1000)


async def venue(nombre, url, sub, parse):
    import websockets
    while True:
        try:
            async with websockets.connect(url, ping_interval=20, max_queue=None, open_timeout=10) as ws:
                if sub:
                    await ws.send(json.dumps(sub))
                async for raw in ws:
                    rec = time.time() * 1000
                    try:
                        for t_src, p, q in parse(json.loads(raw)):
                            FILAS.append((nombre, t_src, rec, p, q))
                    except Exception:
                        pass
        except Exception as e:
            print(f"{nombre}: {type(e).__name__} {e}; reconecto", flush=True)
            await asyncio.sleep(2)


def p_binance(d):
    if "p" in d:
        yield d["T"], float(d["p"]), float(d["q"])


def p_coinbase(d):
    if d.get("type") in ("match", "last_match"):
        yield iso_ms(d["time"]), float(d["price"]), float(d["size"])


def p_kraken(d):
    if d.get("channel") == "trade":
        for x in d.get("data", []):
            yield iso_ms(x["timestamp"]), float(x["price"]), float(x["qty"])


def p_bybit(d):
    for x in d.get("data", []) if d.get("topic", "").startswith("publicTrade") else []:
        yield int(x["T"]), float(x["p"]), float(x["v"])


def p_okx(d):
    for x in d.get("data", []) if d.get("arg", {}).get("channel") == "trades" else []:
        yield int(x["ts"]), float(x["px"]), float(x["sz"])


def p_bitstamp(d):
    if d.get("event") == "trade":
        x = d["data"]
        yield int(x["microtimestamp"]) / 1000, float(x["price"]), float(x["amount"])


VENUES = [
    ("binance", "wss://stream.binance.com:9443/ws/btcusdt@aggTrade", None, p_binance),
    ("binancef", "wss://fstream.binance.com/ws/btcusdt@aggTrade", None, p_binance),
    ("coinbase", "wss://ws-feed.exchange.coinbase.com", {"type": "subscribe", "product_ids": ["BTC-USD"], "channels": ["matches"]}, p_coinbase),
    ("kraken", "wss://ws.kraken.com/v2", {"method": "subscribe", "params": {"channel": "trade", "symbol": ["BTC/USD"]}}, p_kraken),
    ("bybit", "wss://stream.bybit.com/v5/public/spot", {"op": "subscribe", "args": ["publicTrade.BTCUSDT"]}, p_bybit),
    ("okx", "wss://ws.okx.com:8443/ws/v5/public", {"op": "subscribe", "args": [{"channel": "trades", "instId": "BTC-USDT"}]}, p_okx),
    ("bitstamp", "wss://ws.bitstamp.net", {"event": "bts:subscribe", "data": {"channel": "live_trades_btcusd"}}, p_bitstamp),
]


async def capturar(seg):
    tareas = [asyncio.create_task(venue(*v)) for v in VENUES]
    await asyncio.sleep(seg)
    for t in tareas:
        t.cancel()


def pct(v):
    v = np.asarray(v, float)
    if len(v) == 0:
        return "n=0"
    p = np.percentile(v, [50, 90, 99])
    return f"n={len(v):7} P50 {p[0]:7.1f} P90 {p[1]:7.1f} P99 {p[2]:7.1f}"


def analizar(filas):
    por = collections.defaultdict(list)
    for v, ts, rec, p, q in filas:
        por[v].append((rec, ts, p))
    print("\n1. recepción − hora de la fuente (ms; incluye el desfase de reloj de cada venue):")
    for v in sorted(por):
        a = np.array(por[v])
        print(f"   {v:9} {pct(a[:, 0] - a[:, 1])}")
    # serie por recepción en rejilla de 25 ms (último precio)
    t0 = min(min(x[0] for x in por[v]) for v in por)
    t1 = max(max(x[0] for x in por[v]) for v in por)
    grid = np.arange(t0, t1, 25.0)
    serie = {}
    for v in por:
        a = np.array(sorted(por[v]))
        idx = np.searchsorted(a[:, 0], grid, side="right") - 1
        s = np.where(idx >= 0, a[np.clip(idx, 0, None), 2], np.nan)
        serie[v] = s
    print("\n2. Eventos de Binance spot (|ret 500 ms| >= 2 bps, con nuestro reloj): ms hasta que cada venue cruza el mismo "
          "umbral en la misma dirección (negativo = llegó ANTES que Binance)")
    b = serie["binance"]
    k = 20                                         # 500 ms
    ret = (b[k:] / b[:-k] - 1) * 1e4
    ev = np.flatnonzero(np.abs(ret) >= 2) + k
    sel, ult = [], -10 ** 9
    for i in ev:                                   # 1 evento por 2 s
        if i - ult >= 80:
            sel.append(i)
            ult = i
    print(f"   eventos: {len(sel)}")
    for v in sorted(serie):
        if v == "binance":
            continue
        s = serie[v]
        lags = []
        for i in sel:
            sg = np.sign(b[i] - b[i - k])
            base = s[i - k] if i - k >= 0 else np.nan
            if not base == base:
                continue
            lo, hi = max(0, i - 2 * k - 40), min(len(s), i + 120)     # buscar de -1,5 s a +3 s
            hit = None
            for j in range(lo, hi):
                ref = s[j - k] if j - k >= 0 else np.nan
                if ref == ref and s[j] == s[j] and sg * (s[j] / ref - 1) * 1e4 >= 2:
                    hit = j
                    break
            if hit is not None:
                lags.append((hit - i) * 25)
        lags = np.array(lags)
        if len(lags):
            print(f"   {v:9} n={len(lags):4}/{len(sel)} mediana {np.median(lags):+7.0f} ms | P25 {np.percentile(lags, 25):+6.0f} "
                  f"P75 {np.percentile(lags, 75):+6.0f} | llega ANTES que Binance {np.mean(lags < 0) * 100:4.0f} %")
    print("\n3. Correlación cruzada de retornos de 100 ms (rejilla 25 ms) frente a Binance: lag de máxima correlación "
          "(positivo = el venue va DETRÁS)")
    rb = np.diff(np.log(b[::4]))
    for v in sorted(serie):
        if v == "binance":
            continue
        rv = np.diff(np.log(serie[v][::4]))
        m = ~np.isnan(rb) & ~np.isnan(rv)
        best = None
        for lag in range(-10, 11):                  # ±1 s en pasos de 100 ms
            x = rb[max(0, -lag):len(rb) - max(0, lag)]
            y = rv[max(0, lag):len(rv) - max(0, -lag)]
            mm = ~np.isnan(x) & ~np.isnan(y)
            if mm.sum() > 100 and x[mm].std() > 0 and y[mm].std() > 0:
                c = np.corrcoef(x[mm], y[mm])[0, 1]
                if best is None or c > best[1]:
                    best = (lag * 100, c)
        print(f"   {v:9} lag {best[0]:+5d} ms  corr {best[1]:.3f}" if best else f"   {v:9} sin datos")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seg", type=int, default=1200)
    a = ap.parse_args()
    print(f"captura {a.seg} s desde {datetime.now(timezone.utc).isoformat(timespec='seconds')}", flush=True)
    try:
        asyncio.run(capturar(a.seg))
    except Exception:
        pass
    ruta = f"{OUT_DIR}/leadlag_venues_{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H%M')}.csv.gz"
    with gzip.open(ruta, "wt") as f:
        f.write("venue,t_fuente_ms,t_recepcion_ms,precio,cantidad\n")
        for r in FILAS:
            f.write(",".join(map(str, r)) + "\n")
    print(f"filas {len(FILAS)} -> {ruta}")
    analizar(FILAS)


if __name__ == "__main__":
    main()
