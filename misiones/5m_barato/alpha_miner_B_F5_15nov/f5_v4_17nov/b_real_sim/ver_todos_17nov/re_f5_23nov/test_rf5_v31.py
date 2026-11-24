"""test_rf5_v31.py -- v3.1 (validador 24-Nov): sello/K_max de las replicas, K6 sobre dias_k6, Bretz persistente, A no bloquea, C1 (eventos desplazados)."""
import os, sys, json
import numpy as np, pytest
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
os.environ.setdefault('RF5_OUT', '/tmp/rf5_test_v31/'); os.makedirs('/tmp/rf5_test_v31/', exist_ok=True)
import rf5_fronteras as FR, rf5_eval as EV, rf5_nulo_inc as NI, rf5_run as RR

@pytest.fixture
def inc(tmp_path, monkeypatch):
    monkeypatch.setattr(RR, 'OUT', str(tmp_path) + '/'); os.makedirs(NI.dir_inc()); return tmp_path

def _linea(d, j, sello=None, kmax=None, fam='K'):
    return json.dumps(dict(dia=d, j=j, d={'K1': 0.1}, sello=NI.sello() if sello is None else sello, K_max=FR.k_max(fam) if kmax is None else kmax)) + '\n'

def test_sello_estable_y_cubre_el_nulo():
    assert len(NI.sello()) == 16 and NI.sello() == NI.sello() and all(f in RR.FICH_REG for f in NI.SELLO_FICH if f.endswith('.py'))

def test_lee_sellado_acepta_vigente_y_rechaza_otro_sello_o_kmax(inc):
    p = NI.ruta('K', 'x'); open(p, 'w').write(_linea('x', 0) + _linea('x', 1)); assert set(NI.lee_sellado(p, FR.k_max('K'))) == {('x', 0), ('x', 1)}
    open(p, 'a').write(_linea('x', 2, sello='deadbeef00000000')); 
    with pytest.raises(ValueError, match='SELLO_O_KMAX'): NI.lee_sellado(p, FR.k_max('K'))
    open(p, 'w').write(_linea('x', 0, kmax=500))
    with pytest.raises(ValueError): NI.lee_sellado(p, FR.k_max('K'))
    open(p, 'w').write(json.dumps(dict(dia='x', j=0, d={})) + '\n')                       # sin sello = rechazado
    with pytest.raises(ValueError): NI.lee_sellado(p, FR.k_max('K'))

def test_lee_replicas_y_replicas_faltan_rechazan_sello_distinto(inc):
    open(NI.ruta('K', 'x'), 'w').write(_linea('x', 0, sello='0' * 16))
    with pytest.raises(ValueError): NI.lee_replicas('K', ['x'], FR.k_max('K'))
    f = EV.replicas_faltan(['x']); assert 'SELLO_O_KMAX_DISTINTO' in f['K']

def test_calcula_dia_no_mezcla_sellos(inc, monkeypatch):
    monkeypatch.setattr(RR, 'lee_dia', lambda d: dict(status='COMPLETE')); open(NI.ruta('K', '2026-11-30'), 'w').write(_linea('2026-11-30', 0, sello='1' * 16))
    assert NI.calcula_dia('K', '2026-11-30') == 'BLOCKED'

def test_a_no_bloquea_y_solo_bloquean_k_y_k6(inc):
    assert EV.BLOQUEAN_MIRADA == ('K', 'K6') and set(EV.replicas_faltan(['x'])) == {'K', 'K6'}

def _k6_manifest(d, ok=True, status='COMPLETE'):
    json.dump(dict(status=status, cobertura=dict(calma_evaluable=dict(estado='EVALUABLE' if ok else 'NO_EVALUABLE_CALMA'))), open(RR.OUT + f'manifest_rf5K6_{d}.json', 'w'))

def test_mirada_k6_es_el_6o_dia_valido_de_k6_y_espera_a_los_pendientes(inc):
    D = lambda i: f'2026-12-{i:02d}'; est = {D(i): dict(status='COMPLETE', iv=True, iii='OK') for i in range(1, 9)}
    for i in (1, 2, 4, 5, 6, 7, 8): _k6_manifest(D(i))
    d = NI.mirada_k6(est); assert d['mirada'] == 0 and d['espera'] == [D(3)]               # el dia 3 aun no tiene K6 terminal: espera (RF5 si miraria)
    assert FR.decide_mirada(est)['mirada'] == 1
    _k6_manifest(D(3), ok=False)                                                            # dia 3 no evaluable: no cuenta; la mirada de K6 son los 6 primeros dias VALIDOS DE K6
    d = NI.mirada_k6(est); assert d['mirada'] == 1 and d['dias'] == [D(i) for i in (1, 2, 4, 5, 6, 7)] and NI.decide_fam('K6', est)['dias'] == d['dias']
    assert NI.decide_fam('K', est)['dias'] == [D(i) for i in range(1, 7)]                   # K sigue los dias de RF5

def test_mirada_k6_con_mas_del_20pc_no_evaluables_es_insufficient(inc):
    D = lambda i: f'2026-12-{i:02d}'; est = {D(i): dict(status='COMPLETE', iv=True, iii='OK') for i in range(1, 11)}
    for i in range(1, 11): _k6_manifest(D(i), ok=i > 3)                                     # 3 de 10 no evaluables (30 %)
    assert NI.mirada_k6(est)['mirada'] == 0 and NI.mirada_k6(est)['nombre'] == 'K6_INSUFFICIENT'
    for i in range(1, 11): _k6_manifest(D(i), ok=i > 1)                                     # 1 de 7 dias hasta la mirada (14 %): OK; la mirada de K6 usa los 6 primeros evaluables (2..7)
    d = NI.mirada_k6(est); assert d['mirada'] == 1 and d['dias'] == [D(i) for i in range(2, 8)]

