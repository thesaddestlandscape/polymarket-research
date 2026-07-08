"""
ledger_fiscal.py — Registro limpio de movimientos de la wallet live para
declaración fiscal. Genera un CSV reproducible con fecha, tipo, contravalor
en USD/EUR y hash de transacción. Read-only, no toca producción ni trading.

Dos fuentes:
  1. data-api.polymarket.com/activity (TRADE/REDEEM) — SIEMPRE disponible,
     sin clave. Cubre toda la actividad DENTRO de Polymarket (compras y
     canjes de posiciones).
  2. api.polygonscan.com (transferencias USDC on-chain) — SOLO si hay
     POLYGONSCAN_API_KEY en data/live/.env. Cubre entradas/salidas de la
     wallet (depósito inicial, retiradas a exchange). Sin esto, el registro
     NO incluye el depósito inicial ni cualquier retirada — se avisa
     explícitamente en la salida, no se omite en silencio (fail loud).

Cómo conseguir la clave (gratis, ~2min): https://polygonscan.com/myapikey
Añadir a data/live/.env: POLYGONSCAN_API_KEY=xxxxx

Salida: data/live/ledger_fiscal_polymarket.csv (movimientos dentro de
Polymarket) + data/live/ledger_fiscal_onchain.csv (entradas/salidas de la
wallet, solo si hay clave).
"""
import csv
import os
import time
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path

import requests

DIR = Path(__file__).parent
ENV_PATH = DIR / "data/live/.env"
OUT_POLY = DIR / "data/live/ledger_fiscal_polymarket.csv"
OUT_ONCHAIN = DIR / "data/live/ledger_fiscal_onchain.csv"
DATA_API = "https://data-api.polymarket.com"
POLYGONSCAN_API = "https://api.polygonscan.com/api"
USDC_POLYGON = "0x3c499c542cef5e3811e1192ce70d8cc03d5c3359"


def _cargar_env() -> dict:
    d = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                d[k.strip()] = v.strip()
    return d


@lru_cache(maxsize=None)
def eur_por_usd(fecha: str) -> float | None:
    """Tipo de cambio USD->EUR del día (Frankfurter, sin clave, BCE).
    fecha en formato YYYY-MM-DD. None si el día no tiene dato (festivo)."""
    try:
        r = requests.get(f"https://api.frankfurter.app/{fecha}",
                         params={"from": "USD", "to": "EUR"}, timeout=10)
        r.raise_for_status()
        return r.json().get("rates", {}).get("EUR")
    except Exception:
        return None


def fetch_polymarket_activity(wallet: str) -> list:
    """TRADE + REDEEM completos de la wallet, paginado hasta agotar."""
    evs = []
    offset = 0
    while True:
        r = requests.get(f"{DATA_API}/activity",
                         params={"user": wallet, "limit": 500, "offset": offset},
                         timeout=20)
        r.raise_for_status()
        chunk = r.json()
        if not chunk:
            break
        evs.extend(chunk)
        if len(chunk) < 500:
            break
        offset += 500
        time.sleep(0.2)
    return evs


def fetch_onchain_usdc(wallet: str, api_key: str) -> list | None:
    """Transferencias USDC (Polygon) entrantes/salientes de la wallet.
    None si la API falla (clave inválida, rate limit, etc.) — fail loud,
    el caller decide qué avisar."""
    try:
        r = requests.get(POLYGONSCAN_API, params={
            "module": "account", "action": "tokentx",
            "contractaddress": USDC_POLYGON, "address": wallet,
            "startblock": 0, "endblock": 99999999, "sort": "asc",
            "apikey": api_key,
        }, timeout=20)
        r.raise_for_status()
        d = r.json()
        if d.get("status") != "1":
            print(f"  [WARN] Polygonscan respondió: {d.get('message')} — {d.get('result')}")
            return None
        return d.get("result", [])
    except Exception as e:
        print(f"  [WARN] fetch_onchain_usdc falló: {e}")
        return None


