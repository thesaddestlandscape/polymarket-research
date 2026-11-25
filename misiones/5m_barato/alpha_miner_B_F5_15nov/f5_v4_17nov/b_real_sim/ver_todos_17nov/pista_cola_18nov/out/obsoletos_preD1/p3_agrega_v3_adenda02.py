#!/usr/bin/env python3
"""p3_agrega.py v2 (ADENDA_01_18nov: NaN excluidos, own excluidos, sensibilidades a/b/c y e250, hi=DATA_BLOCKED) (RE-B-COLA-CANCELA, MECANISMO, NO EV): emparejado evento-placebo, tablas por ventana y clase de suelo, 7 variantes con
max-estadistico (permutacion por mercado), IC90 por dias y por cierre, LR, M1/M2, n_mk=1 vs >=2, huecos a/b/c. Uso: p3_agrega.py [coin=btc] [act|act2]"""
import sys, glob, pickle, json, os, collections, numpy as np, pandas as pd
COIN = sys.argv[1] if len(sys.argv) > 1 else 'btc'; ACT = sys.argv[2] if len(sys.argv) > 2 else 'act'
H = os.path.dirname(os.path.abspath(__file__)); rng = np.random.default_rng(7)
SUF = os.environ.get('PISTA_SUF', ''); fs = sorted(glob.glob(os.environ.get('PISTA_P3_GLOB') or f'{H}/out/p1_{COIN}_2026-11-??.pkl')); Es, Ps, JN, OCN = [], [], collections.Counter(), collections.Counter()
for f in fs:
    d = pickle.load(open(f, 'rb')); Es.append(d['EV']); Ps.append(d['PL']); JN.update(d['JN']); OCN.update(d['OCN'])
E = pd.concat(Es, ignore_index=True); P = pd.concat(Ps, ignore_index=True)
N_OWN = int(E.own.astype(bool).sum()); E = E[~E.own.astype(bool)].reset_index(drop=True)      # ADENDA fix 5: fuera los casados de nuestra wallet
V = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7']
for X in (E, P):
    for v in V: X['F' + v] = X['f_' + v].notna()
    X['F90_V1'] = X.f_V1.notna() & (X.f_V1 <= X.dl90)
    for w in ('W1', 'W2', 'W3', 'WA', 'S250_WA', 'S250_W3'):          # ADENDA fix 6: dato faltante = NaN (se excluye), NUNCA 0
        X['C' + w] = np.where(X[w + '_c'].isna(), np.nan, (X[w + '_c'] > 0).astype(float))
    for w in ('W1', 'W2', 'W3', 'WA'): X['C' + w + '_0'] = np.where(X[w + '_c0'].isna(), np.nan, (X[w + '_c0'] > 0).astype(float))   # legado pre-D-1 (diagnostico)
    for v in ('V1', 'V2', 'V3', 'V4', 'V5', 'V7'): X['F' + v + '_e250'] = X['f_' + v + '_e250'].notna()
    X['FV1_0'] = X.f_V1_0.notna()
    p95 = X.su_p95.fillna(40)
    X['F90c111_V1'] = X.f_V1.notna() & (X.f_V1 <= X.t - 20 - (p95 + 111))      # cancelacion p90 B2 = 111 ms (ADENDA: 147 ms es alta_ex_menos_envio p90 B2, no cancelacion)
    X['F90c46_V1'] = X.f_V1.notna() & (X.f_V1 <= X.t - 20 - (p95 + 46))        # cancelacion p90 B3 = 46 ms
    X['mkt'] = X.end
