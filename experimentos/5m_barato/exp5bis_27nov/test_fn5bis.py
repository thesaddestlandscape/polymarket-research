#!/usr/bin/env python3
"""Pruebas de fn5bis (fixture diminuta; sin red ni datos reales). python3 -I -B test_fn5bis.py"""
import sys, os, gzip, json, tempfile
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
import fn5bis_core as C
import fn5bis_etapa2 as S
import cadena_v2v3 as CV

HDR = 'tipo,bloque,ts_est,tx,log_index,order_hash,maker,taker,side,token_id,maker_amt,taker_amt,fee\n'
X, XC = '111', '112'                       # token de la orden y complementario
EXCH = '0xe111180000d2663c0091e4f400237545b87b996b'
OWN = '0x659a40ff9920febc5a66836213040924343d297f'


def fila(t, tx, li, h, maker, taker, side, tok, ma, ta): return f'{t},1,1.0,{tx},{li},{h},{maker},{taker},{side},{tok},{ma},{ta},0\n'


def chain(tmp):
    p = tmp + '/onchain.csv.gz'; r = [HDR]
    # tx A: tomador compra la complementaria a 0,65 contra el bid de un maker ajeno en X a 0,35 (100 acc) -> cruzado, barrido duro de L=0,40
    r += [fila('F', '0xA', 1, '0xh1', '0xmakerajeno1', '0xtomador1', 0, X, 35.0, 100.0), fila('F', '0xA', 2, '0xhT1', '0xtomador1', EXCH, 0, XC, 65.0, 100.0), fila('M', '0xA', 3, '0xhT1', '0xtomador1', '', 0, XC, 65.0, 100.0)]
    # tx B: barrido de 2 acc (<5) a 0,38 en misma ficha (tomador vende X)
    r += [fila('F', '0xB', 1, '0xh2', '0xmakerajeno2', '0xtomador2', 0, X, 0.76, 2.0), fila('F', '0xB', 2, '0xhT2', '0xtomador2', EXCH, 1, X, 0.76, 2.0), fila('M', '0xB', 3, '0xhT2', '0xtomador2', '', 1, X, 0.76, 2.0)]
    # tx C: fila de wallet propia como maker (debe excluirse y contarse) y tx cuyo tomador es propio
    r += [fila('F', '0xC', 1, '0xh3', OWN, '0xtomador3', 0, X, 35.0, 100.0), fila('F', '0xD', 1, '0xh4', '0xmakerajeno4', '0xb6ed7b123b' + '0' * 30, 0, X, 35.0, 100.0)]
    # tx E: a precio por encima de L (no cuenta)
    r += [fila('F', '0xE', 1, '0xh5', '0xmakerajeno5', '0xtomador5', 0, X, 45.0, 100.0)]
    with gzip.open(p, 'wt') as f: f.write(''.join(r))
    return p


def libro5tx(tmp, dia='2026-11-18'):
    os.makedirs(tmp + '/tx', exist_ok=True)
    with gzip.open(tmp + f'/tx/libro5_tx_{dia}_1.csv.gz', 'wt') as f:       # t_ev, token, tx, recv (duplicados y desordenados a proposito)
        f.write('1000,111,0xA,1700\n900,111,0xB,5000\n1000,111,0xA,1650\n1,111,0xD,1\n1,111,0xE,1000\n')
    C.TXD = tmp + '/tx/'


def ordenes(motor_fill_second=False):
    base = dict(coin='eth', clase='lo', token=X, token_comp=XC, size=5.0)
    rows = [dict(base, mid='m1', lado='YES', L=0.40, t_arr=1000, t_end=2000, q=0.0, tf=-1, k=1),           # FN duro cruzado (tx A rx 1650: firme)
            dict(base, mid='m2', lado='YES', L=0.40, t_arr=4800, t_end=6000, q=0.0, tf=-1, k=2),           # tx B 2 acc <5 -> barrido parcial
            dict(base, mid='m3', lado='YES', L=0.40, t_arr=1000, t_end=2300, q=5.0, tf=1600, k=3),         # motor rellena y la cadena no tiene nada cerca de tf=1200 con rx; 0xA a 1050 esta a 150 ms -> respaldada
            dict(base, mid='m4', lado='YES', L=0.40, t_arr=50000, t_end=51000, q=5.0, tf=50500, k=4)]       # FP: relleno sin respaldo
    return pd.DataFrame(rows)


