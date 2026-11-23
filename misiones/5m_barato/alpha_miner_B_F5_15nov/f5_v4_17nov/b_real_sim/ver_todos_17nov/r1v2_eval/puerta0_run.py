#!/usr/bin/env python3
"""puerta0_run.py MODO [DIA] -- runner idempotente de la FASE A de R1v2 (Puerta 0). MODO: dia DIA | final.
 dia DIA : replay de la politica REAL de B (b_policy_sim.run_day sobre eng_v5.build) UNA vez por dia y DOS variantes de canal bloqueo (0 = motor vigente intacto = PRIMARIA, 1 = canal bloqueo activo = sensibilidad);
           anota F5_t/tercil (sec7_core), F5 con reloj exchange y canal. Salida: p0_ordenes_DIA.pkl + p0_cov_DIA.json. El resumen parcial por dia son SOLO CONTEOS (sin EV).
 final   : lee los dias COMPLETE, aplica unidad 1.er relleno, estratos de suelo (tabla firmada), rejilla {bloqueo x rebate x estres NONE x estrato x conjunto de dias} y escribe puerta0_resultado.json + run_manifest.json.
Contrato de job: manifest por dia (hashes de codigo, inputs), checkpoint atomico validado por sha antes de saltar, claves unicas (dia, mid, n_ord, bloq), cobertura esperada/procesada/saltada/duplicados.
Reutiliza r1v2_sec7/sec7_run.job (no se copia). 0 ordenes reales, 0 red, nada en data/."""
import sys, os, json, time, hashlib
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; V = os.path.dirname(HV.rstrip('/')) + '/'; BSIM = os.path.dirname(V.rstrip('/')) + '/'
OUT = os.environ.get('P0_OUT', HV + 'out_p0/'); os.makedirs(OUT, exist_ok=True)
os.environ['SEC7_OUT'] = OUT
sys.path.insert(0, HV); sys.path.insert(0, V + 'r1v2_sec7/'); sys.path.insert(0, BSIM)
import sec7_run as RU
RU.OUT = OUT
DIAS = ['2026-11-03', '2026-11-04', '2026-11-05', '2026-11-06', '2026-11-07', '2026-11-08', '2026-11-09', '2026-11-10', '2026-11-11', '2026-11-12', '2026-11-13', '2026-11-14']
# ADENDA_08 (23-Nov): conjuntos A=05-09 (ADENDA_06), B=10-14 (replica NO CIEGA), C=A+B (decision). Los dias nuevos (>= NUEVOS_DESDE) exigen sha de tape/bad = referencia y cobertura libro5_tx (fail-closed).
DIAS_A = [d for d in DIAS if '2026-11-05' <= d <= '2026-11-09']; DIAS_B = [d for d in DIAS if '2026-11-10' <= d <= '2026-11-14']; DIAS_C = DIAS_A + DIAS_B
NUEVOS_DESDE = '2026-11-10'; COV_TX_MIN = 0.90; ETIQ_NO_CIEGO = 'NO CIEGO (PREREG \u00a76)'
TXD = os.environ.get('P0_TXD', '/mnt/HC_Volume_106538179/libro5_tx/'); TAPES_REF = os.environ.get('P0_TAPES_REF', HV + 'TAPES_SHA256_23nov.txt')
TABLA = V + 'cierre_limites_19nov/tabla_suelo_ventanas_19nov.csv'
PASSTV4 = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/passT_v4.py'; PASSTV4_SHA = '85256bcc7872afdfdc7d18f9bf4cd3e27e46c0d4176aceb263d6821045bbf535'
SHA_PREREG = {'PREREG_R1v2_19nov.md': '48fe638e1f561ec3da82d8571b5ef97cc435ec523e994ace0aad2d1fc97b33e7', 'CONTRATO_R1v2_19nov_v2.md': '6bda3605c0bf480deb5a928e1734640d18ffe1f9a0f6dccd99ab9f2f668fca81'}
ts, log, sha, atomic_json, atomic_pkl = RU.ts, RU.log, RU.sha, RU.atomic_json, RU.atomic_pkl

