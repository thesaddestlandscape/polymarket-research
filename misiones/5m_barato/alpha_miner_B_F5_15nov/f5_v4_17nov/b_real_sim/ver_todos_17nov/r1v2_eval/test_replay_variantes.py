#!/usr/bin/env python3
"""test_replay_variantes.py -- hooks de cancelacion/no-armar dentro del replay de la politica REAL de B (stubs; sin datos de produccion). Ejecutar: python3 test_replay_variantes.py"""
import sys, os, types
import numpy as np, pandas as pd
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import replay_variantes as RV, variantes_b as VB
import test_b_real_sim as TB, b_policy_sim as BS
t0 = TB.T0; FIN = TB.FIN
BS.G.capt_outcome = lambda E, k: E.capt.outcome(E.D, k)
def stub(prints=None, gana=1.0, ru=None, rd=None, coin='eth'):
    ru = ru or [(t0 - 400000, 0.22, 0.24)]; rd = rd or [(t0 - 400000, 0.70, 0.72)]; return TB.Stub([(coin, ru, rd)], prints=prints or {0: [(t0 + 20000, 0.19)]}, gana=gana)
def run(f, st, HK=None, P=TB.P0):
    if f is BS.run_day: return f('x', P, E=st)[0]
    return f('x', P, E=st, HK=HK)[0]
def ser(ticks): t = np.array([a for a, _ in ticks], np.int64); p = np.array([b for _, b in ticks], float); return {'eth': (t, p)}
COLS = ['mid', 'lado', 'L', 'size', 't_dec', 't_arr', 'q', 'tf', 'motivo_fin', 'n_ord']

def test_parche_anclas_y_equivalencia_textual():
    txt = open(RV.SRC).read(); p = RV.parchea(txt); assert RV.verifica_parche(txt, p) and p.count('# [HOOK]') == 5 and RV.MOD.sha_origen == RV.SHA_SRC
    assert not RV.verifica_parche(txt, p.replace('size = tamano_orden(objetivo, 5, 1.0)', 'size = tamano_orden(objetivo, 5, 2.0)'))                 # cualquier cambio fuera de las lineas [HOOK] se detecta
    for a in (RV.A_ALTA, RV.A_VIDA, RV.A_EVT, RV.A_SIG):
        try: RV.parchea(txt.replace(a, 'XX', 1) if txt.count(a) == 1 else txt + a); assert False
        except ValueError: pass                                                                                                                      # ancla ausente o duplicada: fail-closed
    old = RV.SHA_SRC; RV.SHA_SRC = '0' * 64
    try: RV.carga(); assert False
    except ValueError: pass
    finally: RV.SHA_SRC = old
def test_sin_hook_identico_al_original_en_varios_escenarios():
    esc = [stub(), stub(prints={}), stub(ru=[(t0 - 400000, 0.22, 0.24), (t0 - 5000, 0.24, 0.26)], rd=[(t0 - 400000, 0.70, 0.72), (t0 - 5000, 0.68, 0.70)], prints={0: [(t0 + 40000, 0.21)]}),
           stub(ru=[(t0 - 400000, 0.22, 0.24), (t0 + 60000, 0.30, 0.32)], rd=[(t0 - 400000, 0.70, 0.72), (t0 + 60000, 0.62, 0.64)], prints={0: [(t0 + 100000, 0.21)]}, gana=0.0)]
    for e in esc:
        a = run(BS.run_day, e); b = run(RV.run_day, e, None); c = run(RV.run_day, e, RV.HookBase()); assert len(a) >= 1
        for x in (b, c): pd.testing.assert_frame_equal(a[COLS].reset_index(drop=True), x[COLS].reset_index(drop=True))
