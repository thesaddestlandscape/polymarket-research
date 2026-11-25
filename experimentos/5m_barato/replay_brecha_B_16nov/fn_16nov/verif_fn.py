#!/usr/bin/env python3
# fn_16nov/verif_fn.py (FN_132, 16-Nov): COPIA de l2_carrera_10nov/verif_v4.py (sha 93f893c7..., NO editado) + variantes FN. SOLO LECTURA, 0 ordenes.
# Variantes (todas v3 sello + dedupe + engine_v4, BASE): v3d (= verif_v4, reproduccion EXACTA obligatoria), v3d_own (filas de libro en L y bsz inicial SIN nuestra
# propia cantidad viva: en forward no hay orden propia en el libro), v3d_comp (cinta + ventas del COMPLEMENTARIO por otros makers, precio YES-eq 1-p: la cinta WS del dry-run
# ya las incluye, la de validacion no), v3d_own_comp, v3d_gen5 (CONTRASTE no forward: restar 5 acciones a toda fila/bsz del segmento, sin mirar si estamos).
# VERSION v4 (16-Nov): copia de verif_v3.py con engine_v4 (relleno sin polvo, FLOOR=1e-3, funcion unica engine_v4.relleno/es_fill). Salida en out_v4/ (no pisa out_v3/). Original sin editar.
"""verif_v3.py DIA -- verif_real/verif.py (no se edita) con SELLO v3 (stamp_v3.py) y motor con/sin dedupe (engine_v3.fill_segment_v3), contra las ordenes REALES de B (ordenes_b.csv, ledger; 20-23 Oct). SOLO LECTURA, 0 ordenes.
RELOJ: sa_ms v1 solo tiene EXCHANGE (q_t y t_t). El 'print' de cada tx es el WS emparejado por tamano (t_m, EX, como verif.py); la fila de consumo se busca por firma EXACTA (token+precio+tamano TOTAL del tx, incluida nuestra
orden: nuestro tamano SI esta en la fila real del libro) en +-1,5 s EX; unica -> ex(fila)-1; ambigua/sin firma -> t_m - c_dia - 1 (c_dia = p50 de d_ex de las unicas del dia); sin emparejado WS (src=bloque) -> bloque-2,25 s -63 ms (legacy, contado).
Cinta = fills de OTROS makers (NUESTRA wallet excluida, como verif.py). Salida: verif_real/out_v4/V3_<D>.pkl, columnas <tag>_<VAR>_f_q/_tf, tag in {v2o (regla vieja + motor original: regresion de V_<D>.pkl), v3o (sello v3, motor original), v3d (sello v3 + dedupe)}, VAR in BASE/OPT."""
import sys, os, json, time, numpy as np, pandas as pd
T0 = time.time(); H = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/'; OUT = os.path.dirname(os.path.abspath(__file__)) + '/out/'; os.makedirs(OUT, exist_ok=True); sys.path.insert(0, H)
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
sys.path.insert(0, P2 + 'escalera_B'); import engine as G
sys.path.insert(0, P2 + 'captura_prints'); import reconstructor_relleno as RR
import engine_v4 as E4, stamp_v3 as ST
DL = '/root/polymarket-research-datalogs/'; OWN = '0x659a40ff9920febc5a66836213040924343d297f'
d = sys.argv[1]
if os.path.exists(OUT + f'V3_{d}.pkl'): print('ya', d); sys.exit(0)
E = G.DayEng(d, 'ws'); D = E.D; tok5 = {t for t, m in zip(D.toks, D.marco) if m == '5min'}
ch = []
for c in pd.read_csv('/mnt/HC_Volume_106538179/keep_onchain_re_as_b/' + f'onchain_fills_{d}.csv.gz', usecols=['tipo', 'ts_est', 'tx', 'log_index', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt'],
                     dtype={'token_id': str, 'maker': str, 'taker': str, 'tx': str}, chunksize=400000):
    ch.append(c[c.token_id.isin(tok5)])
fills = RR.fills_makers(pd.concat(ch)); del ch; fills['maker'] = fills.maker.str.lower(); ASKS = fills[(fills.side == 1) & (fills.maker != OWN)].copy(); fills = fills[fills.side == 0].copy()
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
# ---- FN: ventas de otros makers en el COMPLEMENTARIO -> fila equivalente en el token (precio 1-p, side 0); sello: print WS emparejado (k,0)/(comp,1) - c_dia - 1, si no bloque - 2250 - 63
ASKS['kc'] = ASKS.token_id.map(D.tokidx); ASKS = ASKS[ASKS.kc.notna()].copy(); ASKS['k'] = [D.comp(int(c)) for c in ASKS.kc.values]; ASKS = ASKS[ASKS.k.notna()].copy(); ASKS['k'] = ASKS.k.astype(int)
ASKS['token_id'] = [D.toks[k] for k in ASKS.k.values]; ASKS['price'] = 1.0 - ASKS.price; ASKS['side'] = 0
gA = ASKS.groupby(['tx', 'token_id']).agg(S=('sh', 'sum'), ts=('ts_est', 'min')).reset_index(); tmA = {}
for tx, tok, S, ts in zip(gA.tx.values, gA.token_id.values, gA.S.values, gA.ts.values):
    k = D.tokidx.get(tok); c0 = ts * 1000 - 2250; best = None
    for kk, sd in ((k, 0), (D.comp(k), 1)):
        if kk is None: continue
        tt, sz = prints_of(kk, sd); i0 = np.searchsorted(tt, ts * 1000 - 4500); i1 = np.searchsorted(tt, ts * 1000 - 200, side='right')
        for j in range(i0, i1):
            if abs(sz[j] - S) <= 0.02 and (best is None or abs(tt[j] - c0) < abs(best - c0)): best = int(tt[j])
    if best is not None: tmA[(tx, tok)] = best
ASKS['t_m'] = [tmA.get((a, b), -1) for a, b in zip(ASKS.tx.values, ASKS.token_id.values)]
print('asks complementario', len(ASKS), 'emparejadas WS', round(float((ASKS.t_m >= 0).mean()), 4) if len(ASKS) else None, flush=True)
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
TAPES = {}; C_DIA = int(c_dia) if c_dia is not None else 19
for tag, tmv, EV_ in (('v2o', tm2x, evX), ('v3', tm3, evA)):
    mm = EV_[['k', 'tx']].assign(tm=tmv)
    t2 = tp.merge(mm, on=['k', 'tx'], how='left'); t2['t_ws_ms'] = t2.tm.astype(np.int64)
    TAPES[tag] = G.Tape('chain', D, t2[['token_id', 'price', 'sh', 'side', 't_ws_ms', 'tx', 'log_index']])
    if tag == 'v3':
        a2 = ASKS.copy(); a2['t_ws_ms'] = np.where(a2.t_m >= 0, a2.t_m - C_DIA - 1, a2.ts_est * 1000 - 2250 - 63).astype(np.int64)
        TAPES['v3c'] = G.Tape('chain', D, pd.concat([t2[['token_id', 'price', 'sh', 'side', 't_ws_ms', 'tx', 'log_index']], a2[['token_id', 'price', 'sh', 'side', 't_ws_ms', 'tx', 'log_index']]], ignore_index=True))
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
A_ACK = 24
BFo = pd.read_csv(DL + 'calibracion_etiqueta/b_fills_onchain.csv', dtype={'token_id': str, 'tx': str}).drop_duplicates(['tx', 'log_index'])[['order_hash', 'tx', 'log_index']]
OWNF = own.merge(BFo, on=['tx', 'log_index'], how='left').merge(own_k[['tx', 'token_id', 'tm3']].drop_duplicates(['tx', 'token_id']), on=['tx', 'token_id'], how='left')
OWNF = {h: (g.tm3.fillna(g.ts_est * 1000 - 2250).values.astype(float), g.sh.values.astype(float)) for h, g in OWNF.groupby('order_hash')}
def run_mod(tape, k, L, t0, t1, size, oid, t_fuera, modo):
    qt, v0, v2, prev = qupd3(k, L, t0, t1); v2 = np.asarray(v2, float).copy(); prev = np.asarray(prev, float).copy(); qt = np.asarray(qt)
    bk = D.book(k, t0); a, b = D.qb[k], D.qb[k + 1]; jb = np.searchsorted(D.qt[a:b], t0, side='right') - 1; tb_row = int(D.qt[a + jb]) if jb >= 0 else -1
    w0, w1 = t0 - A_ACK, t_fuera - A_ACK
    ft, fs = OWNF.get(oid, (np.empty(0), np.empty(0)))
    def rem(t): return max(size - float(fs[ft < t].sum()), 0.0)
    for i in range(len(qt)):
        t = int(qt[i])
        if modo == 'gen5': sub = 5.0
        elif w0 <= t <= w1: sub = rem(t)
        else: sub = 0.0
        v2[i] = max(v2[i] - sub, 0.0)
        if np.isfinite(prev[i]): prev[i] = max(prev[i] - sub, 0.0)
    if bk is not None:
        sub0 = 5.0 if modo == 'gen5' else (rem(tb_row) if tb_row >= w0 else 0.0)
        bk = (bk[0], bk[1], max(bk[2] - sub0, 0.0), bk[3])
    return E4.fill_segment_v4(bk, 0.0, (qt, v0, v2, prev), tape.get(k, L, t0, t1), L, t0, t1, size, 'BASE', dedupe=True)
CONF = (('v3d', 'v3', True),)
MODS = (('v3d_own', 'v3', 'own'), ('v3d_comp', 'v3c', None), ('v3d_own_comp', 'v3c', 'own'), ('v3d_gen5', 'v3', 'gen5'))
O = pd.read_csv(DL + 'calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str}); O = O[O.dia == d]
rows = []
for r in O.itertuples():
    k = D.tokidx.get(str(r.tok)); base = dict(oid=r.oid, dia=d, coin=r.coin, L=round(float(r.precio), 2), size=float(r.size), t_ini=int(r.t_ini * 1000), t_fuera=int(r.t_fuera * 1000), t_fin=int(r.t_fin * 1000), T=r.T,
                                             real_fill=int(r.fill), real_q=float(r.acc_llena), gana=r.gana_lado, cola=r.cola, k=k)
    if k is None or D.marco[k] != '5min' or D.comp(k) is None: base.update(cov='sin_sa_ms'); rows.append(base); continue
    L = base['L']; ta = base['t_ini']
    for tag, tk, dd in CONF:
        for var in ('BASE',):
            q, tf, mot = run(TAPES[tk], k, L, ta, base['t_fuera'], base['size'], var, dd); base[f'{tag}_{var}_f_q'] = float(q); base[f'{tag}_{var}_f_tf'] = int(tf) if E4.es_fill(q) else -1
    for tag, tk, modo in MODS:
        if modo is None: q, tf, mot = run(TAPES[tk], k, L, ta, base['t_fuera'], base['size'], 'BASE', True)
        else: q, tf, mot = run_mod(TAPES[tk], k, L, ta, base['t_fuera'], base['size'], r.oid, base['t_fuera'], modo)
        base[f'{tag}_BASE_f_q'] = float(q); base[f'{tag}_BASE_f_tf'] = int(tf) if E4.es_fill(q) else -1
    base['cov'] = 'ok'; rows.append(base)
R = pd.DataFrame(rows)
for _c in [c for c in R.columns if c.endswith('_f_q')]: R[_c].dropna().apply(E4.assert_sin_polvo)      # ningun relleno 0<q<FLOOR
R.to_pickle(OUT + f'V3_{d}.pkl')
json.dump(dict(dia=d, cobertura_emparejado=cob, ramas_v3=BR, c_dia=c_dia, n_eventos=len(evA), t=round(time.time() - T0, 1)), open(OUT + f'V3_{d}.json', 'w'))
print('ok', d, 'ordenes', len(R), 'real fills', int(R.real_fill.sum()), {c: int((R[c] >= E4.FLOOR).sum()) for c in R.columns if c.endswith('_BASE_f_q')}, round(time.time() - T0, 1), 's', flush=True)
