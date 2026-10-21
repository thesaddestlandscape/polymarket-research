#!/usr/bin/env python3
"""Tests del replay v3 (sin datos reales, sin red). Desde este directorio: python3 -m pytest -q test_h23_sim_v3.py"""
import math, os, random, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'v2'))
sys.path.insert(0, os.path.join(HERE, '..'))
import numpy as np
import pytest
import h23_regla as R1
import h23_regla_v3 as R3
import h23_sim_v2 as V2
import h23_sim_v3 as V3


def test_regla_v3_solo_difiere_en_lo_declarado():
    a, b = dict(R1.CONFIG), dict(R3.CONFIG)
    dif = {k for k in set(a) | set(b) if a.get(k) != b.get(k)}
    assert dif == {'version', 'nombre', 'repuja_ms', 'repost_min_ms', 'acc_max_real', 'precio_min_ejec', 'precio_max_ejec', 't_min_ejec_s'}
    assert {k: v for k, v in b['repost_min_ms'].items() if k in a['repost_min_ms']} == a['repost_min_ms']
    assert R3.CONFIG['repuja_ms'] == 150 and R1.hash_config() != R3.hash_config()
    for f in ('querer', 'p_limite', 'fee', 'acciones', 'margen', 'lado_de_refs'):                  # la regla en si es identica
        for x in [(0.30, 0.33, 0.45, 0.47, 0.05), (0.10, 0.12, 0.30, 0.31, 0.02), (0.55, 0.56, 0.66, 0.70, 0.05)]:
            if f == 'querer': assert R1.querer(*x) == R3.querer(*x)
    for b15 in np.linspace(0.05, 0.95, 91):
        assert R1.p_limite(float(b15), 0.05) == R3.p_limite(float(b15), 0.05)


def test_acciones_real_igual_que_tamano_orden_h47():
    dev = '/root/polymarket-research-dev'
    if not os.path.exists(dev + '/experimento_maker_h47.py'): pytest.skip('dev no disponible')
    src = open(dev + '/experimento_maker_h47.py').read()
    ns = {'math': math, 'SIZE_MIN': 5, 'SIZE_MAX': 10}
    i = src.index('def tamano_orden'); j = src.index('def precio_a')
    exec(src[i:j], ns)                                                            # solo esa funcion pura (el modulo H47 no se importa)
    for c in range(1, 100):
        p = c / 100
        assert R3.acciones_real(p) == ns['tamano_orden'](p, 5, 1.0), p


def test_acciones_real_valores():
    assert R3.acciones_real(0.08) is None            # 13 acc > 10: no se envia
    assert R3.acciones_real(0.10) == 10.0 and R3.acciones_real(0.19) == 6.0 and R3.acciones_real(0.20) == 5.0 and R3.acciones_real(0.60) == 5.0
    assert R3.acciones_real(0.0) is None and R3.acciones_real(None) is None


def _rand_serie(rng, n=60):
    t0 = 1_000_000
    inst = np.cumsum(rng.integers(1, 900, n)) + t0
    pool = [None, 0.05, 0.12, 0.30, 0.31, 0.45, 0.62]
    want = [pool[i] for i in rng.integers(0, len(pool), n)]
    bsz = rng.integers(1, 500, n).astype(float)
    return inst, want, bsz


def test_segmentos_v3_igual_que_v2_sin_tope_de_tiempo():
    rng = np.random.default_rng(3)
    for _ in range(400):
        inst, want, bsz = _rand_serie(rng)
        for rep in V3.REPS:
            assert V3.segmentos(inst, want, bsz, rep, float('inf')) == V2.segmentos(inst, want, bsz, rep, True)


def test_segmentos_no_abre_puja_nueva_tras_el_tope_pero_mantiene_la_viva():
    inst = np.array([1000, 2000, 3000, 4000, 5000]); bsz = np.ones(5) * 10
    w = [0.30, 0.30, 0.30, None, 0.30]
    s = V3.segmentos(inst, w, bsz, 0, 3500)                                        # tope 3500: la re-puja de t=5000 no se abre
    assert s == [[0.30, 10.0, 1000, 4000]]
    s2 = V3.segmentos(inst, [0.30, 0.31, 0.31, 0.31, 0.31], bsz, 0, 1500)          # cambio de precio tras el tope: se cancela y NO se re-pone
    assert s2 == [[0.30, 10.0, 1000, 2000]]
    s3 = V3.segmentos(inst, [None, None, 0.30, 0.30, 0.30], bsz, 0, 2500)          # primera puja despues del tope: ninguna
    assert s3 == [[0.30, 10.0, 3000, None]][:0] or s3 == []


