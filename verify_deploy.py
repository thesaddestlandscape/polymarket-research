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
    "dash":    {"entry": "dashboard_server.py",    "probe": "http:8888"},
    "control": {"entry": "live_control.py",        "probe": "log:logs/live_control.log:escuchando comandos"},
    "pfinish": {"entry": "photo_finish_logger.py", "probe": None},
    "ballenas_fast": {"entry": "ballenas_executor_btc15m.py",
                       "probe": "log:logs/ballenas_fast.log:arrancado"},
    # Solo se vigila el .sh (sus hijos python son proceso fresco cada ciclo).
    "fast":    {"entry": "run_fast.sh", "shallow": True, "no_restart": True},
    "slow":    {"entry": "run_slow.sh", "shallow": True, "no_restart": True},
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


def proceso_de(entry: str) -> tuple[int, int] | None:
    """(pid, start_epoch) del proceso cuya cmdline contiene entry, o None."""
    out = subprocess.run(["ps", "-eo", "pid,etimes,cmd"],
                         capture_output=True, text=True).stdout
    ahora = int(time.time())
    for line in out.splitlines()[1:]:
        parts = line.split(None, 2)
        if len(parts) == 3 and entry in parts[2] and "SCREEN" not in parts[2]:
            return int(parts[0]), ahora - int(parts[1])
    return None


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
    cfg = SCREENS.get(nombre)
    if cfg is None:
        print(f"screen desconocida: {nombre} (válidas: {', '.join(SCREENS)})")
        return 2
    if cfg.get("no_restart"):
        print(f"🚫 {nombre} no se reinicia desde aquí (regla #8: diagnostica primero; "
              f"watchdog + marker orden_en_curso.json). Hazlo a mano si procede.")
        return 2
    subprocess.run(["screen", "-S", nombre, "-X", "quit"], capture_output=True)
    time.sleep(1)
    t0 = time.time()
    subprocess.run(["screen", "-dmS", nombre, "python3", cfg["entry"]], cwd=BASE)
    time.sleep(3)
    proc = proceso_de(cfg["entry"])
    if proc is None:
        print(f"🚨 {nombre}: el proceso NO está vivo tras el restart")
        return 1
    ok, detalle = probe_ok(cfg.get("probe"), t0)
    print(f"{'✅' if ok else '🚨'} {nombre}: reiniciado pid={proc[0]} — probe: {detalle}")
    return 0 if ok else 1


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--restart":
        sys.exit(reiniciar(sys.argv[2]))
    sys.exit(informe(estado()))
