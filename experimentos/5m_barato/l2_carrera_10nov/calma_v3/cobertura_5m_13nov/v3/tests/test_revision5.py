"""5a revision (/code-review medium): H1 (cualquier clase en un Traceback propio), H2 (filtro transitorio por CLASE), H3 (Traceback propio identico en 3 intentos), H4 (objetivo vacio nunca 'ya'),
H6 (dry-run no escribe AVISO_LOG), H7 (bases de data/markets previas al ciclo), H8 (duracion de la fila G), H9 (UNICA fuente de listas de clases: deploy/clases_error.conf)."""
import importlib.util, re, subprocess, sys, os
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_espera_hijos import sh, V3, LIB, REPO                                           # noqa: E402

CONF = V3 / "deploy" / "clases_error.conf"
SCRIPT = V3 / "deploy" / "deploy_deltas_libro_ws_once.sh"
RUNNER = V3 / "deploy" / "p6_ciclo_aislado.py"
_spec = importlib.util.spec_from_file_location("p6_ciclo_aislado", RUNNER)
P6 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(P6)


def tb(final, mod="capture_markets.py"):
    return f'Traceback (most recent call last):\n  File "{REPO}/{mod}", line 3, in una_captura\n    x()\n{final}\n'


def bash_codigo(tmp_path, texto):
    (tmp_path / "t.txt").write_text(texto)
    return [l for l in sh(tmp_path, 'cap_error_codigo "$(cat $TMP/t.txt)"').splitlines() if l]


def bash_blando(tmp_path, texto):
    (tmp_path / "t.txt").write_text(texto)
    return [l for l in sh(tmp_path, 'cap_error_blando "$(cat $TMP/t.txt)"').splitlines() if l]


# ---------------------------------------------------------------- H9: fuente unica
def test_h9_la_fuente_unica_la_leen_bash_y_python_con_los_mismos_valores(tmp_path):
    conf = P6._carga_conf(CONF)
    assert set(conf) == {"CAP_ERR_BLANDO", "CAP_CLASE_RED", "CAP_CLASE_HTTP", "CAP_HTTP_TRANSITORIO_MSG", "CAP_CLASE_JSON", "CAP_JSON_TRANSITORIO_MSG", "CAP_CLASE_OS", "CAP_TRANSITORIO_ERE", "CAP_OS_ENTORNO_MSG", "CAP_LINEA_TRANSITORIA_ERE", "CAP_LINEA_ERR"}
    for k, v in conf.items():
        assert sh(tmp_path, f'printf "%s" "${k}"') == v, k
    assert P6.TRANSITORIO.pattern == conf["CAP_TRANSITORIO_ERE"] and P6.LINEA_ERR == conf["CAP_LINEA_ERR"] and P6.CODIGO_BLANDO == conf["CAP_ERR_BLANDO"]


def test_t6_ninguna_variable_muerta_en_el_conf_ni_en_el_codigo():
    """T6: toda clave del conf se usa en el codigo (python o lib) y no quedan las variables derivadas CAP_ERR_DURO/CODIGO_DURO/CODIGO/CAP_ERR_CODIGO."""
    codigo = RUNNER.read_text() + LIB.read_text()
    for k in P6._carga_conf(CONF):
        assert k in codigo, f"{k} no se usa"
    for muerta in ("CAP_ERR_DURO", "CODIGO_DURO", "CAP_ERR_CODIGO", "P6.CODIGO\\b"):
        assert muerta not in codigo and muerta not in CONF.read_text(), muerta


def test_h9_no_quedan_listas_de_clases_duplicadas_en_lib_ni_runner():
    for f in (LIB, RUNNER):
        t = f.read_text()
        assert "NameError|AttributeError" not in t and "ReadTimeout|ConnectTimeout" not in t, f"{f.name} duplica una lista: debe leerla de clases_error.conf"


def test_t7_bash_no_reimplementa_el_clasificador():
    t = LIB.read_text()
    assert "cap_cand_tb" not in t and "cap_filtra" not in t and "--clasifica duro" in t and "--clasifica blando" in t


def test_h9_el_conf_esta_sellado_en_sha256sums():
    assert re.search(r"^[0-9a-f]{64}  deploy/clases_error\.conf$", (V3 / "SHA256SUMS").read_text(), re.M)


