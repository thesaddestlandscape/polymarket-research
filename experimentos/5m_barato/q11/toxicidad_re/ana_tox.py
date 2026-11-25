#!/usr/bin/env python3
"""RE-Q11 toxicidad del fill (05-Nov). EXPLORATORIO sobre dias GASTADOS. Implementa DISENO_TOX.md (sha 07bde82a...). Uso: python3 -I ana_tox.py > out/ana_tox.log"""
import os, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; BC = H + '../barrido_corr/out/'
DEC = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/A3_guarda/ret_cinta_corregida/descomp/out/'
A = pd.read_pickle(BC + 'A_all.pkl'); MK = pd.read_pickle(H + 'out/MK.pkl')
mk = MK[MK.src == 'G0'].reset_index(drop=True); assert len(mk) == len(A) and (mk.tf.values == A.tf.values).all()
for c in mk.columns:
    if c[:3] in ('m30', 'p1_', 'p10', 'p60', 'arr'): A[c] = mk[c].values
dec = pd.concat([pd.read_pickle(DEC + f'dec2_{d}.pkl') for d in sorted(A.dia.unique())]); dec = dec[dec['var'] == 'G0']
dec = dec.assign(L2=dec.L.round(2), q6=dec.q.round(6)).drop_duplicates(['k', 'L2', 'tf', 'q6'])[['k', 'L2', 'tf', 'q6', 'edad', 'lagj']]
A = A.assign(L2=A.L.round(2), q6=A.q.round(6)).merge(dec, on=['k', 'L2', 'tf', 'q6'], how='left')
print('union dec2: edad missing', int(A.edad.isna().sum()), 'de', len(A), '| chequeo bid tf-300 motor vs g300_bid: dif max', float(np.nanmax(np.abs(A.m300_bid - A.g300_bid))))
A = A[~A.blq.astype(bool)].copy(); print('sin blq n', len(A), 'cierres', A.fin.nunique(), 'dias', A.dia.nunique())
A['rel'] = A.g300_bid - A.L; A['m0'] = (A.g300_bid + A.g300_ask) / 2
A['edad2'] = A.tf - (A.t_dec + 68)
print('edad dec2 vs tf-t_arr: dif max', float(np.nanmax(np.abs(A.edad - A.edad2))))
rng = np.random.default_rng(7)
def ev(x): c = x.cost.sum(); return x.pnl.sum() / c if c > 0 else np.nan
def boot_dif(df, lab, B=4000, by='fin'):
    g = df.assign(lab=lab).groupby([by, 'lab']).agg(p=('pnl', 'sum'), c=('cost', 'sum')).unstack(fill_value=0.0)
    P1, C1, P0, C0 = g[('p', True)].values, g[('c', True)].values, g[('p', False)].values, g[('c', False)].values
    n = len(g); idx = rng.integers(0, n, (B, n))
    d = P1[idx].sum(1) / C1[idx].sum(1) - P0[idx].sum(1) / C0[idx].sum(1)
    return np.nanpercentile(d, [1.25, 5, 95, 98.75])
def perm_p(df, lab, obs, N=1000):
    lab = np.asarray(lab); grp = (df.dia.astype(str) + df.act.astype(str)).values; cnt = 0; pnl = df.pnl.values; cost = df.cost.values
    gi = pd.Series(np.arange(len(df))).groupby(grp).indices
    for _ in range(N):
        l2 = lab.copy()
        for ii in gi.values(): l2[ii] = rng.permutation(lab[ii])
        d = pnl[l2].sum() / cost[l2].sum() - pnl[~l2].sum() / cost[~l2].sum()
        cnt += abs(d) >= abs(obs) - 1e-12
    return (cnt + 1) / (N + 1)
def decomp(x):
    ok = np.isfinite(x.m0.values); c = x.cost.values[ok].sum(); q = x.q.values[ok]
    r = dict(n=len(x), ev=ev(x), cob_m0=ok.mean(), desc=(q * (x.m0.values[ok] - x.L.values[ok])).sum() / c, info=(q * (x.gana.values[ok] - x.m0.values[ok])).sum() / c)
    for h in ('p1', 'p10', 'p60'):
        m = (x[h + '_bid'] + x[h + '_ask']).values / 2; o = ok & np.isfinite(m)
        r['mk_' + h] = (x.q.values[o] * (m[o] - x.m0.values[o])).sum() / x.cost.values[o].sum() if o.any() else np.nan
    return r
