"""test_run_scripts.py -- run_rf5.sh / run_k6.sh (v3): si se agota la espera de RAM el dia se ABORTA (no se ejecuta igualmente), rc=1 y marcador abortado_<dia>.json. Copia del script en un directorio temporal con rf5_run.py/prep_tapes_rf5.sh de mentira y `sleep` nulo: no toca datos ni lanza nada pesado."""
import os, subprocess, shutil, stat, json
import pytest

HV = os.path.dirname(os.path.abspath(__file__)) + '/'

def _prepara(tmp, script):
    d = tmp / 'hv'; d.mkdir(); b = tmp / 'bin'; b.mkdir(); out = tmp / 'out'; out.mkdir()
    shutil.copy(HV + script, d / script); (d / 'prep_tapes_rf5.sh').write_text('#!/bin/bash\nexit 0\n'); (d / 'rf5_run.py').write_text("import sys; open(sys.argv[0].replace('rf5_run.py','EJECUTADO_'+sys.argv[-1]), 'w').write('x')\n")
    (d / 'rf5_k6_dia.py').write_text("import sys; open(sys.argv[0].replace('rf5_k6_dia.py','EJECUTADO_K6_'+sys.argv[-1]), 'w').write('x')\n"); (d / 'c4_btc.py').write_text('pass\n')
    for n in ('prep_tapes_rf5.sh', script): os.chmod(d / n, 0o755)
    (b / 'sleep').write_text('#!/bin/bash\nexit 0\n'); os.chmod(b / 'sleep', 0o755)
    return d, b, out

def _corre(tmp_path, script, ram_min):
    d, b, out = _prepara(tmp_path, script)
    if script == 'run_k6.sh': (out / 'manifest_rf5dia_2026-11-18.json').write_text(json.dumps(dict(status='COMPLETE', dia='2026-11-18')))
    env = dict(os.environ, PATH=str(b) + ':' + os.environ['PATH'], RF5_OUT=str(out) + '/', RF5_ESPERA='2', RF5_RAM_MIN=str(ram_min))
    r = subprocess.run(['bash', str(d / script)], env=env, capture_output=True, text=True, timeout=120); log = ''.join(open(str(out / f)).read() for f in os.listdir(out) if f.startswith('run') and f.endswith('.log'))
    return r.returncode, log, d, out

def test_run_rf5_aborta_el_dia_si_se_agota_la_espera_de_ram(tmp_path):
    rc, log, d, out = _corre(tmp_path, 'run_rf5.sh', 10 ** 9)
    # (la ventana horaria prohibida tambien aborta; ambos casos dan rc=1 y ningun EJECUTADO)
    assert rc == 1 and 'ABORTADO dia 2026-11-18' in log and not [f for f in os.listdir(d) if f.startswith('EJECUTADO')] and os.path.exists(out / 'abortado_2026-11-18.json')

def test_run_rf5_ejecuta_si_hay_ram_y_ventana(tmp_path):
    import time
    h = int(time.strftime('%H%M', time.gmtime()))
    if (600 <= h < 915) or (2215 <= h < 2230): return          # dentro de una ventana prohibida el script (correctamente) aborta
    try: rc, log, d, out = _corre(tmp_path, 'run_rf5.sh', 1)
    except subprocess.TimeoutExpired: pytest.skip('cola global de pesados (scripts/cron_pesado.sh, flock) ocupada: el camino feliz usa el cron_pesado real; repetir con la cola libre')
    assert rc == 0 and os.path.exists(d / 'EJECUTADO_2026-11-18') and 'ABORTADO' not in log

def test_run_k6_aborta_el_dia_si_se_agota_la_espera_de_ram(tmp_path):
    rc, log, d, out = _corre(tmp_path, 'run_k6.sh', 10 ** 9)
    assert rc == 1 and 'ABORTADO dia 2026-11-18' in log and not [f for f in os.listdir(d) if f.startswith('EJECUTADO')]
