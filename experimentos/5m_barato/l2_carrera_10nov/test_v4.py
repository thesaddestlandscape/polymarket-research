"""Tests v4 (sin polvo). Ejecutar: cd l2_carrera_10nov && python3 -m pytest -q test_v4.py
Regresion: los dos casos publicados (23-Oct ETH x=40 cola 16,2 -> residuo 6,19999981 vs print 6,2; SOL x=35 cola 19,78 -> 8,99999973 vs 9,0)."""
import os, sys, numpy as np, pytest
H = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, H)
import engine_v3 as E3, engine_v4 as E4


def _prints(pr):
    a = np.array(pr, float); return a[:, 0].astype(np.int64), a[:, 1], a[:, 2]


def _qupd(rows):
    a = np.array(rows, float); return a[:, 0].astype(np.int64), a[:, 1], a[:, 2], a[:, 3]


CASOS = [('ETH x=40 cola 16,2', 0.40, 6.19999981, 6.2), ('SOL x=35 cola 19,78', 0.35, 8.99999973, 9.0)]


@pytest.mark.parametrize('nombre,L,cola,s', CASOS)
def test_regresion_polvo_v3_lo_tenia_v4_no(nombre, L, cola, s):
    book = (L, L + 0.02, cola, 5.0); p = _prints([(1000, L, s)])
    # v3 con la cola del libro (BASE, sin filas): el print agota la cola y el else devuelve s - ahead = polvo
    q3, tf3, _ = E3.fill_segment_v3(book, 0.0, (np.empty(0, np.int64), np.empty(0), np.empty(0), np.empty(0)), p, L, 0, 5000, 5.0, 'BASE', dedupe=False)
    assert 0 < q3 < 1e-6 and tf3 == 1000, (nombre, q3)                      # el defecto, documentado
    q4, tf4, mot = E4.fill_segment_v4(book, 0.0, (np.empty(0, np.int64), np.empty(0), np.empty(0), np.empty(0)), p, L, 0, 5000, 5.0, 'BASE', dedupe=True)
    assert q4 == 0.0 and tf4 is None and mot == 'ok', (nombre, q4)


@pytest.mark.parametrize('nombre,L,cola,s', CASOS)
def test_float32_real_cola_agotada(nombre, L, cola, s):
    """cola en float32 (como D.v2) y print float64 exacto: nunca queda relleno 0<q<FLOOR, en ningun redondeo."""
    for c32 in (np.float32(s), np.nextafter(np.float32(s), np.float32(0)), np.nextafter(np.float32(s), np.float32(99))):
        book = (L, L + 0.02, c32, 5.0)
        q, tf, _ = E4.fill_segment_v4(book, 0.0, (np.empty(0, np.int64),) * 4, _prints([(1000, L, s)]), L, 0, 5000, 5.0, 'BASE')
        assert q == 0.0 and tf is None


def test_relleno_real_se_conserva():
    book = (0.10, 0.12, 4.0, 5.0)
    q, tf, _ = E4.fill_segment_v4(book, 0.0, (np.empty(0, np.int64),) * 4, _prints([(1000, 0.10, 10.0)]), 0.10, 0, 5000, 5.0, 'BASE')
    assert q == pytest.approx(5.0) and tf == 1000                           # 10 - 4 = 6 -> acotado por rem=5
    book = (0.10, 0.12, 4.0, 5.0)
    q, tf, _ = E4.fill_segment_v4(book, 0.0, (np.empty(0, np.int64),) * 4, _prints([(1000, 0.10, 4.5)]), 0.10, 0, 5000, 5.0, 'BASE')
    assert q == pytest.approx(0.5) and tf == 1000                           # relleno parcial legitimo 0,5
    q, tf, _ = E4.fill_segment_v4(book, 0.0, (np.empty(0, np.int64),) * 4, _prints([(1000, 0.09, 1.0)]), 0.10, 0, 5000, 5.0, 'BASE')
    assert q == pytest.approx(5.0) and tf == 1000                           # barrido por debajo de L


def test_relleno_funcion_unica():
    assert E4.relleno(6.2, 6.19999981) == (0.0, 0.0)                        # cola agotada exacta
    assert E4.relleno(6.2, 6.2000007) == (0.0, 0.0)
    a, g = E4.relleno(5.0, 20.0); assert (a, g) == (15.0, 0.0)              # cola no agotada
    a, g = E4.relleno(10.0, 4.0, 5.0); assert a == 0.0 and g == pytest.approx(5.0)   # acotado por rem
    a, g = E4.relleno(10.0, 4.0); assert a == 0.0 and g == pytest.approx(6.0)
    a, g = E4.relleno(4.0005, 4.0); assert (a, g) == (0.0, 0.0)             # 5e-4 < FLOOR = 0
    a, g = E4.relleno(4.002, 4.0); assert a == 0.0 and g == pytest.approx(0.002)   # 2e-3 >= FLOOR: relleno real
    assert E4.relleno(3.0, float('inf')) == (float('inf'), 0.0)
    a, g = E4.relleno(1e4, 1e4 - 5.0, 1.0); assert a == 0.0 and g == pytest.approx(1.0)  # tolerancia relativa no se come un relleno grande
    assert E4.relleno(0.0, 0.0) == (0.0, 0.0)


def test_assert_polvo_falla():
    with pytest.raises(AssertionError): E4.assert_sin_polvo(2e-7)
    assert E4.assert_sin_polvo(0.0) == 0.0 and E4.assert_sin_polvo(1e-3) == 1e-3
    assert not E4.es_fill(2e-7) and E4.es_fill(1e-3) and not E4.es_fill(0.0)


def test_aleatorio_nunca_polvo_y_igual_a_v3_salvo_polvo():
    """fixtures aleatorias con cola float32 de numeros de 2 decimales y prints float64 exactos: v4 nunca devuelve 0<q<FLOOR; donde v3 da q>=FLOOR, v4 da el mismo q (+-1e-3); el generador SI provoca polvo en v3."""
    rng = np.random.default_rng(7); n_polvo = 0; n_real = 0
    for _ in range(4000):
        L = round(float(rng.choice([0.05, 0.10, 0.35, 0.40])), 2); c64 = round(float(rng.uniform(1, 30)), 2); cola = float(np.float32(c64))
        book = (L, L + 0.02, cola, 5.0); npr = int(rng.integers(1, 5))
        pr = [(1000 + 100 * i, L, float(rng.choice([c64, round(c64 / 2, 2), round(float(rng.uniform(0.5, 12)), 2), 3.0]))) for i in range(npr)]
        p = _prints(pr); rem = float(rng.choice([5.0, 5.0, 2.5])); e = (np.empty(0, np.int64),) * 4
        q3, tf3, _ = E3.fill_segment_v3(book, 0.0, e, p, L, 0, 5000, rem, 'BASE', dedupe=False)
        q4, tf4, _ = E4.fill_segment_v4(book, 0.0, e, p, L, 0, 5000, rem, 'BASE', dedupe=False)
        assert q4 == 0.0 or q4 >= E4.FLOOR
        if q3 >= E4.FLOOR:
            n_real += 1; assert abs(q4 - q3) <= 1e-3 + 1e-9, (book, pr, q3, q4)
        elif 0 < q3 < E4.FLOOR: n_polvo += 1
    assert n_polvo > 0 and n_real > 100, (n_polvo, n_real)
