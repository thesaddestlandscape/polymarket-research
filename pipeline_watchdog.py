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
REPO_WEATHER = Path("/root/polymarket-weather")
LOG_FAST   = REPO / "logs" / "fast.log"
LOG_LIVE   = REPO / "logs" / "live.log"
LOG_SLOW   = REPO / "logs" / "slow.log"
LOG_WATCH  = REPO / "logs" / "watchdog.log"
DIR_SHADOW = REPO / "data" / "shadow"
DIR_BINANCE = REPO / "data" / "binance"

CHECK_INTERVAL     = 120   # segundos entre ciclos
MAX_PRED_SILENCE   = 300   # sin actualizar predictions → alerta
MAX_POSTMORTEM_MB  = 50    # MB máx postmortem.csv
MAX_LOG_MB         = 80    # MB máx por log antes de rotar (05-Sep: bajado de 200 a 80 —
# disco al 93%, 13 logs de ejecutores/vigías habían crecido a 95-155MB sin rotar
# nunca por quedarse justo debajo del umbral viejo; fix_log_size() ya cubre TODOS
# los logs/*.log via glob desde 18-Ago, el bug real era el umbral, no el alcance)
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
    # mantenimiento (18-Ago): resolve/postmortem/resumen/git-batch,
    # desacoplado de run_fast.sh para que predict/live_trade nunca se
    # bloqueen -- ver run_fast_mantenimiento.sh. Reinicio real vía
    # restart_screen()::name=="mantenimiento" más abajo (llama a
    # restart_mantenimiento_seguro.sh, mismo patrón single-point-of-truth
    # que 'fast') -- este comando de aquí NUNCA se ejecuta, solo existe
    # para que la clave aparezca en SCREEN_RESTART y el chequeo genérico
    # `if name in SCREEN_RESTART` de check_screens() dispare la llamada a
    # restart_screen(). Sin nice: alimenta strategy_params.json, que
    # live_trade.py consume, así que necesita correr con prontitud.
    "mantenimiento": f"cd {REPO} && bash run_fast_mantenimiento.sh >> logs/fast.log 2>&1",
    "control": f"cd {REPO} && .venv/bin/python live_control.py >> logs/live_control.log 2>&1",
    # dash (24-Ago): fusiona dashboard_server.py (8888) + sports_dashboard_
    # server.py (8890, antes screen "dash-sports") en un solo proceso -- ver
    # dashboards_consolidado.py. Mismo patrón que el resto de fusiones de
    # esta lista, ninguno mueve dinero real (HTTP de solo lectura).
    "dash":    f"cd {REPO} && nice -n 10 .venv/bin/python dashboards_consolidado.py >> logs/dashboards_consolidado.log 2>&1",
    # observadores (05-Ago): fusión de 10 procesos observacionales/FASE0
    # (pfinish, favultsec, puntoconf, ressniper, p22fase0, boxbuilder,
    # solcontrario5m, xrpcontrario15m, favcontraria, fav5malt) en UNO solo,
    # cada uno en su propio hilo -- ver observadores_fase0.py. Decisión
    # explícita Javi: el bankroll no permite subir el VPS, así que se
    # reduce el número de procesos en vez del coste. Ninguno de los 10
    # ejecuta dinero real ni cambia de lógica (cero cambios en los 10
    # ficheros originales, solo cambia el proceso que los corre). Ver
    # project_push_roto_carga_cpu_resuelto_05ago / project_consolidacion_
    # observadores_fase0_05ago en memoria.
    "observadores": f"cd {REPO} && nice -n 10 .venv/bin/python observadores_fase0.py >> logs/observadores_fase0.log 2>&1",
    # fetchers (07-Ago): fusión de 4 fetchers de datos externos (chainlink,
    # liqs, libroambos, polyactivity -- historial de cada uno en los
    # comentarios de fetchers_fase0.py::FETCHERS) en UN SOLO proceso, cada
    # uno en su propio hilo -- mismo patrón que observadores_fase0.py
    # (05-Ago) y ejecutores_dryrun_fase0.py (06-Ago). Decisión explícita
    # Javi: seguir reduciendo procesos persistentes en vez de subir el VPS.
    # Ninguno de los 4 ejecuta dinero real ni cambia de lógica (cero cambios
    # en los 4 ficheros originales, solo cambia el proceso que los corre).
    "fetchers": f"cd {REPO} && nice -n 10 .venv/bin/python fetchers_fase0.py >> logs/fetchers_fase0.log 2>&1",
    # ejeclive (10-Ago): consolida los 4 ejecutores de baja latencia con
    # dinero real (ballenas_fast=ballenas_executor_btc15m.py, ballenas_5m=
    # ballenas_executor_5min.py, favaltaconv=favorito_altaconviccion_
    # executor_15min.py, favbtc60mno=favorito_confirmado_btc60min_buyno_
    # executor.py -- las 4 screens de antes) en UN SOLO proceso
    # (executores_live_consolidado.py). Motivo: los 4 abrían su propia
    # conexión websocket independiente a ballenas_firehose_cache (RTDS),
    # cada una parseando el stream completo por separado -- 4 conexiones/
    # 4x parseo para el mismo dato exacto. Como iniciar() ya es idempotente
    # por proceso, compartir uno colapsa 3 de las 4 conexiones a no-ops
    # automáticos, sin tocar ninguna línea de lógica de los 4 ejecutores
    # (el runner solo parchea log() para prefijar el origen y lanza cada
    # main() en su propio hilo). Si CUALQUIERA de los 4 muere, el proceso
    # entero se cierra (os._exit) para forzar un restart limpio -- evita
    # duplicar hilos internos de un módulo reiniciado a medias (riesgo de
    # doble-ejecución con dinero real). Contrapartida explícita: un bug en
    # cualquiera de los 4 ahora tumba a los 4 durante el reinicio (antes
    # solo tumbaba al suyo) -- a cambio de ~75% menos conexiones/CPU. Ver
    # executores_live_consolidado.py y project_consolidacion_4_ejecutores_
    # pendiente_corte_10ago en memoria.
    "ejeclive": f"cd {REPO} && .venv/bin/python executores_live_consolidado.py >> logs/ejecutores_live_consolidado.log 2>&1",
    # ejecdryrun (06-Ago): consolida 7 ejecutores DRY_RUN de baja latencia
    # (ballenas_15m, fav15mexec, fav60mexec, gbmlate15m, updowngbmtardio,
    # walletmirror, wmexec -- historial completo de cada uno en sus propios
    # commits de creación) en UN SOLO proceso con un hilo cada uno, mismo
    # patrón que observadores_fase0.py (05-Ago). Alivia la sobresuscripción
    # de CPU sin tocar dinero real -- los 4 ejecutores de dinero real viven
    # ahora en "ejeclive" (10-Ago, ver arriba), ya no en 4 screens propias.
    # Ver ejecutores_dryrun_fase0.py y project_cpu_consolidacion_pendiente_
    # 05ago en memoria.
    "ejecdryrun": f"cd {REPO} && nice -n 10 .venv/bin/python ejecutores_dryrun_fase0.py >> logs/ejecutores_dryrun_fase0.log 2>&1",
    # walletmirror (11-Ago): wallet_mirror_executor_dryrun.py pasó a
    # DRY_RUN=False (SEGUIR#BTC#5min#grande, aprobado Javi) -- sacado de
    # "ejecdryrun" (exige DRY_RUN=True en todos sus módulos) a su propia
    # screen, dinero real, sin nice (mismo trato que ejeclive).
    "walletmirror": f"cd {REPO} && .venv/bin/python wallet_mirror_executor_dryrun.py >> logs/wallet_mirror_executor.log 2>&1",
    # precierre (05-Sep): resolution_sniper_precierre_executor.py, DRY_RUN=True
    # -- ejecutor de baja latencia con camino crítico propio (nunca pasa por
    # _ejecutar_orden_polymarket, ver docstring del propio módulo), presupuesto
    # de 2s a offset=-2s del cierre nominal. Screen PROPIA (no en "ejecdryrun")
    # a propósito: comparte proceso/GIL con otros 7 hilos DRY_RUN metería
    # jitter justo en la medición de latencia real que este ejecutor existe
    # para validar antes de plantear DRY_RUN=False. Sin nice -- aunque hoy no
    # mueve dinero, su propósito es medir el peor caso de latencia real, y
    # nice reduciría prioridad justo en el instante que importa medir bien.
    "precierre": f"cd {REPO} && .venv/bin/python resolution_sniper_precierre_executor.py >> logs/resolution_sniper_precierre_executor.log 2>&1",
    # vigiasfreq (17-Ago): consolida 17 scripts de un solo disparo que
    # corrían vía cron cada 5-60min (~130 arranques de intérprete/hora
    # dispersos: vigia_calidad_datos, vigia_ballenas_snapshot_freshness,
    # vigia_nested_arb_gate, resuelve_ballenas_5min/15min, wallet_mirror_
    # sniper --resolver, live_balance, vigia_carga_sistema, vigia_wallet_
    # mirror_postfix, fetch_binance_perp_cvd_oi, vigia_ballenas_5min_
    # fillability, vigia_ballenas_bypass, vigia_causal_vs_fillable,
    # vigia_ballenas_cobertura, shadow_pnl_fiel, vigia_micro_bucket_kill_
    # switch, vigia_gate_bucket_wallet_mirror) en UN SOLO proceso con
    # scheduler interno (tick 20s, cada tarea con su propio intervalo
    # exacto al de su cron retirado) -- mismo patrón que observadores_
    # fase0.py (05-Ago) / vigias_horarios_fase0.py (11-Ago). Origen:
    # vigia_carga_sistema.py llevaba todo el día oscilando anomalo=True
    # por sobresuscripción de CPU en 2 cores. Ninguno de los 17 ejecuta
    # dinero real ni cambia de lógica -- cero cambios en los 17 ficheros
    # originales, solo cambia el proceso/cadencia que los dispara.
    # nested_arb_scanner.py (cadencia 1min, la más fina) se deja fuera a
    # propósito, sigue en su cron propio. Ver vigias_frecuentes_fase0.py.
    "vigiasfreq": f"cd {REPO} && nice -n 10 .venv/bin/python vigias_frecuentes_fase0.py >> logs/vigias_frecuentes_fase0.log 2>&1",
    # dash-sports: 24-Ago, fusionada dentro de "dash" (dashboards_consolidado.py)
    # -- ver esa entrada arriba y SCREENS_RETIRADAS abajo.
    # 20-Ago: sports-mirror + sports-ws fusionadas en sports_fase0_consolidado.py
    # (barrido de salud diaria, load5 sostenido ~8 en 2 cores, ratio~4x) --
    # mismo patrón que ejecutores_dryrun_fase0.py/observadores_fase0.py, ver
    # docstring de ese fichero para el razonamiento completo. weather-mirror
    # queda FUERA a propósito (repo independiente /root/polymarket-weather,
    # CLAUDE.md prohíbe mezclar); wallet_mirror_executor_dryrun.py (crypto,
    # screen walletmirror) también queda fuera -- DRY_RUN=False, dinero real.
    "sportsfase0": f"cd {REPO} && nice -n 10 .venv/bin/python sports_fase0_consolidado.py >> logs/sports_fase0_consolidado.log 2>&1",
    # 20-Ago: nested_arb_scanner.py sale de su cron '* * * * *' (flock) a
    # proceso persistente propio -- NO se funde con vigias_frecuentes_fase0.py
    # (cadencia 1min más sensible que sus hermanos ahí, ver docstring de
    # nested_arb_loop.py). Puramente observacional, sin dinero real.
    "nestedarb": f"cd {REPO} && nice -n 10 .venv/bin/python nested_arb_loop.py >> logs/nested_arb_loop.log 2>&1",
    "dash-weather": f"cd {REPO_WEATHER} && nice -n 10 .venv/bin/python dashboard_server.py >> logs/dashboard-weather.log 2>&1",
    "weather-mirror": f"cd {REPO_WEATHER} && nice -n 10 .venv/bin/python weather_wallet_mirror_sniper.py >> logs/weather_wallet_mirror_sniper.log 2>&1",
    "weather-ws": f"cd {REPO_WEATHER} && nice -n 10 .venv/bin/python weather_activity_ws.py >> logs/weather_activity_ws.log 2>&1",
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


