import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
import markouts_desde_registro as M

def rec(t0, tardio=False):
    return {'slug': 'eth-updown-5m-1000', 'lado': 'YES', 'rellenos': [{'oid': 'x', 'acc': 5.0, 'precio': 0.20, 't_deteccion': t0, 'tardio': tardio}]}

def test_basico_y_missing_y_stale():
    xs = [(1000.0, 0.20), (1010.0, 0.30), (1100.0, 0.10)]       # fin = 1300
    f = M.calcular(rec(1003.0), xs)[0]
    assert f['mid_5s'] == 0.20 and abs(f['markout_5s']) < 1e-12        # a 1008: ultimo q = 1000
    assert f['mid_30s'] == 0.30 and abs(f['markout_30s'] - 0.5) < 1e-9  # a 1033: q=1010
    assert f['mid_120s'] == 0.10 and abs(f['markout_120s'] + 0.5) < 1e-9
    assert f['stale_30s'] is False and abs(f['edad_q_30s'] - 23.0) < 1e-9
    g = M.calcular(rec(1250.0), xs)[0]                                  # +120 pasa del cierre -> missing, no 0
    assert g['mid_120s'] is None and g['markout_120s'] is None and g['mid_30s'] is None and g['hueco_30s'] is True and g['mid_ultimo_conocido_30s'] == 0.10 and g['stale_30s'] is True
    assert M.calcular(rec(1003.0, tardio=True), xs)[0]['mid_5s'] is None
    assert M.calcular(rec(1003.0), [])[0]['markout_5s'] is None



def test_fallback_libro5_solo_donde_q_falta():
    xs = [(1000.0, 0.20), (1010.0, 0.30)]                                   # q termina en 1010: a 1033/1123 esta stale (>30 s)
    xs5 = [(1000.0, 0.21), (1020.0, 0.25), (1100.0, 0.40), (1120.0, 0.35)]
    f = M.calcular(rec(1020.0), xs, xs5)[0]
    assert f['fuente_5s'] == 'm5_registro.q' and f['mid_5s'] == 0.30        # a 1025: q=1010 (edad 15): libro5 NO se toca
    assert f['fuente_30s'] == 'libro5_ms' and f['mid_30s'] == 0.25 and abs(f['markout_30s'] + 0.0) < 1e-9 + 1   # a 1050: q edad 40 stale -> libro5 1020 (edad 30)
    assert f['fuente_120s'] == 'libro5_ms' and f['mid_120s'] == 0.35 and f['markout_120s'] > 0   # a 1140
    assert M.necesita_fb(rec(1020.0), xs) and not M.necesita_fb(rec(1003.0), [(1000.0 + 20 * i, .2) for i in range(7)])
    assert M.calcular(rec(1003.0), [], xs5)[0]['fuente_5s'] == 'libro5_ms'  # sin q ninguna: libro5
    assert M.calcular(rec(1020.0), xs, None)[0]['fuente_30s'] == 'm5_registro.q'   # sin fallback: igual que antes


def test_hueco_comun_a_ambas_fuentes_es_missing_no_valor_viejo():
    xs = [(1000.0, 0.20)]; xs5 = [(1000.0, 0.20)]                         # ninguna fuente tiene nada desde 1000: a 1125 edad 125 > 60
    f = M.calcular(rec(1020.0), xs, xs5)[0]
    assert f['mid_5s'] is not None and f['hueco_5s'] is False             # a 1025: edad 25, stale pero no hueco
    assert f['mid_120s'] is None and f['markout_120s'] is None and f['hueco_120s'] is True and f['mid_ultimo_conocido_120s'] == 0.20
    assert f['fuente_120s'] == 'hueco_sin_dato'


def test_libro5_parse_B_d_G():
    L = ['B,1,T,0.20:10;0.19:5,0.22:7,,1000000,1', 'd,1,T,B,0.21,3,,1001000,2', 'd,1,T,A,0.22,0,,1001000,3',
         'G,1,*,caida,,,1002000,4', 'd,1,T,B,0.30,1,,1003000,5', 'B,1,T,0.10:1,0.12:1,,1004000,6', 'B,1,U,0.5:1,0.6:1,,1004000,7']
    o = M._libro5_parse(L, ['T'])['T']
    assert abs(dict(o)[1000.0] - 0.21) < 1e-9 and abs(dict(o)[1004.0] - 0.11) < 1e-9
    assert all(t != 1003.0 for t, _ in o)          # tras G no hay continuidad: la d sin B previo no genera mid
    assert not any(abs(m - 0.5) < 1e-9 for _, m in o)   # token U ajeno ignorado
    assert [t for t, _ in o] == sorted({t for t, _ in o})


