#!/usr/bin/env python3
"""Juez forward H-Q11-SOL013 (PREREG_Q11_SOL013.md + ADDENDUM2/3, congelados). Solo lectura de dec2_D/dec3s100_D.pkl; 0 ordenes.
Regla: act=='SOL', L==0.13, variante T1 (dec2) y T1 a -100 ms (dec3s100); comparadores PLA_T1 y G0. Dias que cuentan >= 2026-11-06 con AMBOS pkl.
Criterios diarios/terminal/PROMOCION: ADDENDUM3_Q11 (sha c991602c) via q11_decision.py. Estado terminal en <salida>/estado_sol013.json.
Uso: filtro_sol013.py [--desde D] [--hasta D] [--salida DIR] [--hoy D]  (ensayo sobre gastados: --desde 2026-10-26 --salida /ruta/ensayo)"""
import sys, os, json, argparse, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, HERE)
import numpy as np, pandas as pd
import q11_decision as Q
ap = argparse.ArgumentParser(); ap.add_argument('--desde', default='2026-11-06'); ap.add_argument('--hasta', default='9999-12-31'); ap.add_argument('--salida', default=HERE); ap.add_argument('--out', default=Q.DEC_OUT); ap.add_argument('--hoy', default=None)
a = ap.parse_args(); SEED, B = 13, 4000
os.makedirs(a.salida, exist_ok=True)
def escribir(L, jd):
    tmp = a.salida + '/.RESUMEN.tmp'; open(tmp, 'w').write('\n'.join(L) + '\n'); os.replace(tmp, a.salida + '/RESUMEN.md')
    tmpj = a.salida + '/.resumen.tmp'; json.dump(jd, open(tmpj, 'w'), indent=1, default=float); os.replace(tmpj, a.salida + '/resumen.json')
dias, R2, R3, err = Q.cargar_dias(a.out, a.desde, a.hasta)
cab = f'# RESUMEN H-Q11-SOL013 (generado {dt.datetime.now(dt.timezone.utc):%FT%TZ})'
if err or not dias:
    why = 'ERROR_DATOS: ' + '; '.join(err[:3]) if err else f'Dias validos desde {a.desde}: 0 (aun no hay dec2+dec3s100 de dias que cuenten)'
    escribir([cab, why, '## VEREDICTO: INSUFFICIENT'], dict(dias=[], veredicto='INSUFFICIENT', error=err)); print(why); sys.exit(0)
def sel(R, v):
    R = R[(R.act == 'SOL') & ((R.L - 0.13).abs() < 1e-9) & (R['var'] == v)] if len(R) else R
    return R
T1, PLA, G0, S100 = sel(R2, 'T1'), sel(R2, 'PLA_T1'), sel(R2, 'G0'), sel(R3, 'T1')
nd_valid = len(dias); n = len(T1)
e, ep, eg, e100 = Q.ev(T1), Q.ev(PLA), Q.ev(G0), Q.ev(S100); s2 = Q.sin2(T1)
vT = Q.vec_cierre(T1, B, SEED); lo, hi = Q.q(vT, .05), Q.q(vT, .95); plo, phi = Q.q(vT, .0125), Q.q(vT, .9875)
dT, dP, dG = Q.evdia(T1), Q.evdia(PLA), Q.evdia(G0)
DP = sorted(set(dT.index) & set(dP.index)); DG = sorted(set(dT.index) & set(dG.index))   # D_T1PLA, D_T1G0 (dias comparables)
kP = sum(dT[d] > dP[d] for d in DP); kG = sum(dT[d] > dG[d] for d in DG)
ndP, ndG = len(DP), len(DG)
# muestra b: solo dias de D_T1PLA
sub = lambda x: x[x.dia.isin(DP)] if len(x) else x
T1b, PLAb, G0b = sub(T1), sub(PLA), sub(G0)
eb, epb, egb = Q.ev(T1b), Q.ev(PLAb), Q.ev(G0b); s2b = Q.sin2(T1b); vTb = Q.vec_cierre(T1b, B, SEED); lob = Q.q(vTb, .05)
cA = {'EV>0': Q.gt(e), 'EV(-100ms)>0': Q.gt(e100), 'EV sin 2 mejores dias>0': Q.gt(s2), 'IC90 cierre inf>0': Q.gt(lo), 'EV(T1)>EV(PLA_T1) agregado': Q.gt(e - ep),
      'EV(T1)>EV(G0) agregado': Q.gt(e - eg), 'n>=40 rellenos T1': n >= 40}
