#!/usr/bin/env python3
"""test_l2_rasgos.py -- rasgos L2/15m/D2 del contrato CONTRATO_RASGOS_E1_L2_19nov: orden (rx,pid,seq), dedupe, huecos/truncado, A5, F, A3/A4 con regla de 400 ms, NaN 'stream vivo', no look-ahead, D1, D2 (fail-closed), AUC del indicador de ausencia. Fixtures en memoria."""
import sys, os, tempfile, gzip
import numpy as np, pandas as pd
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import l2_rasgos as L2, e1_modelo as E1
nan = float('nan'); TMP = tempfile.mkdtemp(prefix='l2_test_')
def ln(tipo, rx, tok, c1='', c2='', c3='', seq=0): return f'{tipo},{rx},{tok},{c1},{c2},{c3},{rx},{seq}'
def opener_de(files, rc=None):
    def seq(p):
        s = [int(l.split(',')[7]) for l in files[p]]; return f'#SEQ,{min(s)},{max(s)},{len(s)}' if s else '#SEQ,0,0,0'
    def op(p, tokfile): return iter(files[p] + [seq(p)]), (lambda: ((rc or {}).get(p, 0), 'gzip: unexpected end of file' if (rc or {}).get(p) else ''))
    return op
def arma(files, toks=('T1', 'T2'), rc=None, win=(0, 10 ** 9)):
    rutas = [(p, p) for p in sorted(files)]; ev, hu = L2.materializa('D', {t: win for t in toks}, rutas, opener=opener_de(files, rc), tmpdir=TMP); return ev, hu
def q(files, tok='T1', t=10000, L=0.28, **kw):
    ev, hu = arma(files, **kw); d = L2.L2Dia(ev); return d.libro(tok, t, L), d
BOOK = ln('B', 1000, 'T1', '0.28:100;0.30:20', '0.35:5', '', 1)

def test_orden_rx_pid_seq_sin_mezclar_seq_dedupe_y_perdidos():
    f = {'p1': [ln('B', 900, 'T1', '0.20:10;0.19:5', '0.22:7', '', 1), ln('d', 1000, 'T1', 'B', '0.20', '12', 2), ln('d', 1005, 'T1', 'B', '0.21', '3', 5)],
         'p2': [ln('d', 1000, 'T1', 'B', '0.19', '6', 2)], 'p3': [ln('d', 2000, 'T1', 'B', '0.22', '1', 7), ln('d', 2000, 'T1', 'B', '0.22', '1', 7)]}                                   # mismo seq (2) en OTRO pid: no es duplicado
    ev, hu = arma(f); a, b = int(ev['ini'][0]), int(ev['fin'][0])
    assert ev['rx'][a:b].tolist() == [900, 1000, 1000, 1005, 2000] and [round(float(x), 2) for x in ev['precio'][a:b]][1:3] == [0.20, 0.19]        # (rx, pid, seq): p1 antes que p2 con el mismo rx
    assert hu['duplicadas'] == 1 and hu['ficheros']['p1']['seq_perdidos'] == 2 and hu['ficheros']['p3']['retrocesos_seq'] == 1 and not hu['truncado']          # seq perdidos del stream SIN filtrar (#SEQ)
    assert hu['tokens']['T1']['n_B'] == 1 and hu['tokens']['T1']['n_d'] == 4 and hu['tokens']['T1']['first_rx'] == 900                          # mapa de huecos por (dia, token)
def test_fichero_truncado_y_fuera_de_orden():
    ev, hu = arma({'p1': [BOOK]}, rc={'p1': 1}); assert hu['truncado'] and hu['ficheros']['p1']['truncado']
    ev, hu = arma({'p1': [ln('d', 100000, 'T1', 'B', '0.2', '1', 1), ln('d', 200000, 'T1', 'B', '0.2', '2', 2), ln('d', 50, 'T1', 'B', '0.2', '3', 3)]}); assert hu['ficheros']['p1']['fuera_de_orden'] == 1       # llega mas tarde que el buffer