def test_h9_el_conf_de_CLASES_CONF_manda_en_bash_y_en_python(tmp_path):
    c = tmp_path / "otro.conf"; c.write_text(CONF.read_text().replace("(KeyError|IndexError|ValueError|TypeError)", "(KeyError)"))
    assert sh(tmp_path, 'printf "%s" "$CAP_ERR_BLANDO"', env={"CLASES_CONF": str(c)}) == "(KeyError)"
    r = subprocess.run([sys.executable, "-c", f"import importlib.util as u; s=u.spec_from_file_location('p','{RUNNER}'); m=u.module_from_spec(s); s.loader.exec_module(m); print(m.CODIGO_BLANDO)"],
                       capture_output=True, text=True, env={**os.environ, "CLASES_CONF": str(c)})
    assert r.stdout.strip() == "(KeyError)", r.stderr


# ---------------------------------------------------------------- H1: cualquier clase en un Traceback propio
@pytest.mark.parametrize("final", ["FileNotFoundError: [Errno 2] No such file", "PermissionError: [Errno 13] denied", "UnicodeDecodeError: 'utf-8' codec can't decode byte",
                                   "RecursionError: maximum recursion depth exceeded", "StopIteration", "json.decoder.JSONDecodeError: x",
                                   "builtins.FileNotFoundError: x", "pandas.errors.ParserError: boom", "MiExcepcionPropia: algo", "requests.exceptions.MissingSchema: Invalid URL"])
def test_h1_un_traceback_propio_de_cualquier_clase_es_error_de_codigo(tmp_path, final):
    t = tb(final)
    esperado = [final.strip()]                       # (JSONDecodeError con mensaje no tipico = codigo, T10)
    assert [l.strip() for l in bash_codigo(tmp_path, t)] == esperado, final
    assert [l.strip() for l in P6.clasifica(t)[0]] == esperado, final


def test_h1_linea_sin_traceback_de_clase_no_listada_es_dura_y_la_de_datos_blanda(tmp_path):
    t = "  ERROR polymarket: FileNotFoundError: x\n  Error gamma slug=a offset=0: KeyError: 'id'\n  ERROR precios: MiExcepcionPropia: y\n"
    assert [l.strip() for l in bash_codigo(tmp_path, t)] == ["ERROR polymarket: FileNotFoundError: x", "ERROR precios: MiExcepcionPropia: y"]
    assert [l.strip() for l in bash_blando(tmp_path, t)] == ["Error gamma slug=a offset=0: KeyError: 'id'"]
    d, b = P6.clasifica(t)
    assert [l.strip() for l in d] == ["ERROR polymarket: FileNotFoundError: x", "ERROR precios: MiExcepcionPropia: y"] and [l.strip() for l in b] == ["Error gamma slug=a offset=0: KeyError: 'id'"]


def test_h1_un_traceback_ajeno_o_de_apagado_no_cuenta(tmp_path):
    ajeno = tb("ValueError: x", mod="capture_wallets.py")
    assert bash_codigo(tmp_path, ajeno) == [] and P6.clasifica(ajeno)[0] == []
    apagado = tb("KeyboardInterrupt")
    assert bash_codigo(tmp_path, apagado) == [] and P6.clasifica(apagado)[0] == []


# ---------------------------------------------------------------- H2: el filtro transitorio mira la CLASE
@pytest.mark.parametrize("linea,codigo", [
    ("NameError: name 'JSONDecodeError' is not defined", True),
    ("AttributeError: module 'x' has no attribute 'ConnectionError'", True),
    ("RuntimeError: ReadTimeout wrapper roto, Connection reset", True),
    ("ValueError: HTTP 429 mal parseado", True),
    ("OSError: [Errno 110] Connection timed out", False),        # clase de SO + mensaje de red: transitoria
    ("OSError: [Errno 28] No space left on device", False),        # B: disco lleno = entorno (inconcluso), no codigo
    ("MemoryError", False), ("requests.exceptions.ContentDecodingError: ('Received response with content-encoding: gzip, but failed to decode it.')", False),
    ("requests.exceptions.ReadTimeout: HTTPSConnectionPool", False),
    ("requests.exceptions.ConnectionError: x", False),
    ("json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)", False)])
def test_h2_traceback_el_filtro_transitorio_mira_la_clase_no_el_texto(tmp_path, linea, codigo):
    t = tb(linea)
    assert bool(bash_codigo(tmp_path, t)) == codigo, linea
    assert bool(P6.clasifica(t)[0]) == codigo, linea


