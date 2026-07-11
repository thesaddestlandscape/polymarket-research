#!/usr/bin/env python3
"""Read-only: gate de promoción más riguroso que n>=15/n>=40 para candidatos_evaluacion_live.

Ítem #10 del backlog 10-Jul (ver memoria idea_intervalo_confianza_gradual +
idea_control_aleatorio_hipotesis). Combina dos capas de escepticismo baratas
sobre results.csv (dato ya resuelto), SIN tocar el gate real ni ningún config:

  1. Wilson score interval (90%) sobre el hit-rate del bucket, en vez de un
     punto estimado desnudo. Si el intervalo inferior no supera 0.5, el
     hit-rate no se distingue de un coinflip por mucho que n cruce el umbral.
  2. Control aleatorio (shuffle): sobre las MISMAS resoluciones (outcome_real,
     independiente de qué decisión se tomó), simula 5000 veces una dirección
     BUY_YES/BUY_NO al 50/50 y recalcula ic_bayes. Si el IC real no supera al
     ~95% de esas tiradas aleatorias, el patrón no se distingue de ruido/beta
     de mercado en ese periodo — el caso STRUCT_NO_15M (no replicó con fills
     reales) es el tipo de hallazgo que esto habría marcado como frágil.

No sustituye N_BUCKET_MIN=15 / n>=40 IC>=0.08 (CLAUDE.md) — es una capa
adicional de lectura antes de proponer una promoción. No escribe nada.
Correr desde la raíz del repo:  python3 analisis_gate_riguroso.py
"""
import csv, json, os, random, math
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "data", "shadow", "results.csv")
CONFIG_LIVE = os.path.join(BASE, "data", "live", "config_live.json")

N_SHUFFLE = 5000
Z_90 = 1.645
IC_LIVE_MIN = 0.08
N_LIVE_MIN = 40


def cargar_candidatos():
    cfg = json.load(open(CONFIG_LIVE))
    tuplas = cfg.get("candidatos_evaluacion_live", [])
    claves = []
    for t in tuplas:
        strat, pair, tf, dec = t.split("#")
        claves.append((t, strat, f"{pair}#{tf}", dec))
    return claves


def cargar_filas(claves):
    wanted = {(s, sub, d) for _, s, sub, d in claves}
    filas = defaultdict(list)
    with open(RES) as f:
        for row in csv.DictReader(f):
            if row.get("acierto") in (None, ""):
                continue
            k = (row["strategy"], row["subtype"], row["decision"])
            if k in wanted:
                filas[k].append(row)
    return filas


def wilson_ci(aciertos, n, z=Z_90):
    if n == 0:
        return (0.0, 0.0)
    phat = aciertos / n
    denom = 1 + z * z / n
    centro = phat + z * z / (2 * n)
    ajuste = z * math.sqrt(phat * (1 - phat) / n + z * z / (4 * n * n))
    return ((centro - ajuste) / denom, (centro + ajuste) / denom)


def ic_bayes(aciertos, n):
    return (aciertos + 1) / (n + 2) - 0.5


def shuffle_percentile(rows, ic_real, n_shuffle=N_SHUFFLE):
    """% de tiradas aleatorias (misma n, mismas resoluciones) que igualan o superan el IC real."""
    outcomes_yes = [row["outcome_real"] == "YES" for row in rows]
    n = len(outcomes_yes)
    if n == 0:
        return 1.0
    supera = 0
    for _ in range(n_shuffle):
        aciertos_sim = sum(
            1 for oy in outcomes_yes if (random.random() < 0.5) == oy
        )
        if ic_bayes(aciertos_sim, n) >= ic_real:
            supera += 1
    return supera / n_shuffle


def benjamini_hochberg(pvals, fdr=0.10):
    """Corrección por comparaciones múltiples (propuesta #23 backlog, artículo
    DSR/PBO/FDR 11-Jul): con K candidatas evaluadas A LA VEZ, un umbral fijo
    p<0.05 por tupla es una máquina de falsos descubrimientos — bajo el nulo,
    0.05×K tuplas lo cruzan por azar. BH controla la fracción esperada de
    falsos positivos ENTRE las aceptadas (FDR), endureciendo el umbral con K.
    Devuelve lista de bool (True = sobrevive) alineada con pvals."""
    indexed = sorted(range(len(pvals)), key=lambda i: pvals[i])
    n = len(pvals)
    keep = [False] * n
    cutoff = -1
    for rank, i in enumerate(indexed, start=1):
        if pvals[i] <= fdr * rank / n:
            cutoff = rank
    for rank, i in enumerate(indexed, start=1):
        if rank <= cutoff:
            keep[i] = True
    return keep


def main():
    claves = cargar_candidatos()
    filas_por_clave = cargar_filas(claves)

    resultados = []
    for tupla, strat, sub, dec in claves:
        rows = filas_por_clave.get((strat, sub, dec), [])
        n = len(rows)
        if n == 0:
            resultados.append((tupla, 0, None, None, None, None, None))
            continue
        aciertos = sum(1 for r in rows if r["acierto"] == "1")
        hit = aciertos / n
        ic = ic_bayes(aciertos, n)
        lo, hi = wilson_ci(aciertos, n)
        p_shuf = shuffle_percentile(rows, ic)
        resultados.append((tupla, n, hit, ic, lo, hi, p_shuf))

    # BH sobre el conjunto completo de candidatas con datos — el denominador
    # honesto es cuántas se evalúan a la vez, no cada una aislada.
    con_datos = [(i, r[6]) for i, r in enumerate(resultados) if r[6] is not None]
    keep_bh = benjamini_hochberg([p for _, p in con_datos]) if con_datos else []
    bh_ok = {con_datos[j][0] for j, k in enumerate(keep_bh) if k}

    print(f"K={len(con_datos)} candidatas evaluadas simultáneamente — FDR (Benjamini-Hochberg) al 10%")
    print(f"{'tupla':<45} {'n':>4} {'hit%':>6} {'IC':>7} {'Wilson90%':>18} {'p_shuffle':>10}  veredicto")
    print("-" * 115)
    for i, (tupla, n, hit, ic, lo, hi, p_shuf) in enumerate(resultados):
        if n == 0:
            print(f"{tupla:<45} {0:>4}  {'--':>5} {'--':>7} {'--':>18} {'--':>10}  sin datos")
            continue
        razones = []
        if n < N_LIVE_MIN:
            razones.append(f"n<{N_LIVE_MIN}")
        if ic < IC_LIVE_MIN:
            razones.append(f"IC<{IC_LIVE_MIN}")
        if lo <= 0.5:
            razones.append("Wilson cruza 0.5")
        if p_shuf > 0.05:
            razones.append(f"no bate shuffle (p={p_shuf:.3f})")
        if i not in bh_ok:
            razones.append("no sobrevive FDR-BH multi-test")
        veredicto = "GATE OK" if not razones else "NO CONCLUYENTE: " + ", ".join(razones)

        print(f"{tupla:<45} {n:>4} {hit*100:>5.1f}% {ic:>+7.3f} [{lo:>6.3f},{hi:>6.3f}] {p_shuf:>10.3f}  {veredicto}")


if __name__ == "__main__":
    main()
