"""Unidades de lo nuevo (2a pasada de revision): runner de P6 aislado, P6 de ciclo real, parada del capture en curso, padre observadores envuelto, libro5 por pid a
traves de las 00:00Z, lock bnreg por /proc/locks (sin adquirirlo), contrato con verify_deploy, sello e2e, y sembrar_cache_tokens (rc de ESTA ejecucion, guardado
incremental, presupuesto de tiempo, rutas derivadas de --cache)."""
import importlib.util, json, os, subprocess, sys, time
from datetime import datetime, timedelta, timezone
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_espera_hijos import sh, OBS, H, REPO, V3, LIB          # noqa: E402

RUNNER = V3 / "deploy" / "p6_ciclo_aislado.py"
PY = "/root/polymarket-research/.venv/bin/python"


# ------------------------------------------------------------------ runner de P6 aislado (captura real en dir temporal)
FAKE_CAP = '''
import os, sys, pathlib
modo = os.environ.get("FAKE_CAP_MODO", "ok")
def una_captura():
    p = pathlib.Path("data/markets"); p.mkdir(parents=True, exist_ok=True)
    estado = pathlib.Path(os.environ.get("FAKE_CAP_ESTADO", "/nonexistent"))
    if modo == "ok": (p / "x.csv").write_text("h\\nfila\\n"); print("Eventos unicos: 1")
    elif modo == "error_capturado": print("  ERROR polymarket: NameError: name 'zz' is not defined")
    elif modo == "traceback": raise NameError("zz")
    elif modo == "429": print("  429 gamma slug=x: rafaga abortada")
    elif modo == "429_luego_ok":
        if estado.exists(): (p / "x.csv").write_text("h\\nfila\\n")
        else: estado.write_text("1"); print("  429 gamma slug=x offset=0: rafaga abortada (la lista parcial NO se guardara)")       # formato REAL (L2: la excusa va anclada)
    elif modo == "adelanto":
        (p / "x.csv").write_text("h\\nfila\\n"); (pathlib.Path(os.environ["UNIVERSO_5M_DIR"]) / "adelanto_2026-11-14.csv").write_text("x")
    elif modo == "sin_filas": print("  nada que decir")
    elif modo == "429_falso": print("  precio 94290.5 en 1429 mercados, hora 10:42:9")                 # NO es un 429
    elif modo == "conn_fuera": raise ConnectionError("Max retries exceeded: red caida")               # red fuera de los try: Traceback sin ser un bug
    elif modo == "rc3_sin_traza": print("  algo raro"); sys.exit(3)
    elif modo == "matado": os.kill(os.getpid(), 9)
    elif modo == "valor": raise ValueError("ahora SI es de la clase de bugs de codigo (M3)")
    elif modo == "oserror_timeout": raise OSError("connection timed out")                               # OSError con causa transitoria: no es de codigo (M3)
    elif modo == "keyerror": raise KeyError("clave")
    elif modo == "gamma_keyerror": print("  Error gamma slug=x offset=0: KeyError: 'id'")
    elif modo == "gamma_keyerror_luego_ok":
        if estado.exists(): (p / "x.csv").write_text("h\\nfila\\n")
        else: estado.write_text("1"); print("  Error gamma slug=x offset=0: KeyError: 'id'")
    elif modo == "excepcion_al_inicio_de_linea": print("ValueError: texto suelto que NO es un traceback de capture_markets ni una linea de error")
    return 1, 1
'''


def runner(tmp_path, modo, intentos=2, extra=None):
    repo = tmp_path / "repo"; repo.mkdir(exist_ok=True)
    (repo / "capture_markets.py").write_text(FAKE_CAP)
    antes = sorted(p.name for p in repo.iterdir())
    r = subprocess.run([PY, str(RUNNER), "--repo", str(repo), "--tmp", str(tmp_path / "t"), "--timeout", "30", "--intentos", str(intentos), "--pausa", "0"],
                       capture_output=True, text=True, env={**os.environ, "FAKE_CAP_MODO": modo, "FAKE_CAP_ESTADO": str(tmp_path / "estado"), **(extra or {})}, timeout=120)
    assert sorted(p.name for p in repo.iterdir()) == antes, "el runner NO debe escribir en el repo"
    return r


