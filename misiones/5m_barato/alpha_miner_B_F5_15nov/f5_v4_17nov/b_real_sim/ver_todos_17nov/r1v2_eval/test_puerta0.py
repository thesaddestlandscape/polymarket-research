#!/usr/bin/env python3
"""test_puerta0.py -- pruebas de la FASE A (Puerta 0) de R1v2 con fixtures diminutos (sin datos de produccion, sin red). Ejecutar: python3 test_puerta0.py"""
import sys, os, json, tempfile, shutil
import numpy as np, pandas as pd
import subprocess
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; V = os.path.dirname(HV.rstrip('/')) + '/'; BSIM = os.path.dirname(V.rstrip('/')) + '/'
TMP = tempfile.mkdtemp(prefix='p0_test_'); os.environ['P0_OUT'] = TMP + '/out/'; os.environ['P0_K'] = '300'
sys.path.insert(0, HV); sys.path.insert(0, V + 'r1v2_sec7/'); sys.path.insert(0, BSIM)
import puerta0_core as P0, sec7_core as C, sec7_calculos as K
nan = float('nan')
T0 = 1_000_000
def S(rows, dlag=20):
    a = np.array(rows, float); return C.SerieL1(a[:, 0], a[:, 0] - dlag, a[:, 1], a[:, 2], a[:, 3], a[:, 4])
def mk(rows):
    """rows: (dia, tercil, q, L, gana) -> DataFrame de ordenes con las columnas de run_day/anota."""
    R = pd.DataFrame(rows, columns=['dia', 'tercil', 'q', 'L', 'gana']); n = len(R)
    R['mid'] = [f'm{i}' for i in range(n)]; R['lado'] = 'YES'; R['coin'] = 'eth'; R['k'] = range(n); R['t_arr'] = 1000 + np.arange(n); R['tf'] = np.where(R.q > 0, R.t_arr + 5, -1); R['t_dec'] = 1792454700000 + np.arange(n)
    R['cost'] = R.q * R.L; R['pnl'] = R.q * (R.gana - R.L); R['tercil_ex'] = R.tercil; R['canal'] = ''; R['bloq'] = 0; return R

def test_unidad_primer_relleno_anula_extras():
    R = mk([('d1', 'bajo', 5, 0.2, 1), ('d1', 'bajo', 5, 0.2, 0)]); R['mid'] = 'mA'; R.loc[1, 't_arr'] = 5000; R.loc[1, 'tf'] = 5005
    U = P0.unidad_primer_relleno(R); assert U.attrs['extra_rellenos'] == 1 and list(U.q) == [5.0, 0.0] and U.cost.sum() == 1.0 and U.pnl.sum() == 5 * 0.8
    U2 = P0.unidad_primer_relleno(mk([('d1', 'alto', 5, 0.2, 1), ('d1', 'alto', 0, 0.2, 1)])); assert U2.attrs['extra_rellenos'] == 0 and len(U2) == 2
    assert P0.unidad_primer_relleno(mk([('d1', 'alto', 5, 0.2, 1)]).iloc[0:0]).attrs['extra_rellenos'] == 0

def test_rebate_aritmetica():
    R = mk([('d1', 'bajo', 10, 0.20, 0)]); assert abs(P0.con_rebate(R, 0.0).iloc[0] - R.pnl.iloc[0]) < 1e-12
    assert abs(P0.con_rebate(R, 0.2).iloc[0] - (R.pnl.iloc[0] + 0.2 * 0.07 * 0.2 * 0.8 * 10)) < 1e-12          # 0,2 del fee del tomador por accion, solo sobre q
    assert P0.con_rebate(mk([('d1', 'bajo', 0, 0.2, 1)]), 0.2).iloc[0] == 0.0                                  # sin relleno no hay rebate

def test_ev_ponderado_por_euro_y_incondicional():
    R = mk([('d1', 'bajo', 10, 0.10, 1), ('d1', 'medio', 10, 0.90, 0), ('d1', 'alto', 0, 0.2, 1), ('d1', 'alto', 5, 0.5, 0)]); R['pnl_x'] = R.pnl
    g = P0.agrega_dia(R); bm = P0.resumen_grupo(g, 'bm'); al = P0.resumen_grupo(g, 'alto')
    assert bm['n_ordenes'] == 2 and bm['n_rellenos'] == 2 and abs(bm['EV_eur'] - (9.0 - 9.0) / (1.0 + 9.0)) < 1e-12        # (+9 -9)/(1+9): ponderado por EUR, no media de ratios (+9 y -1 -> +4)
    assert al['n_ordenes'] == 2 and al['n_rellenos'] == 1 and abs(al['EV_eur'] + 1.0) < 1e-12 and abs(al['p_relleno'] - 0.5) < 1e-12 and abs(al['pnl_por_orden'] + 1.25) < 1e-12   # incondicional: no relleno cuenta como orden con pnl 0

def test_celdas_validas_y_sha():
    rows = []
    for d, n_lo, n_hi, n_ind, n_sin in (('d1', 20, 4, 0, 5), ('d2', 12, 12, 0, 0), ('d3', 10, 5, 0, 0), ('d4', 23, 0, 1, 0)):
        k = 0
        for c, n in (('lo', n_lo), ('hi', n_hi), ('indet', n_ind), ('sin_datos', n_sin)):
            for _ in range(n): rows.append((d, 'ETH', k, c)); k += 1
    t = pd.DataFrame(rows, columns=['dia', 'coin', 'w0_ms', 'clase_estrato']); t['coin'] = t.coin.str.lower(); c = P0.celdas_validas(t).set_index('dia')
    assert c.loc['d1', 'valida'] and c.loc['d1', 'n_clas'] == 24 and c.loc['d1', 'sin_datos'] == 5          # sin_datos no se clasifica ni se imputa
    assert c.loc['d2', 'valida'] and c.loc['d2', 'frac_lo'] == 0.5                                           # justo en el borde (>=0,5, >=24)
    assert not c.loc['d3', 'valida']                                                                          # n_clas=15 <24
    assert c.loc['d4', 'valida'] and c.loc['d4', 'indet'] == 1
    cel = pd.DataFrame(dict(dia=['a', 'a', 'a', 'b', 'b', 'b'], coin=['eth', 'sol', 'xrp'] * 2, valida=[True, True, True, True, False, True])); r = P0.dias_lo_validos(cel); assert r['todas_las_monedas'] == ['a'] and r['alguna_moneda'] == ['a', 'b']
    p = TMP + '/t.csv'; open(p, 'w').write('dia,coin,w0_ms,clase_estrato\nd,ETH,1,lo\n')
    try: P0.lee_tabla_suelo(p); assert False
    except ValueError: pass
    assert len(P0.lee_tabla_suelo(V + 'cierre_limites_19nov/tabla_suelo_ventanas_19nov.csv')) == 39744                 # la tabla firmada real cuadra con su sha

