#!/usr/bin/env python3
"""RE-F5-PUERTA0 (23-Nov): desagregacion EXPLORATORIA de las ordenes B simuladas de la Puerta 0 (p0_ordenes_D.pkl, 03-14 Nov, ya vistos).
Solo lectura. Unidad = 1.er relleno mercado-lado (q>0 unico por dia,mid,lado; se verifica). EV = Sum pnl / Sum coste (EUR). IC90 por DIAS (bootstrap dias)."""
import sys, glob, json, numpy as np, pandas as pd
sys.path.insert(0, '../r1v2_eval'); import puerta0_core as P
OUT = 'out'; import os; os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(20261123); K = 2000
fs = [f_ for f_ in sorted(glob.glob('../r1v2_eval/out_p0/p0_ordenes_2026-11-*.pkl')) if f_.rsplit('p0_ordenes_', 1)[1][:10] < '2026-11-15']      # v3: nunca dias >= 15-Nov (ciegos desde 18-Nov)
R = pd.concat([pd.read_pickle(f) for f in fs], ignore_index=True)
R = R[R.dia >= '2026-11-05']  # C = 05-14 (03-04 aparte)
res = {}
def ev(x): c = x.cost.sum(); return x.pnl.sum() / c if c > 0 else np.nan
def boot(F, key, a, b):
    """diff EV(a)-EV(b) con IC90 por dias; F = rellenos; key = columna de grupo; a,b = listas de valores"""
    dias = sorted(F.dia.unique()); M = np.zeros((len(dias), 4))
    for i, d in enumerate(dias):
        x = F[F.dia == d]; A = x[x[key].isin(a)]; B = x[x[key].isin(b)]
        M[i] = [A.pnl.sum(), A.cost.sum(), B.pnl.sum(), B.cost.sum()]
    def f(ix):
        s = M[ix].sum(0); return s[0]/s[1] - s[2]/s[3] if s[1] > 0 and s[3] > 0 else np.nan
    pt = f(np.arange(len(dias))); bs = np.array([f(rng.integers(0, len(dias), len(dias))) for _ in range(K)]); bs = bs[np.isfinite(bs)]
    dpos = sum(1 for i in range(len(dias)) if np.isfinite(f(np.array([i]))) and f(np.array([i])) > 0)
    return dict(diff=round(pt, 4), lo=round(np.percentile(bs, 5), 4), hi=round(np.percentile(bs, 95), 4), dias=len(dias), dias_pos=dpos)
def tabla(F, cols):
    g = F.groupby(cols, observed=True).agg(nf=('q', 'size'), cost=('cost', 'sum'), pnl=('pnl', 'sum'), nd=('dia', 'nunique')).reset_index()
    g['EV'] = (g.pnl / g.cost).round(4); g['cost'] = g.cost.round(1); g['pnl'] = g.pnl.round(2); return g