def lee_tapes_ref(path=None):
    """{ruta: sha256} de TAPES_SHA256_23nov.txt (formato sha256sum). Vacio si no existe (los dias nuevos entonces quedan INCOMPLETE)."""
    path = path or TAPES_REF
    if not os.path.exists(path): return {}
    return {l.split(None, 1)[1].strip(): l.split()[0] for l in open(path) if l.strip() and not l.startswith('#') and len(l.split()) >= 2}
def stat_sha(p):
    """inputs_dia con sha256 ademas de size/mtime (ADENDA_08 7); sha_ref_ok = coincide con TAPES_SHA256_23nov.txt (None si no esta en la referencia)."""
    s = os.stat(p); h = sha(p); ref = lee_tapes_ref().get(p)
    return dict(size=s.st_size, mtime=int(s.st_mtime), sha256=h, sha_ref_ok=(None if ref is None else ref == h))
RU.stat = stat_sha                               # RU.job usa el global stat() al escribir inputs del manifest

def dias_vec(d):
    import pandas as pd
    return [(pd.Timestamp(d) + pd.Timedelta(days=i)).strftime('%Y-%m-%d') for i in (-1, 0, 1)]
def tx_del_dia(x, txd=None):
    import glob, pandas as pd
    s = set()
    for f in sorted(glob.glob((txd or TXD) + f'libro5_tx_{x}_*.csv.gz')): s |= set(pd.read_csv(f, header=None, usecols=[2], names=['tx'], dtype=str).tx)
    return s
def cobertura_tx(d, txd=None, pb=None):
    """ADENDA_08 7: cobertura libro5_tx con_tx/units de d-1, d, d+1 (eng_v5 lee TXD de esos 3 dias). units = tx distintos del tape del dia x; con_tx = los que estan en libro5_tx de x-1..x+1.
    ok solo si los 3 dias tienen tape y cov >= COV_TX_MIN; sin tape o sin units = no ok (nunca 'bueno por defecto')."""
    import gc, pandas as pd
    pb = pb or RU.PB; cache = {}; out = {}
    def T(y):
        if y not in cache: cache[y] = tx_del_dia(y, txd)
        return cache[y]
    for x in dias_vec(d):
        p = pb + f'tape_{x}.pkl'
        if not os.path.exists(p): out[x] = dict(units=0, con_tx=0, cov=None, motivo='sin tape'); continue
        t = pd.read_pickle(p); u = set(t['tx'].dropna().astype(str)); del t
        tev = set().union(*[T(y) for y in dias_vec(x)]); con = len(u & tev); out[x] = dict(units=len(u), con_tx=con, cov=(con / len(u)) if u else None)
    gc.collect()
    ok = all(v['cov'] is not None and v['cov'] >= COV_TX_MIN for v in out.values())
    return dict(ok=ok, min_cov=COV_TX_MIN, dias=out)
def incompleto(d, cov, refs):
    """None si el dia puede ejecutarse; si no, lista de motivos. Solo los dias nuevos (>= NUEVOS_DESDE) lo exigen; los anteriores solo registran."""
    if d < NUEVOS_DESDE: return None
    m = []
    if not cov['ok']: m.append('cobertura libro5_tx con_tx/units < %.2f o sin tape en d-1,d,d+1: %s' % (COV_TX_MIN, {k: (None if v['cov'] is None else round(v['cov'], 3)) for k, v in cov['dias'].items()}))
    for k, p in RU.inputs_dia(d).items():
        if not os.path.exists(p): continue
        r = lee_tapes_ref().get(p)
        if r is None: m.append(f'{k}: sin sha de referencia en TAPES_SHA256')
        elif r != sha(p): m.append(f'{k}: sha256 != referencia')
    return m or None

def code_hashes():
    H = {f: sha(HV + f) for f in ('puerta0_core.py', 'puerta0_run.py')}
    for f in ('sec7_core.py', 'sec7_calculos.py', 'sec7_run.py'): H['sec7/' + f] = sha(V + 'r1v2_sec7/' + f)
    for f in ('b_policy_sim.py', 'eng_v5.py', 'ejecutor_puro.py'): H['motor/' + f] = sha(BSIM + f)
    H['passT_v4.py(ref)'] = sha(PASSTV4)
    return H
