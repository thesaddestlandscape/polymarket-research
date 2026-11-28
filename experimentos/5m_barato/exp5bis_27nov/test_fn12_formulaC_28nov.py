"""Tests de FN12 con la formula C (fn12_brazo_lcancel_28nov.tabla_c). python3 -m pytest -q test_fn12_formulaC_28nov.py"""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fn12_brazo_lcancel_28nov as F
import latencias_vigentes as LVm


def test_clasifica_umbrales_y_offset_arr_irreducible():
    assert F.clasifica(10, 20, 21, 'offset_post') == 'flip_seguro'                    # hi < ext
    assert F.clasifica(10, 20, 20, 'offset_post') == 'flip_posible'                   # lo < ext <= hi
    assert F.clasifica(10, 20, 10, 'offset_post') == 'sin_flip'                       # lo >= ext
    assert F.clasifica(-144, -123, 500, 'offset_arr<=100ms') == 'ambigua_irreducible' # el casado es anterior a t_arr: no depende de L_cancel


@pytest.mark.skipif(not os.path.exists(F.O + 'ordenes_K6_base_2026-11-24.pkl'), reason='datos del 27-Nov no disponibles')
def test_tabla_c_denominador_12_formula_c_y_brazos():
    LV = LVm.carga(); T = F.tabla_c(LV)
    assert len(T) == 12 and set(T.clase) == {'lo'} and set(T.coin) <= {'ETH', 'SOL', 'XRP'}                    # denominador 12, por moneda y clase (hoy todas lo)
    assert (T.causa.str.startswith('offset_arr')).sum() == 1 and (T.central_rx == 'ambigua_irreducible').sum() == 1
    # monotonia: un L_cancel mayor nunca reduce los flips (mismos 12, misma base)
    orden = {'sin_flip': 0, 'flip_posible': 1, 'flip_seguro': 2, 'ambigua_irreducible': 3}
    for _, r in T.iterrows():
        if r.central_rx == 'ambigua_irreducible': continue
        v = [orden[r[b]] for b in ('central_rx', 'L119_no_medido', 'L147_heredado', 'estres_202', 'estres_1320')]
        assert v == sorted(v), (r.mid, v)
    R = F.resumen_c(T, LV, {})
    assert R['denominador'] == 12 and sum(R['brazos']['central_rx']['total'].values()) == 12 and R['latencias_vigentes_sha256'] == LV['sha256_contenido']
    assert all('rotulo' in b for b in R['brazos'].values())
