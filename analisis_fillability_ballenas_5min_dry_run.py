#!/usr/bin/env python3
"""Piloto puntual: fill-ability histórico para BALLENAS_TARDIAS#ETH#5min#BUY_YES
usando ballenas_5min_dry_run.csv (que ya trae condition_id, no necesita
market_id_resolver). Mismo método que analisis_fillability_historico_trades.py,
adaptado al esquema de este tracker en concreto."""
import csv
import json
import time
from pathlib import Path

from analisis_fillability_historico_trades import (
    _trades_de_mercado, _parse_ts, TOLERANCIA_PRECIO, STAKE_REFERENCIA_USD,
)

REPO = Path(__file__).resolve().parent
TRACKER = REPO / "data/shadow/ballenas_5min_dry_run.csv"


def cargar_senales_eth():
    vistos = {}
    with open(TRACKER, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("activo") != "ETH":
                continue
            mid = row.get("market_id")
            if mid not in vistos or row["timestamp_utc"] < vistos[mid]["timestamp_utc"]:
                vistos[mid] = row
    return list(vistos.values())


def main():
    senales = cargar_senales_eth()
    print(f"BALLENAS_TARDIAS#ETH#5min#BUY_YES: {len(senales)} señales únicas")
    resultados = []
    for i, row in enumerate(senales):
        mid = row["market_id"]
        cid = row.get("condition_id")
        ts_senal = _parse_ts(row["timestamp_utc"])
        ts_cierre = _parse_ts(row["end_date"])
        try:
            precio_obj = float(row["py"])
        except (KeyError, ValueError, TypeError):
            continue
        if not cid or ts_senal is None or ts_cierre is None:
            continue

        trades = _trades_de_mercado(cid)
        time.sleep(0.15)

        vol = 0.0
        n_rel = 0
        for t in trades:
            ts_t = t.get("timestamp")
            if ts_t is None or not (ts_senal <= float(ts_t) <= ts_cierre + 5):
                continue
            outcome = (t.get("outcome") or "").strip().lower()
            if outcome not in ("up", "yes"):
                continue
            try:
                precio_t = float(t.get("price", 0))
                size_t = float(t.get("size", 0))
            except (TypeError, ValueError):
                continue
            if precio_t <= precio_obj + TOLERANCIA_PRECIO:
                vol += precio_t * size_t
                n_rel += 1

        fillable = vol >= STAKE_REFERENCIA_USD
        resultados.append({"market_id": mid, "precio_objetivo": precio_obj,
                           "vol_usd_a_precio": round(vol, 2), "n_trades_relevantes": n_rel,
                           "fillable_proxy": fillable, "n_trades_totales_mercado": len(trades)})
        estado = "✅ fillable" if fillable else ("〜 sin vol suficiente" if trades else "🔴 sin trades")
        print(f"  [{i+1}/{len(senales)}] mid={mid} precio_obj={precio_obj:.3f} "
              f"vol=${vol:.2f} ({n_rel} trades) -- {estado}")

    n_fill = sum(1 for r in resultados if r["fillable_proxy"])
    n_tot = len(resultados)
    print()
    print(f"RESUMEN BALLENAS_TARDIAS#ETH#5min#BUY_YES: {n_fill}/{n_tot} fillable_proxy "
          f"({n_fill/n_tot*100:.1f}%)" if n_tot else "sin datos")
    out = REPO / "data/shadow/fillability_historico_BALLENAS_TARDIAS_ETH_5min_BUY_YES.json"
    out.write_text(json.dumps(resultados, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Guardado en {out}")


if __name__ == "__main__":
    main()
