#!/usr/bin/env python3
"""
Reenfoque de GBM_LATE_15M_ESPACIO_ATR#ETH#15min#BUY_YES tras la pausa del
14-Jul (gap fillable-vs-no-fillable de 60.3pp, la peor de las 8 tuplas de
ese momento: fillable n=31 hit=19.4% pnl=-30.83€ vs no-fillable n=74
hit=79.7% pnl=+100.16€ — ver nota _pares_espacioatr_eth_pausa_nota_2026-07-14
en config_live.json).

Petición Javi (15-Jul): en vez de reabrir sin dato nuevo, cruzar el mismo
dataset (misma metodología que analisis_causal_fillability_general.py:
libro_snapshots motivo=candidato_evaluacion + ratio_vs_stake>=5x = fillable)
contra la banda de precio que ballenas_observer.py ya tiene confirmada para
ETH#15m ([0.70,0.90), z=5.90, n=183) — hipótesis: la selección adversa se
concentra en señales FUERA de esa banda (donde ESPACIO_ATR igual dispara,
por su propio filtro de distancia ATR, pero las ballenas no confirman).

Solo lectura, no toca dinero ni config.
"""
import csv
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data/shadow/results.csv"
LIBRO = REPO / "data/live/libro_snapshots.csv"
STATE = REPO / "data/shadow/ballenas_timing_state.json"
RATIO_MIN = 5.0
STRATEGY = "GBM_LATE_15M_ESPACIO_ATR"
SUBTYPE = "ETH#15min"
DECISION = "BUY_YES"


def main():
    estado = json.loads(STATE.read_text())
    banda = estado.get("ETH#15m", {})
    lo, hi = banda.get("banda_lo"), banda.get("banda_hi")
    print(f"Banda ballenas ETH#15m: [{lo},{hi})  z={banda.get('z')}  n={banda.get('n')}")

    idx = {}
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["strategy"] != STRATEGY or r["subtype"] != SUBTYPE or r["decision"] != DECISION:
                continue
            try:
                feats = json.loads(r.get("features") or "{}")
            except Exception:
                feats = {}
            try:
                pnl = float(r.get("pnl_neto") or 0)
                acierto = int(r.get("acierto") or 0)
            except (ValueError, TypeError):
                continue
            idx[r["market_id"]] = {"pnl": pnl, "acierto": acierto, "py": feats.get("py_entrada")}

    print(f"Resoluciones en results.csv para esta tupla: {len(idx)}")

    filas = []
    with open(LIBRO, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r.get("strategy"), r.get("subtype"), r.get("direction")) != (STRATEGY, SUBTYPE, DECISION):
                continue
            if r.get("motivo") != "candidato_evaluacion":
                continue
            try:
                ratio = float(r.get("ratio_vs_stake") or 0)
            except ValueError:
                ratio = 0
            info = idx.get(r["market_id"])
            if not info:
                continue
            fillable = ratio >= RATIO_MIN
            py = info["py"]
            dentro_banda = (py is not None and lo is not None and lo <= py < hi)
            filas.append({"fillable": fillable, "dentro_banda": dentro_banda,
                          "pnl": info["pnl"], "acierto": info["acierto"], "py": py})

    print(f"Filas cruzadas (snapshot+resolución+feature py): {len(filas)}")

    def resumen(nombre, subset):
        n = len(subset)
        if n == 0:
            print(f"  {nombre}: n=0")
            return
        hit = sum(1 for f in subset if f["acierto"]) / n
        pnl = sum(f["pnl"] for f in subset)
        print(f"  {nombre}: n={n:>3} hit={hit*100:5.1f}% pnl_total={pnl:+8.2f}€ pnl_medio={pnl/n:+.3f}€")

    print("\n=== Cruce completo (4 celdas) ===")
    resumen("FILLABLE  + DENTRO banda ballenas", [f for f in filas if f["fillable"] and f["dentro_banda"]])
    resumen("FILLABLE  + FUERA  banda ballenas", [f for f in filas if f["fillable"] and not f["dentro_banda"]])
    resumen("NO-fillable + DENTRO banda ballenas", [f for f in filas if not f["fillable"] and f["dentro_banda"]])
    resumen("NO-fillable + FUERA  banda ballenas", [f for f in filas if not f["fillable"] and not f["dentro_banda"]])

    print("\n=== Solo por banda (colapsando fillable) ===")
    resumen("DENTRO banda ballenas (todo)", [f for f in filas if f["dentro_banda"]])
    resumen("FUERA  banda ballenas (todo)", [f for f in filas if not f["dentro_banda"]])

    print("\n=== Solo por fillability (colapsando banda, replica el hallazgo del 14-Jul) ===")
    resumen("FILLABLE (todo)", [f for f in filas if f["fillable"]])
    resumen("NO-fillable (todo)", [f for f in filas if not f["fillable"]])


if __name__ == "__main__":
    main()
