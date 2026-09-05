"""
verify_deploy.py — ¿Los procesos persistentes corren el código que hay en disco?

Mejora #2 del plan de loops (cicatrices: dashboard editado 07-Jul sin restart;
live_control corrió del 01 al 08-Jul con módulos cacheados de una semana).

Para cada screen persistente compara el arranque del proceso con el mtime más
reciente de su cierre de imports locales (recursivo). Los scripts del fast/slow
loop NO necesitan esto: son proceso fresco cada ciclo; aquí solo se vigila el
propio .sh del loop.

Uso:
  python3 verify_deploy.py                  # informe (exit 1 si algo STALE)
  python3 verify_deploy.py --restart dash   # reinicia esa screen + probe

fast/slow NUNCA se reinician desde aquí (regla #8 del manual: primero
diagnosticar; el watchdog ya reinicia solo y hay marker orden_en_curso.json).
"""
import os
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

BASE = Path(__file__).parent

# probe: cómo confirmar que el proceso reiniciado está VIVO y sirviendo,
# no solo presente en ps.
SCREENS = {
    # dash (24-Ago): fusiona dashboard_server.py (8888) + sports_dashboard_
    # server.py (8890, antes screen "dash-sports") -- ver dashboards_
    # consolidado.py. "entry" importa los 2 módulos originales, así que el
    # cierre de imports los cubre igual que antes para detectar STALE.
    "dash":    {"entry": "dashboards_consolidado.py", "probe": "http:8888"},
    "control": {"entry": "live_control.py",        "probe": "log:logs/live_control.log:escuchando comandos"},
    # pfinish/favultsec/puntoconf/ressniper/p22fase0/boxbuilder/solcontrario5m/
    # xrpcontrario15m/favcontraria/fav5malt fusionados en "observadores" el
    # 05-Ago (ver observadores_fase0.py) -- 10 procesos -> 1, mitigación de
    # sobresuscripción de CPU (project_push_roto_carga_cpu_resuelto_05ago).
    "observadores": {"entry": "observadores_fase0.py",
                      "probe": "log:logs/observadores_fase0.log:hilos arrancados"},
    # chainlink/polyactivity/liqs/libroambos fusionados en "fetchers" el
    # 07-Ago (ver fetchers_fase0.py) -- 4 procesos -> 1, misma mitigación
    # de sobresuscripción de CPU que "observadores"/"ejecdryrun".
    "fetchers": {"entry": "fetchers_fase0.py",
                 "probe": "log:logs/fetchers_fase0.log:hilos arrancados"},
    # ejeclive (10-Ago): ballenas_fast/ballenas_5m/favaltaconv/favbtc60mno
    # (4 screens, dinero real) fusionados en UN proceso -- ver
    # executores_live_consolidado.py y pipeline_watchdog.py::SCREEN_RESTART
    # para el motivo completo (eliminar 3 de 4 conexiones websocket
    # redundantes al firehose RTDS). El "entry" importa los 4 módulos
    # originales, así que el cierre de imports los cubre igual que antes.
    "ejeclive": {"entry": "executores_live_consolidado.py",
                 "probe": "log:logs/ejecutores_live_consolidado.log:arrancando 5 ejecutores"},
    # ballenas_15m/fav15mexec/fav60mexec/gbmlate15m/updowngbmtardio/
    # walletmirror/wmexec fusionados en "ejecdryrun" el 06-Ago (ver
    # ejecutores_dryrun_fase0.py) -- 7 procesos -> 1, mismo patrón que la
    # fusión de "observadores" (05-Ago). El proceso "ejeclive" (dinero
    # real) NO se toca.
    "ejecdryrun": {"entry": "ejecutores_dryrun_fase0.py",
                    "probe": "log:logs/ejecutores_dryrun_fase0.log:hilos arrancados"},
    # walletmirror (11-Ago): wallet_mirror_executor_dryrun.py pasó a
    # DRY_RUN=False (SEGUIR#BTC#5min#grande, aprobado Javi) -- sacado de
    # "ejecdryrun" (exige DRY_RUN=True en todos sus módulos, se negaba a
    # arrancar) a su propia screen, dinero real.
    "walletmirror": {"entry": "wallet_mirror_executor_dryrun.py",
                      "probe": "log:logs/wallet_mirror_executor.log:arrancado"},
    # precierre (05-Sep): resolution_sniper_precierre_executor.py, DRY_RUN=True,
    # screen propia por sensibilidad a latencia (ver nota en pipeline_watchdog.py).
    "precierre": {"entry": "resolution_sniper_precierre_executor.py",
                  "probe": "log:logs/resolution_sniper_precierre_executor.log:arrancado"},
    # vigiasfreq (17-Ago): 17 scripts de un solo disparo (cron cada
    # 5-60min) fusionados en UN proceso con scheduler interno -- ver
    # vigias_frecuentes_fase0.py y pipeline_watchdog.py::SCREEN_RESTART.
    "vigiasfreq": {"entry": "vigias_frecuentes_fase0.py",
                   "probe": "log:logs/vigias_frecuentes_fase0.log:arrancando scheduler"},
    # sportsfase0 (20-Ago): sports-mirror (sports_wallet_mirror_sniper.py) +
    # sports-ws (sports_activity_ws.py) fusionados en UN proceso -- mismo
    # patrón que "ejecdryrun"/"observadores", mitigación de la sobresuscripción
    # de CPU detectada en el barrido diario de salud (load5~8 en 2 cores).
    # weather-mirror/weather-ws NO se tocan (repo independiente
    # /root/polymarket-weather, CLAUDE.md prohíbe mezclar).
    "sportsfase0": {"entry": "sports_fase0_consolidado.py",
                     "probe": "log:logs/sports_fase0_consolidado.log:hilos arrancados"},
    # 20-Ago: nested_arb_scanner.py, antes cron '* * * * *', ahora proceso
    # persistente propio vía nested_arb_loop.py (ver su docstring).
    "nestedarb": {"entry": "nested_arb_loop.py",
                   "probe": "log:logs/nested_arb_loop.log:arrancando"},
    # Solo se vigila el .sh (sus hijos python son proceso fresco cada ciclo).
    "fast":    {"entry": "run_fast.sh", "shallow": True, "no_restart": True},
    "slow":    {"entry": "run_slow.sh", "shallow": True, "no_restart": True},
    # mantenimiento (18-Ago): resolve/postmortem/resumen/git-batch,
    # desacoplado de run_fast.sh -- ver run_fast_mantenimiento.sh y
    # project_desacoplar_fast_loop_postmortem_18ago. No dinero real
    # (no envía órdenes), pero tampoco se auto-reinicia a ciegas desde
    # aquí -- mismo trato que fast/slow, watchdog_fast.sh/pipeline_
    # watchdog.py lo cubren.
    "mantenimiento": {"entry": "run_fast_mantenimiento.sh", "shallow": True, "no_restart": True},
}