def test_a5_f_sin_lookahead_y_rewind():
    f = {'p': [BOOK, ln('T', 1500, 'T1', '0.28', 'BUY', '3', 2), ln('T', 1800, 'T1', '0.28', 'SELL', '2', 3), ln('T', 1900, 'T1', '0.30', 'BUY', '9', 4), ln('T', 2500, 'T1', '0.28', 'BUY', '7', 5)]}
    r, d = q(f, t=2000, L=0.28); assert r['a5_huecos'] == 1.0 and r['f_n10'] == 2.0 and r['f_tam10'] == 5.0                               # 0,29 vacio; T de rx 2500 (futuro) NO cuenta
    assert d.libro('T1', 2000, 0.30)['a5_huecos'] == 0.0 and d.libro('T1', 2000, 0.20)['a5_huecos'] == 8.0
    d.libro('T1', 3000, 0.28); r2 = d.libro('T1', 2000, 0.28); assert d.n_rewind == 1 and r2['f_tam10'] == 5.0                              # consulta anterior: rewind y mismo resultado
def test_nan_stream_vivo_baja_y_latido():
    assert all(np.isnan(v) for v in q({'p': [ln('d', 1000, 'T1', 'B', '0.28', '10', 1)]})[0].values())                                       # sin B: libro desconocido, no 'vacio'
    assert all(np.isnan(v) for v in q({'p': [BOOK]}, t=40000)[0].values())                                                                    # >30 s sin eventos y sin latido: grabador caido
    r, _ = q({'p': [BOOK, ln('d', 39500, 'T2', 'B', '0.5', '1', 2)]}, t=40000); assert r['a5_huecos'] == 1.0                                    # latido de OTRO token: mercado quieto = valido (0 movimientos = 0)
    assert all(np.isnan(v) for v in q({'p': [BOOK, ln('G', 5000, 'T1', 'baja', '', '', 2)]}, t=6000)[0].values())                               # baja abierta
    assert q({'p': [BOOK, ln('G', 5000, '*', 'baja', '', '', 2), ln('B', 7000, 'T1', '0.28:100', '0.35:5', '', 3)]}, t=7500)[0]['a5_huecos'] == 0.0   # G global y reapertura por B
    assert all(np.isnan(v) for v in q({'p': [BOOK, ln('G', 5000, '*', 'baja', '', '', 2)]}, t=6000)[0].values())
def test_a3_regla_400ms_cancel_vs_ambiguo_vs_relleno():
    r, _ = q({'p': [ln('B', 1000, 'T1', '0.28:100', '0.35:5', '', 1), ln('d', 9000, 'T1', 'B', '0.28', '60', 2)]}); assert abs(r['a3_cf1'] - 0.4) < 1e-9 and r['a3_amb1'] == 0 and r['a3_sal'] == 0.0     # 40 de 100, rx<=t-400 y sin T
    r, _ = q({'p': [ln('B', 1000, 'T1', '0.28:100', '0.35:5', '', 1), ln('d', 9000, 'T1', 'B', '0.28', '60', 2), ln('T', 9100, 'T1', '0.28', 'SELL', '40', 3)]}); assert r['a3_cf1'] == 0.0     # T compatible: era un relleno, no cancelacion
    r, _ = q({'p': [ln('B', 1000, 'T1', '0.28:100', '0.35:5', '', 1), ln('d', 9700, 'T1', 'B', '0.28', '90', 2), ln('d', 9900, 'T1', 'B', '0.28', '85', 3)]})
    assert r['a3_cf1'] == 0.0 and abs(r['a3_amb2'] - 10 / 100) < 1e-9 and abs(r['a3_amb3'] - 5 / 90 * 1.0) < 1e-6 or abs(r['a3_amb3'] - 5 / 90) < 1e-6        # ultimos 400 ms: SOLO ambiguo, jamas cancel
    r, _ = q({'p': [ln('B', 1000, 'T1', '0.28:100', '0.35:5', '', 1), ln('d', 9000, 'T1', 'B', '0.28', '0', 2)]}); assert r['a3_cf1'] == 1.0 and r['a3_sal'] == 1.0                             # salida total
    r, _ = q({'p': [ln('B', 1000, 'T1', '0.28:100', '0.35:5', '', 1), ln('d', 9000, 'T1', 'B', '0.28', '60', 2), ln('d', 10500, 'T1', 'B', '0.28', '1', 3)]}); assert abs(r['a3_cf1'] - 0.4) < 1e-9   # rx 10500 > t: no existe
def test_a4_niveles_mejores():
    r, _ = q({'p': [ln('B', 1000, 'T1', '0.28:100;0.30:20', '0.35:5', '', 1), ln('d', 9000, 'T1', 'B', '0.30', '5', 2)]}); assert abs(r['a4_cf1'] - 15 / 20) < 1e-9 and r['a3_cf1'] == 0.0
