#!/usr/bin/env python3
"""
analisis_sol5min_contrario_riguroso_03ago.py — gate riguroso (Wilson +
shuffle + split-half) sobre la hipótesis CONTRARIA para SOL#5m: si el
lado MAYORITARIO del flujo de ballenas acierta solo 16.3% cuando la
concentración es extrema (>=0.9) en la banda de precio 0.3-0.5 (hallazgo
03-Ago), el lado MINORITARIO debería acertar ~83.7% -- una señal invertida,
no solo "no seguir a las ballenas aquí".

Reusa exactamente la misma muestra/banda que analisis_ballenas_dosis_
respuesta_16jul.py (import directo). Guarda TODOS los buckets de
concentración (no solo alto/bajo) para ver si el efecto contrario es
monótono o solo vive en el extremo.

Solo lectura.
"""
import json
from collections import Counter

import numpy as np

import analisis_ballenas_dosis_respuesta_16jul as dr
from shadow_resolve import fetch_mercados_paralelo, parse_outcome_prices
from smart_money_tracker import trades_de_mercado

COMBO = "SOL#5m"
_rng = np.random.default_rng(20260803)


def _wilson90(k: int, n: int) -> tuple[float, float]:
    if n == 0:
        return (0.0, 0.0)
    z = 1.645
    p = k / n
    denom = 1 + z * z / n
    centro = (p + z * z / (2 * n)) / denom
    margen = (z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5)) / denom
    return (max(0.0, centro - margen), min(1.0, centro + margen))


def _shuffle_vs_mitad(k: int, n: int, iters: int = 20000) -> float:
    """p-valor de que k/n aciertos se deba al azar (moneda justa 50/50)."""
    sims = _rng.binomial(n, 0.5, size=iters)
    obs_dev = abs(k - n / 2)
    return float(np.mean(np.abs(sims - n / 2) >= obs_dev))


def main():
    dr.COMBOS = [COMBO]
    bandas = dr.cargar_bandas()
    lo, hi, rl, rh = bandas[COMBO]
    print(f"Banda SOL#5m: precio [{lo},{hi}) ventana [{rl},{rh}]min")

    seleccion = dr.muestrear_mercados({COMBO: bandas[COMBO]})
    cids = seleccion.get(COMBO, [])
    print(f"Muestra: {len(cids)} mercados")

    mapa_cid_mid = dr.mapear_condition_a_market()

    filas = []  # (cid, pct_mayoria, acierta_mayoria, ts_mercado)
    for i, cid in enumerate(cids):
        mid = mapa_cid_mid.get(cid)
        if mid is None:
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
        if abs(py - 1.0) < 0.01:
            outcome_real = "YES"
        elif abs(pn - 1.0) < 0.01:
            outcome_real = "NO"
        else:
            continue

        trades = trades_de_mercado(cid)
        n_yes = n_no = 0
        for t in trades:
            if (t.get("side") or "").strip().upper() != "BUY":
                continue
            precio_t = t.get("price")
            outcome_t = (t.get("outcome") or "").strip().lower()
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
        acierta_mayoria = int(lado_mayoria == outcome_real)
        filas.append((cid, pct_mayoria, acierta_mayoria, mercado.get("endDate", "")))

        if (i + 1) % 30 == 0:
            print(f"  {i+1}/{len(cids)} procesados...")

    print(f"\nTotal con dato completo: {len(filas)}")

    # Todos los buckets, no solo alto/bajo -- ver si el efecto es monótono
    buckets = [(0.5, 0.6), (0.6, 0.7), (0.7, 0.8), (0.8, 0.9), (0.9, 0.95), (0.95, 1.01)]
    print(f"\n{'bucket':<14}{'n':>5}{'acc_mayoria':>13}{'acc_CONTRARIO':>15}")
    print("-" * 47)
    for blo, bhi in buckets:
        sub = [f for f in filas if blo <= f[1] < bhi]
        if not sub:
            continue
        acc = sum(f[2] for f in sub) / len(sub)
        print(f"[{blo:.2f},{bhi:.2f})".ljust(14) + f"{len(sub):>5}" + f"{acc*100:>12.1f}%" + f"{(1-acc)*100:>14.1f}%")

    # Gate riguroso SOLO sobre el bucket objetivo [0.9,1.0) -- la señal contraria propuesta
    objetivo = [f for f in filas if f[1] >= 0.9]
    n = len(objetivo)
    if n == 0:
        print("\nSin datos en bucket objetivo.")
        return
    k_contrario = sum(1 - f[2] for f in objetivo)  # aciertos del lado MINORITARIO
    hit_contrario = k_contrario / n
    print(f"\n=== GATE RIGUROSO: apostar el lado MINORITARIO cuando concentración>=0.9 ===")
    print(f"n={n}, hit_contrario={hit_contrario*100:.1f}%")
    if n < 15:
        print(f"⚠️ n={n} < 15 -- EXPLORATORIO, no concluir nada todavía.")

    lo90, hi90 = _wilson90(int(k_contrario), n)
    print(f"Wilson90% = [{lo90*100:.1f}%, {hi90*100:.1f}%]")
    p_shuffle = _shuffle_vs_mitad(int(k_contrario), n)
    print(f"shuffle p-valor (vs moneda justa 50%) = {p_shuffle:.4f}")

    if n >= 8:
        orden = sorted(objetivo, key=lambda f: f[3] or f[0])  # por fecha si hay, si no por cid
        mitad = n // 2
        m1 = orden[:mitad]
        m2 = orden[mitad:]
        acc1 = sum(1 - f[2] for f in m1) / len(m1)
        acc2 = sum(1 - f[2] for f in m2) / len(m2)
        print(f"split-half (por orden temporal aprox): 1ª mitad={acc1*100:.1f}% (n={len(m1)}) "
              f"| 2ª mitad={acc2*100:.1f}% (n={len(m2)})")
        consistente = (acc1 > 0.5) == (acc2 > 0.5)
        print(f"{'consistente (ambas >50%)' if consistente else 'INCONSISTENTE'}")


if __name__ == "__main__":
    main()
