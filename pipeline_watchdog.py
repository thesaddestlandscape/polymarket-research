"""
pipeline_watchdog.py — Guardián local del pipeline. Corre en screen -S watchdog.

Intervalo: 120s (2 minutos).
Checks de sintaxis periódicos: cada 5 ciclos (~10 min).

Checks en cada ciclo:
  1. predictions_HOY.csv actualizado en los últimos 5 min
  2. Screens fast/slow/control corriendo → restart si caídas
  3. Errores en fast.log → patrón conocido → fix automático
  4. postmortem.csv > 50MB → regenerar
  5. fast.log > 200MB → rotar (keep last 10000 lines)
  6. strategy_params.json válido (JSON + estructura)
  7. Disco < 85% libre

Checks cada 5 ciclos (~10 min):
  8. Sintaxis de todos los scripts del pipeline (py_compile)
  9. results.csv recibiendo resoluciones (no colgado en resolve)

Fixes automáticos:
  A. UnboundLocalError (dead code) → eliminar línea + py_compile verify
  B. postmortem.csv bloat → delete (se regenera en siguiente ciclo del bot)
  C. Screen fast/control caída → restart con comando original

NO toca lógica de negocio. Solo bugs obvios y archivos de datos corruptos.
"""

import re
import sys
import time
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO       = Path(__file__).parent
LOG_FAST   = REPO / "logs" / "fast.log"
LOG_WATCH  = REPO / "logs" / "watchdog.log"
DIR_SHADOW = REPO / "data" / "shadow"

CHECK_INTERVAL     = 120   # segundos entre ciclos
MAX_PRED_SILENCE   = 300   # sin actualizar predictions → alerta
MAX_POSTMORTEM_MB  = 50    # MB máx postmortem.csv
MAX_FAST_LOG_MB    = 200   # MB máx fast.log antes de rotar
DISK_WARN_PCT      = 85    # % usado → warning
SYNTAX_CHECK_EVERY = 5     # ciclos entre chequeos de sintaxis de todos los scripts
RESOLVE_LAG_SECS   = 7200  # 2h sin nuevas resoluciones → warning

PIPELINE_SCRIPTS = [
    "shadow_predict.py", "shadow_resolve.py", "shadow_postmortem.py",
    "shadow_resumen.py", "live_trade.py", "live_guard.py", "live_stake.py",
    "fetch_binance_klines.py", "capture_markets.py", "hypothesis_tracker.py",
    "arb_scanner.py", "generate_report.py", "data_quality.py",
]

# Comandos para reiniciar screens críticas si caen
SCREEN_RESTART = {
    "fast":    f"cd {REPO} && bash run_fast.sh >> logs/fast.log 2>&1",
    "control": f"cd {REPO} && .venv/bin/python live_control.py >> logs/live_control.log 2>&1",
}

# Cuando stdout está redirigido (screen >> watchdog.log), print() ya escribe al fichero
# → no duplicar con write directo. Si es TTY (interactivo) → sí escribir al fichero.
_STDOUT_REDIRECTED = not sys.stdout.isatty()


def log(msg: str):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    if not _STDOUT_REDIRECTED:
        with open(LOG_WATCH, "a") as f:
            f.write(line + "\n")


def pred_csv_hoy() -> Path:
    return DIR_SHADOW / f"predictions_{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.csv"


def segundos_desde_update(path: Path) -> float | None:
    if not path.exists():
        return None
    return time.time() - path.stat().st_mtime


def ultimos_errores_log(n_lineas: int = 300) -> str:
    if not LOG_FAST.exists():
        return ""
    try:
        r = subprocess.run(["tail", "-n", str(n_lineas), str(LOG_FAST)],
                           capture_output=True, text=True, timeout=5)
        return r.stdout
    except Exception:
        return ""


def extraer_traceback(texto: str) -> str:
    bloques = texto.split("Traceback")
    if len(bloques) < 2:
        return ""
    ultimo = "Traceback" + bloques[-1]
    lineas = ultimo.split("\n")
    resultado = []
    for l in lineas:
        resultado.append(l)
        if (l and not l.startswith(" ") and not l.startswith("Traceback")
                and not l.startswith("File") and len(resultado) > 3):
            break
    return "\n".join(resultado[:25])


# ──────────────────────────────────────────────────────────────────────────────
# CHECK: screens activas
# ──────────────────────────────────────────────────────────────────────────────
def check_screens() -> dict[str, bool]:
    try:
        r = subprocess.run(["screen", "-ls"], capture_output=True, text=True, timeout=5)
        output = r.stdout + r.stderr
        return {name: (f".{name}\t" in output or f".{name} " in output)
                for name in ["fast", "slow", "control"]}
    except Exception:
        return {}


