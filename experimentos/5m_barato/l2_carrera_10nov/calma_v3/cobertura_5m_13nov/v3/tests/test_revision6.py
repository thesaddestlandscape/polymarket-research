"""6a pasada (coordinador, 14-Nov noche): A (universo de tokens del hijo nuevo vs el viejo en P5 + Tracebacks no fatales en el aviso OK), B (MemoryError/ENOSPC/ContentDecodingError/JSON truncado =
entorno, inconcluso; 400/404 siguen siendo codigo), C (cp ATOMICO a main y en la marcha atras), D (horas REALES del slot: 04:10 y 03:19 con reloj que avanza), L1 (Traceback propio con clase de una
palabra = DURO), L2 (la excusa de texto libre solo con formas ancladas; regresion con slow.log reales), L3 (volumen de pruebas e2e automatico y mensaje claro)."""
import importlib.util, os, subprocess, sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_espera_hijos import sh, V3, LIB, REPO                                           # noqa: E402
from test_deploy_sandbox import sb, run, estado, ORIG, SCRIPT, sha, _hora_en_p6          # noqa: E402,F401
from test_revision4 import _aviso, FIX                                                    # noqa: E402
from test_revision5 import tb, bash_codigo, bash_blando, P6                               # noqa: E402


# ---------------------------------------------------------------- L1: clase de una sola palabra en un Traceback propio
@pytest.mark.parametrize("final", ["Boom", "Fallo", "X", "MiError"])
def test_l1_traceback_propio_con_clase_de_una_palabra_es_duro(tmp_path, final):
    t = tb(final)
    assert [l.strip() for l in bash_codigo(tmp_path, t)] == [final] and [l.strip() for l in P6.clasifica(t)[0]] == [final]


def test_l1_los_bordes_siguen_igual(tmp_path):
    assert bash_codigo(tmp_path, tb("Boom", mod="capture_wallets.py")) == []                    # traceback ajeno
    assert bash_codigo(tmp_path, tb("KeyboardInterrupt")) == []                                  # apagado
    assert bash_codigo(tmp_path, "Boom\n") == []                                                 # una palabra suelta sin Traceback no es nada
    assert bash_codigo(tmp_path, tb("requests.exceptions.ConnectionError")) == []                # una palabra pero clase de red: transitoria


def test_l1_sandbox_ciclo_real_con_traceback_de_una_palabra_hace_marcha_atras(sb):
    r = run(sb, "--ejecutar", modo="cap_tb_palabra", extra={"P6_ESPERA_S": "30", "P6_PASO": "0.3", "P6_CICLO_S": "20"})
    assert r.returncode == 1 and "error de codigo" in r.stdout and "marcha atras hecha (OK)" in r.stdout and estado(sb) == ORIG, r.stdout


# ---------------------------------------------------------------- B: entorno = inconcluso; 400/404 = codigo
@pytest.mark.parametrize("final", ["MemoryError", "OSError: [Errno 28] No space left on device", "requests.exceptions.ContentDecodingError: ('gzip roto')", "ContentDecodingError",
                                   "json.decoder.JSONDecodeError: Unterminated string starting at: line 1 column 9 (char 8)", "json.decoder.JSONDecodeError: Expecting ',' delimiter: line 1 column 3 (char 2)"])
def test_b_entorno_o_cuerpo_truncado_no_es_codigo(tmp_path, final):
    assert bash_codigo(tmp_path, tb(final)) == [] and P6.clasifica(tb(final))[0] == [], final
    clase, _, msg = final.partition(": ")
    l = f"  Error gamma slug=x offset=0: {clase.split('.')[-1]}: {msg}\n" if msg else f"  Error gamma slug=x offset=0: {clase}\n"
    assert bash_codigo(tmp_path, l) == [] and P6.clasifica(l)[0] == [] and P6.clasifica(l)[1] == [], final


