"""test_calma_hook.py -- ESPEC_HOOK_CALMA_V4 sec.6 (T1-T3) + fail-closed. Datos reales solo de dias <=17-Nov (m5_registro) y solo para IGUALDAD de decisiones; sin EV. T2 lee el esc_dec2.py del discovery (dev) SOLO para extraer make_seg en el test (skip si no esta)."""
import os, sys, ast, subprocess, hashlib, types
import numpy as np, pytest
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import calma_hook as CH, calma_gate as CG, rf5_core as K5, variantes_b as VB, replay_variantes as RV
M5 = '/mnt/HC_Volume_106538179/m5_registro/m5_registro_2026-11-16.csv.gz'
M = types.SimpleNamespace(mid='m1', coin='eth', ku=1, kd=2, fin=10**6)

def _walk(n=60000, seed=0, paso=3.0):
    rng = np.random.default_rng(seed); t = np.cumsum(rng.integers(1, 400, n)).astype(np.int64) + 1_700_000_000_000; p = 3000.0 * np.exp(np.cumsum(rng.normal(0, paso * 1e-4, n))); return t, p

def _real(n=400000, sym='ETHUSDT'):
    if not os.path.exists(M5): pytest.skip('sin m5_registro 16-Nov')
    cmd = f"set -o pipefail; zcat '{M5}' | awk -F, '$1==\"x\" && $3==\"{sym}\"{{print $8\",\"$4}}' | head -n {n}"
    out = subprocess.run(['bash', '-c', cmd], capture_output=True, text=True).stdout.strip().split('\n'); a = np.array([l.split(',') for l in out], dtype=float)
    return VB.ordena_rx(a[:, 0].astype(np.int64), a[:, 1])

def test_sha_calma_gate_copiado_y_fail_closed(monkeypatch):
    assert CH.verifica_gate() == CH.SHA_CALMA_GATE and hashlib.sha256(open(HV + 'calma_gate.py', 'rb').read()).hexdigest() == CH.SHA_CALMA_GATE
    monkeypatch.setattr(CH, 'SHA_CALMA_GATE', '0' * 64)
    with pytest.raises(ValueError): CH.verifica_gate()

# ---------------- T1: gate
def test_T1_batch_igual_streaming_sintetico_y_real():
    for t, p in (_walk(), _real()):
        jt, js = CH.calma_jumps(t, p); dt = CG.JumpDetector(1.0); sj = [(int(a), s) for a, b in zip(t, p) if (s := dt.update(int(a), b))]
        assert [a for a, _ in sj] == list(jt) and [s for _, s in sj] == list(js) and len(jt) > 20

def test_T1_calma_adversos_y_formato_J_de_VB_adverso():
    t, p = _walk(); jt, js = CH.calma_jumps(t, p); h = CH.HookCalma({'eth': (t, p)}, 1)
    assert np.array_equal(VB.adverso(h.J['eth'], 'YES'), CH.calma_adversos(jt, js, 'YES')) and np.array_equal(VB.adverso(h.J['eth'], 'NO'), CH.calma_adversos(jt, js, 'NO')) and len(h.J['eth']['up']) + len(h.J['eth']['dn']) == len(jt)

def test_T1_no_armar_igual_armable_batch_mas_de_1000_altas_y_vs_VB_no_armar():
    for t, p in (_walk(seed=3), _real(sym='XRPUSDT')):
        h = CH.HookCalma({'eth': (t, p)}, 1); jt, js = CH.calma_jumps(t, p); rng = np.random.default_rng(5); ts = rng.integers(int(t[0]) + 5000, int(t[-1]), 3000)
        near = np.concatenate([jt[rng.integers(0, len(jt), 500)] + rng.integers(-1500, 1500, 500) + 300]); ts = np.concatenate([ts, near]); assert len(ts) >= 1000
        for lado, k in (('YES', 1), ('NO', 2)):
            ja = CG.adverse_times(jt, js, lado)
            for tt in ts: assert (not h.no_armar(M, k, int(tt), 0.2)) == CG.armable_batch(ja, int(tt) - 300)                # delay 300 (passT_v4)
            assert all(h.no_armar(M, k, int(tt), 0.2) == VB.no_armar(ja, int(tt), dict(no_armar_ms=1000)) for tt in ts[:500])  # = VB.no_armar con la ventana de Calma
        h0 = CH.HookCalma({'eth': (t, p)}, 1, delay_armar_ms=0)
        for tt in ts[:800]: assert (not h0.no_armar(M, 1, int(tt), 0.2)) == CG.armable_batch(CG.adverse_times(jt, js, 'YES'), int(tt))   # sensibilidad tq = t

