"""Tests del arnes PREREG_DB1 (fixtures diminutos; sin datos reales, sin red, sin ordenes). Ejecutar: python3 -m pytest -q experimentos/5m_barato/db1/tests"""
import sys, os, json, types, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.insert(0, HERE); sys.path.insert(0, HERE + '../q11')
import numpy as np, pandas as pd, pytest
import passdb as P, eval_db1 as E
D0 = int(pd.Timestamp('2026-11-10', tz='UTC').timestamp()) * 1000
def test_parches_aplican_sobre_fuentes_registradas(): P.parchear(P.MAIN_VN); P.extraer_rt(); P.parchear(P.PLA_VN)
def test_parche_falla_si_cambia_passT(monkeypatch, tmp_path):
    f = tmp_path / 'passT.py'; f.write_text('x=1\n'); monkeypatch.setattr(P, 'PT', str(f))
    with pytest.raises(AssertionError): P.parchear(P.MAIN_VN)
def test_circ_shift_mod_dia_y_conserva_n():
    a = np.array([D0 - 5000, D0 + 10, D0 + 86400000 - 1000, D0 + 40000000], np.int64); b = P.circ_shift(a, D0, 60000)   # el del dia anterior no entra
    assert len(b) == 3 and (b >= D0).all() and (b < D0 + 86400000).all() and (np.diff(b) >= 0).all()
    assert D0 + ((86400000 - 1000 + 60000) % 86400000) in b and D0 + 10 + 60000 in b
    assert P.shift_ms(3, '2026-11-10') == P.shift_ms(3, '2026-11-10') and 60000 <= P.shift_ms(3, '2026-11-10') <= 86340000
    assert P.shift_ms(3, '2026-11-10') != P.shift_ms(4, '2026-11-10') and 1 <= P.koff(5, '2026-11-10') <= 287
def test_recent_ventana_t1300_t300():
    tr = np.array([1000, 2000], np.int64); tq = np.array([1000, 1999, 2000, 2999, 3000, 3001], np.int64)   # t = tq + 300
    # (tq-1000, tq]: tq=1000 -> (0,1000] incluye 1000; 1999 -> (999,1999] incluye 1000; 2999 -> (1999,2999] incluye 2000; 3000 -> (2000,3000] NO incluye 2000
    assert P.recent(tr, tq).tolist() == [True, True, True, True, False, False]
def test_first_after_inclusivo_y_none():
    a = np.array([10, 20, 30], np.int64); assert P.first_after(a, 20, 25) == 20 and P.first_after(a, 21, 25) is None and P.first_after(a, 31, 99) is None
def _occ(huecos=()):
    o = {c: np.ones(86400, bool) for c in P.COINS}
    for a, b in huecos:
        for c in P.COINS: o[c][a:b] = False
    return o
def _ticks(occ_huecos=None, solo=None):
    o = _occ(occ_huecos or ()); return o
def test_salud_addendum1_cobertura_baja_no_invalida_y_dia_perfecto_valido():
    o = _occ(); o['XRP'][::2] = False; o['SOL'][::2] = False   # densidad 50 % por moneda (como el feed real): ya NO invalida (R1), sin silencio > 30 s
    s = P.salud_desde_occ(o, {c: 1 for c in P.COINS}, [3]); assert s['valido'] and s['regla'] == 'ADDENDUM1' and s['horas_sanas'] == 23 and s['horas_excluidas'] == [] and s['cobertura']['XRP'] == pytest.approx(0.5, abs=0.01)
def test_salud_hueco_moneda_gt30s_excluye_solo_su_hora_y_30s_exacto_no_cuenta():
    o = _occ(); o['SOL'][7200 + 100:7200 + 100 + 40] = False       # SOL calla 41 s (diferencia entre ticks 41 > 30) en la hora 2; ETH/XRP siguen: la union no tiene hueco
    s = P.salud_desde_occ(o, {c: 1 for c in P.COINS}, []); assert s['horas_excluidas_hueco'] == [2] and s['huecos_por_moneda_gt30s']['SOL'] == 1 and s['huecos_union_gt10s'] == 0 and s['valido']
    o = _occ(); o['SOL'][7300:7329] = False                       # 30 s entre ticks: NO es > 30
    s = P.salud_desde_occ(o, {c: 1 for c in P.COINS}, []); assert s['horas_excluidas'] == [] and s['valido']
def test_salud_hueco_union_gt10s_y_fin_de_hueco_mas_15s_cruza_hora():
    s = P.salud_desde_occ(_occ([(7200 + 3560, 7200 + 3585)]), {c: 1 for c in P.COINS}, []); assert s['huecos_union_gt10s'] == 1 and s['horas_excluidas'] == [2, 3]   # hueco termina en 3585 + 15 s > 3600
    s = P.salud_desde_occ(_occ([(7200, 7209)]), {c: 1 for c in P.COINS}, []); assert s['huecos_union_gt10s'] == 0 and s['horas_excluidas'] == []              # union 10 s no pasa de 10
def test_salud_r4_muchas_horas_o_hueco_prolongado_no_valido():
    s = P.salud_desde_occ(_occ([(3600 * h + 100, 3600 * h + 200) for h in (1, 3, 5, 7)]), {c: 1 for c in P.COINS}, []); assert len(s['horas_excluidas_hueco']) == 4 and not s['valido']      # 4+ horas
    s = P.salud_desde_occ(_occ([(3600 * h + 100, 3600 * h + 200) for h in (1, 3, 5)]), {c: 1 for c in P.COINS}, []); assert s['valido'] and len(s['horas_excluidas_hueco']) == 3
    s = P.salud_desde_occ(_occ([(3600 * h + 100, 3600 * h + 500) for h in (1, 3, 5)]), {c: 1 for c in P.COINS}, []); assert len(s['horas_hueco_union_gt300s']) == 3 and not s['valido']   # caida prolongada en >2 horas
    s = P.salud_desde_occ(_occ(), {c: 1 for c in P.COINS}, list(range(10))); assert s['valido'] and s['horas_sanas'] == 14 and s['horas_restantes'] == 14   # ADDENDUM3-B2: las horas bad tx_ws salen sin mas (ya no exigen >= 20)
    s = P.salud_desde_occ(_occ(), {c: 1 for c in P.COINS}, list(range(12))); assert s['valido'] and s['horas_restantes'] == 12                       # B3: 12 horas bastan
    s = P.salud_desde_occ(_occ(), {c: 1 for c in P.COINS}, list(range(13))); assert not s['valido'] and s['horas_restantes'] == 11 and '< 12' in s['motivo']   # B3: 11 no