@pytest.mark.parametrize("final", ["requests.exceptions.HTTPError: 400 Client Error: Bad Request for url: https://x", "requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://x",
                                   "json.decoder.JSONDecodeError: Extra data: line 1 column 5 (char 4)", "PermissionError: [Errno 13] Permission denied", "OSError: [Errno 2] No such file or directory"])
def test_b_los_400_404_y_el_resto_siguen_siendo_codigo(tmp_path, final):
    assert len(bash_codigo(tmp_path, tb(final))) == 1 and len(P6.clasifica(tb(final))[0]) == 1, final


@pytest.mark.parametrize("modo", ["cap_enospc", "cap_memoryerror"])
def test_b_enospc_o_memoryerror_en_el_ciclo_real_no_revierte_un_despliegue_sano(sb, modo):
    r = run(sb, "--ejecutar", modo=modo, extra={"P6_ESPERA_S": "30", "P6_PASO": "0.3", "P6_CICLO_S": "20"})
    assert r.returncode == 0 and "MARCHA ATRAS" not in r.stdout and "marcha atras" not in r.stdout.lower().replace("sin marcha atras", "") and estado(sb)[0] != ORIG[0], r.stdout


# ---------------------------------------------------------------- L2: la excusa de texto libre solo con formas ancladas
def test_l2_ninguna_regla_ancha_en_el_codigo_ni_en_el_conf():
    conf = P6._carga_conf(V3 / "deploy/clases_error.conf")
    assert conf["CAP_LINEA_TRANSITORIA_ERE"].startswith("^") and not any(c in conf["CAP_LINEA_TRANSITORIA_ERE"] for c in ("\\b",))
    assert "TRANSITORIO.search(out)" not in (V3 / "deploy/p6_ciclo_aislado.py").read_text()                     # el runner decide por excusa(): clase o linea anclada
    assert 'grep -aqE "$CAP_TRANSITORIO_ERE"' not in LIB.read_text()


@pytest.mark.parametrize("final,codigo", [
    ("OSError: [Errno 110] Connection timed out", False), ("OSError: [Errno 111] Connection refused", False), ("OSError: [Errno 104] Connection reset by peer", False),
    ("OSError: [Errno -2] Name or service not known", False), ("OSError: timed out", False), ("OSError: 429 Too Many Requests", False), ("OSError: 503 Service Unavailable", False),
    ("OSError: [Errno 28] No space left on device", False),                                  # clase B (CAP_OS_ENTORNO_MSG), no la ERE de red
    ("OSError: [Errno 32] Broken pipe", True), ("OSError: [Errno 101] Network is unreachable", True),          # L2 a la letra: retirados de la ERE => DURO (fail-closed)
    ("OSError: [Errno 103] Connection aborted", True), ("OSError: [Errno -3] Temporary failure in name resolution", True),
    ("OSError: fallo raro: Connection reset en medio", True), ("OSError: no hay 429 aqui", True), ("OSError: [Errno 13] Permission denied", True)])
def test_l2_cap_transitorio_ere_solo_red_anclada(tmp_path, final, codigo):
    assert bool(bash_codigo(tmp_path, tb(final))) == codigo and bool(P6.clasifica(tb(final))[0]) == codigo, final
    conf = P6._carga_conf(V3 / "deploy/clases_error.conf")
    for ya_no in ("Broken pipe", "Network is unreachable", "No space left", "Errno 28", "aborted"):
        assert ya_no not in conf["CAP_TRANSITORIO_ERE"], ya_no


def test_l2_regresion_slow_log_real_429_se_excusa_y_no_hay_codigo(tmp_path):
    t = (FIX / "slow_real_429_2723.log").read_text()
    assert P6.excusa(t) and P6.clasifica(t)[0] == []
    seg = sh(tmp_path, f"slow_segmento {FIX}/slow_real_429_2723.log 0 2723")
    assert sh(tmp_path, 'cap_excusa "$T"', env={"T": seg}).strip() != ""


