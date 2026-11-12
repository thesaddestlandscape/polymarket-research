#!/usr/bin/env python3
"""Pruebas EN SECO de los artefactos C6 del dry-run B-CXB60 (12-Nov). NO instala nada (ni cron, ni screen, ni toca pipeline_watchdog.py / verify_deploy.py reales: trabaja sobre COPIAS en un tmp), NO envia Telegram
(CXB60_SIN_TELEGRAM=1), NO lanza el dry-run. Ejecutar: python3 -I test_c6_seco.py"""
import os, sys, json, time, shutil, tempfile, subprocess, datetime as dt, importlib.util, ast, re
H = os.path.dirname(os.path.abspath(__file__)) + '/'; DR = os.path.dirname(H.rstrip('/')) + '/'; REPO = '/root/polymarket-research/'
TMP = tempfile.mkdtemp(prefix='c6_test_'); ENV = dict(os.environ, CXB60_SIN_TELEGRAM='1', CXB60_PY=sys.executable)


def test_parche_watchdog_verify():
    d = TMP + '/repo'; os.makedirs(d)
    for f in ('pipeline_watchdog.py', 'verify_deploy.py'): shutil.copy(REPO + f, d + '/' + f)
    r = subprocess.run(['patch', '-p1', '-d', d, '--no-backup-if-mismatch'], stdin=open(H + 'watchdog_verify_cxb60.patch'), capture_output=True, text=True); assert r.returncode == 0, r.stdout + r.stderr
    for f in ('pipeline_watchdog.py', 'verify_deploy.py'): subprocess.run([sys.executable, '-m', 'py_compile', d + '/' + f], check=True)
    # pipeline_watchdog: la clave esta en SCREEN_RESTART (AST) y en check_screens, y el comando apunta a un runner que existe, con nice/ionice/ulimit y sin choom ni credenciales
    src = open(d + '/pipeline_watchdog.py').read(); tree = ast.parse(src); sr = None
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign) and any(getattr(t, 'id', '') == 'SCREEN_RESTART' for t in n.targets): sr = n.value
    claves = [k.value for k in sr.keys if isinstance(k, ast.Constant)]; assert 'cxb60dry' in claves and claves.count('cxb60dry') == 1
    cmd = next(ast.get_source_segment(src, v) for k, v in zip(sr.keys, sr.values) if isinstance(k, ast.Constant) and k.value == 'cxb60dry')
    assert 'cxb60_dryrun_fase0.py' in cmd and 'ulimit -v 7000000' in cmd and 'nice -n 15 ionice -c3' in cmd and 'choom' not in cmd and '.env' not in cmd and 'logs/cxb60_dryrun.log' in cmd and 'exec' in cmd
    assert os.path.exists(REPO + 'experimentos/5m_barato/l2_carrera_10nov/dryrun/cxb60_dryrun_fase0.py')
    assert '"bnreg", "cxb60dry"]' in src                                                              # y se anade SIN pisar el cambio previo (bnreg) del arbol de trabajo
    # el comando se ejecuta bien en un `bash -c` SECO: sustituyo el .py por un eco para probar el entrecomillado/exec/redireccion (no lanza el runner)
    cmd_txt = cmd.strip().strip('f').strip('"'); sec = cmd_txt.replace('{REPO}', TMP).replace('.venv/bin/python -I experimentos/5m_barato/l2_carrera_10nov/dryrun/cxb60_dryrun_fase0.py', 'echo ARRANQUE_SECO')
    os.makedirs(TMP + '/logs', exist_ok=True); r = subprocess.run(['bash', '-c', sec], capture_output=True, text=True); assert r.returncode == 0, (r.stdout, r.stderr, sec)
    assert 'ARRANQUE_SECO' in open(TMP + '/logs/cxb60_dryrun.log').read()
    # verify_deploy: entrada con entry existente y probe `fresh:` sobre el heartbeat; el resto de probes (log:, http:, None) NO cambian de comportamiento
    spec = importlib.util.spec_from_file_location('vd_parcheado', d + '/verify_deploy.py'); vd = importlib.util.module_from_spec(spec); spec.loader.exec_module(vd); vd.BASE = vd.Path(REPO)
    e = vd.SCREENS['cxb60dry']; assert e['probe'].startswith('fresh:') and e['probe'].endswith('/heartbeat.json:180') and (vd.BASE / e['entry']).exists()
    ci = vd.cierre_imports(vd.BASE / e['entry']); assert len(ci) >= 1; pr = vd.proceso_de(e['entry']); assert pr is None or len(pr) == 2        # (con un `guard_rss.py ... cxb60_dryrun_fase0.py` esperando en la maquina, proceso_de lo toma por el runner: trampa del pid fantasma ya documentada)
    assert vd.probe_ok(None, 0) == (True, 'sin probe (basta proceso vivo)') and vd.probe_ok('otra:cosa', 0)[0] is False
    vd.BASE = vd.Path(TMP); hb = TMP + '/hb_probe.json'; spec_f = f'fresh:{hb}:180'
    assert not vd.probe_ok(spec_f, 0)[0]                                                                                    # no existe
    json.dump(dict(status='RUNNING'), open(hb, 'w')); ok, msg = vd.probe_ok(spec_f, 0); assert ok, msg                        # fresco, RUNNING
    assert not vd.probe_ok(spec_f, time.time() + 5)[0]                                                                      # sin escrituras desde el restart
    os.utime(hb, (time.time() - 400, time.time() - 400)); ok, msg = vd.probe_ok(spec_f, 0); assert not ok and 'parado hace' in msg, msg      # heartbeat viejo
    json.dump(dict(status='STOPPED_FAILED'), open(hb, 'w')); ok, msg = vd.probe_ok(spec_f, 0); assert not ok and 'STOPPED' in msg, msg
    open(hb, 'w').write('no json'); ok, msg = vd.probe_ok(spec_f, 0); assert ok                                               # ilegible no mata (lo vigila el heartbeat vigia); fresco por mtime
    # el fallo que motivo el cambio: un probe de log INICIO se pierde con >20 lineas, el `fresh:` NO depende de ningun log
    os.makedirs(TMP + '/logs', exist_ok=True); open(TMP + '/logs/x.log', 'w').write('INICIO\n' + 'abre fichero\n' * 25); assert not vd.probe_ok('log:logs/x.log:INICIO', 0)[0]
    # estado(): con un proceso falso con el nombre del runner el veredicto usa el probe (informe) -> comprobado con proceso_de real = None (CAIDO) en este arbol
    vd.BASE = vd.Path(REPO); ver = vd.estado()['cxb60dry']['veredicto']; assert ver == ('CAIDO' if pr is None else ver) and ver in ('CAIDO', 'STALE', 'FRESH')
    print('T1 ok: el parche aplica sobre los ficheros ACTUALES (con el cambio bnreg sin commitear), compila, el comando arranca en un bash seco, CAIDO coherente; nuevo probe fresh: (heartbeat) probado: ausente/fresco/restart/viejo/STOPPED; probe log INICIO sigue perdiendose con >20 lineas')


