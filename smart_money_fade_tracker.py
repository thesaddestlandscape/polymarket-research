#!/usr/bin/env python3
"""Tracker del FADE de smart money (07-Jul) — read-only, datos de producción.

Mide lo que el motor de hipotesis_custom.json NO puede: cruza NUESTRA decisión
(BUY_YES/BUY_NO) contra el SIGNO del smart_money_consensus, y separa:
  - ALINEADO : decidimos igual que el consenso smart (BUY_YES & consenso>0, o BUY_NO & <0)
  - CONTRARIO: decidimos al revés del consenso (= el FADE)
Hipótesis (débil, n=45 en el escaneo 07-Jul): CONTRARIO rinde mejor que ALINEADO
→ el consenso 'smart' via /positions estaba invertido y fadearlo tiene edge.

Gate: n≥60 por lado y (hit_contrario − hit_alineado) ≥ 0.05.

⚠️ Excluye resoluciones anteriores a 2026-07-02T06:12Z: antes de esa fecha el
smart_money_consensus venía de la clasificación ROTA (endpoint /positions solo
retenía el residuo perdedor; 'wowitsamazing' figuraba -$478k siendo +$10k/mes).
Ver hipotesis_custom.json::H-CUSTOM-SMART-MONEY-CONSENSUS y memoria
project_state_2026-07-02.

Uso:  python3 smart_money_fade_tracker.py
"""
import csv
import json

RESULTS = "/root/polymarket-research/data/shadow/results.csv"
CORTE_CLASIF_ROTA = "2026-07-02T06:12"  # antes de esto el consenso está invertido/roto
GATE_N = 60
GATE_GAP = 0.05


def f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def main():
    rows = list(csv.DictReader(open(RESULTS)))
    usable = []
    for r in rows:
        if r["acierto"] not in ("1", "0"):
            continue
        if r["resolution_timestamp"][:16] < CORTE_CLASIF_ROTA:
            continue  # descartar tramo de clasificación rota
        try:
            fe = json.loads(r.get("features", "{}") or "{}")
        except (ValueError, TypeError):
            continue
        cons = fe.get("smart_money_consensus")
        nw = fe.get("smart_money_n_wallets") or 0
        cons = f(cons)
        if cons is None or nw < 1 or cons == 0:
            continue  # sin lean smart o sin wallets → no aplica
        dec = r["decision"]
        if dec not in ("BUY_YES", "BUY_NO"):
            continue
        # ¿nuestra decisión va con el signo del consenso o en contra?
        cons_yes = cons > 0  # consenso se inclina a Up/YES
        dec_yes = dec == "BUY_YES"
        grupo = "ALINEADO" if (cons_yes == dec_yes) else "CONTRARIO(fade)"
        usable.append((grupo, r["acierto"] == "1", f(r["pnl_neto"]) or 0.0, nw))

    print(f"Tracker FADE smart money — resoluciones válidas (post-{CORTE_CLASIF_ROTA}, "
          f"consenso≠0, n_wallets≥1): {len(usable)}\n")
    if not usable:
        print("  (aún 0 — el consenso limpio se empezó a capturar el 02-Jul; sigue cogiendo N)")
        return

    for g in ("ALINEADO", "CONTRARIO(fade)"):
        sub = [x for x in usable if x[0] == g]
        n = len(sub)
        if n == 0:
            print(f"  {g:<18} n=0")
            continue
        hit = sum(1 for x in sub if x[1]) / n
        pnl = sum(x[2] for x in sub)
        print(f"  {g:<18} n={n:<4} hit={hit:.0%} pnl={pnl:+.2f}€ pnl/op={pnl/n:+.3f}")

    a = [x for x in usable if x[0] == "ALINEADO"]
    c = [x for x in usable if x[0] == "CONTRARIO(fade)"]
    if a and c:
        gap = (sum(x[1] for x in c) / len(c)) - (sum(x[1] for x in a) / len(a))
        listo = len(a) >= GATE_N and len(c) >= GATE_N and gap >= GATE_GAP
        print(f"\n  gap hit (contrario−alineado) = {gap:+.3f}  (gate: ≥{GATE_GAP} y n≥{GATE_N}/lado)")
        print(f"  → {'GATE LISTO: el fade tiene edge, proponer a Javi' if listo else 'sigue cogiendo N'}")


if __name__ == "__main__":
    main()