def test_r4_addendum3_cuentan_solo_horas_binance_y_las_txws_no_suman():
    o = _occ([(3600 * h + 100, 3600 * h + 200) for h in (1, 3, 5)])               # 3 horas por hueco de union: valido (<= 3)
    s = P.salud_desde_occ(o, {}, [10, 11, 12, 13]); assert s['valido'] and s['horas_excluidas'] == [1, 3, 5] and s['horas_bad_txws'] == [10, 11, 12, 13] and s['horas_restantes'] == 17 and s['lectura_r4'] == 'ADDENDUM3-B'
    o = _occ([(3600 * h + 100, 3600 * h + 200) for h in (1, 3, 5, 7)]); assert not P.salud_desde_occ(o, {}, [10, 11])['valido']                        # 4 horas de Binance: no
    o = _occ([(3600 * 15 + 100, 3600 * 15 + 200)]); assert P.salud_desde_occ(o, {}, list(range(12)))['horas_restantes'] == 11 and not P.salud_desde_occ(o, {}, list(range(12)))['valido']   # 12 tx_ws + 1 Binance = 11 < 12
    o = _occ([(3600 * h + 100, 3600 * h + 500) for h in (1, 3)]); s = P.salud_desde_occ(o, {}, []); assert s['valido'] and len(s['horas_hueco_union_gt300s']) == 2      # <= 2 con hueco > 300 s
    s = P.salud_desde_occ(o, {}, [1]); assert len(s['horas_hueco_union_gt300s']) == 1                                                                  # la hora 1 es bad tx_ws: no cuenta contra Binance
def test_salud_moneda_sin_ticks_o_dia_sin_datos_no_valido():
    o = _occ(); o['XRP'][:] = False; assert not P.salud_desde_occ(o, {}, [])['valido']
    assert not P.salud_desde_occ(_occ(), {}, list(range(24)))['valido']
def test_salud_eventos_r5_y_fichero_ausente():
    ev = [('caida', 3 * 3600 + 5), ('hijo_asume', 9 * 3600 + 1)]
    s = P.salud_desde_occ(_occ(), {}, [], ev); assert s['horas_excluidas'] == [3, 9] and s['valido'] and s['huecos_csv'].startswith('2')
    s = P.salud_desde_occ(_occ(), {}, [], None); assert s['horas_excluidas'] == [] and s['huecos_csv'] == 'ausente'     # missing != sin eventos: se anota
def test_eventos_huecos_ignora_benignos(tmp_path, monkeypatch):
    monkeypatch.setattr(P, 'DL', str(tmp_path) + '/'); assert P.eventos_huecos('2026-11-10', D0) is None
    (tmp_path / 'binance_huecos_2026-11-10.csv').write_text(f'evento,t_ms,conn_id,pid,motivo\narranque,{D0+10},,1,x\nlock_tomado,{D0+11},,1,\nconexion,{D0+12},1,1,\ncaida,{D0+7200000+5},1,1,x\nparada,{D0-5},,1,\n')
    assert P.eventos_huecos('2026-11-10', D0) == [('caida', 7200)]     # la parada del dia anterior no entra
def test_salud_sensibilidad_R6_se_guarda():
    o = _occ(); o['SOL'][7300:7340] = False; s = P.salud_desde_occ(o, {}, []); assert s['excl_sensibilidad_R6']['15'] == [2] and s['excl_sensibilidad_R6']['60'] == [] and s['horas_excluidas'] == [2]
def test_sv_delta_minimo_5_comision_profundidad():
    assert P.sv_delta(4.99, 0.2, 100, 0.0) == 0.0                                  # < 5 acciones: no se puede vender
    assert P.sv_delta(5.0, 0.2, 3.0, 0.0) == 0.0                                   # profundidad visible 3 < 5
    assert P.sv_delta(5.0, 0.2, 100, 0.0) == pytest.approx(5 * (0.2 - 0.0) - 0.07 * 0.2 * 0.8 * 5)   # perdedor: vender gana 1 - fee
    assert P.sv_delta(5.0, 0.2, 100, 1.0) == pytest.approx(5 * (0.2 - 1.0) - 0.07 * 0.2 * 0.8 * 5)   # ganador: vender cuesta
def test_sv_delta_redondea_tick_y_evita_autocruce_con_escalera():
    assert P.sv_delta(5.0, 0.2000001, 100, 0.0) == pytest.approx(5 * 0.2 - 0.07 * 0.2 * 0.8 * 5)       # ruido float -> tick
    assert P.sv_delta(5.0, 0.13, 100, 0.0, propios=(0.10, 0.13, 0.16, 0.19)) == 0.0                 # el mejor bid puede ser NUESTRA orden: no se vende contra uno mismo
    assert P.sv_delta(5.0, 0.12, 100, 0.0, propios=(0.10, 0.13, 0.16, 0.19)) > 0
    assert P.sv_delta(5.0, 0.0, 100, 0.0) == 0.0
def test_band_max_levels_todas_las_variantes():
    assert max(P.niveles_desde_fuente()) <= P.BAND_MAX      # engine.py registrado
    P.check_band((0.10, 0.19)); R = pd.DataFrame(dict(var=['G0', 'DB1_150@CROSS'], L=[0.19, 0.19])); P.check_band((0.10, 0.19), R)
    with pytest.raises(AssertionError): P.check_band((0.10, 0.25))
    with pytest.raises(AssertionError): P.check_band((0.10, 0.19), pd.DataFrame(dict(var=['G0', 'DB1_150@THIN'], L=[0.19, 0.21])))
    assert set(P.FVS) == {'CROSS', 'STRICT', 'OPT', 'THIN'}      # las cotas de relleno no cambian los niveles: check_band comprueba L de TODAS las variantes (incl. @cota)
