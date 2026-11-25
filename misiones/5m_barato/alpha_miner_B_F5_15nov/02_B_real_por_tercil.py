#!/usr/bin/env python3
"""Paso 2 (PREREG_B_F5): EV de los fills reales de B por tercil de F5 (lags 100/250/1000/2000/5000 ms y F5 en la decision de la puja), reglas G1/G2/inversion, IC90 por cierre, placebo, sin 2 mejores cierres."""
import os, sys, json, numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from lib_ev import *
AQ = os.path.dirname(os.path.abspath(__file__))
F = pd.read_pickle(AQ + '/B_fills.pkl'); O = pd.read_pickle(AQ + '/B_ordenes.pkl')
F['pnl'] = F['size'] * (F.gana - F.precio); F['coste'] = F['size'] * F.precio
F['rebate'] = 0.2 * 0.07 * F.precio * (1 - F.precio) * F['size']
F = F.sort_values(['bloque', 'logidx_fill'])
def unidades(F, col):
    first = F.groupby('mkt_lado').first()
    agg = F.groupby('mkt_lado').agg(pnl=('pnl', 'sum'), coste=('coste', 'sum'), rebate=('rebate', 'sum'))
    U = agg.join(first[list(dict.fromkeys(['dia', 'coin', 'cierre', col, 'F5_100', 'F5_250']))]); U['cl'] = U.cierre; U['ter'] = ter(U[col].values); return U.reset_index()
txt = []
Ufull = unidades(F, 'F5_100'); txt += ['# B real 20-23 Oct: fills reales on-chain (e02real_fills.json, 215 fills -> %d unidades mercado-lado; EV pond. total %+.4f; PnL %+.2f EUR; coste %.2f EUR)' % (len(Ufull), ev(Ufull.pnl, Ufull.coste), Ufull.pnl.sum(), Ufull.coste.sum()),
     'Maker sin comision ni rebate (rebate teorico 0,2*0,07*q(1-q): +%.2f EUR, %+.3f/EUR). Terciles con cortes TRAIN congelados.' % (Ufull.rebate.sum(), Ufull.rebate.sum() / Ufull.coste.sum()), '']
res = {}
for L in (100, 250, 1000, 2000, 5000):
    U = unidades(F, f'F5_{L}'); lines, o = resumen(U, f'F5 a t_fill-{L} ms (primer fill de la unidad)'); txt += lines
    res[f'L{L}'] = o
    if L in (100, 250):
        PL = placebo_multi(U, ['G1', 'G2'], ['dia'], B=2000)
        for r in ('G1', 'G2'):
            obs, p, mu = PL[r]; txt.append(f'   placebo {r} (permutar tercil dentro de dia, 2000): DeltaEV obs {obs:+.3f}, media placebo {mu:+.3f}, p={p:.3f}')
            res[f'L{L}'][r]['placebo_p'] = p
        R1 = U[U.ter.isin(RET['G1'])].groupby('cl').pnl.sum().sort_values(ascending=False); T5 = R1.head(5).sum(); txt.append(f"   concentracion G1: top-5 cierres de {len(R1)} suman {T5:+.2f} EUR de {R1.sum():+.2f} EUR de pnl retenido; los 5 peores {R1.tail(5).sum():+.2f}")
        by = U.groupby('dia').apply(lambda d: pd.Series({'n': len(d), 'EV_todo': ev(d.pnl, d.coste), 'EV_G1': ev(d.pnl[d.ter.isin(RET['G1'])], d.coste[d.ter.isin(RET['G1'])]), 'EV_alto': ev(d.pnl[d.ter == 'alto'], d.coste[d.ter == 'alto'])}), include_groups=False)
        txt.append('   por dia:\n' + by.round(3).to_string()); txt.append('')
# transicion de tercil F5_100 -> F5_250 / 1000 en fills (persistencia): relevante para "cancelar al cruzar"
G = F.drop_duplicates('mkt_lado')
for L in (250, 1000, 5000):
    ct = pd.crosstab(G.ter_100, G[f'ter_{L}']); txt.append(f'# Persistencia del tercil en fills: F5@100 (filas) vs F5@{L} (cols)\n' + ct.to_string())
# F5 en la decision de la puja (orden-nivel) para las ordenes que se rellenaron: ledger puja_post.libro
Orf = O[O.relleno].copy(); Orf['cl'] = Orf.cierre; Orf['ter'] = Orf.ter_post
Orf['coste'] = Orf.coste.astype(float); Orf['pnl'] = Orf.pnl.astype(float); Orf['dia'] = Orf.dia
lines, o = resumen(Orf[['ter', 'pnl', 'coste', 'cl', 'dia']], 'F5_post (libro en la decision de la orden, ledger) - ordenes rellenadas'); txt += lines; res['post_rellenadas'] = o
# orden-nivel completo: P(fill) y EV por orden y por EUR expuesto por tercil de F5_post (seleccion adversa explicita)
O['exp'] = O['size'] * O.precio; O['pnl'] = O.pnl.fillna(0.0).astype(float); O['coste'] = O.coste.fillna(0.0).astype(float)
t = O.groupby('ter_post').agg(ordenes=('oid', 'size'), rellenadas=('relleno', 'sum'), coste=('coste', 'sum'), pnl=('pnl', 'sum'), exposicion=('exp', 'sum')); t['P_fill'] = t.rellenadas / t.ordenes
t['EV_pond_relleno'] = t.pnl / t.coste; t['pnl_por_orden'] = t.pnl / t.ordenes; t['pnl_por_EUR_expuesto'] = t.pnl / t.exposicion
txt += ['', '# Orden-nivel (3.796 ordenes; F5_post = log1p(ask top) en la decision)', t.round(4).to_string()]
Oc = O.groupby('cierre').agg(n=('oid', 'size')); 
res['ordenes_tercil'] = t.round(5).reset_index().to_dict('records')
# por moneda (B real, tercil @250)
U = unidades(F, 'F5_250'); txt += ['', '# Por moneda (unidades, F5@250): EV por tercil', U.groupby(['coin', 'ter']).apply(lambda d: pd.Series({'n': len(d), 'EV': ev(d.pnl, d.coste), 'coste': d.coste.sum()}), include_groups=False).round(3).to_string()]
open(AQ + '/B_real_por_tercil.txt', 'w').write('\n'.join(txt)); json.dump(res, open(AQ + '/B_real_por_tercil.json', 'w'), default=float, indent=1); print('\n'.join(txt))
