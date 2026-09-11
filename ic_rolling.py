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
N_MIN_ESTRATO_MITAD = 15  # propuesta #5 backlog quant-desk: mismo listón por activo-mitad


def ic_bayes(rows):
    n = len(rows)
    if not n:
        return 0.0
    aciertos = sum(1 for r in rows if r.get("acierto") == "1")
    return (aciertos + 1) / (n + 2) - 0.5


def asset_de(r):
    subtype = r.get("subtype", "")
    return subtype.split("#", 1)[0] if "#" in subtype else (subtype or "?")


def gap_pareado_por_activo(rows_ord, mid):
    """Propuesta #5 backlog quant-desk (13-jul, Part V reducción de varianza):
    el gap crudo (ic2-ic1 sobre el agregado completo) confunde maduración/
    agotamiento REAL del edge con un simple cambio de COMPOSICIÓN entre
    mitades (ej. la 2ª mitad tiene más BTC que la 1ª, y BTC ya rinde distinto
    a ETH/SOL por razones ajenas al tiempo). Aísla el efecto: compara ic1 vs
    ic2 DENTRO de cada activo por separado (cada mitad de cada activo con
    n>=N_MIN_ESTRATO_MITAD, misma disciplina que el split global) y agrega
    ponderando por n compartido — un activo con más peso en ambas mitades
    pesa más en el gap final, pero la comparación en sí siempre es dentro
    del MISMO activo, nunca entre activos distintos."""
    primera, segunda = rows_ord[:mid], rows_ord[mid:]
    por_activo_1, por_activo_2 = {}, {}
    for r in primera:
        por_activo_1.setdefault(asset_de(r), []).append(r)
    for r in segunda:
        por_activo_2.setdefault(asset_de(r), []).append(r)
    num, den, n_estratos_ok = 0.0, 0, 0
    for a in set(por_activo_1) | set(por_activo_2):
        r1, r2 = por_activo_1.get(a, []), por_activo_2.get(a, [])
        if len(r1) < N_MIN_ESTRATO_MITAD or len(r2) < N_MIN_ESTRATO_MITAD:
            continue
        peso = min(len(r1), len(r2))
        num += peso * (ic_bayes(r2) - ic_bayes(r1))
        den += peso
        n_estratos_ok += 1
    if den == 0:
        return None, 0
    return num / den, n_estratos_ok


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
        gap_par, n_estratos = gap_pareado_por_activo(rows_ord, mid)
        resultados.append((clave, n, len(primera), ic1, len(segunda), ic2, gap,
                            gap_par, n_estratos))

    resultados.sort(key=lambda x: -abs(x[6]))

    print("=" * 118)
    print("IC ROLLING (split-half cronológico) — claves con n>=30, ordenado por |gap| desc")
    print("gap_par = mismo split pero pareado por activo (propuesta #5), aísla maduración/")
    print("agotamiento real de un simple cambio de composición BTC/ETH/SOL/XRP entre mitades")
    print("=" * 118)
    print(f"{'clave':<45} {'n':>5} {'n1':>5} {'ic1':>8} {'n2':>5} {'ic2':>8} {'gap':>8} {'gap_par':>9} {'n_estr':>6}  veredicto")
    print("-" * 118)
    for clave, n, n1, ic1, n2, ic2, gap, gap_par, n_estratos in resultados:
        if abs(gap) < GAP_ESTABLE:
            veredicto = "ESTABLE"
        elif gap > 0:
            veredicto = "MADURANDO (mejora)"
        else:
            veredicto = "AGOTANDO (empeora)"
        gap_par_str = f"{gap_par:+.4f}" if gap_par is not None else "n/a"
        divergencia = ""
        if gap_par is not None and abs(gap) >= GAP_ESTABLE and abs(gap_par) >= GAP_ESTABLE:
            if (gap > 0) != (gap_par > 0):
                divergencia = "  ⚠️ SIGNO OPUESTO al pareado — sospechar composición, no edge"
        print(f"{clave:<45} {n:>5} {n1:>5} {ic1:>+8.4f} {n2:>5} {ic2:>+8.4f} {gap:>+8.4f} "
              f"{gap_par_str:>9} {n_estratos:>6}  {veredicto}{divergencia}")

    print("-" * 100)
    print(f"{len(resultados)} claves con n>=30. Disciplina: n<15 por mitad no concluye nada")
    print("(ya filtrado). MADURANDO/AGOTANDO con n2 aún bajo = vigilar, no actuar todavía.")


if __name__ == "__main__":
    main()
