#!/usr/bin/env python3
"""test_sec7.py -- pruebas unitarias de R1v2 sec.7 con fixtures diminutos (sin datos de produccion, sin red, <200 MB). Ejecutar: python3 test_sec7.py"""
import sys, os, json, types, tempfile, shutil
import numpy as np, pandas as pd
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; BSIM = os.path.dirname(os.path.dirname(HV.rstrip('/'))) + '/'
TMP = tempfile.mkdtemp(prefix='sec7_test_'); os.environ['SEC7_OUT'] = TMP + '/'
sys.path.insert(0, HV); sys.path.insert(0, BSIM)
import sec7_core as C, sec7_calculos as K
nan = float('nan')
def S(rows, dlag=20):
    """rows: (rx, bid, ask, bsz, asz) -> SerieL1 con ex = rx - dlag."""
    a = np.array(rows, float); return C.SerieL1(a[:, 0], a[:, 0] - dlag, a[:, 1], a[:, 2], a[:, 3], a[:, 4])
T0 = 1_000_000

def test_constantes_igual_motor():
    import eng_v5 as EV; assert C.FLOOR == EV.E4.FLOOR and abs(C.TOLP - EV.G.TOLP) < 1e-12 and abs(C.TOL - EV.G.EPS) < 1e-12
    sys.path.insert(0, os.path.dirname(BSIM.rstrip('/'))); import suelo_causal as SC; assert (C.D_LO, C.D_HI) == (SC.D_LO, SC.D_HI) and C.BIN_MS == SC.BIN_MS

def mk(comp_rows, own_rows=None):
    own = S(own_rows or [(T0 - 5000, 0.22, 0.24, 50, 40)]); comp = S(comp_rows); return own, comp
def test_bloqueo_i_basico_y_fecha_rx():
    own, comp = mk([(T0 - 5000, 0.70, 0.72, 30, 30), (T0 + 1000, 0.81, 0.83, 7.0, 9)])            # L=0,19 -> 1-L=0,81
    ev = C.primer_bloqueo(own, comp, 0.19, T0, T0 + 5000, 5.0)
    assert ev and ev['tipo'] == 'i' and ev['t_rx'] == T0 + 1000 and ev['t_ex'] == T0 + 980 and ev['q'] == 5.0 and ev['nivel'] == 7.0       # fecha = rx; ex solo para ordenar
def test_bloqueo_ii_y_tamano_min():
    own, comp = mk([(T0 - 5000, 0.70, 0.72, 30, 30)], [(T0 - 5000, 0.22, 0.24, 50, 40), (T0 + 2000, 0.15, 0.19, 50, 3.0)])           # ask propio baja a L
    ev = C.primer_bloqueo(own, comp, 0.19, T0, T0 + 5000, 5.0); assert ev['tipo'] == 'ii' and ev['q'] == 3.0       # min(rem 5, nivel 3)
def test_ya_cumplido_en_llegada_no_es_evento():
    own, comp = mk([(T0 - 5000, 0.81, 0.83, 7, 9), (T0 + 1000, 0.81, 0.83, 8, 9)]); info = {}
    from collections import Counter; info = Counter(); assert C.primer_bloqueo(own, comp, 0.19, T0, T0 + 5000, 5.0, info=info) is None and info['ya_cumplido_llegada'] == 1
def test_falso_a_verdadero_rearma():
    own, comp = mk([(T0 - 5000, 0.81, 0.83, 7, 9), (T0 + 500, 0.70, 0.72, 7, 9), (T0 + 3000, 0.82, 0.83, 6, 9)])
    ev = C.primer_bloqueo(own, comp, 0.19, T0, T0 + 5000, 5.0); assert ev and ev['t_rx'] == T0 + 3000                  # cierto en llegada, cae, vuelve: evento en la vuelta
