#!/usr/bin/env python3
# ver_todos_17nov/v4_verif_dem.py: COPIA GENERADA de b_real_sim/verif_v5.py (17-Nov) + gancho dem_hook (cinta de demanda tomadora residual). verif_v5 NO se toca. sys.path del dir de este fichero.
# VERSION v5 (17-Nov, b_real_sim): verif_v4 con tiempos del CONTRATO v2. verif_v4 NO se toca. # (v4:): copia de verif_v3.py con engine_v4 (relleno sin polvo, FLOOR=1e-3, funcion unica engine_v4.relleno/es_fill). Salida en out_v4/ (no pisa out_v3/). Original sin editar.
"""verif_v3.py DIA -- verif_real/verif.py (no se edita) con SELLO v3 (stamp_v3.py) y motor con/sin dedupe (engine_v3.fill_segment_v3), contra las ordenes REALES de B (ordenes_b.csv, ledger; 20-23 Oct). SOLO LECTURA, 0 ordenes.
RELOJ: sa_ms v1 solo tiene EXCHANGE (q_t y t_t). El 'print' de cada tx es el WS emparejado por tamano (t_m, EX, como verif.py); la fila de consumo se busca por firma EXACTA (token+precio+tamano TOTAL del tx, incluida nuestra
orden: nuestro tamano SI esta en la fila real del libro) en +-1,5 s EX; unica -> ex(fila)-1; ambigua/sin firma -> t_m - c_dia - 1 (c_dia = p50 de d_ex de las unicas del dia); sin emparejado WS (src=bloque) -> bloque-2,25 s -63 ms (legacy, contado).
Cinta = fills de OTROS makers (NUESTRA wallet excluida, como verif.py). Salida: verif_real/out_v4/V3_<D>.pkl, columnas <tag>_<VAR>_f_q/_tf, tag in {v2o (regla vieja + motor original: regresion de V_<D>.pkl), v3o (sello v3, motor original), v3d (sello v3 + dedupe)}, VAR in BASE/OPT."""
import sys, os, json, time, numpy as np, pandas as pd
T0 = time.time(); H = os.path.dirname(os.path.abspath(__file__)) + '/'; HV = H; H = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/'; OUT = HV + 'out/'; os.makedirs(OUT, exist_ok=True); sys.path.insert(0, H); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# ---- v5: tiempos de la orden real segun CONTRATO v2 sec.2. ARR in {legacy (t_ini), call0 (t_call0+EX_ALTA), dec (t_dec+D_ALTA+EX_ALTA)}; CANC in {legacy (t_fuera), int (t_cancel_int+EX_CANC)}
ARR = os.environ.get('V5_ARR', 'call0'); CANC = os.environ.get('V5_CANC', 'int'); EXA = int(os.environ.get('B_EX_ALTA', 35)); EXC = int(os.environ.get('B_EX_CANC', 33)); DAL = int(os.environ.get('B_D_ALTA', 53)); DSEND = int(os.environ.get('V5_DSEND', 0))
TAGP = 'DEM_' + f'r3_{ARR}{DSEND}a{EXA}_{CANC}c{EXC}_{os.environ.get("V5_ENG", "v3d")}'
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
sys.path.insert(0, P2 + 'escalera_B'); import engine as G
sys.path.insert(0, P2 + 'captura_prints'); import reconstructor_relleno as RR
import engine_v4 as E4, stamp_v3 as ST
DL = '/root/polymarket-research-datalogs/'; OWN = '0x659a40ff9920febc5a66836213040924343d297f'
d = sys.argv[1]
if os.path.exists(OUT + f'V5_{TAGP}_{d}.pkl'): print('ya', TAGP, d); sys.exit(0)
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
import dem_hook as DH
DEM = DH.construir(D, RAW, FM_ALL, evA, tm3, OWN, d, OUT)
CONF = (('v3d', 'v3', True),)
O = pd.read_csv(DL + 'calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str}); O = O[O.dia == d]
rows = []
for r in O.itertuples():
    k = D.tokidx.get(str(r.tok)); base = dict(oid=r.oid, dia=d, coin=r.coin, L=round(float(r.precio), 2), size=float(r.size), t_ini=int(r.t_ini * 1000), t_fuera=int(r.t_fuera * 1000), t_fin=int(r.t_fin * 1000), T=r.T,
                                             real_fill=int(r.fill), real_q=float(r.acc_llena), gana=r.gana_lado, cola=r.cola, k=k)
    if k is None or D.marco[k] != '5min' or D.comp(k) is None: base.update(cov='sin_sa_ms'); rows.append(base); continue
    L = base['L']; tcall0 = int(round(r.t_call0 * 1000)); tdec = int(round(r.t_dec * 1000)); tci = None if pd.isna(r.t_cancel_int) else int(round(r.t_cancel_int * 1000)); cie = int(r.cie)
    ta = {'legacy': base['t_ini'], 'call0': tcall0 + DSEND + EXA, 'dec': tdec + DAL + EXA}[ARR]
    # fin de la orden: legacy = t_fuera (1a observacion fuera de libro). 'int' = cancelacion enviada en t_cancel_int + EXC. Ordenes SIN cancelacion (58, todas con relleno completo): NO se usa t_fuera (=hora del relleno, circular): viven hasta T_STOP (60 s) + EXC
    te = base['t_fuera'] if CANC == 'legacy' else (tci + EXC if tci is not None else (cie - 60) * 1000 + EXC)
    te = max(te, ta + 1); base.update(t_arr=ta, t_end=te, sin_cancel=int(tci is None), t_call0=tcall0, t_dec=tdec, t_cancel_int=tci)
    for tag, tk, dd in CONF:
        for var in ('BASE', 'OPT'):
            q, tf, mot = run(TAPES[tk], k, L, ta, te, base['size'], var, dd); base[f'{tag}_{var}_f_q'] = float(q); base[f'{tag}_{var}_f_tf'] = int(tf) if E4.es_fill(q) else -1; base[f'{tag}_{var}_mot'] = mot
    if DEM is not None: base.update(DH.variantes(DEM, D, k, L, ta, te, base['size'], TAPES['v3'], qupd3, E4, cola=float(r.cola) if np.isfinite(r.cola) else np.nan))
    # diagnostico FN (solo se mira DESPUES, nunca decide): estado del libro a la llegada y prints propios/ajenos en la ventana
    bk = D.book(k, ta); base['bk_bid'] = float(bk[0]) if bk is not None else np.nan; base['bk_ask'] = float(bk[1]) if bk is not None else np.nan; base['bk_bsz'] = float(bk[2]) if bk is not None else np.nan
    pt_, pp_, ps_ = TAPES['v3'].get(k, L, ta, te); base['n_pr'] = int(len(pt_)); base['sz_pr_eqL'] = float(ps_[np.abs(pp_ - L) <= G.TOLP].sum()); base['n_pr_bajo'] = int((pp_ < L - G.TOLP).sum())
    pt2, pp2, ps2 = TAPES['v3'].get(k, L, ta - 5000, te + 5000); base['n_pr_wide'] = int(len(pt2))
    base['cov'] = 'ok'; rows.append(base)
R = pd.DataFrame(rows)
for _c in [c for c in R.columns if c.endswith('_f_q')]: R[_c].dropna().apply(E4.assert_sin_polvo)      # ningun relleno 0<q<FLOOR
# fills reales por orden (tm3 propio) -> columnas real_tm3 (primer relleno), real_tx_ajeno (el tx tiene prints de OTROS makers en la cinta)
bf = pd.read_csv(DL + 'calibracion_etiqueta/b_fills_onchain.csv', usecols=['tx', 'token_id', 'order_hash'], dtype={'token_id': str, 'tx': str}).drop_duplicates()
ok_ = own_k.merge(bf, on=['tx', 'token_id'], how='left'); ajeno = set(zip(tp.tx.values, tp.token_id.astype(str).values)); ok_['ajeno'] = [(a, b) in ajeno for a, b in zip(ok_.tx, ok_.token_id.astype(str))]
minp = tp.assign(token_id=tp.token_id.astype(str)).groupby(['tx', 'token_id']).price.min(); ok_['ajenoL'] = [(a_, b_) in minp.index and float(minp[(a_, b_)]) <= float(p_) + G.TOLP for a_, b_, p_ in zip(ok_.tx, ok_.token_id.astype(str), ok_.price)]
g_ = ok_.dropna(subset=['order_hash']).groupby('order_hash').agg(real_tm3=('tm3', 'min'), real_rama=('rama', 'first'), real_ajeno=('ajeno', 'max'), real_ajenoL=('ajenoL', 'max'), real_n_tx=('tx', 'nunique'))
R = R.merge(g_, left_on='oid', right_index=True, how='left')
def _bpre(r):
    if not np.isfinite(r.real_tm3) or r.k is None or (isinstance(r.k, float) and np.isnan(r.k)): return np.nan
    bk_ = D.book(int(r.k), int(r.real_tm3) - 63); return float(bk_[0]) if bk_ is not None else np.nan
R['real_bid_pre'] = [_bpre(r) for r in R.itertuples()]    # bid del libro (EX, sa_ms v1) en t_pre = tm3 - 63 ms: SOLO diagnostico de clase (tipo B ex post: bid_pre >= L + 0,0099); nunca decide
R.to_pickle(OUT + f'V5_{TAGP}_{d}.pkl')
json.dump(dict(dia=d, tag=TAGP, arr=ARR, canc=CANC, ex_alta=EXA, ex_canc=EXC, d_send=DSEND, cobertura_emparejado=cob, ramas_v3=BR, c_dia=c_dia, n_eventos=len(evA), t=round(time.time() - T0, 1)), open(OUT + f'V5_{TAGP}_{d}.json', 'w'))
print('ok', d, 'ordenes', len(R), 'real fills', int(R.real_fill.sum()), {t: int((R.get(f'{t}_BASE_f_q', pd.Series(dtype=float)) >= E4.FLOOR).sum()) for t, _, _ in CONF}, round(time.time() - T0, 1), 's', flush=True)
