#!/usr/bin/env python3
"""Tests del vigia diario de la re-puja (sin red, sin datos reales; fixtures en tmp). Desde este directorio: python3 -m pytest -q test_vigia_h23_repuja.py
Cubre: validacion de salida (cabecera, duplicados, cobertura ausente/corrupta), reinicio idempotente, celda primaria, EV ponderado por EUR, sin 2 mejores dias, IC solo con >=5 dias,
emparejado r150-r1500 (placebo), missing != 0, gate (no medido != cumplido) y seguridad (sin ordenes/claves)."""
import csv, json, os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pytest
import vigia_h23_repuja as V


def fila(D, cierre, brazo, rep, lleno, coste, gana, rebate=0.0, sizing='real', modo='primer', cola='base', lp=79, lc=60):
    return dict(coin='BTC', dia=D, cierre=cierre, lado='Up', m5='m', brazo=brazo, sizing=sizing, modo=modo, rep=rep, cola=cola, lat_post=lp, lat_cancel=lc, n_cotiz=1, need=5, lleno=lleno,
                coste=coste, n_fill=1 if lleno else 0, t_rel='', p_rel='', gana=gana, rebate=rebate)


def escribe_dia(out, D, filas, cob=True, cabecera=None):
    with open(f'{out}v3_BTC_{D}.csv', 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cabecera or V.SIM_COLS, extrasaction='ignore')
        w.writeheader()
        w.writerows(filas)
    if cob:
        json.dump(dict(coin='BTC', dia=D, cierres_grupo=97, con_lado=80, con_libro=80, errores=0, sin_desenlace=0), open(f'{out}v3_cobertura_BTC_{D}.json', 'w'))


@pytest.fixture
def out(tmp_path, monkeypatch):
    o = str(tmp_path) + '/'
    monkeypatch.setattr(V, 'OUT', o)
    monkeypatch.setattr(V, 'VIG', o + 'vig/')
    monkeypatch.setattr(V, 'DL', o + 'dl/')
    monkeypatch.setattr(V, 'SHADOW_V3', o + 'sh/')
    return o


def test_validar_dia_casos(out):
    D = '2026-10-19'
    assert V.validar_dia(D)[:2] == (False, 'sin_csv')
    escribe_dia(out, D, [fila(D, 1, 'A', 150, 5, 1.5, 'True')], cob=False)
    assert V.validar_dia(D)[:2] == (False, 'csv_sin_cobertura')
    escribe_dia(out, D, [fila(D, 1, 'A', 150, 5, 1.5, 'True')])
    ok, why, info = V.validar_dia(D)
    assert ok and info['filas'] == 1 and info['con_libro'] == 80
    escribe_dia(out, D, [fila(D, 1, 'A', 150, 5, 1.5, 'True')] * 2)                       # clave duplicada
    assert V.validar_dia(D)[:2] == (False, 'clave_duplicada')
    escribe_dia(out, D, [fila(D, 1, 'A', 150, 5, 1.5, 'True')], cabecera=V.SIM_COLS[:-1] + ['otra'])
    assert V.validar_dia(D)[0] is False
    escribe_dia(out, D, [fila('2026-10-20', 1, 'A', 150, 5, 1.5, 'True')])                # fila de otro dia
    assert V.validar_dia(D)[:2] == (False, 'dia_incorrecto')
    open(f'{out}v3_cobertura_BTC_{D}.json', 'w').write('{truncado')
    assert V.validar_dia(D)[0] is False                                                    # cobertura corrupta


def test_ev_ponderado_por_euro_y_sin_2_mejores():
    pos = [dict(dia=f'2026-10-{19 + i}', pnl=p, coste=c, lleno=5, g=1.0 if p > 0 else 0.0) for i, (p, c) in enumerate([(3.0, 1.0), (-1.0, 1.0), (0.5, 2.0), (-2.0, 2.0), (1.0, 1.0), (-0.5, 0.5)])]
    r = V.resumen_pos(pos)
    assert r['n'] == 6 and r['dias'] == 6
    assert r['ev_pond'] == pytest.approx(1.0 / 7.5)                                        # sum pnl / sum coste, no media de cocientes
    assert r['ev_unit'] == pytest.approx((3 - 1 + 0.25 - 1 + 1 - 1) / 6)
    # sin los 2 mejores dias (3,0 y 1,0): quedan 0,5 -1 -2 -0,5 = -3 sobre coste 5,5
    assert r['sin2'] == pytest.approx(-3.0 / 5.5) and r['dias_sin2'] == 4
    assert r['ic_lo'] is not None                                                          # 6 dias >= 5
    r4 = V.resumen_pos(pos[:4])
    assert r4['ic_lo'] is None and r4['ic_hi'] is None                                     # <5 dias: IC no estimable
    assert V.resumen_pos([]) == dict(n=0, dias=0)


