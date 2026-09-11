#!/usr/bin/env python3
"""Vigía data_quality.json (13-Jul, decisión Javi): "simbolo_bloqueado()
se queda fail-open si data_quality.json no se puede leer — vigilamos".

Contexto: `simbolo_bloqueado()` (data_quality.py) gatea 3 estrategias GBM
en shadow_predict.py, incluidos los pares live SOL/ETH. Si
data_quality.json no se puede leer, devuelve False para CUALQUIER símbolo
(nada bloqueado) — ya avisa con un print() en el momento, pero eso solo
se ve si alguien mira logs/fast.log. Decisión explícita de Javi: no pasar
a fail-closed todavía, mantenerlo así y vigilarlo activamente en vez de
confiar en que alguien se acuerde de mirar el log (mandato del proyecto:
"convertirlo en código que se audite solo", no una promesa).

Comprueba dos fallos, ambos indistinguibles desde dentro de
simbolo_bloqueado():
  1. El fichero no es JSON válido / no tiene 'estado_global'.
  2. El fichero existe y es válido pero lleva sin refrescarse más de
     STALE_MIN (generar_reporte() lo reescribe cada ciclo, ~20s, vía
     shadow_predict.py — si lleva minutos sin tocarse, algo se rompió
     silenciosamente en ese camino).

Read-only, no toca dinero ni decisiones — solo avisa. Latch para no
repetir el mismo aviso cada 10min mientras el problema persiste.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DQ_PATH = REPO / "data/shadow/data_quality.json"
LATCH = REPO / "data/shadow/vigia_calidad_datos_latch.json"
STALE_MIN = 10


def main() -> int:
    from shadow_digest import enviar_telegram

    try:
        latch = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        latch = {}

    problema = None
    if not DQ_PATH.exists():
        problema = "data_quality.json no existe"
    else:
        try:
            dq = json.loads(DQ_PATH.read_text(encoding="utf-8"))
            if "estado_global" not in dq:
                problema = "data_quality.json sin 'estado_global'"
            else:
                ts_str = dq.get("timestamp_utc", "")
                ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                if ts.tzinfo is None:
                    ts = ts.replace(tzinfo=timezone.utc)
                edad_min = (datetime.now(timezone.utc) - ts).total_seconds() / 60
                if edad_min > STALE_MIN:
                    problema = f"sin refrescar hace {edad_min:.0f}min (>{STALE_MIN}min)"
        except Exception as e:
            problema = f"ilegible: {type(e).__name__}: {e}"

    print(f"[vigia_calidad_datos] {'PROBLEMA: ' + problema if problema else 'OK'}")

    if problema:
        if not latch.get("avisado"):
            msg = (
                f"🔴 VIGÍA calidad de datos: {problema}\n"
                f"Mientras esto dure, simbolo_bloqueado() es fail-OPEN "
                f"(NO bloquea ningún símbolo, ni siquiera con datos malos) "
                f"— afecta a GBM_LATE_15M en pares live SOL/ETH.\n"
                f"Decisión 13-Jul: se vigila en vez de pasar a fail-closed. "
                f"Revisar logs/fast.log y por qué generar_reporte() no "
                f"está refrescando data_quality.json."
            )
            ok = enviar_telegram(msg)
            latch["avisado"] = True
            latch["problema"] = problema
            print(f"[vigia_calidad_datos] aviso enviado (telegram={ok})")
            LATCH.write_text(json.dumps(latch, ensure_ascii=False, indent=1))
    elif latch.get("avisado"):
        # Recuperado — resetea el latch en silencio (mismo patrón que
        # vigia_ic_live: un futuro bajón sí debe volver a avisar).
        LATCH.write_text(json.dumps({}, ensure_ascii=False, indent=1))
        print("[vigia_calidad_datos] recuperado, latch reseteado")

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_calidad_datos] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
