"""test_rf5_p1.py -- tests de ESPEC_ENGINEER_RF5 P1 (E1 puertas C1/C3, saltar no-COMPLETE/precintado, tabla de suelo). Sin red, sin ordenes; los datos reales usados son SOLO conteos de cobertura (0 EV/PnL)."""
import os, sys, json, tempfile
import numpy as np, pandas as pd, pytest
HV = os.path.dirname(os.path.abspath(__file__)) + '/'
_TMP = tempfile.mkdtemp(prefix='rf5p1_'); os.environ['RF5_OUT'] = _TMP + '/'; os.environ['P0_TAPES_REF'] = _TMP + '/tapes.txt'
sys.path.insert(0, HV)
import rf5_core as K5, rf5_eval as EV, rf5_gates as GT, cobertura_bruta as CB, rf5_run as RR
C = K5.lee_cortes(); HL = GT.lee_horas_leidas()
DAYS = lambda d: RR.P0R.dias_vec(d)

# ---------------------------------------------------------------- C1: cobertura SIN filtrar
def _chain(horas_malas, n=1000, cob_mala=0.4, dia='2026-12-10'):
    rows = []; rng = np.random.default_rng(1)
    for h in range(24):
        cob = cob_mala if h in horas_malas else 1.0
        for i in range(n):
            rows.append(dict(ts_est=pd.Timestamp(f'{dia} {h:02d}:00:00', tz='UTC').timestamp() + i, side=0, tx=f'tx{h}_{i}', price=0.3 + 0.01 * rng.random(), sh=5.0, token_id=f't{i % 4}', src='tx_ws' if (i / n) < cob else 'bloque'))
    ch = pd.DataFrame(rows); tev = set(ch.tx[ch.src == 'tx_ws']); return ch, tev

def test_c1_nueve_horas_malas_incomplete_aunque_la_cinta_filtrada_cubra_0998():
    ch, tev = _chain(set(range(3, 12)))                                            # 9 horas malas (cob 0,4)
    r = CB.agrega_horas(ch, tev); sanas = [h for h in r['horas'] if h['sana']]
    filtrada = sum(h['con_tx'] for h in sanas) / sum(h['units'] for h in sanas); assert filtrada > 0.998                # la comprobacion VACIA del runner viejo pasaba
    assert r['cov'] < 0.90 and len([h for h in r['horas'] if not h['sana']]) == 9
    bad = {x: [] for x in DAYS('2026-12-10')}; bad['2026-12-10'] = sorted(set(range(3, 12)))
    cov = {x: dict(units=r['units'], con_tx=r['con_tx']) for x in DAYS('2026-12-10')}; res = GT.evalua_c1(DAYS('2026-12-10'), cov, bad, HL)
    assert not res['ok'] and any('(i)' in m for m in res['motivos']) and any('(ii)' in m for m in res['motivos'])
    cov_ok = {x: dict(units=1000, con_tx=999) for x in DAYS('2026-12-10')}; res2 = GT.evalua_c1(DAYS('2026-12-10'), cov_ok, bad, HL)          # cobertura bruta alta pero 9 horas malas => (ii) igualmente
    assert not res2['ok'] and not any('(i)' in m for m in res2['motivos']) and any('(ii)' in m for m in res2['motivos'])

def test_c1_horas_leidas_de_dm1_y_dp1():
    d = '2026-12-10'; dm1, _, dp1 = DAYS(d); cov = {x: dict(units=100, con_tx=100) for x in DAYS(d)}
    assert GT.evalua_c1(DAYS(d), cov, {dm1: [], d: [], dp1: []}, HL)['ok']
    assert GT.evalua_c1(DAYS(d), cov, {dm1: [5, 6], d: [], dp1: [7]}, HL)['ok']                       # horas malas que la simulacion NO lee no bloquean
    r = GT.evalua_c1(DAYS(d), cov, {dm1: [23], d: [], dp1: []}, HL); assert not r['ok'] and '(iii)' in r['motivos'][0]
    r = GT.evalua_c1(DAYS(d), cov, {dm1: [], d: [], dp1: [0]}, HL); assert not r['ok']
    assert not GT.evalua_c1(DAYS(d), cov, {dm1: [], d: [], dp1: None}, HL)['ok']                      # sin bad_d+1 => no valido (fail-closed)
    assert GT.evalua_c1(DAYS(d), cov, {dm1: [], d: [0, 1], dp1: []}, HL)['ok'] and not GT.evalua_c1(DAYS(d), cov, {dm1: [], d: [0, 1, 2], dp1: []}, HL)['ok']   # f_horas >= 22/24

