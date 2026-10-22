"""scanlib.py -- barrido de reglas (good/bad) con estadistico t de la diferencia de EV ponderado por EUR y p FWER por max-estadistico
(permutacion de FILAS dentro de dia). Tabla T: columnas c (coste), pn (pnl), dia, + rasgos. Reglas: rasgo>=q / rasgo<=q (cuantiles de DESCUBRIMIENTO),
y categorias 'no X'. Una regla define 'buenos' (se cotiza) y 'malos' (se descarta)."""
import numpy as np, pandas as pd
QS = (0.1, 0.25, 0.5, 0.75, 0.9)
def build_rules(T, feats, dis, cats):
    """Devuelve lista de reglas (nombre, funcion(T)->bool buenos) con umbrales fijados con la parte de descubrimiento."""
    R = []
    for f in feats:
        v = T.loc[dis, f].values; v = v[np.isfinite(v)]
        for q in QS:
            thr = float(np.quantile(v, q))
            R.append((f'{f}>={thr:.4g}(q{q})', f, '>=', thr)); R.append((f'{f}<={thr:.4g}(q{q})', f, '<=', thr))
    for c, vals in cats.items():
        for x in vals: R.append((f'{c}!={x}', c, '!=', x))
    return R
def masks(T, R):
    M = np.zeros((len(R), len(T)), dtype=np.float32)
    for i, (_, f, op, thr) in enumerate(R):
        x = T[f].values
        if op == '>=': m = x >= thr
        elif op == '<=': m = x <= thr
        else: m = x != thr
        M[i] = np.where(np.isfinite(x) if x.dtype.kind == 'f' else True, m, False)
    return M
def stats(M, pn, c):
    """t de (EV_buenos - EV_malos) y EVs, vectorizado. M: reglas x N (1 = bueno)."""
    V = np.stack([pn, c, pn * pn, pn * c, c * c], 1).astype(np.float64)
    Sg = M @ V; St = V.sum(0)[None, :]; Sb = St - Sg
    def ev_se(S):
        ev = S[:, 0] / np.maximum(S[:, 1], 1e-12)
        var = (S[:, 2] - 2 * ev * S[:, 3] + ev ** 2 * S[:, 4]) / np.maximum(S[:, 1], 1e-12) ** 2
        return ev, np.sqrt(np.maximum(var, 1e-18))
    eg, sg = ev_se(Sg); eb, sb = ev_se(Sb); ng = M.sum(1); nb = M.shape[1] - ng
    t = (eg - eb) / np.sqrt(sg ** 2 + sb ** 2)
    return eg, eb, t, ng, nb, sg
def maxstat(T, R, nperm=1000, seed=7, minfrac=0.08):
    rng = np.random.default_rng(seed); N = len(T)
    pn = T.pn.values; c = T.c.values
    eg, eb, t0, ng, nb, _ = stats(masks(T, R), pn, c)
    valid = (ng >= minfrac * N) & (nb >= minfrac * N)
    days = T.dia.values; groups = [np.flatnonzero(days == d) for d in np.unique(days)]
    mx = np.zeros(nperm); X = T.copy()
    cols = sorted({r[1] for r in R})
    A = {k: T[k].values for k in cols}
    for b in range(nperm):
        idx = np.arange(N)
        for g in groups: idx[g] = rng.permutation(g)
        Xp = pd.DataFrame({k: A[k][idx] for k in cols}); Xp['pn'] = pn; Xp['c'] = c
        _, _, t, ngp, nbp, _ = stats(masks(Xp, R), pn, c)
        vp = (ngp >= minfrac * N) & (nbp >= minfrac * N)
        mx[b] = np.max(np.where(vp, t, -np.inf))
    p_fw = np.array([(1 + (mx >= t0[i]).sum()) / (nperm + 1) for i in range(len(R))])
    return dict(eg=eg, eb=eb, t=t0, ng=ng, nb=nb, valid=valid, p_fw=p_fw, mx=mx)
