#!/usr/bin/env python3
"""Diagnóstico reproducible de los 3 hilos abiertos 07-Jul (calibración + sizing).

Lee SIEMPRE los datos de PRODUCCIÓN (paths absolutos) para que, viva donde viva
este script (dev), analice el live real. Read-only: no escribe nada.

Uso:  python3 calib_sizing_diag.py
Re-correr "en unos días" para decidir con N los 3 hilos:
  1) Banda sobreconfianza P(YES)∈[0.58,0.63)  -> penalización cuando n>=15 y gap>=0.08
  2) Edge-a-tamaño (Gate #1 des-pineo)         -> reabrir techo cuando n>=15 des-pineados
  3) Stake<->outcome (¿inversión real?)        -> mismo régimen, corr por época + por PnL

Nombres de columna reales (ojo, trampa): en trades.csv 'ic_modelo' almacena en
realidad P(YES) del modelo (valores ~0.5-0.7), NO la IC del bucket.
"""
import csv

TRADES = "/root/polymarket-research/data/live/trades.csv"
PIN = 1.05          # stake pineado actual (min=max)
FORWARD_DESDE = "2026-07-05"  # post-fixes + BUY_NO retirado


def f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def corr(xs, ys):
    n = len(xs)
    if n < 3:
        return None
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = sum((x - mx) ** 2 for x in xs) ** 0.5
    dy = sum((y - my) ** 2 for y in ys) ** 0.5
    return num / (dx * dy) if dx * dy else None


def load():
    rows = list(csv.DictReader(open(TRADES)))
    return [r for r in rows if r["status"] == "CLOSED" and f(r["pnl_neto_eur"]) is not None]


def win(r):
    return f(r["pnl_neto_eur"]) > 0


def hilo1_calibracion(closed):
    print("=" * 64)
    print("HILO 1 — Calibración P(YES) BUY_YES (banda sobreconfianza)")
    print("=" * 64)
    by = [r for r in closed if r["direction"] == "BUY_YES"]
    bins = [(0.50, 0.58), (0.58, 0.63), (0.63, 1.01)]
    for lo, hi in bins:
        g = [r for r in by if f(r["ic_modelo"]) is not None and lo <= f(r["ic_modelo"]) < hi]
        if not g:
            continue
        pred = sum(f(r["ic_modelo"]) for r in g) / len(g)
        real = sum(1 for r in g if win(r)) / len(g)
        gap = pred - real
        flag = "SOBRECONFIADO" if gap >= 0.08 else "ok"
        gate = "  <-- GATE (n>=15) LISTO" if (gap >= 0.08 and len(g) >= 15) else ""
        print(f"  P(YES)[{lo:.2f},{hi:.2f}): n={len(g):<3} pred={pred:.2f} real={real:.2f} gap={gap:+.2f}  {flag}{gate}")


def hilo2_edge_a_tamano(closed):
    print("=" * 64)
    print("HILO 2 — Edge-a-tamaño (Gate #1: reabrir techo con n>=15 des-pineados)")
    print("=" * 64)
    despin = [r for r in closed if (f(r["stake_eur"]) or 0) > PIN + 0.01 and r["timestamp_utc"][:10] >= FORWARD_DESDE]
    n = len(despin)
    if n:
        hit = sum(1 for r in despin if win(r)) / n
        pnl = sum(f(r["pnl_neto_eur"]) for r in despin)
        print(f"  trades des-pineados forward (stake>{PIN}): n={n}/15  hit={hit:.0%}  pnl={pnl:+.2f}€")
    else:
        print(f"  trades des-pineados forward: n=0/15 (stake pineado a {PIN})")
    print(f"  -> {'GATE LISTO para revisar' if n >= 15 else 'sigue cogiendo N'}")


def hilo3_stake_outcome(closed):
    print("=" * 64)
    print("HILO 3 — Stake<->outcome (¿inversión real o confound/ruido?)")
    print("=" * 64)
    by = [r for r in closed if r["direction"] == "BUY_YES"]
    for lab, cond in [("TODO", lambda d: True),
                      ("PRE-FIX <=03-Jul", lambda d: d <= "2026-07-03"),
                      ("FORWARD >=05-Jul", lambda d: d >= FORWARD_DESDE)]:
        g = [r for r in by if cond(r["timestamp_utc"][:10])]
        if len(g) < 3:
            print(f"  {lab:<18} n={len(g)} (insuf.)")
            continue
        stk = [f(r["stake_eur"]) for r in g]
        w = [1.0 if win(r) else 0.0 for r in g]
        c = corr(stk, w)
        print(f"  {lab:<18} n={len(g):<3} corr(stake,acierto)={c:+.3f}  hit={sum(w)/len(g):.0%}")
    # por PnL (no por hit) forward: edge alto vs bajo
    fw = [r for r in by if r["timestamp_utc"][:10] >= FORWARD_DESDE and f(r["edge_neto"]) is not None]
    if len(fw) >= 6:
        med = sorted(f(r["edge_neto"]) for r in fw)[len(fw) // 2]
        for lab, cond in [(f"edge<={med:.3f}", lambda e: e <= med), (f"edge>{med:.3f}", lambda e: e > med)]:
            g = [r for r in fw if cond(f(r["edge_neto"]))]
            if g:
                hit = sum(1 for r in g if win(r)) / len(g)
                pnl = sum(f(r["pnl_neto_eur"]) for r in g)
                print(f"    forward {lab}: n={len(g)} hit={hit:.0%} pnl={pnl:+.2f}€")
    print("  NOTA: corr binaria con n<15 = ruido; decidir por PnL y con régimen estable.")


def main():
    closed = load()
    print(f"\ntrades.csv CLOSED con pnl: {len(closed)}\n")
    hilo1_calibracion(closed)
    print()
    hilo2_edge_a_tamano(closed)
    print()
    hilo3_stake_outcome(closed)
    print()


if __name__ == "__main__":
    main()
