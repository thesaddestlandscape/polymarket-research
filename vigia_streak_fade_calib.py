#!/usr/bin/env python3
"""Vigía calibración STREAK_FADE_15M: avisa por Telegram (una vez) cuando el
mecanismo AUTOMÁTICO de recalibración Platt (shadow_postmortem._fit_calibracion_prob,
el mismo usado con ORDER_FLOW_5M/UPDOWN_GBM el 01-Jul) activa calibracion_prob para
esta estrategia — la corrige la sobreconfianza detectada 10-Jul (lado BUY_NO
prob_yes_modelo≈0.30 sobreconfiado 15pp: NO ocurre 55% de las veces, no 70%).

No vigila "n≈200" como umbral fijo — esa cifra es solo el SUELO estructural del
walk-forward (min_train=max(100,n//3) + n_oos≥100), no garantiza activación: el n
real necesario depende del efecto observado (análisis de potencia). La señal
correcta es la transición real calibracion_prob None -> valor, que calcula
shadow_postmortem.py cada ciclo sin intervención. Read-only, no toca dinero ni
config. Ver project_10_propuestas_quant_desk_13jul (ítem 9) e idea_calibracion_platt.
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

ESTRATEGIA = "STREAK_FADE_15M"
LATCH = REPO / "data/live/vigia_streak_fade_calib_latch.json"
PARAMS = REPO / "data/shadow/strategy_params.json"


def main() -> int:
    from shadow_digest import enviar_telegram

    if not PARAMS.exists():
        print("[vigia_streak_fade_calib] sin strategy_params.json")
        return 0
    params = json.loads(PARAMS.read_text(encoding="utf-8"))
    entry = params.get("estrategias", params).get(ESTRATEGIA, {})
    n = entry.get("n", 0)
    calib = entry.get("calibracion_prob")
    print(f"[vigia_streak_fade_calib] n={n} calibracion_prob={calib}")

    if calib is None:
        return 0  # aún no activa, nada que avisar

    # Activó: latch para no repetir el aviso
    if LATCH.exists():
        try:
            if json.loads(LATCH.read_text()).get("avisado"):
                return 0
        except Exception:
            pass

    a = calib.get("a") if isinstance(calib, dict) else None
    b = calib.get("b") if isinstance(calib, dict) else None
    msg = (
        f"🔔 VIGÍA: recalibración Platt AUTOMÁTICA se activó en {ESTRATEGIA}\n"
        f"n={n}  a={a}  b={b}\n"
        f"El mecanismo (mismo que ORDER_FLOW_5M/UPDOWN_GBM, 01-Jul) confirmó con "
        f"walk-forward + bootstrap + potencia estadística que prob_yes_modelo "
        f"estaba sobreconfiado (hallazgo 10-Jul: lado BUY_NO sobreconfiado 15pp) "
        f"y ya corrige automáticamente. Shadow puro — no toca dinero. Solo informativo."
    )
    ok = enviar_telegram(msg)
    LATCH.write_text(json.dumps({
        "avisado": True, "n": n, "calibracion_prob": calib, "telegram_ok": ok,
    }, ensure_ascii=False, indent=1))
    print(f"[vigia_streak_fade_calib] aviso enviado (telegram={ok}), latch escrito")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_streak_fade_calib] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
