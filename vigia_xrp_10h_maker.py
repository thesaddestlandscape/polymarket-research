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
# 28-Jul (decisión Javi): el aviso original a n=25 (17-Jul, z=2.11) se
# diluyó con más n (hoy n=35, z=1.45 -- regresión a la media, firma clásica
# de hallazgo al límite). En vez de cerrar la puerta del todo, se decidió
# dejarlo madurar más y re-evaluar a un umbral más alto antes de decidir en
# firme -- GATE_N_DECISION es el segundo corte, con su propio latch
# independiente para poder avisar dos veces (una por gate).
GATE_N_DECISION = 70


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


def _stats(filas: list) -> dict:
    n = len(filas)
    pnls = [float(r["pnl1_maker"]) for r in filas]
    aciertos = sum(1 for r in filas if r.get("acierto") == "1")
    ev = sum(pnls) / n
    sd = st.stdev(pnls) if n > 1 else 0.0
    se = sd / (n ** 0.5) if n > 1 else 0.0
    z = ev / se if se > 0 else 0.0
    return {"n": n, "hit": aciertos / n, "ev": ev, "z": z,
            "fill": sum(1 for r in filas if r.get("filled") == "1") / n}


def main() -> int:
    from shadow_digest import enviar_telegram

    filas = _bucket_10h_xrp()
    n = len(filas)
    print(f"[vigia_xrp_10h_maker] n={n}/{GATE_N} (gate decisión: {GATE_N_DECISION})")

    try:
        latch = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        latch = {}

    if n >= GATE_N and not latch.get("gate1_avisado"):
        s = _stats(filas)
        msg = (
            f"🔔 VIGÍA XRP 10h UTC cruzó n≥{GATE_N}\n"
            f"n={s['n']} hit={s['hit']:.1%} fill_maker={s['fill']:.1%} EV_maker={s['ev']:+.3f} z={s['z']:+.2f}\n"
            f"Franja 09:30-13:00 UTC nunca probada en vivo (hueco entre ventanas). "
            f"Indicio original (11-Jul, n=14): EV+0.32 z=1.83, específico de XRP "
            f"(SOL/ETH/BTC planos a la misma hora). Con n>={GATE_N} toca releer el "
            f"análisis completo (analisis_maker_xrp_tardio.py + desglose horario) "
            f"y decidir con Javi si vale la pena probar — sigue sin ser suficiente "
            f"para abrir ventana live sin más revisión. Solo informativo, no toca dinero."
        )
        ok = enviar_telegram(msg)
        latch["gate1_avisado"] = True
        latch["gate1"] = {"n": s["n"], "ev_maker": s["ev"], "z": s["z"], "hit": s["hit"], "telegram_ok": ok}
        LATCH.write_text(json.dumps(latch, ensure_ascii=False, indent=1))
        print(f"[vigia_xrp_10h_maker] gate1 aviso enviado (telegram={ok})")

    # 28-Jul: gate2 -- decisión Javi de dejarlo madurar en vez de cerrarlo
    # tras ver z bajar de 2.11 (n=26) a 1.45 (n=35). Avisa UNA vez más al
    # llegar a GATE_N_DECISION, con el resultado explícito de si sobrevivió
    # o se diluyó -- para que la decisión de probarlo en real (o cerrarlo
    # definitivamente) se tome con el n que el propio Javi pidió esperar,
    # no otra vez con un n límite.
    if n >= GATE_N_DECISION and not latch.get("gate2_avisado"):
        s = _stats(filas)
        veredicto = ("sobrevive (z≥1.65)" if s["z"] >= 1.65
                      else "se diluyó -- ya no se distingue de ruido (z<1.65)")
        msg = (
            f"🔔 VIGÍA XRP 10h UTC cruzó el gate de DECISIÓN n≥{GATE_N_DECISION}\n"
            f"n={s['n']} hit={s['hit']:.1%} fill_maker={s['fill']:.1%} EV_maker={s['ev']:+.3f} z={s['z']:+.2f}\n"
            f"Veredicto: {veredicto}. Este es el momento de decidir en firme "
            f"(probar en real con stake mínimo, o cerrar formalmente) -- no dejarlo "
            f"acumulando indefinidamente otra vez. Solo informativo, no toca dinero."
        )
        ok = enviar_telegram(msg)
        latch["gate2_avisado"] = True
        latch["gate2"] = {"n": s["n"], "ev_maker": s["ev"], "z": s["z"], "hit": s["hit"], "telegram_ok": ok}
        LATCH.write_text(json.dumps(latch, ensure_ascii=False, indent=1))
        print(f"[vigia_xrp_10h_maker] gate2 (decisión) aviso enviado (telegram={ok})")

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_xrp_10h_maker] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