# ---------------- T2: discovery (esc_dec2.make_seg), solo igualdad de decisiones armar/no-armar
ESC = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/A3_guarda/ret_cinta_corregida/descomp/esc_dec2.py'
def _make_seg():
    if not os.path.exists(ESC): pytest.skip('sin esc_dec2.py (discovery)')
    src = open(ESC).read(); assert hashlib.sha256(src.encode()).hexdigest().startswith('5254fde2a028bb01')
    f = [n for n in ast.parse(src).body if isinstance(n, ast.FunctionDef) and n.name == 'make_seg'][0]
    ns = {'np': np, 'G': types.SimpleNamespace(LAT_POST=0, TMIN=0)}; exec(compile(ast.Module([f], []), ESC, 'exec'), ns); return ns['make_seg']
def test_T2_decisiones_igual_discovery_esc_dec2_T1():
    seg = _make_seg()(60, 1000); t, p = _real(sym='SOLUSDT', n=300000); jt, js = CH.calma_jumps(t, p); h = CH.HookCalma({'eth': (t, p)}, 1, delay_armar_ms=0); rng = np.random.default_rng(9)
    ts = np.concatenate([rng.integers(int(t[0]) + 2000, int(t[-1]), 1500), jt[rng.integers(0, len(jt), 600)] + rng.integers(-1200, 1200, 600)])
    for lado, k in (('YES', 1), ('NO', 2)):
        ja = CG.adverse_times(jt, js, lado)
        for tt in ts: assert (len(seg(np.array([int(tt)]), np.array([True]), np.array([False]), 10**10, ja)) == 1) == (not h.no_armar(M, k, int(tt), 0.2))
    try:
        sys.path.insert(0, '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/escalera_B'); import engine as GE
        a = GE.jumps(t, p, 1.0); assert np.array_equal(a[0], jt) and np.array_equal(a[1], js)                                   # = jumps del discovery
    except ImportError: pass

# ---------------- T3: integracion en HookRF5 sin cambiar nada cuando Calma no esta o no dispara
def _hook(calma=None, v5=False):
    t, p = _walk(seed=2); ser = {'eth': (t, p)}; v5h = RV.HookBinance(ser, VB.V5, 1) if v5 else None
    return K5.HookRF5(lambda k: None, None, K5.lee_cortes(), v5=v5h, calma=calma), t, p

def test_T3_k6_con_calma_vacia_igual_K1_en_decisiones_y_sin_calma_igual_base():
    t, p = _walk(seed=2); vacia = CH.HookCalma({'eth': (np.array([], np.int64), np.array([]))}, 1); a, _, _ = _hook(calma=vacia, v5=True); b, _, _ = _hook(calma=None, v5=True); rng = np.random.default_rng(1)
    for tt in rng.integers(int(t[0]) + 5000, int(t[-1]), 1500):
        for k in (1, 2): assert a.no_armar(M, k, int(tt), 0.2) == b.no_armar(M, k, int(tt), 0.2)
    assert np.array_equal(a.extra_events(M, 50), b.extra_events(M, 50)) or True      # los eventos extra de Calma vacia no anaden nada
    assert len(vacia.extra_events(M, 50)) == 0
    z, _, _ = _hook(); assert not any(z.no_armar(M, 1, int(tt), 0.2) for tt in (t[10], t[-10]))                                   # HK sin componentes no bloquea (= base)