def test_horas_leidas_declaradas_con_sha(tmp_path):
    assert HL['sha256'] == GT.sha(HV + 'horas_leidas_d1.json') and HL['dm1'] == [23] and HL['dp1'] == [0]
    p = tmp_path / 'x.json'; p.write_text('{"d-1": [24], "d+1": []}')
    with pytest.raises(ValueError): GT.lee_horas_leidas(str(p))

def _cb(x): 
    p = RR.OUT.replace(os.path.basename(RR.OUT.rstrip('/')), '') ; return None
REAL = HV + 'out_rf5_ciego/'; DEVB = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/precursores_barrido/out/'
@pytest.mark.skipif(not all(os.path.exists(REAL + f'cobertura_bruta_2026-11-{d}.json') for d in (15, 16, 17, 18, 19)), reason='sin cobertura_bruta reales (se generan con cobertura_bruta.py)')
def test_c1_datos_reales_de_cobertura_sin_ev():
    def ev(d):
        dias = DAYS(d); cov = {}; 
        for x in dias: j = json.load(open(REAL + f'cobertura_bruta_{x}.json')); cov[x] = dict(units=j['units'], con_tx=j['con_tx'])
        return GT.evalua_c1(dias, cov, {x: RR.bad_horas(x, DEVB) for x in dias}, HL)
    r18, r17, r16 = ev('2026-11-18'), ev('2026-11-17'), ev('2026-11-16')
    assert not r18['ok'] and any('(i) 2026-11-19' in m for m in r18['motivos'])                      # 18-Nov: la cobertura sin filtrar del 19 es 0,72
    assert r17['ok']
    assert not any('(i)' in m for m in r16['motivos'])                                                  # 16-Nov: (i) pasa; la unica causa es (iii) hora 23 del 15 no sana
    assert r16['motivos'] and all('(iii)' in m for m in r16['motivos'])

# ---------------------------------------------------------------- evaluador salta lo no COMPLETE / precintado
def test_eval_no_abre_precintados_ni_dias_no_validos(tmp_path, monkeypatch):
    out = str(tmp_path) + '/'; d = '2026-12-01'
    for f in (f'rf5A_{d}.pkl', f'rf5_f5_0_{d}.pkl'): pd.DataFrame(dict(a=[1])).to_pickle(out + f)
    abiertos = []; orig = pd.read_pickle
    def espia(p, *a, **k):
        abiertos.append(os.path.basename(p))
        if os.path.basename(p) == f'rf5A_{d}.pkl': raise PermissionError('chmod 000')
        return orig(p, *a, **k)
    monkeypatch.setattr(pd, 'read_pickle', espia); reg = []
    R, F = EV.carga(out, [d], precint=set(), registro=reg); assert R is None and reg == [dict(dia=d, estado='precintado', motivo='sin permiso de lectura (chmod)')]       # sin excepcion
    abiertos.clear(); reg = []; R, F = EV.carga(out, [d], precint={f'rf5A_{d}.pkl'}, registro=reg); assert R is None and reg[0]['estado'] == 'precintado' and abiertos == []   # nombre precintado: ni se intenta abrir
    est = {d: dict(status='INCOMPLETE', iv=True, iii='OK'), '2026-12-02': dict(status='PENDING', iv=True, iii='OK'), '2026-12-03': dict(status='BLOCKED', iv=True, iii='OK')}; assert EV.dias_validos(est) == []

def test_precinto_real_18nov_listado():
    p = EV.precintados(); assert {'rf5A_2026-11-18.pkl', 'rf5_f5_0_2026-11-18.pkl'} <= p

def test_resumen_con_dia_precintado_no_rompe(tmp_path, monkeypatch):
    out = str(tmp_path) + '/'; d = '2026-11-18'; est = {d: dict(status='COMPLETE', iv=True, iii='OK')}
    for f in (f'rf5A_{d}.pkl', f'rf5_f5_0_{d}.pkl'): open(out + f, 'wb').write(b'no se abre')
    r = EV.resumen(out, est, C); assert r['modo'].startswith('SOLO_CONTEOS') and r['precintados_u_omitidos'][0]['estado'] == 'precintado' and 'familia_A' not in r

# ---------------------------------------------------------------- C3
def _lado(coin, i, coste=1.0, sin=False): return dict(coin=coin, mid=f'{coin}{i}', k=1, coste=coste, sin_res=sin)

