#!/usr/bin/env python3
"""Backtest #4 (escalera intra-ventana) + #2 (spread intra-bloque) sobre shadow.
Read-only. Bloque = mismo end_date (franja 15min); pares distintos = mismas resolución.
Objetivo: cuantificar correlacion de ventana y si una regla de sizing la neutraliza.
"""
import csv, statistics
from collections import defaultdict

STRAT = "GBM_LATE_15M"
rows = []
with open("/root/polymarket-research/data/shadow/results.csv") as f:
    for r in csv.DictReader(f):
        if r["strategy"] != STRAT:
            continue
        if "15min" not in r["subtype"]:
            continue
        try:
            r["_pnl"] = float(r["pnl_neto"])
            r["_ac"] = int(float(r["acierto"]))
        except (ValueError, KeyError):
            continue
        # UP/DOWN real del mercado, independiente de la direccion apostada:
        # para BUY_YES acierto=1 <-> subio; para BUY_NO acierto=1 <-> bajo.
        r["_up"] = r["_ac"] if r["decision"] == "BUY_YES" else 1 - r["_ac"]
        r["_pair"] = r["subtype"].split("#")[0]
        rows.append(r)

print(f"n filas {STRAT} #15min = {len(rows)}")

# ---- Bloques por end_date ----
blocks = defaultdict(list)
for r in rows:
    blocks[r["end_date"]].append(r)
multi = {k: v for k, v in blocks.items() if len({x["_pair"] for x in v}) >= 2}
print(f"bloques totales={len(blocks)}  con >=2 pares={len(multi)}")

# ================= #2 CORRELACION / SPREAD =================
print("\n" + "=" * 60)
print("#2 CORRELACION DE VENTANA + SPREAD (bloques >=2 pares)")
print("=" * 60)
co_mov = 0  # todos los pares del bloque en la misma direccion (up o down)
mixed = 0
for k, v in multi.items():
    ups = {x["_up"] for x in v}
    if len(ups) == 1:
        co_mov += 1
    else:
        mixed += 1
tot = co_mov + mixed
print(f"  co-movimiento (todos misma direccion): {co_mov}/{tot} = {100*co_mov/tot:.1f}%")
print(f"  mixto (al menos uno diverge):          {mixed}/{tot} = {100*mixed/tot:.1f}%")

# Doble-perdida en BUY_YES (bloque): todos los BUY_YES del bloque pierden
byes = {k: [x for x in v if x["decision"] == "BUY_YES"] for k, v in multi.items()}
byes = {k: v for k, v in byes.items() if len(v) >= 2}
dbl_loss = sum(1 for v in byes.values() if all(x["_ac"] == 0 for x in v))
dbl_win = sum(1 for v in byes.values() if all(x["_ac"] == 1 for x in v))
print(f"\n  BUY_YES en bloque >=2 (n bloques={len(byes)}):")
print(f"    doble-PERDIDA (todos pierden): {dbl_loss}/{len(byes)} = {100*dbl_loss/max(len(byes),1):.1f}%")
print(f"    doble-GANANCIA (todos ganan):  {dbl_win}/{len(byes)} = {100*dbl_win/max(len(byes),1):.1f}%")

# Spread simulado: YES en par A, NO en par B del mismo bloque (2 primeros pares por hora entrada)
# gana si resuelven distinto. PnL aproximado a precio de mercado.
spread_pnl = []
both_yes_pnl = []
for k, v in byes.items():
    v = sorted(v, key=lambda x: x["prediction_timestamp"])
    a, b = v[0], v[1]
    # both-YES real (dos apuestas BUY_YES a 1.05 cada una)
    both_yes_pnl.append(a["_pnl"] + b["_pnl"])
    # spread: YES en A (tal cual), NO en B (invertir outcome de B)
    # payout NO en B: gana si B bajo. PnL NO ~ simetrico usando precio.
    try:
        pB = float(b["precio_yes_mercado"])
    except ValueError:
        continue
    stake = 1.05
    # comprar NO a precio (1-pB): shares=stake/(1-pB); si B baja paga 1/share
    if b["_up"] == 0:  # B bajo -> NO gana
        pnl_noB = stake * pB / (1 - pB) if pB < 1 else 0
    else:
        pnl_noB = -stake
    spread_pnl.append(a["_pnl"] + pnl_noB)

if spread_pnl:
    print(f"\n  Simulacion 2 primeros pares/bloque (n={len(spread_pnl)}):")
    print(f"    both-YES  : pnl_total={sum(both_yes_pnl):+.1f}€  medio/bloque={statistics.mean(both_yes_pnl):+.3f}€")
    print(f"    spread Y/N: pnl_total={sum(spread_pnl):+.1f}€  medio/bloque={statistics.mean(spread_pnl):+.3f}€")

# ================= #4 ESCALERA (bloque->bloque) =================
print("\n" + "=" * 60)
print("#4 ESCALERA: autocorrelacion bloque->bloque (BUY_YES)")
print("=" * 60)
# Secuencia de bloques por dia, marcados como bloque perdedor si mayoria BUY_YES pierde
day_blocks = defaultdict(list)
for k, v in blocks.items():
    by = [x for x in v if x["decision"] == "BUY_YES"]
    if not by:
        continue
    losses = sum(1 for x in by if x["_ac"] == 0)
    bad = losses > len(by) / 2
    pnl = sum(x["_pnl"] for x in by)
    day = k[:10]
    day_blocks[day].append((k, bad, pnl, by))

base_bad = 0
tot_b = 0
after_bad = [0, 0]  # [bad, total] cuando bloque previo fue bad
after_good = [0, 0]
saved = 0.0  # pnl que ahorraria skip del bloque siguiente tras uno bad
for day, bl in day_blocks.items():
    bl.sort(key=lambda x: x[0])
    for i, (k, bad, pnl, by) in enumerate(bl):
        tot_b += 1
        base_bad += bad
        if i > 0:
            prev_bad = bl[i - 1][1]
            if prev_bad:
                after_bad[1] += 1
                after_bad[0] += bad
                saved += -pnl  # si skippeas este bloque, evitas su pnl (bueno si pnl<0)
            else:
                after_good[1] += 1
                after_good[0] += bad
print(f"  bloques BUY_YES analizados={tot_b}  base P(bloque malo)={100*base_bad/tot_b:.1f}%")
if after_bad[1]:
    print(f"  P(malo | previo malo)  = {100*after_bad[0]/after_bad[1]:.1f}%  (n={after_bad[1]})")
if after_good[1]:
    print(f"  P(malo | previo bueno) = {100*after_good[0]/after_good[1]:.1f}%  (n={after_good[1]})")
print(f"  PnL agregado de bloques que siguen a uno malo (lo que 'ahorraria' skippearlos) = {saved:+.1f}€")
print("  (>0 = skippear tras bloque malo ahorra dinero; <0 = skippear cuesta)")
