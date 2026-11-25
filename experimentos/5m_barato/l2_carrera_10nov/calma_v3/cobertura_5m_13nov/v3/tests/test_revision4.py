"""4a pasada (red-team final): B1 (cabecera duplicada del formato REAL de slow.log), M1 (segmento acotado a capture_markets), M3 (clases de error de codigo), M4 (estado de
restart_ram), M6 (periodo del watchdog medido), I1/I2 (avisos y --activar sobre YA DESPLEGADO), M2 (tope de ventana de la captura aislada), M5/M7/(d)/(e).
Los fixtures de tests/fixtures/ son TROZOS REALES (14-Nov) de logs/slow.log (ciclos 2737 y 2723) y logs/watchdog.log: el formato no es sintetico."""
import importlib.util, json, subprocess, sys, time, os
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_espera_hijos import sh, V3, LIB, REPO                                           # noqa: E402
from test_deploy_sandbox import sb, run, env_de, estado, ORIG, CAP_EXTRA, _hora_file, _hora_en_p6, _hasta, SCRIPT, sha, e2e_sha_py   # noqa: E402,F401

FIX = V3 / "tests" / "fixtures"
_spec = importlib.util.spec_from_file_location("p6_ciclo_aislado", V3 / "deploy/p6_ciclo_aislado.py")
P6 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(P6)
HDR = "[t] --- Ciclo slow 5 ---\n" * 2                                                   # run_slow.sh:14 log() hace tee -a al mismo log que el screen: SIEMPRE dos veces
FIN = "[t] === Fin ===\n[t] === Captura wallets ===\n  ERROR leaderboard VOL MONTH: HTTPError: 400 Client Error: Bad Request for url: https://data-api\n  Error en posiciones de 0xabc: ValueError\n"
COMPL = "[t] --- Ciclo slow 5 completado ---\n" * 2


# ---------------------------------------------------------------- B1 / M1: segmento del ciclo en el formato REAL
def test_b1_segmento_real_ciclo_2737_acotado_a_capture_markets(tmp_path):
    out = sh(tmp_path, f'slow_segmento {FIX}/slow_real_2737.log 0 2737').splitlines()
    assert len(out) == 115 and out[0] == out[1] and "Ciclo slow 2737 ---" in out[0], (len(out), out[:2])     # las 2 cabeceras identicas NO cortan
    assert out[-1].endswith("=== Fin ===") and not any("Captura wallets" in l or "ValueError" in l or "Traceback" in l or "400 Client Error" in l for l in out)
    assert len(sh(tmp_path, f'slow_segmento {FIX}/slow_real_2737.log 0 2738').splitlines()) == 29        # el ciclo siguiente (en curso) tambien
    assert sh(tmp_path, f'slow_segmento {FIX}/slow_real_2737.log 0 2999') == ""                          # un ciclo que no esta => vacio (no atribuible)


def test_b1_segmento_real_con_429_de_gamma(tmp_path):
    out = sh(tmp_path, f'slow_segmento {FIX}/slow_real_429_2723.log 0 2723')
    assert out.count("429 Client Error") == 50 and "Captura wallets" not in out and out.rstrip().endswith("=== Fin ===")


def _verifica_real(tmp_path, previo, cabecera, cuerpo, crece):
    slow = tmp_path / "slow.log"; slow.write_text(previo)
    (tmp_path / "cab.txt").write_text(cabecera); (tmp_path / "cuerpo.txt").write_text(cuerpo)
    grow = 'echo fila >> $MARKETS_DIR/$(date -u +%F).csv; ' if crece else ""
    return sh(tmp_path, f'''
cap_pre=""; P6_MARCA_TS=$(( $(date +%s) - 10 )); P6_MARCA_OFF=$(stat -c %s {slow}); MARKETS_DIR={tmp_path}/mk; mkdir -p $MARKETS_DIR
cat {tmp_path}/cab.txt >> {slow}
setsid sleep 2 & p=$!; echo "$p 1 python {REPO}/capture_markets.py" > "$PSF"
(sleep 1; {grow} cat {tmp_path}/cuerpo.txt >> {slow}) &
P6_ESPERA_S=10 P6_PASO=0.3 verifica_capture {slow}; echo "rc=$? $CAP_MOTIVO"''', env={"P6_CICLO_S": "20"}, timeout=60)


def _real_2737():
    ls = (FIX / "slow_real_2737.log").read_text().splitlines(keepends=True)
    i = next(k for k, l in enumerate(ls) if "Ciclo slow 2737 ---" in l)
    return "".join(ls[:i]), "".join(ls[i:i + 2]), "".join(ls[i + 2:])