def test_c3_por_moneda_y_umbral_099():
    L = [_lado(c, i) for c in ('ETH', 'SOL', 'XRP') for i in range(200)]; r = GT.evalua_c3(L); assert r['estado'] == 'OK' and r['por_moneda']['ETH']['frac_lados'] == 1.0
    L[0]['sin_res'] = True; L[1]['sin_res'] = True; L[2]['sin_res'] = True                                   # 3/200 ETH sin resolver = 0,985 < 0,99
    r = GT.evalua_c3(L); assert r['estado'] == 'PENDIENTE' and r['por_moneda']['ETH']['sin_resolver'] == 3 and r['por_moneda']['ETH']['coste_sin_resolver'] == 3.0 and r['por_moneda']['SOL']['frac_lados'] == 1.0
    L2 = [_lado(c, i) for c in ('ETH', 'SOL') for i in range(50)]; assert GT.evalua_c3(L2)['estado'] == 'PENDIENTE'          # XRP sin lados con relleno = sin evidencia (fail-closed)
    L3 = [_lado('ETH', i) for i in range(200)] + [_lado(c, i) for c in ('SOL', 'XRP') for i in range(200)]; L3[5]['coste'] = 100.0; L3[5]['sin_res'] = True    # pocos lados pero casi todo el coste sin resolver
    assert GT.evalua_c3(L3)['estado'] == 'PENDIENTE'
    assert GT.terminal_c3('2026-11-24', '2026-11-27', RR.dmas) and not GT.terminal_c3('2026-11-24', '2026-11-26', RR.dmas)

def test_c3_relleno_sin_resolver_cambia_el_ev_de_peor_caso_en_menos_coste_exacto():
    base = dict(dia='2026-12-01', k=1, lado='YES', pol='base', bloq=0, fin=1000, q=5.0)
    R = pd.DataFrame([dict(base, mid='a', coin='eth', cost=2.0, pnl=1.0, sin_res=False), dict(base, mid='b', coin='eth', cost=3.0, pnl=-3.0, sin_res=True)])   # b: sin desenlace => marcador gana=0 => pnl = -coste
    prim, peor = EV.sin_resolver_fuera(R); u_p = EV.unidades(prim, 'base'); u_w = EV.unidades(peor, 'base')
    assert u_p.pnl.sum() == 1.0 and u_w.pnl.sum() == 1.0 - 3.0 and u_w.pnl.sum() - u_p.pnl.sum() == -3.0           # diferencia = -coste exacto del lado sin resolver
    assert 'sin_res' not in pd.DataFrame(dict(a=[1])).columns and EV.sin_resolver_fuera(pd.DataFrame(dict(a=[1])))[0].equals(pd.DataFrame(dict(a=[1])))

def test_marcador_desenlace_es_peor_caso_y_reversible():
    import eng_v5 as EV5
    G = EV5.G; orig = G.capt_outcome
    try:
        G.capt_outcome = lambda E, k: (None if k == 1 else 1.0)
        D = type('D', (), dict(mid=['m0', 'm1']))()
        class E: pass
        e = E(); e.D = D
        with RR.desenlace_con_marcador() as unres:
            assert G.capt_outcome(e, 1) == 0.0 and G.capt_outcome(e, 0) == 1.0 and unres == {'m1'}
        assert G.capt_outcome(e, 1) is None and RR.UNRES == set()                                                    # restaurado
    finally: G.capt_outcome = orig

def test_c3_lados_union_y_columnas():
    R = pd.DataFrame([dict(mid='a', k=1, coin='eth', q=1.0, cost=1.0, sin_res=False, pol='base'), dict(mid='a', k=1, coin='eth', q=1.0, cost=1.5, sin_res=False, pol='F3'), dict(mid='b', k=1, coin='sol', q=0.0, cost=0.0, sin_res=True, pol='base')])
    r = RR.c3_lados(R); assert r['por_moneda']['ETH']['lados_relleno'] == 1 and r['por_moneda']['ETH']['coste_total'] == 1.5 and r['por_moneda']['SOL']['lados_relleno'] == 0   # sin relleno no cuenta como lado con relleno

# ---------------------------------------------------------------- tabla de suelo sucesora
def test_tabla_suelo_real_18_22_y_pendiente():
    df, info = GT.lee_tabla_suelo(C); assert info[0]['sha256'] == 'b72d49faa846f270460bc8a4eb9fe82850ec58f1c335fc00c3ae1b9090300919' and len(df) == 8640
    for d in ('2026-11-18', '2026-11-22'): r = GT.suelo_dia(df, d); assert r['estado'] == 'OK' and all(v['valido'] for v in r['por_moneda'].values())
    assert GT.suelo_dia(df, '2026-11-23')['estado'] == 'suelo_pendiente' and GT.suelo_dia(None, '2026-11-18')['estado'] == 'suelo_pendiente'

