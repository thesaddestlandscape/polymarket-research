#!/usr/bin/env python3
"""Propuesta #8 backlog quant-desk (13-jul): ¿coincidencia/discrepancia entre
estrategias en el mismo market_id predice el acierto? Solo lectura, no toca
predict/live. Fuente: data/shadow/results.csv + strategy_params.json.

Uso: python3 analisis_ensemble_estrategias.py
"""
import csv
import json
import math
from collections import defaultdict

RESULTS_CSV = "data/shadow/results.csv"
STRATEGY_PARAMS = "data/shadow/strategy_params.json"
LIVE_STRATS = {"GBM_LATE_15M", "GBM_LATE_15M_ESPACIO_ATR",
               "GBM_LATE_15M_TARDIO", "FAVORITO_CONFIRMADO"}
GBM_FAM = {"GBM_LATE_15M", "GBM_LATE_15M_ESPACIO_ATR", "GBM_LATE_15M_TARDIO"}


def ic_de(sp, strategy):
    return sp.get(strategy, {}).get("ic_bayes")


def prop_z(k, n, p0=0.5):
    if n == 0:
        return None
    p = k / n
    return (p - p0) / math.sqrt(p0 * (1 - p0) / n)


def main():
    rows = list(csv.DictReader(open(RESULTS_CSV)))
    sp = json.load(open(STRATEGY_PARAMS))["estrategias"]

    by_market = defaultdict(list)
    for r in rows:
        by_market[r["market_id"]].append(r)

    def bucket(strategy_filter=None):
        n_sola = w_sola = n_agree = w_agree = n_dis = w_dis = 0
        for mid, rs in by_market.items():
            if strategy_filter:
                rs = [r for r in rs if r["strategy"] in strategy_filter]
            uniq = {}
            for r in rs:
                uniq.setdefault(r["strategy"], r)
            strategies = set(uniq.keys())
            decs = set(r["decision"] for r in uniq.values())
            for r in uniq.values():
                try:
                    w = int(r["acierto"])
                except (ValueError, KeyError):
                    continue
                if len(strategies) == 1:
                    n_sola += 1; w_sola += w
                elif len(decs) == 1:
                    n_agree += 1; w_agree += w
                else:
                    n_dis += 1; w_dis += w
        return (n_sola, w_sola, n_agree, w_agree, n_dis, w_dis)

    print("=" * 70)
    print("TODAS las estrategias shadow")
    n_sola, w_sola, n_agree, w_agree, n_dis, w_dis = bucket()
    print(f"sola:      n={n_sola:5d}  hit={100*w_sola/n_sola:.1f}%")
    print(f"coinciden: n={n_agree:5d}  hit={100*w_agree/n_agree:.1f}%")
    print(f"discrepan: n={n_dis:5d}  hit={100*w_dis/n_dis:.1f}%")

    print()
    print("=" * 70)
    print(f"SOLO estrategias live hoy: {sorted(LIVE_STRATS)}")
    n_sola, w_sola, n_agree, w_agree, n_dis, w_dis = bucket(LIVE_STRATS)
    print(f"sola:      n={n_sola:5d}  hit={100*w_sola/n_sola:.1f}%" if n_sola else "sola: n/a")
    print(f"coinciden: n={n_agree:5d}  hit={100*w_agree/n_agree:.1f}%  z(vs 53%)~ver script completo" if n_agree else "coinciden: n/a")
    print(f"discrepan: n={n_dis:5d}  hit={100*w_dis/n_dis:.1f}%" if n_dis else "discrepan: n/a")

    # En discrepancia: ¿gana más veces la estrategia con mayor ic_bayes vigente?
    print()
    print("=" * 70)
    print("Discrepancia (decisión distinta, mismo market_id): ¿gana el de mayor IC?")
    for label, strat_filter in [("todas", None), ("solo live hoy", LIVE_STRATS)]:
        mayor = menor = 0
        for mid, rs in by_market.items():
            if strat_filter:
                rs = [r for r in rs if r["strategy"] in strat_filter]
            uniq = {}
            for r in rs:
                uniq.setdefault(r["strategy"], r)
            strat_list = list(uniq.values())
            for i in range(len(strat_list)):
                for j in range(i + 1, len(strat_list)):
                    a, b = strat_list[i], strat_list[j]
                    if a["decision"] == b["decision"]:
                        continue
                    ica, icb = ic_de(sp, a["strategy"]), ic_de(sp, b["strategy"])
                    if ica is None or icb is None or ica == icb:
                        continue
                    hi, lo = (a, b) if ica > icb else (b, a)
                    try:
                        w_hi, w_lo = int(hi["acierto"]), int(lo["acierto"])
                    except (ValueError, KeyError):
                        continue
                    if w_hi and not w_lo:
                        mayor += 1
                    elif w_lo and not w_hi:
                        menor += 1
        n = mayor + menor
        z = prop_z(mayor, n) if n else None
        print(f"[{label}] mayor-IC gana={mayor} menor-IC gana={menor} "
              f"n={n} pct_mayor={100*mayor/n:.1f}% z={z:.2f}" if n else f"[{label}] n/a")

    # Discrepancia intra-familia GBM vs FAVORITO-vs-GBM (genuinamente distintos)
    print()
    print("=" * 70)
    print("Discrepancia intra-familia GBM vs FAVORITO-vs-GBM (modelos genuinamente distintos)")
    n_intra = w_intra = n_cross = w_cross = 0
    for mid, rs in by_market.items():
        rs_live = [r for r in rs if r["strategy"] in LIVE_STRATS]
        uniq = {}
        for r in rs_live:
            uniq.setdefault(r["strategy"], r)
        if len(uniq) < 2:
            continue
        decs = set(r["decision"] for r in uniq.values())
        if len(decs) < 2:
            continue
        strat_set = set(uniq.keys())
        es_cross = "FAVORITO_CONFIRMADO" in strat_set and bool(strat_set & GBM_FAM)
        for r in uniq.values():
            try:
                w = int(r["acierto"])
            except (ValueError, KeyError):
                continue
            if es_cross:
                n_cross += 1; w_cross += w
            else:
                n_intra += 1; w_intra += w
    print(f"intra-familia GBM: n={n_intra} hit={100*w_intra/n_intra:.1f}%" if n_intra else "n/a")
    print(f"FAVORITO vs GBM:   n={n_cross} hit={100*w_cross/n_cross:.1f}%" if n_cross else "n/a")


if __name__ == "__main__":
    main()
