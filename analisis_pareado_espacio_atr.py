#!/usr/bin/env python3
"""
analisis_pareado_espacio_atr.py — #8 del backlog (10-Jul): ¿la mejora de IC de
GBM_LATE_15M_ESPACIO_ATR (0.159 n=555) sobre GBM_LATE_15M (0.114 n=3146) es
genuina o correlación de muestra? Compara SOLO los market_id donde ambas
estrategias dispararon (mismo mercado, mismo outcome real) — control pareado,
no dos muestras independientes que pueden diferir en mezcla de horas/pares/
regímenes de mercado.

Solo lectura de results.csv, no toca dinero ni config. ic_bayes replica
exactamente la fórmula de shadow_postmortem.py: (aciertos+1)/(n+2)-0.5.
"""
import csv
from collections import defaultdict
from pathlib import Path

RESULTS = Path("data/shadow/results.csv")
BASE = "GBM_LATE_15M"
ATR = "GBM_LATE_15M_ESPACIO_ATR"


def ic_bayes(aciertos: int, n: int) -> float:
    return (aciertos + 1) / (n + 2) - 0.5


def main():
    filas = defaultdict(dict)  # market_id -> {strategy: row}
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            strat = row.get("strategy", "")
            if strat not in (BASE, ATR):
                continue
            mid = row.get("market_id", "")
            acierto = row.get("acierto", "")
            if acierto not in ("True", "False", "1", "0"):
                continue
            filas[mid][strat] = row

    pares = [(v[BASE], v[ATR]) for v in filas.values() if BASE in v and ATR in v]
    print(f"Market_id con AMBAS estrategias resueltas: {len(pares)}")
    if not pares:
        print("Sin solape — no se puede parear todavía.")
        return

    def acierto_bool(row):
        return row.get("acierto") in ("True", "1")

    n = len(pares)
    ac_base = sum(1 for b, a in pares if acierto_bool(b))
    ac_atr = sum(1 for b, a in pares if acierto_bool(a))
    ic_base = ic_bayes(ac_base, n)
    ic_atr = ic_bayes(ac_atr, n)

    # Concordancia: ¿en cuántos market_id coinciden ambas (mismo acierto/fallo)?
    concuerdan = sum(1 for b, a in pares if acierto_bool(b) == acierto_bool(a))
    solo_atr_gana = sum(1 for b, a in pares if acierto_bool(a) and not acierto_bool(b))
    solo_base_gana = sum(1 for b, a in pares if acierto_bool(b) and not acierto_bool(a))

    pnl_base = sum(float(b.get("pnl_neto") or 0) for b, a in pares)
    pnl_atr = sum(float(a.get("pnl_neto") or 0) for b, a in pares)

    print(f"\nPareado (mismos {n} market_id, control estricto):")
    print(f"  GBM_LATE_15M       : hit={ac_base}/{n} ({ac_base/n:.1%}) ic_bayes={ic_base:+.4f} pnl={pnl_base:+.2f}")
    print(f"  ESPACIO_ATR        : hit={ac_atr}/{n} ({ac_atr/n:.1%}) ic_bayes={ic_atr:+.4f} pnl={pnl_atr:+.2f}")
    print(f"  Concuerdan (mismo resultado ambas): {concuerdan}/{n} ({concuerdan/n:.1%})")
    print(f"  Solo ATR acierta (BASE falla)      : {solo_atr_gana}")
    print(f"  Solo BASE acierta (ATR falla)      : {solo_base_gana}")
    print(f"\nDiferencia IC pareada: {ic_atr - ic_base:+.4f} (n={n})")
    if n < 200:
        print(f"⚠️  n={n} < 200 (gate del ítem #8) — no concluir todavía, solo lectura de progreso.")


if __name__ == "__main__":
    main()
