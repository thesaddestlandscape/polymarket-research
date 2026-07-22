#!/usr/bin/env python3
"""analisis_randomized_oos.py — hueco de robustez #3 (último) de
`idea_huecos_robustez_metodologia_21jul` (checklist de 10 tests quant,
Javi 21-Jul). Cierra el trío junto con Parameter Stability (22-Jul, barre
el umbral) y Noise Test (22-Jul, perturba la feature) -- este ataca el
split train/test.

Problema: la validación walk-forward del proyecto (analisis_embargo_
train_test.py, P17) y el criterio de "n forward desde promoción" usan
SIEMPRE el corte cronológico fijo más reciente como test -- nunca se
comprueba si ESE periodo concreto (el más reciente) resultó ser atípico
por puro azar. Si el mercado tuvo un régimen inusualmente bueno/malo justo
en las últimas semanas, ninguna estrategia lo sabría con el método actual.

Método: para cada tupla de dinero real (pares_permitidos_live) y
candidatos, ordena las filas resueltas cronológicamente, calcula el gate()
estándar (analisis_gate_riguroso.py, Wilson+shuffle+PnL bootstrap -- MISMO
criterio que ya decide promoción, no uno nuevo) sobre el 30% final
(walk-forward estándar, baseline) y sobre N ventanas de test de ESE MISMO
TAMAÑO pero posicionadas aleatoriamente en cualquier punto del histórico
disponible (bloques contiguos -- preserva autocorrelación temporal, no es
un shuffle fila a fila). Compara dónde cae el resultado del 30% final
dentro de la distribución de resultados de ventanas aleatorias.

Solo lectura. No decide nada, no toca config_live.json ni ningún gate real.
"""
import argparse
import csv
import random
from collections import defaultdict
from datetime import datetime, timezone

from analisis_gate_riguroso import RES, CONFIG_LIVE, gate
from analisis_embargo_train_test import cargar_tuplas

TEST_FRAC = 0.30
N_RANDOM = 60  # gate() hace bootstrap n_boot=5000 (analisis_gate_riguroso.N_SHUFFLE) por
               # ventana -- 300 era inviable en tiempo real con >200 candidatos, ver commit
SEED = 22072026
N_MIN_TOTAL = 40  # por debajo de esto ni el walk-forward estándar tiene sentido


def _ts_pred(row):
    try:
        ts = datetime.fromisoformat(row["prediction_timestamp"].replace("Z", "+00:00"))
        return ts if ts.tzinfo else ts.replace(tzinfo=timezone.utc)
    except Exception:
        return None


