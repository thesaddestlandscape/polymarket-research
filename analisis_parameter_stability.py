#!/usr/bin/env python3
"""Read-only: Parameter Stability — barrido de los umbrales fijados en
shadow_predict.py para ver si el resultado (IC/PnL) es una meseta estable
alrededor del valor elegido o un pico frágil (síntoma clásico de
sobreajuste al backtest puntual que los fijó).

Hueco #2 de 4 identificado en la auditoría de robustez del 21-Jul (ver
memoria idea_huecos_robustez_metodologia_21jul) — "el más barato": reusa
results.csv + features JSON ya existentes, sin datos nuevos.

Metodología (deliberadamente conservadora, ver limitación al final):
para cada umbral, el barrido solo puede ESTRECHAR el rango ya vigente hoy
en shadow_predict.py, nunca ensancharlo — un filtro que hace `return None`
(skip duro) nunca genera una fila en results.csv para las señales que caen
fuera del rango actual, así que no hay dato real con el que reconstruir
"qué habría pasado" con un umbral MÁS PERMISIVO. Sí se puede reconstruir
con total fidelidad qué habría pasado con un umbral MÁS ESTRICTO, filtrando
la población ya observada por el valor de la feature (ya logueada en
`features` JSON de cada fila) contra el candidato a umbral.

Reusa analisis_gate_riguroso.gate() (Wilson+shuffle+bootstrap PnL) para
cada punto del barrido -- mismo criterio de "concluyente" que el resto del
proyecto, no una fórmula nueva. No escribe nada, no toca ningún config.

Correr desde la raíz del repo:  python3 analisis_parameter_stability.py
"""
import csv
import json
import os
import sys
from pathlib import Path

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
from analisis_gate_riguroso import gate  # noqa: E402 — reusa Wilson+shuffle+bootstrap, no reinventa

RES = os.path.join(BASE, "data", "shadow", "results.csv")