# 18-Ago (/code-review, hallazgo real): logs/fast.log pasó de ser el log
# de UN SOLO proceso a ser compartido por 'fast' (run_fast.sh) Y
# 'mantenimiento' (run_fast_mantenimiento.sh, desacoplado el mismo día --
# comparte el fichero a propósito, ver docstring ahí). El diagnóstico de
# silencio de más abajo (consecutivos_silencio, basado SOLO en klines/
# live.log, ambos exclusivos de 'fast') seguía correcto, pero
# extraer_traceback() tomaba ciegamente el ÚLTIMO traceback del tail
# compartido -- si 'mantenimiento' loguea un error real casi a la vez que
# 'fast' se queda en silencio por otra causa, FIX-A podía aplicarse sobre
# el traceback EQUIVOCADO (de shadow_postmortem.py, no de shadow_predict.py/
# live_trade.py), retrasando el diagnóstico real del loop de dinero real.
_SCRIPTS_FAST = ("fetch_binance_klines.py", "shadow_predict.py", "live_trade.py")


def extraer_traceback(texto: str, scripts_permitidos: tuple[str, ...] | None = None) -> str:
    """Devuelve el ÚLTIMO traceback del texto cuyo PUNTO DE ENTRADA (la
    primera línea "File ..." del bloque, el script invocado directamente
    por `$PYTHON script.py >> LOG`, no cualquier módulo importado dentro)
    esté en `scripts_permitidos` -- None desactiva el filtro (comportamiento
    original, usado para diagnósticos que no distinguen proceso).

    18-Ago (2º /code-review, hallazgo real): la v1 de este filtro comprobaba
    si CUALQUIER línea del bloque mencionaba un script permitido -- pero
    shadow_resolve.py (que corre en 'mantenimiento') importa live_trade y
    llama a live_trade._ejecutar_venta_temprana(), así que un traceback
    originado en shadow_resolve.py con una llamada a esa función también
    contenía "live_trade.py" en una línea intermedia y colaba el filtro.
    La primera línea "File ..." es siempre el script que arrancó la
    ejecución (frame más externo) -- ESA es la que identifica el proceso
    real, no cualquier import que aparezca más abajo en la pila."""
    bloques = texto.split("Traceback")
    for bloque in reversed(bloques[1:]):
        candidato = "Traceback" + bloque
        if scripts_permitidos is not None:
            m = re.search(r'File "([^"]+)"', candidato)
            if not m or not any(s in m.group(1) for s in scripts_permitidos):
                continue
        lineas = candidato.split("\n")
        resultado = []
        for l in lineas:
            resultado.append(l)
            if (l and not l.startswith(" ") and not l.startswith("Traceback")
                    and not l.startswith("File") and len(resultado) > 3):
                break
        return "\n".join(resultado[:25])
    return ""


