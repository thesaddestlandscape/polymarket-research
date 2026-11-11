"""Tests v3 (fixtures diminutas salvo los marcados `datos`): dedupe de cola, sello por firma, cargar con bidL NaN, regresion legacy, seguridad dry-run.
Ejecutar: cd l2_carrera_10nov && python3 -m pytest -q test_v3.py"""
import os, sys, re, importlib
import numpy as np, pandas as pd, pytest
H = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, H)
import engine_v3 as E3
G = E3.G


def _qupd(rows):
    """rows [(t, bid, szb, szb_prev)] -> (qt, v0, v2, v2prev)"""
    a = np.array(rows, float)
    return a[:, 0].astype(np.int64), a[:, 1], a[:, 2], a[:, 3]


def _prints(pr):
    if not pr: return (np.empty(0, np.int64), np.empty(0), np.empty(0))
    a = np.array(pr, float); return a[:, 0].astype(np.int64), a[:, 1], a[:, 2]


BOOK = (0.10, 0.12, 20.0, 5.0)    # bid 0,10 con 20 acciones delante, la orden llega a t=0


# ---------------------------------------------------------------- 1. dedupe: demostracion del doble conteo
def escenario(t_print):
    """Cola 20 delante de nosotros en L=0,10. t=1000: un tomador consume 10 (fila: szb 20->10; print de 10 sellado en t_print). t=3000: otro tomador consume 5.
    Realidad: tras el 1er consumo quedan 10 por delante; el 2o (5) NO nos llega (5 < 10). Fills correctos: 0."""
    q = _qupd([(1000, 0.10, 10.0, 20.0)])
    p = _prints([(t_print, 0.10, 10.0), (3000, 0.10, 5.0)])
    return q, p


def test_doble_conteo_demostrado():
    # sello correcto (print ANTES de su fila) -> sin relleno
    q, p = escenario(999)
    assert G.fill_segment(BOOK, 0.0, q[:3], p, 0.10, 0, 5000, 5.0, 'BASE')[0] == 0.0
    # print sellado EN la fila (tipo 0 antes que 1, orden del original): ahead = min(20,10)=10, luego -10 = 0, luego el 2o consumo (5) rellena 5 = FANTASMA
    q, p = escenario(1000)
    qty_o, tf_o, _ = G.fill_segment(BOOK, 0.0, q[:3], p, 0.10, 0, 5000, 5.0, 'BASE')
    assert qty_o == pytest.approx(5.0) and tf_o == 3000
    # idem print sellado DESPUES de la fila (el caso real: print +20 ms)
    q, p = escenario(1020)
    qty_o2, _, _ = G.fill_segment(BOOK, 0.0, q[:3], p, 0.10, 0, 5000, 5.0, 'BASE')
    assert qty_o2 == pytest.approx(5.0)
    # v3 sin dedupe == original; con dedupe: 0 en los tres sellados
    for tp in (999, 1000, 1020, 1090):
        q, p = escenario(tp)
        assert E3.fill_segment_v3(BOOK, 0.0, q, p, 0.10, 0, 5000, 5.0, 'BASE', dedupe=False)[0] == G.fill_segment(BOOK, 0.0, q[:3], p, 0.10, 0, 5000, 5.0, 'BASE')[0]
        d = {}
        assert E3.fill_segment_v3(BOOK, 0.0, q, p, 0.10, 0, 5000, 5.0, 'BASE', dedupe=True, diag=d)[0] == 0.0, tp
        assert d['paired'] == (0 if tp == 999 else 1) or tp == 1090   # a 90 ms sigue dentro de row_win=100: se empareja; a 999 ya iba bien (se empareja tambien: print en (t_fila-.., t_fila])