def test_pvalor_formula_y_signo():
    m, p = E.pvalor(10.0, [0.0] * 99); assert m == 0.0 and p == pytest.approx(1 / 100)
    m, p = E.pvalor(0.0, list(np.linspace(-1, 1, 99))); assert p >= 0.9
def test_hora_bloqueada():
    f = lambda h, m: dt.datetime(2026, 11, 10, h, m, tzinfo=dt.timezone.utc)
    assert E.hora_bloqueada(f(6, 0)) and E.hora_bloqueada(f(9, 14)) and not E.hora_bloqueada(f(9, 15)) and E.hora_bloqueada(f(22, 20)) and not E.hora_bloqueada(f(22, 30)) and not E.hora_bloqueada(f(13, 20))
def test_producir_bloqueado_en_hora_y_sin_ordenes():
    with pytest.raises(SystemExit): E.producir('2026-11-10', ahora=dt.datetime(2026, 11, 10, 7, 0, tzinfo=dt.timezone.utc))
def test_producir_idempotente_si_existe_RX(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(E, 'OUT', str(tmp_path) + '/'); (tmp_path / 'RX_2026-11-10.pkl').write_bytes(b'x')
    assert E.producir('2026-11-10', ahora=dt.datetime(2026, 11, 10, 13, 0, tzinfo=dt.timezone.utc)) == 0 and 'ya' in capsys.readouterr().out
def test_checkpoint_corrupto_se_trata_como_vacio(tmp_path):
    f = tmp_path / 'c.json'; f.write_text('{no es json'); assert E.leer_json(str(f), {}) == {}
def test_cargar_rechaza_dia_distinto(tmp_path):
    pd.DataFrame(dict(dia=['2026-11-09'], pnl=[1.0])).to_pickle(tmp_path / 'RX_2026-11-10.pkl')
    with pytest.raises(ValueError): E.cargar(['2026-11-10'], str(tmp_path) + '/')
def test_dia_en_curso_y_sha_prereg_distinto(tmp_path, monkeypatch):
    monkeypatch.setattr(E, 'OUT', str(tmp_path) + '/'); assert E.dia_valido('2026-11-10', hoy='2026-11-10')['en_curso']
    (tmp_path / 'validez_2026-11-05.json').write_text(json.dumps(dict(dia='2026-11-05', prereg_sha='otro', valido_db1=True, valido_db2=True)))
    monkeypatch.setattr(E, 'tiene_insumos', lambda d: ['tape']); assert E.dia_valido('2026-11-05', hoy='2026-11-11').get('pendiente')   # cache con otro sha del prereg se rechaza
def test_aceptacion_falla_sin_rx_de_quemados(tmp_path, monkeypatch):
    monkeypatch.setattr(E, 'OUT', str(tmp_path) + '/'); r = E.aceptacion(str(tmp_path / 'a.json')); assert not r['pass_'] and 'faltan' in r['motivo']
def test_sin_aceptacion_el_informe_es_insufficient(tmp_path, monkeypatch):
    monkeypatch.setattr(E, 'HERE', str(tmp_path) + '/'); monkeypatch.setattr(E, 'OUT', str(tmp_path) + '/out/'); monkeypatch.setattr(E, 'tiene_insumos', lambda d: ['tape'])
    L, st = E.informe('2026-11-12', None); assert st == 'INSUFFICIENT' and any('ACEPTACION' in x for x in L)
# ---- disparadores (Ctx) con un D de juguete
class FakeD:
    def __init__(s):
        s.toks = ['a', 'b', 'c', 'd']; s.act = np.array(['ETH'] * 4); s.marco = np.array(['5min'] * 4); s.mid = np.array(['m1', 'm1', 'm2', 'm2']); s.lado = np.array(['YES', 'NO', 'YES', 'NO'])
        s.fin = np.array([D0 // 1000 + 300, D0 // 1000 + 300, D0 // 1000 + 600, D0 // 1000 + 600])
        # prints: token 0 (YES m1): vende en t=100 (contra YES), compra en t=200 (a favor); token 1 (NO m1): compra en t=300 (contra YES: compra del complementario), vende en t=400 (a favor)
        s.tk = np.array([0, 0, 1, 1, 2, 3]); s.tt = np.array([100, 200, 300, 400, 5000, 6000]) + D0; s.tsd = np.array([0, 1, 1, 0, 0, 1]); s.tp = np.full(6, 0.1); s.tsz = np.array([5.0, 5.1, 5.2, 5.3, 5.4, 5.5])
        s.tb = np.searchsorted(s.tk, np.arange(5))
    def comp(s, k): return {0: 1, 1: 0, 2: 3, 3: 2}[k]
def _ctx(seed=None):
    c = P.Ctx('2026-11-10', seed); c.D = FakeD(); c.day0 = D0; c.TR = {'ETH': dict(up=np.array([D0 + 1000, D0 + 9000], np.int64), dn=np.array([D0 + 3000], np.int64))}
    c.kmap = {(c.D.act[i], int(c.D.fin[i]), c.D.lado[i]): i for i in range(4)}; return c
def test_prints_contra_y_a_favor_por_lado():
    c = _ctx(); ag, fa = c.prints(0); assert (ag - D0).tolist() == [100, 300] and (fa - D0).tolist() == [200, 400]
    ag, fa = c.prints(1); assert (ag - D0).tolist() == [200, 400] and (fa - D0).tolist() == [100, 300]   # lado NO: invertido
def test_specs_signo_firmado_a_favor_del_lado_y_cancelacion():
    c = _ctx(); g = np.array([D0 + 3500], np.int64); tq = g - 300; base = np.array([True]); Gm = base
    sy = c.db_specs(0, 0.1, g, base, Gm, 'ETH', 'YES', tq); sn = c.db_specs(1, 0.1, g, base, Gm, 'ETH', 'NO', tq)
    # YES: adverso = caida de Binance (dn=D0+3000) dentro de (tq-1000, tq] = (D0+2200, D0+3200] -> NO arma; NO: adverso = subida (up D0+1000, D0+9000): fuera de ventana -> arma
    assert sy['DB1_150'][0].tolist() == [False] and sn['DB1_150'][0].tolist() == [True]
    assert sy['INV1_150'][0].tolist() == [True] and sn['INV1_150'][0].tolist() == [False]   # inversion: a favor del lado (NO: caida dn en ventana => no arma)
    # cancelacion: primer disparo en [t_arr, t_end] + l ; sin disparo => None
    assert sn['DB1_150'][1](D0 + 500, D0 + 2000) == D0 + 1000 + 150 and sn['DB1_150'][1](D0 + 1500, D0 + 8000) is None and sy['DB1_300'][1](D0 + 2500, D0 + 4000) == D0 + 3000 + 300
    # DB2: prints contra YES en 100 y 300 -> en tq (D0+3200) la ventana (2200,3200] no los contiene -> arma; con tq = D0+1000 ventana (0,1000] contiene el 100 -> no arma
    assert sy['DB2_150'][0].tolist() == [True] and c.db_specs(0, 0.1, np.array([D0 + 1300]), base, Gm, 'ETH', 'YES', np.array([D0 + 1000]))['DB2_150'][0].tolist() == [False]
    assert sy['DBU_150'][0].tolist() == [False]    # union: el disparo de Binance basta
    assert 'G0@CROSS' in sy and 'DB1_150@THIN' in sy and sy['G0'][1] is None
def test_placebo_db1_desplaza_y_db2_alinea_por_tiempo_hasta_cierre():
    c = _ctx(seed=7); c.TR = {'ETH': dict(up=np.array([D0 + 1000], np.int64), dn=np.array([D0 + 3000], np.int64))}
    c.TR['ETH']['up'] = P.circ_shift(c.TR['ETH']['up'], D0, P.shift_ms(7, c.d)); assert len(c.TR['ETH']['up']) == 1 and c.TR['ETH']['up'][0] != D0 + 1000
    k0 = P.koff(7, c.d); assert 1 <= k0 <= 287
    c.kmap = {('ETH', int(D0 // 1000 + 300 + 300 * j), 'YES'): 10 + j for j in range(2)}     # sin mercado desplazado => sin disparos (cuenta de huecos)
    assert c.prints_placebo(0).size == 0 and c.miss_pla == 1
    c2 = _ctx(seed=7); import unittest.mock as um
    with um.patch.object(P, 'koff', lambda s, d: 1): ag = c2.prints_placebo(0)   # k=1 cierre (300 s) despues: mercado m2 (fin +600) -> prints de tokens 2/3 desplazados -300 s
    assert len(ag) == 2 and (ag == np.sort(np.array([5000 + D0, 6000 + D0]) + (300 - 600) * 1000)).all()
def test_validar_lado_concordancia():
    D = FakeD(); ks = [0, 1, 2, 3]; ts = (D.tt[:6]).astype('int64')
    C = pd.DataFrame(dict(kidx=D.tk, pr=np.full(6, 0.1), sz=D.tsz, ts_ms=ts + 500, side=D.tsd))
    r = P.validar_lado(C, D, ks); assert r['n_match'] == 6 and r['concordancia'] == 1.0 and not r['valido']   # < 1000 casados: no valido (missing != OK)
    assert P.validar_lado(None, D, ks)['valido'] is False
def test_extras_sin_libro_es_nan_y_sin_bid_es_cero():
    class DN(FakeD):
        def book(s, k, t): return None
    class DB(FakeD):
        def book(s, k, t): return (float('nan'), 0.12, 0.0, 3.0)
    C = pd.DataFrame(dict(tx=['t1'], li=[1], bloque=[7], taker=['A'], side=[0], kidx=[0], pr=[0.1], sz=[5.0], ts_ms=[0]))
    R = pd.DataFrame(dict(var=['G0'], dia=['2026-11-10'], act=['ETH'], lado=['YES'], fin=[D0 // 1000 + 300], k=[0], L=[0.10], q=[5.0], tf=[D0 + 100], gana=[0.0], cost=[0.5], pnl=[0.0]))
    tpx = pd.DataFrame(dict(k=[0], tx=['t1'], log_index=[1], tm=[D0 + 100]))
    a = P.extras(dict(D=DN(), _TPX=tpx), R.copy(), C); assert np.isnan(a.sv150[0]) and np.isnan(a.sv1000[0]) and np.isnan(a.mk1[0])
    b = P.extras(dict(D=DB(), _TPX=tpx), R.copy(), C); assert b.sv150[0] == 0.0 and np.isnan(b.mk1[0])
def test_extras_burst_markout_y_salida():
    class D_(FakeD):
        def book(s, k, t): return (0.10, 0.12, 20.0, 3.0)
    D = D_(); C = pd.DataFrame(dict(tx=['t1', 't2'], li=[1, 2], bloque=[7, 7], taker=['A', 'B'], side=[0, 0], kidx=[0, 0], pr=[0.1, 0.1], sz=[5.0, 5.0], ts_ms=[0, 0]))
    R = pd.DataFrame(dict(var=['G0'], dia=['2026-11-10'], act=['ETH'], lado=['YES'], fin=[D0 // 1000 + 300], k=[0], L=[0.10], q=[5.0], tf=[D0 + 100], gana=[0.0], cost=[0.5], pnl=[0.0]))
    ns = dict(D=D, _TPX=pd.DataFrame(dict(k=[0, 0], tx=['t1', 't2'], log_index=[1, 2], tm=[D0 + 100, D0 + 100]))); R = P.extras(ns, R, C)
    assert bool(R.burst[0]) and bool(R.burst_known[0]) and R.mk1[0] == pytest.approx(0.01) and R.sv150[0] == pytest.approx(5 * 0.10 - 0.07 * 0.1 * 0.9 * 5) and R.pnl_nr[0] == pytest.approx(5 * (0.0 - 0.1))
    C1 = C.iloc[:1]; R2 = P.extras(ns, R.drop(columns=[c for c in R.columns if c in ('burst', 'burst_known')]).copy(), C1); assert not bool(R2.burst[0]) and bool(R2.burst_known[0])   # un solo tomador: no es rafaga
    R3 = P.extras(ns, R.copy(), None); assert np.isnan(R3.burst[0]) and not bool(R3.burst_known[0])    # sin on-chain: desconocido = NaN, no 'no rafaga' confirmada
# ---- metricas y veredicto con datos sinteticos
def _R(dias=10, extra_pnl=0.5):
    rows = []; fin = 0
    for di in range(dias):
        d = (pd.Timestamp('2026-11-10') + pd.Timedelta(days=di)).strftime('%Y-%m-%d')
        for j in range(40):
            fin += 300; act = ['ETH', 'SOL', 'XRP'][j % 3]; lado = ['YES', 'NO'][j % 2]; gana = 0.0 if j % 5 == 3 else float(j % 4 == 0)
            row = dict(dia=d, act=act, lado=lado, fin=fin, k=fin, L=0.13, q=5.0, tf=fin * 1000 - 10000, gana=gana, seg=0, T=10.0, ftype='thru1', canc=0, burst=(j % 5 == 0), burst_known=True, mk1=-0.03, mk5=-0.03, mk30=-0.03, sv150=0.1, sv500=0.1, sv1000=0.1)
            for v in ('G0', 'G0@CROSS', 'G0@STRICT', 'G0@OPT', 'G0@THIN'): rows.append(dict(row, var=v))
            if j % 5 != 3:   # el brazo quita 1 de cada 5 (j%5==3, ambos lados) y son perdedores
                for v in ('DB1_150', 'DB1_150@CROSS', 'DB1_150@STRICT', 'DB1_150@OPT', 'DB1_150@THIN', 'INV1_150'): rows.append(dict(row, var=v))
    R = pd.DataFrame(rows); R['cost'] = R.q * R.L; R['pnl_nr'] = R.q * (R.gana - R.L); R['reb'] = 0.01; R['pnl'] = R.pnl_nr + R.reb
    R.loc[R['var'] == 'INV1_150', 'pnl_nr'] = -1.0; return R
def test_metricas_dpnl_quitados_y_dims():
    R = _R(); days = sorted(R.dia.unique()); m = E.metricas(R, 'DB1', days)
    assert m['n_g0'] == 400 and m['n_arm'] == 320 and m['quitados'] == 80 and m['quitados_malos_n'] == 80 and m['quitados_buenos_n'] == 0
    assert m['base']['tot'] == pytest.approx(80 * 5 * 0.13) and m['base']['ncierres'] == 400 and m['cross']['tot'] == pytest.approx(52.0)
    assert sum(m['dim']['moneda'].values()) == pytest.approx(52.0) and m['coin_pos_max'] <= 0.5 and m['dim']['lado']['YES'] > 0 and m['dim']['lado']['NO'] > 0
def test_veredicto_refuta_insufficient_y_candidato():
    R = _R(); days = sorted(R.dia.unique()); m = E.metricas(R, 'DB1', days)
    pl = dict(p=0.03, d_obs=m['base']['tot'], m=0.0, perm=[0.0] * 99); et, c = E.veredicto_cp(m, 10, pl, None); assert 'CANDIDATO' in et and not et.startswith('NO'), (et, c)
    assert E.veredicto_cp(m, 10, None, None)[0].startswith('NO CANDIDATO')                      # sin placebo: nunca CANDIDATO
    pl_mal = dict(pl, p=0.5); assert E.veredicto_cp(m, 10, pl_mal, None)[0].startswith('NO CANDIDATO')
    m2 = dict(m, inv=1e9); assert E.veredicto_cp(m2, 10, pl, None)[0].startswith('NO CANDIDATO')   # C7: la inversion no puede ganar al placebo
    m3 = dict(m, dim=dict(m['dim'], lado={'YES': 5.0, 'NO': -1.0})); assert 'REGIMEN' in E.veredicto_cp(m3, 10, pl, None)[0]
    neg = dict(m, base=dict(m['base'], tot=-1.0)); assert E.veredicto_cp(neg, 10, pl, None)[0] == 'REFUTA'
    assert E.veredicto_cp(dict(m, nd=2), 10, pl, None)[0] == 'INSUFFICIENT' and E.veredicto_cp(dict(m, base=dict(m['base'], ncierres=2)), 10, pl, None)[0] == 'INSUFFICIENT'
    R20 = _R(20); d20 = sorted(R20.dia.unique()); m20 = E.metricas(R20, 'DB1', d20)
    assert E.veredicto_cp(m20, 20, dict(pl, p=0.5, d_obs=m20['base']['tot']), None)[0] == 'REFUTA'   # checkpoint 20 sin CANDIDATO = REFUTA terminal
    assert E.veredicto_cp(m, 20, dict(pl, p=0.5), None)[0] == 'INSUFFICIENT'   # 10 dias no son el checkpoint 20
def test_veredicto_rechaza_fuera_de_checkpoint_y_con_menos_de_10_dias():
    R = _R(5); m = E.metricas(R, 'DB1', sorted(R.dia.unique()))
    with pytest.raises(ValueError): E.veredicto_cp(m, 5, None, None)
    et, c = E.veredicto_cp(m, 10, None, None); assert et == 'INSUFFICIENT' and 'fuera de checkpoint' in c['motivo']      # nunca REFUTA/CANDIDATO con 5 dias
    neg = dict(m, base=dict(m['base'], tot=-5.0)); assert E.veredicto_cp(neg, 10, None, None)[0] == 'INSUFFICIENT'
@pytest.fixture(autouse=True)
def _sin_r6_en_fixtures(request, monkeypatch):
    if 'sens_r6' not in request.node.name: monkeypatch.setattr(E, 'sens_r6', lambda arm, days, tot: dict({'15': tot, '30': tot, '60': tot}, cambio_signo=False))     # R6 lee RX/excl/cov del disco: se prueba aparte
def test_rmr_solo_conocidos_y_cobertura():
    R = _R(); R['burst'] = R.burst.astype(float); R.loc[(R['var'] == 'G0') & (R.index % 2 == 0), 'burst_known'] = False; R.loc[(R['var'] == 'G0') & (R.index % 2 == 0), 'burst'] = np.nan
    r = E.rmr(R); assert r['G0']['n_conocidos'] < r['G0']['n_todos'] and r['G0']['conocido'] < 1 and r['G0']['n'] <= r['G0']['n_conocidos'] and r['DB1_150']['conocido'] == 1.0
def test_cache_validez_invalida_por_clave_addendum_y_codigo(tmp_path, monkeypatch):
    monkeypatch.setattr(E, 'OUT', str(tmp_path) + '/'); monkeypatch.setattr(E, 'tiene_insumos', lambda d: [])
    (tmp_path / 'validez_2026-11-01.json').write_text(json.dumps(dict(dia='2026-11-01', prereg_sha=E.PREREG_SHA, valido_db1=True, valido_db2=True, motivo='')))    # cache de la clave vieja (solo prereg)
    r = E.dia_valido('2026-11-01', hoy='2026-11-10'); assert r.get('pendiente') and r['valido_db1'] is False         # no se reutiliza (sin RX/cov)
    k0 = E.clave_validez(); monkeypatch.setattr(E.P, 'ADD1_SHA', 'x' * 64); assert E.clave_validez() != k0
    monkeypatch.undo(); monkeypatch.setattr(E, 'sha_codigo', lambda: 'otro'); assert E.clave_validez() != k0
def test_dia_con_cov_sin_regla_addendum1_no_valido(tmp_path, monkeypatch):
    monkeypatch.setattr(E, 'OUT', str(tmp_path) + '/'); monkeypatch.setattr(E, 'tiene_insumos', lambda d: []); monkeypatch.setattr(E.E1, 'asentado', lambda *a: (True, ''))
    (tmp_path / 'RX_2026-11-01.pkl').write_bytes(b'x'); lp = dict(valido=True, concordancia=1.0, motivo='')
    (tmp_path / 'cov_2026-11-01.json').write_text(json.dumps(dict(cobertura_desenlace=1.0, lado_print=lp, binance=dict(valido=True, cobertura_min=0.4, horas_excluidas=[], motivo=''))))
    r = E.dia_valido('2026-11-01', hoy='2026-11-10'); assert not r['valido_db1'] and 'ADDENDUM1' in r['motivo']
    (tmp_path / 'validez_2026-11-01.json').unlink()
    (tmp_path / 'cov_2026-11-01.json').write_text(json.dumps(dict(cobertura_desenlace=1.0, lado_print=lp, binance=dict(regla='ADDENDUM1', addendum1_sha=E.P.ADD1_SHA, valido=True, cobertura_min=0.4, horas_excluidas=[], horas_excluidas_hueco=[], motivo=''))))
    r = E.dia_valido('2026-11-01', hoy='2026-11-10'); assert not r['valido_db1'] and 'ADDENDUM3-B' in r['motivo']      # cov con la lectura antigua de R4: se reproduce
    (tmp_path / 'validez_2026-11-01.json').unlink()
    (tmp_path / 'cov_2026-11-01.json').write_text(json.dumps(dict(cobertura_desenlace=1.0, lado_print=lp, binance=dict(regla='ADDENDUM1', lectura_r4='ADDENDUM3-B', addendum1_sha=E.P.ADD1_SHA, valido=True, cobertura_min=0.4, horas_excluidas=[], horas_excluidas_hueco=[], horas_bad_txws=[3], horas_restantes=23, motivo=''))))
    r = E.dia_valido('2026-11-01', hoy='2026-11-10'); assert r['valido_db1'] and r['horas_restantes'] == 23 and r['horas_txws_perdidas'] == [3] and r['clave'] == E.clave_validez() and r['binance_min'] == 0.4
def test_congelados_coinciden_con_los_ficheros(): E.verificar_congelados(); assert P.ADD1_SHA == open(E.PREREG_ADD1.replace('.md', '.sha256')).read().split()[0]
def test_rmr_fraccion_cancelable():
    R = _R(); r = E.rmr(R); assert r['G0']['n'] == 80 and r['DB1_150']['n'] == 60 or r['DB1_150']['n'] <= r['G0']['n']
    assert 0 <= r['DB1_150']['fraccion_cancelable'] <= 1
def test_markout_precision_recobrado():
    R = _R(); o = E.markout_salida(R, arms=('G0',)); assert o['G0']['mk1']['marcados'] == 400 and o['G0']['mk1']['precision'] == pytest.approx(float((R[R['var']=='G0'].gana == 0).mean())) and o['G0']['mk1']['recobrado'] == 1.0
def test_seguridad_dry_run_sin_envio_ni_secretos():
    src = open(HERE + 'passdb.py').read() + open(HERE + 'eval_db1.py').read()
    for prohibido in ('py_clob_client', 'post_order', 'create_order', '.env', 'private_key', 'PRIVATE_KEY', 'requests.post', 'sign_order', 'enviar_orden'): assert prohibido not in src.replace('SOLO lectura', ''), prohibido

def test_fichero_ficticio_out_no_se_dobla():   # regresion 10-Nov: passT hace OUT = dirname(__file__)+'/out/'
    for od in (P.HERE + 'out/', P.HERE + 'placebo/s3/out/'):
        assert os.path.dirname(P.fichero_ficticio(od)) + '/out/' == od

def test_validar_lado_kidx_int16_del_engine_no_rompe_merge_asof():   # regresion 10-Nov: D.tk int16 vs kidx int64 -> MergeError
    D = types.SimpleNamespace(tk=np.array([0, 1, 1], np.int16), tt=np.array([1000, 2000, 3000]), tp=np.array([.5, .5, .4]), tsz=np.array([10., 10., 5.]), tsd=np.array([1, 0, 1]))
    C = pd.DataFrame(dict(kidx=np.array([0, 1], np.int64), pr=[.5, .5], sz=[10., 10.], ts_ms=[1000, 2000], side=[1, 0]))
    r = P.validar_lado(C, D, [0, 1]); assert r['n_ws'] == 3 and r['n_match'] == 2 and r['concordancia'] == 1.0

# ---- ADDENDUM3 (a): la exclusion de Binance es un FILTRO posterior; (b) vida por (variante, mercado, lado); aceptacion A1-A3
def _fin(h, m=0): return D0 // 1000 + h * 3600 + m * 60 + 300      # fin del mercado cuya apertura (fin-300) cae en la hora h, minuto m
def test_mascara_excluidas_equivale_a_engine_sane_por_apertura_o_cierre():
    fin = np.array([_fin(5), _fin(5, 56), _fin(6), D0 // 1000 + 6 * 3600], np.int64)   # apertura en 5, apertura 5:56 (cierre 6:01), apertura 6:00, cierre justo a las 6:00 (apertura 5:55)
    assert P.mascara_excluidas(fin, [5]).tolist() == [True, True, False, True] and P.mascara_excluidas(fin, [6]).tolist() == [False, True, True, True] and P.mascara_excluidas(fin, []).tolist() == [False] * 4
    for f in fin:   # misma regla que engine.sane: horas de t0 = (fin-300)*1000 y de fin*1000
        hs = {pd.Timestamp((f - 300) * 1000, unit='ms', tz='UTC').hour, pd.Timestamp(f * 1000, unit='ms', tz='UTC').hour}
        for h in range(24): assert bool(P.mascara_excluidas([f], [h])[0]) == (h in hs)
def test_filtrar_y_excluidas_fallan_ruidosos_si_falta_el_fichero(tmp_path, monkeypatch):
    monkeypatch.setattr(E, 'OUT', str(tmp_path) + '/'); x = pd.DataFrame(dict(dia=['2026-11-10'] * 3, fin=[_fin(5), _fin(7), _fin(5, 58)], pnl=[1., 2., 3.]))
    x.to_pickle(tmp_path / 'RX_2026-11-10.pkl')
    with pytest.raises(FileNotFoundError): E.cargar(['2026-11-10'])          # missing != 'sin horas excluidas'
    (tmp_path / 'excl_2026-11-10.json').write_text(json.dumps(dict(dia='2026-11-10', horas_excluidas=[5])))
    assert E.cargar(['2026-11-10']).pnl.tolist() == [2.0] and E.cargar(['2026-11-10'], filtro=False).pnl.tolist() == [1., 2., 3.]
    (tmp_path / 'cov_2026-11-10.json').write_text(json.dumps(dict(binance=dict(excl_sensibilidad_R6={'15': [5, 7], '60': []}))))
    assert E.cargar(['2026-11-10'], G='15').pnl.tolist() == [] and E.cargar(['2026-11-10'], G='60').pnl.tolist() == [1., 2., 3.]
def test_vida_por_variante_mercado_lado_y_filtro(tmp_path, monkeypatch):
    c = _ctx(); c.acc('G0', D0 + 10, D0 + 110, 0); c.acc('G0', D0 + 200, D0 + 250, 0); c.acc('G0', D0, D0 + 70, 2); c.acc('DB1_150', D0, D0 + 5, 1)
    f0 = int(c.D.fin[0]); f2 = int(c.D.fin[2]); assert c.vida == {'G0': {f'ETH|{f0}|YES': 150, f'ETH|{f2}|YES': 70}, 'DB1_150': {f'ETH|{f0}|NO': 5}}
    monkeypatch.setattr(E, 'OUT', str(tmp_path) + '/'); (tmp_path / 'vida_2026-11-10.json').write_text(json.dumps(c.vida)); (tmp_path / 'excl_2026-11-10.json').write_text(json.dumps(dict(horas_excluidas=[])))
    assert E.vida_suma('2026-11-10') == {'G0': 220.0, 'DB1_150': 5.0}
    (tmp_path / 'excl_2026-11-10.json').write_text(json.dumps(dict(horas_excluidas=[0])))        # f0 = D0+300 s: apertura hora 0 -> fuera; f2 = D0+600 s tambien -> todo fuera
    assert E.vida_suma('2026-11-10') == {'G0': 0.0, 'DB1_150': 0.0}
def test_passdb_ya_no_inyecta_extra_bad_y_pasa_k_a_acc():
    assert not any('_EXTRA_BAD' in a or '_EXTRA_BAD' in b for a, b in P.REEMPL) and any('_ACC(name, t_arr, t_end, k)' in b for a, b in P.REEMPL)
def _fx(tmp_path, monkeypatch, dias, ex, rx_extra=None):
    """RT sintetico (toxicidad_thru1/out) y RX = RT filtrado (como produce la ruta nueva: sin Binance, luego filtro). Devuelve (RT por dia)."""
    monkeypatch.setattr(E, 'OUT', str(tmp_path) + '/'); (tmp_path / 'tx').mkdir(); monkeypatch.setattr(E.E1, 'TX', str(tmp_path / 'tx') + '/'); monkeypatch.setattr(E, 'QUEMADOS', dias); monkeypatch.setattr(E, 'verificar_congelados', lambda: None); monkeypatch.setattr(E.Q, 'hoy_utc', lambda: '2026-11-10')
    out = {}
    for i, d in enumerate(dias):
        fins = [_fin(5), _fin(6), _fin(7), _fin(8)]; rows = []
        for v in ('G0', 'CXJ150'):
            for j, f in enumerate(fins): rows.append(dict(**{'var': v, 'dia': d, 'fin': f, 'k': j, 'L': 0.1, 'tf': f * 1000 - 5000 - (3 if v == 'CXJ150' else 0), 'q': 5.0, 'cost': 0.5, 'pnl': -0.5 + j + (0.2 if v == 'CXJ150' else 0), 'gana': 0.0, 'act': 'ETH', 'lado': 'YES', 'pnl_nr': -0.5, 'reb': 0.0}))
        rt = pd.DataFrame(rows); out[d] = rt; rt.to_pickle(tmp_path / 'tx' / f'RT_{d}.pkl'); (tmp_path / f'excl_{d}.json').write_text(json.dumps(dict(dia=d, horas_excluidas=ex.get(d, []))))
        rx = rt.copy() if rx_extra is None else rx_extra(d, rt); rx.to_pickle(tmp_path / f'RX_{d}.pkl')
    return out
def test_aceptacion_a1_a3_pasa_con_rx_igual_a_rt_y_detecta_diferencias(tmp_path, monkeypatch):
    dias = ['2026-11-01', '2026-11-02']; ex = {'2026-11-01': [5]}                 # 11-01 pierde los mercados de la hora 5 (fin 5:05 y 5:00+... ver _fin); 11-02 sin horas excluidas
    _fx(tmp_path, monkeypatch, dias, ex); r = E.aceptacion(str(tmp_path / 'a.json'))
    assert r['checks']['A1 RX filtrado == RT filtrado (G0 y CXJ150, 10 dias, fila a fila y suma pnl)'] and r['checks']['A3 dias sin filas excluidas: RX == RT sin filtro (>=1 dia)'] and list(r['A3_dias_sin_filas_excluidas']) == ['2026-11-02']
    assert r['valores']['union_g0_n'] == 8 and r['valores']['filtrado_g0_n'] == 7 and not r['checks']['A2 G0 n=2938']        # A2 sobre el objetivo literal: n distinto -> falla (no hay tolerancia)
    # RX con una fila de mas dentro de las horas NO excluidas -> A1 falla; en un dia sin exclusiones -> A3 falla
    def extra(d, rt): return pd.concat([rt, rt[(rt['var'] == 'G0') & (rt.k == 3)].assign(tf=1)], ignore_index=True)
    _fx(tmp_path / 'x', monkeypatch, dias, ex, extra) if (tmp_path / 'x').mkdir() is None else None
    r = E.aceptacion(str(tmp_path / 'x' / 'a.json')); assert not r['checks']['A1 RX filtrado == RT filtrado (G0 y CXJ150, 10 dias, fila a fila y suma pnl)'] and not r['checks']['A3 dias sin filas excluidas: RX == RT sin filtro (>=1 dia)']
def test_aceptacion_a3_exige_al_menos_un_dia_de_control(tmp_path, monkeypatch):
    dias = ['2026-11-01']; _fx(tmp_path, monkeypatch, dias, {'2026-11-01': [5]}); r = E.aceptacion(str(tmp_path / 'a.json')); assert not r['checks']['A3 dias sin filas excluidas: RX == RT sin filtro (>=1 dia)']
# ---- test (a) con datos reales: ruta nueva (RX sin Binance + filtro) == ruta actual (Binance excluido DENTRO de la simulacion), TODAS las variantes, 10 dias quemados
REF = HERE + 'ref_ruta_actual_10nov/'
@pytest.mark.skipif(not os.path.exists(REF + 'RX_2026-11-04.pkl') or not os.path.exists(E.OUT + 'RX_2026-11-04.pkl'), reason='faltan la ruta actual de referencia o la ruta nueva producida')
def test_ruta_nueva_filtrada_igual_a_ruta_actual_todas_las_variantes_10_quemados():
    cols_num = ['k', 'L', 'q', 'tf', 'cost', 'pnl', 'pnl_nr', 'reb', 'gana', 'seg', 't_dec', 'canc']; malos = []
    for d in E.QUEMADOS:
        old = pd.read_pickle(REF + f'RX_{d}.pkl'); new = E.filtrar(pd.read_pickle(E.OUT + f'RX_{d}.pkl'), E.excluidas(d, d_ex=REF)); assert E.excluidas(d, d_ex=REF) == E.excluidas(d)
        assert set(old['var']) == set(new['var']), d
        for v in old['var'].unique():
            a = old[old['var'] == v].sort_values(['k', 'L', 'seg', 'tf']).reset_index(drop=True); b = new[new['var'] == v].sort_values(['k', 'L', 'seg', 'tf']).reset_index(drop=True)
            ok = len(a) == len(b) and all(np.allclose(a[c].astype(float), b[c].astype(float), atol=1e-9, equal_nan=True) for c in cols_num) and (a['ftype'].astype(str).values == b['ftype'].astype(str).values).all()
            if not ok: malos.append((d, v, len(a), len(b)))
    assert not malos, malos

def test_sens_r6_usa_las_horas_g15_g60_y_anota_cambio_de_signo(tmp_path, monkeypatch):
    monkeypatch.setattr(E, 'OUT', str(tmp_path) + '/'); d = '2026-11-10'; rows = []
    for v, ps in (('G0', [-1.0, -1.0]), ('DB1_150', [-1.0, 0.5])):          # mercado 0 en la hora 5 (empate con G0), mercado 1 en la hora 7: el brazo gana 1,5 solo ahi
        for j, f in enumerate((_fin(5), _fin(7))): rows.append({'var': v, 'dia': d, 'fin': f, 'k': j, 'L': 0.1, 'tf': f, 'q': 5.0, 'cost': 0.5, 'pnl': ps[j], 'pnl_nr': ps[j], 'gana': 0.0, 'act': 'ETH', 'lado': 'YES'})
    pd.DataFrame(rows).to_pickle(tmp_path / 'RX_2026-11-10.pkl'); (tmp_path / 'excl_2026-11-10.json').write_text(json.dumps(dict(horas_excluidas=[])))
    (tmp_path / 'cov_2026-11-10.json').write_text(json.dumps(dict(binance=dict(excl_sensibilidad_R6={'15': [7], '60': []}))))
    monkeypatch.setattr(E.E1, 'dser', lambda a, b: (a.groupby('k').pnl.sum() - b.groupby('k').pnl.sum()).fillna(0.0))
    r = E.sens_r6('DB1', [d], 1.5); assert r['15'] == pytest.approx(0.0) and r['60'] == pytest.approx(1.5) and r['cambio_signo'] is True      # G=15 quita el unico mercado donde el brazo gana: dPnL 0 vs +1,5