def test_cruzado_y_nan_no_cuentan_ni_se_imputan():
    from collections import Counter; info = Counter()
    own, comp = mk([(T0 - 5000, 0.70, 0.72, 30, 30), (T0 + 1000, 0.90, 0.80, 7, 9)])            # complementario CRUZADO bid>ask con bid>=1-L: NO es bloqueo
    assert C.primer_bloqueo(own, comp, 0.19, T0, T0 + 5000, 5.0, info=info) is None and info['cruzado'] >= 1
    own, comp = mk([(T0 - 5000, 0.70, 0.72, 30, 30), (T0 + 1000, nan, nan, nan, nan)]); info = Counter()
    assert C.primer_bloqueo(own, comp, 0.19, T0, T0 + 5000, 5.0, info=info) is None and info['sin_dato'] >= 1              # NaN no se imputa a 0 ni a evento
def test_excluir_igual_opcional():
    own, comp = mk([(T0 - 5000, 0.70, 0.72, 30, 30), (T0 + 1000, 0.81, 0.81, 7, 9)])
    assert C.primer_bloqueo(own, comp, 0.19, T0, T0 + 5000, 5.0) is not None and C.primer_bloqueo(own, comp, 0.19, T0, T0 + 5000, 5.0, excluir_igual=True) is None
def test_sin_lookahead_quitar_futuro_no_cambia():
    rows = [(T0 - 5000, 0.70, 0.72, 30, 30), (T0 + 1000, 0.81, 0.83, 7, 9), (T0 + 4000, 0.60, 0.62, 7, 9)]
    own, comp = mk(rows); a = C.primer_bloqueo(own, comp, 0.19, T0, T0 + 5000, 5.0)
    own2, comp2 = mk(rows[:2]); b = C.primer_bloqueo(own2, comp2, 0.19, T0, T0 + 5000, 5.0); assert a == b
    own3, comp3 = mk(rows[:1] + [(T0 + 6000, 0.81, 0.83, 7, 9)]); assert C.primer_bloqueo(own3, comp3, 0.19, T0, T0 + 5000, 5.0) is None            # evento posterior a t_end: nada
def test_puja_no_viva_antes_de_llegada_ni_despues_del_fin():
    own, comp = mk([(T0 - 5000, 0.70, 0.72, 30, 30), (T0 - 100, 0.81, 0.83, 7, 9)])            # ex = T0-120 < t_arr: la orden aun no existia en el exchange
    assert C.primer_bloqueo(own, comp, 0.19, T0, T0 + 5000, 5.0) is None
def test_desorden_y_duplicados_rx():
    rows = [(T0 + 1000, 0.81, 0.83, 7, 9), (T0 - 5000, 0.70, 0.72, 30, 30), (T0 + 1000, 0.81, 0.83, 7, 9)]       # fuera de orden y duplicada
    own = S([(T0 - 5000, 0.22, 0.24, 50, 40)]); comp = S(rows); ev = C.primer_bloqueo(own, comp, 0.19, T0, T0 + 5000, 5.0); assert ev and ev['t_rx'] == T0 + 1000
    assert (np.diff(comp.rx) >= 0).all()
def test_tamano_bajo_suelo_no_es_relleno():
    from collections import Counter; info = Counter(); own, comp = mk([(T0 - 5000, 0.70, 0.72, 30, 30), (T0 + 1000, 0.81, 0.83, 0.0005, 9)])
    assert C.primer_bloqueo(own, comp, 0.19, T0, T0 + 5000, 5.0, info=info) is None and info['sin_tamano'] == 1
def test_serie_de_dia_sin_rx_no_imputa():
    D = types.SimpleNamespace(qb=np.array([0, 4]), t0=1000, _otro=np.array([100, -1, 300, 200]), qt=np.array([1090, 1150, 1290, 1180]), v0=np.arange(4, dtype=np.float32), v1=np.arange(4, dtype=np.float32) + 1, v2=np.ones(4, np.float32), v3=np.ones(4, np.float32) * 2)
    s = C.serie_de_dia(D, 0); assert s.n_sin_rx == 1 and len(s) == 3 and list(s.rx) == [1100, 1200, 1300] and list(s.ex) == [1090, 1180, 1290]       # la fila sin rx se excluye y se cuenta

# ---- wrapper
class StubE:
    def __init__(self, res=(0.0, None, 'ok'), prints=None): self.res = res; self.prints = prints; self.D = types.SimpleNamespace(x=1)
    def run_segment(self, k, L, t_arr, t_end, rem, var): return self.res
    class tape_: pass
