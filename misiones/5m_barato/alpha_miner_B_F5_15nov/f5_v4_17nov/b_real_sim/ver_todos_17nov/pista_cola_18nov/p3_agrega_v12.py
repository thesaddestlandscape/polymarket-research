#!/usr/bin/env python3
"""p3_agrega_v12.py = v7 (ADENDA_12_19nov: lee p7v12/p7wv12, REQ v12; copia de v6 sin otro cambio) / v6 (ADENDA_06 + ADENDA_07_18nov + ADENDA_11_19nov: z0+normal, Holm x2, small EXPLORATORIO, dia incompleto se excluye, 4d F1) (RE-B-COLA-CANCELA, MECANISMO, NO EV).
PARTE CONFIRMATORIA (nueva): test unico B1 = V1 pooled, IPW+EB (pesos de p7 por dia), clase lo, universo primario n_mk=1 C1 sin propios; unidad = DIA (C1 t de Student df=dias-1, media simple),
C2 bootstrap por mercado, C3 permutacion con signo por mercado sobre d_m con max-estadistico V1..V7, Holm x2 en estratos {z0, normal} (small EXPLORATORIO), C5 (<=35 %/dia, leave-one-day-out), veredicto B4' (ADENDA_07 D1).
PARTE EXPLORATORIA (heredada de v3: emparejado por placebo, tablas por ventana, M1/M2, hueco b/c, H-ACT): etiquetada EXPLORATORIO en el JSON.
Dias: lista del veredicto {13,14,15,17,18,19-Nov}; 12 y 16-Nov SOLO con P3_DISENO=1 (salida *_DISENO, sin veredicto). No lee ninguna columna f_* antes de pasar: hashes de HASHES_CODIGO.txt, informe de balance E por dia (p7),
dia completo y balance valido; si falta algo -> estado BLOCKED sin imprimir tasas. Uso: p3_agrega.py [coin=btc] [act|act2]"""
import sys, glob, pickle, json, os, collections, hashlib, re, numpy as np, pandas as pd
from scipy import stats as sst
COIN = sys.argv[1] if len(sys.argv) > 1 else 'btc'; ACT = sys.argv[2] if len(sys.argv) > 2 else 'act'
H = os.path.dirname(os.path.abspath(__file__)); rng = np.random.default_rng(7)
DISENO = os.environ.get('P3_DISENO', '0') == '1'; SUF = os.environ.get('PISTA_SUF', '')
VERDICT_DAYS = ['2026-11-13', '2026-11-14', '2026-11-15', '2026-11-17', '2026-11-18', '2026-11-19']; DESIGN_DAYS = ['2026-11-12', '2026-11-16']
DAYS = DESIGN_DAYS if DISENO else VERDICT_DAYS
if not DISENO: assert SUF == '', 'en modo veredicto PISTA_SUF debe ser vacio'
OUTJ = f'{H}/out/p3v12_{COIN}_{ACT}{SUF}{"_DISENO" if DISENO and "DISENO" not in SUF else ""}.json'
def sha(fn): return hashlib.sha256(open(fn, 'rb').read()).hexdigest()
def blocked(msg, extra=None):
    json.dump(dict(estado='BLOCKED', motivo=msg, extra=extra or {}, dias_lista=DAYS), open(OUTJ.replace('.json', '_BLOCKED.json'), 'w'), indent=1, default=str); print('BLOCKED:', msg); sys.exit(2)
# ---- 1. hashes congelados (H1/H25)
REQ = ['p1_dia.py', 'p3_agrega_v12.py', 'p7_ipw_balance_v12.py', 'p5_control_sin_relleno.py', 'run_p1.sh', 'ADENDA_07_18nov.md', 'ADENDA_09_18nov.md', 'ADENDA_10_19nov.md', 'ADENDA_11_19nov.md', 'ADENDA_12_19nov.md', 'ADENDA_13_19nov.md', 'ADENDA_13b_19nov.md']; HASHOK = {}
if not DISENO:
    hf = f'{H}/HASHES_CODIGO.txt'; last = {}
    for ln in open(hf):
        p_ = ln.split()
        if len(p_) == 2 and re.fullmatch(r'[0-9a-f]{64}', p_[0]): last[p_[1]] = p_[0]
    for nm in REQ:
        if nm not in last: blocked(f'{nm} sin hash en HASHES_CODIGO.txt')
        if sha(f'{H}/{nm}') != last[nm]: blocked(f'hash de {nm} en disco != HASHES_CODIGO.txt (codigo modificado tras congelar)')
        HASHOK[nm] = last[nm]