def fmt(r): return ' '.join(f'{k} {v:+.3f}' if isinstance(v, float) else f'{k} {v}' for k, v in r.items())
BEST2 = A.groupby('dia').pnl.sum().nlargest(2).index.tolist(); print('2 mejores dias de G0:', BEST2)
print('\n== G0 total:', fmt(decomp(A)), '| pnl', round(A.pnl.sum(), 1))
K = {'K1_posicion rel<=+0,005': (A.rel <= 0.005) & A.rel.notna(), 'K2_edad<=3s': A.edad <= 3000, 'K3_lagj<=3s': A.lagj <= 3000, 'K4_T>=150': A['T'] >= 150}
VALID = {'K1_posicion rel<=+0,005': A.rel.notna(), 'K2_edad<=3s': A.edad.notna(), 'K3_lagj<=3s': A.lagj.notna(), 'K4_T>=150': A['T'].notna()}
print('\n== CONTRASTES PRINCIPALES (dif = EV(grupo) - EV(resto); IC cierre 1,25/5/95/98,75; IC dia 5/95; placebo dia x moneda)')
for nm, lab in K.items():
    v = VALID[nm].values; df = A[v]; l = lab.values[v].astype(bool)
    e1, e0 = ev(df[l]), ev(df[~l]); dif = e1 - e0
    ic = boot_dif(df, l); icd = boot_dif(df, l, by='dia')[[1, 2]]; p = perm_p(df, l, dif)
    dd = df[~df.dia.isin(BEST2)]; ld = l[~df.dia.isin(BEST2)]; dif2 = ev(dd[ld]) - ev(dd[~ld])
    pd_ = df.assign(l=l).groupby('dia').apply(lambda x: ev(x[x.l]) - ev(x[~x.l]) if x.l.any() and (~x.l).any() else np.nan)
    print(f'{nm}: n {l.sum()}/{(~l).sum()} cierres {df[l].fin.nunique()}/{df[~l].fin.nunique()} | EV {e1:+.3f} vs {e0:+.3f} pnl {df[l].pnl.sum():+.1f}/{df[~l].pnl.sum():+.1f} | dif {dif:+.3f} '
          f'IC90c ({ic[1]:+.3f},{ic[2]:+.3f}) ICa/4 ({ic[0]:+.3f},{ic[3]:+.3f}) IC90d ({icd[0]:+.3f},{icd[1]:+.3f}) p_plac {p:.3f} | sin2mej dif {dif2:+.3f} | dias dif<0 {(pd_ < 0).sum()}/{pd_.notna().sum()}')
    print('    grupo :', fmt(decomp(df[l]))); print('    resto :', fmt(decomp(df[~l])))
print('\n== SECUNDARIOS (descriptivo)')
A['relb'] = pd.cut(A.rel, [-1, -0.005, 0.005, 0.055, 1], labels=['encima_bid', 'en_bid', '1-5c_bajo', '>=6c_bajo'])
for col in ('relb', 'act', 'lado', 'L'):
    for v, x in A.groupby(col, observed=True): print(f'{col}={v}:', fmt(decomp(x)), '| pnl', round(x.pnl.sum(), 1), 'cierres', x.fin.nunique(), 'dias+', int((x.groupby("dia").pnl.sum() > 0).sum()))
for col in ('g300_bsz', 'g300_spr', 'edad', 'lagj'):
    qb = pd.qcut(A[col], 3, duplicates='drop')
    for v, x in A.groupby(qb, observed=True): print(f'{col} {v}:', fmt(decomp(x)), '| pnl', round(x.pnl.sum(), 1))