def test_vigia_heartbeat():
    D = TMP + '/hb'; os.makedirs(D); env = dict(ENV, CXB60_DIR=D); V = H.rstrip('/') + '/../vigia_cxb60_heartbeat.py'
    run = lambda: subprocess.run([sys.executable, '-I', V], capture_output=True, text=True, env=env)
    r = run(); assert r.returncode == 1 and 'sin heartbeat' in r.stdout and 'AVISO (seco' in r.stdout
    proc = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)', 'cxb60_dryrun_fase0.py'])                    # proceso hijo propio con el nombre en su cmdline (se mata abajo por pid)
    try:
        open(D + '/cxb60.pid', 'w').write(str(proc.pid)); hb = lambda **k: json.dump(dict(wall=time.time(), status='RUNNING', lag_s=3.0, **k), open(D + '/heartbeat.json', 'w'))
        hb(); r = run(); assert r.returncode == 0 and 'sano' in r.stdout and not json.load(open(D + '/vigia_latch.json')), r.stdout                  # sano y latch limpio
        json.dump(dict(wall=time.time() - 700, status='RUNNING', lag_s=3.0), open(D + '/heartbeat.json', 'w')); r = run(); assert r.returncode == 1 and 'heartbeat de hace' in r.stdout and 'AVISO' in r.stdout
        r = run(); assert r.returncode == 1 and 'AVISO' not in r.stdout                                                                       # mismo episodio: latch, no re-avisa
        hb(); json.dump(dict(wall=time.time(), status='STOPPED_FAILED', lag_s=1.0), open(D + '/heartbeat.json', 'w')); r = run(); assert r.returncode == 1 and 'status STOPPED_FAILED' in r.stdout
        hb(); r = run(); assert r.returncode == 0
        json.dump(dict(wall=time.time(), status='RUNNING', lag_s=900.0), open(D + '/heartbeat.json', 'w')); r = run(); assert r.returncode == 1 and 'lag del flujo' in r.stdout
        hb(); open(D + '/cxb60.pid', 'w').write('999999'); r = run(); assert r.returncode == 1 and 'pid ausente' in r.stdout
    finally: proc.kill(); proc.wait()
    print('T2 ok: vigia heartbeat: sin hb / hb viejo / STOPPED / lag >600 s / pid ausente -> aviso (seco), sano -> 0, latch evita repetir el mismo episodio y se limpia al recuperar')


