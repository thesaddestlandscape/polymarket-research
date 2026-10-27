#!/usr/bin/env python3
"""cf_diario.py -- CONTRAFACTUAL SHADOW 'tomadores informados' sobre B (PREREG.md, solo lectura de produccion; 100 % pasivo).
Lee: ledger de la wallet dedicada (movimientos.csv/posiciones.csv), m5_onchain (taker de cada fill de B y, para la corriente POB,
los rellenos de otros makers), desenlaces oficiales. Escribe SOLO bajo contrafactual/salidas[ _tag ]/ y la cache de tx->taker.
Uso:  nice -n 19 ionice -c3 python3 -I cf_diario.py [--desde 2026-10-24] [--hasta AAAA-MM-DD] [--tag dryrun] [--sin-pob] [--rehacer]
Idempotente: tx->taker cacheado, particion POB por dia cacheada, el resumen se recompone entero del ledger cada vez (mismo input => mismo output)."""
import sys, os, json, time, hashlib, argparse, datetime as dt, gzip
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
import cf_lib as L

HERE = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.normpath(os.path.join(HERE, '..'))
LEDGER = '/root/polymarket-research/experimentos/5m_barato/contabilidad_wallet_dedicada/'
ap = argparse.ArgumentParser()
ap.add_argument('--desde', default='2026-10-24'); ap.add_argument('--hasta', default=None)
ap.add_argument('--tag', default=''); ap.add_argument('--sin-pob', action='store_true'); ap.add_argument('--rehacer', action='store_true')
ap.add_argument('--reps', type=int, default=3000); ap.add_argument('--perms', type=int, default=5000)
a = ap.parse_args()
hoy = dt.datetime.now(dt.timezone.utc).date()
HASTA = a.hasta or (hoy - dt.timedelta(days=1)).isoformat()
OUT = os.path.join(BASE, 'salidas' + ('_' + a.tag if a.tag else '')); os.makedirs(OUT + '/pob', exist_ok=True)
T0 = time.time()
def log(*x): print(dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), *x, flush=True)
def jdump(o, p):
    json.dump(o, open(p + '.tmp', 'w'), indent=1, default=lambda v: float(v) if isinstance(v, (np.floating, np.integer)) else str(v)); os.replace(p + '.tmp', p)
def sha_file(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]

# ---------------- sets congelados (verificar hash)
META = json.load(open(BASE + '/datos/SETS_META.json'))
SETS = {}
for nm in ('I', 'V'):
    items = [x for x in open(BASE + '/datos/set_%s.txt' % nm).read().split('\n') if x]
    assert L.sha256_lines(items) == META['sha256_set_' + nm], 'SET_%s alterado: hash no coincide' % nm
    SETS[nm] = set(items)
POOL = [x for x in open(BASE + '/datos/pool_I.txt').read().split('\n') if x]
assert L.sha256_lines(POOL) == META['sha256_pool_I'], 'POOL_I alterado'
log('sets OK', {k: len(v) for k, v in SETS.items()}, 'pool', len(POOL), 'ventana', a.desde, '..', HASTA, 'tag', a.tag or '-')

