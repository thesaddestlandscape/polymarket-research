#!/usr/bin/env python3
"""Read-only, one-off (17-Jul, petición Javi: "cruzalo con ballenas"):
¿el mecanismo de selección adversa que ballenas ya explicó para
FAVORITO_CONFIRMADO#*#15min#BUY_NO (16-Jul, ver
idea_ballenas_explica_seleccion_adversa_favoritoconfirmado_16jul) también
aplica al lado BUY_YES? Motivo: analisis_ic_fillable.py (mismo día) encontró
selección adversa REAL (p_shuffle<0.10) en FAVORITO_CONFIRMADO#SOL/ETH#15min
#BUY_YES -- IC fillable ~mitad del IC shadow que Kelly usa hoy.

Mismo método que el hallazgo BUY_NO: mapea market_id->condition_id desde
data/markets/*.csv, cruza contra ballenas_timing_history.csv (ya trae
acierto/compro_yes precomputados, sin necesidad de re-derivar desde
outcome_real), separa los mercados en dos grupos usando libro_snapshots.csv
(motivo=candidato_evaluacion): fillable (ratio_vs_stake>=5, conseguimos
ejecutar) vs no_fillable (ratio<5, vetados por profundidad -- el grupo que
NO podemos capturar). Compara concentración/precio/timing de ballenas del
lado YES (el nuestro) vs NO (el que nos compite por la profundidad ask que
necesitamos) en ambos grupos.

Solo lectura. No toca dinero ni config.
"""
import csv
from pathlib import Path

import analisis_ballenas_fillability_16jul as _abf16
from analisis_ballenas_fillability_16jul import mapear_condition_a_market

REPO = Path(__file__).resolve().parent
LIBRO = REPO / "data/live/libro_snapshots.csv"
BALLENAS = REPO / "data/shadow/ballenas_timing_history.csv"
RATIO_MIN = 5.0

# condition_id existe en data/markets/*.csv solo desde el 10-Jul (8 ficheros
# disponibles hoy) -- el default de analisis_ballenas_fillability_16jul.py
# (últimos 5) se queda corto para tuplas live desde el 14-Jul; usar todos.
_abf16.ARCHIVOS_MARKETS_RECIENTES = 30

TUPLAS = [("SOL", "15min", "15m"), ("ETH", "15min", "15m")]
STRATEGY = "FAVORITO_CONFIRMADO"
DIRECTION = "BUY_YES"


def grupos_mercados(activo: str, subtype: str) -> tuple[set, set]:
    """(fillable, no_fillable) -- market_id de candidato_evaluacion,
    separados por ratio_vs_stake>=RATIO_MIN."""
    fillable, no_fillable = set(), set()
    with open(LIBRO, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r.get("motivo") != "candidato_evaluacion" or r.get("strategy") != STRATEGY
                    or r.get("subtype") != subtype or r.get("direction") != DIRECTION):
                continue
            try:
                ratio = float(r.get("ratio_vs_stake") or 0)
            except ValueError:
                ratio = 0
            (fillable if ratio >= RATIO_MIN else no_fillable).add(r["market_id"])
    return fillable, no_fillable


def _nuevo_acumulador():
    return {"n_yes": 0, "n_no": 0, "precios_yes": [], "precios_no": [],
            "restantes_yes": [], "restantes_no": []}


