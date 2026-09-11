#!/usr/bin/env python3
"""
analisis_p22_senal_contraria_04ago.py — Petición Javi 04-Ago: "¿algo de
P22/Box Builder que podamos usar atendiendo a los nuevos descubrimientos?"

Box Builder: probado (ver idea_box_builder_refutado_profundidad_cero_04ago)
el ángulo "comprar solo el lado profundo como apuesta direccional, sin
exigir arbitraje completo" -- n=63, hit=50.8%, ask medio=0.523,
edge=-1.5pp. Sin edge, confirmado muerto también por este ángulo.

P22: la reorientación por MAGNITUD (analisis_p22_reorientacion_04ago.py)
ya mostró dosis-respuesta monótona (más recuperación de profundidad =
peor acierto de la dirección ORIGINAL). Este script empuja esa cola hasta
el extremo: si el acierto de la dirección original cae POR DEBAJO de 50%
de forma significativa, la recuperación extrema de profundidad es una
señal CONTRARIA explotable (apostar lo opuesto a la señal vetada), no
solo "esperar no ayuda".

Resultado (n=301, ratio_max>=1000): hit=39.5% (dirección original),
p_shuffle=0.0007 vs 50%. Dominado por FAVORITO_CONFIRMADO (n=171,
hit=32.2%, Wilson90%=[26.6%,38.3%], split-half 31.4%/32.9% -- muy
estable). Sin verificar todavía: fill-ability del lado CONTRARIO (este
dataset solo trackea profundidad del lado ORIGINAL vetado, no del
opuesto) -- pendiente antes de que esto sea accionable.
"""
import csv
import random
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
P22 = REPO / "data" / "shadow" / "p22_cola_posicion_fase0.csv"
RESULTS = REPO / "data" / "shadow" / "results.csv"
RATIO_MAX_UMBRAL = 1000.0
N_MIN = 15


def _wilson(hit: int, n: int, z: float = 1.645) -> tuple:
    if n == 0:
        return (0.0, 0.0)
    p = hit / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5)
    return ((centro - margen) / denom, (centro + margen) / denom)


def main():
    rows = list(csv.DictReader(open(P22, encoding="utf-8")))
    por_combo = {}
    for r in rows:
        clave = (r["market_id"], r["strategy"], r["subtype"], r["direction"])
        if clave not in por_combo or r["veto_timestamp_utc"] < por_combo[clave]["veto_timestamp_utc"]:
            por_combo[clave] = r
    combos = list(por_combo.values())

    outcomes = {}
    for r in csv.DictReader(open(RESULTS, encoding="utf-8")):
        if r.get("acierto") in ("1", "0"):
            outcomes[(r["strategy"], r["subtype"], r["decision"], r["market_id"])] = int(r["acierto"])

    extremo = [c for c in combos if c.get("mejora_detectada") == "1" and c.get("ratio_max")
               and float(c["ratio_max"]) >= RATIO_MAX_UMBRAL]
    hits = [outcomes[(c["strategy"], c["subtype"], c["direction"], c["market_id"])]
            for c in extremo if (c["strategy"], c["subtype"], c["direction"], c["market_id"]) in outcomes]
    n, h = len(hits), sum(hits)
    print(f"ratio_max>={RATIO_MAX_UMBRAL:.0f}: n={n} hit_direccion_original={100*h/n:.1f}% "
          f"Wilson90%={_wilson(h, n)}")

    rng = random.Random(42)
    obs = h / n - 0.5
    extremos = sum(1 for _ in range(3000)
                   if abs(sum(1 for _ in range(n) if rng.random() < 0.5) / n - 0.5) >= abs(obs))
    print(f"p_shuffle vs 50% (moneda justa): {extremos/3000:.4f}\n")

    print("desagregado por estrategia:")
    por_estrategia = defaultdict(list)
    for c in extremo:
        clave = (c["strategy"], c["subtype"], c["direction"], c["market_id"])
        if clave in outcomes:
            por_estrategia[c["strategy"]].append(outcomes[clave])
    for est, hs in sorted(por_estrategia.items(), key=lambda kv: -len(kv[1])):
        ne, he = len(hs), sum(hs)
        w = _wilson(he, ne) if ne >= N_MIN else None
        print(f"  {est:45s} n={ne:4d} hit={100*he/ne:5.1f}%" +
              (f"  Wilson90%={w}" if w else "  (n<15)"))


if __name__ == "__main__":
    main()
