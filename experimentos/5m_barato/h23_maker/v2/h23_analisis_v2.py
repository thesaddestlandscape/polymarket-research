#!/usr/bin/env python3
"""h23_analisis_v2.py -- agrega el replay v2 (v2_<COIN>_<D>.csv). Solo lectura. EV ponderado por EUR (sum pnl/sum coste), por unidad, IC90 por DIAS
(bootstrap de dias, 3000, semilla 7), sin 2 mejores dias, PnL total y /dia, cobertura, validacion contra el replay v1, rango de sensibilidad, capacidad (stake),
descriptivo ciego de H61 y alts. Uso: python3 -I h23_analisis_v2.py [dir] > salida.txt"""
import glob, os, sys, json
import numpy as np, pandas as pd
O = sys.argv[1] if len(sys.argv) > 1 else '/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v2/'
V1 = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_maker/'
fs = sorted(f for f in glob.glob(O + 'v2_*_20*.csv') if os.path.getsize(f) > 0)
M = pd.concat([pd.read_csv(f) for f in fs], ignore_index=True)
M['gana_f'] = M.gana.map({True: 1.0, False: 0.0, 'True': 1.0, 'False': 0.0})
M['pnl'] = M.lleno * M.gana_f - M.coste + M.rebate
rng = np.random.default_rng(7)
CEN = dict(cola='base', lat_post=79, lat_cancel=60)
def cen(df, mult=1.0):
    return df[(df.cola == CEN['cola']) & (df.lat_post == 79) & (df.lat_cancel == 60) & (df.mult == mult)]
def ev(g):
    f = g[(g.lleno > 0) & g.gana_f.notna()]
    if not len(f): return dict(n=0)
    d = f.groupby('dia').agg(p=('pnl', 'sum'), c=('coste', 'sum')); D = d.values
    b = [(lambda k: k[:, 0].sum() / k[:, 1].sum())(D[rng.integers(0, len(D), len(D))]) for _ in range(3000)]
    s2 = d.sort_values('p', ascending=False).iloc[2:]
    return dict(n=len(f), dias=f.dia.nunique(), pos=int((d.p > 0).sum()), pnl=f.pnl.sum(), coste=f.coste.sum(), ev=f.pnl.sum() / f.coste.sum(), unit=(f.pnl / f.coste).mean(),
                lo=np.percentile(b, 5), hi=np.percentile(b, 95), s2=(s2.p.sum() / s2.c.sum()) if len(s2) and s2.c.sum() > 0 else float('nan'),
                ac=f.gana_f.mean(), pr=f.coste.sum() / f.lleno.sum())
def fm(d):
    if d['n'] == 0: return 'n=0'
    return ('n=%d d=%d(+%d) PnL=%+.2f coste=%.2f EVpond=%+.3f EVunit=%+.3f IC90d=(%+.2f,%+.2f) sin2mejores=%+.3f acierto=%.2f vs precio=%.2f'
            % (d['n'], d['dias'], d['pos'], d['pnl'], d['coste'], d['ev'], d['unit'], d['lo'], d['hi'], d['s2'], d['ac'], d['pr']))