def test_flag_apagado_identico_y_sin_registro():
    own, comp = mk([(T0 - 5000, 0.70, 0.72, 30, 30), (T0 + 1000, 0.81, 0.83, 7, 9)])
    for res in ((0.0, None, 'ok'), (5.0, T0 + 3000, 'ok')):
        W = C.EngineBloqueo(StubE(res), activo=False, fuente=lambda k: (own, comp)); assert W.run_segment(0, 0.19, T0, T0 + 5000, 5.0, 'BASE') == res and W.fills == {} and not W.cont
    assert W.D.x == 1                                                                           # delegacion
def test_bloqueo_gana_si_es_anterior_al_print_y_pierde_si_es_posterior():
    own, comp = mk([(T0 - 5000, 0.70, 0.72, 30, 30), (T0 + 1000, 0.81, 0.83, 7, 9)])         # ex del evento = T0+980
    W = C.EngineBloqueo(StubE((5.0, T0 + 3000, 'ok')), activo=True, fuente=lambda k: (own, comp)); r = W.run_segment(0, 0.19, T0, T0 + 5000, 5.0, 'BASE')
    assert r == (5.0, T0 + 1000, 'ok') and list(W.fills.values())[0]['canal'] == 'bloqueo'
    W = C.EngineBloqueo(StubE((5.0, T0 + 500, 'ok')), activo=True, fuente=lambda k: (own, comp)); r = W.run_segment(0, 0.19, T0, T0 + 5000, 5.0, 'BASE')
    assert r == (5.0, T0 + 500, 'ok') and W.cont['bloqueo_ignorado_print_previo'] == 1 and list(W.fills.values())[0]['canal'] == 'print_nd'     # stub sin cinta
def test_seria_taker_no_busca_bloqueo():
    own, comp = mk([(T0 - 5000, 0.70, 0.72, 30, 30), (T0 + 1000, 0.81, 0.83, 7, 9)])
    W = C.EngineBloqueo(StubE((0.0, None, 'seria_taker')), activo=True, fuente=lambda k: (own, comp)); assert W.run_segment(0, 0.19, T0, T0 + 5000, 5.0, 'BASE')[0] == 0.0
def test_clasifica_print_TT_nivel_nd():
    pr = (np.array([100, 500]), np.array([0.19, 0.17]))
    assert C.clasifica_print(pr, 0.19, 100) == 'print_nivel' and C.clasifica_print(pr, 0.19, 450) == 'TT' and C.clasifica_print(pr, 0.19, 300) == 'print_nd' and C.clasifica_print(None, 0.19, 1) == 'print_nd'
def test_integracion_b_policy_sim_con_canal_bloqueo():
    import test_b_real_sim as TB, b_policy_sim as BS
    FIN = TB.FIN; t0 = TB.T0
    ru = [(t0 - 400000, 0.22, 0.24)]; rd = [(t0 - 400000, 0.70, 0.72)]
    st = TB.Stub([('eth', ru, rd)])
    comp = S([(t0 - 400000, 0.70, 0.72, 30, 30), (t0 + 20000, 0.81, 0.83, 7.0, 9)]); own = S([(t0 - 400000, 0.22, 0.24, 50, 40)])
    W = C.EngineBloqueo(st, activo=True, fuente=lambda k: (own, comp) if k == 0 else (None, None))
    BS.G.capt_outcome = lambda E, k: E.capt.outcome(E.D, k)
    R, cov = BS.run_day('x', TB.P0, E=W); R['dia'] = 'x'
    f = R[R.q > 0]; assert len(f) == 1 and f.tf.iloc[0] == t0 + 20000 and f.q.iloc[0] == f['size'].iloc[0] or f.q.iloc[0] <= f['size'].iloc[0]
    A = C.anota_ordenes(R, W, lambda k: own if k == 0 else comp); assert (A[A.q > 0].canal == 'bloqueo').all() and set(A.tercil) <= {'bajo', 'medio', 'alto', 'inval'}
    cen = C.censo(A, por=('dia', 'coin')); assert cen[0]['n_bloqueo'] == 1 and cen[0]['n_rellenos'] == 1 and cen[0]['n_TT'] == 0
    # flag apagado: el mismo replay NO produce relleno (el stub no tiene prints) -> los resultados previos no cambian
    R0, _ = BS.run_day('x', TB.P0, E=C.EngineBloqueo(TB.Stub([('eth', ru, rd)]), activo=False)); assert (R0.q > 0).sum() == 0

