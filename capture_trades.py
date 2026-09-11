"""
capture_trades.py — v1. Captura trades recientes de las top wallets del leaderboard.

Usa la API pública de Polymarket data-api para obtener actividad de cada wallet
sin necesidad de acceso directo a la blockchain de Polygon.
Guarda en data/trades/YYYY-MM-DD.csv con campos normalizados.
"""
import csv, glob, json, time
from datetime import datetime, timezone, timedelta
from pathlib import Path
import requests

TIMEOUT = 30
VENTANA_HORAS = 4          # trades de las últimas 4 horas
PAUSA_ENTRE_WALLETS = 0.5  # segundos entre peticiones para no saturar la API
MAX_WALLETS = 50            # procesar solo top N wallets del leaderboard

DIR_WALLETS = Path("data/wallets")
DIR_TRADES  = Path("data/trades")
DIR_TRADES.mkdir(parents=True, exist_ok=True)

CABECERA = [
    "timestamp_utc", "wallet", "market_id", "condition_id",
    "question", "outcome", "side", "price", "usd_amount", "trade_type",
]

HEADERS_HTTP = {
    "User-Agent": "Mozilla/5.0 (compatible; polymarket-research/1.0)",
    "Accept": "application/json",
}

DATA_API = "https://data-api.polymarket.com/activity"


def cargar_wallets_leaderboard():
    archivos = sorted(glob.glob(str(DIR_WALLETS / "leaderboard_*.csv")))
    if not archivos:
        print("  No hay leaderboard CSV, abortando.")
        return []
    archivo = archivos[-1]
    wallets = []
    with open(archivo, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            addr = (row.get("address") or "").strip().lower()
            if addr:
                wallets.append(addr)
            if len(wallets) >= MAX_WALLETS:
                break
    print(f"  Leaderboard cargado desde {Path(archivo).name}: {len(wallets)} wallets")
    return wallets


def fetch_actividad(wallet_addr):
    try:
        r = requests.get(
            DATA_API,
            params={"user": wallet_addr, "limit": 500},
            headers=HEADERS_HTTP,
            timeout=TIMEOUT,
        )
        if r.status_code == 404:
            return []
        r.raise_for_status()
        return r.json() or []
    except Exception as e:
        print(f"    Error data-api para {wallet_addr[:10]}...: {type(e).__name__}: {e}")
        return []


def normalizar_trade(item, wallet_addr):
    ts_raw = item.get("timestamp") or item.get("createdAt") or item.get("created_at") or ""
    if isinstance(ts_raw, (int, float)):
        ts = datetime.fromtimestamp(ts_raw, tz=timezone.utc).isoformat(timespec="seconds")
    elif isinstance(ts_raw, str) and ts_raw:
        ts = ts_raw[:19]
    else:
        ts = ""

    condition_id = (item.get("conditionId") or item.get("condition_id") or "").strip()
    market_id    = (item.get("marketId") or item.get("market_id") or item.get("market") or "").strip()
    question     = (item.get("question") or item.get("title") or "").strip()
    outcome      = (item.get("outcome") or item.get("side") or "").strip()
    side_raw     = (item.get("type") or item.get("side") or "").upper()

    if side_raw in ("BUY", "SELL"):
        side = side_raw
    elif outcome.lower() in ("yes", "up"):
        side = "BUY"
    elif outcome.lower() in ("no", "down"):
        side = "SELL"
    else:
        side = ""

    if outcome.lower() in ("yes", "up", "1"):
        outcome = "YES"
    elif outcome.lower() in ("no", "down", "0"):
        outcome = "NO"

    try:    price = float(item.get("price") or 0)
    except: price = 0.0
    try:    usd_amount = float(item.get("usdcSize") or item.get("amount") or item.get("size") or 0)
    except: usd_amount = 0.0

    trade_type = (item.get("tradeType") or item.get("maker_taker") or "").upper()

    return {
        "timestamp_utc": ts, "wallet": wallet_addr,
        "market_id": market_id, "condition_id": condition_id,
        "question": question, "outcome": outcome, "side": side,
        "price": price, "usd_amount": usd_amount, "trade_type": trade_type,
    }


def es_reciente(ts_str, ventana_horas):
    if not ts_str:
        return False
    try:
        s = ts_str[:19] + "+00:00"
        dt = datetime.fromisoformat(s)
        return (datetime.now(timezone.utc) - dt).total_seconds() <= ventana_horas * 3600
    except Exception:
        return False


def archivar_si_obsoleto(archivo, cabecera):
    if not archivo.exists():
        return
    try:
        with open(archivo, encoding="utf-8") as f:
            primera = f.readline().strip()
        if primera != ",".join(cabecera):
            destino = archivo.with_suffix(".old.csv")
            archivo.rename(destino)
            print(f"  Archivado {archivo.name} → {destino.name} (cabecera obsoleta)")
    except Exception as e:
        print(f"  Error verificando {archivo}: {e}")


def main():
    ts_inicio = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts_inicio}] === Capture Trades v1 ===")

    wallets = cargar_wallets_leaderboard()
    if not wallets:
        return

    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    archivo = DIR_TRADES / f"{fecha}.csv"
    archivar_si_obsoleto(archivo, CABECERA)
    nuevo = not archivo.exists()
    total_trades = 0
    wallets_con_datos = 0

    with open(archivo, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(CABECERA)
        for i, wallet in enumerate(wallets):
            actividad = fetch_actividad(wallet)
            if not actividad:
                time.sleep(PAUSA_ENTRE_WALLETS)
                continue
            recientes = []
            for item in actividad:
                trade = normalizar_trade(item, wallet)
                if not es_reciente(trade["timestamp_utc"], VENTANA_HORAS):
                    continue
                if not trade["market_id"] and not trade["condition_id"]:
                    continue
                recientes.append(trade)
            if recientes:
                wallets_con_datos += 1
                for t in recientes:
                    w.writerow([
                        t["timestamp_utc"], t["wallet"], t["market_id"],
                        t["condition_id"], t["question"], t["outcome"],
                        t["side"], f"{t['price']:.6f}", f"{t['usd_amount']:.2f}",
                        t["trade_type"],
                    ])
                total_trades += len(recientes)
            if (i + 1) % 10 == 0:
                print(f"  Procesadas {i+1}/{len(wallets)} wallets, {total_trades} trades recientes")
            time.sleep(PAUSA_ENTRE_WALLETS)

    print(f"  Total: {wallets_con_datos}/{len(wallets)} wallets con trades recientes")
    print(f"  Trades guardados en {archivo}: {total_trades}")
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] === Fin ===")


if __name__ == "__main__":
    main()
