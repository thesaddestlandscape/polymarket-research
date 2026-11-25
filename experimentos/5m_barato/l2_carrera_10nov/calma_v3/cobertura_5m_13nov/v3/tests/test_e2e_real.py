"""Ensayo END-TO-END en sandbox con PROCESOS REALES (no produccion): un `observadores_fase0.py` de pruebas lanza el libro_estado_ws REAL (padre + hijo lector por el WS
publico del CLOB, solo lectura, universo fijo de mercados 5m VIVOS (CSV de data/markets + CLOB REST)) con rutas de registro/libro5 del sandbox. Se ejecutan los scripts de despliegue REALES con rutas
parametrizadas (DEPLOY_SANDBOX=1 aborta si alguna ruta es la real) y un verify_deploy de pruebas que mata/arranca el observadores como `screen -X quit` (SIGHUP al grupo).
Cubre: despliegue v3 completo, rollback forzado (respawn real del hijo) y la MEDIDA de cuanto tardan los hijos en morir tras matar a su padre.
L1: sin red el ensayo se SALTA (un skip NO sella); sin >= 10 GB libres en $E2E_DIR FALLA con mensaje claro (L3; conftest/run_tests.sh montan un tmpfs de pruebas): conftest.py solo escribe el sello
(datalogs/traspaso_deltas_ws/e2e_ok.json, con el sha de los scripts) cuando los 5 tests PASAN, y el P0 del despliegue real exige ese sello (<24 h, sha actual)."""
import json, os, shutil, signal, subprocess, sys, time
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_deploy_sandbox import V3, SCRIPT, PY, REAL, sha, _base_libro, _base_capture, estado, ORIG, sellar   # noqa: E402

E2E = V3 / "tests" / "e2e"


def _tokens_vivos():
    """Universo FIJO de mercados 5m VIVOS (libro5 solo graba tokens 5m): cola del CSV de hoy de data/markets (solo lectura) + tokens por el CLOB REST (gamma da 429 con facilidad)."""
    import csv, io, requests
    ahora = time.time()
    f = Path("/root/polymarket-research/data/markets") / (time.strftime("%Y-%m-%d", time.gmtime(ahora)) + ".csv")
    cab = open(f).readline()
    with open(f, "rb") as fh:
        sz = os.path.getsize(f); fh.seek(max(0, sz - 600_000)); fh.readline(); cola = fh.read().decode("utf-8", "replace")
    vivos = {}
    for r in csv.DictReader(io.StringIO(cab + cola)):
        try:
            if "-updown-5m-" not in r["slug"]:
                continue
            edt = time.mktime(time.strptime(r["end_date"][:19], "%Y-%m-%dT%H:%M:%S")) - time.timezone
            if ahora + 600 < edt < ahora + 3600:
                vivos[r["condition_id"]] = (r["slug"].split("-")[0].upper(), r["market_id"], r["end_date"], edt)
        except Exception:
            continue
    toks, claves, meta = [], {}, {}
    for cid, (a, mid, edt_txt, edt) in sorted(vivos.items(), key=lambda kv: kv[1][3])[:10]:
        try:
            m = requests.get(f"https://clob.polymarket.com/markets/{cid}", timeout=10).json()
            d = {t["outcome"]: t["token_id"] for t in m["tokens"]}
            for tk, lado in ((d["Up"], "YES"), (d["Down"], "NO")):
                toks.append(tk); claves[tk] = f"{a}#5min"; meta[tk] = [a, "5min", mid, edt_txt, lado]
        except Exception:
            continue
    return {"toks": toks, "claves": claves, "meta": meta}


@pytest.fixture(scope="module")
def universo():
    try:
        u = _tokens_vivos()
    except Exception as e:                      # sin requests / sin red
        pytest.skip(f"sin red para el ensayo end-to-end: {e}")
    if len(u["toks"]) < 4:
        pytest.skip("no hay mercados 5m vivos / el CLOB REST no respondio (sin red?)")
    return u


def _matar_sandbox(sb):
    for d in os.listdir("/proc"):
        if d.isdigit():
            try:
                cmd = open(f"/proc/{d}/cmdline", "rb").read().replace(b"\0", b" ").decode(errors="replace")
                if str(sb) in cmd and int(d) != os.getpid():
                    os.kill(int(d), 9)
            except OSError:
                pass


