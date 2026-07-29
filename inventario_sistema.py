#!/usr/bin/env python3
"""
inventario_sistema.py — petición explícita Javi 29-Jul: "cada inicio de
sesión, revisa TODOS los loggers, observers, .py y demás, ABSOLUTAMENTE
TODOS, para ver cómo van, así no se te olvidan jamás". Origen inmediato:
esta misma sesión, recalculé a mano un cruce de ballenas que
`ballenas_observer.py` ya mantenía en vivo (`ballenas_timing_state_fino.json`)
porque no tenía presente que ese proceso ya existía y ya lo calculaba.

En vez de prometer "me acordaré mejor" (la corrección incorrecta según
project_mision_sistema.md), esto es código que se audita solo: enumera
TODOS los .py del repo y los clasifica en 3 grupos, para que un vistazo
al arranque de sesión baste sin tener que recordar de memoria qué existe.

  A) En screen persistente (SCREENS de verify_deploy.py) — delega en
     verify_deploy.py para el estado FRESH/STALE real, aquí solo lista.
  B) En crontab -l — reporta antigüedad del log (mtime) para detectar
     silenciosos que dejaron de escribir sin que nadie lo note.
  C) NI en screen NI en cron, pero con nombre de infraestructura
     recurrente (vigia_*, *_logger, *_observer, *_executor, fetch_*,
     analisis_diario_*, gate_*) — candidato a "se me olvidó conectarlo",
     se lista explícitamente SIEMPRE, aunque esté vacío (para que quede
     claro que se revisó, no que se omitió).
  D) Resto (scripts de análisis puntual, casi siempre con fecha en el
     nombre tipo _28jul.py, o módulos importados sin punto de entrada
     propio) — solo se cuenta, no se lista uno a uno (sería ruido: son
     históricos, no infraestructura viva que revisar cada sesión).

Solo lectura. No reinicia nada (para eso, verify_deploy.py --restart).
"""
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent

# Patrones de nombre que delatan infraestructura recurrente (no análisis
# puntual) -- si un script nuevo con uno de estos prefijos/sufijos no
# aparece ni en screen ni en cron, es la señal exacta que este script
# existe para no dejar pasar en silencio.
PATRONES_INFRA = (
    "vigia_", "fetch_", "analisis_diario_",
)
SUFIJOS_INFRA = ("_logger.py", "_observer.py", "_executor.py", "_executor_btc15m.py",
                  "_executor_5min.py")

# Excepciones verificadas manualmente (29-Jul): scripts que matchean un
# patrón de infra recurrente pero en realidad se invocan DENTRO de otro
# proceso ya vigilado (run_fast.sh los llama como subprocess cada ciclo,
# no tienen ni necesitan cron/screen propios). Añadir aquí solo tras
# confirmar con `grep <script> run_fast.sh/run_slow.sh`, nunca a ciegas.
EXCEPCIONES_C = {
    "fetch_binance_klines.py",  # invocado en run_fast.sh:43 cada ciclo
}


def _screens_scripts() -> dict[str, str]:
    """nombre_screen -> script .py (relee SCREENS de verify_deploy.py sin
    reimplementar la lista, para que nunca diverjan)."""
    sys.path.insert(0, str(REPO))
    import verify_deploy
    return {nombre: cfg["entry"] for nombre, cfg in verify_deploy.SCREENS.items()}


def _cron_scripts() -> dict[str, str]:
    """basename.py -> línea de crontab completa (para extraer el log)."""
    try:
        salida = subprocess.run(["crontab", "-l"], capture_output=True, text=True, timeout=10).stdout
    except Exception:
        return {}
    out = {}
    for linea in salida.splitlines():
        m = re.search(r"/([A-Za-z0-9_]+\.py)", linea)
        if m:
            out[m.group(1)] = linea.strip()
    return out


def _log_de_cron(linea: str) -> Path | None:
    m = re.search(r">>\s*(\S+\.log)", linea)
    if m:
        return REPO / m.group(1) if not m.group(1).startswith("/") else Path(m.group(1))
    return None


