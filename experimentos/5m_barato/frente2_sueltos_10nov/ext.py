#!/usr/bin/env python3
"""FRENTE 2 sueltos (10-Nov, alpha-miner). EXPLORATORIO sobre dias QUEMADOS (26-Oct..04-Nov, 07-08 Nov). Solo lectura, 0 ordenes.
Por relleno G0 de q11/toxicidad_thru1/out/RT_D.pkl: etiqueta R0 (db1/addendum2/out/d_D.npz, alineada por secuencia),
rasgos ex ante del segmento (SEGT_D), libro top (sa_ms via capt.Day, reloj de recepcion) antes y DESPUES del relleno
(markouts y valor de salida al bid con fee tomador), retornos Binance (recepcion) y tamano de la orden tomadora (tape).
Los rasgos post-relleno SOLO se usan para reglas de salida (decision posterior al relleno); nunca para 'evitar'.
Uso: nice -n 19 ionice -c3 python3 -I ext.py D [D ...]  -> out/F_<D>.pkl (idempotente)."""
import sys, os, json, time, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
RTD = '/root/polymarket-research/experimentos/5m_barato/q11/toxicidad_thru1/out/'
A2 = '/root/polymarket-research/experimentos/5m_barato/db1/addendum2/out/'
PB = P2 + 'precursores_barrido/out/'
sys.path.insert(0, P2 + 'capturabilidad_A_R1ws'); import capt
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/q11/barrido_multi'); import bfeat
COIN = ['BTC', 'ETH', 'SOL', 'XRP']; TOLP = 0.0049; EXL = 250   # llegada de una orden tomadora: decision + ~68 ms red + ~145 ms taker delay
DTS = (-300, 250, 1000, 1250, 5000, 5250, 30000, 30250)

def load_x_lean(dias, t_from):   # = passT.load_x_lean (recepcion c[7])
    acc = {}
    for dd in dias:
        f = bfeat.xfile(dd)
        if not f: continue
        for ch in pd.read_csv(f, header=None, usecols=[2, 3, 7], names=['sym', 'px', 'recv'], dtype={'sym': 'category', 'px': 'float64', 'recv': 'int64'}, chunksize=1500000):
            ch = ch[ch.recv.values >= t_from]
            for sym, g_ in ch.groupby('sym', observed=True): acc.setdefault(str(sym)[:-4], []).append((g_.recv.values, g_.px.values))
    out = {}
    for sym, L_ in acc.items():
        t = np.concatenate([x[0] for x in L_]); o = np.argsort(t, kind='stable'); out[sym] = (t[o], np.concatenate([x[1] for x in L_])[o])
    return out

