"""Harness del script de despliegue en un sandbox (REPO/DL/locks falsos; DEPLOY_SANDBOX=1 aborta si alguna ruta es la real).
Stubs en PATH: `screen` y `ps`; verify_deploy.py falso (modo ok / nolog / dos hijos). Nada toca el sistema real."""
import hashlib, json, os, shutil, subprocess, sys, time
from pathlib import Path
import pytest

V3 = Path(__file__).resolve().parent.parent
SCRIPT = V3 / "deploy" / "deploy_deltas_libro_ws_once.sh"
REAL = Path("/root/polymarket-research")
BASE_LIBRO = V3 / "diffs" / "libro_estado_ws.main_orig_a_v3.diff"
PY = REAL / ".venv" / "bin" / "python"


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def _base_libro(dst):
    """Reconstruye la base original de main (a0196...) a partir del objetivo y el diff invertido (no depende de lo desplegado hoy)."""
    subprocess.run(["patch", "-R", "-s", "-o", str(dst), str(V3 / "delta_v3" / "libro_estado_ws.py"), str(BASE_LIBRO)], check=True)
    assert sha(dst).startswith("a0196ee4")


def _base_capture(dst):
    subprocess.run(["patch", "-R", "-s", "-o", str(dst), str(V3 / "stage" / "capture_markets.py"), str(V3 / "diffs" / "capture_markets.main_a_v3.diff")], check=True)
    assert sha(dst).startswith("5e2706bb")




def e2e_sha_py(sembrar="/no/existe"):
    """sha del sello e2e: igual que lib::e2e_sha (cat de los ficheros EN ESTE ORDEN; los que no existen se omiten)."""
    fs = [SCRIPT, V3 / "deploy/lib_espera_hijos.sh", V3 / "deploy/p6_ciclo_aislado.py", V3 / "deploy/clases_error.conf", Path(sembrar), V3 / "delta_v3/libro_estado_ws.py", V3 / "stage/capture_markets.py", V3 / "stage/universo_5m_io.py"]
    return hashlib.sha256(b"".join(f.read_bytes() for f in fs if f.exists())).hexdigest()[:32]


def sellar(sb, **kw):
    d = sb / "dl/traspaso_deltas_ws"; d.mkdir(parents=True, exist_ok=True)
    (d / "e2e_ok.json").write_text(json.dumps({"sha": e2e_sha_py(), "ts": int(time.time()), "pasados": 5, **kw}))


def env_de(sb, hora="03:15", modo="ok", extra=None):
    env = {"PATH": f"{sb}/bin:" + os.environ["PATH"], "SB": str(sb), "REPO": str(sb / "repo"), "DL": str(sb / "dl"), "V3": str(V3), "PY": str(PY),
           "LIBRO5": str(sb / "libro5"), "LOGOBS": str(sb / "repo/logs/observadores_fase0.log"), "WDLOG": str(sb / "repo/logs/watchdog.log"),
           "RAMLOCK": str(sb / "ramlock"), "LOADAVG": str(sb / "loadavg"), "CFGDIR": str(sb / "dl/universo_5m"), "MIN_GB": "0",
           "DEPLOY_SANDBOX": "1", "SANDBOX_HORA": hora, "FAKE_VD_MODE": modo, "P2_SLEEP": "0", "P5_CONN_S": "6", "P5_MUEREN_S": "3", "WD_PERIODO": "0.5",
           "WD_MARGEN": "0", "P5_PASO": "0.5", "P5_ESTABLE_S": "1", "P5_BN_S": "2", "P0_BN_S": "1", "P5_CRECE_S": "5", "P5_SCREEN_S": "2", "P5_TERM_S": "999",
           "P6_ESPERA_S": "0", "P6_AISLADO": "1", "P6_RUNNER": str(sb / "p6_runner.py"), "P6_ESTABLE_ADEL_S": "0", "SEMBRAR_PY": "/no/existe", "P5_G_S": "1", "HOME": os.environ.get("HOME", "/root")}
    env.update(extra or {})
    return env


@pytest.fixture
def sb(tmp_path):
    sb = tmp_path / "sb"
    for d in ("repo/logs", "dl", "libro5", "bin"):
        (sb / d).mkdir(parents=True)
    _base_libro(sb / "repo/libro_estado_ws.py")
    _base_capture(sb / "repo/capture_markets.py")
    shutil.copy(REAL / "data_quality.py", sb / "repo")
    shutil.copy(V3 / "tests" / "fake_verify_deploy.py", sb / "repo/verify_deploy.py")
    (sb / "repo/pipeline_watchdog.py").write_text('SCREEN_RESTART = {\n    "observadores": f"cd {REPO} && nice -n 10 choom -n -300 -- .venv/bin/python observadores_fase0.py >> logs/observadores_fase0.log 2>&1",\n}\n')
    (sb / "repo/logs/watchdog.log").write_text("2026-11-13 12:00:00 tick\n")
    (sb / "repo/logs/observadores_fase0.log").write_text("log previo\n")
    (sb / "ps_out").write_text("800 1 .venv/bin/python observadores_fase0.py\n5555 800 python -u %s/repo/libro_estado_ws.py --hijo\n" % sb)
    (sb / "repo/logs/slow.log").write_text("slow previo\n")
    (sb / "bin/screen").write_text("#!/bin/bash\necho '123.observadores (Detached)'; echo '124.vigiasfreq (Detached)'\n")
    (sb / "bin/ps").write_text("#!/bin/bash\ncat \"$SB/ps_out\"\n")
    for f in ("screen", "ps"):
        (sb / "bin" / f).chmod(0o755)
    (sb / "loadavg").write_text("0.10 0.10 0.10 1/100 1\n")
    (sb / "p6_runner.py").write_text("import os, sys, time\ntime.sleep(float(os.environ.get('P6_STUB_SLEEP', '0')))\nrc = int(os.environ.get('P6_STUB_RC', '0'))\nprint(os.environ.get('P6_STUB_MSG', 'FALLO intento 1: stub' if rc == 1 else 'OK stub'))\nsys.exit(rc)\n")      # sustituto del runner real (probado en test_p6_y_seed.py)
    # bnreg falso: proceso vivo + lock de Binance retenido por otro proceso
    (sb / "dl/.binance_registro.lock").write_text("")
    holder = subprocess.Popen(["flock", str(sb / "dl/.binance_registro.lock"), "sleep", "600"])      # = bnreg: el pid que figura en /proc/locks
    (sb / "dl/.binance_registro.lock").write_text(f"bnreg pid={holder.pid}\n")
    (sb / "dl/BNREG_HABILITADO").write_text("")
    sellar(sb)
    (sb / "dl/binance_registro_estado.json").write_text(json.dumps({"pid": holder.pid, "estado": "activo", "lock": True, "ts": int(time.time() * 1000) + 10**8}))
    # ticker del watchdog (el script espera un tick)
    tick = subprocess.Popen(["bash", "-c", f'while true; do sleep 0.3; echo "$(date +%s.%N) tick" >> {sb}/repo/logs/watchdog.log; done'])
    time.sleep(0.5)
    yield sb
    for p in (holder, tick):
        p.kill()
        p.wait()
    if (sb / "pids").exists():
        for x in (sb / "pids").read_text().split():
            try:
                os.kill(int(x), 9)
            except OSError:
                pass


