#!/usr/bin/env python3
"""Read-only: gate riguroso (Wilson 90% + split-half) sobre
resolution_sniper_observer.py -- retoma el hallazgo de titular engañoso
del 29-Jul (idea/project_auditoria_observacional_29jul): el 96-100%
agregado no sobrevive al restringir al subconjunto accionable
(chainlink_direccion_implicita presente, offset temprano). Corre sobre
las 3 fechas acumuladas de data/shadow/resolution_sniper_obs_*.csv,
segmentado por (activo, marco, offset_s) -- nunca agregado, ver CLAUDE.md
punto 17. Solo lectura, no toca ningún gate real.

Correr desde la raíz del repo: python3 analisis_gate_riguroso_resolution_sniper_30jul.py
"""
import csv
import glob
import math
import random
from collections import defaultdict

Z_90 = 1.645
N_MIN = 15
N_SHUFFLE = 2000


def wilson_lower(hits: int, n: int, z: float = Z_90) -> float:
    if n == 0:
        return 0.0
    p = hits / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centro - margen) / denom


def cargar():
    filas = []
    for fn in sorted(glob.glob("data/shadow/resolution_sniper_obs_*.csv")):
        with open(fn, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if not r.get("chainlink_direccion_implicita"):
                    continue
                try:
                    offset = int(float(r["offset_s"]))
                except (ValueError, KeyError):
                    continue
                direccion = r["chainlink_direccion_implicita"]
                ask = r.get("ask_yes") if direccion == "Up" else r.get("ask_no")
                try:
                    ask = float(ask)
                except (TypeError, ValueError):
                    continue
                acierto = r.get("acierto_direccion_implicita") in ("1", "True", "true")
                filas.append({
                    "activo": r["activo"], "marco": r["marco"], "offset": offset,
                    "ask": ask, "acierto": acierto, "ts": r["timestamp_utc"],
                })
    return filas


def main():
    filas = cargar()
    print(f"Filas accionables totales (direccion_implicita presente): {len(filas)}")

    # Segmentado por (activo, marco, offset) -- solo offsets tempranos
    # (entrada antes/justo al cierre nominal, offset<=2s) son "accionables"
    # de verdad; offsets tardíos ya tienen el precio resuelto (ask~0.99).
    grupos = defaultdict(list)
    for f in filas:
        if f["offset"] <= 2:
            grupos[(f["activo"], f["marco"], f["offset"])].append(f)

    print(f"\n{'activo':<6}{'marco':<7}{'offset':>7}{'n':>6}{'hit%':>8}{'wilson90lo':>12}{'ask_medio':>11}{'edge':>8}{'split1':>8}{'split2':>8}")
    resultados = []
    for (activo, marco, offset), grupo in sorted(grupos.items()):
        n = len(grupo)
        if n < N_MIN:
            continue
        hits = sum(1 for g in grupo if g["acierto"])
        hit_rate = hits / n
        wlo = wilson_lower(hits, n)
        ask_medio = sum(g["ask"] for g in grupo) / n
        edge = hit_rate - ask_medio  # gap entre acierto real y lo que "sabe" el precio

        grupo_ordenado = sorted(grupo, key=lambda g: g["ts"])
        mitad = len(grupo_ordenado) // 2
        h1 = grupo_ordenado[:mitad]
        h2 = grupo_ordenado[mitad:]
        hit1 = sum(1 for g in h1 if g["acierto"]) / len(h1) if h1 else 0
        hit2 = sum(1 for g in h2 if g["acierto"]) / len(h2) if h2 else 0

        print(f"{activo:<6}{marco:<7}{offset:>7}{n:>6}{hit_rate*100:>7.1f}%{wlo:>12.3f}{ask_medio:>11.3f}{edge:>+8.3f}{hit1*100:>7.1f}%{hit2*100:>7.1f}%")
        resultados.append({
            "activo": activo, "marco": marco, "offset": offset, "n": n,
            "hit_rate": hit_rate, "wilson90_lo": wlo, "ask_medio": ask_medio,
            "edge": edge, "split1": hit1, "split2": hit2,
        })

    # Shuffle control: sobre el subconjunto accionable completo, ¿el edge
    # medio (hit_rate - ask_medio) observado supera lo que daría un
    # ACIERTO ALEATORIO real (Bernoulli 0.5 fresco cada tirada)? OJO: un
    # random.shuffle() sobre la lista de aciertos NO sirve -- permuta el
    # ORDEN pero deja el CONTEO total de aciertos intacto (es una lista
    # fija de True/False), así que sum(aciertos) da SIEMPRE el mismo
    # resultado y el control queda inerte (encontrado en la propia
    # verificación de este script, corregido antes de reportar nada).
    accionables = [f for f in filas if f["offset"] <= 2]
    if accionables:
        n_acc = len(accionables)
        ask_medio_global = sum(f["ask"] for f in accionables) / n_acc
        edge_real = sum(1 for f in accionables if f["acierto"]) / n_acc - ask_medio_global
        random.seed(42)
        mayor_igual = 0
        for _ in range(N_SHUFFLE):
            hit_shuf = sum(random.random() < 0.5 for _ in range(n_acc)) / n_acc
            edge_shuf = hit_shuf - ask_medio_global
            if edge_shuf >= edge_real:
                mayor_igual += 1
        p_shuffle = mayor_igual / N_SHUFFLE
        print(f"\nShuffle control (agregado offset<=2s, n={n_acc}): "
              f"edge_real={edge_real:+.4f} p_shuffle={p_shuffle:.4f}")

    print("\nGATE: n>=15, Wilson90_lo>0.5 (mejor que azar con margen), "
          "edge>0 (paga más de lo que el precio ya refleja), split-half consistente.")
    gate_ok = [r for r in resultados if r["wilson90_lo"] > 0.5 and r["edge"] > 0
               and abs(r["split1"] - r["split2"]) < 0.30]
    print(f"Combos que pasan GATE OK: {len(gate_ok)} de {len(resultados)} evaluados (n>=15)")
    for r in gate_ok:
        print(f"  {r['activo']}#{r['marco']}#offset={r['offset']}: "
              f"n={r['n']} hit={r['hit_rate']*100:.1f}% wilson90lo={r['wilson90_lo']:.3f} edge={r['edge']:+.3f}")


if __name__ == "__main__":
    main()
