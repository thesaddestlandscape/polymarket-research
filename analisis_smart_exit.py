#!/usr/bin/env python3
"""
analisis_smart_exit.py — Calibración OFFLINE del umbral de salida anticipada.

Read-only (paso 2 de idea_smart_exit): cruza data/live/smart_exit_prices.csv
(ticks de precio de posiciones OPEN, logueados por smart_exit_logger cada 1min)
con data/live/trades.csv (outcome real de cada posición) y simula: ¿qué PnL
habría dado salir en el primer tick que cruza cada umbral, vs aguantar a
resolución como hoy?

Realismo de venta (la salida cruza el spread y paga fee taker):
  precio_lado logueado es MID (aprox paso 1) → se aplica un haircut
  configurable (HAIRCUT_VENTA) que agrupa medio-spread + fee de venta.
  Con pocos datos el veredicto es orientativo; el corte formal exige
  N_MIN_POSICIONES posiciones cerradas con ticks.

Uso: python3 analisis_smart_exit.py
No escribe nada, no toca órdenes. Gate de decisión: n>=30 posiciones.
"""

import csv
from collections import defaultdict
from pathlib import Path

PRICES_CSV = Path("data/live/smart_exit_prices.csv")
TRADES_CSV = Path("data/live/trades.csv")

HAIRCUT_VENTA = 0.06     # fracción del valor de salida: ~2-3c de spread + fee venta ~3.78%
N_MIN_POSICIONES = 30    # mismo listón que el resto de decisiones del proyecto

# Umbrales a simular: take-profit (salir si precio del lado >= X)
TP_GRID = [0.70, 0.75, 0.80, 0.85, 0.90, 0.95]
# Stop-loss (salir si precio del lado <= Y) — se simula por separado
SL_GRID = [0.10, 0.15, 0.20, 0.25, 0.30]

# Stop-loss en € de pérdida no realizada (16-Jul, petición Javi): dispara si
# el pnl "de salir ahora" cae por debajo de -X€. La 1ª pasada (misma fecha)
# usó pnl_salida_eur crudo = mid, SIN haircut ("optimista", ver idea_smart_exit.md)
# y dio +12.61€ de mejora con umbral -0.30€ sobre 27 pérdidas. Esta repite la
# misma mecánica pero con el HAIRCUT_VENTA ya validado (spread+fee reales).
EUR_SL_GRID = [0.30, 0.50, 0.70]


