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
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

# 25-Ago: rutas relativas rompían en cron (cwd distinto de REPO,
# FileNotFoundError en candidata2_weekly_temprano_espejo_fase0.py que
# importa clasificar_wallets() -- 0 ejecuciones exitosas desde el
# despliegue). Resolver siempre contra el directorio del propio fichero,
# misma convención que el resto del proyecto.
REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
sys.path.insert(0, str(REPO))

BOTS = json.load(open(DIR_SHADOW / "bot_wallets_universo_25ago.json")).keys()
WEDGE = json.load(open(DIR_SHADOW / "wallet_edge_score_por_activo_marco.json"))
UMBRAL_SNIPER_MIN = 5.0  # restante_min mediana <5min en marco corto -> sniper


def clasificar_wallets():
    """Para cada bot, marco dominante + restante_min mediana -> arquetipo."""
    por_wallet = defaultdict(lambda: defaultdict(list))  # wallet -> marco -> [restante_min]
    with open(DIR_SHADOW / "ballenas_timing_history.csv", encoding="utf-8") as f:
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


def bucket(p):
    import math
    return round(math.floor(p / 0.05 + 1e-9) * 0.05, 4)


def main():
    arquetipos = clasificar_wallets()
    conteo = defaultdict(int)
    for w, info in arquetipos.items():
        conteo[info["arquetipo"]] += 1
    print("Distribución de arquetipos entre las 84 bot wallets:")
    for arq, n in sorted(conteo.items(), key=lambda kv: -kv[1]):
        print(f"  {arq}: {n}")

    # /code-review propio (25-Ago, corrección explícita Javi: "ya vuelves a
    # cagarla, hay que desagregar por activo, marco temporal Y micro-bucket
    # SIEMPRE", CLAUDE.md pt.17) -- el agregado por arquetipo del primer
    # intento mezclaba TODOS los activos/marcos/precios de las wallets de
    # ese arquetipo en un solo numero, exactamente lo que puede esconder un
    # micro-bucket de oro dentro de un arquetipo que en agregado parece malo
    # (o al reves: un arquetipo "bueno" en agregado que en realidad depende
    # de 1-2 combos, con el resto mediocre). Ahora se desagrega por
    # (arquetipo, activo, marco, bucket 0.05 de precio_medio) SIEMPRE.
    por_celda = defaultdict(lambda: {"n": 0, "hit_pond": 0.0, "edge_pp_pond": 0.0,
                                      "g_kelly_pond": 0.0, "n_combos": 0, "n_combos_sig": 0})
    for v in WEDGE.values():
        w = v.get("wallet", "").lower()
        if w not in arquetipos:
            continue
        precio_medio = v.get("precio_medio")
        if precio_medio is None:
            continue
        arq = arquetipos[w]["arquetipo"]
        celda = (arq, v.get("activo"), v.get("marco"), f"{bucket(precio_medio):.2f}")
        n = v.get("n", 0)
        d = por_celda[celda]
        d["n"] += n
        d["hit_pond"] += (v.get("hit") or 0) * n
        d["edge_pp_pond"] += (v.get("edge_pp") or 0) * n
        d["g_kelly_pond"] += (v.get("g_kelly") or 0) * n
        d["n_combos"] += 1
        if v.get("sig_bhfdr"):
            d["n_combos_sig"] += 1

    print(f"\nCeldas (arquetipo, activo, marco, bucket_precio): {len(por_celda)}")
    print("Celdas con n>=100 y g_kelly_pond>0 (candidatas reales, desagregadas):")
    celdas_buenas = [(k, d) for k, d in por_celda.items() if d["n"] >= 100 and d["g_kelly_pond"] / d["n"] > 0]
    for k, d in sorted(celdas_buenas, key=lambda kv: -kv[1]["g_kelly_pond"] / kv[1]["n"]):
        arq, activo, marco, b = k
        print(f"  {arq} {activo}#{marco}[{b}) n={d['n']} combos={d['n_combos']}(sig={d['n_combos_sig']}) "
              f"hit={d['hit_pond']/d['n']:.3f} edge_pp={d['edge_pp_pond']/d['n']:+.3f} "
              f"g_kelly={d['g_kelly_pond']/d['n']:+.6f}")

    print(f"\nTotal celdas buenas (n>=100, g_kelly_pond>0): {len(celdas_buenas)}")

    print("\nCeldas con n>=100 y g_kelly_pond<0 (para contraste, primeras 10 por -g_kelly):")
    celdas_malas = [(k, d) for k, d in por_celda.items() if d["n"] >= 100 and d["g_kelly_pond"] / d["n"] <= 0]
    for k, d in sorted(celdas_malas, key=lambda kv: kv[1]["g_kelly_pond"] / kv[1]["n"])[:10]:
        arq, activo, marco, b = k
        print(f"  {arq} {activo}#{marco}[{b}) n={d['n']} hit={d['hit_pond']/d['n']:.3f} "
              f"edge_pp={d['edge_pp_pond']/d['n']:+.3f} g_kelly={d['g_kelly_pond']/d['n']:+.6f}")


if __name__ == "__main__":
    main()
