#!/usr/bin/env python3
"""live_balance.py — Lee el balance REAL de Polymarket (read-only) y lo cachea.

Motivo (2026-07-07): el dashboard/`trades.csv` reportaban un PnL live de plan
(precio de entrada previsto, `fee_eur=0.00`) que NUNCA se contrastaba contra el
wallet. Real −3.63 USDC vs registrado −0.78 → dashboard engañoso. Este módulo
ancla el bankroll live a la verdad de suelo: el USDC del wallet + valor de
posiciones abiertas.

- **Read-only**: solo consulta balance/posiciones, jamás envía órdenes.
- **Fail-closed**: si la API falla, NO sobrescribe el JSON cacheado (deja el
  último bueno) y sale con código !=0. El dashboard trata el JSON viejo/ausente
  como "n/d" y no fabrica cifras.
- **No en el hot-path del dashboard**: se invoca periódicamente (slow loop/cron);
  el dashboard solo LEE `data/live/balance_real.json`.

Uso:  python3 live_balance.py          # fetch + cache
      from live_balance import cargar_balance_real   # lectura cacheada
"""
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

DIR_LIVE = Path(__file__).parent / "data" / "live"
CACHE_PATH = DIR_LIVE / "balance_real.json"
HIST_PATH = DIR_LIVE / "balance_history.csv"

try:
    from live_stake import CAPITAL_OPERATIVO_INICIAL as DEPOSITO_INICIAL
except Exception:
    DEPOSITO_INICIAL = 25.44  # depósito real 2026-06-29 (fallback)

DATA_API = "https://data-api.polymarket.com"
USDC_DECIMALS = 1_000_000  # USDC = 6 decimales


def _get_clob_client():
    """Cliente CLOB V2 autenticado (mismo flujo que live_trade)."""
    from dotenv import load_dotenv
    from py_clob_client_v2 import ClobClient, ApiCreds
    from py_clob_client_v2.constants import POLYGON
    load_dotenv(DIR_LIVE / ".env")
    creds = ApiCreds(
        api_key=os.getenv("POLY_API_KEY"),
        api_secret=os.getenv("POLY_API_SECRET"),
        api_passphrase=os.getenv("POLY_API_PASSPHRASE"),
    )
    return ClobClient(
        "https://clob.polymarket.com",
        key=os.getenv("POLY_PRIVATE_KEY"),
        chain_id=POLYGON,
        creds=creds,
        signature_type=3,
        funder=os.getenv("POLY_DEPOSIT_WALLET"),
    )


def _free_usdc(client) -> float:
    """USDC libre (colateral) del wallet, en unidades USDC."""
    from py_clob_client_v2.clob_types import BalanceAllowanceParams, AssetType
    ba = client.get_balance_allowance(
        BalanceAllowanceParams(asset_type=AssetType.COLLATERAL))
    raw = ba.get("balance") if isinstance(ba, dict) else None
    if raw is None:
        raise RuntimeError(f"balance_allowance sin 'balance': {ba!r}")
    return int(raw) / USDC_DECIMALS


def _positions_value(wallet: str) -> float:
    """Valor mark-to-market de las posiciones abiertas (data-api /value).

    Devuelve 0.0 si no hay posiciones vivas (todo resuelto/redimido).
    """
    r = requests.get(f"{DATA_API}/value", params={"user": wallet}, timeout=20)
    r.raise_for_status()
    d = r.json()
    if isinstance(d, list) and d:
        return float(d[0].get("value") or 0.0)
    if isinstance(d, dict):
        return float(d.get("value") or 0.0)
    return 0.0


def fetch_balance_real() -> dict:
    """Consulta el balance real. Lanza excepción si algo falla (fail-closed)."""
    wallet = os.getenv("POLY_DEPOSIT_WALLET")
    client = _get_clob_client()
    if not wallet:
        wallet = os.getenv("POLY_DEPOSIT_WALLET")
    free = _free_usdc(client)
    pos = _positions_value(wallet)
    total = free + pos
    return {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "wallet": wallet,
        "free_usdc": round(free, 4),
        "positions_value": round(pos, 4),
        "total": round(total, 4),
        "deposito_inicial": DEPOSITO_INICIAL,
        "pnl_real": round(total - DEPOSITO_INICIAL, 4),
    }


def _append_history(snap: dict) -> None:
    """Serie temporal del balance real (para la equity curve fiel)."""
    nuevo = not HIST_PATH.exists()
    with open(HIST_PATH, "a", encoding="utf-8") as f:
        if nuevo:
            f.write("ts,free_usdc,positions_value,total,pnl_real\n")
        f.write(f"{snap['ts']},{snap['free_usdc']},{snap['positions_value']},"
                f"{snap['total']},{snap['pnl_real']}\n")


def actualizar_balance_real() -> dict | None:
    """Refresca el cache de balance AHORA (fetch + write). Guardado: nunca lanza.

    Pensado para engancharse tras abrir/cerrar un trade real, de modo que el
    dashboard y los mensajes de Telegram reflejen el balance del wallet al
    instante en vez de esperar al cron de 15min. Devuelve el snapshot o None.
    """
    try:
        snap = fetch_balance_real()
        CACHE_PATH.write_text(json.dumps(snap, indent=1), encoding="utf-8")
        try:
            _append_history(snap)
        except Exception:
            pass
        return snap
    except Exception:
        return None


def cargar_balance_real(max_edad_s: int | None = None) -> dict | None:
    """Lee el JSON cacheado. Devuelve None si falta o está rancio (fail-closed)."""
    try:
        snap = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return None
    if max_edad_s is not None:
        try:
            ts = datetime.fromisoformat(snap["ts"])
            edad = (datetime.now(timezone.utc) - ts).total_seconds()
            if edad > max_edad_s:
                snap["_rancio"] = True
                snap["_edad_s"] = round(edad)
        except Exception:
            return None
    return snap


def main() -> int:
    try:
        snap = fetch_balance_real()
    except Exception as e:
        # Fail-closed: no tocar el cache; el último bueno se conserva.
        print(f"[live_balance] ERROR fetch (cache intacto): {e!r}", file=sys.stderr)
        return 1
    CACHE_PATH.write_text(json.dumps(snap, indent=1), encoding="utf-8")
    try:
        _append_history(snap)
    except Exception as e:
        print(f"[live_balance] aviso: no se pudo escribir history: {e!r}", file=sys.stderr)
    print(f"[live_balance] real total={snap['total']} USDC "
          f"(libre={snap['free_usdc']} pos={snap['positions_value']}) "
          f"pnl_real={snap['pnl_real']} vs deposito {snap['deposito_inicial']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
