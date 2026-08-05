#!/usr/bin/env python3
"""Read-only: gate riguroso (Wilson 90% + shuffle real + split-half) sobre
data/shadow/wallet_mirror_dry_run.csv ("grandes jugadas" / Wallet Mirror,
P24). Segmentado por tipo (SEGUIR/FADE) x es_jugada_grande x activo
(CLAUDE.md punto 17) -- nunca solo el agregado. Solo lectura.

Correr desde la raíz del repo: python3 analisis_gate_riguroso_wallet_mirror_30jul.py
"""
import csv
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
    with open("data/shadow/wallet_mirror_dry_run.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("acierto") not in ("0", "1"):
                continue
            filas.append({
                "tipo": r["tipo"], "activo": r["activo"], "marco": r["marco"],
                "acierto": r["acierto"] == "1",
                "jugada_grande": r.get("es_jugada_grande") == "1",
                "ts": r["trade_timestamp"],
            })
    return filas


def evaluar(filas, etiqueta, agrupar_por):
    print(f"\n=== {etiqueta} (n resuelto: {len(filas)}) ===")
    grupos = defaultdict(list)
    for f in filas:
        clave = tuple(f[k] for k in agrupar_por)
        grupos[clave].append(f)

    resultados = []
    for clave, grupo in sorted(grupos.items()):
        n = len(grupo)
        if n < N_MIN:
            print(f"{clave}: n={n} (<{N_MIN}, sin concluir)")
            continue
        hits = sum(1 for g in grupo if g["acierto"])
        hit_rate = hits / n
        wlo = wilson_lower(hits, n)

        grupo_ordenado = sorted(grupo, key=lambda g: g["ts"])
        mitad = len(grupo_ordenado) // 2
        h1, h2 = grupo_ordenado[:mitad], grupo_ordenado[mitad:]
        hit1 = sum(1 for g in h1 if g["acierto"]) / len(h1) if h1 else 0
        hit2 = sum(1 for g in h2 if g["acierto"]) / len(h2) if h2 else 0

        random.seed(42)
        mayor_igual = sum(1 for _ in range(N_SHUFFLE)
                           if sum(random.random() < 0.5 for _ in range(n)) / n >= hit_rate)
        p_shuffle = mayor_igual / N_SHUFFLE

        print(f"{clave}: n={n} hit={hit_rate*100:.1f}% wilson90lo={wlo:.3f} "
              f"p_shuffle={p_shuffle:.4f} split1={hit1*100:.1f}% split2={hit2*100:.1f}%")
        resultados.append({"clave": clave, "n": n, "hit_rate": hit_rate, "wilson90_lo": wlo,
                            "p_shuffle": p_shuffle, "split1": hit1, "split2": hit2})

    gate_ok = [r for r in resultados if r["wilson90_lo"] > 0.5 and r["p_shuffle"] < 0.05
               and abs(r["split1"] - r["split2"]) < 0.20]
    print(f"GATE OK (wilson90lo>0.5, p_shuffle<0.05, split-half<20pp gap): {len(gate_ok)} de {len(resultados)}")
    for r in gate_ok:
        print(f"  {r['clave']}: n={r['n']} hit={r['hit_rate']*100:.1f}%")
    return resultados


def main():
    filas = cargar()
    evaluar(filas, "Por tipo (SEGUIR/FADE)", ["tipo"])
    evaluar(filas, "Por tipo x jugada_grande", ["tipo", "jugada_grande"])
    evaluar([f for f in filas if f["jugada_grande"]], "SOLO jugada_grande=True, por tipo x activo",
            ["tipo", "activo"])
    evaluar([f for f in filas if not f["jugada_grande"]], "SOLO jugada_grande=False, por tipo x activo",
            ["tipo", "activo"])


if __name__ == "__main__":
    main()
