"""Tests de relojes (fixtures diminutas, sin datos reales): extractor v2, Day2 (ex/rx), idempotencia, integridad (assert real), seguridad dry-run.
Ejecutar: cd l2_carrera_10nov && python3 -m pytest -q test_relojes.py"""
import os, sys, gzip, json, hashlib, importlib, re
import numpy as np, pandas as pd, pytest
H = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, H)

DIA = '2026-11-03'; FIN = '2026-11-03 12:05:00+00:00'
FINMS = int(pd.Timestamp(FIN).timestamp() * 1000)
TOK_Y, TOK_N = 'tokY' + '1' * 10, 'tokN' + '2' * 10


def _fixture(dl):
    """maker_ms_<DIA>_1.csv.gz: 2 tokens ETH 5min. q: (ex, rx). Incluye: orden rx invertido (lote), rx ausente, fila fuera de ventana, token ajeno, fila x/b."""
    base = FINMS - 200000
    rows = ['k,%d,%s,ETH,5min,55001,%s,YES' % (base, TOK_Y, FIN), 'k,%d,%s,ETH,5min,55001,%s,NO' % (base, TOK_N, FIN),
            'k,%d,tokZ,BTC,5min,55002,%s,YES' % (base, FIN),
            'x,%d,ETHUSDT,2250.0,1.0,0,%d,%d' % (base, base, base + 3),
            'q,%d,%s,0.20,0.25,10.0,12.0,%d' % (base + 1000, TOK_Y, base + 1019),
            'q,%d,%s,0.21,0.25,11.0,12.0,%d' % (base + 1100, TOK_Y, base + 1250),      # lote retrasado: llega DESPUES de la fila siguiente (orden de llegada != orden exchange)
            'q,%d,%s,0.22,0.26,11.0,12.0,%d' % (base + 1200, TOK_Y, base + 1219),
            'q,%d,%s,0.19,0.27,11.0,12.0,' % (base + 1300, TOK_Y),                      # rx ausente
            'q,%d,%s,0.30,0.31,1.0,1.0,%d' % (FINMS - 900000, TOK_Y, FINMS - 899900),   # fuera de ventana (LO)
            'q,%d,tokZ,0.30,0.31,1.0,1.0,%d' % (base + 1000, base + 1010),              # token ajeno
            'q,%d,%s,0.80,0.81,5.0,6.0,%d' % (base + 1000, TOK_N, base + 1030),
            't,%d,%s,0.20,SELL,5.5,%d,' % (base + 1500, TOK_Y, base + 1540),
            't,%d,%s,0.20,BUY,2.0,,' % (base + 1600, TOK_Y)]                            # t sin rx
    with gzip.open(dl + f'maker_ms_{DIA}_1.csv.gz', 'wt') as f: f.write('\n'.join(rows) + '\n')
    return base


@pytest.fixture()
def dl(tmp_path, monkeypatch):
    d = str(tmp_path / 'dl') + '/'; os.makedirs(d)
    monkeypatch.setenv('SA2_DL', d); monkeypatch.setenv('SA2_OUT', d + 'sa_ms2/')
    base = _fixture(d)
    for m in ('ms_extract_v2', 'relojes'):
        sys.modules.pop(m, None)
    return d, base


def test_extractor_dos_relojes_e_idempotencia(dl):
    d, base = dl
    X = importlib.import_module('ms_extract_v2')
    of = X.day(DIA)
    z = np.load(of, allow_pickle=True); t0 = int(z['t0'])
    ky = list(z['tokens']).index(TOK_Y); qk = z['q_k']; ex = z['q_t_ex'].astype(np.int64) + t0; rx = z['q_t_rx'].astype(np.int64); rx = np.where(rx >= 0, rx + t0, -1)
    assert len(ex) == 5                                       # 4 de TOK_Y + 1 de TOK_N (fuera de ventana y token ajeno descartados)
    assert list(ex[qk == ky]) == [base + 1000, base + 1100, base + 1200, base + 1300]   # orden exchange (= v1)
    assert list(rx[qk == ky]) == [base + 1019, base + 1250, base + 1219, -1]
    assert sorted(z['t_t_rx'].tolist()) == [-1, base + 1540 - t0]
    man = json.load(open(of[:-4] + '.manifest.json'))
    assert man['contadores']['q_rx_missing'] == 1 and man['contadores']['t_rx_missing'] == 1 and man['estado'] == 'COMPLETE'
    h1 = hashlib.sha256(open(of, 'rb').read()).hexdigest()
    X.day(DIA)                                                # reinicio idempotente: no reescribe
    assert hashlib.sha256(open(of, 'rb').read()).hexdigest() == h1
    assert not [f for f in os.listdir(os.path.dirname(of)) if '.tmp' in f]