P7SHA = sha(f'{H}/p7_ipw_balance_v12.py')      # ADENDA_13 §5: el informe y los pesos deben venir de ESTE p7 v12 (en veredicto == hash congelado, ya verificado arriba)
# ---- 2. dias: pkl, informe de balance E, completo
CAND = []; PEND = []; EXCL = {}; EXCL_INC = {}; ERR = {}
for D_ in DAYS:
    f1 = f'{H}/out/p1_{COIN}_{D_}{SUF}.pkl'
    if not os.path.exists(f1): PEND.append(D_); continue
    jp, wp = f'{H}/out/p7v12_{COIN}_{D_}{SUF}.json', f'{H}/out/p7wv12_{COIN}_{D_}{SUF}.pkl'
    if not (os.path.exists(jp) and os.path.exists(wp)): blocked(f'falta el informe de balance E (p7) del dia {D_}')
    rj = json.load(open(jp))
    if rj.get('version') != 'p7_v12_ADENDA12' or rj.get('SHA256_codigo') != P7SHA: blocked(f'el informe p7 del dia {D_} no es de p7_ipw_balance_v12.py en disco (version {rj.get("version")}, SHA256_codigo distinto)')
    w_ = pickle.load(open(wp, 'rb'))
    if w_.get('version') != 'p7w_v12' or w_.get('SHA256_codigo') != P7SHA or w_.get('SHA256_pkl_p1') != sha(f1): blocked(f'los pesos p7w del dia {D_} no son de p7_ipw_balance_v12.py en disco / no corresponden al pkl de p1')
    del w_
    if rj.get('SHA256_pkl_p1') != sha(f1): blocked(f'el informe p7 del dia {D_} no corresponde al pkl de p1 en disco')
    if not DISENO:       # ADENDA_11 §7.1 (4a): el dia incompleto se EXCLUYE y se lista (cuenta contra >=5 dias validos), ya no bloquea
        if not rj['dia_completo']['ok']: EXCL_INC[D_] = rj['dia_completo']
        if not rj['dia_valido_E']: EXCL[D_] = rj['E4_fallos']
        if D_ in EXCL_INC or D_ in EXCL: continue
    CAND.append(D_)
if not DISENO and not CAND: blocked('ningun dia valido (completo y con balance E superado)', dict(pendientes=PEND, excluidos_E=EXCL, excluidos_incompletos=EXCL_INC))
fs = [f'{H}/out/p1_{COIN}_{D_}{SUF}.pkl' for D_ in CAND]; Es, Ps, PWs, JN, OCN = [], [], {}, collections.Counter(), collections.Counter()
for f, D_ in zip(fs, CAND):
    d = pickle.load(open(f, 'rb')); assert d['D'] == D_ and D_ in DAYS and d.get('version') == 'p1_v11_ADENDA11', (D_, d.get('version')); Es.append(d['EV']); Ps.append(d['PL']); PWs[D_] = d['PW']; JN.update(d['JN']); OCN.update(d['OCN'])
