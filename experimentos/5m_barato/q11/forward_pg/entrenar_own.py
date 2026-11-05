#!/usr/bin/env python3
"""PREREG_Q11_PG_O50 - entrenamiento UNICO del modelo OWN CONGELADO (antes del 06-Nov 00:00Z). DEV, solo lectura de datos, 0 ordenes.
Reconstruye para 26-Oct..04-Nov las filas de la rejilla de decision de barrido_corr/passC1.py (sha 9e08dfef...) con SOLO los rasgos OWN
(T, L, bid-L, moneda, lado) y la etiqueta yN60, en el MISMO orden de filas, para que la submuestra 12 % (semilla = fecha) sea la de passC2o.py.
(1) Verificacion de fidelidad: reentrena el modelo walk-forward del 04-Nov (dias 26-Oct..03-Nov) y lo compara con C2o_thr.json y Po_2026-11-04.pkl.
(2) Congelado: mismos hiperparametros sobre los 10 dias; umbral = cuantil 0,5 de p in-sample (c = 0,5, misma definicion que C2o).
Salida: modelo_own.pkl, modelo_own.json, out/entrenar_own.log, cache out/c1own_<D>.pkl.
Uso: cd forward_pg && nice -n 19 ionice -c3 bash -c 'ulimit -v 3000000; OMP_NUM_THREADS=1 python3 -I -W ignore entrenar_own.py'"""
import sys, os, json, time, gc, hashlib, pickle, numpy as np, pandas as pd, warnings; warnings.filterwarnings('ignore')
import sklearn
from sklearn.ensemble import HistGradientBoostingClassifier as HGB
T0 = time.time()
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = H + 'out/'; os.makedirs(OUT, exist_ok=True)
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
sys.path.insert(0, P2 + 'escalera_B'); import engine as G
PB = P2 + 'precursores_barrido/out/'; BC = '/root/polymarket-research/experimentos/5m_barato/q11/barrido_corr/out/'
DIAS = ['2026-10-26', '2026-10-27', '2026-10-28', '2026-10-29', '2026-10-30', '2026-10-31', '2026-11-01', '2026-11-02', '2026-11-03', '2026-11-04']
OWN = ['T', 'L', 'bidL', 'act_i', 'lado_i']
PAR = dict(max_depth=3, max_iter=120, learning_rate=0.05, min_samples_leaf=200, l2_regularization=5.0, random_state=0)   # = passC2o.py
LOG = []
def log(s): print(s, flush=True); LOG.append(str(s))

def c1own(d):
    f = OUT + f'c1own_{d}.pkl'
    if os.path.exists(f): return pd.read_pickle(f)
    tape = pd.read_pickle(PB + f'tape_{d}.pkl'); bad = {tuple(x) for x in json.load(open(PB + f'bad_{d}.json'))['bad']}
    E = G.DayEng(d, 'chain', tape, bad); D = E.D
    # eventos de la cinta con hora re-sincronizada (literal de passC1.py)
    tp = tape.assign(k=tape.token_id.map(D.tokidx)); tp = tp[tp.k.notna()].copy(); tp['k'] = tp.k.astype(int); tp['blq'] = (tp.src.astype(str) != 'tx_ws'); tp['pr3'] = tp.price.round(3)
    ev = tp.groupby(['k', 'tx']).agg(t=('t_ws_ms', 'min'), pmin=('price', 'min'), pmax=('price', 'max'), npr=('pr3', 'nunique'), nmk=('maker', 'nunique'), sh=('sh', 'sum'), blq=('blq', 'max')).reset_index()
    del tp, tape; gc.collect()
    tm = np.empty(len(ev), np.int64); evk = ev.k.values; evt = ev.t.values.astype(np.int64); evp = ev.pmin.values
    for i in range(len(ev)):
        k = evk[i]; t = evt[i]; pm = evp[i]
        a, b = D.qb[k], D.qb[k + 1]; qt = D.qt[a:b]; v0 = D.v0[a:b]
        i0 = np.searchsorted(qt, t - 400, side='left'); i1 = np.searchsorted(qt, t, side='right'); tm[i] = t - 63
        if i1 > i0 and i0 > 0:
            lo = v0[i0 - 1:i1] <= pm + G.TOLP; w = np.where(lo[1:] & ~lo[:-1])[0]
            if len(w): tm[i] = int(qt[i0 + w[0]])
    ev['tm'] = tm
    EVN = {int(k): (g.tm.values.astype(np.int64), g.pmin.values, g.npr.values, g.nmk.values) for k, g in ev[~ev.blq.values].sort_values('tm').groupby('k')}
    ks = [k for k in E.ks if E.sane(k) == 'ok' and G.capt_outcome(E, k) is not None]
    def lab(k, L, g, h):
        a = EVN.get(k)
        if a is None: return np.zeros(len(g), bool)
        te = a[0][(a[2] >= 2) & (a[1] < L - G.TOLP)]
        return (np.searchsorted(te, g + h, side='right') - np.searchsorted(te, g + G.LAT_POST, side='right')) > 0
    blocks = []
    for k in ks:
        g, bid, ask, b15, vol, hora = E.feats(k); fin = int(D.fin[k]); gm = {L: G.gate_vec('G', L, b15, vol, hora) for L in G.LEVELS}
        anyg = np.zeros(len(g), bool)
        for L in G.LEVELS: anyg |= gm[L]
        if not anyg.any(): continue
        for L in G.LEVELS:
            m = gm[L]
            if not m.any(): continue
            blocks.append(pd.DataFrame(dict(k=np.full(m.sum(), k, np.int32), t=g[m], L=np.full(m.sum(), L, np.float32), T=((fin * 1000 - g[m]) / 1000.0).astype(np.float32),
                                            bidL=(bid[m] - L).astype(np.float32), yN60=lab(k, L, g, 60000)[m])))
    C = pd.concat(blocks, ignore_index=True)
    C['act'] = [D.act[k] for k in C.k.values]; C['lado'] = [D.lado[k] for k in C.k.values]
    C['act_i'] = C.act.map({'ETH': 0, 'SOL': 1, 'XRP': 2}).astype(np.int8); C['lado_i'] = (C.lado == 'YES').astype(np.int8)
    C = C[['k', 't', 'L', 'T', 'bidL', 'act_i', 'lado_i', 'yN60']]
    C.to_pickle(f + '.tmp'); os.replace(f + '.tmp', f); del E, D; gc.collect()
    log(f'c1own {d}: filas {len(C)} yN60 {C.yN60.mean():.4f} ({time.time() - T0:.0f} s)')
    return C