def run(sb, *args, hora="03:15", modo="ok", extra=None):
    return subprocess.run(["bash", str(SCRIPT), *args], capture_output=True, text=True, env=env_de(sb, hora, modo, extra), timeout=240)


def estado(sb):
    return (sha(sb / "repo/libro_estado_ws.py")[:8], sha(sb / "repo/capture_markets.py")[:8], (sb / "repo/universo_5m_io.py").exists())


ORIG = ("a0196ee4", "5e2706bb", False)


def test_dry_run_no_cambia_nada_y_las_guardas_pasan(sb):
    r = run(sb)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "Modo dry-run: no se cambio nada" in r.stdout and "FALLA" not in r.stdout
    assert estado(sb) == ORIG and not (sb / "vd_calls.txt").exists()


def test_sandbox_aborta_si_una_ruta_es_la_real(sb):
    r = run(sb, extra={"DL": "/root/polymarket-research-datalogs"})
    assert r.returncode == 3 and "SANDBOX" in r.stdout


@pytest.mark.parametrize("hora", ["07:00", "15:00", "19:50", "23:50"])
def test_horas_prohibidas_fallan_en_dry_run(sb, hora):
    r = run(sb, hora=hora)
    assert r.returncode == 1 and "FALLA fuera de" in r.stdout and estado(sb) == ORIG


def test_despliegue_ok_copia_los_3_ficheros_reinicia_una_vez_y_no_activa(sb):
    r = run(sb, "--ejecutar")
    assert r.returncode == 0, r.stdout + r.stderr
    assert sha(sb / "repo/libro_estado_ws.py") == sha(V3 / "delta_v3/libro_estado_ws.py")
    assert sha(sb / "repo/capture_markets.py") == sha(V3 / "stage/capture_markets.py")
    assert sha(sb / "repo/universo_5m_io.py") == sha(V3 / "stage/universo_5m_io.py")
    assert (sb / "vd_calls.txt").read_text().split() == ["observadores", "ok"]               # UN solo reinicio
    assert not (sb / "dl/universo_5m/cfg_CAPTURE_5M_HORIZONTE_MIN").exists() and "NO activado" in r.stdout
    assert (sb / "dl/traspaso_deltas_ws/libro_estado_ws.py.pre").exists() and not (sb / "dl/traspaso_deltas_ws/universo_5m_io.py.pre").exists()


def test_idempotente_segunda_ejecucion_no_reinicia(sb):
    assert run(sb, "--ejecutar").returncode == 0
    n = (sb / "vd_calls.txt").read_text()
    r = run(sb, "--ejecutar")
    assert r.returncode == 0 and "YA DESPLEGADO" in r.stdout and (sb / "vd_calls.txt").read_text() == n


def test_activar_y_sustituye_restart_ram(sb):
    r = run(sb, "--ejecutar", "--activar", "--sustituye-restart-ram", extra={"CONFIRMO_ADELANTO_6_MONEDAS": "1"})
    assert r.returncode == 0, r.stdout + r.stderr
    assert (sb / "vd_calls.txt").read_text().split() == ["observadores", "ok", "vigiasfreq", "ok"]
    assert (sb / "dl/universo_5m/cfg_CAPTURE_5M_HORIZONTE_MIN").read_text().strip() == "1440"
    assert (sb / "dl/universo_5m/cfg_CAPTURE_429_FIX").read_text().strip() == "1"
    assert r.stdout.index("P1 flock restart_ram_fase0 (temprano") < r.stdout.index("P0b: carga ok")      # M7: el lock ANTES de la espera de carga


def test_activar_sin_confirmar_las_6_monedas_se_ignora(sb):
    r = run(sb, "--ejecutar", "--activar")
    assert r.returncode == 4 and "--activar RECHAZADO (rc 4)" in r.stdout and not (sb / "dl/universo_5m/cfg_CAPTURE_5M_HORIZONTE_MIN").exists()      # #1: rechazado en P0, rc 4 + aviso critico
    assert estado(sb) == ORIG, "rechazado antes de tocar nada"


def test_parte_de_v5_tambien_vale(sb):
    v5 = sb / "v5.py"
    subprocess.run(["patch", "-s", "-o", str(v5), str(sb / "repo/libro_estado_ws.py"), str(V3 / "diffs" / "libro_estado_ws.main_orig_a_v3.diff")], check=True)
    # v5 real (huecos_causa_13nov/stage): main = v5 => el diff v5->v3 debe aplicar
    v5real = REAL / "experimentos/5m_barato/l2_carrera_10nov/calma_v3/huecos_causa_13nov/stage/libro_estado_ws.py"
    assert sha(v5real).startswith("f306815c")
    shutil.copy(v5real, sb / "repo/libro_estado_ws.py")
    r = run(sb, "--ejecutar")
    assert r.returncode == 0, r.stdout + r.stderr
    assert sha(sb / "repo/libro_estado_ws.py") == sha(V3 / "delta_v3/libro_estado_ws.py")


