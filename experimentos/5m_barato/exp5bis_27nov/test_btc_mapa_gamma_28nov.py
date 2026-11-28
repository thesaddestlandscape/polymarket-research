import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import btc_mapa_gamma_28nov as B
import sin_mapar_A_28nov as S


def test_mapa_extra_solo_btc_5m_y_slugs_validos():
    g = S.rejilla('2026-11-18', 'btc', '5m')
    cache = {g[0][0]: dict(tokens=['a', 'b'], version='v1', end=g[0][2]), g[1][0]: dict(tokens=['c', 'd'], version='v2', end=g[1][2]),
             S.rejilla('2026-11-18', 'btc', '15m')[0][0]: dict(tokens=['x', 'y'], version='v1', end=1), 'eth-updown-5m-1': dict(tokens=['e', 'f'], version='v1', end=1)}
    m = B.mapa_extra_btc('2026-11-18', cache)
    assert m == {'a': 'btc', 'b': 'btc', 'c': 'btc', 'd': 'btc'}                  # no 15m, no otras monedas; slugs sin registro no aportan


def test_otras_monedas_identicas_y_detecta_cambio():
    prev = {'eth': dict(estado='COMPLETE', filas_F_v2=5, filas_F_v3=0, join=0.99), 'sol': dict(estado='COMPLETE', filas_F_v2=0, filas_F_v3=7, join=0.98)}
    assert B.compara_otras_monedas(dict(prev, btc=dict(estado='COMPLETE')), prev) == (True, [])
    nuevo = {k: dict(v) for k, v in prev.items()}; nuevo['sol']['join'] = 0.5
    ok, dif = B.compara_otras_monedas(nuevo, prev); assert not ok and dif[0][:2] == ('sol', 'join')
