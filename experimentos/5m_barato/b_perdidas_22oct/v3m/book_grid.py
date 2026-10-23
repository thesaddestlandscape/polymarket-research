#!/usr/bin/env python3
"""book_grid.py DIA [DIA...] -- top del libro (bb, ba, bs, as) de cada token 5m ETH/SOL/XRP en la rejilla de sim_v2
(TK = 295..65 s antes del cierre, 47 pasos), desde el archivo VOL/m5_registro (filas q crudas de maker_ms). Replica la semantica
de ms_extract.py + sim_v2.book(): ultima fila q con t <= instante, solo filas con t en [cierre-330 s, cierre+10 s]; empates en t ->
la ultima en orden de fichero. Independiente del orden (el registro no es cronologico): reduce por (token, primer paso alcanzable).
Salida: /root/polymarket-research-datalogs/v3m_puerta/grid_DIA.npz. Solo lectura de produccion. PREREG_V3_PUERTA_v2 §1-§2."""
import sys, os, subprocess, tempfile
import numpy as np, pandas as pd
VOL = '/mnt/HC_Volume_106538179/m5_registro/'; OUT = '/root/polymarket-research-datalogs/v3m_puerta/'
COINS = ('ETH', 'SOL', 'XRP'); TK = 295 - 5 * np.arange(47)
def kmap(d):
    from datetime import date, timedelta
    tm = {}
    for dd in ((date.fromisoformat(d) - timedelta(1)).isoformat(), d):
        f = VOL + f'm5_registro_{dd}.csv.gz'
        if not os.path.exists(f): continue
        p = subprocess.Popen(f"zcat '{f}' 2>/dev/null | grep '^k,'", shell=True, stdout=subprocess.PIPE)
        for ch in pd.read_csv(p.stdout, header=None, names=['tipo', 't', 'tok', 'act', 'marco', 'mid', 'fin', 'lado'], dtype=str, on_bad_lines='skip', chunksize=200000):
            ch = ch[ch.act.isin(COINS) & (ch.marco == '5min')]
            for r in ch.itertuples(): tm[r.tok] = (r.act, r.marco, r.mid, r.fin, r.lado)
        p.wait()
    return tm
def day(d):
    of = OUT + f'grid_{d}.npz'
    if os.path.exists(of): print(d, 'ya'); return
    tm = kmap(d); toks = sorted(tm); ti = {t: i for i, t in enumerate(toks)}
    finms = np.array([int(pd.Timestamp(tm[t][3]).timestamp() * 1000) for t in toks], np.int64)
    G = finms[:, None] - TK[None, :] * 1000                       # (ntok, 47) ascendente
    LO = finms - 330000; HI = finms + 10000
    with tempfile.NamedTemporaryFile('w', delete=False, dir=OUT, suffix='.tok') as fh:
        fh.write('\n'.join(',' + t + ',' for t in toks) + '\n'); tokf = fh.name
    f = VOL + f'm5_registro_{d}.csv.gz'
    p = subprocess.Popen(f"zcat '{f}' 2>/dev/null | grep '^q,' | grep -F -f '{tokf}'", shell=True, stdout=subprocess.PIPE)
    acc = []; nrow = 0; nkeep = 0; seq0 = 0
    for ch in pd.read_csv(p.stdout, header=None, names=['tipo', 't', 'tok', 'c1', 'c2', 'c3', 'c4', 'c5'], dtype={'tok': str, 'c1': str, 'c2': str, 'c3': str, 'c4': str, 'c5': str},
                          on_bad_lines='skip', chunksize=200000):
        nrow += len(ch)
        ch = ch[ch.tok.isin(ti)]
        kk = ch.tok.map(ti).values.astype(np.int64); t = pd.to_numeric(ch.t, errors='coerce').values
        ok = np.isfinite(t)
        kk, t, ch = kk[ok], t[ok].astype(np.int64), ch[ok]
        keep = (t >= LO[kk]) & (t <= HI[kk]); kk, t, ch = kk[keep], t[keep], ch[keep]
        if not len(t): continue
        g = G[kk]; k0 = (g < t[:, None]).sum(1)                   # primer paso con g >= t
        m = k0 < 47; kk, t, k0, ch = kk[m], t[m], k0[m], ch[m]
        V = np.stack([pd.to_numeric(ch[c], errors='coerce').values.astype(np.float32) for c in ('c1', 'c2', 'c3', 'c4')], 1)
        seq = seq0 + np.arange(len(t)); seq0 += len(t); nkeep += len(t)
        df = pd.DataFrame(dict(key=kk * 47 + k0, t=t, seq=seq, v0=V[:, 0], v1=V[:, 1], v2=V[:, 2], v3=V[:, 3]))
        df = df.sort_values(['key', 't', 'seq']).drop_duplicates('key', keep='last'); acc.append(df)
        if len(acc) > 50:
            a = pd.concat(acc); acc = [a.sort_values(['key', 't', 'seq']).drop_duplicates('key', keep='last')]
    p.wait(); os.unlink(tokf)
    a = pd.concat(acc).sort_values(['key', 't', 'seq']).drop_duplicates('key', keep='last')
    n = len(toks); T = np.full((n, 47), -1, np.int64); S = np.full((n, 47), -1, np.int64); V = np.full((n, 47, 4), np.nan, np.float32)
    ii, kk = (a.key.values // 47), (a.key.values % 47)
    T[ii, kk] = a.t.values; S[ii, kk] = a.seq.values; V[ii, kk] = a[['v0', 'v1', 'v2', 'v3']].values
    # acumulado: para el paso k, la fila con mayor (t, seq) entre las de k0 <= k
    out = np.full((n, 47, 4), np.nan, np.float32); bt = np.full(n, -1, np.int64); bs_ = np.full(n, -1, np.int64); bv = np.full((n, 4), np.nan, np.float32)
    for k in range(47):
        better = (T[:, k] > bt) | ((T[:, k] == bt) & (S[:, k] > bs_) & (T[:, k] >= 0))
        bt = np.where(better, T[:, k], bt); bs_ = np.where(better, S[:, k], bs_); bv = np.where(better[:, None], V[:, k], bv)
        out[:, k] = np.where((bt >= 0)[:, None], bv, np.nan)
    np.savez_compressed(of, tokens=np.array(toks), tmap=np.array([tm[t] for t in toks]), book=out)
    print(d, 'tokens', n, 'filas q leidas', nrow, 'en ventana', nkeep, 'tokens con libro', int(np.isfinite(out[:, :, 0]).any(1).sum()), '->', of, flush=True)
if __name__ == '__main__':
    for d in sys.argv[1:]: day(d)