def test_cadena_y_exclusiones():
    with tempfile.TemporaryDirectory() as tmp:
        E, Mk, cont = C.carga_cadena('x', {X}, ruta=chain(tmp))
        assert set(E.tx) == {'0xA', '0xB', '0xE'}, set(E.tx)            # propia (0xC) y tx con tomador propio (0xD) fuera; las filas del tomador (hash en M) fuera
        assert cont['F_maker_wallet_B_exacta'] == 1 and cont['F_filas_con_prefijo_propio'] == 2
        assert abs(float(E[E.tx == '0xA'].price.iloc[0]) - 0.35) < 1e-9 and float(E[E.tx == '0xA'].qty.iloc[0]) == 100.0
        assert C.tipo_casado(Mk, '0xA', X, XC) == 'cruzado' and C.tipo_casado(Mk, '0xB', X, XC) == 'misma_ficha' and C.tipo_casado(Mk, '0xZ', X, XC) == 'sin_M'


def test_rx_min_y_fn_fp_causas():
    with tempfile.TemporaryDirectory() as tmp:
        libro5tx(tmp); E, Mk, cont = C.carga_cadena('x', {X}, ruta=chain(tmp)); rx, _ = C.carga_rx('2026-11-18', set(E.tx))
        assert rx['0xA'] == 1650 and rx['0xB'] == 5000                       # min sobre duplicados desordenados; 0xE=1000
        res, fn, fp, O, units = C.audita_dia(ordenes(), E, Mk, rx, cont, '2026-11-18')
        assert res['FN_duros_unidades'] == 2, res
        causas = {f['mid']: f['causa'] for f in fn}
        assert causas['m1'] == 'cruzado' and causas['m2'] == 'barrido_parcial<5', causas
        assert [f['mid'] for f in fp] == ['m4'], fp                          # m3 respaldado (0xA a 150 ms del tf); m4 sin filas
        assert res['unidades_con_evidencia_dura'] == 3 and res['recall_duro'] is not None
        assert res['FN_nivel_ambiguos_unidades(motor sin relleno y fila ajena EN el nivel; depende de la cola)'] == 0   # 0xE a 0,45 > L no cuenta


def test_borde_y_un_fn_basta():
    with tempfile.TemporaryDirectory() as tmp:
        libro5tx(tmp); E, Mk, cont = C.carga_cadena('x', {X}, ruta=chain(tmp)); rx, _ = C.carga_rx('2026-11-18', set(E.tx)); tev = C.carga_rx.tev; assert tev['0xA'] == 1000
        R = ordenes().iloc[:1].copy(); R['t_arr'] = 1700; R['t_end'] = 2000                 # tx A rx 1650: 50 ms ANTES de la llegada = ambiguo por offset de reloj (FN_offset_ambiguo, cuenta como FN>0)
        res, fn, fp, O, u = C.audita_dia(R, E, Mk, rx, cont, 'd', tev=tev)
        assert res['FN_duros_unidades'] == 0 and res['FN_offset_ambiguos_unidades'] == 1 and fn[0]['causa'] == 'offset_pre<=100ms' and fn[0]['lag_rx_menos_t_ev_ms'] == 650 and fn[0]['casado_rx_est_lo_menos_t_end_ms'] == 1000 + 20 - 2000
        R['t_arr'] = 1900; R['t_end'] = 2200                                                  # a 250 ms: aun no armada -> motor correcto, no FN
        res, fn, fp, O, u = C.audita_dia(R, E, Mk, rx, cont, 'd'); assert res['FN_duros_unidades'] == 0 and res['FN_offset_ambiguos_unidades'] == 0 and not fn
        R['t_arr'] = 1300; R['t_end'] = 1600                                                  # tras t_end: 50 ms -> offset_post
        res, fn, fp, O, u = C.audita_dia(R, E, Mk, rx, cont, 'd'); assert fn[0]['causa'] == 'offset_post<=100ms'
        R['t_arr'] = 3000; R['t_end'] = 3300                                                  # a 1350 ms: fuera incluso del borde -> sin evidencia
        res, fn, fp, O, u = C.audita_dia(R, E, Mk, rx, cont, 'd'); assert res['FN_duros_unidades'] == 0 and not fn