# ──────────────────────────────────────────────────────────────────────────────
# CHECK: screens activas
# ──────────────────────────────────────────────────────────────────────────────
# Screens retiradas por fusión en observadores_fase0.py (05-Ago) -- NINGUNA
# de estas debe existir nunca. Si aparece, es un duplicado escribiendo las
# mismas filas que su hilo dentro de "observadores" (pasó de verdad el
# 05-Ago: pfinish/favultsec revivieron solas ~12h después de matarlas a
# mano, origen exacto sin confirmar -- posible rutina cloud/agente leyendo
# el `screen -dmS <nombre> ...` que estos 10 scripts tenían documentado en
# su propio docstring, ya corregido). Defensa activa: matarlas en cuanto
# aparezcan, cada ciclo, venga de donde venga.
SCREENS_RETIRADAS = {
    "pfinish", "favultsec", "puntoconf", "ressniper", "p22fase0",
    "boxbuilder", "solcontrario5m", "xrpcontrario15m", "favcontraria",
    "fav5malt",
    # 07-Ago: fusionadas en "fetchers" (fetchers_fase0.py) -- ver SCREEN_RESTART.
    "chainlink", "polyactivity", "liqs", "libroambos",
    # 20-Ago: fusionadas en "sportsfase0" (sports_fase0_consolidado.py) -- ver SCREEN_RESTART.
    "sports-mirror", "sports-ws",
    # 24-Ago: fusionada en "dash" (dashboards_consolidado.py) -- ver SCREEN_RESTART.
    "dash-sports",
}