def test_b1_ciclo_real_2737_con_crecimiento_y_errores_ajenos_de_wallets_pasa(tmp_path):
    previo, cab, cuerpo = _real_2737()                                      # su capture_wallets trae HTTPError 400 y 13 ValueError: NO son del capture_markets
    out = _verifica_real(tmp_path, previo, cab, cuerpo, crece=True)
    assert "rc=0" in out, out


def test_m1_httperror_de_wallets_no_es_excusa_si_data_markets_no_crece(tmp_path):
    previo, cab, cuerpo = _real_2737()
    out = _verifica_real(tmp_path, previo, cab, cuerpo, crece=False)         # el ciclo real 2737 no tiene 429 en SU capture_markets: sin crecer => FALLO
    assert "rc=1" in out and "NO crecio" in out, out


def test_b1_ciclo_real_con_429_de_gamma_excusa_el_no_crecimiento(tmp_path):
    ls = (FIX / "slow_real_429_2723.log").read_text().splitlines(keepends=True)
    i = next(k for k, l in enumerate(ls) if "Ciclo slow 2723 ---" in l)
    out = _verifica_real(tmp_path, "".join(ls[:i]), "".join(ls[i:i + 2]), "".join(ls[i + 2:]), crece=False)
    assert "rc=2" in out and "crecimiento no verificado" in out, out          # #7: la excusa 429 ya NO aprueba sin crecimiento: inconcluso (el llamador exige la aislada OK)


@pytest.mark.parametrize("cuerpo,rc,frag", [
    ("  ERROR polymarket: NameError: name 'x' is not defined\n" + FIN, 1, "error de codigo"),                                  # B1: con 2 cabeceras el awk viejo no lo veia
    ("  ERROR polymarket: ValueError: boom\n" + FIN, 1, "error de codigo"),                                                    # T2: ERROR polymarket con clase de datos = codigo propio (try/except Exception: print)
    ("  Error gamma slug=x offset=0: ValueError: respuesta rara\n" + FIN, 0, ""),                                              # #3: 'Error gamma' (respuesta malformada) con crecimiento: no revierte
    ("  ERROR polymarket: OSError: disco lleno\n" + FIN, 1, "error de codigo"),                                                # M3
    ("  ERROR precios: RuntimeError: boom\n" + FIN, 1, "error de codigo"),
    ("  ERROR polymarket: OSError: [Errno 110] Connection timed out\n" + FIN, 0, ""),                                          # OSError transitorio: no es de codigo
    ("  Error gamma slug=bitcoin offset=0: HTTPError: 429 Client Error: Too Many Requests for url: https://gamma\n" + FIN, 0, ""),
    ("  nada\n" + FIN + COMPL + "[t] --- Ciclo slow 6 ---\n[t] --- Ciclo slow 6 ---\n  ERROR polymarket: NameError: x\n", 0, ""),      # el ciclo SIGUIENTE no cuenta
    ("  nada\n[t] === Fin ===\n" + "[t] === Captura wallets ===\nTraceback (most recent call last):\n  File \"" + str(REPO) + "/capture_wallets.py\", line 1, in f\nNameError: ajeno\n", 0, ""),
])
def test_b1_formato_real_cabecera_duplicada_y_errores(tmp_path, cuerpo, rc, frag):
    out = _verifica_real(tmp_path, "previo\n", HDR, cuerpo, crece=True)
    assert f"rc={rc}" in out and frag in out, out


def test_b1_no_crece_con_httperror_de_wallets_y_sin_excusa_es_fallo_en_formato_sintetico_real(tmp_path):
    out = _verifica_real(tmp_path, "previo\n", HDR, "  nada\n" + FIN, crece=False)
    assert "rc=1" in out and "NO crecio" in out, out


def test_b1_sin_cabecera_tras_el_despliegue_no_es_atribuible(tmp_path):
    out = _verifica_real(tmp_path, "previo\n", "", "  ERROR polymarket: NameError: x\n", crece=True)
    assert "rc=2" in out and "no es atribuible" in out, out


# ---------------------------------------------------------------- M3
def test_m3_lib_y_runner_comparten_la_lista_de_clases_blandas(tmp_path):
    # La fuente unica es deploy/clases_error.conf (paridad completa en test_revision5.py).
    assert sh(tmp_path, 'echo "$CAP_ERR_BLANDO"').strip() == P6.CODIGO_BLANDO


# ---------------------------------------------------------------- M6: el periodo del watchdog se MIDE en el log real
def _wd(tmp_path, log_file, ahora, **env):
    return sh(tmp_path, f'wd_fase {log_file} {ahora}', env={"PY": "/root/polymarket-research/.venv/bin/python", **env}).strip()


