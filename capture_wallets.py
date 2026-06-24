"""
capture_wallets.py — captura del top 75 de wallets en cripto + sus posiciones.

Frecuencia: ejecutado cada 2 horas por el workflow .github/workflows/wallets.yml.

Endpoints utilizados (oficiales, ver https://docs.polymarket.com/api-reference):
  - GET https://data-api.polymarket.com/v1/leaderboard
  - GET https://data-api.polymarket.com/positions

Definición de 'top wallet' (MONTH + WEEK, categoría CRYPTO):
  Se obtienen cuatro rankings:
    a) MONTH ordenado por PNL (top 50)
    b) MONTH ordenado por VOL (top 50)
    c) WEEK ordenado por PNL (top 50)
    d) WEEK ordenado por VOL (top 50)
  Se fusionan por período y se calcula un score combinado:
    score = 0.6 * (1 - rank_pnl_normalizado) + 0.4 * (1 - rank_vol_normalizado)
  Los top 50 mensuales y top 50 semanales se combinan, se deduplican por
  dirección y se conservan los 75 con mejor score combinado.

Nota: la API oficial NO expone winRate como campo. Por eso se sustituye la
combinación PNL+winRate+VOL pactada inicialmente por PNL+VOL. Es la definición
mejor aproximada disponible públicamente.

Salida:
  - data/wallets/leaderboard_YYYY-MM-DD.csv  (ranking en cada captura)
  - data/wallets/positions_YYYY-MM-DD.csv    (posiciones detalladas)
"""

import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

TIMEOUT = 30
TOP_N = 75
DELAY_BETWEEN_USERS = 0.25   # segundos entre llamadas a /positions (rate limit cortés)
BOT_TRADES_THRESHOLD = 500   # más de 500 trades en el período → probable bot (market maker/sweeper)

DIR_WALLETS = Path("data/wallets")
DIR_WALLETS.mkdir(parents=True, exist_ok=True)

LEADERBOARD_URL = "https://data-api.polymarket.com/v1/leaderboard"
POSITIONS_URL = "https://data-api.polymarket.com/positions"


