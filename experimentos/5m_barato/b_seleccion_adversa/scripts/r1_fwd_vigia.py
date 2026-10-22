#!/usr/bin/env python3
"""r1_fwd_vigia.py [--telegram] -- vigia diario del forward PREREGISTRADO de R1 (reglas_congeladas.json v2). Solo medicion.
Dias forward = >= 2026-10-22 (units_DIA.csv.gz de r1_fwd_extract.py). Por regla (R1a vol30>=26, R1b hora>=4, R1=ambas): diferencia de EV ponderado por EUR
EV(pujar)-EV(descartar), IC por bootstrap de DIAS (IC90 y IC95), sin los 2 mejores dias, n descartado. Veredicto:
 ACUMULANDO (<10 dias o n_desc<5000) | CONFIRMADA (>=10 dias, n_desc>=5000, IC95 inf>0 [Bonferroni 2 reglas], sin2mejores>0) | REFUTADA (>=10 dias, IC90 sup<=0)
 | NO_CONFIRMADA (>=20 dias sin confirmar) | INCONCLUSA. Telegram solo si cambia el veredicto de alguna regla (latch por veredicto, no por cifras)."""
import sys, os, glob, json
import numpy as np, pandas as pd
OUTD = '/root/polymarket-research-datalogs/sa_r1/'; FWD0 = '2026-10-22'
def boot(g, n=5000, seed=3):
    g = g.dropna(); d = g.dif.values; r = np.random.default_rng(seed)
    if len(d) < 2: return (np.nan,) * 4
    # remuestreo de dias con sus sumas: dif = EV_pujar - EV_desc recalculado por remuestra
    i = r.integers(0, len(g), (n, len(g)))
    pe = g.pp.values[i].sum(1) / np.maximum(g.pc.values[i].sum(1), 1e-9); de = g.dp.values[i].sum(1) / np.maximum(g.dc.values[i].sum(1), 1e-9); e = pe - de
    return np.quantile(e, .05), np.quantile(e, .95), np.quantile(e, .025), np.quantile(e, .975)
def main():
    tg = '--telegram' in sys.argv
    f2 = {f[-17:-7]: f for f in glob.glob(OUTD + 'units2_*.csv.gz')}
    fs = sorted(f2.get(f[-17:-7], f) for f in glob.glob(OUTD + 'units_*.csv.gz') if f[-17:-7] >= FWD0)
    os.makedirs(OUTD, exist_ok=True); est_f = OUTD + 'estado_forward.json'; prev = json.load(open(est_f)) if os.path.exists(est_f) else {}
    if not fs:
        print('sin dias forward todavia'); res = {'dias': 0, 'reglas': {}}
    else:
        U = pd.concat([pd.read_csv(f) for f in fs], ignore_index=True); res = {'dias': int(U.dia.nunique()), 'ultimo_dia': U.dia.max(), 'n_unidades': len(U), 'eur': round(float(U.c.sum())), 'EV_todas': float(U.p.sum() / U.c.sum()), 'reglas': {}}
        U['R1'] = U.R1a & U.R1b
        if 'A' in U:
            U['A'] = U['A'].fillna(False).astype(bool); U['A_R1ws'] = U.A & U.R1ws.fillna(False).astype(bool)
        for nm in [x for x in ('R1a', 'R1b', 'R1', 'A', 'A_R1ws') if x in U]:
            m = U[nm].astype(bool).values
            if nm in ('A', 'A_R1ws'): U2 = U[U.b15.notna()]; m = U2[nm].astype(bool).values; Ux = U2
            else: Ux = U
            g = pd.DataFrame({'pp': Ux.p[m].groupby(Ux.dia[m]).sum(), 'pc': Ux.c[m].groupby(Ux.dia[m]).sum(), 'dp': Ux.p[~m].groupby(Ux.dia[~m]).sum(), 'dc': Ux.c[~m].groupby(Ux.dia[~m]).sum()}).dropna()
            if len(g) == 0: continue
            g['dif'] = g.pp / g.pc - g.dp / g.dc
            evp = g.pp.sum() / g.pc.sum(); evd = g.dp.sum() / g.dc.sum(); lo90, hi90, lo95, hi95 = boot(g)
            top = g.dif.sort_values(ascending=False).index[:2]; g2 = g.drop(top)
            dif2 = (g2.pp.sum() / g2.pc.sum() - g2.dp.sum() / g2.dc.sum()) if len(g2) else np.nan
            nd = int((~m).sum()); dias = len(g)
            if dias >= 10 and nd >= 5000 and lo95 > 0 and dif2 > 0: v = 'CONFIRMADA'
            elif dias >= 10 and hi90 <= 0: v = 'REFUTADA'
            elif dias >= 20: v = 'NO_CONFIRMADA'
            elif dias < 10 or nd < 5000: v = 'ACUMULANDO'
            else: v = 'INCONCLUSA'
            res['reglas'][nm] = dict(veredicto=v, dias=dias, n_pujar=int(m.sum()), n_descartar=nd, EV_pujar=float(evp), EV_descartar=float(evd), dif=float(evp - evd), IC90=[float(lo90), float(hi90)], IC95=[float(lo95), float(hi95)],
                                     dif_sin2mejores=float(dif2), eur_retenido=float(g.pc.sum() / (g.pc.sum() + g.dc.sum())))
    print(json.dumps(res, indent=1, default=float))
    firma = {k: v['veredicto'] for k, v in res['reglas'].items()}
    cambio = bool(firma) and firma != prev.get('firma', {}) and not (not prev.get('firma') and all(x == 'ACUMULANDO' for x in firma.values()))
    json.dump({'firma': firma, 'ultimo': res}, open(est_f, 'w'), indent=1, default=float)
    if tg and cambio:
        sys.path.insert(0, '/root/polymarket-research')
        from shadow_digest import enviar_telegram
        enviar_telegram('R1 forward (selección adversa B): veredicto nuevo ' + json.dumps(firma) + f" | días {res['dias']} | " + ' | '.join(f"{k}: dif {v['dif']:+.3f} IC90 ({v['IC90'][0]:+.3f},{v['IC90'][1]:+.3f}) n_desc {v['n_descartar']}" for k, v in res['reglas'].items()))
main()
