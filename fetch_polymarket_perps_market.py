#!/usr/bin/env python3
"""fetch_polymarket_perps_market.py — Captura de TODO el universo de mercados
de Polymarket Perps (67 instrumentos: cripto/oro/plata/petróleo/índices/
acciones), no solo las wallets. Petición explícita Javi 09-Sep: "hay que
intentar captura absolutamente todo el universo para obtener los mejores
datos" -- complementa a fetch_polymarket_perps_leaderboard.py (wallets) con
la foto del propio mercado (volumen, precio, funding) por instrumento.

Diseño de bajo consumo (mismo criterio que el resto de fetchers de esta
sesión -- RAM ajustada, ver project_disco_ram_critico_09sep): CRON, no
screen. Dos llamadas ligeras:

  GET /v1/info/instruments   -- lista de los 67 mercados (símbolo,
      max_leverage, funding_interval, etc.) -- cambia poco, se cachea a
      disco y solo se re-descarga si el cache tiene >24h.
  GET /v1/info/statistics    -- volumen + precio de apertura + klines de
      TODOS los instrumentos en UNA sola llamada (~97KB, verificado
      09-Sep) -- de aquí sacamos qué instrumentos son realmente líquidos,
      dato que usa fetch_polymarket_perps_wallet_fills.py para decidir en
      qué mercados vale la pena mirar fills de wallet (no tiene sentido
      gastar requests en las ~35 acciones ilíquidas si el volumen real
      está concentrado en cripto/oro/índices).

Salida: data/shadow/polymarket_perps_market_YYYY-MM-DD.csv (append,
snapshot por instrumento cada corrida -- solo volumen/precio, NO las
klines completas para no inflar el CSV).
"""
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
DIR_SHADOW.mkdir(parents=True, exist_ok=True)

API_BASE = "https://api.perpetuals.polymarket.com"
TIMEOUT = 20

RUTA_INSTRUMENTS_CACHE = DIR_SHADOW / "polymarket_perps_instruments.json"
CAMPOS = ["timestamp_utc", "instrument_id", "symbol", "category", "volume", "open_price"]


def _cargar_instrumentos() -> dict:
    """Cache de /v1/info/instruments a disco, refrescado si tiene >24h."""
    if RUTA_INSTRUMENTS_CACHE.exists():
        edad_h = (datetime.now(timezone.utc).timestamp() - RUTA_INSTRUMENTS_CACHE.stat().st_mtime) / 3600
        if edad_h < 24:
            try:
                data = json.loads(RUTA_INSTRUMENTS_CACHE.read_text())
                return {d["instrument_id"]: d for d in data}
            except Exception:
                pass
    try:
        r = requests.get(f"{API_BASE}/v1/info/instruments", timeout=TIMEOUT)
        r.raise_for_status()
        data = r.json()
        RUTA_INSTRUMENTS_CACHE.write_text(json.dumps(data, ensure_ascii=False))
        return {d["instrument_id"]: d for d in data}
    except Exception as e:
        print(f"  [WARN] instruments error: {type(e).__name__}: {e}", file=sys.stderr)
        return {}


def _out_path(ahora: datetime) -> Path:
    return DIR_SHADOW / f"polymarket_perps_market_{ahora.date().isoformat()}.csv"


def main() -> int:
    ahora = datetime.now(timezone.utc)
    ahora_iso = ahora.isoformat(timespec="seconds")

    instrumentos = _cargar_instrumentos()
    if not instrumentos:
        print(f"[{ahora_iso}] Sin lista de instrumentos, abortando.")
        return 0

    try:
        r = requests.get(f"{API_BASE}/v1/info/statistics", timeout=TIMEOUT)
        r.raise_for_status()
        stats = r.json()
    except Exception as e:
        print(f"[{ahora_iso}] [WARN] statistics error: {type(e).__name__}: {e}", file=sys.stderr)
        return 0

    filas = []
    for s in stats:
        iid = s.get("instrument_id")
        meta = instrumentos.get(iid, {})
        filas.append({
            "timestamp_utc": ahora_iso,
            "instrument_id": iid,
            "symbol": s.get("symbol", meta.get("symbol", "")),
            "category": meta.get("category", ""),
            "volume": s.get("volume", ""),
            "open_price": s.get("open_price", ""),
        })

    path = _out_path(ahora)
    nuevo = not path.exists()
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        if nuevo:
            w.writeheader()
        for fila in filas:
            w.writerow(fila)

    print(f"[{ahora_iso}] {len(filas)} instrumentos escritos en {path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
