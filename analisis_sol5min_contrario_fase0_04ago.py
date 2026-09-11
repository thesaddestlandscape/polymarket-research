#!/usr/bin/env python3
"""
analisis_sol5min_contrario_fase0_04ago.py — Cruza
data/shadow/sol5min_contrario_fase0.csv contra el outcome oficial real
(gamma-api, vía shadow_resolve.fetch_mercados_paralelo) para responder
la pregunta que dejó pendiente idea_sol5min_estrategia_contraria_
confirmada_03ago: el hallazgo retrospectivo (82.6% hit, n=46) ¿replica en
datos forward?

Reporta también fill-ability (ratio_vs_stake del lado minoritario, ya
capturado en muestras_json) cruzado con el outcome, para ver si el
fill-ability correlaciona con acierto (mismo patrón que P22) o no.

Resultado 04-Ago (primera corrida, n=63/64, TODAS las filas de ese día):
NO replica -- hit=47.6% (Wilson90%=[37.6%,57.9%]), no se solapa con el
original [71.7%,89.9%]. Ver idea_sol5min_contrario_no_replica_forward_04ago.
Re-ejecutar cuando el CSV acumule más días.
"""
import csv
import json
import random
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

CSV_PATH = REPO / "data" / "shadow" / "sol5min_contrario_fase0.csv"
N_MIN = 15


def _wilson(hit: int, n: int, z: float = 1.645) -> tuple:
    if n == 0:
        return (0.0, 0.0)
    p = hit / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5)
    return ((centro - margen) / denom, (centro + margen) / denom)


def _shuffle_p(hits_a: list, hits_b: list, n_shuffle: int = 2000, seed: int = 42) -> float | None:
    if not hits_a or not hits_b:
        return None
    obs = (sum(hits_a) / len(hits_a)) - (sum(hits_b) / len(hits_b))
    todos = hits_a + hits_b
    n_a = len(hits_a)
    rng = random.Random(seed)
    extremos = 0
    for _ in range(n_shuffle):
        rng.shuffle(todos)
        diff = (sum(todos[:n_a]) / n_a) - (sum(todos[n_a:]) / len(todos[n_a:]))
        if abs(diff) >= abs(obs):
            extremos += 1
    return extremos / n_shuffle


def main():
    from shadow_resolve import fetch_mercados_paralelo, parse_outcome_prices

    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8")))
    print(f"filas totales: {len(rows)}")
    print(f"rango de fechas: {min(r['ts_deteccion_utc'] for r in rows)} .. "
          f"{max(r['ts_deteccion_utc'] for r in rows)}")
    pcts = [float(r["pct_mayoria_detectado"]) for r in rows]
    print(f"pct_mayoria_detectado: min={min(pcts):.2f} max={max(pcts):.2f} "
          f"(debe ser todo >=0.9, criterio de detección)\n")

    market_ids = [r["market_id"] for r in rows]
    resueltos = fetch_mercados_paralelo(market_ids, workers=5)

    hits_todos = []
    fillable_inicial_hits, fillable_tarde_hits, no_fillable_hits = [], [], []
    n_sin_resolucion = 0

    for r in rows:
        mkt = resueltos.get(r["market_id"])
        if not mkt:
            n_sin_resolucion += 1
            continue
        precios = parse_outcome_prices(mkt.get("outcomePrices"))
        if not precios or len(precios) < 2:
            n_sin_resolucion += 1
            continue
        py, pn = float(precios[0]), float(precios[1])
        if abs(py - 1.0) < 0.01:
            outcome = "YES"
        elif abs(pn - 1.0) < 0.01:
            outcome = "NO"
        else:
            n_sin_resolucion += 1
            continue

        gano = 1 if outcome == r["lado_minoria"] else 0
        hits_todos.append(gano)

        muestras = json.loads(r["muestras_json"])
        ratios = [m[1] for m in muestras if m[1] is not None]
        if not ratios:
            no_fillable_hits.append(gano)
        elif ratios[0] >= 5.0:
            fillable_inicial_hits.append(gano)
        elif max(ratios) >= 5.0:
            fillable_tarde_hits.append(gano)
        else:
            no_fillable_hits.append(gano)

    n = len(hits_todos)
    h = sum(hits_todos)
    print(f"resueltos: {n} | sin resolución: {n_sin_resolucion}\n")
    print(f"TODOS: n={n} hit={100*h/n:.1f}% Wilson90%={_wilson(h, n)}")
    print("  (referencia retrospectiva 03-Ago: n=46 hit=82.6% Wilson90%="
          f"{_wilson(38, 46)})\n")

    for nombre, lst in (("fillable INICIAL (ratio>=5x al detectar)", fillable_inicial_hits),
                         ("fillable TARDE (ratio>=5x solo después)", fillable_tarde_hits),
                         ("NUNCA fillable en la ventana", no_fillable_hits)):
        if lst:
            hh = sum(lst)
            print(f"{nombre}: n={len(lst)} hit={100*hh/len(lst):.1f}% "
                  f"Wilson90%={_wilson(hh, len(lst)) if len(lst) >= N_MIN else '(n<15)'}")

    if len(fillable_inicial_hits) >= N_MIN and (len(fillable_tarde_hits) + len(no_fillable_hits)) >= N_MIN:
        resto = fillable_tarde_hits + no_fillable_hits
        p = _shuffle_p(fillable_inicial_hits, resto)
        print(f"\np_shuffle (fillable_inicial vs resto): {p:.4f}")


if __name__ == "__main__":
    main()