def OBSPID(sb):
    return int((sb / "obs.pid").read_text())


def _hijos_de(sb):
    out = []
    for d in os.listdir("/proc"):
        if d.isdigit():
            try:
                cmd = open(f"/proc/{d}/cmdline", "rb").read().replace(b"\0", b" ").decode(errors="replace")
                if cmd.endswith("libro_estado_ws.py --hijo ") and str(sb / "repo") in cmd:
                    out.append(int(d))
            except OSError:
                pass
    return out


def _dir_base():
    """L3: el directorio del sandbox e2e debe tener >= 10,5 GB libres (el hijo REAL pausa libro5 con < 10 GB en su volumen: umbral del codigo desplegado, no se toca). Lo normal es que lo
    prepare conftest.py/run_tests.sh (tmpfs con trap de limpieza) y lo exporte en E2E_DIR. Si no llega, el ensayo FALLA con un mensaje claro (no un skip silencioso, que ademas no sella)."""
    d = os.environ.get("E2E_DIR")
    libre = shutil.disk_usage(d).free / 2**30 if d and os.path.isdir(d) else 0.0
    if libre < 10.5:
        pytest.fail(f"E2E necesita >=10 GB libres en $E2E_DIR (E2E_DIR={d!r}: {libre:.1f} GB libres; el hijo real pausa libro5 por debajo de 10 GB). run_tests.sh y conftest.py montan un tmpfs solos; "
                    f"si fijas E2E_DIR a mano, apunta a un volumen con espacio (no al disco raiz)", pytrace=False)
    return d


@pytest.fixture
def rsb(universo):
    import tempfile
    sb = Path(tempfile.mkdtemp(dir=_dir_base(), prefix="e2e_deploy_")) / "sb"
    for d in ("repo/logs", "dl", "libro5", "bin", "tx"):
        (sb / d).mkdir(parents=True)
    sellar(sb)
    (sb / "p6_runner.py").write_text("print('OK stub (la captura real aislada se prueba en test_p6_y_seed.py)')\n")
    (sb / "repo/pipeline_watchdog.py").write_text('SCREEN_RESTART = {\n    "observadores": f"cd {REPO} && nice -n 10 choom -n -300 -- .venv/bin/python observadores_fase0.py >> logs/observadores_fase0.log 2>&1",\n}\n')
    _base_libro(sb / "repo/libro_estado_ws.py"); _base_capture(sb / "repo/capture_markets.py")
    shutil.copy(REAL / "data_quality.py", sb / "repo")
    shutil.copy(E2E / "verify_deploy_real.py", sb / "repo/verify_deploy.py"); shutil.copy(E2E / "observadores_fase0.py", sb / "repo/observadores_fase0.py")
    (sb / "universo.json").write_text(json.dumps(universo))
    (sb / "repo/logs/watchdog.log").write_text("x\n"); (sb / "repo/logs/observadores_fase0.log").write_text("log previo\n"); (sb / "repo/logs/slow.log").write_text("")
    (sb / "bin/screen").write_text(f"#!/bin/bash\n[ -d /proc/$(cat {sb}/obs.pid 2>/dev/null || echo 0) ] && echo '123.observadores (Detached)'; echo '124.vigiasfreq (Detached)'\n")
    (sb / "bin/screen").chmod(0o755)
    (sb / "loadavg").write_text("0.10 0.10 0.10 1/100 1\n")
    (sb / "dl/.binance_registro.lock").write_text("")
    holder = subprocess.Popen(["flock", str(sb / "dl/.binance_registro.lock"), "sleep", "3000"], start_new_session=True)       # = bnreg (pid en /proc/locks)
    (sb / "dl/.binance_registro.lock").write_text(f"bnreg pid={holder.pid}\n")
    (sb / "dl/BNREG_HABILITADO").write_text("")
    (sb / "dl/binance_registro_estado.json").write_text(json.dumps({"pid": holder.pid, "estado": "activo", "lock": True, "ts": int(time.time() * 1000) + 10**9}))
    subprocess.Popen(["bash", "-c", f'while true; do sleep 0.3; echo "$(date +%s.%N) tick" >> {sb}/repo/logs/watchdog.log; done'], start_new_session=True)
    env = {**os.environ, "LIBRO_WS_REGISTRO_DIR": str(sb / "dl"), "LIBRO5_DIR": str(sb / "libro5"), "TXLOG_DIR": str(sb / "tx"), "UNIVERSO_JSON": str(sb / "universo.json"),
           "TOK_CACHE": str(sb / "cache.json")}
    p = subprocess.Popen([str(PY), "observadores_fase0.py"], cwd=sb / "repo", stdout=open(sb / "repo/logs/observadores_fase0.log", "a"), stderr=subprocess.STDOUT,
                         stdin=subprocess.DEVNULL, start_new_session=True, env=env)
    (sb / "obs.pid").write_text(str(p.pid))
    t0 = time.time()
    while time.time() - t0 < 90 and not _hijos_de(sb):
        time.sleep(1)
    if not _hijos_de(sb):
        _matar_sandbox(sb); pytest.skip("el hijo real no arranco en 90 s")
    time.sleep(8)
    yield sb
    _matar_sandbox(sb)
    shutil.rmtree(sb.parent, ignore_errors=True)


