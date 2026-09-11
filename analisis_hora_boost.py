#!/usr/bin/env python3
"""Read-only: mapea la coordinación de las reglas horarias de GBM sobre datos shadow (P15).

Las tres reglas de "hora del día" para BUY_YES#15min GBM viven en sitios distintos y
pueden pisarse/contradecirse:
  (a) set hardcoded 24H {5,6,7,15,16,17,18,19} → boost ×1.1  (shadow_predict.py:2695)
  (b) meta.gbm_blacklist_hours_auto  → skip                  (strategy_params.json, dinámico)
  (c) meta.hora_boost_factor         → boost ×factor         (strategy_params.json, dinámico)

Este script reconstruye, sobre results.csv (dato ya logueado, features.hora_utc), el
hit-rate / pnl / edge realizado por hora, cruza contra las 3 reglas ACTUALES y señala
incoherencias (hora boosteada Y blacklisteada, hora buena blacklisteada, hora top sin boost).
NO toca producción. Correr desde la raíz del repo:  python3 analisis_hora_boost.py

Contexto: el doble-conteo del stake (a×c sobre la misma hora) es LATENTE mientras
hora_boost_factor esté ausente, e impacto live=0 mientras max_stake esté pinned al suelo.
El valor real del mapa es reconciliar las 3 reglas antes de despinnar max_stake.
"""
import csv, json, os
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "data", "shadow", "results.csv")
PARAMS = os.path.join(BASE, "data", "shadow", "strategy_params.json")
HARD_24H = {5, 6, 7, 15, 16, 17, 18, 19}   # shadow_predict.py:2695 (constante en código)


def cargar_reglas_meta():
    """Lee blacklist_auto y hora_boost_factor ACTUALES (dinámicas)."""
    try:
        meta = json.load(open(PARAMS)).get("meta", {})
    except Exception:
        meta = {}
    bl = set(int(h) for h in meta.get("gbm_blacklist_hours_auto", []) or [])
    hb = {int(k): float(v) for k, v in (meta.get("hora_boost_factor", {}) or {}).items()}
    return bl, hb


def signed_edge(row):
    try:
        e = abs(float(row["edge_neto"]))
        return e if row["acierto"] == "1" else -e
    except Exception:
        return None


def stats(rows):
    n = len(rows)
    if n == 0:
        return (0, 0.0, 0.0, 0.0)
    hits = sum(1 for r in rows if r["acierto"] == "1")
    pnl = sum(float(r["pnl_neto"]) for r in rows if r["pnl_neto"] not in ("", None))
    ses = [x for x in (signed_edge(r) for r in rows) if x is not None]
    return (n, hits / n, pnl, (sum(ses) / len(ses) if ses else 0.0))


def main():
    blacklist_auto, hora_boost = cargar_reglas_meta()
    per_hour = defaultdict(list)
    with open(RES) as f:
        for row in csv.DictReader(f):
            if row["decision"] != "BUY_YES" or "15min" not in row["subtype"]:
                continue
            if not row["strategy"].startswith(("UPDOWN_GBM", "GBM_LATE")):
                continue
            try:
                feat = json.loads(row["features"]) if row["features"] else {}
            except Exception:
                feat = {}
            h = feat.get("hora_utc")
            if h is None:
                continue
            per_hour[int(h)].append(row)

    total = sum(len(v) for v in per_hour.values())
    print(f"BUY_YES #15min GBM con hora_utc: n={total}")
    print(f"Reglas actuales: HARD_24H={sorted(HARD_24H)} | blacklist_auto={sorted(blacklist_auto)} "
          f"| hora_boost_factor={hora_boost or '(ausente)'}\n")
    print(f"{'hora':>4} {'n':>5} {'hit%':>6} {'pnl':>9} {'edge_real':>10}  flags")

    incoherencias = []
    boosted, plain = [], []
    for h in sorted(per_hour):
        n, hit, pnl, me = stats(per_hour[h])
        flags = []
        if h in HARD_24H:
            flags.append("BOOST×1.1")
            boosted += per_hour[h]
        else:
            plain += per_hour[h]
        if h in hora_boost:
            flags.append(f"META×{hora_boost[h]}")
        if h in blacklist_auto:
            flags.append("BLACKLIST_AUTO")
        # incoherencias
        if h in HARD_24H and h in blacklist_auto:
            flags.append("⚠️BOOST+BLACKLIST")
            incoherencias.append(f"h{h}: boosteada Y blacklisteada (edge {me:+.4f})")
        if h in HARD_24H and h in hora_boost:
            flags.append("⚠️DOBLE-BOOST")
            incoherencias.append(f"h{h}: doble-boost activo (×1.1 × {hora_boost[h]})")
        if h in blacklist_auto and me > 0.03 and n >= 15:
            incoherencias.append(f"h{h}: blacklisteada pero edge BUENO {me:+.4f} n={n}")
        if h not in HARD_24H and me > 0.05 and n >= 15:
            incoherencias.append(f"h{h}: edge TOP {me:+.4f} n={n} pero SIN boost")
        print(f"{h:>4} {n:>5} {hit*100:>5.1f}% {pnl:>9.2f} {me:>10.4f}  {' '.join(flags)}")

    print("\n=== AGREGADO boosted (set 24H) vs no-boosted ===")
    for label, rows in (("BOOSTED ", boosted), ("no-boost", plain)):
        n, hit, pnl, me = stats(rows)
        print(f"{label} n={n:>4}  hit={hit*100:>5.1f}%  pnl={pnl:>8.2f}  edge_real={me:>+.4f}")

    print("\n=== INCOHERENCIAS ===")
    if incoherencias:
        for x in incoherencias:
            print(f"  ⚠️ {x}")
    else:
        print("  (ninguna con las reglas actuales)")
    print("\nNota: el ×1.1 en agregado se justifica solo si BOOSTED>no-boost en edge_real. "
          "El doble-boost y el impacto live están gated (max_stake pinned). Ver P15 en CLAUDE.md.")


if __name__ == "__main__":
    main()