IMPORT_RE = re.compile(r"^\s*(?:from|import)\s+([A-Za-z_]\w*)", re.MULTILINE)


def cierre_imports(entry: Path) -> set[Path]:
    """Cierre transitivo de imports que resuelven a .py locales del repo."""
    vistos, cola = set(), [entry]
    while cola:
        f = cola.pop()
        if f in vistos or not f.exists():
            continue
        vistos.add(f)
        if f.suffix != ".py":
            continue
        try:
            src = f.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for mod in IMPORT_RE.findall(src):
            local = BASE / f"{mod}.py"
            if local.exists() and local not in vistos:
                cola.append(local)
    return vistos


_PROCESO_DE_RE_CACHE: dict[str, re.Pattern] = {}


def proceso_de(entry: str) -> tuple[int, int] | None:
    """(pid, start_epoch) del proceso cuya cmdline contiene entry como
    TOKEN completo (precedido por inicio/espacio/'/', seguido de fin/
    espacio), o None.

    18-Ago (hallazgo real, spam de "Deploy obsoleto" cada ~2min en
    Telegram): un `entry in parts[2]` de substring plano hacía que
    "dashboard_server.py" (nuestro dashboard cripto) matcheara también
    "sports_dashboard_server.py" (otro subsistema del mismo repo, PID
    vivo desde mucho antes que cualquier cambio de hoy) -- ese proceso
    ajeno siempre "ganaba" (aparece antes en `ps`, PID más bajo), así que
    verify_deploy() creía que "dash" corría un proceso viejísimo y lo
    marcaba STALE en bucle infinito aunque el dashboard cripto real
    estuviera FRESH. Con boundary de \\b (regex, no split por espacios --
    "/" también debe cortar el match, ver 'python3 dashboard_server.py'
    vs 'python3 sports_dashboard_server.py') el substring solo matchea
    como palabra completa."""
    pattern = _PROCESO_DE_RE_CACHE.get(entry)
    if pattern is None:
        pattern = re.compile(r"(?:^|[\s/])" + re.escape(entry) + r"(?:$|\s)")
        _PROCESO_DE_RE_CACHE[entry] = pattern
    out = subprocess.run(["ps", "-eo", "pid,etimes,cmd"],
                         capture_output=True, text=True).stdout
    ahora = int(time.time())
    base_resuelto = str(BASE.resolve())
    candidatos = []
    for line in out.splitlines()[1:]:
        parts = line.split(None, 2)
        if len(parts) == 3 and pattern.search(parts[2]) and "SCREEN" not in parts[2]:
            candidatos.append((int(parts[0]), ahora - int(parts[1])))
    if not candidatos:
        return None
    # 18-Ago: sigue habiendo un segundo caso real de colisión -- dos repos
    # DISTINTOS (este y polymarket-weather) tienen cada uno su propio
    # script llamado literalmente "dashboard_server.py", indistinguibles
    # por cmdline sola. Desempatar por cwd real del proceso (/proc/pid/cwd)
    # -- el nuestro se lanza con `cd {REPO} && ...`, así que su cwd (y el
    # de su hijo python heredado) es siempre BASE, a diferencia del de
    # otro repo. Si /proc no está disponible o ningún candidato resuelve
    # (entorno no-Linux, proceso ya muerto) cae al primer candidato como
    # antes -- mismo comportamiento que la versión previa, no peor.
    for pid, edad in candidatos:
        try:
            cwd = os.readlink(f"/proc/{pid}/cwd")
        except OSError:
            continue
        if cwd == base_resuelto:
            return pid, edad
    return candidatos[0]


