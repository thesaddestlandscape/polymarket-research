#!/usr/bin/env python3
"""Paso 10 (FASE 1, aritmetica pura, sin lectura de datos pesados): modelo de escalado EXPLICITO y chequeo de dependencia de dias extremos.
Parte (a): re-pooling de los periodos de regimen quitando sus dias dominantes (lee regimen_serie_diaria.txt: EV*coste por dia).
Parte (b): anual = 365 * coste_dia * EV * f ; cuota s = coste_dia / V_tipoB ; coste_dia necesario para 200 kEUR; banca Kelly fraccional y dias de composicion.
TODO es HIPOTESIS NO MEDIDA salvo las anclas marcadas [A]. EV de escenario = indice de motor (in-sample) o ΔEV poblacional, NO prevision de euros."""
import os, re, math, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); out = []
rows = []
for ln in open(HERE + '/regimen_serie_diaria.txt'):
    m = re.match(r'(2026-\d\d-\d\d)\s+([+-]\d+\.\d+)\s+([+-]\d+\.\d+)\s+(\d+\.\d)\s+(\d+)', ln)
    if m: rows.append((m.group(1), float(m.group(2)), float(m.group(3)), float(m.group(4)), int(m.group(5))))
D = {d: (evA, evB, cB) for d, evA, evB, cB, n in rows}
def pool(days, drop=()):
    c = sum(D[d][2] for d in days if d not in drop); p = sum(D[d][1] * D[d][2] for d in days if d not in drop)
    return p / c, c
import datetime as dt
def rng(a, b):
    x = dt.date.fromisoformat(a); y = dt.date.fromisoformat(b); return [(x + dt.timedelta(i)).isoformat() for i in range((y - x).days + 1)]
out.append('# (a) EV tipo B pooled (T_rem>60 s) por periodo: con todo, sin sus 2 MEJORES dias por pnl (convencion del proyecto) y, para el bloque de B real, sin el PEOR dia (diagnostico, no robustez)')
for nm, (a, b) in (('INS 09-19 Oct', ('2026-10-09', '2026-10-19')), ('B real 20-23 Oct', ('2026-10-20', '2026-10-23')), ('DER 24Oct-03Nov', ('2026-10-24', '2026-11-03')), ('OOS 04-14Nov', ('2026-11-04', '2026-11-14'))):
    days = rng(a, b); e, c = pool(days); pn = {d: D[d][1] * D[d][2] for d in days}
    best2 = tuple(sorted(days, key=lambda d: -pn[d])[:2]); worst = min(days, key=lambda d: pn[d])
    e2, c2 = pool(days, best2); e3, c3 = pool(days, (worst,)); top = max(days, key=lambda d: abs(pn[d]))
    out.append(f'{nm:17s} EV {e:+.3f} (coste {c:,.0f} EUR) | sin 2 mejores ({",".join(x[5:] for x in best2)}): {e2:+.3f} | sin el peor ({worst[5:]}): {e3:+.3f} | dia de mayor |pnl| {top[5:]} ({D[top][1]:+.3f} sobre {D[top][2]:,.0f} EUR = {100*abs(pn[top])/max(1e-9,abs(e*c)):.0f} % del pnl del periodo)')
V = float(np.mean([D[d][2] for d in D])); out.append(f'[A] V_tipoB (T>60 s, ETH/SOL/XRP, banda 0,10-0,30, todos los makers) = {V:,.0f} EUR/dia (media de {len(D)} dias 09-Oct..14-Nov; poblacion, no capturable entera)')
# anclas B real y motor
costeB, unidadesB, sdU = 221.30 / 4, 202 / 4, 2.14
out.append(f'[A] B real: coste {costeB:.1f} EUR/dia = {100*costeB/V:.2f} % de V; {unidadesB:.1f} unidades/dia; SD retorno/EUR por unidad {sdU} (validaciones.txt); EV -0,072 (n=202)')
out.append('[A] motor TRAIN 15 d (PASS_T_V3 §5-6): CXB60 EV +0,135, 39,6 EUR/dia de coste, 58,8 rellenos/dia; F5A+CXB60 +0,206, 28,7 EUR/dia (maximo de K=10, in-sample)')
out.append('# (b) anual (kEUR) = 365 x coste_dia x EV x f (f=1: sin regimen). EV de escenario: 0 / +0,03 (ΔEV poblacional G1 OOS +0,02..+0,04 sobre base ~0) / +0,05 / +0,135 (CXB60 motor) / +0,206 (F5A+CXB60 motor)')
EVS = (0.0, 0.03, 0.05, 0.135, 0.206)
out.append('coste_dia (cuota s de V)   ' + '  '.join(f'EV{e:+.3f}' for e in EVS))
for c in (55, 150, 500, 1000, 2000):
    out.append(f'{c:5d} EUR/dia (s={100*c/V:5.1f} %)   ' + '  '.join(f'{365*c*e/1000:7.1f}' for e in EVS))
out.append('coste_dia necesario para 200 kEUR/ano (EUR/dia | % de V): ' + ' ; '.join(f'EV{e:+.3f}: {200000/365/e:,.0f} | {100*200000/365/e/V:.0f} %' for e in EVS[1:]))
out.append('# Composicion (Kelly fraccional k=0,5; n_u unidades/dia fijo; sigma^2 = SD^2; stake/unidad u = k*EV/sigma^2 * banca; crecimiento/dia = n_u*k(2-k)*EV^2/(2 sigma^2))')
s2 = sdU ** 2; k = 0.5
for e in EVS[1:]:
    g = unidadesB * k * (2 - k) * e * e / (2 * s2)
    for cap in (500, 2000):
        u = cap / unidadesB; Bcap = u / (k * e / s2); days = math.log(Bcap / 20.0) / g if Bcap > 20 else 0
        out.append(f'EV{e:+.3f} cap {cap:4d} EUR/dia: crecimiento {100*g:5.2f} %/dia | stake/unidad {u:5.1f} EUR | banca Kelly-1/2 necesaria {Bcap:7.0f} EUR | dias desde 20 EUR {days:6.0f} | anual al tope {365*cap*e/1000:6.1f} kEUR = {100*365*cap*e/200000:4.1f} % del hueco')
out.append('Nota: unidades NO independientes (racimos por cierre): el n efectivo es menor y el crecimiento real, menor; con EV<=0 la fraccion Kelly es 0 (no se escala).')
open(HERE + '/modelo_escalado_f1.txt', 'w').write('\n'.join(out)); print('\n'.join(out))
