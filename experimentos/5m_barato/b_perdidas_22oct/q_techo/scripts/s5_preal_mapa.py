#!/usr/bin/env python3
"""s5_preal_mapa.py -- PREREG Q-TECHO seccion 6: mapa precio->acierto por tramo con el ASK/BID REAL (P-REAL, 05-21 Oct, T=180 s +250 ms) vs poblacion de rellenos maker (09-21). Descriptivo."""
import sys, json, glob, os
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qlib import tramo, COINS
FEE = 0.07; D = '/root/polymarket-research-datalogs/preal'; OUT = []
def P(*a):
    s = ' '.join(str(x) for x in a); OUT.append(s); print(s, flush=True)
des = json.load(open(D + '/desenl_cache.json'))
L = []
for f in sorted(glob.glob(D + '/ask_t0_2026-10-*.csv.gz')):
    x = pd.read_csv(f, usecols=['dia', 'coin', 'mid', 'cierre', 'lado', 'bid_180_250', 'ask_180_250', 'edad_180_250', 'bid_120_250', 'ask_120_250'], dtype={'mid': str}); L.append(x)
X = pd.concat(L, ignore_index=True); X['out'] = X.mid.map(des); X = X[X.out.notna()].copy(); X['gana'] = (X.out == X.lado).astype(float)
X['vivo'] = X.groupby(['coin', 'cierre']).edad_180_250.transform('min') <= 30000
P(f'# P-REAL mapa: tokens {len(X)} (desenlace oficial; cobertura {X.out.notna().mean():.3f} de los listados no medible aqui: se excluyen sin desenlace), dias {X.dia.nunique()}')
def tab(X, pcol, lab, fee):
    d = X[X[pcol].between(0.1001, 0.3) & X.vivo & (X.bid_180_250 <= X.ask_180_250)].copy(); d['tr'] = tramo(d[pcol].values)
    d['cost'] = d[pcol] * (1 + fee * (1 - d[pcol])); d['pnl'] = d.gana - d.cost
    g = d.groupby(['coin', 'tr']).agg(n=('gana', 'size'), hit=('gana', 'mean'), px=(pcol, 'mean'), pnl=('pnl', 'sum'), cost=('cost', 'sum')); g['ev'] = g.pnl / g.cost; g['hit_menos_px'] = g.hit - g.px
    return g
res = {}
for pcol, lab, fee in [('ask_180_250', 'ASK real (tomador, fee 0,07)', FEE), ('bid_180_250', 'BID real en reposo, SIN condicionar a relleno (maker fee 0)', 0.0)]:
    for coins, nm in [(list(COINS), 'ETH/SOL/XRP'), (['BTC', 'BNB', 'DOGE'], 'BTC/BNB/DOGE')]:
        g = tab(X[X.coin.isin(coins)], pcol, lab, fee); g2 = g.groupby('tr').apply(lambda h: pd.Series(dict(n=h.n.sum(), hit=(h.hit * h.n).sum() / h.n.sum(), px=(h.px * h.n).sum() / h.n.sum(), ev=h.pnl.sum() / h.cost.sum())), include_groups=False)
        g2['hit_menos_px'] = g2.hit - g2.px; P(f'\n## {lab} | {nm} | por tramo (0=(0,10-0,15] .. 3=(0,25-0,30])\n' + g2.round(4).to_string()); res[f'{pcol}_{nm}'] = g2.round(5).reset_index().to_dict('list')
        if nm == 'ETH/SOL/XRP': P('  por moneda x tramo:\n' + g[['n', 'hit', 'px', 'ev']].round(4).to_string())
# poblacion de rellenos
B = '/root/polymarket-research/experimentos/5m_barato/b_seleccion_adversa/datos/units/'
U = pd.concat([pd.read_pickle(B + f'units_2026-10-{d:02d}.pkl') for d in range(9, 22)], ignore_index=True); U['tr'] = tramo(U.pc.values); U['gana_f'] = U.gana.astype(float)
g = U.groupby('tr').apply(lambda h: pd.Series(dict(n=len(h), hit=h.gana_f.mean(), px=h.pc.mean(), ev=h.p.sum() / h.c.sum())), include_groups=False); g['hit_menos_px'] = g.hit - g.px
P('\n## RELLENOS de otros makers (09-21 Oct, precio de relleno maker, fee 0) ETH/SOL/XRP por tramo\n' + g.round(4).to_string()); res['relleno'] = g.round(5).reset_index().to_dict('list')
gm = U.groupby(['act', 'tr']).apply(lambda h: pd.Series(dict(n=len(h), hit=h.gana_f.mean(), px=h.pc.mean(), ev=h.p.sum() / h.c.sum())), include_groups=False); P('  por moneda x tramo:\n' + gm.round(4).to_string())
b = tab(X[X.coin.isin(COINS)], 'bid_180_250', '', 0.0).groupby('tr').apply(lambda h: h.pnl.sum() / h.cost.sum(), include_groups=False)
P('\n## SELECCION ADVERSA POR RELLENO = EV(relleno maker) - EV(bid no condicionado), por tramo (ETH/SOL/XRP; ambos fee 0, periodos distintos 09-21 vs 05-21, descriptivo)\n' + pd.DataFrame(dict(ev_relleno=g.ev, ev_bid_incond=b, AS=g.ev - b)).round(4).to_string())
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos', 'preal_mapa.json'), 'w'), default=float)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos', 'preal_mapa.txt'), 'w').write('\n'.join(OUT))