SUB = {}; NFULL = {}
for d in DIAS:
    C = c1own(d); NFULL[d] = len(C); rng = np.random.default_rng(int(d.replace('-', '')))
    SUB[d] = C[rng.random(len(C)) < 0.12].reset_index(drop=True); del C; gc.collect()
# (1) verificacion contra el walk-forward del 04-Nov de passC2o
TR = pd.concat([SUB[x] for x in DIAS[:9]], ignore_index=True)
m = HGB(**PAR).fit(TR[OWN], TR.yN60.values.astype(int)); ptr = m.predict_proba(TR[OWN])[:, 1]; thr_v = float(np.quantile(ptr, 0.5))
ref = json.load(open(BC + 'C2o_thr.json'))['2026-11-04']['OWN']['0.5']
TE = c1own('2026-11-04'); pte = m.predict_proba(TE[OWN])[:, 1].astype(np.float32); Po = pd.read_pickle(BC + 'Po_2026-11-04.pkl')
mismo_orden = len(Po) == len(TE) and bool((Po.k.values == TE.k.values).all()) and bool((Po.t.values == TE.t.values).all())
dmax = float(np.abs(Po.p_OWN.values - pte).max()) if mismo_orden else float('nan')
log(f'VERIFICACION walk-forward 04-Nov: filas train {len(TR)} | umbral {thr_v!r} vs C2o {ref!r} (dif {abs(thr_v - ref):.2e}) | filas test {len(TE)} vs Po {len(Po)} mismo orden {mismo_orden} | max|p - p_Po| {dmax:.2e}')
VER_OK = mismo_orden and abs(thr_v - ref) < 1e-9 and dmax < 1e-6
log(f'VERIFICACION {"OK" if VER_OK else "FALLA"}')
del TR, TE, Po, m; gc.collect()
if not VER_OK: log('ABORTO: el entrenamiento no reproduce passC2o; no se congela modelo'); open(OUT + 'entrenar_own.log', 'w').write('\n'.join(LOG) + '\n'); sys.exit(2)
# (2) modelo congelado sobre los 10 dias
TR = pd.concat([SUB[x] for x in DIAS], ignore_index=True); y = TR.yN60.values.astype(int)
M = HGB(**PAR).fit(TR[OWN], y); ptr = M.predict_proba(TR[OWN])[:, 1]; THR = float(np.quantile(ptr, 0.5))
cob = {d: round(float((M.predict_proba(SUB[d][OWN])[:, 1] <= THR).mean()), 3) for d in DIAS}
# sonda fija para detectar cambios de libreria/pickle
pr = [(T, L, bl, a, s) for T in (65.0, 120.0, 180.0, 239.0) for L in G.LEVELS for bl in (-0.02, 0.0, 0.03, 0.06, 0.10, np.nan) for a in (0, 1, 2) for s in (0, 1)]
PR = pd.DataFrame(pr, columns=OWN).astype({'T': np.float32, 'L': np.float32, 'bidL': np.float32, 'act_i': np.int8, 'lado_i': np.int8})
ps = M.predict_proba(PR[OWN])[:, 1]; sonda_sha = hashlib.sha256(np.round(ps, 10).tobytes()).hexdigest()
pickle.dump(M, open(H + 'modelo_own.pkl.tmp', 'wb')); os.replace(H + 'modelo_own.pkl.tmp', H + 'modelo_own.pkl')
msha = hashlib.sha256(open(H + 'modelo_own.pkl', 'rb').read()).hexdigest()
meta = dict(regla='PG_O50', rasgos=OWN, hiperparametros=PAR, dias_entrenamiento=DIAS, submuestra='12 % por dia, rng = default_rng(int(fecha)) como passC2o.py',
            filas_train=int(len(TR)), pos_train=round(float(y.mean()), 5), umbral_c05=THR, cobertura_in_sample=cob, filas_rejilla_por_dia=NFULL,
            sklearn=sklearn.__version__, numpy=np.__version__, pandas=pd.__version__, modelo_sha256=msha, sonda_sha256=sonda_sha, n_sonda=len(PR),
            verificacion=dict(umbral_wf_0411=thr_v, umbral_c2o_0411=ref, max_dif_p=dmax, ok=VER_OK), creado_utc=pd.Timestamp.utcnow().isoformat())
json.dump(meta, open(H + 'modelo_own.json', 'w'), indent=1)
log(f'CONGELADO: filas train {len(TR)} pos {y.mean():.4f} | umbral c=0,5 {THR!r} | cobertura in-sample {cob} | modelo sha256 {msha} | sonda {sonda_sha[:16]} | {time.time() - T0:.0f} s')
open(OUT + 'entrenar_own.log', 'w').write('\n'.join(LOG) + '\n')
