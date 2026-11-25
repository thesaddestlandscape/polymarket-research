#!/usr/bin/env python3
"""e1_modelo.py -- R1v2 FASE B (pendiente 1): E1 (logistica L2, C=1) -> q(x_t)=P(ganar|relleno), mu = q/L - 1 (maker, fee 0, rebate 0 primario), mu_ucb = percentil 90 de mu sobre remuestreos POR DIAS del TRAIN.
Entrenamiento SOLO con TRAIN (26-28 Oct + 03-06 Nov, PREREG sec.6): cualquier otro dia -> ValueError (fail-closed). Rasgos con rx<=t (Binance con rx<=t-1000). Rasgo NaN -> fila NO evaluable: se excluye del
entrenamiento y la regla no se aplica (nunca y=0; el test de fuga por rasgo mide si el indicador de NaN predice el desenlace). IPW: 1/S(t) con S = supervivencia del hazard v11 (L2 C=1, mismos rasgos, entrenado en TRAIN), truncada p99.
LIMITE DECLARADO (no es el E1 completo del diseno sec.2): rasgos de L1 con rx<=t (grupos E, A1, B1/B2, C) = 'E1-L1'. PENDIENTES por falta de L2/prints/15m en el replay: A3-A5 (masa evaporada/niveles mejores), D (15m), F (flujo propio), hazard sobre TRAIN (los HZ_*.pkl existentes son de octubre 20-23).
0 ordenes, 0 red."""
import sys, os
import numpy as np, pandas as pd
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; V = os.path.dirname(HV.rstrip('/')) + '/'; BSIM = os.path.dirname(V.rstrip('/')) + '/'
sys.path.insert(0, HV); sys.path.insert(0, V + 'r1v2_sec7/'); sys.path.insert(0, BSIM)
import variantes_b as VB, sec7_core as C, l2_rasgos as L2
TRAIN_DIAS = ('2026-10-26', '2026-10-27', '2026-10-28', '2026-11-03', '2026-11-04', '2026-11-05', '2026-11-06')
FEATS = ['dist', 'spread', 'lbsz', 'lask', 'Tc', 'yes', 'c_eth', 'c_sol', 'cbb', 'dcbb1', 'par', 'r5', 'r30']
FEATS_L2 = [f for g in ('A5', 'F', 'A3', 'A4', 'D1', 'D2') for f in L2.GRUPOS[g]]; FEATS_ALL = FEATS + FEATS_L2; GRUPOS_E1 = dict(E=FEATS, **L2.GRUPOS)
GRID_MS = 250; MAX_AGE = 30000; SEED = 20261119; C_REG = 1.0

def rasgos(own, comp, t, L, T_s, coin, lado, bsrc, max_age=MAX_AGE, l2=None, ctx=None):
    """dict FEATS -> valor | NaN. Solo estados con rx <= t (SerieL1.idx_rx); estado rancio (>30 s) o libro cruzado/ausente -> NaN (no se imputa); Binance con rx <= t-1000 (VB.ret_bps) y signo a favor de nuestro lado."""
    nan = float('nan'); f = {k: nan for k in FEATS_ALL}; f['yes'] = 1.0 if lado == 'YES' else 0.0; f['c_eth'] = 1.0 if str(coin).lower() == 'eth' else 0.0; f['c_sol'] = 1.0 if str(coin).lower() == 'sol' else 0.0
    f['Tc'] = float(T_s) / 300.0
    if own is not None and comp is not None:
        i, ic = own.idx_rx(t), comp.idx_rx(t)
        if i >= 0 and ic >= 0 and t - int(own.rx[i]) <= max_age and t - int(comp.rx[ic]) <= max_age and C._valido(own.bid[i], own.ask[i])[0] and C._valido(comp.bid[ic], comp.ask[ic])[0]:
            f['dist'] = float(own.bid[i] - L); f['spread'] = float(own.ask[i] - own.bid[i]); f['lbsz'] = float(np.log1p(own.bsz[i])) if own.bsz[i] >= 0 else nan; f['lask'] = float(np.log1p(own.asz[i])) if own.asz[i] >= 0 else nan
            f['cbb'] = float(comp.bid[ic]); f['par'] = float(own.ask[i] + comp.ask[ic] - 1.0); j = comp.idx_rx(t - 1000)
            if j >= 0 and t - 1000 - int(comp.rx[j]) <= max_age and np.isfinite(comp.bid[j]): f['dcbb1'] = float(comp.bid[ic] - comp.bid[j])
    if bsrc is not None:
        tb, pb = bsrc; sg = 1.0 if lado == 'YES' else -1.0
        for nom, w in (('r5', 5000), ('r30', 30000)): f[nom] = float(sg * VB.ret_bps(tb, pb, [int(t) - 1000], w)[0])
    if l2 is not None and ctx is not None: f.update(l2.rasgos(ctx['tok'], t, L, lado, coin, ctx['fin']))      # L2/15m/D2: misma funcion en TRAIN/SELECCION/HOLD; no evaluable = NaN
    return f

