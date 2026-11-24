"""test_rf5_nulo_inc.py -- nulo incremental (ADENDA_RF5_NULO_INCREMENTAL_24nov): agregado incremental == bloque bit a bit (sintetico; el real en 17-Nov es rf5_nulo_inc.py dia ... --prueba), espera si falta una replica, K_max y resolucion, ventana, guardas. Sin datos reales."""
import os, sys, json, hashlib
import numpy as np, pytest
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import rf5_run as RR, rf5_nulo as NU, rf5_fronteras as FR, rf5_nulo_inc as NI

DIAS = ['2026-12-01', '2026-12-02', '2026-12-03']; POLS = ('K1', 'K2', 'K3', 'K4')

def fake(d, j, sesgo=0.0):
    """Delta determinista por (dia, j, pol): normal(sesgo, 1) por hash."""
    out = {}
    for p in POLS:
        r = np.random.default_rng(int.from_bytes(hashlib.sha256(f'{d}|{j}|{p}'.encode()).digest()[:8], 'big')); out[p] = float(r.normal(sesgo, 1.0))
    return out

@pytest.fixture
def inc(tmp_path, monkeypatch):
    monkeypatch.setattr(RR, 'OUT', str(tmp_path) + '/'); os.makedirs(NI.dir_inc(), exist_ok=True); return tmp_path

def escribe(fam, d, js, kmax):
    with open(NI.ruta(fam, d), 'a') as f:
        for j in js: f.write(json.dumps(dict(dia=d, j=j, d=fake(d, j), sello=NI.sello(), K_max=kmax)) + '\n')

def test_incremental_igual_a_bloque_bit_a_bit_con_orden_y_reanudacion_distintos(inc):
    K = 80; Tobs = 1.3
    # bloque: nulo_K_run calcula todo con su sim_bloque, bloques de 25
    ck = str(inc / 'bloque.jsonl'); calc = []
    def sim_bloque(d, lista): calc.extend(lista); return {j: fake(d, j) for j, _ in lista}
    b = NU.nulo_K_run(DIAS, Tobs, None, ck, K=K, h=1000, sim_bloque=sim_bloque, bloque=25)         # h grande: recorre toda la secuencia
    # incremental: dias en otro orden, tamaños de bloque distintos, una interrupcion y reanudacion, lineas duplicadas y una truncada
    escribe('K', DIAS[2], range(0, 30), K); escribe('K', DIAS[0], range(K), K); escribe('K', DIAS[2], range(20, K), K); escribe('K', DIAS[1], range(K), K)
    with open(NI.ruta('K', DIAS[1]), 'a') as f: f.write('{"dia": "2026-12-02", "j": 7, "d": {"K1"')                       # linea truncada (corte de luz)
    hechos, faltan = NI.lee_replicas('K', DIAS, K); assert faltan == {} and len(hechos) == K * len(DIAS)
    assert all(hechos[(d, j)] == fake(d, j) for d in DIAS for j in range(K))                                               # las replicas son IDENTICAS a las del bloque
    i = NI.agrega_replicas('K', DIAS, Tobs, K, h=1000); assert i['p_max'] == b['p_max'] and i['exceden'] == b['exceden'] and i['n_perm'] == b['n_perm'] == K
    for h in (3, 8, 20):                                                                                                    # con parada de Besag-Clifford tambien coincide
        bb = NU.nulo_K_run(DIAS, Tobs, None, str(inc / f'b{h}.jsonl'), K=K, h=h, sim_bloque=sim_bloque, bloque=7); ii = NI.agrega_replicas('K', DIAS, Tobs, K, h=h)
        assert (ii['p_max'], ii['exceden'], ii['n_perm'], ii['parada']) == (bb['p_max'], bb['exceden'], bb['n_perm'], bb['parada'])

def test_replicas_de_mas_no_cambian_el_p(inc):
    K = 50; escribe('K', DIAS[0], range(K), K); escribe('K', DIAS[1], range(K), K); escribe('K', DIAS[2], range(K), K)
    a = NI.agrega_replicas('K', DIAS, 0.4, K, h=1000); h50, f = NI.lee_replicas('K', DIAS, K); assert f == {} and len(h50) == 3 * K     # solo j < K_max entran
    b = NU.nulo_K_run(DIAS, 0.4, None, str(inc / 'x.jsonl'), K=K, h=1000, sim_bloque=lambda d, l: {j: fake(d, j) for j, _ in l}, bloque=K); assert a['p_max'] == b['p_max']

def test_si_falta_una_replica_la_mirada_espera(inc):
    K = 40; escribe('K', DIAS[0], range(K), K); escribe('K', DIAS[1], range(K), K); escribe('K', DIAS[2], [j for j in range(K) if j != 17], K)
    h, f = NI.lee_replicas('K', DIAS, K); assert h is None and f == {DIAS[2]: 1}
    r = NI.agrega_replicas('K', DIAS, 1.0, K); assert r['estado'] == 'ESPERA_REPLICAS' and r['faltan'] == {DIAS[2]: 1} and 'p_max' not in r
    escribe('K', DIAS[2], [17], K); assert 'p_max' in NI.agrega_replicas('K', DIAS, 1.0, K)