def dia(d):
    of = H + f'out/F_{d}.pkl'
    if os.path.exists(of): print('ya', d); return
    t0 = time.time()
    R = pd.read_pickle(RTD + f'RT_{d}.pkl'); R = R[R['var'] == 'G0'].reset_index(drop=True)
    S = pd.read_pickle(RTD + f'SEGT_{d}.pkl')
    # --- etiqueta R0 por alineacion de secuencia con el npz (sim_* en el orden de R[oks])
    z = np.load(A2 + f'd_{d}.npz', allow_pickle=True); n = len(z['sim_pnl']); j = 0
    lab = np.full(len(R), -1, np.int8); r0t = np.full(len(R), -1, np.int8); r4 = np.full(len(R), -1, np.int8); first = np.full(len(R), -1, np.int8)
    cc = pd.Categorical(R.act.values, categories=COIN).codes; tk = np.round(R.L.values * 100).astype(np.int16)
    for i in range(len(R)):
        if j < n and np.float32(R.pnl.values[i]) == z['sim_pnl'][j] and np.float32(R.cost.values[i]) == z['sim_cost'][j] and cc[i] == z['sim_coin'][j] and tk[i] == z['sim_tick'][j]:
            lab[i] = z['sim_R0'][j]; r0t[i] = z['sim_R0_t'][j]; r4[i] = z['sim_R4'][j]
            if 'sim_first' in z.files and len(z['sim_first']) == n: first[i] = z['sim_first'][j]
            j += 1
    assert j == n, (d, j, n)
    R['R0'] = lab; R['R0_t'] = r0t; R['R4'] = r4; R['first'] = first
    # --- rasgos ex ante del segmento
    S2 = S[['k', 'L', 'seg', 't_dec', 'bidL', 'r3', 'dbid3', 'ja3', 'vida_ms']].copy(); S2['L'] = S2.L.round(2)
    R['L'] = R.L.round(2); R = R.merge(S2, on=['k', 'L', 'seg', 't_dec'], how='left', validate='one_to_one')
    # --- libro top (recepcion)
    D = capt.Day(d)
    def qa(k, times):
        a, b = D.qb[k], D.qb[k + 1]; times = np.asarray(times, np.int64)
        if b <= a: return [np.full(len(times), np.nan)] * 5
        jj = np.searchsorted(D.qt[a:b], times, side='right') - 1; ok = jj >= 0; jj = np.where(ok, jj, 0) + a
        f = lambda v: np.where(ok, v[jj].astype(float), np.nan)
        return f(D.v0), f(D.v1), f(D.v2), f(D.v3), np.where(ok, D.qt[jj], -1)
    rows = []
    tape = pd.read_pickle(PB + f'tape_{d}.pkl'); tape = tape[tape.side == 0]
    tape['k'] = tape.token_id.map(D.tokidx); tape = tape[tape.k.notna()]; tape['k'] = tape.k.astype(int)
    TG = {k: g.sort_values('t_ws_ms') for k, g in tape.groupby('k')}
    TX = tape.groupby(['k', 'tx']).agg(shtx=('sh', 'sum'), nmk=('maker', 'nunique')).to_dict('index')
    day0 = int(pd.Timestamp(d, tz='UTC').timestamp()) * 1000
    XS = load_x_lean([(pd.Timestamp(d) - pd.Timedelta(days=1)).strftime('%Y-%m-%d'), d], day0 - 2 * 3600 * 1000)
    def bret(coin, ta, tb):   # retorno bps entre ultimo tick <=ta y ultimo <=tb (frescura 15 s en ambos)
        A_ = XS.get(coin)
        if A_ is None: return np.nan
        t, p = A_; ia = np.searchsorted(t, ta, side='right') - 1; ib = np.searchsorted(t, tb, side='right') - 1
        if ia < 0 or ib < 0 or t[ia] < ta - 15000 or t[ib] < tb - 15000: return np.nan
        return (p[ib] / p[ia] - 1) * 1e4
    for i, r in R.iterrows():
        k = int(r.k); L = float(r.L); tf = int(r.tf); fin = int(r.fin); sg = 1.0 if r.lado == 'YES' else -1.0; op = (fin - 300) * 1000
        rec = {}
        bb, aa, bs, as_, qt_ = qa(k, [tf + x for x in DTS])
        for x, b_, a_, s_ in zip(DTS, bb, aa, bs):
            nm = ('m' + str(abs(x))) if x < 0 else ('p' + str(x)); rec['bid_' + nm] = b_; rec['ask_' + nm] = a_; rec['bsz_' + nm] = s_
        bd, ad, _, _, _ = qa(k, [int(r.t_dec) - 300]); rec['bid_dec'] = bd[0]; rec['ask_dec'] = ad[0]
        bA, _, sA, _, _ = qa(k, [(fin - 30) * 1000, (fin - 30) * 1000 + EXL]); rec['bid_T30'] = bA[1]; rec['bsz_T30'] = sA[1]
        # 15m mismo lado
        f15 = int(np.ceil(fin / 900.0) * 900); k15 = D.t15.get((r.act, f15, r.lado))
        if k15 is not None:
            b15, _, _, _, _ = qa(k15, [int(r.t_dec) - 300, tf + 1000, tf + 5000]); rec['b15_dec'], rec['b15_p1000'], rec['b15_p5000'] = b15
        else: rec['b15_dec'] = rec['b15_p1000'] = rec['b15_p5000'] = np.nan
        # stop: primera cotizacion tras tf con bid <= L - s, dentro de W; salida al bid de t*+250
        a, b = D.qb[k], D.qb[k + 1]; qt = D.qt[a:b]; v0 = D.v0[a:b]
        i0 = np.searchsorted(qt, tf, side='right'); iend = np.searchsorted(qt, fin * 1000 - 5000, side='right')
        for s_ in (0.02, 0.03, 0.05):
            for W, wn in ((30000, '30'), (None, 'E')):
                i1 = iend if W is None else min(iend, np.searchsorted(qt, tf + W, side='right'))
                w = np.where(v0[i0:i1] <= L - s_ + 1e-9)[0]
                key = f'stop{int(s_ * 100)}_{wn}'
                if len(w):
                    ts_ = int(qt[i0 + w[0]]); be, _, se, _, _ = qa(k, [ts_ + EXL]); rec[key + '_t'] = ts_ - tf; rec[key + '_b'] = be[0]; rec[key + '_s'] = se[0]
                else: rec[key + '_t'] = np.nan; rec[key + '_b'] = np.nan; rec[key + '_s'] = np.nan
        # Binance (recepcion), firmado a favor del lado
        rec['bn_pre3'] = sg * bret(r.act, tf - 3000, tf); rec['bn_p1'] = sg * bret(r.act, tf, tf + 1000); rec['bn_p5'] = sg * bret(r.act, tf, tf + 5000)
        rec['bn_pre1h'] = sg * bret(r.act, op - 3600000, op); rec['bn_inwin'] = sg * bret(r.act, op, int(r.t_dec) - 300)
        # orden tomadora (tape crudo, mismo emparejamiento que add2: primer print en [tf, tf+400] con price <= L+TOLP)
        g = TG.get(k); rec['shtx'] = np.nan; rec['nmk'] = np.nan
        if g is not None:
            tt = g.t_ws_ms.values; ia = np.searchsorted(tt, tf, 'left'); ib = np.searchsorted(tt, tf + 400, 'right')
            for q_ in range(ia, ib):
                if g.price.values[q_] <= L + TOLP:
                    v = TX.get((k, g.tx.values[q_]));
                    if v: rec['shtx'] = v['shtx']; rec['nmk'] = v['nmk']
                    break
        rows.append(rec)
    F = pd.concat([R, pd.DataFrame(rows)], axis=1)
    F.to_pickle(of + '.tmp'); os.replace(of + '.tmp', of)
    print('ok', d, len(F), 'R0', int((F.R0 == 1).sum()), 'suelto', int((F.R0 == 0).sum()), 'sinlab', int((F.R0 < 0).sum()), round(time.time() - t0, 1), 's', flush=True)

if __name__ == '__main__':
    for d in sys.argv[1:]:
        if d >= '2026-11-10': raise SystemExit('PROHIBIDO dias >= 2026-11-10')
        dia(d)
