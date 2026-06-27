"""
fetch_binance_klines.py — Fetches 1-min OHLCV klines for crypto assets.

Primary source: Kraken public REST API (no geo-restrictions, no auth needed).
Fallback source: Binance public API (may return HTTP 451 from US-based CI runners).

Saves to data/binance/klines_YYYY-MM-DD.json as:
{
  "timestamp_utc": "...",
  "BTC": [[open_time_ms, open, high, low, close, volume], ...],
  "ETH": [...],
  ...
}
open_time_ms is Unix milliseconds (consistent with Binance format).

If all sources are unreachable, prints a warning and exits 0.
"""
import csv, json, sys, time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import requests

from data_quality import validar_precio, leer_ultimo_precio, obtener_consensus_spot, _cross_cache_fresco

DIR_PRICES = Path("data") / "prices"
DIR_PRICES.mkdir(parents=True, exist_ok=True)

SPOT_SYMBOLS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]

TIMEOUT = 15
LIMIT   = 25  # number of 1-min candles

# Kraken pair names (XBT = BTC on Kraken)
KRAKEN_PAIRS = {
    "BTC":  "XBTUSD",
    "ETH":  "ETHUSD",
    "SOL":  "SOLUSD",
    "XRP":  "XRPUSD",
    "DOGE": "DOGEUSD",
    "BNB":  "BNBUSD",
}

# Binance symbol names (fallback)
BINANCE_SYMBOLS = {
    "BTC":  "BTCUSDT",
    "ETH":  "ETHUSDT",
    "SOL":  "SOLUSDT",
    "XRP":  "XRPUSDT",
    "DOGE": "DOGEUSDT",
    "BNB":  "BNBUSDT",
}

DIR_BINANCE = Path("data") / "binance"
DIR_BINANCE.mkdir(parents=True, exist_ok=True)


def fetch_kraken(asset: str) -> list | None:
    """Fetch last LIMIT 1-min candles from Kraken. Returns [[open_time_ms, o, h, l, c, v], ...]."""
    pair = KRAKEN_PAIRS.get(asset)
    if not pair:
        return None
    try:
        # Kraken OHLC: since = now - LIMIT minutes
        since = int(time.time()) - LIMIT * 60
        r = requests.get(
            "https://api.kraken.com/0/public/OHLC",
            params={"pair": pair, "interval": 1, "since": since},
            timeout=TIMEOUT,
        )
        r.raise_for_status()
        body = r.json()
        if body.get("error"):
            print(f"  [WARN] Kraken error for {asset}: {body['error']}", file=sys.stderr)
            return None
        result = body.get("result", {})
        # Kraken returns the pair key (sometimes with X/Z prefix). Take first non-"last" key.
        candle_key = next((k for k in result if k != "last"), None)
        if not candle_key:
            return None
        candles = result[candle_key][-LIMIT:]  # take last LIMIT candles
        # Kraken format: [time_sec, open, high, low, close, vwap, volume, count]
        # Convert to Binance-compatible: [open_time_ms, open, high, low, close, volume]
        return [[c[0] * 1000, c[1], c[2], c[3], c[4], c[6]] for c in candles]
    except Exception as e:
        print(f"  [WARN] Kraken error for {asset}: {type(e).__name__}: {e}", file=sys.stderr)
        return None


def fetch_binance(asset: str, with_flow: bool = False) -> list | None:
    """Fetch last LIMIT 1-min klines from Binance.
    with_flow=True → devuelve 7 columnas: [time_ms, o, h, l, c, vol, taker_buy_vol]
    with_flow=False → 6 columnas compatibles con Kraken.
    """
    symbol = BINANCE_SYMBOLS.get(asset)
    if not symbol:
        return None
    try:
        r = requests.get(
            "https://api.binance.com/api/v3/klines",
            params={"symbol": symbol, "interval": "1m", "limit": LIMIT},
            timeout=TIMEOUT,
        )
        r.raise_for_status()
        raw = r.json()
        if with_flow:
            # col 9: taker_buy_base_asset_volume
            return [[k[0], k[1], k[2], k[3], k[4], k[5], k[9]] for k in raw]
        return [[k[0], k[1], k[2], k[3], k[4], k[5]] for k in raw]
    except Exception as e:
        print(f"  [WARN] Binance error for {asset}: {type(e).__name__}: {e}", file=sys.stderr)
        return None