E = pd.concat(Es, ignore_index=True); P = pd.concat(Ps, ignore_index=True)
assert set(E.D.unique()) <= set(DAYS), 'dia fuera de la lista'
for nm_, X_ in (('EV', E), ('PL', P), *[('PW' + k_, v_) for k_, v_ in PWs.items()]): assert int((X_.absr5_rx > X_.t - 1000).sum()) == 0, ('absr5 usa rx posterior a t-1000', nm_)      # ADENDA_11 §5.3
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
R = {'version': 'p3_v7_ADENDA12', 'ETIQUETA': 'DISENO' if DISENO else 'VEREDICTO', 'dias_usados': CAND, 'dias_pendientes': PEND, 'dias_excluidos_E4': EXCL, 'dias_excluidos_incompletos': EXCL_INC, 'hashes_verificados': HASHOK, 'seccion_heredada_v3': 'EXPLORATORIO', 'n_eventos_propios_excluidos': N_OWN, 'ficheros': [os.path.basename(f) for f in fs], 'act_emparejado': ACT, 'n_eventos': len(E), 'n_placebo_cand': len(P),
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
# ======================= PARTE CONFIRMATORIA (ADENDA_06 B/C/F + ADENDA_07 D1/D5) =======================
rg = np.random.default_rng(20261118)
VAR7 = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7']; VAR250 = ['V1_e250', 'V2_e250', 'V3_e250', 'V4_e250', 'V5_e250', 'V7_e250']; VARS = VAR7 + VAR250
EVI = E.set_index('evid')
def weights_for(D_):
    w = pickle.load(open(f'{H}/out/p7wv12_{COIN}_{D_}{SUF}.pkl', 'rb')); assert w['dia'] == D_ and w['version'] == 'p7w_v12' and w.get('SHA256_codigo') == P7SHA; return w['pesos']
WGT = {D_: weights_for(D_) for D_ in CAND}
PRIM_ST = ('z0', 'normal')        # ADENDA_11 §3 (B1): estratos del test confirmatorio; small es EXPLORATORIO
def tabs(key, cl, estratos=PRIM_ST):
    """eventos soportados y controles ponderados de la clase cl y de los estratos dados (todos los dias usados). F = el disparo existe (f_* no nulo)."""
    ev, ct = [], []
    for D_ in CAND:
        wk = WGT[D_].get(key)
        if wk is None or len(wk['S']) == 0: continue
        S_ = wk['S'][(wk['S'].cl == cl) & wk['S'].st.isin(estratos)]; W_ = wk['W'][(wk['W'].cl == cl) & wk['W'].st.isin(estratos)]
        if len(S_) == 0: continue
        e_ = EVI.loc[S_.evid.values]; c_ = PWs[D_].loc[W_.index.values]
        a = S_[['evid', 'st', 'D', 'end']].reset_index(drop=True); b = W_[['st', 'om', 'D', 'end']].reset_index(drop=True)
        for v in VARS: a[v] = e_['f_' + v].notna().astype(float).values; b[v] = c_['f_' + v].notna().astype(float).values
        ev.append(a); ct.append(b)
    if not ev: return pd.DataFrame(), pd.DataFrame()
    return pd.concat(ev, ignore_index=True), pd.concat(ct, ignore_index=True)
def per_day(ev, ct, var):
    o = []
    for D_, g in ev.groupby('D'):
        c = ct[ct.D == D_]
        if len(c) == 0 or c.om.sum() <= 0: continue
        o.append((D_, len(g), float(g[var].mean() - (c.om * c[var]).sum() / c.om.sum())))
    return pd.DataFrame(o, columns=['D', 'n', 'd'])
def ic_t(x, lvl=0.90):
    x = np.asarray(x, float); n = len(x)
    if n < 2: return [np.nan, np.nan]
    h = sst.t.ppf(0.5 + lvl / 2, n - 1) * x.std(ddof=1) / np.sqrt(n); return [float(x.mean() - h), float(x.mean() + h)]
def mkt_arrays(ev, ct, vars_):
    mk = pd.factorize(pd.concat([ev.end, ct.end], ignore_index=True))[0]; me, mc = mk[:len(ev)], mk[len(ev):]; M = mk.max() + 1
    nev = np.bincount(me, minlength=M).astype(float); sw = np.bincount(mc, weights=ct.om.values, minlength=M)
    sF = np.column_stack([np.bincount(me, weights=ev[v].values, minlength=M) for v in vars_]); swF = np.column_stack([np.bincount(mc, weights=ct.om.values * ct[v].values, minlength=M) for v in vars_])
    return nev, sw, sF, swF
def boot_mkt(nev, sw, sF, swF, j, B=2000):
    M = len(nev); o = []
    for _ in range(B):
        k = rg.integers(M, size=M); o.append((sF[k, j].sum() / nev[k].sum()) - (swF[k, j].sum() / sw[k].sum()) if nev[k].sum() > 0 and sw[k].sum() > 0 else np.nan)
    o = np.array(o); return o[np.isfinite(o)]
def perm_T(nev, sw, sF, swF, B=2000):
    d_ = sF - swF; den = np.sqrt((d_ ** 2).sum(0) + 1e-12); T = d_.sum(0) / den; M = len(nev); mx = np.empty(B); one = np.empty((B, d_.shape[1]))
    for b in range(B):
        fl = rg.integers(2, size=M) * 2 - 1; Tb = (d_ * fl[:, None]).sum(0) / den; one[b] = Tb; mx[b] = Tb.max()
    return T, mx, one
def analiza(ev, ct, var='V1', B=2000):
    """C1 (dias, t), C2 (mercado), semiancho, LODO, C5, LR, sin 2 mejores dias, Kish."""
    kc = float(ct.om.sum() ** 2 / (ct.om ** 2).sum()) if len(ct) else None
    pdv = per_day(ev, ct, var); o = dict(n_eventos=int(len(ev)), dias=int(len(pdv)), mercados=int(ev.end.nunique()), n_mercados_ev=int(ev.end.nunique()), n_eff_ctrl_kish=round(kc, 1) if kc else None,
                                         n_eff_contraste=round(1.0 / (1.0 / len(ev) + 1.0 / kc), 1) if kc and len(ev) else None)      # ADENDA_11 §4.2 (C6)
    if len(pdv) == 0: o['nota'] = 'sin dias'; return o
    d = pdv.d.values; c1 = ic_t(d); o['C1'] = dict(dif_media_dias=round(float(d.mean()), 4), ic90=[round(x, 4) for x in c1], semiancho=round((c1[1] - c1[0]) / 2, 4) if np.isfinite(c1[0]) else None, por_dia={r.D: round(r.d, 4) for r in pdv.itertuples()})
    o['C1_secundaria_ponderada_por_eventos'] = round(float((pdv.n * pdv.d).sum() / pdv.n.sum()), 4)
    nev, sw, sF, swF = mkt_arrays(ev, ct, [var]); bs = boot_mkt(nev, sw, sF, swF, 0, B); pooled = float(sF[:, 0].sum() / nev.sum() - swF[:, 0].sum() / sw.sum())
    c2 = [float(np.percentile(bs, 5)), float(np.percentile(bs, 95))] if len(bs) > 50 else [np.nan, np.nan]
    o['C2'] = dict(dif_pooled=round(pooled, 4), ic90=[round(x, 4) for x in c2], semiancho=round((c2[1] - c2[0]) / 2, 4) if np.isfinite(c2[0]) else None, B=int(len(bs)))
    ww = [o['C1']['ic90'], o['C2']['ic90']]; wid = [x[1] - x[0] if np.isfinite(x[0]) else -1 for x in ww]; k = int(np.argmax(wid))
    o['IC_mas_ancho'] = dict(cual='C1' if k == 0 else 'C2', ic90=ww[k], semiancho=round(wid[k] / 2, 4) if wid[k] >= 0 else None)
    share = (pdv.n / pdv.n.sum()).values; o['C5'] = dict(max_dia_frac_masa=round(float(share.max()), 3), cumple_35=bool(share.max() <= 0.35 + 1e-12))
    sg0 = np.sign(d.mean()); lo = {}
    for i_ in range(len(pdv)):
        r_ = np.delete(d, i_); lo[pdv.D.iat[i_]] = round(float(r_.mean()), 4) if len(r_) else None
    o['C5']['leave_one_day_out'] = lo; o['C5']['signos_iguales'] = bool(all(v is not None and np.sign(v) == sg0 and sg0 != 0 for v in lo.values())) if len(pdv) > 1 else False
    o['C5']['cumple'] = bool(o['C5']['cumple_35'] and o['C5']['signos_iguales'])
    ef = float(sF[:, 0].sum() / nev.sum()); cf = float(swF[:, 0].sum() / sw.sum()); o['tasa_evento'] = round(ef, 4); o['tasa_control_pond'] = round(cf, 4); o['LR'] = round(ef / cf, 2) if cf > 0 else None
    M_ = len(nev); lrb = []
    for _ in range(B):
        kk = rg.integers(M_, size=M_); a_, b_ = sF[kk, 0].sum() / max(nev[kk].sum(), 1e-9), swF[kk, 0].sum() / max(sw[kk].sum(), 1e-9)
        if b_ > 0: lrb.append(a_ / b_)
    o['LR_ic90_mercados'] = [round(float(np.percentile(lrb, 5)), 2), round(float(np.percentile(lrb, 95)), 2)] if len(lrb) > 50 else None
    if len(d) > 2: dd = np.sort(d)[:-2]; o['sin_2_mejores_dias'] = dict(dif_media=round(float(dd.mean()), 4), ic90=[round(x, 4) for x in ic_t(dd)])
    else: o['sin_2_mejores_dias'] = dict(nota='<3 dias')
    return o
def maxstat_block(ev, ct, vars_, B=2000):
    nev, sw, sF, swF = mkt_arrays(ev, ct, vars_); T, mx, one = perm_T(nev, sw, sF, swF, B)
    return {v: dict(T=round(float(T[i]), 3), dif_pooled=round(float(sF[:, i].sum() / nev.sum() - swF[:, i].sum() / sw.sum()), 4), p_maxstat=round(float((mx >= T[i]).mean()), 4), p_sin_corregir=round(float((one[:, i] >= T[i]).mean()), 4)) for i, v in enumerate(vars_)}
def holm(ps):
    k = sorted(ps, key=lambda x: ps[x]); m = len(k); adj = {}; run = 0.0
    for i, x in enumerate(k): run = max(run, min(1.0, (m - i) * ps[x])); adj[x] = round(run, 4)
    return adj
def decidir(dif, low1, up, hs, pmx, c5_cumple, LR, ddv, n_dias, n_ev, f1_activado=False, dif_c1all=None, up_c1all=None):
    """B4' (ADENDA_07 D1) + ADENDA_11 4d. dif = C1 media simple de dias; low1 = limite inferior IC90 C1; up/hs = limite superior y semiancho del IC90 MAS ANCHO (C1/C2); pmx = p_maxstat(V1); ddv = exceso n_mk=1 - n_mk>=2;
    F1 activo: SOPORTADA exige mismo signo en c1all; NO SOPORTADA exige limite superior del IC90 mas ancho de c1all < +0,02 (la igualdad de signo NO se exige)."""
    fin = lambda x: x is not None and np.isfinite(x)
    cond = dict(dif_mayor_0=bool(fin(dif) and dif > 0), p_maxstat_V1_lt_005=bool(fin(pmx) and pmx < 0.05), IC90_dias_C1_inferior_gt_0=bool(fin(low1) and low1 > 0), semiancho_decisivo_leq_003=bool(fin(hs) and hs <= 0.03), C5_cumple=bool(c5_cumple),
                LR_V1_geq_15=bool(LR is not None and LR >= 1.5), exceso_nmk1_geq_nmk2=bool(fin(ddv) and ddv >= 0))
    razones = []
    if n_dias < 5: razones.append(f'<5 dias validos ({n_dias})')
    if n_ev < 300: razones.append(f'n eventos primarios {n_ev} <300')
    sig_ok = (not f1_activado) or bool(fin(dif_c1all) and fin(dif) and np.sign(dif_c1all) == np.sign(dif))
    up_ok = (not f1_activado) or bool(fin(up_c1all) and up_c1all < 0.02)
    if all(cond.values()) and not razones and sig_ok: return 'SOPORTADA', cond, razones
    if n_dias >= 5 and n_ev >= 300 and fin(up) and up < 0.02 and up_ok: return 'NO SOPORTADA', cond, razones
    if not sig_ok: razones.append('F1: signo distinto (o no medido) entre universo primario y c1all (bloquea SOPORTADA)')
    if not up_ok: razones.append('F1: limite superior del IC90 mas ancho de c1all >= +0,02 o no medido (bloquea NO SOPORTADA)')
    if not cond['exceso_nmk1_geq_nmk2']: razones.append('H-ACT: exceso n_mk=1 < exceso n_mk>=2 (o sin medir)')
    razones += [f'no cumple {k}' for k, v in cond.items() if not v]
    return 'INSUFFICIENT', cond, razones
CONF = dict(etiqueta='CONFIRMATORIO', hipotesis='V1 pooled, IPW+EB, clase lo, estratos z0+normal (ADENDA_11 B1), universo primario n_mk=1 C1 sin propios; unidad = dia', dias_usados=CAND, n_dias_validos=len(CAND), dias_pendientes=PEND, dias_excluidos_E4=EXCL, dias_excluidos_incompletos=EXCL_INC)
CONF.update(B_permutaciones=2000, B_bootstrap_mercado=2000, nivel_IC=0.90, IC_C1='t de Student df=dias-1 sobre d_D (media simple)', IC_C2='bootstrap por mercado (percentiles 5/95)')
ev, ct = tabs('prim|vec', 'lo'); CONF['n_eventos_primarios'] = int(len(ev))
if len(ev) == 0:
    CONF['veredicto'] = 'INSUFFICIENT'; CONF['razones'] = ['sin eventos primarios soportados en clase lo']
else:
    CONF['V1'] = analiza(ev, ct, 'V1'); CONF['V1_e250'] = analiza(ev, ct, 'V1_e250')
    CONF['maxstat_V1_V7'] = maxstat_block(ev, ct, VAR7); CONF['maxstat_e250'] = maxstat_block(ev, ct, VAR250)
    pst, est = {}, {}
    for st_ in PRIM_ST:
        e2, c2_ = ev[ev.st == st_], ct[ct.st == st_]
        if len(e2) < 2 or len(c2_) < 2: est[st_] = dict(n_eventos=int(len(e2)), nota='sin datos'); continue
        a_ = analiza(e2, c2_, 'V1', B=1000); nev_, sw_, sF_, swF_ = mkt_arrays(e2, c2_, ['V1']); T_, mx_, one_ = perm_T(nev_, sw_, sF_, swF_, 2000); a_['p_perm_V1'] = round(float((one_[:, 0] >= T_[0]).mean()), 4); pst[st_] = a_['p_perm_V1']; est[st_] = a_
    adj = holm(pst)          # ADENDA_11 §3.3: Holm x2 sobre {z0, normal}
    for k_, v_ in adj.items(): est[k_]['p_holm_x2'] = v_
    CONF['estratos_holm'] = est
    esm, csm = tabs('prim|vec', 'lo', ('small',))          # small: EXPLORATORIO, p SIN corregir, fuera del veredicto
    if len(esm) >= 2 and len(csm) >= 2:
        a_ = analiza(esm, csm, 'V1', B=500); nev_, sw_, sF_, swF_ = mkt_arrays(esm, csm, ['V1']); T_, mx_, one_ = perm_T(nev_, sw_, sF_, swF_, 2000); a_['p_perm_V1_sin_corregir'] = round(float((one_[:, 0] >= T_[0]).mean()), 4)
    else: a_ = dict(n_eventos=int(len(esm)), nota='sin datos')
    a_['etiqueta'] = 'EXPLORATORIO (ADENDA_11 B1: fuera del veredicto y de dia_valido_E)'; CONF['small_EXPLORATORIO'] = a_
    rj_all = {D_: json.load(open(f'{H}/out/p7v12_{COIN}_{D_}{SUF}.json')) for D_ in CAND}; f1 = {D_: v['F1'] for D_, v in rj_all.items()}
    CONF['c1all_balance_E_por_dia'] = {D_: dict(fallos=v.get('E4_fallos_c1all'), pooled_z0_normal=(v.get('E_c1all', {}).get('pooled', {}) or {}).get('primario_z0_normal'),
                                                estratos={t_: {k_: e_.get(k_) for k_ in ('n_soporte', 'n_eff_contraste', 'E1_SMD_max_abs', 'E2_KS')} for t_, e_ in (v.get('E_c1all', {}).get('estratos', {}) or {}).items()}) for D_, v in rj_all.items()}      # 4d: publicado
    CONF['F1_por_dia'] = {D_: dict(max_abs_SMD=v['max_abs'], activar=v['activar_veredicto_c1all']) for D_, v in f1.items()}
    CONF['F1_activado'] = bool(any(v['activar_veredicto_c1all'] for v in f1.values()))
    evc, ctc = tabs('c1all|vec', 'lo'); CONF['c1all_V1'] = analiza(evc, ctc, 'V1', B=1000) if len(evc) else dict(nota='sin eventos'); CONF['c1all_V1']['etiqueta'] = 'CONFIRMATORIO si F1_activado, si no EXPLORATORIO'
    CONF['H_ACT_dd_nmk1_menos_nmk2_FV1'] = R.get('dd_nmk1_menos_nmk2_FV1')
    # ---- veredicto B4' (ADENDA_07 D1)
    v1 = CONF['V1']; wid = v1.get('IC_mas_ancho', {}); up = wid.get('ic90', [np.nan, np.nan])[1]; low1 = v1['C1']['ic90'][0]; dif = v1['C1']['dif_media_dias']; hs = wid.get('semiancho')
    pmx = CONF['maxstat_V1_V7']['V1']['p_maxstat']; ddv = (R.get('dd_nmk1_menos_nmk2_FV1') or {}).get('dd')
    sc = CONF['c1all_V1'].get('C1', {}).get('dif_media_dias') if CONF['F1_activado'] else None
    upc = (CONF['c1all_V1'].get('IC_mas_ancho') or {}).get('ic90', [np.nan, np.nan])[1] if CONF['F1_activado'] else None; CONF['limite_superior_IC_mas_ancho_c1all'] = round(float(upc), 4) if upc is not None and np.isfinite(upc) else None
    ver, cond, razones = decidir(dif, low1, up, hs, pmx, v1['C5']['cumple'], v1.get('LR'), ddv, len(CAND), CONF['n_eventos_primarios'], CONF['F1_activado'], sc, upc)
    if DISENO: ver = 'NO_APLICA_DISENO'
    CONF['condiciones_SOPORTADA'] = cond; CONF['limite_superior_IC_mas_ancho'] = round(float(up), 4) if np.isfinite(up) else None; CONF['veredicto'] = ver; CONF['razones'] = razones
    CONF['reglas'] = 'B4 reescrita por ADENDA_07 D1: NO SOPORTADA = n>=300, >=5 dias validos, limite superior del IC90 mas ancho (C1/C2) < +0,02; ADENDA_11 4d: con F1 activo tambien c1all (limite superior < +0,02); signo igual solo para SOPORTADA'
    EXPL = dict(etiqueta='EXPLORATORIO')
    for v in ('V2', 'V3', 'V4', 'V5', 'V6', 'V7'): EXPL['variante_' + v] = analiza(ev, ct, v, B=500)
    for cl_ in ('hi', 'indet'):
        e3, c3 = tabs('prim|vec', cl_); EXPL['clase_' + cl_] = analiza(e3, c3, 'V1', B=500) if len(e3) else dict(nota='sin eventos soportados')
    e4, c4 = tabs('prim|propio', 'lo'); EXPL['solo_nivel_propio_V1'] = analiza(e4, c4, 'V1', B=500) if len(e4) else dict(nota='sin eventos')
    e5, c5_ = ev[ev.st != 'z0'], ct[ct.st != 'z0']; EXPL['sin_z0_V1'] = analiza(e5, c5_, 'V1', B=500) if len(e5) else dict(nota='sin eventos')
    CONF['EXPLORATORIO'] = EXPL
R['CONFIRMATORIO'] = CONF; R['semilla_confirmatorio'] = 20261118
json.dump(R, open(OUTJ, 'w'), indent=1, default=str)
print('p3 OK', OUTJ, 'etiqueta', R['ETIQUETA'], 'dias', CAND)