def test_k_max_por_familia_y_resolucion_5_sobre_umbral():
    assert FR.K_MAX == {'K': 250, 'K6': 1100, 'A': 500}
    for m in (1, 2):
        assert FR.resolucion_ok('K1_K4', m) and FR.resolucion_ok('A', m) and FR.resolucion_ok('K6', m, 0.01) and FR.resolucion_ok('K6', m, 0.05)
    assert 5 / FR.UMBRAL[2]['p_max_K1_K4'] < 500 and 5 / FR.UMBRAL[2]['p_max_A'] < 500 and 1063 < 5 / FR.UMBRAL[2]['K6_alfa001'] < 1064 <= 1500 and not FR.resolucion_ok('K6', 2, 0.01, k=1000)
    assert NI.ORDEN == ('K', 'K6', 'A')                                                     # la familia K antes que la A

def test_ventana_prohibida_y_limites():
    for h, ok in (('0559', True), ('0600', False), ('0914', False), ('0915', True), ('2214', True), ('2215', False), ('2229', False), ('2230', True), ('1200', True)): assert NI.ventana_ok(h) is ok

def test_no_aplica_antes_del_24nov_o_sin_dia_complete_y_prueba_no_ciega(inc, monkeypatch):
    monkeypatch.setattr(RR, 'lee_dia', lambda d: dict(status='COMPLETE'))
    assert NI.calcula_dia('K', '2026-11-22') == 'NO_APLICA'                                  # 18-22 se reprocesan pero no cuentan como validos
    monkeypatch.setattr(RR, 'lee_dia', lambda d: dict(status='PENDING')); assert NI.calcula_dia('K', '2026-11-25') == 'NO_APLICA'
    monkeypatch.setattr(RR, 'lee_dia', lambda d: None); assert NI.calcula_dia('A', '2026-11-25') == 'NO_APLICA'
    with pytest.raises(SystemExit): NI.calcula_dia('K', '2026-11-18', prueba=True)          # la prueba solo vale para dias <= 17-Nov

def test_corre_exige_autorizacion_y_el_estado_solo_tiene_conteos(inc, monkeypatch):
    monkeypatch.delenv('RF5_NULO_AUTORIZADO', raising=False)
    with pytest.raises(SystemExit) as e: NI.main_corre(['K'])
    assert 'BLOQUEADO' in str(e.value)
    NI.escribe_estado('K', DIAS[0], 12, 500, 'PARCIAL'); e = json.load(open(NI.ruta_estado()))
    assert set(e['K'][DIAS[0]]) == {'n', 'K_max', 'estado', 'sello', 't'} and e['K'][DIAS[0]]['n'] == 12

def test_agrega_sin_dias_de_mas_ni_de_menos_y_replicas_precintadas_en_su_dir(inc):
    escribe('K', DIAS[0], range(10), 10); assert NI.ruta('K', DIAS[0]).startswith(NI.dir_inc()) and NI.dir_inc().endswith('nulo_inc/')
    assert NI.lee_replicas('K', [DIAS[0], DIAS[1]], 10)[0] is None                              # un dia sin ninguna replica: espera

def test_vigia_avisos_del_nulo_incremental():
    import vigia_rf5 as V, time
    ahora = time.time(); t_fin = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(ahora - 40 * 3600))
    est = {'2026-11-24': dict(status='COMPLETE', t_fin=t_fin), '2026-11-22': dict(status='COMPLETE', t_fin=t_fin), '2026-11-25': dict(status='PENDING')}
    hb = dict(epoch=ahora - 3600, t='x')
    A = dict(V.avisos_nulo(est, hb, {}, ahora)); assert set(A) == {f'R8_nulo_{f}_2026-11-24_sin_replicas' for f in ('K', 'K6', 'A')}          # 22-Nov (reprocesado, no cuenta) y 25 (PENDING) no avisan
    ne = {'K': {'2026-11-24': dict(n=500, K_max=500, estado='COMPLETO')}, 'K6': {'2026-11-24': dict(n=3, K_max=1500, estado='BLOCKED: DATA_BLOCKED')}, 'A': {'2026-11-24': dict(n=10, K_max=500, estado='PARCIAL')}}
    A2 = dict(V.avisos_nulo(est, hb, ne, ahora)); assert set(A2) == {'R9_nulo_K6_2026-11-24_BLOCKED'}
    assert any(f == 'R10_nulo_parado' for f, _ in V.avisos_nulo(est, None, ne, ahora)) and not any(f == 'R10_nulo_parado' for f, _ in V.avisos_nulo(est, hb, ne, ahora))
    assert 'K: 11-24 500/500' in V.resumen_nulo(ne) and 'solo conteos' in V.resumen_nulo(ne)
    assert dict(V.avisos_nulo(est, hb, {'K': {'2026-11-24': dict(n=500, K_max=500, estado='COMPLETO')}, 'K6': {'2026-11-24': dict(n=1500, K_max=1500, estado='COMPLETO')}, 'A': {'2026-11-24': dict(n=500, K_max=500, estado='COMPLETO')}}, ahora)) == {}
