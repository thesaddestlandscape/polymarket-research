"""Tests de e1b_diario.py / e1b_eval.py. Ejecutar:  cd .../seleccion_adversa_plan/e1b && python3 -m pytest -q tests
Fixture minima sintetica (1 mercado ETH 5m en un dia pasado) para reinicio idempotente, manifest corrupto, gzip truncado, duplicados, cobertura."""
import os, sys, json, gzip, shutil, subprocess, hashlib
import numpy as np, pandas as pd, pytest

AQUI = os.path.dirname(os.path.abspath(__file__)); E1B_CODE = os.path.abspath(os.path.join(AQUI, '..'))
sys.path.insert(0, E1B_CODE)
import e1b_eval as EV

DIA = '2026-10-10'
FIN = int(pd.Timestamp('2026-10-10 12:05:00', tz='UTC').timestamp())      # cierre del 5m
FIN15 = int(pd.Timestamp('2026-10-10 12:15:00', tz='UTC').timestamp())
TOK = {'Y5': '111', 'N5': '112', 'Y15': '221', 'N15': '222'}


def fila_q(t, tok, b, a, recv): return f'q,{t},{tok},{b},{a},5.0,5.0,{recv}'
def gz(path, lines):
    with gzip.open(path, 'wt') as f: f.write('\n'.join(lines) + '\n')


