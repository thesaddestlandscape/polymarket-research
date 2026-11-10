#!/usr/bin/env python3
"""Verificacion motor passT (engine BASE, cinta chain, tf=print-63ms|caida L1) contra B REAL (ordenes_b.csv, 20-23 Oct). SOLO LECTURA, 0 ordenes.
ADAPTACION declarada: libro5_tx no existe antes del 24-Oct -> reloj 'tx_ws' sustituido por EMPAREJADO con el print WS de sa_ms (token o complementario, tamano = total del tx, ventana ts_bloque-4,5..-0,2 s);
si no hay emparejado -> bloque-2,25 s. Se EXCLUYEN de la cinta los fills de NUESTRA wallet (fuga). Uso: python3 -I verif.py DIA -> out/V_<D>.pkl"""
import sys, os, json, time, subprocess, collections, numpy as np, pandas as pd
T0 = time.time(); H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = H + 'out/'
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
sys.path.insert(0, P2 + 'escalera_B'); import engine as G
sys.path.insert(0, P2 + 'captura_prints'); import reconstructor_relleno as RR
DL = '/root/polymarket-research-datalogs/'; OWN = '0x659a40ff9920febc5a66836213040924343d297f'
d = sys.argv[1]
E = G.DayEng(d, 'ws'); D = E.D; tok5 = {t for t, m in zip(D.toks, D.marco) if m == '5min'}
ch = []
for c in pd.read_csv('/mnt/HC_Volume_106538179/keep_onchain_re_as_b/' + f'onchain_fills_{d}.csv.gz', usecols=['tipo', 'ts_est', 'tx', 'log_index', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt'],
                     dtype={'token_id': str, 'maker': str, 'taker': str, 'tx': str}, chunksize=400000):
    ch.append(c[c.token_id.isin(tok5)])
fills = RR.fills_makers(pd.concat(ch)); del ch; fills['maker'] = fills.maker.str.lower(); fills = fills[fills.side == 0].copy()
print('onchain makers side0', len(fills), 'own', int((fills.maker == OWN).sum()), round(time.time() - T0, 1), flush=True)
# ---- emparejado con prints WS (sa_ms)
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
tt_ = pd.to_datetime(fills.ts_est, unit='s', utc=True); cov = fills.assign(h=tt_.dt.hour, ok=(fills.src == 'ws_match')).groupby('h').ok.agg(['size', 'mean']).round(3)
print('cobertura emparejado', round(float((fills.src == 'ws_match').mean()), 4), 'horas<0.95:', cov[cov['mean'] < 0.95].index.tolist(), round(time.time() - T0, 1), flush=True)
fills[(fills.maker == OWN)][['tx', 'token_id', 'ts_est', 't_ws_ms', 'src', 'sh', 'price']].to_pickle(OUT + f'ownfills_{d}.pkl')
fills_x = fills[fills.maker != OWN]
# ---- tf = print-63 ms | caida L1 (passT, lineas identicas)
tp = fills_x.assign(k=fills_x.token_id.map(D.tokidx)); tp = tp[tp.k.notna()].copy(); tp['k'] = tp.k.astype(int)
ev = tp.groupby(['k', 'tx']).agg(t=('t_ws_ms', 'min'), pmin=('price', 'min')).reset_index()
tm = np.empty(len(ev), np.int64); evk = ev.k.values; evt = ev.t.values.astype(np.int64); evp = ev.pmin.values
for i in range(len(ev)):
    k = evk[i]; t = evt[i]; pm = evp[i]; a, b = D.qb[k], D.qb[k + 1]; qt = D.qt[a:b]; v0 = D.v0[a:b]
    i0 = np.searchsorted(qt, t - 400, side='left'); i1 = np.searchsorted(qt, t, side='right'); tm[i] = t - 63
    if i1 > i0 and i0 > 0:
        lo = v0[i0 - 1:i1] <= pm + G.TOLP; w = np.where(lo[1:] & ~lo[:-1])[0]
        if len(w): tm[i] = int(qt[i0 + w[0]])
ev['tm'] = tm; tp = tp.merge(ev[['k', 'tx', 'tm']], on=['k', 'tx'], how='left'); tp['t_ws_ms'] = tp.tm.astype(np.int64)
E.tape = G.Tape('chain', D, tp[['token_id', 'price', 'sh', 'side', 't_ws_ms', 'tx', 'log_index']])
print('tf: caida L1 en', round(float(((ev.tm - (ev.t - 63)) != 0).mean()), 3), 'de', len(ev), 'tx', round(time.time() - T0, 1), flush=True)
# ---- replay de las ordenes reales
O = pd.read_csv(DL + 'calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str}); O = O[O.dia == d]
BF = pd.read_csv(DL + 'calibracion_etiqueta/b_fills_onchain.csv', dtype={'token_id': str}); own_by = BF.groupby('order_hash').agg(ts_oc=('ts_est', 'min'), tx=('tx', 'first'), tok=('token_id', 'first'))
rows = []; TCH = E.tape; TWS = G.Tape('ws', D)
for r in O.itertuples():
    k = D.tokidx.get(str(r.tok)); base = dict(oid=r.oid, dia=d, coin=r.coin, L=round(float(r.precio), 2), size=float(r.size), t_ini=int(r.t_ini * 1000), t_fuera=int(r.t_fuera * 1000), t_fin=int(r.t_fin * 1000), T=r.T,
                                             real_fill=int(r.fill), real_q=float(r.acc_llena), gana=r.gana_lado, cola=r.cola, k=k)
    if k is None or D.marco[k] != '5min' or D.comp(k) is None: base.update(cov='sin_sa_ms'); rows.append(base); continue
    L = base['L']; ta = base['t_ini']
    for tag, te in (('f', base['t_fuera']), ('n', base['t_fin'])):
        for var in ('BASE', 'OPT', 'CONS'):
            q, tf, mot = E.run_segment(k, L, ta, te, base['size'], var); base[f'{var}_{tag}_q'] = float(q); base[f'{var}_{tag}_tf'] = int(tf) if q > 1e-9 else -1
    E.tape = TWS
    for var in ('BASE', 'OPT'):
        q, tf, mot = E.run_segment(k, L, ta, base['t_fuera'], base['size'], var); base[f'WS{var}_f_q'] = float(q); base[f'WS{var}_f_tf'] = int(tf) if q > 1e-9 else -1
    E.tape = TCH
    pr = D.prints(k, L, ta, base['t_fuera'] + 250); base['n_prints'] = len(pr)
    pc = [x for x in pr if x[3] == 1]; ps = [x for x in pr if x[3] == 0]
    base['t_comp'] = pc[0][0] if pc else -1; base['t_self'] = ps[0][0] if ps else -1
    base['t_prn_any'] = pr[0][0] if pr else -1
    if r.oid in own_by.index:
        o = own_by.loc[r.oid]; base['ts_oc'] = float(o.ts_oc); w = own_by_t = None
        m = fills[(fills.tx == o.tx) & (fills.token_id == o.tok)]; base['t_own_print'] = int(m.t_ws_ms.iloc[0]) if len(m) else -1; base['own_src'] = m.src.iloc[0] if len(m) else ''
    base['cov'] = 'ok'; base['qbook'] = D.book(k, ta) is not None; rows.append(base)
R = pd.DataFrame(rows); R.to_pickle(OUT + f'V_{d}.pkl')
print('ok', d, 'ordenes', len(R), 'cov', R['cov'].value_counts().to_dict(), 'real fills', int(R.real_fill.sum()), 'sim BASE fills (fuera)', int((R.get('BASE_f_q', pd.Series(dtype=float)) > 1e-9).sum()), round(time.time() - T0, 1), 's', flush=True)
