#!/usr/bin/env python3
"""Tests de la capa de DATOS de H23 (22-Oct): lector del registro propio de pares, libro de huecos del registro maker_ms, job largo de replay (validacion, reanudacion idempotente,
guardas, corrupcion) y manifiesto de cobertura. Sin red, sin datos de produccion. Desde este directorio: python3 -m pytest -q test_h23_datos.py"""
import csv, gzip, json, os, sys, time, zlib
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/v4_comprar_lo_bueno/r3')
import numpy as np
import pytest
import simlib
import h23_pares_lector as P
import h23_huecos_ws as H
import h23_job_replay as J

C = 1_800_000_000          # 2027-01-15 08:00:00 UTC (multiplo de 900)
DIA = '2027-01-15'
T5U, T5D, T15U, T15D = 'tu5', 'td5', 'tu15', 'td15'


def gzmiembros(path, bloques):
    with open(path, 'wb') as f:
        for b in bloques:
            f.write(gzip.compress(('\n'.join(b) + '\n').encode()))


def lineas_ejemplo():
    return [f'P,{C},m5,m15,{T5U},{T5D},{T15U},{T15D},BTC,-370000',
            f'c,{C},0,-369000',
            f'q,{C},0,-309000,-10,0.3,0.33,100.0,50.0,s',
            f'q,{C},2,-309000,0,0.4,0.44,80.0,80.0,s',
            f'q,{C},0,-250000,-5,0.31,0.33,70.0,50.0,p',
            f'q,{C},0,-250000,-5,,,,,b',                                  # sin libro: NaN y 0.0 en tamanos
            f't,{C},1,-200000,-7,0.66,SELL,12.5',
            f't,{C},0,-190000,-7,0.30,BUY,3',
            f'g,{C},2,-100000,ConnectionClosedError: x;y',
            f'q,{C},2,-99000,-3,0.4,0.44,80.0,80.0,b']


def test_cargar_asigna_dia_por_cierre_y_lee_dos_ficheros(tmp_path):
    ls = lineas_ejemplo()
    # un par que cruza medianoche: P y casi todo en el fichero del dia anterior, la cola en el del dia siguiente al cierre
    C2 = 1_800_003_600 - 3600 + 900     # cierre posterior
    gzmiembros(tmp_path / f'h23_pares_BTC_{DIA}.csv.gz', [ls[:5], ls[5:]])
    pares = P.cargar('BTC', DIA, str(tmp_path))
    assert list(pares) == [C]
    p = pares[C]
    assert p['mkt5'] == 'm5' and p['toks'] == [T5U, T5D, T15U, T15D] and len(p['q']) == 5 and len(p['t']) == 2
    assert p['huecos'] == [(2, C * 1000 - 100000, 'ConnectionClosedError: x;y')] and p['conex'] == [(0, C * 1000 - 369000)]
    assert P.cargar('BTC', '2027-01-16', str(tmp_path)) == {}                       # otro dia: no lo asigna
    # el dia siguiente al cierre: el cierre a las 08:00 pertenece al dia del vigia (C-1 s) = 2027-01-15
    assert P._dia_de_cierre(C) == DIA


def test_lectura_tolerante_a_miembro_gzip_truncado(tmp_path):
    f = tmp_path / f'h23_pares_BTC_{DIA}.csv.gz'
    gzmiembros(f, [lineas_ejemplo()[:4]])
    with open(f, 'ab') as fh:
        fh.write(gzip.compress(b'q,1800000000,0,-1,0,0.3,0.33,1,1,p\n' * 100)[:-9])     # corte brusco
    pares = P.cargar('BTC', DIA, str(tmp_path))
    assert 2 < len(pares[C]['q']) <= 102 and all(len(x) == 8 for x in pares[C]['q'])                  # lo anterior se lee; el miembro truncado se descarta, sin excepcion


def test_grupos_misma_interfaz_que_simlib_y_mismo_resultado(tmp_path):
    gzmiembros(tmp_path / f'h23_pares_BTC_{DIA}.csv.gz', [lineas_ejemplo()])
    pares = P.cargar('BTC', DIA, str(tmp_path))
    C_, QS, TS = next(P.grupos(pares, simlib))
    assert C_ == C and set(QS) == {T5U, T5D, T15U, T15D}
    q = QS[T5U]
    assert isinstance(q, simlib.Q) and list(q.rx) == [C * 1000 - 309000, C * 1000 - 250000, C * 1000 - 250000]
    assert q.ex[0] == q.rx[0] - 10 and q.bid[0] == 0.3 and q.bsz[0] == 100.0
    assert np.isnan(q.bid[2]) and q.bsz[2] == 0.0                                       # libro vacio: NaN en precios, 0.0 en tamanos (como simlib.grupos)
    t = TS[T5D]
    assert isinstance(t, simlib.T) and list(t.p) == [0.66] and list(t.buy) == [False] and list(t.sz) == [12.5]
    assert TS[T5U].buy[0] == True
    # indices de estado sin look-ahead: ultimo rx <= t
    assert q.i(C * 1000 - 260000) == 0 and q.i(C * 1000 - 250000) == 2 and q.i(C * 1000 - 400000) == -1
    km = P.kmap(pares)
    assert km[('5min', C, 'YES')] == (T5U, 'm5') and km[('15min', C, 'NO')] == (T15D, 'm15')


