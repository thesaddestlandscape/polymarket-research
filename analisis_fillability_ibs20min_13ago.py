#!/usr/bin/env python3
"""
analisis_fillability_ibs20min_13ago.py -- fill-ability real (libro
colapsado por market_id, criterio canónico de analisis_fills.py) del
bucket ibs_20min>=0.8 en la familia GBM_LATE_15M#BUY_YES
(idea_ibs20min_feature_fantasma_breakout_12ago): la señal shadow es muy
limpia (hit 37.9%->73.2% monótono) pero arquetipo A de esta familia
(edge de modelo propio) suele morir en el libro real -- este script
comprueba si ibs_20min alto sobrevive o no antes de proponer nada.
Solo lectura.
"""
import csv
import json
from collections import defaultdict
from datetime import datetime, timezone

RESULTS = "data/shadow/results.csv"
SNAPSHOTS = "data/live/libro_snapshots.csv"

FAMILIA = {"GBM_LATE_15M", "GBM_LATE_15M_TARDIO", "GBM_LATE_15M_ESPACIO_ATR",
           "GBM_LATE_15M_MULTIHORIZONTE", "GBM_LATE_15M_PYCONFIRMADO"}

# Mismo valor que shadow_postmortem.py::TWAP_FECHA_CAMBIO /
# live_trade.py::CLV_FECHA_CAMBIO_TWAP / gate_bucket_propio.py -- toda esta
# familia opera en 15min, TWAP_MARCOS_AFECTADOS. Filtrar SIEMPRE de oficio
# (feedback_twap_y_datos_completos_regla_permanente_11ago) -- sin esto, el
# 85% de las filas de 15min en results.csv son régimen pre-TWAP y
# contaminan cualquier hallazgo de esta familia.
TWAP_FECHA_CAMBIO = datetime(2026, 8, 7, tzinfo=timezone.utc)