def test_anota_suelo_ventana_y_sin_tabla():
    w0 = 1792454700000; R = mk([('2026-10-20', 'bajo', 5, 0.2, 1), ('2026-10-20', 'alto', 5, 0.2, 1), ('2026-10-20', 'alto', 5, 0.2, 1)])
    R['t_dec'] = [w0 + 299999, w0 + 300000, w0 + 10_000_000]; R['coin'] = 'ETH'
    tab = pd.DataFrame(dict(dia='2026-10-20', coin='eth', w0_ms=[w0, w0 + 300000], clase_estrato=['lo', 'hi'])); cel = pd.DataFrame(dict(dia=['2026-10-20'], coin=['eth'], valida=[True]))
    A = P0.anota_suelo(R, tab, cel); assert list(A.estrato) == ['lo', 'hi', 'sin_tabla'] and list(A.celda_valida) == [True, True, True]
    A2 = P0.anota_suelo(R.assign(dia='2026-10-21'), tab, cel); assert set(A2.estrato) == {'sin_tabla'} and not A2.celda_valida.any()      # sin fila: no se imputa

def test_bootstrap_por_dias_determinista_e_insufficient():
    rows = [(f'd{i}', t, 5, 0.3, g) for i in range(8) for t, g in (('bajo', 1), ('medio', 1), ('alto', 0), ('alto', 0))]; R = mk(rows); R['pnl_x'] = R.pnl; g = P0.agrega_dia(R)
    a = P0.boot_diff(g, np.random.default_rng(1), 500); b = P0.boot_diff(g, np.random.default_rng(1), 500); assert a == b and a['n_dias'] == 8
    ev_bm = (5 * 0.7) / (5 * 0.3); assert abs(a['diff'] - (ev_bm - (-1.0))) < 1e-9 and a['lo'] > 0                                   # dias identicos: IC estrecho alrededor de la diferencia exacta
    assert P0.boot_diff(g[g.dia == 'd0'], np.random.default_rng(1), 50)['nota'].startswith('INSUFFICIENT')
    assert P0.sin_mejores_dias(g)['n_dias'] == 6

def test_veredicto_pasa_nopasa_insufficient():
    d = dict(diff=0.2, lo=0.05, hi=0.4); assert P0.veredicto_puerta0(-0.1, d) == 'PASA'
    assert P0.veredicto_puerta0(0.05, d) == 'NO_PASA'                                                                          # EV(alto) > 0 => falla aunque la diferencia sea positiva
    assert P0.veredicto_puerta0(-0.1, dict(diff=0.2, lo=-0.01, hi=0.4)) == 'NO_PASA'
    assert P0.veredicto_puerta0(-0.1, dict(diff=nan, lo=nan, hi=nan)) == 'INSUFFICIENT'

def test_estres_none_coincide_con_sec7_y_es_uniforme():
    rows = [('d1', t, q, L, g) for t, q, L, g in (('bajo', 5, 0.2, 1), ('bajo', 0, 0.2, 1), ('medio', 5, 0.15, 0), ('alto', 5, 0.25, 0), ('alto', 0, 0.25, 1), ('alto', 5, 0.18, 1))]; R = mk(rows)
    ref = K.estres_none(R, tasa=0.018, ev_none=-0.115)
    out = P0.evalua(R, ['d1'], None, 0.0, 'central', K=20)
    assert abs(out['por_tercil']['alto']['EV_eur'] - ref['alto']['EV_con_estres']) < 1e-12 and abs(out['por_tercil']['bajo']['EV_eur'] - ref['bajo']['EV_con_estres']) < 1e-12
    base = P0.evalua(R, ['d1'], None, 0.0, 'sin', K=20); assert abs(base['por_tercil']['alto']['EV_eur'] - ref['alto']['EV_visible']) < 1e-12 and base['etiqueta'].startswith(P0.ETIQUETA)
    assert out['alto']['pnl'] < base['alto']['pnl']                                                                            # EV NONE negativo: solo resta

def test_auc_y_test_fuga_nan():
    assert P0.auc([0, 0, 1, 1], [0, 0, 1, 1])[0] == 1.0 and P0.auc([1, 1, 0, 0], [0, 0, 1, 1])[0] == 0.0 and P0.auc([1, 1, 1, 1], [0, 1, 0, 1])[0] == 0.5 and np.isnan(P0.auc([1, 2], [1, 1])[0])
    rng = np.random.default_rng(5); n = 400
    def dia(d, leak):
        y = rng.integers(0, 2, n); inv = (rng.random(n) < (0.1 + 0.6 * y * leak)); R = mk([(d, 'inval' if inv[i] else 'bajo', 5, 0.2, int(y[i])) for i in range(n)]); return R
    ok = pd.concat([dia('d1', 0), dia('d2', 0)]); r = P0.test_fuga_nan(ok); assert r['estado'] == 'OK' and r['dias_evaluables'] == 2
    leak = pd.concat([dia('d1', 1), dia('d2', 1)]); r = P0.test_fuga_nan(leak); assert r['estado'] == 'FUGA_SOSPECHOSA'          # NaN-si-no-hay-datos que predice el desenlace se detecta
    few = mk([('d1', 'inval', 5, 0.2, 1), ('d1', 'bajo', 5, 0.2, 0)]); assert P0.test_fuga_nan(few)['estado'] == 'INSUFFICIENT'      # sin n suficiente no se cierra nada

