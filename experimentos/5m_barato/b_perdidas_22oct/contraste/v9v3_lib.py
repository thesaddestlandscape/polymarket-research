#!/usr/bin/env python3
"""v9v3_lib.py -- funciones del contraste V9/V3 (estadistica, placebo, reglas de veto). Sin E/S. Probadas en test_v9v3_lib.py."""
import numpy as np, pandas as pd
REPS_B, REPS_P = 2000, 2000
# ---------------------------------------------------------------- estadistica comun
def agg(df, key, ycols=('pv', 'cv', 'pr', 'cr')):
    return df.groupby(key)[list(ycols)].sum().values
def dnet(a):   # a: (..., G, 4) sumas -> (delta, net)
    pv, cv, pr, cr = a[..., 0].sum(-1), a[..., 1].sum(-1), a[..., 2].sum(-1), a[..., 3].sum(-1)
    with np.errstate(divide='ignore', invalid='ignore'):
        return (pr / cr) - (pv / cv), -pv
def boot(a, rng, reps=REPS_B):
    G = len(a); ds, ns = [], []
    for s in range(0, reps, 200):
        n_ = min(200, reps - s); idx = rng.integers(0, G, (n_, G)); d, n = dnet(a[idx]); ds.append(d); ns.append(n)
    d, n = np.concatenate(ds), np.concatenate(ns)
    return (float(np.nanquantile(d, .05)), float(np.nanquantile(d, .95)), float(np.nanquantile(n, .05)), float(np.nanquantile(n, .95)))
def prep(df):
    """df con columnas dia, cierre, pnl, cost, veto(bool). Anade pv/cv/pr/cr."""
    v = df['veto'].values.astype(bool)
    df = df.assign(pv=np.where(v, df.pnl, 0.0), cv=np.where(v, df.cost, 0.0), pr=np.where(v, 0.0, df.pnl), cr=np.where(v, 0.0, df.cost))
    return df
def placebo(pnl, g, nv, reps, rng):
    """pnl, g (codigos de grupo), nv (n vetados por grupo, constante en el grupo). Devuelve neto placebo por replica. Solo grupos con nv>0."""
    m = nv > 0
    pnl, g, nv = pnl[m], g[m], nv[m]
    if len(pnl) == 0: return np.zeros(reps)
    o = np.argsort(g, kind='stable'); pnl, g, nv = pnl[o], g[o], nv[o]
    starts = np.r_[0, np.flatnonzero(g[1:] != g[:-1]) + 1]; gid = np.repeat(np.arange(len(starts)), np.diff(np.r_[starts, len(g)])); st_row = starts[gid]
    base = np.arange(len(g)) - st_row; out = np.empty(reps)
    for r in range(reps):
        k = rng.random(len(g)); o2 = np.lexsort((k, gid))              # permuta dentro de cada grupo
        veto_sorted = base < nv[o2]                                   # el rango por posicion en el grupo permutado
        out[r] = -pnl[o2][veto_sorted].sum()
    return out
