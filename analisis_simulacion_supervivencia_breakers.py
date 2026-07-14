#!/usr/bin/env python3
"""
Simulación de supervivencia de los circuit breakers (14-Jul, sesión
siguiente, petición Javi tras dispararse el breaker de racha con
bankroll=7.10€): "todo el mundo hace backtest de la estrategia, casi
nadie hace backtest del propio reto (las reglas de riesgo)". Los
breakers actuales (racha=4, freno_diario=30%, bankroll_minimo=1€) se han
calibrado REACTIVAMENTE, incidente a incidente (ver notas en
config_live.json: freno_diario 0.15→0.30 tras -6.54€ el 03-Jul, suelo
8€→3€→1€), nunca simulados sistemáticamente contra el histórico real.

Método: usa la secuencia REAL de trades.csv (no shadow — refleja
selección adversa/fill-ability reales), preservando el orden cronológico
real (para no perder rachas reales de pérdidas correladas). Para cada
punto de partida posible en el histórico, "reproduce" esa secuencia como
si empezara HOY desde el bankroll actual, aplicando los breakers reales
día a día (agrupando trades por día Madrid real), hasta que la cuenta
revienta (bankroll<=suelo) o se recupera (bankroll>=objetivo) o se agota
el histórico disponible.

Puramente análisis retrospectivo — no toca live_trade.py/config_live.json,
no cambia ningún parámetro real.

Uso: python3 analisis_simulacion_supervivencia_breakers.py
     [--racha N] [--freno-diario PCT] [--suelo EUR] [--objetivo EUR]
"""
import argparse
import csv
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

TRADES_CSV = Path("data/live/trades.csv")
UTC_OFFSET_VERANO = 2  # Madrid CEST


def cargar_trades_por_dia():
    """Devuelve lista de (dia_madrid, [pnl_neto_eur, ...]) en orden cronológico."""
    rows = []
    with open(TRADES_CSV, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["status"] != "CLOSED":
                continue
            try:
                ts = datetime.fromisoformat(r["close_timestamp"].replace("Z", "+00:00"))
                pnl = float(r["pnl_neto_eur"])
            except (ValueError, TypeError):
                continue
            ts_madrid = ts + timedelta(hours=UTC_OFFSET_VERANO)
            rows.append((ts_madrid.date(), pnl))
    rows.sort(key=lambda x: x[0])

    por_dia = defaultdict(list)
    for dia, pnl in rows:
        por_dia[dia].append(pnl)
    dias_ordenados = sorted(por_dia.keys())
    return [(d, por_dia[d]) for d in dias_ordenados]


def simular_desde(dias_pnl, start_idx, bkr_inicial, racha_max, freno_diario_pct,
                   suelo, objetivo, max_dias=60):
    """
    Reproduce dias_pnl[start_idx:] como si empezara hoy desde bkr_inicial.
    Devuelve: ('bust'|'recuperado'|'inconcluso', n_dias_transcurridos, bkr_final)
    """
    bkr = bkr_inicial
    dias_usados = 0

    for dia, pnls_del_dia in dias_pnl[start_idx:start_idx + max_dias]:
        dias_usados += 1
        bkr_ini_dia = bkr
        racha = 0
        freno_dia_activo = False

        for pnl in pnls_del_dia:
            if freno_dia_activo:
                break  # el freno diario/racha ya paró el resto del día
            bkr += pnl
            if bkr <= suelo:
                return "bust", dias_usados, bkr
            if bkr >= objetivo:
                return "recuperado", dias_usados, bkr
            # actualizar racha
            if pnl < 0:
                racha += 1
            else:
                racha = 0
            # chequear breakers para el RESTO del día
            caida_dia = (bkr_ini_dia - bkr) / bkr_ini_dia if bkr_ini_dia > 0 else 0
            if racha >= racha_max or caida_dia >= freno_diario_pct:
                freno_dia_activo = True

    return "inconcluso", dias_usados, bkr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--racha", type=int, default=4)
    ap.add_argument("--freno-diario", type=float, default=0.30)
    ap.add_argument("--suelo", type=float, default=1.00)
    ap.add_argument("--objetivo", type=float, default=8.50)
    ap.add_argument("--bkr-inicial", type=float, default=7.10)
    args = ap.parse_args()

    dias_pnl = cargar_trades_por_dia()
    n_dias_total = len(dias_pnl)
    print(f"Días con trades reales en el histórico: {n_dias_total} "
          f"({dias_pnl[0][0]} a {dias_pnl[-1][0]})")
    print(f"Parámetros: racha_max={args.racha} freno_diario={args.freno_diario:.0%} "
          f"suelo={args.suelo}€ objetivo={args.objetivo}€ bkr_inicial={args.bkr_inicial}€\n")

    resultados = []
    for start_idx in range(n_dias_total - 2):  # necesita al menos algo de recorrido
        resultado, n_dias, bkr_final = simular_desde(
            dias_pnl, start_idx, args.bkr_inicial, args.racha,
            args.freno_diario, args.suelo, args.objetivo)
        resultados.append((resultado, n_dias, bkr_final))

    n = len(resultados)
    bust = [r for r in resultados if r[0] == "bust"]
    recuperado = [r for r in resultados if r[0] == "recuperado"]
    inconcluso = [r for r in resultados if r[0] == "inconcluso"]

    print(f"Caminos simulados (1 por cada punto de partida posible en el histórico): n={n}")
    print(f"  BUST (revienta, toca suelo {args.suelo}€):      {len(bust):>3} ({len(bust)/n*100:5.1f}%)")
    print(f"  RECUPERADO (llega a {args.objetivo}€):           {len(recuperado):>3} ({len(recuperado)/n*100:5.1f}%)")
    print(f"  INCONCLUSO (se acaba el histórico antes):  {len(inconcluso):>3} ({len(inconcluso)/n*100:5.1f}%)")

    if bust:
        dias_bust = sorted(r[1] for r in bust)
        print(f"\n  Días hasta reventar (mediana): {dias_bust[len(dias_bust)//2]}"
              f" (min={dias_bust[0]}, max={dias_bust[-1]})")
    if recuperado:
        dias_rec = sorted(r[1] for r in recuperado)
        print(f"  Días hasta recuperar (mediana): {dias_rec[len(dias_rec)//2]}"
              f" (min={dias_rec[0]}, max={dias_rec[-1]})")


if __name__ == "__main__":
    main()
