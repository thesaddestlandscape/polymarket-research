#!/usr/bin/env python3
"""reglas.py b|pop DIAS_ELEGIR DIAS_MEDIR -- evalua las 40 reglas preregistradas (+ inversiones) de salida tras el relleno.
Ganancia de una regla = sum(salida - payout) en unidades disparadas; se divide por el coste de TODAS las unidades del periodo (EV ponderado por EUR).
Placebo: disparos barajados dentro de dia entre unidades con salida posible (mismo n). Max-estadistico sobre las 40 reglas."""
import sys, os, glob, numpy as np, pandas as pd
DD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
TAUS = (5, 15, 30, 60)
def reglas():
    R = []
    for t in TAUS:
        R.append((f'A0_t{t}', t, lambda d: np.ones(len(d), bool), lambda d: np.zeros(len(d), bool)))
        for th in (0.01, 0.02, 0.04): R.append((f'A1_bid-{th}_t{t}', t, lambda d, th=th: d.dbid.values <= -th + 1e-9, lambda d, th=th: d.dbid.values >= th - 1e-9))
        for x in (3, 6): R.append((f'A2_bn-{x}_t{t}', t, lambda d, x=x: d.bnret.values <= -x, lambda d, x=x: d.bnret.values >= x))
        for th in (0.01, 0.02): R.append((f'A3_15-{th}_t{t}', t, lambda d, th=th: d.d15.values <= -th + 1e-9, lambda d, th=th: d.d15.values >= th - 1e-9))
        def imb(d):
            tot = (d.fav + d.con).values; return np.where(tot > 0, (d.fav - d.con).values / np.maximum(tot, 1e-9), 0), tot
        R.append((f'A4_flujo_t{t}', t, lambda d: (imb(d)[0] <= -0.5) & (imb(d)[1] >= 10), lambda d: (imb(d)[0] >= 0.5) & (imb(d)[1] >= 10)))
        R.append((f'A5_imb_t{t}', t, lambda d: (d.bsz / (d.bsz + d.asz)).values <= 0.25, lambda d: (d.bsz / (d.bsz + d.asz)).values >= 0.75))
    return R
def cargar(modo, dias):
    fs = [os.path.join(DD, f'largo_{modo}_{d}.csv') for d in dias]
    return pd.concat([pd.read_csv(f) for f in fs if os.path.exists(f)], ignore_index=True)
def evalua(L, R, nperm=1000, seed=7):
    U = L[L.tau == TAUS[0]]; coste = U.coste.sum(); dias = sorted(L.dia.unique())
    coste_d = U.groupby('dia').coste.sum()
    rng = np.random.default_rng(seed); out = []; permmax = np.full(nperm, -np.inf); permmax_inv = None
    for name, tau, f, finv in R:
        d = L[L.tau == tau].reset_index(drop=True)
        ap = d.aplic.values == 1; trig = np.nan_to_num(f(d)).astype(bool) & ap; inv = np.nan_to_num(finv(d)).astype(bool) & ap
        delta = np.where(ap, d.salida.fillna(0).values - d.payout.values, 0.0)
        g = delta[trig].sum(); gi = delta[inv].sum()
        lose = d.gana.values == 0
        salv = d.salida.fillna(0).values[trig & lose].sum(); sacr = (d.payout.values - d.salida.fillna(0).values)[trig & ~lose].sum()
        perd_ev = (-d.coste.values[trig & lose]).sum()
        gd = {dd: delta[trig & (d.dia.values == dd)].sum() / coste_d[dd] for dd in dias}
        # placebo: barajar disparos dentro de dia entre aplicables
        pl = np.zeros(nperm)
        for dd in dias:
            idx = np.where(ap & (d.dia.values == dd))[0]; k = int((trig[idx]).sum())
            if k == 0 or len(idx) == 0: continue
            dv = delta[idx]
            for i in range(nperm): pl[i] += dv[rng.choice(len(idx), k, replace=False)].sum()
        permmax = np.maximum(permmax, pl / coste)
        out.append(dict(regla=name, tau=tau, n_aplic=int(ap.sum()), n_disp=int(trig.sum()), disp_perd=int((trig & lose).sum()), disp_gan=int((trig & ~lose).sum()),
                        eur_salvados_perd=round(salv, 2), eur_sacrif_gan=round(sacr, 2), ganancia_eur=round(g, 2), ganancia_por_eur=g / coste,
                        placebo_media=pl.mean() / coste, p_placebo=float((pl >= g - 1e-12).mean()), inversion_por_eur=gi / coste, n_inv=int(inv.sum()),
                        dias_pos=sum(v > 0 for v in gd.values()), **{f'g_{dd[5:]}': round(v, 4) for dd, v in gd.items()},
                        acierto_disp=(~lose[trig]).mean() if trig.any() else np.nan, bid_exec_disp=d.bid_exec.values[trig].mean() if trig.any() else np.nan))
    T = pd.DataFrame(out)
    T['p_maxstat'] = [float((permmax >= x - 1e-12).mean()) for x in T.ganancia_por_eur]
    return T, coste, len(U)
if __name__ == '__main__':
    modo = sys.argv[1]; dsel = sys.argv[2].split(','); dmed = sys.argv[3].split(',') if len(sys.argv) > 3 else []
    R = reglas(); pd.set_option('display.width', 250); pd.set_option('display.max_columns', 40); pd.set_option('display.max_rows', 200)
    for nombre, dias in (('ELEGIR', dsel), ('MEDIR', dmed)):
        if not dias: continue
        L = cargar(modo, dias); T, coste, n = evalua(L, R)
        print(f'\n=== {modo} {nombre} dias {dias}: unidades {n}, coste {coste:.1f}, hold EV {(L[L.tau==5].payout.sum()-coste)/coste:+.4f}')
        print(T.sort_values('ganancia_por_eur', ascending=False).to_string(index=False, float_format=lambda x: f'{x:+.4f}'))
        T.to_csv(os.path.join(DD, '..', f'reglas_{modo}_{nombre}_{"_".join(x[5:] for x in dias)}.csv'), index=False)
