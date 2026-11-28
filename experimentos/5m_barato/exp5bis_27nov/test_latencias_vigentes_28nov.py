"""Tests de latencias_vigentes.py (fuente unica). python3 -m pytest -q test_latencias_vigentes_28nov.py"""
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import latencias_vigentes as LV


def test_json_vigente_valido_y_trazable():
    d = LV.carga()
    assert d['sha256_contenido'] == LV.sello(d)
    for f in d['fuentes']:
        assert f['sha256'] != 'missing' and len(f['sha256']) == 64                       # cada fuente con su sha
    assert d['L_cancel_central']['BTC']['ex_ms'] is None and 'no_medido' in d['L_cancel_central']['BTC']['calidad']           # BTC no medido: nunca un numero inventado
    for c in ('ETH', 'SOL', 'XRP'):
        assert 25 < d['L_cancel_central'][c]['ex_ms'] < 60 and 50 < d['L_cancel_central'][c]['rx_ms'] < 80 and d['L_cancel_central'][c]['n'] >= 10
        assert LV.l_cancel_rx(d, c) == d['L_cancel_central'][c]['rx_ms'] and LV.l_alta_rx(d, c) > LV.l_cancel_rx(d, c) - 5
    assert 70 < d['D_post']['p50'] < 80 and d['D_post']['n'] >= 100
    assert set(d['brazos_L_cancel']) == {'74', '111', '119', '147', '202', '1320'} and d['brazos_L_cancel']['74']['rol'].startswith('intermedio_heredado')
    assert 'NO es una cancelacion' in d['brazos_L_cancel']['147']['origen'] and d['brazos_L_cancel']['119']['rol'] == 'no_medido'


def test_carga_falla_cerrado_si_editado_o_falta(tmp_path):
    d = json.load(open(LV.JSON_VIGENTE))
    d['L_cancel_central']['ETH']['rx_ms'] = 1.0                                          # edicion a mano
    p = tmp_path / 'x.json'
    p.write_text(json.dumps(d))
    with pytest.raises(LV.LatenciasInvalidas):
        LV.carga(str(p))
    with pytest.raises(LV.LatenciasInvalidas):
        LV.carga(str(tmp_path / 'no_existe.json'))


def test_central_reproducible_desde_anclas():
    """El central coincide con el recalculo desde las salidas de ancla (las mismas fuentes con sha)."""
    d = LV.carga()
    anclas = [f['fichero'] for f in d['fuentes'] if f['tipo'] == 'ancla_p1b_28nov']
    d2 = LV.construye(anclas)
    d2['sha256_contenido'] = None
    for k in ('L_cancel_central', 'L_alta_central', 'D_post', 'D_det_a_DELETE', 'por_moneda'):
        assert json.dumps(d2[k], sort_keys=True) == json.dumps(d[k], sort_keys=True), k