def test_cron_resolve_seco():
    O = TMP + '/out'; os.makedirs(O + '/c59'); S = DR + 'cron_resolve_cxb60.sh'; env = dict(ENV, CXB60_OUT=O, CXB60_LOG_RESOLVE=TMP + '/resolve.log')
    r = subprocess.run(['bash', S], capture_output=True, text=True, env=env); assert r.returncode == 0 and 'AVISO' not in r.stdout, (r.stdout, r.stderr)          # sin dias: el informe responde SIN_DATOS y no avisa
    assert 'SIN_DATOS' in open(TMP + '/resolve.log').read()
    ayer = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=1)).strftime('%F'); open(f'{O}/dec_{ayer}.csv.gz', 'wb').write(b'no soy un gzip')
    r = subprocess.run(['bash', S], capture_output=True, text=True, env=env); assert r.returncode == 0, r.stdout                      # un dec_ ilegible se TOLERA (0 filas validas): no es fallo del cron; lo recoge la cobertura (dia no valido en el informe)
    assert json.load(open(f'{O}/informe_cxb60.json'))['dias_usados'] == [] if os.path.exists(f'{O}/informe_cxb60.json') else True
    r = subprocess.run(['bash', S], capture_output=True, text=True, env=dict(env, CXB60_PY='/bin/false')); assert r.returncode == 1 and 'AVISO (seco, sin Telegram): cxb60 resolve FALLO' in r.stdout, (r.returncode, r.stdout)   # si el resolvedor/informe FALLA -> aviso
    assert subprocess.run(['bash', '-n', S]).returncode == 0
    print('T3 ok: cron resolve en seco: sin datos -> exit 0 sin aviso; dec_ ilegible -> tolerado (dia no valido); resolvedor que falla (rc!=0) -> exit 1 con aviso de fallo (sin Telegram real)')


def test_lanzar_probar():
    D = TMP + '/lz'; S = DR + 'lanzar_cxb60_dryrun.sh'; env = dict(ENV, CXB60_DIR=D)
    r = subprocess.run(['bash', S, '--forzar', '--probar'], capture_output=True, text=True, env=env); assert r.returncode == 0 and 'PROBAR: comprobaciones OK' in r.stdout, (r.stdout, r.stderr)
    assert not os.path.exists(D + '/cxb60.pid') and 'cxb60_dryrun_fase0.py' in r.stdout                        # no lanzo nada, no dejo pid
    r = subprocess.run(['bash', S, '--probar'], capture_output=True, text=True, env=env); h = dt.datetime.now(dt.timezone.utc).hour
    assert r.returncode in (0, 2) and (r.returncode == 0 or any(k in r.stdout for k in ('06-09Z', 'MemAvailable', 'load5'))), r.stdout                  # sin --forzar: o pasa o explica por que no
    # el .sh refusa fuera de condiciones: simulo hora 06-09Z con un 'date' falso en el PATH
    fk = TMP + '/fakebin'; os.makedirs(fk); open(fk + '/date', 'w').write('#!/bin/bash\n[ "$1" = "-u" ] && [ "$2" = "+%H" ] && { echo 07; exit 0; }\nexec /usr/bin/date "$@"\n'); os.chmod(fk + '/date', 0o755)
    r = subprocess.run(['bash', S, '--probar'], capture_output=True, text=True, env=dict(env, PATH=fk + ':' + os.environ['PATH'])); assert r.returncode == 2 and '06-09Z' in r.stdout, (r.returncode, r.stdout)
    print('T4 ok: lanzar --probar comprueba hashes/horario/RAM/load y NO lanza ni deja pid; a las 07Z (reloj simulado) rechaza con exit 2')


if __name__ == '__main__':
    try:
        for n, f in list(globals().items()):
            if n.startswith('test_') and callable(f): f()
        print('TODOS OK (C6 en seco)')
    finally: shutil.rmtree(TMP, ignore_errors=True)
