"""qlib.py -- funciones comunes Q-TECHO (modelos, reglas, bootstrap/permutacion por cierre). Sin red."""
import numpy as np, pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.isotonic import IsotonicRegression
from sklearn.preprocessing import StandardScaler
COINS = ('ETH', 'SOL', 'XRP')
NUM_FWD = ['pc', 'T', 'vol30', 'bb', 'ba', 'bs', 'spread', 'depth_ticks', 'b15', 'a15', 'lvl15', 'gap15', 'd15_30', 'dbb30', 'vol30ws', 'r60f', 'rpre_s', 'CON']
NUM_FULL = NUM_FWD + ['gap_last', 'dp5', 'dp30', 'dp60', 'hi60', 'rng60', 'd_open', 'vol_all', 'flow60', 'fv_gap', 'z', 'sig_bps_s', 'b10']
MISS = ['b15', 'bb', 'r60f', 'rpre_s']
def logit(p): p = np.clip(p, 1e-4, 1 - 1e-4); return np.log(p / (1 - p))
def design(T, cols):
    X = T[cols].astype(float).copy()
    for m in MISS: X['miss_' + m] = T[m].isna().astype(float)
    h = T.hora.values.astype(float); X['hs'] = np.sin(2 * np.pi * h / 24); X['hc'] = np.cos(2 * np.pi * h / 24)
    X['lpc'] = logit(T.pc.values)
    return X
class Imp:
    def fit(self, X): self.med = X.median(); return self
    def tr(self, X): return X.fillna(self.med).fillna(0.0)
def tramo(pc): return np.clip(np.floor((np.asarray(pc, float) - 1e-9) / 0.05 + 1e-9).astype(int) - 2, 0, 3)   # (0.10-0.15]..(0.25-0.30] -> 0..3
# ---------------- modelos
class MapQ:
    def __init__(self, k=50): self.k = k
    def fit(self, T):
        self.m0 = T.gana_f.mean(); self.tab = {}
        g = T.assign(tr=tramo(T.pc.values)).groupby('tr').gana_f.agg(['sum', 'count'])
        for i in range(4):
            s, n = (g.loc[i, 'sum'], g.loc[i, 'count']) if i in g.index else (0, 0)
            self.tab[i] = (s + self.k * self.m0) / (n + self.k)
        return self
    def predict(self, T): return np.array([self.tab[i] for i in tramo(T.pc.values)])
class LogQ:
    def __init__(self, cols, C): self.cols, self.C = cols, C
    def fit(self, T):
        X = design(T, self.cols); self.imp = Imp().fit(X); X = self.imp.tr(X); self.sc = StandardScaler().fit(X)
        self.m = LogisticRegression(C=self.C, max_iter=1000).fit(self.sc.transform(X), T.gana_f.values); return self
    def predict(self, T): return self.m.predict_proba(self.sc.transform(self.imp.tr(design(T, self.cols))))[:, 1]
class HgbQ:
    def __init__(self, cols, seed=20261024): self.cols, self.seed = cols, seed
    def fit(self, T):
        X = design(T, self.cols)
        self.m = HistGradientBoostingClassifier(max_depth=3, max_iter=150, learning_rate=0.05, l2_regularization=1.0, min_samples_leaf=200, random_state=self.seed).fit(X, T.gana_f.values); self.cols_x = list(X.columns); return self
    def predict(self, T): return self.m.predict_proba(design(T, self.cols)[self.cols_x])[:, 1]
def make(fam, cols=None, C=None):
    if fam == 'MAP': return MapQ()
    if fam == 'LOGIT': return LogQ(cols, C)
    if fam == 'HGB': return HgbQ(cols)
def fit_cal(fam, cols, C, Ttr):
    """modelo final + isotonica sobre predicciones fuera de muestra de 3 bloques contiguos de dias."""
    mod = make(fam, cols, C).fit(Ttr)
    if fam == 'MAP': return mod, None
    days = sorted(Ttr.dia.unique()); bl = np.array_split(np.arange(len(days)), 3); oof = np.full(len(Ttr), np.nan)
    for b in bl:
        te = Ttr.dia.isin([days[i] for i in b]).values
        if te.all() or (~te).sum() < 500: continue
        oof[te] = make(fam, cols, C).fit(Ttr[~te]).predict(Ttr[te])
    ok = np.isfinite(oof)
    iso = IsotonicRegression(out_of_bounds='clip', y_min=0.001, y_max=0.999).fit(oof[ok], Ttr.gana_f.values[ok])
    return mod, iso