def montar_fuentes(root, trunc=False, tev_lag=0):
    vol = root / 'vol'; dl = root / 'dl'; (vol / 'm5_registro').mkdir(parents=True); (vol / 'm15_registro').mkdir(parents=True); dl.mkdir()
    fs = lambda e: pd.Timestamp(e, unit='s', tz='UTC').strftime('%Y-%m-%d %H:%M:%S+00:00')
    k5 = [f'k,{FIN*1000-400000},{TOK["Y5"]},ETH,5min,900001,{fs(FIN)},YES', f'k,{FIN*1000-400000},{TOK["N5"]},ETH,5min,900001,{fs(FIN)},NO']
    k15 = [f'k,{FIN*1000-800000},{TOK["Y15"]},ETH,15min,900002,{fs(FIN15)},YES', f'k,{FIN*1000-800000},{TOK["N15"]},ETH,15min,900002,{fs(FIN15)},NO']
    t0 = (FIN - 290) * 1000                                                  # puja viva desde aqui (bid 0,20 -> obj 0,18 en ETH)
    q = [fila_q(t0, TOK['Y5'], 0.20, 0.22, t0), fila_q(t0, TOK['N5'], 0.78, 0.80, t0), fila_q(t0 - 5000, TOK['Y15'], 0.25, 0.27, t0 - 5000)]
    tf = (FIN - 200) * 1000                                                  # un SELL propio a 0,17 < 0,18 : relleno
    t = [f't,{tf - tev_lag},{TOK["Y5"]},0.17,SELL,10,{tf},']      # tev = recepcion - tev_lag
    # Binance ETH cae 5 bps en los 2 s previos al print: S1 (<= -2 bps) debe dispararse
    x = [f'x,{tf-3000},ETHUSDT,2000.0,1,0,{tf-3000},{tf-3000}', f'x,{tf-1500},ETHUSDT,1999.0,1,0,{tf-1500},{tf-1500}', f'x,{tf-500},ETHUSDT,1998.5,1,0,{tf-500},{tf-500}',
         f'x,{tf-3000},SOLUSDT,100.0,1,0,{tf-3000},{tf-3000}', f'x,{tf-3000},XRPUSDT,1.0,1,0,{tf-3000},{tf-3000}']
    gz(vol / 'm5_registro' / f'm5_registro_{DIA}.csv.gz', k5 + q + t + x)
    gz(vol / 'm15_registro' / f'm15_registro_{DIA}.csv.gz', k15 + q[-1:])
    if trunc:
        p = vol / 'm5_registro' / f'm5_registro_{DIA}.csv.gz'; b = p.read_bytes(); p.write_bytes(b[:len(b) // 2])
    cache = root / 'cache.json'; cache.write_text(json.dumps({'900001': 'NO'}))   # gana NO -> perdemos 0,18/acc: S1 evita la perdida
    return vol, dl, cache


def lanzar(root, dias=None, extra_env=None):
    env = dict(os.environ, E1B_DIR=str(root / 'e1b'), E1B_SRC_VOL=str(root / 'vol'), E1B_SRC_DL=str(root / 'dl'), E1B_CACHE_DES=str(root / 'cache.json'))
    env.update(extra_env or {})
    return subprocess.run([sys.executable, '-I', os.path.join(E1B_CODE, 'e1b_diario.py'), 'run', '--dias', dias or DIA], env=env, capture_output=True, text=True)


def sha(p):
    # contenido descomprimido (la cabecera gzip lleva mtime)
    return hashlib.sha256(gzip.open(p, 'rb').read() if p.name.endswith('.gz') else open(p, 'rb').read()).hexdigest() if hasattr(p, 'name') else hashlib.sha256(open(p, 'rb').read()).hexdigest()


# ---------------------------------------------------------------- orquestador
def test_extraccion_idempotente_reinicio_y_sin_duplicados(tmp_path):
    montar_fuentes(tmp_path); (tmp_path / 'e1b').mkdir()
    r = lanzar(tmp_path); assert r.returncode in (0, 3), r.stderr[-2000:]
    E = tmp_path / 'e1b'; M = json.load(open(E / 'dias' / f'{DIA}.json'))
    assert M['etapas']['extract']['ok'] and M['etapas']['sim']['ok'], M
    assert M['estado'] == 'PARTIAL'                              # 1 mercado de 864 esperados -> dia NO valido (cobertura, no se disfraza)
    assert M['cobertura']['esperados'] == 864 and M['cobertura']['recibidos_dia'] == 1 and M['cobertura']['con_desenlace'] == 1
    X = pd.read_csv(E / f'e1_{DIA}.csv.gz'); B = X[X['var'] == 'BASE']
    assert len(B) == 1 and B.fill.iloc[0] == 1 and abs(B.obj.iloc[0] - 0.18) < 1e-9 and not X.duplicated(['mid', 'var']).any()
    s1 = X[X['var'] == 'S1_x2_w2000|D100']; assert s1.fill.iloc[0] == 0          # la senal retira la puja: no hay otro candidato
    inv = X[X['var'] == 'S1_x2_w2000|INV']; assert inv.fill.iloc[0] == 1          # inversion: no hay senal a favor
    Y = pd.read_csv(E / f'e1x_{DIA}.csv.gz'); assert not Y.duplicated(['mid', 'var']).any() and Y.n_cand.iloc[0] == B.n_cand.iloc[0] == 1
    assert Y[Y['var'] == 'S1_x2_w2000|X50'].fill.iloc[0] == 0 and Y[Y['var'] == 'S1_x2_w2000|INV250'].fill.iloc[0] == 1 and len(Y[Y['var'].str.endswith('_250')]) == 8
    assert Y[Y['var'] == 'C1|D250'].shape[0] == 1 and Y[Y['var'] == 'C2|FILL'].shape[0] == 1
    aux = pd.read_csv(E / f'aux_{DIA}.csv.gz'); assert abs(aux.lvl15.iloc[0] - 0.07) < 1e-6     # bid15 0,25 - obj 0,18 -> R2-falso
    h1 = {f: sha(E / f) for f in (f'e1_{DIA}.csv.gz', f'aux_{DIA}.csv.gz', f'e1x_{DIA}.csv.gz')}; npz1 = os.path.getmtime(E / f'ms_{DIA}.npz')
    # reinicio: no rehace nada
    r2 = lanzar(tmp_path); assert r2.returncode in (0, 3)
    assert 'extract: ya hecho' in r2.stdout and 'sim: ya hecha' in r2.stdout
    assert os.path.getmtime(E / f'ms_{DIA}.npz') == npz1 and {f: sha(E / f) for f in h1} == h1
    # manifest corrupto: se aparta (.corrupto), se rehace y el resultado es identico (sin filas duplicadas)
    (E / 'dias' / f'{DIA}.json').write_text('{"etapas": {"extract": {"ok": tr')
    r3 = lanzar(tmp_path); assert r3.returncode in (0, 3), r3.stderr[-1500:]
    assert any('corrupto' in f for f in os.listdir(E / 'dias'))
    X3 = pd.read_csv(E / f'e1_{DIA}.csv.gz'); assert not X3.duplicated(['mid', 'var']).any() and len(X3) == len(X)
    assert {f: sha(E / f) for f in h1} == h1
    # npz borrado a medias / basura: se vuelve a extraer
    (E / f'ms_{DIA}.npz').write_bytes(b'basura'); r4 = lanzar(tmp_path); assert r4.returncode in (0, 3)
    assert {f: sha(E / f) for f in h1} == h1


def test_gzip_truncado_es_BLOCKED_y_no_produce_filas(tmp_path):
    montar_fuentes(tmp_path, trunc=True); (tmp_path / 'e1b').mkdir()
    r = lanzar(tmp_path); M = json.load(open(tmp_path / 'e1b' / 'dias' / f'{DIA}.json'))
    assert M['estado'] == 'BLOCKED' and 'gzip' in M['motivo']; assert not (tmp_path / 'e1b' / f'e1_{DIA}.csv.gz').exists()


def test_sin_fuentes_BLOCKED_y_dia_no_terminado(tmp_path):
    (tmp_path / 'vol' / 'm5_registro').mkdir(parents=True); (tmp_path / 'vol' / 'm15_registro').mkdir(parents=True); (tmp_path / 'dl').mkdir(); (tmp_path / 'e1b').mkdir()
    (tmp_path / 'cache.json').write_text('{}')
    lanzar(tmp_path); M = json.load(open(tmp_path / 'e1b' / 'dias' / f'{DIA}.json')); assert M['estado'] == 'BLOCKED' and 'sin fuentes' in M['motivo']
    futuro = '2099-01-01'; lanzar(tmp_path, dias=futuro); assert json.load(open(tmp_path / 'e1b' / 'dias' / f'{futuro}.json'))['motivo'] == 'dia no terminado'


def test_fallback_crudo_si_no_hay_archivo(tmp_path):
    vol, dl, cache = montar_fuentes(tmp_path); (tmp_path / 'e1b').mkdir()
    shutil.move(vol / 'm5_registro' / f'm5_registro_{DIA}.csv.gz', dl / f'maker_ms_{DIA}_123.csv.gz'); os.remove(vol / 'm15_registro' / f'm15_registro_{DIA}.csv.gz')
    lanzar(tmp_path); M = json.load(open(tmp_path / 'e1b' / 'dias' / f'{DIA}.json')); assert M['etapas']['extract']['fuentes_tipo'] == 'crudo' and M['etapas']['sim']['ok']


def test_prereg_cambiado_aborta(tmp_path, monkeypatch):
    # el hash esperado se lee de .sha256: comprobamos que el actual coincide (si no, el cron aborta)
    pre = os.path.join(E1B_CODE, '..', 'PREREG_E1b_CONFIRMACION_S1.md'); esp = open(os.path.join(E1B_CODE, '..', 'PREREG_E1b_CONFIRMACION_S1.sha256')).read().split()[0]
    assert sha(pre) == esp


# ---------------------------------------------------------------- evaluador
def filas(dia, mids, base_pnl_win, s1_fill, cierre0=1000, obj=0.20):
    """mercados con relleno BASE (obj) ; S1_D100: s1_fill[i] (1 = sigue relleno, 0 = retirado) ; resto de variantes = BASE salvo INV/SH=BASE y D250=D100"""
    R = []
    for i, m in enumerate(mids):
        gana = base_pnl_win[i]
        base = dict(dia=dia, act='ETH', mid=m, fin=cierre0 + i // 3 * 300 + int(dia[-2:]) * 100000, yes=1, gana=gana, n_cand=1)
        R.append({**base, 'var': 'BASE', 'fill': 1, 'obj': obj, 'r': 5})
        for v in ('D100', 'D250', 'D0'):
            R.append({**base, 'var': f'S1_x2_w2000|{v}', 'fill': s1_fill[i], 'obj': obj if s1_fill[i] else np.nan, 'r': 5 if s1_fill[i] else -1})
        for v in ['INV'] + EV.SH: R.append({**base, 'var': f'S1_x2_w2000|{v}', 'fill': 1, 'obj': obj, 'r': 5})
    return R


def dataset(ndias, ganadora=True, sesgo=0.0):
    rng = np.random.default_rng(1); R = []; A = []
    for k in range(ndias):
        d = f'2026-10-{23+k:02d}'; n = 60
        win = (rng.random(n) < 0.15).astype(int)
        # S1 retira (fill 0) casi todos los perdedores si ganadora, ninguno si no
        fill = np.where(win == 0, (rng.random(n) > 0.8).astype(int) if ganadora else 1, 1)
        mids = [f'{d}-{i}' for i in range(n)]
        R += filas(d, mids, win, fill); A += [(m, 0.05) for m in mids]
    return pd.DataFrame(R), pd.DataFrame(A, columns=['mid', 'lvl15'])


def test_paired_calculo_a_mano():
    X = pd.DataFrame(filas('2026-10-23', ['a', 'b'], [0, 1], [0, 1]))
    X, B = EV.preparar(X); m, dp, b = EV.paired(X, B, 'S1_x2_w2000|D100')
    # a: perdedor retirado: base pnl = 5*(0-0.2) = -1.0 -> variante 0 -> dp +1.0 ; b: igual -> 0 ; coste base 2.0
    assert abs(m['dpnl'] - 1.0) < 1e-9 and abs(m['dpe'] - 0.5) < 1e-9 and m['quitados'] == 1 and m['sustitutos'] == 0 and abs(m['ret'] - 0.5) < 1e-9


def test_duplicados_se_rechazan():
    X = pd.DataFrame(filas('2026-10-23', ['a', 'a'], [0, 0], [1, 1]))
    with pytest.raises(ValueError): EV.preparar(X)
    X = pd.DataFrame(filas('2026-10-23', ['a'], [0], [1])); X = pd.concat([X, X.iloc[:2]])
    with pytest.raises(ValueError): EV.preparar(X)


def test_gate_confirmada_con_5_dias():
    X, aux = dataset(5, True); r = EV.evaluar(X, aux, nboot=2000)
    assert r['n_dias'] == 5 and r['gate']['G1'] and r['gate']['G2'] and r['gate']['G4'] and r['gate']['G5']
    # INV y desplazamientos = BASE -> dpe 0 -> G3 cumple
    assert r['gate']['G3'] and r['veredicto'] == 'CONFIRMADA'


def test_4_dias_siempre_acumulando():
    X, aux = dataset(4, True); r = EV.evaluar(X, aux, nboot=2000); assert r['veredicto'] == 'ACUMULANDO' and r['n_dias'] == 4


def test_refutada_por_ic_superior_con_5_dias():
    # S1 retira SOLO ganadores -> dPnL < 0 en todos los dias
    rng = np.random.default_rng(2); R = []; A = []
    for k in range(5):
        d = f'2026-10-{23+k:02d}'; n = 60; win = (rng.random(n) < 0.3).astype(int); fill = np.where(win == 1, 0, 1); mids = [f'{d}-{i}' for i in range(n)]
        R += filas(d, mids, win, fill); A += [(m, 0.05) for m in mids]
    r = EV.evaluar(pd.DataFrame(R), pd.DataFrame(A, columns=['mid', 'lvl15']), nboot=2000)
    assert r['D100']['dpnl'] < 0 and r['D100']['ic_dia'][1] <= 0 and r['veredicto'] == 'REFUTADA'


def test_refutada_a_10_dias_por_estimacion_puntual():
    # sin efecto (S1 = BASE) -> dpe = 0 -> a 10 dias REFUTADA ; a 9 dias ACUMULANDO (IC por dia degenerado en 0 no es <= 0 con NaN? dpe=0 -> ic = (0,0) -> sup <= 0 -> REFUTADA ya a 5)
    X, aux = dataset(10, False); r = EV.evaluar(X, aux, nboot=1000)
    assert abs(r['D100']['dpe']) < 1e-12 and r['veredicto'] == 'REFUTADA'


def test_g5_exige_aux_y_r2_falso_positivo():
    X, aux = dataset(5, True); r = EV.evaluar(X, None, nboot=1000); assert r['gate']['G5'] is False and r['veredicto'] != 'CONFIRMADA'
    aux2 = aux.assign(lvl15=0.0)                       # todo R2-verdadero: R2-falso vacio -> G5 falso (no se confirma por ausencia)
    r = EV.evaluar(X, aux2, nboot=1000); assert r['gate']['G5'] is False and r['veredicto'] != 'CONFIRMADA'


def test_umbral_r2_borde_030_es_verdadero():
    X, aux = dataset(5, True); a = aux.assign(lvl15=0.03); r = EV.evaluar(X, a, nboot=500)
    assert r['R2']['R2_falso']['rellenos'] == 0 and r['R2']['R2_verdadero']['rellenos'] > 0


def test_dias_validos_excluye_partial_y_missing(tmp_path):
    E = str(tmp_path) + '/'; os.makedirs(E + 'dias')
    for d, est in (('2026-10-23', 'COMPLETE'), ('2026-10-24', 'PARTIAL'), ('2026-10-25', 'BLOCKED'), ('2026-10-22', 'COMPLETE')):
        json.dump({'estado': est, 'motivo': 'x'}, open(E + f'dias/{d}.json', 'w'))
    open(E + 'dias/2026-10-26.json', 'w').write('{roto')
    for d_ in ('2026-10-23', '2026-10-22', '2026-10-24'): pd.DataFrame({'a': [1]}).to_csv(E + f'e1_{d_}.csv.gz', index=False)
    pd.DataFrame({'a': [1]}).to_csv(E + 'e1x_2026-10-23.csv.gz', index=False); pd.DataFrame({'a': [1]}).to_csv(E + 'e1x_2026-10-22.csv.gz', index=False)
    ok, no = EV.dias_validos(E, '2026-10-23')
    assert ok == ['2026-10-23'] and set(no) == {'2026-10-24', '2026-10-25', '2026-10-26'}       # el 22 queda fuera (pre-forward) y nada se imputa como 0


def test_bootstrap_determinista():
    a = EV.boot([1, 2, -1, 3], [5, 5, 5, 5], ['a', 'b', 'c', 'd'], 500); b = EV.boot([1, 2, -1, 3], [5, 5, 5, 5], ['a', 'b', 'c', 'd'], 500); assert a == b


# ---------------------------------------------------------------- reproduccion de e1_eval sobre 17-22 Oct (datos reales; se salta si no estan)
DATOS = os.path.join(E1B_CODE, '..', 'datos')
@pytest.mark.skipif(not os.path.exists(DATOS + '/e1_2026-10-22.csv.gz'), reason='sin datos E1')
def test_reproduce_e1_eval_S1_x2_w2000():
    # e1_eval.txt: DESC dPnL +55.8 (+0.0317/EUR) dias +21.7 +11.6 +22.6 ; TEST +62.2 (+0.0416) dias +42.0 +2.2 +18.1 ; INV +0.0021/+0.0027 ; D250 +0.0236/+0.0490
    esp = {'DESC': (55.8, 0.0317, [21.7, 11.6, 22.6], 0.0021, 0.0236), 'TEST': (62.2, 0.0416, [42.0, 2.2, 18.1], 0.0027, 0.0490)}
    for per, dias in (('DESC', EV.DESC), ('TEST', EV.TEST)):
        X = pd.concat([pd.read_csv(f'{DATOS}/e1_{d}.csv.gz') for d in dias], ignore_index=True); r = EV.evaluar(X, None, nboot=2000); m = r['D100']
        dp, dpe, pd_, inv, d250 = esp[per]
        assert abs(m['dpnl'] - dp) < 0.06 and abs(m['dpe'] - dpe) < 5e-5 and [round(v, 1) for v in m['por_dia'].values()] == pd_
        assert abs(r['INV']['dpe'] - inv) < 5e-5 and abs(r['D250']['dpe'] - d250) < 5e-5
    # IC90 por cierre publicado DESC (+0.0012,+0.0593) / TEST (+0.0098,+0.0730): tolerancia por Monte Carlo distinto
    X = pd.concat([pd.read_csv(f'{DATOS}/e1_{d}.csv.gz') for d in EV.TEST], ignore_index=True); m = EV.evaluar(X, None, nboot=4000)['D100']
    assert abs(m['ic_cierre'][0] - 0.0098) < 0.004 and abs(m['ic_cierre'][1] - 0.0730) < 0.004


# ---------------------------------------------------------------- A4: tev (extraer_e1b) y X50
def test_extraer_e1b_identico_a_extraer_y_guarda_tev(tmp_path):
    vol, dl, cache = montar_fuentes(tmp_path, tev_lag=600)
    import importlib; SAL = os.path.abspath(os.path.join(E1B_CODE, '..', '..', 'salida', 'scripts')); sys.path.insert(0, SAL)
    import extraer as X0, extraer_e1b as X1
    out = {}
    for nm, mod in (('o', X0), ('n', X1)):
        mod.VOL = str(vol) + '/'; mod.DL = str(dl) + '/'; o = tmp_path / nm; o.mkdir(); mod.OUT = str(o); mod.day(DIA); out[nm] = np.load(o / f'ms_{DIA}.npz')
    for k in out['o'].files:
        assert np.array_equal(out['o'][k], out['n'][k]), k
    assert set(out['n'].files) - set(out['o'].files) == {'qd', 'td'}
    assert list(out['n']['td']) == [600] and set(out['n']['qd']) == {0}


def test_X50_con_tev_anterior_a_la_recepcion_no_evita(tmp_path):
    montar_fuentes(tmp_path, tev_lag=600); (tmp_path / 'e1b').mkdir(); lanzar(tmp_path)
    E = tmp_path / 'e1b'; X = pd.read_csv(E / f'e1_{DIA}.csv.gz'); Y = pd.read_csv(E / f'e1x_{DIA}.csv.gz')
    assert X[X['var'] == 'S1_x2_w2000|D250'].fill.iloc[0] == 0          # por recepcion la senal (500 ms antes) cubre el print
    assert Y[Y['var'] == 'S1_x2_w2000|X50'].fill.iloc[0] == 1           # por hora de exchange el print fue 100 ms ANTES que la senal -> no se evita


# ---------------------------------------------------------------- V1 (ADDENDUM)
def filas_add(dia, mids, win, modo, obj=0.20):
    """modo: 'sust' = S1 mantiene todos los rellenos pero mas baratos (0,18) ; 'volumen' = S1 elimina ~30 % al azar (sin sustitucion) ; 'ganadores' = elimina solo ganadores"""
    R = []; rng = np.random.default_rng(abs(hash(dia)) % 1000)
    for i, m in enumerate(mids):
        gana = int(win[i]); base = dict(dia=dia, act='ETH', mid=m, fin=1000 + i // 3 * 300 + int(dia[-2:]) * 100000, yes=1, gana=gana, n_cand=1)
        R.append({**base, 'var': 'BASE', 'fill': 1, 'obj': obj, 'r': 5})
        if modo == 'sust': vf, vo, vr = 1, 0.18, 6
        elif modo == 'volumen': vf = int(i % 3 != 0); vo, vr = (obj, 5) if vf else (np.nan, -1)      # quita 1 de cada 3 sin mirar el resultado
        else: vf = int(not gana); vo, vr = (obj, 5) if vf else (np.nan, -1)
        for v in ('D100', 'D250', 'D0', 'X50'): R.append({**base, 'var': f'S1_x2_w2000|{v}', 'fill': vf, 'obj': vo, 'r': vr})
        for v in ['INV', 'INV250'] + EV.SH + [f'SH{s:+d}_250' for s in (-240, -180, -120, -60, 60, 120, 180, 240)]: R.append({**base, 'var': f'S1_x2_w2000|{v}', 'fill': 1, 'obj': obj, 'r': 5})
        R.append({**base, 'var': 'C1|D250', 'fill': 1, 'obj': obj, 'r': 5}); R.append({**base, 'var': 'C2|FILL', 'fill': 1, 'obj': obj, 'r': 5})
    return R


def dataset_add(ndias, modo):
    rng = np.random.default_rng(3); R = []; A = []
    for k in range(ndias):
        n = 120; d = f'2026-10-{23+k:02d}'; mids = [f'{d}-{i}' for i in range(n)]
        win = np.array([int(i % 20 < 3) for i in range(n)]) if modo == 'volumen' else (rng.random(n) < 0.15).astype(int)      # volumen: acierto 15 % determinista
        R += filas_add(d, mids, win, modo); A += [(m, 0.05) for m in mids]
    X = pd.DataFrame(R); return X, pd.DataFrame(A, columns=['mid', 'lvl15'])


def split(X):
    ext = X['var'].isin(['S1_x2_w2000|X50', 'S1_x2_w2000|INV250', 'C1|D250', 'C2|FILL']) | X['var'].str.endswith('_250') & ~X['var'].str.endswith('|D250')
    return X[~ext], X[ext]


def test_V1_confirmada_si_sustitucion_pura():
    X, aux = dataset_add(5, 'sust'); X0, Xe = split(X); r = EV.evaluar_add(X0, Xe, aux, None, nboot=1000, nnull=300)
    assert r['A2']['sust_pe'] > 0 and r['A2']['elim_n'] == 0 and r['A2']['ok'] and r['A1']['ok'] and r['A5']['ok'] and r['A4']['X50_ok'] and r['gate']['G5']
    assert r['veredicto_V1'] == 'CONFIRMADA_ADD', r['gate']


def test_V1_no_confirma_si_solo_volumen_y_etiqueta():
    X, aux = dataset_add(6, 'volumen'); X0, Xe = split(X); r = EV.evaluar_add(X0, Xe, aux, None, nboot=1000, nnull=300); v0 = EV.evaluar(X0, aux, nboot=1000)
    assert v0['veredicto'] == 'CONFIRMADA' and r['A2']['sust_pe'] == 0 and not r['A2']['ok'] and r['veredicto_V1'] != 'CONFIRMADA_ADD'
    assert 'SOLO POR VOLUMEN' in EV.etiqueta_final(v0['veredicto'], r['veredicto_V1'])


def test_V1_refutada_si_elimina_solo_ganadores():
    X, aux = dataset_add(5, 'ganadores')
    X = X.copy(); m = X['var'].str.startswith('S1_x2_w2000|D') | (X['var'] == 'S1_x2_w2000|X50')
    X.loc[m, 'fill'] = np.where(X.loc[m, 'gana'] == 1, 0, 1); X.loc[m, 'obj'] = np.where(X.loc[m, 'fill'] == 1, 0.20, np.nan); X.loc[m, 'r'] = np.where(X.loc[m, 'fill'] == 1, 5, -1)
    X0, Xe = split(X); r = EV.evaluar_add(X0, Xe, aux, None, nboot=1000, nnull=300)
    assert r['veredicto_V1'] != 'CONFIRMADA_ADD'


def test_V1_A5_control_domina_si_gana_mas_con_mas_volumen():
    X, aux = dataset_add(5, 'sust'); X = X.copy()
    m = X['var'] == 'C2|FILL'; X.loc[m, 'obj'] = 0.18          # control igual de bueno que S1 y con la misma retencion -> domina (>=)
    X0, Xe = split(X); r = EV.evaluar_add(X0, Xe, aux, None, nboot=500, nnull=200); assert not r['A5']['ok'] and r['veredicto_V1'] != 'CONFIRMADA_ADD'


def test_V1_X50_missing_no_es_cero():
    X, aux = dataset_add(5, 'sust'); X0, Xe = split(X); Xe = Xe[Xe['var'] != 'S1_x2_w2000|X50']
    r = EV.evaluar_add(X0, Xe, aux, None, nboot=500, nnull=200); assert r['A4']['X50'] is None and not r['A4']['X50_ok'] and r['veredicto_V1'] == 'ACUMULANDO'


def test_V1_4_dias_acumulando_y_A3_usa_delta_E1_si_B_real_pequeno():
    X, aux = dataset_add(4, 'sust'); X0, Xe = split(X); r = EV.evaluar_add(X0, Xe, aux, pd.DataFrame({'dia': ['2026-10-23'], 'gana': [1], 'coste': [1.0]}), nboot=500, nnull=200)
    assert r['veredicto_V1'] == 'ACUMULANDO' and r['A3']['fuente_delta'].startswith('delta E1') and abs(r['A3']['coste_dia_b'] - 42.0) < 1e-9


def test_addendum_sha():
    p = os.path.join(E1B_CODE, '..', 'ADDENDUM_E1b'); assert sha(p + '.md') == open(p + '.sha256').read().split()[0]
