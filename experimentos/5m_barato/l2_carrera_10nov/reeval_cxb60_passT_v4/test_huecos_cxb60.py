import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import huecos_cxb60 as H

def test_vac_max_con_hueco_de_30s_y_denso():
    fin = 1000; rx = np.concatenate([np.arange((fin - 300) * 1000, (fin - 200) * 1000, 400), np.arange((fin - 170) * 1000, fin * 1000 + 1, 400)])   # hueco de ~30 s dentro de la ventana
    assert abs(H.vac_max_mercado(rx, fin) - 30.0) < 0.5
    assert H.vac_max_mercado(np.arange((fin - 300) * 1000, fin * 1000 + 1, 400), fin) < 1.0
    assert H.vac_max_mercado(np.array([(fin - 300) * 1000 + 100_000]), fin) == 200.0                     # un solo mensaje: el mayor tramo ciego es 200 s (borde final)
    assert H.vac_max_mercado(None, fin) == 300.0 and H.vac_max_mercado(np.array([5]), fin) == 300.0      # sin filas en la ventana => toda la ventana ciega

def test_excluye_fail_closed():
    assert H.excluye_mercados({'a': 4.9, 'b': 5.0, 'c': None, 'd': float('nan'), 'e': 0.2}) == {'b', 'c', 'd'}
