"""test_rf5_rapido.py -- aceleracion del simulador: parche reversible, Mkt.top rapido == original (incl. fallbacks), memo de run_segment identico (resultado, fills, contadores), tope de memoria. La igualdad BIT A BIT del replay completo (dia 17-Nov) la prueba rf5_rapido_prueba.py (out_rf5_ciego/rapido_17nov_*.json)."""
import os, sys, types
import numpy as np, pytest
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import rf5_rapido as RP, replay_variantes as RV

def _K(rng, n=400, desordenado=False):
    qt = np.sort(rng.integers(0, 10_000, n)).astype(np.int64)
    if desordenado: qt[10], qt[11] = qt[11], qt[10] + 5
    v0 = rng.uniform(0, 1, n).astype(np.float32); v1 = rng.uniform(0, 1, n).astype(np.float32); v0[rng.integers(0, n, 20)] = np.nan; v1[rng.integers(0, n, 20)] = 0.0; v0[rng.integers(0, n, 10)] = -1.0
    return types.SimpleNamespace(qb={5: 0, 6: n, 7: 2 * n}, qt=np.concatenate([qt, qt]), v0=np.concatenate([v0, v0]), v1=np.concatenate([v1, v1]))

def test_parche_rapido_reversible_y_anclas_fail_closed():
    txt = open(RV.SRC, encoding='utf-8').read(); p = RV.parchea(txt); q = RP.parchea_rapido(p); assert RP.verifica_rapido(p, q) and q != p and q.count('# [RAPIDO]') > 5
    with pytest.raises(ValueError): RP.parchea_rapido(p.replace(RP.A_OCUP, ''))            # ancla ausente => fail-closed
    m = RP.carga_rapido(); assert m.sha_origen == RV.SHA_SRC and m.sha_hooks != m.sha_rapido and len(m.sha_rapido) == 64

@pytest.mark.parametrize('desord', [False, True])
def test_top_rapido_igual_original_t_monotono_y_no_monotono(desord):
    rng = np.random.default_rng(3); K = _K(rng, desordenado=desord); orig = RV.MOD.ns['Mkt']; fast = RP.carga_rapido().ns['Mkt']
    a = orig('m', 5, 6, 10**6, 'eth', K); b = fast('m', 5, 6, 10**6, 'eth', K)
    ts = list(range(-50, 10_050, 7)) + list(rng.integers(-100, 10_100, 3000))            # creciente y despues aleatorio (no monotono)
    for t in ts:
        for k in (5, 6): assert a.top(k, int(t)) == b.top(k, int(t))

def test_memo_run_segment_resultado_fills_y_contadores_identicos():
    import sec7_core as C
    class E0:
        def __init__(s): s.n = 0
        def run_segment(s, k, L, t_arr, t_end, rem, variant): s.n += 1; return (float(rem) * 0.5 if k % 2 else 0.0), (int(t_arr) + 7 if k % 2 else None), 'ok'
    class W(C.EngineBloqueo):
        def __init__(s, E, **kw): super().__init__(E, **kw)
    base = W(E0(), activo=False); cache = RP.EngineBloqueoCache(E0(), activo=False); args = [(1, 0.2, 100, 900, 5.0, 'BASE'), (2, 0.3, 100, 900, 5.0, 'BASE'), (1, 0.2, 100, 900, 5.0, 'BASE'), (1, 0.2, 100, 950, 5.0, 'BASE')]
    r0 = [base.run_segment(*a) for a in args]; r1 = [cache.run_segment(*a) for a in args]; assert r0 == r1 and cache.hits == 1 and cache.miss == 3 and cache._E.n == 3

def test_memo_reproduce_fills_y_cont_de_bloqueo_activo(monkeypatch):
    import sec7_core as C
    class E0:
        def run_segment(s, k, L, t_arr, t_end, rem, variant): return 2.0, int(t_arr) + 5, 'ok'
    cache = RP.EngineBloqueoCache(E0(), activo=True); monkeypatch.setattr(C, 'clasifica_print', lambda *a, **k: 'print_x', raising=False)
    cache.tape = types.SimpleNamespace(get=lambda *a: None); cache._E.tape = cache.tape; cache.fuente = lambda k: (None, None)
    cache.run_segment(1, 0.2, 100, 900, 5.0, 'BASE'); f1 = dict(cache.fills); c1 = dict(cache.cont); cache.fills.clear(); cache.cont.clear()
    r = cache.run_segment(1, 0.2, 100, 900, 5.0, 'BASE'); assert cache.hits == 1 and cache.fills == f1 and dict(cache.cont) == c1 and r == (2.0, 105, 'ok') and len(f1) == 1                  # el acierto reproduce el efecto lateral

def test_tope_de_memoria(monkeypatch):
    class E0:
        def run_segment(s, *a): return 1.0, None, 'ok'
    monkeypatch.setattr(RP.EngineBloqueoCache, 'MAX', 5); c = RP.EngineBloqueoCache(E0(), activo=False)
    for i in range(20): c.run_segment(1, 0.2, i, 900, 5.0, 'BASE')
    assert len(c._memo) == 5 and c.miss == 20