def main():
    now_utc = datetime.now(timezone.utc)
    ts_str  = now_utc.isoformat(timespec="seconds")
    fecha   = now_utc.strftime("%Y-%m-%d")
    print(f"[{ts_str}] Fetching 1-min klines (Kraken primary, Binance fallback)...")

    data = {"timestamp_utc": ts_str}
    any_success = False

    def _fetch_asset(asset):
        klines = fetch_binance(asset, with_flow=True)
        source = "Binance+flow"
        if klines is None:
            klines = fetch_kraken(asset)
            source = "Kraken"
        return asset, klines, source

    with ThreadPoolExecutor(max_workers=len(KRAKEN_PAIRS)) as ex:
        for asset, klines, source in ex.map(_fetch_asset, list(KRAKEN_PAIRS)):
            if klines is not None:
                data[asset] = klines
                any_success = True
                has_flow = len(klines[0]) >= 7 if klines else False
                print(f"  {asset}: {len(klines)} klines OK [{source}{'  ✓flow' if has_flow else ''}]")
            else:
                print(f"  {asset}: SKIP (both sources failed)")

    if not any_success:
        print("[WARN] No klines fetched — all sources unreachable. Exiting 0.")
        sys.exit(0)

    out_path = DIR_BINANCE / f"klines_{fecha}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, separators=(",", ":"))
    print(f"  Saved -> {out_path}")

    # Escribir spot price (close de última vela) en prices CSV cada 60s
    # Solo si el archivo ya existe (capture_markets lo crea con el header completo)
    # Kraken/Binance reemplaza la dependencia de CoinGecko free tier para los 6 activos principales
    prices_path = DIR_PRICES / f"{fecha}.csv"
    if not prices_path.exists():
        # Crear el archivo con header si no existe (no depender de capture_markets)
        with open(prices_path, "w", newline="", encoding="utf-8") as pf:
            csv.writer(pf).writerow(["timestamp_utc", "asset", "price_usd", "change_1h_pct", "change_24h_pct"])

    # Leer último precio de cada asset (para detección de spikes en L1)
    last_prices = {sym: leer_ultimo_precio(sym, prices_path) for sym in SPOT_SYMBOLS}

    # L1: extraer y validar precios desde klines
    binance_prices: dict[str, float] = {}
    for sym in SPOT_SYMBOLS:
        klines_sym = data.get(sym)
        if not (klines_sym and isinstance(klines_sym, list)):
            continue
        try:
            price = float(klines_sym[-1][4])
        except (IndexError, ValueError, TypeError):
            continue
        ok, motivo = validar_precio(sym, price, last_prices.get(sym))
        if not ok:
            print(f"  [DQ L1] {sym} RECHAZADO ({motivo})")
            continue
        binance_prices[sym] = price

    # L4: cross-source consensus (Binance vs Coinbase vs Kraken)
    # TTL 5min: solo hace peticiones externas cuando el cache está stale.
    # Coinbase = settlement reference para BTC/ETH en Polymarket.
    assets_gbm  = ["BTC", "ETH", "SOL", "XRP"]
    binance_gbm = {k: v for k, v in binance_prices.items() if k in assets_gbm}
    if binance_gbm:
        try:
            consensus = obtener_consensus_spot(binance_gbm, assets_gbm, timeout=4)
            cross     = consensus.get("cross", {})
            cached    = consensus.get("cached", False)
            if not cached and cross.get("alertas"):
                for a in cross["alertas"]:
                    icon = "🚨" if a["accion"] == "BLOQUEADO" else "⚠️"
                    print(f"  [DQ L4] {icon} {a['sym']} div={a['max_div_pct']:.2f}% ({'cache' if cached else 'fresco'})")
            for sym, px_consenso in consensus.get("precios", {}).items():
                if sym in binance_prices:
                    binance_prices[sym] = px_consenso
        except Exception as _cs_err:
            print(f"  [DQ L4] Cross-source error (no bloqueante): {_cs_err}")

    if binance_prices:
        with open(prices_path, "a", newline="", encoding="utf-8") as pf:
            w = csv.writer(pf)
            for sym, price in binance_prices.items():
                w.writerow([ts_str, sym, price, "", ""])
        btc = binance_prices.get('BTC','?')
        eth = binance_prices.get('ETH','?')
        sol = binance_prices.get('SOL','?')
        print(f"  Spot → prices/{fecha}.csv  BTC={btc} ETH={eth} SOL={sol}")

    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] Done.")


if __name__ == "__main__":
    main()