def tf_base(): return int(run(BS.run_day, stub()).tf.iloc[0])
def test_binance_cancel_efectividad_frontera_y_mercado_cerrado():
    tf = tf_base(); assert tf == t0 + 20000
    for tp in (0, 30):
        for delta, quita in ((0, True), (-1, False)):               # tau + tp + 74 + 20 == tf -> se anula; un ms mas tarde -> el relleno ya ocurrio
            tau = tf - (tp + 74 + 20) - delta if True else 0; tau = tf - (tp + 74 + 20) + (0 if quita else 1)
            S = ser([(tau - 1500, 100.0), (tau, 99.90)]); HK = RV.HookBinance(S, VB.V5, tp); R = run(RV.run_day, stub(), HK)
            assert HK.cont['vidas_con_disparo'] == 1
            assert VB.cancela_a_tiempo(tau, tf, tp) == quita                                                         # misma regla que variantes_b
            if quita: assert (R.q > 0).sum() == 0 and R.motivo_fin.iloc[-1] == 'regla' and len(R) == 1
            else: assert (R.q > 0).sum() == 1 and R.tf.iloc[0] == tf
def test_binance_sin_disparo_antes_de_llegada_ni_lado_contrario():
    tf = tf_base(); HKb = RV.HookBinance(ser([(1, 100.0), (2, 100.0)]), VB.V5, 0); base = run(RV.run_day, stub(), HKb); assert (base.q > 0).sum() == 1 and not HKb.cont['vidas_con_disparo']
    tau = tf - 200; S = ser([(tau - 1500, 100.0), (tau, 100.10)])                                                   # sube: adverso solo para Down; la orden es YES
    HK = RV.HookBinance(S, VB.V5, 0); R = run(RV.run_day, stub(), HK); assert (R.q > 0).sum() == 1 and not HK.cont['vidas_con_disparo']
    S2 = ser([(t0 - 100000 - 1500, 100.0), (t0 - 100000, 99.90)]); HK = RV.HookBinance(S2, VB.V5, 0); R = run(RV.run_day, stub(), HK); assert (R.q > 0).sum() == 1                  # salto previo a la llegada: no cancela la viva
def test_binance_no_armar_retrasa_el_alta_hasta_levantar_la_ventana():
    base = run(RV.run_day, stub(prints={}), None); td0 = int(base.t_dec.iloc[0]); tq = td0 - 300; tau = tq - 1000
    HK = RV.HookBinance(ser([(tau - 1500, 100.0), (tau, 99.90)]), VB.V5, 0); R = run(RV.run_day, stub(prints={}), HK)
    assert HK.cont['bloqueadas'] >= 1 and len(R) >= 1 and int(R.t_dec.iloc[0]) >= tau + VB.DELAY_ARMAR_MS + VB.V5['no_armar_ms'] and int(R.t_dec.iloc[0]) > td0
    HK6 = RV.HookBinance(ser([(tau - 3500, 100.0), (tau, 99.90)]), VB.V6, 0); R6 = run(RV.run_day, stub(prints={}), HK6); assert HK6.cont['bloqueadas'] >= 1          # V6: ventana 2068 ms tambien bloquea
def test_t_end_bloqueo_usa_reloj_exchange():
    fills = {(0, 0.19, 1000, 5000): dict(canal='bloqueo', t_ex=4960)}; h = RV.HookBase(); h.fills = lambda: fills
    o = dict(k=0, L=0.19, t_arr=1000, tf1=5000); assert h._t_end(o, 4000, 4000, 0, 74) == 4000 + 74 + 19 + 40                                           # se desplaza (tf1 - t_ex): tf1<=t_end <=> t_ex<=t_end_exchange
    o2 = dict(k=0, L=0.19, t_arr=1000, tf1=None); assert h._t_end(o2, 4000, 4000, 0, 74) == 4000 + 74 + 19
    h.fills = lambda: {(0, 0.19, 1000, 5000): dict(canal='print_nivel', t_ex=5000)}; assert h._t_end(o, 4000, 4000, 0, 74) == 4000 + 74 + 19
