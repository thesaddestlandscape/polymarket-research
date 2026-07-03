#!/usr/bin/env python3
"""
Análisis de fills condicional al libro (2026-07-03).

Cruza data/live/libro_snapshots.csv (estado del libro de cada señal en fase
de ejecución, o bloqueada por stake no viable) con data/shadow/results.csv
(outcome del shadow a precio de plan) por market_id+strategy+decision.

Motivación: los fills taker live acertaron 19% vs 83% las señales vetadas
por profundidad (03-Jul) — la fill-ability es un anti-predictor. Este script
es el criterio de reapertura del live: si con n≥30 por motivo el subconjunto
no-ejecutado mantiene hit >> ejecutadas, la entrada correcta es maker
condicional (limit al precio de plan solo donde el taker no llena), no taker.

Uso: python3 analisis_fills.py [--dias N]  (default: todo el histórico)
"""
import argparse
import csv
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

DIR = Path(__file__).parent
SNAPSHOTS = DIR / "data/live/libro_snapshots.csv"
RESULTS = DIR / "data/shadow/results.csv"

# Prioridad: qué tan lejos llegó la señal en el pipeline live. Si un mercado
# tiene varios snapshots (reintentos ~20s), el motivo final es el más alto.
PRIORIDAD = ["ejecutada", "fok_kill", "abort_requote",
             "veto_profundidad", "veto_sin_datos", "no_viable_stake"]
N_MIN_DECISION = 30


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=0,
                    help="limitar a los últimos N días (0 = todo)")
    args = ap.parse_args()

    if not SNAPSHOTS.exists():
        print(f"Sin datos aún: {SNAPSHOTS} no existe. El fast loop lo genera "
              "con cada señal que llega a fase de ejecución o queda bloqueada "
              "por stake no viable (dentro de ventana horaria, switch ON).")
        return 1

    desde = None
    if args.dias > 0:
        desde = (datetime.now(timezone.utc) - timedelta(days=args.dias)).isoformat()

    # 1. Snapshots → una señal por (market_id, strategy, direction)
    senales = {}  # key → {"motivo", "ratio", "mejor_ask", "precio_plan", "ts"}
    with open(SNAPSHOTS, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if desde and r["timestamp_utc"] < desde:
                continue
            key = (r["market_id"], r["strategy"], r["direction"])
            prev = senales.get(key)
            if prev is None or PRIORIDAD.index(r["motivo"]) < PRIORIDAD.index(prev["motivo"]):
                senales[key] = {"motivo": r["motivo"],
                                "ratio": r.get("ratio_vs_stake", ""),
                                "ts": r["timestamp_utc"]}

    # 2. Outcomes shadow a precio de plan
    outcomes = {}  # (market_id, strategy, decision) → (acierto, pnl_neto)
    with open(RESULTS, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            outcomes[(r["market_id"], r["strategy"], r["decision"])] = (
                int(r["acierto"]), float(r["pnl_neto"]))

    # 3. Cruce y agregación por motivo
    agg = defaultdict(lambda: [0, 0, 0.0, 0])  # motivo → [wins, n, pnl, sin_outcome]
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

    titulo = f"últimos {args.dias}d" if args.dias else "histórico completo"
    print(f"Fills condicional al libro ({titulo}) — outcome SHADOW a precio de plan")
    print(f"{'motivo':<18}{'n':>5}{'hit':>7}{'pnl_medio':>11}{'pnl_total':>11}  n≥{N_MIN_DECISION}")
    for motivo in PRIORIDAD:
        if motivo not in agg:
            continue
        w, n, pnl, sin = agg[motivo]
        if n == 0:
            print(f"{motivo:<18}{0:>5}{'—':>7}{'—':>11}{'—':>11}  (pendiente: {sin} sin resolver)")
            continue
        listo = "✅" if n >= N_MIN_DECISION else f"⏳ ({n}/{N_MIN_DECISION})"
        extra = f" | {sin} sin resolver aún" if sin else ""
        print(f"{motivo:<18}{n:>5}{w / n:>7.0%}{pnl / n:>+10.3f}€{pnl:>+10.2f}€  {listo}{extra}")

    ejec = agg.get("ejecutada")
    veto = agg.get("veto_profundidad")
    bloq = agg.get("no_viable_stake")
    print()
    if ejec and ejec[1] >= N_MIN_DECISION and veto and veto[1] >= N_MIN_DECISION:
        gap = veto[0] / veto[1] - ejec[0] / ejec[1]
        if gap > 0.15:
            print(f"→ Selección adversa CONFIRMADA con n≥{N_MIN_DECISION}: hit veto "
                  f"{veto[0]/veto[1]:.0%} vs ejecutadas {ejec[0]/ejec[1]:.0%}. "
                  "Construir entrada maker condicional (limit a precio de plan "
                  "en señales vetadas; ver maker_sim.py CANCEL_MIN).")
        else:
            print(f"→ Gap veto-vs-ejecutadas {gap:+.0%} con n≥{N_MIN_DECISION}: "
                  "la selección adversa NO se confirma; revisar antes de cambiar la entrada.")
    else:
        faltan = []
        for nombre, a in (("ejecutada", ejec), ("veto_profundidad", veto),
                          ("no_viable_stake", bloq)):
            n = a[1] if a else 0
            if n < N_MIN_DECISION:
                faltan.append(f"{nombre} {n}/{N_MIN_DECISION}")
        print(f"→ Aún sin n suficiente para decidir: {', '.join(faltan)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
