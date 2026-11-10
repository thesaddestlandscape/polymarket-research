#!/usr/bin/env python3
"""ADDENDUM2 de PREREG_DB1 (sec. 6, RMR): etiquetas de rafaga alternativas por dia. Criterio congelado antes: CRITERIO_PREVIO.txt
(sha 18310f5f61f380a0..., 2026-11-10T08:26Z). Solo lectura, 0 ordenes, solo dias quemados 20-Oct..08-Nov (rechaza D >= 2026-11-10).
Uso (nice -n 19 ionice -c3, ulimit -v 3000000): python3 -I add2_dia.py D [D ...] -> out/d_<D>.npz (idempotente por fichero).
Contenido por dia: unidades S_pop (bids de banda <=0,2049 de otros makers, ETH/SOL/XRP + BTC aparte), S_sim (G0 de RT emparejado a su tx
por tape) y S_real (rellenos de B), cada una con pnl, coste, estrato y etiqueta de cada regla (y su version P-temp)."""
import sys, os, json, numpy as np, pandas as pd, pyarrow.parquet as pq
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
V = '/mnt/HC_Volume_106538179/agentes_datos/diseccion_bots_b_09nov/'
PB = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/precursores_barrido/out/'
RTD = '/root/polymarket-research/experimentos/5m_barato/q11/toxicidad_thru1/out/'
BW = '0x659a40ff9920febc5a66836213040924343d297f'
CHAIN = {'0xe111180000d2663c0091e4f400237545b87b996b', '0x4bfb41d5b3570defd03c39a9a4d8de6bd8b8982e', '0xc5d563a36ae78145c45a50134d48a1215220f80a'}
BAND = 0.2049; SHIFT = 15; KM = 10000
BLOCK_RULES = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R10', 'R11']
MS_RULES = ['R0f', 'R8', 'R9']

def nuniq_by_key(key, val, mask):
    d = pd.DataFrame({'k': key[mask], 'v': val[mask]}).drop_duplicates()
    return d.groupby('k').size()

def lab_block(keys, S):
    """etiquetas de las reglas de bloque para un vector de claves de grupo (int64). S = tablas por grupo del dia."""
    def m(s): return pd.Series(keys).map(s).fillna(0).values
    n0, n1, n2, n3, nx, c2, sh = m(S['n0']), m(S['n1']), m(S['n2']), m(S['n3']), m(S['nx']), m(S['c2']), m(S['sh'])
    r0 = n0 >= 2
    return dict(R0=r0, R1=n1 >= 2, R2=n2 >= 2, R3=n3 >= 2, R4=n0 >= 3, R5=r0 & (c2 > 0), R7=nx >= 2, R11=r0 & (sh >= 100))