@pytest.mark.parametrize("linea,codigo", [
    ("  Error gamma slug=x offset=0: NameError: name 'JSONDecodeError' is not defined", True),
    ("  ERROR polymarket: AttributeError: 'Timeout' object has no attribute 'ConnectionError'", True),
    ("  Error gamma slug=x offset=0: HTTPError: 429 Client Error: Too Many Requests", False),
    ("  ERROR precios: OSError: connection timed out", False)])
def test_h2_lineas_de_error_el_filtro_transitorio_mira_la_clase(tmp_path, linea, codigo):
    assert bool(bash_codigo(tmp_path, linea + "\n")) == codigo, linea
    assert bool(P6.clasifica(linea + "\n")[0]) == codigo, linea


def test_h2_blando_con_texto_transitorio_en_el_mensaje_sigue_siendo_blando(tmp_path):
    l = "  Error gamma slug=x offset=0: KeyError: 'ConnectionError'\n"
    assert len(bash_blando(tmp_path, l)) == 1 and len(P6.clasifica(l)[1]) == 1


def test_h2_paridad_bash_python_sobre_un_corpus(tmp_path):
    corpus = "".join([tb("MemoryError"), tb("NameError: name 'JSONDecodeError' is not defined"), tb("requests.exceptions.ConnectionError: x"),
                      "  Error gamma slug=a offset=0: KeyError: 'id'\n  Error gamma lote 5m 1..2: HTTPError: 502\n  ERROR adelanto 5m: UnicodeDecodeError: x\n",
                      "ValueError: suelto no es traceback\n  ERROR polymarket: OSError: Connection reset by peer\n"])
    d, b = P6.clasifica(corpus)
    assert [l.strip() for l in bash_codigo(tmp_path, corpus)] == [l.strip() for l in d]
    assert [l.strip() for l in bash_blando(tmp_path, corpus)] == [l.strip() for l in b]
    assert len(d) == 2 and len(b) == 1      # MemoryError (B) ya no es codigo: entorno


# ---------------------------------------------------------------- T5 (rama de firmas identicas eliminada) / R1 / R5
FAKE_ERR = '''
import os, sys
modo = os.environ.get("FAKE_CAP_MODO")
class Boom(Exception):
    pass
def una_captura():
    if modo == "conn":
        raise ConnectionError("Max retries exceeded: red caida")
    if modo == "http403":
        import requests; raise requests.exceptions.HTTPError("403 Client Error: Forbidden for url: https://gamma")
    if modo == "http400":
        import requests; raise requests.exceptions.HTTPError("400 Client Error: Bad Request for url: https://gamma")
    if modo == "boom":
        raise Boom
    return 1, 1
'''


def _runner(tmp_path, modo, intentos):
    repo = tmp_path / "repo"; repo.mkdir(exist_ok=True); (repo / "capture_markets.py").write_text(FAKE_ERR)
    import tempfile; t = tempfile.mkdtemp(dir=tmp_path)
    return subprocess.run([sys.executable, str(RUNNER), "--repo", str(repo), "--tmp", t + "/t", "--timeout", "30", "--intentos", str(intentos), "--pausa", "0"],
                          capture_output=True, text=True, env={**os.environ, "FAKE_CAP_MODO": modo}, timeout=120)


def test_t5_no_queda_la_rama_de_firmas_identicas():
    assert "firmas" not in RUNNER.read_text() and "IDENTICO" not in RUNNER.read_text()


@pytest.mark.parametrize("modo", ["conn", "http403"])
def test_r1_una_caida_de_red_o_un_403_en_los_3_intentos_NO_es_fallo(tmp_path, modo):
    r = _runner(tmp_path, modo, 3)
    assert r.returncode == 2, (modo, r.returncode, r.stdout)


def test_t1_un_400_del_propio_request_si_es_codigo_y_una_excepcion_propia_tambien(tmp_path):
    for modo in ("http400", "boom"):
        r = _runner(tmp_path, modo, 3)
        assert r.returncode == 1 and "FALLO intento 2" in r.stdout and "persiste tras reintento" in r.stdout, (modo, r.returncode, r.stdout)


def test_r5_error_de_datos_de_gamma_en_todos_los_intentos_es_inconcluso_no_fallo(tmp_path):
    t = "  Error gamma slug=x offset=0: KeyError: 'id'\n"
    assert P6.clasifica(t) == ([], [t.rstrip("\n")])


