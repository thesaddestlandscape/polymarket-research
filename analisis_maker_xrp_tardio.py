#!/usr/bin/env python3
"""Read-only: ¿el enfoque maker (piloto ya arreglado hoy) rescataría XRP
específicamente para GBM_LATE_15M_TARDIO#XRP#15min#BUY_YES? Pregunta directa
tras el hallazgo del 11-Jul: esta tupla pasa ambos gates estadísticos
(Wilson+shuffle Y corrección por tests múltiples) con margen, pero sigue
bloqueada por selección adversa taker específica de XRP (ver
project_diagnostico_perdidas_10jul). El criterio de reapertura documentado
en config_live.json dice: "(b) se implementa entrada maker sobre señales
vetadas y XRP la pasa".

maker_sim.py YA simuló esto pero solo para GBM_LATE_15M/UPDOWN_GBM base (no
para el subtipo TARDIO, que no está en su ESTRATEGIAS_SIM) y con UN solo
MEJORA=0.02 fijo. Este script repite la simulación con datos reales de tape
(mismo método: data-api/trades, conservador) pero:
  1. Específicamente sobre las 90 señales resueltas de
     GBM_LATE_15M_TARDIO#XRP#15min#BUY_YES (el candidato real, no un proxy).
  2. Con un BARRIDO de MEJORA (0.01 a 0.05) para ver si ALGÚN precio de
     entrada pasivo da EV positivo, no solo el 0.02 por defecto.

No toca ningún gate, config ni estrategia — solo lectura pública
(gamma-api + data-api), mismo patrón que maker_sim.py.
"""
import csv
import time
from datetime import datetime, timedelta, timezone

import requests

RESULTS = "data/shadow/results.csv"
GAMMA_API = "https://gamma-api.polymarket.com"
DATA_API = "https://data-api.polymarket.com"
H = {"User-Agent": "Mozilla/5.0 (compatible; polymarket-research/1.0)"}
TIMEOUT = 10
CANCEL_MIN = 4
MEJORAS = [0.01, 0.015, 0.02, 0.03, 0.04, 0.05]


def cargar_senales():
    filas = []
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("strategy") != "GBM_LATE_15M_TARDIO":
                continue
            if row.get("subtype") != "XRP#15min":
                continue
            if row.get("decision") != "BUY_YES":
                continue
            if row.get("acierto") not in ("True", "False", "1", "0"):
                continue
            filas.append(row)
    return filas


def conditionId_de(market_id):
    try:
        r = requests.get(f"{GAMMA_API}/markets/{market_id}", timeout=TIMEOUT, headers=H)
        if r.status_code != 200:
            return None
        data = r.json()
        if isinstance(data, list) and data:
            data = data[0]
        return data.get("conditionId") if isinstance(data, dict) else None
    except Exception:
        return None


def trades_de(cond_id):
    try:
        r = requests.get(f"{DATA_API}/trades", params={"market": cond_id, "limit": 500},
                          headers=H, timeout=TIMEOUT)
        if r.status_code != 200:
            return []
        return r.json() or []
    except Exception:
        return []


def parse_ts(s):
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        return None


def main():
    senales = cargar_senales()
    print(f"Señales GBM_LATE_15M_TARDIO#XRP#15min#BUY_YES resueltas: {len(senales)}\n")

    resultados = []  # (py, t0, t1, acierto, trades)
    for i, row in enumerate(senales, 1):
        py = float(row.get("precio_yes_mercado") or 0)
        if not (0.02 < py < 0.98):
            continue
        t0 = parse_ts(row.get("prediction_timestamp", ""))
        end = parse_ts(row.get("end_date", ""))
        if not t0 or not end:
            continue
        t1 = end - timedelta(minutes=CANCEL_MIN)
        if t1 <= t0:
            continue
        cond_id = conditionId_de(row["market_id"])
        if not cond_id:
            continue
        trades = trades_de(cond_id)
        time.sleep(0.15)
        acierto = row.get("acierto") in ("True", "1")
        resultados.append((py, t0, t1, acierto, trades))
        if i % 20 == 0:
            print(f"  {i}/{len(senales)} procesadas...")

    print(f"\nSeñales con tape recuperado: {len(resultados)}\n")
    print(f"{'MEJORA':>8} {'n_fill':>8} {'fill%':>7} {'EV_maker/señal':>16}")
    print("-" * 45)
    for mejora in MEJORAS:
        n_fill = 0
        pnl_total = 0.0
        for py, t0, t1, acierto, trades in resultados:
            limit = round(py - mejora, 4)
            if limit <= 0.01:
                continue
            filled = False
            for t in trades:
                if t.get("outcome") != "Up":
                    continue
                try:
                    p = float(t.get("price") or 0)
                    tt = datetime.fromtimestamp(int(t["timestamp"]), tz=timezone.utc)
                except Exception:
                    continue
                if p <= limit and t0 <= tt <= t1:
                    filled = True
                    break
            if filled:
                n_fill += 1
                pnl_total += (round(1 / limit - 1, 4) if acierto else -1.0)
        n = len(resultados)
        ev = pnl_total / n if n else 0.0
        print(f"{mejora:>8.3f} {n_fill:>8} {n_fill/n*100 if n else 0:>6.1f}% {ev:>+16.4f}")


if __name__ == "__main__":
    main()