def test_day2_vistas(dl):
    d, base = dl
    importlib.import_module('ms_extract_v2').day(DIA)
    R = importlib.import_module('relojes')
    ex, rx = R.Day2(DIA, 'ex', with_otro=True), R.Day2(DIA, 'rx', with_otro=True)
    k = ex.tokidx[TOK_Y]
    a, b = ex.qb[k], ex.qb[k + 1]; assert b - a == 4
    assert list(ex.v0[a:b]) == pytest.approx([0.20, 0.21, 0.22, 0.19]) and ex.n_sin_rx == 1
    a, b = rx.qb[k], rx.qb[k + 1]; assert b - a == 3 and rx.n_sin_rx == 1          # la fila sin rx se descarta de la vista rx
    assert list(rx.qt[a:b]) == [base + 1019, base + 1219, base + 1250]               # orden de LLEGADA
    assert list(rx.v0[a:b]) == pytest.approx([0.20, 0.22, 0.21])
    assert [rx.otro(i) for i in range(a, b)] == [base + 1000, base + 1200, base + 1100]
    assert ex.book(k, base + 1230)[0] == pytest.approx(0.22) and rx.book(k, base + 1230)[0] == pytest.approx(0.22)
    assert ex.book(k, base + 1260)[0] == pytest.approx(0.22) and rx.book(k, base + 1260)[0] == pytest.approx(0.21)   # ultimo en LLEGAR manda en rx
    assert ex.book(k, base + 1150)[0] == pytest.approx(0.21) and rx.book(k, base + 1150)[0] == pytest.approx(0.20)    # el exchange ya tiene 0.21; a nosotros aun no nos ha llegado
    # trades: ex ve ambos, rx solo el que tiene recepcion
    assert (ex.tb[k + 1] - ex.tb[k]) == 2 and (rx.tb[k + 1] - rx.tb[k]) == 1


def test_engine_clock_conocimiento_rx_mecanica_ex(dl):
    d, base = dl
    importlib.import_module('ms_extract_v2').day(DIA)
    EC = importlib.import_module('engine_clock')
    L = EC.DayEngClock(DIA, 'chain', pd.DataFrame(dict(side=[], t_ws_ms=[], tx=[], log_index=[], token_id=[], price=[], sh=[])), modo='legacy')
    C = EC.DayEngClock(DIA, 'chain', pd.DataFrame(dict(side=[], t_ws_ms=[], tx=[], log_index=[], token_id=[], price=[], sh=[])), modo='causal')
    k = L.D.tokidx[TOK_Y]; t = np.array([base + 1150, base + 1230])
    assert list(L.quotes(k, t)[0]) == pytest.approx([0.21, 0.22])         # legacy: conocimiento en exchange (0.21 ya 'conocido' en 1150)
    assert list(C.quotes(k, t)[0]) == pytest.approx([0.20, 0.22])         # causal: en 1150 solo habia llegado 0.20
    # fill view de causal es exchange; K es recepcion
    assert C.clock_fill == 'ex' and C.clock_know == 'rx' and C.D.clock == 'ex' and C.K.clock == 'rx'


def test_assert_real_rellenos_sin_segmento(tmp_path, monkeypatch):
    sys.modules.pop('paso0_lib_v2', None)
    P = importlib.import_module('paso0_lib_v2')
    F = pd.DataFrame(dict(dia=['2026-11-03'] * 2, k=[1, 2], L=[0.1, 0.1], seg=[0, 0], q=[5.0, 5.0], gana=[0.0, 1.0], pnl=[0.0, 0.0], tf=[1, 2], t_dec=[1, 2], fin=[1, 2], token=['a', 'b'], act=['ETH', 'ETH'], cost=[0.5, 0.5]))
    S = pd.DataFrame(dict(dia=['2026-11-03'], k=[1], L=[0.1], seg=[0], bidL=[0.07], T=[200.0]))
    fp, sp = str(tmp_path / 'f.pkl'), str(tmp_path / 's.pkl'); F.to_pickle(fp); S.to_pickle(sp)
    with pytest.raises(RuntimeError, match='sin segmento'):
        P.cargar(fp, sp, dias=['2026-11-03'])


def test_dryrun_sin_imports_de_envio():
    prohibido = re.compile(r'^\s*(import|from)\s+(py_clob_client|web3|eth_account|requests|websockets|aiohttp|live_trade|live_guard|ejecutor_rapido)', re.M)
    for f in ('ms_extract_v2.py', 'relojes.py', 'engine_clock.py', 'passT_v2.py', 'paso0_lib_v2.py', 'calib_relojes.py', 'anclas_relojes.py'):
        p = H + f
        if os.path.exists(p): assert not prohibido.search(open(p).read()), f


def test_calibracion_y_tramas(dl, tmp_path, monkeypatch):
    d, base = dl
    importlib.import_module('ms_extract_v2').day(DIA)
    monkeypatch.setenv('CALIB_OUT', str(tmp_path / 'calib') + '/'); sys.modules.pop('calib_relojes', None)
    C = importlib.import_module('calib_relojes')
    R = C.dia(DIA)
    assert R['q']['n'] == 4 and R['q_sin_rx'] == 1 and R['t']['n'] == 1 and R['t_sin_rx'] == 1
    # trama: edad/tamano
    ex = np.array([100, 110, 300]); rx = np.array([150, 150, 400])
    edad, nt, dp = C.tramas(ex, rx)
    assert list(nt) == [2, 2, 1] and list(edad) == [10, 0, 0] and list(dp) == [10, 10, 0]
