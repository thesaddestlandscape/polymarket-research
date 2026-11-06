#!/usr/bin/env python3
"""Juez forward H-Q11-SOL013 (PREREG_Q11_SOL013.md, congelado). Solo lectura de dec2_D/dec3s100_D.pkl; 0 ordenes.
Regla: act=='SOL', L==0.13, variante T1 (dec2) y T1 a -100 ms (dec3s100); comparadores PLA_T1 y G0. Dias que cuentan >= 2026-11-06 con AMBOS pkl.
Uso: filtro_sol013.py [--desde D] [--hasta D] [--salida DIR]  (ensayo sobre gastados: --desde 2026-10-26 --salida /ruta/ensayo)"""
import sys, os, glob, json, argparse, datetime as dt, numpy as np, pandas as pd
OUT = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/A3_guarda/ret_cinta_corregida/descomp/out/'
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
ap = argparse.ArgumentParser(); ap.add_argument('--desde', default='2026-11-06'); ap.add_argument('--hasta', default='9999-12-31'); ap.add_argument('--salida', default=HERE); ap.add_argument('--out', default=OUT)
a = ap.parse_args(); rng = np.random.default_rng(13)
dias = sorted(os.path.basename(f)[5:15] for f in glob.glob(a.out + 'dec2_*.pkl') if os.path.exists(a.out + 'dec3s100_' + os.path.basename(f)[5:]))
dias = [d for d in dias if a.desde <= d <= a.hasta]
def cargar(pref):
    R = [pd.read_pickle(f'{a.out}{pref}_{d}.pkl') for d in dias]
    R = pd.concat(R, ignore_index=True) if R else pd.DataFrame()
    return R[(R.act == 'SOL') & ((R.L - 0.13).abs() < 1e-9)] if len(R) else R
if not dias:
    os.makedirs(a.salida, exist_ok=True); open(a.salida + '/RESUMEN.md', 'w').write(f'# RESUMEN H-Q11-SOL013 (generado {dt.datetime.now(dt.timezone.utc):%FT%TZ})\nDias validos desde {a.desde}: 0 (aun no hay dec2+dec3s100 de dias que cuenten)\n## VEREDICTO: INSUFFICIENT\n'); print('0 dias validos'); sys.exit(0)
R2, R3 = cargar('dec2'), cargar('dec3s100')
def sel(R, v): return R[R['var'] == v] if len(R) else R
def ev(x): return x.pnl.sum() / x.cost.sum() if len(x) and x.cost.sum() > 0 else float('nan')
def sin2(x):  # quita los 2 mejores dias por PNL (criterio del informe Q11)
    g = x.groupby('dia')[['pnl', 'cost']].sum()
    if len(g) <= 2: return float('nan')
    r = g.drop(g.pnl.sort_values(ascending=False).index[:2]); return r.pnl.sum() / r.cost.sum() if r.cost.sum() > 0 else float('nan')
def ic90_cierre(x, B=4000):  # bootstrap por cierre (fin) del ratio sum(pnl)/sum(cost)
    if not len(x): return (float('nan'),) * 2
    g = x.groupby('fin')[['pnl', 'cost']].sum().values
    if len(g) < 3: return (float('nan'),) * 2
    i = rng.integers(0, len(g), (B, len(g))); s = g[i].sum(axis=1); e = s[:, 0] / s[:, 1]; return tuple(np.quantile(e, [.05, .95]))
def evdia(x): g = x.groupby('dia')[['pnl', 'cost']].sum(); return g.pnl / g.cost
T1, PLA, G0, S100 = sel(R2, 'T1'), sel(R2, 'PLA_T1'), sel(R2, 'G0'), sel(R3, 'T1')
nd = len(dias); n = len(T1)
e, ep, eg, e100 = ev(T1), ev(PLA), ev(G0), ev(S100); s2 = sin2(T1); lo, hi = ic90_cierre(T1)
dT, dP, dG = evdia(T1), evdia(PLA), evdia(G0)
def frac(dA, dB):  # fraccion de dias VALIDOS con EV(A)>EV(B); dia sin relleno de A = no cuenta a favor (conservador)
    return float(np.mean([(d in dA.index and (d not in dB.index or dA[d] > dB[d])) for d in dias])) if dias else float('nan')
