#!/usr/bin/env python3
"""an_full_tape.py S OUT.csv -- EV de TODOS los rellenos maker (sin nosotros) por celda (dia, moneda, banda pc 0,05, banda T 60 s, lado barato/caro).
Celda: n, acc, coste, pnl, aciertos. pnl = acc*(gana) - coste (sin rebate)."""
import sys, os
S, OUT = sys.argv[1], sys.argv[2]
sys.path.insert(0, S); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
from datetime import date, timedelta
from fills_loader import all_fills
US = '0x659a40ff9920febc5a66836213040924343d297f'
rows = []
for i in range(13):
    d = (date(2026, 10, 9) + timedelta(i)).isoformat()
    F = all_fills(d, S); F = F[(F.maker != US) & F.des.notna()].copy()
    F['T'] = F.fin - F.ts; F = F[(F['T'] > 0) & (F['T'] <= 300)]
    F['cost'] = F.sh * F.pc; F['gana'] = (F.lado_c == F.des); F['pnl'] = np.where(F.gana, F.sh, 0.0) - F.cost
    F['pb'] = (np.floor(F.pc / 0.05 - 1e-9) * 0.05).round(2); F['Tb'] = np.minimum((np.floor((F['T'] - 1e-9) / 60)) * 60, 240).astype(int)
    F['big'] = F.sh > 20
    g = F.groupby(['act', 'pb', 'Tb', 'big']).agg(n=('sh', 'size'), sh=('sh', 'sum'), cost=('cost', 'sum'), pnl=('pnl', 'sum'), w=('gana', 'sum')).reset_index(); g.insert(0, 'dia', d)
    rows.append(g); print(d, len(F), flush=True)
pd.concat(rows).to_csv(OUT, index=False)
