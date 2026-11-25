#!/usr/bin/env python3
"""sec7_run.py MODO [DIA] -- runner idempotente de R1v2 sec.7 (a)-(d). MODO: sim DIA | oct DIA | global | final.
 sim DIA : replay de B (b_policy_sim.run_day) con el canal bloqueo ACTIVO (EngineBloqueo(E, activo=True)); anota canal/F5_t/tercil; emite CENSO por canal x tercil (conteos y P(relleno)).
           EV/estres NONE solo si SEC7_EMITIR_EV=1 (por defecto NO: el contrato sec.11 exige antes prereg+Puerta 0+E-SO-3...).
 oct DIA : cordura del canal bloqueo con las ordenes REALES (ordenes_b.csv) + error de tiempo de los TP (d) por clase de suelo.
 global  : (c) 13 sin L2 con/sin 23-Oct + verificacion de unidades tk_sz/tk_rem (sin motor, ligero).
 final   : manifest del job, cobertura por dia y estado COMPLETE/PARTIAL/FAILED/BLOCKED.
Contrato de job largo: manifest por (modo, dia) con hashes, escritura atomica (tmp + os.replace), validacion del output antes de saltar (sha), claves unicas (dia, mid, n_ord) comprobadas, cobertura esperada/recibida/procesada/saltada/duplicados.
Memoria: ejecutar via run_sec7.sh (ulimit -v 3 GB). 0 ordenes, nada en data/."""
import sys, os, json, time, hashlib, traceback
HV = os.path.dirname(os.path.abspath(__file__)) + '/'
BR = os.path.dirname(HV.rstrip('/')) + '/'; BSIM = os.path.dirname(BR.rstrip('/')) + '/'
sys.path.insert(0, HV); sys.path.insert(0, BSIM)
OUT = os.environ.get('SEC7_OUT', HV + 'out_sec7/'); os.makedirs(OUT, exist_ok=True)
DIAS_SIM = ['2026-11-03', '2026-11-04', '2026-11-05', '2026-11-06', '2026-11-07', '2026-11-08', '2026-11-09']
DIAS_OCT = ['2026-10-20', '2026-10-21', '2026-10-22', '2026-10-23']
ORD_B = '/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv'
PB = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/precursores_barrido/out/'
EMITIR_EV = os.environ.get('SEC7_EMITIR_EV', '0') == '1'
def ts(): return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
def log(*a): print(ts(), *a, flush=True)
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()
def atomic_json(p, o):
    json.dump(o, open(p + '.tmp', 'w'), indent=1, default=str); os.replace(p + '.tmp', p)
def atomic_pkl(p, df):
    df.to_pickle(p + '.tmp'); os.replace(p + '.tmp', p)
def code_hashes():
    fs = ['sec7_core.py', 'sec7_calculos.py', 'sec7_run.py']; H = {f: sha(HV + f) for f in fs}
    for f in ('b_policy_sim.py', 'eng_v5.py', 'ejecutor_puro.py'): H['motor/' + f] = sha(BSIM + f)
    return H
def mpath(modo, d): return OUT + f'manifest_{modo}_{d}.json'
def ya_completo(modo, d, outs):
    """checkpoint valido = manifest COMPLETE y cada output existe con el sha registrado."""
    p = mpath(modo, d)
    if not os.path.exists(p): return False
    try:
        m = json.load(open(p))
        return m.get('status') == 'COMPLETE' and all(os.path.exists(OUT + f) and sha(OUT + f) == h for f, h in m.get('outputs', {}).items()) and set(m.get('outputs', {})) == set(outs)
    except Exception: return False
def inputs_dia(d):
    return {'tape': PB + f'tape_{d}.pkl', 'bad': PB + f'bad_{d}.json'}
def stat(p):
    s = os.stat(p); return dict(size=s.st_size, mtime=int(s.st_mtime))

