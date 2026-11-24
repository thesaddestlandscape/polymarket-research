"""test_rf5_fronteras.py -- ADENDA_RF5_INTERINA_24nov sec.6 (Pocock-LD, mirada 1 en el 6.o dia valido, final en el 10.o, K_max 500 (K1-K4) / 500 (A) / 1500 (K6) (ADENDA_RF5_NULO_INCREMENTAL), IC t por dias) y su cableado en rf5_eval / rf5_nulo_run. Datos sinteticos; no lee datos reales ni dias >= 18-Nov."""
import os, sys, json
import numpy as np, pandas as pd, pytest
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
os.environ.setdefault('RF5_OUT', '/tmp/rf5_test_fronteras/'); os.makedirs('/tmp/rf5_test_fronteras/', exist_ok=True)
import rf5_fronteras as FR, rf5_eval as EV, rf5_core as K5

def _est(n_validos, extra=None):
    e = {f'2026-12-{i + 1:02d}': dict(status='COMPLETE', iv=True, iii='OK') for i in range(n_validos)}; e.update(extra or {}); return e

def test_constantes_transcritas_de_la_adenda_y_t_de_student():
    u1, u2 = FR.UMBRAL[1], FR.UMBRAL[2]
    assert (u1['p_max_K1_K4'], u2['p_max_K1_K4']) == (0.02834, 0.02171) and (u1['K6_alfa001'], u2['K6_alfa001']) == (0.00709, 0.00470) and (u1['K6_alfa005'], u2['K6_alfa005']) == (0.03543, 0.02792)
    assert (u1['p_max_A'], u2['p_max_A']) == (0.03543, 0.02792) and (u1['vs_azar'], u2['vs_azar']) == (0.0709, 0.0617) and FR.K_MAX == {'K': 500, 'A': 500, 'K6': 1500} and FR.SEMILLA == 20261124 and FR.H_BC == 20
    from scipy import stats
    assert stats.t.ppf(1 - u1['ic_unil'], 5) == pytest.approx(FR.T_MULT[1], abs=1e-3) and stats.t.ppf(1 - u2['ic_unil'], 9) == pytest.approx(FR.T_MULT[2], abs=1e-3)

def test_resolucion_besag_clifford_K_max_cubre_5_sobre_umbral():
    for fam in ('K1_K4', 'A'):
        for m in (1, 2): assert FR.resolucion_ok(fam, m)
    assert FR.resolucion_ok('K6', 2, 0.01) and FR.resolucion_ok('K6', 2, 0.01, k=1500) and not FR.resolucion_ok('K6', 2, 0.01, k=1000)      # K6 final a 0,01 exige >= 1064 (por eso K_max=1500)
    with pytest.raises(ValueError): FR.umbral_p('K6', 1, 0.02)

def test_decide_mirada_6_primeros_validos_y_10():
    assert FR.decide_mirada(_est(5))['mirada'] == 0
    d = FR.decide_mirada(_est(6)); assert d['mirada'] == 1 and len(d['dias']) == 6
    d = FR.decide_mirada(_est(8)); assert d['mirada'] == 1 and d['dias'] == sorted(_est(8))[:6]                           # entran EXACTAMENTE los 6 primeros aunque haya mas
    d = FR.decide_mirada(_est(12)); assert d['mirada'] == 2 and d['dias'] == sorted(_est(12))[:10]

def test_no_se_mira_con_un_dia_anterior_pendiente_ni_cuenta_incomplete():
    e = _est(6, {'2026-11-30': dict(status='PENDING')}); assert FR.decide_mirada(e)['mirada'] == 0 and FR.decide_mirada(e)['nombre'] == 'ESPERA_PENDIENTES'
    e = _est(6, {'2026-11-30': dict(status='INCOMPLETE'), '2026-11-29': dict(status='COMPLETE', iv=False, iii='OK')}); d = FR.decide_mirada(e); assert d['mirada'] == 1 and '2026-11-30' not in d['dias']      # terminales no validos no bloquean ni cuentan
    e = _est(6, {'2026-11-30': dict(status='COMPLETE', iv=None, iii='OK')}); assert FR.decide_mirada(e)['mirada'] == 0                      # desenlace aun sin cerrar (D+3)
    e = _est(6, {'2026-12-20': dict(status='PENDING')}); assert FR.decide_mirada(e)['mirada'] == 1                                         # un pendiente POSTERIOR no bloquea