@pytest.mark.parametrize("modo,rc,frag", [("ok", 0, "OK intento 1"), ("error_capturado", 1, "NameError"), ("traceback", 1, "NameError"),
                                          ("429", 2, "INCONCLUSO"), ("429_luego_ok", 0, "OK intento 2"), ("adelanto", 1, "adelanto APAGADO"),
                                          ("sin_filas", 1, "0 filas"), ("keyerror", 1, "KeyError"),
                                          ("429_falso", 1, "0 filas"),                      # '1429' / '94290.5' / una hora NO son un 429: sin excusa => fallo
                                          # hallazgo 4: rc != 0 SIN evidencia de bug (red fuera de los try, rc raro, proceso matado, excepcion ajena) => INCONCLUSO, nunca FALLO
                                          ("conn_fuera", 2, "causa transitoria"), ("rc3_sin_traza", 2, "sin error de codigo ni causa conocida"),
                                          ("matado", 2, "sin error de codigo ni causa conocida"),
                                          # M3: ValueError/RuntimeError/OSError cuentan como codigo, salvo con causa transitoria en la misma linea
                                          ("valor", 1, "ValueError"), ("oserror_timeout", 2, "causa transitoria"),
                                          # #3/#4: una linea de datos ('Error gamma ..: KeyError') sin filas no decide; el rc 1 solo si se repite en TODOS los intentos (aqui 2 de 2)
                                          ("gamma_keyerror", 2, "TODOS los intentos"), ("gamma_keyerror_luego_ok", 0, "OK intento 2"),
                                          ("excepcion_al_inicio_de_linea", 1, "0 filas")])
def test_runner_p6_aislado_veredicto_determinista(tmp_path, modo, rc, frag):
    r = runner(tmp_path, modo)
    assert r.returncode == rc and frag in r.stdout, (r.returncode, r.stdout, r.stderr)


# ------------------------------------------------------------------ padre observadores: cmdline envuelta (hallazgo 9)
@pytest.mark.parametrize("padre,ok", [
    ("choom -n -300 -- .venv/bin/python observadores_fase0.py", True),
    ("nice -n 10 choom -n -300 -- .venv/bin/python -u observadores_fase0.py --x", True),
    ("bash -c cd /root/polymarket-research && .venv/bin/python observadores_fase0.py >> logs/o.log 2>&1", True),
    ("vim observadores_fase0.py.bak", False), ("python mi_observadores_fase0.py", False), ("python otro.py", False)])
def test_padre_observadores_envuelto_en_cualquier_posicion(tmp_path, padre, ok):
    ps = f"900 1 {padre}\n" + H(99)
    assert sh(tmp_path, 'echo "[$(hijos_vivos)]"', ps).strip() == ("[99]" if ok else "[]")


def test_padre_no_reconocido_da_diagnostico_claro_y_no_un_falso_exito(tmp_path):
    ps = "900 1 python lanzador_raro.py\n" + H(99)
    out = sh(tmp_path, 'viejos="11"; espera_hijos; echo "rc=$?"; echo "$ESPERA_MOTIVO"; diag_padres', ps, {"P5_MUEREN_S": "1"})
    assert "rc=1" in out and "padre NO reconocido" in out and "lanzador_raro.py" in out, out


# ------------------------------------------------------------------ libro5 por pid a traves de las 00:00Z (hallazgo 7)
def test_libro5_crece_cruza_medianoche_sin_falso_fallo(tmp_path):
    (tmp_path / "libro5").mkdir()
    ayer = tmp_path / "libro5" / "libro5_ms_2026-11-13_99.csv.gz"; ayer.write_text("G,1\n")
    hoy = tmp_path / "libro5" / "libro5_ms_2026-11-14_99.csv.gz"
    out = sh(tmp_path, f'(sleep 0.5; echo "G,2" > {hoy}) &\nlibro5_crece 99 4; echo "rc=$?"; echo "f5=$(f5_de 99)"')           # el fichero de AYER ya no crece; aparece el de HOY
    assert "rc=0" in out and out.strip().endswith("libro5_ms_2026-11-13_99.csv.gz"), out                                # f5_de = el mas antiguo (lleva la G de arranque)
    assert "rc=1" in sh(tmp_path, "libro5_crece 99 1; echo rc=$?")                                                      # nada crece: sigue siendo DURO