def test_repuja_exacta_150_vs_1500():
    inst = np.array([1000, 1100, 1200, 3000]); bsz = np.ones(4) * 7
    w = [0.30, None, 0.30, 0.30]                                                   # cancelar en 1100, el objetivo vuelve en 1200
    assert V3.segmentos(inst, w, bsz, 0, float('inf')) == [[0.30, 7.0, 1000, 1100], [0.30, 7.0, 1200, None]]
    assert V3.segmentos(inst, w, bsz, 150, float('inf')) == [[0.30, 7.0, 1000, 1100], [0.30, 7.0, 1250, None]]
    assert V3.segmentos(inst, w, bsz, 1500, float('inf')) == [[0.30, 7.0, 1000, 1100], [0.30, 7.0, 2600, None]]


def test_querible_universo_ejecutable():
    assert V3.querible(0.09, True) is None and V3.querible(0.61, True) is None and V3.querible(0.10, True) == 0.10 and V3.querible(0.60, True) == 0.60
    assert V3.querible(0.09, False) == 0.09 and V3.querible(None, True) is None


def _fills():
    FIL = [(2000, 0.30, 2.0), (2100, 0.30, 4.0), (2200, 0.29, 3.0)]
    FE = np.array([f[0] for f in FIL], dtype=np.int64)
    return FIL, FE


def test_llenar_primer_corta_en_el_primer_relleno_y_acum_acumula():
    FIL, FE = _fills()
    segs = [[0.30, 0.0, 1000, None]]
    l_a, c_a, t_a, p_a, n_a = V3.llenar(segs, 5.0, 0.0, 79, 60, FIL, FE, 9000, False)
    assert (round(l_a, 6), n_a, t_a) == (5.0, 2, 2000)                               # 2 + 3 (de 4) = need en 2 operaciones
    l_p, c_p, t_p, p_p, n_p = V3.llenar(segs, 5.0, 0.0, 79, 60, FIL, FE, 9000, True)
    assert (l_p, n_p, t_p, p_p) == (2.0, 1, 2000, 0.30) and abs(c_p - 0.6) < 1e-9     # parcial: un relleno (aunque parcial) cierra la puja
    # cola: con 9 acc por delante los dos prints al 0,30 (2+4=6) no llegan a nosotros; el de 0,29 ATRAVIESA el nivel y nos barre (need completo)
    assert V3.llenar([[0.30, 9.0, 1000, None]], 5.0, 1.0, 79, 60, FIL, FE, 9000, False)[0] == 5.0
    assert V3.llenar([[0.30, 9.0, 1000, 2100]], 5.0, 1.0, 79, 60, FIL, FE, 9000, False)[0] == 0.0     # cancelada antes de que llegue el print que barre (2200 > 2100+60)


def test_llenar_respeta_latencias_y_cancelacion():
    FIL, FE = _fills()
    assert V3.llenar([[0.30, 0.0, 1000, 1500]], 5.0, 0.0, 79, 60, FIL, FE, 9000, False)[0] == 0.0     # cancelada antes del 1er print
    assert V3.llenar([[0.30, 0.0, 1950, None]], 5.0, 0.0, 79, 60, FIL, FE, 9000, True)[0] == 4.0      # alta llega en 2029 > 2000: no ve el 1er print, si el de 2100
    assert V3.llenar([[0.30, 0.0, 1900, None]], 5.0, 0.0, 79, 60, FIL, FE, 9000, True)[0] == 2.0      # alta en 1979: ve el de 2000
    assert V3.llenar([[0.30, 0.0, 1000, 2080]], 5.0, 0.0, 79, 60, FIL, FE, 9000, False)[0] == 5.0     # cancelacion efectiva en 2140: ve 2000 y 2100 (2+3)
    assert V3.llenar([[0.30, 0.0, 1000, 2000]], 5.0, 0.0, 79, 60, FIL, FE, 9000, False)[0] == 2.0     # decision de cancelar en 2000, efectiva 2060: el print de 2000 aun casa, el de 2100 no


def test_llenar_barre_si_el_print_atraviesa_el_nivel():
    FIL = [(2000, 0.28, 9.0)]; FE = np.array([2000], dtype=np.int64)
    l, c, t, p, n = V3.llenar([[0.30, 100.0, 1000, None]], 5.0, 1.0, 79, 60, FIL, FE, 9000, False)
    assert l == 5.0 and abs(c - 1.5) < 1e-9                                         # pe < nuestro precio: barrido completo, sin cola delante


def test_idempotencia_salida_existente(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(V3, 'OUT', str(tmp_path) + '/')
    (tmp_path / 'v3_BTC_2026-01-01.csv').write_text('x\n')
    V3.main('2026-01-01')                                                           # no toca ni recalcula (si lo intentara, fallaria al abrir k_2026-01-01.csv)
    assert 'ya hecho' in capsys.readouterr().out and (tmp_path / 'v3_BTC_2026-01-01.csv').read_text() == 'x\n'
