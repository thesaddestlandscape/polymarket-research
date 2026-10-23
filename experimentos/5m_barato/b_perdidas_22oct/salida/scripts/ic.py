#!/usr/bin/env python3
"""ic.py -- IC90 bootstrap por CIERRE (fin del 5m; varias monedas en el mismo cierre = una apuesta) y por dia de la ganancia de reglas
elegidas; residuo de calibracion (acierto - bid de salida) por dia en las disparadas. Tambien motivos de 'salida no posible'."""
import sys, os, numpy as np, pandas as pd
sys.argv = ['x']; import reglas as R
DD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
RS = {r[0]: r for r in R.reglas()}
def boot(d, trig, coste_tot_por_grupo, col, n=4000, seed=5):
    delta = np.where(trig, d.salida.fillna(0).values - d.payout.values, 0.0)
    g = pd.DataFrame({'k': d[col].values, 'x': delta}).groupby('k').x.sum()
    cg = coste_tot_por_grupo.reindex(g.index).fillna(0).values; gx = g.values
    rng = np.random.default_rng(seed); i = rng.integers(0, len(gx), (n, len(gx)))
    e = gx[i].sum(1) / cg[i].sum(1); return gx.sum() / cg.sum(), np.quantile(e, .05), np.quantile(e, .95), len(gx)
for modo, dias, nombres in (('pop', ['2026-10-17', '2026-10-18', '2026-10-19'], ['A5_imb_t60', 'A4_flujo_t15', 'A2_bn-3_t30', 'A1_bid-0.02_t30', 'A0_t15']),
                            ('pop', ['2026-10-20', '2026-10-21', '2026-10-22'], ['A5_imb_t60', 'A4_flujo_t15', 'A2_bn-3_t30', 'A1_bid-0.02_t30', 'A0_t15']),
                            ('b', ['2026-10-20', '2026-10-21', '2026-10-22'], ['A2_bn-3_t30', 'A5_imb_t60', 'A4_flujo_t15', 'A1_bid-0.02_t30', 'A0_t15'])):
    L = R.cargar(modo, dias); L['cierre'] = L.mercado.str.split('-').str[-1]
    U = L[L.tau == 5]; cc = U.groupby('cierre').coste.sum(); cd = U.groupby('dia').coste.sum()
    print(f'\n## {modo} {dias[0][5:]}..{dias[-1][5:]} unidades {len(U)} cierres {U.cierre.nunique()}')
    for nm in nombres:
        _, tau, f, _ = RS[nm]; d = L[L.tau == tau].reset_index(drop=True)
        trig = np.nan_to_num(f(d)).astype(bool) & (d.aplic.values == 1)
        ev, lo, hi, ng = boot(d, trig, cc, 'cierre'); evd, lod, hid, nd = boot(d, trig, cd, 'dia')
        res = {dd: (d.gana.values[trig & (d.dia.values == dd)] - d.bid_exec.values[trig & (d.dia.values == dd)]).mean() for dd in dias}
        print(f'  {nm:16s} disparadas {trig.sum():4d} ganancia {ev:+.4f}/EUR IC90 cierre ({lo:+.4f},{hi:+.4f}) n_cierres {ng} | IC90 dia ({lod:+.4f},{hid:+.4f}) '
              f'| residuo acierto-bid_salida por dia ' + ' '.join(f'{v:+.3f}' for v in res.values()))
    d = L[L.tau == 5]; na = d[d.aplic == 0]
    print('  tau=5 salida no posible:', len(na), 'sin bid:', int(na.bid.isna().sum()), 'cruzado/bid>=ask o sin bid en ejecucion:', int(((na.bid >= na.ask) | na.bid.isna()).sum()))