def test_pct_invalido_y_cambio_tercil():
    R = mk([('d1', 'bajo', 5, 0.2, 1), ('d1', 'inval', 5, 0.2, 0), ('d1', 'alto', 0, 0.2, 1), ('d1', 'inval', 0, 0.2, 1)]); R.loc[2, 'tercil_ex'] = 'medio'
    p = P0.pct_invalido(R)['todas']; assert p['n_inval'] == 2 and p['pct_inval'] == 0.5 and p['n_rellenos_inval'] == 1 and abs(p['EV_eur_inval'] + 1.0) < 1e-12
    c = P0.cambio_tercil(R); assert c['n_validas_ambas'] == 2 and c['frac_cambia'] == 0.5 and not c['ok']

def test_f5_ex_usa_reloj_exchange_y_no_imputa():
    s = C.SerieL1([T0 + 100, T0 + 900], [T0 + 50, T0 + 600], [0.2, 0.2], [0.3, 0.3], [1, 1], [np.expm1(C.C0), np.expm1(C.C1) + 1], 0)
    assert C.f5t(s, T0 + 700) is not None and abs(C.f5t(s, T0 + 700) - C.C0) < 1e-6                 # rx<=t: solo la 1.a fila (la 2.a llega en T0+900)
    assert P0.f5_ex(s, T0 + 700) > C.C1                                                              # exchange<=t ya ve la 2.a (ex T0+600): por eso es solo la metrica de cambio, nunca decision
    assert P0.f5_ex(s, T0) is None and P0.f5_ex(None, T0) is None and P0.f5_ex(s, T0 + 60000) is None
    R = mk([('d1', 'bajo', 0, 0.2, 1)]); R['t_dec'] = T0 + 700; A = P0.anota_ex(R, lambda k: s, C.tercil); assert A.tercil_ex.iloc[0] == 'alto'

def test_dry_un_mercado_politica_real_con_stub():
    import test_b_real_sim as TB, b_policy_sim as BS
    t0 = TB.T0; ru = [(t0 - 400000, 0.22, 0.24)]; rd = [(t0 - 400000, 0.70, 0.72)]
    own = S([(t0 - 20000, 0.22, 0.24, 50, np.expm1(C.C0 - 0.5))]); comp = S([(t0 - 20000, 0.70, 0.72, 30, 30)])
    st = TB.Stub([('eth', ru, rd)], prints={0: [(t0 + 20000, 0.19)]}); W = C.EngineBloqueo(st, activo=False, fuente=lambda k: (own, comp) if k == 0 else (None, None))
    BS.G.capt_outcome = lambda E, k: E.capt.outcome(E.D, k); R, cov = BS.run_day('x', TB.P0, E=W); R['dia'] = '2026-11-05'
    R = C.anota_ordenes(R, W, lambda k: own if k == 0 else comp); R = P0.anota_ex(R, lambda k: own if k == 0 else comp, C.tercil); R['bloq'] = 0
    U = P0.unidad_primer_relleno(R); assert (U.q > 0).sum() == 1 and U.attrs['extra_rellenos'] == 0 and (U.tercil == 'bajo').all()
    out = P0.evalua(U, ['2026-11-05'], None, 0.0, 'sin', K=10); assert out['bm']['n_rellenos'] == 1 and out['alto']['n_ordenes'] == 0 and out['diff_ic90_dias']['n_dias'] == 1 and out['veredicto_bruto'] == 'INSUFFICIENT'

def fake_dia_pkl(RU, d, n=40, seed=1, leak=False):
    rng = np.random.default_rng(seed); rows = []
    for i in range(n):
        g = int(rng.integers(0, 2)); tc = str(rng.choice(['bajo', 'medio', 'alto', 'inval']))
        if leak: tc = 'inval' if (g == 1 and rng.random() < 0.8) else str(rng.choice(['bajo', 'medio', 'alto']))
        rows.append((d, tc, float(rng.choice([0, 5])), float(rng.choice([0.12, 0.2])), g))
    R = mk(rows); R['mid'] = [f'{d}_m{i}' for i in range(n)]; R['n_ord'] = 0; R['coin'] = rng.choice(['eth', 'sol', 'xrp'], n); R['t_dec'] = 1793750400000 + 300000 * rng.integers(0, 288, n)
    R = pd.concat([R.assign(bloq=0), R.assign(bloq=1)], ignore_index=True); return R
def test_runner_final_idempotente_checkpoint_y_dias_quemados():
    PR = fresh('runner')
    RU = PR.RU; assert RU.OUT == PR.OUT and PR.OUT.startswith(TMP)
    for d in PR.DIAS[:3]:                                                                                       # 03,04,05-Nov (03 y 04 quemados)
        def fn(dd, d=d): R = fake_dia_pkl(RU, d); PR.atomic_pkl(PR.OUT + f'p0_ordenes_{d}.pkl', R); PR.atomic_json(PR.OUT + f'p0_cov_{d}.json', dict(ok=1)); return dict(ok=1), dict(ok=1)
        assert RU.job('dia', d, [f'p0_ordenes_{d}.pkl', f'p0_cov_{d}.json'], fn, {'x': HV + 'puerta0_core.py'}) == 'COMPLETE'
    assert PR.final() == 'PARTIAL'                                                                              # 9 dias sin hacer => PARTIAL, nunca COMPLETE
    m = json.load(open(PR.OUT + 'run_manifest.json')); r = json.load(open(PR.OUT + 'puerta0_resultado.json'))
    assert m['status'] == 'PARTIAL' and m['estado_por_dia']['2026-11-09'] == 'MISSING' and m['code']['puerta0_core.py'] and m['prereg']['PREREG_R1v2_19nov.md'].startswith('48fe638e')
    k = 'bloq0|A_confirmatorio_05_09|reb0.0|estres_sin|estrato_todos'; assert r['rejilla'][k]['dias'] == ['2026-11-05'] and r['rejilla'][k.replace('A_confirmatorio_05_09', 'POSTHOC_todos_los_dias')]['dias'] == PR.DIAS[:3]
    assert len(r['rejilla']) == 2 * 3 * 2 * 3 * 6 and len(r['combinado']) == 3 * 2 * 3 * 6 and r['cobertura']['bloq0']['extra_rellenos_anulados'] == 0 and 'fuga_nan' in r['validez']
    sha1 = PR.sha(PR.OUT + 'puerta0_resultado.json'); PR.final(); assert PR.sha(PR.OUT + 'puerta0_resultado.json') == sha1                       # idempotente: mismo resultado, mismas filas
    open(PR.OUT + 'p0_ordenes_2026-11-05.pkl', 'ab').write(b'x'); PR.final(); assert json.load(open(PR.OUT + 'run_manifest.json'))['estado_por_dia']['2026-11-05'].startswith('FAILED')       # checkpoint corrupto detectado
    assert RU.job('dia', '2026-11-05', ['p0_ordenes_2026-11-05.pkl', 'p0_cov_2026-11-05.json'], fn, {'x': HV + 'puerta0_core.py'}) == 'COMPLETE'                          # y se reanuda en ese dia


