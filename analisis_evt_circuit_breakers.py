#!/usr/bin/env python3
"""Propuesta #10 backlog quant-desk (13-jul): ¿los circuit breakers de %
fijo (freno_diario_pct=0.30, freno_ventana_pct=0.20) están bien calibrados,
o los datos reales sugieren algo distinto vía VaR/ES de cola (EVT)?

SOLO ANÁLISIS — el propio backlog marca esta propuesta como "toca dinero,
tratar como análisis primero, no como cambio automático". No escribe en
config_live.json ni toca live_stake.py.

Metodología: reconstruye el bankroll MODELO exacto que usa el circuit
breaker real (bankroll_actual() = CAPITAL_OPERATIVO_INICIAL + cumsum de
pnl_neto_eur de trades CLOSED, misma fórmula que live_stake.py) a partir de
trades.csv, agrupa por día calendario Madrid (UTC+2 fijo, igual que
_ahora_madrid) y calcula la caída diaria realizada como % del bankroll al
inicio de ese día — exactamente la métrica que compara freno_diario_pct.

Uso: python3 analisis_evt_circuit_breakers.py
"""
import csv
from collections import defaultdict
from datetime import datetime, timezone, timedelta

TRADES_CSV = "data/live/trades.csv"
CAPITAL_OPERATIVO_INICIAL = 25.44  # misma constante que live_stake.py
UTC_OFFSET_VERANO = 2


def _madrid(ts_str: str) -> datetime:
    ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
    if ts.tzinfo is None:
        ts = ts.replace(tzinfo=timezone.utc)
    return ts + timedelta(hours=UTC_OFFSET_VERANO)


def main():
    rows = [r for r in csv.DictReader(open(TRADES_CSV)) if r["status"] == "CLOSED"]
    # Orden cronológico por cierre real (close_timestamp), fallback a timestamp_utc
    for r in rows:
        r["_ts_cierre"] = r["close_timestamp"] or r["timestamp_utc"]
    rows.sort(key=lambda r: r["_ts_cierre"])

    print(f"Trades CLOSED: {len(rows)} | rango: {rows[0]['_ts_cierre']} → {rows[-1]['_ts_cierre']}")

    # Reconstrucción exacta del bankroll modelo (misma fórmula que bankroll_actual())
    bkr = CAPITAL_OPERATIVO_INICIAL
    por_dia = defaultdict(list)  # fecha_madrid -> [(bkr_antes, pnl), ...]
    for r in rows:
        pnl = float(r["pnl_neto_eur"] or 0)
        fecha_madrid = _madrid(r["_ts_cierre"]).date().isoformat()
        por_dia[fecha_madrid].append((bkr, pnl))
        bkr += pnl

    print(f"Bankroll modelo final reconstruido: {bkr:.2f}€ "
          f"(cross-check: coincide con bankroll_actual() si trades.csv no cambió)")
    print()

    dias = []
    for fecha, trades_dia in sorted(por_dia.items()):
        bkr_inicio = trades_dia[0][0]
        pnl_dia = sum(p for _, p in trades_dia)
        n_dia = len(trades_dia)
        caida_pct = -pnl_dia / bkr_inicio if bkr_inicio > 0 else None
        dias.append({"fecha": fecha, "bkr_inicio": bkr_inicio, "pnl": pnl_dia,
                      "n": n_dia, "caida_pct": caida_pct})

    print(f"{'fecha':12s} {'bkr_inicio':>10s} {'pnl_día':>9s} {'n':>3s} {'caída_%':>8s}")
    for d in dias:
        marca = " 🛑" if d["caida_pct"] and d["caida_pct"] >= 0.30 else ""
        print(f"{d['fecha']:12s} {d['bkr_inicio']:10.2f} {d['pnl']:+9.2f} {d['n']:3d} "
              f"{d['caida_pct']*100:7.1f}%{marca}" if d["caida_pct"] is not None else
              f"{d['fecha']:12s} {d['bkr_inicio']:10.2f} {d['pnl']:+9.2f} {d['n']:3d} {'n/a':>8s}")

    caidas = sorted([d["caida_pct"] for d in dias if d["caida_pct"] and d["caida_pct"] > 0], reverse=True)
    n_dias = len(dias)
    n_caidas = len(caidas)
    print()
    print(f"Días con actividad: {n_dias} | días con caída neta: {n_caidas}")
    if caidas:
        print(f"Peor caída diaria observada: {caidas[0]*100:.1f}%")
        print(f"Caídas (desc): {[f'{c*100:.1f}%' for c in caidas]}")
    print()
    print("=" * 70)
    print(f"VEREDICTO n: con {n_caidas} caídas diarias observadas (trades.csv completo, "
          f"01-Jul→hoy, incluye el periodo congelado 03-05-Jul), muy por debajo de n≥15 "
          f"del proyecto para concluir NADA — un ajuste EVT/GPD (Generalized Pareto sobre "
          f"excedencias) necesita típicamente n≥50-100 excedencias para ser estable. "
          f"No se reporta un VaR/ES paramétrico: sería sobre-ajuste con {n_caidas} puntos.")
    print("Lo único defendible con este n: la caída diaria máxima observada como referencia "
          "cruda, comparada contra el freno_diario_pct=0.30 actual.")


if __name__ == "__main__":
    main()