def run(sb, *args, modo="ok", modo_rb="ok", extra=None, timeout=420):
    env = {"PATH": f"{sb}/bin:" + os.environ["PATH"], "SB": str(sb), "REPO": str(sb / "repo"), "DL": str(sb / "dl"), "V3": str(V3), "PY": str(PY), "LIBRO5": str(sb / "libro5"),
           "LOGOBS": str(sb / "repo/logs/observadores_fase0.log"), "WDLOG": str(sb / "repo/logs/watchdog.log"), "RAMLOCK": str(sb / "ramlock"), "LOADAVG": str(sb / "loadavg"),
           "CFGDIR": str(sb / "dl/universo_5m"), "MIN_GB": "0", "DEPLOY_SANDBOX": "1", "SANDBOX_HORA": "03:15", "E2E_MODE": modo, "E2E_MODE_RB": modo_rb, "P2_SLEEP": "0",
           "WD_PERIODO": "0.5", "WD_MARGEN": "0", "P5_PASO": "1", "P5_ESTABLE_S": "5", "P5_MUEREN_S": "40", "P5_CONN_S": "120", "P5_BN_S": "5", "P0_BN_S": "2", "P5_CRECE_S": "60",
           "P5_TERM_S": "20", "P5_KILL_GRACIA": "10", "P6_ESPERA_S": "0", "P6_AISLADO": "1", "P6_RUNNER": str(sb / "p6_runner.py"), "SEMBRAR_PY": "/no/existe", "P5_G_S": "10", "HOME": os.environ.get("HOME", "/root")}
    env.update(extra or {})
    return subprocess.run(["bash", str(SCRIPT), *args], capture_output=True, text=True, env=env, timeout=timeout)


def test_e2e_despliegue_v3_real_completo(rsb):
    viejos = _hijos_de(rsb)
    r = run(rsb, "--ejecutar")
    assert r.returncode == 0, r.stdout[-3000:]
    assert sha(rsb / "repo/libro_estado_ws.py") == sha(V3 / "delta_v3/libro_estado_ws.py") and estado(rsb)[2]
    nuevos = _hijos_de(rsb)
    assert len(nuevos) == 1 and not set(nuevos) & set(viejos), (viejos, nuevos)               # UN hijo, el nuevo; los viejos murieron
    assert "OK: desplegado" in r.stdout and "marcha atras" not in r.stdout.lower().replace("marcha atras si", "")


def test_e2e_rollback_forzado_real_por_respawn_del_hijo(rsb):
    """El hijo nuevo es matado (SIGKILL) a los ~12 s: el supervisor del padre lo relanza = RESPAWN real => DURO => marcha atras verificada con procesos reales."""
    r = run(rsb, "--ejecutar", modo="mata_hijo", extra={"E2E_T": "10"})
    assert r.returncode == 1 and "MARCHA ATRAS" in r.stdout, r.stdout[-3500:]
    low = r.stdout.lower()                                                                    # matar al hijo => DURO por respawn O por libro5 que deja de crecer (lo que se vea primero)
    assert "marcha atras hecha (ok)" in low and ("respawn" in low or "no crece" in low), r.stdout[-3500:]
    assert estado(rsb) == ORIG                                                                # main vuelve a la base
    assert len(_hijos_de(rsb)) == 1                                                           # y queda un unico hijo vivo (del observadores restaurado)