@pytest.mark.parametrize("modo", ["viejos_salen", "ajeno", "tb_apagado", "bn_vuelve", "traceback", "tb_apagado_y_real", "tb_websockets"])
def test_casos_tolerados_no_hacen_marcha_atras(sb, modo):
    """Viejos que salen, hijo ajeno de otro padre, traceback de apagado, bnreg que tarda, Traceback real / de websockets con el libro5 creciendo (mercado quieto: solo G/B)."""
    r = run(sb, "--ejecutar", modo=modo)
    assert r.returncode == 0 and "MARCHA ATRAS" not in r.stdout, r.stdout
    assert estado(sb)[0] != ORIG[0]                                                            # quedo desplegado
    assert (sb / "vd_calls.txt").read_text().split() == ["observadores", modo]                 # UN solo reinicio


@pytest.mark.parametrize("modo,frag", [("nolog", "ningun 'conectado"), ("dos", "RESPAWN del hijo o hijo extra"), ("transitorio", "RESPAWN del hijo o hijo extra"),
                                      ("respawn", "respawn"), ("bn_pierde", "bnreg sin latido fresco"),
                                      ("viejo_no_sale", "viejos aun vivos '5555'"), ("cero", "= 0 hijos"),
                                      ("mudo", "NO crece"), ("tb_websockets_mudo", "NO crece")])
def test_fallo_duro_hace_marcha_atras_automatica_y_verificada(sb, modo, frag):
    r = run(sb, "--ejecutar", modo=modo)
    assert r.returncode == 1 and frag.lower() in r.stdout.lower() and "MARCHA ATRAS" in r.stdout, r.stdout
    assert estado(sb) == ORIG                                                                  # los 3 restaurados; universo_5m_io borrado
    assert (sb / "vd_calls.txt").read_text().split()[-2:] == ["observadores", "ok"]            # 2a llamada = la de la marcha atras
    assert "marcha atras hecha (OK)" in r.stdout and "marcha atras OK" in r.stdout            # verificada (hijo + libro5) y el aviso va DESPUES con el resultado
    assert r.stdout.index("marcha atras hecha (OK)") < r.stdout.index("CRITICO deploy deltas libro_ws: FALLO tras el despliegue")
    assert not (sb / "dl/universo_5m/cfg_CAPTURE_5M_HORIZONTE_MIN").exists()


def test_marcha_atras_que_falla_lo_dice_en_el_aviso(sb):
    r = run(sb, "--ejecutar", modo="dos", extra={"FAKE_VD_MODE_RB": "cero"})
    assert r.returncode == 1 and "marcha atras hecha (FALLO)" in r.stdout and "marcha atras FALLO" in r.stdout, r.stdout
    assert estado(sb) == ORIG                                                                  # los ficheros SI quedan restaurados; lo que falla es el reinicio verificado


