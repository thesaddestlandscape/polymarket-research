#!/usr/bin/env python3
"""Wang Transform (Yang 2026, ver idea_awesome_quant_hallazgos_13jul) contra
FAVORITO_CONFIRMADO: ¿el sesgo favorito-longshot que el paper formaliza
(p_mercado = Phi(Phi^-1(p_real) + lambda), lambda_hat=0.183 global,
calibrado sobre 291k contratos de dias/meses) replica en nuestra escala de
minutos?

FAVORITO_CONFIRMADO ya apuesta CON el lado que el mercado favorece (no
tiene modelo propio de pricing, es model-free) -- es exactamente el test
correcto: para cada prediccion, el precio del lado apostado (py si
BUY_YES, 1-py si BUY_NO) es la probabilidad "de mercado" del lado
favorito. Comparamos esa probabilidad cruda contra la tasa de acierto
REAL, bucketizada por distancia a 0.5, y probamos si corregir con el Wang
Transform (lambda=0.183) da una probabilidad mejor calibrada que la cruda.

Metodologia: reliability diagram (mismo patron que
idea_bayes_calibracion_bot_12jul) + comparacion de log-loss/Brier entre
(a) probabilidad cruda del mercado, (b) probabilidad corregida con Wang
Transform. NO toca shadow_predict.py ni ninguna decision -- solo lectura
de results.csv historico. Correr desde la raiz del repo:
python3 analisis_wang_transform_favorito.py
"""
import csv
import math

RESULTS = "data/shadow/results.csv"
WANG_LAMBDA = 0.183


def norm_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def norm_ppf(p, lo=-8.0, hi=8.0, it=60):
    if p <= 0:
        return lo
    if p >= 1:
        return hi
    for _ in range(it):
        mid = (lo + hi) / 2
        if norm_cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def cargar_favorito():
    rows = []
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["strategy"] != "FAVORITO_CONFIRMADO":
                continue
            try:
                py = float(r["precio_yes_mercado"])
                dec = r["decision"]
                acierto = int(r["acierto"])
            except (ValueError, TypeError):
                continue
            if dec == "BUY_YES":
                p_favorito = py
            elif dec == "BUY_NO":
                p_favorito = 1 - py
            else:
                continue
            if not (0.001 < p_favorito < 0.999):
                continue
            rows.append({
                "p_mercado": p_favorito,
                "acierto": acierto,
                "subtype": r.get("subtype", ""),
                "ts": r.get("resolution_timestamp", ""),
            })
    return rows


def brier(rows, prob_key):
    return sum((r[prob_key] - r["acierto"]) ** 2 for r in rows) / len(rows)


def log_loss(rows, prob_key):
    eps = 1e-6
    total = 0.0
    for r in rows:
        p = min(max(r[prob_key], eps), 1 - eps)
        total += -(r["acierto"] * math.log(p) + (1 - r["acierto"]) * math.log(1 - p))
    return total / len(rows)


def main():
    rows = cargar_favorito()
    print(f"n_total FAVORITO_CONFIRMADO (BUY_YES+BUY_NO) = {len(rows)}")
    print(f"p_mercado medio = {sum(r['p_mercado'] for r in rows)/len(rows):.4f}")
    print(f"acierto medio (win rate real)  = {sum(r['acierto'] for r in rows)/len(rows):.4f}")
    print()

    # Wang-corrected probability para cada fila
    for r in rows:
        z = norm_ppf(r["p_mercado"])
        r["p_wang"] = norm_cdf(z - WANG_LAMBDA)

    # Reliability diagram: bucket por p_mercado (deciles)
    rows_sorted = sorted(rows, key=lambda r: r["p_mercado"])
    n = len(rows_sorted)
    n_buckets = 10
    print(f"{'bucket':>8} {'n':>5} {'p_mercado_medio':>16} {'p_wang_medio':>13} {'win_real':>9} {'gap_mercado':>12} {'gap_wang':>9}")
    for i in range(n_buckets):
        lo = i * n // n_buckets
        hi = (i + 1) * n // n_buckets
        sub = rows_sorted[lo:hi]
        if not sub:
            continue
        p_mkt = sum(r["p_mercado"] for r in sub) / len(sub)
        p_wang = sum(r["p_wang"] for r in sub) / len(sub)
        win_real = sum(r["acierto"] for r in sub) / len(sub)
        print(f"{i:>8} {len(sub):>5} {p_mkt:>16.4f} {p_wang:>13.4f} {win_real:>9.4f} "
              f"{p_mkt-win_real:>+12.4f} {p_wang-win_real:>+9.4f}")

    print()
    b_mkt = brier(rows, "p_mercado")
    b_wang = brier(rows, "p_wang")
    ll_mkt = log_loss(rows, "p_mercado")
    ll_wang = log_loss(rows, "p_wang")
    print(f"Brier score:  mercado_crudo={b_mkt:.5f}  wang_corregido={b_wang:.5f}  "
          f"({'MEJORA' if b_wang < b_mkt else 'EMPEORA'} el Wang Transform)")
    print(f"Log-loss:     mercado_crudo={ll_mkt:.5f}  wang_corregido={ll_wang:.5f}  "
          f"({'MEJORA' if ll_wang < ll_mkt else 'EMPEORA'} el Wang Transform)")

    # Por subtype (activo#horizonte) para ver si el patron es consistente
    print()
    print("--- Por subtype (n>=40) ---")
    subtypes = sorted(set(r["subtype"] for r in rows))
    for st in subtypes:
        sub = [r for r in rows if r["subtype"] == st]
        if len(sub) < 40:
            continue
        b_m = brier(sub, "p_mercado")
        b_w = brier(sub, "p_wang")
        print(f"  {st:20s} n={len(sub):4d}  brier_mercado={b_m:.4f}  brier_wang={b_w:.4f}  "
              f"{'mejora' if b_w<b_m else 'empeora'}")


if __name__ == "__main__":
    main()
