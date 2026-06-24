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
import json, sys, time
from datetime import datetime, timezone
from pathlib import Path
import requests

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


def fetch_binance(asset: str) -> list | None:
    """Fetch last LIMIT 1-min klines from Binance (fallback). May return 451 on CI runners."""
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

    for asset in KRAKEN_PAIRS:
        klines = fetch_kraken(asset)
        source = "Kraken"
        if klines is None:
            klines = fetch_binance(asset)
            source = "Binance"
        if klines is not None:
            data[asset] = klines
            any_success = True
            print(f"  {asset}: {len(klines)} klines OK [{source}]")
        else:
            print(f"  {asset}: SKIP (both sources failed)")

    if not any_success:
        print("[WARN] No klines fetched — all sources unreachable. Exiting 0.")
        sys.exit(0)

    out_path = DIR_BINANCE / f"klines_{fecha}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, separators=(",", ":"))
    print(f"  Saved -> {out_path}")
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] Done.")


if __name__ == "__main__":
    main()
