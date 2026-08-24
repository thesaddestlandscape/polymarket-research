#!/usr/bin/env python3
"""
analisis_confluencia_rsn_botsnipers_25ago.py -- Candidata 1 "gallina de
los huevos de oro" (25-Ago, petición Javi): ¿confluye la dirección
implícita de Chainlink (RESOLUTION_SNIPER_NAIVE, ya en vivo 5min) con la
actividad de los bot-snipers identificados hoy en el mismo instante?

Solo lectura. No promociona nada por sí solo.
"""
import csv
import glob
from collections import defaultdict

import json
# 25-Ago: ampliado de 8 (top por volumen) a las 84 wallets bot confirmadas
# por analisis_bot_wallets_universo_25ago.py (trades/día>20, horas_activas
# >=20/24, TODAS con edge estadístico ya confirmado) -- petición explícita
# Javi: "no cojas solo las 8, coge las 50 wallets de bots".
BOT_WALLETS = set(json.load(open("data/shadow/bot_wallets_universo_25ago.json")).keys())


def cargar_bot_trades():
    """condition_id -> [(compro_yes_bool, restante_min), ...] para los 8 bot-sniper wallets, marco=5m."""
    out = defaultdict(list)
    n_filas = 0
    with open("data/shadow/ballenas_timing_history.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("marco") != "5m":
                continue
            if r.get("wallet", "").lower() not in BOT_WALLETS:
                continue
            n_filas += 1
            try:
                rm = float(r["restante_min"])
            except (TypeError, ValueError):
                rm = None
            out[r["condition_id"]].append((r.get("compro_yes") == "1", rm))
    print(f"[bots] filas matching wallet+marco=5m: {n_filas} | condition_ids únicos: {len(out)}")
    return out


def cargar_senales_rsn():
    rows = []
    for f in sorted(glob.glob("data/shadow/resolution_sniper_obs_*.csv")):
        rows.extend(csv.DictReader(open(f, encoding="utf-8")))
    print(f"[rsn] filas totales todos los ficheros: {len(rows)}")
    sub = []
    for r in rows:
        if r.get("marco") != "5min":
            continue
        if r.get("acierto_direccion_implicita") not in ("0", "1"):
            continue
        try:
            off = float(r["offset_s"])
        except (TypeError, ValueError):
            continue
        if not (0 <= off <= 3):
            continue
        dirimpl = r.get("chainlink_direccion_implicita")
        ask = r.get("ask_yes") if dirimpl == "Up" else r.get("ask_no")
        try:
            ask = float(ask)
        except (TypeError, ValueError):
            continue
        if not (0.05 <= ask <= 0.95):
            continue
        sub.append(r)
    print(f"[rsn] señales calificadas (5min, offset 0-3, ask en rango): {len(sub)}")
    return sub


def main():
    bots = cargar_bot_trades()
    senales = cargar_senales_rsn()

    cids_bot = set(bots.keys())
    cids_rsn = {r["condition_id"] for r in senales}
    print(f"overlap de condition_id (bot cids ∩ señales rsn cids): {len(cids_bot & cids_rsn)}")

    confluye_hit, confluye_n = 0, 0
    no_confluye_hit, no_confluye_n = 0, 0
    for r in senales:
        cid = r["condition_id"]
        dirimpl = r["chainlink_direccion_implicita"]
        trades = bots.get(cid, [])
        match = any(
            (compro_up and dirimpl == "Up") or (not compro_up and dirimpl == "Down")
            for compro_up, rm in trades
        )
        ac = int(r["acierto_direccion_implicita"])
        if match:
            confluye_n += 1
            confluye_hit += ac
        else:
            no_confluye_n += 1
            no_confluye_hit += ac

    print(f"\nCONFLUYE (bot-sniper misma dirección, cualquier restante_min): n={confluye_n} "
          f"hit={confluye_hit/confluye_n:.4f}" if confluye_n else "\nCONFLUYE: n=0")
    print(f"NO CONFLUYE: n={no_confluye_n} hit={no_confluye_hit/no_confluye_n:.4f}" if no_confluye_n else "NO CONFLUYE: n=0")


if __name__ == "__main__":
    main()
