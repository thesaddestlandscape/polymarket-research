"""Utilidades comunes del barrido de seleccion adversa de B (22-Oct). EV siempre ponderado por EUR (sum pnl / sum coste)."""
import numpy as np, pandas as pd
def ev(p, c): 
    c = np.sum(c); return np.sum(p) / c if c > 0 else np.nan
def day_boot(df, pcol='p', ccol='c', dcol='dia', n=4000, seed=1):
    """EV agregado y IC90 bootstrap por DIA (bloques), mas EV sin los 2 mejores dias (por pnl) y dias+."""
    g = df.groupby(dcol)[[pcol, ccol]].sum(); a, b = g[pcol].values, g[ccol].values
    if len(g) < 2 or b.sum() <= 0: return dict(ev=ev(df[pcol], df[ccol]), lo=np.nan, hi=np.nan, ev_sin2=np.nan, dias=len(g), dpos=int((a > 0).sum()), n=len(df), eur=float(b.sum()))
    r = np.random.default_rng(seed); i = r.integers(0, len(g), (n, len(g))); e = a[i].sum(1) / np.maximum(b[i].sum(1), 1e-9)
    o = np.argsort(-a)[2:]; evs = a[o].sum() / b[o].sum() if len(o) and b[o].sum() > 0 else np.nan
    return dict(ev=a.sum() / b.sum(), lo=np.quantile(e, .05), hi=np.quantile(e, .95), ev_sin2=evs, dias=len(g), dpos=int((a > 0).sum()), n=len(df), eur=float(b.sum()))
def fmt(d): return f"EV {d['ev']:+.3f} IC90d({d['lo']:+.3f},{d['hi']:+.3f}) sin2mejoresdias {d['ev_sin2']:+.3f} dias+ {d['dpos']}/{d['dias']} n={d['n']} €={d['eur']:.0f}"
