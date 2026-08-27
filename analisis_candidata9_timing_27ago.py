#!/usr/bin/env python3
"""analisis_candidata9_timing_27ago.py -- propuesta #4 del barrido de
10 ideas 27-Ago: desagrega CANDIDATA9_BOT_CONSENSO#BTC#5min[0.50,0.55)
(ya confirmado, ver candidata9_10_gate_bucket.json) por restante_min al
cierre del mercado en el instante del trigger, no solo por precio.

Reusa eventos_candidata9() de analisis_candidata9_10_gate_bucket_26ago.py
tal cual (mismo trigger, sin look-ahead) pero conserva el condition_id y
extrae restante_min del propio market_slug (contiene el open_time unix
del mercado 5min, close_time = open_time + 5min).

FASE 0 -- solo lectura, no toca produccion.
"""
import csv
import math
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_gate_bucket_propio_28jul import shuffle_test  # noqa: E402

IN_BOTS = REPO / "data/shadow/bot_wallets_gate_bucket_fase0.csv"
FEE = 0.07
N_MIN_BOTS_C9 = 3
BUCKET_LO, BUCKET_HI = 0.50, 0.55
ACTIVO, MARCO = "BTC", "5min"
MARCO_MIN = {"5min": 5, "15min": 15, "60min": 60, "240min": 240}


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def to_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def pnl_neto(ask, acierto):
    gross_win = (1 - ask) / ask
    return gross_win * (1 - FEE) if acierto else -1.0


def close_time_de_slug(slug, marco):
    m = re.search(r"(\d{9,11})$", slug)
    if not m:
        return None
    open_ts = int(m.group(1))
    dur_s = MARCO_MIN.get(marco, 5) * 60
    return datetime.fromtimestamp(open_ts + dur_s, tz=timezone.utc)


def eventos_candidata9_con_timing():
    por_mercado = defaultdict(list)
    with open(IN_BOTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("outcome_real"):
                continue
            if r["activo"] != ACTIVO or r["marco"] != MARCO:
                continue
            por_mercado[r["condition_id"]].append(r)

    out = []
    for cond, filas in por_mercado.items():
        if len(filas) < N_MIN_BOTS_C9:
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
        outcome = filas[0]["outcome_real"]
        slug = filas[0]["market_slug"]

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
        if ask is None or not (BUCKET_LO <= ask < BUCKET_HI):
            continue
        acierto = 1 if lado_mayoria == outcome else 0
        pnl = pnl_neto(ask, acierto)
        ts = parse_ts(trigger["trade_timestamp"])
        close_time = close_time_de_slug(slug, MARCO)
        if close_time is None:
            continue
        restante_s = (close_time - ts).total_seconds()
        out.append((restante_s, ask, acierto, pnl))
    return out


def wilson90_lo(hits, n):
    if n == 0:
        return None
    p = hits / n
    z = 1.6448536269514722
    denom = 1 + z ** 2 / n
    centro = p + z ** 2 / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z ** 2 / (4 * n ** 2))
    return (centro - margen) / denom


def reporta(nombre, rows):
    n = len(rows)
    if n == 0:
        print(f"{nombre}: n=0")
        return
    hits = sum(a for _, _, a, _ in rows)
    pnl_medio = sum(p for _, _, _, p in rows) / n
    wlo = wilson90_lo(hits, n)
    asks = [a for _, a, _, _ in rows]
    ask_medio = sum(asks) / n
    breakeven = ask_medio
    print(f"{nombre}: n={n} hit={100*hits/n:.1f}% wilson90lo={100*wlo:.1f}% "
          f"ask_medio={ask_medio:.3f}(breakeven) pnl/tr={pnl_medio:+.3f}€")


def comparar_vs_resto(nombre, sub, resto):
    if len(sub) < 15 or len(resto) < 15:
        print(f"  [{nombre} vs resto] n insuficiente para shuffle (sub={len(sub)}, resto={len(resto)})")
        return
    pnls_sub = np.array([p for _, _, _, p in sub])
    pnls_resto = np.array([p for _, _, _, p in resto])
    diff, p = shuffle_test(pnls_sub, pnls_resto)
    print(f"  [{nombre} vs resto] diff_pnl={diff:+.3f} p_shuffle={p:.4f}")


def main():
    rows = eventos_candidata9_con_timing()
    print(f"Total eventos BTC#5min[{BUCKET_LO},{BUCKET_HI}): n={len(rows)}")
    restantes = sorted(r[0] for r in rows)
    if restantes:
        print(f"restante_s: min={restantes[0]:.0f} p25={np.percentile(restantes,25):.0f} "
              f"mediana={np.percentile(restantes,50):.0f} p75={np.percentile(restantes,75):.0f} "
              f"max={restantes[-1]:.0f}")
    print()
    reporta("AGREGADO", rows)
    print()

    # terciles por restante_s
    if len(rows) >= 30:
        rows_sorted = sorted(rows, key=lambda r: r[0])
        n = len(rows_sorted)
        t1 = rows_sorted[: n // 3]
        t2 = rows_sorted[n // 3 : 2 * n // 3]
        t3 = rows_sorted[2 * n // 3 :]
        print(f"tercil bajo (más cerca del cierre) restante_s<={t1[-1][0]:.0f}:")
        reporta("  TERCIL_BAJO_restante", t1)
        comparar_vs_resto("TERCIL_BAJO", t1, t2 + t3)
        print(f"tercil medio restante_s in ({t1[-1][0]:.0f},{t2[-1][0]:.0f}]:")
        reporta("  TERCIL_MEDIO_restante", t2)
        comparar_vs_resto("TERCIL_MEDIO", t2, t1 + t3)
        print(f"tercil alto restante_s>{t2[-1][0]:.0f}:")
        reporta("  TERCIL_ALTO_restante", t3)
        comparar_vs_resto("TERCIL_ALTO", t3, t1 + t2)
    else:
        print("n<30, no se particiona en terciles con rigor.")

    # cortes fijos en segundos, ajustados a un mercado de 5min (300s)
    print()
    print("== cortes fijos (60s) ==")
    for lo, hi in [(0, 60), (60, 120), (120, 180), (180, 240), (240, 300), (300, 99999)]:
        sub = [r for r in rows if lo <= r[0] < hi]
        reporta(f"  [{lo},{hi})s", sub)


if __name__ == "__main__":
    main()