def fetch_leaderboard(order_by: str, time_period: str = "MONTH") -> list:
    """Obtiene el leaderboard de cripto ordenado por PNL o VOL para el período indicado."""
    params = {
        "category": "CRYPTO",
        "timePeriod": time_period,
        "orderBy": order_by,
        "limit": 50,
        "offset": 0,
    }
    r = requests.get(LEADERBOARD_URL, params=params, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()


def combinar_rankings(por_pnl: list, por_vol: list) -> list:
    """Fusiona los dos rankings y calcula score combinado."""
    by_addr = {}
    n_pnl = max(1, len(por_pnl))
    n_vol = max(1, len(por_vol))

    for i, u in enumerate(por_pnl):
        addr = (u.get("proxyWallet") or "").lower()
        if not addr:
            continue
        by_addr.setdefault(addr, dict(u))
        by_addr[addr]["_rank_pnl"] = i  # 0 = mejor
    for i, u in enumerate(por_vol):
        addr = (u.get("proxyWallet") or "").lower()
        if not addr:
            continue
        by_addr.setdefault(addr, dict(u))
        by_addr[addr]["_rank_vol"] = i

    for u in by_addr.values():
        # Si no está en uno de los dos rankings, le ponemos el peor rank posible.
        rank_pnl = u.get("_rank_pnl", n_pnl)
        rank_vol = u.get("_rank_vol", n_vol)
        norm_pnl = rank_pnl / n_pnl
        norm_vol = rank_vol / n_vol
        u["_score"] = 0.6 * (1 - norm_pnl) + 0.4 * (1 - norm_vol)

    fusionados = sorted(by_addr.values(), key=lambda u: u["_score"], reverse=True)
    return fusionados[:TOP_N]


def fetch_positions(address: str) -> list:
    """Obtiene posiciones actuales (size>1) de un usuario."""
    params = {"user": address, "sizeThreshold": 1, "limit": 500}
    r = requests.get(POSITIONS_URL, params=params, timeout=TIMEOUT)
    if r.status_code != 200:
        return []
    try:
        return r.json()
    except ValueError:
        return []


def guardar_leaderboard(top: list, ts: str) -> None:
    fecha = ts[:10]
    archivo = DIR_WALLETS / f"leaderboard_{fecha}.csv"
    nuevo = not archivo.exists()
    with open(archivo, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow([
                "timestamp_utc", "rank_combined", "address", "username",
                "pnl", "vol", "rank_pnl", "rank_vol", "score",
                "verified_badge", "x_username", "timeframe",
                "num_trades", "wallet_type",
            ])
        for i, u in enumerate(top, 1):
            try:
                num_trades = int(u.get("numTrades") or u.get("tradesCount") or 0)
            except (ValueError, TypeError):
                num_trades = 0
            wallet_type = "BOT" if num_trades > BOT_TRADES_THRESHOLD else ("HUMAN" if num_trades > 0 else "UNKNOWN")
            w.writerow([
                ts, i,
                (u.get("proxyWallet") or "").lower(),
                u.get("userName", ""),
                u.get("pnl", ""),
                u.get("vol", ""),
                u.get("_rank_pnl", ""),
                u.get("_rank_vol", ""),
                round(u.get("_score", 0), 4),
                u.get("verifiedBadge", ""),
                u.get("xUsername", ""),
                "MONTH+WEEK",
                num_trades,
                wallet_type,
            ])


def guardar_posiciones(filas: list, ts: str) -> None:
    fecha = ts[:10]
    archivo = DIR_WALLETS / f"positions_{fecha}.csv"
    nuevo = not archivo.exists()
    with open(archivo, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow([
                "timestamp_utc", "address", "username",
                "condition_id", "title", "outcome",
                "size", "avg_price", "current_value", "initial_value",
                "cash_pnl", "percent_pnl", "cur_price", "end_date",
            ])
        for fila in filas:
            w.writerow(fila)


def main():
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] === Captura wallets ===")

    try:
        por_pnl = fetch_leaderboard("PNL", "MONTH")
        print(f"  Leaderboard PNL MONTH: {len(por_pnl)} entradas")
    except Exception as e:
        print(f"  ERROR leaderboard PNL MONTH: {type(e).__name__}: {e}")
        sys.exit(1)

    try:
        por_vol = fetch_leaderboard("VOL", "MONTH")
        print(f"  Leaderboard VOL MONTH: {len(por_vol)} entradas")
    except Exception as e:
        print(f"  ERROR leaderboard VOL MONTH: {type(e).__name__}: {e}")
        por_vol = []

    try:
        por_pnl_week = fetch_leaderboard("PNL", "WEEK")
        print(f"  Leaderboard PNL WEEK: {len(por_pnl_week)} entradas")
    except Exception as e:
        print(f"  ERROR leaderboard PNL WEEK: {type(e).__name__}: {e}")
        por_pnl_week = []

    try:
        por_vol_week = fetch_leaderboard("VOL", "WEEK")
        print(f"  Leaderboard VOL WEEK: {len(por_vol_week)} entradas")
    except Exception as e:
        print(f"  ERROR leaderboard VOL WEEK: {type(e).__name__}: {e}")
        por_vol_week = []

    # Combinar rankings MONTH y WEEK, deduplicar por dirección, quedarse con TOP_N
    top_month = combinar_rankings(por_pnl, por_vol)
    top_week = combinar_rankings(por_pnl_week, por_vol_week)
    # Merge: empezar con el pool mensual y añadir wallets semanales si no están ya
    by_addr = {(u.get("proxyWallet") or "").lower(): u for u in top_month if (u.get("proxyWallet") or "")}
    for u in top_week:
        addr = (u.get("proxyWallet") or "").lower()
        if addr and addr not in by_addr:
            by_addr[addr] = u
    # Reordenar por score y tomar TOP_N
    top = sorted(by_addr.values(), key=lambda u: u.get("_score", 0), reverse=True)[:TOP_N]
    print(f"  Top combinado MONTH+WEEK: {len(top)} wallets")
    guardar_leaderboard(top, ts)

    posiciones_filas = []
    errores = 0
    for u in top:
        addr = (u.get("proxyWallet") or "").lower()
        if not addr:
            continue
        try:
            posiciones = fetch_positions(addr)
            for p in posiciones:
                posiciones_filas.append([
                    ts, addr, u.get("userName", ""),
                    p.get("conditionId", ""),
                    p.get("title", ""),
                    p.get("outcome", ""),
                    p.get("size", ""),
                    p.get("avgPrice", ""),
                    p.get("currentValue", ""),
                    p.get("initialValue", ""),
                    p.get("cashPnl", ""),
                    p.get("percentPnl", ""),
                    p.get("curPrice", ""),
                    (p.get("endDate") or "")[:19],
                ])
        except Exception as e:
            errores += 1
            if errores <= 3:
                print(f"  Error en posiciones de {addr}: {type(e).__name__}")
        time.sleep(DELAY_BETWEEN_USERS)

    guardar_posiciones(posiciones_filas, ts)
    print(f"  Posiciones registradas: {len(posiciones_filas)} "
          f"(errores: {errores})")
    print(f"[{ts}] === Fin captura wallets ===")


if __name__ == "__main__":
    main()