def main():
    env = _cargar_env()
    wallet = env.get("POLY_DEPOSIT_WALLET")
    if not wallet:
        print("[ERROR] POLY_DEPOSIT_WALLET no encontrado en data/live/.env — no se puede continuar.")
        return 1

    print(f"Wallet: {wallet}\n")

    # 1. Actividad dentro de Polymarket (TRADE/REDEEM) — siempre disponible
    print("Descargando actividad Polymarket (TRADE/REDEEM)...")
    evs = fetch_polymarket_activity(wallet)
    print(f"  {len(evs)} eventos")

    filas = []
    for e in sorted(evs, key=lambda x: x.get("timestamp", 0)):
        try:
            dt = datetime.fromtimestamp(int(e["timestamp"]), tz=timezone.utc)
        except Exception:
            continue
        fecha = dt.strftime("%Y-%m-%d")
        usd = float(e.get("usdcSize") or 0)
        tipo = e.get("type", "")
        signo = -1 if tipo == "TRADE" else 1  # TRADE=sale USDC, REDEEM=entra
        usd_firmado = signo * usd
        tc = eur_por_usd(fecha)
        eur = round(usd_firmado * tc, 4) if tc else ""
        filas.append({
            "fecha_utc": dt.isoformat(),
            "tipo": tipo,
            "mercado": e.get("title") or e.get("slug") or "",
            "outcome": e.get("outcome", ""),
            "usd": round(usd_firmado, 4),
            "eur": eur,
            "tc_usd_eur": tc or "",
            "tx_hash": e.get("transactionHash", ""),
        })

    with open(OUT_POLY, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()) if filas else
                           ["fecha_utc", "tipo", "mercado", "outcome", "usd", "eur", "tc_usd_eur", "tx_hash"])
        w.writeheader()
        w.writerows(filas)
    print(f"  guardado: {OUT_POLY} ({len(filas)} filas)")

    neto_usd = sum(f["usd"] for f in filas)
    print(f"  neto TRADE+REDEEM: {neto_usd:+.2f} USD (esto NO incluye el depósito inicial "
          f"ni retiradas — ver sección on-chain)")

    # 2. Entradas/salidas de la wallet (on-chain) — solo si hay clave
    print()
    api_key = env.get("POLYGONSCAN_API_KEY")
    if not api_key:
        print("⚠️  POLYGONSCAN_API_KEY no está en data/live/.env — SIN ESTO el registro "
              "NO incluye el depósito inicial a la wallet ni ninguna retirada a un "
              "exchange. Consigue una clave gratis en https://polygonscan.com/myapikey "
              "(2 min, sin coste) y añade la línea POLYGONSCAN_API_KEY=xxxxx al .env, "
              "luego vuelve a correr este script.")
        return 0

    print("Descargando transferencias USDC on-chain (Polygonscan)...")
    txs = fetch_onchain_usdc(wallet, api_key)
    if txs is None:
        print("⚠️  No se pudo obtener el historial on-chain — revisa la clave. "
              "El registro de Polymarket (arriba) sigue siendo válido.")
        return 0

    filas_chain = []
    for t in txs:
        try:
            dt = datetime.fromtimestamp(int(t["timeStamp"]), tz=timezone.utc)
            valor_usdc = int(t["value"]) / (10 ** int(t.get("tokenDecimal", 6)))
        except Exception:
            continue
        fecha = dt.strftime("%Y-%m-%d")
        entra = t.get("to", "").lower() == wallet.lower()
        usd_firmado = valor_usdc if entra else -valor_usdc
        tc = eur_por_usd(fecha)
        eur = round(usd_firmado * tc, 4) if tc else ""
        filas_chain.append({
            "fecha_utc": dt.isoformat(),
            "direccion": "ENTRADA" if entra else "SALIDA",
            "contraparte": t.get("from") if entra else t.get("to"),
            "usd": round(usd_firmado, 4),
            "eur": eur,
            "tc_usd_eur": tc or "",
            "tx_hash": t.get("hash", ""),
        })

    with open(OUT_ONCHAIN, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas_chain[0].keys()) if filas_chain else
                           ["fecha_utc", "direccion", "contraparte", "usd", "eur", "tc_usd_eur", "tx_hash"])
        w.writeheader()
        w.writerows(filas_chain)
    print(f"  guardado: {OUT_ONCHAIN} ({len(filas_chain)} filas)")
    print("  NOTA: esta lista incluye TODAS las transferencias USDC de la wallet, "
          "incluidas las que van hacia/desde los contratos de Polymarket (ya cubiertas "
          "arriba). Un asesor puede filtrar por contraparte para quedarse solo con "
          "depósitos/retiradas externas reales — no lo hago yo automáticamente para no "
          "arriesgar una clasificación equivocada.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
