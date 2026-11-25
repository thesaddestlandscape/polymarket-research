#!/usr/bin/env python3
"""test_variantes_b.py -- FASE B parcial: V5 (CXJ150) y V6 (E1b S1) contra el codigo de referencia (passT_v4.py y e1_sim.py, solo lectura, sha comprobado). Ejecutar: python3 test_variantes_b.py"""
import sys, os, ast, hashlib, types
import numpy as np, pandas as pd
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import variantes_b as VB
PT4 = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/passT_v4.py'; PT4_SHA = '85256bcc7872afdfdc7d18f9bf4cd3e27e46c0d4176aceb263d6821045bbf535'
E1 = '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/seleccion_adversa_plan/scripts/e1_sim.py'; E1_SHA = 'f826196dd790712d324ee61bc5b8b2a20309e8b55ed585b09a595004c33b0e95'
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def ref_passT(xs):
    """ejecuta bnr y first_after de passT_v4 (lineas literales) con XS = xs."""
    assert sha(PT4) == PT4_SHA; L = open(PT4).read().split('\n'); a = next(i for i, l in enumerate(L) if l.startswith('def bnr(')); b = next(i for i, l in enumerate(L) if l.startswith('JUMP = {}'))
    c = next(i for i, l in enumerate(L) if l.startswith('def first_after'))
    ns = {'np': np, 'XS': xs}; exec('\n'.join(L[a:b] + L[c:c + 2]), ns); return ns
def ref_bn_trig():
    assert sha(E1) == E1_SHA; tree = ast.parse(open(E1).read()); ns = {'np': np}
    for n in tree.body:
        if isinstance(n, ast.FunctionDef) and n.name == 'bn_trig': exec(compile(ast.Module([n], []), E1, 'exec'), ns)
    return ns['bn_trig']
