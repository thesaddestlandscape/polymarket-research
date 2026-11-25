#!/usr/bin/env python3
"""p3_agrega.py (RE-B-COLA-CANCELA, MECANISMO, NO EV): emparejado evento-placebo, tablas por ventana y clase de suelo, 7 variantes con
max-estadistico (permutacion por mercado), IC90 por dias y por cierre, LR, M1/M2, n_mk=1 vs >=2, huecos a/b/c. Uso: p3_agrega.py [coin=btc] [act|act2]"""
import sys, glob, pickle, json, os, collections, numpy as np, pandas as pd
COIN = sys.argv[1] if len(sys.argv) > 1 else 'btc'; ACT = sys.argv[2] if len(sys.argv) > 2 else 'act'
H = os.path.dirname(os.path.abspath(__file__)); rng = np.random.default_rng(7)
fs = sorted(glob.glob(f'{H}/out/p1_{COIN}_2026-11-??.pkl')); Es, Ps, JN, OCN = [], [], collections.Counter(), collections.Counter()
for f in fs:
    d = pickle.load(open(f, 'rb')); Es.append(d['EV']); Ps.append(d['PL']); JN.update(d['JN']); OCN.update(d['OCN'])
E = pd.concat(Es, ignore_index=True); P = pd.concat(Ps, ignore_index=True)
V = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7']
for X in (E, P):
    for v in V: X['F' + v] = X['f_' + v].notna()
    X['F90_V1'] = X.f_V1.notna() & (X.f_V1 <= X.dl90)
    for w in ('W1', 'W2', 'W3', 'WA'): X['C' + w] = X[w + '_c'].fillna(0) > 0
    X['mkt'] = X.end
E['C1'] = E.q150 - E.S > 1e-9; E['C2'] = (E.bet1000 > 0) & (E.bet150 <= 0)
# estratos (cortes por dia a partir de los eventos)
def cuts(x): return np.nanquantile(x, [1 / 3, 2 / 3]) if np.isfinite(x).sum() > 10 else np.array([np.inf, np.inf])
for D_, g in E.groupby('D'):
    for c in ('q150', 'absr5', ACT):
        q = cuts(g[c].astype(float).values)
        for X in (E, P):
            m = X.D == D_; X.loc[m, 's_' + c] = np.searchsorted(q, X.loc[m, c].astype(float).fillna(-1).values, 'right')