def test_l2_regresion_slow_log_real_2737_los_errores_de_wallets_no_excusan_nada(tmp_path):
    t = (FIX / "slow_real_2737.log").read_text()
    assert P6.excusa(t) == [] and P6.clasifica(t)[0] == []                                                      # HTTPError 400 del leaderboard, ValueError de posiciones, Traceback ajeno
    seg = sh(tmp_path, f"slow_segmento {FIX}/slow_real_2737.log 0 2737")
    assert sh(tmp_path, 'cap_excusa "$T"', env={"T": seg}).strip() == ""


@pytest.mark.parametrize("linea", ["  Error gamma slug=x offset=0: NameError: name 'Timeout' is not defined", "el codigo dijo Connection reset sin ser una excepcion", "  Eventos: HTTP 429 mercados",
                                   "ValueError: timed out parsing"])
def test_l2_texto_arbitrario_con_palabras_de_red_no_excusa(linea):
    assert P6.excusa(linea + "\n") == []


def test_l2_sandbox_sin_crecer_con_texto_ancho_es_duro_y_con_forma_anclada_es_inconcluso(sb):
    r = run(sb, "--ejecutar", modo="cap_sin_crecer_1429", extra={"P6_ESPERA_S": "30", "P6_PASO": "0.3", "P6_CICLO_S": "20"})
    assert r.returncode == 1 and "NO crecio" in r.stdout, r.stdout


# ---------------------------------------------------------------- C: cp atomico
def _cp_atomico(tmp_path, cuerpo):
    f = tmp_path / "fn.sh"; f.write_text(subprocess.run(["sed", "-n", "/^cp_atomico() {/,/^}/p", str(SCRIPT)], capture_output=True, text=True).stdout)
    return subprocess.run(["bash", "-c", f". {f}\n{cuerpo}"], capture_output=True, text=True, cwd=tmp_path)


def test_c_cp_atomico_conserva_modo_no_deja_temporales_y_falla_limpio(tmp_path):
    (tmp_path / "src").write_text("nuevo\n"); (tmp_path / "dst").write_text("viejo\n"); os.chmod(tmp_path / "dst", 0o640)
    r = _cp_atomico(tmp_path, 'cp_atomico src dst; echo rc=$?')
    assert "rc=0" in r.stdout and (tmp_path / "dst").read_text() == "nuevo\n" and oct((tmp_path / "dst").stat().st_mode & 0o777) == "0o640" and not list(tmp_path.glob("*.deltatmp.*"))
    r = _cp_atomico(tmp_path, 'cp_atomico no_existe dst; echo rc=$?')
    assert "rc=1" in r.stdout and (tmp_path / "dst").read_text() == "nuevo\n" and not list(tmp_path.glob("*.deltatmp.*"))
    (tmp_path / "dir").mkdir()
    r = _cp_atomico(tmp_path, 'cp_atomico src dir; echo rc=$?')                                                    # destino = directorio: mv -T falla, no se cuela dentro
    assert "rc=1" in r.stdout and not (tmp_path / "dir/src").exists() and not list(tmp_path.glob("*.deltatmp.*"))


def _cp_espia(sb):
    """Un `cp` falso (en PATH del sandbox) que, cuando el destino es un temporal *.deltatmp.*, anota el sha del main que va a sustituir ANTES de copiar: prueba de que main no se toca durante el cp."""
    (sb / "bin/cp").write_text('#!/bin/bash\nfor a in "$@"; do last=$a; done\ncase "$last" in *.deltatmp.*) m=${last%.deltatmp.*}; echo "$(basename "$m") $([ -e "$m" ] && sha256sum "$m" | cut -c1-8 || echo ausente)" >> "$SB/cp_vistos.txt";; esac\nexec /bin/cp "$@"\n')
    (sb / "bin/cp").chmod(0o755)