# ---------------------------------------------------------------- T1: mas fallos de red/HTTP del entorno
@pytest.mark.parametrize("final", ["requests.exceptions.HTTPError: 403 Client Error: Forbidden for url: https://x", "requests.exceptions.HTTPError: 401 Client Error: Unauthorized",
                                   "requests.exceptions.HTTPError: 408 Client Error: Request Timeout",
                                   "urllib.error.HTTPError: HTTP Error 429: Too Many Requests", "urllib.error.HTTPError: HTTP Error 503: Service Unavailable",
                                   "ssl.SSLEOFError: EOF occurred in violation of protocol", "urllib3.exceptions.ProtocolError: ('Connection aborted.', x)",
                                   "requests.exceptions.TooManyRedirects: Exceeded 30 redirects."])
def test_t1_fallos_de_red_http_del_entorno_no_son_codigo(tmp_path, final):
    t = tb(final)
    assert bash_codigo(tmp_path, t) == [] and P6.clasifica(t)[0] == [], final


@pytest.mark.parametrize("linea", ["  Error gamma slug=x offset=0: HTTPError: 403 Client Error: Forbidden", "  ERROR precios: HTTPError: 429 Client Error: Too Many Requests (CoinGecko)",
                                   "  ERROR precios: ReadTimeout: HTTPSConnectionPool(host='api.coingecko.com')", "  ERROR polymarket: SSLEOFError: EOF", "  Error gamma lote 5m 1..2: ProtocolError: x"])
def test_t1_lineas_de_error_del_entorno_no_son_candidatas_duras(tmp_path, linea):
    assert bash_codigo(tmp_path, linea + "\n") == [] and P6.clasifica(linea + "\n") == ([], []), linea


@pytest.mark.parametrize("final", ["requests.exceptions.HTTPError: 400 Client Error: Bad Request", "requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://x/?a=503"])
def test_t1_400_y_404_siguen_siendo_codigo(tmp_path, final):
    assert len(bash_codigo(tmp_path, tb(final))) == 1 and len(P6.clasifica(tb(final))[0]) == 1


# ---------------------------------------------------------------- T2: ERROR polymarket/precios con clases de datos son codigo propio; BLANDO solo 'Error gamma'
@pytest.mark.parametrize("linea", ["  ERROR polymarket: KeyError: 'id'", "  ERROR precios: ValueError: bad", "  ERROR adelanto 5m: TypeError: x", "  ERROR polymarket: IndexError: list index out of range"])
def test_t2_error_polymarket_precios_con_clases_de_datos_es_duro(tmp_path, linea):
    assert [l.strip() for l in bash_codigo(tmp_path, linea + "\n")] == [linea.strip()] and bash_blando(tmp_path, linea + "\n") == []
    d, b = P6.clasifica(linea + "\n")
    assert [l.strip() for l in d] == [linea.strip()] and b == []


@pytest.mark.parametrize("linea", ["  Error gamma slug=x offset=0: KeyError: 'id'", "  Error gamma lote 5m 1..2: ValueError: x (se reintenta en el ciclo siguiente)"])
def test_t2_error_gamma_con_clase_de_datos_sigue_blando(tmp_path, linea):
    assert bash_codigo(tmp_path, linea + "\n") == [] and len(bash_blando(tmp_path, linea + "\n")) == 1
    assert P6.clasifica(linea + "\n") == ([], [linea])


# ---------------------------------------------------------------- T10: JSONDecodeError acotado por mensaje
@pytest.mark.parametrize("msg,codigo", [("Expecting value: line 1 column 1 (char 0)", False), ("Extra data: line 1 column 5 (char 4)", True), ("Unterminated string starting at: line 1 column 9 (char 8)", False), ("Expecting ',' delimiter: line 1 column 40 (char 39)", False),
                                        ("Expecting property name enclosed in double quotes: line 1 column 2 (char 1)", True)])
def test_t10_jsondecodeerror_solo_transitorio_con_el_mensaje_tipico_de_cuerpo_vacio_o_html(tmp_path, msg, codigo):
    for t in (tb("json.decoder.JSONDecodeError: " + msg), f"  Error gamma slug=x offset=0: JSONDecodeError: {msg}\n"):
        assert bool(bash_codigo(tmp_path, t)) == codigo, (msg, t)
        assert bool(P6.clasifica(t)[0]) == codigo, (msg, t)


# ---------------------------------------------------------------- R6: solo la ULTIMA linea del bloque es la clase
def test_r6_una_linea_Note_en_columna_0_dentro_del_texto_no_es_una_clase(tmp_path):
    t = tb("ValueError: x") + "Note: respuesta de gamma truncada\nOtraCosa: foo\n"
    assert [l.strip() for l in bash_codigo(tmp_path, t)] == ["ValueError: x"]
    assert [l.strip() for l in P6.clasifica(t)[0]] == ["ValueError: x"]


