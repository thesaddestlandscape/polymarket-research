#!/usr/bin/env python3
"""Vigía meta: resumen horario consolidado de TODOS los avisos que los demás
vigías mandan por Telegram (~35 scripts, cada uno con su propio latch/umbral).

Origen (06-Ago, petición explícita de Javi tras el incidente de git lock
huérfano 2h29min sin detectar): un aviso real (vigia_cobertura_feature_rules
avisando de GBM_LATE_15M_MULTIHORIZONTE sin aprendizaje causal) llevaba
tiempo en Telegram sin que nadie lo revisara ni actuara. Javi: "revisa
telegram tu cada hora... que para algo está el aviso" -- pero la revisión y
el ARREGLO con criterio los hace Claude Code en sesión (ver cron de sesión
complementario, session-bound, máx 7 días); ESTE script es la parte que
tiene que sobrevivir sin depender de ninguna sesión -- garantiza que NINGÚN
aviso se quede más de 1h sin aparecer consolidado en un único mensaje,
aunque no haya ninguna sesión de Claude Code abierta para actuar sobre él.

Mecanismo: cada script que llama a enviar_telegram() (shadow_digest.py)
imprime "aviso enviado" en su propio log (logs/vigia_*.log) al mandar un
mensaje real. Este vigía trackea, POR FICHERO, el offset de bytes ya
revisado (data/live/vigia_resumen_alertas_offsets.json) y en cada corrida
solo mira las líneas NUEVAS desde la última vez -- así una corrida horaria
cubre exactamente "lo que pasó en la última hora" sin re-procesar nada.

Si hay avisos nuevos: manda UN mensaje consolidado (evita ruido de 35
mensajes sueltos). Si no hay nada nuevo: no manda nada (silencio = todo
tranquilo), pero deja constancia en su propio log para que
vigia_pipeline_latencia.py / el barrido de sesión detecten si ESTE vigía
deja de correr.

Read-only sobre los demás logs, no toca dinero ni config -- solo agrega y
notifica. La decisión/arreglo sigue siendo de Claude Code en sesión o de
Javi, igual que todos los demás vigías de este proyecto.
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

LOGS_DIR = REPO / "logs"
OFFSETS = REPO / "data/live/vigia_resumen_alertas_offsets.json"

# Líneas que indican que un vigía mandó un aviso real por Telegram (mismo
# patrón textual usado en todos los vigias_*.py existentes, ver grep cruzado
# 06-Ago sobre logs/vigia_*.log).
PATRON_AVISO = re.compile(r"aviso enviado|Mensaje enviado a Telegram", re.IGNORECASE)


def _cargar_offsets():
    try:
        return json.loads(OFFSETS.read_text())
    except Exception:
        return {}


def _guardar_offsets(offsets):
    OFFSETS.parent.mkdir(parents=True, exist_ok=True)
    OFFSETS.write_text(json.dumps(offsets, indent=2))


def _lineas_nuevas(path: Path, offset: int):
    """Devuelve (lineas_con_aviso, nuevo_offset). Si el fichero se truncó/rotó
    (offset > tamaño actual), reinicia desde 0 -- nunca lanza, nunca se
    bloquea esperando datos que no van a llegar."""
    size = path.stat().st_size
    start = offset if offset <= size else 0
    lineas = []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        f.seek(start)
        for linea in f:
            if PATRON_AVISO.search(linea):
                lineas.append(linea.strip())
    return lineas, size


def main() -> int:
    from shadow_digest import enviar_telegram

    offsets = _cargar_offsets()
    hallazgos = {}  # nombre_log -> [lineas]

    for log_path in sorted(LOGS_DIR.glob("vigia_*.log")):
        nombre = log_path.stem
        offset_previo = offsets.get(nombre, log_path.stat().st_size)  # 1ª vez: no reprocesar histórico
        lineas, nuevo_offset = _lineas_nuevas(log_path, offset_previo)
        offsets[nombre] = nuevo_offset
        if lineas:
            hallazgos[nombre] = lineas

    _guardar_offsets(offsets)

    n_avisos = sum(len(v) for v in hallazgos.values())
    print(f"[vigia_resumen_alertas] {len(hallazgos)} vigías con avisos nuevos, "
          f"{n_avisos} avisos en la última hora")

    if not hallazgos:
        return 0  # silencio -- nada nuevo, no molestar a Javi cada hora en vano

    detalle = []
    for nombre, lineas in sorted(hallazgos.items()):
        detalle.append(f"• {nombre}: {len(lineas)} aviso(s)")
    msg = (
        f"📋 RESUMEN HORARIO de avisos ({n_avisos} en {len(hallazgos)} vigía(s)):\n"
        + "\n".join(detalle)
        + "\n\nRevisar logs/<vigia>.log para el detalle. Si no hay sesión de "
          "Claude Code activa revisándolo, queda pendiente hasta la próxima."
    )
    ok = enviar_telegram(msg)
    print(f"[vigia_resumen_alertas] resumen enviado (telegram={ok})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