def test_huecos_en_ventana():
    p = dict(huecos=[(0, C * 1000 - 400000, 'x'), (1, C * 1000 - 100000, 'y'), (2, C * 1000 - 5000, 'z')])
    h = P.huecos_en_ventana(p, C)
    assert [x[2] for x in h] == ['y']            # el de -400 s queda fuera; el de -5 s esta tras C-10 s


# ---------------------------------------------------------------------------------------------------------------------
LOG = """[2026-10-22T10:00:00+00:00] [libro_estado_ws] conectado [BTC#5min], 8 tokens (lector en proceso separado, pid 111)
[2026-10-22T10:00:01+00:00] [libro_estado_ws] conectado [BTC#15min], 8 tokens (lector en proceso separado, pid 111)
[2026-10-22T10:05:00+00:00] [libro_estado_ws] sesión caída [BTC#5min]: ConnectionClosedError: x; reconecta en 2 s
[2026-10-22T10:05:02+00:00] [libro_estado_ws] conectado [BTC#5min], 8 tokens (lector en proceso separado, pid 111)
[2026-10-22T10:30:00+00:00] [libro_estado_ws] conectado [BTC#5min], 8 tokens (lector en proceso separado, pid 222)
[2026-10-22T10:30:01+00:00] [libro_estado_ws] conectado [BTC#15min], 8 tokens (lector en proceso separado, pid 222)
[2026-10-22T10:31:00+00:00] [libro_estado_ws] sesión caída [BTC#15min]: ConnectionClosedError: y; reconecta en 2 s
"""


def test_libro_de_huecos(tmp_path):
    log = tmp_path / 'obs.log'
    log.write_text(LOG)
    dl = tmp_path / 'dl'
    dl.mkdir()
    f = dl / 'maker_ms_2026-10-22_111.csv.gz'
    f.write_bytes(gzip.compress(b'x'))
    t_fin = H._t('2026-10-22T10:29:00+00:00')
    os.utime(f, (t_fin, t_fin))
    h = H.construir(str(log), str(dl))
    cai = [x for x in h['BTC#5min'] if x['tipo'] == 'caida']
    assert len(cai) == 1 and cai[0]['a'] == H._t('2026-10-22T10:05:00+00:00') - 1 and cai[0]['b'] == H._t('2026-10-22T10:05:02+00:00') + 1
    rei = [x for x in h['BTC#5min'] if x['tipo'] == 'reinicio']
    assert len(rei) == 1 and rei[0]['a'] == t_fin and rei[0]['b'] == H._t('2026-10-22T10:30:00+00:00') + 5 and rei[0]['fin_estimado'] is False
    assert [x['tipo'] for x in h['BTC#15min']] == ['reinicio']                          # la ultima caida no tiene `conectado` posterior: no se inventa su fin
    # clasificacion de un cierre cuya ventana toca el reinicio
    led = {g: v for g, v in h.items()}
    C_in = int(H._t('2026-10-22T10:30:00+00:00')) + 100                                  # la ventana [C-305, C-10] contiene 10:29:00-10:30:05
    assert H.estado_cierre(led, 'BTC', C_in)[0] == 'reinicio'
    assert H.estado_cierre(led, 'ETH', C_in)[0] == 'limpio'
    assert H.estado_cierre(led, 'BTC', C_in + 3600)[0] == 'limpio'


def test_guardar_ledger_idempotente_y_corrupcion(tmp_path):
    h = {'BTC#5min': [dict(a=1000.0, b=1002.0, tipo='caida')]}
    f, n = H.guardar(h, str(tmp_path))
    f2, n2 = H.guardar(h, str(tmp_path))
    assert n == n2 == 1                                                                # re-guardar no duplica
    open(f, 'w').write('{corrupto')
    f3, n3 = H.guardar(h, str(tmp_path))
    assert n3 == 1 and any('.invalido_' in x for x in os.listdir(tmp_path))            # el corrupto se aparta, no se borra