# ---------------------------------------------------------------- R7: HTTPError solo es transitorio con 429/5xx
@pytest.mark.parametrize("msg,codigo", [("429 Client Error: Too Many Requests for url: https://g", False), ("502 Server Error: Bad Gateway", False), ("500 Server Error", False),
                                        ("400 Client Error: Bad Request for url: https://g/?x=500", True), ("404 Client Error: Not Found", True)])
def test_r7_httperror_solo_transitorio_con_429_o_5xx(tmp_path, msg, codigo):
    t = tb("requests.exceptions.HTTPError: " + msg)
    assert bool(bash_codigo(tmp_path, t)) == codigo, msg
    assert bool(P6.clasifica(t)[0]) == codigo, msg
    l = f"  Error gamma slug=x offset=0: HTTPError: {msg}\n"
    assert bool(bash_codigo(tmp_path, l)) == codigo and bool(P6.clasifica(l)[0]) == codigo, msg


# ---------------------------------------------------------------- R2 / R3: la copia verificada del conf es la que usa p6 y una lib que no carga aborta
def test_r3_conf_ausente_o_vacio_hace_fallar_la_carga_de_la_lib(tmp_path):
    for contenido in (None, ""):
        c = tmp_path / "x.conf"
        if contenido is not None: c.write_text(contenido)
        r = subprocess.run(["bash", "-c", f". {LIB}; echo rc=$?"], capture_output=True, text=True, env={**os.environ, "CLASES_CONF": str(tmp_path / "x.conf")})
        assert "rc=2" in r.stdout and "ABORTO" in r.stdout, (contenido, r.stdout, r.stderr)


def test_r3_el_script_comprueba_el_rc_de_la_carga_de_la_lib_y_exporta_CLASES_CONF():
    src = SCRIPT.read_text()
    assert '. "$_LIB_COPIA" || {' in src and 'export CLASES_CONF="$_CONF_COPIA"' in src
    # la copia verificada NO se borra en la misma linea que se carga la lib: solo la lib
    l = [x for x in src.splitlines() if x.startswith('export CLASES_CONF=')][0]
    assert l.endswith('rm -f "$_LIB_COPIA"') and '$_CONF_COPIA"' not in l.split("||")[0].split(";")[-1] + ""


def test_r2_p6_lee_el_conf_verificado_via_CLASES_CONF_exportada(tmp_path):
    # el despliegue exporta CLASES_CONF; p6_aislado lo hereda y el runner lo usa (no el fichero vivo)
    c = tmp_path / "v.conf"; c.write_text(CONF.read_text().replace("(KeyError|IndexError|ValueError|TypeError)", "(KeyError)"))
    r = subprocess.run(["bash", "-c", f'export CLASES_CONF={c}; . {LIB}; PY={sys.executable}; REPO=/x; P6_RUNNER={tmp_path}/r.py; '
                        f'p6_aislado; echo "$CAP_MOTIVO"'], capture_output=True, text=True,
                       env={**os.environ}, cwd=tmp_path) if (tmp_path / "r.py").write_text("import os; print('FALLO intento 1: ' + os.environ['CLASES_CONF'])\nraise SystemExit(1)\n") else None
    assert str(c) in r.stdout, (r.stdout, r.stderr)


# ---------------------------------------------------------------- H4: objetivo vacio nunca es 'ya'
def _estados(tmp_path, main_vacio, obj_vacio):
    src = SCRIPT.read_text()
    fn = src[src.index("# H4:"):src.index("# guarda de base:")]
    sha_def = re.search(r"^sha\(\) \{.*\}$", src, re.M).group(0)
    m = tmp_path / "main"; o = tmp_path / "obj"
    m.write_text("" if main_vacio else "x"); o.write_text("" if obj_vacio else "x")
    cuerpo = f'{sha_def}\nBASE_LIBRO_ORIG=aaaa; BASE_LIBRO_V5=bbbb; BASE_CAP=cccc\nM_LIBRO={m}; T_LIBRO={o}; M_CAP={m}; T_CAP={o}; M_IO={m}; T_IO={o}\n{fn}\necho "$(estado_libro) $(estado_cap) $(estado_io)"'
    return subprocess.run(["bash", "-c", cuerpo], capture_output=True, text=True).stdout.split()