def test_bretz_persistente_k1_rechazada_en_mirada1_se_lee_en_el_final(tmp_path):
    out = str(tmp_path) + '/'; NUK = dict(p_max=0.01)
    assert EV.k1_rechazada_persistente(out, 1, ['a'], 'COMBINADA_EV_POSITIVO', NUK) is True
    assert EV.k1_rechazada_persistente(out, 2, ['a'], 'NO_CONFIRMADA', NUK) is True                  # leido del resumen sellado, sin recontrastar K
    assert json.load(open(out + 'rf5_k1_mirada1.json'))['sello'] == NI.sello()
    o2 = str(tmp_path) + '/2/'; os.makedirs(o2)
    assert EV.k1_rechazada_persistente(o2, 1, ['a'], 'NO_CONFIRMADA', NUK) is False and EV.k1_rechazada_persistente(o2, 2, ['a'], 'NO_CONFIRMADA', NUK) is False
    assert EV.k1_rechazada_persistente(o2, 2, ['a'], 'COMBINADA_EV_POSITIVO', NUK) is True and json.load(open(o2 + 'rf5_k1_mirada1.json'))['k1_rechazada'] is False     # el fichero de la mirada 1 no se reescribe

def test_lee_nulo_rechaza_sello_o_kmax_distinto(tmp_path):
    out = str(tmp_path) + '/'; base = dict(dias=['a'], mirada=1, estado='NULO_RESIMULADO_EXACTO', p_max=0.01)
    json.dump(dict(base, sello=NI.sello(), K_max=FR.k_max('K6')), open(out + 'nulo_K6_resultado.json', 'w')); assert EV.lee_nulo(out, 'K6', ['a'], 1) is not None
    json.dump(dict(base, sello='f' * 16, K_max=FR.k_max('K6')), open(out + 'nulo_K6_resultado.json', 'w')); assert EV.lee_nulo(out, 'K6', ['a'], 1) is None
    json.dump(dict(base, sello=NI.sello(), K_max=1500), open(out + 'nulo_K6_resultado.json', 'w')); assert EV.lee_nulo(out, 'K6', ['a'], 1) is None

def test_workers_fijo_a_1():
    with pytest.raises(SystemExit, match='workers = 1'): NI.main(['cola', '--workers', '2'])

def test_umbrales_vs_azar_exactos():
    assert FR.UMBRAL[1]['vs_azar'] == 0.07085 and FR.UMBRAL[2]['vs_azar'] == 0.06165

def test_bretz_no_precinta_sin_nulo_K_ni_con_veredicto_pendiente(tmp_path):
    """v3.2: sin nuK (o con veredicto PENDIENTE*) la mirada 1 NO escribe rf5_k1_mirada1.json; si lo hiciera, un 'K1 no rechazada' provisional quedaria fijado y K6 perderia el alfa 0,05 en el final."""
    o = str(tmp_path) + '/'; f = o + 'rf5_k1_mirada1.json'
    assert EV.k1_rechazada_persistente(o, 1, ['a'], 'EV_POSITIVO_PENDIENTE_PMAXK', None) is False and not os.path.exists(f)
    assert EV.k1_rechazada_persistente(o, 1, ['a'], 'EV_POSITIVO_PENDIENTE_PMAXK', dict(p_max=0.01)) is False and not os.path.exists(f)
    assert EV.k1_rechazada_persistente(o, 1, ['a'], 'NO_CONFIRMADA', None) is False and not os.path.exists(f)
    assert EV.k1_rechazada_persistente(o, 1, ['a'], None, dict(p_max=0.01)) is False and not os.path.exists(f)
    assert EV.k1_rechazada_persistente(o, 2, ['a'], 'COMBINADA_EV_POSITIVO', dict(p_max=0.01)) is True          # el final rechaza ahora: sin fichero previo, vale el veredicto actual

def test_simk6_una_devuelve_delta_y_pasa_ev_shift(monkeypatch):
    """v3.2: SimK6.una se rompio (NameError pn) sin que ningun test lo ejecutara; ahora se ejecuta con un replay simulado."""
    import rf5_nulo_run as NR
    visto = {}
    def falso_replay(d, P, W, ctx, nombre, tabla, bsrc, cortes, tp, veto, bsrc_calma=None, ev_shift=None): visto['ev'] = ev_shift; return 'R', None, None
    monkeypatch.setattr(RR, '_replay', falso_replay); monkeypatch.setattr(NR, 'unidades_dia', lambda R: ('pn', 'co')); monkeypatch.setattr(NR, 'delta_dia', lambda pn, co, k1, b: (pn, co, k1, b))
    sim = NI.SimK6(cortes={}, tp=1.0); st = dict(d='x', P=None, W=None, ctx=None, bsrc={}, d0=1000, k1=('K1pnl', 'K1cost'), base=('bpnl', 'bcost'))
    assert sim.una(st, 0, 5000) == {'K6': ('pn', 'co', 'K1pnl', 'bcost')} and visto['ev'] == (1000, 5000, ('calma',))