def test_c_el_despliegue_copia_a_main_por_temporal_y_no_deja_restos(sb):
    _cp_espia(sb)
    r = run(sb, "--ejecutar")
    vistos = dict(l.split() for l in (sb / "cp_vistos.txt").read_text().splitlines())
    assert r.returncode == 0 and set(vistos) == {"universo_5m_io.py", "capture_markets.py", "libro_estado_ws.py"}, (vistos, r.stdout)
    assert vistos["capture_markets.py"] == ORIG[1] and vistos["libro_estado_ws.py"] == ORIG[0] and vistos["universo_5m_io.py"] == "ausente"          # main intacto mientras se copia
    assert not list((sb / "repo").glob("*.deltatmp.*"))


def test_c_la_marcha_atras_restaura_por_temporal_y_reconcilia_con_los_pre(sb):
    _cp_espia(sb)
    r = run(sb, "--ejecutar", modo="dos")
    lineas = (sb / "cp_vistos.txt").read_text().splitlines()
    assert r.returncode == 1 and "marcha atras hecha (OK)" in r.stdout and estado(sb) == ORIG and len(lineas) >= 5, (lineas, r.stdout)                # 3 del despliegue + restauraciones
    assert not list((sb / "repo").glob("*.deltatmp.*"))
    pre = sb / "dl/traspaso_deltas_ws"
    assert sha(sb / "repo/libro_estado_ws.py") == sha(next(pre.rglob("libro_estado_ws.py.pre"))) and sha(sb / "repo/capture_markets.py") == sha(next(pre.rglob("capture_markets.py.pre")))


# ---------------------------------------------------------------- A: universo de tokens del hijo nuevo vs el viejo
LOG_VIEJO = "log previo\n[x] conectado [BTC#5min], 6 tokens (lector en proceso separado, pid 5555)\n[x] conectado [BTC#5min], 8 tokens (lector en proceso separado, pid 5555)\n[x] conectado [ETH#5min], 3 tokens (lector en proceso separado, pid 7777)\n"


LOG_8_Y_LUEGO_6 = "[x] conectado [BTC#5min], 8 tokens (lector en proceso separado, pid 5555)\n[x] conectado [BTC#5min], 6 tokens (lector en proceso separado, pid 5555)\n"
LOG_60 = "[x] conectado [BTC#60min], 50 tokens (lector en proceso separado, pid 5555)\n"


@pytest.mark.parametrize("viejo,nuevo,pids_v,rc,frag", [
    (LOG_VIEJO, "[x] conectado [BTC#5min], 8 tokens (lector en proceso separado, pid 99)\n", "5555", 0, "BTC#5min 8"),
    (LOG_VIEJO, "[x] conectado [BTC#5min], 10 tokens (lector en proceso separado, pid 99)\n", "5555", 0, "BTC#5min 10"),
    (LOG_VIEJO, "[x] conectado [BTC#5min], 6 tokens (lector en proceso separado, pid 99)\n", "5555", 0, "BTC#5min 6"),            # R1: 6 vs 8 (rotacion de mercados) NO es REDUCIDO
    (LOG_VIEJO, "[x] conectado [BTC#5min], 5 tokens (lector en proceso separado, pid 99)\n", "5555", 1, "BTC#5min:8->5(minimo 6"),   # caida real (>2 bajo el maximo)
    (LOG_8_Y_LUEGO_6, "[x] conectado [BTC#5min], 6 tokens (lector en proceso separado, pid 99)\n", "5555", 0, "viejo_max[BTC#5min 8"),   # viejo termina en 6, pero llego a 8
    (LOG_60, "[x] conectado [BTC#60min], 49 tokens (lector en proceso separado, pid 99)\n", "5555", 1, "BTC#60min:50->49"),              # 60min estable: estricto
    (LOG_60, "[x] conectado [BTC#60min], 50 tokens (lector en proceso separado, pid 99)\n", "5555", 0, "BTC#60min 50"),
    (LOG_VIEJO, "[x] conectado [ETH#5min], 8 tokens (lector en proceso separado, pid 99)\n", "5555 7777", 1, "BTC#5min:8->ausente"),
    (LOG_VIEJO, "[x] conectado [BTC#5min], 4 tokens (lector en proceso separado, pid 98)\n", "5555", 1, "no imprimio"),         # linea de OTRO pid: no cuenta
    ("log previo\n", "[x] conectado [BTC#5min], 4 tokens (lector en proceso separado, pid 99)\n", "5555", 0, "SIN REFERENCIA"),
    (LOG_VIEJO, "[x] conectado [BTC#5min] pid 99\n", "5555", 1, "no imprimio 'N tokens'")])