E['C1'] = E.q150 - E.S > 1e-9; E['C2'] = (E.bet1000 > 0) & (E.bet150 <= 0)
# estratos (cortes por dia a partir de los eventos)
def cuts(x): return np.nanquantile(x, [1 / 3, 2 / 3]) if np.isfinite(x).sum() > 10 else np.array([np.inf, np.inf])
for D_, g in E.groupby('D'):
    for c in ('q150', 'absr5', ACT):
        q = cuts(g[c].astype(float).values)
        for X in (E, P):
            m = X.D == D_; v_ = X.loc[m, c].astype(float).values
            X.loc[m, 's_' + c] = np.where(np.isnan(v_), -1, np.searchsorted(q, np.nan_to_num(v_), 'right'))   # NaN = estrato propio (-1), no el tercil bajo
for X in (E, P): X['s_ttc'] = (X.ttc // 60000).clip(-1, 10); X['st'] = list(zip(X.s_q150, X.s_ttc, X.s_absr5, X['s_' + ACT]))
PI = collections.defaultdict(list); PI2 = collections.defaultdict(list); PI3 = collections.defaultdict(list)
for i, r in enumerate(P[['D', 'X', 'p', 'st']].itertuples(index=False)): PI[(r.D, r.X, r.p, r.st)].append(i); PI2[(r.D, r.p, r.st)].append(i); PI3[(r.D, r.p, r.st[:3])].append(i)
used = collections.Counter(); pm = []; mt = []
for r in E[['D', 'X', 'p', 'st']].itertuples(index=False):
    c = PI.get((r.D, r.X, r.p, r.st)); t = 'nivel'
    if not c: c = PI2.get((r.D, r.p, r.st)); t = 'precio'
    if not c: c = PI3.get((r.D, r.p, r.st[:3])); t = 'precio_sin_act'      # ADENDA: placebos uniformes -> pocos con actividad alta; relaja SOLO el tercil de actividad
    if not c: pm.append(-1); mt.append('sin'); continue
    c2 = [x for x in c if used[x] == 0] or c; j = c2[rng.integers(len(c2))]; used[j] += 1; pm.append(j); mt.append(t)
E['pl'] = pm; E['mtype'] = mt
# ADENDA_02 (punto 2): si P trae `evid` (p1 v3) el emparejado es por EVENTO con calibre (mismo mercado y nivel, otro instante); los estratos de arriba solo sirven de respaldo
if 'evid' in P.columns and P.evid.notna().any():
    PE = collections.defaultdict(list)
    for i, (e_, c_) in enumerate(zip(P.evid, P.cal)):
        if isinstance(e_, str): PE[e_].append(i)
    pm, mt = [], []
    for e_ in E.evid:
        c = PE.get(e_)
        if not c: pm.append(-1); mt.append('sin'); continue
        j = c[rng.integers(len(c))]; pm.append(j); mt.append(P.cal.iat[j])
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
        a, b = S[c].astype(float).values, Q[c].astype(float).values; m = np.isfinite(a) & np.isfinite(b)     # NaN en cualquiera de los dos -> par excluido
        if m.sum() < 2: o[c] = {'n_valid': int(m.sum()), 'nota': 'sin pares validos'}; continue
        a, b, dd_, mk_ = a[m], b[m], S.D.values[m], S.mkt.values[m]
        o[c] = dict(n_valid=int(m.sum()), n_excl_nan=int((~m).sum()), ev=round(a.mean(), 4), pl=round(b.mean(), 4), dif=round(a.mean() - b.mean(), 4),
                    LR=round(a.mean() / b.mean(), 2) if b.mean() > 0 else None,
                    ic90_dias=ic_dias(a, b, dd_), ic90_cierre=ic_clus(a, b, mk_),
                    por_dia={k: round(float(a[dd_ == k].mean() - b[dd_ == k].mean()), 3) for k in sorted(set(dd_))})
    return o
def maxstat(S, B=2000, suf=''):
    VV = [v for v in V if not (suf and v == 'V6')]      # V6 (Binance) no depende de las caidas del libro: sin variante e250
    S, Q = pairs(S); A = S[['F' + v + suf for v in VV]].values.astype(float); Bm = Q[['F' + v + suf for v in VV]].values.astype(float)
    obs = (A - Bm).mean(0); mk = pd.factorize(S.mkt)[0]; nm = mk.max() + 1; mx = []
    for _ in range(B):
        fl = rng.integers(2, size=nm)[mk] * 2 - 1; mx.append(((A - Bm) * fl[:, None]).mean(0).max())
    mx = np.array(mx); return {v + suf: dict(dif=round(float(obs[i]), 4), p_maxstat=round(float((mx >= obs[i]).mean()), 4)) for i, v in enumerate(VV)}
COLS = ['CW1', 'CW2', 'CW3', 'CWA', 'CS250_WA', 'CS250_W3'] + ['F' + v for v in V] + ['F90_V1', 'F90c111_V1', 'F90c46_V1'] + ['F' + v + '_e250' for v in ('V1', 'V2', 'V3', 'V4', 'V5', 'V7')]
R = {'version': 'p3_v3_ADENDA02', 'n_eventos_propios_excluidos': N_OWN, 'ficheros': [os.path.basename(f) for f in fs], 'act_emparejado': ACT, 'n_eventos': len(E), 'n_placebo_cand': len(P),
     'emparejado': E.mtype.value_counts().to_dict(), 'JN': dict(JN), 'OCN': dict(OCN)}
R['union_T1'] = round((JN['T1_tot'] - JN['T1_None']) / max(1, JN['T1_tot']), 4); R['union_Trow'] = round(JN['Trow_ok'] / max(1, JN['Trow_tot']), 4)
R['union_falsos_pm60s'] = round((JN['T1_falso_-60000'] + JN['T1_falso_60000']) / 2 / max(1, JN['T1_tot']), 4)
R['union_onchain_centrica'] = round(OCN['agg_unidos'] / max(1, OCN['agg_en_cobertura']), 4)
U = {'prim_nmk1_C1': (E.n_mk == 1) & E.C1, 'nmk1_C2': (E.n_mk == 1) & E.C2, 'nmk2plus_C1': (E.n_mk >= 2) & E.C1, 'nmk_nan_C1': E.n_mk.isna() & E.C1,
     'prim_mint': (E.n_mk == 1) & E.C1 & (E.ty == 'mint'), 'prim_dir': (E.n_mk == 1) & E.C1 & (E.ty == 'dir'),
     'prim_sin_prev_print': (E.n_mk == 1) & E.C1 & (E.prevpr <= 0),
     # sensibilidades ADENDA fix 6: (a) solo emparejados 'nivel', (b) n_mk=1 SIN exigir C1, (c) universo prim_sin_decS
     'sensA_prim_solo_nivel': (E.n_mk == 1) & E.C1 & (E.mtype == 'nivel'), 'sensB_nmk1_sin_C1': (E.n_mk == 1),
     'sensC_prim_sin_decS': (E.n_mk == 1) & E.C1 & ~E.dec_eq_S.astype(bool)}
def smd(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float); a, b = a[np.isfinite(a)], b[np.isfinite(b)]
    return round(float((a.mean() - b.mean()) / np.sqrt((a.var() + b.var()) / 2 + 1e-12)), 3) if len(a) > 1 and len(b) > 1 else None
_m = U['prim_nmk1_C1']; _S, _Q = pairs(E[_m]); _un = E[_m & (E.pl < 0)]; _ma = E[_m & (E.pl >= 0)]
R['emparejado_prim'] = {'n_prim': int(_m.sum()), 'n_con_pareja': int(len(_S)), 'frac_sin_pareja': round(float(1 - len(_S) / max(1, _m.sum())), 4), 'tipos': E[_m].mtype.value_counts().to_dict()}
R['balance_prim_SMD_evento_vs_placebo'] = {c: smd(_S[c], _Q[c]) for c in ('act2', 'WA_q', 'ttc', 'absr5', 'act', 'q150')}
R['sin_pareja_vs_con_pareja_prim'] = {c: {'sin_med': (round(float(_un[c].median()), 2) if len(_un) else None), 'con_med': (round(float(_ma[c].median()), 2) if len(_ma) else None)} for c in ('act2', 'WA_q', 'ttc', 'absr5', 'S', 'nT')}
R['sin_pareja_vs_con_pareja_prim']['FV1_sin'] = round(float(_un.FV1.mean()), 4) if len(_un) else None; R['sin_pareja_vs_con_pareja_prim']['FV1_con'] = round(float(_ma.FV1.mean()), 4) if len(_ma) else None
R['frac_dec_eq_S_prim'] = round(float(E[U['prim_nmk1_C1']].dec_eq_S.mean()), 4)
for k, m in U.items():
    R[k] = {'todo': tabla(E[m], COLS)}
    for cl in ('lo', 'hi', 'indet'):
        mm = m & (E.suelo == cl)
        if mm.sum() >= 30: R[k][cl] = tabla(E[mm], ['CW1', 'CW2', 'CW3', 'FV1', 'F90_V1'])
        else: R[k][cl] = {'n_ev': int(mm.sum()), 'nota': 'DATA_BLOCKED (0 eventos de esta clase de suelo)' if mm.sum() == 0 else 'INSUFFICIENT n<30'}
R['latencia_clase_hi'] = 'DATA_BLOCKED: paquete_l ensayo_real B2/B3/B5 (13-Nov) = 257 lo / 58 ambiguo / 0 hi; hi solo sensibilidad'
# D-1: cuanto queda del artefacto de la propia casacion (nuevo vs legado, eventos y placebo)
def d1(X, nm):
    o = {'n': int(len(X))}
    for w in ('W1', 'W2', 'W3', 'WA'): o['C' + w + '_nuevo'] = round(float(X['C' + w].mean()), 4); o['C' + w + '_legado'] = round(float(X['C' + w + '_0'].mean()), 4)
    o['FV1_nuevo'] = round(float(X.FV1.mean()), 4); o['FV1_legado'] = round(float(X.FV1_0.mean()), 4)
    return o
R['D1'] = {'eventos_todos': d1(E, 'E'), 'eventos_prim': d1(E[U['prim_nmk1_C1']], 'Ep'), 'placebo_todos': d1(P, 'P')}
de = E[E.dec_eq_S.astype(bool)]
R['D1']['dec_eq_S'] = dict(n=int(len(de)), frac_eventos=round(float(E.dec_eq_S.astype(bool).mean()), 4),
    frac_control_otro_cluster=round(float(E.dec_eq_S_ctrl.dropna().astype(bool).mean()), 4) if E.dec_eq_S_ctrl.notna().any() else None,
    CWA_nuevo_entre_dec_eq_S=round(float(de.CWA.mean()), 4) if len(de) else None, CWA_legado_entre_dec_eq_S=round(float(de.CWA_0.mean()), 4) if len(de) else None)
R['maxstat_prim'] = maxstat(E[U['prim_nmk1_C1']]); R['maxstat_prim_e250'] = maxstat(E[U['prim_nmk1_C1']], suf='_e250')
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
    S = E[m]; R['M1_' + nm] = dict(n=int(len(S)), p50=round(float(S.FV1.mean()), 4), p90_alta147=round(float(S.F90_V1.mean()), 4), p90_cancel111=round(float(S.F90c111_V1.mean()), 4), p90_cancel46=round(float(S.F90c46_V1.mean()), 4), umbral='>=0,70 p50 y >=0,50 p90')
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
json.dump(R, open(f'{H}/out/p3_{COIN}_{ACT}{SUF}.json', 'w'), indent=1, default=str); print(json.dumps({k: R[k] for k in ('n_eventos', 'emparejado', 'union_T1', 'union_falsos_pm60s', 'union_onchain_centrica')}, default=str))
