#!/usr/bin/env python3
"""
analisis_p22_reorientacion_04ago.py — Petición Javi 04-Ago: "haz lo mismo
con P22 y Box Builder [que hiciste con P13], a ver si era cuestión de
reorientación". P22 se refutó con "mejora_detectada" binario (¿cruzó
ratio>=5x en 60s, sí/no?) — aquí se prueba si la MAGNITUD (ratio_max) o
el TIMING (t_mejora_s, cuándo dentro de los 60s) de esa mejora reorienta
el hallazgo, en vez de tratarlo como binario.

Metodología: mismo colapso por señal + cruce contra outcome real que
analisis_p22_cola_posicion_04ago.py, pero desagregando el subconjunto
CON mejora en cuantiles de ratio_max y en buckets de t_mejora_s, para
ver si hay algún corte donde el patrón se invierta o desaparezca.
"""
import csv
import statistics
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
P22 = REPO / "data" / "shadow" / "p22_cola_posicion_fase0.csv"
RESULTS = REPO / "data" / "shadow" / "results.csv"
N_MIN = 15


def _cargar_p22():
    rows = list(csv.DictReader(open(P22, encoding="utf-8")))
    por_combo = {}
    for r in rows:
        clave = (r["market_id"], r["strategy"], r["subtype"], r["direction"])
        if clave not in por_combo or r["veto_timestamp_utc"] < por_combo[clave]["veto_timestamp_utc"]:
            por_combo[clave] = r
    return list(por_combo.values())


def _cargar_outcomes():
    out = {}
    for r in csv.DictReader(open(RESULTS, encoding="utf-8")):
        if r.get("acierto") in ("1", "0"):
            out[(r["strategy"], r["subtype"], r["decision"], r["market_id"])] = int(r["acierto"])
    return out


def _wilson(hit: int, n: int, z: float = 1.645) -> tuple:
    if n == 0:
        return (0.0, 0.0)
    p = hit / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5)
    return ((centro - margen) / denom, (centro + margen) / denom)


def main():
    combos = _cargar_p22()
    outcomes = _cargar_outcomes()

    con_mejora = [c for c in combos if c.get("mejora_detectada") == "1"]
    sin_mejora = [c for c in combos if c.get("mejora_detectada") != "1"]
    print(f"combos únicos: {len(combos)} | con mejora: {len(con_mejora)} | sin mejora: {len(sin_mejora)}\n")

    sin_mejora_hits = [outcomes[(c["strategy"], c["subtype"], c["direction"], c["market_id"])]
                        for c in sin_mejora
                        if (c["strategy"], c["subtype"], c["direction"], c["market_id"]) in outcomes]
    hit_sin = sum(sin_mejora_hits) / len(sin_mejora_hits) if sin_mejora_hits else None
    print(f"baseline SIN mejora: n={len(sin_mejora_hits)} hit={hit_sin*100:.1f}%\n" if hit_sin else "")

    # --- Reorientación 1: magnitud de ratio_max (cuantiles) ---
    con_ratio = [(c, float(c["ratio_max"])) for c in con_mejora if c.get("ratio_max")]
    con_ratio.sort(key=lambda x: x[1])
    n_terciles = len(con_ratio) // 3
    terciles = [con_ratio[:n_terciles], con_ratio[n_terciles:2*n_terciles], con_ratio[2*n_terciles:]]
    nombres = ["ratio_max BAJO (5-", "ratio_max MEDIO", "ratio_max ALTO"]
    print("=== Reorientación 1: por MAGNITUD de la mejora (terciles de ratio_max) ===")
    for nombre, grupo in zip(nombres, terciles):
        if not grupo:
            continue
        lo, hi = grupo[0][1], grupo[-1][1]
        hits = [outcomes[(c["strategy"], c["subtype"], c["direction"], c["market_id"])]
                for c, _ in grupo
                if (c["strategy"], c["subtype"], c["direction"], c["market_id"]) in outcomes]
        if len(hits) >= N_MIN:
            h = sum(hits)
            print(f"  {nombre} [{lo:.1f},{hi:.1f}]: n={len(hits)} hit={100*h/len(hits):.1f}% "
                  f"Wilson90%={_wilson(h, len(hits))}")
        else:
            print(f"  {nombre} [{lo:.1f},{hi:.1f}]: n={len(hits)} (<{N_MIN}, no concluye)")

    # --- Reorientación 2: timing (t_mejora_s, terciles) ---
    con_t = [(c, float(c["t_mejora_s"])) for c in con_mejora if c.get("t_mejora_s")]
    con_t.sort(key=lambda x: x[1])
    n_terciles_t = len(con_t) // 3
    terciles_t = [con_t[:n_terciles_t], con_t[n_terciles_t:2*n_terciles_t], con_t[2*n_terciles_t:]]
    nombres_t = ["t_mejora TEMPRANO", "t_mejora MEDIO", "t_mejora TARDÍO"]
    print("\n=== Reorientación 2: por TIMING de la mejora (terciles de t_mejora_s) ===")
    for nombre, grupo in zip(nombres_t, terciles_t):
        if not grupo:
            continue
        lo, hi = grupo[0][1], grupo[-1][1]
        hits = [outcomes[(c["strategy"], c["subtype"], c["direction"], c["market_id"])]
                for c, _ in grupo
                if (c["strategy"], c["subtype"], c["direction"], c["market_id"]) in outcomes]
        if len(hits) >= N_MIN:
            h = sum(hits)
            print(f"  {nombre} [{lo:.1f}s,{hi:.1f}s]: n={len(hits)} hit={100*h/len(hits):.1f}% "
                  f"Wilson90%={_wilson(h, len(hits))}")
        else:
            print(f"  {nombre} [{lo:.1f}s,{hi:.1f}s]: n={len(hits)} (<{N_MIN}, no concluye)")

    # --- Reorientación 3: cruce magnitud x timing (extremos) ---
    print("\n=== Reorientación 3: extremos combinados ===")
    rapido_y_grande = [c for c, r in con_ratio if float(c.get("t_mejora_s", 999)) <= 10 and r >= 20]
    hits = [outcomes[(c["strategy"], c["subtype"], c["direction"], c["market_id"])]
            for c in rapido_y_grande
            if (c["strategy"], c["subtype"], c["direction"], c["market_id"]) in outcomes]
    if len(hits) >= N_MIN:
        h = sum(hits)
        print(f"  mejora RÁPIDA (<=10s) Y GRANDE (ratio>=20x): n={len(hits)} hit={100*h/len(hits):.1f}% "
              f"Wilson90%={_wilson(h, len(hits))}")
    else:
        print(f"  mejora RÁPIDA Y GRANDE: n={len(hits)} (<{N_MIN}, no concluye)")


if __name__ == "__main__":
    main()
