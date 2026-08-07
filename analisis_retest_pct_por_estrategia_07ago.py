#!/usr/bin/env python3
"""Read-only: re-evalúa retest_pct desagregado por (familia GBM_LATE, activo,
marco, dirección) con el rigor completo del proyecto (Wilson+shuffle+
split-half+PnL bootstrap+BH-FDR), no solo el caso único que se miró el
13-Jul (GBM_LATE_15M#SOL#15min#BUY_YES, n=528).

Origen (07-Ago, petición explícita Javi, revisando artículos de day-trading:
"Podríamos probar el 1 [ORB] en diferentes estrategias, quizá en aquel
momento que lo probamos no sabíamos todo lo que sabemos ahora, el proyecto
estaba más verde"): retest_pct se loguea desde 13-Jul dentro de _s_gbm_late
(shadow_predict.py) — cubre TODA la familia GBM_LATE (base/TARDIO/
ESPACIO_ATR/PYCONFIRMADO/60M) × 6 activos × ambas direcciones, no solo el
caso original. Hoy hay ~24.5k filas con retest_pct no-nulo (vs 528 del
13-Jul) — más de 40x el dato original, y nunca se re-analizó desagregado.

Hallazgo original (idea_retest_gbm_late_15m_13jul): retest_pct==0 (recorrido
monótono, sin retroceso) acierta MÁS que retest_pct>0 en GBM_LATE_15M#SOL#
BUY_YES — signo CONTRARIO al patrón "break-and-retest" de ORB que lo
inspiró. Este script comprueba si ese signo (monótono > con retroceso) es
universal en la familia o específico de ese caso.

Reutiliza el mismo kit de rigor que analisis_gate_riguroso.py (wilson_ci,
ic_bayes vía shadow_postmortem, shuffle, pnl_bootstrap, BH-FDR) — no
reinventa los tests. Solo lectura, no toca prob_yes/edge/decisión de nada.
"""
import csv
import json
import math
import random
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import shadow_postmortem as sp  # noqa: E402

BASE = Path(__file__).resolve().parent
RESULTS = BASE / "data" / "shadow" / "results.csv"

N_SHUFFLE = 5000
Z_90 = 1.645
N_MIN_POR_GRUPO = 40  # mínimo por lado (retest==0 y retest>0) para concluir

ic_bayes = sp._ic_bayes
benjamini_hochberg = sp._benjamini_hochberg


def wilson_ci(aciertos, n, z=Z_90):
    if n == 0:
        return (0.0, 0.0)
    phat = aciertos / n
    denom = 1 + z * z / n
    centro = phat + z * z / (2 * n)
    ajuste = z * math.sqrt(phat * (1 - phat) / n + z * z / (4 * n * n))
    return ((centro - ajuste) / denom, (centro + ajuste) / denom)


def cargar_filas():
    """clave (strategy, subtype, decision) -> lista de dicts
    {ts, acierto, pnl_neto, retest0} ordenada cronológicamente."""
    grupos = defaultdict(list)
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            strat = row.get("strategy", "")
            if "GBM_LATE" not in strat and "UPDOWN_GBM" not in strat:
                continue
            if row.get("acierto") not in ("0", "1"):
                continue
            try:
                feat = json.loads(row.get("features") or "{}")
            except Exception:
                continue
            rp = feat.get("retest_pct")
            if rp is None:
                continue
            try:
                pnl = float(row["pnl_neto"]) if row.get("pnl_neto") not in (None, "") else None
            except ValueError:
                pnl = None
            clave = (strat, row["subtype"], row["decision"])
            grupos[clave].append({
                "ts": row.get("resolution_timestamp") or row.get("prediction_timestamp") or "",
                "acierto": int(row["acierto"]),
                "pnl": pnl,
                "retest0": (rp == 0),
            })
    for clave in grupos:
        grupos[clave].sort(key=lambda r: r["ts"])
    return grupos


def shuffle_diff_hit(filas, diff_real, n_iter=N_SHUFFLE, seed=42):
    """Permutación: baraja la etiqueta retest0/retest>0 sobre las MISMAS
    resoluciones, recalcula diff(hit_retest0 - hit_retestpos). p = fracción
    de tiradas que igualan o superan |diff_real| (dos colas, mismo espíritu
    que shuffle_percentile de analisis_gate_riguroso.py pero para una
    comparación entre 2 grupos en vez de IC vs azar puro)."""
    rnd = random.Random(seed)
    aciertos = [r["acierto"] for r in filas]
    n0 = sum(1 for r in filas if r["retest0"])
    n = len(filas)
    if n0 == 0 or n0 == n:
        return None
    idx = list(range(n))
    mayor_igual = 0
    for _ in range(n_iter):
        rnd.shuffle(idx)
        grupo0 = idx[:n0]
        grupo1 = idx[n0:]
        d = (sum(aciertos[i] for i in grupo0) / n0) - (sum(aciertos[i] for i in grupo1) / len(grupo1))
        if abs(d) >= abs(diff_real):
            mayor_igual += 1
    return mayor_igual / n_iter


