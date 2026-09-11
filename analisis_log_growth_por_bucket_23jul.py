#!/usr/bin/env python3
"""
analisis_log_growth_por_bucket_23jul.py -- P28 punto 2 (petición Javi
23-Jul): extiende analisis_log_growth.py (gate de crecimiento geométrico
por tupla completa) a DOS niveles -- bucket grande de precio de entrada
y micro-bucket dentro de cada bucket grande -- para encontrar, dentro de
una tupla con payout inverso confirmado, si hay una franja de precio
donde el crecimiento es especialmente negativo (candidata a excluir) u
otra donde es positivo/menos malo (candidata a apostar más, sizing
diferenciado por micro-bucket en vez de uno solo por tupla).

Reutiliza _retorno() de analisis_log_growth.py (misma fórmula exacta,
no reimplementada) -- SLIPPAGE, convención BUY_NO invertido, etc.

Solo lectura. No toca prob_yes, decision ni ningún gate real.
"""
import csv
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_log_growth import _retorno, N_MIN, SLIPPAGE  # noqa: E402

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data" / "shadow" / "results.csv"
F = 0.10  # misma fracción de referencia que analisis_log_growth.py


def _gate_rows(rows):
    n = len(rows)
    if n == 0:
        return None
    rs = [_retorno(r) for r in rows]
    hit = 100 * sum(1 for r in rows if r["acierto"] == "1") / n
    ev = sum(rs) / n
    g = sum(math.log(1 + F * x) for x in rs) / n
    return {"n": n, "hit_pct": hit, "ev_por_dolar": ev, "growth": g,
            "pasa": n >= N_MIN and g > 0}


def _precio_perspectiva_decision(row):
    """precio desde la perspectiva de la decisión tomada (para bucketizar
    de forma consistente con _retorno: BUY_NO se invierte)."""
    p = float(row["precio_yes_mercado"])
    if row["decision"] == "BUY_NO":
        p = 1 - p
    return min(0.999, max(0.001, p))


def analizar_tupla(strategy, subtype, decision, bucket_grande=0.20, bucket_micro=0.05):
    rows = [
        r for r in csv.DictReader(open(RESULTS, encoding="utf-8"))
        if r["strategy"] == strategy and r["subtype"] == subtype
        and r["decision"] == decision and r.get("acierto") in ("0", "1")
    ]
    tup = f"{strategy}#{subtype}#{decision}"
    total = _gate_rows(rows)
    if total is None:
        print(f"{tup}: sin filas")
        return
    print(f"\n=== {tup} — TOTAL: n={total['n']} hit={total['hit_pct']:.1f}% "
          f"EV/$={total['ev_por_dolar']:+.3f} g(f=10%)={total['growth']:+.5f} "
          f"-> {'PASA' if total['pasa'] else 'NO — payout inverso' if total['n']>=N_MIN else 'n<15'}")

    for r in rows:
        r["_p"] = _precio_perspectiva_decision(r)

    # bucket grande
    por_grande = {}
    lo = 0.0
    while lo < 1.0:
        hi = round(lo + bucket_grande, 3)
        sub = [r for r in rows if lo <= r["_p"] < hi]
        por_grande[(lo, hi)] = sub
        lo = hi

    print(f"  --- bucket grande (paso {bucket_grande}) ---")
    for (lo, hi), sub in por_grande.items():
        g = _gate_rows(sub)
        if g is None:
            continue
        flag = "PASA" if g["pasa"] else ("NO" if g["n"] >= N_MIN else "n<15")
        print(f"    [{lo:.2f},{hi:.2f}): n={g['n']:<5} hit={g['hit_pct']:5.1f}% "
              f"EV/$={g['ev_por_dolar']:+.3f} g={g['growth']:+.5f}  {flag}")

    # micro-bucket dentro de CADA bucket grande con n suficiente para desglosar
    print(f"  --- micro-bucket (paso {bucket_micro}) dentro de cada bucket grande ---")
    for (lo_g, hi_g), sub_g in por_grande.items():
        if len(sub_g) < N_MIN:
            continue
        print(f"    dentro de [{lo_g:.2f},{hi_g:.2f}):")
        lo = lo_g
        while lo < hi_g:
            hi = round(lo + bucket_micro, 3)
            sub = [r for r in sub_g if lo <= r["_p"] < hi]
            g = _gate_rows(sub)
            if g is not None and g["n"] > 0:
                flag = "PASA" if g["pasa"] else ("NO" if g["n"] >= N_MIN else "n<15")
                print(f"      [{lo:.2f},{hi:.2f}): n={g['n']:<4} hit={g['hit_pct']:5.1f}% "
                      f"EV/$={g['ev_por_dolar']:+.3f} g={g['growth']:+.5f}  {flag}")
            lo = hi


if __name__ == "__main__":
    TUPLAS_PAYOUT_INVERSO = [
        ("FAVORITO_CONFIRMADO", "BTC#15min", "BUY_NO"),
        ("FAVORITO_CONFIRMADO", "SOL#15min", "BUY_NO"),
        ("FAVORITO_CONFIRMADO", "ETH#15min", "BUY_NO"),
        ("FAVORITO_CONFIRMADO", "ETH#60min", "BUY_NO"),
    ]
    for strat, sub, dec in TUPLAS_PAYOUT_INVERSO:
        analizar_tupla(strat, sub, dec)
