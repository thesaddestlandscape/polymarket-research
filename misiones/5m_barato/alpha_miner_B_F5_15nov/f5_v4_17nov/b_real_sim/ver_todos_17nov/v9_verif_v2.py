#!/usr/bin/env python3
# ver_todos_17nov/v9_verif_v2.py (18-Nov): COPIA GENERADA de v4_verif_dem.py (lineas 1-83 identicas salvo OUT=out_v2/, TAGP V2_) + variantes del PREREG_VER_TODOS_v2_18nov (dem_hook_v2). v4_verif_dem/dem_hook NO se tocan.
# ver_todos_17nov/v4_verif_dem.py: COPIA GENERADA de b_real_sim/verif_v5.py (17-Nov) + gancho dem_hook (cinta de demanda tomadora residual). verif_v5 NO se toca. sys.path del dir de este fichero.
# VERSION v5 (17-Nov, b_real_sim): verif_v4 con tiempos del CONTRATO v2. verif_v4 NO se toca. # (v4:): copia de verif_v3.py con engine_v4 (relleno sin polvo, FLOOR=1e-3, funcion unica engine_v4.relleno/es_fill). Salida en out_v4/ (no pisa out_v3/). Original sin editar.
"""verif_v3.py DIA -- verif_real/verif.py (no se edita) con SELLO v3 (stamp_v3.py) y motor con/sin dedupe (engine_v3.fill_segment_v3), contra las ordenes REALES de B (ordenes_b.csv, ledger; 20-23 Oct). SOLO LECTURA, 0 ordenes.
RELOJ: sa_ms v1 solo tiene EXCHANGE (q_t y t_t). El 'print' de cada tx es el WS emparejado por tamano (t_m, EX, como verif.py); la fila de consumo se busca por firma EXACTA (token+precio+tamano TOTAL del tx, incluida nuestra
orden: nuestro tamano SI esta en la fila real del libro) en +-1,5 s EX; unica -> ex(fila)-1; ambigua/sin firma -> t_m - c_dia - 1 (c_dia = p50 de d_ex de las unicas del dia); sin emparejado WS (src=bloque) -> bloque-2,25 s -63 ms (legacy, contado).
Cinta = fills de OTROS makers (NUESTRA wallet excluida, como verif.py). Salida: verif_real/out_v4/V3_<D>.pkl, columnas <tag>_<VAR>_f_q/_tf, tag in {v2o (regla vieja + motor original: regresion de V_<D>.pkl), v3o (sello v3, motor original), v3d (sello v3 + dedupe)}, VAR in BASE/OPT."""
import sys, os, json, time, numpy as np, pandas as pd
T0 = time.time(); H = os.path.dirname(os.path.abspath(__file__)) + '/'; HV = H; H = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/'; OUT = HV + 'out_v2/'; os.makedirs(OUT, exist_ok=True); sys.path.insert(0, H); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# ---- v5: tiempos de la orden real segun CONTRATO v2 sec.2. ARR in {legacy (t_ini), call0 (t_call0+EX_ALTA), dec (t_dec+D_ALTA+EX_ALTA)}; CANC in {legacy (t_fuera), int (t_cancel_int+EX_CANC)}
ARR = os.environ.get('V5_ARR', 'call0'); CANC = os.environ.get('V5_CANC', 'int'); EXA = int(os.environ.get('B_EX_ALTA', 35)); EXC = int(os.environ.get('B_EX_CANC', 33)); DAL = int(os.environ.get('B_D_ALTA', 53)); DSEND = int(os.environ.get('V5_DSEND', 0))
TAGP = 'V2_' + f'r3_{ARR}{DSEND}a{EXA}_{CANC}c{EXC}_{os.environ.get("V5_ENG", "v3d")}'
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
sys.path.insert(0, P2 + 'escalera_B'); import engine as G
sys.path.insert(0, P2 + 'captura_prints'); import reconstructor_relleno as RR
import engine_v4 as E4, stamp_v3 as ST
DL = '/root/polymarket-research-datalogs/'; OWN = '0x659a40ff9920febc5a66836213040924343d297f'
d = sys.argv[1]
if os.path.exists(OUT + f'{TAGP}_{d}.pkl'): print('ya', TAGP, d); sys.exit(0)
E = G.DayEng(d, 'ws'); D = E.D; tok5 = {t for t, m in zip(D.toks, D.marco) if m == '5min'}
ch = []
for c in pd.read_csv('/mnt/HC_Volume_106538179/keep_onchain_re_as_b/' + f'onchain_fills_{d}.csv.gz', usecols=['tipo', 'ts_est', 'tx', 'log_index', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt'],
                     dtype={'token_id': str, 'maker': str, 'taker': str, 'tx': str}, chunksize=400000):
    ch.append(c[c.token_id.isin(tok5)])
RAW = pd.concat(ch); del ch; FM_ALL = RR.fills_makers(RAW); FM_ALL['maker'] = FM_ALL.maker.str.lower(); fills = RR.fills_makers(RAW); fills['maker'] = fills.maker.str.lower(); fills = fills[fills.side == 0].copy()
# ---- emparejado con prints WS (identico a verif.py)
PR = {}
def prints_of(k, sd):
    key = (k, sd)
    if key not in PR:
        a, b = D.tb[k], D.tb[k + 1]; m = D.tsd[a:b] == sd; PR[key] = (D.tt[a:b][m], D.tsz[a:b][m].astype(float))
    return PR[key]
g = fills.groupby(['tx', 'token_id']).agg(S=('sh', 'sum'), ts=('ts_est', 'min')).reset_index(); tm_ = {}
for tx, tok, S, ts in zip(g.tx.values, g.token_id.values, g.S.values, g.ts.values):
    k = D.tokidx.get(tok)
    if k is None: continue
    c0 = ts * 1000 - 2250; best = None
    for kk, sd in ((k, 0), (D.comp(k), 1)):
        if kk is None: continue
        tt, sz = prints_of(kk, sd); i0 = np.searchsorted(tt, ts * 1000 - 4500); i1 = np.searchsorted(tt, ts * 1000 - 200, side='right')
        for j in range(i0, i1):
            if abs(sz[j] - S) <= 0.02 and (best is None or abs(tt[j] - c0) < abs(best - c0)): best = int(tt[j])
    if best is not None: tm_[(tx, tok)] = best
fills['t_m'] = [tm_.get((a, b), -1) for a, b in zip(fills.tx.values, fills.token_id.values)]
fills['src'] = np.where(fills.t_m >= 0, 'ws_match', 'bloque'); fills['t_ws_ms'] = np.where(fills.t_m >= 0, fills.t_m, (fills.ts_est * 1000 - 2250)).astype(np.int64)
cob = float((fills.src == 'ws_match').mean()); print('cobertura emparejado', round(cob, 4), 'fills', len(fills), flush=True)
own = fills[fills.maker == OWN]; fills_x = fills[fills.maker != OWN]
# ---- eventos (k, tx) con S/pmax/npr de TODOS los fills (incluye nuestra orden: esta en la fila real del libro) y tape de otros
fa = fills.assign(k=fills.token_id.map(D.tokidx)); fa = fa[fa.k.notna()].copy(); fa['k'] = fa.k.astype(int); fa['pr3'] = fa.price.round(3)
evA = fa.groupby(['k', 'tx']).agg(t=('t_ws_ms', 'min'), tm_ws=('t_m', 'max'), pmin=('price', 'min'), pmax=('pr3', 'max'), S=('sh', 'sum'), npr=('pr3', 'nunique')).reset_index()
tp = fills_x.assign(k=fills_x.token_id.map(D.tokidx)); tp = tp[tp.k.notna()].copy(); tp['k'] = tp.k.astype(int)
def stamp_v2(ev):
    tm = np.empty(len(ev), np.int64); evk = ev.k.values; evt = ev.t.values.astype(np.int64); evp = ev.pmin.values
    for i in range(len(ev)):
        k = evk[i]; t = evt[i]; pm = evp[i]; a, b = D.qb[k], D.qb[k + 1]; qt = D.qt[a:b]; v0 = D.v0[a:b]
        i0 = np.searchsorted(qt, t - 400, side='left'); i1 = np.searchsorted(qt, t, side='right'); tm[i] = t - 63
        if i1 > i0 and i0 > 0:
            lo = v0[i0 - 1:i1] <= pm + G.TOLP; w = np.where(lo[1:] & ~lo[:-1])[0]
            if len(w): tm[i] = int(qt[i0 + w[0]])
    return tm
tev = np.where(evA.tm_ws.values >= 0, evA.tm_ws.values, -1).astype(np.int64)
tm3, rama, row, dex, c_dia, nex = ST.stamp_events(D.qt, D.v0, D.v2, D.qb, evA.k.values, tev, evA.pmax.values, evA.pmin.values, evA.S.values, evA.npr.values)
tm3 = np.where(rama == 'sinev', evA.t.values.astype(np.int64) - 63, tm3)
BR = {r: int((rama == r).sum()) for r in ('sig', 'amb', 'nosig', 'guard', 'sinev')}; print('ramas v3', BR, 'c_dia', c_dia, 'n eventos', len(evA), flush=True)
evX = tp.groupby(['k', 'tx']).agg(t=('t_ws_ms', 'min'), pmin=('price', 'min')).reset_index(); tm2x = stamp_v2(evX); tm2 = pd.Series(tm2x, index=pd.MultiIndex.from_frame(evX[['k', 'tx']])).reindex(pd.MultiIndex.from_frame(evA[['k', 'tx']])).values
TAPES = {}
for tag, tmv, EV_ in (('v3', tm3, evA),):
    mm = EV_[['k', 'tx']].assign(tm=tmv)
    t2 = tp.merge(mm, on=['k', 'tx'], how='left'); t2['t_ws_ms'] = t2.tm.astype(np.int64)
    TAPES[tag] = G.Tape('chain', D, t2[['token_id', 'price', 'sh', 'side', 't_ws_ms', 'tx', 'log_index']])
# sello de NUESTRO propio relleno (para medir donde cae el relleno real respecto al simulado)
own_k = own.assign(k=own.token_id.map(D.tokidx)).merge(evA[['k', 'tx']].assign(tm3=tm3, tm2=tm2, rama=rama), on=['k', 'tx'], how='left')
pass

def qupd3(k, L, t0, t1):
    a, b = D.qb[k], D.qb[k + 1]; qt = D.qt[a:b]; i0 = np.searchsorted(qt, t0, side='right'); i1 = np.searchsorted(qt, t1, side='right'); s, e = a + i0, a + i1
    prev = np.full(e - s, np.nan)
    if e > s:
        j = np.arange(s, e) - 1; ok = j >= a; pv0 = np.where(ok, D.v0[np.maximum(j, 0)], np.nan); pv2 = np.where(ok, D.v2[np.maximum(j, 0)], np.nan)
        prev = np.where(ok & (np.abs(pv0.astype(float) - L) < G.EPS), pv2, np.nan)
    return qt[i0:i1], D.v0[s:e], D.v2[s:e], prev
def run(tape, k, L, t0, t1, size, var, dedupe):
    return E4.fill_segment_v4(D.book(k, t0), 0.0, qupd3(k, L, t0, t1) if var == 'BASE' else None, tape.get(k, L, t0, t1), L, t0, t1, size, var, dedupe=dedupe)
# ======================= v2 (PREREG_VER_TODOS_v2_18nov) =======================
import hashlib, dem_hook as DH, dem_hook_v2 as DH2
assert hashlib.sha256(open(HV + 'PREREG_VER_TODOS_v2_18nov.md', 'rb').read()).hexdigest().startswith('b3374be38c2f12ce')
def qupd3t(k, L, t0, t1):
    qt, v0, v2, prev = qupd3(k, L, t0, t1); a = D.qb[k]; i0 = np.searchsorted(D.qt[a:D.qb[k + 1]], t0, side='right'); s = a + i0
    j = np.arange(s, s + len(qt)) - 1; prevt = np.where(j >= a, D.qt[np.maximum(j, 0)], t0 - 1).astype(float)
    return qt, v0, v2, prev, prevt
def eng(bk, q, prints, L, ta, te, size):
    qq, tf, mot = E4.fill_segment_v4(bk, 0.0, q, prints, L, ta, te, size, 'BASE', dedupe=True)
    return float(qq), (int(tf) if E4.es_fill(qq) else -1)
DH.construir(D, RAW, FM_ALL, evA, tm3, OWN, d, OUT)
EVD = DH2.add_tfill(pd.read_pickle(OUT + f'DEMEV_{d}.pkl')); EVD.to_pickle(OUT + f'DEMEV_{d}.pkl')
DEM = {k: g.sort_values('t') for k, g in EVD[EVD.dec == 'ok'].groupby('k')}
print('DEMt elegibles (sin filas nuestras, n_aj>0, resid_t>1e-3):', int(((EVD.dec == 'ok') & (EVD.f_own <= 0) & (EVD.n_aj > 0) & (EVD.resid_t > DH2.FLOOR)).sum()),
      'resid S_T>1e-3 sin filas nuestras:', int(((EVD.dec == 'ok') & (EVD.f_own <= 0) & (EVD.n_aj > 0) & (EVD.resid > DH2.FLOOR)).sum()), 'de', len(EVD), flush=True)
RND = []
for sd in range(DH2.NRND):
    rg = np.random.default_rng(1000 + sd); RND.append({k: int(rg.choice([-1, 1]) * rg.uniform(5000, 30000)) for k in sorted(DEM)})
bf = pd.read_csv(DL + 'calibracion_etiqueta/b_fills_onchain.csv', usecols=['tx', 'token_id', 'order_hash'], dtype={'token_id': str, 'tx': str}).drop_duplicates()
okk = own_k.merge(bf, on=['tx', 'token_id'], how='left').dropna(subset=['order_hash', 'tm3'])
OWNBY = {h: sorted(zip(g.tm3.astype(float), g.sh.astype(float))) for h, g in okk.groupby('order_hash')}
AMB = {}
for kk_, t_, r_ in zip(evA.k.values, tm3, rama):
    if r_ in ('amb', 'sinev'): AMB.setdefault(int(kk_), []).append(int(t_))
AMB = {k: np.sort(np.array(v)) for k, v in AMB.items()}
BN = pd.read_csv(f'/root/polymarket-research-datalogs/binance_bookticker_{d}.csv', usecols=['ts_recepcion_ms', 'activo', 'mid']).dropna()
BN = {a: (g.ts_recepcion_ms.values.astype(np.int64), np.log(g.mid.values.astype(float))) for a, g in BN.sort_values('ts_recepcion_ms').groupby('activo')}
L2 = DH2.L2Day(); SUELO = int(os.environ.get('V2_SUELO', 38))
O = pd.read_csv(DL + 'calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str}); O = O[O.dia == d]
rows = []; bins = []; nb_skip = dict(sin_libro=0, sin_bn=0)
for r in O.itertuples():
    k = D.tokidx.get(str(r.tok)); base = dict(oid=r.oid, dia=d, coin=r.coin, lado=r.lado, L=round(float(r.precio), 2), size=float(r.size), T=r.T, real_fill=int(r.fill), real_q=float(r.acc_llena), gana=r.gana_lado, cola=r.cola, k=k)
    if k is None or D.marco[k] != '5min' or D.comp(k) is None: base.update(cov='sin_sa_ms'); rows.append(base); continue
    L = base['L']; size = base['size']; tcall0 = int(round(r.t_call0 * 1000)); tdec = int(round(r.t_dec * 1000)); tci = None if pd.isna(r.t_cancel_int) else int(round(r.t_cancel_int * 1000)); cie = int(r.cie)
    ta = {'legacy': int(r.t_ini * 1000), 'call0': tcall0 + DSEND + EXA, 'dec': tdec + DAL + EXA}[ARR]
    te = int(r.t_fuera * 1000) if CANC == 'legacy' else (tci + EXC if tci is not None else (cie - 60) * 1000 + EXC)
    te = max(te, ta + 1); base.update(t_arr=ta, t_end=te, sin_cancel=int(tci is None))
    own = OWNBY.get(r.oid, []); live = DH2.live_fn(size, own); base['own_n'] = len(own); base['own_t1'] = own[0][0] if own else np.nan
    PR = TAPES['v3'].get(k, L, ta, te); cola = float(r.cola)
    q, tf, mot = run(TAPES['v3'], k, L, ta, te, size, 'BASE', True); base['BASE_f_q'] = float(q); base['BASE_f_tf'] = int(tf) if E4.es_fill(q) else -1
    bk, qc = DH._cola(D, k, L, ta, te, size, cola, qupd3); base['COLA_f_q'], base['COLA_f_tf'] = eng(bk, qc, PR, L, ta, te, size)
    bkc = DH2.bk_cola(D, k, L, ta, cola); qv = DH2.q_viva(*qupd3t(k, L, ta, te), live)
    base['COLAv_f_q'], base['COLAv_f_tf'] = cv = eng(bkc, qv, PR, L, ta, te, size)
    g = DEM.get(k)
    for nm, kind, sh in [('DEMe_COLAv', 'e', 0), ('DEMt_COLAv', 't', 0), ('DEMt_COLAv_p30', 't', 30000), ('DEMt_COLAv_m30', 't', -30000)] + [(f'DEMt_COLAv_rnd{s_}', 't', RND[s_].get(k, 0)) for s_ in range(DH2.NRND)]:
        st, ss = DH2.dem_arrays(g, L, ta, te, kind, sh); base[f'{nm}_nsint'] = len(st)
        base[f'{nm}_f_q'], base[f'{nm}_f_tf'] = cv if len(st) == 0 else eng(bkc, qv, DH2.inject(PR, st, ss, L), L, ta, te, size)
        if len(st): base[f'{nm}_rsum'] = float(ss.sum())
    ser = L2.series(r.tok, L); base['l2'] = int(ser is not None); bk0 = D.book(k, ta)
    for nm, su, sh, opt in [('L2Q', SUELO, 0, False), ('L2Q20', 20, 0, False), ('L2Q_opt', SUELO, 0, True), ('L2Q_p30', SUELO, 30000, False), ('L2Q_m30', SUELO, -30000, False)]:
        if ser is None or bk0 is None: base[f'{nm}_f_q'], base[f'{nm}_f_tf'] = cv; continue
        a0, q2, found = DH2.l2_q(ser, L, ta, te, size, live, su, sh, opt)
        base[f'{nm}_f_q'], base[f'{nm}_f_tf'] = eng((L, bk0[1], a0, bk0[3]), q2, PR, L, ta, te, size)
        if nm == 'L2Q': base['l2_found_add'] = found; base['l2_ahead0'] = a0; base['l2_nrows'] = len(q2[0])
    for CAP in DH2.CAPS:
        tec = max(min(te, ta + CAP), ta + 1); PRc = TAPES['v3'].get(k, L, ta, tec)
        q, tf, mot = E4.fill_segment_v4(D.book(k, ta), 0.0, qupd3(k, L, ta, tec), PRc, L, ta, tec, size, 'BASE', dedupe=True); base[f'BASE_cap{CAP}_f_q'] = float(q); base[f'BASE_cap{CAP}_f_tf'] = int(tf) if E4.es_fill(q) else -1
        base[f'COLAv_cap{CAP}_f_q'], base[f'COLAv_cap{CAP}_f_tf'] = eng(bkc, DH2.q_viva(*qupd3t(k, L, ta, tec), live), PRc, L, ta, tec, size)
    a_ = AMB.get(k); base['n_amb_sinev'] = 0 if a_ is None else int(np.searchsorted(a_, te, side='right') - np.searchsorted(a_, ta, side='left'))
    # ---- bins de hazard (paso 2b): solo datos <= t; y = 1.er relleno real (sello v3) en [t, t+250)
    tf1 = own[0][0] if own else None; tend = te if tf1 is None else min(te, int(tf1) + 1); sgn = 1.0 if r.lado == 'YES' else -1.0
    bt, bl = BN.get(r.coin.upper(), (None, None))
    for i_, t in enumerate(range(ta, tend, 250)):
        if i_ >= 400: break
        bkb = D.book(k, t - 40)
        if bkb is None: nb_skip['sin_libro'] += 1; continue
        if bt is None or np.searchsorted(bt, t - 30000, side='right') == 0: nb_skip['sin_bn'] += 1; continue
        j0 = np.searchsorted(bt, t, side='right') - 1; lm = lambda w: bl[np.searchsorted(bt, t - w, side='right') - 1]
        bins.append(dict(oid=r.oid, dia=d, coin=r.coin, t=t, y=int(tf1 is not None and t <= tf1 < t + 250), L=L, size=size, gana=r.gana_lado, real_fill=int(r.fill),
                         dist=round((bkb[0] - L) / 0.01), spread=bkb[1] - bkb[0], lbsz=np.log1p(bkb[2]), lcola=np.log1p(cola), Tc=cie - t / 1000, yes=int(r.lado == 'YES'),
                         r1=sgn * (bl[j0] - lm(1000)), r5=sgn * (bl[j0] - lm(5000)), r30=sgn * (bl[j0] - lm(30000)), a5=abs(bl[j0] - lm(5000))))
    base['cov'] = 'ok'; rows.append(base)
R = pd.DataFrame(rows)
for _c in [c for c in R.columns if c.endswith('_f_q')]: R[_c].dropna().apply(E4.assert_sin_polvo)
g_ = okk.groupby('order_hash').agg(real_tm3=('tm3', 'min'), real_rama=('rama', 'first')); R = R.merge(g_, left_on='oid', right_index=True, how='left')
ftx = okk.groupby('order_hash').tx.apply(set); R['real_txs'] = R.oid.map(ftx)
R.to_pickle(OUT + f'{TAGP}_{d}.pkl'); pd.DataFrame(bins).to_pickle(OUT + f'HZ_{TAGP}_{d}.pkl')
json.dump(dict(dia=d, tag=TAGP, ex_alta=EXA, ex_canc=EXC, suelo_l2=SUELO, ramas_v3=BR, c_dia=c_dia, n_eventos=len(evA), n_bins=len(bins), bins_skip=nb_skip, t=round(time.time() - T0, 1)), open(OUT + f'{TAGP}_{d}.json', 'w'))
print('ok', d, 'ordenes', len(R), 'real fills', int(R.real_fill.sum()), 'BASE sim', int((R.get('BASE_f_q', pd.Series(dtype=float)) >= E4.FLOOR).sum()), 'bins', len(bins), nb_skip, round(time.time() - T0, 1), 's', flush=True)
