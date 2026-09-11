#!/usr/bin/env python3
"""
analisis_log_growth_zona_twap_10ago.py -- Pendiente #1 checkpoint 10-Ago.

Repite el gate de crecimiento logaritmico (analisis_log_growth.py) para
BALLENAS_TARDIAS#BTC#15min#BUY_YES y
FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min#BUY_YES, pero:
  - restringido a las zonas de precio ya confirmadas hoy en
    zonas_validadas_externas.json (bueno_confirmado), NO al agregado
    completo de la tupla (eso fue lo que dio g<0 el 03-Ago/07-Ago).
  - restringido a resoluciones con prediction_timestamp >= 2026-08-07
    (post-TWAP, mismo criterio que gate_bucket_propio tras el fix de
    esta sesion) para no mezclar regimen pre/post-TWAP.

No escribe nada, no toca dinero -- solo lee results.csv/zonas_validadas.
"""
import csv
import json
import math
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data" / "shadow" / "results.csv"
ZONAS = REPO / "data" / "shadow" / "zonas_validadas_externas.json"
SLIPPAGE = 0.02
N_MIN = 15
CORTE_TWAP = datetime(2026, 8, 7, tzinfo=timezone.utc)

OBJETIVOS = [
    ("BALLENAS_TARDIAS", "BTC#15min", "BUY_YES"),
    ("FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION", "ETH#15min", "BUY_YES"),
]


def _retorno(row):
    p = min(0.99, max(0.01, float(row["precio_yes_mercado"])))
    if row["decision"] == "BUY_NO":
        p = 1 - p
    if row["acierto"] == "1":
        return (1 - p) / p - SLIPPAGE
    return -1 - SLIPPAGE


def _en_zona(precio, zonas):
    return any(lo <= precio < hi for lo, hi in zonas)


def _parse_ts(s):
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


def main():
    zonas_json = json.loads(ZONAS.read_text())
    f = 0.10

    print(f"{'tupla':70s} {'n':>5s} {'hit%':>6s} {'EV/$':>7s} {'g(f=10%)':>10s}  gate")
    for strategy, subtype, decision in OBJETIVOS:
        clave = f"{strategy}#{subtype}#{decision}"
        zonas = zonas_json.get(clave, {}).get("zonas_bueno_confirmado", [])
        if not zonas:
            print(f"{clave:70s}  -- sin zonas_bueno_confirmado en zonas_validadas_externas.json")
            continue

        filas = []
        with open(RESULTS, encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                if r["strategy"] != strategy or r["subtype"] != subtype or r["decision"] != decision:
                    continue
                if r.get("acierto") not in ("0", "1"):
                    continue
                ts = _parse_ts(r.get("prediction_timestamp", ""))
                if ts is None or ts < CORTE_TWAP:
                    continue
                try:
                    precio = float(r["precio_yes_mercado"])
                except (TypeError, ValueError):
                    continue
                if not _en_zona(precio, zonas):
                    continue
                filas.append(r)

        n = len(filas)
        if n == 0:
            print(f"{clave:70s}   n=0  -- sin resoluciones post-TWAP en zona confirmada {zonas}")
            continue
        rs = [_retorno(r) for r in filas]
        hit = 100 * sum(1 for r in filas if r["acierto"] == "1") / n
        ev = sum(rs) / n
        g = sum(math.log(1 + f * x) for x in rs) / n
        pasa = n >= N_MIN and g > 0
        flag = "PASA" if pasa else ("NO -- payout inverso" if n >= N_MIN else "NO -- n<15, sin concluir")
        print(f"{clave:70s} {n:5d} {hit:5.1f}% {ev:+7.3f} {g:+10.5f}  {flag}   zonas={zonas}")


if __name__ == "__main__":
    main()
