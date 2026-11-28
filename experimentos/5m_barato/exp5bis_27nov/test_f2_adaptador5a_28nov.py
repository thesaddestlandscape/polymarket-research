import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import f2_adaptador5a_28nov as A


class _D:
    tokidx = {'tA': 1, 'tB': 2}


class FakeE:
    """run_segment(k, L, t_arr, t_end, size, modo) -> (q, tf, status): rellena 5 si la ventana contiene el instante 1000 (un print a t=1000)."""
    D = _D()
    llamadas = []

    def run_segment(self, k, L, ta, te, rem, modo):
        FakeE.llamadas.append((k, ta, te))
        return (5.0 if ta <= 1000 <= te else 0.0, None, 'ok')


def fila(tok='tA', motivo='cancel_bid<L', t_dec=900, t_arr=968, t_end=1000 - 1, t_trig=939, coin='ETH', mid='m1', lado='YES', q3=0.0):
    return dict(tok=tok, mid=mid, coin=coin, lado=lado, L=0.2, t_dec=t_dec, t_arr=t_arr, t_end=t_end, t_trig=t_trig, motivo=motivo, rem=5.0, q3=q3, fin=0)


def test_tiempos_grabados_identidad_y_brazos():
    f = fila()
    assert A.tiempos(f) == (968, 999)
    assert A.tiempos(f, 34, 74) == (934, 939 + 74)
    # sin disparo o sin cancelacion el t_end grabado se conserva
    assert A.tiempos(fila(t_trig=None), 34, 74)[1] == 999
    assert A.tiempos(fila(motivo='gate_falso'), 34, 74)[1] == 999


def test_brazo_L_cancel_mas_lento_hace_flip_y_grabado_no():
    E = FakeE(); fs = [fila()]
    assert A.corre(E, fs)[0] == 0.0                         # grabado: t_end 999 < print 1000
    assert A.corre(E, fs, 34, 74)[0] == 5.0                 # cancel efectivo 1013 > 1000: el print llega a la orden viva


def test_token_fuera_del_motor_es_nan_no_cero():
    q = A.corre(FakeE(), [fila(tok='BTCtok', coin='BTC')])
    assert np.isnan(q[0])
    assert len(A.unidades([fila(tok='BTCtok', coin='BTC')], q)) == 0


def test_guarda_t_arr_ge_t_end_solo_en_brazos_no_en_identidad():
    FakeE.llamadas.clear(); f = fila(t_arr=1005, t_end=999)
    A.corre(FakeE(), [f]); assert len(FakeE.llamadas) == 1          # identidad: se llama al motor igual que el replay 1c
    FakeE.llamadas.clear(); A.corre(FakeE(), [fila(t_dec=2000, t_trig=2100, t_end=2160)], 34, 74); assert FakeE.llamadas[0][1] == 2034


def test_unidades_primer_relleno_mercado_lado_y_conteos_pareados():
    fs = [fila(mid='m1', q3=1.0), fila(mid='m1', q3=0.0), fila(mid='m2', q3=0.0, coin='SOL')]
    q = np.array([5.0, 0.0, 0.0])
    c = A.conteos(A.unidades(fs, q))
    assert c['ETH'] == dict(unidades=1, v3=1, v4=1, ambos=1, v3_no_v4_si=0, v3_si_v4_no=0)
    assert c['SOL']['unidades'] == 1 and c['SOL']['v4'] == 0


# ---------------------------------------------------------------- 28-Nov: formula C (REDTEAM C)
import latencias_vigentes as LVm


def test_formula_c_suma_d_post_l_alta_y_d_det_l_cancel_rx():
    P = dict(d_post=75.0, l_alta_rx=67.0, d_det=0.0, l_cancel_rx=59.0)
    f = fila(t_dec=900, t_trig=939)
    assert A.tiempos_c(f, P) == (900 + 75 + 67, 939 + 0 + 59)                               # t_arr = dec + D_post + L_alta_rx ; t_end = trig + D_det + L_cancel_rx
    assert A.tiempos_c(fila(t_trig=None), P)[1] == 999 and A.tiempos_c(fila(motivo='gate_falso'), P)[1] == 999       # sin disparo / sin cancelacion: t_end grabado


def test_brazos_c_desde_latencias_vigentes_btc_missing_y_fijos_a_rx():
    LV = LVm.carga(); B = A.brazos_c(LV)
    assert set(B) == {'central_rx', 'central_dpost_p90', 'L119_no_medido', 'L147_heredado', 'estres_202', 'estres_1320'}                # 74 FUERA
    for c in ('ETH', 'SOL', 'XRP'):
        cc = LV['L_cancel_central'][c]; off = cc['rx_ms'] - cc['ex_ms']
        assert B['central_rx'][c]['l_cancel_rx'] == cc['rx_ms'] and B['central_rx'][c]['d_post'] == LV['D_post']['p50'] and B['central_dpost_p90'][c]['d_post'] == LV['D_post']['p90']
        assert abs(B['L147_heredado'][c]['l_cancel_rx'] - (147.0 + off)) < 1e-9 and abs(B['estres_1320'][c]['l_cancel_rx'] - (1320.0 + off)) < 1e-9        # ex -> rx con el offset medido de la moneda
    assert all(v is None for v in [LV['L_cancel_central']['BTC']['rx_ms']]) and 'BTC' not in B['central_rx']


def test_corre_formula_c_btc_o_sin_central_es_nan_y_la_llegada_mas_tardia_cambia_el_resultado():
    E = FakeE(); fs = [fila()]
    rapida = dict(d_post=0.0, l_alta_rx=34.0, d_det=0.0, l_cancel_rx=74.0)
    lenta = dict(d_post=75.5, l_alta_rx=67.0, d_det=0.0, l_cancel_rx=59.0)
    assert A.corre(E, fs, fc=lambda c: rapida)[0] == 5.0                                      # t_arr 934 <= 1000 <= t_end 1013
    assert A.corre(E, fs, fc=lambda c: lenta)[0] == 0.0                                       # t_arr = 900 + 75,5 + 67 = 1042 > 1000: la orden llega DESPUES del print (la formula C no la deja rellenarse)
    assert np.isnan(A.corre(E, fs, fc=lambda c: None)[0])                                     # moneda sin latencia medida (BTC): missing, nunca 0
    assert np.isnan(A.corre(E, [fila(tok='BTCtok', coin='BTC')], fc=lambda c: lenta)[0])
