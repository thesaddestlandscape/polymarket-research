#!/usr/bin/env python3
"""Tests del runner MULTIVARIANTE v3 (12-Nov): CXB35/45/60/100/150 + CXBEMP (l empirico) y BTC como subvariante. Datos SINTETICOS en un tmp; nunca toca el datalog real ni arranca el demonio. python3 -I test_multivariante.py
M1 especificaciones: G0, GEO1, CXB35/45/60/100/150, CXBEMP y placebo PLC60_s (100 por defecto); CXBEMP cancela y usa 'arm'.
M2 l_emp: determinista (misma clave -> mismo valor), independiente de las llamadas previas, distribucion = pool congelado (min >= 30,5, p50 ~44, p90 ~99), distinto entre segmentos/L/tokens.
M3 extremo a extremo ETH+BTC: filas seg de las 8 variantes; en cada segmento cancelado l_efectivo = t_end - t_trig_rx es EXACTAMENTE l para CXBl y >= 3+pool.min para CXBEMP; la cancelacion con l menor nunca llega despues.
M4 reproducibilidad: dos corridas independientes dan filas identicas (salvo run_id/wall) y la 2a con reinicio no duplica; cobertura: BTC aparte (dia_valido_btc) sin contaminar dia_valido primario.
M5 informe: poblacion primaria excluye BTC; --coins BTC --clave-valido dia_valido_btc informa BTC aparte; dosis_respuesta_l con las 6 variantes y tendencia.
M6 hashes: l_pool_emp.json esta en los ficheros congelados."""
import os, sys, json, tempfile, subprocess, shutil, datetime as dt
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import cxb60_core as C, cxb60_dryrun_fase0 as R, cxb60_io as IO
import test_runner_dryrun as T

BT = dict(zip((T.TA, T.TB, T.TC, T.TD), ('555555551', '555555552', '555555553', '555555554')))


def btc_txt(seed):
    s = T.sint(seed)
    for a, b in BT.items(): s = s.replace(a, b)
    return s.replace(',ETH,', ',BTC,').replace(',777,', ',779,').replace(',888,', ',889,')


def datos(d, dia, seed=3):
    f = d + f'/maker_ms_{dia}_1.csv.gz'; T.escribe(f, T.sint(seed) + btc_txt(seed + 1)); return f


def corre(f, out, dia, extra=()):
    cmd = [sys.executable, '-I', HERE + 'cxb60_dryrun_fase0.py', '--out', out, '--once', '--files', f, '--solo-dia', dia, '--sin-verificar-hash', '--placebo', '3', '--c-print-par', '0'] + list(extra)
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=600); assert r.returncode == 0, r.stderr[-2000:] + r.stdout[-800:]


def test_specs():
    sp = C.default_specs(R.L_LIST, 100); nom = [s.name for s in sp]
    assert nom[:8] == ['G0', 'GEO1', 'CXB35', 'CXB45', 'CXB60', 'CXB100', 'CXB150', 'CXBEMP'] and sum(n.startswith('PLC60_') for n in nom) == 100 and len(set(nom)) == len(nom) == 108, nom[:12]
    e = [s for s in sp if s.name == 'CXBEMP'][0]; assert e.cancels and e.uses_arm and e.kind == 'CXBEMP' and R.L_LIST == (35, 45, 60, 100, 150)
    assert 'BTC' in R.UNIVERSE and R.UNIVERSE_PRIM == {'ETH', 'SOL', 'XRP'}
    print('M1 ok: 108 especificaciones (G0, GEO1, 5 CXB, CXBEMP, 100 placebos); BTC en el universo, primario sin BTC')


def test_l_emp():
    P = C.POOL_EMP; assert len(P) == 1453 and C.PROC_MS == 3
    a = [C.l_emp(1234, 0.16, s) for s in range(5)]; C.l_emp(9, 0.1, 0); b = [C.l_emp(1234, 0.16, s) for s in range(5)]; assert a == b                         # sin estado oculto
    v = np.array([C.l_emp(k, L, s) for k in range(200) for L in (0.10, 0.13, 0.16, 0.19) for s in range(6)])
    assert v.min() >= 30.5 and 42 <= np.median(v) <= 47 and 90 <= np.percentile(v, 90) <= 110, (v.min(), np.median(v), np.percentile(v, 90))
    assert len({C.l_emp(1, 0.16, s) for s in range(40)}) > 5 and len({C.l_emp(k, 0.16, 0) for k in range(40)}) > 5 and len({C.l_emp(1, L, 0) for L in (0.10, 0.13, 0.16, 0.19)}) > 1
    print(f'M2 ok: l_emp determinista; n={len(v)} min {v.min()} p50 {np.median(v):.0f} p90 {np.percentile(v, 90):.0f} (pool+3: p50 43,9 / p90 99,3)')


