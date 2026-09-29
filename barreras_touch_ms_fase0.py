#!/usr/bin/env python3
"""barreras_touch_ms_fase0.py -- FASE 0 (solo observación) de ronda2 #5 (mercados "qué precio tocará BTC",
barreras) con el principio micro-latencia (29-Sep): el mercado se decide en el instante en que un trade de Binance
imprime >= K (up) / <= K (down) -- la regla dice "any Binance 1 minute candle ... final High >= K": el High de una vela
no puede bajar, así que el desenlace queda fijado en ESE trade aunque la vela cierre hasta 60 s después y el mercado
resuelva "immediately" después. Pregunta: ¿cuánto tarda el libro del YES en irse a ~1 tras ese trade, y cuánto queda
ejecutable (ask < 0,97) a +50/100/250/500/1000/3000/10000 ms?

Diseño (ultra-velocidad):
  - universo: mercados "hit" (↑ K / ↓ K) de BTC/ETH/SOL/XRP con strike a <=1 % del spot y YES aún <0,97, refresco 5 min;
    sus tokens se PRE-suscriben en libro_estado_ws (histórico 100 ms) para tener el libro antes del trigger.
  - detector: WS aggTrade de Binance (BTC/ETH/SOL/XRP), comprobación por trade (microsegundos) del cruce del strike.
  - por evento: timestamp del trade (E), de recepción, estado del libro a -1000..+30000 ms y trades de Polymarket
    posteriores -> data/shadow/barreras_touch_ms_fase0.csv (eventos raros, fichero minúsculo).
NO coloca órdenes. Hilo de observadores_fase0.
"""
import asyncio
import csv
import json
import re
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
import websockets

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import libro_estado_ws as LE  # noqa: E402

GAMMA = "https://gamma-api.polymarket.com"
BINANCE_REST = "https://api.binance.com/api/v3/ticker/price"
WS_URL = "wss://stream.binance.com:9443/stream?streams=" + "/".join(f"{s}usdt@aggTrade" for s in ("btc", "eth", "sol", "xrp"))
OUT = REPO / "data" / "shadow" / "barreras_touch_ms_fase0.csv"
ACTIVOS = {"bitcoin": "BTC", "ethereum": "ETH", "solana": "SOL", "xrp": "XRP"}
CERCA = 0.02
REFRESCO_S = 300
OFFSETS_MS = (-1000, 0, 50, 100, 250, 500, 1000, 2000, 3000, 5000, 10000, 30000)
COLS = ["market_id", "question", "activo", "tipo", "strike", "t_trade_ms", "t_recv_ms", "precio_trigger", "latencia_feed_ms",
        "ms_hasta_fin_vela", "offset_ms", "best_bid", "best_ask", "edad_estado_ms", "n_trades_pm_30s", "precio_trade_pm_medio"]
_MERC, _LOCK, _COLA = {}, threading.Lock(), []     # market_id -> dict; cola de eventos por volcar


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _spots():
    out = {}
    for a in ACTIVOS.values():
        try:
            out[a] = float(requests.get(BINANCE_REST, params={"symbol": f"{a}USDT"}, timeout=5).json()["price"])
        except Exception:
            pass
    return out


def _refrescar():
    """Mercados 'hit' cerca del dinero (gamma events) -> _MERC, y pre-suscripción de sus tokens."""
    spots = _spots()
    nuevos = {}
    for off in range(0, 600, 100):
        try:
            evs = requests.get(f"{GAMMA}/events", params={"active": "true", "closed": "false", "limit": 100, "offset": off,
                                                          "order": "volume24hr", "ascending": "false"}, timeout=20).json()
        except Exception:
            break
        if not isinstance(evs, list) or not evs:
            break
        for e in evs:
            t = e.get("title", "")
            act = next((v for k, v in ACTIVOS.items() if k in t.lower()), None)
            if not act or not re.search(r"\bhit\b", t, re.I) or not spots.get(act):
                continue
            for m in e.get("markets", []):
                g = m.get("groupItemTitle") or ""
                mm = re.search(r"([↑↓])\s*([\d,]+(?:\.\d+)?)", g)
                if not mm:
                    continue
                k = float(mm.group(2).replace(",", ""))
                if abs(k / spots[act] - 1) > CERCA:
                    continue
                up = mm.group(1) == "↑"
                if (up and spots[act] >= k) or ((not up) and spots[act] <= k):
                    continue                      # ya tocado en este instante (o mal lado): no es un trigger futuro
                try:
                    toks = json.loads(m.get("clobTokenIds") or "[]")
                    ask = float(m["bestAsk"]) if m.get("bestAsk") is not None else 1.0
                except Exception:
                    continue
                if len(toks) < 2 or ask >= 0.97:
                    continue
                nuevos[str(m["id"])] = {"mid": str(m["id"]), "q": m.get("question", "")[:100], "act": act,
                                        "up": up, "k": k, "yes": toks[0], "no": toks[1], "disparado": False}
    with _LOCK:
        for mid, v in nuevos.items():
            if mid in _MERC:
                v["disparado"] = _MERC[mid]["disparado"]
            _MERC[mid] = v
        for mid in [m for m in _MERC if m not in nuevos and not _MERC[m]["disparado"]]:
            _MERC.pop(mid)
    for v in nuevos.values():
        LE.pedir([v["yes"]], REFRESCO_S + 120)
    _log(f"universo: {len(nuevos)} mercados hit cerca del dinero, spots {spots}")