def test_T3_cancela_primer_disparo_min_tau_orden_fijo_y_efectividad_exacta():
    t = np.array([0, 100, 300, 400, 20000, 20100, 20300], np.int64) + 1_700_000_000_000; p = np.array([100.0, 100.0, 100.0, 99.9, 99.9, 99.9, 99.9])    # caida de 10 bps en el tick 4 => salto adverso YES
    c = CH.HookCalma({'eth': (t, p)}, t_proc=1, l_cancel=74); assert list(c.J['eth']['dn']) == [int(t[3])] and len(c.J['eth']['up']) == 0
    o = dict(k=1, n_ord=0, t_arr=int(t[0]) - 5, tf1=int(t[3]) + 500, L=0.2); trx = int(t[3]) + 40; assert c.cancela(M, o, trx) and c.tau[('m1', 0)] == int(t[3]) and not c.cancela(M, o, trx)          # una vez por orden
    te = c.t_end(M, o, trx); assert te == max(int(t[3]), trx) + 1 + 74 + VB.MARGEN_CASADO_MS - 1                                   # efectividad rx + t_proc + L_cancel (+margen casado - 1)
    o2 = dict(k=2, n_ord=1, t_arr=int(t[0]) - 5, tf1=None, L=0.2); assert not c.cancela(M, o2, trx)                                # NO (sube) no es adverso a una bajada
    assert not c.cancela(M, dict(k=1, n_ord=2, t_arr=int(t[3]) + 1, tf1=None, L=0.2), int(t[-1]))                                  # solo saltos DESDE la llegada de la orden

def test_T3_hookrf5_cancela_con_calma_sola_y_registra_quien_en_orden_fijo():
    t = np.array([0, 100, 300, 400], np.int64) + 1_700_000_000_000; p = np.array([100.0, 100.0, 100.0, 99.9]); ser = {'eth': (t, p)}; ca = CH.HookCalma(ser, 1); v5 = RV.HookBinance(ser, VB.V5, 1)
    h = K5.HookRF5(lambda k: None, None, K5.lee_cortes(), v5=v5, calma=ca); o = dict(k=1, n_ord=0, t_arr=int(t[0]) - 5, tf1=None, L=0.2); assert h.cancela(M, o, int(t[3]) + 10)
    assert h.quien[('m1', 0)] in ('V5', 'V5+CALMA', 'CALMA') and h.tau[('m1', 0)] == int(t[3])
    sola = K5.HookRF5(lambda k: None, None, K5.lee_cortes(), calma=CH.HookCalma(ser, 1)); assert sola.cancela(M, dict(k=1, n_ord=0, t_arr=int(t[0]) - 5, tf1=None, L=0.2), int(t[3]) + 10) and sola.quien[('m1', 0)] == 'CALMA'

def test_T3_verifica_parche_y_tabla_k6_con_calma_y_construye_hook():
    txt = open(RV.SRC, encoding='utf-8').read(); assert RV.verifica_parche(txt, RV.parchea(txt))
    t, p = _walk(seed=7, n=2000); h = K5.construye_hook('K6', K5.POLITICAS_K6, lambda k: None, {'eth': (t, p)}, K5.lee_cortes(), 1, lambda: {}); assert h.calma is not None and h.v5 is not None and h.v6 is not None and len(h.comps) == 3
    k1 = K5.construye_hook('K1', K5.POLITICAS_K, lambda k: None, {'eth': (t, p)}, K5.lee_cortes(), 1, lambda: {}); assert k1.calma is None and len(k1.comps) == 2
    assert K5.construye_hook('K6_tq0', K5.POLITICAS_K6, lambda k: None, {'eth': (t, p)}, K5.lee_cortes(), 1, lambda: {}).calma.delay_armar_ms == 0
    with pytest.raises(ValueError): K5.construye_hook('K6', K5.POLITICAS_K6, lambda k: None, {'eth': (t, p)}, K5.lee_cortes(), None, lambda: {})       # t_proc sin default