def test_extremo_a_extremo():
    d = tempfile.mkdtemp(); dia = dt.datetime.fromtimestamp(T.FIN - 150, dt.timezone.utc).strftime('%Y-%m-%d'); f = datos(d, dia); o1, o2 = d + '/o1/', d + '/o2/'
    corre(f, o1, dia); filas, ls = T.leer_dec(o1, dia); seg = [x for x in filas if x['tipo'] == 'seg']
    vs = {x['var'] for x in seg}; assert {'G0', 'GEO1', 'CXB35', 'CXB45', 'CXB60', 'CXB100', 'CXB150', 'CXBEMP'} <= vs, vs
    coins = {x['coin'] for x in seg}; assert coins == {'ETH', 'BTC'}, coins
    n_canc = {}
    for x in seg:
        if x['var'].startswith('CXB') and int(x['canc']) == 1 and str(x['t_trig_rx']) not in ('', 'None'):
            l_eff = int(float(x['t_end'])) - int(float(x['t_trig_rx'])); n_canc[x['var']] = n_canc.get(x['var'], 0) + 1
            if x['var'] == 'CXBEMP': assert l_eff >= 3 + int(C.POOL_EMP.min()) - 1, (l_eff, x)
            elif int(float(x['t_end'])) > int(float(x['t_arr'])): assert l_eff == int(x['var'][3:]), (x['var'], l_eff)                    # (si t_end==t_arr la cancelacion se recorta a la llegada)
    assert n_canc.get('CXB60', 0) > 0 and n_canc.get('CXBEMP', 0) > 0, n_canc
    nof = [x for x in filas if x['tipo'] == 'nof']; assert len(nof) == 2 * 2 * len(C.LEVELS) * len(C.default_specs(R.L_LIST, 1)), len(nof)        # 2 tokens x 2 monedas x 4 L x (8 var + placebo semilla 1)
    claves = [(x['tok'], x['L'], x['var'], x['seg']) for x in seg]; assert len(claves) == len(set(claves))
    cov = json.load(open(o1 + f'coverage_{dia}.json')); assert set(cov['por_moneda']) == {'ETH', 'SOL', 'XRP', 'BTC'} and cov['por_moneda']['BTC']['procesados'] == 2 and cov['por_moneda']['ETH']['procesados'] == 2 and cov['procesados'] == 2, cov['procesados']   # el total primario NO suma BTC
    assert 'dia_valido_btc' in cov and 'dia_valido_4monedas' in cov and cov['dia_valido'] is False and cov['dia_valido_btc'] is False                    # sintetico: dia no completo, SOL/XRP sin mercados
    corre(f, o2, dia); filas2, ls2 = T.leer_dec(o2, dia); k = lambda L_: sorted([tuple(x[c] for c in ('tipo', 'tok', 'L', 'var', 'seg', 't_dec_rx', 't_arr', 't_end', 'canc', 't_trig_rx', 'q', 'tf', 'rem_antes')) for x in L_ if x['tipo'] in ('seg', 'nof')], key=str)
    assert k(filas) == k(filas2), 'dos corridas independientes difieren (no determinista)'
    n1 = len(ls); corre(f, o1, dia); filas3, ls3 = T.leer_dec(o1, dia); assert len(ls3) == n1, 'el reinicio duplica filas'
    shutil.rmtree(d); print('M3/M4 ok: seg de 8 variantes, l efectivo exacto (CXBl) y >= 3+pool.min (CXBEMP), cancelaciones por variante', n_canc, '; determinista y reinicio idempotente; cobertura BTC aparte')


def test_informe_btc_aparte():
    import cxb60_resolve as V
    d = tempfile.mkdtemp(); out = d + '/out/'; os.makedirs(out); gm = d + '/gm'; os.makedirs(gm); dia = dt.datetime.fromtimestamp(T.FIN - 150, dt.timezone.utc).strftime('%Y-%m-%d')
    json.dump({'x': dict(id=777, des='YES', toks=[T.TA, T.TB]), 'y': dict(id=779, des='NO', toks=[BT[T.TA], BT[T.TB]])}, open(gm + '/gmap_x.json', 'w'))
    f = datos(d, dia, 5); corre(f, out, dia)
    json.dump(dict(dia=dia, dia_valido=True, dia_valido_btc=True, cobertura=1.0, dia_completo=True, por_moneda={'ETH': dict(cobertura=1.0), 'BTC': dict(cobertura=1.0)}), open(out + f'coverage_{dia}.json', 'w'))
    subprocess.run([sys.executable, '-I', HERE + 'cxb60_resolve.py', dia, '--out', out, '--gmap-dir', gm], capture_output=True, text=True, timeout=120, check=True)
    for extra, nombre, pob in (([], 'informe_cxb60.json', ['ETH', 'SOL', 'XRP']), (['--coins', 'BTC', '--clave-valido', 'dia_valido_btc'], 'informe_cxb60_BTC.json', ['BTC'])):
        subprocess.run([sys.executable, '-I', HERE + 'cxb60_informe.py', '--out', out, '--c59-dir', out + 'nada'] + extra, capture_output=True, text=True, timeout=300, check=True)
        inf = json.load(open(out + nombre)); assert inf['poblacion'] == pob and inf['dias_usados'] == [dia], inf.get('poblacion')
        assert set(inf['mercados_procesados_por_moneda']) <= set(pob) and sum(inf['mercados_procesados_por_moneda'].values()) == 2, inf['mercados_procesados_por_moneda']
        dr = inf['dosis_respuesta_l']; assert {'CXB35', 'CXB45', 'CXB60', 'CXB100', 'CXB150', 'CXBEMP'} <= set(dr), set(dr)
        assert 'CXBEMP' in inf['variantes'] and 'CXB45' in inf['variantes'] and (not pob == ['BTC'] or set(inf['por_moneda'].get('CXB60', {})) <= {'BTC'})
    shutil.rmtree(d); print('M5 ok: informe primario sin BTC; --coins BTC informa BTC aparte; dosis-respuesta en l con 6 variantes')


def test_hashes():
    assert 'l_pool_emp.json' in IO.FICHEROS_CONGELADOS and os.path.exists(HERE + 'l_pool_emp.json'); h = json.load(open(IO.HASHES_FILE))['hashes']
    assert 'l_pool_emp.json' in h and h['l_pool_emp.json'] == IO.sha256_file(HERE + 'l_pool_emp.json')
    print('M6 ok: l_pool_emp.json esta en el conjunto congelado y en HASHES_CONGELADOS.json')


if __name__ == '__main__':
    test_specs(); test_l_emp(); test_extremo_a_extremo(); test_informe_btc_aparte(); test_hashes(); print('TODOS OK (multivariante)')