def test_unidad_primer_relleno_motor_unico():
    with tempfile.TemporaryDirectory() as tmp:
        libro5tx(tmp); E, Mk, cont = C.carga_cadena('x', {X}, ruta=chain(tmp)); rx, _ = C.carga_rx('2026-11-18', set(E.tx))
        R = ordenes().iloc[:1].copy(); R2 = R.copy(); R2['L'] = 0.39; R2['q'] = 5.0; R2['tf'] = 1500; R2['t_arr'] = 1400; R2['t_end'] = 1600; R2['tf'] = 1500   # 2 ordenes del mismo (mercado,lado): una sin relleno y otra con
        res, fn, fp, O, u = C.audita_dia(pd.concat([R, R2], ignore_index=True), E, Mk, rx, cont, 'd')
        assert res['unidades'] == 1 and res['unidades_con_relleno_motor'] == 1 and res['FN_duros_unidades'] == 0      # contar (mercado,lado), no ordenes ni fills


def test_calibracion_1b_y_poblacion_completa():
    with tempfile.TemporaryDirectory() as tmp:
        libro5tx(tmp); E, Mk, cont = C.carga_cadena('x', {X}, ruta=chain(tmp)); rx, _ = C.carga_rx('2026-11-18', set(E.tx))
        res, fn, fp, O, u = C.audita_dia(ordenes(), E, Mk, rx, cont, 'd')
        G = C.calibracion_1b(O, 'd'); assert len(G) == 4                      # TODAS las ordenes armadas, rellenadas o no
        s = C.resumen_calibracion(G)['total']
        assert s['n'] == 4 and s['motor1_obs0'] == 1 and s['motor0_obs1'] == 2 and s['motor1_obs1'] == 1 and abs(s['P_motor'] - 0.5) < 1e-9 and abs(s['brier_motor_vs_obs'] - 0.75) < 1e-9, s


def test_idempotencia_y_manifest():
    with tempfile.TemporaryDirectory() as tmp:
        libro5tx(tmp); S.OUT5 = tmp + '/'; S.MIN_FILAS_CADENA_MONEDA = 1; ch = chain(tmp); CV.V2_DIRS = (tmp + '/',); CV.V3_DIRS = (tmp + '/',); os.replace(ch, tmp + '/onchain_fills_2026-11-18.csv.gz')
        Rr = pd.concat([ordenes(), ordenes().iloc[:2].assign(coin='sol', token='999', mid='s1')], ignore_index=True); Rr.to_pickle(tmp + '/ordenes_K6_base_2026-11-18.pkl')
        S.dia('2026-11-18'); j1 = json.load(open(tmp + '/fn5bis_dia_2026-11-18.json')); m1 = os.path.getmtime(tmp + '/fn5bis_dia_2026-11-18.json')
        S.dia('2026-11-18'); assert os.path.getmtime(tmp + '/fn5bis_dia_2026-11-18.json') == m1      # mismas entradas: no rehace (sin doble conteo)
        j2 = json.load(open(tmp + '/fn5bis_dia_2026-11-18.json')); assert j1 == j2 and j1['FN_duros_unidades'] == 2 and j1['monedas_validas'] == ['eth'] and 'sol' in j1['monedas_excluidas_sin_cadena'] and j1['unidades'] == 4
        S.final('2026-11-18,2026-11-24'); f = json.load(open(tmp + '/fn5bis_final.json')); mm = json.load(open(tmp + '/run_manifest.json'))
        assert f['dias_que_faltan'] == ['2026-11-24'] and mm['status'] == 'PARTIAL' and f['totales']['FN_duros'] == 2 and f['veredicto_1a_referencia_propia'].startswith('BLOCKED') and f['totales']['F_maker_wallet_B'] == 1
        # corrupcion: JSON del dia truncado -> se rehace (no se reutiliza basura)
        open(tmp + '/fn5bis_dia_2026-11-18.json', 'w').write('{"entradas_sha16": ')
        S.dia('2026-11-18'); assert json.load(open(tmp + '/fn5bis_dia_2026-11-18.json'))['FN_duros_unidades'] == 2