def _t(s):
    import calendar
    return calendar.timegm(time.strptime(s, "%Y-%m-%dT%H:%M:%SZ"))


def test_m6_log_real_silencioso_cada_605s_sincroniza_con_el_ultimo_tick(tmp_path):
    r = _wd(tmp_path, FIX / "watchdog_real_quiet.log", _t("2026-11-14T05:29:00Z"))
    assert r == "SYNC 104.4", r                                    # ultima marca 05:26:30, +150 s: 121,2 - 28,8 + 12


def test_m6_log_real_con_alerta_de_disco_cada_121s(tmp_path):
    ultima = [l for l in (FIX / "watchdog_real_disk.log").read_text().splitlines() if l.startswith("[")][-1][1:21]
    r = _wd(tmp_path, FIX / "watchdog_real_disk.log", _t(ultima) + 18)
    assert r.startswith("SYNC ") and abs(float(r[5:]) - (121.2 - 18 + 12)) < 0.2, r


def _log_marcas(tmp_path, ahora, offsets, extra=""):
    f = tmp_path / "wd.log"
    f.write_text("".join(time.strftime("[%Y-%m-%dT%H:%M:%SZ]", time.gmtime(ahora - o)) + f"  tick{extra if o == offsets[-1] else ''}\n" for o in sorted(offsets, reverse=True)))
    return f


def test_m6_menos_de_3_marcas_no_sincroniza(tmp_path):
    ahora = int(time.time()); r = _wd(tmp_path, _log_marcas(tmp_path, ahora, [30, 200]), ahora)
    assert r.startswith("NOSYNC solo 2 marcas"), r


def test_m6_huecos_que_no_son_multiplo_del_periodo_no_sincroniza(tmp_path):
    ahora = int(time.time()); r = _wd(tmp_path, _log_marcas(tmp_path, ahora, [1000, 500, 100]), ahora)
    assert r.startswith("NOSYNC hueco"), r


def test_m6_marcas_regulares_cualquier_multiplo_sincroniza_y_un_tick_con_reinicio_se_salta(tmp_path):
    ahora = int(time.time()); f = _log_marcas(tmp_path, ahora, [30 + 605, 30 + 121, 30])
    assert _wd(tmp_path, f, ahora).startswith("SYNC "), "605 s y 121 s son multiplos de 121,2"
    esp = float(_wd(tmp_path, f, ahora)[5:])
    f2 = _log_marcas(tmp_path, ahora, [30 + 605, 30 + 121, 30], extra=" DEPLOY OBSOLETO: x -- auto-reiniciando")
    assert abs(float(_wd(tmp_path, f2, ahora)[5:]) - (esp + 121.2)) < 0.3


def test_m6_espera_tick_sin_marcas_suficientes_avisa_y_sigue_y_con_log_viejo_falla(tmp_path):
    f = tmp_path / "wd.log"; f.write_text("x\n")
    out = sh(tmp_path, f'log() {{ echo "$*"; }}; WD_SIN_SYNC_S=0 espera_tick_watchdog {f}; echo "rc=$?"', env={"PY": "/root/polymarket-research/.venv/bin/python"})
    assert "AVISO: sin sincronia con el watchdog" in out and "rc=0" in out, out
    os_old = time.time() - 2000; os.utime(f, (os_old, os_old))
    assert "rc=1" in sh(tmp_path, f'espera_tick_watchdog {f}; echo "rc=$?"', env={"PY": "/root/polymarket-research/.venv/bin/python"})


# ---------------------------------------------------------------- M4: el cron de restart_ram solo cuenta como OMITIDO si su hora cayo con el lock tomado
def test_m4_horas_de_restart_ram_leidas_del_crontab_real(tmp_path):
    (tmp_path / "bin").mkdir(exist_ok=True)
    (tmp_path / "bin/crontab").write_text("#!/bin/bash\ncat <<'EOF'\n20 3 * * * flock -n /tmp/restart_ram_fase0.lock /bin/bash /root/polymarket-research/scripts/restart_ram_fase0.sh >> x.log 2>&1\n"
                                          "20 22 * * * flock -n /tmp/restart_ram_fase0.lock /bin/bash /root/polymarket-research/scripts/restart_ram_fase0.sh >> x.log 2>&1\n"
                                          "# 5 5 * * * restart_ram_fase0.sh\n*/5 * * * * flock -n /tmp/restart_ram_fase0.lock /root/polymarket-research/.venv/bin/python /root/polymarket-research/guard_ram_fase0.py\nEOF\n")
    (tmp_path / "bin/crontab").chmod(0o755)
    assert sh(tmp_path, "restart_ram_horas").strip() == "03:20 22:20"