def ms_tables(D):
    """feat del dia: por orden (tx) -> etiquetas R0f/R8/R9 y sus P-temp (tau +-30 s, bloque +-15)."""
    F = pq.read_table(V + f'feat_{D}.parquet', columns=['tx', 'tw', 'mkt', 'tau_abs', 'bloque', 'ts', 'cierre']).to_pandas()
    F = F[F.tau_abs.notna()]; F['mkt'] = F.mkt.astype(str); F = F.drop_duplicates('tx').sort_values(['mkt', 'tau_abs']).reset_index(drop=True)
    mc = pd.factorize(F.mkt)[0].astype(np.int64); w = pd.factorize(F.tw)[0]; t = F.tau_abs.values.astype(np.float64)
    newrun = np.r_[True, (mc[1:] != mc[:-1]) | (w[1:] != w[:-1])]; rid = np.cumsum(newrun) - 1
    first = np.flatnonzero(newrun); last = np.r_[first[1:] - 1, len(t) - 1]; rm = mc[first]
    pl = np.r_[np.nan, t[last[:-1]]]; pok = np.r_[False, rm[1:] == rm[:-1]]
    nf = np.r_[t[first[1:]], np.nan]; nok = np.r_[rm[:-1] == rm[1:], False]
    dp = np.where(pok[rid], t - pl[rid], np.inf); dn = np.where(nok[rid], nf[rid] - t, np.inf)
    out = pd.DataFrame({'tx': F.tx.values})
    for W, nm in ((250, 'R8'), (1000, 'R9')): out[nm] = (dp <= W) | (dn <= W)
    # P-temp ms: >=2 tramos (=> >=2 tw distintos) en [t'-W, t'+W], t' = tau +-30 s, mismo mercado
    opn = (F.cierre.values.astype(np.float64) - 300) * 1000.0; sgn = np.where(t - opn < 150000, 1.0, -1.0); tp = t + sgn * SHIFT * 2000.0
    ti = F.tau_abs.values.astype(np.int64); ky = mc * 10**13 + ti; base = mc * 10**13; tpi = tp.astype(np.int64)
    for W, nm in ((250, 'R8'), (1000, 'R9')):
        lo = np.searchsorted(ky, base + tpi - W, 'left'); hi = np.searchsorted(ky, base + tpi + W, 'right')
        ok = hi > lo; out[nm + '_t'] = ok & (rid[np.maximum(hi - 1, 0)] - rid[np.minimum(lo, len(t) - 1)] >= 1)
    gk = F.bloque.values.astype(np.int64) * KM + mc
    n = nuniq_by_key(gk, w, np.ones(len(F), bool)); out['R0f'] = pd.Series(gk).map(n).fillna(0).values >= 2
    gks = (F.bloque.values.astype(np.int64) + np.where(sgn > 0, SHIFT, -SHIFT)) * KM + mc
    out['R0f_t'] = pd.Series(gks).map(n).fillna(0).values >= 2
    return out.set_index('tx')

