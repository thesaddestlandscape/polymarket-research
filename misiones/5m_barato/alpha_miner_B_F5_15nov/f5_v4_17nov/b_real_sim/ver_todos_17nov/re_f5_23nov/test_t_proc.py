"""test_t_proc.py -- ESPEC E3: cronometro de t_proc (parseo + deteccion V5/V6 + estado -> STUB de cancelacion). Sin red, sin firma, sin ordenes."""
import os, sys, time, json
import numpy as np, pytest
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import t_proc_cronometro as TP, rf5_core as K5
import variantes_b as VB

def test_parseo_igual_que_libro_estado_ws_y_descarta_basura():
    src = open('/root/polymarket-research/libro_estado_ws.py').read()
    assert 'd = json.loads(raw).get("data")' in src and 'if d.get("e") == "aggTrade":' in src          # la logica espejada sigue siendo la del registro real
    raw = TP.mensaje('ETHUSDT', 1700000000123, 3000.5); assert TP.parsea_tick(raw) == ('ETHUSDT', 1700000000123, 3000.5)
    for malo in (b'no json', b'{"data": 3}', b'{"data": {"e": "bookTicker", "s": "X"}}', b'{}', b''): assert TP.parsea_tick(malo) is None

def test_detector_streaming_igual_que_variantes_b_saltos_bit_a_bit():
    rng = np.random.default_rng(3); n = 20000; t = np.cumsum(rng.integers(1, 400, n)).astype(np.int64) + 1_700_000_000_000; p = 3000 * np.exp(np.cumsum(rng.normal(0, 4e-4, n)))
    for nom, var in (('V5', VB.V5), ('V6', VB.V6)):
        J = VB.saltos(t, p, var); det = TP.DetectorSalto(var['w_ms'], var['thr_bps']); up = []; dn = []
        for a, b in zip(t, p):
            r = det.tick(int(a), float(b)); (up if r == 'up' else dn).append(int(a)) if r else None
        assert up == list(J['up']) and dn == list(J['dn']) and len(up) + len(dn) > 50, nom
    assert TP.VARS['V5']['w_ms'] == VB.V5['w_ms'] and TP.VARS['V5']['thr_bps'] == VB.V5['thr_bps'] and TP.VARS['V6']['w_ms'] == VB.V6['w_ms'] and TP.VARS['V6']['thr_bps'] == VB.V6['thr_bps']

def test_procesa_marca_tiempos_ordenados_y_cancela_solo_stub():
    dets = {'ETHUSDT': {v: TP.DetectorSalto(**TP.VARS[v]) for v in TP.VARS}}; est = TP.Estado(); est.arma('ETHUSDT', 'YES', 'o1'); est.arma('ETHUSDT', 'NO', 'o2')
    assert TP.procesa(TP.mensaje('ETHUSDT', 1000, 3000.0), dets, est, t_ms=1000) is None                                  # primer tick: sin referencia
    assert TP.procesa(TP.mensaje('ETHUSDT', 1500, 3000.0 * 0.999), dets, est, t_ms=1500) is None                         # sin tick <= t-w (1 s): sin senal
    t0 = time.time_ns() // 1_000_000 + 5000; dets2 = {'ETHUSDT': {v: TP.DetectorSalto(**TP.VARS[v]) for v in TP.VARS}}
    TP.procesa(TP.mensaje('ETHUSDT', t0 - 3000, 3000.0), dets2, est, t_ms=t0 - 3000)
    r = TP.procesa(TP.mensaje('ETHUSDT', t0, 3000.0 * 0.999), dets2, est, t_ms=t0)
    assert r is not None and r[0] <= r[1] <= r[2] and 'V5' in r[3] and r[3]['V5'] == 'dn' and est.intenciones >= 1        # dn adverso del YES => intencion sobre 'o1'; el stub no envia
    assert est.decide('ETHUSDT', 'dn') == ['o1'] and est.decide('ETHUSDT', 'up') == ['o2']

def test_mide_con_ticks_sinteticos_y_resumen(monkeypatch):
    import types
    rng = np.random.default_rng(5); n = 4000; t = np.cumsum(rng.integers(1, 300, n)).astype(np.int64) + 1_700_000_000_000; p = 3000 * np.exp(np.cumsum(rng.normal(0, 6e-4, n)))
    fake = types.SimpleNamespace(FB=types.SimpleNamespace(carga_binance=lambda d: {'eth': (t, p), 'sol': (t + 1, p * 0.01), 'xrp': (t + 2, p * 1e-3)}))
    monkeypatch.setitem(sys.modules, 'rf5_run', fake); filas, nm = TP.mide('2026-11-17', max_ticks=6000); r = TP.resumen(filas, nm)
    assert nm == 6000 and r['rafaga']['n'] > 0 and r['ritmado']['n'] > 0 and r['rafaga']['p50_ms'] > 0 and r['rafaga']['p90_ms'] >= r['rafaga']['p50_ms'] and all(f[4] >= 0 for f in filas)

def test_dia_ciego_prohibido_y_sin_red_ni_ordenes():
    src = open(HV + 't_proc_cronometro.py').read()
    for prohibido in ('post_order', 'create_order', 'py_clob_client', 'requests.', 'urllib', 'websockets', '.env', 'dotenv', 'private_key', 'sign_order', 'socket'): assert prohibido not in src, prohibido
    import subprocess; r = subprocess.run([sys.executable, '-I', HV + 't_proc_cronometro.py', '2026-11-18'], capture_output=True, text=True); assert r.returncode != 0 and 'ciego' in (r.stderr + r.stdout)