# ============================== code-review 3: un test por hallazgo
import subprocess
def fresh(sub):
    import puerta0_run as PR
    PR.OUT = TMP + f'/{sub}/'; PR.RU.OUT = PR.OUT; os.makedirs(PR.OUT, exist_ok=True); return PR
def llena(PR, dias, **kw):
    for d in dias:
        def fn(dd, d=d): R = fake_dia_pkl(PR.RU, d, **kw.get(d, {})); PR.atomic_pkl(PR.OUT + f'p0_ordenes_{d}.pkl', R); PR.atomic_json(PR.OUT + f'p0_cov_{d}.json', dict(ok=1)); return dict(ok=1), dict(ok=1)
        assert PR.RU.job('dia', d, [f'p0_ordenes_{d}.pkl', f'p0_cov_{d}.json'], fn, {'x': HV + 'puerta0_core.py'}) == 'COMPLETE'
def celda(diff, lo, ev_alto, n_dias=7, bruto=None):
    v = P0.veredicto_puerta0(ev_alto, dict(diff=diff, lo=lo, hi=1)); return dict(diff_ic90_dias=dict(diff=diff, lo=lo, hi=1.0, n_dias=n_dias), alto=dict(EV_eur=ev_alto), veredicto_bruto=bruto or v)
def test_h1_fuga_bloquea_todas_las_celdas():
    c = celda(0.2, 0.1, -0.1); assert P0.veredicto_combinado(c, c, 10, 'FUGA_SOSPECHOSA')['veredicto'] == 'BLOCKED_FUGA' and P0.veredicto_combinado(c, c, 10, 'OK')['veredicto'] == 'PASA'
    PR = fresh('h1'); llena(PR, PR.DIAS, **{d: dict(n=300, leak=True) for d in PR.DIAS}); PR.final(); r = json.load(open(PR.OUT + 'puerta0_resultado.json'))
    assert r['validez']['fuga_nan']['estado'] == 'FUGA_SOSPECHOSA' and r['veredicto_oficial']['veredicto'] == 'BLOCKED_FUGA' and {v['veredicto'] for v in r['combinado'].values()} == {'BLOCKED_FUGA'}
def test_h2_fuga_decisoria_solo_dias_confirmatorios():
    PR = fresh('h2'); llena(PR, PR.DIAS, **{'2026-11-03': dict(n=300, leak=True), '2026-11-04': dict(n=300, leak=True), **{d: dict(n=300, seed=7) for d in PR.DIAS[2:]}}); PR.final(); r = json.load(open(PR.OUT + 'puerta0_resultado.json'))['validez']
    assert r['fuga_nan']['estado'] == 'OK' and r['fuga_nan']['decisorio_dias'] == PR.DIAS[2:] and r['fuga_nan_posthoc_03_04']['bloq0']['estado'] == 'FUGA_SOSPECHOSA'          # 03-04 fugan pero solo se publican aparte
    assert {x['dia'] for x in r['fuga_nan']['bloq0']['por_dia']} == set(PR.DIAS[2:]) and {x['dia'] for x in r['fuga_nan_posthoc_03_04']['bloq0']['por_dia']} == set(PR.DIAS[:2])
def test_h3_veredicto_combinado_bloq0_y_bloq1_mismo_signo():
    ok = celda(0.2, 0.1, -0.1); V = P0.veredicto_combinado
    assert V(ok, ok, 10, 'OK')['veredicto'] == 'PASA'
    assert V(ok, celda(-0.05, -0.2, -0.1), 10, 'OK')['veredicto'] == 'NO_PASA'                     # bloq1 con signo contrario
    assert V(ok, celda(0.2, 0.1, 0.05), 10, 'OK')['veredicto'] == 'NO_PASA'                         # bloq1 con EV_alto > 0
    assert V(celda(0.2, -0.1, -0.1), ok, 10, 'OK')['veredicto'] == 'NO_PASA'                        # bloq0 no pasa (IC cruza 0)
    assert V(ok, None, 10, 'OK')['veredicto'] == 'INSUFFICIENT' and V(ok, celda(nan, nan, nan), 10, 'OK')['veredicto'] == 'INSUFFICIENT' and V(celda(nan, nan, nan), ok, 10, 'OK')['veredicto'] == 'INSUFFICIENT'
    assert V(ok, celda(0.01, -0.5, -0.1), 10, 'OK')['veredicto'] == 'PASA'                          # bloq1 solo exige mismo signo y EV_alto<=0, no IC propio
def test_h4_menos_de_10_dias_lo_nunca_pasa():
    ok = celda(0.2, 0.1, -0.1); V = P0.veredicto_combinado; a = V(ok, ok, 9, 'OK'); assert a['veredicto'] == 'PARTIAL' and a['n_dias'] == 7 and a['n_dias_lo_validos'] == 9
    assert V(celda(0.2, -0.1, 0.1), ok, 9, 'OK')['veredicto'] == 'INSUFFICIENT' and V(ok, ok, 10, 'OK')['veredicto'] == 'PASA'
    assert all('n_dias' in V(ok, ok, n, 'OK') for n in (0, 9, 10))
def test_h5_dias_confirmatorios_faltantes_insufficient():
    PR = fresh('h5'); llena(PR, PR.DIAS[:3]); PR.final(); r = json.load(open(PR.OUT + 'puerta0_resultado.json'))
    conf = [v for k, v in r['combinado'].items() if k.startswith('C_decision')]; assert conf and all(v['veredicto'] == 'INSUFFICIENT' and v['dias_faltantes'] == PR.DIAS[3:] for v in conf)      # faltan 06-14
    assert r['veredicto_oficial']['veredicto'] == 'INSUFFICIENT'