# ---- F5_t / censo / cordura
def test_f5t_invalido_no_se_imputa_y_cortes():
    s = S([(T0, 0.2, 0.3, 1, np.expm1(C.C0)), (T0 + 100000, 0.2, 0.3, 1, np.expm1(C.C1) + 1)])
    assert C.f5t(s, T0 - 1) is None and C.tercil(None) == 'inval' and C.f5t(s, T0 + 31000) is None and C.f5t(s, T0 + 100) is not None
    assert C.tercil(C.C0) == 'bajo' and C.tercil(C.C0 + 1e-9) == 'medio' and C.tercil(C.C1) == 'medio' and C.tercil(C.C1 + 1e-9) == 'alto'
    assert abs(C.f5t(s, T0 + 100) - C.C0) < 1e-6
def test_cordura_dt0_permitido_y_violacion():
    own, comp = mk([(T0 - 5000, 0.70, 0.72, 30, 30), (T0 + 1000, 0.81, 0.83, 7, 9)]); f = lambda k: (own, comp)
    base = dict(dia='d', coin='eth', k=0, L=0.19, t_arr=T0, t_end=T0 + 9000, rem=5.0)
    fil, res = C.cordura([dict(base, real_tm3=T0 + 990)], f); assert res['n_dt0'] == 1 and res['n_violaciones'] == 0 and res['pasa']          # evento a dt~0 del relleno real
    fil, res = C.cordura([dict(base, real_tm3=T0 + 6000)], f); assert res['n_violaciones'] == 1 and not res['pasa']                           # evento con la orden real viva y SIN relleno cercano
    fil, res = C.cordura([dict(base, real_tm3=nan)], f); assert res['n_violaciones'] == 1
    fil, res = C.cordura([dict(base, real_tm3=nan), dict(base, k=1)], lambda k: (own, comp) if k == 0 else (None, None)); assert res['sin_serie'] == 1 and not res['pasa']
    fil, res = C.cordura([], f); assert res['status'] == 'BLOCKED'

# ---- (b)
def ordenes(rows): return pd.DataFrame(rows, columns=['tercil', 'q', 'cost', 'pnl'])
def test_estres_uniforme_aritmetica_y_no_doble_conteo():
    R = ordenes([('bajo', 5, 1.0, 0.5), ('bajo', 0, 0, 0), ('medio', 5, 1.0, -1.0), ('alto', 5, 1.0, -0.5)] + [('bajo', 0, 0, 0)] * 96)         # 100 ordenes; 3 rellenos, coste medio 1,0
    o = K.estres_none(R, tasa=0.02, ev_none=-0.115)
    assert o['bajo']['n_ordenes'] == 98 and abs(o['bajo']['n_none_esperadas'] - 1.96) < 1e-9 and abs(o['bajo']['pnl_none'] - 1.96 * 1.0 * -0.115) < 1e-9
    assert abs(o['bajo']['EV_con_estres'] - (0.5 + 1.96 * -0.115) / (1.0 + 1.96)) < 1e-9                                                        # misma tasa en todos los terciles
    assert o['_params']['uniforme'] and K.ETIQUETA.startswith('RELLENOS VISIBLES') and abs(o['medio']['n_none_esperadas'] - 0.02) < 1e-9 and abs(o['alto']['n_none_esperadas'] - 0.02) < 1e-9
    assert abs(sum(o[t]['pct_ordenes'] for t in ('bajo', 'medio', 'alto')) - 1) < 1e-9
    assert abs(o['bajo']['p_relleno'] - 1 / 98) < 1e-9 and np.isnan(ordenes([('bajo', 0, 0, 0)]).pipe(K.estres_none)['bajo']['EV_visible'])           # sin rellenos: NaN, no 0
    assert len(K.rejilla_estres(R)) == 6
