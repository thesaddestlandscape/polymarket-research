#!/usr/bin/env python3
"""Read-only: benchmark zero-intelligence para ORDER_FLOW_5M (propuesta #7,
backlog quant-desk 13-jul, Gode&Sunder). ORDER_FLOW_5M sigue con IC agregado
bajo (+0.013) pese a n=1574 — la pregunta del paper: ¿el patrón que SÍ se ve
en su bucket filtrado (BUY_NO, delta_ratio en zona, IC=+0.044 n=934) se
distingue de un flujo aleatorio con la misma distribución de resoluciones, o
es selección de zona post-hoc sobre ruido?

Reutiliza wilson_ci/ic_bayes/shuffle_percentile de analisis_gate_riguroso.py
(mismo control aleatorio ya validado el 10-Jul) en vez de reimplementar.
No toca config ni estrategia — solo lectura de results.csv.
"""
import csv
from collections import defaultdict

from analisis_gate_riguroso import wilson_ci, ic_bayes, shuffle_percentile

RES = "data/shadow/results.csv"


def cargar_of_buy_no():
    """Todas las filas ORDER_FLOW_5M#{cualquier par}#5min#BUY_NO resueltas,
    agrupadas por par y en agregado — es el bucket real que opera hoy en
    shadow (DELTA_MIN/DELTA_MAX ya filtran en shadow_predict.py, esto solo
    lee el resultado)."""
    por_par = defaultdict(list)
    agregado = []
    with open(RES) as f:
        for row in csv.DictReader(f):
            if row.get("strategy") != "ORDER_FLOW_5M":
                continue
            if row.get("decision") != "BUY_NO":
                continue
            if row.get("acierto") in (None, ""):
                continue
            if not row.get("subtype", "").endswith("#5min"):
                continue
            par = row["subtype"].split("#", 1)[0]
            por_par[par].append(row)
            agregado.append(row)
    return por_par, agregado


def evaluar(nombre, rows):
    n = len(rows)
    if n == 0:
        print(f"{nombre:<20} sin datos")
        return
    aciertos = sum(1 for r in rows if r["acierto"] == "1")
    hit = aciertos / n
    ic = ic_bayes(aciertos, n)
    lo, hi = wilson_ci(aciertos, n)
    p_shuf = shuffle_percentile(rows, ic)
    veredicto = "BATE zero-intelligence" if (lo > 0.5 and p_shuf <= 0.05) else "NO se distingue de ruido"
    print(f"{nombre:<20} n={n:<5} hit={hit*100:5.1f}% ic={ic:+.4f} "
          f"Wilson90%=[{lo:.3f},{hi:.3f}] p_shuffle={p_shuf:.3f}  -> {veredicto}")


def main():
    por_par, agregado = cargar_of_buy_no()
    print("ORDER_FLOW_5M#BUY_NO (zona delta_ratio filtrada) vs control aleatorio (Gode&Sunder)\n")
    evaluar("AGREGADO (todos pares)", agregado)
    print()
    for par in sorted(por_par):
        evaluar(par, por_par[par])


if __name__ == "__main__":
    main()
