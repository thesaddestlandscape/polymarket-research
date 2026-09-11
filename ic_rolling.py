#!/usr/bin/env python3
"""Read-only: IC por mitades cronológicas (split-half) para cada estrategia/
subtype/par/duración con n>=30 — ¿el edge está MADURANDO (mejora en la mitad
reciente), AGOTÁNDOSE (empeora) o ESTABLE? El IC agregado histórico (el que
vive en strategy_params.json) puede esconder cualquiera de los dos: un edge
reciente fuerte enterrado bajo meses planos, o un edge que ya murió pero el
agregado todavía lo muestra positivo por inercia.

Caso real que motivó esto (09-Jul): UPDOWN_GBM#BUY_YES#15min con IC agregado
-0.02 escondía un tramo reciente con n=56 hit66% — se encontró filtrando a
mano. Este script automatiza esa comprobación para todas las claves.

Mismo esquema de agregación que shadow_postmortem.calcular_params (s,
s#subtype, s#asset, s#duración) y la misma fórmula ic_bayes con shrinkage
((aciertos+1)/(n+2)-0.5). Disciplina del proyecto: cada mitad necesita
n>=15 para contar (n total >=30). NO toca producción — solo lee results.csv.
Correr desde la raíz del repo:  python3 ic_rolling.py
"""
import csv
import os

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "data", "shadow", "results.csv")
ROWS = list(csv.DictReader(open(RES)))
N_MIN_MITAD = 15
GAP_ESTABLE = 0.03  # |delta ic_bayes| por debajo de esto se considera ruido


def ic_bayes(rows):
    n = len(rows)
    if not n:
        return 0.0
    aciertos = sum(1 for r in rows if r.get("acierto") == "1")
    return (aciertos + 1) / (n + 2) - 0.5


def claves_de(r):
    s = r["strategy"]
    subtype = r.get("subtype", "")
    claves = [s]
    if "#" in subtype:
        a_part, d_part = subtype.split("#", 1)
        claves += [f"{s}#{subtype}", f"{s}#{a_part}", f"{s}#{d_part}"]
    elif subtype:
        claves.append(f"{s}#{subtype}")
    return claves


def main():
    por_clave = {}
    for r in ROWS:
        for clave in claves_de(r):
            por_clave.setdefault(clave, []).append(r)

    resultados = []
    for clave, rows in por_clave.items():
        n = len(rows)
        if n < 2 * N_MIN_MITAD:
            continue
        rows_ord = sorted(rows, key=lambda r: r["resolution_timestamp"])
        mid = n // 2
        primera, segunda = rows_ord[:mid], rows_ord[mid:]
        ic1, ic2 = ic_bayes(primera), ic_bayes(segunda)
        gap = ic2 - ic1
        resultados.append((clave, n, len(primera), ic1, len(segunda), ic2, gap))

    resultados.sort(key=lambda x: -abs(x[6]))

    print("=" * 100)
    print("IC ROLLING (split-half cronológico) — claves con n>=30, ordenado por |gap| desc")
    print("=" * 100)
    print(f"{'clave':<45} {'n':>5} {'n1':>5} {'ic1':>8} {'n2':>5} {'ic2':>8} {'gap':>8}  veredicto")
    print("-" * 100)
    for clave, n, n1, ic1, n2, ic2, gap in resultados:
        if abs(gap) < GAP_ESTABLE:
            veredicto = "ESTABLE"
        elif gap > 0:
            veredicto = "MADURANDO (mejora)"
        else:
            veredicto = "AGOTANDO (empeora)"
        print(f"{clave:<45} {n:>5} {n1:>5} {ic1:>+8.4f} {n2:>5} {ic2:>+8.4f} {gap:>+8.4f}  {veredicto}")

    print("-" * 100)
    print(f"{len(resultados)} claves con n>=30. Disciplina: n<15 por mitad no concluye nada")
    print("(ya filtrado). MADURANDO/AGOTANDO con n2 aún bajo = vigilar, no actuar todavía.")


if __name__ == "__main__":
    main()
