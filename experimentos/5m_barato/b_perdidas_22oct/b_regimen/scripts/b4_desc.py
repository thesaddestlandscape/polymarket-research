#!/usr/bin/env python3
"""b4_desc.py -- descriptivo post-hoc (EXPLORATORY): EV por nivel de pc (explica E1 = posicion en la banda) y B real por alineacion/CON."""
import sys, os, numpy as np, pandas as pd
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/q_techo/scripts')
OUT = []
def P(*a):
    s = ' '.join(str(x) for x in a); OUT.append(s); print(s, flush=True)
T = pd.read_pickle('/mnt/HC_Volume_106538179/agentes_datos/b_regimen/tab_reg.pkl')
T['per'] = np.where(T.dia <= '2026-10-16', 'P1', 'P2'); T['pcb'] = (np.floor((T.pc - 1e-9) / 0.02) * 0.02 + 0.02).round(2)
P('EV por nivel de pc (bins 0,02; EUR-pond.) y n:')
for per, X in T.groupby('per'):
    t = X.groupby('pcb').agg(eur=('c', 'sum'), pnl=('p', 'sum'), n=('c', 'size')); t['EV'] = t.pnl / t.eur; P(per, ' '.join(f'{k:.2f}:{v:+.3f}({n})' for k, v, n in zip(t.index, t.EV, t.n)))
# E1 vs pc: correlacion dentro de tramo
v = T[T.E1.notna()]; P('corr(E1, -pc) dentro de tramo (MAP => casi deterministica):', round(float(np.corrcoef(v.E1, -v.pc)[0, 1]), 3))
# B real
B = pd.read_csv('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/post_25_27/datos/pos_b.csv')
P('\nB real: columnas con tmin/coin:', B.shape)
B = B[B.coin.isin(['ETH', 'SOL', 'XRP'])].copy()
z = np.load('/root/polymarket-research-datalogs/regimen_5m/barras_bookticker.npz')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'b3_larga.py')).read().split('def classes')[0].split('def z240_for')[1].join(['def z240_for', '']) if False else '')
def z240_for(coin, tmin, bars):
    m0 = int(bars[coin + '_m0']); Pp = pd.Series(bars[coin + '_P']).ffill(limit=5).values; lp = np.log(Pp); R = np.diff(lp, prepend=np.nan)
    cq = np.concatenate([[0.0], np.cumsum(np.where(np.isfinite(R), R ** 2, 0.0))]); cn = np.concatenate([[0], np.cumsum(np.isfinite(R).astype(int))])
    io = (np.asarray(tmin) - m0).astype(int); ok = (io - 1440 >= 1) & (io < len(lp)); ioc = np.where(ok, io, 1500)
    cnt = cn[ioc + 1] - cn[ioc - 1439]; sq = cq[ioc + 1] - cq[ioc - 1439]; s = np.where(ok & (cnt >= 0.8 * 1440), np.sqrt(sq / np.maximum(cnt, 1)), np.nan)
    zz = (lp[np.clip(io, 0, len(lp) - 1)] - lp[np.clip(io - 240, 0, len(lp) - 1)]) / (s * np.sqrt(240)); zz[~ok] = np.nan; return zz
B['z240'] = np.nan
for c in ('ETH', 'SOL', 'XRP'):
    m = (B.coin == c).values; B.loc[m, 'z240'] = z240_for(c, B.tmin.values[m], z)
B['sd'] = np.where(B.lado == 'YES', 1.0, -1.0); zs = B.sd * B.z240
B['aln'] = np.where(zs >= 1, 'ALIGN', np.where(zs <= -1, 'COUNTER', np.where(zs.isna(), 'NA', 'FLAT')))
B['reg'] = np.where(B.z240 >= 1, 'ALC', np.where(B.z240 <= -1, 'BAJ', np.where(B.z240.isna(), 'NA', 'LAT')))
B['cls'] = B.clase_rpre
P('B real n posiciones', len(B), 'coste', round(B.coste.sum(), 2), 'pnl', round(B.pnl.sum(), 2), 'EV', round(B.pnl.sum() / B.coste.sum(), 3))
for key in ('aln', 'reg', 'cls'):
    t = B.groupby(key).agg(n=('pnl', 'size'), coste=('coste', 'sum'), pnl=('pnl', 'sum'), gana=('gana_lado', 'mean')); t['EV'] = t.pnl / t.coste; P(f'-- B por {key}\n' + t.round(3).to_string())
t = B.groupby(['aln', 'cls']).agg(n=('pnl', 'size'), coste=('coste', 'sum'), pnl=('pnl', 'sum')); t['EV'] = t.pnl / t.coste; P('-- B aln x cls\n' + t.round(3).to_string())
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos', 'b4_resultados.txt'), 'w').write('\n'.join(OUT))
