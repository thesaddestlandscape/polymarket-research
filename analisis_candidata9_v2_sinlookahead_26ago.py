#!/usr/bin/env python3
"""analisis_candidata9_v2_sinlookahead_26ago.py -- Candidata 9, v2 sin
look-ahead: el precio de entrada (ask) se toma del trade EXACTO que hace
que el lado mayoritario cruce a mayoria estricta (no la mediana de todos
los trades del lado mayoritario, que podia incluir asks posteriores al
momento real de decision). Añade split-half cronologico (primera vs
segunda mitad de mercados por fecha) sobre el subconjunto con ask
disponible.

Solo lectura.
"""
import csv
import zlib
from collections import defaultdict
from datetime import datetime

import numpy as np

IN = "data/shadow/bot_wallets_gate_bucket_fase0.csv"
N_MIN_BOTS = 3
STAKE = 1.05
UMBRAL_PROFUNDIDAD = 5 * STAKE


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def to_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def shuffle_test_prop(hits, n, p0, iters=5000, seed_key="c9v2"):
    rng = np.random.default_rng(zlib.crc32(seed_key.encode("utf-8")))
    sims = rng.binomial(n, p0, size=iters)
    obs = hits
    if obs >= n * p0:
        return float(np.mean(sims >= obs))
    return float(np.mean(sims <= obs))


def main():
    por_mercado = defaultdict(list)
    with open(IN, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("outcome_real"):
                continue
            por_mercado[r["condition_id"]].append(r)

    # eventos: clave -> lista de dict(ts, hit, ask, prof)
    eventos = defaultdict(list)

    for cond, filas in por_mercado.items():
        if len(filas) < N_MIN_BOTS:
            continue
        votos_final = defaultdict(int)
        for r in filas:
            votos_final[r["lado_wallet"]] += 1
        if len(votos_final) == 1:
            continue
        lado_mayoria = max(votos_final, key=votos_final.get)
        n_mayoria = votos_final[lado_mayoria]
        n_total = sum(votos_final.values())
        if n_mayoria == n_total - n_mayoria:
            continue  # empate exacto

        activo = filas[0]["activo"]
        marco = filas[0]["marco"]
        outcome = filas[0]["outcome_real"]

        # orden cronologico, buscar el trade EXACTO en que lado_mayoria
        # cruza a mayoria estricta (cuenta_mayoria > resto acumulado)
        filas_ordenadas = sorted(filas, key=lambda r: parse_ts(r["trade_timestamp"]))
        cuenta = defaultdict(int)
        trigger = None
        for r in filas_ordenadas:
            cuenta[r["lado_wallet"]] += 1
            resto = sum(v for k, v in cuenta.items() if k != lado_mayoria)
            if cuenta[lado_mayoria] > resto and r["lado_wallet"] == lado_mayoria:
                trigger = r
                break
        if trigger is None:
            continue  # no debería pasar si votos_final ya tiene mayoria, pero por robustez

        acierto = 1 if lado_mayoria == outcome else 0
        ask = to_float(trigger["mejor_ask_deteccion"])
        prof = to_float(trigger["profundidad_eur_deteccion"])
        ts = parse_ts(trigger["trade_timestamp"])
        eventos[(activo, marco)].append({"ts": ts, "hit": acierto, "ask": ask, "prof": prof})

    print(f"{'activo':6} {'marco':6} {'n':6} {'hit':7} {'ask_med':8} {'edge_bruto':11} {'p_shuffle':10} {'fill%':7} "
          f"{'split1':8} {'split2':8}")
    resumen = []
    for (activo, marco), evs in sorted(eventos.items(), key=lambda kv: -len(kv[1])):
        evs_ask = [e for e in evs if e["ask"] is not None]
        n = len(evs_ask)
        if n < 15:
            continue
        evs_ask.sort(key=lambda e: e["ts"])
        hits = sum(e["hit"] for e in evs_ask)
        hit = hits / n
        ask_med = float(np.median([e["ask"] for e in evs_ask]))
        edge = hit - ask_med
        p = shuffle_test_prop(hits, n, p0=ask_med, seed_key=f"{activo}#{marco}#v2")
        profs = [e["prof"] for e in evs_ask if e["prof"] is not None]
        fillable = sum(1 for pf in profs if pf >= UMBRAL_PROFUNDIDAD)
        fill_pct = 100.0 * fillable / len(profs) if profs else None
        fill_str = f"{fill_pct:6.1f}%" if fill_pct is not None else "  n/a "

        mid = n // 2
        h1 = evs_ask[:mid]
        h2 = evs_ask[mid:]
        def edge_split(sub):
            if len(sub) < 8:
                return None
            hh = sum(e["hit"] for e in sub) / len(sub)
            am = float(np.median([e["ask"] for e in sub]))
            return hh - am
        e1, e2 = edge_split(h1), edge_split(h2)
        e1_str = f"{e1*100:+.1f}pp" if e1 is not None else "n/a"
        e2_str = f"{e2*100:+.1f}pp" if e2 is not None else "n/a"

        print(f"{activo:6} {marco:6} {n:6} {hit*100:6.1f}% {ask_med:7.3f} {edge*100:+9.1f}pp {p:10.4f} {fill_str} "
              f"{e1_str:8} {e2_str:8}")
        resumen.append((activo, marco, n, edge, p, fill_pct, e1, e2))

    print("\n--- BH-FDR sobre los combos con n>=15 ---")
    resumen_p = sorted(resumen, key=lambda r: r[4])
    m = len(resumen_p)
    for i, (activo, marco, n, edge, p, fill_pct, e1, e2) in enumerate(resumen_p, start=1):
        umbral_bh = i / m * 0.05
        supera = "SI" if p <= umbral_bh else "no"
        consist = "consistente" if (e1 is not None and e2 is not None and (e1 > 0) == (e2 > 0)) else "revisar"
        print(f"  rank={i}/{m} {activo}#{marco}: p={p:.4f} umbral_BH={umbral_bh:.4f} supera_BH={supera} split_half={consist}")


if __name__ == "__main__":
    main()