def test_dedupe_conserva_tf_del_print():
    """el relleno fechado por un print reordenado antes de su fila conserva el SELLO DEL PRINT como tf (bug visto en CX/TRAIN: tf = hora de la fila, 21 'nomatch' de 4.601)."""
    book = (0.10, 0.12, 4.0, 5.0)
    q = _qupd([(1000, 0.10, 4.0, 14.0)])                               # fila: szb 14 -> 4 (consumo 10)
    p = _prints([(1060, 0.10, 10.0)])                                  # print sellado 60 ms despues de la fila, cola 4 < 10: relleno de 5
    d = {}
    r = E3.fill_segment_v3(book, 0.0, q, p, 0.10, 0, 5000, 5.0, 'BASE', dedupe=True, diag=d)
    assert d['paired'] == 1 and r[0] == pytest.approx(5.0) and r[1] == 1060


def test_dedupe_no_quita_rellenos_reales():
    """Si el consumo SI llega a nuestra posicion (cola 4 < consumo 10) el relleno sigue ahi con dedupe, con los tres sellados."""
    book = (0.10, 0.12, 4.0, 5.0)
    q = _qupd([(1000, 0.10, 4.0, 4.0)])       # fila sin caida de tamano (el consumo de 10 se tragaria 4 de delante + 6 nuestras: fila posterior no a L)
    for tp in (999, 1020):
        p = _prints([(tp, 0.10, 10.0)])
        r = E3.fill_segment_v3(book, 0.0, q, p, 0.10, 0, 5000, 5.0, 'BASE', dedupe=True)
        assert r[0] == pytest.approx(5.0)       # min(rem, 10-4)=5 con rem=5
    # fila con caida distinta del tamano del print: no se empareja (no es la firma)
    q2 = _qupd([(1000, 0.10, 14.0, 20.0)])
    d = {}
    E3.fill_segment_v3((0.10, 0.12, 20.0, 5.0), 0.0, q2, _prints([(1020, 0.10, 10.0)]), 0.10, 0, 5000, 5.0, 'BASE', dedupe=True, diag=d)
    assert d['paired'] == 0


def test_dedupe_off_identico_al_original_aleatorio():
    rng = np.random.default_rng(7)
    for it in range(400):
        L = float(rng.choice([0.10, 0.13, 0.16, 0.19])); bid = float(rng.choice([L - 0.01, L, L + 0.01])); bsz = float(rng.integers(1, 60))
        book = (bid, L + 0.02, bsz, 5.0); nq = int(rng.integers(0, 6)); nt = int(rng.integers(0, 6))
        tq = np.sort(rng.integers(1, 4000, nq)); v0 = rng.choice([L, L - 0.01, L + 0.01], nq); v2 = rng.integers(1, 60, nq).astype(float); vp = np.where(rng.random(nq) < .7, v2 + rng.integers(0, 15, nq), np.nan)
        tp = np.sort(rng.integers(1, 4000, nt)); pp = rng.choice([L, L - 0.02, L + 0.01], nt); ps = rng.integers(1, 20, nt).astype(float)
        var = str(rng.choice(['BASE', 'OPT', 'CONS'])); rem = 5.0
        a = G.fill_segment(book, 1.0, (tq.astype(np.int64), v0, v2), (tp.astype(np.int64), pp, ps), L, 0, 5000, rem, var) if var == 'BASE' else G.fill_segment(book, 1.0, None, (tp.astype(np.int64), pp, ps), L, 0, 5000, rem, var)
        b = E3.fill_segment_v3(book, 1.0, (tq.astype(np.int64), v0, v2, vp), (tp.astype(np.int64), pp, ps), L, 0, 5000, rem, var, dedupe=False) if var == 'BASE' else E3.fill_segment_v3(book, 1.0, None, (tp.astype(np.int64), pp, ps), L, 0, 5000, rem, var, dedupe=False)
        assert a == b, (it, a, b)


# ---------------------------------------------------------------- 2. sello por firma
import stamp_v3 as ST


def _book(rows):
    """rows [(ex, bid, szb)] de un token -> EX,B,Z,qb"""
    a = np.array(rows, float); return a[:, 0].astype(np.int64), a[:, 1], a[:, 2], np.array([0, len(rows)])