def cargar():
    if not PRICES_CSV.exists():
        raise SystemExit(f"No existe {PRICES_CSV} — ¿smart_exit_logger corriendo?")
    ticks = defaultdict(list)  # market_id -> [filas ordenadas por ts]
    with open(PRICES_CSV, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            ticks[r["market_id"]].append(r)
    for mid in ticks:
        ticks[mid].sort(key=lambda r: r["ts_utc"])

    cierres = {}  # market_id -> pnl_neto_eur real (posición CLOSED)
    with open(TRADES_CSV, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("status") == "CLOSED" and r.get("pnl_neto_eur"):
                cierres[r["market_id"]] = float(r["pnl_neto_eur"])
    return ticks, cierres


def simular(ticks, cierres, condicion):
    """condicion(precio_lado) -> True = salir en ese tick.
    Devuelve (n, pnl_sim, pnl_real, n_salidas)."""
    n = pnl_sim = pnl_real = n_salidas = 0
    for mid, filas in ticks.items():
        if mid not in cierres:
            continue  # posición aún abierta o sin cierre casado — no evaluable
        n += 1
        real = cierres[mid]
        pnl_real += real
        salida = None
        for r in filas:
            try:
                p = float(r["precio_lado"])
                stake = float(r["stake_eur"])
                valor = float(r["valor_salida_eur"])
            except (ValueError, KeyError):
                continue
            if condicion(p):
                salida = valor * (1.0 - HAIRCUT_VENTA) - stake
                break
        if salida is not None:
            pnl_sim += salida
            n_salidas += 1
        else:
            pnl_sim += real
    return n, pnl_sim, pnl_real, n_salidas


def simular_perdidas_eur(ticks, cierres, umbral_eur):
    """Solo posiciones que CERRARON en pérdida real (el universo de la
    pregunta de Javi: ¿se puede cortar antes una perdedora?). Dispara en el
    primer tick donde el pnl HAIRCUT-AJUSTADO (no el crudo mid de la 1ª
    pasada) cruza -umbral_eur. Devuelve (n_perdidas, pnl_sim, pnl_real,
    n_disparos)."""
    n = pnl_sim = pnl_real = n_disparos = 0
    for mid, filas in ticks.items():
        real = cierres.get(mid)
        if real is None or real >= 0:
            continue  # no es una pérdida real cerrada
        n += 1
        pnl_real += real
        salida = None
        for r in filas:
            try:
                stake = float(r["stake_eur"])
                valor = float(r["valor_salida_eur"])
            except (ValueError, KeyError):
                continue
            valor_ajustado = valor * (1.0 - HAIRCUT_VENTA)
            pnl_ajustado = valor_ajustado - stake
            if pnl_ajustado <= -umbral_eur:
                salida = pnl_ajustado
                break
        if salida is not None:
            pnl_sim += salida
            n_disparos += 1
        else:
            pnl_sim += real
    return n, pnl_sim, pnl_real, n_disparos


def main():
    ticks, cierres = cargar()
    evaluables = [m for m in ticks if m in cierres]
    print(f"Posiciones con ticks: {len(ticks)} | cerradas y evaluables: {len(evaluables)}")
    if len(evaluables) < N_MIN_POSICIONES:
        print(f"⚠️  n={len(evaluables)} < {N_MIN_POSICIONES} — resultados ORIENTATIVOS, no decidir umbral todavía.")
    print(f"Haircut de venta aplicado: {HAIRCUT_VENTA:.0%} del valor de salida\n")

    print("TAKE-PROFIT (salir si precio_lado >= X):")
    print(f"{'X':>6} {'n':>4} {'salidas':>8} {'pnl_sim':>9} {'pnl_real':>9} {'delta':>8}")
    for x in TP_GRID:
        n, sim, real, ns = simular(ticks, cierres, lambda p, x=x: p >= x)
        if n:
            print(f"{x:>6.2f} {n:>4} {ns:>8} {sim:>+9.2f} {real:>+9.2f} {sim-real:>+8.2f}")

    print("\nSTOP-LOSS (salir si precio_lado <= Y):")
    print(f"{'Y':>6} {'n':>4} {'salidas':>8} {'pnl_sim':>9} {'pnl_real':>9} {'delta':>8}")
    for y in SL_GRID:
        n, sim, real, ns = simular(ticks, cierres, lambda p, y=y: p <= y)
        if n:
            print(f"{y:>6.2f} {n:>4} {ns:>8} {sim:>+9.2f} {real:>+9.2f} {sim-real:>+8.2f}")

    print("\nSTOP-LOSS en € de pérdida no realizada (solo posiciones que cerraron en pérdida,")
    print(f"haircut {HAIRCUT_VENTA:.0%} ya aplicado al valor de salida en cada tick — spread+fee reales):")
    print(f"{'umbral':>7} {'n_perdidas':>10} {'disparos':>8} {'pnl_sim':>9} {'pnl_real':>9} {'mejora':>8}")
    for u in EUR_SL_GRID:
        n, sim, real, ns = simular_perdidas_eur(ticks, cierres, u)
        if n:
            print(f"{-u:>7.2f} {n:>10} {ns:>8} {sim:>+9.2f} {real:>+9.2f} {sim-real:>+8.2f}")

    print("\nDecisión: delta>0 sostenido con n>=30 → proponer umbral a Javi (toca dinero).")


if __name__ == "__main__":
    main()
