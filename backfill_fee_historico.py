"""
backfill_fee_historico.py — recalcula fee_eur/pnl_neto_eur de los trades live
CLOSED que quedaron con fee_eur=0.0 antes del fix del 08-Jul (commit c8bd4d406).

Reutiliza EXACTAMENTE las mismas funciones ya revisadas (/code-review) de
shadow_resolve.py -- ninguna lógica nueva, mismo ground-truth (data-api/activity)
con el mismo clamp de seguridad y desambiguación por shares. Un solo uso,
idempotente (salta filas que ya tengan fee_confirmado=1 en notas).

Escritura atómica (tmp + os.replace). No toca filas OPEN ni ERROR.
"""
import csv
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from shadow_resolve import _fees_reales_recientes, _fee_real_para_trade  # noqa: E402

TRADES_PATH = Path("data/live/trades.csv")


def main() -> int:
    if not TRADES_PATH.exists():
        print("trades.csv no existe.")
        return 1

    trades = list(csv.DictReader(open(TRADES_PATH, encoding="utf-8")))
    candidatos = [t for t in trades if t.get("status") == "CLOSED"
                  and "fee_confirmado=1" not in (t.get("notas") or "")]
    print(f"trades CLOSED totales: {sum(1 for t in trades if t.get('status')=='CLOSED')}")
    print(f"candidatos a backfill (sin fee_confirmado=1): {len(candidatos)}")
    if not candidatos:
        print("nada que hacer.")
        return 0

    fees_recientes = _fees_reales_recientes(limit_paginas=6)  # histórico más largo que el uso normal
    print(f"eventos TRADE reales encontrados en data-api: {sum(len(v) for v in fees_recientes.values())}")

    actualizados = 0
    sin_confirmar = 0
    delta_total = 0.0
    for t in trades:
        if t.get("status") != "CLOSED" or "fee_confirmado=1" in (t.get("notas") or ""):
            continue
        fee_real = _fee_real_para_trade(t, fees_recientes)
        pnl_bruto = float(t.get("pnl_bruto_eur") or 0)
        if fee_real is not None:
            pnl_neto_antes = float(t.get("pnl_neto_eur") or 0)
            pnl_neto_nuevo = round(pnl_bruto - fee_real, 4)
            delta_total += pnl_neto_nuevo - pnl_neto_antes
            t["fee_eur"] = f"{fee_real:.4f}"
            t["pnl_neto_eur"] = f"{pnl_neto_nuevo:.4f}"
            t["notas"] = f"{t.get('notas','')} fee_confirmado=1 backfill_08jul".strip()
            actualizados += 1
        else:
            t["notas"] = f"{t.get('notas','')} fee_confirmado=0 backfill_08jul".strip()
            sin_confirmar += 1

    print(f"\nactualizados con fee real: {actualizados}")
    print(f"sin confirmar (fuera de ventana data-api): {sin_confirmar}")
    print(f"delta total en pnl_neto_eur histórico: {delta_total:+.2f}$ (antes sobreestimado en esta magnitud)")

    if actualizados == 0:
        print("nada que escribir.")
        return 0

    cols = list(trades[0].keys())
    tmp = TRADES_PATH.with_suffix(".csv.tmp_backfill")
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(trades)
    os.replace(tmp, TRADES_PATH)
    print(f"\nguardado: {TRADES_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