def test_h4_main_y_objetivo_vacios_no_son_ya(tmp_path):
    assert _estados(tmp_path, True, True) == ["NO", "NO", "NO"]


def test_h4_objetivo_vacio_con_main_no_vacio_no_es_ya_y_el_caso_normal_si(tmp_path):
    assert "ya" not in _estados(tmp_path, False, True)
    assert _estados(tmp_path, False, False) == ["ya", "ya", "ya"]


# ---------------------------------------------------------------- H6: el dry-run no escribe el AVISO_LOG
def _avisos(tmp_path, ejecutar):
    src = SCRIPT.read_text()
    fn = src[src.index("aviso_critico() {"):src.index("act() {")]
    cuerpo = f'EJECUTAR={ejecutar}; SUSTITUYE=0; LOCK=0; AVISO_LOG={tmp_path}/logs/aviso.log; log() {{ :; }}; telegram() {{ :; }}\n{fn}\naviso_critico "ABORTO: x"; aviso_ok "DESPLIEGUE OK"'
    subprocess.run(["bash", "-c", cuerpo], capture_output=True, text=True)
    return tmp_path / "logs/aviso.log"


def test_h6_dry_run_no_escribe_aviso_log_y_ejecutar_si(tmp_path):
    assert not _avisos(tmp_path / "dry", 0).exists() and not (tmp_path / "dry/logs").exists()
    f = _avisos(tmp_path / "real", 1)
    assert f.exists() and "ABORTO: x" in f.read_text() and "DESPLIEGUE OK" in f.read_text()


def test_h6_el_script_no_tiene_otra_escritura_directa_al_aviso_log_fuera_de_ejecutar():
    for l in SCRIPT.read_text().splitlines():
        if ">> \"$AVISO_LOG\"" in l:
            assert "EJECUTAR" in l or "telegram()" in l or "Telegram NO enviado" in l, l


# ---------------------------------------------------------------- H8: la fila G dura P5_G_S, no 3x
def test_h8_el_bucle_de_la_fila_G_itera_P5_G_S_entre_3():
    linea = [l for l in SCRIPT.read_text().splitlines() if "f5_de" in l and "seq 1" in l][0]
    expr = re.search(r'seq 1 (\$\(\(.*?\)\)) \)?"?\)?;', linea) or re.search(r'seq 1 (\$\(\(.*?\)\))', linea)
    assert expr, linea
    for g, n in ((60, 20), (10, 4), (3, 1)):
        out = subprocess.run(["bash", "-c", f'P5_G_S={g}; echo {expr.group(1)}'], capture_output=True, text=True).stdout.strip()
        assert int(out) * 3 >= g and (int(out) - 1) * 3 < g, (g, out)
    assert "sleep 3" in linea


# ---------------------------------------------------------------- H7: la base de data/markets es previa al ciclo (marca), no la del momento de adoptar el pid
def _p6_h7(tmp_path, con_base_marca):
    (tmp_path / "markets").mkdir(exist_ok=True); (tmp_path / "cfg").mkdir(exist_ok=True)
    sl = tmp_path / "slow.log"; sl.write_text("previo\n")
    e = {"P6_ESPERA_S": "6", "P6_CICLO_S": "10", "P6_PASO": "0.2", "SLOW": str(sl), "MARKETS_DIR": str(tmp_path / "markets"), "CFGDIR": str(tmp_path / "cfg")}
    hoy = "$(date -u +%F)"
    pre = 'P6_M0=$(snap_markets); P6_A0=$(adelanto_firma)\n' if con_base_marca else ""
    cuerpo = (f'cap_pre=""; P6_MARCA_TS=$(( $(date +%s) - 10 )); P6_MARCA_OFF=$(stat -c %s $SLOW)\n{pre}'
              f'setsid sleep 3 & p=$!; printf "%s 1 /x/python {REPO}/capture_markets.py\\n" $p > "$PSF"\n'
              f'echo "[t] --- Ciclo slow 5 ---" >> $SLOW; echo fila >> "$MARKETS_DIR/{hoy}.csv"; echo "  Eventos unicos" >> $SLOW; echo "[t] === Fin ===" >> $SLOW\n'
              f'verifica_capture $SLOW; echo "rc=$? $CAP_MOTIVO"')
    return sh(tmp_path, cuerpo, "", e, timeout=60)


