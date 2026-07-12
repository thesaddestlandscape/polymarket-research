#!/usr/bin/env python3
"""¿Escalonar la entrada (dividir el stake en 2-3 intentos a distintos
momentos de la ventana tardía) mejora el precio medio de ejecución frente
al FOK único actual? Tarea #5 de la lista de soluciones (12-Jul).

Método (mismo patrón conservador que maker_sim.py/nested_arb_scanner.py):
para una muestra de señales live REALES ya resueltas (GBM_LATE_15M SOL/ETH
BUY_YES), se reconstruye el tape público (data-api/trades) alrededor de la
ejecución real. Se simulan 3 sub-órdenes iguales del mismo stake total en
t0 (momento real de la señal), t0+30s, t0+60s: cada una se "llena" al precio
del primer print real en el lado nuestro (Up) que aparezca en una ventana de
±20s alrededor de su sub-momento -- si no hay print, esa sub-orden no se
llena (mismo riesgo de fallo que un FOK real). Se compara el precio medio
ponderado del TWAP simulado contra el precio de entrada REAL (FOK único).

Solo lectura, no toca dinero ni coloca ninguna orden.
"""
import csv
import sys
import time
from datetime import datetime, timedelta, timezone

import requests

H = {"User-Agent": "Mozilla/5.0 (compatible; polymarket-research/1.0)"}
GAMMA = "https://gamma-api.polymarket.com"
DATA_API = "https://data-api.polymarket.com"
TIMEOUT = 10
SUBORDENES_OFFSETS_S = [0, 30, 60]
VENTANA_MATCH_S = 20
N_MUESTRA = 30


def _condition_id(market_id):
    try:
        r = requests.get(f"{GAMMA}/markets/{market_id}", headers=H, timeout=TIMEOUT)
        d = r.json() if r.status_code == 200 else None
        if isinstance(d, list) and d:
            d = d[0]
        return d.get("conditionId") if isinstance(d, dict) else None
    except Exception:
        return None


def _trades(cond_id):
    try:
        r = requests.get(f"{DATA_API}/trades", params={"market": cond_id, "limit": 200},
                          headers=H, timeout=TIMEOUT)
        return r.json() if r.status_code == 200 else []
    except Exception:
        return []


def main():
    trades = list(csv.DictReader(open("data/live/trades.csv", encoding="utf-8")))
    muestra = [t for t in trades if t["strategy"] == "GBM_LATE_15M" and t["direction"] == "BUY_YES"
               and t["subtype"] in ("SOL#15min", "ETH#15min") and t["status"] == "CLOSED"
               and "maker_pilot=1" not in t["notas"]][-N_MUESTRA:]

    print(f"Muestra: {len(muestra)} trades reales (últimos {N_MUESTRA})\n")

    resultados = []
    for i, t in enumerate(muestra, 1):
        mid = t["market_id"]
        try:
            ts0 = datetime.fromisoformat(t["timestamp_utc"].replace("Z", "+00:00"))
            precio_real = float(t["entry_price"])
        except Exception:
            continue
        cid = _condition_id(mid)
        if not cid:
            continue
        tape = _trades(cid)
        time.sleep(0.15)

        precios_chunk = []
        for off in SUBORDENES_OFFSETS_S:
            t_target = ts0 + timedelta(seconds=off)
            candidatos = []
            for x in tape:
                try:
                    tt = datetime.fromtimestamp(x["timestamp"], tz=timezone.utc)
                except Exception:
                    continue
                if x.get("outcome") != "Up":
                    continue
                if abs((tt - t_target).total_seconds()) <= VENTANA_MATCH_S:
                    candidatos.append((abs((tt - t_target).total_seconds()), float(x["price"])))
            if candidatos:
                candidatos.sort()
                precios_chunk.append(candidatos[0][1])
            # si no hay print, esa sub-orden no se llena (None implícito, se excluye del promedio)

        if not precios_chunk:
            continue
        precio_twap = sum(precios_chunk) / len(precios_chunk)
        fill_rate_twap = len(precios_chunk) / len(SUBORDENES_OFFSETS_S)
        resultados.append({
            "market_id": mid, "precio_real_fok": precio_real,
            "precio_twap": round(precio_twap, 4), "chunks_llenados": len(precios_chunk),
            "fill_rate_twap": fill_rate_twap,
            "mejora_pct": round((precio_real - precio_twap) / precio_real * 100, 2),
        })
        if i % 10 == 0:
            print(f"  {i}/{len(muestra)} procesados...")

    print(f"\nSeñales con tape reconstruido: {len(resultados)}\n")
    if not resultados:
        return

    mejor_en_twap = sum(1 for r in resultados if r["precio_twap"] < r["precio_real_fok"])
    peor_en_twap = sum(1 for r in resultados if r["precio_twap"] > r["precio_real_fok"])
    igual = len(resultados) - mejor_en_twap - peor_en_twap
    mejora_media = sum(r["mejora_pct"] for r in resultados) / len(resultados)
    fill_medio = sum(r["fill_rate_twap"] for r in resultados) / len(resultados)
    fill_100 = sum(1 for r in resultados if r["fill_rate_twap"] == 1.0)

    print(f"TWAP mejor precio: {mejor_en_twap}/{len(resultados)}")
    print(f"TWAP peor precio:  {peor_en_twap}/{len(resultados)}")
    print(f"Igual:             {igual}/{len(resultados)}")
    print(f"Mejora media de precio: {mejora_media:+.2f}% (positivo = TWAP más barato que FOK real)")
    print(f"Fill-rate medio de las 3 sub-órdenes: {fill_medio:.1%}")
    print(f"Señales con las 3 sub-órdenes llenas (100%): {fill_100}/{len(resultados)}")


if __name__ == "__main__":
    sys.exit(main())
