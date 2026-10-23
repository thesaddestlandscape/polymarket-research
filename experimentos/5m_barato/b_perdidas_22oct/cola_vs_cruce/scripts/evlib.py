"""evlib -- EV ponderado por EUR, IC90 bootstrap por dia y por cierre, sin 2 mejores dias. Semilla fija."""
import numpy as np, pandas as pd
def ev(df, pnl='pnl', cost='coste'):
    c = df[cost].sum(); return np.nan if c <= 0 else df[pnl].sum() / c
def boot(df, grp, pnl='pnl', cost='coste', B=2000, seed=20261022):
    if len(df) == 0: return (np.nan, np.nan)
    g = df.groupby(grp)[[pnl, cost]].sum().values
    if len(g) < 2: return (np.nan, np.nan)
    rng = np.random.default_rng(seed); i = rng.integers(0, len(g), (B, len(g)))
    s = g[i]; v = s[:, :, 0].sum(1) / np.maximum(s[:, :, 1].sum(1), 1e-12)
    return tuple(np.percentile(v, [5, 95]))
def sin2(df, pnl='pnl', cost='coste', dia='dia'):
    g = df.groupby(dia)[[pnl, cost]].sum(); g = g.sort_values(pnl).iloc[:-2] if len(g) > 2 else g.iloc[0:0]
    return np.nan if g[cost].sum() <= 0 else g[pnl].sum() / g[cost].sum()
def fila(df, nombre, pnl='pnl', cost='coste', dia='dia', cierre='cierre'):
    d = df.groupby(dia)[[pnl, cost]].sum(); pd_ = (d[pnl] / d[cost]).round(3).tolist()
    a, b = boot(df, dia, pnl, cost); c, e = boot(df, cierre, pnl, cost)
    return dict(sub=nombre, n=len(df), coste=round(df[cost].sum(), 2), pnl=round(df[pnl].sum(), 2), ev=round(ev(df, pnl, cost), 3),
                ic_dia=f'({a:+.3f},{b:+.3f})', ic_cierre=f'({c:+.3f},{e:+.3f})', sin2=round(sin2(df, pnl, cost, dia), 3),
                hit=round(df['gana'].mean(), 3) if 'gana' in df else None, p_med=round((df.get('p', pd.Series(dtype=float))).mean(), 3) if 'p' in df else None,
                por_dia=pd_)
