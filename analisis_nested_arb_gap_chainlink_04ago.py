#!/usr/bin/env python3
"""
analisis_nested_arb_gap_chainlink_04ago.py — Reorienta el filtro de
nested_arb_scanner.py/P13 con datos reales (petición Javi 04-Ago,
"reoriéntalo atendiendo a los objetivos del proyecto").

Hallazgo previo (idea_p13_nested_arb_corridor_collector_reanalisis_04ago):
el filtro gap_opens_pct<0.04% / depth>$15 (calibrado 07-Jul con n=7) NO
predice roturas de garantía con n=343 -- las roturas tienen gap MENOR y
depth MAYOR que el umbral, justo lo contrario de la teoría original.

Hipótesis nueva (ya anotada en el docstring de nested_arb_scanner.py, sin
probar hasta hoy): o_inner/o_outer se calculan desde data/prices/{date}.csv
(nuestra fuente propia, tolerancia ±3min) -- si esa fuente DISCREPA de
Chainlink (la fuente de resolución OFICIAL de Polymarket) sobre CUÁL
apertura es mayor, compramos el combo equivocado sin saberlo: la garantía
matemática asume que o_inner/o_outer están bien ordenados, pero si el gap
real es pequeño, un error de medición puede invertir el orden percibido.

Metodología: para cada posición CLOSED con cobertura Chainlink (ts_cierre
>=20-Jul, cuando fetch_chainlink_prices.py empezó a capturar), recalcula
o_inner/o_outer con AMBAS fuentes (misma función _precio_en, tol_min=3) y
compara:
  1. ¿Coincide el SIGNO del gap (qué apertura es mayor) entre fuentes?
  2. ¿La magnitud del gap real (Chainlink) es sistemáticamente distinta
     en las roturas vs las buenas?
"""
import csv
import glob
import gzip
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
DIR_PRICES = REPO / "data" / "prices"
SIM_CSV = REPO / "data" / "shadow" / "nested_arb_sim.csv"

NESTING_MIN = {
    "5min15m": (5, 15),
    "15min60m": (15, 60),
}


def _cargar_precios(prefijo: str, fechas: set) -> dict:
    """{asset: {epoch_min: precio}} para las fechas dadas. prefijo='' para
    nuestra fuente propia (data/prices/YYYY-MM-DD.csv), prefijo='chainlink_'
    para la oficial. Soporta .csv y .csv.gz (política de retención 03-Ago
    comprime >5 días -- sin esto la mayoría de fechas de chainlink_*.csv.gz
    se leían como "sin fichero", perdiendo casi todo el cruce)."""
    out = {}
    for fecha in fechas:
        p = DIR_PRICES / f"{prefijo}{fecha}.csv"
        p_gz = DIR_PRICES / f"{prefijo}{fecha}.csv.gz"
        if p.exists():
            _abrir, ruta = open, p
        elif p_gz.exists():
            _abrir, ruta = gzip.open, p_gz
        else:
            continue
        with _abrir(ruta, "rt", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                try:
                    ep = int(datetime.fromisoformat(
                        r["timestamp_utc"].replace("Z", "+00:00")).timestamp()) // 60
                    out.setdefault(r["asset"].upper(), {})[ep] = float(r["price_usd"])
                except Exception:
                    continue
    return out


def _precio_en(precios: dict, act: str, dt: datetime, tol_min: int = 3):
    ep = int(dt.timestamp()) // 60
    serie = precios.get(act, {})
    for d in range(tol_min + 1):
        for e in (ep - d, ep + d):
            if e in serie:
                return serie[e]
    return None


def main():
    rows = list(csv.DictReader(open(SIM_CSV, encoding="utf-8")))
    cerradas = [r for r in rows if r["status"] == "CLOSED" and r.get("ts_cierre", "") >= "2026-07-20"]
    print(f"cerradas con posible cobertura Chainlink (ts_cierre>=20-Jul): {len(cerradas)}")

    # Fechas necesarias (end_utc y el día anterior, por si inner_ini/outer_ini cruzan medianoche)
    fechas = set()
    for r in cerradas:
        try:
            end_dt = datetime.fromisoformat(r["end_utc"].replace("Z", "+00:00"))
        except Exception:
            continue
        fechas.add(end_dt.date().isoformat())
        fechas.add((end_dt.date() - timedelta(days=1)).isoformat())

    print("cargando precios propios y Chainlink...")
    precios_propios = _cargar_precios("", fechas)
    precios_chainlink = _cargar_precios("chainlink_", fechas)

    n_comparables = 0
    coincide_signo = {"buenas": 0, "rotas": 0}
    discrepa_signo = {"buenas": 0, "rotas": 0}
    gaps_chainlink_abs = {"buenas": [], "rotas": []}

    for r in cerradas:
        try:
            end_dt = datetime.fromisoformat(r["end_utc"].replace("Z", "+00:00"))
        except Exception:
            continue
        nesting = r["nesting"]
        if nesting not in NESTING_MIN:
            continue
        inner_min, outer_min = NESTING_MIN[nesting]
        inner_ini = end_dt - timedelta(minutes=inner_min)
        outer_ini = end_dt - timedelta(minutes=outer_min)
        act = r["activo"]

        o_in_p = _precio_en(precios_propios, act, inner_ini)
        o_out_p = _precio_en(precios_propios, act, outer_ini)
        o_in_c = _precio_en(precios_chainlink, act, inner_ini)
        o_out_c = _precio_en(precios_chainlink, act, outer_ini)
        if None in (o_in_p, o_out_p, o_in_c, o_out_c):
            continue

        n_comparables += 1
        es_buena = r.get("garantia_ok") in ("True", "1", "true")
        grupo = "buenas" if es_buena else "rotas"

        signo_propio = o_in_p >= o_out_p
        signo_chainlink = o_in_c >= o_out_c
        gap_chainlink_pct = abs((o_in_c / o_out_c - 1) * 100)
        gaps_chainlink_abs[grupo].append(gap_chainlink_pct)

        if signo_propio == signo_chainlink:
            coincide_signo[grupo] += 1
        else:
            discrepa_signo[grupo] += 1

    print(f"\ncomparables (ambas fuentes con dato en inner_ini y outer_ini): {n_comparables}\n")
    for grupo in ("buenas", "rotas"):
        total = coincide_signo[grupo] + discrepa_signo[grupo]
        if total == 0:
            print(f"{grupo}: sin comparables")
            continue
        pct_discrepa = 100 * discrepa_signo[grupo] / total
        gaps = gaps_chainlink_abs[grupo]
        gap_medio = sum(gaps) / len(gaps) if gaps else None
        print(f"{grupo}: n={total}  discrepancia de signo (orden invertido según Chainlink)="
              f"{discrepa_signo[grupo]}/{total} ({pct_discrepa:.1f}%)  "
              f"gap_chainlink_abs medio={gap_medio:.4f}%" if gap_medio is not None else "")


if __name__ == "__main__":
    main()