# ------------------------------------------------------------------ L5: el lock de bnreg se LEE de /proc/locks, nunca se adquiere
def test_lock_bnreg_por_proc_locks_sin_adquirirlo(tmp_path):
    lk = tmp_path / "bn.lock"; lk.write_text("")
    assert "rc=1" in sh(tmp_path, f'lock_tomado_por 1 {lk}; echo rc=$?')
    assert subprocess.run(["flock", "-n", str(lk), "true"]).returncode == 0              # sin nadie dentro, la sonda no lo deja tomado ni lo toca
    h = subprocess.Popen(["flock", str(lk), "sleep", "30"]); time.sleep(0.5)
    try:
        assert "rc=0" in sh(tmp_path, f'lock_tomado_por {h.pid} {lk}; echo rc=$?')
        assert "rc=1" in sh(tmp_path, f'lock_tomado_por {h.pid + 1} {lk}; echo rc=$?')    # otro pid no es el dueno
        assert subprocess.run(["flock", "-n", str(lk), "true"]).returncode == 1          # y el dueno sigue teniendolo (la sonda no se lo quito)
    finally:
        h.kill(); h.wait()


def test_ninguna_sonda_flock_n_sobre_el_lock_de_bnreg():
    for f in (V3 / "deploy/lib_espera_hijos.sh", V3 / "deploy/deploy_deltas_libro_ws_once.sh"):
        assert "flock -n" not in f.read_text() and "-c true" not in f.read_text(), f


# ------------------------------------------------------------------ L4: contrato con verify_deploy (solo lectura)
def test_contrato_verify_deploy_real_pasa_y_es_solo_lectura(tmp_path):
    out = subprocess.run(["bash", "-c", f'log() {{ :; }}; . {LIB}; contrato_verify_deploy; echo "rc=$? $CONTRATO_MOTIVO"'], capture_output=True, text=True,
                         env={**os.environ, "REPO": "/root/polymarket-research", "PY": PY}, timeout=90).stdout       # ps REAL (no el falso de sh())
    assert "rc=0" in out, out


@pytest.mark.parametrize("vd,pw,frag", [("print('otra cosa')\n# \"--restart\"\n", None, "formato"), ("print('x')\n", None, "--restart"),
                                        ("print('\\u2705 observadores FRESH  pid=1')\n# \"--restart\"\n", "SCREEN_RESTART = {}\n", "SCREEN_RESTART")])
def test_contrato_verify_deploy_detecta_cambios(tmp_path, vd, pw, frag):
    r = tmp_path / "r"; r.mkdir()
    (r / "verify_deploy.py").write_text(vd)
    (r / "pipeline_watchdog.py").write_text(pw or '    "observadores": "cd x && python observadores_fase0.py",\n')
    out = sh(tmp_path, 'contrato_verify_deploy; echo "rc=$? $CONTRATO_MOTIVO"', env={"REPO": str(r), "PY": PY})
    assert "rc=1" in out and frag in out, out


# ------------------------------------------------------------------ L1: sello del ensayo e2e
def test_sello_e2e(tmp_path):
    f = tmp_path / "f.txt"; f.write_text("a")
    h = subprocess.run(["bash", "-c", f". {LIB}; e2e_sha {f}"], capture_output=True, text=True).stdout.strip()
    st = tmp_path / "s.json"
    chk = lambda: sh(tmp_path, f'e2e_sello_ok {st} {f}; echo "rc=$? $E2E_MOTIVO"', env={"PY": PY})
    assert "rc=1" in chk() and "no hay sello" in chk()
    st.write_text(json.dumps({"sha": h, "ts": int(time.time()), "pasados": 5})); assert "rc=0" in chk()
    st.write_text(json.dumps({"sha": "x" * 32, "ts": int(time.time()), "pasados": 5})); assert "OTRA version" in chk()
    st.write_text(json.dumps({"sha": h, "ts": int(time.time()) - 25 * 3600, "pasados": 5})); assert "mas de 24 h" in chk()
    st.write_text(json.dumps({"sha": h, "ts": int(time.time()), "pasados": 3})); assert "cubre 3 tests" in chk()
    st.write_text("no json"); assert "rc=1" in chk()


