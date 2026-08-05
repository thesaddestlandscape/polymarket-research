#!/usr/bin/env python3
"""
analisis_fillability_top_candidatas_03ago.py — aplica el colapso CANÓNICO
de analisis_fills.py (por market_id, prioridad de motivo, nunca contar
filas sueltas) pero desagregado por tupla exacta (subtype incluido, no
solo strategy+direction) a las candidatas top de
analisis_barrido_candidatas_stage0_03ago.py.

Objetivo (petición Javi 03-Ago): encontrar el "giro" -- candidatas con IC
alto en shadow que además tengan fill-ability real, o que escondan un
subconjunto fillable dentro de un agregado mal fillable (mismo patrón que
SOL#5min: la solución vivía en un ángulo no obvio).

Solo lectura.
"""
import csv
from collections import defaultdict
from pathlib import Path

DIR = Path(__file__).parent
SNAPSHOTS = DIR / "data/live/libro_snapshots.csv"
RESULTS = DIR / "data/shadow/results.csv"

PRIORIDAD = ["ejecutada", "fok_kill", "post_only_mode", "abort_requote",
             "veto_profundidad", "veto_sin_datos", "veto_ballenas_debil",
             "no_viable_stake", "veto_discrepancia_tuplas", "fuera_ventana",
             "senal_caducada", "maker_colocada"]


def _prio(motivo):
    try:
        return PRIORIDAD.index(motivo)
    except ValueError:
        return len(PRIORIDAD)


TUPLAS = [
    "FAVORITO_CONFIRMADO#SOL#240min#BUY_YES",
    "UPDOWN_GBM_15M_TARDIO#SOL#15min#BUY_YES",
    "UPDOWN_GBM_15M_TARDIO#SOL#15min#BUY_NO",
    "GBM_LATE_15M#BTC#15min#BUY_YES",
    "GBM_LATE_15M_ESPACIO_ATR#SOL#15min#BUY_YES",
    "GBM_LATE_15M_ESPACIO_ATR#BTC#15min#BUY_YES",
    "FAVORITO_CONFIRMADO#SOL#5min#BUY_YES",
    "UPDOWN_GBM#BNB#15min#BUY_NO",
    "UPDOWN_GBM#ETH#15min#BUY_NO",
]


def _split(t):
    partes = t.split("#")
    return partes[0], "#".join(partes[1:-1]), partes[-1]


def main():
    senales = {}
    with open(SNAPSHOTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            key = (r["market_id"], r["strategy"], r["subtype"], r["direction"])
            prev = senales.get(key)
            if prev is None or _prio(r["motivo"]) < _prio(prev["motivo"]):
                senales[key] = {"motivo": r["motivo"]}

    outcomes = {}
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            outcomes[(r["market_id"], r["strategy"], r["subtype"], r["decision"])] = (
                int(r["acierto"]), float(r["pnl_neto"]))

    for t in TUPLAS:
        strategy, subtype, direction = _split(t)
        agg = defaultdict(lambda: [0, 0, 0.0])
        for (mid, s, sub, dec), sig in senales.items():
            if s != strategy or sub != subtype or dec != direction:
                continue
            out = outcomes.get((mid, s, sub, direction))
            a = agg[sig["motivo"]]
            if out:
                acierto, pnl = out
                a[0] += acierto
                a[1] += 1
                a[2] += pnl

        n_total = sum(v[1] for v in agg.values())
        print(f"\n=== {t} ===  (n con outcome: {n_total})")
        if n_total == 0:
            print("  sin cruce libro+outcome todavía")
            continue
        for motivo in sorted(agg, key=lambda m: -agg[m][1]):
            w, n, pnl = agg[motivo]
            if n == 0:
                continue
            print(f"  {motivo:<22} n={n:>4} hit={w/n*100:>5.1f}% pnl_total={pnl:>+8.2f}€ pnl_medio={pnl/n:>+.3f}€")


if __name__ == "__main__":
    main()
