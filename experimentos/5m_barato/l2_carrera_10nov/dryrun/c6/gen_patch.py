#!/usr/bin/env python3
"""Regenera watchdog_verify_cxb60.patch contra los pipeline_watchdog.py / verify_deploy.py ACTUALES del repo (no los modifica; trabaja en un tmp). python3 -I gen_patch.py"""
import os, shutil, subprocess, tempfile
R = '/root/polymarket-research/'; HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; W = tempfile.mkdtemp(prefix='c6_gen_')
for k in 'ab': os.makedirs(W + k)
for f in ('pipeline_watchdog.py', 'verify_deploy.py'):
    for k in 'ab': shutil.copy(R + f, f'{W}{k}/{f}')
p = open(W + 'b/pipeline_watchdog.py').read(); ancla = '    "dash-weather": f"cd {REPO_WEATHER} && nice -n 10 .venv/bin/python dashboard_server.py >> logs/dashboard-weather.log 2>&1",\n'; assert ancla in p
nuevo = '''    # cxb60dry (12-Nov, C6; INSTALAR SOLO tras congelar PREREG_CXB60_FORWARD): dry-run multivariante B-CXB60, SOLO simula (0 ordenes, sin claves ni red de envio), lee los maker_ms_*.csv.gz del volumen. Sin choom (sin dinero).
    # Sin imports de la cadena de observadores_fase0 (no reinicia nada). Los ficheros ejecutados estan hasheados en dryrun/HASHES_CONGELADOS.json: el proceso aborta (exit 3) si difieren. ulimit -v holgado; el tope real es el RSS (--max-rss-mb 3000, exit 4).
    "cxb60dry": f"cd {REPO} && nice -n 15 ionice -c3 bash -c 'ulimit -v 7000000; exec .venv/bin/python -I experimentos/5m_barato/l2_carrera_10nov/dryrun/cxb60_dryrun_fase0.py' >> logs/cxb60_dryrun.log 2>&1",
'''
p = p.replace(ancla, nuevo + ancla, 1); a = '"r3shadow", "logl2", "bnreg"]}'; assert a in p; p = p.replace(a, '"r3shadow", "logl2", "bnreg", "cxb60dry"]}', 1); open(W + 'b/pipeline_watchdog.py', 'w').write(p)
v = open(W + 'b/verify_deploy.py').read()
rama = '''    if spec.startswith("fresh:"):
        # fresh:<ruta>:<max_edad_s> -- el fichero (p. ej. heartbeat.json que el proceso reescribe cada 30 s) se ha escrito en los ultimos N s, despues del restart,
        # y si es JSON con "status" no empieza por STOPPED. No depende del tail de ningun log (el probe `log:` pierde un INICIO unico tras 20 lineas).
        _, ruta, edad = spec.rsplit(":", 2)
        f = BASE / ruta
        if not f.exists():
            return False, f"{ruta} no existe"
        m = f.stat().st_mtime
        if m < desde_epoch:
            return False, f"{ruta} sin escrituras desde el restart"
        if time.time() - m > float(edad):
            return False, f"{ruta} parado hace {time.time() - m:.0f}s (> {edad}s)"
        try:
            st = str(json.loads(f.read_text(encoding="utf-8")).get("status", ""))
        except (ValueError, OSError):
            st = ""
        if st.startswith("STOPPED"):
            return False, f"{ruta} status {st}"
        return True, f"{ruta} fresco ({time.time() - m:.0f}s)"
'''
ancla2 = '    return False, f"probe desconocido: {spec}"'; assert ancla2 in v; v = v.replace(ancla2, rama + ancla2, 1)
assert '\nimport os\n' in v and '\nimport json\n' not in v; v = v.replace('\nimport os\n', '\nimport json\nimport os\n', 1)
a3 = '    # 21-Oct: dashboard 5m barato SOLO LECTURA, puerto 8892'; assert a3 in v
ent = '''    # 12-Nov (C6, INSTALAR SOLO tras congelar el PREREG_CXB60_FORWARD): dry-run B-CXB60 (0 ordenes; ver pipeline_watchdog.py::SCREEN_RESTART). "entry" = el runner congelado; sus modulos hermanos (cxb60_core, frozen/) NO estan en la raiz del repo,
    # asi que cierre_imports solo ve el propio .py: la integridad del resto la garantiza HASHES_CONGELADOS.json en el arranque. Probe `fresh:` sobre el heartbeat (se reescribe cada 30 s): un probe `log:...:INICIO` se pierde del tail de 20 lineas tras varios reinicios.
    "cxb60dry": {"entry": "experimentos/5m_barato/l2_carrera_10nov/dryrun/cxb60_dryrun_fase0.py", "probe": "fresh:/root/polymarket-research-datalogs/cxb60_dryrun/heartbeat.json:180"},
'''
v = v.replace(a3, ent + a3, 1); open(W + 'b/verify_deploy.py', 'w').write(v)
d = ''.join(subprocess.run(['diff', '-u', '--label', f'a/{f}', '--label', f'b/{f}', f'{W}a/{f}', f'{W}b/{f}'], capture_output=True, text=True).stdout for f in ('pipeline_watchdog.py', 'verify_deploy.py'))
open(HERE + 'watchdog_verify_cxb60.patch', 'w').write(d); shutil.rmtree(W); print(len(d.splitlines()), 'lineas de parche')