# ---------------- metrica comun
def metricas(U, setname, rng):
    """U: DataFrame con c,p,flag(bool),cl,dia,coin,tk (tomador del primer fill). EXCESO = EV_ret - EV_total (pond. por EUR)."""
    r = {'set': setname, 'n_unidades': int(len(U))}
    if len(U) == 0: r['estado'] = 'SIN_DATOS'; return r
    c = U.c.values; p = U.p.values; f = U.flag.values
    ev = lambda m: float(p[m].sum() / c[m].sum()) if m.any() and c[m].sum() > 0 else None
    r.update(n_unidades_flag=int(f.sum()), n_cierres=int(U.cl.nunique()), n_cierres_flag=int(U.cl[f].nunique()), n_dias=int(U.dia.nunique()),
             n_dias_con_flag_y_noflag=int(len(set(U.dia[f]) & set(U.dia[~f]))), coste=float(c.sum()), pnl=float(p.sum()),
             frac_eur_flag=float(c[f].sum() / c.sum()), EV_total=ev(np.ones(len(U), bool)), EV_flag=ev(f), EV_ret=ev(~f),
             media_unidad_total=float((p / c).mean()))
    exc = lambda m: (p[~m].sum() / c[~m].sum() - p.sum() / c.sum()) if (~m).any() and c[~m].sum() > 0 else np.nan
    r['EXCESO'] = float(exc(f)) if f.any() else None
    if not f.any() or f.all(): r['estado'] = 'SIN_BANDERADAS'; return r
    # IC90 por cierre (bootstrap de clusters)
    cl = pd.factorize(U.cl)[0]; ncl = cl.max() + 1
    Pt = np.bincount(cl, p, ncl); Ct = np.bincount(cl, c, ncl); Pr = np.bincount(cl, p * ~f, ncl); Cr = np.bincount(cl, c * ~f, ncl)
    es = []
    for _ in range(0, a.reps, 500):
        w = rng.multinomial(ncl, np.ones(ncl) / ncl, size=min(500, a.reps - len(es))).astype(float)
        with np.errstate(divide='ignore', invalid='ignore'):
            es.append((w @ Pr) / (w @ Cr) - (w @ Pt) / (w @ Ct))
    es = np.concatenate(es); es = es[np.isfinite(es)]
    r['IC90_cierre'] = [float(np.percentile(es, 5)), float(np.percentile(es, 95))]
    # sin los 2 mejores dias (EXCESO diario propio)
    ed = {}
    for d, g in U.groupby('dia'):
        m = g.flag.values
        if m.any() and (~m).any(): ed[d] = float(g.p.values[~m].sum() / g.c.values[~m].sum() - g.p.sum() / g.c.sum())
    r['exceso_diario'] = ed
    top2 = sorted(ed, key=ed.get, reverse=True)[:2]; k2 = ~U.dia.isin(top2).values
    r['dias_excluidos_top2'] = top2
    r['EXCESO_sin_2_mejores_dias'] = float(p[k2 & ~f].sum() / c[k2 & ~f].sum() - p[k2].sum() / c[k2].sum()) if (k2 & ~f).any() and (k2 & f).any() else None
    # por moneda
    pm = {}
    for co, g in U.groupby('coin'):
        m = g.flag.values; cc = g.c.values; pp = g.p.values
        pm[co] = {'n_unid': int(len(g)), 'n_flag': int(m.sum()), 'EV_total': float(pp.sum() / cc.sum()),
                  'EXCESO': float(pp[~m].sum() / cc[~m].sum() - pp.sum() / cc.sum()) if m.any() and (~m).any() else None}
    r['por_moneda'] = pm
    # concentracion
    tkf = U[f].groupby('tk').c.sum(); r['top_tomador_frac_eur_flag'] = float(tkf.max() / tkf.sum()); r['n_tomadores_flag'] = int(len(tkf))
    pdf = U[f].groupby('dia').p.sum().abs(); r['top_dia_frac_pnl_flag_abs'] = float(pdf.max() / pdf.sum()) if pdf.sum() > 0 else None
    # placebo: k tomadores al azar (a nivel TOMADOR) de POOL_I ∩ observados y de todos los observados
    codes, uniq = pd.factorize(U.tk); obs = set(uniq); k = len(tkf); obs_ex = exc(f); idx = {t: i for i, t in enumerate(uniq)}
    def plc(pool):
        pool = np.array(sorted(idx[t] for t in pool))      # indices de tomadores observados
        if len(pool) <= k: return None
        s = []
        for _ in range(a.perms):
            v = np.zeros(len(uniq), bool); v[rng.choice(pool, k, replace=False)] = True; s.append(exc(v[codes]))
        s = np.array(s); s = s[np.isfinite(s)]
        return float((1 + (s >= obs_ex).sum()) / (len(s) + 1)), int(len(pool))
    r['placebo_pool_I_observados'] = plc(obs & set(POOL)); r['placebo_pool_todos_observados'] = plc(obs)
    pf = np.array([exc(rng.permutation(f)) for _ in range(min(a.perms, 3000))]); pf = pf[np.isfinite(pf)]
    r['placebo_p_por_fill_permutando_banderas'] = float((1 + (pf >= obs_ex).sum()) / (len(pf) + 1))
    # gates del PREREG s.4
    g = {}
    g['G1_n_cierres_flag>=40'] = r['n_cierres_flag'] >= 40
    g['G2_dias>=10'] = r['n_dias_con_flag_y_noflag'] >= 10
    g['G3_IC90_cierre_inf>0'] = r['IC90_cierre'][0] > 0
    g['G4_EXCESO_sin_2_mejores>0'] = bool(r['EXCESO_sin_2_mejores_dias'] is not None and r['EXCESO_sin_2_mejores_dias'] > 0)
    pp_ = r['placebo_pool_I_observados']; g['G5_placebo_p<0.05'] = bool(pp_ is not None and pp_[0] < 0.05)
    mons = [m for m, v in pm.items() if v['n_flag'] >= 10]
    g['G6_signo>0_en_>=2_de_3_monedas'] = bool(sum(1 for m in mons if pm[m]['EXCESO'] is not None and pm[m]['EXCESO'] > 0) >= 2)
    g['G7_concentracion(top_tomador<=30%,top_dia<=40%)'] = bool(r['top_tomador_frac_eur_flag'] <= 0.30 and (r['top_dia_frac_pnl_flag_abs'] or 0) <= 0.40)
    r['gates'] = g
    if g['G1_n_cierres_flag>=40'] and g['G2_dias>=10']:
        r['estado'] = 'PASS' if all(g.values()) else ('REFUTADO' if (not g['G3_IC90_cierre_inf>0'] or not g['G5_placebo_p<0.05']) else 'NO_PASA')
    else:
        r['estado'] = 'EN_CURSO'
    return r

