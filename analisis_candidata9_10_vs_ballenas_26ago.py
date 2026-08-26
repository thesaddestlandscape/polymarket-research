#!/usr/bin/env python3
"""analisis_candidata9_10_vs_ballenas_26ago.py -- Cruce contra ballenas
(CLAUDE.md pt.8/9: "ballenas = la lente por defecto, cruzar SIEMPRE") de
las candidatas 9 (consenso mayoritario bot wallets) y 10 (cross-activo
BTC), restringido al nucleo confirmado BTC#5min/15min. Usa los eventos
"trigger" ya calculados (mismo criterio sin look-ahead que las v2) y los
cruza contra ballenas_timing_history.csv (universo de wallets MUCHO mas
amplio, no solo las 84 bot wallets) por condition_id:

  1. Cobertura: cuantos mercados donde el bot-consensus dispara TAMBIEN
     tienen actividad de ballenas.
  2. Confluencia: cuando ambas fuentes tienen señal, coinciden en
     direccion?
  3. Cobertura incremental: en los mercados donde ballenas NO tiene
     señal (o el mercado no aparece en su historico), sobrevive el edge
     del bot-consensus? -- esto es lo que decide si aporta algo nuevo o
     es la misma señal vista con otro dataset.

Solo lectura.
"""
import csv
import zlib
from collections import defaultdict
from datetime import datetime

import numpy as np

IN_BOTS = "data/shadow/bot_wallets_gate_bucket_fase0.csv"
IN_BALLENAS = "data/shadow/ballenas_timing_history.csv"
N_MIN_BOTS = 3
MARCO_MAP = {"5min": "5m", "15min": "15m"}


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def to_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def shuffle_test_prop(hits, n, p0, iters=5000, seed_key="v_ballenas"):
    rng = np.random.default_rng(zlib.crc32(seed_key.encode("utf-8")))
    sims = rng.binomial(n, p0, size=iters)
    obs = hits
    if obs >= n * p0:
        return float(np.mean(sims >= obs))
    return float(np.mean(sims <= obs))


def cargar_ballenas_por_mercado():
    """condition_id -> {"votos": {lado: n}, "lado_mayoria": str|None}"""
    por_mercado = defaultdict(lambda: defaultdict(int))
    with open(IN_BALLENAS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["activo"] != "BTC" or r["marco"] not in ("5m", "15m"):
                continue
            compro_yes = r.get("compro_yes")
            if compro_yes in (None, ""):
                continue
            lado = "Up" if compro_yes in ("1", "True", "true") else "Down"
            por_mercado[(r["condition_id"], r["marco"])][lado] += 1
    out = {}
    for k, votos in por_mercado.items():
        if not votos:
            continue
        lado_mayoria = max(votos, key=votos.get)
        out[k] = {"votos": dict(votos), "lado_mayoria": lado_mayoria, "n": sum(votos.values())}
    return out


def eventos_candidata9_btc():
    por_mercado = defaultdict(list)
    with open(IN_BOTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("outcome_real") or r["activo"] != "BTC" or r["marco"] not in ("5min", "15min"):
                continue
            por_mercado[r["condition_id"]].append(r)

    eventos = []
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
            continue
        marco = filas[0]["marco"]
        outcome = filas[0]["outcome_real"]
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
            continue
        ask = to_float(trigger["mejor_ask_deteccion"])
        prof = to_float(trigger["profundidad_eur_deteccion"])
        eventos.append({
            "condition_id": cond, "marco": marco, "lado": lado_mayoria,
            "hit": 1 if lado_mayoria == outcome else 0, "ask": ask, "prof": prof,
        })
    return eventos


def main():
    ballenas = cargar_ballenas_por_mercado()
    eventos = eventos_candidata9_btc()
    print(f"Eventos candidata9 BTC (5min+15min): {len(eventos)}")
    print(f"Mercados BTC 5m/15m con actividad de ballenas: {len(ballenas)}")

    for marco_bots, marco_ball in (("5min", "5m"), ("15min", "15m")):
        evs = [e for e in eventos if e["marco"] == marco_bots]
        con_ballenas, sin_ballenas = [], []
        confluencia, discrepancia = 0, 0
        for e in evs:
            b = ballenas.get((e["condition_id"], marco_ball))
            if b is None:
                sin_ballenas.append(e)
            else:
                con_ballenas.append(e)
                if b["lado_mayoria"] == e["lado"]:
                    confluencia += 1
                else:
                    discrepancia += 1

        print(f"\n=== BTC#{marco_bots} ===")
        print(f"  con actividad de ballenas: {len(con_ballenas)} ({confluencia} confluyen, {discrepancia} discrepan)")
        print(f"  SIN actividad de ballenas (cobertura incremental): {len(sin_ballenas)}")

        UMBRAL_PROFUNDIDAD = 5 * 1.05
        for nombre, grupo in (("con_ballenas", con_ballenas), ("sin_ballenas", sin_ballenas)):
            asks = [e["ask"] for e in grupo if e["ask"] is not None]
            n = len(asks)
            if n < 15:
                print(f"    {nombre}: n={n}<15, insuficiente")
                continue
            hits = sum(e["hit"] for e in grupo if e["ask"] is not None)
            hit = hits / n
            ask_med = float(np.median(asks))
            edge = hit - ask_med
            p = shuffle_test_prop(hits, n, p0=ask_med, seed_key=f"{marco_bots}#{nombre}")
            profs = [e["prof"] for e in grupo if e["prof"] is not None]
            n_prof = len(profs)
            fillable = sum(1 for pf in profs if pf >= UMBRAL_PROFUNDIDAD)
            fill_pct = 100.0 * fillable / n_prof if n_prof else None
            fill_str = f"{fill_pct:.1f}% (n_prof={n_prof})" if fill_pct is not None else "n/a"
            print(f"    {nombre}: n={n} hit={hit*100:.1f}% ask_med={ask_med:.3f} edge={edge*100:+.1f}pp p={p:.4f} fill={fill_str}")


if __name__ == "__main__":
    main()
