#!/usr/bin/env python3
"""Tests del juez forward Calma v3 (chequeo_libro5tx.py + juez_calma_v3_dia.py). python3 -I test_juez_calma_v3.py  (sintetico en tmp; sin subprocesos pesados; no toca datalogs ni dev)
J1 chequeo: cobertura continua = ok; hueco > 1 min detectado (incluidos bordes 00:00 y 24:00); eventos fuera del dia no cuentan; solapes entre ficheros no duplican; gz truncado = error; sin ficheros = no ok; .csv sin comprimir se ignora y se anota.
J2 parse_tabla sobre una salida real de ana_dec_v3_b.
J3 juez: forward original sin terminar -> BLOCKED rc 4 (no calcula); gz corrupto -> BLOCKED rc 5 (--forzar continua); salidas v3 ausentes -> FAILED; todo presente -> COMPLETE con sello_print=v3 y cobertura; dia previo sin v3 -> PARTIAL (faltan);
    huecos > 1 min NO bloquean pero quedan registrados; reintento idempotente (mismo estado, los pkl no cambian de bytes ni mtime)."""
import os, sys, json, gzip, shutil, tempfile
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import chequeo_libro5tx as CK, juez_calma_v3_dia as J
TMP = tempfile.mkdtemp(prefix='t_juez_'); D = '2026-11-12'; D0 = int(pd.Timestamp(D, tz='UTC').timestamp()) * 1000; DIA = 86400000


def gz(path, ts):
    with gzip.open(path, 'wt') as f:
        for t in ts: f.write(f'{int(t)},tok,0xtx,{int(t) + 20}\n')