def pnl_bootstrap_grupo(filas, n_boot=N_SHUFFLE, seed=42):
    pnls = [r["pnl"] for r in filas if r["pnl"] is not None]
    n = len(pnls)
    if n == 0:
        return None
    rnd = random.Random(seed)
    media = sum(pnls) / n
    medias = []
    for _ in range(n_boot):
        muestra = [pnls[rnd.randrange(n)] for _ in range(n)]
        medias.append(sum(muestra) / n)
    medias.sort()
    lo = medias[int(0.05 * n_boot)]
    hi = medias[int(0.95 * n_boot) - 1]
    return media, lo, hi


def split_half_signo(filas):
    """Divide cronológicamente en 2 mitades, devuelve el signo de
    diff(hit_retest0 - hit_retestpos) en cada mitad -- consistencia real
    exige mismo signo en ambas, no solo en el agregado."""
    mid = len(filas) // 2
    signos = []
    for mitad in (filas[:mid], filas[mid:]):
        g0 = [r["acierto"] for r in mitad if r["retest0"]]
        g1 = [r["acierto"] for r in mitad if not r["retest0"]]
        if len(g0) < 10 or len(g1) < 10:
            signos.append(None)
            continue
        d = (sum(g0) / len(g0)) - (sum(g1) / len(g1))
        signos.append(round(d, 4))
    return signos


def evaluar(clave, filas):
    g0 = [r for r in filas if r["retest0"]]
    g1 = [r for r in filas if not r["retest0"]]
    if len(g0) < N_MIN_POR_GRUPO or len(g1) < N_MIN_POR_GRUPO:
        return None
    hit0 = sum(r["acierto"] for r in g0) / len(g0)
    hit1 = sum(r["acierto"] for r in g1) / len(g1)
    diff = hit0 - hit1
    lo0, hi0 = wilson_ci(sum(r["acierto"] for r in g0), len(g0))
    lo1, hi1 = wilson_ci(sum(r["acierto"] for r in g1), len(g1))
    p_shuf = shuffle_diff_hit(filas, diff)
    pnl0 = pnl_bootstrap_grupo(g0)
    pnl1 = pnl_bootstrap_grupo(g1)
    signos = split_half_signo(filas)
    consistente = (signos[0] is not None and signos[1] is not None
                   and signos[0] * signos[1] > 0)
    return {
        "clave": clave, "n0": len(g0), "n1": len(g1),
        "hit0": hit0, "hit1": hit1, "diff": diff,
        "wilson0": (lo0, hi0), "wilson1": (lo1, hi1),
        "p_shuf": p_shuf, "pnl0": pnl0, "pnl1": pnl1,
        "split_half": signos, "consistente": consistente,
    }


def main():
    grupos = cargar_filas()
    resultados = []
    for clave, filas in grupos.items():
        r = evaluar(clave, filas)
        if r is not None:
            resultados.append(r)

    resultados.sort(key=lambda r: -(r["n0"] + r["n1"]))

    pvals = [r["p_shuf"] for r in resultados if r["p_shuf"] is not None]
    keep_bh = benjamini_hochberg(pvals) if pvals else []
    bh_iter = iter(keep_bh)
    print(f"K={len(resultados)} combos con n>={N_MIN_POR_GRUPO} en ambos lados "
          f"(retest_pct==0 vs >0) — FDR Benjamini-Hochberg al 10%\n")
    print(f"{'estrategia#subtype#dir':<48} {'n0':>5} {'n1':>5} {'hit0%':>7} {'hit1%':>7} "
          f"{'diff':>7} {'p_shuf':>7} {'split-half':>18}  {'PnL0/tr':>9} {'PnL1/tr':>9}  veredicto")
    print("-" * 165)
    for r in resultados:
        strat, sub, dec = r["clave"]
        etiqueta = f"{strat}#{sub}#{dec}"
        sobrevive_bh = next(bh_iter) if r["p_shuf"] is not None else False
        veredicto_partes = []
        if r["p_shuf"] is None or r["p_shuf"] > 0.05:
            veredicto_partes.append("no bate shuffle")
        elif not sobrevive_bh:
            veredicto_partes.append("no sobrevive FDR-BH")
        if not r["consistente"]:
            veredicto_partes.append("split-half inconsistente")
        veredicto = "CONFIRMADO" if not veredicto_partes else "NO CONCLUYENTE: " + ", ".join(veredicto_partes)
        pnl0_str = f"{r['pnl0'][0]:+.3f}" if r["pnl0"] else "--"
        pnl1_str = f"{r['pnl1'][0]:+.3f}" if r["pnl1"] else "--"
        sh_str = f"[{r['split_half'][0]},{r['split_half'][1]}]"
        print(f"{etiqueta:<48} {r['n0']:>5} {r['n1']:>5} {r['hit0']*100:>6.1f}% {r['hit1']*100:>6.1f}% "
              f"{r['diff']*100:>+6.1f}p {r['p_shuf']:>7.3f} {sh_str:>18}  {pnl0_str:>9} {pnl1_str:>9}  {veredicto}")


if __name__ == "__main__":
    main()