def job(modo, d, outs, fn, needs):
    if ya_completo(modo, d, outs): log('ya COMPLETE', modo, d); return 'COMPLETE'
    falta = [k for k, p in needs.items() if not os.path.exists(p)]
    man = dict(job=f'sec7 {modo} {d}', status='RUNNING', code=code_hashes(), params=dict(emitir_ev=EMITIR_EV), inputs={k: stat(p) for k, p in needs.items() if os.path.exists(p)}, t_ini=ts())
    if falta:
        man.update(status='BLOCKED', motivo=f'faltan inputs {falta}', t_fin=ts()); atomic_json(mpath(modo, d), man); log('BLOCKED', modo, d, falta); return 'BLOCKED'
    atomic_json(mpath(modo, d), man)
    try:
        res, cob = fn(d)
        man.update(status='COMPLETE', outputs={f: sha(OUT + f) for f in outs}, cobertura=cob, resumen_parcial=res, t_fin=ts())
        atomic_json(mpath(modo, d), man); log('COMPLETE', modo, d, json.dumps(res, default=str)[:600]); return 'COMPLETE'
    except Exception as ex:
        man.update(status='FAILED', err=repr(ex), tb=traceback.format_exc()[-1500:], t_fin=ts()); atomic_json(mpath(modo, d), man); log('FAILED', modo, d, repr(ex)); return 'FAILED'

# ------------------------------------------------------------------ sim
def run_sim(d):
    import pandas as pd, b_policy_sim as BS, eng_v5 as EV, sec7_core as C, sec7_calculos as K
    E, info = EV.build(d); W = C.EngineBloqueo(E, activo=True); P = BS.params()
    R, cov = BS.run_day(d, P, E=W); R['dia'] = d
    dup = int(R.duplicated(['dia', 'mid', 'n_ord']).sum()) if len(R) else 0
    R = C.anota_ordenes(R, W, W._serie)
    if 'sin_registro' in set(R.canal): log('AVISO: rellenos sin canal registrado', int((R.canal == 'sin_registro').sum()))
    atomic_pkl(OUT + f'sim_ordenes_{d}.pkl', R)
    cen = C.censo(R); res = dict(censo=cen, contadores_motor=dict(W.cont), etiqueta='CENSO (conteos); sin EV')
    if EMITIR_EV: res['estres_none'] = K.rejilla_estres(R)
    cob = dict(esperado_mercados=cov.get('mercados'), ordenes=cov.get('ordenes'), ordenes_rellenas=cov.get('ordenes_rellenas'), saltados=cov.get('skip'), duplicados_clave=dup,
               invalidos=int((R.tercil == 'inval').sum()) if len(R) else 0, motor=cov.get('info_motor'))
    atomic_json(OUT + f'sim_censo_{d}.json', res); return res, cob

# ------------------------------------------------------------------ oct
def run_oct(d):
    import numpy as np, pandas as pd, eng_v5 as EV, sec7_core as C, sec7_calculos as K
    E, info = EV.build(d); W = C.EngineBloqueo(E, activo=True); D = E.D
    O = pd.read_csv(ORD_B, usecols=['oid', 'tok', 'coin', 'precio', 'size', 't_call0', 't_fin', 't_fuera', 'dia'], dtype={'tok': str}); O = O[O.dia == d]
    T = pd.read_pickle(BR + 'tomador_202.pkl'); T = T[T.dia == d].copy()
    real = dict(zip(T.oid, T.real_tm3.astype(float)))
    vent = []; sin_tok = 0
    for r in O.itertuples():
        k = D.tokidx.get(str(r.tok))
        if k is None: sin_tok += 1; continue
        t_end = (r.t_fuera if np.isfinite(r.t_fuera) else r.t_fin)
        vent.append(dict(dia=d, coin=r.coin, k=k, L=float(r.precio), t_arr=int(r.t_call0 * 1000) + 35, t_end=int(t_end * 1000), rem=float(r.size), real_tm3=real.get(r.oid)))
    filas, res = C.cordura(vent, W.fuente)
    # (d) clase de suelo causal por orden (ventanas 5+5 min de bins de 10 s completos antes de t_dec, filas del coin) y error de tiempo de los TP
    cache = {}; cl = []
    for r in T.itertuples():
        c = str(r.coin).lower()
        if c not in cache: cache[c] = C.suelo_por_coin(D, c)
        cl.append(C.clase_suelo_en(cache[c][0], cache[c][1], int(r.t_dec)))
    T['clase_suelo'] = cl; err = K.error_tiempo_tp(T)
    atomic_pkl(OUT + f'oct_tp_{d}.pkl', T[['oid', 'dia', 'coin', 'sim', 'v3d_BASE_f_tf', 'real_tm3', 'clase_suelo']])
    atomic_json(OUT + f'oct_cordura_{d}.json', dict(por_dia_coin=filas, resumen=res, error_tiempo_tp=err))
    cob = dict(ordenes_esperadas=int(len(O)), ventanas_procesadas=int(res.get('n_ventanas', 0)), sin_token=sin_tok, sin_serie=res.get('sin_serie'), tp_filas=int(len(T)))
    return dict(cordura=res, error_tiempo_tp=err), cob