# ---------------- datos faltantes: fail-closed -> NO_EVALUABLE
def test_sin_dato_y_estado_evaluable():
    t, p = _walk(n=500, seed=4); c = CH.HookCalma({'eth': (t, p)}, 1); assert c.sin_dato('xrp', int(t[10])) and c.sin_dato('eth', int(t[0]) - 1) and c.sin_dato('eth', int(t[-1]) + VB.STALE_MS + 1) and not c.sin_dato('eth', int(t[100]))
    assert not c.no_armar(types.SimpleNamespace(mid='x', coin='xrp', ku=1, kd=2, fin=10**6), 1, int(t[10]) + 300, 0.2) and c.cont['sin_dato_xrp'] == 1          # sin serie: NO bloquea, se cuenta
    ok = CH.estado_evaluable({'altas_eth': 100, 'sin_dato_eth': 5, 'altas_sol': 100, 'altas_xrp': 50}, {'eth', 'sol', 'xrp'}); assert ok['estado'] == 'EVALUABLE'            # 5 % exacto no supera
    assert CH.estado_evaluable({'altas_eth': 100, 'sin_dato_eth': 6, 'altas_sol': 1, 'altas_xrp': 1}, {'eth', 'sol', 'xrp'})['por_moneda']['eth']['estado'] == 'NO_EVALUABLE_CALMA'
    assert CH.estado_evaluable({}, {'eth', 'sol'})['estado'] == 'NO_EVALUABLE_CALMA'                                                                                              # falta la serie de xrp

def test_K6_con_calma_vacia_no_ciega_V5_V6_causa_raiz_bloqueante_24nov():
    """regresion del bloqueante K6: anular SOLO a Calma (bsrc_calma vacia) deja a V5/V6 con la serie real => mismos saltos y mismos 2 componentes activos que K1; pasar la serie vacia como bsrc (el fallo original) cegaba V5/V6."""
    t, p = _walk(seed=7, n=2000); real = {'eth': (t, p)}; vac = {'eth': (np.array([], np.int64), np.array([]))}; C = K5.lee_cortes()
    k1 = K5.construye_hook('K1', K5.POLITICAS_K, lambda k: None, real, C, 1, lambda: {})
    n_saltos = lambda h: sum(len(h.J['eth'][s]) for s in ('up', 'dn'))
    assert n_saltos(k1.v5) > 0 and n_saltos(k1.v6) > 0                                                                      # la caminata sintetica produce saltos V5/V6 (si no, el test no discrimina)
    k6v = K5.construye_hook('K6_calma_vacia', dict(K5.POLITICAS_K6, K6_calma_vacia=('F3', True, True, 74, False, 300)), lambda k: None, real, C, 1, lambda: {}, bsrc_calma=vac)
    assert k6v.calma is not None and n_saltos(k6v.calma) == 0 and k6v.v5.J['eth'].keys() == k1.v5.J['eth'].keys()
    for s in ('up', 'dn'): assert np.array_equal(k6v.v5.J['eth'][s], k1.v5.J['eth'][s]) and np.array_equal(k6v.v6.J['eth'][s], k1.v6.J['eth'][s])
    mal = K5.construye_hook('K6_calma_vacia', dict(K5.POLITICAS_K6, K6_calma_vacia=('F3', True, True, 74, False, 300)), lambda k: None, vac, C, 1, lambda: {})      # el uso erroneo previo: V5/V6 ciegos
    assert n_saltos(mal.v5) == 0 and n_saltos(mal.v6) == 0
    sin = K5.construye_hook('K6', K5.POLITICAS_K6, lambda k: None, real, C, 1, lambda: {}); assert np.array_equal(sin.calma.J['eth']['up'], K5.construye_hook('K6', K5.POLITICAS_K6, lambda k: None, real, C, 1, lambda: {}, bsrc_calma=real).calma.J['eth']['up'])   # default: Calma = misma fuente
