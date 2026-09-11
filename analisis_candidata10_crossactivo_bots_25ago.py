#!/usr/bin/env python3
"""analisis_candidata10_crossactivo_bots_25ago.py -- Candidata 10: misma
bot wallet operando 2 activos distintos en ventana temporal corta --
¿el trade cruzado predice acierto mejor que operar sin confirmacion
cruzada? Usa bot_wallets_gate_bucket_fase0.csv (outcome_real ya resuelto).

Solo lectura.
"""
import csv
import math
import zlib
from collections import defaultdict
from datetime import datetime, timedelta

import numpy as np

IN = "data/shadow/bot_wallets_gate_bucket_fase0.csv"
VENTANA_MIN = 30
N_MIN = 15


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def shuffle_test_prop(hits_a, n_a, hits_b, n_b, iters=5000, seed_key="c10"):
    rng = np.random.default_rng(zlib.crc32(seed_key.encode("utf-8")))
    pool = np.array([1] * (hits_a + hits_b) + [0] * ((n_a - hits_a) + (n_b - hits_b)))
    diff_obs = hits_a / n_a - hits_b / n_b
    diffs = []
    for _ in range(iters):
        perm = rng.permutation(pool)
        pa = perm[:n_a].mean()
        pb = perm[n_a:n_a + n_b].mean()
        diffs.append(pa - pb)
    diffs = np.array(diffs)
    p = float(np.mean(np.abs(diffs) >= abs(diff_obs)))
    return diff_obs, p


def main():
    filas = []
    with open(IN, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("outcome_real") or not r.get("acierto"):
                continue
            filas.append(r)

    por_wallet = defaultdict(list)
    for r in filas:
        por_wallet[r["wallet"]].append(r)

    multi_activo_bots = 0
    for w, trs in por_wallet.items():
        if len({t["activo"] for t in trs}) >= 2:
            multi_activo_bots += 1
    print(f"Bots con >=2 activos: {multi_activo_bots}/{len(por_wallet)}")

    # Para cada trade, marca si hay OTRO trade del MISMO wallet, activo
    # DISTINTO, mismo lado_wallet (Up/Down), dentro de +-VENTANA_MIN.
    resultados = defaultdict(lambda: {"con_confirm": [], "sin_confirm": []})
    resultados_marco = defaultdict(lambda: {"con_confirm": [], "sin_confirm": []})

    for w, trs in por_wallet.items():
        if len({t["activo"] for t in trs}) < 2:
            continue
        trs_ts = [(parse_ts(t["trade_timestamp"]), t) for t in trs]
        for ts_i, ti in trs_ts:
            confirm = False
            for ts_j, tj in trs_ts:
                if tj is ti or tj["activo"] == ti["activo"]:
                    continue
                if abs((ts_j - ts_i).total_seconds()) <= VENTANA_MIN * 60 and tj["lado_wallet"] == ti["lado_wallet"]:
                    confirm = True
                    break
            acierto = int(ti["acierto"])
            clave = ti["activo"]
            marco = ti["marco"]
            grupo = "con_confirm" if confirm else "sin_confirm"
            resultados[clave][grupo].append(acierto)
            resultados_marco[(clave, marco)][grupo].append(acierto)

    print("\n--- Por activo (agregado marcos, exploratorio) ---")
    print(f"{'activo':6} {'n_con':6} {'hit_con':8} {'n_sin':6} {'hit_sin':8} {'diff':8} {'p_shuffle':10}")
    for activo, d in sorted(resultados.items()):
        n_c, n_s = len(d["con_confirm"]), len(d["sin_confirm"])
        if n_c < N_MIN or n_s < N_MIN:
            print(f"{activo:6} n_con={n_c} n_sin={n_s} -- insuficiente")
            continue
        hits_c, hits_s = sum(d["con_confirm"]), sum(d["sin_confirm"])
        diff, p = shuffle_test_prop(hits_c, n_c, hits_s, n_s, seed_key=f"activo#{activo}")
        print(f"{activo:6} {n_c:6} {hits_c/n_c*100:7.1f}% {n_s:6} {hits_s/n_s*100:7.1f}% {diff*100:+7.1f}pp {p:10.4f}")

    print("\n--- Por (activo,marco), desagregado (CLAUDE.md pt.17) ---")
    print(f"{'activo':6} {'marco':6} {'n_con':6} {'hit_con':8} {'n_sin':6} {'hit_sin':8} {'diff':8} {'p_shuffle':10}")
    n_evaluables = 0
    for (activo, marco), d in sorted(resultados_marco.items()):
        n_c, n_s = len(d["con_confirm"]), len(d["sin_confirm"])
        if n_c < N_MIN or n_s < N_MIN:
            print(f"{activo:6} {marco:6} n_con={n_c} n_sin={n_s} -- insuficiente")
            continue
        n_evaluables += 1
        hits_c, hits_s = sum(d["con_confirm"]), sum(d["sin_confirm"])
        diff, p = shuffle_test_prop(hits_c, n_c, hits_s, n_s, seed_key=f"{activo}#{marco}")
        print(f"{activo:6} {marco:6} {n_c:6} {hits_c/n_c*100:7.1f}% {n_s:6} {hits_s/n_s*100:7.1f}% {diff*100:+7.1f}pp {p:10.4f}")
    print(f"\nCombos (activo,marco) con n suficiente en AMBOS grupos: {n_evaluables}")


if __name__ == "__main__":
    main()