# ------------------------------------------------------------------ global
def run_global(d):
    import pandas as pd, sec7_calculos as K
    HV2 = BR + 'solo_observable_19nov/'
    F = pd.read_pickle(HV2 + 'so1_filas.pkl'); B = pd.read_pickle(HV2 + 'so1b_filas.pkl')[['oid', 'hit']]
    F = F.merge(B, on='oid', how='left')           # hit NaN (sin L2) NO se imputa: grupos_clase1 manda SIN_L2 por mk
    T = pd.read_pickle(BR + 'tomador_202.pkl')
    res = dict(sin_l2=K.trata_sin_l2(F), unidades_tk=K.verifica_unidades_tk(T))
    atomic_json(OUT + 'global_sin_l2_unidades.json', res)
    return res, dict(filas_so1=int(len(F)), filas_tomador=int(len(T)))

def final():
    est = {}
    for modo, dias in (('sim', DIAS_SIM), ('oct', DIAS_OCT)):
        for d in dias:
            p = mpath(modo, d); est[f'{modo}_{d}'] = (json.load(open(p)).get('status') if os.path.exists(p) else 'MISSING')
    p = mpath('global', 'x'); est['global'] = json.load(open(p)).get('status') if os.path.exists(p) else 'MISSING'
    vals = set(est.values()); st = 'COMPLETE' if vals == {'COMPLETE'} else ('FAILED' if 'FAILED' in vals else ('BLOCKED' if 'BLOCKED' in vals and 'COMPLETE' not in vals else 'PARTIAL'))
    rep = dict(job='sec7 R1v2', status=st, dias_esperados=dict(sim=DIAS_SIM, oct=DIAS_OCT), estado_por_dia=est, code=code_hashes(), t_fin=ts(), emitir_ev=EMITIR_EV,
               repro='cd %s && bash run_sec7.sh' % HV, etiqueta='conteos/cordura/error de tiempo; NO es EV de B ni de R1v2')
    atomic_json(OUT + 'run_manifest.json', rep); log('FINAL', st, est); return st

if __name__ == '__main__':
    modo = sys.argv[1]
    if modo == 'sim': d = sys.argv[2]; r = job('sim', d, [f'sim_ordenes_{d}.pkl', f'sim_censo_{d}.json'], run_sim, inputs_dia(d))
    elif modo == 'oct': d = sys.argv[2]; r = job('oct', d, [f'oct_tp_{d}.pkl', f'oct_cordura_{d}.json'], run_oct, inputs_dia(d))
    elif modo == 'global': r = job('global', 'x', ['global_sin_l2_unidades.json'], run_global, {'so1': BR + 'solo_observable_19nov/so1_filas.pkl', 'tomador': BR + 'tomador_202.pkl'})
    elif modo == 'final': r = final()
    else: raise SystemExit(__doc__)
    sys.exit(0 if r in ('COMPLETE', 'BLOCKED') else 1)
