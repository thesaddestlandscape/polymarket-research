#!/usr/bin/env python3
"""
analisis_p22_cola_posicion_04ago.py — Primer análisis riguroso de
data/shadow/p22_cola_posicion_fase0.csv (n=7639 filas acumuladas desde
29-Jul), petición Javi 04-Ago de retomar el hallazgo de baja latencia y
cerrar el Stage 0 (selección adversa/payout asimétrico).

Pregunta P22: tras un veto por profundidad (motivo_origen=veto_profundidad,
señal REAL ya vetada en producción) o un candidato con libro pobre
(candidato_evaluacion, ratio<5x), si hubiéramos esperado hasta 60s
vigilando el libro, ¿la profundidad se recupera? Y si se recupera,
¿el mercado en ese momento sigue siendo un buen sitio para entrar
(la dirección predicha sigue siendo correcta) o la recuperación de
profundidad llega junto con selección adversa (el precio ya se movió
en contra, mismo problema que el piloto maker estático ya refutado)?

Metodología (CLAUDE.md 3b: colapsar por señal, nunca contar filas):
  1. Colapsa por (market_id, strategy, subtype, direction) -- se queda
     con la PRIMERA fila (veto_timestamp_utc más temprano) por combo, ya
     que reintentos del mismo mercado no son observaciones independientes.
  2. Cruza cada combo contra results.csv (por market_id+strategy+subtype+
     decision) para obtener el outcome real (acierto) de la predicción
     que generó ese veto -- did the underlying signal turn out to be
     right, independent of whether it got filled?
  3. Reporta, separado por motivo_origen (veto_profundidad=real,
     candidato_evaluacion=nunca estuvo en whitelist) y desagregado por
     estrategia:
     - % con mejora_detectada (profundidad recuperada en 60s)
     - t_mejora_s mediana cuando mejora
     - hit-rate del subconjunto CON mejora vs SIN mejora (¿esperar ayuda
       o la mejora llega correlacionada con que el mercado ya perdió el
       edge?)
"""
import csv
import glob
import json
import random
import statistics
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
P22 = REPO / "data" / "shadow" / "p22_cola_posicion_fase0.csv"
RESULTS = REPO / "data" / "shadow" / "results.csv"

N_MIN = 15  # CLAUDE.md: ninguna conclusión con n<15


def _cargar_p22():
    rows = list(csv.DictReader(open(P22, encoding="utf-8")))
    por_combo = {}
    for r in rows:
        clave = (r["market_id"], r["strategy"], r["subtype"], r["direction"])
        if clave not in por_combo or r["veto_timestamp_utc"] < por_combo[clave]["veto_timestamp_utc"]:
            por_combo[clave] = r
    return list(por_combo.values()), len(rows)


def _cargar_outcomes():
    """(strategy, subtype, decision, market_id) -> acierto (1/0)."""
    out = {}
    for r in csv.DictReader(open(RESULTS, encoding="utf-8")):
        if r.get("acierto") in ("1", "0"):
            clave = (r["strategy"], r["subtype"], r["decision"], r["market_id"])
            out[clave] = int(r["acierto"])
    return out


def _wilson(hit: int, n: int, z: float = 1.645) -> tuple:
    if n == 0:
        return (0.0, 0.0)
    p = hit / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5)
    return ((centro - margen) / denom, (centro + margen) / denom)


def _shuffle_p(hits_a: list, hits_b: list, n_shuffle: int = 2000, seed: int = 42) -> float:
    """p-value de permutación para diff de tasas (A-B), two-sided."""
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
    combos, n_filas_crudo = _cargar_p22()
    outcomes = _cargar_outcomes()
    print(f"filas crudas: {n_filas_crudo} | combos únicos (colapsado por señal): {len(combos)}\n")

    for motivo in ("veto_profundidad", "candidato_evaluacion"):
        subset = [c for c in combos if c["motivo_origen"] == motivo]
        print(f"=== motivo_origen={motivo} (n={len(subset)}) ===")

        por_estrategia = defaultdict(list)
        for c in subset:
            por_estrategia[c["strategy"]].append(c)

        for strategy, filas in sorted(por_estrategia.items(), key=lambda kv: -len(kv[1])):
            n = len(filas)
            n_mejora = sum(1 for f in filas if f.get("mejora_detectada") == "1")
            t_mejoras = [float(f["t_mejora_s"]) for f in filas
                         if f.get("mejora_detectada") == "1" and f.get("t_mejora_s")]

            # cruce con outcome real: separar CON mejora vs SIN mejora
            con_mejora_hitlist, sin_mejora_hitlist = [], []
            for f in filas:
                clave = (f["strategy"], f["subtype"], f["direction"], f["market_id"])
                acierto = outcomes.get(clave)
                if acierto is None:
                    continue
                if f.get("mejora_detectada") == "1":
                    con_mejora_hitlist.append(acierto)
                else:
                    sin_mejora_hitlist.append(acierto)
            con_mejora_n, sin_mejora_n = len(con_mejora_hitlist), len(sin_mejora_hitlist)
            con_mejora_hits, sin_mejora_hits = sum(con_mejora_hitlist), sum(sin_mejora_hitlist)

            linea = (f"  {strategy:45s} n={n:4d} mejora={n_mejora:4d} ({100*n_mejora/n:.1f}%)")
            if t_mejoras:
                linea += f"  t_mejora_mediana={statistics.median(t_mejoras):.1f}s"
            print(linea)
            if con_mejora_n >= N_MIN and sin_mejora_n >= N_MIN:
                hit_con = con_mejora_hits / con_mejora_n
                hit_sin = sin_mejora_hits / sin_mejora_n
                w_con = _wilson(con_mejora_hits, con_mejora_n)
                w_sin = _wilson(sin_mejora_hits, sin_mejora_n)
                p_shuffle = _shuffle_p(con_mejora_hitlist, sin_mejora_hitlist)
                print(f"      outcome CON mejora: n={con_mejora_n} hit={hit_con*100:.1f}% Wilson90%={w_con}")
                print(f"      outcome SIN mejora: n={sin_mejora_n} hit={hit_sin*100:.1f}% Wilson90%={w_sin}")
                print(f"      diff={100*(hit_con-hit_sin):+.1f}pp  p_shuffle={p_shuffle:.4f}"
                      f"  {'*** ROBUSTO ***' if p_shuffle < 0.05 and w_con[1] < w_sin[0] else ''}")
            elif con_mejora_n or sin_mejora_n:
                print(f"      outcome (n insuficiente en algún lado, no shuffle): "
                      f"con_mejora n={con_mejora_n} hits={con_mejora_hits} | "
                      f"sin_mejora n={sin_mejora_n} hits={sin_mejora_hits}")
        print()


if __name__ == "__main__":
    main()