@pytest.mark.parametrize("desfase_min,esperado", [(-5, "OMITIDO"), (30, "NO omitido")])
def test_m4_estado_restart_ram(tmp_path, desfase_min, esperado):
    ahora = int(time.time()); slot = time.strftime("%H:%M", time.gmtime(ahora + desfase_min * 60))
    out = sh(tmp_path, f'LOCK_T0={ahora - 600}; RESTART_RAM_CRONS="{slot}"; estado_restart_ram')
    assert esperado in out, out


def test_m4_sin_lock_o_sin_horario_no_se_afirma_que_se_omitio(tmp_path):
    assert "no se llego a tomar" in sh(tmp_path, 'LOCK_T0=0; RESTART_RAM_CRONS="22:20"; estado_restart_ram')
    assert "no se pudo leer su horario" in sh(tmp_path, 'LOCK_T0=$(( $(date +%s) - 60 )); RESTART_RAM_CRONS=""; estado_restart_ram')


# ---------------------------------------------------------------- sandbox: B1 (formato real), I1, I2, M2, M5, M7, (d), (e)
@pytest.mark.parametrize("modo,rc,frag", [("cap_nameerror_real", 1, "error de codigo"), ("cap_runtimeerror_real", 1, "error de codigo"),
                                          ("cap_valueerror_real", 1, "error de codigo"),                                              # T2: ERROR polymarket con clase de datos = codigo propio
                                          ("cap_gamma_keyerror_crece", 0, "P6 ciclo real de capture_markets con el codigo nuevo"),    # #3: 'Error gamma' malformada CON crecimiento: no revierte
                                          ("cap_429_real", 0, "verificado por la captura aislada")])                                  # #7: 429 sin crecimiento + aislada OK
def test_b1_sandbox_ciclo_real_con_cabecera_duplicada(sb, modo, rc, frag):
    r = run(sb, "--ejecutar", modo=modo, extra=CAP_EXTRA)
    assert r.returncode == rc and frag in r.stdout, r.stdout
    assert (estado(sb) == ORIG) == (rc == 1), r.stdout                                      # FALLO => marcha atras; OK => desplegado


def _aviso(sb):
    f = sb / "repo/logs/deploy_deltas_ws_aviso.log"
    return f.read_text() if f.exists() else ""


def test_i1_desplegado_sin_verificar_manda_aviso_critico(sb):
    r = run(sb, "--ejecutar", extra={"P6_ESPERA_S": "0", "P6_STUB_RC": "2"})                 # sin ciclo real y captura aislada inconclusa
    assert r.returncode == 4 and "DESPLEGADO SIN VERIFICAR (rc 4)" in _aviso(sb), r.stdout


def test_i1_activar_diferido_manda_aviso_critico(sb):
    r = run(sb, "--ejecutar", "--activar", extra={**_hora_en_p6(sb), "CONFIRMO_ADELANTO_6_MONEDAS": "1"})
    assert r.returncode == 4 and "--activar DIFERIDO (rc 4)" in _aviso(sb) and "--activar NO aplicado: estamos dentro de una ventana prohibida" in r.stdout, r.stdout


def _desplegado(sb):
    assert run(sb, "--ejecutar").returncode == 0 and estado(sb) != ORIG


def test_i2_ya_desplegado_activar_con_todo_en_orden_escribe_los_cfg_rc0(sb):
    _desplegado(sb)
    r = run(sb, "--ejecutar", "--activar", extra={"CONFIRMO_ADELANTO_6_MONEDAS": "1"})
    assert r.returncode == 0 and "YA DESPLEGADO" in r.stdout and (sb / "dl/universo_5m/cfg_CAPTURE_5M_HORIZONTE_MIN").exists(), r.stdout


def test_r3b_ya_desplegado_activar_con_p6_intermitente_se_rehusa_y_sin_intermitente_activa(sb):
    _desplegado(sb)
    r = run(sb, "--ejecutar", "--activar", extra={"CONFIRMO_ADELANTO_6_MONEDAS": "1", "P6_STUB_RC": "0", "P6_STUB_MSG": "AVISO INTERMITENTE: un error de codigo previo NO se repitio (ValueError: flaky)\nOK intento 2"})
    assert r.returncode == 1 and "--activar REHUSADO (rc 1): P6 INTERMITENTE" in _aviso(sb) and "YA DESPLEGADO" in r.stdout, r.stdout + _aviso(sb)
    assert not (sb / "dl/universo_5m/cfg_CAPTURE_5M_HORIZONTE_MIN").exists() and not (sb / "dl/universo_5m/cfg_CAPTURE_429_FIX").exists()
    r = run(sb, "--ejecutar", "--activar", extra={"CONFIRMO_ADELANTO_6_MONEDAS": "1", "P6_STUB_RC": "0", "P6_STUB_MSG": "OK stub"})            # sin intermitente: activa como antes
    assert r.returncode == 0 and (sb / "dl/universo_5m/cfg_CAPTURE_5M_HORIZONTE_MIN").exists(), r.stdout


