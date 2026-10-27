#!/usr/bin/env python3
"""valida_tp1.py DIA - equivalencia de tp1.dia() con el pipeline original del mapa (datos/niche_dia.csv, generado por s2->s4b) para un dia ya procesado."""
import sys, pandas as pd, numpy as np
import infra_lib as L, tp1 as P, n4 as N4
d = sys.argv[1]; m = P.dia(d, forzar=True); print(m['estado'], m.get('motivos'), m.get('advertencias'))
des = L.read_json(L.ROOT / 'mapa_escala/des.json', {}); G = P.carga_dia(d, des)
ref = pd.read_csv('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mapa_escala/datos/niche_dia.csv'); ref = ref[ref.dia == d]
R = {'N1': ref[(ref.marco == '5min') & (ref.coin == 'BTC') & (ref.banda == 3)], 'N2': ref[(ref.marco == '15min') & (ref.coin == 'ETH') & ref.banda.isin([6, 7])], 'N3': ref[(ref.marco == '5min') & (ref.banda == 7)]}
for k in ('N1', 'N2', 'N3'):
    g = G[k]; g = g[g.con_des]; a_c, a_p = g.coste.sum(), g.pnl.sum(); b_c, b_p = R[k].coste.sum(), R[k].pnl.sum()
    print(f'{k}: tp1 coste {a_c:,.2f} pnl {a_p:,.2f} EV {a_p / a_c:+.5f} | mapa coste {b_c:,.2f} pnl {b_p:,.2f} EV {b_p / b_c:+.5f} | dif coste {a_c / b_c - 1:+.5%} dif pnl {a_p - b_p:+.2f}')