def stream(n=4000, seed=3, gaps=False):
    rng = np.random.default_rng(seed); t = np.cumsum(rng.integers(1, 400, n)).astype(np.int64) + 10_000_000; p = 100 * np.exp(np.cumsum(rng.normal(0, 1.2e-4, n)))
    if gaps: t[n // 2:] += 20000                                                      # hueco > 15 s
    return t, p

def test_ret_bps_igual_bnr_passT_con_huecos():
    t, p = stream(gaps=True); ns = ref_passT({'x': (t, p)}); q = np.sort(np.random.default_rng(1).integers(t[0] - 5000, t[-1] + 30000, 3000)).astype(np.int64)
    a = VB.ret_bps(t, p, q, 1000); b = ns['bnr']('x', q, 1000); assert np.array_equal(np.isnan(a), np.isnan(b)) and np.allclose(a[~np.isnan(a)], b[~np.isnan(b)], atol=1e-9) and np.isnan(a).any()
    assert np.isnan(VB.ret_bps(np.array([], np.int64), np.array([]), q[:3], 1000)).all()
def test_saltos_V5_igual_JUMP_passT():
    t, p = stream(); ns = ref_passT({'x': (t, p)}); r1 = ns['bnr']('x', t, 1000); J = VB.saltos(t, p, VB.V5)
    assert np.array_equal(J['up'], t[r1 >= 3]) and np.array_equal(J['dn'], t[r1 <= -3]) and len(J['up']) > 3 and len(J['dn']) > 3
def test_umbral_inclusivo():
    t = np.array([1000, 2000, 3000], np.int64); p = np.array([100.0, 100.0, 100.0 * (1 + 3e-4)]); J = VB.saltos(t, p, VB.V5); assert list(J['up']) == [3000] and len(J['dn']) == 0       # exactamente 3 bps cuenta
    p = np.array([100.0, 100.0, 100.0 * (1 + 2.9e-4)]); assert len(VB.saltos(t, p, VB.V5)['up']) == 0
def test_V6_igual_bn_trig_e1_y_diferencia_declarada():
    bn = ref_bn_trig(); t, p = stream(6000, seed=7); D = types.SimpleNamespace(xs=[0, len(t)], xr=t, xv=p.astype(np.float64)); t0 = int(t[0]) + 5000; t1 = int(t[-1])
    c, f = bn(D, 0, 1, t0, t1, 2000, 2); J = VB.saltos(t, p, VB.V6); m = J['dn'] >= t0
    assert np.array_equal(J['dn'][m], c) and np.array_equal(J['up'][J['up'] >= t0], f) and len(c) > 5                                        # sg=+1 (lado YES): adverso = ret <= -2 bps en 2 s
    c2, f2 = bn(D, 0, -1, t0, t1, 2000, 2); assert np.array_equal(J['up'][J['up'] >= t0], c2) and np.array_equal(J['dn'][J['dn'] >= t0], f2)       # sg=-1 (lado Down): adverso = ret >= +2
    # diferencia declarada: e1 corta la serie en [t0-W-1000, t1]; con un hueco >W+1000 antes de un tick, e1 pone ret=0 y passT/V6 usa el tick anterior al hueco
    t = np.array([0, 100, 200, 10_000, 10_050], np.int64); p = np.array([100, 100, 100, 99.0, 99.0]); D = types.SimpleNamespace(xs=[0, 5], xr=t, xv=p)
    c, _ = bn(D, 0, 1, 10_000, 10_050, 2000, 2); assert len(c) == 0 and 10_000 in VB.saltos(t, p, VB.V6)['dn']
def test_adverso_y_lado():
    J = dict(up=np.array([1]), dn=np.array([2])); assert list(VB.adverso(J, 'YES')) == [2] and list(VB.adverso(J, 'NO')) == [1]
    try: VB.adverso(J, 'Up'); assert False
    except ValueError: pass                                                                                    # vocabulario Up/Down no aceptado en silencio
def test_no_armar_ventanas_V5_V6():
    t = 100_000; tq = t - 300; j = np.array([tq - 3000, tq - 2068])
    assert not VB.no_armar(np.array([tq - 3000]), t, VB.V5) and VB.no_armar(np.array([tq - 2999]), t, VB.V5) and VB.no_armar(np.array([tq]), t, VB.V5) and not VB.no_armar(np.array([tq + 1]), t, VB.V5)   # (tq-3000, tq]
    assert not VB.no_armar(np.array([tq - 2068]), t, VB.V6) and VB.no_armar(np.array([tq - 2067]), t, VB.V6) and not VB.no_armar(np.array([], np.int64), t, VB.V6)
def test_primer_disparo_solo_desde_llegada_igual_first_after():
    j = np.array([100, 500, 900], np.int64); ns = ref_passT({'x': (j, j.astype(float))}); fa = ns['first_after']
    for t0, t1 in ((0, 99), (100, 100), (101, 499), (101, 500), (501, 2000), (901, 2000)): assert VB.primer_disparo(j, t0, t1) == fa(j, t0, t1)
    assert VB.primer_disparo(j, 501, 2000) == 900 and VB.primer_disparo(j, 101, 499) is None            # un salto previo a la llegada no es disparo
def test_efectividad_frontera():
    assert VB.cancela_a_tiempo(1000, 1000 + 74 + 20, 0) and not VB.cancela_a_tiempo(1000, 1000 + 74 + 19, 0) and not VB.cancela_a_tiempo(1000, 1000 + 74 + 20, 1) and VB.cancela_a_tiempo(1000, 1111 + 20, 0, 111)
    assert not VB.cancela_a_tiempo(None, 5, 0) and not VB.cancela_a_tiempo(5, None, 0)
def mk_R():
    return pd.DataFrame(dict(dia='d', coin=['eth', 'eth', 'xrp'], lado=['YES', 'YES', 'NO'], t_dec=[100_000, 200_000, 100_000], t_arr=[100_100, 200_100, 100_100], t_end=[190_000, 290_000, 190_000], tf=[150_000, 250_000, -1], q=[5.0, 5.0, 0.0], gana=[1, 0, 1], mid=['a', 'b', 'c']))
def series_demo(extra=()):
    te = np.array([50_000, 60_000, 70_000, 99_000, 99_500, 120_000, 150_000 - 80, 199_600, 200_500, 250_000 - 10, 250_100, *extra], np.int64)
    pe = np.array([100.0, 100.0, 100.0, 100.0, 99.95, 99.90, 99.80, 100.0, 100.0, 100.0, 100.0, *([100.0] * len(extra))]); tx = np.array([10_000, 20_000], np.int64)     # xrp: ultimo tick hace > 15 s
    return {'eth': (te, pe), 'xrp': (tx, np.array([1.0, 1.0]))}
def test_marca_ordenes_y_sin_dato_y_no_lookahead():
    R = mk_R(); S = series_demo(); M = VB.marca_ordenes(R, S, VB.V5, 0)
    # orden 0 (YES): bajada de 5 bps en 1 s en 99.5k (ret=-5 bps vs 99k? 99.95/100 = -5 bps) -> salto adverso previo a la llegada: no_armar; en vida 120k: -10 bps adverso -> disparo
    assert bool(M.V5_CXJ150_no_armar.iloc[0])
    assert bool(M.V5_CXJ150_disparo.iloc[0]) and bool(M.V5_CXJ150_cancela_fill.iloc[0])                          # disparo ~149,9k-ish, relleno a 150k: llega a tiempo solo si tb+74 <= 150000-20
    assert bool(M.V5_CXJ150_sin_dato.iloc[2]) and not bool(M.V5_CXJ150_disparo.iloc[2]) and not bool(M.V5_CXJ150_no_armar.iloc[2])    # sin dato fresco: NaN != salto, ni cancela ni bloquea (nunca y=0)
    assert pct_ok(VB.pct_sin_dato(M, 'V5_CXJ150'))
    # sin look-ahead: ticks posteriores a t_end de cada orden no cambian ninguna marca
    S2 = series_demo(extra=(400_000, 400_100)); M2 = VB.marca_ordenes(R, S2, VB.V5, 0); cols = [c for c in M.columns if c.startswith('V5')]; assert M[cols].equals(M2[cols])
    # fill demasiado pegado al disparo: no llega a tiempo
    t = np.array([60_000, 149_950, 149_960], np.int64); p = np.array([100.0, 100.0, 99.90]); Mx = VB.marca_ordenes(R.iloc[:1], {'eth': (t, p)}, VB.V5, 0); assert bool(Mx.V5_CXJ150_disparo.iloc[0]) and not bool(Mx.V5_CXJ150_cancela_fill.iloc[0])
def pct_ok(d): return d['xrp']['pct'] == 1.0 and d['eth']['pct'] == 0.0 and d['todas']['n'] == 3
def test_frecuencia_y_solape():
    R = mk_R(); S = series_demo(); R = VB.marca_ordenes(R, S, VB.V5, 0); R = VB.marca_ordenes(R, S, VB.V6, 0)
    f = VB.frecuencia_disparo(R, 'V5_CXJ150'); assert abs(f['frac_vidas_con_disparo'] - 2 / 3) < 1e-12 or f['frac_vidas_con_disparo'] in (1 / 3, 2 / 3, 1.0)
    s = VB.solape(R); assert s['n'] == 3 and s['ambas'] + s['solo_v5'] + s['solo_v6'] + s['ninguna'] == 3
    R2 = R.copy(); R2['V5_CXJ150_disparo'] = [True, True, False]; R2['V6_E1bS1_disparo'] = [True, False, True]; assert VB.solape(R2) == dict(ambas=1, solo_v5=1, solo_v6=1, ninguna=0, n=3)
    R2['V5_CXJ150_disparo'] = True; assert VB.frecuencia_disparo(R2, 'V5_CXJ150')['solo_no_operar']                    # >50 % de las vidas => 'solo no operar'
def test_max_statistic_y_horquilla():
    nul = np.zeros((99, 3)); r = VB.p_max_permutacion([1.0, 0.5, 0.2], nul); assert abs(r['p_max'] - 1 / 100) < 1e-12 and r['n_var'] == 3 and r['p_ajustado'][1] == 0.01
    rng = np.random.default_rng(0); nul = rng.normal(size=(999, 6)); r = VB.p_max_permutacion([0.1] * 5 + [0.2], nul); assert r['p_max'] > 0.3                    # 6 variantes sin senal: el mejor no pasa
    assert VB.mantiene_signo(dict(a=0.1, b=0.05, c=0.2)) and not VB.mantiene_signo(dict(a=0.1, b=-0.05, c=0.2)) and not VB.mantiene_signo(dict(a=0.1, b=0.0, c=0.2)) and not VB.mantiene_signo(dict(a=0.1, b=0.2))
def test_fuga_flag_detecta_y_no_inventa():
    rng = np.random.default_rng(9); n = 600; y = rng.integers(0, 2, n)
    R = pd.DataFrame(dict(dia=np.repeat(['d1', 'd2'], n // 2), coin=np.tile(['eth', 'sol'], n // 2), gana=y, flag=rng.random(n) < 0.3)); r = VB.fuga_flag(R, 'flag', K=200); assert r['estado'] == 'OK' and r['p_perm'] > 0.05
    R['leak'] = (R.gana > 0.5) & (rng.random(n) < 0.8); r = VB.fuga_flag(R, 'leak', K=200); assert r['estado'] == 'FUGA_SOSPECHOSA' and r['p_perm'] < 0.05
def test_orden_rx_y_duplicados():
    t, p = VB.ordena_rx([5, 3, 3, 9], [1.0, 2.0, 3.0, 4.0]); assert list(t) == [3, 3, 5, 9] and list(p) == [2.0, 3.0, 1.0, 4.0]       # estable: empate conserva orden de llegada
def test_h9_t_proc_obligatorio_y_casado_exchange_en_bloqueo():
    import inspect
    for f in (VB.cancela_a_tiempo, VB.marca_orden, VB.marca_ordenes): assert inspect.signature(f).parameters['t_proc'].default is inspect.Parameter.empty        # sin default
    for call in (lambda: VB.cancela_a_tiempo(1, 1000), lambda: VB.marca_ordenes(mk_R(), series_demo(), VB.V5)):
        try: call(); assert False
        except TypeError: pass
    # relleno por bloqueo: tf = t_rx = 150_000 pero t_ex = 150_040 (reloj exchange): con disparo en 149_900 y L=74: 149_900+74+20=149_994 <= casado-... 
    t = np.array([60_000, 100_000 + 5000, 149_800, 149_810], np.int64); p = np.array([100.0, 100.0, 100.0, 99.90]); R = mk_R().iloc[:1].copy(); R['canal'] = 'bloqueo'
    R['t_ex_fill'] = 149_900.0; M1 = VB.marca_ordenes(R, {'eth': (t, p)}, VB.V5, 0); assert bool(M1.V5_CXJ150_disparo.iloc[0]) and not bool(M1.V5_CXJ150_cancela_fill.iloc[0])      # disparo 149_810+74+20 > 149_900-... -> no a tiempo en reloj exchange
    R['t_ex_fill'] = 150_000.0; assert bool(VB.marca_ordenes(R, {'eth': (t, p)}, VB.V5, 0).V5_CXJ150_cancela_fill.iloc[0])
    R['t_ex_fill'] = np.nan
    try: VB.marca_ordenes(R, {'eth': (t, p)}, VB.V5, 0); assert False
    except ValueError: pass                                                                                    # bloqueo sin t_ex: fail-closed
    # con t_rx (150_000, mal reloj) y t_ex 149_900 el resultado seria distinto: se usa t_ex
    R['t_ex_fill'] = 149_900.0; R['tf'] = 150_000; assert not bool(VB.marca_ordenes(R, {'eth': (t, p)}, VB.V5, 0).V5_CXJ150_cancela_fill.iloc[0])
def test_seguridad():
    src = open(HV + 'variantes_b.py').read()
    for pr in ('post_order', 'create_order', 'py_clob_client', 'dotenv', 'live/.env', 'private_key', 'requests.', 'urlopen', 'pkill', 'pgrep', 'c[6]'): assert pr not in src, pr
if __name__ == '__main__':
    ts = [(n, f) for n, f in sorted(globals().items()) if n.startswith('test_') and callable(f)]
    for n, f in ts: f(); print('OK', n)
    print(len(ts), 'tests OK')
