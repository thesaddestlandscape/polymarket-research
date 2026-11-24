"""test_huecos_real.py -- huecos_real con un maker_ms sintetico (sin datos reales): segundos por moneda desde filas k/q/t y dec_ con filas mkt."""
import os, sys, gzip, json, csv, io
import numpy as np, pytest
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import huecos_real as HR

def test_segundos_y_main_sintetico(tmp_path, monkeypatch):
    d = '2026-11-16'; import calendar, time; d0 = calendar.timegm(time.strptime(d, '%Y-%m-%d')); fin = d0 + 3600; tok = '111'
    L = [f'k,{d0*1000},{tok},ETH,5min,777,2026-11-16 01:00:00+00:00,YES']
    for s in range(fin - 332, fin + 1):
        if not (fin - 200 <= s < fin - 190): L.append(f'q,{s*1000},{tok},0.5,0.6,10,10,{s*1000 + 40}')              # hueco real de 10 s
    L.append(f't,{(fin-100)*1000},{tok},0.5,BUY,1.0,{(fin-100)*1000+20},')
    with gzip.open(tmp_path / f'maker_ms_{d}_1.csv.gz', 'wt') as f: f.write('tipo,t_ms,id,c1,c2,c3,c4,c5\n' + '\n'.join(L) + '\n')
    (tmp_path / 'cxb60_dryrun').mkdir(); det = json.dumps(dict(hueco_feed=True, vac_max_s=55)); row = ['mkt', 'run', d, tok, '777', 'ETH', 'YES', str(fin)] + [''] * 13 + [det, '']
    buf = io.StringIO(); csv.writer(buf).writerow(row)
    with gzip.open(tmp_path / 'cxb60_dryrun' / f'dec_{d}.csv.gz', 'wt') as f: f.write('tipo,run_id,dia\n' + buf.getvalue())
    monkeypatch.setattr(HR, 'DL', str(tmp_path) + '/'); monkeypatch.setattr(HR, 'DEC', str(tmp_path) + '/cxb60_dryrun/'); monkeypatch.setattr(HR, 'OUT', str(tmp_path) + '/out/'); monkeypatch.setattr(HR, 'CRUDO', str(tmp_path) + '/nocrudo/')
    r = HR.main(d); assert r['estado'] == 'OK' and r['n_mercados'] == 1 and r['vac_max_nuevo']['p50'] == 10 and r['vac_max_runner']['p50'] == 55 and r['frac_hueco_ge5_nuevo'] == 1.0 and r['aceptacion_p50_menor_10s'] is False
    j = json.load(open(tmp_path / 'out' / f'huecos_mercados_{d}.json')); assert j['n'] == 1 and j['n_excluir'] == 1 and j['mercados'][0]['vac_max_s'] == 10 and j['mercados'][0]['excluir'] is True and j['pre_s'] == 332      # adaptador de la reeval

def test_se_niega_en_dia_ciego():
    with pytest.raises(SystemExit): HR.main('2026-11-18')

def test_ficheros_dia_ignora_stubs_y_cae_al_crudo(tmp_path):
    import gzip as gz; dl = tmp_path / 'dl'; cr = tmp_path / 'cr'; dl.mkdir(); cr.mkdir(); d = '2026-11-16'
    with gz.open(dl / f'maker_ms_{d}_1.csv.gz', 'wt') as f: f.write('tipo,t_ms,id,c1,c2,c3,c4,c5\n')           # stub de cabecera (como los de datalogs 13-17 Nov)
    with gz.open(cr / f'maker_ms_{d}_1.csv.gz', 'wt') as f: f.write('tipo,t_ms,id,c1,c2,c3,c4,c5\n' + ''.join(f'q,{i*7919},{i*104729},3,4,5,6,{i*15485863}\n' for i in range(400)))
    with gz.open(cr / f'maker_ms_{d}_2.csv.gz', 'wt') as f: f.write('x\n')
    fs = HR.ficheros_dia(d, dl=str(dl) + '/', crudo=str(cr) + '/'); assert [os.path.basename(f) for f in fs] == [f'maker_ms_{d}_1.csv.gz'] and fs[0].startswith(str(cr))
    assert HR.ficheros_dia('2099-01-01', dl=str(dl) + '/', crudo=str(cr) + '/') == []

def test_reloj_de_recepcion_no_el_de_exchange(tmp_path, monkeypatch):
    """una fila q con t_ms de exchange DENTRO del hueco pero recepcion fuera NO tapa el hueco; una t sin recv (campo vacio) no cuenta."""
    import gzip as gz, calendar, time; d = '2026-11-16'; d0 = calendar.timegm(time.strptime(d, '%Y-%m-%d')); fin = d0 + 3600; tok = '9'; L = [f'k,{d0*1000},{tok},SOL,5min,1,x,YES']
    for s in range(fin - 332, fin + 1):
        if not (fin - 100 <= s < fin - 80): L.append(f'q,{s*1000},{tok},0.5,0.6,1,1,{s*1000+10}')
    L += [f'q,{(fin-90)*1000},{tok},0.5,0.6,1,1,{(fin-60)*1000 + 7_000_000}', f't,{(fin-90)*1000},{tok},0.5,BUY,1,,']              # rx fuera de la ventana (no tapa), t sin recv
    with gz.open(tmp_path / f'maker_ms_{d}_1.csv.gz', 'wt') as f: f.write('tipo,t_ms,id,c1,c2,c3,c4,c5\n' + '\n'.join(L) * 1 + '\n' + '\n'.join(['q,1,2,3,4,5,6,7'] * 100) + '\n')
    monkeypatch.setattr(HR, 'DL', str(tmp_path) + '/'); monkeypatch.setattr(HR, 'CRUDO', str(tmp_path) + '/nocrudo/'); (A, d0_), n = HR.segundos_por_moneda(d)
    from huecos_cxb60 import vac_max_seg; secs = set((np.nonzero(A['sol'])[0] + (d0_ - 7200)).tolist()); assert vac_max_seg(secs, fin) == 20