cB = {'EV>0': Q.gt(eb), 'EV sin 2 mejores dias>0': Q.gt(s2b), 'IC90 cierre inf>0': Q.gt(lob), 'EV(T1)>EV(PLA_T1)': Q.gt(eb - epb), 'EV(T1)>EV(G0)': Q.gt(eb - egb), 'n>=40 rellenos T1': len(T1b) >= 40}
cC = {f'nd(T1,PLA_T1)>=10 y >=60 % victorias ({kP}/{ndP})': Q.ok60(kP, ndP), f'nd(T1,G0)>=10 y >=60 % victorias ({kG}/{ndG})': Q.ok60(kG, ndG)}
confirma = all(cA.values()) and all(cB.values()) and all(cC.values())
# REFUTA sobre D_T1PLA (sec. 5 fila 4)
refuta_def = ndP > 0 and all(v == v for v in (eb, s2b, epb))
refuta = refuta_def and (eb <= 0 or s2b <= 0 or eb <= epb)
estado_path = a.salida + '/estado_sol013.json'; st = Q.cargar_estado(estado_path)
tok, why, st = Q.veredicto(st, err, nd_valid, ndP, confirma, refuta_def, refuta, a.hoy)
Q.guardar_estado(estado_path, st)
IC_ok = Q.gt(plo); ICc_ok = Q.gt(Q.q(vTb, .0125))
promo = tok == 'CONFIRMA_FINAL' and IC_ok and ICc_ok
f = Q.f3; sw = T1[T1.nmk >= 3]; ns = T1[T1.nmk < 3]
L = [cab, f'Prereg PREREG_Q11_SOL013.md + ADDENDUM2/3 (no modificar). Rango: {a.desde}..{a.hasta}. Fuente: {a.out}', '',
     f'Dias validos (dec2+dec3s100): {nd_valid} {dias[0]}..{dias[-1]}; con rellenos T1: {len(dT)}; nd_validos(T1,PLA_T1)={ndP}; nd_validos(T1,G0)={ndG}',
     f'T1 SOL L=0,13: n={n} rellenos, mercados={T1.mkt.nunique() if n else 0}, cierres={T1.fin.nunique() if n else 0}, coste={T1.cost.sum():.1f} EUR, pnl={T1.pnl.sum():.2f}',
     f'EV ponderado por EUR (sum pnl/sum coste): T1 {f(e)} | -100 ms {f(e100)} (n={len(S100)}) | sin 2 mejores dias {f(s2)} | IC90 por cierre ({f(lo)}, {f(hi)})',
     f'EV por unidad (media pnl/coste): {f((T1.pnl / T1.cost).mean()) if n else "nan"}; dias +: {int((T1.groupby("dia").pnl.sum() > 0).sum())}/{len(dT)}',
     f'Comparadores: PLA_T1 n={len(PLA)} EV {f(ep)} (sin2 {f(Q.sin2(PLA))}) | G0 n={len(G0)} EV {f(eg)} (sin2 {f(Q.sin2(G0))})',
     f'Victorias estrictas por dia comparable: T1>PLA_T1 {kP}/{ndP} | T1>G0 {kG}/{ndG}',
     f'Muestra b (solo D_T1PLA): T1 n={len(T1b)} EV {f(eb)} sin2 {f(s2b)} IC90 inf {f(lob)} | PLA_T1 EV {f(epb)} | G0 EV {f(egb)}',
     f'DIAGNOSTICO barrido (nmk>=3): {len(sw)} rellenos EV {f(Q.ev(sw))}; resto {len(ns)} EV {f(Q.ev(ns))} (no es regla de decision)',
     '', '## CONFIRMA (sec. 3): a) todos los dias validos'] + [f'- [{"x" if v else " "}] {k}' for k, v in cA.items()] + ['b) solo dias de D_T1PLA'] + [f'- [{"x" if v else " "}] {k}' for k, v in cB.items()] + \
    ['c) dias comparables'] + [f'- [{"x" if v else " "}] {k}' for k, v in cC.items()] + [f'=> sec. 3 cumplida: {confirma} | racha {st.get("racha")}/3 (last_nd={st.get("last_nd")}) | refuta_def={refuta_def} refuta={refuta}', '',
     f'PROMOCION (alfa/4): {"SI" if promo else "NO"} | seguimiento={tok} | IC cierre T1 [1,25%;98,75%] B=4000 todos los dias=({f(plo)},{f(phi)}) req inf>0: {Q.si(IC_ok)} | dias comparables T1-PLA_T1=({f(Q.q(vTb, .0125))},{f(Q.q(vTb, .9875))}) req inf>0: {Q.si(ICc_ok)} | placebo: no aplica',
     '', f'## VEREDICTO: {tok} ({why})', 'Aviso prereg: si el EV viene igual de PLA_T1, el mecanismo es "SOL a 0,13" y no la calma.', 'Exploratorio; no autoriza nada live. Rellenos sin barrido NO se filtran (clasificacion ex post).']
escribir(L, dict(dias=dias, n=n, ev=e, ev100=e100, sin2=s2, ic90_cierre=[lo, hi], ev_pla=ep, ev_g0=eg, nd_T1PLA=ndP, nd_T1G0=ndG, victorias=[kP, kG], veredicto=tok, detalle=why, promocion=promo))
print('\n'.join(L))
