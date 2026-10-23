#!/usr/bin/env python3
"""c11_posicion_ev.py -- PREREG_COLA (sha a72007c5...), pregunta 4. EV (Σpnl/Σcoste, ponderado por EUR) por posicion en la rafaga (POS1) en la poblacion 17-22 Oct (sin B) y B descriptivo.
Contraste primario ATRAS-FRENTE; IC90 por dia y por cierre; placebo (permutar POS1 dentro del mismo mercado y dentro de (mercado,c)); sin 2 mejores dias; mitades.
Secundarios: ATRAS vs resto, SOLO vs multi, terciles de profundidad de la rafaga; B por terciles de A0. Salida datos/posicion_ev.txt"""
import os, glob, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_COLA.md'), 'rb').read()).hexdigest().startswith('a72007c5deecc5e7')
pd.set_option('display.width', 220)
U = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(os.path.join(D, 'pop_units_*.csv.gz')))], ignore_index=True)
sin_des = int(U[U.es_b == 0].gana.isna().sum()); Ub = U[U.es_b == 1]; U = U[(U.es_b == 0) & U.gana.notna()].copy()
U['depth'] = U.sh_ahead_same + U.sh_better
rng = np.random.default_rng(20261022); out = []
def P(*a): out.append(' '.join(str(x) for x in a))
def ev(df): c = df.coste.sum(); return df.pnl.sum() / c if c > 0 else np.nan
def diff(a, b): return ev(a) - ev(b)
def boot(df, key, la, lb, nb=2000):
    g = df.groupby(key)
    gi = [x.index.values for _, x in g]; v = []
    for _ in range(nb):
        idx = np.concatenate([gi[i] for i in rng.integers(0, len(gi), len(gi))]); s = df.loc[idx]
        v.append(diff(s[s.pos1.isin(la)], s[s.pos1.isin(lb)]))
    return np.nanpercentile(v, [5, 95])
def sin2(df, la, lb):
    d = df.groupby('dia').pnl.sum().sort_values().index[:-2]; s = df[df.dia.isin(d)]
    return diff(s[s.pos1.isin(la)], s[s.pos1.isin(lb)])
def placebo(df, la, lb, key, nperm=2000):
    d = df[df.pos1.isin(la + lb)].copy().sort_values(key).reset_index(drop=True)
    codes = pd.factorize(d[key].astype(str).agg('|'.join, axis=1) if isinstance(key, list) else d[key])[0]
    lab = d.pos1.isin(la).values; pnl = d.pnl.values; cost = d.coste.values
    def stat(m): return pnl[m].sum() / cost[m].sum() - pnl[~m].sum() / cost[~m].sum()
    obs = stat(lab); v = []
    for _ in range(nperm):
        idx = np.lexsort((rng.random(len(d)), codes)); m = lab[idx]; v.append(stat(m))
    v = np.array(v); return obs, (v <= obs).mean(), (v >= obs).mean(), v.mean()
P(f'Poblacion 17-22 Oct (ETH/SOL/XRP 5m, pc 0,10-0,30, T 60-300, 5 acc por maker-mercado-lado, sin B): unidades {len(U)} (sin desenlace excluidas: {sin_des}); coste {U.coste.sum():.0f} EUR; EV global {ev(U):+.4f}')
t = U.groupby('pos1').apply(lambda d: pd.Series(dict(n=len(d), coste=d.coste.sum(), ev=ev(d), hit=d.gana.mean(), pc=d.pc.mean()))).round(4)
P(t.to_string())
P('\nEV por clase y dia (n unidades):'); P(U.pivot_table(index='pos1', columns='dia', values='pnl', aggfunc='sum').div(U.pivot_table(index='pos1', columns='dia', values='coste', aggfunc='sum')).round(3).to_string())
def contraste(nom, la, lb, primario=False):
    a = U[U.pos1.isin(la)]; b = U[U.pos1.isin(lb)]
    d = diff(a, b); icd = boot(U, 'dia', la, lb); icc = boot(U, 'fin', la, lb)
    s2 = sin2(U, la, lb); h1 = U[U.dia <= '2026-10-19']; h2 = U[U.dia >= '2026-10-20']
    d1 = diff(h1[h1.pos1.isin(la)], h1[h1.pos1.isin(lb)]); d2 = diff(h2[h2.pos1.isin(la)], h2[h2.pos1.isin(lb)])
    o, pl, pg, pm = placebo(U, la, lb, 'mid'); o2, pl2, pg2, pm2 = placebo(U, la, lb, ['mid', 'c'])
    P(f'\n{"PRIMARIO " if primario else ""}{nom}: n {len(a)} vs {len(b)}; EV {ev(a):+.4f} vs {ev(b):+.4f}; diferencia {d:+.4f}')
    P(f'   IC90 por dia ({icd[0]:+.3f},{icd[1]:+.3f}) | por cierre ({icc[0]:+.3f},{icc[1]:+.3f}) | sin 2 mejores dias {s2:+.4f} | mitades 17-19 {d1:+.4f} / 20-22 {d2:+.4f}')
    P(f'   placebo dentro de mercado: p(<=obs)={pl:.3f} p(>=obs)={pg:.3f} (media placebo {pm:+.4f}) | dentro de (mercado,lado): p(<=)={pl2:.3f} p(>=)={pg2:.3f} (media {pm2:+.4f})')
    return d, icd, icc, s2, d1, d2, pl
