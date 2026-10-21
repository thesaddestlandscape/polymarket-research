#!/usr/bin/env python3
"""h23_analisis_v3.py -- agrega el replay v3 (v3_BTC_D.csv). Solo lectura. EV ponderado por EUR (sum pnl/sum coste), por unidad, IC90 por DIAS (bootstrap de dias, 3000, semilla 7)
SOLO si hay >= 5 dias con relleno (si no: 'IC no estimable'), sin 2 mejores dias, PnL total, 1 relleno por cierre, desenlace oficial (sin desenlace = missing, se cuenta aparte, nunca 0).
Periodos: DISC = 06-18 Oct (13 dias, ya vistos por H23 v1/v2: descubrimiento), OOS = dias >= 19-Oct (no vistos al preregistrar r150). Celda central: cola base, alta 79, cancel 60.
Uso: python3 -I h23_analisis_v3.py [dir] > salida.txt"""
import glob, json, os, sys
import numpy as np, pandas as pd
O = sys.argv[1] if len(sys.argv) > 1 else '/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v3/'
OOS_DESDE = '2026-10-19'
M = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(O + 'v3_BTC_20*.csv')) if os.path.getsize(f) > 0], ignore_index=True)
M['g'] = M.gana.map({True: 1.0, False: 0.0, 'True': 1.0, 'False': 0.0})
M['pnl'] = M.lleno * M.g - M.coste + M.rebate
M['periodo'] = np.where(M.dia >= OOS_DESDE, 'OOS', 'DISC')
rng = np.random.default_rng(7)

def cen(d): return d[(d.cola == 'base') & (d.lat_post == 79) & (d.lat_cancel == 60)]

def ev(f):
    f = f[(f.lleno > 0) & f.g.notna()]
    if not len(f): return dict(n=0)
    d = f.groupby('dia').agg(p=('pnl', 'sum'), c=('coste', 'sum')); D = d.values
    if len(D) >= 5:
        b = [(lambda k: k[:, 0].sum() / k[:, 1].sum())(D[rng.integers(0, len(D), len(D))]) for _ in range(3000)]
        lo, hi = np.percentile(b, 5), np.percentile(b, 95)
    else: lo = hi = float('nan')
    s2 = d.sort_values('p', ascending=False).iloc[2:]
    return dict(n=len(f), dias=len(d), pos=int((d.p > 0).sum()), pnl=f.pnl.sum(), coste=f.coste.sum(), ev=f.pnl.sum() / f.coste.sum(), unit=(f.pnl / f.coste).mean(),
                lo=lo, hi=hi, s2=(s2.p.sum() / s2.c.sum()) if len(s2) and s2.c.sum() > 0 else float('nan'), ns2=len(s2), ac=f.g.mean(), pr=f.coste.sum() / f.lleno.sum())

def fm(d):
    if d['n'] == 0: return 'n=0'
    ic = 'IC90d=(%+.2f,%+.2f)' % (d['lo'], d['hi']) if d['lo'] == d['lo'] else 'IC90d=n/e(<5 dias)'
    s2 = 'sin2mejores=%+.3f(%dd)' % (d['s2'], d['ns2']) if d['s2'] == d['s2'] else 'sin2mejores=n/e'
    return ('n=%2d d=%2d(+%d) PnL=%+7.2f coste=%6.2f EVpond=%+.3f EVunit=%+.3f %s %s acierto=%.2f vs precio=%.2f'
            % (d['n'], d['dias'], d['pos'], d['pnl'], d['coste'], d['ev'], d['unit'], ic, s2, d['ac'], d['pr']))

