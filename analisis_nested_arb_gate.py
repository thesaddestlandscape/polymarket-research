#!/usr/bin/env python3
"""Gate de promoción a live de nested_arb, SEGMENTADO por nesting.

Origen (12-Jul): el reporte agregado ("34 filtradas, 94.1% garantía") mezclaba
dos poblaciones con perfiles de riesgo distintos. Desglosando: 5min-en-15min
(n=28 filtradas) tiene garantía 100% — el filtro gap<0.04%/depth>$15 (tuneado
sobre datos mayormente de esta ventana) funciona perfecto ahí. 15min-en-60min
(n=6 filtradas) tiene garantía solo 66.7% — el MISMO filtro no transfiere
bien a esa ventana (la referencia de apertura de un mercado 60min se mide
más lejos en el tiempo del cierre; con n=6 no hay datos para re-tunear un
umbral propio, e intentarlo con n tan bajo sería sobreajustar a 2-3 puntos).

Este script NO propone un nuevo umbral numérico — con n=6 cualquier corte
sería ruido. Reporta el gate correcto (n≥30 cerradas, garantía~100%)
SEPARADO por nesting, para no repetir el error de promediar dos riesgos
distintos. Read-only, no toca dinero ni config.
"""
import csv

SIM_CSV = "data/shadow/nested_arb_sim.csv"
GATE_N = 30
GATE_GARANTIA_PCT = 97.0


def _es_bool(v) -> bool:
    return v in ("1", "True", "true")


def main() -> None:
    rows = list(csv.DictReader(open(SIM_CSV, encoding="utf-8")))
    cerradas = [r for r in rows if r.get("status") == "CLOSED"]
    filtradas = [r for r in cerradas if _es_bool(r.get("pasa_filtro"))]

    buckets = {}
    for r in filtradas:
        nesting = r.get("nesting", "desconocido")
        buckets.setdefault(nesting, []).append(r)

    print(f"nested_arb_sim.csv: {len(rows)} filas | {len(cerradas)} cerradas | "
          f"{len(filtradas)} filtradas (pasa_filtro=1)\n")
    print(f"Gate de promoción a live: n>={GATE_N} cerradas-filtradas Y garantía>={GATE_GARANTIA_PCT}%\n")

    for nesting, grupo in sorted(buckets.items(), key=lambda kv: -len(kv[1])):
        n = len(grupo)
        ok = sum(1 for r in grupo if _es_bool(r.get("garantia_ok")))
        pct = ok / n * 100 if n else 0
        pnl = sum(float(r.get("pnl_usd") or 0) for r in grupo)
        pasa_gate = n >= GATE_N and pct >= GATE_GARANTIA_PCT
        estado = "✅ GATE OK — proponer a Javi" if pasa_gate else "⛔ no listo"
        print(f"{nesting:15s} n={n:3} garantia_ok={ok}/{n}={pct:5.1f}%  pnl_total={pnl:+.2f}$  {estado}")
        if not pasa_gate and n < GATE_N:
            print(f"                → faltan {GATE_N - n} cerradas-filtradas para evaluar el gate")
        elif not pasa_gate:
            fallos = [r for r in grupo if not _es_bool(r.get("garantia_ok"))]
            print(f"                → {len(fallos)} fallo(s) de garantía, revisar antes de proponer:")
            for f in fallos:
                print(f"                  {f.get('activo')} {f.get('combo')} "
                      f"gap={f.get('gap_opens_pct')}% depth=${f.get('depth_usd')} pnl={f.get('pnl_usd')}$")


if __name__ == "__main__":
    main()