print('NaN rel:', fmt(decomp(A[A.rel.isna()])))
print('\n== rel x S_nivel / thru (tipo de relleno)')
for (a, b), x in A.groupby(['relb', 'S_nivel'], observed=True): print(a, 'S_nivel' if b else 'noS', fmt(decomp(x)))
deep = A[A.rel > 0.005]; print('profundos rel>0,005: n', len(deep), 'fraccion sh_tx<5 (cota relleno parcial BASE optimista)', round(float((deep.sh_tx < 5).mean()), 3),
      '| EV si q:=min(q, sh_tx)', round(float((np.minimum(deep.q, deep.sh_tx) * (deep.gana - deep.L)).sum() / (np.minimum(deep.q, deep.sh_tx) * deep.L).sum()), 3))
top = A[A.rel <= 0.005]; print('en/encima bid: n', len(top), 'fraccion sh_tx<5', round(float((top.sh_tx < 5).mean()), 3))
# ---------------- mecanismo GEO6 vs G0: quitados / anadidos / conservados
G6 = MK[MK.src == 'GEO6'].copy(); G6['key'] = list(zip(G6.k, G6.L.round(2), G6.tf)); A['key'] = list(zip(A.k, A.L.round(2), A.tf))
R6 = pd.concat([pd.read_pickle(BC + f'RC5d_{d}.pkl') for d in sorted(A.dia.unique())]); R6 = R6[R6['var'] == 'GEO6'].copy(); R6['key'] = list(zip(R6.k, R6.L.round(2), R6.tf))
G6 = G6.merge(R6[['key', 'gana', 'cost', 'pnl', 'act', 'lado', 'T']], on='key', how='left'); G6['m0'] = (G6.m300_bid + G6.m300_ask) / 2
A0 = pd.read_pickle(BC + 'A_all.pkl'); A0['key'] = list(zip(A0.k, A0.L.round(2), A0.tf)); A0['m0'] = (A0.g300_bid + A0.g300_ask) / 2
for c in ('p1', 'p10', 'p60'):
    for s in ('_bid', '_ask'): A0[c + s] = mk[c + s].values
k6 = set(G6.key); k0 = set(A0.key)
quit_ = A0[~A0.key.isin(k6)]; cons = A0[A0.key.isin(k6)]; anad = G6[~G6.key.isin(k0)]
print('\n== GEO6 vs G0 (10 dias, incluye blq como en C5d): quitados', len(quit_), 'pnl', round(quit_.pnl.sum(), 1), '| conservados', len(cons), 'pnl', round(cons.pnl.sum(), 1),
      '| anadidos (hueco)', len(anad), 'pnl', round(anad.pnl.sum(), 1), '| Delta = -quitados + anadidos =', round(-quit_.pnl.sum() + anad.pnl.sum(), 1))
for nm, x in (('quitados', quit_), ('conservados', cons), ('anadidos', anad)):
    print(f'  {nm}:', fmt(decomp(x)))
x = quit_.assign(rel=quit_.g300_bid - quit_.L); print('  quitados con rel<=0,005 (a tf-300):', round(float((x.rel <= 0.005).mean()), 3))
dq = quit_.groupby('dia').pnl.sum(); da = anad.groupby('dia').pnl.sum(); dD = (-dq).add(da, fill_value=0); print('  Delta por dia:', dD.round(1).to_dict())
b2 = dD.nlargest(2).index; print('  Delta sin 2 mejores dias de Delta:', round(dD.drop(b2).sum(), 1), '| dias Delta>0', int((dD > 0).sum()), '/', len(dD))
# bootstrap por cierre de Delta descompuesto
cq = quit_.groupby('fin').pnl.sum(); ca = anad.groupby('fin').pnl.sum(); cD = (-cq).add(ca, fill_value=0).reindex(A0.fin.unique(), fill_value=0).values
bs = np.array([cD[rng.integers(0, len(cD), len(cD))].sum() for _ in range(4000)]); print('  Delta IC90 cierre', np.percentile(bs, [5, 95]).round(1), 'ICa/4', np.percentile(bs, [1.25, 98.75]).round(1))
cQ = (-cq).reindex(A0.fin.unique(), fill_value=0).values; bs = np.array([cQ[rng.integers(0, len(cQ), len(cQ))].sum() for _ in range(4000)]); print('  solo quitar (sin anadidos) IC90 cierre', np.percentile(bs, [5, 95]).round(1), 'total', round(cQ.sum(), 1))
A.drop(columns=['key']).to_pickle(H + 'out/TOX.pkl'); print('FIN')