for v, Rv in R.groupby('bloq'):
    Rv = Rv.copy(); Rv['grupo'] = np.where(Rv.tercil == 'alto', 'alto', 'bm')
    F = Rv[Rv.q > 0].copy(); dup = F.duplicated(['dia', 'mid', 'lado']).sum()
    F['nrep'] = pd.cut(F.n_ord, [-1, 0, 2, 9, 1e9], labels=['0', '1-2', '3-9', '10+'])
    F['prof'] = ((F.bid_dec - F.L) / 0.01).round().clip(-1, 6).astype(int)
    F['Tb'] = pd.cut(F.T_dec, [-1e9, 60, 120, 200, 1e9], labels=['<60', '60-120', '120-200', '>200'])
    F['edad'] = pd.cut((F.tf - F.t_arr) / 1000, [-1e9, 0.5, 2, 10, 1e9], labels=['<0,5s', '0,5-2s', '2-10s', '>10s'])
    F['Lb'] = pd.cut(F.L, [0, 0.10, 0.20, 0.30, 0.50, 1], labels=['<0,10', '0,10-0,20', '0,20-0,30', '0,30-0,50', '>0,50'])
    F['mitad'] = np.where(F.dia <= '2026-11-09', 'A', 'B')
    # quintiles de f5t recalibrados DENTRO de B real (cortes de todas las ordenes, exploratorio)
    qs = np.quantile(Rv.f5t.dropna(), [0.2, 0.4, 0.6, 0.8]); F['q5'] = np.searchsorted(qs, F.f5t)
    r = dict(n_ordenes=len(Rv), n_rellenos=len(F), dup_mercado_lado=int(dup), ev_total=round(ev(F), 4), cortes_q5=[round(x, 3) for x in qs],
             frac_ordenes_tercil=Rv.tercil.value_counts(normalize=True).round(3).to_dict(),
             p_relleno_tercil=(Rv.groupby('tercil').q.apply(lambda s: (s > 0).mean())).round(4).to_dict())
    r['diff_bm_alto'] = boot(F, 'grupo', ['bm'], ['alto'])
    r['diff_bajo_alto'] = boot(F, 'tercil', ['bajo'], ['alto'])
    r['diff_q5_0_vs_4'] = boot(F, 'q5', [0], [4])
    Fx = F[F.tercil_ex != 'inval'].copy(); Fx['gex'] = np.where(Fx.tercil_ex == 'alto', 'alto', 'bm'); r['diff_bm_alto_reloj_exchange'] = boot(Fx, 'gex', ['bm'], ['alto'])
    for c in ['coin', 'nrep', 'prof', 'Tb', 'edad', 'Lb', 'lado', 'mitad'] + (['canal'] if v == 1 else []):
        r['por_' + c] = {str(k): boot(F[F[c] == k], 'grupo', ['bm'], ['alto']) for k in F[c].dropna().unique() if (F[c] == k).sum() >= 15 and F[(F[c] == k) & (F.grupo == 'alto')].shape[0] >= 5}
        tabla(F, [c, 'tercil']).to_csv(f'{OUT}/tab_bloq{v}_{c}.csv', index=False)
    tabla(F, ['q5']).to_csv(f'{OUT}/tab_bloq{v}_q5.csv', index=False)
    tabla(F, ['dia', 'grupo']).to_csv(f'{OUT}/tab_bloq{v}_dia.csv', index=False)
    # transicion: tercil de la 1.a colocacion del mercado-lado vs tercil de la orden que rellena
    first = Rv.sort_values('t_dec').groupby(['dia', 'mid', 'lado']).tercil.first().rename('t0')
    F = F.join(first, on=['dia', 'mid', 'lado']); r['transicion_t0_vs_trelleno'] = pd.crosstab(F.t0, F.tercil).to_dict()
    # FILTRO DE COLOCACION a nivel mercado-lado (contrafactual exacto: lados independientes): no entrar si t0 == alto
    S = Rv.groupby(['dia', 'mid', 'lado']).agg(cost=('cost', 'sum'), pnl=('pnl', 'sum'), nf=('q', lambda s: int((s > 0).any())), coin=('coin', 'first')).reset_index().join(first, on=['dia', 'mid', 'lado'])
    S['g0'] = np.where(S.t0 == 'alto', 'alto', 'bm')
    r['colocacion_mercado_lado'] = dict(n_lados=len(S), por_t0=tabla(S.assign(q=1), ['t0']).to_dict('records'), diff_bm_alto=boot(S, 'g0', ['bm'], ['alto']),
                                       pnl_total=round(S.pnl.sum(), 2), pnl_si_filtra_alto=round(S[S.g0 == 'bm'].pnl.sum(), 2), pnl_si_filtra_bajo=round(S[S.t0 != 'bajo'].pnl.sum(), 2))
    # que retira la retirada: hipotetico de ordenes alto NO rellenadas (gana del token, solo etiqueta)
    U = Rv[Rv.q == 0]; r['p_gana_ordenes'] = {f'{t}_{"rell" if f else "norell"}': round(Rv[(Rv.tercil == t) & ((Rv.q > 0) == f)].gana.mean(), 4) for t in P.TERC for f in (True, False)}
    r['L_medio_rellenos_tercil'] = F.groupby('tercil').L.mean().round(4).to_dict()
    res[f'bloq{v}'] = r
json.dump(res, open(f'{OUT}/desagrega.json', 'w'), indent=1, default=str); print(json.dumps(res, default=str)[:200])
