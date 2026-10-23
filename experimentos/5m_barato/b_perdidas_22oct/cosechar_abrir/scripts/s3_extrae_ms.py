#!/usr/bin/env python3
"""s3_extrae_ms.py DIA -- como b_perdidas_22oct/salida/scripts/extraer.py pero con BTC y con volcado a disco por moneda (RAM baja):
BTC/ETH/SOL/XRP 5m (solo ventana viva) + 15m (solo cambios de bid o huecos >60 s): filas q (top) y t (operaciones WS) por RECEPCION y aggTrade Binance (c[7]).
Salida DL/m5_cosechar_abrir/ms5_<MONEDA>_<DIA>.npz (tokens/tmap globales del dia + qr,qk,qv,tr,tk,tv; x = Binance de esa moneda). Solo lectura de produccion."""
import sys, os, subprocess, tempfile
import numpy as np, pandas as pd
VOL = '/mnt/HC_Volume_106538179/'
OUT = '/root/polymarket-research-datalogs/m5_cosechar_abrir'
COINS = ('BTC', 'ETH', 'SOL', 'XRP')
def pipe(files, pat):
    fl = ' '.join(f"'{f}'" for f in files)
    return subprocess.Popen(f"for f in {fl}; do zcat \"$f\" 2>/dev/null; done | grep -E '{pat}'", shell=True, stdout=subprocess.PIPE)