@pytest.mark.parametrize("kill", ["hup_group", "term_parent", "kill_parent"])
def test_medida_cuanto_tarda_en_morir_el_hijo_tras_matar_a_su_padre(rsb, kill):
    """(a) Mide con procesos reales: SIGHUP al grupo (lo que hace `screen -X quit`), SIGTERM solo al padre y SIGKILL solo al padre. El hijo sale al ver EOF en su stdin."""
    hijo = _hijos_de(rsb)[0]
    t0 = time.time()
    if kill == "hup_group": os.killpg(OBSPID(rsb), signal.SIGHUP)
    elif kill == "term_parent": os.kill(OBSPID(rsb), signal.SIGTERM)
    else: os.kill(OBSPID(rsb), signal.SIGKILL)
    vivo = lambda: os.path.exists(f"/proc/{hijo}") and "zombie" not in open(f"/proc/{hijo}/status").read().lower()
    while vivo() and time.time() - t0 < 120:
        time.sleep(0.05)
    dt = time.time() - t0
    print(f"\nMEDIDA muerte del hijo real tras {kill}: {dt:.2f} s")
    (V3 / "tests" / "e2e" / "medidas_muerte_hijo.txt").open("a").write(f"{kill} {dt:.2f}\n")
    assert dt < 60, f"el hijo viejo tarda {dt:.1f} s en morir tras {kill}: superaria el plazo de 90 s? (escalada TERM/KILL a huerfanos cubre el resto)"


def test_e2e_p6_ciclo_real_en_el_formato_real_de_slow_log_detecta_un_error_de_codigo(rsb):
    """B1 (red-team 14-Nov): run_slow.sh escribe cada cabecera '--- Ciclo slow N ---' DOS veces (tee + redireccion del screen). Un ciclo simulado en ESE formato (cabecera x2, un proceso real
    cuya linea de comandos lleva $REPO/capture_markets.py, data/markets crece, 'ERROR polymarket: NameError', '=== Fin ===' y el capture_wallets con su HTTPError ajeno) con P6_ESPERA_S>0:
    el error de codigo del ciclo nuevo se VE (antes el segmento quedaba en 1 linea y P6 daba un OK falso) => DURO => marcha atras verificada con procesos reales."""
    slow = rsb / "repo/logs/slow.log"; mk = rsb / "repo/data/markets"; mk.mkdir(parents=True, exist_ok=True)
    sp = rsb / "run_slow_sim.sh"
    sp.write_text(f'''#!/bin/bash
for i in $(seq 1 1500); do grep -qs '== P6' {rsb}/dl/traspaso_deltas_ws/deploy_*.log && break; sleep 0.2; done
sleep 1
for k in 1 2; do echo "[$(date -u +%FT%TZ)] --- Ciclo slow 9 ---" >> {slow}; done
bash -c 'sleep 8; :' {rsb}/repo/capture_markets.py &
sleep 2
echo fila >> {mk}/$(date -u +%F).csv
printf '%s\\n' "  ERROR polymarket: NameError: name 'x' is not defined" "[$(date -u +%FT%TZ)] === Fin ===" "[$(date -u +%FT%TZ)] === Captura wallets ===" "  ERROR leaderboard VOL MONTH: HTTPError: 400 Client Error" >> {slow}
wait
''')
    sim = subprocess.Popen(["bash", str(sp)], start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        r = run(rsb, "--ejecutar", extra={"P6_ESPERA_S": "90", "P6_PASO": "1", "P6_CICLO_S": "60"})
    finally:
        sim.kill()
    assert r.returncode == 1 and "error de codigo en el ciclo NUEVO de capture_markets" in r.stdout and "NameError" in r.stdout, r.stdout[-3500:]
    assert "marcha atras hecha (ok)" in r.stdout.lower() and estado(rsb) == ORIG and len(_hijos_de(rsb)) == 1, r.stdout[-3500:]
