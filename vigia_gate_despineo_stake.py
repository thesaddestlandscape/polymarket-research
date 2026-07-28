#!/usr/bin/env python3
"""vigia_gate_despineo_stake.py — Vigía del gate de reapertura del despineo
de max_stake_eur (28-Jul, ver _max_stake_nota en config_live.json).

Motivo: la vez anterior que se despineó el stake (07-Jul) salió con
correlación negativa stake↔acierto y se re-pineó el mismo día, con un gate
de reapertura ("n≥15 trades limpios") que nadie volvió a comprobar --
avisos de Telegram puntuales se pierden en el ruido si nadie los busca
(mismo principio que vigia_log_growth.py). Este vigía cierra ese hueco:
corre analisis_gate_despineo_stake_28jul.py a diario y avisa por Telegram
UNA VEZ (latch) en cuanto n>=15, con el veredicto ya calculado -- si sale
alerta de correlación negativa, la decisión de re-pinear sigue siendo de
Javi, este script solo informa.
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_gate_despineo_stake_28jul import main as correr_analisis, OUT_JSON, N_MIN

LATCH = REPO / "data/live/vigia_gate_despineo_stake_latch.json"


def main() -> int:
    from shadow_digest import enviar_telegram

    latch = {}
    if LATCH.exists():
        try:
            latch = json.loads(LATCH.read_text())
        except Exception:
            latch = {}
    if latch.get("avisado"):
        print("[vigia_gate_despineo_stake] ya avisado, nada que hacer")
        return 0

    correr_analisis()
    try:
        resultado = json.loads(OUT_JSON.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[vigia_gate_despineo_stake] ERROR leyendo {OUT_JSON}: {e}")
        return 0

    n = resultado.get("n", 0)
    if n < N_MIN:
        print(f"[vigia_gate_despineo_stake] n={n}/{N_MIN}, sin concluir")
        return 0

    veredicto = resultado.get("veredicto", "?")
    msg = (
        f"🔔 VIGÍA gate despineo stake: n={n} trades reales desde el 28-Jul\n"
        f"corr(stake,acierto)={resultado.get('corr', 0):+.3f} "
        f"p_shuffle={resultado.get('p_shuffle', 1):.4f}\n"
        f"{veredicto}\n"
        f"Gate de reapertura del 07-Jul, por fin revisado — decidir si "
        f"mantener max_stake_eur=2.00€ o re-pinear."
    )
    ok = enviar_telegram(msg)
    latch = {"avisado": True, "n": n, "corr": resultado.get("corr"),
             "p_shuffle": resultado.get("p_shuffle"), "telegram_ok": ok}
    LATCH.write_text(json.dumps(latch, ensure_ascii=False, indent=1))
    print(f"[vigia_gate_despineo_stake] aviso enviado (telegram={ok})")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_gate_despineo_stake] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
