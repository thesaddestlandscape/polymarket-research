"""
capture_prices.py — Captura precio spot de activos cripto via CoinGecko.
Guarda en data/prices/YYYY-MM-DD.csv con precio actual, cambio 1h y 24h.
"""
import csv
from datetime import datetime, timezone
from pathlib import Path
import requests

TIMEOUT = 30
DIR_PRICES = Path("data/prices")
DIR_PRICES.mkdir(parents=True, exist_ok=True)

ACTIVOS = {
    "BTC":  "bitcoin",
    "ETH":  "ethereum",
    "SOL":  "solana",
    "XRP":  "ripple",
    "DOGE": "dogecoin",
}

CABECERA = ["timestamp_utc", "asset", "price_usd", "change_1h_pct", "change_24h_pct"]

HEADERS_HTTP = {
    "User-Agent": "Mozilla/5.0 (compatible; polymarket-research/1.0)",
    "Accept": "application/json",
}


def fetch_precios():
    ids = ",".join(ACTIVOS.values())
    try:
        r = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={
                "ids": ids,
                "vs_currencies": "usd",
                "include_24hr_change": "true",
                "include_1hr_change": "true",
            },
            headers=HEADERS_HTTP,
            timeout=TIMEOUT,
        )
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"  Error CoinGecko: {type(e).__name__}: {e}")
        return {}


def main():
    ts = datetime.now(timezone.utc)
    ts_str = ts.isoformat(timespec="seconds")
    print(f"[{ts_str}] === Capture Prices ===")

    datos = fetch_precios()
    if not datos:
        print("  Sin datos, abortando.")
        return

    fecha = ts.strftime("%Y-%m-%d")
    archivo = DIR_PRICES / f"{fecha}.csv"
    nuevo = not archivo.exists()

    filas = []
    for symbol, cg_id in ACTIVOS.items():
        entry = datos.get(cg_id, {})
        price      = entry.get("usd", 0)
        change_1h  = entry.get("usd_1h_change", 0) or 0
        change_24h = entry.get("usd_24h_change", 0) or 0
        filas.append([ts_str, symbol, f"{price:.2f}", f"{change_1h:.4f}", f"{change_24h:.4f}"])
        print(f"  {symbol}: ${price:,.2f}  1h={change_1h:+.2f}%  24h={change_24h:+.2f}%")

    with open(archivo, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(CABECERA)
        w.writerows(filas)

    print(f"  Guardado en {archivo} ({len(filas)} activos)")
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] === Fin ===")


if __name__ == "__main__":
    main()
