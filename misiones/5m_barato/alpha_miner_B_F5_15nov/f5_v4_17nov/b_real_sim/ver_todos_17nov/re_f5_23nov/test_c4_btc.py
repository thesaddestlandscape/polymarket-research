"""test_c4_btc.py -- verificacion automatica de las 10 condiciones de BTC (fixtures; sin datos reales) y prep_day_btc (estados de fallo cerrado)."""
import os, sys, json, hashlib
import numpy as np, pytest
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import c4_btc as C4, prep_day_btc as PB

def _btc_ms(path, n_btc5=3):
    tm = np.array([['BTC', '5min', str(i), '2026-11-04 00:00:00+00:00', 'YES'] for i in range(n_btc5)] + [['BTC', '15min', '9', 'x', 'NO']], dtype='<U25'); np.savez(path, tokens=np.array([str(i) for i in range(len(tm))]), tmap=tm)

def test_dias_y_tokens(tmp_path):
    assert C4.dias('2026-11-03', '2026-11-05') == ['2026-11-03', '2026-11-04', '2026-11-05']; p = tmp_path / 'b.npz'; _btc_ms(p); assert C4.tokens_btc5(str(p)) == 3 and C4.tokens_btc5(str(tmp_path / 'no.npz')) == -1; _btc_ms(p, 0); assert C4.tokens_btc5(str(p)) == 0

def test_evalua_todo_bloqueado_sin_datos_y_diez_condiciones(tmp_path):
    (tmp_path / 'sa_ms').mkdir(); r = C4.evalua('2026-11-20', dl=str(tmp_path) + '/', btcd=str(tmp_path) + '/rf5_btc/', vol=str(tmp_path), firmas={}, cortes={}, m5fn=lambda d: False)
    assert r['estado'] == 'DATA_BLOCKED_BTC' and r['n'] == 10 and len(r['condiciones']) == 10 and r['n_ok'] <= 1                          # a lo sumo la 6 (tabla vacia => no ok) -> normalmente 0
    assert r['condiciones']['1_btc_ms']['faltan'][0] == '2026-11-03' and r['condiciones']['4_adenda_p20_p80_btc']['estado'] == 'PENDIENTE_FIRMA'

def test_condiciones_1_9_10_ok_con_fixture_y_firma_con_sha(tmp_path):
    (tmp_path / 'sa_ms').mkdir()
    for d in C4.dias('2026-11-03', '2026-11-05'): _btc_ms(tmp_path / 'sa_ms' / f'btc_ms_{d}.npz')
    ad = tmp_path / 'adenda.md'; ad.write_text('x'); fi = {'cond4_adenda_cortes': dict(ruta=str(ad), sha256=hashlib.sha256(b'x').hexdigest())}
    old = C4.HASTA_COEFS; C4.HASTA_COEFS = '2026-11-05'
    try: r = C4.evalua('2026-11-05', dl=str(tmp_path) + '/', btcd=str(tmp_path) + '/rf5_btc/', vol=str(tmp_path), firmas=fi, cortes={}, m5fn=lambda d: True)
    finally: C4.HASTA_COEFS = old
    c = r['condiciones']; assert c['1_btc_ms']['estado'] == 'OK' and c['9_binance_btc_m5_registro']['estado'] == 'OK' and c['10_maker_ms_tokens_btc5_03_17']['estado'] == 'OK' and c['4_adenda_p20_p80_btc']['estado'] == 'OK' and r['estado'] == 'DATA_BLOCKED_BTC'
    fi['cond4_adenda_cortes']['sha256'] = '0' * 64; assert C4.firma('cond4_adenda_cortes', fi)[0] is False                                   # sha distinto => no firmada

def test_prep_day_btc_estados_de_fallo_cerrado(tmp_path):
    (tmp_path / 'sa_ms').mkdir(); dl = str(tmp_path) + '/'; out = str(tmp_path / 'out') + '/'
    assert PB.prep('2026-11-04', dl=dl, out=out) == 'SIN_BTC_MS'; _btc_ms(tmp_path / 'sa_ms' / 'btc_ms_2026-11-04.npz', 0); assert PB.prep('2026-11-04', dl=dl, out=out) == 'SIN_TOKENS_BTC5'
    _btc_ms(tmp_path / 'sa_ms' / 'btc_ms_2026-11-04.npz'); assert PB.prep('2026-11-04', dl=dl, out=out, keep=str(tmp_path) + '/nada/') == 'SIN_ONCHAIN'
    assert hashlib.sha256(open(HV + 'reconstructor_relleno.py', 'rb').read()).hexdigest()[:16] == PB.SHA_RECON
