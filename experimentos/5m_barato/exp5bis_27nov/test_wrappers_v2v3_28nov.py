import os, sys, json
sys.dont_write_bytecode = True
RF5 = '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim/ver_todos_17nov/re_f5_23nov'
sys.path.insert(0, RF5)
import pytest
import cobertura_bruta_v2v3 as W
import vigia_rf5_v2v3 as VW


def _touch(p, txt='x'):
    os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w').write(txt); return p


def test_dia_solo_v2_usa_los_mismos_ficheros_del_sello_incluido_parcial(tmp_path):
    keep = str(tmp_path / 'keep') + '/'
    a = _touch(keep + 'onchain_fills_2026-11-18.csv.gz'); b = _touch(keep + 'onchain_fills_2026-11-18_parcial.csv.gz')
    d, usados = W.prepara_keep('2026-11-18', keep_v2=keep, base=str(tmp_path / 'k2') + '/')
    assert sorted(f for _, f in usados) == sorted([a, b]) and all(v == 'v2' for v, _ in usados)
    assert sorted(os.listdir(d)) == ['onchain_fills_2026-11-18.csv.gz', 'onchain_fills_2026-11-18_parcial.csv.gz']
    import glob
    assert len(glob.glob(d + 'onchain_fills_2026-11-18*.csv.gz')) == 2             # el glob de cobertura_bruta.calcula ve ambos


def test_dia_v3_incluye_cadena_v3_y_el_glob_del_sello_la_ve(tmp_path):
    v2 = _touch(str(tmp_path / 'o' / 'onchain_fills_2026-11-25.csv.gz')); v3 = _touch(str(tmp_path / 'o' / 'onchain_fills_v3_2026-11-25.csv.gz'))
    d, usados = W.prepara_keep('2026-11-25', keep_v2=str(tmp_path / 'vacio') + '/', base=str(tmp_path / 'k3') + '/', rutas=[('v2', v2), ('v3', v3)])
    import glob
    nombres = sorted(os.path.basename(f) for f in glob.glob(d + 'onchain_fills_2026-11-25*.csv.gz'))
    assert nombres == ['onchain_fills_2026-11-25.csv.gz', 'onchain_fills_2026-11-25_v3.csv.gz'] and {v for v, _ in usados} == {'v2', 'v3'}


def test_prepara_keep_reejecucion_no_acumula_ni_borra_originales(tmp_path):
    keep = str(tmp_path / 'keep') + '/'; a = _touch(keep + 'onchain_fills_2026-11-18.csv.gz')
    for _ in range(2): d, u = W.prepara_keep('2026-11-18', keep_v2=keep, base=str(tmp_path / 'k2') + '/')
    assert len(os.listdir(d)) == 1 and os.path.exists(a)


def test_dia_v3_sin_cadena_v3_falla_fuerte(tmp_path):
    with pytest.raises(FileNotFoundError):
        W.prepara_keep('2026-11-30', keep_v2=str(tmp_path) + '/', base=str(tmp_path / 'k') + '/')    # CV.rutas_cadena exige V3 desde 23-Nov


def test_identidad_bloqueada_para_dias_v3_y_sin_sellado(tmp_path):
    ok, m = W.identidad('2026-11-25'); assert not ok and 'BLOCKED' in m
    ok, m = W.identidad('2026-11-18', sellado=str(tmp_path / 'no_existe.json')); assert not ok and 'BLOCKED' in m


def test_vigia_R11_cadena_no_complete_en_dia_complete(tmp_path, monkeypatch):
    est = {'2026-11-25': dict(status='COMPLETE')}
    ruta = str(tmp_path / 'em_%s.json')
    json.dump({'eth': {'estado': 'COMPLETE'}, 'sol': {'estado': 'BLOCKED_V3'}, 'xrp': {'estado': 'COMPLETE'}}, open(ruta % '2026-11-25', 'w'))
    monkeypatch.setattr(VW, 'ESTADO', ruta)
    A = VW.avisos_v2v3(est, {'epoch': 1e12}, 100.0, hoy_='2026-11-26', ahora=1e12)
    firmas = [f for f, _ in A]
    assert 'R11_cadena_2026-11-25_sol' in firmas and 'R11_cadena_2026-11-25_eth' not in firmas
    assert all('0.' not in f for f in firmas if f.startswith('R11'))           # firma estable: sin valores recalculados
    A2 = VW.avisos_v2v3({'2026-11-20': dict(status='COMPLETE')}, {'epoch': 1e12}, 100.0, hoy_='2026-11-26', ahora=1e12)
    assert not any(f.startswith('R11') for f, _ in A2)                          # <= 22-Nov: sin cambios respecto al sellado