def test_a_compara_tokens(tmp_path, viejo, nuevo, pids_v, rc, frag):
    (tmp_path / "v.txt").write_text(viejo); (tmp_path / "n.txt").write_text(nuevo)
    out = sh(tmp_path, f'compara_tokens "$(cat $TMP/v.txt)" "$(cat $TMP/n.txt)" 99 "{pids_v}"; echo "rc=$?"; echo "$TOK_DET"')
    assert f"rc={rc}" in out and frag in out, out


def _log_viejo(sb, tokens=8):
    (sb / "repo/logs/observadores_fase0.log").write_text(f"log previo\n[x] conectado [BTC#5min], {tokens} tokens (lector en proceso separado, pid 5555)\n")


def test_a_universo_reducido_es_rc4_con_aviso_critico_sin_marcha_atras_y_no_activa(sb):
    _log_viejo(sb, 8)
    r = run(sb, "--ejecutar", "--activar", extra={"FAKE_TOKENS": "4", "CONFIRMO_ADELANTO_6_MONEDAS": "1"})
    a = _aviso(sb)
    assert r.returncode == 4 and "UNIVERSO REDUCIDO" in a and "BTC#5min:8->4" in a and "MARCHA ATRAS" not in r.stdout and estado(sb)[0] != ORIG[0], r.stdout + a
    assert not (sb / "dl/universo_5m/cfg_CAPTURE_429_FIX").exists() and "--activar NO aplicado: universo de tokens REDUCIDO" in r.stdout and "DESPLIEGUE OK" not in a


def test_a_universo_igual_es_ok_y_el_aviso_lleva_universo_y_tracebacks(sb):
    _log_viejo(sb, 8)
    r = run(sb, "--ejecutar", extra={"FAKE_TOKENS": "8"})
    a = _aviso(sb)
    assert r.returncode == 0 and "DESPLIEGUE OK" in a and "universo viejo[BTC#5min 8" in a and "nuevo[BTC#5min 8" in a, r.stdout + a
    assert "Tracebacks no fatales de libro_estado_ws/universo/websockets en el log nuevo: 0" in a, a


def test_a_el_aviso_ok_cuenta_los_tracebacks_no_fatales_del_hijo_nuevo(sb):
    r = run(sb, "--ejecutar", modo="traceback")
    a = _aviso(sb)
    assert r.returncode == 0 and "DESPLIEGUE OK" in a and "en el log nuevo: 1 " in a, r.stdout + a


# ---------------------------------------------------------------- D: horas REALES del slot (04:10) y 03:19 (P6 no cabe)
def test_d_slot_0410_p6_ciclo_real_completo_sin_acotar(sb):
    """04:10 -> la proxima ventana (06:00) esta a 110 min: P6 con sus valores POR DEFECTO (ciclo 900 s, margen 300 s) cabe entera."""
    r = run(sb, "--ejecutar", hora="04:10", modo="cap_ok", extra={"P6_ESPERA_S": "30", "P6_PASO": "0.3"})
    assert r.returncode == 0 and "ACOTADO" not in r.stdout and "OMITIDO" not in r.stdout and "P6 ciclo real de capture_markets con el codigo nuevo" in r.stdout, r.stdout


def test_d_0319_con_reloj_congelado_NO_reproduce_el_hallazgo(sb):
    """Documenta por que el reloj congelado engana: a las 03:19 fijas quedan 21 min -> lim6 = 1260-900-300 = 60 s y P6 se ACOTA (no se omite). El hallazgo del red-team (P6 no cabe) exige reloj que AVANZA."""
    r = run(sb, "--ejecutar", hora="03:19", modo="cap_ok", extra={"P6_ESPERA_S": "2400", "P6_PASO": "0.3"})
    assert r.returncode == 0 and "ciclo real ACOTADO a 60s" in r.stdout, r.stdout