cob = [json.load(open(c)) for c in sorted(glob.glob(O + 'v3_cobertura_BTC_*.json'))]
print('DIAS', sorted(M.dia.unique()))
print('cobertura (dia, cierres_grupo, con_lado, con_libro, errores, sin_desenlace):', [(c['dia'][5:], c['cierres_grupo'], c['con_lado'], c['con_libro'], c['errores'], c['sin_desenlace']) for c in cob])
print('rellenos sin desenlace oficial (missing, excluidos del EV):', int(M[(M.lleno > 0) & M.g.isna()].groupby(['dia', 'cierre']).ngroups))
REPV = (0, 50, 150, 300, 500, 1500)
for periodo, sub in (('DISC 06-18', M[M.periodo == 'DISC']), ('OOS >=19-Oct', M[M.periodo == 'OOS']), ('TODO', M)):
    if not len(sub): print(f'\n######## {periodo}: SIN DATOS'); continue
    nd = sub.dia.nunique()
    print(f'\n######## {periodo}: {nd} dias {sorted(sub.dia.unique())[0]}..{sorted(sub.dia.unique())[-1]} (celda central; 1 relleno por cierre)')
    for sizing, modo in (('real', 'primer'), ('real', 'acum'), ('2eur', 'acum')):
        print(f'--- sizing={sizing} cierre={modo} ' + ('(PRIMARIO preregistrado: tamano real, universo ejecutable, un relleno cierra la puja)' if (sizing, modo) == ('real', 'primer') else ''))
        for brazo in ('A', 'B'):
            for rep in REPV:
                g = cen(sub[(sub.brazo == brazo) & (sub.sizing == sizing) & (sub.modo == modo) & (sub.rep == rep)])
                d = ev(g)
                print(f'{brazo} r{rep:<5d} cotiz={g[g.n_cotiz > 0].cierre.nunique():3d} rell/d={(g.lleno > 0).sum() / nd:.2f} | {fm(d)}')
    print('--- EMPAREJADO r150 - r1500 (sizing real, primer; cierres con relleno en cualquiera): PnL total, comunes, solo-r150, solo-r1500')
    for brazo in ('A', 'B'):
        for sz, md in (('real', 'primer'), ('real', 'acum')):
            a = cen(sub[(sub.brazo == brazo) & (sub.sizing == sz) & (sub.modo == md) & (sub.rep == 150)]); a = a[(a.lleno > 0) & a.g.notna()].set_index('cierre')
            b = cen(sub[(sub.brazo == brazo) & (sub.sizing == sz) & (sub.modo == md) & (sub.rep == 1500)]); b = b[(b.lleno > 0) & b.g.notna()].set_index('cierre')
            com = a.index.intersection(b.index); sa, sb = a.index.difference(b.index), b.index.difference(a.index)
            print(f'{brazo} {sz}/{md}: n150={len(a)} n1500={len(b)} comunes={len(com)} solo150={len(sa)} (PnL {a.loc[sa].pnl.sum():+.2f}, acierto {a.loc[sa].g.mean() if len(sa) else float("nan"):.2f}) solo1500={len(sb)} (PnL {b.loc[sb].pnl.sum():+.2f}) | PnL150={a.pnl.sum():+.2f} PnL1500={b.pnl.sum():+.2f} delta={a.pnl.sum() - b.pnl.sum():+.2f} | dPnL en comunes={(a.loc[com].pnl - b.loc[com].pnl).sum():+.2f}')
    print('--- SENSIBILIDAD (rango, no se elige): EVpond[n] sizing real/primer, por cola x (alta,cancel)')
    for brazo in ('A', 'B'):
        for rep in (150, 1500):
            cells = []
            for cola in ('opt', 'base', 'cons'):
                for lp, lc in ((79, 60), (79, 150), (254, 60), (254, 150)):
                    g = sub[(sub.brazo == brazo) & (sub.sizing == 'real') & (sub.modo == 'primer') & (sub.rep == rep) & (sub.cola == cola) & (sub.lat_post == lp) & (sub.lat_cancel == lc)]
                    d = ev(g); cells.append(f"{cola[0]}{lp}/{lc}:{d['ev']:+.2f}[{d['n']}]" if d['n'] else f'{cola[0]}{lp}/{lc}:--[0]')
            print(f'{brazo} r{rep:<5d}', ' '.join(cells))
    print('--- RITMO: rellenos/dia (central, real/primer) con IC Poisson 90 % y dias a n=40')
    from scipy.stats import chi2
    for brazo in ('A', 'B'):
        for rep in (150, 300, 1500):
            n = len(cen(sub[(sub.brazo == brazo) & (sub.sizing == 'real') & (sub.modo == 'primer') & (sub.rep == rep) & (sub.lleno > 0)]))
            lo = chi2.ppf(0.05, 2 * n) / 2 / nd if n else 0.0; hi = chi2.ppf(0.95, 2 * n + 2) / 2 / nd
            r = n / nd
            print(f'{brazo} r{rep:<5d} n={n} -> {r:.2f}/dia (IC90 {lo:.2f}-{hi:.2f}) -> n=40 en {40 / r if r else float("inf"):.0f} dias (IC {40 / hi:.0f}-{40 / lo if lo else float("inf"):.0f})')