def main():
    # 1. results.csv -> filas de la familia, BUY_YES, con ibs_20min parseado
    filas = []
    with open(RESULTS, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["strategy"] not in FAMILIA or r["decision"] != "BUY_YES":
                continue
            try:
                ts_pred = datetime.fromisoformat(r["prediction_timestamp"].replace("Z", "+00:00"))
            except (ValueError, KeyError):
                continue
            if ts_pred < TWAP_FECHA_CAMBIO:
                continue  # régimen pre-TWAP, no mezclar (CLAUDE.md, regla permanente)
            try:
                feats = json.loads(r["features"]) if r["features"] else {}
            except (json.JSONDecodeError, TypeError):
                continue
            ibs = feats.get("ibs_20min")
            if ibs is None:
                continue
            filas.append({
                "market_id": r["market_id"], "strategy": r["strategy"],
                "ibs_20min": float(ibs),
                "acierto": int(r["acierto"]), "pnl_neto": float(r["pnl_neto"]),
            })
    print(f"Filas GBM_LATE_15M*#BUY_YES con ibs_20min disponible, "
          f"POST-TWAP (prediction_timestamp>={TWAP_FECHA_CAMBIO.date()}): {len(filas)}")

    # 0. Re-verificar el patrón monótono original (idea_ibs20min_feature_
    #    fantasma_breakout_12ago) SOLO con datos post-TWAP -- el hallazgo del
    #    12-Ago no filtraba por régimen, así que puede estar mezclando 5 días
    #    post-TWAP con semanas de régimen pre-TWAP. Si no sobrevive aquí, la
    #    fill-ability de abajo sería un análisis sobre una señal que ya no es
    #    la que se creía.
    print("\n=== Paso 0: patrón ibs_20min re-verificado SOLO post-TWAP ===")
    cortes = [0.0, 0.2, 0.4, 0.6, 0.8, 1.01]
    for i in range(len(cortes) - 1):
        lo, hi = cortes[i], cortes[i + 1]
        sub = [f for f in filas if lo <= f["ibs_20min"] < hi]
        if not sub:
            print(f"  ibs_20min∈[{lo:.1f},{hi:.1f})  n=0")
            continue
        hit = sum(f["acierto"] for f in sub) / len(sub)
        pnl = sum(f["pnl_neto"] for f in sub) / len(sub)
        print(f"  ibs_20min∈[{lo:.1f},{hi:.1f})  n={len(sub):>5}  hit={hit:6.1%}  pnl/tr={pnl:+.3f}€")

    # 2. libro_snapshots.csv -> ratio_vs_stake MÁXIMO colapsado por (market_id,
    #    strategy) -- esta familia NO está en pares_permitidos_live, así que
    #    el motivo real es siempre "candidato_evaluacion" (nunca "ejecutada"/
    #    "veto_profundidad", esos motivos solo existen para tuplas live) --
    #    usamos ratio_vs_stake>=5x como criterio de fillable real, mismo
    #    umbral ya validado en P25/P27 (CLAUDE.md, "ratio_vs_stake≥5x").
    RATIO_FILLABLE = 5.0
    ratios = {}
    with open(SNAPSHOTS, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["strategy"] not in FAMILIA or r["direction"] != "BUY_YES":
                continue
            try:
                ts_snap = datetime.fromisoformat(r["timestamp_utc"].replace("Z", "+00:00"))
            except (ValueError, KeyError):
                continue
            if ts_snap < TWAP_FECHA_CAMBIO:
                continue  # mismo corte de régimen que arriba
            try:
                ratio = float(r["ratio_vs_stake"])
            except (ValueError, TypeError):
                continue
            key = (r["market_id"], r["strategy"])
            ratios[key] = max(ratio, ratios.get(key, 0.0))
    print(f"Señales en libro_snapshots.csv (colapsadas por market_id, ratio máximo entre reintentos): {len(ratios)}")

    # 3. cruce: para cada fila, ¿el libro llegó a estar fillable (ratio>=5x)
    #    alguna vez? desagregado por ibs_20min>=0.8 vs <0.8
    grupos = defaultdict(lambda: defaultdict(lambda: [0, 0, 0.0]))  # grupo -> fillable/no_fillable -> [wins,n,pnl]
    sin_snapshot = 0
    for fila in filas:
        grupo = "ibs>=0.8" if fila["ibs_20min"] >= 0.8 else "ibs<0.8"
        ratio = ratios.get((fila["market_id"], fila["strategy"]))
        if ratio is None:
            sin_snapshot += 1
            continue
        etiqueta = "fillable(ratio>=5x)" if ratio >= RATIO_FILLABLE else "no_fillable(ratio<5x)"
        a = grupos[grupo][etiqueta]
        a[0] += fila["acierto"]
        a[1] += 1
        a[2] += fila["pnl_neto"]

    print(f"Filas sin snapshot de libro correspondiente: {sin_snapshot} "
          f"(nunca llegaron a fase de captura de libro)")
    print()
    for grupo in ("ibs>=0.8", "ibs<0.8"):
        print(f"--- {grupo} ---")
        motivos = grupos.get(grupo, {})
        for etiqueta in ("fillable(ratio>=5x)", "no_fillable(ratio<5x)"):
            if etiqueta not in motivos:
                continue
            w, n, pnl = motivos[etiqueta]
            print(f"  {etiqueta:<22}{n:>5}  hit={w/n:6.1%}  pnl_medio={pnl/n:+.3f}€  pnl_total={pnl:+.2f}€")
        print()

    # 4. foco: fillable vs no_fillable dentro de ibs>=0.8 (el bucket que interesa)
    alto = grupos.get("ibs>=0.8", {})
    fillable = alto.get("fillable(ratio>=5x)")
    no_fillable = alto.get("no_fillable(ratio<5x)")
    print("=== Foco: ibs_20min>=0.8, fillable vs no_fillable ===")
    if fillable:
        print(f"fillable (ratio>=5x):    n={fillable[1]}  hit={fillable[0]/fillable[1]:.1%}  pnl_medio={fillable[2]/fillable[1]:+.3f}€")
    else:
        print("fillable: sin datos")
    if no_fillable:
        print(f"no_fillable (ratio<5x):  n={no_fillable[1]}  hit={no_fillable[0]/no_fillable[1]:.1%}  pnl_medio={no_fillable[2]/no_fillable[1]:+.3f}€")
    else:
        print("no_fillable: sin datos")


if __name__ == "__main__":
    main()
