#!/usr/bin/env python3
"""sim.py -- PREREG.md (sha en PREREG.sha256). Pujas propias simuladas con la regla de relleno v2 (v2lib.lleno). Salida arms_D.parquet. Reanudable por dia. Solo lectura de datos."""
import os, sys, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__))
assert hashlib.sha256(open(AQ + '/PREREG.md', 'rb').read()).hexdigest() == open(AQ + '/PREREG.sha256').read().split()[0]
sys.path.insert(0, AQ + '/../calibracion_etiqueta/v2'); from v2lib import lleno
DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/'; OUT = AQ + '/datos/'; os.makedirs(OUT, exist_ok=True)
S = 5.0; E_MS = 250; G = 0.5; LAT = 70
def leeq(D, keep):
    out = []
    for ch in pd.read_csv(DL + f'q_{D}.gz', header=None, names=['id','r','b','a','tb','ta'], chunksize=2_000_000,
                          dtype={'id': np.int64, 'r': np.int64, 'b': np.float32, 'a': np.float32, 'tb': np.float32, 'ta': np.float32}, on_bad_lines='skip'):
        out.append(ch[ch.id.isin(keep)].dropna())
    return pd.concat(out, ignore_index=True)
VAR = [('bb_f0', 0.0, 0.0), ('bb_f1', 0.0, 1.0), ('c1_f0', 0.01, 0.0)]
def dia(D):
    P = pd.read_pickle(DL + f'r_{D}.pkl')[['dia','coin','tid','r','q','acc','gana','fin']]
    P = P[P.tid >= 0].sort_values(['tid','r']).reset_index(drop=True)
    dd = (P.groupby('tid').r.diff() <= 300) & (P.groupby('tid').acc.diff().abs() < 1e-6); ndup = int(dd.sum()); P = P[~dd.values].reset_index(drop=True)
    keep = set(P.tid.unique().tolist()); Q = leeq(D, keep)
    o = np.lexsort((Q.ta.values, Q.tb.values, Q.a.values, Q.b.values, Q.r.values, Q.id.values)); Q = Q.iloc[o]
    Q = Q[~Q.duplicated().values]; ids = Q.id.values; R = Q.r.values; B = Q.b.values.astype(float); A = Q.a.values.astype(float); TB = Q.tb.values.astype(float); TA = Q.ta.values.astype(float)
    pi = P.tid.values; meta = P.groupby('tid').agg(coin=('coin','first'), fin=('fin','first'), gana=('gana','first'))
    rows = []
    for L_MS in (10000, 3000):
        cols = {k: [] for k in ['tid','coin','t','F5','L'] + [f'{v[0]}_{x}' for v in VAR for x in ('acc','pnl','cost')]}
        for tk in np.unique(ids):
            a0, a1 = np.searchsorted(ids, [tk, tk + 1]); p0, p1 = np.searchsorted(pi, [tk, tk + 1])
            if p1 == p0: continue
            r = R[a0:a1]; b = B[a0:a1]; a = A[a0:a1]; tb = TB[a0:a1]; ta = TA[a0:a1]; n = len(r)
            fin = float(meta.fin.loc[tk]) * 1000; gana = float(meta.gana.loc[tk]); coin = meta.coin.loc[tk]
            pr = P.r.values[p0:p1]; pq = P.q.values[p0:p1]; pa = P.acc.values[p0:p1]
            ch = np.flatnonzero(b[1:] != b[:-1]) + 1          # indices donde cambia el bid
            done = {v[0]: False for v in VAR}; i = 0
            while i < n:
                t = r[i]
                if not (b[i] < a[i] and 0.10 < b[i] <= 0.30 + 1e-9 and 1500 <= fin - t <= 300000): i += 1; continue
                k = np.searchsorted(ch, i, 'right'); nx = r[ch[k]] if k < len(ch) else np.inf
                te = min(nx, t + L_MS, fin - 1500); ti = t + LAT
                rec = {'tid': tk, 'coin': coin, 't': t, 'F5': np.log1p(ta[i]), 'L': L_MS}
                for nm, sh, f in VAR:
                    pp = round(b[i] - sh, 2)
                    if done[nm] or pp <= 0.10 + 1e-9 or te <= ti: rec[nm + '_acc'] = rec[nm + '_pnl'] = rec[nm + '_cost'] = 0.0; continue
                    m = (pr >= ti) & (pr <= te + E_MS) & (pq <= pp + 1e-9)
                    cons = [(float(x), float(y), False) for x, y in zip(pr[m], pa[m])]
                    fl = lleno(cons, ti, te, E_MS, f, G, S, float(tb[i]))
                    if fl is None: rec[nm + '_acc'] = rec[nm + '_pnl'] = rec[nm + '_cost'] = 0.0
                    else:
                        acc = min(S, float(pa[m].sum())); rec[nm + '_acc'] = acc; rec[nm + '_cost'] = pp * acc; rec[nm + '_pnl'] = acc * (gana - pp); done[nm] = True
                for kk, vv in rec.items(): cols[kk].append(vv)
                i = int(np.searchsorted(r, max(te, t + 2000), 'left'))
        df = pd.DataFrame(cols); df['dia'] = D; rows.append(df)
    df = pd.concat(rows, ignore_index=True); df['hora'] = ((df.t // 3600000) % 24).astype(int); df['band'] = df.hora // 6
    df.to_parquet(OUT + f'arms_{D}.parquet'); 
    s = {v[0]: (int((df[v[0]+'_cost'] > 0).sum()), round(float(df[v[0]+'_pnl'].sum()/max(df[v[0]+'_cost'].sum(),1e-9)), 4)) for v in VAR}
    print(D, 'prints', len(P), 'dup', ndup, 'tokens', len(keep), 'arms', len(df), 'fills,EV', s, flush=True)
for d in range(6, 24):
    D = f'2026-10-{d:02d}'
    if os.path.exists(OUT + f'arms_{D}.parquet') or not os.path.exists(DL + f'q_{D}.gz'): continue
    dia(D)