def cargar_filas_ordenadas(claves):
    wanted = {(s, sub, d) for _, s, sub, d in claves}
    filas = defaultdict(list)
    with open(RES, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("acierto") in (None, ""):
                continue
            k = (row["strategy"], row["subtype"], row["decision"])
            if k in wanted:
                filas[k].append(row)
    for k in filas:
        filas[k] = [r for r in filas[k] if _ts_pred(r) is not None]
        filas[k].sort(key=_ts_pred)
    return filas


def evaluar_tupla(tupla, rows, rng, n_random):
    n = len(rows)
    if n < N_MIN_TOTAL:
        return None
    n_test = max(int(n * TEST_FRAC), 15)
    if n_test >= n:
        return None

    test_reciente = rows[n - n_test:]
    g_reciente = gate(test_reciente)

    n_train_min = max(int(n * 0.10), 5)  # deja algo de margen antes del inicio del test
    max_start = n - n_test
    if max_start <= n_train_min:
        return None  # no hay hueco real para mover la ventana

    resultados_random = []
    for _ in range(n_random):
        start = rng.randrange(n_train_min, max_start + 1)
        ventana = rows[start:start + n_test]
        g = gate(ventana)
        if g:
            resultados_random.append(g)
    if not resultados_random:
        return None

    ics = sorted(g["ic"] for g in resultados_random)
    n_gate_ok = sum(1 for g in resultados_random if g["veredicto"] == "GATE OK")
    ic_reciente = g_reciente["ic"] if g_reciente else None
    percentil = (sum(1 for v in ics if v <= ic_reciente) / len(ics)) if ic_reciente is not None else None

    return {
        "tupla": tupla, "n_total": n, "n_test": n_test,
        "g_reciente": g_reciente,
        "n_ventanas_random": len(resultados_random),
        "pct_ventanas_gate_ok": round(n_gate_ok / len(resultados_random) * 100, 1),
        "ic_random_p10": round(ics[int(0.10 * len(ics))], 4),
        "ic_random_p50": round(ics[int(0.50 * len(ics))], 4),
        "ic_random_p90": round(ics[int(0.90 * len(ics))], 4),
        "percentil_ic_reciente": round(percentil * 100, 1) if percentil is not None else None,
    }


def reportar(titulo, claves, filas_por_clave, rng, n_random):
    print("=" * 78)
    print(titulo)
    print("=" * 78)
    for tupla, strat, sub, dec in claves:
        rows = filas_por_clave.get((strat, sub, dec), [])
        r = evaluar_tupla(tupla, rows, rng, n_random)
        if r is None:
            print(f"{tupla}: n insuficiente ({len(rows)}) para walk-forward randomizado (min {N_MIN_TOTAL})")
            continue
        gr = r["g_reciente"]
        veredicto_reciente = gr["veredicto"] if gr else "sin datos"
        ic_reciente = f"{gr['ic']:+.3f}" if gr else "—"
        print(f"\n{tupla}  (n_total={r['n_total']}, n_test={r['n_test']}, "
              f"{r['n_ventanas_random']} ventanas aleatorias evaluadas)")
        print(f"  30% MÁS RECIENTE (walk-forward estándar actual): IC={ic_reciente} -> {veredicto_reciente}")
        print(f"  Ventanas aleatorias del mismo tamaño en cualquier punto del histórico:")
        print(f"    IC  p10={r['ic_random_p10']:+.3f}  p50={r['ic_random_p50']:+.3f}  p90={r['ic_random_p90']:+.3f}")
        print(f"    % de ventanas que habrían dado GATE OK: {r['pct_ventanas_gate_ok']:.1f}%")
        if r["percentil_ic_reciente"] is not None:
            pct = r["percentil_ic_reciente"]
            print(f"    Percentil del IC del 30% reciente dentro de esa distribución: {pct:.1f}%")
            if pct >= 90:
                print("    ⚠️  El periodo de test actual está en el 10% MÁS FAVORABLE posible -- el "
                      "veredicto de promoción pudo depender de la suerte de qué ventana se usó, no solo del edge.")
            elif pct <= 10:
                print("    ⚠️  El periodo de test actual está en el 10% MENOS FAVORABLE posible -- una "
                      "estrategia con edge real podría estar siendo infravalorada por el corte actual.")


def ejecutar_live(n_random=N_RANDOM, seed=SEED):
    """Núcleo reutilizable para vigia_robustez_diaria.py -- solo las 8
    tuplas de dinero real (pares_permitidos_live), no candidatos (245
    tuplas es demasiado caro para un cron diario, ver docstring del
    módulo). Devuelve lista de dicts, uno por tupla evaluable."""
    rng = random.Random(seed)
    claves_live = cargar_tuplas("pares_permitidos_live")
    filas = cargar_filas_ordenadas(claves_live)
    out = []
    for tupla, strat, sub, dec in claves_live:
        rows = filas.get((strat, sub, dec), [])
        r = evaluar_tupla(tupla, rows, rng, n_random)
        if r is not None:
            out.append(r)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--candidatos", action="store_true",
                     help="incluir también candidatos_evaluacion_live (245 tuplas, mucho más lento)")
    ap.add_argument("--n-random", type=int, default=N_RANDOM)
    args = ap.parse_args()
    rng = random.Random(SEED)
    n_random = args.n_random

    print(f"Test: gate() estándar (Wilson+shuffle+PnL bootstrap, analisis_gate_riguroso.py) sobre el")
    print(f"{TEST_FRAC*100:.0f}% final (walk-forward actual) vs {n_random} ventanas del mismo tamaño en")
    print(f"posiciones aleatorias del histórico disponible (bloques contiguos, preserva autocorrelación).\n")

    claves_live = cargar_tuplas("pares_permitidos_live")
    reportar("DINERO REAL — pares_permitidos_live", claves_live, cargar_filas_ordenadas(claves_live), rng, n_random)

    if args.candidatos:
        print()
        claves_cand = cargar_tuplas("candidatos_evaluacion_live")
        reportar("CANDIDATOS — candidatos_evaluacion_live (shadow, sin riesgo)", claves_cand,
                  cargar_filas_ordenadas(claves_cand), rng, n_random)


if __name__ == "__main__":
    main()