def test_i2_ya_desplegado_activar_sin_confirmacion_es_rc4_en_p0_y_aviso(sb):
    _desplegado(sb)
    r = run(sb, "--ejecutar", "--activar")
    assert r.returncode == 4 and not (sb / "dl/universo_5m/cfg_CAPTURE_5M_HORIZONTE_MIN").exists() and "--activar RECHAZADO (rc 4)" in _aviso(sb), r.stdout
    assert "YA DESPLEGADO" not in r.stdout and "P6" not in r.stdout      # #1: antes de lock y de la captura aislada


@pytest.mark.parametrize("hora,extra,frag", [("07:00", {}, "dentro de una ventana prohibida"),
                                              ("03:30", {}, "la proxima ventana prohibida"),                      # 10 min hasta las 03:40: la verificacion aislada puede tardar 930 s
                                              ("03:15", {"P6_STUB_RC": "2"}, "P6 captura aislada del codigo de main no verifica"),
                                              ("03:15", {"P6_STUB_RC": "1"}, "P6 captura aislada del codigo de main no verifica")])
def test_i2_ya_desplegado_activar_se_rehusa_sin_ventana_o_sin_p6_verificado(sb, hora, extra, frag):
    _desplegado(sb)
    r = run(sb, "--ejecutar", "--activar", hora=hora, extra={"CONFIRMO_ADELANTO_6_MONEDAS": "1", **extra})
    assert r.returncode == 1 and "--activar REHUSADO (rc 1)" in _aviso(sb) and frag in _aviso(sb) and not (sb / "dl/universo_5m/cfg_CAPTURE_5M_HORIZONTE_MIN").exists(), r.stdout + _aviso(sb)


def test_i2_ya_desplegado_activar_exige_el_lock_de_restart_ram(sb):
    _desplegado(sb)
    holder = subprocess.Popen(["flock", str(sb / "ramlock"), "sleep", "60"]); time.sleep(0.5)
    try:
        r = run(sb, "--ejecutar", "--activar", extra={"CONFIRMO_ADELANTO_6_MONEDAS": "1", "P1_TIMEOUT": "1"})
    finally:
        holder.kill(); holder.wait()
    assert r.returncode == 1 and "no se pudo tomar" in _aviso(sb) and not (sb / "dl/universo_5m/cfg_CAPTURE_5M_HORIZONTE_MIN").exists(), r.stdout


def test_m2_captura_aislada_que_no_cabe_antes_de_la_ventana_se_omite_con_aviso(sb):
    r = run(sb, "--ejecutar", extra={"P6_ESPERA_S": "0", "P6_AIS_TIMEOUT": "1000"})            # peor caso 3*(1000+70)=3210 s > 25 min hasta las 03:40
    assert r.returncode == 4 and "captura aislada OMITIDA" in r.stdout and "DESPLEGADO SIN VERIFICAR" in _aviso(sb), r.stdout


def test_m4_aborto_con_sustituye_restart_ram_libera_el_lock_y_dice_la_verdad(sb):
    r = run(sb, "--ejecutar", "--sustituye-restart-ram", hora="07:00", extra={"RESTART_RAM_CRONS": "22:20"})      # P0 falla por ventana: ABORTO con el lock tomado
    assert r.returncode == 1 and "ABORTO: comprobaciones previas fallidas" in r.stdout, r.stdout
    assert "restart_ram_fase0: NO omitido" in r.stdout and "OMITIDO por el lock" not in r.stdout and "lock de restart_ram LIBERADO tras el ABORTO" in r.stdout, r.stdout


def test_m5_dry_run_solo_escribe_en_datalogs_y_no_toca_el_repo(sb):
    antes = sorted(str(p.relative_to(sb / "repo")) + ":" + str(p.stat().st_size) for p in (sb / "repo").rglob("*") if p.is_file() and "watchdog.log" not in p.name)
    r = run(sb)
    despues = sorted(str(p.relative_to(sb / "repo")) + ":" + str(p.stat().st_size) for p in (sb / "repo").rglob("*") if p.is_file() and "watchdog.log" not in p.name)
    assert r.returncode == 0 and antes == despues, r.stdout
    assert list((sb / "dl/traspaso_deltas_ws").glob("deploy_*.log")) and not (sb / "repo/logs/deploy_deltas_ws_aviso.log").exists()