def kill_screens_retiradas() -> list[str]:
    """Mata cualquier screen de SCREENS_RETIRADAS que esté viva. Devuelve
    los nombres matados (vacío si no había ninguna) -- llamar cada ciclo,
    es barato (un solo `screen -ls`)."""
    try:
        r = subprocess.run(["screen", "-ls"], capture_output=True, text=True, timeout=5)
        output = r.stdout + r.stderr
    except Exception:
        return []
    matadas = []
    for nombre in SCREENS_RETIRADAS:
        if f".{nombre}\t" in output or f".{nombre} " in output:
            try:
                subprocess.run(["screen", "-S", nombre, "-X", "quit"], timeout=5)
                matadas.append(nombre)
            except Exception as e:
                log(f"  [SCREENS_RETIRADAS] error matando '{nombre}': {e}")
    return matadas


def check_screens() -> dict[str, bool]:
    try:
        r = subprocess.run(["screen", "-ls"], capture_output=True, text=True, timeout=5)
        output = r.stdout + r.stderr
        return {name: (f".{name}\t" in output or f".{name} " in output)
                for name in ["fast", "slow", "mantenimiento", "control", "dash", "observadores", "ejeclive", "fetchers", "ejecdryrun", "walletmirror", "vigiasfreq", "precierre",
                              "dash-weather", "sportsfase0", "weather-mirror", "weather-ws"]}
    except Exception:
        return {}


def _sesiones_con_nombre(name: str) -> list[str]:
    """IDs exactos ('<pid>.<name>') de todas las screens vivas con ese nombre.

    'screen -S <name> -X quit' es ambiguo (y no hace nada) en cuanto hay 2+
    sesiones con el mismo nombre -- hay que apuntar al <pid>.<name> exacto de
    cada una para poder limpiarlas todas antes de spawnear una nueva.
    """
    try:
        r = subprocess.run(["screen", "-ls"], capture_output=True, text=True, timeout=5)
        out = r.stdout + r.stderr
    except Exception:
        return []
    sesiones = []
    for line in out.splitlines():
        line = line.strip()
        primer_campo = line.split()[0] if line.split() else ""
        if primer_campo.endswith(f".{name}"):
            sesiones.append(primer_campo)
    return sesiones


