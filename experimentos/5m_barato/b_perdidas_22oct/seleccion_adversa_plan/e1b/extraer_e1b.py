#!/usr/bin/env python3
"""extraer_e1b.py DIA -- COPIA de ../../salida/scripts/extraer.py (sin tocar el original) que ADEMAS guarda el desfase recepcion-tev (arrays qd, td, int32 ms)
para A4 del ADDENDUM_E1b. Los demas arrays son identicos a los de extraer.py (test). ORIGINAL: ETH/SOL/XRP 5m+15m: filas q (top) y t (operaciones WS) con hora de RECEPCION, y aggTrade Binance (x, recepcion c[7]).
Fuente: VOL/m5_registro + VOL/m15_registro (17-21 Oct) o registro ms crudo (22-Oct). Salida datos/ms_DIA.npz. Solo lectura de produccion."""
import sys, os, glob, subprocess
import numpy as np, pandas as pd
VOL = '/mnt/HC_Volume_106538179/'; DL = '/root/polymarket-research-datalogs/'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
COINS = ('ETH', 'SOL', 'XRP'); SYMS = ('ETHUSDT', 'SOLUSDT', 'XRPUSDT')
def pipe(files, pat):
    fl = ' '.join(f"'{f}'" for f in files)
    return subprocess.Popen(f"for f in {fl}; do zcat \"$f\" 2>/dev/null; done | grep -E '{pat}'", shell=True, stdout=subprocess.PIPE)
def day(d):
    of = os.path.join(OUT, f'ms_{d}.npz')
    if os.path.exists(of): print(d, 'ya'); return
    a = VOL + f'm5_registro/m5_registro_{d}.csv.gz'; b = VOL + f'm15_registro/m15_registro_{d}.csv.gz'
    if os.path.exists(a) and os.path.exists(b): fq = [a, b]; fx = [a]
    else: fq = sorted(glob.glob(DL + f'maker_ms_{d}_*.csv.gz')); fx = fq
    print(d, 'fuentes', fq, flush=True)
    tm = {}
    p = pipe(fq, '^k,')
    for ch in pd.read_csv(p.stdout, header=None, names=['tipo', 't', 'tok', 'act', 'marco', 'mid', 'fin', 'lado'], dtype=str, on_bad_lines='skip', chunksize=200000):
        ch = ch[ch.act.isin(COINS) & ch.marco.isin(['5min', '15min'])]
        for r in ch.itertuples(): tm[r.tok] = (r.act, r.marco, r.mid, r.fin, r.lado)
    p.wait()
    toks = sorted(tm); ti = {t: i for i, t in enumerate(toks)}
    is15 = np.array([tm[t][1] == '15min' for t in toks])
    Q = []; T = []; D0 = int(pd.Timestamp(d, tz='UTC').timestamp() * 1000) - 3600000
    names = ['tipo', 'tev', 'tok', 'c1', 'c2', 'c3', 'c4', 'c5']
    p = pipe(fq, '^(q|t),')
    for ch in pd.read_csv(p.stdout, header=None, names=names, dtype=str, on_bad_lines='skip', chunksize=500000):
        ch = ch[ch.tok.isin(ti)]
        if not len(ch): continue
        q = ch[ch.tipo == 'q']; t = ch[ch.tipo == 't']
        if len(q):
            rr = pd.to_numeric(q.c5, errors='coerce').fillna(0).values.astype(np.int64) - D0
            kk = q.tok.map(ti).values.astype(np.int16)
            vv = np.stack([pd.to_numeric(q[c], errors='coerce').values for c in ('c1', 'c2', 'c3', 'c4')] + [pd.to_numeric(q.c5, errors='coerce').fillna(0).values - pd.to_numeric(q.tev, errors='coerce').fillna(0).values], 1).astype(np.float32)   # col 5 = recepcion - tev (ms)
            # 15m: solo filas donde cambia el bid (o hueco >60 s respecto a la fila previa del mismo token)
            es15 = is15[kk]
            if es15.any():
                df = pd.DataFrame({'k': kk, 'r': rr, 'b': vv[:, 0]})
                pk = df.groupby('k').b.shift(); pr = df.groupby('k').r.shift()
                keep = ~es15 | pk.isna().values | (pk.values != vv[:, 0]) | (np.abs(rr - pr.fillna(0).values) > 60000)
                rr, kk, vv = rr[keep], kk[keep], vv[keep]
            Q.append((rr.astype(np.int32), kk, vv))
        if len(t):   # t,tev,tok,price,side,size,recv
            T.append((pd.to_numeric(t.c4, errors='coerce').fillna(0).values.astype(np.int64) - D0, t.tok.map(ti).values.astype(np.int16),
                      np.stack([pd.to_numeric(t.c1, errors='coerce').values, (t.c2 == 'BUY').astype(float).values, pd.to_numeric(t.c3, errors='coerce').values,
                                pd.to_numeric(t.c4, errors='coerce').fillna(0).values - pd.to_numeric(t.tev, errors='coerce').fillna(0).values], 1).astype(np.float32)))
    p.wait()
    X = []
    p = pipe(fx, '^x,[0-9]+,(ETH|SOL|XRP)USDT,')
    for ch in pd.read_csv(p.stdout, header=None, names=['tipo', 'T', 's', 'p', 'q', 'm', 'E', 'rx'], dtype={'s': str}, on_bad_lines='skip', chunksize=500000):
        ch = ch[ch.s.isin(SYMS)]
        if len(ch): X.append((pd.to_numeric(ch.rx, errors='coerce').fillna(0).values.astype(np.int64) - D0, ch.s.map({s: i for i, s in enumerate(SYMS)}).values.astype(np.int16), pd.to_numeric(ch.p, errors='coerce').values.astype(np.float64)))
    p.wait()
    def cat(L, nv):
        if not L: return np.zeros(0, np.int64), np.zeros(0, np.int16), np.zeros((0, nv), np.float32)
        r = np.concatenate([x[0] for x in L]).astype(np.int32); k = np.concatenate([x[1] for x in L])
        o = np.lexsort((r, k)); r = r[o]; k = k[o]
        v = np.concatenate([x[2] for x in L]); L.clear(); v = v[o]; del o
        return r, k, v
    qr, qk, qv = cat(Q, 5); tr, tk, tv = cat(T, 4); xr, xk, xv = cat(X, 1)
    qd = qv[:, 4].astype(np.int32); qv = qv[:, :4]; td = tv[:, 3].astype(np.int32); tv = tv[:, :3]
    np.savez_compressed(of, tokens=np.array(toks), tmap=np.array([tm[t] for t in toks]), D0=D0, qr=qr, qk=qk, qv=qv, qd=qd, tr=tr, tk=tk, tv=tv, td=td, xr=xr, xk=xk, xv=xv)
    print(d, 'tokens', len(toks), 'q', len(qr), 't', len(tr), 'x', len(xr), '->', of, flush=True)
if __name__ == '__main__':
    for d in sys.argv[1:]: day(d)