def test_ic_t_dias_nivel_unilateral_y_nan():
    v = [0.1, 0.12, 0.08, 0.11, 0.09, 0.13]; mu, lo, hi = FR.ic_t_dias(v, 1); s = np.std(v, ddof=1); assert mu == pytest.approx(np.mean(v)) and lo == pytest.approx(mu - 2.2876 * s / np.sqrt(6), abs=1e-4)
    assert np.isnan(FR.ic_t_dias([0.1], 1)[1]) and np.isnan(FR.ic_t_dias([0.5, 0.5, 0.5], 1)[1])

def test_veredicto_A_usa_umbral_de_la_mirada_y_no_refuta_en_mirada_1():
    C = K5.lee_cortes(); a = dict(delta=0.1, ic90_dias=[0.05, 0.2], ic_dias_t=[0.02, 0.2], ic_cierres=[0.01, 0.2], nulo_exacto=True, p_max_global=0.03, pct_dias_pos=5 / 6, delta_sin_2_mejores_dias=0.05, delta_inversion=-0.1, p_azar=0.05)
    ok = dict(ok_banda=True)
    v1, c1 = EV.veredicto_A('F3', a, ok, C, True, None, dict(estado='OK_HUECOS'), 1); assert v1 == 'CONFIRMADA' and c1['p_max_le_umbral']                      # 0,03 <= 0,03543 en la mirada 1
    v2, c2 = EV.veredicto_A('F3', a, ok, C, True, None, dict(estado='OK_HUECOS'), 2); assert v2 != 'CONFIRMADA' and not c2['p_max_le_umbral']                # 0,03 > 0,02792 en la final
    peor = dict(a, ic_dias_t=[-0.01, 0.2]); assert EV.veredicto_A('F3', a, ok, C, True, peor, dict(estado='OK_HUECOS'), 1)[0] != 'CONFIRMADA'
    m = dict(a, delta=-0.1, ic90_dias=[-0.3, -0.01], ic_dias_t=[-0.3, -0.01], ic_cierres=[-0.3, -0.01]); assert EV.veredicto_A('F3', m, ok, C, True, None, None, 1)[0] == 'ACUMULANDO'            # nunca REFUTADA en la mirada 1
    assert EV.veredicto_A('F3', m, ok, C, True, None, None, 2)[0] == 'REFUTADA' and EV.veredicto_A('F3', dict(m, ic90_dias=[-0.3, 0.1]), ok, C, True, None, None, 2)[0] == 'NO_CONFIRMADA_A_10'
    d4 = dict(a, pct_dias_pos=0.5); assert not EV.veredicto_A('F3', d4, ok, C, True, None, dict(estado='OK_HUECOS'), 1)[1]['dias_pos'] and EV.veredicto_A('F3', dict(a, pct_dias_pos=4 / 6), ok, C, True, None, dict(estado='OK_HUECOS'), 1)[1]['dias_pos']

def test_resumen_conteos_con_5_y_modo_final_con_10(tmp_path):
    import test_rf5 as T
    for n, modo in ((5, 'SOLO_CONTEOS'), (6, 'MIRADA_1')):
        R, F, est = T._sint(n_dias=n); out = str(tmp_path) + f'/{n}/'; os.makedirs(out)
        for d in est: R[R.dia == d][R.columns].pipe(lambda x: x[x.pol.isin(['base', 'F1', 'F2', 'F3', 'U13'])]).to_pickle(out + f'rf5A_{d}.pkl'); F[F.dia == d].to_pickle(out + f'rf5_f5_0_{d}.pkl')
        r = EV.resumen(out, est, K5.lee_cortes(), replicas=lambda dias: {}); assert r['modo'].startswith(modo), r['modo']
        if n == 6: assert r['mirada_decision']['mirada'] == 1 and set(r['familia_A']) == {'F1', 'F2', 'F3', 'U13'} and r['familia_A_global']['umbral_p'] == 0.03543 and r['nulo_resimulado'] == dict(A=None, K=None)