def test_d_0319_con_reloj_que_avanza_P6_se_omite_y_sin_aislado_es_rc4(sb):
    """03:19 de inicio; P2b/P2/P4/P5 consumen minutos (aqui: el reloj pasa a 03:27 durante la captura aislada de P6): lo que queda hasta las 03:40 < ciclo+margen => ciclo real OMITIDO. Con aislado OK
    es rc0 'ok (solo aislado)'; con aislado INCONCLUSO es rc4 NO VERIFICADO (sin marcha atras): es el caso del slot 03:19 que el coordinador descarto."""
    ex = {**_hora_en_p6(sb, ini="03:19"), "P6_STUB_HORA": "03:27", "P6_ESPERA_S": "2400", "P6_PASO": "0.3"}
    r = run(sb, "--ejecutar", hora="03:19", extra=ex)
    assert r.returncode == 0 and "ciclo real OMITIDO" in r.stdout and "ok (solo aislado)" in r.stdout, r.stdout


def test_d_0319_reloj_que_avanza_con_aislado_inconcluso_da_rc4(sb):
    ex = {**_hora_en_p6(sb, ini="03:19"), "P6_STUB_HORA": "03:27", "P6_ESPERA_S": "2400", "P6_PASO": "0.3", "P6_STUB_RC": "2"}
    r = run(sb, "--ejecutar", hora="03:19", extra=ex)
    assert r.returncode == 4 and "ciclo real OMITIDO" in r.stdout and "NO VERIFICADO" in r.stdout and "MARCHA ATRAS" not in r.stdout and estado(sb)[0] != ORIG[0], r.stdout


# ---------------------------------------------------------------- L3: volumen e2e automatico y mensaje claro
def test_l3_e2e_sin_volumen_suficiente_falla_con_mensaje_claro(monkeypatch):
    from test_e2e_real import _dir_base
    monkeypatch.setenv("E2E_DIR", "/no/existe/e2e")
    with pytest.raises(pytest.fail.Exception) as e:
        _dir_base()
    assert "E2E necesita >=10 GB libres en $E2E_DIR" in str(e.value)
    monkeypatch.delenv("E2E_DIR")
    with pytest.raises(pytest.fail.Exception) as e:
        _dir_base()
    assert "E2E necesita >=10 GB libres en $E2E_DIR" in str(e.value)


@pytest.mark.skipif(os.geteuid() != 0, reason="montar un tmpfs requiere root")
def test_l3_vol_e2e_monta_un_tmpfs_grande_mata_a_sus_procesos_y_lo_desmonta_siempre():
    vol = V3 / "tests/e2e/vol_e2e.sh"
    d = subprocess.run(["bash", str(vol), "monta"], capture_output=True, text=True).stdout.strip()
    assert d.startswith("/var/tmp/e2e_vol.") and os.path.ismount(d)
    st = os.statvfs(d); assert st.f_bavail * st.f_frsize / 2**30 >= 10.5
    p = subprocess.Popen(["bash", "-c", "sleep 300; true", d + "/marcador"], start_new_session=True)                    # proceso 'olvidado' del sandbox: su cmdline lleva la ruta
    subprocess.run(["bash", str(vol), "limpia", d])
    assert p.wait(timeout=10) != 0 and not os.path.exists(d) and d not in open("/proc/mounts").read()
    r = subprocess.run(["bash", str(vol), "limpia", "/etc"], capture_output=True, text=True)                          # solo actua sobre /var/tmp/e2e_vol.*
    assert r.returncode == 1 and os.path.isdir("/etc")


