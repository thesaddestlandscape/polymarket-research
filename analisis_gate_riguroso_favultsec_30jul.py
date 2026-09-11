#!/usr/bin/env python3
"""Read-only: gate riguroso (Wilson 90% + shuffle + split-half) sobre
favorito_ultimosegundo_5min.py (screen favultsec) -- FAVORITO_CONFIRMADO en
el instante T-10s de XRP/DOGE/BNB#5min. Acumula las 3 fechas disponibles de
data/shadow/favorito_ultimosegundo_*.csv, segmentado por activo (CLAUDE.md
punto 17). best_ask ya es el precio del lado CORRECTO (bug de lado
equivocado corregido 29-Jul, ver project_analisis_4_piezas_
observacionales_29jul) -- usable directo como precio pagado/breakeven.
Solo lectura, no toca ningún gate real.

Correr desde la raíz del repo: python3 analisis_gate_riguroso_favultsec_30jul.py
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
    for fn in sorted(glob.glob("data/shadow/favorito_ultimosegundo_*.csv")):
        with open(fn, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r.get("outcome_real") in (None, "") or r.get("acierto") in (None, ""):
                    continue  # sin resolver todavía
                try:
                    ask = float(r["best_ask"])
                except (TypeError, ValueError):
                    continue
                acierto = r["acierto"] in ("1", "True", "true")
                filas.append({
                    "activo": r["activo"], "direccion": r["direccion"],
                    "ask": ask, "acierto": acierto, "ts": r["timestamp_utc"],
                })
    return filas


def evaluar(filas, etiqueta):
    print(f"\n=== {etiqueta} (n total resuelto: {len(filas)}) ===")
    grupos = defaultdict(list)
    for f in filas:
        grupos[f["activo"]].append(f)

    print(f"{'activo':<6}{'n':>6}{'hit%':>8}{'wilson90lo':>12}{'ask_medio':>11}{'edge':>8}{'split1':>8}{'split2':>8}")
    resultados = []
    for activo, grupo in sorted(grupos.items()):
        n = len(grupo)
        if n < N_MIN:
            print(f"{activo:<6}{n:>6}  (n<{N_MIN}, sin concluir)")
            continue
        hits = sum(1 for g in grupo if g["acierto"])
        hit_rate = hits / n
        wlo = wilson_lower(hits, n)
        ask_medio = sum(g["ask"] for g in grupo) / n
        edge = hit_rate - ask_medio

        grupo_ordenado = sorted(grupo, key=lambda g: g["ts"])
        mitad = len(grupo_ordenado) // 2
        h1, h2 = grupo_ordenado[:mitad], grupo_ordenado[mitad:]
        hit1 = sum(1 for g in h1 if g["acierto"]) / len(h1) if h1 else 0
        hit2 = sum(1 for g in h2 if g["acierto"]) / len(h2) if h2 else 0

        print(f"{activo:<6}{n:>6}{hit_rate*100:>7.1f}%{wlo:>12.3f}{ask_medio:>11.3f}{edge:>+8.3f}{hit1*100:>7.1f}%{hit2*100:>7.1f}%")
        resultados.append({"activo": activo, "n": n, "hit_rate": hit_rate, "wilson90_lo": wlo,
                            "ask_medio": ask_medio, "edge": edge, "split1": hit1, "split2": hit2})

    if filas:
        # OJO: random.shuffle() sobre la lista de aciertos NO es un control
        # válido -- permuta el orden pero el CONTEO total de True/False no
        # cambia, así que sum(aciertos) da siempre el mismo valor y el
        # p_shuffle queda inerte (bug encontrado y corregido en la propia
        # verificación de este script). Control real: Bernoulli(0.5) fresco
        # cada tirada.
        n_f = len(filas)
        ask_medio_global = sum(f["ask"] for f in filas) / n_f
        edge_real = sum(1 for f in filas if f["acierto"]) / n_f - ask_medio_global
        random.seed(42)
        mayor_igual = 0
        for _ in range(N_SHUFFLE):
            hit_shuf = sum(random.random() < 0.5 for _ in range(n_f)) / n_f
            edge_shuf = hit_shuf - ask_medio_global
            if edge_shuf >= edge_real:
                mayor_igual += 1
        p_shuffle = mayor_igual / N_SHUFFLE
        print(f"\nShuffle control (agregado, n={n_f}): edge_real={edge_real:+.4f} p_shuffle={p_shuffle:.4f}")

    gate_ok = [r for r in resultados if r["wilson90_lo"] > 0.5 and r["edge"] > 0
               and abs(r["split1"] - r["split2"]) < 0.30]
    print(f"GATE OK: {len(gate_ok)} de {len(resultados)} activos evaluados (n>=15)")
    for r in gate_ok:
        print(f"  {r['activo']}: n={r['n']} hit={r['hit_rate']*100:.1f}% wilson90lo={r['wilson90_lo']:.3f} edge={r['edge']:+.3f}")
    return resultados


def main():
    filas = cargar()
    evaluar(filas, "TODAS LAS DIRECCIONES")
    evaluar([f for f in filas if f["direccion"] == "BUY_YES"], "SOLO BUY_YES")
    evaluar([f for f in filas if f["direccion"] == "BUY_NO"], "SOLO BUY_NO")


if __name__ == "__main__":
    main()
