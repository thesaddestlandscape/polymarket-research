"""Evaluador de PREREG_Q11_GIRO (P-C) + ADDENDUM_Q11_PISTAS_GIRO/ADDENDUM2/ADDENDUM3 (sha c991602c) + ADDENDUM4 (sha 3dac1bf4). Solo lectura; 0 ordenes.
Uso: nice -n 19 ionice -c3 python3 -I eval_giro.py [--desde 2026-11-06] [--hasta D] [--salida DIR] [--hoy D]
Rasgos Chainlink (source=='chainlink', recepcion) por moneda; a = fin-300-3 s. Estado terminal: <salida>/estado_P-C.json. Salida: <salida>/eval_giro_resultado.txt"""
import sys, os, argparse
sys.path.insert(0, '/root/polymarket-research/misiones/5m_barato/forward_sol013/')
import numpy as np, pandas as pd
import q11_decision as Q
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
ap = argparse.ArgumentParser(); ap.add_argument('--desde', default='2026-11-06'); ap.add_argument('--hasta', default='9999-12-31'); ap.add_argument('--salida', default=HERE); ap.add_argument('--out', default=Q.DEC_OUT); ap.add_argument('--hoy', default=None); ap.add_argument('--cl-cache', default=Q.CL_CACHE)
a = ap.parse_args(); os.makedirs(a.salida, exist_ok=True)
dias, R2, R3, err = Q.cargar_dias(a.out, a.desde, a.hasta)
out = []; P = out.append
_sp, _g = Q.dias_sin_pareja(a.out, a.desde, a.hasta)
if _sp: P(f'AVISO: dias con dec2 sin dec3s100 (o al reves) en la ventana, NO cuentan (no es error): {_sp}')
def cerrar(nombre='eval_giro_resultado.txt'):   # ERROR_DATOS/sin dias: nombre='eval_giro_AVISO.txt' (no se sobrescribe el ultimo resultado valido)
    tmp = a.salida + '/.eval_giro.tmp'; open(tmp, 'w').write('\n'.join(out) + '\n'); os.replace(tmp, a.salida + '/' + nombre); print('\n'.join(out))
def sin_datos(motivo, err_=None):
    """Salida temprana: NO escribe estado; un terminal ya emitido se imprime (ADDENDUM4 A) junto al aviso de ERROR_DATOS (sec. 5b)."""
    tok, why = Q.veredicto_sin_datos(a.salida + '/estado_P-C.json', err if err_ is None else err_, a.hoy); P(f'[P-C] {motivo} | VEREDICTO P-C: {tok} ({why})')
if err or not dias:
    sin_datos(('ERROR_DATOS: ' + '; '.join(err[:3]) + ' => INSUFFICIENT (no cuenta ningun dia nuevo)') if err else f'sin dias validos >= {a.desde} (dec2+dec3s100)'); cerrar('eval_giro_AVISO.txt'); sys.exit(0)
t1 = R2[(R2['var'] == 'T1') & (R2.lado == 'NO')].copy()
need = sorted({(pd.Timestamp(x) - pd.Timedelta(days=k)).strftime('%Y-%m-%d') for x in dias for k in (0, 1)})   # r4 = 5 h atras desde fin-303 s: basta el dia y el anterior
S, cl_err = Q.cl_series(need, Q.COINS, a.hoy, a.cl_cache)   # cache propia por dia (CSV de data/prices rota a ~20 d) + una lectura por dia
if cl_err:
    sin_datos('ERROR_DATOS: ' + '; '.join(cl_err[:3]) + ' => INSUFFICIENT (no cuenta ningun dia nuevo; no escribe estado)', cl_err); cerrar('eval_giro_AVISO.txt'); sys.exit(0)
def px(coin, t):
    ms, pp = S[coin]; i = np.searchsorted(ms, t, side='right') - 1; ok = (i >= 0) & (t - ms[np.clip(i, 0, None)] < 20000); return np.where(ok, pp[np.clip(i, 0, None)], np.nan)
r1 = np.full(len(t1), np.nan); r4 = np.full(len(t1), np.nan)
for coin in ('ETH', 'SOL', 'XRP'):
    m = (t1.act == coin).values; ar = (t1.fin.values[m] * 1000 - 303000).astype('int64'); r1[m] = np.log(px(coin, ar) / px(coin, ar - 3600000)); r4[m] = np.log(px(coin, ar - 3600000) / px(coin, ar - 18000000))
t1['r1'] = r1; t1['r4'] = r4; P(f'[P-C] T1 NO filas={len(t1)} sin rasgo (excluidas, contadas)={int(np.isnan(r1 + r4).sum())}'); t1 = t1[t1.r1.notna() & t1.r4.notna()].reset_index(drop=True)
hm = (t1.r1 > 0) & (t1.r4 < 0); Hn, Cn = t1[hm], t1[~hm]
def extra_C(ds):
    H = Hn[Hn.dia.isin(ds)]; dh = Q.evdia(H); k = int((dh < 0).sum())
    nc = sum(1 for c in ('ETH', 'SOL', 'XRP') if Q.lt(Q.ev(H[H.act == c])))
    return {f'3b EV_d(H)<0 en >=60 % de dias con H ({k}/{len(dh)}; min 10)': Q.ok60(k, len(dh)), f'5 EV_w(H)<0 en >=2 de 3 monedas ({nc}/3)': nc >= 2}
def plac_C(ds):
    d = t1[t1.dia.isin(ds)].reset_index(drop=True); r4d = d.r4.values   # permuta el signo de r1 dentro de dia
    return Q.placebo_p(d, np.sign(d.r1.values), lambda s: (s > 0) & (r4d < 0), 1000, 20261106)
tok, L, inf = Q.evaluar_par('P-C', ('H', 'C'), Hn, Cn, dias, err, a.salida + '/estado_P-C.json', a.hoy, extra_C, plac_C, 20261106, seed_dia=Q.SEEDS_DIA['P-C'])
out.extend(L); out.extend(f'  info {c}: n(H)={len(Hn[Hn.act == c])} EV_w={Q.f3(Q.ev(Hn[Hn.act == c]))}' for c in ('ETH', 'SOL', 'XRP')); cerrar()
