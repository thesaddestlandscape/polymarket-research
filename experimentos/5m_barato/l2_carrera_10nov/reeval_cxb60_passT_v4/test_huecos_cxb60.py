import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import huecos_cxb60 as H

def test_vac_max_con_hueco_de_30s_y_denso():
    fin = 1000; rx = np.concatenate([np.arange((fin - 332) * 1000, (fin - 200) * 1000, 400), np.arange((fin - 170) * 1000, fin * 1000 + 1, 400)])   # hueco de ~30 s dentro de la ventana
    assert abs(H.vac_max_mercado(rx, fin) - 30.0) < 0.5
    assert H.vac_max_mercado(np.arange((fin - 332) * 1000, fin * 1000 + 1, 400), fin) < 1.0
    assert H.vac_max_mercado(np.array([(fin - 332) * 1000 + 100_000]), fin) == 232.0                     # un solo mensaje: el mayor tramo ciego es 232 s (borde final)
    assert H.vac_max_mercado(None, fin) == 332.0 and H.vac_max_mercado(np.array([5]), fin) == 332.0 and H.PRE_S == 332      # sin filas en la ventana => toda la ventana ciega

def test_excluye_fail_closed():
    assert H.excluye_mercados({'a': 4.9, 'b': 5.0, 'c': None, 'd': float('nan'), 'e': 0.2}) == {'b', 'c', 'd'}

def test_vac_max_seg_racha_de_segundos_sin_mensajes():
    fin = 1000; S = set(range(fin - 332, fin + 1)); assert H.vac_max_seg(S, fin) == 0
    S2 = S - set(range(fin - 100, fin - 60)); assert H.vac_max_seg(S2, fin) == 40 and H.vac_max_seg(set(), fin) == 333           # toda la ventana ciega (fail-closed)
    assert H.vac_max_seg(S - {fin}, fin) == 1 and H.vac_max_seg(np.array([fin - 5]), fin) == 327

def test_un_solo_pre_en_las_dos_medidas_y_feed_declarado():
    fin = 1000; assert H.vac_max_seg(set(), fin) == H.PRE_S + 1 and H.vac_max_mercado(None, fin) == H.PRE_S and H.FILAS_FEED == ('q', 't')
    import inspect; assert inspect.signature(H.vac_max_mercado).parameters['pre_s'].default == H.PRE_S == inspect.signature(H.vac_max_seg).parameters['pre_s'].default