def vector(f, feats=FEATS): return np.array([f[k] for k in feats], float)

class E1:
    def __init__(self, C=C_REG, B=200, seed=SEED, feats=None): self.feats = list(feats or FEATS); self.C = C; self.B = B; self.seed = seed; self.modelos = []; self.base = None
    def _fit(self, X, y, w):
        from sklearn.linear_model import LogisticRegression
        from sklearn.preprocessing import StandardScaler
        from sklearn.pipeline import make_pipeline
        m = make_pipeline(StandardScaler(), LogisticRegression(C=self.C, max_iter=2000)); m.fit(X, y, logisticregression__sample_weight=w); return m
    def ajusta(self, X, y, dia, w=None):
        """X (n, len(FEATS)) sin NaN, y in {0,1} (gana del relleno), dia (n,), w pesos (por orden x IPW). Remuestreo bootstrap POR DIAS (con reemplazo) para el limite superior."""
        X = np.asarray(X, float); y = np.asarray(y, int); dia = np.asarray(dia); w = np.ones(len(y)) if w is None else np.asarray(w, float)
        mal = sorted(set(dia.tolist()) - set(TRAIN_DIAS))
        if mal: raise ValueError(f'dias fuera de TRAIN: {mal}')
        if np.isnan(X).any(): raise ValueError('NaN en rasgos de entrenamiento: excluir filas ANTES (no se imputa)')
        dias = sorted(set(dia.tolist()))
        if len(dias) < 3 or len(set(y.tolist())) < 2: raise ValueError('INSUFFICIENT: <3 dias o una sola clase')
        self.base = self._fit(X, y, w); rng = np.random.default_rng(self.seed); self.modelos = []
        for _ in range(self.B):
            ds = rng.choice(len(dias), len(dias), replace=True); ix = np.concatenate([np.where(dia == dias[j])[0] for j in ds])
            if len(set(y[ix].tolist())) < 2: continue
            self.modelos.append(self._fit(X[ix], y[ix], w[ix]))
        self.dias = dias; self.n = int(len(y)); return self
    def q(self, X): return self.base.predict_proba(np.atleast_2d(np.asarray(X, float)))[:, 1]
    def mu(self, X, L, ucb_pct=90):
        """(mu_hat, mu_ucb): mu = q/L - 1; ucb = percentil 90 de mu sobre los modelos bootstrap-por-dias. NaN en X -> (nan, nan)."""
        X = np.atleast_2d(np.asarray(X, float)); L = np.broadcast_to(np.asarray(L, float), (len(X),)); ok = ~np.isnan(X).any(axis=1); mh = np.full(len(X), np.nan); mu = np.full(len(X), np.nan)
        if ok.any():
            mh[ok] = self.q(X[ok]) / L[ok] - 1.0; Q = np.stack([m.predict_proba(X[ok])[:, 1] for m in self.modelos]) if self.modelos else self.q(X[ok])[None, :]
            mu[ok] = np.percentile(Q / L[ok][None, :] - 1.0, ucb_pct, axis=0)
        return mh, mu

