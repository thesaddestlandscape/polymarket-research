"""Evaluador de PREREG_Q11_PISTAS (P-A, P-B) + ADDENDUM_Q11_PISTAS_GIRO/ADDENDUM2/ADDENDUM3 (sha c991602c) + ADDENDUM4 (sha 3dac1bf4: REFUTA R1-R3 con IC90 por cierre y por dia, tabla A-H, tope). Solo lectura; 0 ordenes.
Uso: nice -n 19 ionice -c3 python3 -I eval_pistas.py [--desde 2026-11-06] [--hasta D] [--salida DIR] [--hoy D]
Criterios diarios sobre D_AB, nd_validos>=10, CONFIRMA en dos muestras, estado terminal persistido (salida/estado_P-A.json, estado_P-B.json),
linea PROMOCION (alfa/4). Logica comun: forward_sol013/q11_decision.py. Salida: <salida>/eval_pistas_resultado.txt"""
import sys, os, argparse
sys.path.insert(0, '/root/polymarket-research/misiones/5m_barato/forward_sol013/')
import numpy as np, pandas as pd
import q11_decision as Q
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
ap = argparse.ArgumentParser(); ap.add_argument('--desde', default='2026-11-06'); ap.add_argument('--hasta', default='9999-12-31'); ap.add_argument('--salida', default=HERE); ap.add_argument('--out', default=Q.DEC_OUT); ap.add_argument('--hoy', default=None); ap.add_argument('--cl-cache', default=Q.CL_CACHE)
a = ap.parse_args(); PR = '/root/polymarket-research/data/prices/'; os.makedirs(a.salida, exist_ok=True)
dias, R2, R3, err = Q.cargar_dias(a.out, a.desde, a.hasta)
out = []; P = out.append
_sp, _g = Q.dias_sin_pareja(a.out, a.desde, a.hasta)
if _sp: P(f'AVISO: dias con dec2 sin dec3s100 (o al reves) en la ventana, NO cuentan (no es error): {_sp}')
def cerrar(nombre='eval_pistas_resultado.txt'):   # ERROR_DATOS/sin dias: nombre='eval_pistas_AVISO.txt' (no se sobrescribe el ultimo resultado valido)
    tmp = a.salida + '/.eval_pistas.tmp'; open(tmp, 'w').write('\n'.join(out) + '\n'); os.replace(tmp, a.salida + '/' + nombre); print('\n'.join(out))
def sin_datos(nombres, motivo, err_=None):
    """Salida temprana: NO escribe estado; cada terminal ya emitido se imprime (ADDENDUM4 A) junto al aviso de ERROR_DATOS (sec. 5b)."""
    for nm in nombres:
        tok, why = Q.veredicto_sin_datos(a.salida + f'/estado_{nm}.json', err if err_ is None else err_, a.hoy); P(f'[{nm}] {motivo} | VEREDICTO {nm}: {tok} ({why})')
if err or not dias:
    sin_datos(('P-A', 'P-B'), ('ERROR_DATOS: ' + '; '.join(err[:3]) + ' => INSUFFICIENT (no cuenta ningun dia nuevo)') if err else f'sin dias validos >= {a.desde} (dec2+dec3s100)'); cerrar('eval_pistas_AVISO.txt'); sys.exit(0)
t1 = R2[R2['var'] == 'T1']; s100 = R3[R3['var'] == 'T1']
# ---- P-B: Z (lagj<=3000) vs R (lagj>3000); 3 monedas
def zr(x): return x[x.lagj.notna() & (x.lagj <= 3000)], x[x.lagj > 3000]
Zn, Rn = zr(t1)
Zs, _ = zr(s100)
def extra_B(ds):
    Z = Zn[Zn.dia.isin(ds)]; dz = Q.evdia(Z); k = int((dz < 0).sum())
    return {f'3b EV_d(Z)<0 en >=60 % de dias con Z ({k}/{len(dz)}; min 10)': Q.ok60(k, len(dz)),
            '5 dec3s100 EV_w(Z)<0': Q.lt(Q.ev(Zs[Zs.dia.isin(ds)]))}