def summarize(name, df, strict_g, rng, reps=REPS_P, per_day=True, extra=None):
    """df: dia, cierre, pnl, cost, veto, [strict_g]: columna de grupos del placebo estricto."""
    d = prep(df); tot = dict(n=int(len(d)), nv=int(d.veto.sum()), cost=float(d.cost.sum()), cost_v=float(d.cv.sum()), pnl_v=float(d.pv.sum()), pnl_r=float(d.pr.sum()),
                             ev_all=float(d.pnl.sum() / d.cost.sum()) if d.cost.sum() > 0 else np.nan)
    tot['ev_v'] = tot['pnl_v'] / tot['cost_v'] if tot['cost_v'] > 0 else np.nan
    tot['ev_r'] = tot['pnl_r'] / d.cr.sum() if d.cr.sum() > 0 else np.nan
    tot['delta'] = tot['ev_r'] - tot['ev_v'] if tot['cost_v'] > 0 else np.nan
    tot['net'] = -tot['pnl_v']; tot['share_veto'] = tot['nv'] / max(tot['n'], 1); tot['share_cost_kept'] = float(d.cr.sum() / max(d.cost.sum(), 1e-12))
    ad = agg(d, 'dia'); days = sorted(d.dia.unique())
    # por dia
    pd_ = d.groupby('dia')[['pv', 'cv', 'pr', 'cr']].sum()
    with np.errstate(divide='ignore', invalid='ignore'):
        day_delta = ((pd_.pr / pd_.cr) - (pd_.pv / pd_.cv)).replace([np.inf, -np.inf], np.nan)
    day_net = -pd_.pv
    tot['por_dia'] = {k: dict(delta=(None if np.isnan(day_delta[k]) else round(float(day_delta[k]), 3)), net=round(float(day_net[k]), 2), nv=int(d[(d.dia == k)].veto.sum()), n=int((d.dia == k).sum())) for k in pd_.index}
    tot['dias_delta_pos'] = int((day_delta > 0).sum()); tot['dias'] = len(days)
    best2 = day_net.sort_values(ascending=False).index[:2]; tot['net_sin2'] = float(day_net.drop(best2).sum())
    lo_d, hi_d, nlo_d, nhi_d = boot(ad, rng); tot['ic90_dia_delta'] = (lo_d, hi_d); tot['ic90_dia_net'] = (nlo_d, nhi_d)
    ac = agg(d, 'cierre'); lo_c, hi_c, nlo_c, nhi_c = boot(ac, rng); tot['ic90_cierre_delta'] = (lo_c, hi_c); tot['ic90_cierre_net'] = (nlo_c, nhi_c); tot['n_cierres'] = int(len(ac))
    # <= 19 Oct
    dm = d[d.dia <= '2026-10-19']
    if len(dm) and dm.veto.any() and (~dm.veto).any():
        tot['delta_le19'] = float(dm.pr.sum() / dm.cr.sum() - dm.pv.sum() / dm.cv.sum()); tot['net_le19'] = float(-dm.pv.sum()); tot['n_le19'] = int(len(dm)); tot['nv_le19'] = int(dm.veto.sum())
    else: tot['delta_le19'] = None; tot['net_le19'] = None; tot['n_le19'] = int(len(dm)); tot['nv_le19'] = int(dm.veto.sum()) if len(dm) else 0
    # placebo
    if tot['nv'] > 0 and reps:
        gcode = pd.factorize(d[strict_g] if isinstance(strict_g, str) else pd.Series(strict_g, index=d.index))[0] if strict_g is not None else None
        nvg = d.groupby(gcode if gcode is not None else d.dia).veto.transform('sum').values
        pl = placebo(d.pnl.values, gcode, nvg, reps, rng); tot['placebo_estricto'] = dict(media=float(pl.mean()), p95=float(np.quantile(pl, .95)), p=float((np.sum(pl >= tot['net'] - 1e-9) + 1) / (reps + 1)), neto_sobre_placebo=float(tot['net'] - pl.mean()))
        dcode = pd.factorize(d.dia)[0]; nvd = d.groupby(dcode).veto.transform('sum').values
        pl2 = placebo(d.pnl.values, dcode, nvd, reps, rng); tot['placebo_simple'] = dict(media=float(pl2.mean()), p=float((np.sum(pl2 >= tot['net'] - 1e-9) + 1) / (reps + 1)), neto_sobre_placebo=float(tot['net'] - pl2.mean()))
    if extra: tot.update(extra)
    return tot

def veto_steps(grp, k, dk):
    """V9 en pasos de 5 s (cinta/simv2): veta el relleno en paso k >= k1+dk, k1 = paso del 1.er relleno del grupo (cierre,lado). El 1.o y los del mismo paso k1 NO se vetan."""
    g = pd.Series(np.asarray(k), index=pd.RangeIndex(len(k))).groupby(np.asarray(grp)).transform('min').values
    return np.asarray(k) >= g + dk
def veto_time(grp, t, L):
    """V9 en tiempo (s): veta el relleno con t - t1 >= L (L>0), t1 = menor t del grupo. El 1.o (gap 0) nunca se veta; si L<=0 solo se veta gap>0."""
    t = np.asarray(t, dtype=float); t1 = pd.Series(t).groupby(np.asarray(grp)).transform('min').values; gap = t - t1
    return (gap >= L) & (gap > 0)
