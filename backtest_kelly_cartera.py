#!/usr/bin/env python3
"""
backtest_kelly_cartera.py — PROPUESTA #3 (dev, shadow-first, NO toca live).

Cuantifica el beneficio de un Kelly consciente de correlación: cuando 2+
posiciones GBM_LATE_15M abren en la misma ventana de 15min y misma dirección,
sus outcomes correlacionan ρ≈0.62 (medido 10-Jul). El Kelly independiente por
señal sobre-apuesta la 2ª → cuando pierden juntas, drawdown doble.

Regla simulada: 1ª posición de la ventana = stake pleno; cada posición
concurrente adicional MISMA dir = stake × haircut. Compara PnL total, varianza
por ventana y max drawdown acumulado bajo varios haircuts vs flat.

Lee datos de PRODUCCIÓN (rutas absolutas). Solo lectura, no escribe nada.
"""
import csv
from datetime import datetime
from collections import defaultdict
import statistics

RES = "/root/polymarket-research/data/shadow/results.csv"


def pdt(s):
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


def win15(dt):
    dt = dt.replace(second=0, microsecond=0)
    return dt.replace(minute=(dt.minute // 15) * 15)


def cargar():
    rows = []
    for r in csv.DictReader(open(RES)):
        if r.get("strategy") != "GBM_LATE_15M":
            continue
        py = r.get("precio_yes_mercado"); dec = r.get("decision", "")
        oc = r.get("outcome_real", ""); ed = pdt(r.get("end_date", ""))
        rt = pdt(r.get("resolution_timestamp", "") or r.get("prediction_timestamp", ""))
        pt = pdt(r.get("prediction_timestamp", ""))
        try:
            py = float(py)
        except (TypeError, ValueError):
            continue
        if oc not in ("YES", "NO") or not ed or not pt or not (0.01 < py < 0.99):
            continue
        p_lado = py if dec == "BUY_YES" else 1 - py
        gana = (oc == "YES" and dec == "BUY_YES") or (oc == "NO" and dec == "BUY_NO")
        rows.append(dict(win=win15(ed), dir=dec, pt=pt, rt=rt or ed,
                         p_lado=p_lado, gana=gana))
    return rows


def pnl(p_lado, gana, stake):
    return stake * (1.0 / p_lado - 1.0) if gana else -stake


def simular(rows, haircut):
    """Asigna stake por orden de aparición dentro de (ventana,dir); 1ª=1.0,
    siguientes = haircut. Devuelve lista (rt, pnl) ordenada por resolución."""
    orden = defaultdict(int)  # (win,dir) -> nº ya abiertas
    out = []
    for r in sorted(rows, key=lambda x: x["pt"]):
        k = (r["win"], r["dir"])
        stake = 1.0 if orden[k] == 0 else haircut
        orden[k] += 1
        out.append((r["rt"], pnl(r["p_lado"], r["gana"], stake), stake))
    return out


def metricas(sim):
    sim = sorted(sim, key=lambda x: x[0])
    pnls = [p for _, p, _ in sim]
    stakes = [s for _, _, s in sim]
    total = sum(pnls)
    capital = sum(stakes)                       # capital total desplegado
    roi = total / capital if capital else 0     # retorno por € arriesgado
    # max drawdown de la curva acumulada
    cum = 0.0; peak = 0.0; mdd = 0.0
    for p in pnls:
        cum += p; peak = max(peak, cum); mdd = min(mdd, cum - peak)
    # peor pérdida de una sola ventana (suma de posiciones de la misma ventana)
    return total, capital, roi, mdd, statistics.pstdev(pnls)


def main():
    rows = cargar()
    print(f"GBM_LATE_15M resueltas: n={len(rows)}")
    # cuántas son concurrentes (afectadas por el haircut)
    orden = defaultdict(int)
    conc = 0
    for r in sorted(rows, key=lambda x: x["pt"]):
        k = (r["win"], r["dir"])
        if orden[k] >= 1:
            conc += 1
        orden[k] += 1
    print(f"posiciones concurrentes (haircut aplicable): {conc} ({conc/len(rows):.0%})\n")
    print(f"{'haircut':>8}{'PnL_tot':>10}{'capital':>10}{'ROI/€':>9}{'maxDD':>10}{'std/pos':>9}")
    for h in [1.0, 0.62, 0.50, 0.38, 0.0]:
        total, cap, roi, mdd, sd = metricas(simular(rows, h))
        tag = " (flat)" if h == 1.0 else (" (skip 2ª=freno conteo)" if h == 0.0 else "")
        print(f"{h:>8.2f}{total:>+10.2f}{cap:>10.1f}{roi:>+9.4f}{mdd:>+10.2f}{sd:>9.4f}{tag}")
    print("\nLectura: ROI/€ = retorno por € arriesgado (eficiencia del capital);"
          "\nmaxDD menos negativo = menos drawdown; el haircut cambia el trade-off"
          " EV<->drawdown. Kelly-óptimo con ρ≈0.62 ≈ haircut 0.62 (1/(1+ρ)).")


if __name__ == "__main__":
    main()