for X in (E, P): X['s_ttc'] = (X.ttc // 60000).clip(-1, 10); X['st'] = list(zip(X.s_q150, X.s_ttc, X.s_absr5, X['s_' + ACT]))
PI = collections.defaultdict(list); PI2 = collections.defaultdict(list)
for i, r in enumerate(P[['D', 'X', 'p', 'st']].itertuples(index=False)): PI[(r.D, r.X, r.p, r.st)].append(i); PI2[(r.D, r.p, r.st)].append(i)
used = collections.Counter(); pm = []; mt = []
for r in E[['D', 'X', 'p', 'st']].itertuples(index=False):
    c = PI.get((r.D, r.X, r.p, r.st)); t = 'nivel'
    if not c: c = PI2.get((r.D, r.p, r.st)); t = 'precio'
    if not c: pm.append(-1); mt.append('sin'); continue
    c2 = [x for x in c if used[x] == 0] or c; j = c2[rng.integers(len(c2))]; used[j] += 1; pm.append(j); mt.append(t)
E['pl'] = pm; E['mtype'] = mt
def pairs(S):
    S = S[S.pl >= 0]; Q = P.iloc[S.pl.values].reset_index(drop=True); return S.reset_index(drop=True), Q
def ic_dias(a, b, days, B=2000):
    dd = pd.DataFrame(dict(a=a, b=b, d=days)).groupby('d').agg(a=('a', 'sum'), b=('b', 'sum'), n=('a', 'size'))
    if len(dd) < 2: return [np.nan, np.nan]
    bs = []
    for _ in range(B):
        k = dd.iloc[rng.integers(len(dd), size=len(dd))]; bs.append((k.a.sum() - k.b.sum()) / k.n.sum())
    return [round(float(x), 4) for x in np.percentile(bs, [5, 95])]
def ic_clus(a, b, cl, B=1000):
    dd = pd.DataFrame(dict(a=a, b=b, d=cl)).groupby('d').agg(a=('a', 'sum'), b=('b', 'sum'), n=('a', 'size')); bs = []
    for _ in range(B):
        k = dd.iloc[rng.integers(len(dd), size=len(dd))]; bs.append((k.a.sum() - k.b.sum()) / k.n.sum())
    return [round(float(x), 4) for x in np.percentile(bs, [5, 95])]
def tabla(S, cols):
    S, Q = pairs(S); o = {'n_ev': int(len(S)), 'dias': int(S.D.nunique()), 'mercados': int(S.mkt.nunique())}
    for c in cols:
        a, b = S[c].astype(float).values, Q[c].astype(float).values
        o[c] = dict(ev=round(a.mean(), 4), pl=round(b.mean(), 4), dif=round(a.mean() - b.mean(), 4), LR=round(a.mean() / b.mean(), 2) if b.mean() > 0 else None,
                    ic90_dias=ic_dias(a, b, S.D.values), ic90_cierre=ic_clus(a, b, S.mkt.values),
                    por_dia={k: round(float(g[c].mean() - Q.loc[g.index, c].mean()), 3) for k, g in S.groupby('D')})
    return o
def maxstat(S, B=2000):
    S, Q = pairs(S); A = S[['F' + v for v in V]].values.astype(float); Bm = Q[['F' + v for v in V]].values.astype(float)
    obs = (A - Bm).mean(0); mk = pd.factorize(S.mkt)[0]; nm = mk.max() + 1; mx = []
    for _ in range(B):
        fl = rng.integers(2, size=nm)[mk] * 2 - 1; mx.append(((A - Bm) * fl[:, None]).mean(0).max())
    mx = np.array(mx); return {v: dict(dif=round(float(obs[i]), 4), p_maxstat=round(float((mx >= obs[i]).mean()), 4)) for i, v in enumerate(V)}
COLS = ['CW1', 'CW2', 'CW3', 'CWA'] + ['F' + v for v in V] + ['F90_V1']
R = {'ficheros': [os.path.basename(f) for f in fs], 'act_emparejado': ACT, 'n_eventos': len(E), 'n_placebo_cand': len(P),
     'emparejado': E.mtype.value_counts().to_dict(), 'JN': dict(JN), 'OCN': dict(OCN)}
R['union_T1'] = round((JN['T1_tot'] - JN['T1_None']) / max(1, JN['T1_tot']), 4); R['union_Trow'] = round(JN['Trow_ok'] / max(1, JN['Trow_tot']), 4)
R['union_falsos_pm60s'] = round((JN['T1_falso_-60000'] + JN['T1_falso_60000']) / 2 / max(1, JN['T1_tot']), 4)
R['union_onchain_centrica'] = round(OCN['agg_unidos'] / max(1, OCN['agg_en_cobertura']), 4)
U = {'prim_nmk1_C1': (E.n_mk == 1) & E.C1, 'nmk1_C2': (E.n_mk == 1) & E.C2, 'nmk2plus_C1': (E.n_mk >= 2) & E.C1, 'nmk_nan_C1': E.n_mk.isna() & E.C1,
     'prim_sin_decS': (E.n_mk == 1) & E.C1 & ~E.dec_eq_S.astype(bool), 'prim_mint': (E.n_mk == 1) & E.C1 & (E.ty == 'mint'), 'prim_dir': (E.n_mk == 1) & E.C1 & (E.ty == 'dir'),
     'prim_sin_prev_print': (E.n_mk == 1) & E.C1 & (E.prevpr <= 0), 'prim_placebo_mismo_nivel': (E.n_mk == 1) & E.C1 & (E.mtype == 'nivel')}
R['frac_dec_eq_S_prim'] = round(float(E[U['prim_nmk1_C1']].dec_eq_S.mean()), 4)
for k, m in U.items():
    R[k] = {'todo': tabla(E[m], COLS)}
    for cl in ('lo', 'hi', 'indet'):
        mm = m & (E.suelo == cl)
        if mm.sum() >= 30: R[k][cl] = tabla(E[mm], ['CW1', 'CW2', 'CW3', 'FV1', 'F90_V1'])
        else: R[k][cl] = {'n_ev': int(mm.sum()), 'nota': 'n<30'}
R['maxstat_prim'] = maxstat(E[U['prim_nmk1_C1']])
# exceso n_mk=1 vs n_mk>=2 (diferencia de diferencias, IC por dias)
def exc(m):
    S, Q = pairs(E[m]); return pd.DataFrame(dict(d=S.D, x=S.FV1.astype(float) - Q.FV1.astype(float)))
a, b = exc(U['prim_nmk1_C1']), exc(U['nmk2plus_C1']); bs = []
ga, gb = a.groupby('d').x, b.groupby('d').x; days = sorted(set(a.d) & set(b.d))
for _ in range(2000):
    k = rng.choice(days, len(days)); bs.append(np.mean(np.concatenate([a[a.d == x].x for x in k])) - np.mean(np.concatenate([b[b.d == x].x for x in k])))
R['dd_nmk1_menos_nmk2_FV1'] = dict(dd=round(a.x.mean() - b.x.mean(), 4), ic90_dias=[round(float(x), 4) for x in np.percentile(bs, [5, 95])])
# M1 (sobre eventos primarios, C1 y C2): R1 dispara a tiempo con p50 / p90
for nm, m in (('C1', U['prim_nmk1_C1']), ('C2', U['nmk1_C2'])):
    S = E[m]; R['M1_' + nm] = dict(n=int(len(S)), p50=round(float(S.FV1.mean()), 4), p90=round(float(S.F90_V1.mean()), 4), umbral='>=0,70 p50 y >=0,50 p90')
S, Q = pairs(E[U['prim_nmk1_C1']])
R['M2_LR_V1'] = dict(p50=round(S.FV1.mean() / max(1e-9, Q.FV1.mean()), 2), p90=round(S.F90_V1.mean() / max(1e-9, Q.F90_V1.mean()), 2), umbral='>=3')
lr = []
for _ in range(2000):
    dd = rng.choice(sorted(S.D.unique()), S.D.nunique()); ix = np.concatenate([np.where(S.D.values == x)[0] for x in dd])
    lr.append(S.FV1.values[ix].mean() / max(1e-9, Q.FV1.values[ix].mean()))
R['M2_LR_V1']['ic90_dias_p50'] = [round(float(x), 2) for x in np.percentile(lr, [5, 95])]
# falsos disparos por hora en reposo: tasa de disparo de V1 en placebos (ventana de evaluacion ~0,93 s) -> disparos por hora de nivel vivo
R['M3_falsos_disparos_por_hora_reposo_aprox'] = round(float(P.FV1.mean()) * 3600 / 0.927, 1)
# hueco b: makers persistentes (grupos en dias impares/pares, medida en los otros)
Ep = E[U['prim_nmk1_C1'] & E.mk.notna()].copy(); Ep['m1'] = Ep.mk.map(lambda t: t[0] if t else None); Ep['par'] = Ep.D.str[-1].astype(int) % 2
hb = {}
for g_def in (0, 1):
    cnt = Ep[Ep.par == g_def].m1.value_counts(); pers = set(cnt[cnt >= 20].index); T_ = Ep[Ep.par != g_def].copy(); T_['pers'] = T_.m1.isin(pers)
    S2, Q2 = pairs(T_); S2['x'] = S2.FV1.astype(float) - Q2.FV1.astype(float).values
    hb[f'grupo_en_par{g_def}'] = dict(n_pers_def=len(pers), n_ev_pers=int(S2.pers.sum()), n_ev_no=int((~S2.pers).sum()),
        exceso_pers=round(float(S2[S2.pers].x.mean()), 4) if S2.pers.any() else None, exceso_no=round(float(S2[~S2.pers].x.mean()), 4),
        top1_maker_frac=round(float(T_.m1.value_counts(normalize=True).iloc[0]), 3) if len(T_) else None)
R['hueco_b'] = hb
# hueco c: salto Binance >=1bp contra el token ANTES (>=50 ms) del inicio de la evaporacion
def lead(X):
    X = X[X.evap0.notna()]; return dict(n=int(len(X)), con_salto=round(float(X.bn0.notna().mean()), 4),
        salto_antes_50ms=round(float(((X.bn0.notna()) & (X.bn0 <= X.evap0 - 50)).mean()), 4))
S, Q = pairs(E[U['prim_nmk1_C1']]); R['hueco_c'] = dict(evento=lead(S), placebo=lead(Q),
    evap_inicio_rel_ms_pcts=[float(x) for x in np.nanpercentile((S.evap0 - S.t).astype(float), [10, 25, 50, 75, 90])] if S.evap0.notna().any() else None,
    llegada_tomador_cota_ms='t_c - 20 - [145, 215] (taker delay medido; no observable)')
R['top1_maker_frac_prim'] = round(float(Ep.m1.value_counts(normalize=True).iloc[0]), 3) if len(Ep) else None
json.dump(R, open(f'{H}/out/p3_{COIN}_{ACT}.json', 'w'), indent=1, default=str); print(json.dumps({k: R[k] for k in ('n_eventos', 'emparejado', 'union_T1', 'union_falsos_pm60s', 'union_onchain_centrica')}, default=str))