@pytest.mark.parametrize("sin_commit", [True, False])
def test_e_aviso_y_copia_del_arbol_de_trabajo_de_main(sb, sin_commit):
    g = lambda *a: subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *a], cwd=sb / "repo", check=True, capture_output=True)
    g("init", "-q"); g("add", "libro_estado_ws.py", "capture_markets.py")
    if not sin_commit:
        g("commit", "-qm", "base")
    r = run(sb)
    assert ("AVISO (e): libro_estado_ws.py de main tiene cambios SIN COMMITEAR" in r.stdout) == sin_commit, r.stdout
    r = run(sb, "--ejecutar")
    assert r.returncode == 0, r.stdout
    pre = sb / "dl/traspaso_deltas_ws"
    for f, base in (("libro_estado_ws.py", ORIG[0]), ("capture_markets.py", ORIG[1])):
        c = list(pre.glob(f + ".main_*")); assert len(c) == 1 and sha(c[0]).startswith(base), (f, c)


def _seed(sb):          # el sembrador entra en el sha del sello e2e (E2E_FILES): se re-sella con ESTE fichero
    seed = sb / "sembrar.py"; seed.write_text("import sys; print('ARGS', ' '.join(sys.argv[1:]))\n")
    (sb / "dl/traspaso_deltas_ws/e2e_ok.json").write_text(json.dumps({"sha": e2e_sha_py(str(seed)), "ts": int(time.time()), "pasados": 5}))
    return seed


def test_m7_con_precierre_vivo_el_presupuesto_de_p2b_baja(sb, tmp_path):
    (sb / "bin/screen").write_text("#!/bin/bash\necho '123.observadores (Detached)'; echo '124.vigiasfreq (Detached)'; echo '125.precierre (Detached)'\n")
    seed = _seed(sb)
    r = run(sb, "--ejecutar", extra={"SEMBRAR_PY": str(seed)})
    assert r.returncode == 0 and "presupuesto de peticiones de P2b reducido a 60s" in r.stdout and "--presupuesto-s 60" in r.stdout, r.stdout


def test_m7_sin_precierre_el_presupuesto_de_p2b_es_el_normal(sb):
    seed = _seed(sb)
    r = run(sb, "--ejecutar", extra={"SEMBRAR_PY": str(seed)})
    assert r.returncode == 0 and "reducido" not in r.stdout and "--presupuesto-s 240" in r.stdout, r.stdout


def test_d_marcha_atras_parcial_conserva_gamma_pausa_si_el_libro_nuevo_sigue_vivo(sb):
    gp = sb / "dl/universo_5m/gamma_pausa.json"
    r = run(sb, "--ejecutar", extra={**_hora_en_p6(sb), "P6_STUB_RC": "1", "FAKE_VD_GAMMA": "1"})      # fallo de P6 dentro de ventana prohibida: parcial, libro nuevo vivo
    assert r.returncode == 1 and "marcha atras hecha (PARCIAL)" in r.stdout and gp.exists() and "se CONSERVA" in r.stdout, r.stdout


def test_m2_ya_dentro_de_una_ventana_en_p6_se_omite_la_captura_aislada_y_queda_sin_verificar(sb):
    r = run(sb, "--ejecutar", extra={**_hora_file(sb), "P6_STUB_RC": "1"})            # el reinicio de observadores nos deja a las 07:00 (ventana): el stub rc 1 NO llega a ejecutarse
    assert r.returncode == 4 and "captura aislada OMITIDA" in r.stdout and "MARCHA ATRAS" not in r.stdout and "DESPLEGADO SIN VERIFICAR" in _aviso(sb), r.stdout


# ================================================================ 5a pasada (red-team de verificacion): 5 pendientes
# (1) errores que capture_markets imprime SIN Traceback: lineas LITERALES de stage/capture_markets.py (:217, :375, :437)
def test_p1_los_formatos_literales_de_error_siguen_en_el_stage():
    src = (V3 / "stage/capture_markets.py").read_text()
    for f in ('print(f"  Error gamma slug={slug} offset={offset}: {type(e).__name__}: {e}")',
              'print(f"  Error gamma lote {a} {tss[0]}..{tss[-1]}: {type(e).__name__}: {e} (se reintenta en el ciclo siguiente)", flush=True)',
              'print(f"  ERROR adelanto 5m: {type(e).__name__}: {e}", flush=True)',
              'print(f"  ERROR precios: {type(e).__name__}: {e}")', 'print(f"  ERROR polymarket: {type(e).__name__}: {e}")'):
        assert f in src, f