def test_celda_primaria_missing_y_emparejado(out):
    D = '2026-10-19'
    filas = [fila(D, 10, 'A', 150, 5, 1.0, 'True', 0.01), fila(D, 10, 'A', 1500, 5, 1.0, 'True', 0.01),            # comun
             fila(D, 11, 'A', 150, 5, 1.0, 'False'),                                                              # recuperado por r150
             fila(D, 12, 'A', 150, 5, 1.0, ''),                                                                    # sin desenlace: missing, NO es 0
             fila(D, 13, 'A', 150, 5, 1.0, 'True', sizing='2eur'),                                                 # otra celda: no cuenta
             fila(D, 14, 'A', 150, 5, 1.0, 'True', cola='cons'),                                                   # otra cola: no cuenta
             fila(D, 15, 'A', 150, 5, 1.0, 'True', modo='acum'),                                                   # otro modo: no cuenta
             fila(D, 16, 'A', 150, 0, 0.0, 'True')]                                                                # sin relleno
    escribe_dia(out, D, filas)
    pos, cob = V.cargar_replay([D])
    assert set(k for k in pos[('A', 150)] if k != '_sin_desenlace') == {'10', '11'}
    assert pos[('A', 150)]['_sin_desenlace'] == ['12']
    em = V.emparejado(pos, 'A')
    assert (em['comunes'], em['solo150'], em['solo1500']) == (1, 1, 0)
    assert em['pnl_solo150'] == pytest.approx(-1.0) and em['dpnl_comunes'] == pytest.approx(0.0) and em['ratio'] == 2.0
    assert pos[('A', 150)]['10']['pnl'] == pytest.approx(5 * 1 - 1.0 + 0.01)               # un unico pago de resolucion: lleno*g - coste + rebate


def test_gate_no_medido_no_es_cumplido():
    res = dict(n=50, dias=12, ev_pond=0.3, ic_lo=0.1, ic_hi=0.5, sin2=0.1)
    est, c = V.evaluar_gate(res, [], [])
    assert c['p50_repuja<=300ms (>=10 reales)'][1] == 'NO_MEDIDO' and c['0 doble exposicion'][1] == 'NO_MEDIDO'
    assert est == 'NO_CUMPLE'                                                              # n y dias pasan, pero faltan criterios del arnes: nunca DRY_RUN_VALIDATED
    lat = [dict(ms_desde_decision_cancel=120 + i) for i in range(12)]
    est, c = V.evaluar_gate(res, lat, [])
    assert est == 'DRY_RUN_VALIDATED'
    est, c = V.evaluar_gate(res, [dict(ms_desde_decision_cancel=400 + i) for i in range(12)], [])
    assert c['p50_repuja<=300ms (>=10 reales)'][1] == 'FALLA' and est == 'NO_CUMPLE'
    est, c = V.evaluar_gate(res, lat, [dict(doble_exposicion=True)])
    assert c['0 doble exposicion'][1] == 'FALLA'
    est, c = V.evaluar_gate(dict(n=3, dias=2, ev_pond=0.9, ic_lo=None, ic_hi=None, sin2=None), lat, [])
    assert est == 'INSUFICIENTE'


def test_reinicio_idempotente_sin_duplicar_pnl(out, monkeypatch):
    for D in ('2026-10-19', '2026-10-20'):
        escribe_dia(out, D, [fila(D, int(D[-2:]) * 10, 'A', 150, 5, 1.0, 'True'), fila(D, int(D[-2:]) * 10, 'A', 1500, 5, 1.0, 'True')])
    monkeypatch.setattr(V, 'dias_esperados', lambda hasta=None: ['2026-10-19', '2026-10-20'])
    monkeypatch.setattr(sys, 'argv', ['x', '--sin-calcular'])
    assert V.main() == 0
    hoy = V.time.strftime('%Y-%m-%d', V.time.gmtime())
    j1 = json.load(open(f'{V.VIG}informe_{hoy}.json'))
    assert V.main() == 0                                                                    # segundo arranque: mismo resultado, sin filas nuevas
    j2 = json.load(open(f'{V.VIG}informe_{hoy}.json'))
    assert j1['replay']['A_r150'] == j2['replay']['A_r150'] and j2['replay']['A_r150']['n'] == 2
    m = json.load(open(V.VIG + 'run_manifest.json'))
    assert m['estado'] == 'COMPLETE' and m['coverage_valid'] == m['coverage_expected'] == 2 and m['dias_pendientes'] == []


def test_dia_corrupto_se_aparta_y_figura_pendiente(out, monkeypatch):
    D = '2026-10-19'
    escribe_dia(out, D, [fila(D, 1, 'A', 150, 5, 1.0, 'True')] * 2)
    for p in (f'{out}v3_BTC_{D}.csv', f'{out}v3_cobertura_BTC_{D}.json'):
        os.utime(p, (1, 1))                                                                 # antiguos: no los escribe nadie ahora
    monkeypatch.setattr(V, 'dias_esperados', lambda hasta=None: [D])
    monkeypatch.setattr(sys, 'argv', ['x', '--sin-calcular'])
    V.main()
    m = json.load(open(V.VIG + 'run_manifest.json'))
    assert m['estado'] == 'PARTIAL' and m['dias_pendientes'] == [D]                        # PARTIAL, nunca "completo"
    assert any('.invalido_' in f for f in os.listdir(out))                                  # la salida mala no se borra: se aparta


def test_sin_ordenes_ni_claves():
    for fn in ('vigia_h23_repuja.py', 'h23_shadow_v3.py'):
        src = open(os.path.join(HERE, fn)).read()
        for prohibido in ('py_clob_client', 'create_order', 'post_order', 'private_key', 'PRIVATE_KEY', 'load_dotenv', '/data/live/.env'):
            assert prohibido not in src, (fn, prohibido)
