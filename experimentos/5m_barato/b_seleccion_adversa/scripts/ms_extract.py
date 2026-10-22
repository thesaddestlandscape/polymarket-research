#!/usr/bin/env python3
"""ms_extract.py DIA [DIA...] -- extrae del registro ms (retencion 4 d) lo necesario para medir spread / tamanos top / bid 15m / trades WS:
filas q (top del libro por cambio) y t (trades WS) de los tokens ETH/SOL/XRP 5min y 15min (mapa por filas k). Salida en datalogs/sa_ms/ms_DIA.npz
(fuera de git) + mapa de tokens. Lee con zcat|grep (tolera gzip truncado). Un fichero a la vez."""
import sys, os, glob, subprocess, io
import numpy as np, pandas as pd
DL = '/root/polymarket-research-datalogs/'; OUT = DL + 'sa_ms/'; os.makedirs(OUT, exist_ok=True)
COINS = tuple(os.environ.get('SA_COINS', 'ETH,SOL,XRP').upper().split(','))
def lines(f, pat):
    p = subprocess.Popen(f"zcat '{f}' 2>/dev/null | grep -E '{pat}'", shell=True, stdout=subprocess.PIPE)
    return p
def day(d):
    of = OUT + (os.environ.get('SA_TAG', '') + '_' if os.environ.get('SA_TAG') else '') + f'ms_{d}.npz'
    if os.path.exists(of): print(d, 'ya'); return
    fs = sorted(glob.glob(DL + f'maker_ms_{d}_*.csv.gz'))
    tm = {}
    from datetime import date, timedelta
    dprev = (date.fromisoformat(d) - timedelta(1)).isoformat()
    for f in sorted(glob.glob(DL + f'maker_ms_{dprev}_*.csv.gz')) + fs:   # mapa de tokens (filas k), incluye el dia anterior
        p = lines(f, '^k,')
        for ch in pd.read_csv(p.stdout, header=None, names=['tipo', 't', 'tok', 'act', 'marco', 'mid', 'fin', 'lado'], dtype=str, on_bad_lines='skip', chunksize=100000):
            ch = ch[ch.act.isin(COINS) & ch.marco.isin(['5min', '15min'])]
            for r in ch.itertuples(): tm[r.tok] = (r.act, r.marco, r.mid, r.fin, r.lado)
        p.wait()
    toks = sorted(tm); ti = {t: i for i, t in enumerate(toks)}
    finE = np.array([int(pd.Timestamp(tm[t][3]).timestamp() * 1000) for t in toks]); vida = np.array([330000 if tm[t][1] == '5min' else 1000000 for t in toks])
    LO = finE - vida; HI = finE + 10000
    Q = []; T = []; t0 = int(pd.Timestamp(d).timestamp() * 1000) - 3600000
    for f in fs:
        for kind, store in (('q', Q), ('t', T)):
            p = lines(f, f'^{kind},')
            names = ['tipo', 't', 'tok', 'c1', 'c2', 'c3', 'c4', 'c5']
            for ch in pd.read_csv(p.stdout, header=None, names=names, dtype={'tok': str, 'c1': str, 'c2': str, 'c3': str, 'c4': str, 'c5': str}, on_bad_lines='skip', chunksize=500000):
                ch = ch[ch.tok.isin(ti)]
                if not len(ch): continue
                kk = ch.tok.map(ti).values.astype(np.int64); tabs = ch.t.astype('int64').values; keep = (tabs >= LO[kk]) & (tabs <= HI[kk])
                if not keep.any(): continue
                ch = ch[keep]; k = kk[keep].astype(np.int16); t = (tabs[keep] - t0).astype(np.int64)
                if kind == 'q':
                    V = np.stack([pd.to_numeric(ch[c], errors='coerce').values.astype(np.float32) for c in ['c1', 'c2', 'c3', 'c4']], 1)
                    store.append((t, k, V))
                else:
                    V = np.stack([pd.to_numeric(ch.c1, errors='coerce').values, (ch.c2 == 'BUY').astype(float).values, pd.to_numeric(ch.c3, errors='coerce').values], 1).astype(np.float32)
                    store.append((t, k, V))
            p.wait()
        print(d, f.split('_')[-1], 'q', sum(len(x[0]) for x in Q), 't', sum(len(x[0]) for x in T), flush=True)
    def cat(L, nv):
        if not L: return np.zeros(0, np.int64), np.zeros(0, np.int16), np.zeros((0, nv), np.float32)
        t = np.concatenate([x[0] for x in L]); k = np.concatenate([x[1] for x in L])
        o = np.argsort(k.astype(np.int64) * 10**10 + t, kind='stable'); t = t[o]; k = k[o]
        V = np.empty((len(t), nv), np.float32); pos = 0; offs = np.cumsum([0] + [len(x[0]) for x in L])
        Vraw = np.concatenate([x[2] for x in L]); L.clear(); V = Vraw[o]; del Vraw, o
        return t, k, V
    qt, qk, qV = cat(Q, 4); tt, tk_, tV = cat(T, 3)
    np.savez_compressed(of, tokens=np.array(toks), tmap=np.array([tm[t] for t in toks]), t0=t0, q_t=qt, q_k=qk, **{'q_v%d' % j: qV[:, j] for j in range(4)}, t_t=tt, t_k=tk_, t_pr=tV[:, 0], t_sd=tV[:, 1], t_sz=tV[:, 2])
    print(d, 'tokens', len(toks), 'q', len(qt), 't', len(tt), 'guardado', of)
if __name__ == '__main__':
    for d in sys.argv[1:]: day(d)
