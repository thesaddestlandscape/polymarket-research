#!/usr/bin/env python3
"""Read-only: gate de promoción más riguroso que n>=15/n>=40 para candidatos_evaluacion_live.

Ítem #10 del backlog 10-Jul (ver memoria idea_intervalo_confianza_gradual +
idea_control_aleatorio_hipotesis). Combina capas de escepticismo baratas
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
  3. PnL real obligatorio (16-Jul, decisión Javi tras
     idea_favoritoconfirmado_btc15min_payout_asimetrico_14jul): IC/hit-rate
     miden si la dirección acierta, NO si paga. FAVORITO_CONFIRMADO#15min#BUY_NO
     (SOL/ETH/BTC) pasó este gate con IC≥0.19 y p_shuffle=0.000 las 3 veces,
     pero el payout es asimétrico (gana poco al acertar, pierde el stake
     entero al fallar) y el PnL real es negativo — "GATE OK" sin mirar PnL
     era una etiqueta engañosa. Bootstrap (5000 remuestreos con reemplazo)
     sobre pnl_neto por trade → CI90% + fracción de remuestreos con media≤0
     (p_boot, mismo rol que p_shuffle para IC). Si la media real ≤0, o el
     CI90% cruza 0, no se concluye rentabilidad aunque IC/hit-rate sean
     excelentes.

No sustituye N_BUCKET_MIN=15 / n>=40 IC>=0.08 (CLAUDE.md) — es una capa
adicional de lectura antes de proponer una promoción. No escribe nada.
Correr desde la raíz del repo:  python3 analisis_gate_riguroso.py
"""
import csv, json, os, random, math, sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import shadow_postmortem as sp  # noqa: E402 — reusa _ic_bayes/_shuffle_pvalue/_benjamini_hochberg (20-Jul, evita 3 copias casi idénticas del mismo test)

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
        partes = t.split("#")
        if len(partes) != 4:
            # p.ej. WEEKLY_PRICE#BTC#BUY_NO (sin timeframe en el nombre) —
            # mismo formato no soportado que analisis_embargo_train_test.py.
            print(f"  (omitida, formato no soportado: {t})")
            continue
        strat, pair, tf, dec = partes
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


# 20-Jul: ic_bayes/shuffle_percentile/benjamini_hochberg delegan en
# shadow_postmortem (fuente única, ver _ic_bayes/_shuffle_pvalue/
# _benjamini_hochberg allí) en vez de mantener copias locales — code-review
# encontró 3 implementaciones casi idénticas del mismo test en el repo.
ic_bayes = sp._ic_bayes


def shuffle_percentile(rows, ic_real, n_shuffle=N_SHUFFLE):
    """% de tiradas aleatorias (misma n) que igualan o superan el IC real.
    El resultado solo depende de n (no de los outcomes fila a fila, ver
    _shuffle_pvalue) — mismo modelo nulo de siempre, ahora determinista y
    vectorizado (antes: random.random() sin semilla, bucle Python)."""
    return sp._shuffle_pvalue(len(rows), ic_real, cola="alta", n_shuffle=n_shuffle)


def pnl_bootstrap(rows, n_boot=N_SHUFFLE):
    """Bootstrap (remuestreo con reemplazo) sobre pnl_neto real por trade.
    Devuelve (media, ci90_lo, ci90_hi, p_boot) donde p_boot = fracción de
    remuestreos con media≤0 (mismo rol que p_shuffle para IC, pero sobre
    dinero real en vez de hit-rate)."""
    pnls = [float(r["pnl_neto"]) for r in rows if r.get("pnl_neto") not in (None, "")]
    n = len(pnls)
    if n == 0:
        return None
    media = sum(pnls) / n
    medias_boot = []
    for _ in range(n_boot):
        muestra = [pnls[random.randrange(n)] for _ in range(n)]
        medias_boot.append(sum(muestra) / n)
    medias_boot.sort()
    lo = medias_boot[int(0.05 * n_boot)]
    hi = medias_boot[int(0.95 * n_boot) - 1]
    p_boot = sum(1 for m in medias_boot if m <= 0) / n_boot
    return media, lo, hi, p_boot