tokB, LB, infB = Q.evaluar_par('P-B', ('Z', 'R'), Zn, Rn, dias, err, a.salida + '/estado_P-B.json', a.hoy, extra_B, None, 20261106, p_aplica=False, seed_dia=Q.SEEDS_DIA['P-B'])
plaz = R2[R2['var'] == 'PLA_T1']; Zp, _ = zr(plaz); g0z, _ = zr(R2[R2['var'] == 'G0'])
P(f'[P-B control informativo (no decide)] PLA_T1 Z\': n={len(Zp)} EV_w={Q.f3(Q.ev(Zp))} | G0 Z: n={len(g0z)} EV_w={Q.f3(Q.ev(g0z))} | por moneda Z: ' + ' '.join(f'{c} n={len(Zn[Zn.act==c])} EV={Q.f3(Q.ev(Zn[Zn.act==c]))}' for c in ('ETH', 'SOL', 'XRP')))
out.extend(LB)
# ---- P-A: rasgo rpre1h (Chainlink source=='chainlink', recepcion), ETH
need = sorted(set(dias) | {(pd.Timestamp(x) - pd.Timedelta(days=1)).strftime('%Y-%m-%d') for x in dias})
SC, cl_err = Q.cl_series(need, ('ETH',), a.hoy, a.cl_cache)   # cache propia por dia + una lectura por dia
if cl_err: sin_datos(('P-A',), 'ERROR_DATOS: ' + '; '.join(cl_err[:3]) + ' => INSUFFICIENT (no cuenta ningun dia nuevo; no escribe estado)', cl_err); cerrar(); sys.exit(0)   # P-B (arriba) es valido y se conserva
ms, pp = SC['ETH']
def px(t):
    i = np.searchsorted(ms, t, side='right') - 1; ok = (i >= 0) & (t - ms[np.clip(i, 0, None)] < 20000); return np.where(ok, pp[np.clip(i, 0, None)], np.nan)
e = t1[t1.act == 'ETH']; ar = (e.fin.values * 1000 - 300000 - 3000).astype('int64'); e = e.assign(rp=np.log(px(ar) / px(ar - 3600000)))
P(f'[P-A] ETH T1 filas={len(e)} sin rasgo (excluidas, contadas)={int(e.rp.isna().sum())}'); e = e[e.rp.notna()]
eNO, eYES = e[e.lado == 'NO'], e[e.lado == 'YES']
Hn, Cn = eNO[eNO.rp > 0], eNO[eNO.rp <= 0]
def extra_A(ds):
    No = eNO[eNO.dia.isin(ds)]; Ho, Co = No[No.rp > 0], No[No.rp <= 0]
    y = eYES[eYES.dia.isin(ds)]; vy = Q.vec_dif(y[y.rp > 0], y[y.rp <= 0], 2000, 20261108)   # control negativo YES-ETH: IC90 por cierre del spread C-H incluye 0
    lo, hi = Q.q(vy, .05), Q.q(vy, .95); ctrl = lo == lo and lo <= 0 <= hi
    dC = Q.evdia(Co); dAll = Q.evdia(No); k = int(sum(dC[d] > dAll[d] for d in dC.index if d in dAll.index))
    return {'3b EV_w(C) sin 2 mejores dias > EV_w(H)': Q.gt(Q.sin2(Co, True) - Q.ev(Ho)) if len(Ho) else False,
            f'4b control YES-ETH: IC90 cierre del spread incluye 0 ({Q.f3(lo)},{Q.f3(hi)})': bool(ctrl),
            f'5 EV_w/dia regla(solo C)>sin regla(C+H) en >=60 % ({k}/{len(dC)}; min 10)': Q.ok60(k, len(dC))}
def plac_A(ds):
    No = eNO[eNO.dia.isin(ds)].reset_index(drop=True); return Q.placebo_p(No, No.rp.values, lambda s: s > 0, 1000, 20261106)
tokA, LA, infA = Q.evaluar_par('P-A', ('H', 'C'), Hn, Cn, dias, err, a.salida + '/estado_P-A.json', a.hoy, extra_A, plac_A, 20261106, seed_dia=Q.SEEDS_DIA['P-A'])
out.extend(LA)
cerrar()