RU.code_hashes = code_hashes                     # el manifest por dia lleva ESTOS hashes
_ya_orig = RU.ya_completo
def ya_completo(modo, d, outs):
    """checkpoint valido = el de sec7 (COMPLETE + sha de outputs) Y manifest['code'] == code_hashes() actual (code-review 3 #7): si el codigo cambio, el dia es invalido y se re-ejecuta."""
    if not _ya_orig(modo, d, outs): return False
    try: return json.load(open(RU.mpath(modo, d))).get('code') == code_hashes()
    except Exception: return False
RU.ya_completo = ya_completo
def sha_prereg():
    """fail-closed (#10): PREREG, ADENDA_01..06, 06b, 07, 08 y CONTRATO v2 cuadran con sus .sha256. Devuelve {fichero: sha}; ValueError si falta o difiere."""
    D = os.environ.get('P0_PREREG_DIR', V); out = {}
    for f in ['PREREG_R1v2_19nov'] + [f'PREREG_R1v2_19nov_ADENDA_0{i}' for i in range(1, 7)] + ['PREREG_R1v2_19nov_ADENDA_06b', 'PREREG_R1v2_19nov_ADENDA_07', 'PREREG_R1v2_19nov_ADENDA_08'] + ['CONTRATO_R1v2_19nov_v2']:
        md = D + f + '.md'; shf = D + f + '.sha256'
        if not (os.path.exists(md) and os.path.exists(shf)): raise ValueError('falta ' + f)
        esp = open(shf).read().split()[0]; real = sha(md)
        if esp != real: raise ValueError(f'{f}: sha {real} != {esp}')
        out[f + '.md'] = real
    return out

def run_dia(d):
    import numpy as np, pandas as pd, b_policy_sim as BS, eng_v5 as EV, sec7_core as C, puerta0_core as P0
    E, info = EV.build(d); P = BS.params(); filas = []; cov = dict(esperado_mercados=None, variantes={}, motor=info)
    for bloq in (0, 1):
        W = C.EngineBloqueo(E, activo=bool(bloq)); R, c = BS.run_day(d, P, E=W); R['dia'] = d
        dup = int(R.duplicated(['dia', 'mid', 'n_ord']).sum()) if len(R) else 0
        R = C.anota_ordenes(R, W, W._serie); R = P0.anota_ex(R, W._serie, C.tercil); R = P0.t_ex_fills(R, W.fills)
        if not bloq: R['canal'] = R.canal.where(R.q <= 0, 'visible(bloqueo apagado)')
        R['bloq'] = bloq; filas.append(R)
        cov['esperado_mercados'] = c.get('mercados')
        cov['variantes'][f'bloq{bloq}'] = dict(ordenes=int(len(R)), rellenos=int((R.q > 0).sum()), saltados=c.get('skip'), duplicados_clave=dup, inval=int((R.tercil == 'inval').sum()),
                                              por_tercil={t: int((R.tercil == t).sum()) for t in ('bajo', 'medio', 'alto', 'inval')}, contadores_motor=dict(W.cont))
    R = pd.concat(filas, ignore_index=True)
    assert not R.duplicated(['dia', 'mid', 'n_ord', 'bloq']).any(), 'clave unica violada'
    atomic_pkl(OUT + f'p0_ordenes_{d}.pkl', R); atomic_json(OUT + f'p0_cov_{d}.json', cov)
    return dict(etiqueta='CONTEOS por dia; sin EV', **{k: v['por_tercil'] for k, v in cov['variantes'].items()}), cov