def day(d):
    if all(os.path.exists(os.path.join(OUT, f'ms5_{c}_{d}.npz')) for c in COINS): print(d, 'ya'); return
    a = VOL + f'm5_registro/m5_registro_{d}.csv.gz'; b = VOL + f'm15_registro/m15_registro_{d}.csv.gz'
    fq = [a, b]
    tm = {}
    p = pipe(fq, '^k,')
    for ch in pd.read_csv(p.stdout, header=None, names=['tipo', 't', 'tok', 'act', 'marco', 'mid', 'fin', 'lado'], dtype=str, on_bad_lines='skip', chunksize=200000):
        ch = ch[ch.act.isin(COINS) & ch.marco.isin(['5min', '15min'])]
        for r in ch.itertuples(): tm[r.tok] = (r.act, r.marco, r.mid, r.fin, r.lado)
    p.wait()
    toks = sorted(tm); ti = {t: i for i, t in enumerate(toks)}
    is15 = np.array([tm[t][1] == '15min' for t in toks])
    coin_of = np.array([COINS.index(tm[t][0]) for t in toks], dtype=np.int8)
    FIN = np.array([int(pd.Timestamp(tm[t][3]).timestamp() * 1000) for t in toks], dtype=np.int64)
    D0 = int(pd.Timestamp(d, tz='UTC').timestamp() * 1000) - 3600000
    tmp = tempfile.mkdtemp(prefix='ms5_', dir=OUT)
    fh = {(c, kind): open(os.path.join(tmp, f'{c}_{kind}.bin'), 'wb') for c in range(4) for kind in ('q', 't', 'x')}
    last = {}      # token -> ultimo bid 15m visto (adelgazado simple, valido porque el flujo se procesa en orden de archivo por tramos)
    names = ['tipo', 'tev', 'tok', 'c1', 'c2', 'c3', 'c4', 'c5']
    p = pipe(fq, '^(q|t),')
    for ch in pd.read_csv(p.stdout, header=None, names=names, dtype=str, on_bad_lines='skip', chunksize=400000):
        ch = ch[ch.tok.isin(ti)]
        if not len(ch): continue
        q = ch[ch.tipo == 'q']; t = ch[ch.tipo == 't']
        if len(q):
            rr = pd.to_numeric(q.c5, errors='coerce').fillna(0).values.astype(np.int64) - D0
            kk = q.tok.map(ti).values.astype(np.int16)
            vv = np.stack([pd.to_numeric(q[c], errors='coerce').values for c in ('c1', 'c2', 'c3', 'c4')], 1).astype(np.float32)
            es15 = is15[kk]
            vent = es15 | ((rr + D0 >= FIN[kk] - 306000) & (rr + D0 <= FIN[kk] + 3000))
            rr, kk, vv, es15 = rr[vent], kk[vent], vv[vent], es15[vent]
            if es15.any():
                df = pd.DataFrame({'k': kk, 'r': rr, 'b': vv[:, 0]})
                pk = df.groupby('k').b.shift(); pr = df.groupby('k').r.shift()
                keep = ~es15 | pk.isna().values | (pk.values != vv[:, 0]) | (np.abs(rr - pr.fillna(0).values) > 60000)
                rr, kk, vv = rr[keep], kk[keep], vv[keep]
            cc = coin_of[kk]
            for c in range(4):
                m = cc == c
                if m.any():
                    rec = np.empty(m.sum(), dtype=[('r', '<i4'), ('k', '<i2'), ('v', '<f4', 4)]); rec['r'] = rr[m]; rec['k'] = kk[m]; rec['v'] = vv[m]
                    rec.tofile(fh[(c, 'q')])
        if len(t):
            tr_ = pd.to_numeric(t.c4, errors='coerce').fillna(0).values.astype(np.int64) - D0
            tk_ = t.tok.map(ti).values.astype(np.int16)
            tv_ = np.stack([pd.to_numeric(t.c1, errors='coerce').values, (t.c2 == 'BUY').astype(float).values, pd.to_numeric(t.c3, errors='coerce').values], 1).astype(np.float32)
            vt = is15[tk_] | ((tr_ + D0 >= FIN[tk_] - 306000) & (tr_ + D0 <= FIN[tk_] + 3000))
            tr_, tk_, tv_ = tr_[vt], tk_[vt], tv_[vt]
            cc = coin_of[tk_]
            for c in range(4):
                m = cc == c
                if m.any():
                    rec = np.empty(m.sum(), dtype=[('r', '<i4'), ('k', '<i2'), ('v', '<f4', 3)]); rec['r'] = tr_[m]; rec['k'] = tk_[m]; rec['v'] = tv_[m]
                    rec.tofile(fh[(c, 't')])
    p.wait()
    p = pipe([a], '^x,[0-9]+,(BTC|ETH|SOL|XRP)USDT,')
    for ch in pd.read_csv(p.stdout, header=None, names=['tipo', 'T', 's', 'p', 'q', 'm', 'E', 'rx'], dtype={'s': str}, on_bad_lines='skip', chunksize=500000):
        for c, sy in enumerate(COINS):
            cs = ch[ch.s == sy + 'USDT']
            if len(cs):
                rec = np.empty(len(cs), dtype=[('r', '<i4'), ('p', '<f8')]); rec['r'] = (pd.to_numeric(cs.rx, errors='coerce').fillna(0).values.astype(np.int64) - D0); rec['p'] = pd.to_numeric(cs.p, errors='coerce').values
                rec.tofile(fh[(c, 'x')])
    p.wait()
    for f in fh.values(): f.close()
    tmap = np.array([tm[t] for t in toks])
    for c, cn in enumerate(COINS):
        q = np.fromfile(os.path.join(tmp, f'{cn if False else c}_q.bin'), dtype=[('r', '<i4'), ('k', '<i2'), ('v', '<f4', 4)])
        o = np.lexsort((q['r'], q['k'])); q = q[o]
        t = np.fromfile(os.path.join(tmp, f'{c}_t.bin'), dtype=[('r', '<i4'), ('k', '<i2'), ('v', '<f4', 3)])
        o = np.lexsort((t['r'], t['k'])); t = t[o]
        x = np.fromfile(os.path.join(tmp, f'{c}_x.bin'), dtype=[('r', '<i4'), ('p', '<f8')]); x = x[np.argsort(x['r'], kind='stable')]
        np.savez_compressed(os.path.join(OUT, f'ms5_{cn}_{d}.npz.tmp.npz'), tokens=np.array(toks), tmap=tmap, D0=D0, qr=q['r'], qk=q['k'], qv=q['v'], tr=t['r'], tk=t['k'], tv=t['v'], xr=x['r'], xv=x['p'])
        os.replace(os.path.join(OUT, f'ms5_{cn}_{d}.npz.tmp.npz'), os.path.join(OUT, f'ms5_{cn}_{d}.npz'))
        print(d, cn, 'q', len(q), 't', len(t), 'x', len(x), flush=True)
        del q, t, x, o
    for f in os.listdir(tmp): os.remove(os.path.join(tmp, f))
    os.rmdir(tmp)
if __name__ == '__main__':
    for d in sys.argv[1:]: day(d)