def test_h7_el_crecimiento_previo_a_la_adopcion_cuenta_si_la_base_es_la_de_la_marca(tmp_path):
    out = _p6_h7(tmp_path, True)
    assert "rc=0" in out, out


# ---------------------------------------------------------------- R4: crecimiento de un ciclo VIEJO que acabo tras la marca no cuenta para el nuevo
def _p6_r4(tmp_path, nuevo_escribe):
    (tmp_path / "markets").mkdir(exist_ok=True); (tmp_path / "cfg").mkdir(exist_ok=True)
    sl = tmp_path / "slow.log"; sl.write_text("previo\n")
    e = {"P6_ESPERA_S": "8", "P6_CICLO_S": "12", "P6_PASO": "0.2", "SLOW": str(sl), "MARKETS_DIR": str(tmp_path / "markets"), "CFGDIR": str(tmp_path / "cfg")}
    hoy = "$(date -u +%F)"
    esc = f'echo fila >> "$MARKETS_DIR/{hoy}.csv"; ' if nuevo_escribe else ""
    cuerpo = (f'cap_pre=""; P6_MARCA_TS=$(( $(date +%s) - 20 )); P6_MARCA_OFF=$(stat -c %s $SLOW); P6_M0=$(snap_markets); P6_A0=$(adelanto_firma)\n'
              f'echo fila >> "$MARKETS_DIR/{hoy}.csv"         # el ciclo VIEJO escribe tras la marca y antes de que arranque el nuevo\n'
              f'sleep 4\n'
              f'setsid sleep 4 & p=$!; printf "%s 1 /x/python {REPO}/capture_markets.py\\n" $p > "$PSF"\n'
              f'echo "[t] --- Ciclo slow 5 ---" >> $SLOW; sleep 1; {esc}echo "  Eventos unicos" >> $SLOW; echo "[t] === Fin ===" >> $SLOW\n'
              f'verifica_capture $SLOW; echo "rc=$? $CAP_MOTIVO"')
    return sh(tmp_path, cuerpo, "", e, timeout=60)


def test_r4_lo_escrito_por_el_ciclo_viejo_tras_la_marca_no_es_crecimiento_del_nuevo(tmp_path):
    out = _p6_r4(tmp_path, False)
    assert "rc=1" in out and "NO crecio" in out, out


def test_r4_lo_escrito_por_el_ciclo_nuevo_si_cuenta(tmp_path):
    assert "rc=0" in _p6_r4(tmp_path, True)


# ---------------------------------------------------------------- T3: sin el arranque del pid nuevo, fail-closed (inconcluso); margen del mtime probado
def test_t3_sin_arranque_del_pid_nuevo_es_inconcluso_nunca_la_regla_antigua(tmp_path):
    (tmp_path / "markets").mkdir(); (tmp_path / "cfg").mkdir()
    sl = tmp_path / "slow.log"; sl.write_text("previo\n")
    e = {"P6_ESPERA_S": "6", "P6_CICLO_S": "10", "P6_PASO": "0.2", "SLOW": str(sl), "MARKETS_DIR": str(tmp_path / "markets"), "CFGDIR": str(tmp_path / "cfg")}
    hoy = "$(date -u +%F)"
    cuerpo = (f'cap_pre=""; P6_MARCA_TS=$(( $(date +%s) - 10 )); P6_MARCA_OFF=$(stat -c %s $SLOW)\n'
              f'setsid sleep 3 & p=$!; printf "%s 1 /x/python {REPO}/capture_markets.py\\n" $p > "$PSF"\n'
              f'echo "[t] --- Ciclo slow 5 ---" >> $SLOW; echo fila >> "$MARKETS_DIR/{hoy}.csv"; echo "[t] === Fin ===" >> $SLOW\n'
              f'proc_inicio() {{ return 1; }}\n'      # /proc ilegible: el arranque del pid nuevo no se puede leer
              f'cap_arranca_tras_marca() {{ return 0; }}\n'
              f'verifica_capture $SLOW; echo "rc=$? $CAP_MOTIVO"')
    out = sh(tmp_path, cuerpo, "", e, timeout=60)
    assert "rc=2" in out and "no se pudo leer el arranque" in out, out


def _crecio(tmp_path, mtime_rel_inicio, slack=None):
    f = tmp_path / "2026-11-14.csv"; f.write_text("a\nb\n")
    ini = 1_800_000_000
    os.utime(f, (ini + mtime_rel_inicio, ini + mtime_rel_inicio))
    env = {"MARKETS_DIR": str(tmp_path)}
    if slack is not None: env["P6_MTIME_SLACK_S"] = str(slack)
    return sh(tmp_path, f'markets_crecio "2026-11-14 0" {ini}.0 && echo SI || echo NO', env=env).strip()