# ---------------- corriente B: fills reales de la wallet dedicada
log('corriente B: leyendo ledger')
M = pd.read_csv(LEDGER + 'movimientos.csv', usecols=['fecha_utc', 'tx', 'log_index', 'tipo', 'importe_pusd', 'mercado', 'outcome', 'size', 'precio', 'experimento'])
Pz = pd.read_csv(LEDGER + 'posiciones.csv', usecols=['mercado', 'outcome', 'experimento', 'estado', 'coste'])
B = M[(M.tipo == 'COMPRA') & (M.experimento == 'H47-B')].copy()
B['dia'] = B.fecha_utc.str[:10]; B = B[(B.dia >= a.desde) & (B.dia <= HASTA)].copy()
B['coste'] = -B.importe_pusd; B['coin'] = B.mercado.str.split('-').str[0].str.upper(); B['cl'] = B.mercado.str.extract(r'(\d+)$')[0]
Pz = Pz[Pz.experimento.str.contains('H47-B', na=False)].drop_duplicates(['mercado', 'outcome'])
B = B.merge(Pz[['mercado', 'outcome', 'estado']], on=['mercado', 'outcome'], how='left')
cob = {'fills_B_ledger_en_ventana': int(len(B)), 'tx_unicos': int(B.tx.nunique()), 'duplicados_tx': int(len(B) - B.tx.nunique())}

CTX = L.CACHE + 'b_tx_taker.csv'; os.makedirs(L.CACHE, exist_ok=True)
cache = pd.read_csv(CTX, dtype=str) if os.path.exists(CTX) else pd.DataFrame(columns=['tx', 'taker', 'ntaker'])
known = set(cache.tx)
need = B[~B.tx.isin(known)]
if len(need):
    log('buscando taker de', len(need), 'tx nuevos en m5_onchain')
    txs = set(need.tx); rows = []
    for d in sorted(set(need.dia)):
        for dd in (d, L.dday(d, 1)):
            f = L.OC % dd
            if not os.path.exists(f): log('  falta', f); continue
            with gzip.open(f, 'rt') as fh:
                for ch in pd.read_csv(fh, chunksize=80000, usecols=['tipo', 'tx', 'maker', 'taker'], dtype=str):
                    ch = ch[ch.tx.isin(txs) & (ch.tipo == 'F') & (ch.maker.str.lower() == L.US)]
                    if len(ch): rows.append(ch[['tx', 'taker']].assign(taker=lambda z: z.taker.str.lower()))
    if rows:
        R = pd.concat(rows).drop_duplicates(); G = R.groupby('tx').taker.agg(['first', 'nunique']).reset_index()
        G.columns = ['tx', 'taker', 'ntaker']; G['ntaker'] = G.ntaker.astype(str)
        cache = pd.concat([cache, G]).drop_duplicates('tx', keep='first')
        cache.to_csv(CTX + '.tmp', index=False); os.replace(CTX + '.tmp', CTX)