def test_h6_script_rechequea_todas_las_condiciones():
    d = tempfile.mkdtemp(dir=TMP); ch = d + '/chain'
    def run(chain, hm='1300', ram='1', extra=None):
        open(ch, 'w').write(chain + ' x\n'); env = dict(os.environ, P0_OUT=d + '/o/', P0_CHAIN=ch, P0_HM=hm, P0_RAM_MIN=ram, P0_ESPERA='0'); env.update(extra or {})
        return subprocess.run(['bash', HV + 'run_puerta0.sh'], env=env, capture_output=True, text=True, timeout=60)
    for kw in (dict(chain='RUNNING'), dict(chain='COMPLETE', hm='0700'), dict(chain='COMPLETE', hm='1100', ram='1') if False else dict(chain='COMPLETE', hm='0930', ram='1') , dict(chain='COMPLETE', ram='999999999')):
        p = run(**kw); log = ''.join(open(d + '/o/' + f).read() for f in os.listdir(d + '/o') if f.endswith('.log')); assert p.returncode == 3 and 'BLOQUEADO' in log, (kw, p.returncode, log)
    p = run('COMPLETE', hm='1220'); assert p.returncode == 3                                       # antes de las 12:30Z
    src = open(HV + 'run_puerta0.sh').read(); assert src.count('cond_ok') >= 3 and 'cond_ok || {' in src          # se re-chequea tras el bucle (y no solo dentro)
def test_h7_checkpoint_exige_mismo_codigo():
    PR = fresh('h7'); llena(PR, PR.DIAS[:1]); d = PR.DIAS[0]; outs = [f'p0_ordenes_{d}.pkl', f'p0_cov_{d}.json']; assert PR.RU.ya_completo('dia', d, outs)
    orig = PR.code_hashes; PR.code_hashes = lambda: dict(orig(), **{'puerta0_core.py': 'x' * 64})
    try:
        assert not PR.RU.ya_completo('dia', d, outs)                                                  # codigo distinto -> checkpoint invalido
        PR.final(); assert json.load(open(PR.OUT + 'run_manifest.json'))['estado_por_dia'][d].startswith('FAILED')
        llamadas = []; assert PR.RU.job('dia', d, outs, lambda dd: (llamadas.append(1), (dict(ok=1), dict(ok=1)))[1], {'x': HV + 'puerta0_core.py'}) == 'COMPLETE' and llamadas == [1]       # re-ejecuta
    finally: PR.code_hashes = orig
def test_h8_estrato_todas_las_monedas_y_conteo_primario():
    R = mk([('d1', 'bajo', 5, 0.2, 1), ('d1', 'alto', 5, 0.2, 0), ('d2', 'bajo', 5, 0.2, 1), ('d2', 'alto', 5, 0.2, 0)]); R['estrato'] = 'lo'; R['celda_valida'] = True
    a = P0.evalua(R, ['d1', 'd2'], 'todas_las_monedas', 0.0, 'sin', K=10, dias_todas=['d1']); b = P0.evalua(R, ['d1', 'd2'], 'lo_valido', 0.0, 'sin', K=10); assert a['dias'] == ['d1'] and b['dias'] == ['d1', 'd2'] and P0.evalua(R, ['d1', 'd2'], 'todas_las_monedas', 0.0, 'sin', K=10)['dias'] == []
    PR = fresh('h8'); llena(PR, PR.DIAS[2:]); PR.final(); r = json.load(open(PR.OUT + 'puerta0_resultado.json')); k = 'C_decision_05_14_NO_CIEGO|reb0.0|estres_sin|estrato_'
    assert k + 'todas_las_monedas' in r['combinado'] and 'bloq1|' + k.split('|')[0] + '|reb0.0|estres_sin|estrato_todas_las_monedas' in r['rejilla']
    tab = P0.lee_tabla_suelo(V + 'cierre_limites_19nov/tabla_suelo_ventanas_19nov.csv'); dv = P0.dias_lo_validos(P0.celdas_validas(tab)); cd = set(r['rejilla']['bloq0|' + k.split('|')[0] + '|reb0.0|estres_sin|estrato_lo_valido']['dias'])
    assert r['combinado'][k + 'lo_valido']['n_dias_lo_validos'] == len(set(dv['alguna_moneda']) & cd) and r['combinado'][k + 'todas_las_monedas']['n_dias_lo_validos'] == len(set(dv['todas_las_monedas']) & set(r['rejilla']['bloq0|' + k.split('|')[0] + '|reb0.0|estres_sin|estrato_todas_las_monedas']['dias']))
def test_h10_pid_tras_flock_y_prereg_fail_closed():
    d = tempfile.mkdtemp(dir=TMP); o = d + '/o/'; os.makedirs(o); env = dict(os.environ, P0_OUT=o, P0_CHAIN=d + '/c', P0_HM='1300', P0_RAM_MIN='1', P0_ESPERA='0'); open(d + '/c', 'w').write('RUNNING')
    h = subprocess.Popen(['flock', o + '.lock', 'sleep', '4']); import time; time.sleep(0.5)
    p = subprocess.run(['bash', HV + 'run_puerta0.sh'], env=env, capture_output=True, text=True, timeout=30); h.wait(); assert p.returncode == 2 and not os.path.exists(o + 'run.pid')           # con el lock ajeno no se escribe el PID
    p = subprocess.run(['bash', HV + 'run_puerta0.sh'], env=env, capture_output=True, text=True, timeout=30); assert p.returncode == 3 and open(o + 'run.pid').read().strip().isdigit()
    pd_ = d + '/pre/'; os.makedirs(pd_)
    for f in os.listdir(V):
        if f.startswith(('PREREG_R1v2_19nov', 'CONTRATO_R1v2_19nov_v2')) and f.endswith(('.md', '.sha256')): shutil.copy(V + f, pd_ + f)
    import puerta0_run as PR; os.environ['P0_PREREG_DIR'] = pd_
    try:
        assert len(PR.sha_prereg()) == 11; open(pd_ + 'PREREG_R1v2_19nov_ADENDA_06.md', 'a').write('x')
        try: PR.sha_prereg(); assert False
        except ValueError: pass
        env['P0_PREREG_DIR'] = pd_; open(d + '/c', 'w').write('COMPLETE'); p = subprocess.run(['bash', HV + 'run_puerta0.sh'], env=env, capture_output=True, text=True, timeout=30); assert p.returncode == 3
        assert 'PREREG' in ''.join(open(o + f).read() for f in os.listdir(o) if f.endswith('.log'))
        r = subprocess.run([sys.executable, HV + 'puerta0_run.py', 'final'], env=dict(os.environ, P0_OUT=d + '/p/'), capture_output=True, text=True); assert r.returncode == 3         # el runner tambien es fail-closed
    finally: os.environ.pop('P0_PREREG_DIR', None)