def test_t3_margen_del_mtime_3s_por_defecto_documentado_y_probado(tmp_path):
    assert _crecio(tmp_path, +5) == "SI"          # escrito tras el arranque
    assert _crecio(tmp_path, -2) == "SI"          # dentro del margen (btime entero/NTP)
    assert _crecio(tmp_path, -3) == "SI"          # justo en el borde
    assert _crecio(tmp_path, -4) == "NO"          # un ciclo viejo que acabo 4 s antes: no cuenta
    assert _crecio(tmp_path, -4, slack=5) == "SI" # configurable
    assert "P6_MTIME_SLACK_S" in LIB.read_text() and "btime" in LIB.read_text()


# ---------------------------------------------------------------- T4: el conf entra en el sello e2e (script, conftest y test del sandbox)
def test_t4_clases_error_conf_esta_en_las_tres_listas_del_sello_e2e():
    d = SCRIPT.read_text(); c = (V3 / "tests/conftest.py").read_text(); t = (V3 / "tests/test_deploy_sandbox.py").read_text()
    assert '$V3/deploy/clases_error.conf' in d.split("E2E_FILES=(")[1].split(")")[0]
    assert 'deploy/clases_error.conf' in c and 'deploy/clases_error.conf' in t
    assert d.index('p6_ciclo_aislado.py" "$V3/deploy/clases_error.conf"') > 0 and c.index('p6_ciclo_aislado.py", _V3 / "deploy/clases_error.conf"') > 0


# ---------------------------------------------------------------- T8: la fila G no descomprime 5000 lineas cada 3 s
def test_t8_fila_G_lee_lo_minimo():
    linea = [l for l in SCRIPT.read_text().splitlines() if "f5_de" in l and "seq 1" in l][0]
    assert "head -n 200" in linea and "5000" not in linea


# ---------------------------------------------------------------- T9: _cfg_escribe compara contenido; adelanto_activo solo con entero > 0
def _cfg9(tmp_path, pre, cuerpo, env=None):
    d = tmp_path / "univ"; d.mkdir(exist_ok=True)
    for k, v in pre.items(): (d / k).write_text(v)
    return sh(tmp_path, cuerpo, env={"CFGDIR": str(d), "CFG_MANIFEST": str(tmp_path / "man.txt"), "CONFIRMO_ADELANTO_6_MONEDAS": "1", **(env or {})})


def test_t9_cfg_existente_con_otro_valor_no_cuenta_como_activado(tmp_path):
    out = _cfg9(tmp_path, {"cfg_CAPTURE_5M_HORIZONTE_MIN": "7"}, 'activar_cfg; echo "rc=$?"')
    assert "rc=1" in out and (tmp_path / "univ/cfg_CAPTURE_5M_HORIZONTE_MIN").read_text() == "7" and not (tmp_path / "univ/cfg_CAPTURE_429_FIX").exists()


def test_t9_cfg_existente_con_el_valor_esperado_si_cuenta(tmp_path):
    out = _cfg9(tmp_path, {"cfg_CAPTURE_429_FIX": "1\n", "cfg_CAPTURE_5M_HORIZONTE_MIN": "1440"}, 'activar_cfg; echo "rc=$?"')
    assert "rc=0" in out


@pytest.mark.parametrize("contenido,activo", [("1440", True), ("1\n", True), ("0", False), ("", False), ("\n", False), ("abc", False), ("-5", False), ("007", True)])
def test_t9_adelanto_activo_solo_con_entero_positivo(tmp_path, contenido, activo):
    out = _cfg9(tmp_path, {"cfg_CAPTURE_5M_HORIZONTE_MIN": contenido}, 'adelanto_activo && echo SI || echo NO')
    assert out.strip() == ("SI" if activo else "NO"), repr(contenido)


def test_t9_la_variable_de_entorno_manda_y_0_no_activa(tmp_path):
    assert _cfg9(tmp_path, {}, 'adelanto_activo && echo SI || echo NO', env={"CAPTURE_5M_HORIZONTE_MIN": "0"}).strip() == "NO"
    assert _cfg9(tmp_path, {}, 'adelanto_activo && echo SI || echo NO', env={"CAPTURE_5M_HORIZONTE_MIN": "60"}).strip() == "SI"