def test_d1_k15_correcto_cruzado_stale_y_sin_cambio():
    ev, hu = arma({'p': []}); m15 = dict(tok={('ETH', 4500, 'YES'): 'K15', ('ETH', 5400, 'YES'): 'K15b'}, q={'K15': (np.array([1000, 9500], np.int64), np.array([0.40, 0.45]), np.array([0.50, 0.50]))}); d = L2.L2Dia(ev, m15)
    assert d.tok15('eth', 3900, 'YES') == 'K15' and d.tok15('eth', 4500, 'YES') == 'K15' and d.tok15('eth', 4800, 'YES') == 'K15b'                        # 15m que CONTIENE al 5m, no el previo (fuga 29-Oct)
    r = d.d1('K15', 10000); assert abs(r['d1_dbid15'] - 0.05) < 1e-12 and r['d1_sin_cambio'] == 0.0; r = d.d1('K15', 20000); assert r['d1_dbid15'] == 0.0 and r['d1_sin_cambio'] == 1.0
    assert np.isnan(d.d1('K15', 50000)['d1_dbid15']) and np.isnan(d.d1('nada', 10000)['d1_dbid15'])
    d.m15['q']['K15'] = (np.array([1000, 9500], np.int64), np.array([0.40, 0.60]), np.array([0.50, 0.50])); assert np.isnan(d.d1('K15', 10000)['d1_dbid15'])         # libro cruzado descartado
def test_d2_twap60_aprox_rx_y_failclosed():
    ev, hu = arma({'p': []}); e0 = 1_000_000; fin = e0 // 1000 + 300
    cl = {'eth': (np.array([e0 - 30000, e0, e0], np.int64), np.array([e0 - 28600, e0 + 1400, e0 + 1500], np.int64), np.array([99.8, 100.2, 100.2]))}; bs = {'eth': (np.array([e0 + 500], np.int64), np.array([100.1]))}
    d = L2.L2Dia(ev, cl=cl, bsrc=bs); assert abs(d.d2('eth', fin, e0 + 2000, 'YES') - 10.0) < 1e-6 and abs(d.d2('eth', fin, e0 + 2000, 'NO') + 10.0) < 1e-6            # TWAP60 = (media30 en ws=e0 + media30 en ws=e0-30 s)/2 = 100,0
    assert np.isnan(d.d2('eth', fin, e0 + 1000, 'YES'))                                                                                                              # la fila ws=e0 llega a rx=e0+1400: antes NaN por diseno (no fuga)
    d = L2.L2Dia(ev, cl={'eth': (cl['eth'][0][1:], cl['eth'][1][1:], cl['eth'][2][1:])}, bsrc=bs); assert np.isnan(d.d2('eth', fin, e0 + 2000, 'YES'))                  # falta la fila ws=e0-30: NaN, no se imputa
    p = TMP + '/chainlink_2026-10-26.csv'; open(p, 'w').write('timestamp_utc,asset,price_usd,ws_timestamp_ms,source\n2026-10-26T00:00:00.172+00:00,ETH,100.0,1792972799000,chainlink\n2026-10-26T00:00:00.300+00:00,ETH,999.0,1792972799000,polybolt_fallback\n')
    c = L2.carga_chainlink('2026-10-26', dirs=(TMP + '/',)); assert c['eth'][2].tolist() == [100.0] and c['eth'][1][0] == 1792972800172              # filtra source; reloj rx = timestamp_utc
    try: L2.carga_chainlink('2026-10-29', dirs=(TMP + '/',)); assert False
    except FileNotFoundError: pass                                                                                                               # fail-closed si falta el dia
