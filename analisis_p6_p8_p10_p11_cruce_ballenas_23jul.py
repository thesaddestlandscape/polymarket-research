#!/usr/bin/env python3
"""
analisis_p6_p8_p10_p11_cruce_ballenas_23jul.py -- petición explícita Javi,
23-Jul: antes de mirar el bug de H-KELLY-HORA, cruzar 4 hipótesis del
backlog (P6 cross-asset GBM+OF BUY_NO, P8 rangos OF por par, P10 ETH15min
reversión, P11 blacklist OF 02h/07h BTC+SOL) contra TODA la infraestructura
de ballenas ya logueada en pred_features -- principio del CLAUDE.md punto 8
("ballenas es la lente por defecto, cruzar SIEMPRE").

Reutiliza _feat/_stats/_ic de hypothesis_tracker.py (no reimplementa el
cálculo de IC). Las 4 hipótesis ya fallan o están cortas de n en su forma
actual -- este script busca si un subconjunto confirmado por ballenas
(ballenas_significativo / ballenas_dentro_banda / smart_money_consensus)
separa una parte buena de una mala dentro de cada una.

Solo lectura. No toca prob_yes ni ninguna decisión real.
"""
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from hypothesis_tracker import _feat, _stats  # noqa: E402

RESULTS = Path(__file__).parent / "data/shadow/results.csv"


def _cargar():
    with open(RESULTS, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _split_por_ballenas(rows, campo="ballenas_significativo"):
    con, sin = [], []
    for r in rows:
        v = _feat(r, campo)
        if v is None:
            continue
        (con if v in (True, 1, "1", "True") else sin).append(r)
    return con, sin


def p10_eth15_reversion(rows):
    print("=== P10: ETH#15min drift_15min<-1 (UPDOWN_GBM) cruzado con ballenas ===")
    sub = [r for r in rows
           if r["strategy"] == "UPDOWN_GBM" and "ETH" in r.get("subtype", "")
           and "15min" in r.get("subtype", "")]
    filtro = [r for r in sub if (_feat(r, "drift_15min") or 0) < -1.0]
    print(f"  base filtro (sin ballenas): {_stats(filtro)}")
    con, sin = _split_por_ballenas(filtro, "ballenas_significativo")
    print(f"  ballenas_significativo=True : {_stats(con)}")
    print(f"  ballenas_significativo=False: {_stats(sin)}")
    dentro, fuera = _split_por_ballenas(filtro, "ballenas_dentro_banda")
    print(f"  ballenas_dentro_banda=True  : {_stats(dentro)}")
    print(f"  ballenas_dentro_banda=False : {_stats(fuera)}")
    smc_pos = [r for r in filtro if (_feat(r, "smart_money_consensus") or 0) > 0]
    smc_neg = [r for r in filtro if (_feat(r, "smart_money_consensus") or 0) <= 0]
    print(f"  smart_money_consensus>0     : {_stats(smc_pos)}")
    print(f"  smart_money_consensus<=0    : {_stats(smc_neg)}")
    print()


def p11_of_blacklist(rows):
    print("=== P11: ORDER_FLOW_5M h=02/07 UTC BTC+SOL BUY_NO cruzado con ballenas ===")
    for hora in (2, 7):
        sub = [r for r in rows
               if r["strategy"] == "ORDER_FLOW_5M" and r.get("decision") == "BUY_NO"
               and any(p in r.get("subtype", "") for p in ("BTC", "SOL"))
               and (_feat(r, "hora_utc") == hora)]
        print(f" -- hora={hora}h UTC: base={_stats(sub)}")
        con, sin = _split_por_ballenas(sub, "ballenas_significativo")
        print(f"    ballenas_significativo=True : {_stats(con)}")
        print(f"    ballenas_significativo=False: {_stats(sin)}")
    print()


def p8_of_rangos_par(rows):
    print("=== P8: ORDER_FLOW_5M por par, delta_ratio cruzado con ballenas_significativo ===")
    pares = ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")
    for par in pares:
        sub = [r for r in rows if r["strategy"] == "ORDER_FLOW_5M" and par in r.get("subtype", "")]
        if len(sub) < 15:
            continue
        con, sin = _split_por_ballenas(sub, "ballenas_significativo")
        s_con, s_sin = _stats(con), _stats(sin)
        print(f"  {par}: total={_stats(sub)} | ballenas=True {s_con} | ballenas=False {s_sin}")
    print()


def p6_cross_asset(rows):
    print("=== P6: overlap GBM(UPDOWN_GBM)+OF(ORDER_FLOW_5M) BUY_NO mismo activo/hora, cruzado con ballenas (lado GBM) ===")
    from collections import defaultdict
    ASSETS = ["BTC", "ETH", "SOL"]
    by_key = defaultdict(lambda: {"gbm": [], "of": []})
    for r in rows:
        if r.get("decision") != "BUY_NO":
            continue
        asset = next((a for a in ASSETS if a in r.get("subtype", "")), None)
        if not asset:
            continue
        ts = r.get("resolution_timestamp", "")
        hour_key = ts[:13]
        if not hour_key:
            continue
        key = (asset, hour_key)
        if r["strategy"] == "UPDOWN_GBM":
            by_key[key]["gbm"].append(r)
        elif r["strategy"] == "ORDER_FLOW_5M":
            by_key[key]["of"].append(r)

    overlaps = [(k, v) for k, v in by_key.items() if v["gbm"] and v["of"]]
    print(f"  n_overlaps={len(overlaps)}")
    gbm_rows_overlap = [r for _, v in overlaps for r in v["gbm"]]
    con, sin = _split_por_ballenas(gbm_rows_overlap, "ballenas_significativo")
    print(f"  lado GBM del overlap, ballenas_significativo=True : {_stats(con)}")
    print(f"  lado GBM del overlap, ballenas_significativo=False: {_stats(sin)}")
    dentro, fuera = _split_por_ballenas(gbm_rows_overlap, "ballenas_dentro_banda")
    print(f"  lado GBM del overlap, ballenas_dentro_banda=True  : {_stats(dentro)}")
    print(f"  lado GBM del overlap, ballenas_dentro_banda=False : {_stats(fuera)}")
    print()
    print("  NOTA: ORDER_FLOW_5M tiene 'ballenas_significativo' logueado pero NO "
          "'ballenas_dentro_banda'/'smart_money_consensus' -- el lado OF del "
          "overlap no se puede cruzar con la misma profundidad que el lado GBM.")
    print()


def main():
    rows = _cargar()
    print(f"[cruce ballenas P6/P8/P10/P11] {len(rows)} filas en results.csv\n")
    p10_eth15_reversion(rows)
    p11_of_blacklist(rows)
    p8_of_rangos_par(rows)
    p6_cross_asset(rows)


if __name__ == "__main__":
    main()
