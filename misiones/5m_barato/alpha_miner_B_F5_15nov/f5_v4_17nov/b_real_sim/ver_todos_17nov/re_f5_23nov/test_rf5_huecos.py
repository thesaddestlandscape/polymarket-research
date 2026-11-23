"""test_rf5_huecos.py -- ESPEC E5: dia sintetico con hueco de 30 s excluye EXACTAMENTE las ordenes solapadas; fail-closed ante dato ausente; FRAGIL_HUECOS si cambia el signo en >=2 de 3 monedas."""
import os, sys
import numpy as np, pandas as pd, pytest
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import rf5_huecos as HU

def test_hueco_30s_excluye_exactamente_las_ordenes_solapadas():
    rx = np.concatenate([np.arange(0, 100_000, 500), np.arange(130_000, 300_000, 500)])             # hueco de 30 s: (99_500, 130_000)
    g = {'eth': HU.huecos(rx)}; assert g['eth'] == [(99_500, 130_000)]
    R = pd.DataFrame([dict(coin='eth', t_dec=t, fin=f, mid=f'm{i}', dia='d', pol='base', bloq=0) for i, (t, f) in enumerate([(10_000, 60), (50_000, 105), (110_000, 200), (131_000, 250), (140_000, 200)])])   # fin en s
    h = HU.marca_huecos(R, g); assert list(h) == [False, True, True, False, False]            # la 2.a vive hasta 105 s (>99,5 s), la 3.a empieza dentro del hueco; la 1.a acaba a 60 s; la 4.a/5.a empiezan despues
    R['hueco'] = h; ex = HU.mercados_excluidos(R); assert ex == {('d', 'm1'), ('d', 'm2')} and len(HU.excluye(R, ex)) == 3

def test_fail_closed_dato_ausente_se_excluye_nunca_se_imputa():
    assert HU.huecos(None) is None and HU.huecos([]) is None and HU.solapa(0, 1, None) is True
    R = pd.DataFrame([dict(coin='xrp', t_dec=1000, fin=10, mid='m', dia='d', pol='base', bloq=0), dict(coin='eth', t_dec=np.nan, fin=10, mid='n', dia='d', pol='base', bloq=0)]); h = HU.marca_huecos(R, {'eth': [], 'xrp': []})
    assert list(h) == [False, True]                                                          # t_dec ausente => se excluye
    assert list(HU.marca_huecos(R, {'eth': []})) == [True, True]                             # moneda sin huecos calculados (sin datos) => excluir
    with pytest.raises(ValueError): HU.excluye(R.drop(columns=[], errors='ignore'), None)
    assert HU.mercados_excluidos(R) is None                                                  # sin columna hueco => None => sensibilidad imposible

def test_fragil_si_cambia_el_signo_en_2_de_3_monedas():
    assert HU.veredicto_fragil(dict(eth=.1, sol=.1, xrp=.1), dict(eth=.1, sol=.2, xrp=.3))['estado'] == 'OK_HUECOS'
    assert HU.veredicto_fragil(dict(eth=.1, sol=.1, xrp=.1), dict(eth=-.1, sol=.2, xrp=.3))['estado'] == 'OK_HUECOS'
    assert HU.veredicto_fragil(dict(eth=.1, sol=.1, xrp=.1), dict(eth=-.1, sol=-.2, xrp=.3))['estado'] == 'FRAGIL_HUECOS'
    assert HU.veredicto_fragil(dict(eth=.1, sol=.1, xrp=.1), dict(eth=-.1, sol=None, xrp=.3))['estado'] == 'FRAGIL_HUECOS'              # dato ausente cuenta como cambio

def test_gaps_de_motor_por_moneda():
    import types
    qt = np.concatenate([np.arange(0, 20_000, 1000), np.arange(40_000, 60_000, 1000)]).astype(np.int64)
    E = types.SimpleNamespace(ks=[0, 1], K=types.SimpleNamespace(qt=qt, qb=np.array([0, 20, 40])), D=types.SimpleNamespace(act=['ETH', 'ETH']))
    assert HU.gaps_de_motor(E) == {'eth': [(19_000, 40_000)]}
    assert HU.gaps_binance({'eth': (np.array([0, 1000, 9000]), None)}) == {'eth': [(1000, 9000)]}

def test_sensibilidad_eval_sin_columna_none_y_con_huecos_estructura():
    import rf5_eval as EV, rf5_core as K5
    from test_rf5 import _sint
    R, F, est = _sint(10); C = K5.lee_cortes(); assert EV.sensibilidad_huecos(R, F, C) is None                    # sin marca de huecos: no hay sensibilidad (fail-closed)
    h = R.assign(hueco=False); sh = EV.sensibilidad_huecos(h, F, C); assert sh['n_mercados_excluidos'] == 0 and sh['A']['F3']['estado'] == 'OK_HUECOS'
    # excluir todos los mercados de eth y sol con f5 alto no cambia el signo de F3 (mismo efecto) pero si se excluyen TODOS los lados vetados el Delta de F3 desaparece
    f5 = F[(F.pol == 'base')].set_index(['dia', 'mid']).f5_0; vet = {(r.dia, r.mid) for r in R[R.pol == 'base'].itertuples() if K5.veta_f5('F3', r.coin, (None if not np.isfinite(f5[(r.dia, r.mid)]) else f5[(r.dia, r.mid)]), C)}
    hh = R.assign(hueco=[(a, b) in vet for a, b in zip(R.dia, R.mid)]); s2 = EV.sensibilidad_huecos(hh, F, C)
    assert s2['n_mercados_excluidos'] == len(vet) and s2['A']['F3']['estado'] == 'FRAGIL_HUECOS' and all(v['cambia_signo'] for v in s2['A']['F3']['por_moneda'].values())
    a = dict(delta=0.1, ic90_dias=[0.05, 0.2], ic90_cierres=[0.04, 0.2], nulo_exacto=True, p_max_global=0.01, pct_dias_pos=0.9, delta_sin_2_mejores_dias=0.05, delta_inversion=-0.1, p_azar=0.01)
    assert EV.veredicto_A('F3', a, dict(ok_banda=True), C, True, None, dict(estado='OK_HUECOS'))[0] == 'CONFIRMADA' and EV.veredicto_A('F3', a, dict(ok_banda=True), C, True, None, dict(estado='FRAGIL_HUECOS'))[0] == 'FRAGIL_HUECOS'