def restart_screen(name: str) -> bool:
    # 'fast' (dinero real, live_trade.py corre dentro) NUNCA se reinicia con
    # el screen -dmS desnudo de abajo -- code-review 21-Jul: este camino no
    # tenía chequeo de orden_en_curso.json ni espera/verificación de que la
    # screen vieja hubiera muerto de verdad, y reabría exactamente la misma
    # carrera de duplicados en results.csv que watchdog_fast.sh ya arregló
    # por su lado (FAVORITO_CONFIRMADO#2866629#BUY_YES 11-Jul, LATE_WINDOW_
    # 5MIN#2998086#BUY_NO 21-Jul). restart_fast_seguro.sh es ahora el único
    # punto de verdad para reiniciar 'fast', compartido con watchdog_fast.sh
    # (cron */5min) -- no reimplementar la lógica aquí.
    if name == "fast":
        try:
            r = subprocess.run(["bash", str(REPO / "restart_fast_seguro.sh")],
                               timeout=30, capture_output=True, text=True)
            if r.returncode == 0:
                log("  [SCREEN] ✅ Screen 'fast' reiniciada (restart_fast_seguro.sh)")
                return True
            elif r.returncode == 1:
                log("  [SCREEN] Reinicio de 'fast' pospuesto (orden en curso, o ya había otra invocación en marcha)")
                return False
            elif r.returncode == 3:
                log("  [SCREEN] 🚨 CARRERA REAL: hay 2+ screens 'fast' vivas tras el reinicio — revisar manualmente YA")
                return False
            else:
                log(f"  [SCREEN] restart_fast_seguro.sh no pudo limpiar la screen 'fast' vieja (exit {r.returncode})")
                return False
        except Exception as e:
            log(f"  [SCREEN] Error ejecutando restart_fast_seguro.sh: {e}")
            return False

    # 'mantenimiento' (18-Ago): mismo motivo que 'fast' arriba -- este loop
    # (cada 120s) y watchdog_fast.sh (cron */5min) son dos disparadores
    # independientes que podrían crear una screen duplicada cada uno por su
    # lado. restart_mantenimiento_seguro.sh es el único punto de verdad,
    # compartido con watchdog_fast.sh -- no reimplementar la lógica aquí.
    if name == "mantenimiento":
        try:
            r = subprocess.run(["bash", str(REPO / "restart_mantenimiento_seguro.sh")],
                               timeout=30, capture_output=True, text=True)
            if r.returncode == 0:
                log("  [SCREEN] ✅ Screen 'mantenimiento' reiniciada (restart_mantenimiento_seguro.sh)")
                return True
            elif r.returncode == 1:
                log("  [SCREEN] Reinicio de 'mantenimiento' pospuesto (otra invocación ya en marcha)")
                return False
            else:
                log(f"  [SCREEN] restart_mantenimiento_seguro.sh falló (exit {r.returncode})")
                return False
        except Exception as e:
            log(f"  [SCREEN] Error ejecutando restart_mantenimiento_seguro.sh: {e}")
            return False

    cmd = SCREEN_RESTART.get(name)
    if not cmd:
        return False
    try:
        # 01-Sep: sin esto, dos disparadores independientes en el mismo ciclo
        # (check_screens() "ausente" en sección 2 + verify_deploy "deploy
        # obsoleto" en sección 2b) podían llamar a restart_screen(name) casi
        # a la vez sin que ninguno supiera del otro -- spawneando DOS screens
        # 'control' con el mismo nombre (mismo timestamp exacto, 01-Sep
        # 05:19:02Z). Con 'control' eso significa dos procesos haciendo
        # polling a Telegram getUpdates con el mismo offset -> 409 Conflict
        # perpetuo, silencioso (nadie lo ve hasta que un comando no responde),
        # bot de control muerto durante >1h hasta el barrido de esta sesión.
        # Mismo riesgo late en cualquier screen de esta lista (dash,
        # observadores, fetchers, ejecdryrun, walletmirror, vigiasfreq...).
        # Matar cualquier screen viva con ese nombre ANTES de crear una nueva
        # hace el restart idempotente frente a llamadas concurrentes, mismo
        # principio que restart_fast_seguro.sh/restart_mantenimiento_seguro.sh
        # ya aplican para 'fast'/'mantenimiento'.
        for sess_id in _sesiones_con_nombre(name):
            subprocess.run(["screen", "-S", sess_id, "-X", "quit"],
                           timeout=5, capture_output=True)
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
CHAINLINK_STALE_SECS = 120  # ~4 ticks/s agregados en horario normal -- 120s sin
# escritura ya es anómalo. Real 28-Jul: fetch_chainlink_prices.py colgó en
# silencio 30+min (websocket muerto sin cierre limpio, `async for raw in ws`
# bloqueado para siempre, sin excepción que el bucle de reconexión pudiera
# capturar) -- el proceso seguía "vivo" (screen listada, PID activo), así que
# check_screens() nunca lo detectó. Fix de raíz aplicado (timeout en el recv,
# ver RECV_TIMEOUT_S en fetch_chainlink_prices.py) + esta red de seguridad
# aparte, por si el proceso se cuelga de otra forma en el futuro. Solo lectura
# (no toca dinero, no hay orden_en_curso que proteger) -- kill+restart directo
# es seguro, a diferencia de 'fast'.
# 07-Ago: chainlink vive ahora dentro de la screen fusionada "fetchers"
# (fetchers_fase0.py) -- un hilo colgado fuerza reiniciar el proceso entero
# (mata también liqs/libroambos/polyactivity, que se re-arrancan solos vía
# el supervisor de hilos), mismo trade-off ya aceptado en observadores_fase0.py.
def check_chainlink_fresh(screens_up: dict) -> None:
    if not screens_up.get("fetchers"):
        return  # check_screens ya se encarga de relanzarla si está caída
    hoy = time.strftime("%Y-%m-%d", time.gmtime())
    p = REPO / "data" / "prices" / f"chainlink_{hoy}.csv"
    if not p.exists():
        return
    age = time.time() - p.stat().st_mtime
    if age > CHAINLINK_STALE_SECS:
        log(f"  ⚠ chainlink: sin ticks nuevos hace {age:.0f}s (screen 'fetchers' viva pero colgada) — reiniciando")
        try:
            subprocess.run(["screen", "-S", "fetchers", "-X", "quit"], timeout=10)
            time.sleep(1)
        except Exception as e:
            log(f"  [CHAINLINK] error al matar screen vieja: {e}")
        restart_screen("fetchers")


