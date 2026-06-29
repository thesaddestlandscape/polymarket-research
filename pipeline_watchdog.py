"""
pipeline_watchdog.py — Guardián local del pipeline. Corre en screen -S watchdog.

Cada 120s verifica que el fast loop esté generando predicciones.
Si detecta silencio + error conocido en el log → aplica el fix mínimo.
Para bugs desconocidos → solo alerta (no toca código).

Checks:
  1. predictions_HOY.csv actualizado en los últimos 5 min
  2. Último error en fast.log → patrón conocido → fix automático
  3. postmortem.csv > 50MB → regenerar (delete → siguiente ciclo lo recrea limpio)

Fixes automáticos implementados:
  A. UnboundLocalError: variable usada antes de asignarse → busca la línea y la elimina
  B. postmortem.csv bloat → elimina (se regenera sano en el siguiente ciclo del bot)

NO toca lógica de negocio. Solo bugs de Python obvios y archivos de datos corruptos.
"""

import os
import re
import sys
import time
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO      = Path(__file__).parent
LOG_FAST  = REPO / "logs" / "fast.log"
LOG_WATCH = REPO / "logs" / "watchdog.log"
DIR_SHADOW = REPO / "data" / "shadow"

CHECK_INTERVAL    = 120    # segundos entre checks
MAX_PRED_SILENCE  = 300    # segundos sin actualizar predictions → alerta
MAX_POSTMORTEM_MB = 50     # MB máximos para postmortem.csv antes de limpiar


def log(msg: str):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    with open(LOG_WATCH, "a") as f:
        f.write(line + "\n")


def pred_csv_hoy() -> Path:
    return DIR_SHADOW / f"predictions_{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.csv"


def segundos_desde_update(path: Path) -> float | None:
    """Retorna cuántos segundos han pasado desde la última modificación del archivo."""
    if not path.exists():
        return None
    mtime = path.stat().st_mtime
    return time.time() - mtime


def ultimos_errores_log(n_lineas: int = 200) -> str:
    """Extrae las últimas n_lineas del fast.log para buscar errores."""
    if not LOG_FAST.exists():
        return ""
    try:
        result = subprocess.run(
            ["tail", "-n", str(n_lineas), str(LOG_FAST)],
            capture_output=True, text=True, timeout=5
        )
        return result.stdout
    except Exception:
        return ""


def extraer_traceback(texto: str) -> str:
    """Extrae el último bloque Traceback del texto de log."""
    bloques = texto.split("Traceback")
    if len(bloques) < 2:
        return ""
    ultimo = "Traceback" + bloques[-1]
    # Cortar hasta el final del error (primera línea que no empieza con espacio ni File)
    lineas = ultimo.split("\n")
    resultado = []
    for l in lineas:
        resultado.append(l)
        if l and not l.startswith(" ") and not l.startswith("Traceback") and not l.startswith("File") and len(resultado) > 3:
            break
    return "\n".join(resultado[:20])


