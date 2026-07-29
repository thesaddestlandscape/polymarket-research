"""
analisis_kelly_precio_gate_29jul.py — gate riguroso del sizing por precio
de entrada (petición explícita Javi, 29-Jul: "ganamos más veces de las que
perdemos, pero cuando perdemos, perdemos mucho, y cuando ganamos, ganamos
poco" — solucionarlo para acercar el sistema a 548€/día).

Diagnóstico confirmado en trades.csv (dinero real) antes de este script:
de las 4 tuplas live hoy, las 3 que entran caro (precio≥0.60) sangran
(ratio ganancia/pérdida 0.16-0.73) y la única que entra barato (0.39,
GBM_LATE_15M#ETH#15min) es la única rentable (ratio 1.51, +7.67€). Esto
replica con más n el hallazgo ya confirmado el 28-Jul con FAVORITO#60min
(project_drenajes_live_barrido_28jul: "breakeven = precio de entrada").

El mecanismo de fondo nunca se corrigió: live_stake.py::calcular_stake()
usa el IC como proxy de edge SIN dividir por (1-precio) -- ver f_actual
vs f_exacto en analisis_kelly_exacto_desagregado_23jul.py (23-Jul, mismo
formulismo, sin rigor de shuffle/split-half/BH-FDR y limitado a las
tuplas ya live de entonces). Este script generaliza esa cuantificación a
TODO el universo (pares_permitidos_live + candidatos_evaluacion_live),
agrupado por BUCKET DE PRECIO (paso 0.10, perspectiva de la decisión),
con la misma barra de rigor que gate_bucket_propio.py (shuffle test +
split-half cronológico + BH-FDR) -- para que la corrección de Kelly que
se implemente la próxima sesión en live_stake.py se apoye en buckets ya
confirmados, no en un patrón bonito con poco n.

f_actual  = |ic_bayes| * 0.5          (igual fórmula que calcular_stake)
f_exacto  = max(0, (p_hat - pi_medio) / (1 - pi_medio)) * 0.5
ratio     = f_exacto / f_actual       (factor de corrección que habría
                                        que aplicar al stake actual)

Un bucket se marca "confirmado" solo si:
  1. n >= N_MIN (15)
  2. shuffle test sobre pnl_neto (bucket vs resto de la misma familia de
     estrategia) con p < P_MAX
  3. split-half cronológico: el signo de (ratio-1) se repite en ambas
     mitades
  4. sobrevive BH-FDR q=0.05 sobre la familia completa de tests

Solo lectura -- no toca live_stake.py, prob_yes ni ningún stake real.
Genera data/shadow/kelly_precio_gate_29jul.json (diagnóstico, NO
consumido todavía por ningún proceso en producción -- decisión de
implementación pendiente de la próxima sesión, ver conversación 29-Jul).
"""
import csv
import json
import math
from collections import defaultdict
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
RESULTS = str(REPO / "data/shadow/results.csv")
CONFIG_LIVE = str(REPO / "data/live/config_live.json")
OUT = str(REPO / "data/shadow/kelly_precio_gate_29jul.json")

STEP = 0.10
N_MIN = 15
P_MAX = 0.05
ITERS = 1000

_rng = np.random.default_rng(29)


def bucket(p):
    return round(math.floor(p / STEP) * STEP, 4)


def _familia(strategy):
    """Agrupa subfamilias del mismo arquetipo (ej. GBM_LATE_15M_TARDIO,
    _ESPACIO_ATR, _PYCONFIRMADO cuentan como GBM_LATE_15M) -- el patrón de
    precio es del ARQUETIPO, no de la variante exacta, y agrupar da más n
    por bucket sin mezclar arquetipos distintos (A vs B, ver
    project_dos_patrones_edge_bandera_21jul)."""
    if strategy.startswith("GBM_LATE"):
        return "GBM_LATE_15M_FAMILIA"
    if strategy.startswith("FAVORITO_CONFIRMADO"):
        return "FAVORITO_CONFIRMADO_FAMILIA"
    if strategy.startswith("BALLENAS"):
        return "BALLENAS_FAMILIA"
    if strategy.startswith("UPDOWN_GBM"):
        return "UPDOWN_GBM_FAMILIA"
    return strategy


def cargar_universo():
    with open(CONFIG_LIVE, encoding="utf-8") as f:
        c = json.load(f)
    tuplas = set()
    for lista in (c.get("pares_permitidos_live", []), c.get("candidatos_evaluacion_live", [])):
        for t in lista:
            partes = t.split("#")
            if len(partes) == 4:
                strategy, activo, marco, decision = partes
                tuplas.add((strategy, f"{activo}#{marco}", decision))
    return tuplas


def cargar_filas(tuplas):
    out = defaultdict(list)  # familia -> [(ts, py, pnl, ic_bucket_key)]
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("acierto") not in ("0", "1"):
                continue
            clave = (row["strategy"], row["subtype"], row["decision"])
            if clave not in tuplas:
                continue
            try:
                py = float(row["precio_yes_mercado"])
                pnl = float(row["pnl_neto"])
            except Exception:
                continue
            if row["decision"] == "BUY_NO":
                py = 1 - py
            py = min(0.999, max(0.001, py))
            acierto = int(row["acierto"])
            fam = _familia(row["strategy"])
            out[fam].append((row.get("prediction_timestamp", ""), py, pnl, acierto))
    return out