POLYACTIVITY_STALE_SECS = 60  # 29-Jul: MISMO patrón que chainlink -- el
# firehose de polyactivity mueve cientos/miles de trades/min en horario
# normal, así que 60s sin ninguna fila nueva ya es anómalo. Encontrado el
# mismo bug de raíz (async for raw in ws sin timeout, conexión muerta en
# silencio) al comparar fidelidad contra ballenas_timing_history.csv --
# 71% de mercados sin cobertura por 3 huecos de ~2h sin ningún error en
# el log. Fix de raíz ya aplicado (RECV_TIMEOUT_S=30), esta es la MISMA
# red de seguridad de refuerzo que ya protege a chainlink, por si se
# repite de otra forma en el futuro.
# 07-Ago: polyactivity vive ahora dentro de la screen fusionada "fetchers"
# (fetchers_fase0.py) -- mismo trade-off que check_chainlink_fresh arriba.


def check_polyactivity_fresh(screens_up: dict) -> None:
    if not screens_up.get("fetchers"):
        return  # check_screens ya se encarga de relanzarla si está caída
    hoy = time.strftime("%Y-%m-%d", time.gmtime())
    p = Path("/root/polymarket-research-datalogs") / f"polymarket_activity_{hoy}.csv"  # 29-Jul: fuera del repo
    if not p.exists():
        return
    age = time.time() - p.stat().st_mtime
    if age > POLYACTIVITY_STALE_SECS:
        log(f"  ⚠ polyactivity: sin filas nuevas hace {age:.0f}s (screen 'fetchers' viva pero colgada) — reiniciando")
        try:
            subprocess.run(["screen", "-S", "fetchers", "-X", "quit"], timeout=10)
            time.sleep(1)
        except Exception as e:
            log(f"  [POLYACTIVITY] error al matar screen vieja: {e}")
        restart_screen("fetchers")


def check_results_growing():
    p = DIR_SHADOW / "results.csv"
    if not p.exists():
        return
    age = time.time() - p.stat().st_mtime
    if age > RESOLVE_LAG_SECS:
        log(f"  ⚠ results.csv sin actualizar hace {age/3600:.1f}h — shadow_resolve podría "
            f"estar colgado (screen 'mantenimiento' desde el desacoplo 18-Ago, ya NO 'fast')")


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
    """Borra postmortem.csv si excede el umbral. 17-Ago: antes esto disparaba
    un bucle infinito (65 borrados en 2h) porque shadow_postmortem.py
    derivaba su dedup del propio CSV -- borrarlo hacía que el siguiente
    ciclo reprocesara los 63k+ pérdidas históricas y reescribiera otro
    CSV >50MB en ~70s. Arreglado en shadow_postmortem.py (índice JSON
    independiente, POSTMORTEM_KEYS_PATH) -- este borrado ya es seguro."""
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
    for logf in sorted((REPO / "logs").glob("*.log")):
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
# 08-Ago (petición explícita Javi, "no paran de llegar avisos... no puede
# ser"): el techo_freno_diario puede quedarse pegado a ~0€ durante horas en
# un día con pnl negativo (no se resetea hasta medianoche UTC) — con el
# cooldown de 30min esto mandaba el MISMO aviso 15-20 veces en una sola
# tarde (ver logs/watchdog.log 05/06-Ago), puro ruido una vez que Javi ya
# lo ha visto la primera vez. Cambiado de cooldown-por-tiempo a
# latch-por-entrada (mismo patrón que vigia_sigma_patrones/vigia_log_growth,
# CLAUDE.md pt.5): un solo aviso al ENTRAR en deadlock, silencio mientras
# se mantenga, nuevo aviso solo si sale y vuelve a entrar (p.ej. un nuevo
# día, o tras operar y volver a bloquearse). No toca el circuit breaker en
# sí (freno_diario/bankroll_minimo siguen exactamente igual) — solo cuántas
# veces se notifica el mismo estado ya conocido.
_deadlock_avisado: bool = False


