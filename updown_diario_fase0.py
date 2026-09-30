#!/usr/bin/env python3
"""updown_diario_fase0.py -- FASE 0, SOLO OBSERVACIÓN: mercados "X Up or Down on <fecha>" (ronda 1 #5).

Regla de resolución (gamma, verificada 30-Sep): Up si el cierre de la vela de 1 min de Binance
X/USDT de las 12:00 ET de hoy es mayor que el de la vela de las 12:00 ET de ayer. La referencia
se conoce exacta desde el día anterior y el subyacente es Binance spot (sin oráculo intermedio).
Volumen por mercado (8-29 Sep, 87 mercados BTC/ETH/SOL/XRP): mediana 22k $, media 64k $.
Retrospectivo con precio MEDIO por minuto: n por tramo demasiado pequeño para concluir.

Qué captura (cron cada minuto; solo actúa en las 2 h previas al cierre y 3 min después):
spot de Binance, referencia, volatilidad de 1 min, z = ln(S/ref)/(sigma*sqrt(min restantes)),
probabilidad justa Phi(z) y el libro REAL de ambos lados (mejor bid/ask y USD hasta ask+1c).
Salida: data/shadow/updown_diario_fase0.csv (≈500 filas/día). Sin órdenes.
Gate para pensar en ejecutor: n>=40 mercados, >=10 días, EV al ask real >= +0,10 con IC90 por
días >0 en una celda definida ANTES de mirar (p. ej. valor = Phi(z) - ask >= 0,10 a T-10 min).
"""
import csv
import json
import math
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
OUT = REPO / "data" / "shadow" / "updown_diario_fase0.csv"
GAMMA = "https://gamma-api.polymarket.com"
CLOB_BOOK = "https://clob.polymarket.com/book"
BINANCE = "https://api.binance.com/api/v3"
ACTIVOS = {"bitcoin": "BTCUSDT", "ethereum": "ETHUSDT", "solana": "SOLUSDT", "xrp": "XRPUSDT",
           "dogecoin": "DOGEUSDT", "bnb": "BNBUSDT"}
MESES = ["january", "february", "march", "april", "may", "june", "july", "august", "september",
         "october", "november", "december"]
VENTANA_ANTES_MIN, VENTANA_DESPUES_MIN = 120, 3
COLS = ["ts_utc", "activo", "slug", "market_id", "min_restantes", "spot", "ref", "sigma_1m", "z", "prob_justa_up",
        "ask_up", "bid_up", "usd_ask_up", "ask_down", "bid_down", "usd_ask_down", "lat_ms", "error"]
_S = requests.Session()


def _phi(x: float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def _libro(token: str):
    r = _S.get(CLOB_BOOK, params={"token_id": token}, timeout=6)
    r.raise_for_status()
    j = r.json()
    asks = sorted((float(a["price"]), float(a["size"])) for a in (j.get("asks") or []))
    bids = sorted(((float(b["price"]), float(b["size"])) for b in (j.get("bids") or [])), reverse=True)
    ask = asks[0][0] if asks else None
    usd = round(sum(p * s for p, s in asks if p <= ask + 0.01), 2) if asks else 0.0
    return ask, (bids[0][0] if bids else None), usd


def _mercado(nombre: str, dia: datetime):
    slug = f"{nombre}-up-or-down-on-{MESES[dia.month - 1]}-{dia.day}-{dia.year}"
    j = _S.get(f"{GAMMA}/markets", params={"slug": slug}, timeout=10).json()
    return (slug, j[0]) if isinstance(j, list) and j else (slug, None)


def _kline_cierre(simbolo: str, apertura_utc: datetime):
    j = _S.get(f"{BINANCE}/klines", params={"symbol": simbolo, "interval": "1m", "limit": 1,
                                             "startTime": int(apertura_utc.timestamp() * 1000)}, timeout=8).json()
    return float(j[0][4]) if j and int(j[0][0]) == int(apertura_utc.timestamp() * 1000) else None


def _sigma_1m(simbolo: str):
    j = _S.get(f"{BINANCE}/klines", params={"symbol": simbolo, "interval": "1m", "limit": 121}, timeout=8).json()
    c = [float(x[4]) for x in j]
    r = [math.log(b / a) for a, b in zip(c, c[1:])]
    if len(r) < 60:
        return None, (c[-1] if c else None)
    m = sum(r) / len(r)
    return math.sqrt(sum((x - m) ** 2 for x in r) / len(r)), c[-1]


def main() -> int:
    ahora = datetime.now(timezone.utc)
    forzar = "--forzar" in sys.argv
    filas = []
    for nombre, simbolo in ACTIVOS.items():
        fila = {"ts_utc": ahora.isoformat(timespec="seconds"), "activo": simbolo[:-4], "error": ""}
        try:
            slug, m = None, None
            for d in (ahora, ahora + timedelta(days=1)):          # el de hoy; si ya cerró, el de mañana
                slug, m = _mercado(nombre, d)
                if m and datetime.fromisoformat(m["endDate"].replace("Z", "+00:00")) + timedelta(minutes=VENTANA_DESPUES_MIN) > ahora:
                    break
                m = None
            if m is None:
                continue
            fin = datetime.fromisoformat(m["endDate"].replace("Z", "+00:00"))
            resto = (fin - ahora).total_seconds() / 60
            if not forzar and not (-VENTANA_DESPUES_MIN <= resto <= VENTANA_ANTES_MIN):
                continue
            t0 = time.time()
            outs, toks = json.loads(m["outcomes"]), json.loads(m["clobTokenIds"])
            i_up = outs.index("Up")
            ref = _kline_cierre(simbolo, fin - timedelta(days=1))
            sigma, spot = _sigma_1m(simbolo)
            ask_u, bid_u, usd_u = _libro(toks[i_up])
            ask_d, bid_d, usd_d = _libro(toks[1 - i_up])
            z = p = ""
            if ref and spot and sigma and resto + 1 > 0.05:
                z = math.log(spot / ref) / (sigma * math.sqrt(max(resto + 1, 0.05)))   # +1: la vela decisiva cierra 1 min después
                p = round(_phi(z), 4)
                z = round(z, 3)
            fila.update({"slug": slug, "market_id": m.get("id", ""), "min_restantes": round(resto, 2), "spot": spot,
                         "ref": ref if ref is not None else "", "sigma_1m": f"{sigma:.6f}" if sigma else "", "z": z,
                         "prob_justa_up": p, "ask_up": ask_u if ask_u is not None else "",
                         "bid_up": bid_u if bid_u is not None else "", "usd_ask_up": usd_u,
                         "ask_down": ask_d if ask_d is not None else "", "bid_down": bid_d if bid_d is not None else "",
                         "usd_ask_down": usd_d, "lat_ms": round((time.time() - t0) * 1000)})
        except Exception as e:
            fila["error"] = f"{type(e).__name__}: {e}"[:120]
        filas.append(fila)
    if not filas:
        return 0
    if "--no-escribir" in sys.argv:
        for f in filas:
            print({k: f.get(k, "") for k in COLS})
        return 0
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        if nuevo:
            w.writeheader()
        for fila in filas:
            w.writerow({k: fila.get(k, "") for k in COLS})
    return 0


if __name__ == "__main__":
    sys.exit(main())