def test_d2_contraste_polybolt_twap60_oficial():
    pbp = '/root/polymarket-research/data/prices/polybolt_2026-11-04.csv.gz'
    if not os.path.exists(pbp) or not os.path.exists('/root/polymarket-research/data/prices/chainlink_2026-11-04.csv.gz'): print('SKIP polybolt/chainlink 2026-11-04 ausentes'); return
    pb = pd.read_csv(pbp, usecols=['canal', 'asset', 'value', 'event_ts_ms']); tw = pb[(pb.canal == 'twap60') & (pb.asset == 'ETH')].drop_duplicates('event_ts_ms').set_index('event_ts_ms').value
    cl = L2.carga_chainlink('2026-11-04'); ev, hu = arma({'p': []}); res = []
    for e0 in tw.index[::97][:400]:
        bs = {'eth': (np.array([e0 + 3000], np.int64), np.array([2000.0]))}; d = L2.L2Dia(ev, cl=cl, bsrc=bs); x = d.d2('eth', int(e0 // 1000) + 300, int(e0) + 5000, 'YES')
        if np.isfinite(x): res.append((2000.0 / (1 + x / 1e4)) / tw[e0] - 1)
    r = np.array(res) * 1e4; assert len(r) >= 300 and abs(r.mean()) < 1.0 and np.percentile(r, 5) > -6 and np.percentile(r, 95) < 6, (len(r), r.mean())       # observado 04-Nov ETH n=389: media +0,1, p5 -3,3, p95 +4,2 bps vs twap60 oficial
def test_carga_m15_k_y_q():
    p = TMP + '/m15.csv.gz'; rows = ['k,1,KA,ETH,15min,77,2026-11-06 01:15:00+00:00,YES', 'k,1,KB,ETH,60min,78,2026-11-06 02:00:00+00:00,YES', 'q,5,KA,0.4,0.5,1,1,100', 'q,5,KB,0.4,0.5,1,1,100', 'q,4,KA,0.3,0.5,1,1,90']
    gzip.open(p, 'wt').write('\n'.join(rows) + '\n'); m = L2.carga_m15(p); assert list(m['tok'].values()) == ['KA'] and m['q']['KA'][0].tolist() == [90, 100] and 'KB' not in m['q']          # solo 15min; ordenado por recepcion
def test_auc_indicador_ausencia_azar_ok_y_fuga_detectada():
    rng = np.random.default_rng(0); rows = []
    for d in ('d1', 'd2', 'd3'):
        y = rng.integers(0, 2, 400); nanm = rng.random(400) < 0.3; v = np.where(nanm, nan, 1.0); lk = np.where(y == 1, rng.random(400) < 0.8, rng.random(400) < 0.2); v2 = np.where(lk, nan, 1.0)
        rows.append(pd.DataFrame(dict(dia=d, y=y, a5_huecos=v, f_n10=v2)))
    r = E1.fuga_nan_por_rasgo(pd.concat(rows), feats=['a5_huecos', 'f_n10']); assert r['a5_huecos']['estado'] == 'OK' and r['f_n10']['estado'] == 'FUGA_SOSPECHOSA'          # AUC ~0,5 por dia vs fuga
def test_fix1_snapshot_no_borra_historia_y_aporta_diferencia():
    base = [ln('B', 1000, 'T1', '0.28:100', '0.35:5', '', 1), ln('d', 9000, 'T1', 'B', '0.28', '60', 2)]
    r, _ = q({'p': base + [ln('B', 9500, 'T1', '0.28:60', '0.35:5', '', 3)]}); assert abs(r['a3_cf1'] - 0.4) < 1e-9                                         # un B sin cambios NO borra la baja de 9000
    r, _ = q({'p': base + [ln('B', 9600, 'T1', '0.28:50', '0.35:5', '', 3)]}); assert abs(r['a3_cf1'] - 0.5) < 1e-9                                         # la diferencia del snapshot (-10) entra como cambio de nivel
    r, _ = q({'p': base + [ln('G', 9500, 'T1', 'baja', '', '', 3), ln('B', 9600, 'T1', '0.28:60', '0.35:5', '', 4)]}); assert r['a3_cf1'] == 0.0                # baja/arranque SI vacian la historia
def test_fix3_misma_clave_dos_bajas_mismo_rx():
    r, _ = q({'p': [ln('B', 1000, 'T1', '0.28:100', '0.35:5', '', 1), ln('d', 9000, 'T1', 'B', '0.28', '60', 2), ln('d', 9000, 'T1', 'B', '0.28', '20', 3)]}); assert abs(r['a3_cf1'] - 0.8) < 1e-9     # 100->60->20: 40+40, sin pisarse
def test_fix4_memoria_cursores_slices_eviccion_y_preroll():
    import tracemalloc
    n = 150_000; lines = [ln('B', 1000, 'T1', '0.28:100', '0.35:5', '', 0)] + [ln('d', 5000 + i, 'T1', 'B', '0.28', str(50 + i % 40), i + 1) for i in range(n)] + [ln('d', 500, 'T1', 'B', '0.28', '1', n + 5)]
    tracemalloc.start(); ev, hu = L2.materializa('D', {'T1': (1000, 5000 + n + 10, 'ETH#5min')}, [('p', 'p')], opener=opener_de({'p': lines}), tmpdir=TMP); peak = tracemalloc.get_traced_memory()[1]; tracemalloc.stop()
    assert peak < 80e6 and hu['n_eventos'] == n + 1 and (ev['rx'] >= 1000).all(), peak                                                                          # limite explicito; el evento de rx 500 (< ini) NO se guarda
    d = L2.L2Dia(ev); d.libro('T1', 5000 + n // 2, 0.28); assert d.cur and all(not isinstance(v, list) for c in d.cur.values() for v in c.values()) and not any(isinstance(v, list) for v in d.__dict__.values() if False)
    d.libro('T1', 5000 + n + 100, 0.28); assert not d.cur                                                                                                          # mercado cerrado: cursor desalojado
def test_fix5_latido_misma_conexion_y_tope_de_edad():
    f = {'p': [BOOK, ln('d', 39500, 'T2', 'B', '0.5', '1', 2)]}; kw = lambda c2: dict(win=(0, 10 ** 9)); ev, hu = L2.materializa('D', {'T1': (0, 10 ** 9, 'ETH#5min'), 'T2': (0, 10 ** 9, 'SOL#5min')}, [('p', 'p')], opener=opener_de(f), tmpdir=TMP)
    assert all(np.isnan(v) for v in L2.L2Dia(ev).libro('T1', 40000, 0.28).values())                                                                                 # latido de OTRA moneda no valida un libro parado
    ev, hu = L2.materializa('D', {'T1': (0, 10 ** 9, 'ETH#5min'), 'T2': (0, 10 ** 9, 'ETH#5min')}, [('p', 'p')], opener=opener_de(f), tmpdir=TMP); assert L2.L2Dia(ev).libro('T1', 40000, 0.28)['a5_huecos'] == 1.0   # misma conexion: quieto valido
    f2 = {'p': [BOOK, ln('d', 200000, 'T2', 'B', '0.5', '1', 2)]}; ev, hu = L2.materializa('D', {'T1': (0, 10 ** 9, 'ETH#5min'), 'T2': (0, 10 ** 9, 'ETH#5min')}, [('p', 'p')], opener=opener_de(f2), tmpdir=TMP)
    assert all(np.isnan(v) for v in L2.L2Dia(ev).libro('T1', 200100, 0.28).values())                                                                                # libro propio de 199 s: ni con latido (tope 120 s)
def test_fix_menores_d1_cruzado_en_j_bid_vacio_y_orden_por_token():
    ev, hu = arma({'p': []}); m15 = dict(tok={}, q={'K': (np.array([1000, 9500], np.int64), np.array([0.60, 0.05]), np.array([0.50, 0.50]))}); assert np.isnan(L2.L2Dia(ev, m15).d1('K', 10000)['d1_dbid15'])     # cruzado en t-1000
    m15['q']['K'] = (np.array([1000, 9500], np.int64), np.array([0.40, nan]), np.array([0.50, 0.50])); assert np.isnan(L2.L2Dia(ev, m15).d1('K', 10000)['d1_dbid15'])                              # bid vacio = NaN
    p = TMP + '/m15b.csv.gz'; gzip.open(p, 'wt').write('k,1,KA,ETH,15min,77,2026-11-06 01:15:00+00:00,YES\nq,5,KA,,0.5,1,1,100\nq,5,KA,0.4,0.5,1,1,90\n'); m = L2.carga_m15(p); assert np.isnan(m['q']['KA'][1][1]) and len(m['q']['KA'][0]) == 2   # fila con bid vacio se conserva como NaN
    ev, hu = arma({'p': [ln('d', 100000, 'T1', 'B', '0.2', '1', 1), ln('d', 200000, 'T1', 'B', '0.2', '2', 2), ln('d', 50, 'T1', 'B', '0.2', '3', 3)]}); a, b = int(ev['ini'][0]), int(ev['fin'][0]); assert ev['rx'][a:b].tolist() == [50, 100000, 200000]   # ordenado por (rx, pid, seq) tras materializar
def test_seguridad_l2():
    src = open(HV + 'l2_rasgos.py').read()
    for p in ('post_order', 'create_order', 'py_clob_client', 'dotenv', 'private_key', 'pkill', 'pgrep', 'tx_hash', 'takerFill'): assert p not in src, p
if __name__ == '__main__':
    ts = [(n, f) for n, f in sorted(globals().items()) if n.startswith('test_') and callable(f)]
    for n, f in ts: f(); print('OK', n)
    print(len(ts), 'tests OK')
