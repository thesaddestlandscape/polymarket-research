#!/usr/bin/env python3
"""Vigía de frescura de data/live/ballenas_recientes.json (04-Ago, petición
explícita Javi: "que no nos deje desprotegidos jamás").

Contexto: desde el paso 5 de idea_veto_ballenas_firehose_snapshot_diseno_
04ago, live_trade.py::_ballenas_conviccion_mercado() lee este snapshot
(escrito cada 10s por el proceso persistente `polyactivity`,
fetch_polymarket_activity_ws.py) en vez de abrir su propia conexión --
necesario porque live_trade.py es un proceso EFÍMERO (se reinvoca fresco
cada ciclo, no puede esperar a conectar+suscribirse+recibir el primer
mensaje dentro de su presupuesto de latencia).

Si `polyactivity` se cae, cuelga, o el disco impide escribir, el snapshot
se queda viejo. ballenas_firehose_cache.leer_snapshot_reciente() ya es
fail-open ante eso (generado_en con más de max_edad_s=60s -> [] -> el veto
trata n=0 como 'sin_datos', deja pasar el trade sin bloquear) -- ESO es
correcto y deliberado (mismo principio ya aprobado por Javi 16-Jul para
el resto de veto_ballenas, ver vigia_ballenas_cobertura.py). Pero fail-open
SILENCIOSO no es aceptable para un mecanismo que hoy protege las 5 tuplas
live simultáneamente (SOL#15m, ETH#15m, SOL#60m, BTC#60m, ETH#60m, ETH#5m,
ver config_live.json::riesgo.veto_ballenas.combos_validados) -- mismo
mandato de "convertirlo en código que se audite solo" que ya siguen
vigia_calidad_datos.py/vigia_ballenas_cobertura.py, aplicado aquí al eslabón
más nuevo de la cadena.

Comprueba DOS fallos, indistinguibles desde dentro de
leer_snapshot_reciente() (que solo puede devolver [] en ambos casos):
  1. El fichero no existe / no es JSON válido / le falta 'generado_en'.
  2. El fichero existe y es válido pero 'generado_en' lleva más de
     STALE_S segundos sin refrescarse (escritor caído/atascado/reconectando
     más tiempo del normal) -- STALE_S=90 da margen de sobra sobre la
     cadencia real de escritura (10s) y sobre el umbral de frescura que ya
     aplica leer_snapshot_reciente() (60s) para no avisar por un blip de
     un solo ciclo de cron.

Read-only, no toca dinero ni config -- solo lee el snapshot y avisa. Latch
con auto-recuperación (mismo patrón que vigia_calidad_datos.py): avisa UNA
vez al entrar en problema, se calla mientras dure, y al recuperarse resetea
el latch en silencio para que un futuro fallo SÍ vuelva a avisar (nunca se
queda "gastado" tras la primera vez).

Cron sugerido: cada 5min (mismo patrón que vigia_calidad_datos.py -- el
análogo más cercano, misma clase de fail-open silencioso vigilado).
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

SNAPSHOT_PATH = REPO / "data" / "live" / "ballenas_recientes.json"
LATCH_PATH = REPO / "data" / "live" / "vigia_ballenas_snapshot_freshness_latch.json"
CONFIG_PATH = REPO / "data" / "live" / "config_live.json"
STALE_S = 90


def _combos_protegidos() -> list:
    try:
        cfg = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        return cfg.get("riesgo", {}).get("veto_ballenas", {}).get("combos_validados", [])
    except Exception:
        return []


def main() -> int:
    from shadow_digest import enviar_telegram

    try:
        latch = json.loads(LATCH_PATH.read_text()) if LATCH_PATH.exists() else {}
    except Exception:
        latch = {}

    problema = None
    edad_s = None
    if not SNAPSHOT_PATH.exists():
        problema = "ballenas_recientes.json no existe"
    else:
        try:
            payload = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
            generado_en = payload.get("generado_en")
            if not generado_en:
                problema = "ballenas_recientes.json sin 'generado_en'"
            else:
                ts = datetime.fromisoformat(generado_en)
                if ts.tzinfo is None:
                    ts = ts.replace(tzinfo=timezone.utc)
                edad_s = (datetime.now(timezone.utc) - ts).total_seconds()
                if edad_s < 0:
                    problema = f"'generado_en' en el futuro ({edad_s:.0f}s) -- reloj desincronizado o corrupción"
                elif edad_s > STALE_S:
                    problema = f"sin refrescar hace {edad_s:.0f}s (>{STALE_S}s)"
        except Exception as e:
            problema = f"ilegible: {type(e).__name__}: {e}"

    estado = f"PROBLEMA: {problema}" if problema else f"OK (edad={edad_s:.1f}s)" if edad_s is not None else "OK"
    print(f"[vigia_ballenas_snapshot_freshness] {estado}")

    if problema:
        if not latch.get("avisado"):
            combos = _combos_protegidos()
            combos_txt = ", ".join(combos) if combos else "(no se pudo leer combos_validados)"
            msg = (
                f"🔴 VIGÍA snapshot ballenas: {problema}\n"
                f"Mientras esto dure, veto_ballenas es fail-OPEN para TODAS las tuplas "
                f"protegidas a la vez: {combos_txt}\n"
                f"No bloquea el trading (deja pasar sin vetar), pero deja SIN esa protección "
                f"hasta que se recupere. Revisar screen `polyactivity` "
                f"(logs/polymarket_activity.log) y `python3 verify_deploy.py`."
            )
            ok = enviar_telegram(msg)
            latch["avisado"] = True
            latch["problema"] = problema
            latch["ts"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            print(f"[vigia_ballenas_snapshot_freshness] aviso enviado (telegram={ok})")
            LATCH_PATH.write_text(json.dumps(latch, ensure_ascii=False, indent=1))
    elif latch.get("avisado"):
        # Recuperado -- resetea el latch en silencio (mismo patrón que
        # vigia_calidad_datos.py): un futuro corte SÍ debe volver a avisar.
        LATCH_PATH.write_text(json.dumps({}, ensure_ascii=False, indent=1))
        print("[vigia_ballenas_snapshot_freshness] recuperado, latch reseteado")

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_ballenas_snapshot_freshness] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
