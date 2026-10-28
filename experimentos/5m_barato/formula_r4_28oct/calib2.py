#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""calib2.py - eleccion del estado OBSERVABLE (barrido en el registro, reloj de recepcion) con los dias de DESCUBRIMIENTO 26-27 Oct unicamente.
Regla fijada ANTES de mirar 20-25: entre estados 'cl' (barrido = grupo de impresiones del mismo token/lado con hueco <=300 ms, tamano >= theta; lado SELL o ALL),
con cobertura media en [0,10; 0,60] y dEV/E>0 en AMBOS dias de descubrimiento, se elige el de mayor dEV/E medio (desempate: kappa frente a S_chain).
Ventana (t-60 s, t-5 s] y 'misma moneda' vienen del descubrimiento (identity3b) y NO se varian."""
import sys, json, numpy as np
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r4_28oct')
import r4 as R
Ds = [R.load_day(d) for d in R.CALIB_DAYS]; caches = [dict() for _ in Ds]
Scc = np.concatenate([R.eval_state(R.prep_state(*R.events_chain(D)), D['T'] * 1000.0, D['coin']) for D in Ds])
VARS = [('cl', sm, th) for sm in ('SELL', 'ALL') for th in (50, 100, 150, 200, 300, 400, 600, 800, 1200)]
rows = []
for spec in VARS:
    dv = []; cov = []; Sl = []
    for i, D in enumerate(Ds):
        S = R.eval_state(R.prep_state(*R.events_reg(D, spec, caches[i])), D['rhat'], D['coin']); Sl.append(S)
        ok = np.isfinite(D['y']); num = (D['sz'] * (D['y'] - D['p']))[ok]; den = (D['sz'] * D['p'])[ok]; Sx = S[ok]
        dv.append(float(num[Sx].sum() / den[Sx].sum() - num[~Sx].sum() / den[~Sx].sum())); cov.append(float(Sx.mean()))
    kp = R.kappa(np.concatenate(Sl), Scc); rows.append((spec, float(np.mean(cov)), dv, float(kp)))
    print('%-22s cobertura=%.3f dEV/E dia26=%+.3f dia27=%+.3f media=%+.3f kappa=%+.3f' % (str(spec), np.mean(cov), dv[0], dv[1], np.mean(dv), kp))
okc = [r for r in rows if 0.10 <= r[1] <= 0.60]
good = [r for r in okc if min(r[2]) > 0]
best = max(good or okc, key=lambda r: (np.mean(r[2]), r[3]))
print('ELEGIDO%s: %s cobertura=%.3f dEV/E dias %s media %+.3f kappa %+.3f' % ('' if good else ' (FALLBACK sin signo + en ambos dias)', best[0], best[1], [round(x, 3) for x in best[2]], np.mean(best[2]), best[3]))
fz = json.load(open(R.BASE + 'frozen_r4.json')); fz['spec_kappa_alternativa'] = fz['spec']
fz.update({'spec': list(best[0]), 'cobertura_calib': best[1], 'dEV_calib_por_dia': best[2], 'kappa_calib': best[3], 'regla': 'calib2.py: max dEV/E medio en 26-27 entre estados cl con cobertura 10-60% y signo + en ambos dias',
           'tabla2': [[list(r[0]), r[1], r[2], r[3]] for r in rows]})
json.dump(fz, open(R.BASE + 'frozen_r4.json', 'w'), indent=1)
