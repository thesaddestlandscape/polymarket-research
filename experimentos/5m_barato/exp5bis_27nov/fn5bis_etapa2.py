#!/usr/bin/env python3
"""fn5bis_etapa2.py dia DIA | final DIA1,DIA2   (27-Nov, engineer 5m barato; CONTRATO_5BIS_EXP5B_27nov.md). Etapa ligera (cadena + libro5_tx, sin motor): FN/FP (1a), calibracion 1b y agregado final (+ F2 1c) con manifest.
'dia': lee ordenes_K6_base_DIA.pkl (etapa 1) y escribe fn5bis_dia_DIA.json (+ fn5bis_ordenes_DIA.pkl, fn5bis_fn_fp_DIA.json). Idempotente: si el JSON existe con los mismos sha de entradas, no rehace.
'final': agrega dias, escribe fn5bis_final.json + run_manifest.json (job, codigo sha, entradas sha, intended/processed dates, status) y COVERAGE por dia."""
import sys, os, json, time, hashlib, collections
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np, pandas as pd
import fn5bis_core as C
OUT5 = '/root/polymarket-research-datalogs/exp5bis_27nov/'
MIN_FILAS_CADENA_MONEDA = 200


def sha16(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 22), b''): h.update(b)
    return h.hexdigest()[:16]


def wjson(p, d):
    tmp = p + '.tmp'
    with open(tmp, 'w') as f: json.dump(d, f, indent=1, sort_keys=True, default=str)
    os.replace(tmp, p)