def probe_ok(spec: str | None, desde_epoch: float) -> tuple[bool, str]:
    if spec is None:
        return True, "sin probe (basta proceso vivo)"
    if spec.startswith("http:"):
        puerto = spec.split(":", 1)[1]
        try:
            urllib.request.urlopen(f"http://localhost:{puerto}/", timeout=5)
            return True, f"HTTP :{puerto} responde"
        except urllib.error.HTTPError as e:
            # 401/403 = el server vive (dashboard tiene auth)
            return True, f"HTTP :{puerto} responde ({e.code})"
        except Exception as e:
            return False, f"HTTP :{puerto} NO responde: {type(e).__name__}"
    if spec.startswith("log:"):
        _, ruta, patron = spec.split(":", 2)
        f = BASE / ruta
        if not f.exists():
            return False, f"{ruta} no existe"
        if f.stat().st_mtime < desde_epoch:
            return False, f"{ruta} sin escrituras desde el restart"
        cola = f.read_text(encoding="utf-8", errors="replace").splitlines()[-20:]
        if any(patron in ln for ln in cola):
            return True, f"'{patron}' en {ruta}"
        return False, f"'{patron}' no aparece en el tail de {ruta}"
    return False, f"probe desconocido: {spec}"


def estado() -> dict[str, dict]:
    res = {}
    for nombre, cfg in SCREENS.items():
        entry = BASE / cfg["entry"]
        proc = proceso_de(cfg["entry"])
        ficheros = {entry} if cfg.get("shallow") else cierre_imports(entry)
        mas_nuevo = max(ficheros, key=lambda f: f.stat().st_mtime)
        mtime = mas_nuevo.stat().st_mtime
        if proc is None:
            veredicto = "CAIDO"
        elif proc[1] < mtime:
            veredicto = "STALE"
        else:
            veredicto = "FRESH"
        res[nombre] = {"veredicto": veredicto, "proc": proc,
                       "mtime": mtime, "fichero_nuevo": mas_nuevo.name,
                       "n_modulos": len(ficheros)}
    return res


def informe(est: dict) -> int:
    peor = 0
    for nombre, d in est.items():
        p = d["proc"]
        proc_str = (f"pid={p[0]} arrancado {time.strftime('%m-%d %H:%M', time.localtime(p[1]))}"
                    if p else "SIN PROCESO")
        print(f"{'✅' if d['veredicto']=='FRESH' else '🚨'} {nombre:<8} {d['veredicto']:<6} "
              f"{proc_str} | disco: {d['fichero_nuevo']} "
              f"{time.strftime('%m-%d %H:%M', time.localtime(d['mtime']))} "
              f"({d['n_modulos']} módulos vigilados)")
        if d["veredicto"] != "FRESH":
            peor = 1
    return peor