def shuffle_test(a, b, iters=ITERS):
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    na, nb = len(a), len(b)
    diff_real = a.mean() - b.mean()
    todos = np.concatenate([a, b])
    n = na + nb
    idx = _rng.random((iters, n)).argsort(axis=1)
    permutado = todos[idx]
    media_a = permutado[:, :na].mean(axis=1)
    media_b = permutado[:, na:].mean(axis=1)
    diffs = media_a - media_b
    p_valor = float(np.mean(np.abs(diffs) >= abs(diff_real)))
    return float(diff_real), p_valor


def bh_fdr_signif(p_valores, q=0.05):
    n = len(p_valores)
    if n == 0:
        return set()
    orden = sorted(range(n), key=lambda i: p_valores[i])
    corte = -1
    for rank, i in enumerate(orden, start=1):
        if p_valores[i] <= (rank / n) * q:
            corte = rank
    if corte == -1:
        return set()
    return set(orden[:corte])


def wilson_ci(k, n, z=1.645):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((centro - margen) / denom, (centro + margen) / denom)


def main():
    universo = cargar_universo()
    filas_por_familia = cargar_filas(universo)
    print(f"Familias: {list(filas_por_familia.keys())}")

    resultado = {}
    pendientes = []
    for fam, filas in filas_por_familia.items():
        print(f"\n=== {fam} (n_total={len(filas)}) ===")
        por_bucket = defaultdict(list)
        for ts, py, pnl, acierto in filas:
            por_bucket[bucket(py)].append((ts, py, pnl, acierto))

        tabla = {}
        for b in sorted(por_bucket):
            dentro = por_bucket[b]
            fuera = [(ts, py, pnl, ac) for bb, fs in por_bucket.items() if bb != b for ts, py, pnl, ac in fs]
            n_d = len(dentro)
            pnl_d = [pnl for _, _, pnl, _ in dentro]
            pnl_f = [pnl for _, _, pnl, _ in fuera]
            wins = sum(ac for _, _, _, ac in dentro)
            p_hat = wins / n_d if n_d else 0.0
            pi_medio = sum(py for _, py, _, _ in dentro) / n_d if n_d else 0.0
            ic_bayes = (wins + 1) / (n_d + 2) - 0.5
            f_actual = abs(ic_bayes) * 0.5
            f_exacto = max(0.0, (p_hat - pi_medio) / (1 - pi_medio)) * 0.5
            ratio = (f_exacto / f_actual) if f_actual > 1e-9 else None
            wilson_lo, wilson_hi = wilson_ci(wins, n_d) if n_d else (0.0, 0.0)

            entrada = {
                "n": n_d, "hit": round(p_hat, 4), "pi_medio": round(pi_medio, 4),
                "pnl_medio": round(sum(pnl_d) / n_d, 4) if n_d else None,
                "f_actual": round(f_actual, 5), "f_exacto": round(f_exacto, 5),
                "ratio_correccion": round(ratio, 3) if ratio is not None else None,
                "wilson90": [round(wilson_lo, 3), round(wilson_hi, 3)],
                "shuffle_p": None, "split_half_diff": None, "veredicto": "sin_concluir",
            }
            tabla[f"{b:.2f}"] = entrada

            if n_d >= N_MIN and pnl_f:
                diff, p_valor = shuffle_test(pnl_d, pnl_f)
                entrada["shuffle_p"] = round(p_valor, 4)
                dentro_sorted = sorted(dentro, key=lambda x: x[0])
                mid = n_d // 2
                m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
                if len(m1) >= 5 and len(m2) >= 5:
                    media_fuera = sum(pnl_f) / len(pnl_f)
                    d1 = sum(pnl for _, _, pnl, _ in m1) / len(m1) - media_fuera
                    d2 = sum(pnl for _, _, pnl, _ in m2) / len(m2) - media_fuera
                    entrada["split_half_diff"] = [round(d1, 4), round(d2, 4)]
                    consistente = (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)
                    if consistente:
                        pendientes.append({"fam": fam, "bucket": f"{b:.2f}", "entrada": entrada,
                                            "p": p_valor, "diff": diff})
        resultado[fam] = tabla

    p_valores = [p["p"] for p in pendientes]
    sobreviven = bh_fdr_signif(p_valores, q=P_MAX)
    print(f"\nTests candidatos: {len(pendientes)} | sobreviven BH-FDR q={P_MAX}: {len(sobreviven)}")

    for idx, p in enumerate(pendientes):
        veredicto = "confirmado" if idx in sobreviven else "sin_concluir"
        p["entrada"]["veredicto"] = veredicto

    print("\n" + "=" * 100)
    print(f"{'Familia':32s} {'bucket':>7s} {'n':>5s} {'hit':>6s} {'pi':>6s} {'pnl/tr':>8s} {'f_act':>7s} {'f_exac':>7s} {'ratio':>6s} {'shuf_p':>7s} {'vered':>12s}")
    for fam, tabla in resultado.items():
        for b, e in sorted(tabla.items()):
            if e["n"] < N_MIN:
                continue
            print(f"{fam:32s} {b:>7s} {e['n']:>5d} {e['hit']*100:>5.1f}% {e['pi_medio']:>6.3f} "
                  f"{e['pnl_medio']:>+8.3f} {e['f_actual']:>7.4f} {e['f_exacto']:>7.4f} "
                  f"{(str(e['ratio_correccion'])+'x') if e['ratio_correccion'] is not None else '-':>7s} "
                  f"{str(e['shuffle_p']):>7s} {e['veredicto']:>12s}")

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({"generado_utc": __import__("datetime").datetime.utcnow().isoformat() + "Z",
                    "step": STEP, "n_min": N_MIN, "p_max": P_MAX, "familias": resultado},
                   f, indent=2, ensure_ascii=False)
    print(f"\nEscrito {OUT}")


if __name__ == "__main__":
    main()
