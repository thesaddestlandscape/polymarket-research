#!/usr/bin/env python3
"""verif_v3.py DIA -- verif_real/verif.py (no se edita) con SELLO v3 (stamp_v3.py) y motor con/sin dedupe (engine_v3.fill_segment_v3), contra las ordenes REALES de B (ordenes_b.csv, ledger; 20-23 Oct). SOLO LECTURA, 0 ordenes.
RELOJ: sa_ms v1 solo tiene EXCHANGE (q_t y t_t). El 'print' de cada tx es el WS emparejado por tamano (t_m, EX, como verif.py); la fila de consumo se busca por firma EXACTA (token+precio+tamano TOTAL del tx, incluida nuestra
orden: nuestro tamano SI esta en la fila real del libro) en +-1,5 s EX; unica -> ex(fila)-1; ambigua/sin firma -> t_m - c_dia - 1 (c_dia = p50 de d_ex de las unicas del dia); sin emparejado WS (src=bloque) -> bloque-2,25 s -63 ms (legacy, contado).
Cinta = fills de OTROS makers (NUESTRA wallet excluida, como verif.py). Salida: verif_real/out_v3/V3_<D>.pkl, columnas <tag>_<VAR>_f_q/_tf, tag in {v2o (regla vieja + motor original: regresion de V_<D>.pkl), v3o (sello v3, motor original), v3d (sello v3 + dedupe)}, VAR in BASE/OPT."""
import sys, os, json, time, numpy as np, pandas as pd
T0 = time.time(); H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = H + 'verif_real/out_v3/'; os.makedirs(OUT, exist_ok=True); sys.path.insert(0, H)
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
sys.path.insert(0, P2 + 'escalera_B'); import engine as G
sys.path.insert(0, P2 + 'captura_prints'); import reconstructor_relleno as RR
import engine_v3 as E3, stamp_v3 as ST
DL = '/root/polymarket-research-datalogs/'; OWN = '0x659a40ff9920febc5a66836213040924343d297f'
d = sys.argv[1]
if os.path.exists(OUT + f'V3_{d}.pkl'): print('ya', d); sys.exit(0)
E = G.DayEng(d, 'ws'); D = E.D; tok5 = {t for t, m in zip(D.toks, D.marco) if m == '5min'}
ch = []
for c in pd.read_csv('/mnt/HC_Volume_106538179/keep_onchain_re_as_b/' + f'onchain_fills_{d}.csv.gz', usecols=['tipo', 'ts_est', 'tx', 'log_index', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt'],
                     dtype={'token_id': str, 'maker': str, 'taker': str, 'tx': str}, chunksize=400000):
    ch.append(c[c.token_id.isin(tok5)])
fills = RR.fills_makers(pd.concat(ch)); del ch; fills['maker'] = fills.maker.str.lower(); fills = fills[fills.side == 0].copy()
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
for tag, tmv, EV_ in (('v2o', tm2x, evX), ('v3', tm3, evA)):
    mm = EV_[['k', 'tx']].assign(tm=tmv)
    t2 = tp.merge(mm, on=['k', 'tx'], how='left'); t2['t_ws_ms'] = t2.tm.astype(np.int64)
    TAPES[tag] = G.Tape('chain', D, t2[['token_id', 'price', 'sh', 'side', 't_ws_ms', 'tx', 'log_index']])
# sello de NUESTRO propio relleno (para medir donde cae el relleno real respecto al simulado)
own_k = own.assign(k=own.token_id.map(D.tokidx)).merge(evA[['k', 'tx']].assign(tm3=tm3, tm2=tm2, rama=rama), on=['k', 'tx'], how='left')
own_k[['tx', 'token_id', 'ts_est', 'tm2', 'tm3', 'rama', 'sh', 'price']].to_pickle(OUT + f'own_{d}.pkl')

def qupd3(k, L, t0, t1):
    a, b = D.qb[k], D.qb[k + 1]; qt = D.qt[a:b]; i0 = np.searchsorted(qt, t0, side='right'); i1 = np.searchsorted(qt, t1, side='right'); s, e = a + i0, a + i1
    prev = np.full(e - s, np.nan)
    if e > s:
        j = np.arange(s, e) - 1; ok = j >= a; pv0 = np.where(ok, D.v0[np.maximum(j, 0)], np.nan); pv2 = np.where(ok, D.v2[np.maximum(j, 0)], np.nan)
        prev = np.where(ok & (np.abs(pv0.astype(float) - L) < G.EPS), pv2, np.nan)
    return qt[i0:i1], D.v0[s:e], D.v2[s:e], prev
def run(tape, k, L, t0, t1, size, var, dedupe):
    return E3.fill_segment_v3(D.book(k, t0), 0.0, qupd3(k, L, t0, t1) if var == 'BASE' else None, tape.get(k, L, t0, t1), L, t0, t1, size, var, dedupe=dedupe)
CONF = (('v2o', 'v2o', False), ('v3o', 'v3', False), ('v3d', 'v3', True))
O = pd.read_csv(DL + 'calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str}); O = O[O.dia == d]
rows = []
for r in O.itertuples():
    k = D.tokidx.get(str(r.tok)); base = dict(oid=r.oid, dia=d, coin=r.coin, L=round(float(r.precio), 2), size=float(r.size), t_ini=int(r.t_ini * 1000), t_fuera=int(r.t_fuera * 1000), t_fin=int(r.t_fin * 1000), T=r.T,
                                             real_fill=int(r.fill), real_q=float(r.acc_llena), gana=r.gana_lado, cola=r.cola, k=k)
    if k is None or D.marco[k] != '5min' or D.comp(k) is None: base.update(cov='sin_sa_ms'); rows.append(base); continue
    L = base['L']; ta = base['t_ini']
    for tag, tk, dd in CONF:
        for var in ('BASE', 'OPT'):
            q, tf, mot = run(TAPES[tk], k, L, ta, base['t_fuera'], base['size'], var, dd); base[f'{tag}_{var}_f_q'] = float(q); base[f'{tag}_{var}_f_tf'] = int(tf) if q > 1e-9 else -1
    base['cov'] = 'ok'; rows.append(base)
R = pd.DataFrame(rows); R.to_pickle(OUT + f'V3_{d}.pkl')
json.dump(dict(dia=d, cobertura_emparejado=cob, ramas_v3=BR, c_dia=c_dia, n_eventos=len(evA), t=round(time.time() - T0, 1)), open(OUT + f'V3_{d}.json', 'w'))
print('ok', d, 'ordenes', len(R), 'real fills', int(R.real_fill.sum()), {t: int((R.get(f'{t}_BASE_f_q', pd.Series(dtype=float)) > 1e-9).sum()) for t, _, _ in CONF}, round(time.time() - T0, 1), 's', flush=True)
