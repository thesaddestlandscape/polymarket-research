#!/usr/bin/env python3
"""fetch_perps_tickers.py -- foto cada 5 min de /v1/info/tickers de Polymarket Perps
(index, mark, last, mid, open_interest, funding_rate, next_funding) para los 67
instrumentos. Hallazgo 29-Sep: el funding SI es publico (el pendiente #4 de
project_perps_pendientes_25sep decia que no). Objetivo: medir basis mark-index,
OI y funding por instrumento a lo largo del tiempo (edge candidato: funding
extremo / basis). Solo lectura, sin dinero. Salida fuera de git:
/root/polymarket-research-datalogs/perps_tickers_YYYY-MM-DD.csv (dias anteriores
se comprimen a .gz, retencion 30 dias). Cron */5.
"""
import csv, gzip, os, sys, time
from datetime import datetime, timezone, timedelta
from pathlib import Path
import requests

DIR = Path("/root/polymarket-research-datalogs")
URL = "https://api.perpetuals.polymarket.com/v1/info/tickers"
CAMPOS = ["ts_utc", "instrument_id", "symbol", "index_price", "mark_price", "last_price",
          "mid_price", "open_interest", "funding_rate", "next_funding"]
RETENCION_DIAS = 30


def main() -> int:
    DIR.mkdir(parents=True, exist_ok=True)
    try:
        r = requests.get(URL, timeout=15)
        r.raise_for_status()
        data = r.json()
        assert isinstance(data, list) and data, "respuesta vacia"
    except Exception as e:
        print(f"{datetime.now(timezone.utc).isoformat()} ERROR {e}", file=sys.stderr)
        return 1
    ahora = datetime.now(timezone.utc)
    ruta = DIR / f"perps_tickers_{ahora:%Y-%m-%d}.csv"
    nuevo = not ruta.exists()
    with open(ruta, "a", newline="") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(CAMPOS)
        ts = ahora.isoformat(timespec="seconds")
        for x in data:
            w.writerow([ts, x.get("instrument_id"), x.get("symbol"), x.get("index_price"),
                        x.get("mark_price"), x.get("last_price"), x.get("mid_price"),
                        x.get("open_interest"), x.get("funding_rate"), x.get("next_funding")])
    hoy = f"{ahora:%Y-%m-%d}"
    for p in DIR.glob("perps_tickers_*.csv"):          # comprimir dias cerrados
        if hoy not in p.name:
            with open(p, "rb") as fi, gzip.open(str(p) + ".gz", "wb") as fo:
                fo.write(fi.read())
            p.unlink()
    lim = time.time() - RETENCION_DIAS * 86400
    for p in DIR.glob("perps_tickers_*.csv.gz"):
        if p.stat().st_mtime < lim:
            p.unlink()
    print(f"{ts} ok {len(data)} instrumentos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