def mk_m(): return types.SimpleNamespace(ku=0, kd=1, coin='eth', fin=FIN)
def test_e1_gate_f5_regla_nan_y_contadores():
    from sec7_core import C0, C1
    def H(s, regla='ucb', c=0.02, **kw): return RV.HookE1(lambda m, k, t, L: s, regla, c, 0, **kw)
    m = mk_m(); assert H((C0 - 0.1, 0.1, 0.1)).no_armar(m, 0, 1000, 0.2) is False                                       # bajo y mu_ucb >= -c: se arma
    h = H((C1 + 0.1, 0.1, 0.1)); assert h.no_armar(m, 0, 1000, 0.2) and h.cont['bloq_f5_alto'] == 1
    h = H(None); assert h.no_armar(m, 0, 1000, 0.2) and h.cont['bloq_f5_inval'] == 1                                  # F5_t invalido = no operar
    h = H((C0 - 0.1, -0.5, -0.03)); assert h.no_armar(m, 0, 1000, 0.2) and h.cont['bloq_regla'] == 1                  # mu_ucb < -0,02
    assert not H((C0 - 0.1, -0.5, -0.02)).no_armar(m, 0, 1000, 0.2) and not H((C0 - 0.1, -0.5, -0.0199)).no_armar(m, 0, 1000, 0.2)    # frontera estricta: -0,02 NO es < -0,02
    assert H((C0 - 0.1, -0.5, 0.3), regla='mu').no_armar(m, 0, 1000, 0.2) and not H((C0 - 0.1, 0.0, -0.9), regla='mu').no_armar(m, 0, 1000, 0.2)   # V4 usa mu_hat, no el ucb
    h = H((C0 - 0.1, float('nan'), float('nan'))); assert not h.no_armar(m, 0, 1000, 0.2) and h.cont['rasgo_no_evaluable'] == 1        # NaN: la regla no se aplica (no es y=0)
    assert not H((C1 + 0.1, 0.1, 0.1), gate_f5=False).no_armar(m, 0, 1000, 0.2)
def test_e1_en_el_replay_bloquea_o_deja_igual_y_cancel_vida_exploratoria():
    from sec7_core import C0, C1
    base = run(RV.run_day, stub(), None); assert (base.q > 0).sum() == 1
    R = run(RV.run_day, stub(), RV.HookE1(lambda m, k, t, L: (C0 - 0.1, 0.1, 0.1), 'ucb', 0.02, 0)); pd.testing.assert_frame_equal(base[COLS].reset_index(drop=True), R[COLS].reset_index(drop=True))   # no dispara: replay identico
    R = run(RV.run_day, stub(), RV.HookE1(lambda m, k, t, L: (C1 + 1, 0.1, 0.1), 'ucb', 0.02, 0)); assert len(R) == 0                                                                    # tercil alto: nunca se coloca
    tf = tf_base(); tfire = tf - 94 - 600
    def punt(m, k, t, L): return (C0 - 0.1, 0.1, 0.1) if t < tfire else (C0 - 0.1, -0.5, -0.5)
    HK = RV.HookE1(punt, 'ucb', 0.02, 0, cancel_vida=True); R = run(RV.run_day, stub(), HK); assert HK.cont['vidas_con_disparo'] == 1 and (R.q > 0).sum() == 0 and R.motivo_fin.iloc[-1] == 'regla'                # exploratoria: cancela la viva
    HK = RV.HookE1(punt, 'ucb', 0.02, 0, cancel_vida=False); R = run(RV.run_day, stub(), HK); assert (R.q > 0).sum() == 1 or len(R) == 0                                                             # primaria: no cancela en vida
def test_seguridad():
    src = open(HV + 'replay_variantes.py').read()
    for p in ('post_order', 'create_order', 'py_clob_client', 'dotenv', 'live/.env', 'private_key', 'requests.', 'urlopen', 'pkill', 'pgrep'): assert p not in src, p
if __name__ == '__main__':
    ts = [(n, f) for n, f in sorted(globals().items()) if n.startswith('test_') and callable(f)]
    for n, f in ts: f(); print('OK', n)
    print(len(ts), 'tests OK')
