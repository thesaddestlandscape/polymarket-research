#!/usr/bin/env python3
"""Reabre el análisis de fill-ability de analisis_fills.py, pero filtrado a
BUY_NO#15min -- el corte exacto que se retiró en bloque de live el 06-Jul por
"selección adversa direccional" (CLAUDE.md: "vuelven vía filtro fill-ability
con n≥30"), pendiente de decisión formal desde el 05-Jul ("inminente").

Misma lógica de agregación por motivo que analisis_fills.py (prioridad de
snapshot por señal, cruce con outcome shadow a precio de plan) -- solo
añade el filtro direction=="BUY_NO" and "15min" in subtype. No reimplementa
el resto: reusa PRIORIDAD/_prio tal cual.
"""
import csv
from collections import defaultdict
from pathlib import Path

import analisis_fills as af

DIR = Path(__file__).parent
N_MIN = 30


def main():
    senales = {}
    with open(af.SNAPSHOTS, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["direction"] != "BUY_NO" or "15min" not in r["subtype"]:
                continue
            key = (r["market_id"], r["strategy"], r["direction"])
            prev = senales.get(key)
            if prev is None or af._prio(r["motivo"]) < af._prio(prev["motivo"]):
                senales[key] = {"motivo": r["motivo"], "ts": r["timestamp_utc"]}

    outcomes = {}
    with open(af.RESULTS, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            outcomes[(r["market_id"], r["strategy"], r["decision"])] = (
                int(r["acierto"]), float(r["pnl_neto"]))

    agg = defaultdict(lambda: [0, 0, 0.0, 0])
    for key, s in senales.items():
        out = outcomes.get(key)
        if out is None:
            agg[s["motivo"]][3] += 1
            continue
        acierto, pnl = out
        a = agg[s["motivo"]]
        a[0] += acierto
        a[1] += 1
        a[2] += pnl

    print("Fills condicional al libro -- SOLO BUY_NO#15min (histórico completo)")
    print(f"{'motivo':<18}{'n':>5}{'hit':>7}{'pnl_medio':>11}{'pnl_total':>11}  n>={N_MIN}")
    for motivo in af.PRIORIDAD:
        if motivo not in agg:
            continue
        w, n, pnl, sin = agg[motivo]
        if n == 0:
            print(f"{motivo:<18}{0:>5}{'—':>7}{'—':>11}{'—':>11}  (pendiente: {sin} sin resolver)")
            continue
        listo = "OK" if n >= N_MIN else f"({n}/{N_MIN})"
        extra = f" | {sin} sin resolver aún" if sin else ""
        print(f"{motivo:<18}{n:>5}{w/n:>7.0%}{pnl/n:>+10.3f}€{pnl:>+10.2f}€  {listo}{extra}")

    ejec = agg.get("ejecutada")
    veto = agg.get("veto_profundidad")
    print()
    if ejec and ejec[1] >= N_MIN and veto and veto[1] >= N_MIN:
        gap = veto[0] / veto[1] - ejec[0] / ejec[1]
        if gap > 0.15:
            print(f"-> Selección adversa CONFIRMADA en BUY_NO#15min con n>={N_MIN}: "
                  f"hit veto {veto[0]/veto[1]:.0%} vs ejecutadas {ejec[0]/ejec[1]:.0%}. "
                  "Sigue bloqueado.")
        else:
            print(f"-> Gap veto-vs-ejecutadas {gap:+.0%} con n>={N_MIN}: "
                  "la selección adversa NO se confirma en BUY_NO#15min con dato actual "
                  "-- revisar si sigue justificado el bloqueo en bloque.")
    else:
        faltan = []
        for nombre, a in (("ejecutada", ejec), ("veto_profundidad", veto)):
            n = a[1] if a else 0
            if n < N_MIN:
                faltan.append(f"{nombre} {n}/{N_MIN}")
        print(f"-> Aún sin n suficiente para decidir: {', '.join(faltan)}")


if __name__ == "__main__":
    main()
