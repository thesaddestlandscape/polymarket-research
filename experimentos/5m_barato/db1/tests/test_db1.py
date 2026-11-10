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
def test_salud_hueco_union_gt60_excluye_hora_y_cobertura():
    s = P.salud_desde_occ(_occ(), {c: 1 for c in P.COINS}, [3]); assert s['valido'] and s['horas_sanas'] == 23 and s['horas_excluidas'] == []
    s = P.salud_desde_occ(_occ([(7200, 7300)]), {c: 1 for c in P.COINS}, []); assert s['horas_excluidas'] == [1, 2] or s['horas_excluidas'] == [2]   # hueco de 100 s en la hora 2
    assert s['valido'] and 2 in s['horas_excluidas'] and s['huecos_union_gt60s'] == 1
    s = P.salud_desde_occ(_occ([(7200, 7230)]), {c: 1 for c in P.COINS}, []); assert s['huecos_union_gt60s'] == 0 and s['horas_excluidas'] == []     # 30 s: no es hueco
    o = _occ(); o['XRP'][::2] = False   # una moneda con 50 % de segundos con tick (sin hueco de union): cobertura < 0,95
    s = P.salud_desde_occ(o, {c: 1 for c in P.COINS}, []); assert not s['valido'] and s['cobertura']['XRP'] == pytest.approx(0.5, abs=0.01)
def test_salud_sin_horas_sanas_no_valido(): assert not P.salud_desde_occ(_occ(), {}, list(range(24)))['valido']
def test_sv_delta_minimo_5_comision_profundidad():
    assert P.sv_delta(4.99, 0.2, 100, 0.0) == 0.0                                  # < 5 acciones: no se puede vender
    assert P.sv_delta(5.0, 0.2, 3.0, 0.0) == 0.0                                   # profundidad visible 3 < 5
    assert P.sv_delta(5.0, 0.2, 100, 0.0) == pytest.approx(5 * (0.2 - 0.0) - 0.07 * 0.2 * 0.8 * 5)   # perdedor: vender gana 1 - fee
    assert P.sv_delta(5.0, 0.2, 100, 1.0) == pytest.approx(5 * (0.2 - 1.0) - 0.07 * 0.2 * 0.8 * 5)   # ganador: vender cuesta
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
def test_extras_burst_markout_y_salida():
    class D_(FakeD):
        def book(s, k, t): return (0.10, 0.12, 20.0, 3.0)
    D = D_(); C = pd.DataFrame(dict(tx=['t1', 't2'], li=[1, 2], bloque=[7, 7], taker=['A', 'B'], side=[0, 0], kidx=[0, 0], pr=[0.1, 0.1], sz=[5.0, 5.0], ts_ms=[0, 0]))
    R = pd.DataFrame(dict(var=['G0'], dia=['2026-11-10'], act=['ETH'], lado=['YES'], fin=[D0 // 1000 + 300], k=[0], L=[0.10], q=[5.0], tf=[D0 + 100], gana=[0.0], cost=[0.5], pnl=[0.0]))
    ns = dict(D=D, _TPX=pd.DataFrame(dict(k=[0, 0], tx=['t1', 't2'], log_index=[1, 2], tm=[D0 + 100, D0 + 100]))); R = P.extras(ns, R, C)
    assert bool(R.burst[0]) and bool(R.burst_known[0]) and R.mk1[0] == pytest.approx(0.01) and R.sv150[0] == pytest.approx(5 * 0.10 - 0.07 * 0.1 * 0.9 * 5) and R.pnl_nr[0] == pytest.approx(5 * (0.0 - 0.1))
    C1 = C.iloc[:1]; R2 = P.extras(ns, R.drop(columns=[c for c in R.columns if c in ('burst', 'burst_known')]).copy(), C1); assert not bool(R2.burst[0]) and bool(R2.burst_known[0])   # un solo tomador: no es rafaga
    R3 = P.extras(ns, R.copy(), None); assert not bool(R3.burst[0]) and not bool(R3.burst_known[0])    # sin on-chain: desconocido, no 'no rafaga' confirmada
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
    assert E.veredicto_cp(m, 20, dict(pl, p=0.5), None)[0] == 'REFUTA'   # checkpoint 20 sin CANDIDATO = REFUTA terminal
def test_rmr_fraccion_cancelable():
    R = _R(); r = E.rmr(R); assert r['G0']['n'] == 80 and r['DB1_150']['n'] == 60 or r['DB1_150']['n'] <= r['G0']['n']
    assert 0 <= r['DB1_150']['fraccion_cancelable'] <= 1
def test_markout_precision_recobrado():
    R = _R(); o = E.markout_salida(R, arms=('G0',)); assert o['G0']['mk1']['marcados'] == 400 and o['G0']['mk1']['precision'] == pytest.approx(float((R[R['var']=='G0'].gana == 0).mean())) and o['G0']['mk1']['recobrado'] == 1.0
def test_seguridad_dry_run_sin_envio_ni_secretos():
    src = open(HERE + 'passdb.py').read() + open(HERE + 'eval_db1.py').read()
    for prohibido in ('py_clob_client', 'post_order', 'create_order', '.env', 'private_key', 'PRIVATE_KEY', 'requests.post', 'sign_order', 'enviar_orden'): assert prohibido not in src.replace('SOLO lectura', ''), prohibido
