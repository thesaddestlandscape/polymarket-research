#!/usr/bin/env python3
"""Vigía cobertura veto_ballenas: avisa por Telegram si el % de evaluaciones
"sin_datos"/"sin_condition_id" se dispara — la mitigación acordada con Javi
16-Jul para el fail-open de live_trade.py::_evaluar_veto_ballenas.

Contexto: veto_ballenas (live_trade.py) falla ABIERTO cuando no consigue
datos suficientes de ballenas en tiempo real (deja pasar el trade normal,
no lo veta) — decisión explícita de Javi tras discutir la tensión con la
regla CLAUDE.md "cada guardia nueva es fail-closed": fallar cerrado podría
vaciar el volumen de SOL#15min sin evidencia de que bloquear ahí sea
correcto, siendo la primera vez que se consulta esto en el momento exacto
de ejecución. Mitigación acordada: fail-open VIGILADO, no silencioso — este
script lee data/live/veto_ballenas_eventos.jsonl (una línea por cada
evaluación real del veto, con o sin datos) y avisa si la cobertura cae por
debajo de lo esperable, para que la decisión fail-open/fail-closed se pueda
revisar con dato real en vez de a ciegas.

Read-only, no toca dinero ni config — solo lee el log de eventos y avisa.
Cron sugerido: cada 30-60min (ver crontab).
"""
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

EVENTOS_PATH = REPO / "data/live/veto_ballenas_eventos.jsonl"
LATCH_PATH = REPO / "data/live/vigia_ballenas_cobertura_latch.json"

VENTANA_HORAS = 6         # solo mirar eventos recientes -- cobertura de HOY, no arrastrar histórico viejo
MIN_EVENTOS_PARA_JUZGAR = 10   # n<10 en la ventana: no hay muestra suficiente para alarmarse
UMBRAL_SIN_DATOS_PCT = 0.30    # >=30% de evaluaciones sin datos -> avisar
COOLDOWN_HORAS = 6             # no repetir el mismo aviso antes de esto


def _parse_dt(s):
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except Exception:
        return None


def main() -> int:
    from shadow_digest import enviar_telegram

    if not EVENTOS_PATH.exists():
        print("[vigia_ballenas_cobertura] sin eventos todavía")
        return 0

    ahora = datetime.now(timezone.utc)
    corte = ahora - timedelta(hours=VENTANA_HORAS)
    eventos = []
    with open(EVENTOS_PATH, encoding="utf-8") as f:
        for linea in f:
            try:
                ev = json.loads(linea)
            except Exception:
                continue
            ts = _parse_dt(ev.get("ts", ""))
            if ts is None or ts < corte:
                continue
            eventos.append(ev)

    n_total = len(eventos)
    n_sin_datos = sum(1 for ev in eventos if ev.get("motivo") in ("sin_datos", "sin_condition_id"))
    pct_sin_datos = (n_sin_datos / n_total) if n_total else 0.0

    print(f"[vigia_ballenas_cobertura] ventana={VENTANA_HORAS}h n={n_total} "
          f"sin_datos={n_sin_datos} ({pct_sin_datos*100:.1f}%)")

    if n_total < MIN_EVENTOS_PARA_JUZGAR or pct_sin_datos < UMBRAL_SIN_DATOS_PCT:
        return 0

    try:
        latch = json.loads(LATCH_PATH.read_text()) if LATCH_PATH.exists() else {}
    except Exception:
        latch = {}
    ultimo = _parse_dt(latch.get("ultimo_aviso", ""))
    if ultimo is not None and (ahora - ultimo) < timedelta(hours=COOLDOWN_HORAS):
        print(f"[vigia_ballenas_cobertura] umbral cruzado pero en cooldown "
              f"(último aviso {latch.get('ultimo_aviso')})")
        return 0

    por_combo = {}
    for ev in eventos:
        combo = ev.get("combo", "?")
        d = por_combo.setdefault(combo, {"n": 0, "sin_datos": 0})
        d["n"] += 1
        if ev.get("motivo") in ("sin_datos", "sin_condition_id"):
            d["sin_datos"] += 1
    detalle = "\n".join(
        f"  {combo}: {d['sin_datos']}/{d['n']} sin datos ({100*d['sin_datos']/d['n']:.0f}%)"
        for combo, d in por_combo.items()
    )
    msg = (
        f"⚠️ VIGÍA veto_ballenas: cobertura débil últimas {VENTANA_HORAS}h\n"
        f"{n_sin_datos}/{n_total} evaluaciones sin datos suficientes ({pct_sin_datos*100:.0f}% "
        f">= umbral {UMBRAL_SIN_DATOS_PCT*100:.0f}%)\n"
        f"{detalle}\n"
        f"El veto está en fail-open (deja pasar el trade sin datos) — con esta "
        f"cobertura conviene revisar si sigue teniendo sentido o si toca "
        f"replantear fail-closed para el/los combo(s) afectados."
    )
    ok = enviar_telegram(msg)
    print(f"[vigia_ballenas_cobertura] aviso enviado (telegram={ok})")
    latch["ultimo_aviso"] = ahora.isoformat(timespec="seconds")
    LATCH_PATH.write_text(json.dumps(latch, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_ballenas_cobertura] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
