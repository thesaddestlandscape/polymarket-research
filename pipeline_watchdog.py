"""
pipeline_watchdog.py — Guardián local del pipeline. Corre en screen -S watchdog.

Intervalo: 120s (2 minutos).
Checks de sintaxis periódicos: cada 5 ciclos (~10 min).

Checks en cada ciclo:
  1. klines_HOY.json actualizado en los últimos 5 min (proxy del fast loop vivo;
     predictions_HOY.csv no sirve porque el dedup diario lo deja sin filas
     nuevas en ciclos enteros aunque el loop esté sano) + logs/live.log
     actualizado (klines se escribe aunque live_trade.py esté roto — corre
     antes e independiente en run_fast.sh — así que hace falta un check
     propio para no quedar ciego a fallos en el camino del dinero real)
  2. Screens fast/slow/control corriendo → restart si caídas
  3. Errores en fast.log → patrón conocido → fix automático
  4. postmortem.csv > 50MB → regenerar
  5. fast.log/live.log/slow.log > 200MB → rotar (keep last 10000 lines) — hasta
     17-Jul solo cubría fast.log (barrido de coherencia: live.log es el log de
     ejecución de dinero real y crecía sin freno desde 25-Jun, 45MB entonces)
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
LOG_LIVE   = REPO / "logs" / "live.log"
LOG_SLOW   = REPO / "logs" / "slow.log"
LOG_WATCH  = REPO / "logs" / "watchdog.log"
DIR_SHADOW = REPO / "data" / "shadow"
DIR_BINANCE = REPO / "data" / "binance"

CHECK_INTERVAL     = 120   # segundos entre ciclos
MAX_PRED_SILENCE   = 300   # sin actualizar predictions → alerta
MAX_POSTMORTEM_MB  = 50    # MB máx postmortem.csv
MAX_LOG_MB         = 200   # MB máx por log (fast/live/slow) antes de rotar
DISK_WARN_PCT      = 85    # % usado → warning
SYNTAX_CHECK_EVERY = 5     # ciclos entre chequeos de sintaxis de todos los scripts

SWITCH_ALERTA_COOLDOWN = 1800  # segundos entre alertas de switch apagado (30 min)
DEADLOCK_ALERTA_COOLDOWN = 1800  # segundos entre alertas de deadlock de bankroll (30 min)
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
    "slow":    f"cd {REPO} && bash run_slow.sh >> logs/slow.log 2>&1",
    "control": f"cd {REPO} && .venv/bin/python live_control.py >> logs/live_control.log 2>&1",
    "dash":    f"cd {REPO} && python3 dashboard_server.py >> logs/dashboard.log 2>&1",
    "pfinish": f"cd {REPO} && .venv/bin/python photo_finish_logger.py >> logs/photo_finish.log 2>&1",
    # ballenas_fast (17-Jul, fusionado desde feat/ballenas-fast-btc15m):
    # ejecutor dedicado de baja latencia BALLENAS_TARDIAS#BTC#15min, DRY_RUN=True
    # (no toca dinero). Screen de proceso único, mismo patrón que pfinish.
    "ballenas_fast": f"cd {REPO} && .venv/bin/python ballenas_executor_btc15m.py >> logs/ballenas_fast.log 2>&1",
    # ballenas_5m (18-Jul): ejecutor de baja latencia BALLENAS_TARDIAS#{ETH,SOL,XRP}#5min,
    # DRY_RUN=True, proceso separado de ballenas_fast (BTC15m, live) para no
    # mezclar blast radius. Ver /root/.claude/plans/ethereal-dazzling-thacker.md
    "ballenas_5m": f"cd {REPO} && .venv/bin/python ballenas_executor_5min.py >> logs/ballenas_5m.log 2>&1",
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


def klines_json_hoy() -> Path:
    return DIR_BINANCE / f"klines_{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.json"


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
                for name in ["fast", "slow", "control", "dash", "pfinish", "ballenas_fast", "ballenas_5m"]}
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
# CHECK: deploy obsoleto — screen corriendo código MÁS VIEJO que el fichero en
# disco. Los loops (run_fast/run_slow) son `while true` de larga duración y los
# screens python (control/dash/pfinish) son procesos únicos: NINGUNO relee su
# fichero de entrada, así que un fix commiteado queda INACTIVO hasta reiniciar la
# screen. Pasó el 2026-07-06 (run_slow.sh con --autostash committeado pero el
# proceso seguía con el código del 01-Jul → rebase-fails persistían). Verificar
# el DEPLOY, no fiarse del commit. Solo ALERTA: reiniciar `fast` (dinero real) es
# decisión deliberada. Los .py que los loops invocan cada ciclo como subproceso
# (live_trade.py, shadow_predict.py…) SÍ se recargan → no aplican aquí.
# ──────────────────────────────────────────────────────────────────────────────
def _entrypoint_script(cmd: str) -> str | None:
    """Fichero de entrada de un comando de screen: 'bash run_fast.sh …' → run_fast.sh."""
    m = re.search(r"(\S+\.(?:sh|py))", cmd)
    return m.group(1) if m else None


def check_stale_deploys(screens_up: dict) -> list[str]:
    """Nombres de screen cuyo fichero de entrada en disco es más nuevo que el
    proceso en marcha (deploy no aplicado). Margen 120s para no marcar el propio
    arranque como stale."""
    stale = []
    now = time.time()
    for name, cmd in SCREEN_RESTART.items():
        if not screens_up.get(name):
            continue
        script = _entrypoint_script(cmd)
        if not script:
            continue
        p = REPO / script
        if not p.exists():
            continue
        try:
            r = subprocess.run(["pgrep", "-f", script], capture_output=True,
                               text=True, timeout=5)
            pids = [x for x in r.stdout.split() if x]
            edades = []
            for pid in pids:
                e = subprocess.run(["ps", "-o", "etimes=", "-p", pid],
                                   capture_output=True, text=True, timeout=5)
                try:
                    edades.append(int(e.stdout.strip()))
                except ValueError:
                    pass
            if not edades:
                continue
            proc_start = now - max(edades)          # arranque del proceso más antiguo
            if p.stat().st_mtime > proc_start + 120:
                dm = (p.stat().st_mtime - proc_start) / 60
                stale.append(f"{name} ({script}): disco {dm:.0f} min más nuevo que "
                             f"el proceso — deploy NO aplicado, reinicia la screen")
        except Exception:
            continue
    return stale


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
# FIX C: logs demasiado grandes → rotar (copytruncate in-place: los procesos
# que ya tienen el fd abierto en O_APPEND vía `screen ... >> logs/x.log`
# siguen escribiendo sin reinicio, igual que fast.log desde el origen)
# ──────────────────────────────────────────────────────────────────────────────
def fix_log_size() -> bool:
    rotado_alguno = False
    for logf in (LOG_FAST, LOG_LIVE, LOG_SLOW):
        if not logf.exists():
            continue
        size_mb = logf.stat().st_size / 1_000_000
        if size_mb < MAX_LOG_MB:
            continue
        log(f"  [FIX-C] {logf.name} {size_mb:.0f}MB > {MAX_LOG_MB}MB → rotando (last 10000 lines)")
        try:
            r = subprocess.run(["tail", "-n", "10000", str(logf)],
                               capture_output=True, text=True, timeout=10)
            logf.write_text(r.stdout, encoding="utf-8")
            log(f"  [FIX-C] ✅ {logf.name} rotado")
            rotado_alguno = True
        except Exception as e:
            log(f"  [FIX-C] Error rotando {logf.name}: {e}")
    return rotado_alguno


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
# CHECK 10: Switch OFF durante ventana horaria → alerta Telegram
# ──────────────────────────────────────────────────────────────────────────────
_switch_alerta_ts: float = 0.0  # timestamp del último alerta enviado


def check_switch_ventana() -> None:
    """Alerta por Telegram si el switch live se apaga dentro de una ventana programada."""
    global _switch_alerta_ts
    try:
        from live_guard import en_ventana_horaria, switch_activo
        from shadow_digest import enviar_telegram

        en_v, motivo = en_ventana_horaria()
        switch_on = switch_activo()

        if en_v and not switch_on:
            if time.time() - _switch_alerta_ts > SWITCH_ALERTA_COOLDOWN:
                _switch_alerta_ts = time.time()
                log(f"⚠ Switch OFF durante ventana ({motivo}) — alerta Telegram enviada")
                enviar_telegram(
                    "⚠️ *Switch apagado durante ventana horaria*\n"
                    f"Ventana activa: `{motivo}`\n"
                    "El bot NO está operando. Activa con:\n"
                    "`bash live_switch.sh on`  o  /on por Telegram"
                )
        elif switch_on:
            _switch_alerta_ts = 0.0  # reset cuando vuelve ON
    except Exception as e:
        log(f"  [check-switch] Error: {e}")


# ──────────────────────────────────────────────────────────────────────────────
# CHECK 11: Bankroll en zona muerta de sizing → alerta Telegram
# ──────────────────────────────────────────────────────────────────────────────
# 17-Jul: bankroll_minimo_eur(1.00€) + min_stake_eur(1.05€) exigían
# bankroll>=2.05€ para que CUALQUIER trade fuera viable. El bankroll cruzó
# esa zona a las 06:45 UTC y quedó parado 8h+ generando no_viable_stake/
# senal_caducada en fast.log sin ninguna alerta — el circuit breaker real
# (Freno 1, bankroll_minimo_eur) solo avisa al cruzar el suelo absoluto, no
# esta zona intermedia. Ver project_bankroll_deadlock_stake_17jul (memoria).
_deadlock_alerta_ts: float = 0.0  # timestamp del último alerta enviado


def check_bankroll_deadlock() -> None:
    """Alerta por Telegram si ninguna señal puede ser viable pase lo que
    pase el IC (probado con IC=1.0, el máximo posible) pese a que el switch
    está ON y el circuit breaker real todavía no ha saltado. Reutiliza
    calcular_stake() tal cual (no duplica su lógica de frenos/margen)."""
    global _deadlock_alerta_ts
    try:
        from live_stake import calcular_stake, bankroll_minimo_eur_hoy
        from live_guard import switch_activo
        from shadow_digest import enviar_telegram

        r = calcular_stake(ic=1.0)
        en_deadlock = switch_activo() and not r["viable"] and r["bankroll"] > bankroll_minimo_eur_hoy()

        if en_deadlock:
            if time.time() - _deadlock_alerta_ts > DEADLOCK_ALERTA_COOLDOWN:
                _deadlock_alerta_ts = time.time()
                log(f"⚠ Bankroll en zona muerta de sizing — alerta Telegram enviada. {r['motivo']}")
                enviar_telegram(
                    "⚠️ *Bankroll en zona muerta (deadlock de sizing)*\n"
                    f"{r['motivo']}\n\n"
                    "Switch ON, circuit breaker real sin disparar, pero NINGUNA señal "
                    "puede ser viable pase lo que pase el IC (probado con IC=1.0) — "
                    "el sistema queda parado en silencio (`no_viable_stake`/`senal_caducada` "
                    "repetidos en fast.log).\n"
                    "Necesita recarga de capital o un override puntual "
                    "(`bankroll_minimo_eur_override` / `freno_diario_pct_override` en config_live.json)."
                )
        else:
            _deadlock_alerta_ts = 0.0  # reset al salir de la zona muerta
    except Exception as e:
        log(f"  [check-deadlock] Error: {e}")


# ──────────────────────────────────────────────────────────────────────────────
# BUCLE PRINCIPAL
# ──────────────────────────────────────────────────────────────────────────────
def main():
    log("=== pipeline_watchdog v2 arrancado ===")
    consecutivos_silencio = 0
    screens_caidas_count: dict[str, int] = {}
    stale_deploy_alertado: set = set()
    ciclo = 0

    while True:
        ciclo += 1
        try:
            # ── 1. Fast loop silencio (klines, se escribe cada ciclo pase lo que pase;
            #      predictions.csv NO sirve de proxy porque el dedup diario deja
            #      ciclos enteros sin filas nuevas aunque el loop esté sano) ──────
            hoy_klines = klines_json_hoy()
            age = segundos_desde_update(hoy_klines)
            klines_mal = age is None or age > MAX_PRED_SILENCE
            if age is None:
                log(f"⚠ klines JSON hoy no existe: {hoy_klines.name}")
            elif klines_mal:
                log(f"⚠ fast loop sin actualizar klines {age:.0f}s (umbral={MAX_PRED_SILENCE}s)")

            # ── 1b. live_trade.py silencio — klines se actualiza aunque
            #       live_trade.py esté roto (corre antes e independientemente
            #       en run_fast.sh, con || true), así que un crash sostenido
            #       en el camino del dinero real podía pasar invisible al
            #       check de arriba y nunca disparar el escaneo de tracebacks
            #       de abajo. logs/live.log lo escribe solo live_trade.py.
            age_live = segundos_desde_update(LOG_LIVE)
            live_mal = age_live is None or age_live > MAX_PRED_SILENCE
            if age_live is None:
                log(f"⚠ logs/live.log no existe")
            elif live_mal:
                log(f"⚠ live_trade.py sin actualizar {age_live:.0f}s (umbral={MAX_PRED_SILENCE}s)")

            if klines_mal or live_mal:
                consecutivos_silencio += 1
                log(f"  ciclo silencio #{consecutivos_silencio}")
            else:
                if consecutivos_silencio > 0:
                    log(f"✅ fast loop activo de nuevo (silencio={consecutivos_silencio} ciclos)")
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

            # ── 2b. Deploy obsoleto (fix commiteado pero screen sin reiniciar) ─
            stale = check_stale_deploys(screens)
            stale_ahora = {s.split()[0] for s in stale}
            for msg in stale:
                log(f"⚠ DEPLOY OBSOLETO: {msg}")
            nuevos = stale_ahora - stale_deploy_alertado
            if nuevos:
                try:
                    from shadow_digest import enviar_telegram
                    enviar_telegram(
                        "⚠️ *Deploy obsoleto*\n"
                        + "\n".join(m for m in stale if m.split()[0] in nuevos)
                        + "\n\nReinicia la screen para aplicar el cambio."
                    )
                except Exception:
                    pass
            stale_deploy_alertado = stale_ahora

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

            # ── 10. Switch OFF durante ventana horaria ────────────────────
            check_switch_ventana()

            # ── 11. Bankroll en zona muerta de sizing ──────────────────────
            check_bankroll_deadlock()

        except Exception as e:
            log(f"Error interno watchdog: {e}")

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