def test_firma_dec_unica_sella_fila_menos_1ms():
    EX, B, Z, qb = _book([(1000, 0.10, 30.0), (2000, 0.10, 20.0), (3000, 0.10, 30.0)])     # consumo de 10 a t=2000
    tm, rama, row, dex, c, nex = ST.stamp_events(EX, B, Z, qb, [0], [2020], [0.10], [0.10], [10.0], [1])
    assert rama[0] == 'sig' and tm[0] == 1999 and dex[0] == 20 and row[0] == 1 and nex[0] == 1


def test_firma_clr_y_barrido():
    EX, B, Z, qb = _book([(1000, 0.10, 10.0), (2000, 0.09, 8.0), (3000, 0.09, 8.0)])       # el nivel 0,10 (10 acc) desaparece en t=2000
    tm, rama, *_ = ST.stamp_events(EX, B, Z, qb, [0], [2021], [0.10], [0.10], [10.0], [1])
    assert rama[0] == 'sig' and tm[0] == 1999
    EX, B, Z, qb = _book([(1000, 0.12, 5.0), (2000, 0.09, 8.0), (3000, 0.09, 8.0)])        # barrido 0,12 -> 0,09: una fila salta de bid>=pmax a bid<=pmin
    tm, rama, *_ = ST.stamp_events(EX, B, Z, qb, [0], [2018], [0.12], [0.09], [14.0], [2])
    assert rama[0] == 'sig' and tm[0] == 1999


def test_ambiguo_y_sin_firma_usan_constante():
    EX, B, Z, qb = _book([(1000, 0.10, 30.0), (1400, 0.10, 20.0), (1800, 0.10, 30.0), (2200, 0.10, 20.0), (4000, 0.10, 20.0)])   # dos consumos de 10: ambiguo
    tm, rama, row, dex, c, nex = ST.stamp_events(EX, B, Z, qb, [0], [2000], [0.10], [0.10], [10.0], [1])
    assert rama[0] == 'amb' and nex[0] == 2 and tm[0] == 2000 - c - 1 and c == 20          # <200 firmas unicas: constante por defecto
    tm, rama, *_ = ST.stamp_events(EX, B, Z, qb, [0], [2000], [0.10], [0.10], [7.0], [1])   # tamano que no coincide: sin firma
    assert rama[0] == 'nosig' and tm[0] == 2000 - 20 - 1
    tm, rama, *_ = ST.stamp_events(EX, B, Z, qb, [0], [-1], [0.10], [0.10], [10.0], [1])
    assert rama[0] == 'sinev'


def test_guardia_d_ex():
    EX, B, Z, qb = _book([(1000, 0.10, 30.0), (2000, 0.10, 20.0), (4000, 0.10, 20.0)])
    tm, rama, *_ = ST.stamp_events(EX, B, Z, qb, [0], [2400], [0.10], [0.10], [10.0], [1])   # firma unica pero a 400 ms: fuera de guardia -> constante
    assert rama[0] == 'guard' and tm[0] == 2400 - 20 - 1


def test_constante_de_epoca_mediana_de_unicas():
    assert ST.epoch_const([30] * 300) == 30 and ST.epoch_const([18] * 100) == 20 and ST.epoch_const([20] * 150 + [900] * 100) == 20


def test_print_antes_de_su_fila_no_doble_cuenta_con_sello_v3():
    """integracion sello+motor: fila de consumo en 1000 (szb 20->10), print real 20 ms despues (t_ev=1020). Sello v3 = 999: sin fantasma. Sello v2 (t_ev) = 1020: fantasma en el motor original, ninguno con dedupe."""
    EX, B, Z, qb = _book([(500, 0.10, 20.0), (1000, 0.10, 10.0)])
    tm, rama, *_ = ST.stamp_events(EX, B, Z, qb, [0], [1020], [0.10], [0.10], [10.0], [1])
    assert tm[0] == 999
    q = _qupd([(1000, 0.10, 10.0, 20.0)])
    r_v3 = G.fill_segment(BOOK, 0.0, q[:3], _prints([(int(tm[0]), 0.10, 10.0), (3000, 0.10, 5.0)]), 0.10, 0, 5000, 5.0, 'BASE')
    r_v2 = G.fill_segment(BOOK, 0.0, q[:3], _prints([(1020, 0.10, 10.0), (3000, 0.10, 5.0)]), 0.10, 0, 5000, 5.0, 'BASE')
    assert r_v3[0] == 0.0 and r_v2[0] == pytest.approx(5.0)


