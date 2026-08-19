#!/usr/bin/env python3
"""
fetch_kalshi_btc15m.py — Captura periódica (REST público, sin auth) del
precio del mercado BTC#15min de Kalshi (serie KXBTC15M, "BTC price up in
next 15 mins?", resuelve vía CF Benchmarks BRTI TWAP 60s -- estructura casi
idéntica a nuestro propio BTC#15min de Polymarket). Solo lectura, no toca
dinero ni ninguna decisión.

Origen (19-Ago, petición explícita Javi -- hilo de investigación externa de
SynthData: el precio de Kalshi BTC#15min precede al spot de Binance en la
ventana 0-10s, correlación 0.036→0.173 a lo largo de 2026). Verificado en
vivo el mismo día que la API pública de Kalshi (api.elections.kalshi.com,
sin autenticación) da acceso completo a mercado/orderbook/trades con
timestamps de milisegundo -- ver idea_kalshi_lidera_binance_leadlag_19ago
en memoria nativa.

Objetivo del captor: acumular precio Kalshi de alta cadencia en paralelo a
data/prices/chainlink_YYYY-MM-DD.csv (ya existente, mismo directorio) para
poder medir MÁS ADELANTE si el movimiento de Kalshi precede al spot
Chainlink/Binance que ya usamos, y si precede al propio precio de
Polymarket en sus mercados BTC#15min -- ningún análisis todavía, solo
captura. Igual que chainlink, dejar acumular varios días antes de analizar.

Descubre el ticker del mercado 15min ACTIVO vía
GET /markets?series_ticker=KXBTC15M&status=open (rota cada 15min, un solo
mercado abierto a la vez) y lo re-resuelve cuando el actual cierra.
Cadencia de polling 2s (mismo orden de magnitud que chainlink, ~43k
filas/día, tamaño comparable a un solo activo de chainlink -- no requiere
sacarlo del repo git como libro_ambos_lados/results.csv).

Corre fusionado en la screen "fetchers" (fetchers_fase0.py), NO screen
propia -- mismo motivo de presupuesto de CPU que el resto de fetchers
consolidados el 07-Ago.
"""

import csv
import time
import urllib.request
import json
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
DIR_PRICES = REPO / "data" / "prices"
DIR_PRICES.mkdir(parents=True, exist_ok=True)

BASE_URL = "https://api.elections.kalshi.com/trade-api/v2"
SERIES_TICKER = "KXBTC15M"
POLL_INTERVAL_S = 2.0
REFRESH_TICKER_EVERY_S = 30  # re-verificar si el mercado activo rotó
HTTP_TIMEOUT_S = 8

COLUMNS = [
    "timestamp_utc", "ticker", "floor_strike", "yes_bid", "yes_ask",
    "last_price", "volume", "open_time", "close_time",
]


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _archivo_hoy() -> Path:
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return DIR_PRICES / f"kalshi_btc15m_{fecha}.csv"


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "polymarket-research/1.0"})
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT_S) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _ticker_activo() -> dict | None:
    """Devuelve el mercado KXBTC15M actualmente abierto, o None si falla."""
    url = f"{BASE_URL}/markets?series_ticker={SERIES_TICKER}&status=open&limit=5"
    data = _get(url)
    mercados = data.get("markets", [])
    if not mercados:
        return None
    # el más reciente por open_time (normalmente solo hay 1 abierto)
    mercados.sort(key=lambda m: m.get("open_time", ""), reverse=True)
    return mercados[0]


def _escribir_tick(m: dict) -> None:
    archivo = _archivo_hoy()
    nuevo = not archivo.exists()
    with open(archivo, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(COLUMNS)
        w.writerow([
            datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
            m.get("ticker"),
            m.get("floor_strike"),
            m.get("yes_bid_dollars") or m.get("yes_bid"),
            m.get("yes_ask_dollars") or m.get("yes_ask"),
            m.get("last_price_dollars") or m.get("last_price"),
            m.get("volume_fp") or m.get("volume"),
            m.get("open_time"),
            m.get("close_time"),
        ])


def main() -> None:
    _log(f"arrancando captor Kalshi {SERIES_TICKER}, poll cada {POLL_INTERVAL_S}s")
    mercado_actual = None
    ultimo_refresh = 0.0
    errores_seguidos = 0
    while True:
        try:
            ahora = time.time()
            necesita_refresh = (
                mercado_actual is None
                or (ahora - ultimo_refresh) >= REFRESH_TICKER_EVERY_S
            )
            if necesita_refresh:
                nuevo = _ticker_activo()
                if nuevo is not None:
                    if mercado_actual is None or nuevo.get("ticker") != mercado_actual.get("ticker"):
                        _log(f"mercado activo: {nuevo.get('ticker')} "
                             f"(strike={nuevo.get('floor_strike')}, "
                             f"cierra={nuevo.get('close_time')})")
                    mercado_actual = nuevo
                ultimo_refresh = ahora

            if mercado_actual is not None:
                # refrescar precio del mercado actual (no solo al detectarlo)
                detalle = _get(f"{BASE_URL}/markets/{mercado_actual['ticker']}")
                m = detalle.get("market", mercado_actual)
                _escribir_tick(m)
            errores_seguidos = 0
        except Exception as e:
            errores_seguidos += 1
            if errores_seguidos <= 3 or errores_seguidos % 20 == 0:
                _log(f"error polling ({errores_seguidos} seguidos): {type(e).__name__}: {e}")
            time.sleep(min(30, POLL_INTERVAL_S * errores_seguidos))
            continue
        time.sleep(POLL_INTERVAL_S)


if __name__ == "__main__":
    main()