def _cerrar(acc: dict, n_mercados: int) -> dict:
    n_tot = acc["n_yes"] + acc["n_no"]

    def _med(xs):
        xs = sorted(xs)
        return xs[len(xs) // 2] if xs else None

    return {
        "n_mercados": n_mercados, "n_trades_ballena": n_tot,
        "pct_yes": round(100 * acc["n_yes"] / n_tot, 1) if n_tot else None,
        "precio_medio_yes": round(sum(acc["precios_yes"]) / len(acc["precios_yes"]), 4) if acc["precios_yes"] else None,
        "pct_no": round(100 * acc["n_no"] / n_tot, 1) if n_tot else None,
        "precio_medio_no": round(sum(acc["precios_no"]) / len(acc["precios_no"]), 4) if acc["precios_no"] else None,
        "restante_min_mediana_no": _med(acc["restantes_no"]),
        "restante_min_mediana_yes": _med(acc["restantes_yes"]),
    }


def main():
    mapa_mid_cid = mapear_condition_a_market()

    # cid -> (activo, marco_ballenas, "fillable"|"no_fillable") para las 2 tuplas
    # a la vez -- así ballenas_timing_history.csv (61MB) se recorre UNA sola
    # vez en total, no 4 veces (antes: timeout a los 180s).
    cid_a_bucket = {}
    n_mercados = {}  # (activo, bucket) -> conteo de mercados (para el resumen)
    for activo, subtype_asset, marco_ballenas in TUPLAS:
        subtype = f"{activo}#{subtype_asset}"
        fillable_mids, no_fillable_mids = grupos_mercados(activo, subtype)
        for bucket, mids in (("fillable", fillable_mids), ("no_fillable", no_fillable_mids)):
            cids = {mapa_mid_cid[m] for m in mids if m in mapa_mid_cid}
            n_mercados[(activo, bucket)] = (len(mids), len(cids))
            for cid in cids:
                cid_a_bucket[cid] = (activo, marco_ballenas, bucket)

    acumuladores = {}  # (activo, bucket) -> acumulador
    with open(BALLENAS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            info = cid_a_bucket.get(r["condition_id"])
            if info is None or r["activo"] != info[0] or r["marco"] != info[1]:
                continue
            activo, _, bucket = info
            try:
                precio = float(r["precio"])
                restante = float(r["restante_min"])
            except (ValueError, KeyError):
                continue
            acc = acumuladores.setdefault((activo, bucket), _nuevo_acumulador())
            if r.get("compro_yes") in ("1", "True", "true"):
                acc["n_yes"] += 1
                acc["precios_yes"].append(precio)
                acc["restantes_yes"].append(restante)
            elif r.get("compro_yes") in ("0", "False", "false"):
                acc["n_no"] += 1
                acc["precios_no"].append(precio)
                acc["restantes_no"].append(restante)

    for activo, subtype_asset, marco_ballenas in TUPLAS:
        subtype = f"{activo}#{subtype_asset}"
        n_fill_mids, n_fill_cids = n_mercados[(activo, "fillable")]
        n_nofill_mids, n_nofill_cids = n_mercados[(activo, "no_fillable")]
        sf = _cerrar(acumuladores.get((activo, "fillable"), _nuevo_acumulador()), n_fill_cids)
        sn = _cerrar(acumuladores.get((activo, "no_fillable"), _nuevo_acumulador()), n_nofill_cids)

        print(f"\n=== {STRATEGY}#{subtype}#{DIRECTION} ===")
        print(f"mercados fillable: {n_fill_mids} (con condition_id: {n_fill_cids}) | "
              f"no_fillable: {n_nofill_mids} (con condition_id: {n_nofill_cids})")
        print(f"{'':20s} {'fillable (ejecutamos)':>28s} {'no_fillable (vetados)':>28s}")
        print(f"{'trades ballena':20s} {sf['n_trades_ballena']:>28d} {sn['n_trades_ballena']:>28d}")
        print(f"{'% lado YES (nuestro)':20s} {str(sf['pct_yes'])+'%':>28s} {str(sn['pct_yes'])+'%':>28s}")
        print(f"{'precio medio YES':20s} {str(sf['precio_medio_yes']):>28s} {str(sn['precio_medio_yes']):>28s}")
        print(f"{'% lado NO (rival)':20s} {str(sf['pct_no'])+'%':>28s} {str(sn['pct_no'])+'%':>28s}")
        print(f"{'precio medio NO':20s} {str(sf['precio_medio_no']):>28s} {str(sn['precio_medio_no']):>28s}")
        print(f"{'restante_min NO':20s} {str(sf['restante_min_mediana_no']):>28s} {str(sn['restante_min_mediana_no']):>28s}")
        print(f"{'restante_min YES':20s} {str(sf['restante_min_mediana_yes']):>28s} {str(sn['restante_min_mediana_yes']):>28s}")


if __name__ == "__main__":
    main()