def final():
    import pandas as pd, numpy as np, puerta0_core as P0
    est = {}; Rs = []
    for d in DIAS:
        p = RU.mpath('dia', d); st = json.load(open(p)).get('status') if os.path.exists(p) else 'MISSING'; est[d] = st
        if st == 'COMPLETE' and RU.ya_completo('dia', d, [f'p0_ordenes_{d}.pkl', f'p0_cov_{d}.json']): Rs.append(pd.read_pickle(OUT + f'p0_ordenes_{d}.pkl'))
        elif st == 'COMPLETE': est[d] = 'FAILED(checkpoint invalido o codigo distinto)'
    vals = set(est.values()); st_g = 'COMPLETE' if vals == {'COMPLETE'} else ('BLOCKED' if vals <= {'BLOCKED', 'MISSING'} and 'COMPLETE' not in vals else ('FAILED' if any(v.startswith('FAILED') for v in vals) else 'PARTIAL'))
    try: prereg = sha_prereg()
    except ValueError as ex: prereg = dict(ERROR=str(ex)); st_g = 'BLOCKED'
    rep = dict(job='puerta0 R1v2 FASE A', measurement_id='R1V2-F5-B-19NOV-v2-P0', status=st_g, dias_esperados=DIAS, estado_por_dia=est, code=code_hashes(), prereg=prereg, tabla_suelo_sha=P0.TABLA_SHA,
               params=dict(C0=3.526360511779785, C1=4.717426776885986, rebates=P0.REBATES, estres=P0.ESTRES, K_boot=P0.K_BOOT, seed=P0.SEED, dias_quemados_hasta=P0.DIAS_QUEMADOS_MAX, umbral_dias_lo=P0.UMBRAL_DIAS_LO), t_fin=ts(),
               repro='cd %s && bash run_puerta0.sh' % HV, etiqueta=P0.ETIQUETA, nota_ev='EV solo en puerta0_resultado.json; el veredicto OFICIAL es res[veredicto_oficial] (combinado bloq0+bloq1, ADENDA_06); NO es EV de R1v2 ni de B real.')
    if 'ERROR' in prereg: atomic_json(OUT + 'run_manifest.json', rep); log('BLOQUEADO prereg', prereg); return 'BLOCKED'
    if not Rs: rep['cobertura'] = 'sin dias COMPLETE'; atomic_json(OUT + 'run_manifest.json', rep); log('FINAL', st_g, est); return 'BLOCKED' if st_g == 'BLOCKED' else 'PARTIAL'
    R0 = pd.concat(Rs, ignore_index=True); tab = P0.lee_tabla_suelo(TABLA); cel = P0.celdas_validas(tab); dv = P0.dias_lo_validos(cel)
    dias_ok = sorted(R0.dia.unique()); faltan = lambda L: [d for d in L if est.get(d) != 'COMPLETE']; faltan_todos = faltan(DIAS)
    # ADENDA_08 3: A (05-09, ADENDA_06), B (10-14, replica NO CIEGA), C = A+B (DECISION, NO CIEGO), POSTHOC (03-14). Todo conjunto que incluye 10-14 lleva la etiqueta NO CIEGO.
    conj = {'A_confirmatorio_05_09': ([d for d in dias_ok if d in DIAS_A], faltan(DIAS_A)), 'B_replica_10_14_NO_CIEGO': ([d for d in dias_ok if d in DIAS_B], faltan(DIAS_B)),
            'C_decision_05_14_NO_CIEGO': ([d for d in dias_ok if d in DIAS_C], faltan(DIAS_C)), 'POSTHOC_todos_los_dias': (dias_ok, faltan_todos)}
    res = dict(rejilla={}, combinado={}, cobertura={}, validez={}, suelo=dict(dias_lo_validos=dv, conteo_primario='dias con >=1 celda (dia,moneda) valida (ADENDA_06 2); sensibilidad todas_las_monedas', celdas=cel[cel.dia.isin(dias_ok) & cel.coin.isin(P0.BCOINS)].to_dict('records')))
    Rb = {}
    for bloq in (0, 1):
        R = P0.unidad_primer_relleno(R0[R0.bloq == bloq]); extra = int(R.attrs.get('extra_rellenos', 0)); R = P0.anota_suelo(R, tab, cel); Rb[bloq] = R
        res['cobertura'][f'bloq{bloq}'] = dict(ordenes=int(len(R)), rellenos=int((R.q > 0).sum()), extra_rellenos_anulados=extra, por_dia={d: int((R.dia == d).sum()) for d in dias_ok},
                                              estrato_sin_tabla=int((R.estrato == 'sin_tabla').sum()), canales=R[R.q > 0].canal.value_counts().to_dict())
    # test de fuga NaN (ADENDA_06 3): decisorio SOLO con dias confirmatorios; 03-04 aparte POST HOC. Si bloq0 o bloq1 fallan -> BLOCKED_FUGA en todas las celdas
    def fuga_de(dias):
        f = {b: P0.test_fuga_nan(Rb[b][Rb[b].dia.isin(dias)]) for b in (0, 1)}
        est_ = 'FUGA_SOSPECHOSA' if any(f[b]['estado'] == 'FUGA_SOSPECHOSA' for b in (0, 1)) else ('INSUFFICIENT' if all(f[b]['estado'] == 'INSUFFICIENT' for b in (0, 1)) else 'OK'); return est_, f
    conf_ok = conj['C_decision_05_14_NO_CIEGO'][0]
    fuga_estado, fg = fuga_de(conf_ok); fg_ph = {b: P0.test_fuga_nan(Rb[b][~Rb[b].dia.isin(conf_ok)]) for b in (0, 1)}
    fuga_conj = {n: fuga_de(dd)[0] for n, (dd, _) in conj.items() if n != 'POSTHOC_todos_los_dias'}          # fuga de A y de B por separado; C usa la de A+B (si falla algun dia de A o B => BLOCKED_FUGA)
    res['validez'] = dict(pct_invalido=P0.pct_invalido(Rb[0]), cambio_tercil_descriptivo=P0.cambio_tercil(Rb[0]), fuga_nan=dict(decisorio_dias=conf_ok, estado=fuga_estado, bloq0=fg[0], bloq1=fg[1], por_conjunto=fuga_conj), fuga_nan_posthoc_03_04={'bloq0': fg_ph[0], 'bloq1': fg_ph[1]})
    for nombre, (dd, falt) in conj.items():
        if not dd: continue
        fuga_n = fuga_conj.get(nombre, fuga_estado)                                  # POSTHOC usa la fuga decisoria (A+B), como antes
        for reb in P0.REBATES:
            for es in P0.ESTRES:
                for estr in (None, 'lo', 'lo_valido', 'todas_las_monedas', 'hi', 'indet'):
                    cells = {}
                    for bloq in (0, 1):
                        cells[bloq] = P0.evalua(Rb[bloq], dd, estr, reb, es, dias_todas=dv['todas_las_monedas']); res['rejilla'][f'bloq{bloq}|{nombre}|reb{reb}|estres_{es}|estrato_{estr or "todos"}'] = cells[bloq]
                    ref = set(dv['todas_las_monedas'] if estr == 'todas_las_monedas' else dv['alguna_moneda']); nlo = len(ref & set(cells[0]['dias']))
                    v = P0.veredicto_combinado(cells[0], cells[1], nlo, fuga_n, falt)
                    if nombre != 'A_confirmatorio_05_09':                                      # ADENDA_08 3: todo veredicto que use 10-14 = NO CIEGO; maximo PASA_NO_CIEGO
                        v['etiqueta_ciego'] = ETIQ_NO_CIEGO
                        if v['veredicto'] == 'PASA': v['veredicto'] = 'PASA_NO_CIEGO'
                    res['combinado'][f'{nombre}|reb{reb}|estres_{es}|estrato_{estr or "todos"}'] = v
    suf = '|reb0.0|estres_sin|estrato_lo_valido'; sin = dict(veredicto='INSUFFICIENT', motivo='sin dias del conjunto')
    kA, kB, kC = ('A_confirmatorio_05_09' + suf, 'B_replica_10_14_NO_CIEGO' + suf, 'C_decision_05_14_NO_CIEGO' + suf)
    # consistencia A vs B (ADENDA_08 3): mismo signo de diff en bloq0 o 'A y B discrepantes' y C = AMBER
    dA, dB = (res['combinado'].get(kA) or {}).get('diff_bloq0'), (res['combinado'].get(kB) or {}).get('diff_bloq0')
    discrep = bool(dA is not None and dB is not None and np.isfinite(dA) and np.isfinite(dB) and np.sign(dA) != np.sign(dB))
    res['consistencia_A_B'] = dict(diff_bloq0_A=dA, diff_bloq0_B=dB, estado='A y B discrepantes' if discrep else ('mismo signo' if dA is not None and dB is not None else 'no evaluable'), C_ambar=discrep)
    res['veredicto_oficial'] = {**dict(clave=kC, conjunto='C = 05-14 Nov (decision, ADENDA_08)', etiqueta_ciego=ETIQ_NO_CIEGO, ambar_A_B_discrepantes=discrep), **res['combinado'].get(kC, sin)}
    res['veredicto_A_05_09'] = {**dict(clave=kA, conjunto='A = 05-09 Nov (ADENDA_06; ya leido)'), **res['combinado'].get(kA, sin)}
    res['veredicto_B_10_14'] = {**dict(clave=kB, conjunto='B = 10-14 Nov (replica)', etiqueta_ciego=ETIQ_NO_CIEGO), **res['combinado'].get(kB, sin)}
    res['lectura'] = dict(primaria=kC + ' (veredicto_combinado, ADENDA_06/08: bloq0 primaria, bloq1 mismo signo; <10 dias lo validos nunca PASA; maximo PASA_NO_CIEGO que NO autoriza promocion)', limites='03-04 Nov POST HOC; B y C = NO CIEGO (PREREG 6): no sirven por si solos para promocionar F5_t ni R1v2; sin ancla de relleno real en noviembre (fidelidad C1 FALLA); hi no validado; veredicto_bruto de cada celda NO es oficial; A (05-09) se publica aparte y no se mezcla con B sin etiqueta')
    atomic_json(OUT + 'puerta0_resultado.json', res); rep['outputs'] = {'puerta0_resultado.json': sha(OUT + 'puerta0_resultado.json')}; atomic_json(OUT + 'run_manifest.json', rep)
    log('FINAL', st_g, est, 'oficial=', res['veredicto_oficial'].get('veredicto')); return 'COMPLETE' if st_g == 'COMPLETE' else 'PARTIAL'

