#!/usr/bin/env python3
"""analisis_dumb_money_invertido_27ago.py -- propuesta #5 del barrido de
alfa del 27-Ago: identificar wallets que sistematicamente pierden cuando
se enfrentan al lado contrario de la mayoria de bot wallets (universo de
84, mismo que Candidata 9) en BTC#5min, para fadearlas directamente.

Resultado: REFUTADO por regresion a la media. Ver memoria
idea_dumb_money_invertido_27ago para el detalle completo.

Solo lectura. No toca produccion.
"""
import csv
import json
from collections import Counter, defaultdict
from datetime import datetime, timedelta

REPO_DATA_ACTIVITY_RAW = "/tmp/btc5min_activity_raw.csv"  # extraido de
# /root/polymarket-research-datalogs/polymarket_activity_2026-08-2[4-7].csv
# filtrado a activo=BTC marco=5min (ver comando de extraccion en el commit)

BOT_UNIVERSO = "data/shadow/bot_wallets_universo_25ago.json"
OUTCOMES = "data/shadow/outcomes_5m_klines.json"


def round_up_5min(ts):
    dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
    minute = (dt.minute // 5 + 1) * 5
    base = dt.replace(second=0, microsecond=0, minute=0) + timedelta(minutes=minute)
    return base.isoformat()


def cargar_eventos():
    bot_uni = set(w.lower() for w in json.load(open(BOT_UNIVERSO)).keys())
    outcomes = json.load(open(OUTCOMES))["BTC"]

    mercados = defaultdict(list)
    with open(REPO_DATA_ACTIVITY_RAW) as f:
        for row in csv.DictReader(f):
            if row["side"] != "BUY":
                continue
            mercados[row["condition_id"]].append(row)

    eventos = []  # (fecha, wallet, gano)
    for cid, trades in mercados.items():
        last_ts = max(t["timestamp_utc"] for t in trades)
        key = round_up_5min(last_ts)
        out = outcomes.get(key)
        if out is None:
            continue
        bot_side_votes = Counter()
        for t in trades:
            w = t["wallet"].lower()
            if w in bot_uni:
                bot_side_votes[t["outcome"]] += 1
        if not bot_side_votes:
            continue
        top_side, top_n = bot_side_votes.most_common(1)[0]
        if top_n < 3:
            continue
        opp_side_label = "Down" if top_side == "Up" else "Up"
        fecha = key[:10]
        for t in trades:
            w = t["wallet"].lower()
            if w in bot_uni or t["outcome"] != opp_side_label:
                continue
            gano = (opp_side_label == "Up" and out == "YES") or (
                opp_side_label == "Down" and out == "NO"
            )
            eventos.append((fecha, w, gano))
    return eventos


def main():
    eventos = cargar_eventos()
    fechas = sorted(set(e[0] for e in eventos))
    mid = fechas[len(fechas) // 2]

    h1, h2 = defaultdict(lambda: [0, 0]), defaultdict(lambda: [0, 0])
    for fecha, w, gano in eventos:
        d = h1 if fecha < mid else h2
        d[w][0] += 1
        if not gano:
            d[w][1] += 1

    lossrates = [v[1] / v[0] for v in h1.values() if v[0] >= 15]
    print(f"wallets n>=15 (agregado): media_lossrate={sum(lossrates)/len(lossrates):.3f}")

    cand = sorted(
        [(w, v[0], v[1] / v[0]) for w, v in h1.items() if v[0] >= 15],
        key=lambda x: -x[2],
    )
    print(f"candidatas h1 n>=15: {len(cand)} -- top 15 peor lossrate, split-half:")
    for w, n1, lr1 in cand[:15]:
        v2 = h2.get(w)
        if v2 and v2[0] >= 5:
            print(f"  {w} h1 n={n1} lossrate={lr1:.2f} -> h2 n={v2[0]} lossrate={v2[1]/v2[0]:.2f}")
        else:
            print(f"  {w} h1 n={n1} lossrate={lr1:.2f} -> h2 sin datos suficientes")


if __name__ == "__main__":
    main()