def reiniciar(nombre: str) -> int:
    """17-Jul: antes construía su propio comando de arranque
    (["screen","-dmS",nombre,"python3",cfg["entry"]]) -- sin redirección de
    stdout/stderr y con el python3 del sistema, no el venv del proyecto.
    Divergía del comando REAL de producción (pipeline_watchdog.SCREEN_RESTART),
    la única fuente de verdad hasta hoy vivía duplicada en dos sitios. Un
    restart manual con este comando roto dejaba el proceso vivo pero sin
    log (probe fallaba en silencio) y, si coincidía con un ciclo del
    watchdog (cron */5), producía 2 screens con el mismo nombre -- 'screen
    -S <nombre> -X quit' deja de poder matar NINGUNA en cuanto hay
    ambigüedad, así que el problema se autoagravaba en vez de corregirse
    solo (ver idea_race_restart_verify_deploy_watchdog_17jul). Ahora
    reutiliza el comando real y mata TODAS las instancias por PID antes de
    arrancar una nueva, nunca por nombre (evita la ambigüedad de raíz)."""
    cfg = SCREENS.get(nombre)
    if cfg is None:
        print(f"screen desconocida: {nombre} (válidas: {', '.join(SCREENS)})")
        return 2
    if cfg.get("no_restart"):
        print(f"🚫 {nombre} no se reinicia desde aquí (regla #8: diagnostica primero; "
              f"watchdog + marker orden_en_curso.json). Hazlo a mano si procede.")
        return 2

    import pipeline_watchdog
    cmd = pipeline_watchdog.SCREEN_RESTART.get(nombre)
    if cmd is None:
        print(f"🚨 {nombre}: sin comando de arranque en pipeline_watchdog.SCREEN_RESTART "
              f"-- añádelo ahí primero (única fuente de verdad)")
        return 2

    r = subprocess.run(["screen", "-ls"], capture_output=True, text=True)
    pids = re.findall(rf"(\d+)\.{re.escape(nombre)}[\s\t]", r.stdout)
    for pid in pids:
        subprocess.run(["screen", "-S", f"{pid}.{nombre}", "-X", "quit"], capture_output=True)
    time.sleep(1)
    t0 = time.time()
    subprocess.run(["screen", "-dmS", nombre, "bash", "-c", cmd], cwd=BASE)
    time.sleep(3)
    proc = proceso_de(cfg["entry"])
    if proc is None:
        print(f"🚨 {nombre}: el proceso NO está vivo tras el restart")
        return 1
    # 10-Ago (hallazgo /code-review, auto-restart de pipeline_watchdog.py):
    # un solo intento de probe a los 3s daba falsos "reinicio fallido" en
    # scripts que tardan un poco más en escribir su línea de arranque
    # (varios hilos, ej. observadores_fase0.py/ejecutores_dryrun_fase0.py) --
    # el proceso YA estaba vivo con el código nuevo, solo el probe llegaba
    # pronto. Reintenta el probe (no el restart) un par de veces antes de
    # declarar fallo real -- evita alertar "revisar a mano" cuando en
    # realidad ya está en FRESH.
    # 16-Ago: el retry de 2×2s (7s totales con el sleep inicial) seguía
    # dando falsos "no se pudo reiniciar" en observadores_fase0.py -- tiene
    # 17 hilos con arranque escalonado (time.sleep(1.0) entre cada uno,
    # observadores_fase0.py:166), así que el mínimo garantizado antes de
    # imprimir "hilos arrancados" ya son 17s, más import de 17 módulos
    # (pandas/requests/etc en cada uno). Medido en logs/observadores_fase0.log
    # (13-Ago): ~85s reales entre "arrancando N observadores" y "N hilos
    # arrancados". Sube el presupuesto a ~120s (24×5s) -- no penaliza a los
    # probes rápidos (dash/control/etc.) porque el loop corta en cuanto ok=True.
    ok, detalle = probe_ok(cfg.get("probe"), t0)
    for _ in range(24):
        if ok:
            break
        time.sleep(5)
        ok, detalle = probe_ok(cfg.get("probe"), t0)
    print(f"{'✅' if ok else '🚨'} {nombre}: reiniciado pid={proc[0]} — probe: {detalle}")
    return 0 if ok else 1


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--restart":
        sys.exit(reiniciar(sys.argv[2]))
    sys.exit(informe(estado()))
