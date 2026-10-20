#!/usr/bin/env python3
"""Paso 3 (H-B): cronologia ms. Para cada orden tomadora rival (R1,R2) en BTC 5m anidado: ultimo evento PUBLICO que subio el margen V4
(m = bid15 - ask5 - fee, >=+1c respecto al estado anterior) o que lo cruzo de < -0,05 a >= -0,05, anterior al envio acotado (ex_fill - 150 ms).
Relojes: tiempo de EXCHANGE de las filas q (c[2]) y del print rival; la fila puede ser sello de lote (error 0-470 ms, trampa conocida).
Tipo: 'ask5' (cambio de q5) o 'bid15' (cambio de q15). Control: placebo del mismo mercado-lado (p1_fills). Dias: argv."""
import sys, glob, numpy as np, pandas as pd
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/v4_comprar_lo_bueno/r3')
from simlib import *
O3 = O + 'r3_out/'
A = pd.read_csv(O3 + 'p1_fills.csv.gz'); A = A[A.w.isin(['R1_9783', 'R2_e38c'])]
res = []
for D in sys.argv[1:]:
    km = kmap(D); k15 = {(C, l): v[0] for (m_, C, l), v in km.items() if m_ == '15min'}; k5 = {(C, l): v[0] for (m_, C, l), v in km.items() if m_ == '5min'}
    X = A[A.dia == D].sort_values('ex').copy(); X['rafaga'] = X.ex // 60
    X['k'] = X[X.placebo == 0].groupby(['w', 'cierre', 'lado', 'rafaga']).ngroup()
    byc = {c: g for c, g in X.groupby('cierre')}
    for g, QS, TS in grupos(D):
        if g not in byc: continue
        rows = byc[g]
        for lado, rr in rows.groupby('lado'):
            q5, q15 = QS.get(k5.get((g, lado))), QS.get(k15.get((g, lado)))
            if q5 is None or q15 is None or not len(q5.ex) or not len(q15.ex): continue
            ex = np.concatenate([q5.ex, q15.ex]); typ = np.concatenate([np.full(len(q5.ex), 5), np.full(len(q15.ex), 15)])
            bid = np.concatenate([np.full(len(q5.ex), np.nan), q15.bid]); ask = np.concatenate([q5.ask, np.full(len(q15.ex), np.nan)])
            o = np.argsort(ex, kind='stable'); ex, typ, bid, ask = ex[o], typ[o], bid[o], ask[o]
            a5 = pd.Series(ask).ffill().values; b15 = pd.Series(bid).ffill().values
            m = b15 - a5 - 0.07 * a5 * (1 - a5)
            ok = ~np.isnan(m); mprev = np.concatenate([[np.nan], m[:-1]]); dm = m - mprev
            rise = ok & (dm >= 0.0099); cross = ok & (m >= -0.05) & (mprev < -0.05)
            idx = np.arange(len(m)); lr = np.maximum.accumulate(np.where(rise, idx, -1)); lc = np.maximum.accumulate(np.where(cross, idx, -1))
            # clasifica la subida: ask5 cae o bid15 sube
            for r in rr.itertuples():
                ts = r.ex - 150; j = np.searchsorted(ex, ts, side='right') - 1
                if j < 0: continue
                ir, ic = lr[j], lc[j]
                post = np.where(rise[j + 1:] & (ex[j + 1:] <= ts + 300))[0]       # subida del margen DESPUES del envio acotado (<=300 ms)
                res.append(dict(dia=D, w=r.w, placebo=r.placebo, k=getattr(r, 'k', np.nan), cierre=g,
                                lag_rise=(ts - ex[ir]) if ir >= 0 else np.nan, tipo_rise=typ[ir] if ir >= 0 else 0,
                                lag_cross=(ts - ex[ic]) if ic >= 0 else np.nan, tipo_cross=typ[ic] if ic >= 0 else 0,
                                m_envio=m[j], sube_tras_envio=len(post) > 0, edad_estado_ms=ts - ex[j]))
    print(D, 'filas acumuladas', len(res), flush=True)
R = pd.DataFrame(res); R.to_csv(O3 + 'p3_cronologia.csv', index=False)
R['first'] = R.k.notna() & (R.groupby(['w', 'cierre']).k.transform('min') == R.k)
def pc(x): return np.nanpercentile(x, [10, 25, 50, 75, 90]).round(0) if len(x.dropna()) else None
out = open('p3_out.txt', 'w')
def P(*a): print(*a); print(*a, file=out)
for w in ['R1_9783', 'R2_e38c']:
    for nom, s in (('REAL 1a rafaga', R[(R.w == w) & (R.placebo == 0) & R['first']]), ('REAL todas', R[(R.w == w) & (R.placebo == 0)]), ('PLACEBO', R[(R.w == w) & (R.placebo == 1)])):
        if not len(s): continue
        P(f'{w} {nom:15s} n={len(s):4d} lag_subida_margen ms P10/25/50/75/90 {pc(s.lag_rise)} | <=250 ms: {(s.lag_rise<=250).mean():.2f} <=1000: {(s.lag_rise<=1000).mean():.2f} | tipo ask5/bid15: {(s.tipo_rise==5).mean():.2f}/{(s.tipo_rise==15).mean():.2f}')
        P(f'{"":24s} lag_cruce(-0,05) P10/50/90 {pc(s.lag_cross)} <=250: {(s.lag_cross<=250).mean():.2f} | margen sube ANTES de que llegue la orden (<=300 ms tras envio): {s.sube_tras_envio.mean():.2f} | edad del ultimo estado P50 {np.nanmedian(s.edad_estado_ms):.0f} ms')
out.close()
