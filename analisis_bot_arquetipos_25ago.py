#!/usr/bin/env python3
"""
analisis_bot_arquetipos_25ago.py -- Candidata 11 (petición Javi 25-Ago,
"mira a ver la 11"): separa las 84 bot wallets (bot_wallets_universo_25ago.json)
en los 2 arquetipos ya vistos en el estudio de las 10 primeras
(project_wallet_bots_identificados_25ago) -- SNIPER (marco corto,
restante_min mediana pequeña) vs WEEKLY_TEMPRANO (marco weekly,
restante_min mediana grande) -- y mide edge_pp/g_kelly por arquetipo por
separado, cruzando con wallet_edge_score_por_activo_marco.json (hoy
mezclados en un solo universo sin distinguir).

Solo lectura. No promociona nada por sí solo.
"""
import csv
import json
from collections import defaultdict

import numpy as np

BOTS = json.load(open("data/shadow/bot_wallets_universo_25ago.json")).keys()
WEDGE = json.load(open("data/shadow/wallet_edge_score_por_activo_marco.json"))
UMBRAL_SNIPER_MIN = 5.0  # restante_min mediana <5min en marco corto -> sniper


def clasificar_wallets():
    """Para cada bot, marco dominante + restante_min mediana -> arquetipo."""
    por_wallet = defaultdict(lambda: defaultdict(list))  # wallet -> marco -> [restante_min]
    with open("data/shadow/ballenas_timing_history.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            w = r.get("wallet", "").lower()
            if w not in BOTS:
                continue
            try:
                rm = float(r["restante_min"])
            except (TypeError, ValueError):
                continue
            por_wallet[w][r.get("marco", "?")].append(rm)

    arquetipos = {}
    for w, marcos in por_wallet.items():
        marco_dom = max(marcos, key=lambda m: len(marcos[m]))
        restantes = marcos[marco_dom]
        mediana = float(np.median(restantes))
        if marco_dom in ("weekly",):
            arquetipo = "WEEKLY_TEMPRANO" if mediana > 500 else "WEEKLY_TARDIO"
        else:
            arquetipo = "SNIPER" if mediana <= UMBRAL_SNIPER_MIN else "DISPERSO"
        arquetipos[w] = {"marco_dominante": marco_dom, "restante_min_mediana": round(mediana, 2),
                          "arquetipo": arquetipo, "n_marco_dom": len(restantes)}
    return arquetipos


def main():
    arquetipos = clasificar_wallets()
    conteo = defaultdict(int)
    for w, info in arquetipos.items():
        conteo[info["arquetipo"]] += 1
    print("Distribución de arquetipos entre las 84 bot wallets:")
    for arq, n in sorted(conteo.items(), key=lambda kv: -kv[1]):
        print(f"  {arq}: {n}")

    # cruce con wallet_edge_score_por_activo_marco.json -- agregado ponderado por n
    por_arquetipo = defaultdict(lambda: {"n": 0, "hit_pond": 0.0, "edge_pp_pond": 0.0,
                                          "g_kelly_pond": 0.0, "n_combos": 0, "n_combos_sig": 0})
    for v in WEDGE.values():
        w = v.get("wallet", "").lower()
        if w not in arquetipos:
            continue
        arq = arquetipos[w]["arquetipo"]
        n = v.get("n", 0)
        d = por_arquetipo[arq]
        d["n"] += n
        d["hit_pond"] += (v.get("hit") or 0) * n
        d["edge_pp_pond"] += (v.get("edge_pp") or 0) * n
        d["g_kelly_pond"] += (v.get("g_kelly") or 0) * n
        d["n_combos"] += 1
        if v.get("sig_bhfdr"):
            d["n_combos_sig"] += 1

    print("\nAgregado ponderado por n de trades, por arquetipo (wallet_edge_score_por_activo_marco.json):")
    for arq, d in sorted(por_arquetipo.items(), key=lambda kv: -kv[1]["n"]):
        if d["n"] == 0:
            continue
        print(f"  {arq}: n_total={d['n']} combos={d['n_combos']} (sig={d['n_combos_sig']}) "
              f"hit_pond={d['hit_pond']/d['n']:.4f} edge_pp_pond={d['edge_pp_pond']/d['n']:+.3f} "
              f"g_kelly_pond={d['g_kelly_pond']/d['n']:+.6f}")

    print("\nDetalle por wallet (top 15 por n_marco_dom):")
    for w, info in sorted(arquetipos.items(), key=lambda kv: -kv[1]["n_marco_dom"])[:15]:
        print(f"  {w} {info}")


if __name__ == "__main__":
    main()