fP, fG = frac(dT, dP), frac(dT, dG)
gt = lambda v, t=0.0: bool(v == v and v > t)
cond = {'EV>0': gt(e), 'EV(-100ms)>0': gt(e100), 'EV sin 2 mejores dias>0': gt(s2), 'IC90 cierre inf>0': gt(lo), 'EV(T1)>EV(PLA_T1) agregado': gt(e - ep) if ep == ep else False,
        'EV(T1)>EV(G0) agregado': gt(e - eg) if eg == eg else False, 'T1>PLA_T1 en >=60% dias': gt(fP, .599), 'T1>G0 en >=60% dias': gt(fG, .599)}
plaok = ep == ep and PLA.dia.nunique() > 2  # ADDENDUM_Q11_SOL013 (2): comparador sin dato (NaN o <=2 dias con rellenos) => INSUFFICIENT, nunca REFUTA
if not plaok: veredicto = 'INSUFFICIENT (comparador PLA_T1 sin dato suficiente; no avanza hacia REFUTED)'
elif nd >= 10 and n >= 40 and all(cond.values()): veredicto = 'CONFIRMA (PROMISING; micro-real solo con OK Javi; SOLVED exige validador independiente)'
elif s2 != s2: veredicto = 'INSUFFICIENT (T1 con <=2 dias con rellenos: sin2 no definido; no REFUTA ni avanza hacia REFUTED)'  # ADDENDUM2 (5)
elif nd >= 10 and (not gt(e) or not gt(s2) or not gt(e - ep if ep == ep else float('nan'))): veredicto = 'REFUTA' + (' (>=20 dias)' if nd >= 20 else '')
elif nd >= 20: veredicto = 'REFUTED (20 dias sin cumplir)'
else: veredicto = 'INSUFFICIENT'
sw = T1[T1.nmk >= 3]; ns = T1[T1.nmk < 3]
f = lambda v: 'nan' if v != v else f'{v:+.3f}'
L = [f'# RESUMEN H-Q11-SOL013 (generado {dt.datetime.now(dt.timezone.utc):%FT%TZ})', f'Prereg PREREG_Q11_SOL013.md (no modificar). Rango: {a.desde}..{a.hasta}. Fuente: {a.out}', '',
     f'Dias validos (dec2+dec3s100): {nd} {dias[0] if dias else None}..{dias[-1] if dias else None}; con rellenos T1: {len(dT)}',
     f'T1 SOL L=0,13: n={n} rellenos, mercados={T1.mkt.nunique() if n else 0}, cierres={T1.fin.nunique() if n else 0}, coste={T1.cost.sum():.1f} EUR, pnl={T1.pnl.sum():.2f}',
     f'EV ponderado por EUR (sum pnl/sum coste): T1 {f(e)} | -100 ms {f(e100)} (n={len(S100)}) | sin 2 mejores dias {f(s2)} | IC90 por cierre ({f(lo)}, {f(hi)})',
     f'EV por unidad (media pnl/coste): {f((T1.pnl / T1.cost).mean()) if n else "nan"}; dias +: {int((T1.groupby("dia").pnl.sum() > 0).sum())}/{len(dT)}',
     f'Comparadores: PLA_T1 n={len(PLA)} EV {f(ep)} (sin2 {f(sin2(PLA))}) | G0 n={len(G0)} EV {f(eg)} (sin2 {f(sin2(G0))})',
     f'T1>PLA_T1 en {fP:.0%} de dias | T1>G0 en {fG:.0%} de dias',
     f'DIAGNOSTICO barrido (nmk>=3): {len(sw)} rellenos EV {f(ev(sw))}; resto {len(ns)} EV {f(ev(ns))} (no es regla de decision)',
     '', '## Gates (todos exigidos con >=10 dias y n>=40)'] + [f'- [{"x" if v else " "}] {k}' for k, v in cond.items()] + [f'- dias>=10: {nd >= 10} | n>=40: {n >= 40}', '',
     f'## VEREDICTO: {veredicto}', 'Aviso prereg: si el EV viene igual de PLA_T1, el mecanismo es "SOL a 0,13" y no la calma.', 'Exploratorio; no autoriza nada live. Rellenos sin barrido NO se filtran (clasificacion ex post).']
os.makedirs(a.salida, exist_ok=True); tmp = a.salida + '/.RESUMEN.tmp'; open(tmp, 'w').write('\n'.join(L) + '\n'); os.replace(tmp, a.salida + '/RESUMEN.md')
json.dump(dict(dias=dias, n=n, ev=e, ev100=e100, sin2=s2, ic90_cierre=[lo, hi], ev_pla=ep, ev_g0=eg, veredicto=veredicto), open(a.salida + '/resumen.json', 'w'), indent=1, default=float)
print('\n'.join(L))
