#!/usr/bin/env python3
"""vigia_gate_calibracion.py — Vigía diario del gate de calibración
(analisis_gate_calibracion.py / data/shadow/gate_calibracion.json).

Origen (31-Jul): vigia_log_loss_vs_mercado.py detectó que UPDOWN_GBM_IBS_ALTO
-- LIVE-CANDIDATA con IC=+0.219, n=30 -- tenía log-loss gap=-0.1735 frente
al precio de mercado (sobreconfiada: 13/31 predicciones clavadas en el
clamp 0.95 con hit-rate real 61.5% ahí). El IC mide dirección, no
calibración -- una candidata puede tener IC positivo y aun así estar mal
calibrada, lo cual generalmente decae en la promoción (peor gestión del
tamaño de la señal). Decisión (Opción B, ver conversación 31-Jul): en vez
de tocar prob_yes (Opción A, requiere aprobación explícita + /code-review,
misma cautela que P19/P20 en CLAUDE.md), añadir este check ADICIONAL antes
de promocionar cualquier candidata, sin tocar código de dinero real.

Hace 3 cosas, mismo patrón que vigia_gate_bucket_propio.py:
1. Re-corre analisis_gate_calibracion.py (results.csv crece cada ciclo).
2. Diffea contra el estado de AYER (latch) -- avisa por Telegram SOLO
   veredictos NUEVOS "mal_calibrado_confirmado" en estrategias que TODAVÍA
   no tienen calibracion_prob activo (el caso que de verdad importa: una
   candidata a punto de promocionarse con sobreconfianza sin corregir).
3. Reporta cobertura: cuántas estrategias siguen sin n>=40 para concluir.

Puramente informativo (igual que vigia_log_growth.py) -- NO bloquea nada
automáticamente. La promoción a pares_permitidos_live sigue siendo manual;
este aviso es una entrada más a revisar junto a IC/Wilson/fill-ability
antes de decidir, no una puerta de aprobación en código.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/shadow/gate_calibracion.json"
LATCH = REPO / "data/live/vigia_gate_calibracion_latch.json"


def main() -> int:
    from shadow_digest import enviar_telegram

    r = subprocess.run([sys.executable, str(REPO / "analisis_gate_calibracion.py")],
                        capture_output=True, text=True, timeout=120, cwd=str(REPO))
    if r.returncode != 0:
        print(f"ERROR ejecutando analisis_gate_calibracion.py: {r.stderr[-2000:]}")
        return 1

    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8")).get("estrategias", {})
    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    avisos = []
    n_sin_concluir = 0
    for strat, info in nuevo.items():
        v_nuevo = info.get("veredicto", "sin_concluir")
        v_antes = previo.get(strat, {}).get("veredicto", "sin_concluir")
        if v_nuevo == "sin_concluir":
            n_sin_concluir += 1
            continue
        if v_antes == v_nuevo:
            continue
        if v_nuevo == "mal_calibrado_confirmado" and not info.get("calibracion_activa"):
            avisos.append(
                f"🔴 {strat}: SIN corregir -- gap={info['gap_medio']:+.4f} "
                f"CI90%=[{info['ci_lo']:.4f},{info['ci_hi']:.4f}] n={info['n']} "
                f"-- el modelo está peor calibrado que el mercado, sin Platt activo. "
                f"NO promocionar sin revisar (o esperar a que calibracion_prob la corrija)."
            )
        elif v_nuevo == "bien_calibrado_confirmado":
            avisos.append(f"🟢 {strat}: bien calibrado confirmado (n={info['n']}, gap={info['gap_medio']:+.4f})")

    print(f"[vigia_gate_calibracion] {len(nuevo)} estrategias, {n_sin_concluir} sin_concluir (n<40)")

    if avisos:
        msg = "🎯 Gate calibración — nuevos veredictos hoy:\n" + "\n".join(avisos)
        print(msg)
        enviar_telegram(msg)
    else:
        print("[vigia_gate_calibracion] sin veredictos nuevos hoy")

    LATCH.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_gate_calibracion] ERROR {type(e).__name__}: {e}")
        sys.exit(1)