B = B.merge(cache, on='tx', how='left')
cob['sin_taker'] = int(B.taker.isna().sum()); cob['tx_multi_taker'] = int((B.ntaker.fillna('1') != '1').sum())
cob['pendientes_sin_liquidar'] = int(B.estado.isin(['liquidada_ganada', 'liquidada_perdida']).eq(False).sum())
Bv = B[B.taker.notna() & (B.ntaker.fillna('1') == '1') & B.estado.isin(['liquidada_ganada', 'liquidada_perdida'])].copy()
Bv['gana'] = (Bv.estado == 'liquidada_ganada').astype(int); Bv['p'] = Bv['size'] * Bv.gana - Bv.coste
Bv = Bv.sort_values(['fecha_utc', 'log_index'])
cob['fills_validos'] = int(len(Bv)); cob['coste_validos'] = float(Bv.coste.sum())
# unidad = (mercado, lado); bandera por el tomador del primer relleno
UB = Bv.groupby(['mercado', 'outcome']).agg(c=('coste', 'sum'), p=('p', 'sum'), cl=('cl', 'first'), dia=('dia', 'first'), coin=('coin', 'first'), tk=('taker', 'first')).reset_index()
rng = np.random.default_rng(777)
resB = {}
for nm in ('I', 'V'):
    UB['flag'] = UB.tk.isin(SETS[nm]).values
    resB[nm] = metricas(UB.copy(), 'SET_' + nm, rng)
    # lectura descriptiva a nivel de fill
    fl = Bv.taker.isin(SETS[nm]).values
    resB[nm]['descriptivo_fill'] = {'n_fills_flag': int(fl.sum()), 'EV_flag': float(Bv.p[fl].sum() / Bv.coste[fl].sum()) if fl.any() else None,
                                    'EV_noflag': float(Bv.p[~fl].sum() / Bv.coste[~fl].sum()) if (~fl).any() else None,
                                    'EXCESO_fill': float(Bv.p[~fl].sum() / Bv.coste[~fl].sum() - Bv.p.sum() / Bv.coste.sum()) if fl.any() and (~fl).any() else None}
serieB = Bv.assign(flagI=Bv.taker.isin(SETS['I']), flagV=Bv.taker.isin(SETS['V'])).groupby('dia').agg(
    n_fills=('p', 'size'), coste=('coste', 'sum'), pnl=('p', 'sum'), n_fills_flagI=('flagI', 'sum'), n_fills_flagV=('flagV', 'sum')).reset_index()
UB.to_csv(OUT + '/cf_unidades_B.csv', index=False)
serieB.to_csv(OUT + '/cf_serie_diaria_B.csv', index=False)
dias_con_fills = int(serieB.dia.nunique()) if len(serieB) else 0
ultima = str(B.fecha_utc.max()) if len(B) else None
# ETA n>=40 cierres banderados (tasa de cierres banderados por dia CON fills; B puede estar parado)
eta = {}
for nm in ('I', 'V'):
    r = resB[nm]; ncf = r.get('n_cierres_flag', 0) or 0
    if dias_con_fills == 0: eta[nm] = 'indeterminado: B sin fills nuevos desde %s' % (M[(M.tipo == 'COMPRA') & (M.experimento == 'H47-B')].fecha_utc.max())
    elif ncf == 0: eta[nm] = 'indeterminado: 0 cierres banderados'
    else:
        tasa = ncf / dias_con_fills; d1 = max(0.0, 40 - ncf) / tasa; d2 = max(0, 10 - (r.get('n_dias_con_flag_y_noflag') or 0))
        eta[nm] = ('a ritmo observado (%.1f cierres flag por dia con fills): G1 (n>=40) faltan %.1f dias de B activo; G2 (>=10 dias) faltan %d dias; '
                   'necesarios max = %.1f dias de B ACTIVO (solo si B tiene fills esos dias)' % (tasa, d1, d2, max(d1, d2)))
for nm in ('I', 'V'): resB[nm]['eta_n40'] = eta[nm]

