#!/usr/bin/env python3
"""Vigía XRP 10h UTC maker: avisa por Telegram (una vez) cuando el bucket
GBM_LATE_15M/UPDOWN_GBM#XRP#BUY_YES a las 10h UTC cruza n>=25 en
maker_sim.csv.

Origen (11-Jul): tras confirmar que el enfoque maker NO rescata XRP en
general (analisis_maker_xrp_tardio.py, EV negativo en barrido completo de
precios), se desglosó por hora y apareció un indicio: 10h UTC muestra
EV_maker=+0.32 (n=14, z=1.83, sobrevive corrección por 24 tests) —
ESPECÍFICO de XRP (SOL/ETH/BTC planos o negativos a la misma hora, no es el
efecto genérico "h10 buena para GBM" ya conocido), y esa franja (09:30-13:00
UTC) NUNCA se ha probado en vivo — cae en el hueco entre ventanas. Con
n=14 (<15) es solo un indicio, no una conclusión — este vigía espera a
n>=25 antes de avisar, sin bloquear ni cambiar nada mientras tanto.

Read-only, no toca dinero ni config. Reusa exactamente el mismo cruce
maker_sim.csv x results.csv (por market_id+strategy+subtype+decision) que
el análisis original, para no divergir del hallazgo (misma lección que
vigia_pybajo: reusar el filtro exacto, no recalcular con criterio propio).
"""
import csv
import json
import statistics as st
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

RESULTS = REPO / "data/shadow/results.csv"
MAKER_SIM = REPO / "data/shadow/maker_sim.csv"
LATCH = REPO / "data/live/vigia_xrp_10h_maker_latch.json"
HORA_OBJETIVO = 10
GATE_N = 25


def _bucket_10h_xrp():
    if not RESULTS.exists() or not MAKER_SIM.exists():
        return []
    idx = {}
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            k = (row["market_id"], row["strategy"], row["subtype"], row["decision"])
            idx[k] = row.get("prediction_timestamp", "")

    filas = []
    with open(MAKER_SIM, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if not row.get("subtype", "").startswith("XRP"):
                continue
            if row.get("decision") != "BUY_YES":
                continue
            k = (row["market_id"], row["strategy"], row["subtype"], row["decision"])
            ts = idx.get(k)
            if not ts:
                continue
            try:
                dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
            except Exception:
                continue
            if dt.hour != HORA_OBJETIVO:
                continue
            filas.append(row)
    return filas


def main() -> int:
    from shadow_digest import enviar_telegram

    filas = _bucket_10h_xrp()
    n = len(filas)
    print(f"[vigia_xrp_10h_maker] n={n}/{GATE_N}")

    if n < GATE_N:
        return 0  # aún acumulando, nada que avisar

    if LATCH.exists():
        try:
            if json.loads(LATCH.read_text()).get("avisado"):
                return 0
        except Exception:
            pass

    pnls = [float(r["pnl1_maker"]) for r in filas]
    aciertos = sum(1 for r in filas if r.get("acierto") == "1")
    ev = sum(pnls) / n
    sd = st.stdev(pnls) if n > 1 else 0.0
    se = sd / (n ** 0.5) if n > 1 else 0.0
    z = ev / se if se > 0 else 0.0
    hit = aciertos / n
    fill = sum(1 for r in filas if r.get("filled") == "1") / n

    msg = (
        f"🔔 VIGÍA XRP 10h UTC cruzó n≥{GATE_N}\n"
        f"n={n} hit={hit:.1%} fill_maker={fill:.1%} EV_maker={ev:+.3f} z={z:+.2f}\n"
        f"Franja 09:30-13:00 UTC nunca probada en vivo (hueco entre ventanas). "
        f"Indicio original (11-Jul, n=14): EV+0.32 z=1.83, específico de XRP "
        f"(SOL/ETH/BTC planos a la misma hora). Con n>={GATE_N} toca releer el "
        f"análisis completo (analisis_maker_xrp_tardio.py + desglose horario) "
        f"y decidir con Javi si vale la pena probar — sigue sin ser suficiente "
        f"para abrir ventana live sin más revisión. Solo informativo, no toca dinero."
    )
    ok = enviar_telegram(msg)
    LATCH.write_text(json.dumps({
        "avisado": True, "n": n, "ev_maker": ev, "z": z, "hit": hit,
        "telegram_ok": ok,
    }, ensure_ascii=False, indent=1))
    print(f"[vigia_xrp_10h_maker] aviso enviado (telegram={ok}), latch escrito")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_xrp_10h_maker] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