def test_script_interrumpido_entre_cp_y_reinicio_restaura_y_avisa(sb):
    import signal
    p = subprocess.Popen(["bash", str(SCRIPT), "--ejecutar"], env=env_de(sb, modo="cuelga"), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    t0 = time.time()
    while not (sb / "vd_calls.txt").exists() and time.time() - t0 < 120:       # el 1er verify_deploy ya esta colgado: main ya tiene el codigo nuevo
        time.sleep(0.2)
    assert estado(sb)[0] != ORIG[0]
    p.send_signal(signal.SIGTERM)
    out = p.communicate(timeout=120)[0]
    assert p.returncode == 143 and "script interrumpido/terminado" in out and "marcha atras hecha (OK)" in out, out
    assert estado(sb) == ORIG


@pytest.mark.parametrize("gamma_previo", [False, True])
def test_marcha_atras_borra_gamma_pausa_solo_si_la_creo_el_despliegue(sb, gamma_previo):
    gp = sb / "dl/universo_5m/gamma_pausa.json"
    if gamma_previo:
        gp.parent.mkdir(parents=True, exist_ok=True); gp.write_text("{}")
    r = run(sb, "--ejecutar", modo="dos", extra={"FAKE_VD_GAMMA": "1"})
    assert r.returncode == 1 and estado(sb) == ORIG
    assert gp.exists() == gamma_previo, r.stdout


def test_pre_base_existente_no_se_sobrescribe_si_main_ya_es_el_objetivo(sb):
    """Despliegue parcial previo: main/libro ya es v3 pero capture sigue en base. El .pre de libro (base) debe conservarse y el despliegue acabar bien."""
    pre = sb / "dl/traspaso_deltas_ws"; pre.mkdir(parents=True, exist_ok=True)
    shutil.copy(sb / "repo/libro_estado_ws.py", pre / "libro_estado_ws.py.pre")
    base_sha = sha(pre / "libro_estado_ws.py.pre")
    shutil.copy(V3 / "delta_v3/libro_estado_ws.py", sb / "repo/libro_estado_ws.py")
    r = run(sb, "--ejecutar")
    assert r.returncode == 0, r.stdout
    assert sha(pre / "libro_estado_ws.py.pre") == base_sha and base_sha.startswith("a0196ee4")


def test_main_ya_objetivo_sin_pre_base_aborta(sb):
    shutil.copy(V3 / "delta_v3/libro_estado_ws.py", sb / "repo/libro_estado_ws.py")
    r = run(sb, "--ejecutar")
    assert r.returncode == 1 and "backup .pre fallido" in r.stdout and not (sb / "vd_calls.txt").exists()


def test_base_desconocida_aborta_sin_tocar_nada(sb):
    with open(sb / "repo/libro_estado_ws.py", "a") as f:
        f.write("# alguien edito main\n")
    r = run(sb, "--ejecutar")
    assert r.returncode == 1 and "FALLA GUARDA DE BASE" in r.stdout and not (sb / "vd_calls.txt").exists()
    assert not (sb / "repo/universo_5m_io.py").exists() and sha(sb / "repo/capture_markets.py").startswith("5e2706bb")


def test_cambio_de_main_durante_la_espera_aborta(sb):
    """P2 espera un tick del watchdog: si main cambia en ese intervalo, la guarda de base se repite y aborta."""
    import threading
    def tocar():
        time.sleep(0.2)
        with open(sb / "repo/capture_markets.py", "a") as f:
            f.write("# cambio concurrente\n")
    # el cambio llega despues de P0 (que tarda varios s por el harness): lo provocamos con un P2_SLEEP largo
    th = threading.Thread(target=lambda: (time.sleep(6), tocar()))
    th.start()
    r = run(sb, "--ejecutar", extra={"P2_SLEEP": "12"})
    th.join()
    assert r.returncode == 1 and "GUARDA DE BASE" in r.stdout and not (sb / "vd_calls.txt").exists()
    assert not (sb / "repo/universo_5m_io.py").exists()


def test_lock_de_restart_ram_ocupado_aborta(sb):
    h = subprocess.Popen(["flock", str(sb / "ramlock"), "sleep", "120"])
    time.sleep(0.5)
    try:
        r = run(sb, "--ejecutar", extra={"P1_TIMEOUT": "1"})
    finally:
        h.kill()
    assert r.returncode == 1 and "no se pudo tomar" in r.stdout and estado(sb) == ORIG


def test_bnreg_latido_viejo_aborta_en_dry_run(sb):
    e = json.loads((sb / "dl/binance_registro_estado.json").read_text()); e["ts"] = 1000
    (sb / "dl/binance_registro_estado.json").write_text(json.dumps(e))
    r = run(sb)
    assert r.returncode == 1 and "FALLA bnreg activo" in r.stdout


def test_bnreg_sin_lock_aborta_en_dry_run(sb):
    (sb / "dl/BNREG_HABILITADO").unlink()
    r = run(sb)
    assert r.returncode == 1 and "FALLA centinela" in r.stdout


def test_sha256sums_alterado_aborta(sb, tmp_path):
    v = tmp_path / "v3copia"
    shutil.copytree(V3, v, ignore=shutil.ignore_patterns("__pycache__", "medicion"))
    (v / "stage/capture_markets.py").write_text((v / "stage/capture_markets.py").read_text() + "\n# alterado\n")
    r = run(sb, extra={"V3": str(v)})
    assert r.returncode == 1 and "FALLA SHA256SUMS" in r.stdout


# ====================================================================== 2a pasada de revision: hallazgos 1-9 y limites L1-L5
def _hasta(p, frag, tmax=120):
    out, t0 = "", time.time()
    while time.time() - t0 < tmax:
        l = p.stdout.readline()
        if not l:
            break
        out += l
        if frag in l:
            return out
    raise AssertionError(f"no salio '{frag}':\n{out}")


@pytest.mark.parametrize("confirma", [False, True])
def test_h1_ya_desplegado_con_activar_exige_la_misma_confirmacion(sb, confirma):
    assert run(sb, "--ejecutar").returncode == 0
    r = run(sb, "--ejecutar", "--activar", extra={"CONFIRMO_ADELANTO_6_MONEDAS": "1"} if confirma else None)
    assert r.returncode == (0 if confirma else 4) and ("YA DESPLEGADO" in r.stdout) == confirma        # #1: sin la confirmacion se rechaza en P0 (rc 4), ni siquiera llega a YA DESPLEGADO
    assert (sb / "dl/universo_5m/cfg_CAPTURE_5M_HORIZONTE_MIN").exists() == confirma and ("--activar RECHAZADO (rc 4)" in r.stdout) == (not confirma), r.stdout


def test_h8_ya_desplegado_no_toma_el_lock_ni_espera_ni_manda_critico(sb):
    assert run(sb, "--ejecutar").returncode == 0
    h = subprocess.Popen(["flock", str(sb / "ramlock"), "sleep", "60"]); time.sleep(0.5)       # restart_ram tiene el lock: antes aquello daba ABORTO + CRITICO
    try:
        r = run(sb, "--ejecutar", extra={"P1_TIMEOUT": "1"})
    finally:
        h.kill(); h.wait()
    assert r.returncode == 0 and "YA DESPLEGADO" in r.stdout and "CRITICO" not in r.stdout and "P1 flock" not in r.stdout, r.stdout


@pytest.mark.parametrize("modo,frag", [("cap_tb", "error de codigo"), ("cap_sin_crecer", "NO crecio"), ("cap_adelanto", "ESCRIBIO ficheros de adelanto")])
def test_p6_ciclo_real_fallo_duro_hace_marcha_atras(sb, modo, frag):
    r = run(sb, "--ejecutar", modo=modo, extra={"P6_ESPERA_S": "30", "P6_PASO": "0.3", "P6_CICLO_S": "20"})
    assert r.returncode == 1 and frag in r.stdout and "marcha atras hecha (OK)" in r.stdout and estado(sb) == ORIG, r.stdout


@pytest.mark.parametrize("modo", ["cap_ok", "cap_trans"])
def test_p6_ciclo_real_ok_y_transitorio_no_aborta(sb, modo):
    r = run(sb, "--ejecutar", modo=modo, extra={"P6_ESPERA_S": "30", "P6_PASO": "0.3", "P6_CICLO_S": "20"})
    assert r.returncode == 0 and "P6 ciclo real de capture_markets con el codigo nuevo" in r.stdout and "MARCHA ATRAS" not in r.stdout, r.stdout


@pytest.mark.parametrize("rc,esperado_rc,frag", [(1, 1, "captura aislada del codigo nuevo"), (2, 4, "NO VERIFICADO"), (0, 0, "ok (solo aislado)")])
def test_p6_aislado_veredictos(sb, rc, esperado_rc, frag):
    r = run(sb, "--ejecutar", extra={"P6_STUB_RC": str(rc), "P6_STUB_MSG": ("FALLO intento 1: " if rc == 1 else "") + "detalle del runner"})
    assert r.returncode == esperado_rc and frag in r.stdout, r.stdout
    assert ("MARCHA ATRAS" in r.stdout) == (rc == 1)                    # inconcluso + ciclo real omitido: desplegado SIN marcha atras y rc 4 propio
    if rc == 1:
        assert estado(sb) == ORIG


def test_h4_un_runner_roto_rc_1_sin_veredicto_fallo_es_inconcluso_no_marcha_atras(sb):
    r = run(sb, "--ejecutar", extra={"P6_STUB_RC": "1", "P6_STUB_MSG": "Traceback (most recent call last): runner roto"})
    assert r.returncode == 4 and "MARCHA ATRAS" not in r.stdout and "sin un veredicto" in r.stdout and estado(sb)[0] != ORIG[0], r.stdout


def test_p6_sin_ciclo_real_pero_aislado_ok_queda_verificado(sb):
    r = run(sb, "--ejecutar", extra={"P6_ESPERA_S": "2", "P6_PASO": "0.3"})
    assert r.returncode == 0 and "verificado por la captura aislada" in r.stdout and "MARCHA ATRAS" not in r.stdout, r.stdout


def test_p6_sin_ciclo_real_y_aislado_inconcluso_da_rc4_y_critico_sin_marcha_atras(sb):
    r = run(sb, "--ejecutar", extra={"P6_ESPERA_S": "2", "P6_PASO": "0.3", "P6_STUB_RC": "2"})
    assert r.returncode == 4 and "NO VERIFICADO" in r.stdout and "CRITICO" in r.stdout and "MARCHA ATRAS" not in r.stdout and estado(sb)[0] != ORIG[0], r.stdout


def test_h3_marcha_atras_desde_p6_retoma_el_lock_de_restart_ram(sb):
    """El lock se libero antes de P6: una marcha atras desde P6 lo retoma (no hay 2o reinicio concurrente con restart_ram) y reinicia."""
    r = run(sb, "--ejecutar", extra={"P6_STUB_RC": "1"})
    assert r.returncode == 1 and "marcha atras hecha (OK)" in r.stdout and estado(sb) == ORIG
    assert (sb / "vd_calls.txt").read_text().split() == ["observadores", "ok", "observadores", "ok"]


def test_h3_si_no_puede_retomar_el_lock_no_reinicia_pero_restaura_y_lo_dice(sb):
    env = env_de(sb, extra={"P6_STUB_RC": "1", "P6_STUB_SLEEP": "4", "P1_TIMEOUT": "2"})
    p = subprocess.Popen(["bash", str(SCRIPT), "--ejecutar"], env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    out = _hasta(p, "== P6")
    h = subprocess.Popen(["flock", str(sb / "ramlock"), "sleep", "30"])             # restart_ram/guard_ram se lo queda mientras corre P6
    try:
        out += p.communicate(timeout=120)[0]
    finally:
        h.kill(); h.wait()
    assert p.returncode == 1 and "SIN REINICIAR" in out and "marcha atras hecha (FALLO)" in out and estado(sb) == ORIG, out
    assert (sb / "vd_calls.txt").read_text().split() == ["observadores", "ok"]          # NO hubo 2o reinicio


def test_h4_senales_durante_la_marcha_atras_se_difieren_y_se_completa(sb):
    import signal
    p = subprocess.Popen(["bash", str(SCRIPT), "--ejecutar"], env=env_de(sb, modo="dos", extra={"FAKE_VD_MODE_RB": "cuelga"}), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    out = _hasta(p, "MARCHA ATRAS")
    for s_ in (signal.SIGTERM, signal.SIGHUP, signal.SIGINT, signal.SIGTERM):
        p.send_signal(s_); time.sleep(0.4)
    out += p.communicate(timeout=180)[0]
    assert "marcha atras hecha (OK)" in out and "se recibio una senal durante la marcha atras" in out and "marcha atras OK" in out, out
    assert estado(sb) == ORIG and (sb / "vd_calls.txt").read_text().count("observadores") == 2


def test_h7_libro5_del_dia_anterior_no_da_falso_fallo(sb):
    """El hijo escribe un fichero de OTRA fecha (despliegue que cruza 00:00Z): el despliegue lo localiza por pid."""
    r = run(sb, "--ejecutar", extra={"FAKE_VD_FECHA": "2026-11-13"})
    assert r.returncode == 0 and "libro5_ms_2026-11-13_" in r.stdout and "OK: desplegado" in r.stdout and "MARCHA ATRAS" not in r.stdout, r.stdout


@pytest.mark.parametrize("cmd", ["nice -n 10 choom -n -300 -- .venv/bin/python -u observadores_fase0.py", "bash -c cd /x && .venv/bin/python observadores_fase0.py >> l 2>&1"])
def test_h9_padre_observadores_con_cmdline_envuelta(sb, cmd):
    (sb / "ps_out").write_text("800 1 %s\n5555 800 python -u %s/repo/libro_estado_ws.py --hijo\n" % (cmd, sb))
    r = run(sb, "--ejecutar", extra={"FAKE_OBS_CMD": cmd})
    assert r.returncode == 0 and "MARCHA ATRAS" not in r.stdout, r.stdout


def test_h9_padre_no_reconocido_falla_en_p0_con_mensaje_claro_sin_tocar_nada(sb):
    (sb / "ps_out").write_text("800 1 python lanzador_raro.py\n5555 800 python -u %s/repo/libro_estado_ws.py --hijo\n" % sb)
    r = run(sb, "--ejecutar")
    assert r.returncode == 1 and "FALLA hay hijo libro_estado_ws vivo y su padre" in r.stdout and "padre NO reconocido" in r.stdout and "lanzador_raro.py" in r.stdout, r.stdout
    assert estado(sb) == ORIG and not (sb / "vd_calls.txt").exists()


def test_l1_sin_sello_e2e_o_con_otro_sha_o_viejo_p0_falla(sb):
    st = sb / "dl/traspaso_deltas_ws/e2e_ok.json"
    st.unlink()
    r = run(sb, "--ejecutar")
    assert r.returncode == 1 and "FALLA ensayo e2e" in r.stdout and "no hay sello" in r.stdout and estado(sb) == ORIG and not (sb / "vd_calls.txt").exists(), r.stdout
    sellar(sb, sha="0" * 32)
    assert "OTRA version" in run(sb).stdout
    sellar(sb, ts=int(time.time()) - 30 * 3600)
    assert "mas de 24 h" in run(sb).stdout
    sellar(sb, pasados=4)
    assert "cubre 4 tests" in run(sb).stdout
    sellar(sb)
    assert run(sb).returncode == 0


def test_l4_contrato_con_verify_deploy_falla_si_cambia_el_formato(sb):
    f = sb / "repo/verify_deploy.py"
    f.write_text(f.read_text().replace("observadores FRESH", "observadores OK"))
    r = run(sb)
    assert r.returncode == 1 and "FALLA contrato con el verify_deploy REAL" in r.stdout and "formato cambiado" in r.stdout, r.stdout


@pytest.mark.parametrize("con_cfg", [True, False])
def test_l3_marcha_atras_con_adelanto_activo_para_el_capture_en_curso(sb, con_cfg):
    v = int(subprocess.run(["bash", "-c", "setsid sleep 300 >/dev/null 2>&1 & echo $!"], capture_output=True, text=True).stdout.strip())
    try:
        if con_cfg:
            (sb / "dl/universo_5m").mkdir(parents=True, exist_ok=True); (sb / "dl/universo_5m/cfg_CAPTURE_5M_HORIZONTE_MIN").write_text("1440")
        r = run(sb, "--ejecutar", modo="dos", extra={"P6_TERM_S": "1", "FAKE_PS_EXTRA": "%d 1 /x/python %s/repo/capture_markets.py\n" % (v, sb)})
        assert r.returncode == 1 and "marcha atras hecha (OK)" in r.stdout and estado(sb) == ORIG, r.stdout
        vivo = os.path.exists(f"/proc/{v}") and "zombie" not in open(f"/proc/{v}/status").read().lower()
        assert vivo != con_cfg                                                                   # con adelanto activo se para; sin cfg no se toca el ciclo en curso
        assert ("parado y sin escrituras de adelanto" in r.stdout) == con_cfg
        assert (sb / "dl/universo_5m/cfg_CAPTURE_5M_HORIZONTE_MIN").exists() == con_cfg      # #8: el cfg escrito A MANO no lo borra la marcha atras (solo los del manifiesto)
        assert ("escrito a mano" in r.stdout) == con_cfg
    finally:
        subprocess.run(["kill", "-9", str(v)], capture_output=True)


def test_l5_el_deploy_no_adquiere_nunca_el_lock_de_bnreg(sb):
    """Con bnreg dueno la comprobacion pasa y, sin dueno, falla -- siempre por /proc/locks: el lock sigue tomado por su dueno tras P0."""
    r = run(sb)
    assert r.returncode == 0 and "OK    bnreg activo y DUENO" in r.stdout
    assert subprocess.run(["flock", "-n", str(sb / "dl/.binance_registro.lock"), "true"]).returncode == 1       # sigue ocupado por el 'bnreg' del fixture


def test_activar_no_se_aplica_si_p6_quedo_sin_veredicto(sb):
    r = run(sb, "--ejecutar", "--activar", extra={"P6_ESPERA_S": "2", "P6_PASO": "0.3", "P6_STUB_RC": "2", "CONFIRMO_ADELANTO_6_MONEDAS": "1"})
    assert r.returncode == 4 and "--activar NO aplicado" in r.stdout and not (sb / "dl/universo_5m/cfg_CAPTURE_5M_HORIZONTE_MIN").exists(), r.stdout


# ====================================================================== 3a pasada de revision (definitiva): hallazgos 1-10
CAP_EXTRA = {"P6_ESPERA_S": "30", "P6_PASO": "0.3", "P6_CICLO_S": "20"}


def test_h1_un_1429_o_una_hora_no_excusan_que_data_markets_no_crezca(sb):
    r = run(sb, "--ejecutar", modo="cap_sin_crecer_1429", extra=CAP_EXTRA)
    assert r.returncode == 1 and "NO crecio" in r.stdout and estado(sb) == ORIG, r.stdout


def test_h1_un_429_real_si_excusa_que_no_crezca(sb):
    r = run(sb, "--ejecutar", modo="cap_sin_crecer_429", extra=CAP_EXTRA)
    assert r.returncode == 0 and "crecimiento no verificado en el ciclo real; verificado por la captura aislada" in r.stdout and "MARCHA ATRAS" not in r.stdout, r.stdout      # (4): el 429 solo excusa si la aislada vio crecer


def _sleeper():
    return int(subprocess.run(["bash", "-c", "setsid sleep 300 >/dev/null 2>&1 & echo $!"], capture_output=True, text=True).stdout.strip())


def test_h3_un_ciclo_que_ya_iba_a_mitad_al_desplegar_no_se_adopta(sb):
    """Un capture_markets arrancado ANTES del cp (codigo viejo) que solo se hace visible en `ps` despues NO es 'el ciclo nuevo': su Traceback/no-crecimiento no cuenta."""
    v = _sleeper()
    try:
        (sb / "repo/logs/slow.log").write_text("slow previo\n")
        r = run(sb, "--ejecutar", modo="cap_tb", extra={**CAP_EXTRA, "FAKE_CAP_VIEJO": "1", "FAKE_CAP_PID": str(v), "P6_ESPERA_S": "8"})
        assert r.returncode == 0 and "no aparecio un ciclo nuevo" in r.stdout and "verificado por la captura aislada" in r.stdout and "MARCHA ATRAS" not in r.stdout, r.stdout
    finally:
        subprocess.run(["kill", "-9", str(v)], capture_output=True)


def test_h3_un_ciclo_visto_ya_avanzado_no_se_adopta(sb):
    r = run(sb, "--ejecutar", modo="cap_tb", extra={**CAP_EXTRA, "P6_TARDE_MAX_S": "0", "P6_ESPERA_S": "6"})            # visto con >0 s de vida: tarde
    assert r.returncode == 0 and "no aparecio un ciclo nuevo" in r.stdout and "MARCHA ATRAS" not in r.stdout, r.stdout


def test_h3_un_ciclo_sin_cabecera_de_run_slow_en_el_log_no_es_atribuible(sb):
    r = run(sb, "--ejecutar", modo="cap_tb", extra={**CAP_EXTRA, "FAKE_SIN_INICIO": "1"})
    assert r.returncode == 0 and "no tiene la cabecera" in r.stdout and "MARCHA ATRAS" not in r.stdout and estado(sb)[0] != ORIG[0], r.stdout


def test_h5_el_despliegue_aborta_si_main_no_queda_apagado_por_cfg(sb):
    """Tras el despliegue cap_ok mira main: sin universo_5m_io en main el adelanto 'apagaria' por falta de modulo => DURO + marcha atras."""
    r = run(sb, "--ejecutar", extra={"FAKE_BORRA_IO": "1"})
    assert r.returncode == 1 and "falta de modulo" in r.stdout and "marcha atras hecha (OK)" in r.stdout and estado(sb) == ORIG, r.stdout


@pytest.mark.parametrize("hora,pasa", [("05:35", True), ("05:41", False), ("05:50", False), ("11:15", True), ("11:25", False), ("22:19", True), ("23:30", False)])
def test_h7_p0_exige_margen_hasta_la_proxima_ventana_prohibida(sb, hora, pasa):
    r = run(sb, hora=hora)
    assert (r.returncode == 0) == pasa and ("FALLA margen" in r.stdout) == (not pasa), r.stdout


def test_h7_p6_real_se_acota_para_no_cruzar_la_ventana(sb):
    """03:15 -> la proxima ventana (03:40) esta a 1500 s: con ciclo 1470 s y margen 20 s quedan 10 s."""
    r = run(sb, "--ejecutar", extra={"P6_ESPERA_S": "2400", "P6_CICLO_S": "1470", "P6_MARGEN_S": "20", "P6_PASO": "0.3"})
    assert r.returncode == 0 and "ciclo real ACOTADO a 10s" in r.stdout and "verificado por la captura aislada" in r.stdout, r.stdout


def test_h7_p6_real_se_omite_si_no_cabe_antes_de_la_ventana(sb):
    r = run(sb, "--ejecutar", extra={"P6_ESPERA_S": "2400", "P6_CICLO_S": "1600"})
    assert r.returncode == 0 and "ciclo real OMITIDO" in r.stdout and "ok (solo aislado)" in r.stdout, r.stdout


def test_h7_si_las_esperas_agotan_el_margen_se_aborta_antes_de_tocar_nada(sb):
    """P2b/P2 consumen tiempo: si al acabar queda < P3_MARGEN_MIN min hasta la ventana, aborta SIN modificar nada."""
    f = sb / "hora.txt"; f.write_text("03:15")
    p = subprocess.Popen(["bash", str(SCRIPT), "--ejecutar"], env=env_de(sb, extra={"SANDBOX_HORA_FILE": str(f), "P2_SLEEP": "3"}), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    out = _hasta(p, "== P2 esperar un tick"); f.write_text("03:35")                      # 5 min hasta el hueco de las 03:40
    out += p.communicate(timeout=120)[0]
    assert p.returncode == 1 and "queda menos de 10 min hasta la ventana prohibida" in out and estado(sb) == ORIG and not (sb / "vd_calls.txt").exists(), out


def _hora_en_p6(sb, ini="03:15"):
    """La hora (simulada) pasa a 07:00 DURANTE la captura aislada de P6 (la comprobacion de ventana de M2 ya paso, a las 03:15): al terminar P6 estamos dentro de la ventana 06:00-09:15."""
    f = sb / "hora.txt"; f.write_text(ini); r = sb / "p6_runner_hora.py"
    r.write_text("import os, sys, time\nopen(os.environ['SANDBOX_HORA_FILE'], 'w').write(os.environ.get('P6_STUB_HORA', '07:00'))\ntime.sleep(float(os.environ.get('P6_STUB_SLEEP', '0')))\n"
                 "rc = int(os.environ.get('P6_STUB_RC', '0')); print('FALLO intento 1: stub' if rc == 1 else 'OK stub'); sys.exit(rc)\n")
    return {"SANDBOX_HORA_FILE": str(f), "P6_RUNNER": str(r)}


def _hora_file(sb, ini="03:15"):
    f = sb / "hora.txt"; f.write_text(ini); return {"SANDBOX_HORA_FILE": str(f), "FAKE_VD_HORA": "07:00"}      # al reiniciar observadores entra la ventana 06:00-09:15


def test_h7_fallo_de_p5_en_ventana_prohibida_prevalece_restaurar_y_reiniciar_con_aviso(sb):
    r = run(sb, "--ejecutar", modo="dos", extra=_hora_file(sb))
    assert r.returncode == 1 and "AVISO EXPLICITO: marcha atras COMPLETA con reinicio de observadores DENTRO de una ventana prohibida" in r.stdout, r.stdout
    assert estado(sb) == ORIG and (sb / "vd_calls.txt").read_text().split()[-2:] == ["observadores", "ok"] and "marcha atras hecha (OK)" in r.stdout


def test_h7_fallo_de_p6_en_ventana_prohibida_restaura_capture_y_no_reinicia_observadores(sb):
    r = run(sb, "--ejecutar", extra={**_hora_en_p6(sb), "P6_STUB_RC": "1"})
    assert r.returncode == 1 and "marcha atras hecha (PARCIAL)" in r.stdout and "SIN REINICIAR observadores (ventana prohibida" in r.stdout, r.stdout
    assert sha(sb / "repo/capture_markets.py").startswith(ORIG[1]) and sha(sb / "repo/libro_estado_ws.py") == sha(V3 / "delta_v3/libro_estado_ws.py")      # libro/io verificados quedan
    assert (sb / "repo/universo_5m_io.py").exists() and (sb / "vd_calls.txt").read_text().split() == ["observadores", "ok"]                               # UN solo reinicio


def test_h7_activar_se_difiere_dentro_de_una_ventana_prohibida(sb):
    r = run(sb, "--ejecutar", "--activar", extra={**_hora_en_p6(sb), "CONFIRMO_ADELANTO_6_MONEDAS": "1"})
    assert r.returncode == 4 and "--activar NO aplicado: estamos dentro de una ventana prohibida" in r.stdout and not (sb / "dl/universo_5m/cfg_CAPTURE_429_FIX").exists(), r.stdout


@pytest.mark.parametrize("fichero", ["capture_markets.py", "libro_estado_ws.py"])
def test_h8_la_marcha_atras_no_pisa_un_main_que_cambio_por_otra_mano(sb, fichero):
    env = env_de(sb, extra={"P6_STUB_RC": "1", "P6_STUB_SLEEP": "4"})
    p = subprocess.Popen(["bash", str(SCRIPT), "--ejecutar"], env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    out = _hasta(p, "== P6")
    with open(sb / "repo" / fichero, "a") as f:
        f.write("# edicion manual posterior al despliegue\n")
    editado = sha(sb / "repo" / fichero)
    out += p.communicate(timeout=120)[0]
    assert p.returncode == 1 and sha(sb / "repo" / fichero) == editado, out                                      # NO se pisa
    assert "CAMBIO tras el despliegue" in out and "CRITICO" in out and "marcha atras hecha (FALLO)" in out, out
    otros = {"capture_markets.py": ["libro_estado_ws.py"], "libro_estado_ws.py": ["capture_markets.py"]}[fichero]
    assert sha(sb / "repo" / otros[0]).startswith(ORIG[0] if otros[0].startswith("libro") else ORIG[1]) and not (sb / "repo/universo_5m_io.py").exists()   # lo demas SI se restaura


def test_h8_un_cp_a_medias_se_restaura_aunque_el_fichero_no_coincida_con_nada(sb):
    # C: la copia a main es ATOMICA (temporal *.deltatmp.* + mv): un cp que muere a medias deja un temporal parcial, NUNCA un main parcial; se borra el temporal y se hace la marcha atras.
    (sb / "bin/cp").write_text('#!/bin/bash\ncase "$*" in *capture_markets.py.deltatmp.*) [ -e "$SB/cp_fallo" ] || { : > "$SB/cp_fallo"; echo "parcial" > "${@: -1}"; exit 1; };; esac\nexec /bin/cp "$@"\n'); (sb / "bin/cp").chmod(0o755)
    r = run(sb, "--ejecutar")
    assert r.returncode == 1 and "cp fallido" in r.stdout and estado(sb) == ORIG and (sb / "cp_fallo").exists() and not list((sb / "repo").glob("*.deltatmp.*")), r.stdout


def test_h8_activar_registra_en_un_manifiesto_lo_que_escribe(sb):
    r = run(sb, "--ejecutar", "--activar", extra={"CONFIRMO_ADELANTO_6_MONEDAS": "1"})
    assert r.returncode == 0, r.stdout
    m = list((sb / "dl/traspaso_deltas_ws").glob("cfg_manifest_*.txt"))
    assert len(m) == 1 and [Path(x).name for x in m[0].read_text().split()] == ["cfg_CAPTURE_429_FIX", "cfg_CAPTURE_5M_HORIZONTE_MIN"]


@pytest.mark.parametrize("estropea", ["lib", "sin_linea"])
@pytest.mark.parametrize("modo", [(), ("--ejecutar",)])
def test_h9_la_lib_se_verifica_antes_de_cargarla_y_no_se_ejecuta_nada_si_no_coincide(sb, tmp_path, estropea, modo):
    v = tmp_path / "v3copia"
    shutil.copytree(V3, v, ignore=shutil.ignore_patterns("__pycache__", "medicion"))
    if estropea == "lib":
        (v / "deploy/lib_espera_hijos.sh").write_text((v / "deploy/lib_espera_hijos.sh").read_text() + "\necho LIB_ALTERADA_EJECUTADA\n")
    else:
        (v / "SHA256SUMS").write_text("".join(l for l in (v / "SHA256SUMS").read_text().splitlines(True) if "lib_espera_hijos.sh" not in l))
    r = run(sb, *modo, extra={"V3": str(v)})
    assert r.returncode == 2 and "no coincide con" in r.stdout and "LIB_ALTERADA_EJECUTADA" not in r.stdout and "P0 comprobaciones" not in r.stdout, r.stdout
    assert estado(sb) == ORIG and not (sb / "vd_calls.txt").exists()


def test_h10_el_v5_es_un_wrapper_que_no_ejecuta_y_no_hay_segundo_sembrador(sb):
    w = V3.parent.parent / "huecos_causa_13nov/stage/deploy_tokens_cache_once.sh"
    assert len(w.read_text().splitlines()) <= 10 and "cp " not in w.read_text() and not (w.parent / "sembrar_cache_tokens.py").exists()
    r = subprocess.run(["bash", str(w), "--ejecutar"], capture_output=True, text=True, env=env_de(sb), timeout=60)
    assert r.returncode == 2 and "SUPERADO" in r.stderr and "rechazado" in r.stderr and estado(sb) == ORIG and not (sb / "vd_calls.txt").exists()
    r = subprocess.run(["bash", str(w)], capture_output=True, text=True, env=env_de(sb), timeout=120)                 # sin --ejecutar: redirige al dry-run de v3
    assert r.returncode == 0 and "SUPERADO" in r.stderr and "Modo dry-run: no se cambio nada" in r.stdout and estado(sb) == ORIG