def test_estres_inval_aparte():
    R = ordenes([('inval', 5, 1.0, 1.0), ('bajo', 5, 1.0, 1.0)]); o = K.estres_none(R); assert 'inval' in o and o['inval']['n_ordenes'] == 1

# ---- (c)
def fix_oct():
    r = []
    def add(n, dia, c1, mk, tt, hit, tp, pnl, cost):
        for _ in range(n): r.append(dict(oid=len(r), dia=dia, c1=c1, mk=mk, tt=tt, hit=hit, tp=tp, pnl=pnl, cost=cost))
    add(2, '2026-10-21', True, True, True, 0.0, False, -0.5, 1.0); add(1, '2026-10-21', True, True, False, 1.0, False, 0.5, 1.0); add(3, '2026-10-22', True, True, False, 0.0, False, -1.0, 1.0)
    add(2, '2026-10-23', True, False, False, nan, False, -1.0, 1.0); add(1, '2026-10-22', True, False, False, nan, False, -1.0, 1.0); add(4, '2026-10-21', False, True, False, 0.0, True, 1.0, 1.0)
    return pd.DataFrame(r)
def test_sin_l2_con_y_sin_23oct_y_no_imputa():
    o = K.trata_sin_l2(fix_oct()); c, s = o['CON_23oct'], o['SIN_23oct']
    assert c['SIN_L2']['n'] == 3 and s['SIN_L2']['n'] == 1 and c['SIN_L2']['EV'] == -1.0 and c['SIN_L2']['pnl'] == -3.0
    assert c['TT']['n'] == 2 and c['REST']['n'] == 1 and c['NONE_L2']['n'] == 3 and c['TP']['n'] == 4 and c['clase1_total']['n'] == 9 and s['clase1_total']['n'] == 7
    assert s['NONE_L2']['n'] == 3 and 'SIN_L2' in c and 'imputado' in o['_nota']                # los SIN_L2 no engrosan NONE ni TP
def test_unidades_tk():
    T = pd.DataFrame(dict(tk_tipo=['compra_comp'] * 4, tk_sz=[12.0, 8, 40, 15], tk_rem=[0.5, 0.375, 0.38, 0.34], tk_eq=[0.18, 0.26, 0.19, 0.22], real_q=[6.0, 5, 6, 5]))
    r = K.verifica_unidades_tk(T); assert r['tk_rem_es_fraccion_0_1'] and r['unidad'] == 'acciones_no_refutada' and not r['unidad_resuelta']
    T2 = T.assign(tk_rem=[1.5, 0.1, 0.1, 0.1]); assert not K.verifica_unidades_tk(T2)['tk_rem_es_fraccion_0_1']
    T3 = T.assign(tk_sz=[1.0] * 4, tk_eq=[0.1] * 4, tk_rem=[0.0] * 4, real_q=[5.0] * 4); r3 = K.verifica_unidades_tk(T3); assert r3['unidad'] == 'USDC' and r3['unidad_resuelta']       # acciones refutada (1 < 5), USDC (10 >= 5) compatible
    assert K.verifica_unidades_tk(T.assign(tk_tipo='vende_propio'))['n'] == 0

# ---- (d)
def test_error_tiempo_tp():
    n = 20; T = pd.DataFrame(dict(sim=[True] * n + [False] * 5, v3d_BASE_f_tf=[1000 + i * 10 for i in range(n)] + [-1] * 5, real_tm3=[1000.0 + i * 10 + (5 if i < 17 else 100) for i in range(n)] + [1.0] * 5,
                                  clase_suelo=['lo'] * 15 + ['hi'] * 5 + ['lo'] * 5))
    o = K.error_tiempo_tp(T); assert o['TODAS']['n'] == 20 and o['lo']['n'] == 15 and o['hi']['n'] == 5                        # los no-TP (sim False / tf -1) no entran
    assert o['lo']['p50'] == 5.0 and o['lo']['veredicto'].startswith('evaluable') and o['hi']['veredicto'].startswith('NO_VALIDADO')
    assert o['TODAS']['p90'] > 74 and o['TODAS']['veredicto'].startswith('INSUFFICIENT') and o['TODAS']['p90_le_74'] is False and o['TODAS']['p90_le_147'] is True
    assert o['lo']['flag_estricto_p90_gt_Lp50'] is False
