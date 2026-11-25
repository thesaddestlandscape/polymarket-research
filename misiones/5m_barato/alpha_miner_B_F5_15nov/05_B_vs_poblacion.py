#!/usr/bin/env python3
"""Paso 5: comparador de B real vs poblacion en los MISMOS dias/monedas (20-23 Oct): EV poblacion (todas / tipo B / por tercil) y EV esperado de B si ganara lo de la poblacion en su celda (dia,moneda[,tercil@100]); exceso de B = real - esperado (AS especifica de B)."""
import os, sys, json, numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from lib_ev import *
AQ = os.path.dirname(os.path.abspath(__file__)); DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/'
P = []
for d in ('2026-10-20', '2026-10-21', '2026-10-22', '2026-10-23'):
    r = pd.read_pickle(DL + f'r_{d}.pkl'); r = r[r.coin.isin(('ETH', 'SOL', 'XRP'))]
    P.append(pd.DataFrame({'dia': d, 'coin': r.coin.values, 'cl': r.fin.values, 'pnl': r.pnl.values, 'coste': r.coste.values, 'ter': ter(r.F5.values), 'tipoB': ((r.bid.values - r.q.values) >= 0.0099) & np.isfinite(r.bid.values), 'acc': r.acc.values, 'q': r.q.values}))
P = pd.concat(P, ignore_index=True)
F = pd.read_pickle(AQ + '/B_fills.pkl'); F['pnl'] = F['size'] * (F.gana - F.precio); F['coste'] = F['size'] * F.precio
txt = ['# Poblacion 20-23 Oct (ETH/SOL/XRP, banda, r_D) vs B real (215 fills / 202 unidades)']
rows = []
for nm, S in (('poblacion todas', P), ('poblacion tipo B', P[P.tipoB])):
    rows.append((nm, len(S), S.coste.sum(), ev(S.pnl, S.coste), *[ev(S.pnl[S.ter == t], S.coste[S.ter == t]) for t in ('bajo', 'medio', 'alto')]))
rows.append(('B real (fills)', len(F), F.coste.sum(), ev(F.pnl, F.coste), *[ev(F.pnl[F.ter_100 == t], F.coste[F.ter_100 == t]) for t in ('bajo', 'medio', 'alto')]))
txt.append(pd.DataFrame(rows, columns=['conjunto', 'n_filas', 'coste_EUR', 'EV_todo', 'EV_bajo', 'EV_medio', 'EV_alto']).round(3).to_string(index=False))
txt.append('\nTamano medio (acc) poblacion banda: %.1f (mediana %.1f); B: 5-6 acc.' % (P.acc.mean(), P.acc.median()))
txt.append('\nPor dia (EV pond.): poblacion todas / poblacion tipo B / B real (n fills)')
for d, g in F.groupby('dia'):
    a = P[P.dia == d]; b = a[a.tipoB]; txt.append(f"{d}: pob todas {ev(a.pnl, a.coste):+.3f} | pob tipoB {ev(b.pnl, b.coste):+.3f} | B real {ev(g.pnl, g.coste):+.3f} (n={len(g)})")
# EV esperado de B si ganara lo de la poblacion en su celda
def esperado(keys, pob):
    cell = pob.groupby(keys).apply(lambda d: pd.Series({'e': ev(d.pnl, d.coste), 'n': len(d)}), include_groups=False).reset_index()
    return cell
Fd = F.copy(); Fd['ter'] = Fd.ter_100
for nm, pob in (('todas', P), ('tipo B', P[P.tipoB])):
    for keys, kf in ((['dia', 'coin'], ['dia', 'coin']), (['dia', 'coin', 'ter'], ['dia', 'coin', 'ter'])):
        c = esperado(keys, pob).rename(columns={'e': 'e_pob'}); M = Fd.merge(c, on=kf, how='left'); ok = M.e_pob.notna()
        exp = (M.coste[ok] * M.e_pob[ok]).sum() / M.coste[ok].sum(); real = ev(M.pnl[ok], M.coste[ok])
        txt.append(f"EV esperado de B con la celda {keys} de poblacion {nm}: {exp:+.3f} | real {real:+.3f} (cubre {ok.mean()*100:.0f}% fills) | exceso B = {real-exp:+.3f}")
open(AQ + '/B_vs_poblacion.txt', 'w').write('\n'.join(txt)); print('\n'.join(txt))
