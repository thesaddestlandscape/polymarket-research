"""P31 (11-Ago): gate riguroso pooled (Wilson+breakeven fee 7%+shuffle)
sobre TODOS los combos (activo,marco,lado) con >=2 wallets robustas
(mismo signo en split-half), usando el precio de la propia wallet como
proxy (mismo criterio que el gate inicial de XRP#15min) -- barrido rápido
para priorizar qué combos merecen el cruce con libro real (data/markets)
después. Solo lectura.
"""
import csv
import json
import math
from collections import defaultdict

import numpy as np

import shadow_postmortem as sp

FEE = 0.07
Z_90 = 1.645
MARCO_LARGO = {"5m": "5min", "15m": "15min", "60m": "60min", "240m": "240min"}


def wilson_lower(hits, n, z=Z_90):
    if n == 0:
        return 0.0
    p = hits / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centro - margen) / denom


def breakeven(p_held):
    gross_win = (1 - p_held) / p_held
    return 1 / (1 + gross_win * (1 - FEE))


def main():
    d = json.load(open("data/shadow/p31_splithalf_wallets.json"))
    robustos = [v for v in d.values() if v["mismo_signo"]]

    grupos = defaultdict(lambda: {"fade": set(), "follow": set()})
    for v in robustos:
        key = (v["activo"], v["marco"])
        lado = "fade" if v["edge2_pp"] < 0 else "follow"
        grupos[key][lado].add(v["wallet"])

    combos = []
    for key, g in grupos.items():
        for lado in ("fade", "follow"):
            if len(g[lado]) >= 2:
                combos.append((key[0], key[1], lado, g[lado]))

    wallet_membership = {}
    for (act, marco, lado, ws) in combos:
        for w in ws:
            wallet_membership.setdefault((w, act, marco), []).append(lado)

    filas_por_combo = {(a, m, lado): [] for (a, m, lado, _) in combos}
    with open("data/shadow/ballenas_timing_history.csv") as f:
        for row in csv.DictReader(f):
            key3 = (row.get("wallet"), row.get("activo"), row.get("marco"))
            lados = wallet_membership.get(key3)
            if not lados:
                continue
            marco_largo = MARCO_LARGO.get(row.get("marco"), row.get("marco"))
            if sp.es_pre_twap(marco_largo, row.get("ts_trade", "")):
                continue
            for lado in lados:
                filas_por_combo[(row["activo"], row["marco"], lado)].append(row)

    resultados = []
    for (act, marco, lado, ws) in combos:
        rows = filas_por_combo[(act, marco, lado)]
        n = len(rows)
        if n < 30:
            continue
        if lado == "fade":
            hits = sum(1 for r in rows if r.get("acierto") not in ("1", "True", "true"))
            p_sum = sum(1 - float(r["precio"]) for r in rows)
        else:
            hits = sum(1 for r in rows if r.get("acierto") in ("1", "True", "true"))
            p_sum = sum(float(r["precio"]) for r in rows)
        hit = hits / n
        p_medio = p_sum / n
        be = breakeven(p_medio)
        wl = wilson_lower(hits, n)
        rng = np.random.default_rng(abs(hash((act, marco, lado))) % (2**32))
        sim = rng.binomial(n, p_medio, size=10000) / n
        pval = float(np.mean(np.abs(sim - p_medio) >= abs(hit - p_medio)))
        margen = (wl - be) * 100
        resultados.append({
            "activo": act, "marco": marco, "lado": lado, "n_wallets": len(ws),
            "n_trades": n, "hit": round(hit, 4), "precio_medio": round(p_medio, 4),
            "breakeven": round(be, 4), "wilson90lo": round(wl, 4),
            "margen_pp": round(margen, 2), "p_shuffle": pval,
        })

    resultados.sort(key=lambda r: -r["margen_pp"])
    print(f"{'activo':6s} {'marco':6s} {'lado':6s} {'n_w':>4s} {'n_trades':>9s} "
          f"{'hit':>7s} {'precio':>7s} {'breakeven':>9s} {'wilson90lo':>10s} "
          f"{'margen_pp':>9s} {'p_shuf':>7s}  GATE")
    for r in resultados:
        pasa = r["margen_pp"] > 0 and r["p_shuffle"] < 0.05
        print(f"{r['activo']:6s} {r['marco']:6s} {r['lado']:6s} {r['n_wallets']:4d} "
              f"{r['n_trades']:9d} {r['hit']:7.4f} {r['precio_medio']:7.4f} "
              f"{r['breakeven']:9.4f} {r['wilson90lo']:10.4f} {r['margen_pp']:9.2f} "
              f"{r['p_shuffle']:7.4f}  {'✅ PASA' if pasa else ''}")

    json.dump(resultados, open("data/shadow/p31_gate_pooled_combos.json", "w"), indent=1)


if __name__ == "__main__":
    main()