def restart_screen(name: str) -> bool:
    cmd = SCREEN_RESTART.get(name)
    if not cmd:
        return False
    try:
        subprocess.run(["screen", "-dmS", name, "bash", "-c", cmd],
                       timeout=10, check=True)
        log(f"  [SCREEN] ✅ Screen '{name}' reiniciada")
        return True
    except Exception as e:
        log(f"  [SCREEN] Error reiniciando '{name}': {e}")
        return False


# ──────────────────────────────────────────────────────────────────────────────
# CHECK: sintaxis de todos los scripts del pipeline
# ──────────────────────────────────────────────────────────────────────────────
def syntax_check_all() -> list[str]:
    rotos = []
    for nombre in PIPELINE_SCRIPTS:
        script = REPO / nombre
        if not script.exists():
            continue
        r = subprocess.run([sys.executable, "-m", "py_compile", str(script)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            error = r.stderr.strip().split("\n")[-1][:120]
            rotos.append(f"{nombre}: {error}")
    return rotos


# ──────────────────────────────────────────────────────────────────────────────
# CHECK: disco
# ──────────────────────────────────────────────────────────────────────────────
def check_disk_space():
    try:
        r = subprocess.run(["df", "-h", "/"], capture_output=True, text=True, timeout=5)
        for line in r.stdout.split("\n")[1:]:
            parts = line.split()
            if len(parts) >= 5:
                pct = int(parts[4].rstrip("%"))
                if pct >= DISK_WARN_PCT:
                    log(f"  ⚠ DISCO: {pct}% usado ({parts[2]} de {parts[1]}) — liberar espacio")
    except Exception:
        pass


# ──────────────────────────────────────────────────────────────────────────────
# CHECK: strategy_params.json integridad
# ──────────────────────────────────────────────────────────────────────────────
def check_strategy_params() -> bool:
    p = DIR_SHADOW / "strategy_params.json"
    if not p.exists():
        log("  ⚠ strategy_params.json no existe — bot operando sin parámetros")
        return False
    try:
        data = json.loads(p.read_text())
        if "estrategias" not in data:
            log("  ⚠ strategy_params.json sin clave 'estrategias' — estructura inválida")
            return False
        return True
    except json.JSONDecodeError as e:
        log(f"  🔴 strategy_params.json JSON inválido: {e} — requiere fix manual urgente")
        return False


# ──────────────────────────────────────────────────────────────────────────────
# CHECK: results.csv recibiendo resoluciones
# ──────────────────────────────────────────────────────────────────────────────
def check_results_growing():
    p = DIR_SHADOW / "results.csv"
    if not p.exists():
        return
    age = time.time() - p.stat().st_mtime
    if age > RESOLVE_LAG_SECS:
        log(f"  ⚠ results.csv sin actualizar hace {age/3600:.1f}h — shadow_resolve podría estar colgado")


# ──────────────────────────────────────────────────────────────────────────────
# FIX A: UnboundLocalError — variable usada antes de asignarse (dead code)
# ──────────────────────────────────────────────────────────────────────────────
def fix_unbound_local(tb: str) -> bool:
    m = re.search(r"cannot access local variable '(\w+)' where it is not associated", tb)
    if not m:
        return False
    var = m.group(1)

    file_match = re.search(r'File "([^"]+\.py)", line (\d+)', tb)
    if not file_match:
        return False
    script_path = Path(file_match.group(1))
    if not script_path.exists():
        script_path = REPO / script_path.name
    if not script_path.exists():
        log(f"  [FIX-A] No encuentro el script: {file_match.group(1)}")
        return False

    linea_error = int(file_match.group(2))
    log(f"  [FIX-A] UnboundLocalError: var='{var}' en {script_path.name}:{linea_error}")

    contenido = script_path.read_text(encoding="utf-8")
    lineas = contenido.split("\n")

    inicio = max(0, linea_error - 50)
    candidatas_uso = []
    definicion_encontrada = False
    for i in range(inicio, linea_error):
        l = lineas[i]
        stripped = l.strip()
        if re.match(rf"^\s*{re.escape(var)}\s*=", l):
            definicion_encontrada = True
        elif var in l and not definicion_encontrada:
            if re.match(r"^\s*\w+\s*=\s*.+", stripped):
                candidatas_uso.append(i)

    if not candidatas_uso:
        log(f"  [FIX-A] Línea problemática no localizada automáticamente en {script_path.name}")
        return False

    linea_idx = candidatas_uso[-1]
    var_asig = re.match(r"^\s*(\w+)\s*=", lineas[linea_idx].strip())
    if not var_asig:
        return False
    var_asig = var_asig.group(1).strip()

    usos_posteriores = any(
        var_asig in lineas[j]
        for j in range(linea_idx + 1, min(linea_idx + 20, len(lineas)))
        if not lineas[j].strip().startswith("#")
        and f"{var_asig} =" not in lineas[j]
    )
    if usos_posteriores:
        log(f"  [FIX-A] '{var_asig}' se usa después → no es dead code, no elimino")
        return False

    log(f"  [FIX-A] Eliminando línea {linea_idx+1}: {lineas[linea_idx].strip()[:80]}")
    backup = script_path.with_suffix(".py.bak")
    backup.write_text(contenido, encoding="utf-8")
    del lineas[linea_idx]
    script_path.write_text("\n".join(lineas), encoding="utf-8")

    r = subprocess.run([sys.executable, "-m", "py_compile", str(script_path)],
                       capture_output=True, text=True)
    if r.returncode != 0:
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
    log(f"  [FIX-B] postmortem.csv {size_mb:.0f}MB > {MAX_POSTMORTEM_MB}MB → eliminando")
    pm.unlink()
    log("  [FIX-B] ✅ postmortem.csv eliminado — siguiente ciclo lo regenera sano")
    return True


# ──────────────────────────────────────────────────────────────────────────────
# FIX C: fast.log demasiado grande → rotar
# ──────────────────────────────────────────────────────────────────────────────
def fix_log_size() -> bool:
    if not LOG_FAST.exists():
        return False
    size_mb = LOG_FAST.stat().st_size / 1_000_000
    if size_mb < MAX_FAST_LOG_MB:
        return False
    log(f"  [FIX-C] fast.log {size_mb:.0f}MB > {MAX_FAST_LOG_MB}MB → rotando (last 10000 lines)")
    try:
        r = subprocess.run(["tail", "-n", "10000", str(LOG_FAST)],
                           capture_output=True, text=True, timeout=10)
        LOG_FAST.write_text(r.stdout, encoding="utf-8")
        log("  [FIX-C] ✅ fast.log rotado")
        return True
    except Exception as e:
        log(f"  [FIX-C] Error rotando fast.log: {e}")
        return False


# ──────────────────────────────────────────────────────────────────────────────
# GIT: commit y push del fix
# ──────────────────────────────────────────────────────────────────────────────
def commit_fix(descripcion: str) -> bool:
    try:
        subprocess.run(["git", "-C", str(REPO), "add", "-A"],
                       timeout=10, check=True, capture_output=True)
        r = subprocess.run(["git", "-C", str(REPO), "diff", "--cached", "--quiet"],
                           timeout=5, capture_output=True)
        if r.returncode == 0:
            return False

        subprocess.run(
            ["git", "-C", str(REPO), "commit", "-m", f"fix(watchdog): {descripcion}"],
            timeout=15, check=True, capture_output=True
        )
        subprocess.run(
            ["git", "-C", str(REPO), "fetch", "origin"],
            timeout=30, capture_output=True
        )
        subprocess.run(
            ["git", "-C", str(REPO), "merge", "origin/main", "-X", "ours", "--no-edit"],
            timeout=30, capture_output=True
        )
        subprocess.run(
            ["git", "-C", str(REPO), "push", "origin", "main"],
            timeout=60, check=True, capture_output=True
        )
        log(f"  [GIT] ✅ fix(watchdog): {descripcion}")
        return True
    except Exception as e:
        log(f"  [GIT] Error en commit/push: {e}")
        return False


# ──────────────────────────────────────────────────────────────────────────────
# BUCLE PRINCIPAL
# ──────────────────────────────────────────────────────────────────────────────
def main():
    log("=== pipeline_watchdog v2 arrancado ===")
    consecutivos_silencio = 0
    screens_caidas_count: dict[str, int] = {}
    ciclo = 0

    while True:
        ciclo += 1
        try:
            # ── 1. Predictions CSV silencio ───────────────────────────────────
            hoy_csv = pred_csv_hoy()
            age = segundos_desde_update(hoy_csv)
            if age is None:
                log(f"⚠ predictions CSV hoy no existe: {hoy_csv.name}")
                consecutivos_silencio += 1
            elif age > MAX_PRED_SILENCE:
                consecutivos_silencio += 1
                log(f"⚠ predictions sin actualizar {age:.0f}s (umbral={MAX_PRED_SILENCE}s) — ciclo silencio #{consecutivos_silencio}")
            else:
                if consecutivos_silencio > 0:
                    log(f"✅ predictions activa de nuevo (silencio={consecutivos_silencio} ciclos)")
                consecutivos_silencio = 0

            # ── 2. Screens health ─────────────────────────────────────────────
            screens = check_screens()
            for name, running in screens.items():
                if running:
                    screens_caidas_count[name] = 0
                else:
                    cnt = screens_caidas_count.get(name, 0) + 1
                    screens_caidas_count[name] = cnt
                    log(f"⚠ Screen '{name}' no encontrada (ausente #{cnt})")
                    if name in SCREEN_RESTART:
                        log(f"  → Reiniciando screen '{name}'")
                        restart_screen(name)

            # ── 3. Si hay silencio, buscar errores en fast.log ────────────────
            if consecutivos_silencio >= 2:
                texto = ultimos_errores_log(400)
                tb = extraer_traceback(texto)
                texto_reciente = texto[-4000:]

                if "UnboundLocalError" in texto_reciente:
                    log("🔴 UnboundLocalError en fast.log → aplicando FIX-A")
                    if fix_unbound_local(tb or ultimos_errores_log(600)):
                        commit_fix("UnboundLocalError eliminado (dead code)")
                        consecutivos_silencio = 0
                    else:
                        log("  FIX-A no aplicable automáticamente — requiere revisión manual")

                elif "SyntaxError" in texto_reciente:
                    m = re.search(r'File "([^"]+)", line (\d+)', texto_reciente)
                    donde = f"{m.group(1)}:{m.group(2)}" if m else "desconocido"
                    log(f"🔴 SyntaxError en {donde} — requiere fix manual")

                elif "ModuleNotFoundError" in texto_reciente or "ImportError" in texto_reciente:
                    m = re.search(r"No module named '([^']+)'", texto_reciente)
                    modulo = m.group(1) if m else "desconocido"
                    log(f"🔴 ImportError: módulo '{modulo}' faltante — instalar con pip")

                elif "NameError" in texto_reciente:
                    m = re.search(r"name '(\w+)' is not defined", texto_reciente)
                    nombre = m.group(1) if m else "?"
                    log(f"🔴 NameError: '{nombre}' no definido — revisar imports y scope")

                elif "AttributeError" in texto_reciente:
                    m = re.search(r"AttributeError: (.{0,100})", texto_reciente)
                    msg = m.group(1) if m else ""
                    log(f"🔴 AttributeError: {msg} — revisar tipo de objeto")

                elif "KeyError" in texto_reciente:
                    m = re.search(r"KeyError: (.{0,60})", texto_reciente)
                    key = m.group(1) if m else "?"
                    log(f"🔴 KeyError: {key} — clave faltante en dict/CSV")

                elif "429" in texto_reciente or "Too Many Requests" in texto_reciente:
                    resolve_src = (REPO / "shadow_resolve.py").read_text(encoding="utf-8")
                    if "time.sleep" not in resolve_src or "workers: int = 3" not in resolve_src:
                        log("🟡 429: throttle faltante en shadow_resolve.py — requiere fix manual")
                    else:
                        log("🟡 429 transitorio (throttle activo) — esperando")

                elif tb:
                    tipo = tb.split("\n")[-1].split(":")[0].strip() if "\n" in tb else "Error"
                    log(f"🔴 {tipo} en fast.log:\n  {tb.split(chr(10))[-1][:150]}")

            # ── 4. postmortem.csv bloat ───────────────────────────────────────
            if fix_postmortem_bloat():
                commit_fix("postmortem.csv bloat eliminado")

            # ── 5. fast.log rotación ──────────────────────────────────────────
            fix_log_size()

            # ── 6. strategy_params.json ───────────────────────────────────────
            check_strategy_params()

            # ── 7. Disco ──────────────────────────────────────────────────────
            check_disk_space()

            # ── 8+9. Checks periódicos cada SYNTAX_CHECK_EVERY ciclos ─────────
            if ciclo % SYNTAX_CHECK_EVERY == 0:
                rotos = syntax_check_all()
                if rotos:
                    log(f"🔴 SyntaxError en {len(rotos)} script(s):")
                    for r in rotos:
                        log(f"  → {r}")
                else:
                    log(f"✅ Sintaxis OK ({len(PIPELINE_SCRIPTS)} scripts — ciclo {ciclo})")

                check_results_growing()

        except Exception as e:
            log(f"Error interno watchdog: {e}")

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