# ---------------------------------------------------------------------------------------------------------------------
def _csv_valido(path, n=3, dup=False, cab=None):
    cols = cab or J.COLS
    with open(path, 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for i in range(n):
            r = {c: '0' for c in cols}
            r.update(coin='ETH', dia='2026-10-10', cierre=str(100 + (0 if dup else i)), brazo='A', sizing='real', modo='primer', rep='150', cola='base', lat_post='79', lat_cancel='60')
            w.writerow(r)


def _job(tmp_path, monkeypatch, args=None):
    out = str(tmp_path / 'out') + '/'
    os.makedirs(out)
    monkeypatch.setitem(J.OUT, 'registro', out)
    monkeypatch.setattr(J, 'JOBS', str(tmp_path / 'jobs') + '/')
    a = J.argparse.Namespace(job='t', fuente='registro', monedas='ETH', dias='2026-10-10,2026-10-11', dir=None, espera_min=0.0, timeout_min=1.0, respeta_otros=False)
    return J.Job(a), out


def test_validar_salida(tmp_path, monkeypatch):
    j, out = _job(tmp_path, monkeypatch)
    f, fc = out + 'v3_ETH_2026-10-10.csv', out + 'v3_cobertura_ETH_2026-10-10.json'
    assert j.validar('ETH', '2026-10-10')[0] is False                                  # falta todo
    _csv_valido(f)
    json.dump(dict(coin='ETH', dia='2026-10-10', errores=0, cierres_grupo=97, con_lado=80, con_libro=80, sin_desenlace=0), open(fc, 'w'))
    ok, d = j.validar('ETH', '2026-10-10')
    assert ok and d['filas'] == 3 and d['con_libro'] == 80
    _csv_valido(f, dup=True)
    assert j.validar('ETH', '2026-10-10') == (False, "clave duplicada ('100', 'A', 'real', 'primer', '150', 'base', '79', '60')")
    _csv_valido(f, cab=J.COLS[:-1])
    assert j.validar('ETH', '2026-10-10')[1] == 'cabecera distinta'
    _csv_valido(f)
    json.dump(dict(coin='ETH', dia='2026-10-10', errores=2), open(fc, 'w'))
    assert j.validar('ETH', '2026-10-10')[1] == 'errores=2'
    json.dump(dict(coin='SOL', dia='2026-10-10', errores=0), open(fc, 'w'))
    assert j.validar('ETH', '2026-10-10')[1] == 'cobertura de otra unidad'


def test_reanudacion_idempotente_corrupcion_y_guardas(tmp_path, monkeypatch):
    j, out = _job(tmp_path, monkeypatch)
    llamadas = []

    def falso_run(cmd, **kw):
        coin, D = cmd[-2], cmd[-1]
        llamadas.append((coin, D))
        _csv_valido(out + f'v3_{coin}_{D}.csv', n=4)
        json.dump(dict(coin=coin, dia=D, errores=0, cierres_grupo=97, con_lado=80, con_libro=80, sin_desenlace=0, cotizados_A=1, cotizados_B=1), open(out + f'v3_cobertura_{coin}_{D}.json', 'w'))
        return type('R', (), {'returncode': 0})()
    monkeypatch.setattr(J.subprocess, 'run', falso_run)
    monkeypatch.setattr(J.Job, 'guardas', lambda self: (True, ''))
    # el CSV de la unidad ya viene con coin ETH/dia fijos en el fake: ajustamos dia al validar
    assert j.correr() == 0 and len(llamadas) == 2
    m = json.load(open(j.mf))
    assert m['estado'] == 'COMPLETE' and set(m['unidades']) == {'ETH|2026-10-10', 'ETH|2026-10-11'} and m['codigo'] and m['regla_hash_config'] == '3eeff503cf0a75c9'
    assert os.path.exists(os.path.join(j.dir, 'informe_final.txt')) and os.path.exists(os.path.join(j.dir, 'resumen_parcial.json'))
    # reanudar: nada que recalcular (sin duplicar filas ni PnL)
    antes = open(out + 'v3_ETH_2026-10-10.csv').read()
    j2 = J.Job(j.a)
    assert j2.correr() == 0 and len(llamadas) == 2 and open(out + 'v3_ETH_2026-10-10.csv').read() == antes
    # corromper una salida: se aparta y se recalcula solo esa unidad
    open(out + 'v3_ETH_2026-10-11.csv', 'a').write('basura,sin,sentido\n')
    j3 = J.Job(j.a)
    assert j3.correr() == 0 and llamadas[2:] == [('ETH', '2026-10-11')]
    assert any('.invalido_' in x for x in os.listdir(out))
    # guardas cerradas: BLOCKED y nada se calcula
    os.remove(out + 'v3_ETH_2026-10-10.csv')
    monkeypatch.setattr(J.Job, 'guardas', lambda self: (False, 'franja'))
    j4 = J.Job(j.a)
    assert j4.correr() == 2 and json.load(open(j4.mf))['estado'] == 'BLOCKED' and len(llamadas) == 3


def test_rangos():
    assert J.rangos('2026-10-06:2026-10-08') == ['2026-10-06', '2026-10-07', '2026-10-08'] and J.rangos('a,b') == ['a', 'b']
