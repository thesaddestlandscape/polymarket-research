#!/usr/bin/env python3
"""[COPIA LOWMEM A3_guarda 02-Nov: mismo formato de salida; parciales ordenados por fichero en disco y fusion por rangos de k, para BTC que superaba 3 GB] ms_extract.py DIA [DIA...] -- extrae del registro ms (retencion 4 d) lo necesario para medir spread / tamanos top / bid 15m / trades WS:
filas q (top del libro por cambio) y t (trades WS) de los tokens ETH/SOL/XRP 5min y 15min (mapa por filas k). Salida en datalogs/sa_ms/ms_DIA.npz
(fuera de git) + mapa de tokens. Lee con zcat|grep (tolera gzip truncado). Un fichero a la vez."""
import sys, os, glob, subprocess, io
import numpy as np, pandas as pd
DL = '/root/polymarket-research-datalogs/'; OUT = DL + 'sa_ms/'; TMP = '/mnt/HC_Volume_106538179/tmp_btc_extract/'; os.makedirs(TMP, exist_ok=True); os.makedirs(OUT, exist_ok=True)
COINS = tuple(os.environ.get('SA_COINS', 'ETH,SOL,XRP').upper().split(','))
def lines(f, pat):
    p = subprocess.Popen(f"zcat '{f}' 2>/dev/null | grep -E '{pat}'", shell=True, stdout=subprocess.PIPE)
    return p
TAGP = os.environ.get('SA_TAG', 'x') + '_'
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
    import shutil
    def key(t, k): return k.astype(np.int64) * 10**10 + t
    parts = {'q': [], 't': []}
    for fi, f in enumerate(fs):
        for kind, nv in (('q', 4), ('t', 3)):
            p = lines(f, f'^{kind},'); L = []
            names = ['tipo', 't', 'tok', 'c1', 'c2', 'c3', 'c4', 'c5']
            for ch in pd.read_csv(p.stdout, header=None, names=names, dtype={'tok': str, 'c1': str, 'c2': str, 'c3': str, 'c4': str, 'c5': str}, on_bad_lines='skip', chunksize=500000):
                ch = ch[ch.tok.isin(ti)]
                if not len(ch): continue
                kk = ch.tok.map(ti).values.astype(np.int64); tabs = ch.t.astype('int64').values; keep = (tabs >= LO[kk]) & (tabs <= HI[kk])
                if not keep.any(): continue
                ch = ch[keep]; k = kk[keep].astype(np.int16); t = (tabs[keep] - t0).astype(np.int64)
                if kind == 'q': V = np.stack([pd.to_numeric(ch[c], errors='coerce').values.astype(np.float32) for c in ['c1', 'c2', 'c3', 'c4']], 1)
                else: V = np.stack([pd.to_numeric(ch.c1, errors='coerce').values, (ch.c2 == 'BUY').astype(float).values, pd.to_numeric(ch.c3, errors='coerce').values], 1).astype(np.float32)
                L.append((t, k, V))
            p.wait()
            if L:
                t = np.concatenate([x[0] for x in L]); k = np.concatenate([x[1] for x in L]); V = np.concatenate([x[2] for x in L]); L.clear()
                o = np.argsort(key(t, k), kind='stable'); t = t[o]; k = k[o]; V = V[o]; del o
                for nm, a in (('t', t), ('k', k), ('V', V)): np.save(TMP + f'{TAGP}{d}_{kind}_{fi}_{nm}.npy', a)
                parts[kind].append(fi); print(d, f.split('_')[-1], kind, len(t), flush=True); del t, k, V
    def merge(kind, nv):
        fl = parts[kind]
        if not fl: return np.zeros(0, np.int64), np.zeros(0, np.int16), [np.zeros(0, np.float32) for _ in range(nv)]
        ks = [np.load(TMP + f'{TAGP}{d}_{kind}_{fi}_k.npy') for fi in fl]
        cnt = sum(np.bincount(np.asarray(k).astype(np.int64), minlength=len(toks)) for k in ks); N = int(cnt.sum())
        qt = np.empty(N, np.int64); qk = np.empty(N, np.int16); qv = [np.empty(N, np.float32) for _ in range(nv)]
        cum = np.concatenate([[0], np.cumsum(cnt)]); k0 = 0; pos = 0
        while k0 < len(toks):
            k1 = k0 + 1
            while k1 < len(toks) and cum[k1 + 1] - cum[k0] <= 3_000_000: k1 += 1
            T_ = []; K_ = []; V_ = []
            for fi, k in zip(fl, ks):
                a = np.searchsorted(k, k0, side='left'); b = np.searchsorted(k, k1, side='left')
                if b > a:
                    mt = np.load(TMP + f'{TAGP}{d}_{kind}_{fi}_t.npy', mmap_mode='r'); T_.append(np.array(mt[a:b])); del mt
                    K_.append(np.asarray(k[a:b])); mv = np.load(TMP + f'{TAGP}{d}_{kind}_{fi}_V.npy', mmap_mode='r'); V_.append(np.array(mv[a:b])); del mv
            if T_:
                t = np.concatenate(T_); kq = np.concatenate(K_); V = np.concatenate(V_); o = np.argsort(key(t, kq), kind='stable'); n = len(t)
                qt[pos:pos + n] = t[o]; qk[pos:pos + n] = kq[o]
                for j in range(nv): qv[j][pos:pos + n] = V[o, j]
                pos += n; del t, kq, V, o
            k0 = k1
        assert pos == N, (pos, N)
        return qt, qk, qv
    qt, qk, qv = merge('q', 4); tt, tk_, tv = merge('t', 3)
    part = of[:-4] + '.part.npz'
    np.savez_compressed(part, tokens=np.array(toks), tmap=np.array([tm[t] for t in toks]), t0=t0, q_t=qt, q_k=qk, **{'q_v%d' % j: qv[j] for j in range(4)}, t_t=tt, t_k=tk_, t_pr=tv[0], t_sd=tv[1], t_sz=tv[2]); os.replace(part, of)
    print(d, 'tokens', len(toks), 'q', len(qt), 't', len(tt), 'guardado', of)
    for fn in glob.glob(TMP + f'{TAGP}{d}_*.npy'): os.remove(fn)
if __name__ == '__main__':
    for d in sys.argv[1:]: day(d)
