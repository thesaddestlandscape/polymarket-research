#!/usr/bin/env python3
"""
analisis_kelly_exacto_desagregado_23jul.py -- P28 punto 4 (petición Javi
23-Jul, "hacerlo PERFECTO, por moneda, franja horaria, timing, bucket
grande y micro-bucket"): cuantifica cuánto cambiaría el stake real bajo
la fórmula de Kelly EXACTA para apuestas binarias, f*=(p-pi)/(1-pi),
frente al sizing actual (live_stake.py::calcular_stake, que usa IC
directamente sin dividir por (1-pi)) -- ver idea_kelly_ic_vs_formula_
exacta_precio_21jul.

Metodología por CADA tupla live (cada una ya fija una moneda/marco/
dirección, así que "por moneda" = una fila por tupla), desagregado
DENTRO de cada tupla por:
  1. franja horaria (hora_utc, bloques de 4h UTC)
  2. timing (T_h/restante_min, terciles)
  3. bucket grande de precio (paso 0.20, perspectiva de la decisión)
  4. micro-bucket de precio (paso 0.05) DENTRO del bucket grande con
     más n, para no fingir precisión donde no la hay

f_actual se aproxima con la MISMA fórmula que live_stake.py::calcular_
stake (ic_bayes * 0.5, half-Kelly, sin tope de bankroll/cap en euros
para que la comparación sea de FRACCIÓN, no de euros concretos).
f_exacto = max(0, (p_hat - pi_medio) / (1 - pi_medio)) * 0.5 (mismo
half-Kelly aplicado a ambas fórmulas, para que la comparación sea
limpia sobre la fórmula base, no sobre si se usa full o half Kelly).

Solo lectura. No toca live_stake.py ni ningún stake real.
"""
import csv
import sys
from pathlib import Path
from collections import defaultdict

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data" / "shadow" / "results.csv"
N_MIN = 15


def _ic_bayes(wins, n):
    if n == 0:
        return 0.0
    return (wins + 1) / (n + 2) - 0.5


def _precio_perspectiva(row):
    p = float(row["precio_yes_mercado"])
    if row["decision"] == "BUY_NO":
        p = 1 - p
    return min(0.999, max(0.001, p))


def _hora(row):
    ts = row.get("resolution_timestamp", "")
    try:
        return int(ts[11:13]) if len(ts) >= 13 else None
    except Exception:
        return None


def _resumen(rows, nombre):
    n = len(rows)
    if n < N_MIN:
        print(f"    {nombre}: n={n} < {N_MIN}, sin concluir")
        return
    wins = sum(1 for r in rows if r["acierto"] == "1")
    p_hat = wins / n
    ic = _ic_bayes(wins, n) * min(1.0, n / 20)
    pi_medio = sum(_precio_perspectiva(r) for r in rows) / n
    f_actual = abs(ic) * 0.5
    f_exacto = max(0.0, (p_hat - pi_medio) / (1 - pi_medio)) * 0.5
    ratio = f_exacto / f_actual if f_actual > 1e-9 else float("inf")
    print(f"    {nombre}: n={n:<5} hit={p_hat:.1%} pi_medio={pi_medio:.3f} "
          f"f_actual={f_actual:.4f} f_exacto={f_exacto:.4f} ratio={ratio:.2f}x")


def analizar_tupla(strategy, subtype, decision):
    rows = [
        r for r in csv.DictReader(open(RESULTS, encoding="utf-8"))
        if r["strategy"] == strategy and r["subtype"] == subtype
        and r["decision"] == decision and r.get("acierto") in ("0", "1")
    ]
    tup = f"{strategy}#{subtype}#{decision}"
    print(f"\n=== {tup} (moneda={subtype.split('#')[0]}) ===")
    _resumen(rows, "TOTAL")

    print("  --- franja horaria (bloques 4h UTC) ---")
    por_hora = defaultdict(list)
    for r in rows:
        h = _hora(r)
        if h is not None:
            por_hora[h // 4].append(r)
    for bloque in sorted(por_hora):
        _resumen(por_hora[bloque], f"[{bloque*4:02d}h-{bloque*4+4:02d}h)")

    print("  --- timing (T_h, terciles) ---")
    import json
    th_rows = []
    for r in rows:
        try:
            feats = json.loads(r["features"] or "{}")
        except Exception:
            continue
        th = feats.get("T_h")
        if th is not None:
            th_rows.append((th, r))
    if len(th_rows) >= N_MIN:
        th_rows.sort(key=lambda x: x[0])
        n = len(th_rows)
        t1, t2 = th_rows[n // 3][0], th_rows[2 * n // 3][0]
        bajo = [r for th, r in th_rows if th <= t1]
        medio = [r for th, r in th_rows if t1 < th < t2]
        alto = [r for th, r in th_rows if th >= t2]
        _resumen(bajo, f"tercio bajo T_h<={t1:.2f}")
        _resumen(medio, "tercio medio")
        _resumen(alto, f"tercio alto T_h>={t2:.2f}")
    else:
        print(f"    T_h disponible en n={len(th_rows)} < {N_MIN}, sin concluir")

    print("  --- bucket grande de precio (paso 0.20) ---")
    por_grande = defaultdict(list)
    for r in rows:
        p = _precio_perspectiva(r)
        b = round((p // 0.20) * 0.20, 2)
        por_grande[b].append(r)
    mejor_bucket, mejor_n = None, 0
    for b in sorted(por_grande):
        sub = por_grande[b]
        _resumen(sub, f"[{b:.2f},{b+0.20:.2f})")
        if len(sub) > mejor_n:
            mejor_bucket, mejor_n = b, len(sub)

    if mejor_bucket is not None and mejor_n >= N_MIN:
        print(f"  --- micro-bucket (paso 0.05) dentro de [{mejor_bucket:.2f},{mejor_bucket+0.20:.2f}), el de más n ---")
        por_micro = defaultdict(list)
        for r in por_grande[mejor_bucket]:
            p = _precio_perspectiva(r)
            b = round((p // 0.05) * 0.05, 3)
            por_micro[b].append(r)
        for b in sorted(por_micro):
            _resumen(por_micro[b], f"[{b:.2f},{b+0.05:.2f})")


if __name__ == "__main__":
    TUPLAS_LIVE = [
        ("FAVORITO_CONFIRMADO", "SOL#15min", "BUY_YES"),
        ("FAVORITO_CONFIRMADO", "SOL#60min", "BUY_YES"),
        ("FAVORITO_CONFIRMADO", "BTC#60min", "BUY_NO"),
        ("UPDOWN_GBM_15M_TARDIO", "BTC#15min", "BUY_YES"),
        ("FAVORITO_CONFIRMADO", "ETH#15min", "BUY_YES"),
        ("BALLENAS_TARDIAS", "BTC#15min", "BUY_YES"),
        ("GBM_LATE_15M", "ETH#15min", "BUY_YES"),
        ("FAVORITO_CONFIRMADO", "BTC#60min", "BUY_YES"),
    ]
    if len(sys.argv) >= 4:
        analizar_tupla(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        for strat, sub, dec in TUPLAS_LIVE:
            analizar_tupla(strat, sub, dec)