def test_p1_lib_y_runner_comparten_el_patron_de_linea_de_error(tmp_path):
    assert sh(tmp_path, 'echo "$CAP_LINEA_ERR"').strip() == P6.LINEA_ERR


LIT_COD = ["  Error gamma slug=bitcoin offset=0: NameError: name 'x' is not defined",
           "  Error gamma lote 5m 1763114100..1763114400: AttributeError: 'NoneType' object has no attribute 'get' (se reintenta en el ciclo siguiente)",
           "  Error gamma slug=x offset=0: ImportError: no module", "  Error gamma slug=x offset=0: SyntaxError: invalid syntax",
           "  ERROR adelanto 5m: ImportError: no module", "  ERROR precios: RuntimeError: x",
           "  ERROR adelanto 5m: ValueError: boom", "  ERROR polymarket: KeyError: 'id'"]          # T2: ERROR polymarket/precios/adelanto con clases de datos = codigo propio
LIT_BLANDO = ["  Error gamma slug=crypto-prices offset=100: KeyError: 'id'",
              "  Error gamma lote 5m 1763114100..1763114400: TypeError: boom (se reintenta en el ciclo siguiente)",
              "  Error gamma slug=x offset=0: IndexError: list index out of range", "  Error gamma slug=x offset=0: ValueError: bad json field"]
LIT_TRANS = ["  Error gamma slug=solana offset=0: HTTPError: 429 Client Error: Too Many Requests for url: https://gamma-api.polymarket.com/events?tag_slug=solana&ac",
             "  Error gamma lote 5m 1763114100..1763114400: ReadTimeout: HTTPSConnectionPool(host='gamma-api.polymarket.com'): Read timed out. (se reintenta en el ciclo siguiente)",
             "  Error gamma slug=eth offset=0: ConnectionError: x", "  Error gamma slug=eth offset=0: JSONDecodeError: Expecting value: line 1 column 1 (char 0)",
             "  ERROR adelanto 5m: HTTPError: 502 Server Error", "  Error gamma lote 5m 1..2: OSError: [Errno 110] Connection timed out (se reintenta en el ciclo siguiente)"]


@pytest.mark.parametrize("linea", LIT_COD)
def test_p1_error_de_codigo_con_formato_literal_de_capture_markets_se_detecta(tmp_path, linea):
    out = _verifica_real(tmp_path, "previo\n", HDR, linea + "\n" + FIN, crece=True)
    assert "rc=1" in out and "error de codigo" in out, out


@pytest.mark.parametrize("linea", LIT_TRANS)
def test_p1_causa_transitoria_con_formato_literal_sigue_excusada(tmp_path, linea):
    out = _verifica_real(tmp_path, "previo\n", HDR, linea + "\n" + FIN, crece=False)
    assert "rc=2" in out and "crecimiento no verificado" in out, out          # #7: la excusa sin crecimiento es inconclusa, no un OK
    assert "rc=0" in _verifica_real(tmp_path, "previo\n", HDR, linea + "\n" + FIN, crece=True)


@pytest.mark.parametrize("fx,n", [("slow_real_2737.log", 2737), ("slow_real_429_2723.log", 2723)])
def test_p1_ningun_ciclo_real_da_un_falso_error_de_codigo(tmp_path, fx, n):
    seg = sh(tmp_path, f'slow_segmento {FIX}/{fx} 0 {n}')
    (tmp_path / "seg.txt").write_text(seg)
    assert sh(tmp_path, 'cap_error_codigo "$(cat $TMP/seg.txt)"').strip() == ""


def test_p1_runner_p6_detecta_los_mismos_formatos():
    for l in LIT_COD:
        assert P6.clasifica(l)[0] == [l.strip()] or P6.clasifica(l)[0] == [l], l
    for l in LIT_BLANDO:
        assert P6.clasifica(l) == ([], [l]), l
    for l in LIT_TRANS:
        assert P6.clasifica(l) == ([], []), l


# (2) Telegram/log de EXITO
def test_p2_despliegue_ok_avisa_con_resumen_y_dice_que_falta_activar(sb):
    r = run(sb, "--ejecutar")
    a = _aviso(sb)
    assert r.returncode == 0 and "OK deploy deltas libro_ws: DESPLIEGUE OK (rc 0)" in a and "FALTA ACTIVAR" in a and "hijo nuevo pid" in a and "sha libro=" in a and "P6=" in a, r.stdout + a


def test_p2_despliegue_ok_con_activar_lo_dice(sb):
    r = run(sb, "--ejecutar", "--activar", extra={"CONFIRMO_ADELANTO_6_MONEDAS": "1"})
    assert r.returncode == 0 and "ADELANTO ACTIVADO" in _aviso(sb) and "FALTA ACTIVAR" not in _aviso(sb), r.stdout