def dia(D):
    if D >= '2026-11-10': raise SystemExit('PROHIBIDO: dias >= 2026-11-10')
    of = HERE + f'out/d_{D}.npz'
    if os.path.exists(of): print('ya', D); return
    os.makedirs(HERE + 'out', exist_ok=True)
    DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
    WC = json.load(open(V + 'wallet_cluster.json'))['wallet_cluster']; C2 = {k for k, v in WC.items() if v == 'C2'}
    bf = PB + f'bad_{D}.json'; bad = {int(h) for d_, h in json.load(open(bf))['bad'] if d_ == D} if os.path.exists(bf) else None
    cols = ['bloque', 'ts_est', 'tx', 'log_index', 'maker', 'coin', 'mkt', 'cierre', 'L', 'pc', 'acc', 'venta', 'taker']
    M = pq.read_table(V + f'mk_{D}.parquet', columns=cols).to_pandas()
    M = M[~M.taker.isin(CHAIN)].reset_index(drop=True)
    M['mkt'] = M.mkt.astype(str); M['coin'] = M.coin.astype(str); M['L'] = M.L.astype(str)
    mc = pd.factorize(M.mkt)[0].astype(np.int64); tk = pd.factorize(M.taker)[0]; txc = pd.factorize(M.tx)[0]; mkr = pd.factorize(M.maker)[0]
    key = M.bloque.values.astype(np.int64) * KM + mc
    pc = M.pc.values; vt = M.venta.values.astype(bool)
    A0 = (~vt) & (pc <= BAND); A1 = pc <= BAND; A2 = ~vt; A3 = np.ones(len(M), bool)
    isc2 = M.taker.isin(C2).values
    S = dict(n0=nuniq_by_key(key, tk, A0), n1=nuniq_by_key(key, tk, A1), n2=nuniq_by_key(key, tk, A2), n3=nuniq_by_key(key, tk, A3),
             nx=nuniq_by_key(key, txc, A0), c2=pd.Series(isc2[A0].astype(int)).groupby(key[A0]).max(), sh=pd.Series(M.acc.values[A0]).groupby(key[A0]).sum())
    sw = pd.DataFrame({'k': key[A0], 'x': txc[A0], 'm': mkr[A0]}).drop_duplicates().groupby(['k', 'x']).size()   # makers distintos por (grupo, orden)
    ml = pd.DataFrame({'k': key[A0], 't': tk[A0], 'li': M.log_index.values[A0]}).groupby(['k', 't']).li.min()   # 1o de la rafaga
    kmin = ml.groupby(level=0).min()
    res = M.mkt.map(DES); win = (M.L == res).values; hasres = res.notna().values
    pnl = M.acc.values * (win.astype(float) - pc); cost = M.acc.values * pc
    opn = M.cierre.values.astype(np.float64) - 300; rel = M.ts_est.values - opn
    minute = np.clip(np.floor(rel / 60.0), -1, 4).astype(np.int8); sgn = np.where(rel < 150, SHIFT, -SHIFT)
    hour = (np.floor(M.ts_est.values / 3600.0) % 24).astype(int); guard = np.ones(len(M), bool) if bad is None else ~np.isin(hour, list(bad))
    MS = ms_tables(D)
    def labels(idx, keys, keys_t):
        L0 = lab_block(keys, S); Lt = lab_block(keys_t, S)
        own = isc2[idx]; L0['R6'] = own; Lt['R6'] = own   # identidad: no depende del bloque (P-temp = mismo valor; se reporta asi)
        swn = pd.DataFrame({'k': keys, 'x': txc[idx]}).merge(sw.rename('n').reset_index(), on=['k', 'x'], how='left')['n'].fillna(0).values
        swt = np.zeros(len(idx), bool)   # P-temp de R10: solo la parte R0 desplazada (la orden propia no existe en el bloque desplazado)
        L0['R10'] = L0['R0'] | (swn >= 3); Lt['R10'] = Lt['R0'] | swt
        fr = pd.DataFrame({'k': keys, 't': tk[idx]}).merge(ml.rename('li').reset_index(), on=['k', 't'], how='left')['li'].values == pd.Series(keys).map(kmin).values
        txs = M.tx.values[idx]; ms = MS.reindex(txs)
        o = {}
        for r in BLOCK_RULES: o[r] = L0[r]; o[r + '_t'] = Lt[r]
        for r in MS_RULES:
            v = ms[r].values; o[r] = np.where(pd.isna(v), -1, v.astype(float)).astype(np.int8)
            vt_ = ms[r + '_t'].values; o[r + '_t'] = np.where(pd.isna(vt_), -1, vt_.astype(float)).astype(np.int8)
        o['first'] = fr
        return o
    pack = {}
    # ---- S_pop (ETH/SOL/XRP) y BTC aparte
    for nm, cm in (('pop', M.coin.isin(['ETH', 'SOL', 'XRP']).values), ('btc', (M.coin == 'BTC').values)):
        idx = np.flatnonzero(A0 & cm & (M.maker.values != BW) & hasres)
        lb = labels(idx, key[idx], (M.bloque.values[idx].astype(np.int64) + sgn[idx]) * KM + mc[idx])
        pack[nm + '_pnl'] = pnl[idx].astype(np.float32); pack[nm + '_cost'] = cost[idx].astype(np.float32)
        pack[nm + '_coin'] = pd.Categorical(M.coin.values[idx], categories=['BTC', 'ETH', 'SOL', 'XRP']).codes.astype(np.int8)
        pack[nm + '_tick'] = np.round(pc[idx] * 100).astype(np.int16); pack[nm + '_min'] = minute[idx]; pack[nm + '_guard'] = guard[idx]
        for r, v in lb.items(): pack[f'{nm}_{r}'] = np.asarray(v).astype(np.int8)
        pack[nm + '_ntot'] = np.array([int((A0 & cm & (M.maker.values != BW)).sum()), len(idx)])
    # ---- S_real (rellenos de B, todas las monedas)
    BF = pd.read_csv(V + 'b_fills_vida.csv', usecols=['tx', 'log_index', 'pnl', 'coste', 'mercado', 'fecha_utc'])
    BF = BF[BF.fecha_utc.str[:10] == D]
    kk = pd.Series(np.arange(len(M)), index=pd.MultiIndex.from_arrays([M.tx.values, M.log_index.values])); kk = kk[~kk.index.duplicated()]
    ridx = np.array([kk.get((a, int(b)), -1) for a, b in zip(BF.tx.values, BF.log_index.values)], dtype=np.int64)
    okr = ridx >= 0; ri = ridx[okr]
    if len(ri):
        lb = labels(ri, key[ri], (M.bloque.values[ri].astype(np.int64) + sgn[ri]) * KM + mc[ri])
        pack['real_pnl'] = BF.pnl.values[okr].astype(np.float32); pack['real_cost'] = BF.coste.values[okr].astype(np.float32)
        pack['real_coin'] = pd.Categorical(M.coin.values[ri], categories=['BTC', 'ETH', 'SOL', 'XRP']).codes.astype(np.int8)
        pack['real_tick'] = np.round(pc[ri] * 100).astype(np.int16); pack['real_guard'] = guard[ri]
        for r, v in lb.items(): pack[f'real_{r}'] = np.asarray(v).astype(np.int8)
    pack['real_ntot'] = np.array([len(BF), int(okr.sum())])
    # ---- S_sim (G0 de RT emparejado a su tx por tape)
    rtf = RTD + f'RT_{D}.pkl'; nsim = [0, 0]
    if os.path.exists(rtf):
        R = pd.read_pickle(rtf); R = R[R['var'] == 'G0'].reset_index(drop=True)
        tok = json.load(open(V + f'tok_{D}.json')); rev = {(v[0], int(v[3]), v[4]): k for k, v in tok.items() if v[1] == '5min'}
        R['tok'] = [rev.get((a, int(f), l)) for a, f, l in zip(R.act, R.fin, R.lado)]
        T = pd.read_pickle(PB + f'tape_{D}.pkl'); T = T[(T.side == 0) & T.token_id.isin(set(R.tok.dropna()))][['token_id', 'price', 't_ws_ms', 'tx', 'log_index']]
        T = T.sort_values(['token_id', 't_ws_ms']); grp = {k: g for k, g in T.groupby('token_id')}
        mi = []
        for tkn, L_, tf in zip(R.tok.values, R.L.values, R.tf.values):
            g = grp.get(tkn); j = -1
            if g is not None:
                tt = g.t_ws_ms.values; a = np.searchsorted(tt, tf, 'left'); b = np.searchsorted(tt, tf + 400, 'right')
                for q in range(a, b):
                    if g.price.values[q] <= L_ + 0.0049:
                        j = kk.get((g.tx.values[q], int(g.log_index.values[q])), -1); break
            mi.append(j)
        mi = np.array(mi, dtype=np.int64); oks = mi >= 0; si = mi[oks]; nsim = [len(R), int(oks.sum())]
        if len(si):
            rel_s = R.tf.values[oks] / 1000.0 - (R.fin.values[oks] - 300); sg = np.where(rel_s < 150, SHIFT, -SHIFT)
            lb = labels(si, key[si], (M.bloque.values[si].astype(np.int64) + sg) * KM + mc[si])
            pack['sim_pnl'] = R.pnl.values[oks].astype(np.float32); pack['sim_cost'] = R.cost.values[oks].astype(np.float32)
            pack['sim_coin'] = pd.Categorical(R.act.values[oks], categories=['BTC', 'ETH', 'SOL', 'XRP']).codes.astype(np.int8)
            pack['sim_tick'] = np.round(R.L.values[oks] * 100).astype(np.int16); pack['sim_guard'] = np.ones(int(oks.sum()), bool)
            for r, v in lb.items(): pack[f'sim_{r}'] = np.asarray(v).astype(np.int8)
    pack['sim_ntot'] = np.array(nsim)
    pack['meta'] = np.array([D, 'bad=' + ('NA' if bad is None else ','.join(map(str, sorted(bad)))), f'des_cov_pop={float(hasres[A0].mean()):.4f}'])
    tmp = of + '.tmp.npz'; np.savez_compressed(tmp, **pack); os.replace(tmp, of)
    print(D, 'pop', pack['pop_ntot'].tolist(), 'btc', pack['btc_ntot'].tolist(), 'real', pack['real_ntot'].tolist(), 'sim', nsim, pack['meta'][1:].tolist(), flush=True)

if __name__ == '__main__':
    for D in sys.argv[1:]: dia(D)
