#!/usr/bin/env python3
"""d5_markout_retirada.py -- EXTRA EXPLORATORIO (NO preregistrado; decidido tras ver el resultado de d2: F-exit 73 % vs R 11 % / P 26 %). Pregunta: ¿la retirada de competidores PREDICE un movimiento
adverso del precio incluso SIN que nos rellenen? (separa la lectura «informacion» de la lectura «superviviente/mecanica»). Markout = mid del token c (largo) a t+1/+5/+30 s menos mid(t),
con el top por recepcion. Eventos: B (R, P, F de control_b_eventos.csv) y una muestra de 600 mercados de la poblacion (controles C y prints E con S1000>=5). Compara exit=1 vs exit=0 dentro de
los grupos SIN relleno nuestro (R, P, C). IC90 por cierre (bootstrap) y placebo (barajar exit dentro de mercado/estrato). Salida datos/markout_retirada.txt"""
import os, sys, glob, json, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); DL = '/root/polymarket-research-datalogs/cola_posicion/'
sys.path.insert(0, AQ); import d1_l2_motor as M
rng = np.random.default_rng(20261022); out = []
def P(*a): out.append(' '.join(str(x) for x in a))
TOK = {}
for l in open(DL + 'snap/ledger_B.jsonl'):
    d = json.loads(l)
    if d.get('tipo') == 'intencion_post': TOK[d['oid']] = d['tok']
def mid_at(tp, L, t):
    O = 'N' if L == 'Y' else 'Y'; b = M.best(tp, L, t); o = M.best(tp, O, t)
    return (b + (1000 - o)) / 2000 if (b > 0 and o > 0) else np.nan
def marks(tp, L, t):
    m0 = mid_at(tp, L, t); return [mid_at(tp, L, t + h) - m0 for h in (1000, 5000, 30000)]
rows = []
B = pd.read_csv(os.path.join(D, 'control_b_eventos.csv')); B['act'] = None; B['mid'] = None
for i, o in B.iterrows(): act, mid, lado, fin = M.TM[TOK[o.oid]]; B.at[i, 'act'] = act; B.at[i, 'mid'] = mid
for (act, mid), g in B.groupby(['act', 'mid']):
    tp = M.carga(M.MK + f'{act}_{mid}.gz')[2]
    for _, o in g.iterrows():
        mk = marks(tp, o.L, int(o.t)); rows.append(dict(fuente='B', grp=o.grp, exit=o['exit'], alone=o.alone, fin=o.fin, coin=o.coin, mid=mid, m1=mk[0], m5=mk[1], m30=mk[2]))
E = pd.concat([pd.read_csv(f, low_memory=False, usecols=['grp', 's1ok', 'mid', 'act', 'L', 'fin', 'r', 'q', 'S1000', 'S150', 'cons', 'banda']) for f in sorted(glob.glob(DL + 'l2_eventos_*.csv.gz'))], ignore_index=True)
E['s1ok'] = E.s1ok.fillna(1); E = E[E.s1ok == 1]; E['mid'] = E.mid.astype(str)
mids = E[['act', 'mid']].drop_duplicates(); mids = mids.sample(min(600, len(mids)), random_state=1)
E = E.merge(mids, on=['act', 'mid'])
E['exit'] = ((E.S1000 >= 5) & ((E.S1000 - E.cons - E.S150) >= 0.8 * E.S1000)).astype(int); E['alone'] = (E.S150 <= 0.5).astype(int)
for (act, mid), g in E.groupby(['act', 'mid']):
    tp = M.carga(M.MK + f'{act}_{mid}.gz')[2]
    for _, o in g.iterrows():
        mk = marks(tp, o.L, int(o.r)); rows.append(dict(fuente='POP', grp=o.grp, exit=o['exit'], alone=o.alone, fin=o.fin, coin=act, mid=mid, m1=mk[0], m5=mk[1], m30=mk[2], banda=o.banda))
X = pd.DataFrame(rows); X.to_csv(os.path.join(D, 'markout_retirada_eventos.csv'), index=False)
def bootd(df, col, nb=1000):
    gi = {c: x.index.values for c, x in df.groupby('fin')}; cl = list(gi); v = []
    for _ in range(nb):
        s = df.loc[np.concatenate([gi[c] for c in rng.choice(cl, len(cl))])]
        a = s[s.exit == 1][col].mean(); b = s[s.exit == 0][col].mean(); v.append(a - b)
    return np.nanpercentile(v, [5, 95])
def placebo(df, col, key, nperm=1000):
    d0 = df[col].values; e0 = df.exit.values.copy(); obs = np.nanmean(d0[e0 == 1]) - np.nanmean(d0[e0 == 0]); idx = df.groupby(key).indices; v = []
    for _ in range(nperm):
        e = e0.copy()
        for k, ix in idx.items(): e[ix] = rng.permutation(e0[ix])
        v.append(np.nanmean(d0[e == 1]) - np.nanmean(d0[e == 0]))
    return obs, float((np.array(v) <= obs).mean())
P('Markout del mid del token c (largo; unidades de precio, 0,01 = 1 c) tras la retirada. exit=1 vs exit=0. NEGATIVO = el precio se mueve contra quien este largo (adverso).')
for nom, sub in (('B sin relleno (R+P)', X[(X.fuente == 'B') & X.grp.isin(['R', 'P'])]), ('B solo R', X[(X.fuente == 'B') & (X.grp == 'R')]), ('B solo P', X[(X.fuente == 'B') & (X.grp == 'P')]),
                 ('POP controles C banda A', X[(X.fuente == 'POP') & (X.grp == 'C') & (X.banda == 'A')]), ('POP controles C banda B', X[(X.fuente == 'POP') & (X.grp == 'C') & (X.banda == 'B')]),
                 ('POP prints E banda A', X[(X.fuente == 'POP') & (X.grp == 'E') & (X.banda == 'A')]), ('B rellenos F', X[(X.fuente == 'B') & (X.grp == 'F')])):
    sub = sub.reset_index(drop=True)
    if sub.exit.sum() < 5 or (sub.exit == 0).sum() < 5: P(f'{nom}: n insuficiente (exit=1: {int(sub.exit.sum())})'); continue
    for col in ('m1', 'm5', 'm30'):
        a = sub[sub.exit == 1][col].mean(); b = sub[sub.exit == 0][col].mean(); ic = bootd(sub, col); obs, p = placebo(sub, col, 'mid')
        P(f'{nom:26s} {col:3s}: exit=1 {a:+.4f} (n={int((sub.exit==1).sum())}) vs exit=0 {b:+.4f} (n={int((sub.exit==0).sum())}); dif {a-b:+.4f} IC90 cierre ({ic[0]:+.4f},{ic[1]:+.4f}); placebo (barajar exit dentro de mercado) p(<=obs)={p:.3f}')
open(os.path.join(D, 'markout_retirada.txt'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
