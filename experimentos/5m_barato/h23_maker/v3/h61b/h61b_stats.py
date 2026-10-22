"""h61b_stats.py -- estadistica comun (vigia, capacidad). EV ponderado por EUR = sum(pnl)/sum(coste); IC90 por DIAS (bootstrap de dias, 3000, semilla 7) solo con >= 5 dias; sin 2 mejores dias.
'missing' != 0: posiciones sin desenlace oficial se excluyen y se cuentan aparte."""
import csv, glob, gzip, os
import numpy as np

DL = "/root/polymarket-research-datalogs/h61b/"
MIN_DIAS_IC = 5


def leer_dia(f):
    with gzip.open(f, "rt") as fh:
        return list(csv.DictReader(fh))


def num(x, default=None):
    try:
        return float(x)
    except (TypeError, ValueError):
        return default


def posiciones(rows, var, brazo, cola="base", lp=79, lc=60, mult=1, modo="primer"):
    """Una fila por cierre con relleno (lleno>0). Devuelve dict cierre -> (dia, pnl|None, coste, lleno, gana|None). pnl=None si falta el desenlace oficial."""
    out = {}
    for r in rows:
        if r["var"] != var or r["brazo"] != brazo or r["cola"] != cola or int(r["lp"]) != lp or int(r["lc"]) != lc or int(r["mult"]) != mult or r["modo"] != modo:
            continue
        lleno = num(r["lleno"], 0.0)
        if lleno <= 0:
            continue
        g = None if r["gana"] == "" else int(r["gana"])
        coste = num(r["coste"]); reb = num(r["rebate"], 0.0)
        out[(r["dia"], int(r["cierre"]))] = (r["dia"], None if g is None else lleno * g - coste + reb, coste, lleno, g)
    return out


def ev_dias(pos):
    """pos: iterable de (dia, pnl, coste). Devuelve dict con n, dias, EV pond, IC90 dias, sin2mejores, etc. Solo posiciones con pnl conocido."""
    p = [(d, x, c) for d, x, c in pos if x is not None]
    if not p:
        return dict(n=0, dias=0)
    dias = {}
    for d, x, c in p:
        a = dias.setdefault(d, [0.0, 0.0]); a[0] += x; a[1] += c
    D = np.array([v for _, v in sorted(dias.items())])
    ev = D[:, 0].sum() / D[:, 1].sum()
    lo = hi = float("nan")
    if len(D) >= MIN_DIAS_IC:
        rng = np.random.default_rng(7)
        b = [(lambda k: k[:, 0].sum() / k[:, 1].sum())(D[rng.integers(0, len(D), len(D))]) for _ in range(3000)]
        lo, hi = float(np.percentile(b, 5)), float(np.percentile(b, 95))
    o = np.argsort(-D[:, 0])[2:]
    s2 = float(D[o, 0].sum() / D[o, 1].sum()) if len(o) and D[o, 1].sum() > 0 else float("nan")
    return dict(n=len(p), dias=len(D), dias_pos=int((D[:, 0] > 0).sum()), pnl=float(D[:, 0].sum()), coste=float(D[:, 1].sum()), ev=float(ev), ic90_lo=lo, ic90_hi=hi, sin2=s2, n_dias_sin2=len(o))


def dif_ev_dias(posC, posV):
    """EV_C - EV_v3 por dias (bootstrap de dias sobre los dias en que cualquiera tiene posicion). posC/posV: dict clave->(dia,pnl,coste,..). Solo posiciones con desenlace."""
    dias = {}
    for k, (d, x, c, *_r) in posC.items():
        if x is not None:
            a = dias.setdefault(d, [0.0, 0.0, 0.0, 0.0]); a[0] += x; a[1] += c
    for k, (d, x, c, *_r) in posV.items():
        if x is not None:
            a = dias.setdefault(d, [0.0, 0.0, 0.0, 0.0]); a[2] += x; a[3] += c
    if not dias:
        return dict(dias=0)
    D = np.array([v for _, v in sorted(dias.items())])
    def f(k):
        c = k[:, 0].sum() / k[:, 1].sum() if k[:, 1].sum() > 0 else float("nan"); v = k[:, 2].sum() / k[:, 3].sum() if k[:, 3].sum() > 0 else float("nan")
        return c - v
    pt = f(D); lo = hi = float("nan")
    if len(D) >= MIN_DIAS_IC:
        rng = np.random.default_rng(7)
        b = np.array([f(D[rng.integers(0, len(D), len(D))]) for _ in range(3000)]); b = b[~np.isnan(b)]
        if len(b): lo, hi = float(np.percentile(b, 5)), float(np.percentile(b, 95))
    return dict(dias=len(D), dev=float(pt), ic90_lo=lo, ic90_hi=hi, dpnl_total=float(D[:, 0].sum() - D[:, 2].sum()))


def dias_con_datos(coin="BTC", desde="2026-10-22", hasta=None, base=DL, prefijo="rows"):
    out = []
    for f in sorted(glob.glob(base + f"{prefijo}_{coin}_20*.csv.gz")):
        d = os.path.basename(f)[len(f"{prefijo}_{coin}_"):-len(".csv.gz")]
        if d >= desde and (hasta is None or d <= hasta):
            out.append((d, f))
    return out
