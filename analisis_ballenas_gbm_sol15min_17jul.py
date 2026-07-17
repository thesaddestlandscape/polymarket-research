#!/usr/bin/env python3
"""Read-only, one-off (17-Jul, petición Javi: "con SOL testeamos con el
pozo de la sabiduría para ver que pasa"). GBM_LATE_15M#SOL#15min#BUY_YES
sigue PAUSADA (16-Jul, últimos 30 reales hit=36.7%, shadow tampoco se
recuperó -- ver project_sol_pausa_selectiva_16jul). A diferencia de
FAVORITO_CONFIRMADO#SOL#15min#BUY_YES (analizada hoy vía proxy
candidato_evaluacion), esta estrategia estuvo LIVE hasta hace 1 día, así
que libro_snapshots.csv tiene intentos REALES de ejecución (motivo=
ejecutada/veto_profundidad), no solo el proxy -- mejor calidad de dato.

Mismo método que analisis_ballenas_favorito_15min_buyyes_17jul.py: cruza
market_id->condition_id (data/markets/*.csv) contra
ballenas_timing_history.csv (una sola pasada) para ver si el mismo
mecanismo (ballenas consumiendo YES temprano en los mercados vetados)
aplica aquí, o si SOL tiene una historia distinta.

No escribe nada, no toca dinero ni config.
Uso: python3 analisis_ballenas_gbm_sol15min_17jul.py
"""
import csv
from pathlib import Path

import analisis_ballenas_fillability_16jul as _abf16
from analisis_ballenas_fillability_16jul import mapear_condition_a_market

REPO = Path(__file__).resolve().parent
LIBRO = REPO / "data" / "live" / "libro_snapshots.csv"
BALLENAS = REPO / "data" / "shadow" / "ballenas_timing_history.csv"

_abf16.ARCHIVOS_MARKETS_RECIENTES = 30  # cobertura completa, no solo últimos 5

STRATEGY = "GBM_LATE_15M"
SUBTYPE = "SOL#15min"
DIRECTION = "BUY_YES"
ACTIVO = "SOL"
MARCO_BALLENAS = "15m"


def grupos_mercados_reales() -> tuple[set, set]:
    """(ejecutada, veto_profundidad) -- intentos REALES de ejecución (no
    proxy), mientras la tupla estuvo live (hasta 16-Jul)."""
    ejecutada, vetada = set(), set()
    with open(LIBRO, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("strategy") != STRATEGY or r.get("subtype") != SUBTYPE or r.get("direction") != DIRECTION:
                continue
            if r.get("motivo") == "ejecutada":
                ejecutada.add(r["market_id"])
            elif r.get("motivo") == "veto_profundidad":
                vetada.add(r["market_id"])
    return ejecutada, vetada


def _nuevo_acc():
    return {"n_yes": 0, "n_no": 0, "precios_yes": [], "precios_no": [],
            "restantes_yes": [], "restantes_no": []}


def _cerrar(acc, n_mercados):
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
        "restante_min_mediana_yes": _med(acc["restantes_yes"]),
        "restante_min_mediana_no": _med(acc["restantes_no"]),
    }


def main():
    ejecutada_mids, vetada_mids = grupos_mercados_reales()
    print(f"Intentos reales GBM_LATE_15M#SOL#15min#BUY_YES: ejecutada={len(ejecutada_mids)} "
          f"veto_profundidad={len(vetada_mids)}")

    mapa_mid_cid = mapear_condition_a_market()
    ejecutada_cids = {mapa_mid_cid[m] for m in ejecutada_mids if m in mapa_mid_cid}
    vetada_cids = {mapa_mid_cid[m] for m in vetada_mids if m in mapa_mid_cid}
    print(f"Con condition_id conocido: ejecutada={len(ejecutada_cids)} veto_profundidad={len(vetada_cids)}")

    cid_a_bucket = {}
    for cid in ejecutada_cids:
        cid_a_bucket[cid] = "ejecutada"
    for cid in vetada_cids:
        cid_a_bucket[cid] = "veto_profundidad"  # si un mercado aparece en ambos, se queda con el peor caso (último)

    acumuladores = {"ejecutada": _nuevo_acc(), "veto_profundidad": _nuevo_acc()}
    with open(BALLENAS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["activo"] != ACTIVO or r["marco"] != MARCO_BALLENAS:
                continue
            bucket = cid_a_bucket.get(r["condition_id"])
            if bucket is None:
                continue
            try:
                precio = float(r["precio"])
                restante = float(r["restante_min"])
            except (ValueError, KeyError):
                continue
            acc = acumuladores[bucket]
            if r.get("compro_yes") in ("1", "True", "true"):
                acc["n_yes"] += 1
                acc["precios_yes"].append(precio)
                acc["restantes_yes"].append(restante)
            elif r.get("compro_yes") in ("0", "False", "false"):
                acc["n_no"] += 1
                acc["precios_no"].append(precio)
                acc["restantes_no"].append(restante)

    se = _cerrar(acumuladores["ejecutada"], len(ejecutada_cids))
    sv = _cerrar(acumuladores["veto_profundidad"], len(vetada_cids))

    print(f"\n=== GBM_LATE_15M#SOL#15min#BUY_YES: ejecutada (real) vs veto_profundidad (real) ===")
    print(f"{'':22s} {'ejecutada':>20s} {'veto_profundidad':>20s}")
    print(f"{'trades ballena':22s} {se['n_trades_ballena']:>20d} {sv['n_trades_ballena']:>20d}")
    print(f"{'% lado YES (nuestro)':22s} {str(se['pct_yes'])+'%':>20s} {str(sv['pct_yes'])+'%':>20s}")
    print(f"{'precio medio YES':22s} {str(se['precio_medio_yes']):>20s} {str(sv['precio_medio_yes']):>20s}")
    print(f"{'% lado NO':22s} {str(se['pct_no'])+'%':>20s} {str(sv['pct_no'])+'%':>20s}")
    print(f"{'precio medio NO':22s} {str(se['precio_medio_no']):>20s} {str(sv['precio_medio_no']):>20s}")
    print(f"{'restante_min YES':22s} {str(se['restante_min_mediana_yes']):>20s} {str(sv['restante_min_mediana_yes']):>20s}")
    print(f"{'restante_min NO':22s} {str(se['restante_min_mediana_no']):>20s} {str(sv['restante_min_mediana_no']):>20s}")


if __name__ == "__main__":
    main()