def test_p2_aislado_ok_y_ciclo_real_no_observado_tambien_avisa_ok(sb):
    r = run(sb, "--ejecutar", extra={"P6_ESPERA_S": "2", "P6_PASO": "0.3"})
    assert r.returncode == 0 and "ciclo real no observado" in _aviso(sb) and "DESPLIEGUE OK (rc 0)" in _aviso(sb), r.stdout


def test_p2_un_fallo_no_manda_aviso_de_exito(sb):
    r = run(sb, "--ejecutar", modo="dos")
    assert r.returncode == 1 and "DESPLIEGUE OK" not in _aviso(sb)


# (3) --activar sin CONFIRMO por el camino principal
def test_p3_activar_sin_confirmo_en_el_camino_principal_es_rc4_con_aviso(sb):
    r = run(sb, "--ejecutar", "--activar")
    assert r.returncode == 4 and "--activar RECHAZADO (rc 4)" in _aviso(sb) and "DESPLIEGUE OK" not in _aviso(sb), r.stdout          # #1: ya en P0
    assert estado(sb) == ORIG and not (sb / "dl/universo_5m/cfg_CAPTURE_5M_HORIZONTE_MIN").exists() and "P0 comprobaciones" not in r.stdout


# (4) 429 doble: captura aislada inconclusa Y ciclo real excusado por 429 sin crecimiento => no verificado
def test_p4_429_doble_no_es_un_ok_es_rc4_crecimiento_no_verificado(sb):
    r = run(sb, "--ejecutar", modo="cap_sin_crecer_429", extra={**CAP_EXTRA, "P6_STUB_RC": "2"})
    a = _aviso(sb)
    assert r.returncode == 4 and "crecimiento no verificado" in a and "DESPLIEGUE OK" not in a and "MARCHA ATRAS" not in r.stdout and estado(sb) != ORIG, r.stdout + a


def test_p4_429_en_el_ciclo_real_con_aislada_ok_si_es_ok(sb):
    r = run(sb, "--ejecutar", modo="cap_sin_crecer_429", extra=CAP_EXTRA)          # la aislada (stub rc 0) vio crecer data/markets
    assert r.returncode == 0 and "DESPLIEGUE OK (rc 0)" in _aviso(sb), r.stdout


# (5) capture_markets muerto sin '=== Fin ===' (SIGKILL/OOM)
def test_p5_sin_fin_con_429_y_sin_crecer_es_inconcluso_nunca_excusa(tmp_path):
    out = _verifica_real(tmp_path, "previo\n", HDR, "  Error gamma slug=x offset=0: HTTPError: 429 Client Error: Too Many Requests\n[t] === Captura wallets ===\n", crece=False)
    assert "rc=2" in out and "SIN '=== Fin ==='" in out, out


def test_p5_sin_fin_no_atribuye_el_stderr_de_capture_wallets(tmp_path):
    cuerpo = "[t] === Captura wallets ===\nTraceback (most recent call last):\n  File \"%s/capture_wallets.py\", line 1, in f\nNameError: ajeno\n" % REPO
    out = _verifica_real(tmp_path, "previo\n", HDR, cuerpo, crece=True)
    assert "rc=2" in out and "SIN '=== Fin ==='" in out, out


def test_p5_un_crash_con_traceback_sin_fin_sigue_siendo_error_de_codigo(tmp_path):
    cuerpo = 'Traceback (most recent call last):\n  File "%s/capture_markets.py", line 3, in f\nNameError: x\n[t] === Captura wallets ===\n' % REPO
    out = _verifica_real(tmp_path, "previo\n", HDR, cuerpo, crece=False)
    assert "rc=1" in out and "error de codigo" in out, out


def test_p5_sandbox_proceso_matado_sin_fin_con_aislada_ok_es_ok_aislado(sb):
    r = run(sb, "--ejecutar", modo="cap_matado", extra=CAP_EXTRA)
    assert r.returncode == 0 and "termino SIN '=== Fin ==='" in r.stdout and "ok (aislado; ciclo real no observado)" in r.stdout, r.stdout


def test_p5_sandbox_proceso_matado_sin_fin_y_aislada_inconclusa_es_rc4(sb):
    r = run(sb, "--ejecutar", modo="cap_matado", extra={**CAP_EXTRA, "P6_STUB_RC": "2"})
    assert r.returncode == 4 and "DESPLEGADO SIN VERIFICAR (rc 4)" in _aviso(sb) and "MARCHA ATRAS" not in r.stdout, r.stdout