def test_r1_sin_referencia_el_aviso_final_lo_dice_y_no_afirma_universo_ok(sb):
    (sb / "repo/logs/observadores_fase0.log").write_text("log previo sin tokens\n")
    r = run(sb, "--ejecutar", extra={"FAKE_TOKENS": "4"})
    log = next((sb / "dl/traspaso_deltas_ws").glob("deploy_*.log")).read_text()
    assert r.returncode == 0 and "SIN REFERENCIA" in log and "OK    universo del hijo nuevo >= viejo" not in log, r.stdout + log[-1500:]


def test_r1_6_vs_8_tokens_5min_en_el_despliegue_no_da_rc4(sb):
    _log_viejo(sb, 8)
    r = run(sb, "--ejecutar", extra={"FAKE_TOKENS": "6"})
    assert r.returncode == 0 and "UNIVERSO REDUCIDO" not in r.stdout and "DESPLIEGUE OK" in _aviso(sb), r.stdout


# ---------------------------------------------------------------- R3: un DURO unico no revierte; el viejo que falla igual => inconcluso
import json as _json
CAP_FALLA = "def una_captura():\n    raise ValueError('boom')\n"
CAP_OTRA = "def una_captura():\n    raise NameError('zz')\n"
CAP_OK = "def una_captura():\n    import pathlib; p = pathlib.Path('data/markets'); p.mkdir(parents=True, exist_ok=True); (p / 'x.csv').write_text('h\\nfila\\n'); print('Eventos unicos: 1')\n"
CAP_UNA_VEZ = ("def una_captura():\n    import pathlib; p = pathlib.Path('data/markets'); p.mkdir(parents=True, exist_ok=True)\n"
               "    f = pathlib.Path(__import__('os').environ['FAKE_ESTADO'])\n"
               "    if not f.exists(): f.write_text('1'); raise ValueError('flaky')\n"
               "    (p / 'x.csv').write_text('h\\nfila\\n')\n")


def _p6(tmp_path, nuevo, viejo=None, intentos=3):
    repo = tmp_path / "repo"; repo.mkdir(exist_ok=True); (repo / "capture_markets.py").write_text(nuevo)
    cmd = [sys.executable, str(V3 / "deploy/p6_ciclo_aislado.py"), "--repo", str(repo), "--tmp", str(tmp_path / "t"), "--timeout", "30", "--intentos", str(intentos), "--pausa", "0"]
    if viejo is not None:
        (tmp_path / "pre.py").write_text(viejo); cmd += ["--pre", str(tmp_path / "pre.py")]
    return subprocess.run(cmd, capture_output=True, text=True, env={**os.environ, "FAKE_ESTADO": str(tmp_path / "estado")}, timeout=120)


def test_r3_duro_que_tambien_falla_en_el_viejo_es_inconcluso_no_fallo(tmp_path):
    r = _p6(tmp_path, CAP_FALLA, viejo=CAP_FALLA)
    assert r.returncode == 2 and "IGUAL el capture_markets VIEJO" in r.stdout and "FALLO" not in r.stdout, r.stdout


def test_r3_duro_que_el_viejo_no_da_y_persiste_es_fallo(tmp_path):
    r = _p6(tmp_path, CAP_FALLA, viejo=CAP_OK)
    assert r.returncode == 1 and "FALLO intento 2" in r.stdout and "persiste tras reintento" in r.stdout, r.stdout


def test_r3_viejo_falla_distinto_sigue_siendo_fallo(tmp_path):
    r = _p6(tmp_path, CAP_FALLA, viejo=CAP_OTRA)
    assert r.returncode == 1 and "ValueError" in r.stdout, r.stdout


def test_r3_duro_unico_que_no_se_repite_es_ok(tmp_path):
    r = _p6(tmp_path, CAP_UNA_VEZ, viejo=CAP_OK)
    assert r.returncode == 0 and "OK intento 2" in r.stdout and "NO se repitio" in r.stdout, r.stdout


