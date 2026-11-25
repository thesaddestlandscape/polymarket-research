"""Utilidades comunes (EV ponderado por EUR, IC por cierre, placebo, sin 2 mejores). Sin I/O."""
import numpy as np, pandas as pd
from scipy import stats
C0, C1 = 3.526360511779785, 4.717426776885986
def ter(f):
    f = np.asarray(f, float)
    return np.where(~np.isfinite(f), 'nan', np.where(f <= C0, 'bajo', np.where(f <= C1, 'medio', 'alto')))
RET = {'todo': ('bajo', 'medio', 'alto', 'nan'), 'G1': ('bajo', 'medio'), 'G2': ('bajo',), 'inv': ('alto',), 'bajo': ('bajo',), 'medio': ('medio',), 'alto': ('alto',), 'nan': ('nan',)}
def ev(pnl, co):
    c = np.sum(co); return float(np.sum(pnl) / c) if c > 0 else np.nan
def t_ic(x, nivel=0.95):
    x = np.asarray(x, float); x = x[np.isfinite(x)]; n = len(x)
    if n < 3: return np.nan, np.nan, np.nan
    se = x.std(ddof=1) / np.sqrt(n); t = x.mean() / se if se > 0 else np.nan
    return x.mean() - stats.t.ppf(nivel, n - 1) * se, stats.t.sf(t, n - 1), x.mean()
def boot_cluster(df, regla, B=1000, seed=20261115, ref='todo'):
    """Bootstrap por cluster (cl): devuelve (IC90 de EV_regla, IC90 de EV_regla-EV_todo)."""
    rng = np.random.default_rng(seed); ret = df.ter.isin(RET[regla]).values
    P = pd.DataFrame({'pr': df.pnl.values * ret, 'cr': df.coste.values * ret, 'pa': df.pnl.values, 'ca': df.coste.values}).groupby(df.cl.values).sum().values
    n = len(P); e = np.empty(B); d = np.empty(B)
    for b in range(B):
        s = P[rng.integers(0, n, n)].sum(0); e[b] = s[0] / s[1] if s[1] > 0 else np.nan; d[b] = e[b] - s[2] / s[3]
    return np.nanpercentile(e, [5, 95]), np.nanpercentile(d, [5, 95])
def sin_mejores(df, regla, col, k=2):
    """EV de la regla quitando los k mejores grupos (col) por pnl de la regla."""
    r = df[df.ter.isin(RET[regla])]
    if len(r) == 0: return np.nan
    g = r.groupby(col).agg(p=('pnl', 'sum'), c=('coste', 'sum')).sort_values('p')
    g = g.iloc[:-k] if len(g) > k else g.iloc[:0]
    return float(g.p.sum() / g.c.sum()) if g.c.sum() > 0 else np.nan
def placebo_multi(df, reglas, strata, B=1000, seed=20261115):
    """Permuta las etiquetas de tercil DENTRO de cada estrato (vectorizado: lexsort por (estrato, clave aleatoria)). Devuelve {regla: (DeltaEV obs, p unilateral, media placebo)}."""
    rng = np.random.default_rng(seed); pn = df.pnl.values; co = df.coste.values
    cod = {'bajo': 0, 'medio': 1, 'alto': 2, 'nan': 3}; lab = np.array([cod[x] for x in df.ter.values], np.int8)
    sid = pd.factorize(pd.MultiIndex.from_arrays([df[c].values for c in strata]))[0]; ord0 = np.argsort(sid, kind='stable'); tot = pn.sum() / co.sum()
    masks = {r: np.isin(np.arange(4), [cod[x] for x in RET[r]]) for r in reglas}
    def delta(L, r):
        m = masks[r][L]; c = co[m].sum(); return (pn[m].sum() / c - tot) if c > 0 else np.nan
    obs = {r: delta(lab, r) for r in reglas}; dist = {r: np.empty(B) for r in reglas}
    for b in range(B):
        ordr = np.lexsort((rng.random(len(lab)), sid)); L = np.empty_like(lab); L[ord0] = lab[ordr]
        for r in reglas: dist[r][b] = delta(L, r)
    return {r: (obs[r], float(np.nanmean(dist[r] >= obs[r] - 1e-12)), float(np.nanmean(dist[r]))) for r in reglas}
def placebo(df, regla, strata, B=2000, seed=20261115):
    return placebo_multi(df, [regla], strata, B, seed)[regla]
def resumen(df, nombre, B=1000):
    """df con columnas ter, pnl, coste, cl, dia. Devuelve lista de lineas de texto y dict de cifras."""
    out = {}; L = [f'## {nombre}  (n={len(df)} unidades, {df.cl.nunique()} cierres, {df.dia.nunique()} dias)']
    tot = ev(df.pnl, df.coste); out['todo'] = tot
    for r in ('bajo', 'medio', 'alto', 'nan'):
        m = df.ter.isin(RET[r]); out[r] = ev(df.pnl[m], df.coste[m]); out['n_' + r] = int(m.sum()); out['co_' + r] = float(df.coste[m].sum())
    L.append(f"EV pond. todo {tot:+.3f} | bajo {out['bajo']:+.3f} (n={out['n_bajo']}) | medio {out['medio']:+.3f} (n={out['n_medio']}) | alto {out['alto']:+.3f} (n={out['n_alto']}) | nan {out['nan']:+.3f} (n={out['n_nan']})")
    for r in ('G1', 'G2', 'inv'):
        m = df.ter.isin(RET[r]); e = ev(df.pnl[m], df.coste[m]); (lo, hi), (dlo, dhi) = boot_cluster(df, r, B)
        out[r] = dict(ev=e, n=int(m.sum()), frac_coste=float(df.coste[m].sum() / df.coste.sum()), ic_cl=(float(lo), float(hi)), dev=e - tot, dic=(float(dlo), float(dhi)), sin2cl=sin_mejores(df, r, 'cl'), sin2dia=sin_mejores(df, r, 'dia'))
        L.append(f"{r}: EV {e:+.3f} (n={m.sum()}, {out[r]['frac_coste']*100:.0f}% del coste) IC90 cierre ({lo:+.3f},{hi:+.3f}) | DeltaEV vs todo {e-tot:+.3f} IC90 ({dlo:+.3f},{dhi:+.3f}) | sin 2 mejores cierres {out[r]['sin2cl']:+.3f}")
    return L, out
