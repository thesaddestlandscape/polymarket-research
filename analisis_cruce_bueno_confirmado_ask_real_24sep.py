#!/usr/bin/env python3
"""24-Sep (Javi: "¿esto nos está pasando en más estrategias?"): cruza cada bueno_confirmado de
gate_bucket_propio.json (medido al precio_yes_mercado de results.csv) con el EV al ASK REAL posterior
del mismo micro-bucket (analisis_auditoria_twap_estrategias_24sep.py, grupos BUCKET|...).
Resultado 24-Sep: 49 bueno_confirmado -> 4 sobreviven, 38 caen, 7 sin datos (WEEKLY/60min)."""
import json
gb = json.load(open("/root/polymarket-research/data/shadow/gate_bucket_propio.json"))
au = json.load(open("/root/polymarket-research/data/shadow/auditoria_twap_estrategias_24sep.json"))["grupos"]
filas = []
for tupla, bs in gb.items():
    if not isinstance(bs, dict):
        continue
    for b, v in bs.items():
        if not isinstance(v, dict) or v.get("veredicto") != "bueno_confirmado":
            continue
        a = au.get(f"BUCKET|{tupla}|{float(b):.2f}")
        filas.append((tupla, b, v.get("n"), v.get("pnl_medio"), a))
sobrevive = cae = sin = 0
print(f"{'tupla':52} {'bucket':6} {'gate n':>6} {'gate €/tr':>9} | {'n_ask':>5} {'€ señal':>8} {'€ ASK':>7} {'IC90 ask':>16} días+")
for t, b, n, p, a in sorted(filas, key=lambda x: x[0]):
    if not a or not a.get("n_ask"):
        sin += 1
        print(f"{t:52} {b:6} {n:>6} {p:>+9.3f} | sin datos 5/15min en auditoría")
        continue
    ea = a["eur_ask"]
    ok = ea is not None and ea >= 0.10 and (a.get("ic90_ask_dias") or [-1])[0] > 0
    sobrevive += ok
    cae += not ok
    print(f"{t:52} {b:6} {n:>6} {p:>+9.3f} | {a['n_ask']:>5} {a['eur_mkt']:>+8.3f} {ea:>+7.3f} {str(a.get('ic90_ask_dias')):>16} {a['dias_pos']}/{a['dias']} {'✅' if ok else '❌'}")
print(f"\nbueno_confirmado: {len(filas)} | sobreviven al ask real (>=+0,10 e IC90 días>0): {sobrevive} | caen: {cae} | sin datos: {sin}")
