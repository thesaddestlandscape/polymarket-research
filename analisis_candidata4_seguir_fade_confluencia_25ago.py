#!/usr/bin/env python3
"""analisis_candidata4_seguir_fade_confluencia_25ago.py -- Candidata 4
(gallina de huevos de oro): doble confirmacion Wallet Mirror SEGUIR x
P31 FADE sobre el MISMO mercado. Cruza wallet_mirror_sniper_dry_run.csv
(tipo SEGUIR, implica direccion = lado_wallet) contra los trades de las
wallets FADE de p31_wallets_watchlist.json (via ballenas_timing_history.csv,
implica direccion = OPUESTA a compro_yes) por condition_id. Confluencia =
ambas implican la MISMA direccion real.

Solo lectura, no toca produccion.
"""
import csv
import json
from collections import defaultdict

WATCHLIST = "data/shadow/p31_wallets_watchlist.json"
SEGUIR = "data/shadow/wallet_mirror_sniper_dry_run.csv"
HIST = "data/shadow/ballenas_timing_history.csv"


def fade_wallets():
    d = json.load(open(WATCHLIST))
    ws = set()
    for combo in d["combos"].values():
        if combo["lado"] == "fade":
            for w in combo["wallets"]:
                ws.add(w.lower())
    return ws


def main():
    fw = fade_wallets()
    print(f"P31 fade wallets: {len(fw)}")

    # trades FADE por condition_id: direccion implicada = opuesta a compro_yes
    fade_por_cond = defaultdict(list)
    with open(HIST, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            w = r.get("wallet", "").lower()
            if w not in fw:
                continue
            cy = r.get("compro_yes")
            if cy not in ("0", "1", "True", "False"):
                continue
            compro_yes = cy in ("1", "True")
            direccion_implicada = "Down" if compro_yes else "Up"  # fade = opuesto
            fade_por_cond[r["condition_id"]].append({
                "wallet": w, "direccion": direccion_implicada,
                "acierto": r.get("acierto"), "ts": r.get("ts_trade"),
            })
    print(f"condition_ids con trade FADE: {len(fade_por_cond)}")

    # SEGUIR trades resueltos
    n_seguir = 0
    n_overlap_market = 0
    confluencia = []  # (acierto_seguir,) cuando coinciden
    discrepancia = []
    with open(SEGUIR, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("tipo") != "SEGUIR":
                continue
            if not r.get("outcome_real"):
                continue
            n_seguir += 1
            cond = r.get("condition_id")
            if cond not in fade_por_cond:
                continue
            n_overlap_market += 1
            direccion_seguir = r.get("lado_wallet")
            acierto = r.get("acierto")
            for fr in fade_por_cond[cond]:
                if fr["direccion"] == direccion_seguir:
                    confluencia.append(acierto)
                else:
                    discrepancia.append(acierto)

    print(f"SEGUIR resueltos: {n_seguir}")
    print(f"SEGUIR con overlap de mercado con alguna wallet FADE: {n_overlap_market}")

    def resumen(nombre, lista):
        n = len(lista)
        if n == 0:
            print(f"{nombre}: n=0")
            return
        hits = sum(1 for a in lista if a == "1")
        print(f"{nombre}: n={n} hit={hits/n*100:.1f}%")

    resumen("Confluencia (SEGUIR y FADE apuntan misma direccion)", confluencia)
    resumen("Discrepancia (SEGUIR y FADE apuntan direccion opuesta)", discrepancia)


if __name__ == "__main__":
    main()
