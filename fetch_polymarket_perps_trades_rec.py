#!/usr/bin/env python3
"""fetch_polymarket_perps_trades_rec.py -- graba TODAS las operaciones de los perps de Polymarket (BTC/ETH/SOL)
para medir el lead-lag frente a Binance (06-Oct, OK Javi "graba horas para coger todos los datos posibles").

Los perps no tienen WS público (404): se sondea REST /v1/info/trades (100 últimas por instrumento) cada ~1,5 s
por instrumento. Medido 05-Oct: ~5 operaciones/min en BTC, 1 respuesta 429 de 1.164. Cron horario con flock:
cada ejecución graba DUR s en datalogs/perps_trades/perps_trades_YYYY-MM-DD_HH.csv (pocos KB/h; retención
30 d en este mismo script). El lead-lag se calcula contra los aggTrades de Binance del registro ms
(maker_ms_*.csv.gz, retención 4 d): analizar dentro de esa ventana.
Columnas: moneda, ts_exchange_ms, precio, cantidad, lado, ts_recepcion_ms. Duplicados entre horas posibles
(se deduplica al analizar por moneda+ts+precio+cantidad+lado).

Uso: fetch_polymarket_perps_trades_rec.py [segundos=3540]
"""
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

DIR = Path("/root/polymarket-research-datalogs/perps_trades")
INST = {6: "BTC", 7: "ETH", 8: "SOL"}
RETENCION_D = 30


def main():
    dur = float(sys.argv[1]) if len(sys.argv) > 1 else 3540
    DIR.mkdir(parents=True, exist_ok=True)
    for f in DIR.glob("perps_trades_*.csv"):
        if time.time() - f.stat().st_mtime > RETENCION_D * 86400:
            f.unlink()
    out = DIR / f"perps_trades_{datetime.now(timezone.utc):%Y-%m-%d_%H}.csv"
    vistos, n429, nreq, huecos, nerr = set(), 0, 0, 0, 0
    ses = requests.Session()
    fin = time.time() + dur
    t_ini = int(time.time() * 1000) - 120_000
    with open(out, "a", encoding="utf-8") as f:
        while time.time() < fin:
            for iid, c in INST.items():
                try:
                    r = ses.get("https://api.perpetuals.polymarket.com/v1/info/trades",
                                params={"instrument_id": iid}, timeout=10)
                    nreq += 1
                    if r.status_code == 429:
                        n429 += 1
                        time.sleep(5)
                        continue
                    d = r.json().get("data", [])
                    nuevos = [t for t in d if t["trade_id"] not in vistos and t["timestamp"] >= t_ini]
                    if d and len(nuevos) == len(d) and vistos:
                        huecos += 1          # los 100 eran nuevos: puede faltar algo entre consultas
                    rec = int(time.time() * 1000)
                    for t in nuevos:
                        vistos.add(t["trade_id"])
                        f.write(f"{c},{t['timestamp']},{t['price']},{t['quantity']},{t['side']},{rec}\n")
                    f.flush()
                except Exception as e:
                    nerr += 1
                    print(f"error {type(e).__name__}: {e}", flush=True)
                    time.sleep(2)
                time.sleep(0.5)
    print(f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} {out.name}: peticiones {nreq}, 429 {n429}, "
          f"errores {nerr}, posibles huecos {huecos}, operaciones {len(vistos)}", flush=True)


if __name__ == "__main__":
    main()