async def _feed():
    while True:
        try:
            async with websockets.connect(WS_URL, open_timeout=10, ping_interval=20, ping_timeout=20) as ws:
                _log("Binance aggTrade conectado")
                while True:
                    raw = await asyncio.wait_for(ws.recv(), 30)
                    t_recv = int(time.time() * 1000)
                    d = json.loads(raw).get("data") or {}
                    sym = (d.get("s") or "")[:-4]
                    if sym not in ACTIVOS.values():
                        continue
                    try:
                        p, t_ev = float(d["p"]), int(d["T"])
                    except (KeyError, ValueError):
                        continue
                    with _LOCK:
                        for v in _MERC.values():
                            if v["act"] != sym or v["disparado"]:
                                continue
                            if (v["up"] and p >= v["k"]) or ((not v["up"]) and p <= v["k"]):
                                v["disparado"] = True
                                _COLA.append((time.time() + 32, dict(v), t_ev, t_recv, p))
        except Exception as e:
            _log(f"feed caído: {type(e).__name__}: {e}; reconecta en 3 s")
            await asyncio.sleep(3)


def _volcar(ev, t_ev, t_recv, p):
    filas = []
    tr = LE.trades(ev["yes"], t_ev, t_ev + 30000)
    for off in OFFSETS_MS:
        e = LE.en(ev["yes"], t_ev + off)
        filas.append({"market_id": ev["mid"], "question": ev["q"], "activo": ev["act"], "tipo": "up" if ev["up"] else "down",
                      "strike": ev["k"], "t_trade_ms": t_ev, "t_recv_ms": t_recv, "precio_trigger": p,
                      "latencia_feed_ms": t_recv - t_ev, "ms_hasta_fin_vela": 60000 - (t_ev % 60000), "offset_ms": off,
                      "best_bid": "" if not e or e["best_bid"] is None else e["best_bid"],
                      "best_ask": "" if not e or e["best_ask"] is None else e["best_ask"],
                      "edad_estado_ms": "" if not e else e["edad_ms"], "n_trades_pm_30s": len(tr),
                      "precio_trade_pm_medio": round(sum(x[1] for x in tr) / len(tr), 4) if tr else ""})
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        if nuevo:
            w.writeheader()
        w.writerows(filas)
    _log(f"TOUCH {ev['act']} {'↑' if ev['up'] else '↓'}{ev['k']} trigger {p} (feed {t_recv - t_ev} ms): volcado")


def main():
    _log("arrancado -- detector de cruce de strikes (aggTrade Binance) + libro del YES por WS")
    LE.iniciar(("15min",))
    threading.Thread(target=lambda: asyncio.run(_feed()), daemon=True, name="barreras_feed").start()
    prox = 0.0
    while True:
        try:
            if time.time() >= prox:
                prox = time.time() + REFRESCO_S
                _refrescar()
            while _COLA and _COLA[0][0] <= time.time():
                _, ev, t_ev, t_recv, p = _COLA.pop(0)
                _volcar(ev, t_ev, t_recv, p)
        except Exception as e:
            _log(f"WARN ciclo fallido: {type(e).__name__}: {e}")
        time.sleep(0.5)


if __name__ == "__main__":
    main()