def test_tabla_suelo_sha_distinto_falla_cerrado(tmp_path):
    p = tmp_path / 't.csv'; p.write_text('dia,coin,w0_ms,w0_utc,n_filas,p5_ms,clase_estrato,causal_w0,p5_prev_h1,p5_prev_h2\n')
    with pytest.raises(ValueError): GT.lee_tabla_suelo(dict(tabla_suelo_sucesora=dict(ruta=str(p), sha256='0' * 64)))
    with pytest.raises(ValueError): GT.lee_tabla_suelo(dict(tabla_suelo_sucesora=dict(ruta=str(tmp_path / 'no.csv'), sha256='0' * 64)))
    assert GT.lee_tabla_suelo(dict(tabla_suelo_sucesora=None)) == (None, None)

def test_suelo_celdas_lo_validas_y_hi_data_blocked():
    def tabla(dia, lo, hi, ind, coin): return [dict(dia=dia, coin=coin, clase_estrato='lo') for _ in range(lo)] + [dict(dia=dia, coin=coin, clase_estrato='hi') for _ in range(hi)] + [dict(dia=dia, coin=coin, clase_estrato='indet') for _ in range(ind)]
    ok = pd.DataFrame(sum([tabla('d', 100, 0, 0, c) for c in ('ETH', 'SOL', 'XRP')], [])); assert GT.suelo_dia(ok, 'd')['estado'] == 'OK'
    hi = pd.DataFrame(sum([tabla('d', 100, 0, 0, 'ETH'), tabla('d', 10, 90, 0, 'SOL'), tabla('d', 100, 0, 0, 'XRP')], [])); r = GT.suelo_dia(hi, 'd'); assert r['estado'] == 'DATA_BLOCKED' and r['por_moneda']['SOL']['n_hi'] == 90
    poco = pd.DataFrame(sum([tabla('d', 20, 0, 0, c) for c in ('ETH', 'SOL', 'XRP')], [])); assert GT.suelo_dia(poco, 'd')['estado'] == 'DATA_BLOCKED'      # n_clasificadas < 24

# ---------------------------------------------------------------- flujo del dia: INCOMPLETE por C1 sin abrir nada pesado
def test_procesa_dia_incomplete_por_c1_y_terminal(tmp_path, monkeypatch):
    out = str(tmp_path) + '/'; pb = str(tmp_path / 'pb') + '/'; os.makedirs(pb); d = '2026-12-10'
    for x in DAYS(d):
        open(pb + f'tape_{x}.pkl', 'w').write('t'); json.dump(dict(bad=([[x, h] for h in range(3, 12)] if x == d else [])), open(pb + f'bad_{x}.json', 'w'))
    monkeypatch.setattr(RR, 'OUT', out); monkeypatch.setattr(RR.RU, 'PB', pb); monkeypatch.setattr(RR.P0R, 'sha_prereg', lambda: {}); monkeypatch.setattr(RR, 'verifica_registro', lambda: [])
    ch, tev = _chain(set(range(3, 12))); r = CB.agrega_horas(ch, tev); monkeypatch.setattr(RR.CB, 'obtener', lambda x, **k: dict(units=r['units'], con_tx=r['con_tx'], horas=r['horas'], resumen=CB.resumen_excluidas_vs_validas(r['horas']), horas_malas_propias=[]))
    monkeypatch.setattr(RR, 'run_A', lambda *a: (_ for _ in ()).throw(AssertionError('no debe simular')))
    assert RR.procesa_dia(d) == 'INCOMPLETE'; m = json.load(open(out + f'manifest_rf5dia_{d}.json'))
    assert m['status'] == 'INCOMPLETE' and m['c1']['ok'] is False and 'detalle' in m['c1'] and m['c1']['detalle']['descriptivo'][d]['resumen']['excluidas']['horas'] == 9 and not os.path.exists(out + f'rf5A_{d}.pkl')
    assert RR.procesa_dia(d) == 'INCOMPLETE'                                                                       # terminal: no se reevalua

def test_dry_run_modulos_nuevos_sin_envio_ni_secretos():
    src = ''.join(open(HV + f).read() for f in ('rf5_gates.py', 'rf5_nulo.py', 'rf5_huecos.py', 'rf5_k6.py', 'cobertura_bruta.py', 'rf5_acople_real.py'))
    for prohibido in ('post_order', 'create_order', 'py_clob_client', 'requests.', 'urllib', '/.env', 'dotenv', 'private_key', 'sign_order', 'Account.sign', 'websockets'): assert prohibido not in src, prohibido

def test_registro_cubre_los_ficheros_nuevos():
    for f in ('rf5_gates.py', 'cobertura_bruta.py', 'horas_leidas_d1.json', 'rf5_nulo.py', 'rf5_huecos.py', 'rf5_k6.py', 't_proc_cronometro.py', 'rf5_acople_real.py', 'rf5_t_proc_ms.txt'): assert f in RR.FICH_REG, f
