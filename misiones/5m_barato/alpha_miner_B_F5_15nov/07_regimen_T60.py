#!/usr/bin/env python3
"""Paso 7 (descriptivo): EV de la poblacion con T_rem>60 s (B cancela a T=60 s) por periodo: 20-23 Oct (dias de B real), 09-19 Oct, DER 24Oct-03Nov, OOS 04-14Nov; todas vs tipo B (q<=bid100-0,01). Muestra la dependencia del regimen del EV base."""
import os, sys, glob, numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from lib_ev import *
DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/'; FW = DL + 'forward/'
rows = []
def add(d, F):
    F = F[F.coin.isin(('ETH', 'SOL', 'XRP'))]
    rows.append(pd.DataFrame({'dia': d, 'pnl': F.pnl.values, 'coste': F.coste.values, 'T': F.fin.values - F.r.values / 1000.0, 'tipoB': ((F.bid.values - F.q.values) >= 0.0099) & np.isfinite(F.bid.values)}))
for d in pd.date_range('2026-10-09', '2026-10-23').strftime('%F'): add(d, pd.read_pickle(DL + f'r_{d}.pkl'))
for p in sorted(glob.glob(FW + 'prints_2026-*.pkl')):
    d = os.path.basename(p)[7:17]
    if '2026-10-24' <= d <= '2026-11-14': add(d, pd.read_pickle(p))
P = pd.concat(rows, ignore_index=True); P = P[P['T'] > 60]
per = {'B real 20-23 Oct': ('2026-10-20', '2026-10-23'), 'INS 09-19 Oct': ('2026-10-09', '2026-10-19'), 'DER 24Oct-03Nov': ('2026-10-24', '2026-11-03'), 'OOS 04-14Nov': ('2026-11-04', '2026-11-14')}
out = ['# EV poblacion (ETH/SOL/XRP, banda, T_rem>60 s = ventana de B) por periodo; EV pond. pooled | media diaria [IC90 inf] | dias+/dias']
for nm, (a, b) in per.items():
    for k, S in (('todas', P[(P.dia >= a) & (P.dia <= b)]), ('tipo B', P[(P.dia >= a) & (P.dia <= b) & P.tipoB])):
        d = S.groupby('dia').apply(lambda x: ev(x.pnl, x.coste), include_groups=False); lo, p, m = t_ic(d)
        out.append(f'{nm:18s} {k:7s} EV {ev(S.pnl, S.coste):+.3f} | {m:+.3f} [{lo:+.3f}] | {int((d>0).sum())}/{len(d)} (filas {len(S)})')
open(os.path.dirname(os.path.abspath(__file__)) + '/regimen_T60.txt', 'w').write('\n'.join(out)); print('\n'.join(out))