if __name__ == '__main__':
    modo = sys.argv[1]
    try: sha_prereg()
    except ValueError as ex: print('BLOQUEADO (fail-closed): prereg/adendas no cuadran:', ex); sys.exit(3)
    if modo == 'dia':
        d = sys.argv[2]; outs = [f'p0_ordenes_{d}.pkl', f'p0_cov_{d}.json']
        cov = None if RU.ya_completo('dia', d, outs) else cobertura_tx(d); mot = incompleto(d, cov, None) if cov else None          # un dia ya COMPLETE (mismo codigo) no re-mide
        if mot:                                   # fail-closed: dia nuevo sin cobertura libro5_tx >= 0,90 (d-1,d,d+1) o con sha de tape/bad distinto/ausente -> INCOMPLETE, no se simula
            atomic_json(RU.mpath('dia', d), dict(job=f'sec7 dia {d}', status='INCOMPLETE', motivo=mot, cobertura_tx=cov, code=code_hashes(), t_fin=ts())); log('INCOMPLETE', d, mot); sys.exit(1)
        r = RU.job('dia', d, outs, run_dia, RU.inputs_dia(d))
        if r == 'COMPLETE':                       # registra la cobertura libro5_tx en el manifest del dia (no altera outputs ni code)
            mp = RU.mpath('dia', d); m = json.load(open(mp))
            if cov and m.get('cobertura_tx') != cov: m['cobertura_tx'] = cov; atomic_json(mp, m)
    elif modo == 'final': r = final()
    else: raise SystemExit(__doc__)
    sys.exit(0 if r in ('COMPLETE', 'BLOCKED') else 1)