# ──────────────────────────────────────────────────────────────────────────────
# FIX A: UnboundLocalError — variable usada antes de asignarse
# Patrón: "cannot access local variable 'X' where it is not associated"
# Estrategia: buscar la línea que usa X antes de que esté definida y eliminarla
# si es dead code (el resultado no se usa en la línea siguiente).
# ──────────────────────────────────────────────────────────────────────────────
def fix_unbound_local(tb: str) -> bool:
    """
    Detecta UnboundLocalError, encuentra la línea culpable en el script,
    y la elimina si es dead code (asignación a variable cuyo resultado no se usa).
    Retorna True si aplicó un fix.
    """
    m = re.search(r"cannot access local variable '(\w+)' where it is not associated", tb)
    if not m:
        return False
    var = m.group(1)

    # Extraer el archivo afectado del traceback
    file_match = re.search(r'File "([^"]+\.py)", line (\d+)', tb)
    if not file_match:
        return False
    script_path = Path(file_match.group(1))
    if not script_path.exists():
        # Intentar con ruta relativa al repo
        script_path = REPO / script_path.name
    if not script_path.exists():
        log(f"  [FIX-A] No encuentro el script: {file_match.group(1)}")
        return False

    linea_error = int(file_match.group(2))
    log(f"  [FIX-A] UnboundLocalError: var='{var}' en {script_path.name}:{linea_error}")

    contenido = script_path.read_text(encoding="utf-8")
    lineas = contenido.split("\n")

    # Buscar la primera ocurrencia de 'var' ANTES de su definición (var =)
    # En el contexto de las últimas 50 líneas antes del error
    inicio = max(0, linea_error - 50)
    fin    = linea_error  # línea 1-based → índice 0-based

    candidatas_uso = []
    definicion_encontrada = False
    for i in range(inicio, fin):
        l = lineas[i]
        stripped = l.strip()
        # ¿Es la definición de la variable?
        if re.match(rf"^\s*{re.escape(var)}\s*=", l):
            definicion_encontrada = True
        # ¿Usa la variable sin haberla definido?
        elif var in l and not definicion_encontrada:
            # ¿La línea es una asignación a otra variable cuyo resultado no se usa?
            # e.g.: "pred_features_now = json.loads(features_json)"
            uso_dead = re.match(r"^\s*\w+\s*=\s*.+", stripped)
            if uso_dead:
                candidatas_uso.append(i)

    if not candidatas_uso:
        log(f"  [FIX-A] No encontré la línea problemática automáticamente en {script_path.name}")
        return False

    # Verificar que la variable definida en esa línea no se usa después
    linea_candidata_idx = candidatas_uso[-1]
    var_asignada_match = re.match(r"^\s*(\w+)\s*=", lineas[linea_candidata_idx].strip())
    if not var_asignada_match:
        log("  [FIX-A] No puedo determinar qué variable se asigna en la línea candidata")
        return False

    var_asignada = var_asignada_match.group(1).strip()
    # Buscar si var_asignada se usa en las líneas siguientes (dentro de las próximas 20)
    usos_posteriores = any(
        var_asignada in lineas[j]
        for j in range(linea_candidata_idx + 1, min(linea_candidata_idx + 20, len(lineas)))
        if not lineas[j].strip().startswith("#")
        and f"{var_asignada} =" not in lineas[j]  # no contar re-asignaciones
    )

    if usos_posteriores:
        log(f"  [FIX-A] '{var_asignada}' se usa después → no es dead code, no elimino")
        return False

    # APLICAR FIX: eliminar la línea
    linea_num_display = linea_candidata_idx + 1
    log(f"  [FIX-A] Eliminando línea {linea_num_display} (dead code): {lineas[linea_candidata_idx].strip()[:80]}")

    # Backup
    backup = script_path.with_suffix(".py.bak")
    backup.write_text(contenido, encoding="utf-8")

    # Eliminar la línea
    del lineas[linea_candidata_idx]
    script_path.write_text("\n".join(lineas), encoding="utf-8")

    # Verificar sintaxis
    result = subprocess.run(
        [sys.executable, "-m", "py_compile", str(script_path)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        log(f"  [FIX-A] Sintaxis rota tras fix → revertiendo")
        script_path.write_text(contenido, encoding="utf-8")
        backup.unlink(missing_ok=True)
        return False

    backup.unlink(missing_ok=True)
    log(f"  [FIX-A] ✅ Fix aplicado y verificado en {script_path.name}")
    return True


# ──────────────────────────────────────────────────────────────────────────────
# FIX B: postmortem.csv bloat
# ──────────────────────────────────────────────────────────────────────────────
def fix_postmortem_bloat() -> bool:
    pm = DIR_SHADOW / "postmortem.csv"
    if not pm.exists():
        return False
    size_mb = pm.stat().st_size / 1_000_000
    if size_mb < MAX_POSTMORTEM_MB:
        return False
    log(f"  [FIX-B] postmortem.csv tiene {size_mb:.0f}MB (umbral={MAX_POSTMORTEM_MB}MB) → eliminando para regeneración limpia")
    pm.unlink()
    log("  [FIX-B] ✅ postmortem.csv eliminado — el siguiente ciclo del bot lo regenera sano")
    return True


# ──────────────────────────────────────────────────────────────────────────────
# FIX C: commit y push del fix
# ──────────────────────────────────────────────────────────────────────────────
def commit_fix(descripcion: str) -> bool:
    try:
        subprocess.run(["git", "-C", str(REPO), "add", "-A"], timeout=10, check=True, capture_output=True)
        result = subprocess.run(
            ["git", "-C", str(REPO), "diff", "--cached", "--quiet"],
            timeout=5, capture_output=True
        )
        if result.returncode == 0:
            return False  # nada que commitear

        msg = f"fix(watchdog): {descripcion}"
        subprocess.run(
            ["git", "-C", str(REPO), "commit", "-m", msg],
            timeout=15, check=True, capture_output=True
        )
        # Pull + push con estrategia ours para datos
        subprocess.run(
            ["git", "-C", str(REPO), "pull", "--rebase", "-X", "ours", "origin", "main"],
            timeout=60, capture_output=True
        )
        subprocess.run(
            ["git", "-C", str(REPO), "push", "origin", "main"],
            timeout=60, check=True, capture_output=True
        )
        log(f"  [COMMIT] ✅ '{msg}' pusheado a origin")
        return True
    except Exception as e:
        log(f"  [COMMIT] Error en git: {e}")
        return False


# ──────────────────────────────────────────────────────────────────────────────
# BUCLE PRINCIPAL
# ──────────────────────────────────────────────────────────────────────────────
def main():
    log("=== pipeline_watchdog arrancado ===")
    consecutivos_silencio = 0

    while True:
        try:
            hoy_csv = pred_csv_hoy()
            age = segundos_desde_update(hoy_csv)

            # ── Check 1: silence del pipeline ────────────────────────────────
            if age is None:
                log(f"predictions CSV de hoy no existe: {hoy_csv.name}")
                consecutivos_silencio += 1
            elif age > MAX_PRED_SILENCE:
                consecutivos_silencio += 1
                log(f"⚠ predictions sin actualizar hace {age:.0f}s (umbral={MAX_PRED_SILENCE}s) — check #{consecutivos_silencio}")
            else:
                if consecutivos_silencio > 0:
                    log(f"✅ predictions vuelve a actualizarse (silencio={consecutivos_silencio} ciclos)")
                consecutivos_silencio = 0

            # ── Check 2: si hay silencio, buscar error en log ─────────────────
            if consecutivos_silencio >= 2:  # 2 ciclos = ~4 min de silencio
                texto_log = ultimos_errores_log(300)
                tb = extraer_traceback(texto_log)

                if "UnboundLocalError" in tb or "UnboundLocalError" in texto_log[-3000:]:
                    log("🔴 UnboundLocalError detectado en fast.log → aplicando FIX-A")
                    if fix_unbound_local(tb or ultimos_errores_log(500)):
                        commit_fix("UnboundLocalError eliminado (variable usada antes de asignarse)")
                        consecutivos_silencio = 0
                    else:
                        log("  FIX-A no pudo aplicarse automáticamente — requiere revisión manual")

                elif "429" in texto_log[-3000:] or "Too Many Requests" in texto_log[-3000:]:
                    log("🟡 429 Too Many Requests detectado — throttle debería estar activo, revisando shadow_resolve.py")
                    # Verificar que el throttle está presente
                    resolve_src = (REPO / "shadow_resolve.py").read_text()
                    if "time.sleep" not in resolve_src or "workers: int = 3" not in resolve_src:
                        log("  Throttle faltante detectado → requiere fix manual (cloud agent lo corregirá)")
                    else:
                        log("  Throttle ya está presente — los 429 son transitorios, esperando")

                elif tb:
                    log(f"🔴 Error en fast.log (no reconocido):\n{tb[:300]}")
                    log("  Bug desconocido — cloud agent lo revisará en próxima hora")

            # ── Check 3: postmortem.csv bloat ─────────────────────────────────
            if fix_postmortem_bloat():
                commit_fix("postmortem.csv bloat eliminado (checkpoint roto)")

        except Exception as e:
            log(f"Error en watchdog loop: {e}")

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