def test_chequeo():
    d = TMP + '/l5a/'; os.makedirs(d); gz(d + 'libro5_tx_2026-11-12_1.csv.gz', np.arange(D0, D0 + DIA, 30000))
    r = CK.chequeo(D, d); assert r['ok'] and r['gap_max_ms'] == 30000 and r['n_huecos'] == 0 and r['eventos_en_dia'] == 2880, r
    d = TMP + '/l5b/'; os.makedirs(d); ts = np.concatenate([np.arange(D0 + 10000, D0 + 3600000, 30000), np.arange(D0 + 3600000 + 90000, D0 + DIA - 130000, 30000)])
    gz(d + 'libro5_tx_2026-11-12_1.csv.gz', ts); gz(d + 'libro5_tx_2026-11-11_9.csv.gz', np.arange(D0 - 100000, D0 + 15000, 5000))   # solapa en el borde: cubre 00:00-00:10
    open(d + 'libro5_tx_2026-11-13_9.csv', 'w').write('x\n')
    r = CK.chequeo(D, d); assert not r['ok'] and r['n_huecos'] == 2 and r['gap_max_ms'] >= 90000 and r['ficheros_sin_comprimir_ignorados'] == ['libro5_tx_2026-11-13_9.csv'], r       # hueco de 90 s + borde final 24:00
    assert r['huecos'][0]['desde_utc'].startswith('2026-11-12T00:59'), r['huecos']
    d = TMP + '/l5c/'; os.makedirs(d); gz(d + 'libro5_tx_2026-11-12_1.csv.gz', np.arange(D0, D0 + DIA, 30000)); raw = open(d + 'libro5_tx_2026-11-12_1.csv.gz', 'rb').read()
    open(d + 'libro5_tx_2026-11-12_2.csv.gz', 'wb').write(raw[:len(raw) // 2])                                                                                                 # truncado
    r = CK.chequeo(D, d); assert not r['ok'] and 'libro5_tx_2026-11-12_2.csv.gz' in r['ficheros_con_error'] and r['motivo'] == 'gz con error', r
    d = TMP + '/l5d/'; os.makedirs(d); r = CK.chequeo(D, d); assert not r['ok'] and r['eventos_en_dia'] == 0


def test_parse():
    txt = '''dias [..]\n===== sello VIEJO (dec2)\nx\n     variante  rellenos  EUR     EV  dEUR_vs_G0      IC90_dias    IC90_cierre  sin2mejores dias+  frac_barrido  EV_barrido  EV_resto
      T1_c300      2262 1669 -0.087       314.9 (169.6, 449.7) (195.8, 422.4)        193.3 10/11         0.066       0.490    -0.127
           G0      3260 2424 -0.190         0.0     (0.0, 0.0)     (0.0, 0.0)          0.0  0/11         0.056      -0.102    -0.195

===== sello V3 (dec2v3)
x
     variante  rellenos  EUR     EV  dEUR_vs_G0      IC90_dias    IC90_cierre
          T1       1838 1349 -0.073       351.5 (129.4, 555.5) (193.5, 507.0)        191.5  9/11         0.077       0.432    -0.114
           G0      3245 2413 -0.186         0.0     (0.0, 0.0)     (0.0, 0.0)          0.0  0/11         0.051      -0.162    -0.188
'''
    v = J.parse_tabla(txt, 'V3'); assert v == {'T1': dict(rellenos=1838, EUR=1349.0, EV=-0.073, dEUR_vs_G0=351.5), 'G0': dict(rellenos=3245, EUR=2413.0, EV=-0.186, dEUR_vs_G0=0.0)}, v
    o = J.parse_tabla(txt, 'VIEJO'); assert o['T1_c300']['dEUR_vs_G0'] == 314.9 and 'T1' not in o and J.parse_tabla(txt, 'NADA') == {}


def montar(n, con_dev=True, con_v3=True, previos=True):
    b = f'{TMP}/{n}/'; dev = b + 'dev/'; out = b + 'out/'; l5 = b + 'l5/'; [os.makedirs(x) for x in (dev, out, l5)]; gz(l5 + 'libro5_tx_2026-11-12_1.csv.gz', np.arange(D0, D0 + DIA, 30000))
    for d in (['2026-11-02', '2026-11-03', D] if previos else [D]):
        if con_dev:
            for t in ('dec2', 'dec3s100'): open(dev + f'{t}_{d}.pkl', 'wb').write(b'x')
        if con_v3 and (d == D or previos):
            for t in ('dec2v3', 'dec3v3s100'): open(out + f'{t}_{d}.pkl', 'wb').write(b'v3')
    return ['--out', out, '--dev-out', dev, '--libro5', l5, '--sin-subprocesos'], out, dev, l5


def test_juez():
    a, out, dev, l5 = montar('j1', con_dev=False); assert J.main([D] + a) == 4 and json.load(open(out + f'manifest_juez_v3_{D}.json'))['estado'] == 'BLOCKED'                      # forward original sin terminar
    a, out, dev, l5 = montar('j2'); open(l5 + 'libro5_tx_2026-11-12_2.csv.gz', 'wb').write(b'no es gz'); assert J.main([D] + a) == 5
    m = json.load(open(out + f'manifest_juez_v3_{D}.json')); assert m['estado'] == 'BLOCKED' and m['sello_print'] == 'v3' and m['libro5tx']['ficheros_con_error']
    assert J.main([D] + a + ['--forzar']) in (0, 1) and json.load(open(out + f'manifest_juez_v3_{D}.json'))['estado'] in ('COMPLETE', 'PARTIAL')                                    # --forzar sigue
    a, out, dev, l5 = montar('j3', con_v3=False); assert J.main([D] + a) == 1 and json.load(open(out + f'manifest_juez_v3_{D}.json'))['estado'] == 'FAILED'                          # sin salidas v3 (y sin run_dias real)
    a, out, dev, l5 = montar('j4'); rc = J.main([D] + a); m = json.load(open(out + f'manifest_juez_v3_{D}.json'))
    assert rc == 0 and m['estado'] == 'COMPLETE' and m['sello_print'] == 'v3' and m['cobertura_dias']['procesados'] == 3 and m['cobertura_dias']['esperados'] == 11 or m['estado'] == 'PARTIAL', m   # desde 02-Nov..12-Nov = 11 dias; solo 3 existen
    assert m['estado'] == 'PARTIAL' and len(m['cobertura_dias']['faltan']) == 8, m['cobertura_dias']
    rc = J.main([D, '--desde', '2026-11-12'] + a); m = json.load(open(out + f'manifest_juez_v3_{D}.json')); assert rc == 0 and m['estado'] == 'COMPLETE' and m['cobertura_dias'] == dict(esperados=1, procesados=1, faltan=[], nota=m['cobertura_dias']['nota']), m
    gaps = TMP + '/l5_gaps/'; os.makedirs(gaps); gz(gaps + 'libro5_tx_2026-11-12_1.csv.gz', np.concatenate([np.arange(D0, D0 + 3600000, 30000), np.arange(D0 + 3600000 + 300000, D0 + DIA, 30000)]))
    a2 = a[:]; a2[a2.index('--libro5') + 1] = gaps; rc = J.main([D, '--desde', '2026-11-12'] + a2); m = json.load(open(out + f'manifest_juez_v3_{D}.json'))
    assert rc == 0 and m['estado'] == 'COMPLETE' and m['libro5tx']['ok_cobertura_24h'] is False and m['libro5tx']['n_huecos'] >= 1, m['libro5tx']                                   # huecos registrados, no bloquean
    st = {f: (os.path.getsize(out + f), os.stat(out + f).st_mtime_ns) for f in os.listdir(out) if f.endswith('.pkl')}; rc = J.main([D, '--desde', '2026-11-12'] + a)
    assert rc == 0 and st == {f: (os.path.getsize(out + f), os.stat(out + f).st_mtime_ns) for f in os.listdir(out) if f.endswith('.pkl')}                                              # idempotente: no recalcula


def test_reintentos():
    a, out, dev, l5 = montar('j5', con_v3=False); a = [x for x in a if x != '--sin-subprocesos']; fake = TMP + '/j5/fake_run_dias.sh'; cnt = TMP + '/j5/cnt'
    open(fake, 'w').write(f'#!/bin/bash\nn=$(cat {cnt} 2>/dev/null || echo 0); n=$((n+1)); echo $n > {cnt}\n[ "$n" -ge 2 ] && {{ echo v3 > {out}dec2v3_{D}.pkl; echo v3 > {out}dec3v3s100_{D}.pkl; }}\nexit 0\n')
    ana = TMP + '/j5/fake_ana.py'; open(ana, 'w').write("print('===== sello VIEJO (dec2)\\n     variante  rellenos  EUR     EV  dEUR_vs_G0\\n           G0      10 5 -0.1 0.0\\n===== sello V3 (dec2v3)\\n     variante  rellenos  EUR     EV  dEUR_vs_G0\\n          T1       8 4 -0.05 1.5\\n           G0      10 5 -0.1 0.0')")
    rc = J.main([D, '--desde', D, '--run-dias', fake, '--ana', ana] + a); m = json.load(open(out + f'manifest_juez_v3_{D}.json'))
    assert rc == 0 and m['run_dias_intentos'] == 2 and m['estado'] == 'COMPLETE' and m['tabla_dec2v3']['T1']['dEUR_vs_G0'] == 1.5 and 'sello_print=v3' in open(m['resumen']).read(), m           # J4 reintenta hasta que aparecen los pkl
    a3, out3, dev3, l53 = montar('j6', con_v3=False); a3 = [x for x in a3 if x != '--sin-subprocesos']; nada = TMP + '/j6/nada.sh'; open(nada, 'w').write('#!/bin/bash\nexit 0\n')
    assert J.main([D, '--run-dias', nada, '--reintentos', '2'] + a3) == 1 and json.load(open(out3 + f'manifest_juez_v3_{D}.json'))['run_dias_intentos'] == 2                              # agota reintentos -> FAILED


if __name__ == '__main__':
    try: test_chequeo(); test_parse(); test_juez(); test_reintentos(); print('TODOS OK (juez calma v3)')
    finally: shutil.rmtree(TMP, ignore_errors=True)
