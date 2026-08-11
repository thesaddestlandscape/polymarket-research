#!/usr/bin/env python3
"""fetch_binance_perp_cvd_oi.py — Captura periódica de klines PERP (no
spot) + Open Interest de Binance Futures para los 6 activos operados.

Origen: idea_amt_spot_vs_perp_cvd_20jul (Auction Market Theory —
divergencia CVD spot vs CVD perp + OI para distinguir breakouts genuinos
de squeezes de apalancamiento). Javi aprobó explícitamente construirlo
20-Jul ("apúntalo para ir construyéndolo en próximas sesiones"), nunca
empezado hasta hoy (11-Ago).

Fuente: REST `fapi.binance.com` (dominio de futuros, distinto del spot
`api.binance.com` que ya usa fetch_binance_klines.py). OJO -- esto NO es
lo mismo que `wss://fstream.binance.com` (websocket de futuros), que está
bloqueado/throttled para la IP de este VPS (ver idea_binance_liquidaciones_
bloqueadas_ip_29jul) -- REST fapi SÍ funciona, verificado 11-Ago para los
6 activos (BTC/ETH/SOL/XRP/DOGE/BNB) antes de escribir este script.

Guarda en data/shadow/binance_perp_cvd_oi_YYYY-MM-DD.csv (APPEND, historial
creciente -- a diferencia de data/binance/klines_YYYY-MM-DD.json que el
fast loop sobreescribe cada ciclo, aquí necesitamos ACUMULAR días de
historia antes de poder calcular nada, mismo motivo por el que
`ballenas_timing_history.csv`/`data/markets/*.csv` son append-only):
timestamp_utc, activo, perp_close, perp_volume, perp_taker_buy_vol,
perp_delta_ratio (mismo cálculo que _calcular_delta_ratio_macro en
shadow_predict.py, aplicado a klines PERP en vez de spot), open_interest.

Puramente captura -- NO calcula divergencia todavía (paso 3 del plan
original, requiere unos días de historia primero) ni toca ninguna
decisión. Cron cada 5min (OI/CVD son señales de minutos-horas según AMT,
no necesitan cadencia de segundos como el fast loop).

⚠️ TWAP -- pendiente de diseño para el paso 3 (NO aplica a este script,
que solo captura en vivo hacia adelante sin comparar contra histórico):
cuando se construya la comparación perp_delta_ratio vs outcome_real,
(a) excluir régimen pre-TWAP igual que el resto del pipeline
(shadow_postmortem.es_pre_twap(), marcos 5min/15min/240min), y (b) más
específico -- el payoff de esos marcos ya es TWAP de 30s/60s antes del
cierre (opción asiática, no snapshot puntual, ver project_twap_chainlink_
confirmado_09ago), así que el CVD perp a comparar debe alinearse con ESA
ventana concreta, no con "las últimas N velas" arbitrarias que captura
este script hoy -- la captura cruda (timestamp por fila) permite recortar
después, pero el análisis debe diseñarse con esto en mente desde el
principio, no como parche posterior."""
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

DIR_SHADOW = Path(__file__).parent / "data/shadow"
DIR_SHADOW.mkdir(parents=True, exist_ok=True)

FAPI = "https://fapi.binance.com"
TIMEOUT = 15
LIMIT = 5  # klines 1min recientes, suficiente para el delta_ratio de la ventana de captura

BINANCE_SYMBOLS = {
    "BTC": "BTCUSDT", "ETH": "ETHUSDT", "SOL": "SOLUSDT",
    "XRP": "XRPUSDT", "DOGE": "DOGEUSDT", "BNB": "BNBUSDT",
}

CAMPOS = ["timestamp_utc", "activo", "perp_close", "perp_volume",
          "perp_taker_buy_vol", "perp_delta_ratio", "open_interest"]


def _out_path(ahora: datetime) -> Path:
    return DIR_SHADOW / f"binance_perp_cvd_oi_{ahora.date().isoformat()}.csv"


def fetch_perp_klines(symbol: str) -> list | None:
    try:
        r = requests.get(f"{FAPI}/fapi/v1/klines",
                          params={"symbol": symbol, "interval": "1m", "limit": LIMIT},
                          timeout=TIMEOUT)
        r.raise_for_status()
        raw = r.json()
        # mismo formato [time_ms,o,h,l,c,vol,taker_buy_vol] que fetch_binance_klines.py::fetch_binance(with_flow=True)
        return [[k[0], k[1], k[2], k[3], k[4], k[5], k[9]] for k in raw]
    except Exception as e:
        print(f"  [WARN] perp klines error {symbol}: {type(e).__name__}: {e}", file=sys.stderr)
        return None


def fetch_open_interest(symbol: str) -> float | None:
    try:
        r = requests.get(f"{FAPI}/fapi/v1/openInterest", params={"symbol": symbol}, timeout=TIMEOUT)
        r.raise_for_status()
        return float(r.json()["openInterest"])
    except Exception as e:
        print(f"  [WARN] OI error {symbol}: {type(e).__name__}: {e}", file=sys.stderr)
        return None


def delta_ratio(klines: list) -> float | None:
    if not klines or len(klines[0]) < 7:
        return None
    tb = sum(float(k[6]) for k in klines)
    tv = sum(float(k[5]) for k in klines)
    ts_vol = tv - tb
    denom = tb + ts_vol
    if denom <= 0:
        return None
    return (tb - ts_vol) / denom


def main() -> int:
    ahora = datetime.now(timezone.utc)
    path = _out_path(ahora)
    nuevo = not path.exists()

    filas = []
    for activo, symbol in BINANCE_SYMBOLS.items():
        klines = fetch_perp_klines(symbol)
        oi = fetch_open_interest(symbol)
        if klines is None and oi is None:
            continue
        ultimo = klines[-1] if klines else None
        filas.append({
            "timestamp_utc": ahora.isoformat(timespec="seconds"),
            "activo": activo,
            "perp_close": float(ultimo[4]) if ultimo else "",
            "perp_volume": sum(float(k[5]) for k in klines) if klines else "",
            "perp_taker_buy_vol": sum(float(k[6]) for k in klines) if klines else "",
            "perp_delta_ratio": delta_ratio(klines) if klines else "",
            "open_interest": oi if oi is not None else "",
        })

    if not filas:
        print("Sin datos de ningún activo -- Binance fapi no responde, nada que escribir.")
        return 0

    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        if nuevo:
            w.writeheader()
        for fila in filas:
            w.writerow(fila)

    print(f"[{ahora.isoformat(timespec='seconds')}] {len(filas)}/{len(BINANCE_SYMBOLS)} activos escritos en {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
