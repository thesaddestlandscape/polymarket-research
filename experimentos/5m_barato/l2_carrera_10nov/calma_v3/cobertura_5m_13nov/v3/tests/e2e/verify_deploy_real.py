"""verify_deploy de PRUEBAS con procesos REALES (se copia como sb/repo/verify_deploy.py): `--restart observadores` mata al observadores de pruebas como lo hace `screen -X quit`
(SIGHUP a su grupo de procesos; E2E_KILL=term_parent|kill_parent para otras variantes) y arranca uno nuevo (`python observadores_fase0.py`, cwd = sb/repo, log = LOGOBS).
E2E_MODE (1a llamada) / E2E_MODE_RB (siguientes): ok | mata_hijo (a los E2E_T s SIGKILL al hijo del observadores nuevo: el supervisor lo relanza = respawn)."""
import os, pathlib, signal, subprocess, sys, time

sb = pathlib.Path(os.environ["SB"])
# contrato con el real: `verify_deploy.py` (informe, solo lectura) y `verify_deploy.py "--restart" <screen>`
if len(sys.argv) == 1:
    print("\u2705 observadores FRESH  pid=%s arrancado (emulador e2e)" % (sb / "obs.pid").read_text().strip())
    sys.exit(1)
pantalla = sys.argv[-1]
calls = sb / "vd_calls.txt"
previas = [l for l in calls.read_text().splitlines() if l.split()[0] == pantalla] if calls.exists() else []
idx = len(previas)
modo = os.environ.get("E2E_MODE", "ok") if idx == 0 else os.environ.get("E2E_MODE_RB", "ok")
with open(calls, "a") as f:
    f.write(pantalla + " " + modo + "\n")
if pantalla != "observadores":
    sys.exit(0)
pidf = sb / "obs.pid"
if pidf.exists():
    old = int(pidf.read_text())
    sig = os.environ.get("E2E_KILL", "hup_group")
    try:
        if sig == "hup_group": os.killpg(os.getpgid(old), signal.SIGHUP)
        elif sig == "term_parent": os.kill(old, signal.SIGTERM)
        else: os.kill(old, signal.SIGKILL)
    except OSError:
        pass
    t0 = time.time()
    while os.path.exists(f"/proc/{old}") and "zombie" not in open(f"/proc/{old}/status").read().lower() and time.time() - t0 < 20:
        time.sleep(0.1)
time.sleep(1)
R = sb / "repo"
env = {**os.environ, "LIBRO_WS_REGISTRO_DIR": str(sb / "dl"), "LIBRO5_DIR": str(sb / "libro5"), "TXLOG_DIR": str(sb / "tx"), "UNIVERSO_JSON": str(sb / "universo.json"),
       "TOK_CACHE": str(sb / "cache.json"), "BNREG_CEDE_S": "30"}
(sb / "tx").mkdir(exist_ok=True)
p = subprocess.Popen([os.environ["PY"], "observadores_fase0.py"], cwd=R, stdout=open(os.environ["LOGOBS"], "a"), stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
                     start_new_session=True, env=env)
pidf.write_text(str(p.pid))
if modo == "mata_hijo":
    subprocess.Popen(["bash", "-c", "sleep %s; for h in $(ps -eo pid,ppid | awk '$2==%d {print $1}'); do kill -9 $h; done" % (os.environ.get("E2E_T", "12"), p.pid)], start_new_session=True)
time.sleep(3)
sys.exit(0)
