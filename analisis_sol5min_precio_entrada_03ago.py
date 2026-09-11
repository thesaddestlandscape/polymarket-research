#!/usr/bin/env python3
"""
analisis_sol5min_precio_entrada_03ago.py — aproxima el precio de entrada
real del lado MINORITARIO en la estrategia contraria de SOL#5min (ver
idea_sol5min_estrategia_contraria_confirmada_03ago), cruzando los mercados
del bucket objetivo (concentración>=0.9, banda 0.3-0.5) contra
libro_ambos_lados_YYYY-MM-DD.csv (captura real de ask_yes/ask_no, 01 a
03-Ago) en el momento aproximado en que la banda de ballenas opera
(rest_lo_min/rest_hi_min de ballenas_timing_state.json).

Preliminar por diseño: solo cubre los mercados que caen en la ventana de 3
días capturada por libro_ambos_lados -- no todo el histórico usado en el
gate riguroso. Sirve para una primera lectura del payout, no como gate
final.

Solo lectura.
"""
import csv
import glob
from collections import Counter
from datetime import datetime, timedelta, timezone

import analisis_ballenas_dosis_respuesta_16jul as dr
from shadow_resolve import fetch_mercados_paralelo, parse_outcome_prices
from smart_money_tracker import trades_de_mercado

COMBO = "SOL#5m"
LIBRO_FILES = sorted(glob.glob("/root/polymarket-research-datalogs/libro_ambos_lados_*.csv"))[-3:]


def cargar_libro_por_mercado():
    por_mid = {}
    for path in LIBRO_FILES:
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                por_mid.setdefault(row["market_id"], []).append(row)
    for mid in por_mid:
        por_mid[mid].sort(key=lambda r: r["timestamp_utc"])
    return por_mid


def main():
    dr.COMBOS = [COMBO]
    bandas = dr.cargar_bandas()
    lo, hi, rl, rh = bandas[COMBO]
    rest_medio_s = (rl + rh) / 2 * 60

    seleccion = dr.muestrear_mercados({COMBO: bandas[COMBO]})
    cids = seleccion.get(COMBO, [])
    mapa_cid_mid = dr.mapear_condition_a_market()
    libro_por_mid = cargar_libro_por_mercado()
    print(f"Mercados con libro_ambos_lados capturado (últimos 3 días): {len(libro_por_mid)} en total")

    resultados = []
    for cid in cids:
        mid = mapa_cid_mid.get(cid)
        if mid is None or mid not in libro_por_mid:
            continue
        resueltos = fetch_mercados_paralelo([mid], workers=1)
        mercado = resueltos.get(mid)
        if not mercado:
            continue
        precios = parse_outcome_prices(mercado.get("outcomePrices"))
        if not precios or len(precios) < 2:
            continue
        try:
            py, pn = float(precios[0]), float(precios[1])
        except (ValueError, TypeError):
            continue
        outcome_real = "YES" if abs(py - 1.0) < 0.01 else ("NO" if abs(pn - 1.0) < 0.01 else None)
        if outcome_real is None:
            continue

        trades = trades_de_mercado(cid)
        n_yes = n_no = 0
        for t in trades:
            if (t.get("side") or "").strip().upper() != "BUY":
                continue
            precio_t, outcome_t = t.get("price"), (t.get("outcome") or "").strip().lower()
            if precio_t is None or outcome_t not in ("up", "down", "yes", "no"):
                continue
            try:
                precio_t = float(precio_t)
            except (ValueError, TypeError):
                continue
            if not (lo <= precio_t < hi):
                continue
            if outcome_t in ("up", "yes"):
                n_yes += 1
            else:
                n_no += 1
        n = n_yes + n_no
        if n < dr.MIN_TRADES_MERCADO:
            continue
        pct_yes = n_yes / n
        lado_mayoria = "YES" if pct_yes >= 0.5 else "NO"
        pct_mayoria = max(pct_yes, 1 - pct_yes)
        if pct_mayoria < 0.9:
            continue
        lado_minoria = "NO" if lado_mayoria == "YES" else "YES"
        acierta_contrario = int(lado_minoria == outcome_real)

        # buscar el tick de libro_ambos_lados más cercano a "rest_medio_s"
        # restante antes del cierre
        end_dt = None
        try:
            end_str = mercado.get("endDate", "")
            end_dt = datetime.fromisoformat(end_str.replace("Z", "+00:00"))
        except Exception:
            pass
        if end_dt is None:
            continue
        objetivo_ts = end_dt - timedelta(seconds=rest_medio_s)
        mejor = None
        mejor_diff = None
        for row in libro_por_mid[mid]:
            try:
                ts = datetime.fromisoformat(row["timestamp_utc"].replace("Z", "+00:00"))
            except Exception:
                continue
            diff = abs((ts - objetivo_ts).total_seconds())
            if mejor_diff is None or diff < mejor_diff:
                mejor_diff = diff
                mejor = row
        if mejor is None or mejor_diff > 90:
            continue
        try:
            ask_minoria = float(mejor["ask_yes"]) if lado_minoria == "YES" else float(mejor["ask_no"])
        except (ValueError, TypeError, KeyError):
            continue

        resultados.append((mid, lado_minoria, ask_minoria, acierta_contrario, mejor_diff))

    print(f"\nMercados con precio de libro real cerca del momento de señal: {len(resultados)}")
    if not resultados:
        return
    for mid, lado, ask, acierta, diff in resultados:
        print(f"  mid={mid} lado_minoria={lado} ask={ask:.3f} acierta={'SI' if acierta else 'no'} "
              f"(diff_tiempo={diff:.0f}s)")

    precios = [r[2] for r in resultados]
    print(f"\nprecio medio de entrada (lado minoritario): {sum(precios)/len(precios):.3f}")
    print(f"precio min/max: {min(precios):.3f} / {max(precios):.3f}")
    n_ok = sum(r[3] for r in resultados)
    print(f"hit rate en este subconjunto (n={len(resultados)}): {n_ok/len(resultados)*100:.1f}%")


if __name__ == "__main__":
    main()