def supervivencia(h):
    """S_j = prod_{i<j}(1 - h_i) con h = hazard por intervalo de 250 ms (v11): prob. de que la orden NO haya sido cerrada antes del punto j (S_0 = 1)."""
    h = np.clip(np.asarray(h, float), 0.0, 1.0); return np.concatenate([[1.0], np.cumprod(1.0 - h)[:-1]]) if len(h) else h

def pesos_ipw(S, trunc_pct=99, piso=1e-6):
    """w = 1/S truncado en el percentil `trunc_pct` de TODOS los pesos (declarado); sensibilidad sin IPW = w=1."""
    w = 1.0 / np.maximum(np.asarray(S, float), piso); return np.minimum(w, np.percentile(w, trunc_pct)) if len(w) else w

def entrena_hazard(B, F, dia_col='dia', y_col='y'):
    """hazard de llegada por intervalos (v11: StandardScaler + logistica L2 C=1) entrenado SOLO con dias TRAIN. B sin NaN."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import make_pipeline
    mal = sorted(set(B[dia_col]) - set(TRAIN_DIAS))
    if mal: raise ValueError(f'dias fuera de TRAIN: {mal}')
    if B[F].isna().any().any(): raise ValueError('NaN en rasgos del hazard')
    return make_pipeline(StandardScaler(), LogisticRegression(C=1.0, max_iter=2000)).fit(B[F], B[y_col])

def platt(q, y):
    """calibracion Platt (dia CALIB 07-Nov): devuelve f(q)->q_cal. Solo con >=2 clases."""
    from sklearn.linear_model import LogisticRegression
    q = np.clip(np.asarray(q, float), 1e-6, 1 - 1e-6); z = np.log(q / (1 - q)).reshape(-1, 1); m = LogisticRegression(C=1e6, max_iter=1000).fit(z, np.asarray(y, int))
    return lambda x: m.predict_proba(np.log(np.clip(np.asarray(x, float), 1e-6, 1 - 1e-6) / (1 - np.clip(np.asarray(x, float), 1e-6, 1 - 1e-6))).reshape(-1, 1))[:, 1]

def puntos_orden(o, own, comp, bsrc, t_proc, l_cancel=VB.L_CANCEL['primaria'], grid=GRID_MS, l2=None, ctx=None):
    """puntos (orden, t) en rejilla 250 ms desde la colocacion (t_dec) hasta min(t_end, tf - (t_proc+L_cancel+20)): solo puntos desde los que una cancelacion seria efectiva. o: dict(t_dec,t_end,tf,q,L,lado,coin,fin,gana,dia,mid,n_ord).
    Una fila por punto con rasgos (NaN si no evaluable), y (gana del relleno; solo ordenes rellenadas), peso por orden = 1/n_puntos (cada orden suma 1)."""
    lc = t_proc + l_cancel + VB.MARGEN_CASADO_MS; filled = o['q'] > 0 and o['tf'] is not None and o['tf'] >= 0; t1 = int(o['t_end']) if not filled else int(min(o['t_end'], o['tf'] - lc))
    ts = [int(o['t_dec'])] + list(range(int(o['t_dec']) + grid, t1 + 1, grid)); rows = []      # el ALTA (t_dec) SIEMPRE (no armar no exige latencia de cancelacion); el tope tf-(t_proc+L+20) solo recorta los puntos de VIDA
    for t in ts:
        f = rasgos(own, comp, t, o['L'], o['fin'] - t / 1000.0, o['coin'], o['lado'], bsrc, l2=l2, ctx=ctx); f.update(fin=o['fin'], es_alta=bool(t == int(o['t_dec'])), dia=o['dia'], mid=o['mid'], n_ord=o['n_ord'], t=t, L=o['L'], y=int(o['gana'] > 0.5), relleno=bool(filled), tf=o['tf'] if filled else np.nan); rows.append(f)
    P = pd.DataFrame(rows)
    if len(P): P['w_orden'] = 1.0 / len(P)
    return P

def fuga_nan_por_rasgo(P, banda=(0.40, 0.60), n_min=20, feats=None):
    """test de fuga POR RASGO (contrato sec.11-5): el indicador 'rasgo NaN' no debe predecir el desenlace (AUC por dia en banda). Solo rasgos con >= n_min NaN en el dia."""
    from puerta0_core import auc
    out = {}
    for k in (feats or FEATS_ALL):
        filas = []
        for d, g in P.groupby('dia'):
            ind = g[k].isna().astype(int).values; y = g.y.values
            if ind.sum() >= n_min and ind.sum() < len(ind): filas.append((d, auc(ind, y)[0], int(ind.sum())))
        fuera = [d for d, a, n in filas if np.isfinite(a) and (a < banda[0] or a > banda[1])]
        out[k] = dict(dias_evaluables=len(filas), auc_por_dia={d: a for d, a, n in filas}, dias_fuera_banda=fuera, estado='INSUFFICIENT' if not filas else ('FUGA_SOSPECHOSA' if fuera else 'OK'))
    return out

class PuntuaE1:
    """callable(m, k, t, L) -> (f5t, mu_hat, mu_ucb) para HookE1. serie(k)->SerieL1; comp por el mercado m (ku/kd); bsrc = {coin: (t_rx, px)}. F5_t = sec7_core.f5t (None = invalido -> devuelve None)."""
    def __init__(self, modelo, serie, bsrc, l2=None, k2tok=None): self.M = modelo; self.serie = serie; self.b = bsrc; self.l2 = l2; self.k2tok = k2tok or {}
    def __call__(self, m, k, t, L):
        kc = m.kd if k == m.ku else m.ku; own, comp = self.serie(k), self.serie(kc); f5 = C.f5t(own, int(t))
        if f5 is None: return None
        lado = 'YES' if k == m.ku else 'NO'; f = rasgos(own, comp, int(t), L, m.fin - t / 1000.0, m.coin, lado, self.b.get(m.coin), l2=self.l2, ctx=dict(tok=self.k2tok.get(k), fin=m.fin) if self.l2 is not None and self.k2tok.get(k) else None); x = vector(f, getattr(self.M, 'feats', FEATS))
        if np.isnan(x).any(): return (f5, float('nan'), float('nan'))
        mh, mu = self.M.mu(x, L); return (f5, float(mh[0]), float(mu[0]))

def pesos_orden(P):
    """peso de cada fila = 1 / (n de filas SUPERVIVIENTES de su orden): cada orden suma 1 DESPUES de quitar los NaN (no el 1/len previo a la exclusion)."""
    return 1.0 / P.groupby('ord_id')['y'].transform('size')

def ablacion(P, modelos, C=C_REG):
    """ABLACION por grupo y baseline 'solo E' (diseno sec.2): modelos {nombre: [rasgos]}; P = filas de relleno SIN NaN en la union de rasgos (MISMAS filas para todos: comparacion justa). Leave-one-day-out: logloss (peso de orden) y AUC por dia del dia excluido."""
    from sklearn.metrics import log_loss
    from puerta0_core import auc
    out = {}; dias = sorted(P.dia.unique())
    for nom, fs in modelos.items():
        res = {}
        for d in dias:
            tr = P[P.dia != d]; te = P[P.dia == d]
            if len(set(tr.y.tolist())) < 2 or not len(te): continue
            m = E1(C=C, B=0)._fit(tr[fs].values, tr.y.values, tr.w_orden.values); q = m.predict_proba(te[fs].values)[:, 1]
            res[d] = dict(n=int(len(te)), logloss=float(log_loss(te.y.values, q, labels=[0, 1], sample_weight=te.w_orden.values)), auc=float(auc(q, te.y.values)[0]) if len(set(te.y.tolist())) > 1 else float('nan'))
        out[nom] = dict(n=int(len(P)), n_rasgos=len(fs), por_dia=res, logloss_medio_dias=float(np.mean([v['logloss'] for v in res.values()])) if res else float('nan'))
    return out