# ------------------------------------------------------------------ P6 ciclo real (verifica_capture) con un capture_markets "vivo" (sleeper real)
def _p6(tmp_path, escribe, env=None, cap_pre="111", cfg=False, pre_slow="previo\n", espera="6", vive=2):
    """Lanza verifica_capture; en segundo plano aparece un capture_markets (sleeper real `vive` s) y `escribe` (shell) actua mientras vive."""
    (tmp_path / "markets").mkdir(exist_ok=True); (tmp_path / "cfg").mkdir(exist_ok=True)
    sl = tmp_path / "slow.log"; sl.write_text(pre_slow)
    if cfg: (tmp_path / "cfg/cfg_CAPTURE_5M_HORIZONTE_MIN").write_text("1440")
    e = {"P6_ESPERA_S": espera, "P6_CICLO_S": "10", "P6_PASO": "0.2", "SLOW": str(sl), "MARKETS_DIR": str(tmp_path / "markets"), "CFGDIR": str(tmp_path / "cfg"), **(env or {})}
    cuerpo = (f'cap_pre="{cap_pre}"; P6_MARCA_TS=$(( $(date +%s) - 10 )); P6_MARCA_OFF=$(stat -c %s $SLOW)\n'
              f'(sleep 0.3; setsid sleep {vive} & p=$!; printf "%s 1 /x/python {REPO}/capture_markets.py\\n" $p > "$PSF"; echo "[t] --- Ciclo slow 5 ---" >> $SLOW; sleep 0.8; {escribe}; echo "[t] === Fin ===" >> $SLOW) &\n'
              f'verifica_capture $SLOW; echo "rc=$? $CAP_MOTIVO"')
    return sh(tmp_path, cuerpo, "", e, timeout=60), sl


HOY = "$(date -u +%F)"
CRECE = f'echo fila >> "$MARKETS_DIR/{HOY}.csv"'


def test_p6_ciclo_real_ok_y_errores(tmp_path):
    out, _ = _p6(tmp_path, f'{CRECE}; echo "  Eventos unicos" >> $SLOW')
    assert "rc=0" in out, out


@pytest.mark.parametrize("final,rc", [("ImportError: boom", 1), ("NameError: x", 1), ("requests.exceptions.ConnectionError: x", 0), ("ValueError: raro", 1),
                                        ("RuntimeError: x", 1), ("OSError: [Errno 28] No space left on device", 0), ("OSError: [Errno 110] Connection timed out", 0)])
def test_p6_traceback_solo_duro_si_es_error_de_codigo_del_ciclo_nuevo(tmp_path, final, rc):
    tb = f'Traceback (most recent call last):\\n  File "{REPO}/capture_markets.py", line 3, in una_captura\\n{final}\\n'
    out, _ = _p6(tmp_path, f'{CRECE}; printf "{tb}" >> $SLOW')
    assert f"rc={rc}" in out, out


def test_p6_traceback_del_ciclo_VIEJO_anterior_al_nuevo_no_cuenta(tmp_path):
    viejo = f'Traceback (most recent call last):\n  File "{REPO}/capture_markets.py", line 3, in f\nNameError: del ciclo viejo\n'
    out, _ = _p6(tmp_path, CRECE, pre_slow=viejo)          # ya estaba en slow.log al desplegar (ciclo viejo en curso): fuera del offset del ciclo nuevo
    assert "rc=0" in out, out


def test_p6_error_de_codigo_capturado_por_una_captura_es_duro(tmp_path):
    out, _ = _p6(tmp_path, f'{CRECE}; echo "  ERROR polymarket: AttributeError: x" >> $SLOW')
    assert "rc=1" in out and "error de codigo" in out, out


def test_p6_data_markets_no_crece_sin_excusa_es_duro_y_con_429_es_inconcluso(tmp_path):
    out, _ = _p6(tmp_path, 'echo "ciclo" >> $SLOW')
    assert "rc=1" in out and "NO crecio" in out, out
    out, _ = _p6(tmp_path, 'echo "  429 gamma: rafaga abortada" >> $SLOW')
    assert "rc=2" in out and "crecimiento no verificado" in out, out          # (4): el 429 ya NO excusa por si solo: sin crecimiento es inconcluso (el despliegue lo cubre con la captura aislada o rc 4)


def test_p6_adelanto_escrito_con_el_adelanto_apagado_es_duro_y_encendido_no(tmp_path):
    esc = f'{CRECE}; echo x > "$CFGDIR/adelanto_2026-11-14.csv"'
    out, _ = _p6(tmp_path, esc)
    assert "rc=1" in out and "ESCRIBIO ficheros de adelanto" in out, out
    out, _ = _p6(tmp_path, esc, cfg=True)
    assert "rc=0" in out, out