def check_bankroll_deadlock() -> None:
    """Alerta por Telegram si ninguna señal puede ser viable pase lo que
    pase el IC (probado con IC=1.0, el máximo posible) pese a que el switch
    está ON y el circuit breaker real todavía no ha saltado. Reutiliza
    calcular_stake() tal cual (no duplica su lógica de frenos/margen)."""
    global _deadlock_avisado
    try:
        from live_stake import calcular_stake, bankroll_minimo_eur_hoy
        from live_guard import switch_activo
        from shadow_digest import enviar_telegram

        r = calcular_stake(ic=1.0)
        en_deadlock = switch_activo() and not r["viable"] and r["bankroll"] > bankroll_minimo_eur_hoy()

        if en_deadlock:
            if not _deadlock_avisado:
                _deadlock_avisado = True
                log(f"⚠ Bankroll en zona muerta de sizing — alerta Telegram enviada. {r['motivo']}")
                enviar_telegram(
                    "⚠️ *Bankroll en zona muerta (deadlock de sizing)*\n"
                    f"{r['motivo']}\n\n"
                    "Switch ON, circuit breaker real sin disparar, pero NINGUNA señal "
                    "puede ser viable pase lo que pase el IC (probado con IC=1.0) — "
                    "el sistema queda parado en silencio (`no_viable_stake`/`senal_caducada` "
                    "repetidos en fast.log).\n"
                    "Necesita recarga de capital o un override puntual "
                    "(`bankroll_minimo_eur_override` / `freno_diario_pct_override` en config_live.json).\n"
                    "_(este aviso no se repite hasta salir y volver a entrar en zona muerta)_"
                )
            else:
                log(f"  [check-deadlock] sigue en zona muerta (ya avisado) — {r['motivo']}")
        else:
            _deadlock_avisado = False  # reset al salir de la zona muerta
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

            # ── 1c. Screens retiradas (fusión 05-Ago) reviviendo por error ────
            matadas = kill_screens_retiradas()
            if matadas:
                log(f"🚨 Screen(s) retirada(s) revivida(s) y matada(s) de nuevo: {matadas} "
                    f"-- duplicaban observadores_fase0.py, filas corrompidas mientras vivieron")
                from shadow_digest import enviar_telegram
                enviar_telegram(
                    f"🚨 Screen(s) retirada(s) revivida(s): {matadas}\n"
                    f"Duplicaban observadores_fase0.py -- ya vueltas a matar. "
                    f"Revisar quién las relanza (no hay cron ni watchdog que lo haga)."
                )

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

            # ── 2a. Chainlink vivo pero colgado (screen OK, sin ticks nuevos) ──
            check_chainlink_fresh(screens)
            check_polyactivity_fresh(screens)

            # ── 2b. Deploy obsoleto -- auto-reinicio (09-Ago, petición explícita
            #      Javi: "que no se quede colgado nunca, el mejor pipeline que
            #      existe"). check_stale_deploys() de arriba solo miraba el
            #      mtime del ENTRYPOINT (ej. observadores_fase0.py), no de los
            #      módulos que importa -- no habría detectado el caso real de
            #      esa misma noche (9 screens STALE por cambios en
            #      gate_bucket_propio.py, importado, no el entrypoint). Se
            #      sustituye por verify_deploy.py::estado() (cierre transitivo
            #      de imports, mismo mecanismo ya usado a mano dos veces esa
            #      noche) vía subprocess -- evita el import circular
            #      (verify_deploy ya importa pipeline_watchdog para
            #      SCREEN_RESTART). Auto-reinicia solo screens de riesgo BAJO
            #      (control/dash/observadores/fetchers/ejecdryrun -- infra o
            #      DRY_RUN=True, verificado en sus propios docstrings).
            #      NO_AUTO_RESTART_DINERO_REAL agrupa DOS motivos distintos
            #      bajo un nombre que solo describe uno (/code-review 18-Ago,
            #      aclarado aquí para que no se lea como "todos estos NUNCA
            #      se reinician solos"): (a) fast/slow/mantenimiento --
            #      marcadas shallow+no_restart=True en verify_deploy.SCREENS
            #      porque son loops bash que invocan Python FRESCO cada
            #      ciclo (~20-90s) -- "código en memoria desactualizado" no
            #      aplica nunca, así que este camino de staleness (2b) no
            #      tiene nada que hacer con ellas; SÍ se reinician solas por
            #      la vía normal (check_screens(), sección 2 más abajo, o
            #      restart_fast_seguro.sh/restart_mantenimiento_seguro.sh)
            #      si la screen desaparece de verdad. (b) los 4 ejecutores
            #      de baja latencia que SÍ operan con DRY_RUN=False (10-Ago,
            #      consolidados en "ejeclive") -- estos SÍ son dinero real
            #      de verdad, y aquí el motivo real es no reiniciar en medio
            #      de un ciclo con posiciones abiertas sin revisión humana.
            #      Sin esta exclusión, cualquier commit que tocara un módulo
            #      en su cierre de imports habría hecho que este loop la
            #      reiniciara sola, sin revisión humana, en mitad de un
            #      ciclo con posiciones reales abiertas -- contradice la
            #      regla del manual de diagnosticar antes de reiniciar
            #      dinero real. Sigue apareciendo en el aviso de Telegram
            #      como "NO reiniciada (dinero real, reinicia a mano si
            #      procede)", igual que antes de este cambio.
            NO_AUTO_RESTART_DINERO_REAL = {
                "fast", "slow", "mantenimiento", "ejeclive",
            }
            try:
                r = subprocess.run(
                    [sys.executable, "-c",
                     "import json, verify_deploy as v; "
                     "print(json.dumps({k: d['veredicto'] for k, d in v.estado().items()}))"],
                    capture_output=True, text=True, timeout=30, cwd=str(REPO))
                if r.returncode == 0:
                    estado_deploy = json.loads(r.stdout.strip())
                else:
                    log(f"⚠ verify_deploy.estado() salió con código {r.returncode}: {r.stderr.strip()[:300]}")
                    estado_deploy = {}
            except Exception as e:
                log(f"⚠ verify_deploy.estado() falló: {e}")
                estado_deploy = {}

            stale_todas = {n for n, v in estado_deploy.items() if v == "STALE"}
            stale_dinero_real = stale_todas & NO_AUTO_RESTART_DINERO_REAL
            stale_ahora = stale_todas - NO_AUTO_RESTART_DINERO_REAL
            reiniciadas, fallidas = [], []
            for name in stale_ahora:
                log(f"⚠ DEPLOY OBSOLETO: {name} — auto-reiniciando")
                try:
                    # 16-Ago: 30s no basta para el nuevo presupuesto de probe de
                    # verify_deploy.py (~120s, ver ahí) -- observadores_fase0.py
                    # (17 hilos, arranque escalonado 1s/hilo) tardaba más que el
                    # timeout y este subprocess lo mataba antes de que el probe
                    # pudiera confirmar éxito, generando falsos "NO se pudieron
                    # reiniciar" por Telegram con el proceso ya sano.
                    rr = subprocess.run(
                        [sys.executable, "verify_deploy.py", "--restart", name],
                        capture_output=True, text=True, timeout=150, cwd=str(REPO))
                    (reiniciadas if rr.returncode == 0 else fallidas).append(name)
                    log(f"  {'✅' if rr.returncode == 0 else '🚨'} {rr.stdout.strip()}")
                except Exception as e:
                    fallidas.append(name)
                    log(f"  🚨 error reiniciando {name}: {e}")

            nuevos = (stale_ahora | stale_dinero_real) - stale_deploy_alertado
            if nuevos:
                try:
                    from shadow_digest import enviar_telegram
                    partes = []
                    if reiniciadas:
                        partes.append("✅ reiniciadas automáticamente: " + ", ".join(reiniciadas))
                    if fallidas:
                        partes.append("🚨 NO se pudieron reiniciar (revisar a mano): " + ", ".join(fallidas))
                    if stale_dinero_real:
                        partes.append("💰 dinero real, auto-restart deshabilitado a propósito — "
                                       "reinicia a mano si procede: " + ", ".join(sorted(stale_dinero_real)))
                    enviar_telegram("⚠️ *Deploy obsoleto detectado*\n" + "\n".join(partes))
                except Exception:
                    pass
            # las reiniciadas OK vuelven a FRESH solas; dinero-real queda
            # latcheada (un solo aviso por episodio STALE, mismo patrón que
            # el resto de vigías del proyecto) hasta que alguien la reinicie
            # a mano y vuelva a FRESH -- entonces sale de estado_deploy con
            # veredicto STALE y el próximo episodio vuelve a avisar.
            stale_deploy_alertado = (stale_ahora - set(reiniciadas)) | stale_dinero_real

            # ── 3. Si hay silencio, buscar errores en fast.log ────────────────
            if consecutivos_silencio >= 2:
                # 800 (antes 400) -- /code-review 18-Ago: logs/fast.log pasó
                # a ser compartido por 'fast' Y 'mantenimiento' (desacoplo del
                # mismo día); con la ventana vieja, la salida intercalada de
                # 'mantenimiento' podía empujar fuera del tail un traceback
                # real de 'fast'. No elimina el riesgo del todo (ambos loops
                # siguen compartiendo el mismo fichero sin separación), pero
                # duplica el margen -- ver _SCRIPTS_FAST más abajo para el
                # filtrado por script de origen, complementario a esto.
                texto = ultimos_errores_log(800)
                # Filtrado a scripts propios de 'fast' -- ver docstring de
                # extraer_traceback()/_SCRIPTS_FAST arriba. FIX-A (más abajo)
                # EDITA código en base a `tb`, así que aquí sí importa que
                # sea el traceback correcto, no solo un log informativo.
                tb = extraer_traceback(texto, scripts_permitidos=_SCRIPTS_FAST)
                texto_reciente = texto[-4000:]

                if "UnboundLocalError" in texto_reciente:
                    # /code-review (18-Ago, hallazgo real): `tb or
                    # ultimos_errores_log(600)` deshacía el filtro de arriba
                    # en el momento exacto en que hacía falta -- si `tb`
                    # sale vacío (el UnboundLocalError es de 'mantenimiento',
                    # no de 'fast'), el fallback volvía a coger el tail SIN
                    # filtrar, y FIX-A podía editar/commitear un fix sobre
                    # el script EQUIVOCADO basado en un error ajeno. Sin
                    # `tb` fast-atribuible, no hay nada seguro que arreglar
                    # aquí -- se deja sin tocar (revisión manual), no se cae
                    # a un texto sin filtrar solo por tener "algo" que pasar.
                    if not tb:
                        log("🔴 UnboundLocalError en fast.log, pero no atribuible a un script de "
                            "'fast' (probable origen en 'mantenimiento', log compartido) -- "
                            "FIX-A NO se aplica a ciegas, requiere revisión manual")
                    else:
                        log("🔴 UnboundLocalError en fast.log → aplicando FIX-A")
                        if fix_unbound_local(tb):
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
