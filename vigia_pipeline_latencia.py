#!/usr/bin/env python3
"""
vigia_pipeline_latencia.py — vigilancia HORARIA del ciclo resolve+postmortem
(cron cada hora), complemento del chequeo diario de analisis_diario_salud_
sistema.py (una vez al día, 07:08 UTC).

Origen (05-Ago, petición explícita Javi tras ver un outlier puntual de 217s
en el snapshot diario -- "vigilar cada hora"): un solo ciclo lento aislado
dentro de 24h de datos ya se diluye en el p50/p95 diario y no dispara nada
hasta la próxima corrida del cron diario, hasta 24h después. Este vigía
mira solo la ÚLTIMA hora y solo avisa si hay ≥2 outliers en esa ventana
(no 1) -- un blip aislado bajo carga puntual (ej. push de git en curso,
carga de CPU alta) es normal y ya se resuelve solo; 2+ en la misma hora es
la señal real de que algo se ha degradado de verdad, mismo criterio que
motivó el incidente del 04-Ago (postmortem atascado >10min, real, no un
blip).

Reutiliza medir_ciclos_pipeline() de analisis_diario_salud_sistema.py
(mismo parseo de fast.log, mismo umbral UMBRAL_CICLO_LENTO_S) para no
duplicar la lógica -- solo cambia la ventana (1h en vez de 24h) y el
criterio de aviso (conteo de outliers, no percentiles).

Cron sugerido (cada hora, offset para no coincidir con el resto):
  15 * * * * flock -n /tmp/vigia_pipeline_latencia.lock /root/polymarket-research/.venv/bin/python /root/polymarket-research/vigia_pipeline_latencia.py >> /root/polymarket-research/logs/vigia_pipeline_latencia.log 2>&1
"""
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

FAST_LOG = REPO / "logs" / "fast.log"
ESTADO_PATH = REPO / "data" / "shadow" / "vigia_pipeline_latencia_state.json"

UMBRAL_CICLO_LENTO_S = 120  # mismo umbral que analisis_diario_salud_sistema.py
MIN_OUTLIERS_PARA_AVISAR = 2  # 1 outlier aislado = ruido normal, no avisar
VENTANA_MIN = 60


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def medir_ultima_hora() -> dict:
    """Duraciones resolve→postmortem de la última hora, tomado de fast.log."""
    if not FAST_LOG.exists():
        return {"error": "fast.log no existe"}
    corte = datetime.now(timezone.utc) - timedelta(minutes=VENTANA_MIN)
    resolve_ts, postmortem_ts = [], []
    re_resolve = re.compile(r"^\[([\d\-T:+]+)\] === Shadow resolve ===")
    re_postmortem = re.compile(r"^\[([\d\-T:+]+)\] === Fin postmortem ===")
    try:
        with open(FAST_LOG, encoding="utf-8", errors="replace") as f:
            for linea in f:
                for regex, bucket in ((re_resolve, resolve_ts), (re_postmortem, postmortem_ts)):
                    m = regex.match(linea)
                    if m:
                        try:
                            ts = datetime.fromisoformat(m.group(1))
                        except ValueError:
                            continue
                        if ts >= corte:
                            bucket.append(ts)
    except Exception as e:
        return {"error": f"no se pudo leer fast.log: {e}"}

    duraciones = []
    j = 0
    for r in resolve_ts:
        while j < len(postmortem_ts) and postmortem_ts[j] < r:
            j += 1
        if j < len(postmortem_ts):
            duraciones.append(round((postmortem_ts[j] - r).total_seconds(), 1))

    outliers = [d for d in duraciones if d > UMBRAL_CICLO_LENTO_S]
    return {
        "n_ciclos": len(duraciones),
        "duraciones_s": duraciones,
        "outliers_s": outliers,
        "n_outliers": len(outliers),
    }


def _cargar_estado() -> dict:
    if ESTADO_PATH.exists():
        try:
            return json.loads(ESTADO_PATH.read_text())
        except Exception:
            pass
    return {}


def _guardar_estado(estado: dict) -> None:
    ESTADO_PATH.write_text(json.dumps(estado, indent=2))


def main() -> int:
    r = medir_ultima_hora()
    if "error" in r:
        _log(f"error: {r['error']}")
        return 1

    hora_actual = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H")
    estado = _cargar_estado()

    _log(f"última {VENTANA_MIN}min: n_ciclos={r['n_ciclos']} "
         f"n_outliers={r['n_outliers']} (umbral={UMBRAL_CICLO_LENTO_S}s) "
         f"outliers={r['outliers_s']}")

    if r["n_outliers"] >= MIN_OUTLIERS_PARA_AVISAR:
        # Latch por hora -- evita reavisar si el cron se re-ejecuta o se
        # corre a mano dentro de la misma hora ya avisada.
        if estado.get("ultima_hora_avisada") != hora_actual:
            from shadow_digest import enviar_telegram
            enviar_telegram(
                f"⏱️ Pipeline lento: {r['n_outliers']} ciclos resolve+postmortem "
                f">{UMBRAL_CICLO_LENTO_S}s en la última hora ({r['outliers_s']}).\n"
                f"Revisar: carga CPU (uptime), procesos colgados (ps aux), "
                f"disco/RAM. Ver también data/shadow/salud_sistema_diaria.json."
            )
            estado["ultima_hora_avisada"] = hora_actual
            _log(f"🚨 aviso enviado ({r['n_outliers']} outliers)")
        else:
            _log("outliers ya avisados esta hora, no se repite")
    estado["ultimo_check"] = datetime.now(timezone.utc).isoformat()
    estado["ultimo_resultado"] = r
    _guardar_estado(estado)
    return 0


if __name__ == "__main__":
    sys.exit(main())
