#!/usr/bin/env python3
"""sim_v3m.py DIA [DIA...] -- simulador B-like de sim_v2.py (b_seleccion_adversa/scripts) con el libro de book_grid.py (m5_registro).
Copia LITERAL de la logica de sim_v2 para p, bb, ba, bs, as, minpc, win, side (se omiten b15 y rasgos Binance: no intervienen en la
puerta ni en el relleno). Salida: datalogs/v3m_puerta/simv3m_DIA.npz (mismas claves que simv2 para esas columnas). PREREG_V3_PUERTA_v2 §2."""
import sys, os
import numpy as np, pandas as pd
SA = '/root/polymarket-research/experimentos/5m_barato/b_seleccion_adversa/scripts'; sys.path.insert(0, SA)
from fills_loader import all_fills
K = 47; TK = 295 - 5 * np.arange(K); CAS = 2.4; OUT = '/root/polymarket-research-datalogs/v3m_puerta/'
def day(d):
    of = OUT + f'simv3m_{d}.npz'
    if os.path.exists(of): print(d, 'ya'); return
    z = np.load(OUT + f'grid_{d}.npz', allow_pickle=True); BK = z['book']
    meta = pd.DataFrame(z['tmap'], columns=['act', 'marco', 'mid', 'fin', 'lado']); meta['mid'] = meta.mid.astype(np.int64)
    t5 = {(r.mid, r.lado): i for i, r in enumerate(meta.itertuples()) if r.marco == '5min'}
    F = all_fills(d, None); F['tc'] = F.ts - CAS
    F = F[F.des.notna()].sort_values(['mkt', 'tc']); mk = F.mkt.values; cuts = np.flatnonzero(np.r_[True, mk[1:] != mk[:-1], True])
    names = ['p', 'bb', 'ba', 'bs', 'as_', 'minpc']; M = {k: [] for k in names}; rec = {k: [] for k in ['dia', 'act', 'mkt', 'fin', 'win', 'side']}
    nmk = 0; nobook = 0; nband = 0
    for ci in range(len(cuts) - 1):
        f = F.iloc[cuts[ci]:cuts[ci + 1]]; mid_ = int(f.mkt.iloc[0]); act = f.act.iloc[0]; fin = float(f.fin.iloc[0]); des = f.des.iloc[0]; nmk += 1
        iy, in_ = t5.get((mid_, 'YES')), t5.get((mid_, 'NO'))
        if iy is None or in_ is None: nobook += 1; continue
        tk = fin - TK
        by = [BK[iy][:, j].astype(np.float32) for j in range(4)]; bn = [BK[in_][:, j].astype(np.float32) for j in range(4)]
        def band(bb): return np.isfinite(bb) & (bb > 0.11 + 1e-9) & (bb <= 0.30 + 1e-9)
        cy, cn = band(by[0]), band(bn[0])
        if not (cy | cn).any(): nband += 1; continue
        first = np.argmax(cy | cn); sgn = 1 if cy[first] else -1; bk = by if sgn > 0 else bn
        bb, ba, bs, as_ = bk
        kk = 2 if act == 'ETH' else 1
        b = np.round(np.nan_to_num(bb, nan=0) * 1000).astype(int); a_ = np.round(np.nan_to_num(ba, nan=9) * 1000).astype(int)
        o = np.where(b % 10 == 0, b - kk * 10, (b // 10 - (kk - 1)) * 10)
        ok = band(bb) & (o >= 100) & (o <= 300) & (o < b) & (o < a_); p = np.where(ok, o / 1000.0, np.nan)
        tc = f.tc.values; pc = f.pc.values; lc = f.lado_c.values == 'YES'
        sidem = lc == (sgn > 0); tcs, pcs = tc[sidem], pc[sidem]
        minpc = np.full(K, np.inf)
        for k in range(K):
            a1, b1 = np.searchsorted(tcs, [tk[k] + 0.1, tk[k] + 5.1], side='right')
            if b1 > a1: minpc[k] = pcs[a1:b1].min()
        vals = dict(p=p, bb=bb, ba=ba, bs=bs, as_=as_, minpc=minpc)
        for k_ in names: M[k_].append(vals[k_])
        rec['dia'].append(d); rec['act'].append(act); rec['mkt'].append(mid_); rec['fin'].append(fin); rec['win'].append((des == 'YES') == (sgn > 0)); rec['side'].append(sgn)
    np.savez_compressed(of, **{k: np.array(v) for k, v in rec.items()}, **{k: np.array(v) for k, v in M.items()})
    print(d, 'mercados en cinta', nmk, 'sin token en mapa', nobook, 'sin banda', nband, 'simulados', len(rec['mkt']), flush=True)
if __name__ == '__main__':
    for d in sys.argv[1:]: day(d)