# ---------------- corriente POB (otros makers), particion diaria cacheada
resP = {}
if not a.sin_pob:
    des = L.load_des(); days = [d.strftime('%Y-%m-%d') for d in pd.date_range(a.desde, HASTA)]
    cobP = {'dias_esperados': len(days), 'dias_procesados': 0, 'dias_sin_archivo': [], 'unidades_sin_desenlace': 0}
    parts = []
    for d in days:
        pth = OUT + '/pob/pob_%s.csv' % d
        if not os.path.exists(L.OC % d): cobP['dias_sin_archivo'].append(d); continue
        if a.rehacer or not os.path.exists(pth):
            F = L.fills_dia(d, des)
            if len(F):
                F = F[(F.maker != L.US) & (F.pc > 0.10) & (F.pc <= 0.30)]
                T = F.fin - F.ts; F = F[(T >= 60) & (T <= 300)]
                nres = F[F.gana < 0]; F = F[F.gana >= 0].sort_values(['ts', 'li'])
                F['cum'] = F.groupby(['maker', 'mid', 'yes']).sh.cumsum(); F['prev'] = F.cum - F.sh
                F = F[F.prev < 5]; F['sh'] = np.minimum(F.sh, 5 - F.prev)         # primeras 5 acciones por maker-mercado-lado
                F['c'] = F.sh * F.pc; F['p'] = F.sh * F.gana - F.c
                U = F.groupby(['maker', 'mid', 'yes']).agg(c=('c', 'sum'), p=('p', 'sum'), cl=('fin', 'first'), coin=('coin', 'first'), tk=('taker', 'first')).reset_index()
                U['dia'] = d; U['sin_desenlace_dia'] = len(nres)
            else:
                U = pd.DataFrame(columns=['maker', 'mid', 'yes', 'c', 'p', 'cl', 'coin', 'tk', 'dia', 'sin_desenlace_dia'])
            U.to_csv(pth + '.tmp', index=False); os.replace(pth + '.tmp', pth)
            log('POB', d, 'unidades', len(U))
        U = pd.read_csv(pth, dtype={'tk': str, 'maker': str}); cobP['dias_procesados'] += 1
        cobP['unidades_sin_desenlace'] += int(U.sin_desenlace_dia.max()) if len(U) else 0
        parts.append(U)
    UP = pd.concat(parts) if parts else pd.DataFrame()
    for nm in ('I', 'V'):
        if len(UP): UP['flag'] = UP.tk.isin(SETS[nm]).values
        resP[nm] = metricas(UP.copy(), 'POB_SET_' + nm, rng) if len(UP) else {'estado': 'SIN_DATOS'}
    resP['cobertura'] = cobP

# ---------------- salida
out = {'job': 'cf_diario', 'prereg_sha256': sha_file(BASE + '/PREREG.md'), 'sets_sha256': {k: META['sha256_set_' + k] for k in 'IV'},
       'ventana': [a.desde, HASTA], 'generado_utc': dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), 'tag': a.tag,
       'evaluacion_valida_para_gates': a.tag == '' and a.desde >= '2026-10-24',
       'cobertura_B': cob, 'B': resB, 'POB': resP,
       'estado_global_B': ('BLOCKED_SIN_FLUJO' if dias_con_fills == 0 else resB['I'].get('estado'))}
jdump(out, OUT + '/cf_resumen_%s.json' % HASTA); jdump(out, OUT + '/cf_resumen_ultimo.json')
man = {'job_id': 'cf_tomadores_informados_B', 'codigo_sha256': {f: sha_file(os.path.join(HERE, f)) for f in ('cf_diario.py', 'cf_lib.py', 'build_set.py')},
       'parametros': vars(a), 'hasta_efectivo': HASTA, 'entradas': {'movimientos.csv': sha_file(LEDGER + 'movimientos.csv'), 'posiciones.csv': sha_file(LEDGER + 'posiciones.csv'),
       'set_I': META['sha256_set_I'], 'set_V': META['sha256_set_V']}, 'inicio_epoch': T0, 'fin_epoch': time.time(),
       'estado': 'COMPLETE', 'cobertura': cob, 'comando': 'nice -n 19 ionice -c3 python3 -I %s %s' % (os.path.join(HERE, 'cf_diario.py'), ' '.join(sys.argv[1:]))}
jdump(man, OUT + '/run_manifest.json')
log('FIN', json.dumps({k: {'estado': v.get('estado'), 'n_unid': v.get('n_unidades'), 'n_flag': v.get('n_unidades_flag'), 'EXC': v.get('EXCESO')} for k, v in resB.items()}), 'cob', json.dumps(cob))