def test_r3_sin_pre_y_ultimo_intento_sigue_fail_closed(tmp_path):
    r = _p6(tmp_path, CAP_FALLA, viejo=None, intentos=1)
    assert r.returncode == 1 and "FALLO intento 1" in r.stdout, r.stdout


def test_r3_l1_traceback_propio_de_una_palabra_sigue_duro(tmp_path):
    r = _p6(tmp_path, "class Boom(Exception): pass\ndef una_captura():\n    raise Boom\n", viejo=CAP_OK)
    assert r.returncode == 1 and "Boom" in r.stdout, r.stdout


def _linea(clase):
    return "def una_captura():\n    print('  ERROR polymarket: %s: x')\n" % clase


def test_m1_firma_de_lineas_sin_traceback_usa_la_clase_no_el_prefijo():
    f = lambda t: P6.firma(P6.clasifica(t)[0])
    assert f("  ERROR polymarket: NameError: x\n") != f("  ERROR polymarket: TypeError: y\n")
    assert f("  ERROR polymarket: NameError: x\n") == f("  ERROR precios: NameError: otro mensaje\n")
    assert f(tb("NameError: x")) == f("  ERROR polymarket: NameError: x\n") and f(tb("a.b.KeyError: 1")) == f(tb("KeyError: 2"))


def test_m1_runner_viejo_con_otra_clase_sin_traceback_es_fallo_y_misma_clase_es_inconcluso(tmp_path):
    r = _p6(tmp_path, _linea("NameError"), viejo=_linea("TypeError"))
    assert r.returncode == 1 and "FALLO intento 2" in r.stdout, r.stdout
    r = _p6(tmp_path / "b", _linea("NameError"), viejo=_linea("NameError")) if (tmp_path / "b").mkdir() is None else None
    assert r.returncode == 2 and "IGUAL el capture_markets VIEJO" in r.stdout, r.stdout


def test_m3_duro_intermitente_no_es_ok_mudo_en_el_runner(tmp_path):
    r = _p6(tmp_path, CAP_UNA_VEZ, viejo=CAP_OK)
    assert r.returncode == 0 and "AVISO INTERMITENTE" in r.stdout, r.stdout


def test_m3_deploy_intermitente_es_rc4_con_aviso_critico_visible_sin_marcha_atras_ni_activar(sb):
    r = run(sb, "--ejecutar", "--activar", extra={"P6_STUB_RC": "0", "P6_STUB_MSG": "AVISO INTERMITENTE: un error de codigo previo NO se repitio (ValueError: flaky)\nOK intento 2", "CONFIRMO_ADELANTO_6_MONEDAS": "1"})
    a = _aviso(sb)
    assert r.returncode == 4 and "MARCHA ATRAS" not in r.stdout and "INTERMITENTE" in a and "DESPLEGADO SIN VERIFICAR" in a and "DESPLIEGUE OK" not in a, r.stdout + a
    assert not (sb / "dl/universo_5m/cfg_CAPTURE_429_FIX").exists() and "--activar NO aplicado" in r.stdout and estado(sb)[0] != ORIG[0]


def test_r3_el_despliegue_pasa_el_pre_al_runner():
    assert '--pre "$PRE/capture_markets.py.pre"' in LIB.read_text()


# ---------------------------------------------------------------- R2: 422 es codigo (validacion de NUESTRO request); 401/403 pendientes
@pytest.mark.parametrize("final,codigo", [("requests.exceptions.HTTPError: 422 Client Error: Unprocessable", True), ("urllib.error.HTTPError: HTTP Error 422: x", True),
                                          ("requests.exceptions.HTTPError: 429 Client Error: Too Many Requests", False), ("requests.exceptions.HTTPError: 403 Client Error: Forbidden", False)])
def test_r2_422_ya_no_es_transitorio(tmp_path, final, codigo):
    assert bool(bash_codigo(tmp_path, tb(final))) == codigo and bool(P6.clasifica(tb(final))[0]) == codigo, final
    assert ("  HTTP Error 422: x" in "") or not P6.LINEA_TRANS.match("HTTP Error 422: x")