r = contraste('ATRAS - FRENTE', ['ATRAS'], ['FRENTE'], True)
adv = (r[0] < 0 and r[1][1] < 0 and r[2][1] < 0 and r[6] < 0.10 and r[4] < 0 and r[5] < 0 and r[3] < 0)
fav = (r[0] > 0 and r[1][0] > 0 and r[2][0] > 0 and r[4] > 0 and r[5] > 0 and r[3] > 0)
P(f'   REGLA PRE-REGISTRADA «ATRAS es adversa»: {"CUMPLE" if adv else "NO CUMPLE"} (mismo sentido contrario, ATRAS mejor, con todos los criterios: {fav})')
contraste('ATRAS - (SOLO+FRENTE+CENTRO)', ['ATRAS'], ['SOLO', 'FRENTE', 'CENTRO'])
contraste('SOLO - multi (FRENTE+CENTRO+ATRAS)', ['SOLO'], ['FRENTE', 'CENTRO', 'ATRAS'])
# terciles de profundidad de la rafaga (acciones con prioridad delante de nosotros en la rafaga: mismo nivel + mejor precio)
Dm = U.copy(); Dm['ter'] = pd.cut(Dm.depth, [-1, 0.0001, 20, 1e9], labels=['0 (primero absoluto)', '(0-20]', '>20'])
P('\nPROFUNDIDAD de la rafaga hasta nosotros (acc con prioridad delante: mismo nivel + mejor precio):'); P(Dm.groupby('ter', observed=True).apply(lambda d: pd.Series(dict(n=len(d), coste=round(d.coste.sum()), ev=round(ev(d), 4), hit=round(d.gana.mean(), 3)))).to_string())
Dm['beyond'] = pd.cut(Dm.sh_beyond, [-1, 0.0001, 10, 1e9], labels=['0 (la rafaga acaba en nosotros)', '(0-10]', '>10'])
P('\nPROFUNDIDAD hacia DETRAS (acc despues de nosotros en la misma rafaga, nivel igual o peor):'); P(Dm.groupby('beyond', observed=True).apply(lambda d: pd.Series(dict(n=len(d), coste=round(d.coste.sum()), ev=round(ev(d), 4), hit=round(d.gana.mean(), 3)))).to_string())
# B descriptivo
Bc = pd.read_csv(os.path.join(D, 'b_cola.csv')); Bc = Bc[Bc.gana.notna()]
Bc['pos1'] = np.where(Bc.n_same == 1, 'SOLO', np.where(Bc.rank_same == 0, 'FRENTE', np.where(Bc.rank_same == Bc.n_same - 1, 'ATRAS', 'CENTRO')))
P(f'\nB real (descriptivo, n={len(Bc)} posiciones con desenlace, EV global {ev(Bc):+.3f}):')
P(Bc.groupby('pos1').apply(lambda d: pd.Series(dict(n=len(d), coste=round(d.coste.sum(), 1), ev=round(ev(d), 3), hit=round(d.gana.mean(), 3)))).to_string())
Bc['terA0'] = pd.cut(Bc.A0, [-1, 0.5, 30, 1e9], labels=['A0=0', '0<A0<=30', 'A0>30'])
P('B por A0 al postear:'); P(Bc.groupby('terA0', observed=True).apply(lambda d: pd.Series(dict(n=len(d), coste=round(d.coste.sum(), 1), ev=round(ev(d), 3), hit=round(d.gana.mean(), 3)))).to_string())
Bc['sol'] = Bc.otros_m100.apply(lambda x: 'otros<=0.5 en -100ms' if x <= 0.5 else ('otros presentes' if x == x else 'sin dato'))
P('B por presencia de otros en el nivel 100 ms antes de la rafaga:'); P(Bc.groupby('sol').apply(lambda d: pd.Series(dict(n=len(d), coste=round(d.coste.sum(), 1), ev=round(ev(d), 3), hit=round(d.gana.mean(), 3)))).to_string())
open(os.path.join(D, 'posicion_ev.txt'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