def test_nulo_resim_se_ignora_si_los_dias_no_coinciden(tmp_path):
    out = str(tmp_path) + '/'; dias = ['a', 'b']; json.dump(dict(dias=dias, mirada=1, estado='NULO_RESIMULADO_EXACTO', p_max=0.01), open(out + 'nulo_A_resultado.json', 'w'))
    assert EV.lee_nulo(out, 'A', dias, 1)['p_max'] == 0.01 and EV.lee_nulo(out, 'A', ['a', 'c'], 1) is None and EV.lee_nulo(out, 'A', dias, 2) is None and EV.lee_nulo(out, 'K', dias, 1) is None

def test_familia_A_con_nulo_resimulado_sustituye_p_y_marca_exacto():
    import test_rf5 as T
    R, F, est = T._sint(6); a = EV.familia_A(R, F, K5.lee_cortes(), K=20, mirada=1, nulo_resim=dict(p_max=0.0123, estado='NULO_RESIMULADO_EXACTO'))
    assert a['p_max_global'] == 0.0123 and a['nulo_exacto'] is True and a['F3']['ic_dias_t'][0] == a['F3']['ic_dias_t'][0] and 'ic_cierres' in a['F3']

def test_registro_cubre_ficheros_externos_y_falla_cerrado(tmp_path, monkeypatch):
    """adenda interina sec.4 cond.1: el runner comprueba al arrancar TAMBIEN los ficheros de fuera de re_f5_23nov (b_policy_sim, engine_v4/passT_v4, replay_variantes, prep_day, puerta0_run...); falta/sha distinto/no registrado => problema."""
    import rf5_run as RR, hashlib
    assert any(n.endswith('b_policy_sim.py') for n in RR.FICH_EXT) and any(n.endswith('engine_v4.py') for n in RR.FICH_EXT) and any(n.endswith('passT_v4.py') for n in RR.FICH_EXT) and any(n.endswith('replay_variantes.py') for n in RR.FICH_EXT)
    assert any(n.startswith('DEV:') and n.endswith('prep_day.py') for n in RR.FICH_EXT) and any(n.endswith('puerta0_run.py') for n in RR.FICH_EXT) and any(n.endswith('cron_pesado.sh') for n in RR.FICH_EXT)
    assert all(os.path.exists(RR.ruta_ext(n)) for n in RR.FICH_EXT)                                      # todo lo externo existe hoy
    monkeypatch.setattr(RR, 'FICH_EXT', ('EXT:a.py', 'EXT:b.py', 'EXT:c.py')); monkeypatch.setattr(RR, 'REPO_', str(tmp_path) + '/'); monkeypatch.setattr(RR, 'FICH_REG', ()); monkeypatch.setattr(RR, 'sha', lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest())
    (tmp_path / 'a.py').write_text('1'); (tmp_path / 'b.py').write_text('2'); monkeypatch.setattr(RR, 'PREREG_RF5_SHA', hashlib.sha256(open(RR.PREREG_RF5, 'rb').read()).hexdigest())
    h = tmp_path / 'H.txt'; h.write_text(f"{hashlib.sha256(b'1').hexdigest()}  {RR.nombre_ext('EXT:a.py')}\n{'0' * 64}  {RR.nombre_ext('EXT:b.py')}\n"); monkeypatch.setattr(RR, 'HASHES', str(h)); p = RR.verifica_registro()
    assert any('EXT:b.py sha !=' in x for x in p) and any('EXT:c.py no existe' in x for x in p) and not any('EXT:a.py' in x for x in p)


def test_la_mirada_espera_si_faltan_replicas_del_nulo(tmp_path):
    import test_rf5 as T
    R, F, est = T._sint(n_dias=6); out = str(tmp_path) + '/'
    r = EV.resumen(out, est, K5.lee_cortes(), replicas=lambda dias: {'K': {dias[-1]: 1}}); assert r['modo'].startswith('ESPERA_NULO_INCREMENTAL') and r['replicas_faltan'] == {'K': {sorted(est)[5]: 1}}
    assert 'familia_A' not in r and 'conteos' not in r and 'veredictos_K' not in r                       # ni se abrieron los pkl (out vacio: de abrirlos habria fallado/precintado)
    import rf5_nulo_inc as NI, rf5_run as RR
    RR_out = RR.OUT; RR.OUT = str(tmp_path) + '/vacio/'; os.makedirs(RR.OUT + 'nulo_inc/')
    try: f = EV.replicas_faltan(sorted(est)[:6]); assert set(f) == {'K', 'K6', 'A'} and all(f[k][sorted(est)[0]] == FR.k_max(k) for k in f)
    finally: RR.OUT = RR_out