def test_no_armable_no_cuenta_como_fn():
    with tempfile.TemporaryDirectory() as tmp:
        libro5tx(tmp); E, Mk, cont = C.carga_cadena('x', {X}, ruta=chain(tmp)); rx, _ = C.carga_rx('2026-11-18', set(E.tx))
        R = ordenes().iloc[:1].copy(); R['t_arr'] = 1000; R['t_end'] = 2000                     # evento 0xA a 650 ms de la llegada: firme
        ST = pd.DataFrame(dict(status_motor=['seria_taker']))
        res, fn, fp, O, u = C.audita_dia(R, E, Mk, rx, cont, 'd', status=ST)
        assert res['FN_duros_unidades'] == 0 and res['no_FN_no_armables_unidades_(motor descarta la orden al llegar)'] == 1 and fn[0]['clase_fn'] == 'no_FN_no_armable'
        res, fn, fp, O, u = C.audita_dia(R, E, Mk, rx, cont, 'd', status=pd.DataFrame(dict(status_motor=['ok'])))
        assert res['FN_duros_unidades'] == 1                                                    # con motor 'ok' y evento firme es FN
        R['t_arr'] = 1600; ST2 = pd.DataFrame(dict(status_motor=['ok']))                         # evento a +50 ms de la llegada: AMBIGUO por offset (print ~ casado+20 ms), no FN firme
        res, fn, fp, O, u = C.audita_dia(R, E, Mk, rx, cont, 'd', status=ST2)
        assert res['FN_duros_unidades'] == 0 and res['FN_offset_ambiguos_unidades'] == 1 and fn[0]['causa'] == 'offset_arr<=100ms'


def test_v2_v3_rutas_concatenacion_y_solape():
    with tempfile.TemporaryDirectory() as tmp:
        CV.V2_DIRS = (tmp + '/',); CV.V3_DIRS = (tmp + '/',)
        d = '2026-11-24'
        with gzip.open(tmp + f'/onchain_fills_{d}.csv.gz', 'wt') as f: f.write(HDR + fila('F', '0xV2', 1, '0xhh1', '0xmk1', '0xtk', 0, '111', 35.0, 100.0))
        try: CV.rutas_cadena(d); assert False, 'debia exigir V3'
        except FileNotFoundError: pass                                                    # fail loud: leer solo V2 el 24-Nov dejaria SOL/XRP vacios
        import shutil; shutil.copy(tmp + f'/onchain_fills_{d}.csv.gz', tmp + '/onchain_fills_2026-11-18.csv.gz')
        assert [v for v, _ in CV.rutas_cadena('2026-11-18')] == ['v2']                    # antes del 23-Nov V3 no se exige
        with gzip.open(tmp + f'/onchain_fills_v3_{d}.csv.gz', 'wt') as f: f.write(HDR + fila('F', '0xV3', 1, '0xhh2', '0xmk2', '0xtk', 0, '222', 35.0, 50.0) + fila('F', '0xV2', 2, '0xhh3', '0xmk3', '0xtk', 0, '111', 35.0, 10.0))
        assert [v for v, _ in CV.rutas_cadena(d)] == ['v2', 'v3']
        E, Mk, cont = C.carga_cadena(d, {'111', '222'})
        assert set(E.tx) == {'0xV2', '0xV3'} and cont['F_filas_v2'] == 1 and cont['F_filas_v3'] == 2 and len(E) == 3
        cnt, txs, sol = CV.filas_por_moneda(d, {'111': 'eth', '222': 'sol'})
        assert cnt[('v2', 'eth')] == 1 and cnt[('v3', 'sol')] == 1 and cnt[('v3', 'eth')] == 1 and sol['solape_tx_v2_v3'] == 1        # el solape por tx se DETECTA (aqui provocado)


if __name__ == '__main__':
    n = 0
    for k, v in sorted(globals().items()):
        if k.startswith('test_'): v(); n += 1; print('OK', k)
    print(n, 'pruebas OK')