# ---------------------------------------------------------------- 3. cargar v3 (bidL NaN != sin segmento)
def _fs(tmp_path, seg_rows, bidL):
    F = pd.DataFrame(dict(dia=['2026-11-03'] * 3, k=[1, 2, 3], L=[0.1] * 3, seg=[0] * 3, q=[5.0] * 3, gana=[0.0, 1.0, 0.0], tf=[1, 2, 3], t_dec=[1, 2, 3], fin=[1, 2, 3], token=['a', 'b', 'c'], act=['ETH'] * 3))
    F['cost'] = F.q * F.L; F['pnl'] = F.q * (F.gana - F.L + 0.2 * 0.07 * F.L * (1 - F.L))
    S = pd.DataFrame(dict(dia=['2026-11-03'] * len(seg_rows), k=seg_rows, L=[0.1] * len(seg_rows), seg=[0] * len(seg_rows), bidL=bidL, T=[200.0] * len(seg_rows)))
    fp, sp = str(tmp_path / 'f.pkl'), str(tmp_path / 's.pkl'); F.to_pickle(fp); S.to_pickle(sp); return fp, sp


def test_cargar_bidL_nan_no_es_error_pero_sin_segmento_si(tmp_path):
    P = importlib.import_module('paso0_lib_v3')
    fp, sp = _fs(tmp_path, [1, 2, 3], [0.07, np.nan, 0.03])
    U, S = P.cargar(fp, sp, dias=['2026-11-03'])
    assert U.attrs['n_rellenos_sin_segmento'] == 0 and U.attrs['n_bidL_nan'] == 1 and list(U.geo6) == [True, False, False]
    fp, sp = _fs(tmp_path, [1, 2], [0.07, np.nan])                      # el relleno k=3 no tiene fila de segmento
    with pytest.raises(RuntimeError, match='sin segmento'):
        P.cargar(fp, sp, dias=['2026-11-03'])
    U, _ = P.cargar(fp, sp, dias=['2026-11-03'], permitir_sin_segmento=True)
    assert U.attrs['n_rellenos_sin_segmento'] == 1
    U, _ = P.cargar(fp, sp, dias=['2026-11-03'], modo='legacy')         # legacy: sin comprobacion, como el original
    assert len(U) == 3


def test_cargar_legacy_reproduce_original_datos(monkeypatch):
    """datos: paso0_lib.cargar() (original) vs paso0_lib_v3.cargar(modo='legacy') sobre out/g0_fills.pkl. guard_dias se anula en el original para no escribir en eval_log.jsonl (A1)."""
    if not os.path.exists(H + 'out/g0_fills.pkl'): pytest.skip('sin datos')
    import l2eval, paso0_lib as P0
    monkeypatch.setattr(l2eval, 'guard_dias', lambda *a, **k: sorted(set(a[0])))
    U0, S0 = P0.cargar()
    P3 = importlib.import_module('paso0_lib_v3'); monkeypatch.setattr(P3.E, 'guard_dias', lambda *a, **k: sorted(set(a[0])))
    U3, S3 = P3.cargar(modo='legacy')
    pd.testing.assert_frame_equal(U0, U3, check_like=False); pd.testing.assert_frame_equal(S0, S3)


def test_dryrun_sin_imports_de_envio():
    prohibido = re.compile(r'^\s*(import|from)\s+(py_clob_client|web3|eth_account|requests|websockets|aiohttp|live_trade|live_guard|ejecutor_rapido)', re.M)
    for f in ('engine_v3.py', 'stamp_v3.py', 'passT_v3.py', 'paso0_lib_v3.py', 'verif_v3.py', 'cxb_motor_v3.py'):
        p = H + f
        if os.path.exists(p): assert not prohibido.search(open(p).read()), f