def test_clase_suelo_causal():
    n = 4000; rx = np.arange(n) * 300 + 10_000_000; d = np.full(n, 19, np.int64); t = int(rx[-1] + 20_000)
    assert C.clase_suelo_en(rx, d, t) == 'lo'
    assert C.clase_suelo_en(rx, np.full(n, 39, np.int64), t) == 'hi' and C.clase_suelo_en(rx, np.full(n, 100, np.int64), t) == 'indet'
    rx2 = np.concatenate([rx, [t + 1]]); d2 = np.concatenate([d, [39]]); assert C.clase_suelo_en(rx2, d2, t) == 'lo'          # una fila con rx >= t nunca cambia la clase
    D = types.SimpleNamespace(t0=0, _otro=np.array([100, 200, -1, 300]), qt=np.array([80, 150, 0, 270]), qk=np.array([0, 0, 0, 1]), act=np.array(['ETH', 'SOL']))
    r_, d_ = C.suelo_por_coin(D, 'eth'); assert list(r_) == [100, 200] and list(d_) == [20, 50]                                       # sin rx no entra; solo el coin

# ---- runner: reanudacion idempotente, corrupcion de checkpoint, bloqueo
def test_runner_idempotente_corrupcion_y_bloqueado():
    import sec7_run as RU; RU.OUT = TMP + '/run/'; os.makedirs(RU.OUT, exist_ok=True); llamadas = []
    def fn(d):
        llamadas.append(d); json.dump(dict(v=len(llamadas)), open(RU.OUT + f'o_{d}.json', 'w')); return dict(ok=1), dict(esperado=1)
    inp = {'x': HV + 'sec7_core.py'}
    assert RU.job('t', 'a', ['o_a.json'], fn, inp) == 'COMPLETE' and len(llamadas) == 1
    assert RU.job('t', 'a', ['o_a.json'], fn, inp) == 'COMPLETE' and len(llamadas) == 1                                          # reanudar: no recalcula
    open(RU.OUT + 'o_a.json', 'w').write('{"v": 999}'); assert RU.job('t', 'a', ['o_a.json'], fn, inp) == 'COMPLETE' and len(llamadas) == 2   # output corrupto/alterado: recalcula
    open(RU.mpath('t', 'a'), 'w').write('{no json'); assert RU.job('t', 'a', ['o_a.json'], fn, inp) == 'COMPLETE' and len(llamadas) == 3     # manifest corrupto
    m = json.load(open(RU.mpath('t', 'a'))); assert m['status'] == 'COMPLETE' and 'code' in m and m['cobertura'] == dict(esperado=1) and m['outputs']['o_a.json']
    assert RU.job('t', 'b', ['o_b.json'], fn, {'x': '/no/existe'}) == 'BLOCKED' and len(llamadas) == 3 and json.load(open(RU.mpath('t', 'b')))['status'] == 'BLOCKED'
    def mal(d): raise ValueError('boom')
    assert RU.job('t', 'c', ['o_c.json'], mal, inp) == 'FAILED' and json.load(open(RU.mpath('t', 'c')))['status'] == 'FAILED'
    assert RU.final() in ('PARTIAL', 'BLOCKED', 'FAILED') and json.load(open(RU.OUT + 'run_manifest.json'))['status'] != 'COMPLETE'           # sin los 12 trabajos nunca es COMPLETE
def test_runner_ev_apagado_por_defecto_y_sin_ordenes():
    import sec7_run as RU; assert RU.EMITIR_EV is False
    src = open(HV + 'sec7_core.py').read() + open(HV + 'sec7_run.py').read() + open(HV + 'sec7_calculos.py').read()
    for prohibido in ('post_order', 'create_order', 'py_clob_client', 'dotenv', 'live/.env', 'private_key', 'requests.', 'urlopen'): assert prohibido not in src, prohibido
if __name__ == '__main__':
    ts = [(n, f) for n, f in sorted(globals().items()) if n.startswith('test_') and callable(f)]
    try:
        for n, f in ts: f(); print('OK', n)
        print(len(ts), 'tests OK')
    finally: shutil.rmtree(TMP, ignore_errors=True)