def test_p6_slow_log_rotado_no_es_atribuible_y_no_decide(tmp_path):
    out, _ = _p6(tmp_path, f'{CRECE}; printf "{"Traceback (most recent call last):"}\\n  File \\"{REPO}/capture_markets.py\\", line 3, in f\\nNameError: x\\n" > $SLOW',
                 pre_slow="A" * 500 + "\n")                  # slow.log truncado/rotado (mas corto que el offset): se relee desde 0
    assert "rc=2" in out and "rotado" in out, out                  # un log rotado/truncado no se relee desde 0 (mezclaria el ciclo viejo): inconcluso


def test_p6_sin_ciclo_nuevo_o_que_no_termina_es_no_verificado(tmp_path):
    (tmp_path / "markets").mkdir(); (tmp_path / "slow.log").write_text("x\n")
    out = sh(tmp_path, 'cap_pre="111"; P6_MARCA_TS=$(date +%s); verifica_capture $TMP/slow.log; echo "rc=$?"', "", {"P6_ESPERA_S": "1", "P6_PASO": "0.2", "MARKETS_DIR": str(tmp_path / "markets"), "CFGDIR": str(tmp_path)})
    assert "rc=2" in out, out
    out, _ = _p6(tmp_path, CRECE, env={"P6_CICLO_S": "1"}, vive=5)
    assert "rc=2" in out and "no termino" in out, out


# ------------------------------------------------------------------ L3: parar el capture_markets en curso
def _sleeper(ignora_term=False):
    cmd = "setsid bash -c 'trap \"\" TERM; exec -a x sleep 300' >/dev/null 2>&1 & echo $!" if ignora_term else "setsid sleep 300 >/dev/null 2>&1 & echo $!"
    return int(subprocess.run(["bash", "-c", cmd], capture_output=True, text=True).stdout.strip())


@pytest.mark.parametrize("ignora_term", [False, True])
def test_parar_capture_en_curso_term_y_kill_y_adelanto_estable(tmp_path, ignora_term):
    v = _sleeper(ignora_term); (tmp_path / "cfg").mkdir()
    try:
        out = sh(tmp_path, 'parar_capture_en_curso; echo "rc=$? $CAP_PARADA"', f"{v} 1 /x/python {REPO}/capture_markets.py\n", {"CFGDIR": str(tmp_path / "cfg"), "P6_TERM_S": "1", "P6_ESTABLE_ADEL_S": "1"})
        assert "rc=0" in out and not os.path.exists(f"/proc/{v}") or "zombie" in open(f"/proc/{v}/status").read().lower(), out
    finally:
        subprocess.run(["kill", "-9", str(v)], capture_output=True)


def test_parar_capture_falla_si_el_adelanto_sigue_escribiendose(tmp_path):
    v = _sleeper(); (tmp_path / "cfg").mkdir()
    w = subprocess.Popen(["bash", "-c", f'for i in $(seq 1 60); do echo $i >> {tmp_path}/cfg/adelanto_x.csv; sleep 0.2; done'])
    try:
        out = sh(tmp_path, 'parar_capture_en_curso; echo "rc=$? $CAP_PARADA"', f"{v} 1 /x/python {REPO}/capture_markets.py\n", {"CFGDIR": str(tmp_path / "cfg"), "P6_TERM_S": "1", "P6_ESTABLE_ADEL_S": "1"})
        assert "rc=1" in out and "siguen cambiando" in out, out
    finally:
        w.kill(); subprocess.run(["kill", "-9", str(v)], capture_output=True)


# ------------------------------------------------------------------ sembrar_cache_tokens: rc de ESTA ejecucion, guardado incremental, presupuesto, rutas de --cache
def _cargar_seeder():
    sp = importlib.util.spec_from_file_location("sembrar_cache_tokens_t", str(V3 / "delta_v3/sembrar_cache_tokens.py"))
    S = importlib.util.module_from_spec(sp); sp.loader.exec_module(S)
    S.REPO = "/root/polymarket-research"
    return S


def _csv_mercados(d, n):
    d.mkdir(exist_ok=True)
    ahora = datetime.now(timezone.utc)
    cab = open(f"/root/polymarket-research/data/markets/{ahora:%Y-%m-%d}.csv").readline()
    filas = []
    for i in range(n):
        fin = (ahora + timedelta(minutes=30 + 5 * i)).replace(second=0, microsecond=0)
        q = f"Bitcoin Up or Down - November 14, 1:00AM-1:05AM ET"
        filas.append(f'{ahora.isoformat(timespec="seconds")},{9000 + i},0x{i + 1:064x},"{q}",btc-updown-5m-{1794640000 + i * 300},{fin:%Y-%m-%dT%H:%M:%S},,,,0.5,0.5,"[""Up"", ""Down""]",0.49,0.51,0.02,,,,1,t,s,Up or Down|Crypto Prices|5M')
    (d / f"{ahora:%Y-%m-%d}.csv").write_text(cab + "\n".join(filas) + "\n")