def pred(mod, iso, T): q = mod.predict(T); return q if iso is None else iso.predict(q)
# ---------------- reglas y metricas
def stats(df, skip):
    c, p = df.c.values, df.p.values; r = ~skip
    return dict(n=int(len(df)), n_skip=int(skip.sum()), ret=float(c[r].sum() / c.sum()) if c.sum() > 0 else np.nan, ev_all=float(p.sum() / c.sum()),
                ev_ret=float(p[r].sum() / c[r].sum()) if c[r].sum() > 0 else np.nan, ev_skip=float(p[skip].sum() / c[skip].sum()) if c[skip].sum() > 0 else np.nan, dpnl=float(-p[skip].sum()), pnl_ret=float(p[r].sum()))
def clus(df): return pd.factorize(df.cierre.values)[0]
def boot(vals, cl, nb=2000, seed=20261024):
    """IC90 del TOTAL (suma de vals) por cierre. vals ya por unidad."""
    k = cl.max() + 1; s = np.bincount(cl, weights=vals, minlength=k); rng = np.random.default_rng(seed); idx = rng.integers(0, k, (nb, k))
    tot = s[idx].sum(1); return float(np.percentile(tot, 5)), float(np.percentile(tot, 95))
def boot_ratio(num, den, cl, nb=2000, seed=20261024):
    k = cl.max() + 1; sn = np.bincount(cl, weights=num, minlength=k); sd = np.bincount(cl, weights=den, minlength=k); rng = np.random.default_rng(seed); idx = rng.integers(0, k, (nb, k))
    r = sn[idx].sum(1) / np.maximum(sd[idx].sum(1), 1e-12); return float(np.percentile(r, 5)), float(np.percentile(r, 95))
def perm_cierre(df, skip, nperm=2000, seed=20261024):
    """p (unilateral dPnL >= observado) con banderas aleatorias a nivel (cierre,moneda,tramo) con la tasa de skip del estrato dia x moneda x tramo."""
    d = df.assign(sk=skip.astype(float), tr=tramo(df.pc.values))
    rate = d.groupby(['dia', 'act', 'tr']).sk.transform('mean').values
    cell = d.assign(rate=rate).groupby(['cierre', 'act', 'tr', 'dia']).agg(sp=('p', 'sum'), rate=('rate', 'first')).reset_index()
    rng = np.random.default_rng(seed); draws = rng.random((nperm, len(cell))) < cell.rate.values[None, :]
    nul = -(draws * cell.sp.values[None, :]).sum(1); obs = -df.p.values[skip].sum()
    return float((1 + (nul >= obs).sum()) / (nperm + 1)), float(nul.mean()), float(np.percentile(nul, 95))
def por_dia(df, skip):
    out = {}
    for d, g in df.groupby('dia'): out[d] = float(-g.p.values[skip[g.index.values] if False else skip[df.index.get_indexer(g.index)]].sum())
    return out
def lossd(y, q1, q2, kind):
    q1 = np.clip(q1, 0.005, 0.995); q2 = np.clip(q2, 0.005, 0.995)
    if kind == 'll': return -(y * np.log(q1) + (1 - y) * np.log(1 - q1)) + (y * np.log(q2) + (1 - y) * np.log(1 - q2))
    return (q1 - y) ** 2 - (q2 - y) ** 2
def ic_mean(vals, cl, nb=2000, seed=20261024):
    k = cl.max() + 1; s = np.bincount(cl, weights=vals, minlength=k); n = np.bincount(cl, minlength=k).astype(float)
    rng = np.random.default_rng(seed); idx = rng.integers(0, k, (nb, k)); m = s[idx].sum(1) / n[idx].sum(1)
    return float(vals.mean()), float(np.percentile(m, 5)), float(np.percentile(m, 95))