def dia(d):
    pk = OUT5 + f'ordenes_K6_base_{d}.pkl'
    if not os.path.exists(pk): raise SystemExit(f'BLOCKED: falta {pk} (etapa 1)')
    ent = dict(ordenes=sha16(pk), onchain=''.join(sha16(p) for _, p in __import__('cadena_v2v3').rutas_cadena(d)), codigo=sha16(HERE + '/fn5bis_core.py') + sha16(__file__))
    psm = OUT5 + f'status_motor_{d}.pkl'
    if os.path.exists(psm): ent['status_motor'] = sha16(psm)
    pj = OUT5 + f'fn5bis_dia_{d}.json'
    prev = {}
    if os.path.exists(pj):
        try: prev = json.load(open(pj))
        except ValueError: print('AVISO: fn5bis_dia corrupto, se rehace', d)          # checkpoint corrupto => se reconstruye (nada se acumula entre dias: sin doble conteo)
    if prev.get('entradas_sha16') == ent: print('ya hecho (mismas entradas)', d); return
    R = pd.read_pickle(pk); ST = pd.read_pickle(psm) if os.path.exists(psm) else None
    toks = set(R.token.astype(str)); t0 = time.time()
    E, Mk, cont = C.carga_cadena(d, toks)
    tok2coin = dict(zip(R.token.astype(str), R.coin.astype(str).str.lower()))
    filas_coin = E.token.map(tok2coin).value_counts().to_dict(); ordenes_coin = R.coin.astype(str).str.lower().value_counts().to_dict()
    validas = sorted(c for c in ordenes_coin if filas_coin.get(c, 0) >= MIN_FILAS_CADENA_MONEDA)       # moneda sin casados on-chain en el dia (p.ej. SOL/XRP 24-25 Nov: el indexador no cubre su contrato) => el motor chain-mode tampoco los ve: dia NO valido para esa moneda
    excl = {c: dict(ordenes=int(ordenes_coin[c]), filas_cadena=int(filas_coin.get(c, 0))) for c in ordenes_coin if c not in validas}
    if excl:
        msk = R.coin.astype(str).str.lower().isin(validas).values
        R = R[msk].reset_index(drop=True); ST = (ST[msk].reset_index(drop=True) if ST is not None else None)
    rx, tk_vistos = C.carga_rx(d, set(E.tx)); tev = getattr(C.carga_rx, 'tev', {})
    cob = dict(filas_ajenas=int(len(E)), con_reloj=int(E.tx.isin(rx).sum()), cobertura_reloj=(float(E.tx.isin(rx).mean()) if len(E) else None))
    res, fn, fp, O, units = C.audita_dia(R, E, Mk, rx, cont, d, tev=tev, status=ST)
    O.to_pickle(OUT5 + f'fn5bis_ordenes_{d}.pkl')
    G = C.calibracion_1b(O, d); G.to_pickle(OUT5 + f'fn5bis_celdas_{d}.pkl')
    res.update(dia=d, entradas_sha16=ent, filas_cadena_ajenas_por_moneda=filas_coin, monedas_validas=validas, monedas_excluidas_sin_cadena=excl, cobertura_join_reloj=cob, fn_lista=fn, fp_lista=fp, calibracion_1b=C.resumen_calibracion(G), segundos=round(time.time() - t0, 1),
               referencia_propia=dict(filas_F_maker_wallet_B_exacta=cont.get('F_maker_wallet_B_exacta'), filas_F_con_prefijo_propio_0x659a_0xb6ed=cont.get('F_filas_con_prefijo_propio'),
                                      nota='0 rellenos reales de B en la cadena => la referencia de relleno PROPIO (§1a) esta vacia; FN propio = 0 por vacuidad, no por prueba'),
               generado=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    wjson(pj, res); print('dia OK', d, res['FN_duros_unidades'], res['unidades_con_evidencia_dura'])


def final(dias):
    t0 = time.time(); ds = dias.split(','); P = {}; faltan = []
    for d in ds:
        p = OUT5 + f'fn5bis_dia_{d}.json'
        (P.__setitem__(d, json.load(open(p))) if os.path.exists(p) else faltan.append(d))
    F2 = {}
    for d in ds:
        p = OUT5 + f'f2_replay_{d}.json'
        if os.path.exists(p):
            F2[d] = json.load(open(p)); q = OUT5 + f'f2_cxb60_seg_{d}.pkl'
            if os.path.exists(q):
                vm = [c.upper() for c in P[d]['monedas_validas']] if d in P else ['ETH', 'SOL', 'XRP']; s = pd.read_pickle(q); s = s[s.coin.isin(vm)]
                F2[d]['por_variante_moneda'] = {k: v for k, v in F2[d]['por_variante_moneda'].items() if k.split('|')[1] in vm}; F2[d]['monedas_validas'] = vm
                u = s.groupby(['coin', 'mid', 'lado']).agg(v3=('q_v3', lambda x: bool((x > 1e-9).any())), v4=('q_v4', lambda x: bool((x > 1e-3).any())), v34=('q_v4_l1_34', lambda x: bool((x > 1e-3).any()))).reset_index()
                F2[d]['CXB60_unidades_mercado_lado'] = {c: dict(unidades=int(len(x)), con_relleno_engine_v3=int(x.v3.sum()), con_relleno_passT_v4=int(x.v4.sum()), con_relleno_passT_v4_l1_34=int(x.v34.sum()), ambos=int((x.v3 & x.v4).sum()), v3_si_v4_no=int((x.v3 & ~x.v4).sum()), v3_no_v4_si=int((~x.v3 & x.v4).sum())) for c, x in u.groupby('coin')}
    E1 = {}
    for d in ds:
        p = OUT5 + f'etapa1_{d}.json'
        if os.path.exists(p):
            j = json.load(open(p)); b = j['brazos']['base']
            E1[d] = dict(sello_rf5_actual=j.get('sello_rf5_actual'), SELLO_FIRMADO_paridad_lib=j.get('sello_paridad_lib_SELLO_FIRMADO'), motor_info=j.get('motor_info'), l3b=j.get('l3b'), ordenes=b['ordenes'], rellenos_motor_ordenes=b['rellenos'], mercados_con_orden=b['mercados_con_orden'],
                         cobertura=b['cobertura'], clases_ventanas=j.get('clases_ventanas'), git_dev_bk=j.get('git_dev_bk'), verifica_registro=j.get('verifica_registro'))
    tot = collections.Counter(); causas = collections.Counter(); G = []
    for d, x in P.items():
        tot['unidades'] += x['unidades']; tot['con_relleno_motor'] += x['unidades_con_relleno_motor']; tot['evidencia_dura'] += x['unidades_con_evidencia_dura']; tot['evidencia_nivel'] += x['unidades_con_evidencia_nivel']
        tot['FN_duros'] += x['FN_duros_unidades']; tot['no_FN_no_armables'] += x['no_FN_no_armables_unidades_(motor descarta la orden al llegar)']; tot['FN_offset_ambiguos'] += x['FN_offset_ambiguos_unidades']; tot['FP'] += x['FP_unidades(motor rellena y 0 filas ajenas a precio<=L en +-300 ms del tf)']
        tot['F_maker_wallet_B'] += x['referencia_propia']['filas_F_maker_wallet_B_exacta'] or 0
        for k, n in list(x['FN_duros_por_moneda_causa'].items()) + list(x['no_FN_no_armables_por_moneda_causa'].items()) + list(x['FN_offset_ambiguos_por_moneda_causa'].items()): causas[k.split('|')[1]] += n
        G.append(pd.read_pickle(OUT5 + f'fn5bis_celdas_{d}.pkl'))
    cal = C.resumen_calibracion(pd.concat(G, ignore_index=True)) if G else {}
    n_dias = len(P)
    v1a = 'INSUFFICIENT' if tot['F_maker_wallet_B'] == 0 else 'BLOCKED(hay filas propias: comparar FN propio no implementado; revisar a mano)'
    v1a_proxy = ('AMBER' if n_dias < 3 else 'GREEN') if (tot['FN_duros'] + tot['FN_offset_ambiguos']) == 0 else 'AMBER'
    out = dict(job='exp5bis FN=0 + M4-sustituto + F2 passT_v4 (CONTRATO_5BIS_EXP5B_27nov.md sha 05b38180664c)', dias_procesados=sorted(P), dias_que_faltan=faltan,
               dias_no_usados=dict(**{'19..23-Nov': 'BLOCKED (pausa libro5)', '25-Nov': 'libro5_ms pid 2744946 truncado: NO COMPLETE (declarado); piloto aparte en capacidad_b_27nov', '26-Nov': 'PENDING'}),
               etapa1_por_dia=E1, monedas_validas_por_dia={d: x['monedas_validas'] for d, x in P.items()}, monedas_excluidas_por_dia={d: x['monedas_excluidas_sin_cadena'] for d, x in P.items()}, totales=dict(tot), causas_FN_duros=dict(causas),
               veredicto_1a_referencia_propia=v1a + ' (0 filas F con maker=wallet B en los dias; FN propio = 0 por vacuidad)',
               veredicto_1a_proxy_makers_ajenos=v1a_proxy + (' (FN nominales=%d, FN offset-ambiguos<=100ms=%d)' % (tot['FN_duros'], tot['FN_offset_ambiguos'])),
               calibracion_1b=cal, veredicto_1b='INSUFFICIENT' + ' (%d dias COMPLETE <3; contrato exige >=3 dias y >=40 (mercado,lado,nivel) por moneda)' % n_dias,
               f2={d: dict(CXB60_unidades_mercado_lado=v.get('CXB60_unidades_mercado_lado'), por_variante_moneda=v['por_variante_moneda'], solo_conteos=v['solo_conteos'], politica=v['politica']) for d, v in F2.items()},
               veredicto_1c='AMBER (conteos passT_v4 sobre las MISMAS ordenes del dry-run; no es reeval completa; %d dias)' % len(F2))
    out['generado'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()); out['segundos_final'] = round(time.time() - t0, 1)
    out['sello_sha256_sin_este_campo'] = hashlib.sha256(json.dumps({k: v for k, v in out.items() if k != 'sello_sha256_sin_este_campo'}, sort_keys=True, default=str).encode()).hexdigest()
    wjson(OUT5 + 'fn5bis_final.json', out)
    ent = {f: sha16(OUT5 + f) for f in sorted(os.listdir(OUT5)) if f.startswith(('ordenes_K6_base_', 'fn5bis_dia_', 'f2_replay_', 'etapa1_'))}
    wjson(OUT5 + 'run_manifest.json', dict(job_id='M5BIS_EXP5B_27NOV_v1/5bis', codigo_sha16=dict(core=sha16(HERE + '/fn5bis_core.py'), etapa2=sha16(__file__), etapa1=sha16(HERE + '/fn5bis_etapa1.py')),
                                           parametros=dict(tol=C.TOL, borde_ms=C.BORDE, politica='K6 base (piloto_m1_m4.etapa1)', latencia='paquete_l 13-Nov (L1 34/47, L3b 59 fallback)'),
                                           entradas_sha16=ent, dias_previstos=ds, dias_procesados=sorted(P), dias_faltan=faltan, status=('COMPLETE' if not faltan and F2 and len(F2) == len(ds) else 'PARTIAL'), generado=out['generado'],
                                           reproduccion='bash %s/run_5bis.sh && python3 -I -B %s/fn5bis_etapa2.py dia 2026-11-18 && python3 -I -B %s/fn5bis_etapa2.py dia 2026-11-24 && python3 -I -B %s/fn5bis_etapa2.py final 2026-11-18,2026-11-24' % (HERE, HERE, HERE, HERE)))
    print('final OK', out['veredicto_1a_proxy_makers_ajenos'], out['totales'])


if __name__ == '__main__':
    {'dia': lambda: dia(sys.argv[2]), 'final': lambda: final(sys.argv[2])}[sys.argv[1]]()
