#!/usr/bin/env python3
"""
vigia_resumen_diario_unico.py -- 31-Ago (petición explícita Javi, propuesta
#10 de la sesión): consolida en UN solo mensaje de Telegram los avisos de
la mañana de la familia de vigías "gate_bucket" (micro-bucket de precio),
que hoy mandan 6-8 mensajes sueltos en la misma franja horaria (06:5x-07:1x
UTC) -- ruido que dificulta ver el panorama completo sin grep-ear log a
log cada sesión (hallazgo real de la propia sesión que motivó esto).

NO sustituye los avisos individuales -- cada vigía sigue mandando el suyo
(mismo criterio de "nunca tocar lo que ya funciona" para las alertas
tempranas: si Javi solo mira Telegram, quiere el aviso YA, no esperar a
este resumen). Este es un AÑADIDO: un digest de "qué cambió hoy en toda
la familia de gates" para la sesión de trabajo, no un reemplazo de la
alerta en tiempo real.

Mecanismo: lee la COLA de cada log de la familia gate_bucket (los que
corren en la franja 06:4x-07:1x UTC, ver LOGS abajo) y extrae el bloque
de la corrida de HOY -- desde la ÚLTIMA línea que matchea un patrón de
cabecera conocido ("nuevos veredictos", "pendientes de 2ª confirmación",
etc.) hasta el final del fichero (asume que el cron ya corrió hoy antes
de que este script se dispare, mismo orden que el resto del bloque
06:4x-07:1x). Si no encuentra ningún bloque reciente, reporta "sin
novedades hoy" para esa fuente en vez de omitirla en silencio.

Cron: se programa DESPUÉS del último de los vigías que consolida (07:07
UTC es el más tardío hoy) -- ver crontab, sugerido 15 7 * * *.
"""
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from shadow_digest import enviar_telegram  # noqa: E402

LOGS_DIR = REPO / "logs"

# (log, etiqueta) -- familia gate_bucket que dispara en la franja 06:4x-07:1x UTC.
FUENTES = [
    ("vigia_gate_bucket_propio.log", "Gate bucket propio (grid fijo, cripto)"),
    ("vigia_gate_bucket_fino.log", "Gate bucket fino (ventana deslizante, cripto)"),
    ("vigia_gate_bucket_propio_fillable.log", "Gate fillable (payout asimétrico, cripto)"),
    ("vigia_bot_wallets_gate_bucket.log", "P-GALLINA bot wallets (DISPERSO/SNIPER/WEEKLY_TEMPRANO)"),
    ("vigia_candidata9_10_gate_bucket.log", "Candidata 9/10 (bot consenso / cross-activo)"),
    ("vigia_sports_wallet_mirror_gate_bucket.log", "Wallet Mirror sports (grid fijo)"),
    ("vigia_sports_wallet_mirror_gate_bucket_fino.log", "Wallet Mirror sports (ventana deslizante)"),
]

# Patrones de cabecera que marcan el arranque de un bloque de "novedades" --
# distintos vigías usan textos ligeramente distintos, se agrupan aquí.
_CABECERAS = re.compile(
    r"(nuevos veredictos|nuevo\(s\) veredicto|con veredicto (final|tras)|"
    r"pendientes de 2ª confirmación|bucket\(s\).*veredicto)"
)
_LINEA_UTIL = re.compile(r"^(🟢|🔴|⏳|🎯|🐋|🤖)")


def _bloque_de_hoy(nombre_log: str) -> list[str]:
    path = LOGS_DIR / nombre_log
    if not path.exists():
        return []
    try:
        lineas = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception:
        return []
    # última posición donde arranca un bloque de cabecera reconocido
    idx_inicio = None
    for i in range(len(lineas) - 1, -1, -1):
        if _CABECERAS.search(lineas[i]):
            idx_inicio = i
            break
    if idx_inicio is None:
        return []
    utiles = [l for l in lineas[idx_inicio:] if _LINEA_UTIL.match(l.strip())]
    return utiles


def main() -> int:
    hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    secciones = []
    total_lineas = 0
    for nombre_log, etiqueta in FUENTES:
        lineas = _bloque_de_hoy(nombre_log)
        if not lineas:
            continue
        total_lineas += len(lineas)
        # tope por fuente para no reventar el límite de Telegram (4096 chars)
        cuerpo = "\n".join(lineas[:12])
        extra = f"\n  … +{len(lineas) - 12} más" if len(lineas) > 12 else ""
        secciones.append(f"*{etiqueta}*\n{cuerpo}{extra}")

    if not secciones:
        print(f"[{hoy}] sin novedades en ninguna fuente de la familia gate_bucket hoy -- no se envía digest")
        return 0

    texto = (
        f"📋 *Resumen diario — familia gate_bucket* ({hoy})\n"
        f"{len(secciones)}/{len(FUENTES)} fuentes con novedades, {total_lineas} líneas en total\n\n"
        + "\n\n".join(secciones)
    )
    if len(texto) > 4000:
        texto = texto[:3950] + "\n\n… (truncado, ver logs/ individuales)"
    ok = enviar_telegram(texto, bot="cripto")
    print(f"[{hoy}] digest enviado={ok}, {len(secciones)} fuentes, {total_lineas} líneas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