def cargar_todas() -> list:
    filas = []
    with open(RES, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("acierto") in (None, ""):
                continue
            filas.append(row)
    return filas


def feature(row: dict, nombre: str):
    try:
        d = json.loads(row.get("features") or "{}")
    except Exception:
        return None
    return d.get(nombre)


def imprimir_barrido(titulo: str, filas_base: list, resultados: list):
    print(f"\n{'='*100}\n{titulo}  (población base n={len(filas_base)})\n{'='*100}")
    print(f"{'umbral':<22} {'n':>6} {'hit%':>7} {'ic':>8} {'wilson_lo':>10} "
          f"{'pnl/trade':>10} {'p_shuf':>8}  veredicto")
    ics, pnls = [], []
    for etiqueta, r in resultados:
        if r is None:
            print(f"{etiqueta:<22} {'sin datos (n=0)':>6}")
            continue
        pnl_media = r.get("pnl_media")
        ics.append(r["ic"])
        if pnl_media is not None:
            pnls.append(pnl_media)
        print(f"{etiqueta:<22} {r['n']:>6} {r['hit']*100:>6.1f}% {r['ic']:>+8.4f} "
              f"{r['lo']:>10.3f} {(f'{pnl_media:+.4f}' if pnl_media is not None else 'n/d'):>10} "
              f"{r['p_shuf']:>8.3f}  {r['veredicto']}")
    if len(ics) >= 2:
        rango_ic = max(ics) - min(ics)
        veredicto_estab = ("⚠️  IC varía mucho entre puntos del barrido (rango="
                            f"{rango_ic:.3f}) — posible pico frágil, revisar con cuidado"
                            if rango_ic > 0.10 else
                            f"✅ IC estable a través del barrido (rango={rango_ic:.3f}) — meseta, no pico")
        print(f"  → {veredicto_estab}")


def sweep_edge_minimo(filas_todas: list):
    """EDGE_MINIMO=0.02 (shadow_predict.py:36) — filtro global sobre
    abs(edge_neto), aplica a TODAS las estrategias. Solo se puede barrer
    hacia ARRIBA (más estricto): resultados.csv ya solo contiene filas con
    abs(edge_neto) > EDGE_MINIMO (+ slippage), las que caían por debajo
    nunca se loguearon."""
    base = [r for r in filas_todas if r.get("edge_neto") not in (None, "")]
    umbrales = [0.02, 0.03, 0.04, 0.05, 0.08]
    resultados = []
    for u in umbrales:
        subset = [r for r in base if abs(float(r["edge_neto"])) >= u]
        resultados.append((f"|edge_neto|>={u}", gate(subset)))
    imprimir_barrido("EDGE_MINIMO (actual=0.02) — TODAS las estrategias agregadas", base, resultados)

    # Desglose en las 2 familias de mayor volumen, por si el agregado oculta heterogeneidad.
    for fam in ("GBM_LATE_15M", "FAVORITO_CONFIRMADO"):
        base_fam = [r for r in base if r["strategy"] == fam]
        if len(base_fam) < 100:
            continue
        resultados_fam = []
        for u in umbrales:
            subset = [r for r in base_fam if abs(float(r["edge_neto"])) >= u]
            resultados_fam.append((f"|edge_neto|>={u}", gate(subset)))
        imprimir_barrido(f"EDGE_MINIMO — solo {fam}", base_fam, resultados_fam)


def sweep_drift_60_buyyes15m(filas_todas: list):
    """DRIFT_60_BUY_YES_15M_LO/HI=0.0/0.25 (shadow_predict.py:1434-1435,
    aplicado en :1805, dentro de s_updown_gbm()) — filtro duro para
    BUY_YES#15min. IMPORTANTE (verificado 22-Jul tras un resultado raro en
    la primera pasada, población base no cuadraba con el filtro ya vigente):
    este filtro vive SOLO en s_updown_gbm(), que solo cubre UPDOWN_GBM y
    UPDOWN_GBM_15M_TARDIO (línea 2010, envuelve s_updown_gbm sin duplicar
    lógica) — la familia GBM_LATE_15M/_TARDIO/_ESPACIO_ATR/_PYCONFIRMADO usa
    una función y un filtro TOTALMENTE DISTINTOS (GBM_LATE_DRIFT_VENT_MIN_PCT
    sobre drift_ventana, no drift_60min). Incluirlas aquí habría sido un
    bug propio (mezclar dos filtros distintos en un solo barrido). Solo se
    puede ESTRECHAR el rango [0,0.25) ya vigente."""
    familia = {"UPDOWN_GBM", "UPDOWN_GBM_15M_TARDIO"}
    base = []
    for r in filas_todas:
        if r["strategy"] not in familia or "15min" not in r["subtype"] or r["decision"] != "BUY_YES":
            continue
        d60 = feature(r, "drift_60min")
        if d60 is None:
            continue
        # d60 YA viene en % desde features JSON (verificado 22-Jul: valores
        # de muestra como 0.15/1.02/2.80 son claramente %, no fracción — un
        # primer intento con d60*100 producía una población de solo 35/1453
        # dentro de [0,0.25), incompatible con que ese filtro YA estuviera
        # aplicado en shadow_predict.py; multiplicar de nuevo por 100 era un
        # bug propio de doble escalado, no un hallazgo real).
        r["_drift_60_pct"] = d60
        base.append(r)

    # HI: estrechar el techo (0.25 actual → más bajo)
    resultados_hi = []
    for hi in (0.25, 0.20, 0.15, 0.10):
        subset = [r for r in base if 0.0 <= r["_drift_60_pct"] < hi]
        resultados_hi.append((f"HI<{hi} (LO=0.0 fijo)", gate(subset)))
    imprimir_barrido("DRIFT_60_BUY_YES_15M_HI (actual=0.25) — familia GBM BUY_YES#15min", base, resultados_hi)

    # LO: subir el suelo (0.0 actual → más alto, dentro del rango ya vigente)
    resultados_lo = []
    for lo in (0.0, 0.05, 0.10, 0.15):
        subset = [r for r in base if lo <= r["_drift_60_pct"] < 0.25]
        resultados_lo.append((f"LO>={lo} (HI=0.25 fijo)", gate(subset)))
    imprimir_barrido("DRIFT_60_BUY_YES_15M_LO (actual=0.0) — familia GBM BUY_YES#15min", base, resultados_lo)


def sweep_delta_min_max(filas_todas: list):
    """DELTA_MIN/DELTA_MAX=0.38/0.46 (shadow_predict.py:2364-2366) —
    ORDER_FLOW_5M, solo BUY_NO (delta_ratio<0), filtro sobre abs(delta_ratio).
    Solo se puede ESTRECHAR el rango [0.38,0.46) ya vigente."""
    base = []
    for r in filas_todas:
        if r["strategy"] != "ORDER_FLOW_5M" or r["decision"] != "BUY_NO":
            continue
        dr = feature(r, "delta_ratio")
        if dr is None:
            continue
        r["_delta_abs"] = abs(dr)
        base.append(r)

    resultados = []
    for lo, hi in [(0.38, 0.46), (0.39, 0.45), (0.40, 0.44), (0.41, 0.43)]:
        subset = [r for r in base if lo <= r["_delta_abs"] < hi]
        resultados.append((f"[{lo},{hi})", gate(subset)))
    imprimir_barrido("DELTA_MIN/DELTA_MAX (actual=[0.38,0.46)) — ORDER_FLOW_5M BUY_NO", base, resultados)


def main():
    filas = cargar_todas()
    print(f"[analisis_parameter_stability] results.csv cargado: {len(filas)} filas resueltas")
    sweep_edge_minimo(filas)
    sweep_drift_60_buyyes15m(filas)
    sweep_delta_min_max(filas)
    print("\n" + "="*100)
    print("LIMITACIÓN (no oculta): estos barridos solo pueden ESTRECHAR los rangos ya vigentes")
    print("hoy en shadow_predict.py (filtros de skip duro → no hay fila logueada fuera de rango).")
    print("Un barrido que ENSANCHE (ej. EDGE_MINIMO por debajo de 0.02, DRIFT_60_HI por encima de")
    print("0.25) exigiría re-simular shadow_predict.py offline sobre klines históricos — no hecho aquí.")
    print("="*100)


if __name__ == "__main__":
    main()