def _intervalo_esperado_minutos(linea: str) -> float:
    """Estima el intervalo esperado entre corridas a partir de los 5
    campos de cron -- necesario porque un umbral fijo (ej. 48h) da falsos
    positivos reales: un cron semanal (día-de-semana fijo) con log de
    hace 3 días es NORMAL, no una señal de fallo (encontrado 29-Jul con
    descubrir_wallets_sospechosas.py, cron `30 5 * * 0`)."""
    campos = linea.split()
    if len(campos) < 5:
        return 60.0  # desconocido -- asumir horario, conservador
    minuto, hora, dia_mes, mes, dia_sem = campos[:5]
    if dia_sem != "*" or (dia_mes != "*" and mes != "*"):
        return 7 * 24 * 60.0  # semanal o más espaciado
    if dia_mes != "*":
        return 30 * 24 * 60.0  # mensual-ish
    if hora == "*":
        if minuto.startswith("*/"):
            return float(minuto[2:])
        return 1.0  # cada minuto (ej. "* * * * *" o con sleep interno)
    if hora.startswith("*/"):
        return float(hora[2:]) * 60.0
    return 24 * 60.0  # hora fija, un disparo al día


def _antiguedad_horas(path: Path) -> float | None:
    try:
        return (datetime.now(timezone.utc).timestamp() - path.stat().st_mtime) / 3600
    except OSError:
        return None


def _es_infra_recurrente(nombre: str) -> bool:
    if any(nombre.startswith(p) for p in PATRONES_INFRA):
        return True
    if any(nombre.endswith(s) for s in SUFIJOS_INFRA):
        return True
    return False


def main() -> int:
    todos = sorted(p.name for p in REPO.glob("*.py"))
    en_screen = _screens_scripts()
    scripts_en_screen = set(en_screen.values())
    cron_map = _cron_scripts()

    print(f"=== INVENTARIO DEL SISTEMA — {len(todos)} scripts .py en el repo ===\n")

    print(f"A) En screen persistente ({len(scripts_en_screen)}): "
          f"{', '.join(sorted(f'{s} ({n})' for n, s in en_screen.items()))}")
    print("   → estado FRESH/STALE real: correr `python3 verify_deploy.py`\n")

    print(f"B) En crontab ({len(cron_map)}) — umbral de alarma = 3x el intervalo "
          f"esperado del propio cron (nunca un número fijo, evita falsos positivos "
          f"en crons semanales/mensuales):")
    filas = []
    for nombre, linea in sorted(cron_map.items()):
        log = _log_de_cron(linea)
        edad = _antiguedad_horas(log) if log else None
        intervalo_min = _intervalo_esperado_minutos(linea)
        umbral_h = max(3 * intervalo_min / 60.0, 1.0)
        tam = log.stat().st_size if log and log.exists() else None
        filas.append((nombre, edad, umbral_h, tam))
    # peor primero: más veces por encima de su propio umbral
    filas.sort(key=lambda f: (f[1] is None, -((f[1] or 0) / f[2])))
    for nombre, edad, umbral_h, tam in filas:
        if edad is None:
            marca = "⚠️ sin log detectado"
        elif edad > umbral_h:
            extra = (" (log vacío/0 bytes -- normal si el script solo escribe en errores/eventos)"
                      if tam == 0 else
                      " -- muchos de estos scripts solo loguean cuando hay algo nuevo que procesar; "
                      "correr a mano antes de concluir que está roto")
            marca = f"🚨 log de hace {edad:.0f}h (esperado <{umbral_h:.0f}h){extra}"
        else:
            marca = f"✅ hace {edad:.1f}h (umbral {umbral_h:.0f}h)"
        print(f"   {nombre:45s} {marca}")

    cubiertos = scripts_en_screen | set(cron_map.keys())
    huerfanos_infra = [n for n in todos if n not in cubiertos and n not in EXCEPCIONES_C
                       and _es_infra_recurrente(n)]
    print(f"\nC) Infraestructura recurrente SIN screen ni cron ({len(huerfanos_infra)}) "
          f"— revisar si se olvidó conectar:")
    if huerfanos_infra:
        for n in huerfanos_infra:
            print(f"   ⚠️  {n}")
    else:
        print("   (ninguno — todo lo que parece infraestructura recurrente está conectado)")

    resto = [n for n in todos if n not in cubiertos and n not in huerfanos_infra]
    print(f"\nD) Resto — análisis puntual/módulos importados, no requieren revisión "
          f"recurrente ({len(resto)}, no listados individualmente)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
