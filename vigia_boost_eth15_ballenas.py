#!/usr/bin/env python3
"""Vigía: FAVORITO_CONFIRMADO#ETH#15min#BUY_YES dentro de la banda de
ballenas -- avisa por Telegram (una vez, latch) en cuanto la ventana
MÓVIL de los últimos VENTANA_DIAS días pase el gate riguroso completo
(Wilson+shuffle+bootstrap PnL, veredicto=GATE OK), no solo el histórico
agregado.

Origen (21-Jul): antes de activar boost_ic_ballenas_favorito_eth15 (hoy
1.0=inactivo) + max_stake_eur_ballenas_eth15_dentro_banda (ya desplegado,
inerte, ver project_techo_stake_condicional_eth15min_ballenas_21jul),
Javi pidió ver los últimos 5 días -- el histórico completo pasa gate
(n=184, PnL/trade=+0.128€, CI limpio) pero la ventana de 5 días SOLA no
(n=80, PnL/trade=+0.117€, CI90%=[-0.056,+0.285] cruza cero), arrastrada
por un día malo (21-Jul, -0.380€/trade). Decisión: dejar en observación,
avisar cuando la ventana reciente se limpie sola, no reevaluar a mano cada
sesión.

Solo lectura sobre results.csv + ballenas_timing_state.json. No toca
dinero ni config, no activa nada -- decisión de subir el boost sigue
siendo 100% de Javi.
"""
import csv
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_gate_riguroso import gate

RESULTS = REPO / "data/shadow/results.csv"
BALLENAS_STATE = REPO / "data/shadow/ballenas_timing_state.json"
LATCH = REPO / "data/live/vigia_boost_eth15_ballenas_latch.json"

STRATEGY, SUBTYPE, DECISION = "FAVORITO_CONFIRMADO", "ETH#15min", "BUY_YES"
VENTANA_DIAS = 5
N_MIN = 40  # mismo umbral de rigor que el resto del proyecto


def _cargar_latch():
    try:
        return json.loads(LATCH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _banda():
    try:
        d = json.loads(BALLENAS_STATE.read_text(encoding="utf-8")).get("ETH#15m", {})
        return d.get("banda_lo"), d.get("banda_hi")
    except Exception:
        return None, None


def _filas_ventana(lo, hi):
    corte = (datetime.now(timezone.utc) - timedelta(days=VENTANA_DIAS)).isoformat()
    filas = []
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r["strategy"], r["subtype"], r["decision"]) != (STRATEGY, SUBTYPE, DECISION):
                continue
            if r.get("acierto") not in ("0", "1"):
                continue
            if (r.get("resolution_timestamp") or "") < corte:
                continue
            try:
                p = float(r["precio_yes_mercado"])
            except (TypeError, ValueError):
                continue
            if lo <= p < hi:
                filas.append(r)
    return filas


def main() -> int:
    latch = _cargar_latch()
    if latch.get("avisado"):
        print(f"[vigia_boost_eth15_ballenas] ya avisado el {latch.get('avisado_en')} -- nada que hacer")
        return 0

    lo, hi = _banda()
    if lo is None or hi is None:
        print("[vigia_boost_eth15_ballenas] banda ETH#15m no calibrada/significativa -- sin evaluar")
        return 0

    filas = _filas_ventana(lo, hi)
    n = len(filas)
    if n < N_MIN:
        print(f"[vigia_boost_eth15_ballenas] n={n}/{N_MIN} en ventana {VENTANA_DIAS}d -- insuficiente todavía")
        return 0

    v = gate(filas)
    print(f"[vigia_boost_eth15_ballenas] ventana {VENTANA_DIAS}d: n={n} hit={v['hit']*100:.1f}% "
          f"pnl_media={v['pnl_media']:+.3f} CI90%=[{v['pnl_lo']:+.3f},{v['pnl_hi']:+.3f}] "
          f"veredicto={v['veredicto']}")

    if v["veredicto"] != "GATE OK":
        return 0

    msg = (f"🐋 FAVORITO_CONFIRMADO#ETH#15min#BUY_YES dentro de banda ballenas: "
           f"la ventana de los últimos {VENTANA_DIAS} días ya pasa gate riguroso limpio.\n"
           f"n={n}  hit={v['hit']*100:.1f}%  pnl/trade={v['pnl_media']:+.3f}€  "
           f"CI90%=[{v['pnl_lo']:+.3f},{v['pnl_hi']:+.3f}]\n"
           f"El histórico completo ya pasaba (n=184). Decisión de subir "
           f"boost_ic_ballenas_favorito_eth15 de 1.0→1.1 sigue siendo tuya.")
    try:
        from shadow_digest import enviar_telegram
        ok = enviar_telegram(msg)
        print(f"[vigia_boost_eth15_ballenas] aviso enviado (telegram={ok})")
    except Exception as e:
        print(f"[vigia_boost_eth15_ballenas] error enviando telegram: {e}")

    latch["avisado"] = True
    latch["avisado_en"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    latch["n"] = n
    latch["pnl_media"] = round(v["pnl_media"], 4)
    LATCH.write_text(json.dumps(latch, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