@pytest.fixture(scope="module")
def seeder():
    return _cargar_seeder()


def _ejecuta(S, tmp_path, n=3, resolver=None, extra=(), cache_previa=None):
    L = S.cargar_modulos(S.REPO)
    _csv_mercados(tmp_path / "m", n)
    cache = tmp_path / "cache.json"
    if cache_previa is not None: cache.write_text(json.dumps(cache_previa))
    yes, no = "1" * 70, "2" * 70
    L._resolver_mercado = resolver or (lambda sess, mid, cid, est, dl: (yes, no, False, None))
    L._sesion_datos = lambda: None
    S.cargar_modulos = lambda repo: L
    for d in (L._TOK, L._MKT, L._CACHE_ENTRIES): d.clear()
    L._GAMMA["score"] = 0
    rc = S.main(["--cache", str(cache), "--markets-dir", str(tmp_path / "m"), "--tasa", "1000", *extra])
    return rc, cache, L


def test_seeder_rc_por_lo_sembrado_en_esta_ejecucion_aunque_la_cache_traiga_vencidos(tmp_path, seeder):
    viejo = {"v": 1, "guardado": 1, "mercados": {"1": {"yes": "1" * 70, "no": "2" * 70, "activo": "BTC", "marco": "5min", "cid": "0x1", "edt": "2020-01-01T00:00:00+00:00"}}, "tombstones": {}}
    rc, cache, L = _ejecuta(seeder, tmp_path, 3, cache_previa=viejo)
    j = json.loads(cache.read_text())
    assert rc == 0 and {"9000", "9001", "9002"} <= set(j["mercados"]), (rc, list(j["mercados"]))        # antes: un vencido ajeno en el fichero daba rc 3


def test_seeder_todos_fallidos_rc3_y_gamma_caida_rc2(tmp_path, seeder):
    (tmp_path / "a").mkdir(); (tmp_path / "b").mkdir()
    rc, _, _ = _ejecuta(seeder, tmp_path / "a", 3, resolver=lambda *a: (None, None, False, "http"))
    assert rc == 3                                                                       # nada sembrado en esta ejecucion
    def cae(sess, mid, cid, est, dl):
        est_L[0]._GAMMA["score"] = 10**6                                                 # gamma caida: el bucle corta
        return (None, None, False, "429")
    est_L = [seeder.cargar_modulos(seeder.REPO)]
    rc, _, _ = _ejecuta(seeder, tmp_path / "b", 3, resolver=cae)
    assert rc in (2, 3)


def test_seeder_guardado_incremental_y_presupuesto_de_tiempo(tmp_path, seeder, monkeypatch):
    monkeypatch.setattr(seeder, "GUARDA_CADA", 2)
    vistos = []
    def res(sess, mid, cid, est, dl):
        vistos.append(mid); time.sleep(0.15)
        return ("1" * 70, "2" * 70, False, None)
    rc, cache, L = _ejecuta(seeder, tmp_path, 8, resolver=res, extra=("--presupuesto-s", "0.5"))
    j = json.loads(cache.read_text())
    assert 0 < len(vistos) < 8 and rc == 0 and len(j["mercados"]) == len(vistos), (rc, len(vistos), len(j["mercados"]))     # el presupuesto corta el bucle y lo hecho queda guardado


def test_seeder_la_cache_y_el_lock_salen_de_cache_nunca_de_la_ruta_real(tmp_path, seeder):
    real_lock = Path("/root/polymarket-research-datalogs/libro_tokens_cache.json.lock")
    antes = real_lock.stat().st_mtime_ns if real_lock.exists() else None
    rc, cache, L = _ejecuta(seeder, tmp_path, 2)
    assert (tmp_path / "cache.json.lock").exists() and rc == 0
    assert (real_lock.stat().st_mtime_ns if real_lock.exists() else None) == antes
    assert seeder.GUARDA_CADA >= 1 and "--presupuesto-s" in (V3 / "deploy/deploy_deltas_libro_ws_once.sh").read_text()        # el deploy pasa un presupuesto < su timeout (+60)
