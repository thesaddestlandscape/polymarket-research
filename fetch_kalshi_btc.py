#!/usr/bin/env python3
"""
fetch_kalshi_btc.py — Captura periódica (REST público, sin auth) del precio
de los mercados BTC de Kalshi, en TODOS los marcos temporales que Kalshi
ofrece para cripto direccional. Solo lectura, no toca dinero ni ninguna
decisión.

Origen (19-Ago, petición explícita Javi -- hilo de investigación externa de
SynthData: el precio de Kalshi BTC#15min precede al spot de Binance en la
ventana 0-10s, correlación 0.036→0.173 a lo largo de 2026), extendido el
mismo día a petición de Javi ("hazlo para todos los marcos temporales, no
solo 15 minutos"). Ver idea_kalshi_lidera_binance_leadlag_19ago en memoria
nativa.

**Marcos disponibles verificados en Kalshi (19-Ago, categoría Crypto)**:
solo existen DOS frecuencias direccionales para BTC -- `fifteen_min`
(serie KXBTC15M, "BTC price up in next 15 mins?", un solo mercado abierto
a la vez, resuelve YES si sube) y `hourly` (serie KXBTCD, "Bitcoin price
above/below $X", ESCALERA de ~100 strikes simultáneos por hora, resuelve
por comparación contra un strike fijo, no un simple up/down). NO existen
en Kalshi mercados cripto de 5min, 240min (4h) ni weekly direccional --
confirmado contra el listado completo de series de la categoría Crypto,
no hay hueco de cobertura que llenar ahí, es un límite real de lo que
Kalshi ofrece.

Ambos resuelven vía CF Benchmarks BRTI (TWAP de 60s) -- estructura
análoga a nuestro propio BTC#15min/60min de Polymarket (TWAP también,
desde el cambio del 07-Ago).

**KXBTC15M** (`_poll_15m`): un solo mercado abierto, se captura tal cual
cada ciclo (igual que la versión original de este captor).

**KXBTCD** (`_poll_hourly`): ~100 strikes por hora, la inmensa mayoría
degenerados (yes_bid=0/yes_ask=1 o viceversa, muy OTM/ITM -- sin
información, solo ruido). Se filtra al vuelo a la banda "viva"
(0 < yes_ask < 1), que sigue al precio spot automáticamente según pasan
los minutos -- normalmente 1-5 strikes informativos a la vez. Un único
GET a la lista trae yes_bid/yes_ask de TODOS los strikes de golpe (sin
llamadas por-mercado), barato pese al tamaño de la escalera.

Salidas: data/prices/kalshi_btc15m_YYYY-MM-DD.csv (sin cambios de
esquema respecto al captor original) y
data/prices/kalshi_btchourly_YYYY-MM-DD.csv (nuevo, incluye floor_strike
y event_ticker ya que hay varios mercados vivos a la vez).

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
HTTP_TIMEOUT_S = 8

# --- KXBTC15M (fifteen_min, un solo mercado abierto) ---
SERIES_15M = "KXBTC15M"
POLL_15M_S = 2.0
REFRESH_TICKER_15M_S = 30

COLUMNS_15M = [
    "timestamp_utc", "ticker", "floor_strike", "yes_bid", "yes_ask",
    "last_price", "volume", "open_time", "close_time",
]

# --- KXBTCD (hourly, escalera de strikes) ---
SERIES_HOURLY = "KXBTCD"
POLL_HOURLY_S = 3.0

COLUMNS_HOURLY = [
    "timestamp_utc", "ticker", "event_ticker", "floor_strike", "yes_bid",
    "yes_ask", "last_price", "volume", "open_time", "close_time",
]


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _archivo_hoy(nombre_base: str) -> Path:
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return DIR_PRICES / f"{nombre_base}_{fecha}.csv"


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "polymarket-research/1.0"})
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT_S) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _escribir_fila(archivo: Path, columnas: list, valores: list) -> None:
    nuevo = not archivo.exists()
    with open(archivo, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(columnas)
        w.writerow(valores)


# ---------------------------------------------------------------- KXBTC15M

def _ticker_activo_15m() -> dict | None:
    url = f"{BASE_URL}/markets?series_ticker={SERIES_15M}&status=open&limit=5"
    data = _get(url)
    mercados = data.get("markets", [])
    if not mercados:
        return None
    mercados.sort(key=lambda m: m.get("open_time", ""), reverse=True)
    return mercados[0]


def _escribir_tick_15m(m: dict) -> None:
    _escribir_fila(_archivo_hoy("kalshi_btc15m"), COLUMNS_15M, [
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


def _poll_15m() -> None:
    _log(f"arrancando poll {SERIES_15M} cada {POLL_15M_S}s")
    mercado_actual = None
    ultimo_refresh = 0.0
    while True:
        try:
            ahora = time.time()
            if mercado_actual is None or (ahora - ultimo_refresh) >= REFRESH_TICKER_15M_S:
                nuevo = _ticker_activo_15m()
                if nuevo is not None:
                    if mercado_actual is None or nuevo.get("ticker") != mercado_actual.get("ticker"):
                        _log(f"[15m] mercado activo: {nuevo.get('ticker')} "
                             f"(strike={nuevo.get('floor_strike')}, cierra={nuevo.get('close_time')})")
                    mercado_actual = nuevo
                ultimo_refresh = ahora
            if mercado_actual is not None:
                detalle = _get(f"{BASE_URL}/markets/{mercado_actual['ticker']}")
                _escribir_tick_15m(detalle.get("market", mercado_actual))
        except Exception as e:
            _log(f"[15m] error: {type(e).__name__}: {e}")
            time.sleep(5)
            continue
        time.sleep(POLL_15M_S)


# ---------------------------------------------------------------- KXBTCD

def _viva(m: dict) -> bool:
    """Strike con precio no degenerado -- filtra la mayoría de la escalera
    (~100 strikes). OJO: el tick mínimo de Kalshi deja el "suelo" en
    ask=0.01/bid=0.00 y el "techo" en ask=1.00/bid=0.99 incluso para
    strikes sin ninguna incertidumbre real -- comprobado en vivo (19-Ago)
    que un filtro `0<ask<1` cuela TODA la escalera (bug real, corregido).
    Se exige que el BID esté estrictamente lejos de ambos extremos."""
    try:
        bid = float(m.get("yes_bid_dollars") or m.get("yes_bid") or 0)
    except (TypeError, ValueError):
        return False
    return 0.02 < bid < 0.98


def _poll_hourly() -> None:
    _log(f"arrancando poll {SERIES_HOURLY} cada {POLL_HOURLY_S}s")
    while True:
        try:
            data = _get(f"{BASE_URL}/markets?series_ticker={SERIES_HOURLY}&status=open&limit=200")
            mercados = data.get("markets", [])
            vivos = [m for m in mercados if _viva(m)]
            ts = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
            archivo = _archivo_hoy("kalshi_btchourly")
            for m in vivos:
                _escribir_fila(archivo, COLUMNS_HOURLY, [
                    ts,
                    m.get("ticker"),
                    m.get("event_ticker"),
                    m.get("floor_strike"),
                    m.get("yes_bid_dollars") or m.get("yes_bid"),
                    m.get("yes_ask_dollars") or m.get("yes_ask"),
                    m.get("last_price_dollars") or m.get("last_price"),
                    m.get("volume_fp") or m.get("volume"),
                    m.get("open_time"),
                    m.get("close_time"),
                ])
        except Exception as e:
            _log(f"[hourly] error: {type(e).__name__}: {e}")
            time.sleep(5)
            continue
        time.sleep(POLL_HOURLY_S)


def main() -> None:
    """Lanza los 2 pollers en hilos propios -- este módulo ya vive dentro
    de un hilo de fetchers_fase0.py, así que aquí solo hace falta un hilo
    extra para el segundo poller (el primero corre en este mismo hilo)."""
    import threading
    t = threading.Thread(target=_poll_hourly, daemon=True, name="kalshi_hourly")
    t.start()
    _poll_15m()  # bucle infinito, ocupa el hilo llamador


if __name__ == "__main__":
    main()