def test_seguridad_sin_ordenes_ni_red():
    src = open(HV + 'puerta0_core.py').read() + open(HV + 'puerta0_run.py').read() + open(HV + 'run_puerta0.sh').read()
    for p in ('post_order', 'create_order', 'py_clob_client', 'dotenv', 'live/.env', 'private_key', 'requests.', 'urlopen', 'pkill', 'pgrep'): assert p not in src, p

# ============================== ADENDA_08 (23-Nov): dias 10-14, conjuntos A/B/C, NO CIEGO, sha de tapes, cobertura libro5_tx
_TABC = []
def _TAB():
    if not _TABC: _TABC.append(P0.lee_tabla_suelo(V + 'cierre_limites_19nov/tabla_suelo_ventanas_19nov.csv'))
    return _TABC[0]
def dia_edge(PR, d, signo=1, n=40):
    """dia sintetico con edge: bajo/medio ganan (signo=1) o pierden (signo=-1), alto al reves; q=5, L=0,2; identico en bloq0 y bloq1."""
    rows = [(d, 'bajo', 5, 0.2, 1 if signo > 0 else 0)] * (n // 4) + [(d, 'medio', 5, 0.2, 1 if signo > 0 else 0)] * (n // 4) + [(d, 'alto', 5, 0.2, 0 if signo > 0 else 1)] * (n // 2)
    R = mk(rows); R['mid'] = [f'{d}_m{i}' for i in range(len(R))]; R['n_ord'] = 0; R['coin'] = 'eth'; w = _TAB()[(_TAB().dia == d) & (_TAB().coin == 'eth') & (_TAB().clase_estrato == 'lo')].w0_ms.values; assert len(w) >= 24; R['t_dec'] = w[np.arange(len(R)) % len(w)] + 1000; R['canal'] = 'visible'
    R = pd.concat([R.assign(bloq=0), R.assign(bloq=1)], ignore_index=True); return R
def llena_edge(PR, dias, signo=lambda d: 1):
    for d in dias:
        def fn(dd, d=d): PR.atomic_pkl(PR.OUT + f'p0_ordenes_{d}.pkl', dia_edge(PR, d, signo(d))); PR.atomic_json(PR.OUT + f'p0_cov_{d}.json', dict(ok=1)); return dict(ok=1), dict(ok=1)
        assert PR.RU.job('dia', d, [f'p0_ordenes_{d}.pkl', f'p0_cov_{d}.json'], fn, {'x': HV + 'puerta0_core.py'}) == 'COMPLETE'
def test_a08_dias_y_conjuntos():
    PR = fresh('a08a'); assert PR.DIAS[-5:] == [f'2026-11-{x}' for x in (10, 11, 12, 13, 14)] and len(PR.DIAS) == 12
    assert PR.DIAS_A == PR.DIAS[2:7] and PR.DIAS_B == PR.DIAS[7:] and PR.DIAS_C == PR.DIAS[2:]
    llena(PR, PR.DIAS[2:]); PR.final(); r = json.load(open(PR.OUT + 'puerta0_resultado.json')); k = '|reb0.0|estres_sin|estrato_todos'
    for n, dd in (('A_confirmatorio_05_09', PR.DIAS_A), ('B_replica_10_14_NO_CIEGO', PR.DIAS_B), ('C_decision_05_14_NO_CIEGO', PR.DIAS_C)): assert r['rejilla']['bloq0|' + n + k]['dias'] == dd, n
    assert r['rejilla']['bloq0|POSTHOC_todos_los_dias' + k]['dias'] == PR.DIAS[2:]
    for kk, v in r['combinado'].items():
        if kk.startswith('A_'): assert 'etiqueta_ciego' not in v
        else: assert v['etiqueta_ciego'].startswith('NO CIEGO') and v['veredicto'] != 'PASA', kk                    # todo lo que usa 10-14 va etiquetado; el maximo es PASA_NO_CIEGO
    vo = r['veredicto_oficial']; assert vo['clave'].startswith('C_decision') and vo['etiqueta_ciego'].startswith('NO CIEGO') and r['veredicto_A_05_09']['clave'].startswith('A_') and r['veredicto_B_10_14']['etiqueta_ciego']
    assert 'NO CIEGO' in r['lectura']['limites'] and 'consistencia_A_B' in r
def test_a08_pasa_no_ciego_y_maximo():
    PR = fresh('a08b'); llena_edge(PR, PR.DIAS[2:]); PR.final(); r = json.load(open(PR.OUT + 'puerta0_resultado.json')); k = '|reb0.0|estres_sin|estrato_todos'
    c = r['combinado']['C_decision_05_14_NO_CIEGO' + k]; a = r['combinado']['A_confirmatorio_05_09' + k]; b = r['combinado']['B_replica_10_14_NO_CIEGO' + k]
    assert c['n_dias'] == 10 and c['n_dias_lo_validos'] == 10 and c['veredicto'] == 'PASA_NO_CIEGO' and c['etiqueta_ciego'].startswith('NO CIEGO'), c           # 10 dias lo validos (tabla firmada 05-14)
    assert a['n_dias_lo_validos'] == 5 and a['veredicto'] == 'PARTIAL' and b['n_dias_lo_validos'] == 5 and b['veredicto'] == 'PARTIAL'                       # <10 dias lo validos: nunca PASA
    assert r['veredicto_oficial']['veredicto'] == 'PASA_NO_CIEGO' and r['veredicto_oficial']['n_dias_lo_validos'] == 10 and r['veredicto_A_05_09']['veredicto'] == 'PARTIAL' and r['veredicto_B_10_14']['veredicto'] == 'PARTIAL'         # celda oficial (lo_valido)
    assert r['consistencia_A_B']['estado'] == 'mismo signo' and not r['consistencia_A_B']['C_ambar'] and 'PASA' not in {v['veredicto'] for kk, v in r['combinado'].items() if not kk.startswith('A_')}
    PR2 = fresh('a08b2'); llena_edge(PR2, PR2.DIAS_A); PR2.final(); r2 = json.load(open(PR2.OUT + 'puerta0_resultado.json'))                              # sin B: C INSUFFICIENT (faltan dias), no PASA
    assert r2['veredicto_oficial']['veredicto'] == 'INSUFFICIENT' and r2['veredicto_oficial']['dias_faltantes'] == PR2.DIAS_B
def test_a08_A_y_B_discrepantes_ambar():
    PR = fresh('a08c'); llena_edge(PR, PR.DIAS[2:], signo=lambda d: 1 if d in PR.DIAS_A else -1); PR.final(); r = json.load(open(PR.OUT + 'puerta0_resultado.json'))
    assert r['consistencia_A_B']['estado'] == 'A y B discrepantes' and r['consistencia_A_B']['C_ambar'] and r['veredicto_oficial']['ambar_A_B_discrepantes'] and r['veredicto_oficial']['veredicto'] != 'PASA_NO_CIEGO'
def test_a08_fuga_en_B_bloquea_C():
    PR = fresh('a08d'); llena(PR, PR.DIAS[2:], **{d: dict(n=300, leak=(d in PR.DIAS_B), seed=7) for d in PR.DIAS[2:]}); PR.final(); r = json.load(open(PR.OUT + 'puerta0_resultado.json'))
    pc = r['validez']['fuga_nan']['por_conjunto']; assert pc['B_replica_10_14_NO_CIEGO'] == 'FUGA_SOSPECHOSA' and pc['A_confirmatorio_05_09'] == 'OK' and r['veredicto_oficial']['veredicto'] == 'BLOCKED_FUGA'
def test_a08_prereg_incluye_06b_07_08():
    d = tempfile.mkdtemp(dir=TMP); pd_ = d + '/pre/'; os.makedirs(pd_)
    for f in os.listdir(V):
        if f.startswith(('PREREG_R1v2_19nov', 'CONTRATO_R1v2_19nov_v2')) and f.endswith(('.md', '.sha256')): shutil.copy(V + f, pd_ + f)
    import puerta0_run as PR; os.environ['P0_PREREG_DIR'] = pd_
    try:
        s = PR.sha_prereg(); assert all(f'PREREG_R1v2_19nov_ADENDA_{x}.md' in s for x in ('06b', '07', '08')) and s['PREREG_R1v2_19nov_ADENDA_08.md'].startswith('d2021064')
        for x in ('06b', '07', '08'):
            m = pd_ + f'PREREG_R1v2_19nov_ADENDA_{x}.md'; orig = open(m).read(); open(m, 'a').write('x')
            try: PR.sha_prereg(); assert False, x
            except ValueError: pass
            open(m, 'w').write(orig)
            sh = pd_ + f'PREREG_R1v2_19nov_ADENDA_{x}.sha256'; o2 = open(sh).read(); os.remove(sh)
            try: PR.sha_prereg(); assert False, x
            except ValueError: pass
            open(sh, 'w').write(o2)
        assert len(PR.sha_prereg()) == 11
        # el script de shell tambien lo exige: adulterar ADENDA_08 -> BLOQUEADO (rc 3)
        m = pd_ + 'PREREG_R1v2_19nov_ADENDA_08.md'; open(m, 'a').write('x'); o = d + '/o/'
        env = dict(os.environ, P0_OUT=o, P0_CHAIN=d + '/c', P0_HM='1300', P0_RAM_MIN='1', P0_ESPERA='0', P0_PREREG_DIR=pd_); open(d + '/c', 'w').write('COMPLETE')
        p = subprocess.run(['bash', HV + 'run_puerta0.sh'], env=env, capture_output=True, text=True, timeout=30); assert p.returncode == 3
    finally: os.environ.pop('P0_PREREG_DIR', None)
    src = open(HV + 'run_puerta0.sh').read(); assert all(f'PREREG_R1v2_19nov_ADENDA_{x}' in src.split('prereg_ok()')[1].split('\n')[0] for x in ('06b', '07', '08')) and '2026-11-10 2026-11-11 2026-11-12 2026-11-13 2026-11-14' in src
def test_a08_inputs_dia_con_sha_y_referencia():
    PR = fresh('a08e'); f = TMP + '/x.bin'; open(f, 'wb').write(b'abc'); h = hashlib_sha(b'abc'); ref = TMP + '/ref.txt'; PR.TAPES_REF = ref
    open(ref, 'w').write(f'{h}  {f}\n# c\n'); s = PR.stat_sha(f); assert s['sha256'] == h and s['sha_ref_ok'] is True and s['size'] == 3
    open(ref, 'w').write(f'{"0" * 64}  {f}\n'); assert PR.stat_sha(f)['sha_ref_ok'] is False
    open(ref, 'w').write(''); assert PR.stat_sha(f)['sha_ref_ok'] is None and PR.lee_tapes_ref(TMP + '/no_existe') == {}
    d = '2026-11-05'; PR.RU.job('dia', d, [f'p0_ordenes_{d}.pkl', f'p0_cov_{d}.json'], lambda dd: (PR.atomic_pkl(PR.OUT + f'p0_ordenes_{d}.pkl', pd.DataFrame({'a': [1]})), PR.atomic_json(PR.OUT + f'p0_cov_{d}.json', {}), (dict(), dict()))[2], {'tape': f})
    assert json.load(open(PR.mpath('dia', d) if hasattr(PR, 'mpath') else PR.RU.mpath('dia', d)))['inputs']['tape']['sha256'] == h          # el manifest registra el sha del input
def hashlib_sha(b):
    import hashlib; return hashlib.sha256(b).hexdigest()
def test_a08_referencia_tapes_cuadra_con_disco():
    import puerta0_run as PR; ref = PR.lee_tapes_ref(HV + 'TAPES_SHA256_23nov.txt'); assert len(ref) == 24
    for d in PR.DIAS:
        for k, p in PR.RU.inputs_dia(d).items(): assert ref[p] == PR.sha(p), (d, k)              # los 12 dias x (tape, bad): la referencia coincide con el disco
def fx_cov(sub, cov_d=1.0, falta_tape=None, n=20):
    """fixture: tapes de d-1,d,d+1 (n tx cada uno) y libro5_tx con la fraccion cov_d de los tx del dia d (los otros dias 100 %)."""
    import gzip; base = TMP + f'/{sub}/'; pb = base + 'pb/'; tx = base + 'tx/'; os.makedirs(pb); os.makedirs(tx)
    for dia in ('2026-11-09', '2026-11-10', '2026-11-11'):
        txs = [f'0x{dia}_{i}' for i in range(n)]
        if dia != falta_tape: pd.DataFrame({'tx': txs, 'price': 0.2}).to_pickle(pb + f'tape_{dia}.pkl')
        keep = txs[: int(round(n * (cov_d if dia == '2026-11-10' else 1.0)))]
        with gzip.open(tx + f'libro5_tx_{dia}_1.csv.gz', 'wt') as g:
            for i, x in enumerate(keep): g.write(f'1,tok,{x},2\n')
    return pb, tx
def test_a08_cobertura_libro5tx_fail_closed():
    import puerta0_run as PR
    pb, tx = fx_cov('c1'); c = PR.cobertura_tx('2026-11-10', tx, pb); assert c['ok'] and all(v['cov'] == 1.0 and v['units'] == 20 for v in c['dias'].values()) and list(c['dias']) == ['2026-11-09', '2026-11-10', '2026-11-11']
    pb, tx = fx_cov('c2', cov_d=0.85); c = PR.cobertura_tx('2026-11-10', tx, pb); assert not c['ok'] and abs(c['dias']['2026-11-10']['cov'] - 0.85) < 1e-9            # 0,85 < 0,90
    pb, tx = fx_cov('c3', cov_d=0.90); assert PR.cobertura_tx('2026-11-10', tx, pb)['ok']                                                                                # borde: >= 0,90
    pb, tx = fx_cov('c4', falta_tape='2026-11-11'); c = PR.cobertura_tx('2026-11-10', tx, pb); assert not c['ok'] and c['dias']['2026-11-11']['cov'] is None          # sin tape: nunca bueno por defecto
    pb, tx = fx_cov('c5', cov_d=0.0); c = PR.cobertura_tx('2026-11-10', tx, pb); assert not c['ok'] and c['dias']['2026-11-10']['con_tx'] == 0                          # feed en pausa (cov 0)
    pb, tx = fx_cov('c6', n=0) if False else fx_cov('c6'); os.remove(tx + 'libro5_tx_2026-11-10_1.csv.gz'); assert not PR.cobertura_tx('2026-11-10', tx, pb)['ok']       # sin ficheros libro5_tx del dia
def test_a08_incompleto_solo_dias_nuevos_y_sha():
    PR = fresh('a08f'); pb, tx = fx_cov('c7', cov_d=0.5); bad = PR.cobertura_tx('2026-11-10', tx, pb); okc = dict(ok=True, dias={})
    assert PR.incompleto('2026-11-09', bad, None) is None                                   # dias antiguos: solo se registra, no bloquea
    m = PR.incompleto('2026-11-10', bad, None); assert m and 'cobertura' in m[0]
    ref0 = PR.TAPES_REF; PR.TAPES_REF = TMP + '/sin_ref.txt'; old_pb = PR.RU.PB
    try:
        os.makedirs(TMP + '/pbx', exist_ok=True); PR.RU.PB = TMP + '/pbx/'; open(PR.RU.PB + 'tape_2026-11-10.pkl', 'wb').write(b't'); open(PR.RU.PB + 'bad_2026-11-10.json', 'wb').write(b'{}')
        m = PR.incompleto('2026-11-10', okc, None); assert m and all('sin sha de referencia' in x for x in m) and len(m) == 2          # sin referencia: INCOMPLETE
        open(PR.TAPES_REF, 'w').write(f'{"0" * 64}  {PR.RU.PB}tape_2026-11-10.pkl\n{hashlib_sha(b"{}")}  {PR.RU.PB}bad_2026-11-10.json\n'); m = PR.incompleto('2026-11-10', okc, None); assert m and len(m) == 1 and 'tape' in m[0] and 'sha256 !=' in m[0]
        open(PR.TAPES_REF, 'w').write(f'{hashlib_sha(b"t")}  {PR.RU.PB}tape_2026-11-10.pkl\n{hashlib_sha(b"{}")}  {PR.RU.PB}bad_2026-11-10.json\n'); assert PR.incompleto('2026-11-10', okc, None) is None
    finally: PR.TAPES_REF = ref0; PR.RU.PB = old_pb
def test_a08_dia_nuevo_sin_cobertura_queda_INCOMPLETE_y_final_no_lo_cuenta():
    d = '2026-11-10'; o = TMP + '/a08g/'; os.makedirs(o); os.makedirs(TMP + '/a08g_tx')                                        # libro5_tx vacio = feed en pausa
    env = dict(os.environ, P0_OUT=o, P0_TXD=TMP + '/a08g_tx/'); p = subprocess.run([sys.executable, HV + 'puerta0_run.py', 'dia', d], env=env, capture_output=True, text=True, timeout=300)
    m = json.load(open(o + f'manifest_dia_{d}.json')); assert p.returncode == 1 and m['status'] == 'INCOMPLETE' and 'cobertura' in m['motivo'][0] and not os.path.exists(o + f'p0_ordenes_{d}.pkl')
    f = subprocess.run([sys.executable, HV + 'puerta0_run.py', 'final'], env=env, capture_output=True, text=True, timeout=120); rm = json.load(open(o + 'run_manifest.json'))
    assert rm['estado_por_dia'][d] == 'INCOMPLETE' and rm['status'] != 'COMPLETE'
if __name__ == '__main__':
    ts = [(n, f) for n, f in sorted(globals().items()) if n.startswith('test_') and callable(f)]
    try:
        for n, f in ts: f(); print('OK', n)
        print(len(ts), 'tests OK')
    finally: shutil.rmtree(TMP, ignore_errors=True)
