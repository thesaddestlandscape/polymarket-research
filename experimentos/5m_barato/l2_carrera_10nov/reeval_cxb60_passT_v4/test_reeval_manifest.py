import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import reeval_manifest as RM

def test_clases_y_estados_sin_leer_contenido(tmp_path):
    for d in ('2026-11-16', '2026-11-18', '2026-11-20'):
        for n in (f'dec_{d}.csv.gz', f'res_{d}.csv.gz'): (tmp_path / n).write_bytes(b'NO_LEER_EV')
        json.dump(dict(dia=d, cobertura=0.99, dia_valido=True, pnl_secreto=123.0, ev=9.9), open(tmp_path / f'coverage_{d}.json', 'w'))
    a = RM.manifest_dia('2026-11-16', str(tmp_path) + '/'); b = RM.manifest_dia('2026-11-18', str(tmp_path) + '/'); c = RM.manifest_dia('2026-11-20', str(tmp_path) + '/')
    assert (a['clase'], a['estado']) == ('EXPLORATORIO', 'PENDIENTE_REPROCESO') and (b['clase'], b['estado']) == ('CONFIRMATORIO', 'PENDIENTE_REPROCESO') and (c['clase'], c['estado']) == ('CONFIRMATORIO', 'INCOMPLETE')
    assert 'pnl_secreto' not in json.dumps(b) and 'ev' not in b['cobertura'] and b['cobertura']['cobertura'] == 0.99                          # solo claves de cobertura; nunca EV
    assert RM.manifest_dia('2026-11-17', str(tmp_path) + '/')['estado'] == 'PENDING' and RM.manifest_dia('2026-11-10')['estado'] == 'FUERA_DE_RANGO'

def test_escribe_atomico(tmp_path):
    m = RM.escribe('2026-11-12', str(tmp_path) + '/', str(tmp_path) + '/out/'); assert os.path.exists(tmp_path / 'out' / 'manifest_reeval_2026-11-12.json') and m['estado'] == 'FUERA_DE_RANGO'