def gate(rows):
    """Veredicto de promoción para un bucket de filas resueltas (results.csv).
    Combina n/IC/Wilson/shuffle (hit-rate) con PnL real bootstrap — un
    bucket con IC/hit excelente pero PnL medio≤0 o CI90% cruzando 0 NO es
    GATE OK (payout asimétrico / selección adversa, ver docstring del módulo)."""
    n = len(rows)
    if n == 0:
        return None
    aciertos = sum(1 for r in rows if r["acierto"] == "1")
    ic = ic_bayes(aciertos, n)
    lo, hi = wilson_ci(aciertos, n)
    p_shuf = shuffle_percentile(rows, ic)
    pnl_stats = pnl_bootstrap(rows)

    razones = []
    if n < N_LIVE_MIN:
        razones.append(f"n<{N_LIVE_MIN}")
    if ic < IC_LIVE_MIN:
        razones.append(f"IC<{IC_LIVE_MIN}")
    if lo <= 0.5:
        razones.append("Wilson cruza 0.5")
    if p_shuf > 0.05:
        razones.append(f"no bate shuffle (p={p_shuf:.3f})")
    if pnl_stats is None:
        razones.append("sin pnl_neto")
    else:
        pnl_media, pnl_lo, pnl_hi, pnl_pboot = pnl_stats
        if pnl_media <= 0:
            razones.append(f"PnL medio≤0 ({pnl_media:+.4f}/trade)")
        elif pnl_lo <= 0:
            razones.append(f"PnL no bate bootstrap (CI90%=[{pnl_lo:+.4f},{pnl_hi:+.4f}] cruza 0)")

    veredicto = "GATE OK" if not razones else "NO CONCLUYENTE: " + ", ".join(razones)
    resultado = {"n": n, "hit": aciertos / n, "ic": ic, "lo": lo, "hi": hi,
                 "p_shuf": p_shuf, "veredicto": veredicto}
    if pnl_stats is not None:
        pnl_media, pnl_lo, pnl_hi, pnl_pboot = pnl_stats
        resultado.update(pnl_media=pnl_media, pnl_lo=pnl_lo, pnl_hi=pnl_hi, pnl_pboot=pnl_pboot)
    return resultado


# Corrección por comparaciones múltiples (propuesta #23 backlog, artículo
# DSR/PBO/FDR 11-Jul): con K candidatas evaluadas A LA VEZ, un umbral fijo
# p<0.05 por tupla es una máquina de falsos descubrimientos — bajo el nulo,
# 0.05×K tuplas lo cruzan por azar. BH controla la fracción esperada de
# falsos positivos ENTRE las aceptadas (FDR), endureciendo el umbral con K.
# Devuelve lista de bool (True = sobrevive) alineada con pvals. 20-Jul:
# delega en shadow_postmortem._benjamini_hochberg (fuente única).
benjamini_hochberg = sp._benjamini_hochberg


def main():
    claves = cargar_candidatos()
    filas_por_clave = cargar_filas(claves)

    resultados = []
    for tupla, strat, sub, dec in claves:
        rows = filas_por_clave.get((strat, sub, dec), [])
        g = gate(rows)
        resultados.append((tupla, g))

    # BH sobre el conjunto completo de candidatas con datos — el denominador
    # honesto es cuántas se evalúan a la vez, no cada una aislada.
    con_datos = [(i, r[1]["p_shuf"]) for i, r in enumerate(resultados) if r[1] is not None]
    keep_bh = benjamini_hochberg([p for _, p in con_datos]) if con_datos else []
    bh_ok = {con_datos[j][0] for j, k in enumerate(keep_bh) if k}

    print(f"K={len(con_datos)} candidatas evaluadas simultáneamente — FDR (Benjamini-Hochberg) al 10%")
    print(f"{'tupla':<45} {'n':>4} {'hit%':>6} {'IC':>7} {'Wilson90%':>18} {'p_shuf':>7} {'PnL/trade':>10} {'PnL_CI90%':>20}  veredicto")
    print("-" * 160)
    for i, (tupla, g) in enumerate(resultados):
        if g is None:
            print(f"{tupla:<45} {0:>4}  {'--':>5} {'--':>7} {'--':>18} {'--':>7} {'--':>10} {'--':>20}  sin datos")
            continue
        razones = [] if g["veredicto"] == "GATE OK" else [g["veredicto"].split(": ", 1)[1]]
        if i not in bh_ok:
            razones.append("no sobrevive FDR-BH multi-test")
        veredicto = "GATE OK" if not razones else "NO CONCLUYENTE: " + ", ".join(razones)

        pnl_str = f"{g['pnl_media']:>+10.4f}" if "pnl_media" in g else f"{'--':>10}"
        pnl_ci_str = f"[{g['pnl_lo']:>+7.4f},{g['pnl_hi']:>+7.4f}]" if "pnl_lo" in g else f"{'--':>20}"
        print(f"{tupla:<45} {g['n']:>4} {g['hit']*100:>5.1f}% {g['ic']:>+7.3f} "
              f"[{g['lo']:>6.3f},{g['hi']:>6.3f}] {g['p_shuf']:>7.3f} {pnl_str} {pnl_ci_str:>20}  {veredicto}")


if __name__ == "__main__":
    main()