def test_lote_idempotente_y_dia_sin_archivar(tmp_path):
    import gzip, json, os
    vol = tmp_path / 'v'; l5 = tmp_path / 'l5'; vol.mkdir(); l5.mkdir()
    ini = 1792654200                                                         # 2026-10-22 07:30
    fin_s = '2026-10-22 07:35:00+00:00'
    def gz(p, filas):
        with gzip.open(p, 'wt') as f: f.write('\n'.join(filas) + '\n')
    q = lambda t, b, a: f'q,{int(t*1000)},TOK1,{b},{a},1,1,{int(t*1000)+20}'
    gz(vol / 'm5_registro_2026-10-22.csv.gz', ['tipo,t_ms,id,c1,c2,c3,c4,c5', f'k,1,TOK1,ETH,5min,9,{fin_s},YES', q(ini + 100, .2, .3), q(ini + 160, .3, .4)])
    gz(l5 / 'libro5_ms_2026-10-22_77.csv.gz', ['tipo,t_ms,token,c1,c2,c3,recepcion,seq', f'B,1,TOK1,0.4:1,0.5:1,,{int((ini+200)*1000)},1'])
    M.VOL, M.L5, M.DL = str(vol), str(l5), str(tmp_path); M.OUT = str(tmp_path / 'out.jsonl')
    r = {'slug': f'eth-updown-5m-{ini}', 'lado': 'YES', 'rellenos': [{'oid': 'a', 'acc': 5.0, 'precio': 0.25, 't_deteccion': ini + 100.5, 'tardio': False}]}
    n1, res1 = M.procesar([r]); assert len(n1) == 1 and res1['escritas'] == 1 and res1['duplicadas_descartadas'] == 0 and res1['fallback_libro5'] == [r['slug']]
    f = n1[0]; assert f['fuente_5s'] == 'm5_registro.q' and f['fuente_120s'] == 'libro5_ms' and abs(f['mid_120s'] - 0.45) < 1e-9
    n2, res2 = M.procesar([r]); assert n2 == [] and res2['ya_hechos'] == 1                     # reinicio: sin duplicar
    assert len(open(M.OUT).read().splitlines()) == 1
    # fila LEGADA stale (sin fuente_*) -> se recalcula con libro5 y se sustituye; las demas lineas quedan; backup creado
    d = json.loads(open(M.OUT).read().splitlines()[0]); leg = {k: v for k, v in d.items() if not k.startswith(('fuente_', 'hueco_', 'mid_ultimo'))}
    leg['stale_30s'] = True; leg['mid_120s'] = 0.30; open(M.OUT, 'w').write(json.dumps(leg) + '\n')
    n4, res4 = M.procesar([r]); assert res4['a_recalcular_stale'] == 1 and res4['escritas'] == 1
    L = open(M.OUT).read().splitlines(); assert len(L) == 1 and 'fuente_120s' in json.loads(L[0]) and abs(json.loads(L[0])['mid_120s'] - 0.45) < 1e-9
    assert os.path.exists(M.OUT + '.bak_prefallback')
    n5, res5 = M.procesar([r]); assert n5 == [] and res5['a_recalcular_stale'] == 0
    # fichero con cola a medias (kill a mitad de escritura): se repara y no se duplica
    open(M.OUT, 'a').write('{"slug": "x"'); assert M.cargar_hechos()[1] == 1
    r2 = dict(r, slug='eth-updown-5m-1792740600', rellenos=[dict(r['rellenos'][0], oid='b', t_deteccion=1792740700.0)])   # dia 23 sin archivar
    n3, res3 = M.procesar([r2]); assert n3 == [] and res3['esperan_archivo_dia'] == 1


if __name__ == '__main__':
    import tempfile, pathlib
    test_basico_y_missing_y_stale(); test_fallback_libro5_solo_donde_q_falta(); test_libro5_parse_B_d_G()
    test_lote_idempotente_y_dia_sin_archivar(pathlib.Path(tempfile.mkdtemp())); print('ok')