for coin in sorted(M.coin.unique()):
    m = M[M.coin == coin]
    cob = [json.load(open(c)) for c in sorted(glob.glob(O + f'v2_cobertura_{coin}_*.json'))]
    print(f'\n######## {coin}: dias={sorted(m.dia.unique())}')
    print('cobertura (cierres_grupo/con_lado/con_libro/errores/sin_desenlace):', [(c['dia'][5:], c['cierres_grupo'], c['con_lado'], c['con_libro'], c['errores'], c['sin_desenlace']) for c in cob])
    nd = m.dia.nunique()
    print('rellenos sin desenlace oficial (missing, excluidos del EV):', m[(m.lleno > 0) & m.gana_f.isna()].cierre.nunique())
    if coin == 'BTC':
        print('\n== VALIDACION contra replay v1 (h23_D.csv): r0 == join, r1500d == join_r; todas las filas coinc. (lleno,coste) ==')
        v1 = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(V1 + 'h23_20*.csv')) if os.path.getsize(f) > 0])
        v1 = v1[v1['var'].isin(['join', 'join_r'])].assign(var=lambda d: d['var'].map({'join': 'r0', 'join_r': 'r1500d'}))
        mm = m[(m['var'].isin(['r0', 'r1500d'])) & (m.mult == 1.0)]
        j = v1.merge(mm, on=['cierre', 'brazo', 'var', 'cola', 'lat_post', 'lat_cancel'], how='outer', suffixes=('_1', '_2'), indicator=True)
        j[['lleno_1', 'lleno_2', 'coste_1', 'coste_2']] = j[['lleno_1', 'lleno_2', 'coste_1', 'coste_2']].fillna(0)
        bad = j[(abs(j.lleno_1 - j.lleno_2) > 1e-6) | (abs(j.coste_1 - j.coste_2) > 1e-4)]
        print(f'filas comparadas {len(j)}, solo en v1 {int((j._merge=="left_only").sum())}, solo en v2 {int((j._merge=="right_only").sum())}, distintas {len(bad)}')
        if len(bad): print(bad[['cierre', 'brazo', 'var', 'cola', 'lat_post', 'lat_cancel', 'lleno_1', 'lleno_2']].head(8).to_string())
    print('\n== TABLA PRINCIPAL: celda central (cola base, alta 79, cancel 60), stake 2 EUR ==')
    for brazo in ('A', 'B'):
        for var in ('r0', 'r50', 'r150', 'r500', 'r1500', 'r1500d'):
            g = cen(m[(m.brazo == brazo) & (m['var'] == var)]); q = g[g.n_cotiz > 0]
            print(f'{brazo} {var:6s} cotizados={q.cierre.nunique():3d} ({q.cierre.nunique()/nd:.2f}/d) rellenos/d={(g.lleno>0).sum()/nd:.2f} | {fm(ev(g))} | PnL/dia={ev(g).get("pnl",0)/nd:+.2f}')
    print('\n== EMPAREJADO vs r0 (cierres con relleno): comunes / solo r0 / solo rep ; delta PnL total (rep - r0), celda central ==')
    for brazo in ('A', 'B'):
        b0 = cen(m[(m.brazo == brazo) & (m['var'] == 'r0')]); b0 = b0[(b0.lleno > 0) & b0.gana_f.notna()].set_index('cierre')
        for var in ('r50', 'r150', 'r500', 'r1500'):
            b1 = cen(m[(m.brazo == brazo) & (m['var'] == var)]); b1 = b1[(b1.lleno > 0) & b1.gana_f.notna()].set_index('cierre')
            com = b0.index.intersection(b1.index)
            print(f'{brazo} {var:6s} comunes={len(com)} solo_r0={len(b0.index.difference(b1.index))} solo_{var}={len(b1.index.difference(b0.index))} | PnL r0={b0.pnl.sum():+.2f} {var}={b1.pnl.sum():+.2f} delta={b1.pnl.sum()-b0.pnl.sum():+.2f} | retencion de rellenos {len(b1)/max(len(b0),1):.2f}')
    print('\n== SENSIBILIDAD (rango, no se elige): EVpond [n] por cola x (alta,cancel) ==')
    for brazo in ('A', 'B'):
        for var in ('r0', 'r150', 'r1500'):
            cells = []
            for cola in ('opt', 'base', 'cons'):
                for lp, lc in ((79, 60), (79, 150), (254, 60), (254, 150)):
                    g = m[(m.brazo == brazo) & (m['var'] == var) & (m.cola == cola) & (m.lat_post == lp) & (m.lat_cancel == lc) & (m.mult == 1.0)]
                    d = ev(g); cells.append(f"{cola[0]}{lp}/{lc}:{d['ev']:+.2f}[{d['n']}]" if d['n'] else f'{cola[0]}{lp}/{lc}:--[0]')
            print(f'{brazo} {var:6s}', ' '.join(cells))
    print('\n== CAPACIDAD (H67): stake x, cola base, 79/60 ==')
    for brazo in ('A', 'B'):
        for var in ('r0', 'r150'):
            for mult in (1.0, 2.5, 5.0, 12.5):
                g = cen(m[(m.brazo == brazo) & (m['var'] == var)], mult); f = g[(g.lleno > 0)]
                comp = (f.lleno >= f.need - 1e-6).mean() if len(f) else float('nan')
                d = ev(g)
                print(f'{brazo} {var:5s} stake={2*mult:5.1f}EUR rellenos/d={len(f)/nd:.2f} completos={comp:.2f} coste/d={f.coste.sum()/nd:.2f} PnL/d={d.get("pnl",0)/nd:+.2f} | {fm(d)}')
    if coin == 'BTC':
        print('\n== H61 DESCRIPTIVO CIEGO (sin EV): frecuencia del disparo ret1s_or<0 ==')
        qi = sum(c['q_inst'] for c in cob); qc = sum(c['q_contra'] for c in cob); qz = sum(c['q_cero'] for c in cob); qs = sum(c['q_sinbin'] for c in cob)
        print(f'instantes de cotizacion (brazo A): {qi}; con ret1s<0: {qc} ({qc/max(qi,1):.1%}); ret1s==0: {qz} ({qz/max(qi,1):.1%}); sin dato Binance: {qs} ({qs/max(qi,1):.1%})')
        for brazo in ('A', 'B'):
            g = cen(m[(m.brazo == brazo) & (m['var'] == 'r0')]); f = g[g.lleno > 0]
            k = f.ret1s_or_bps.notna(); neg = (f.ret1s_or_bps < 0)
            print(f'{brazo} rellenos r0 central: n={len(f)}, con dato Binance={int(k.sum())}, con ret1s<0 en el relleno={int(neg.sum())} -> retencion potencial del corte = {1-neg.sum()/max(k.sum(),1):.2f} (cota superior: no cuenta re-pujas posteriores ni rellenos nuevos)')
