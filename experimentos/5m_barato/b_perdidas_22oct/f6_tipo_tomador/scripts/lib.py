import numpy as np, pandas as pd
D = "/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f6_tipo_tomador/datos/"
DISC = ["2026-10-%02d" % d for d in range(9, 15)]; HOLD = ["2026-10-%02d" % d for d in range(15, 21)]
def carga():
    U = pd.read_pickle(D + "units_clases.pkl")
    U["cl"] = pd.cut(U.tk_n, [-1, 19, 199, 1999, 10**9], labels=["C1<=19", "C2 20-199", "C3 200-1999", "C4>=2000"]).astype(str)
    U["nrep"] = (U.tk_n <= 199)
    U["bp"] = np.floor((U.pc.values - 0.10 + 1e-9) / 0.05).clip(0, 3).astype(int)  # tramos .10-.15 .15-.20 .20-.25 .25-.30
    U["per"] = np.where(U.dia.isin(DISC), "DISC", np.where(U.dia.isin(HOLD), "HOLD", "X"))
    U["cid"] = pd.factorize(U.fin)[0]
    return U
def ev(pnl, c): return pnl.sum() / c.sum() if c.sum() > 0 else np.nan
def boot_ev(df, mask=None, B=2000, seed=1, col_cluster="cid"):
    """IC90 de EV (Σpnl/Σc) por bootstrap de cierres. Devuelve (ev, lo, hi, n_clusters)."""
    if mask is not None: df = df[mask]
    g = df.groupby(col_cluster)[["pnl", "c"]].sum().values
    if len(g) < 5: return (np.nan, np.nan, np.nan, len(g))
    rng = np.random.default_rng(seed); n = len(g)
    idx = rng.integers(0, n, (B, n)); s = g[idx].sum(axis=1)
    r = s[:, 0] / s[:, 1]
    return (g[:, 0].sum() / g[:, 1].sum(), np.percentile(r, 5), np.percentile(r, 95), n)
def boot_diff(df, m1, m0, B=2000, seed=1):
    """EV(m1)-EV(m0) con bootstrap de cierres (mismos cierres remuestreados)."""
    a = df[m1].groupby("cid")[["pnl", "c"]].sum(); b = df[m0].groupby("cid")[["pnl", "c"]].sum()
    ids = np.union1d(a.index.values, b.index.values); A = a.reindex(ids).fillna(0).values; Bm = b.reindex(ids).fillna(0).values
    n = len(ids); rng = np.random.default_rng(seed); idx = rng.integers(0, n, (B, n))
    sa = A[idx].sum(axis=1); sb = Bm[idx].sum(axis=1)
    r = sa[:, 0] / sa[:, 1] - sb[:, 0] / sb[:, 1]
    d0 = A[:, 0].sum() / A[:, 1].sum() - Bm[:, 0].sum() / Bm[:, 1].sum()
    return d0, np.percentile(r, 5), np.percentile(r, 95)
def perm_diff(df, flag, strata, B=2000, seed=2):
    """placebo: permuta 'flag' dentro de estratos; estadistico EV(flag)-EV(~flag). Devuelve (obs, p_unilateral, media_nulo, p95)."""
    pnl = df.pnl.values; c = df.c.values; f = flag.values.copy()
    st = pd.factorize(strata)[0]; rng = np.random.default_rng(seed)
    def stat(ff): return pnl[ff].sum() / c[ff].sum() - pnl[~ff].sum() / c[~ff].sum()
    obs = stat(f); o0 = np.argsort(st, kind="stable"); st_s = st[o0]; fs = f[o0]
    nulls = np.empty(B)
    # permutacion dentro de estrato: reordenar fs dentro de cada bloque via lexsort con clave aleatoria
    for b in range(B):
        k = np.lexsort((rng.random(len(fs)), st_s)); ff = np.empty(len(fs), bool); ff[o0] = fs[k]
        nulls[b] = stat(ff)
    return obs, (nulls >= obs).mean(), nulls.mean(), np.percentile(nulls, 95)
