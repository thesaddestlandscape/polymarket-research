#!/usr/bin/env python3
"""Vigía del gate de promoción de nested_arb (5min-en-15min): avisa por
Telegram (una vez) cuando cruce n>=30 cerradas-filtradas con garantía>=97%.

Origen (13-Jul, propuesta #3 lista de puntos ciegos): vigia_gates_pendientes.py
solo lee results.csv, nunca vigiló nested_arb_sim.csv. El hallazgo más
cercano a proponerse a live de la sesión de ayer (5min15m ya en garantía
100%, n=28, a 2 cerradas del gate) podía cruzar el umbral sin que nadie se
enterara -- mismo patrón que el BNB olvidado en ORDER_FLOW_PAIR_BLACKLIST.

Reusa la lógica de analisis_nested_arb_gate.py (segmentado por nesting,
NUNCA mezclar 5min15m con 15min60m -- tienen garantía muy distinta).
Read-only, no toca dinero ni config.
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import csv  # noqa: E402

SIM_CSV = REPO / "data/shadow/nested_arb_sim.csv"
LATCH = REPO / "data/live/vigia_nested_arb_gate_latch.json"
NESTING_OBJETIVO = "5min15m"
GATE_N = 30
GATE_GARANTIA_PCT = 97.0


def _es_bool(v) -> bool:
    return v in ("1", "True", "true")


def main() -> int:
    from shadow_digest import enviar_telegram

    if not SIM_CSV.exists():
        return 0
    rows = list(csv.DictReader(open(SIM_CSV, encoding="utf-8")))
    grupo = [r for r in rows if r.get("status") == "CLOSED"
             and _es_bool(r.get("pasa_filtro")) and r.get("nesting") == NESTING_OBJETIVO]
    n = len(grupo)
    ok = sum(1 for r in grupo if _es_bool(r.get("garantia_ok")))
    pct = ok / n * 100 if n else 0.0
    pnl = sum(float(r.get("pnl_usd") or 0) for r in grupo)

    print(f"[vigia_nested_arb_gate] {NESTING_OBJETIVO}: n={n}/{GATE_N} garantia={ok}/{n}={pct:.1f}%")

    try:
        latch = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        latch = {}

    if latch.get("avisado"):
        return 0

    if n >= GATE_N and pct >= GATE_GARANTIA_PCT:
        msg = (
            f"🔔 GATE nested_arb ({NESTING_OBJETIVO}) CRUZADO\n"
            f"n={n} garantía={ok}/{n}={pct:.1f}% pnl_total={pnl:+.2f}$\n"
            f"Cumple el criterio de promoción (n≥{GATE_N}, garantía≥{GATE_GARANTIA_PCT}%). "
            f"Decisión de proponer a live: Javi. Ver analisis_nested_arb_gate.py para detalle "
            f"y recordar NO mezclar con el nesting 15min60m (garantía distinta, mucho peor)."
        )
        ok_tg = enviar_telegram(msg)
        latch["avisado"] = True
        latch["n"] = n
        latch["garantia_pct"] = pct
        LATCH.write_text(json.dumps(latch, ensure_ascii=False, indent=1))
        print(f"[vigia_nested_arb_gate] aviso enviado (telegram={ok_tg})")

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_nested_arb_gate] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
