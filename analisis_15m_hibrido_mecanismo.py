#!/usr/bin/env python3
"""analisis_15m_hibrido_mecanismo.py -- 13-Oct, H-C (Javi: "el híbrido tiene que funcionar; no copiar wallets, el
mecanismo"). En TODO el mercado 15m: cada orden TOMADORA de compra de una wallet que llega <= 300 s después de un relleno
MAKER de compra de esa MISMA wallet en el MISMO mercado. ¿En qué estado esa continuación tiene EV>0 con desenlace oficial?
CUBRE = compra el lado contrario al de su relleno maker (coste del par = p_maker + p_tomador + comisión/acción);
REFUERZA = compra el mismo lado. Celdas FIJADAS antes de mirar: tipo × dt (0-10, 10-30, 30-120, 120-300 s) × tiempo al
cierre (T >600, 300-600, 120-300, <120 s) × (CUBRE: coste del par <0,95 / 0,95-1,00 / >=1,00; REFUERZA: precio pagado
frente al del relleno maker: más barato / igual ±1c / más caro).
EXTRACCIÓN 05-07 Oct elige las celdas con n>=100 órdenes y PnL/€ > 0; VALIDACIÓN 08-12 Oct las mide. IC90 por bootstrap
de MERCADOS (no de órdenes); además por días. Unidad: orden tomadora (fila con taker = contrato del exchange).
SOLO LECTURA. Uso: (ulimit -v 4000000; nice -n 19 python3 analisis_15m_hibrido_mecanismo.py)
"""
import collections
import gzip
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_15m_hibrido_cuando import mapa_tokens, VOL, EXCH  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

EXT = ["2026-10-05", "2026-10-06", "2026-10-07"]
VAL = ["2026-10-08", "2026-10-09", "2026-10-10", "2026-10-11", "2026-10-12"]
INF = Path(__file__).resolve().parent / "informes" / "m15_hibrido_mecanismo_13oct.txt"
DT = [(0, 10), (10, 30), (30, 120), (120, 300)]
TT = [(600, 10**6, "T>600"), (300, 600, "T300-600"), (120, 300, "T120-300"), (-10**6, 120, "T<120")]


def cargar(dias, tok):
    out = []
    for d in dias:
        with gzip.open(VOL / "m15_onchain" / f"m15_onchain_{d}.csv.gz", "rt") as fh:
            x = pd.read_csv(fh, dtype={"token_id": str, "maker": str, "taker": str},
                            usecols=["tipo", "ts_est", "log_index", "maker", "taker", "side", "token_id", "maker_amt",
                                     "taker_amt", "fee"])
        x = x[(x.tipo == "F") & (x.side == 0) & x.token_id.isin(tok.keys())].copy()
        x["dia"] = d
        out.append(x)
    X = pd.concat(out, ignore_index=True)
    info = X.token_id.map(tok)
    X["mkt"], X["fin"], X["lado"] = info.str[1], info.str[2].astype(float), info.str[3]
    X["acc"], X["usdc"] = X.taker_amt.astype(float), X.maker_amt.astype(float)
    X = X[X.acc > 0]
    X["p"] = X.usdc / X.acc
    X["rol"] = np.where(X.taker.str.lower() == EXCH, "T", "M")
    X["w"] = X.maker.str.lower()
    return X


def eventos(X, des):
    X = X.sort_values(["w", "mkt", "ts_est", "log_index"], kind="stable")
    ev = []
    for (w, mkt), g in X.groupby(["w", "mkt"], sort=False):
        if des.get(mkt) is None or not (g.rol == "M").any() or not (g.rol == "T").any():
            continue
        ult = {}                                   # lado -> (ts, precio) del último relleno MAKER de compra
        for r in g.itertuples(index=False):
            if r.rol == "M":
                ult[r.lado] = (r.ts_est, r.p)
                continue
            mejor = None
            for lado_m, (ts_m, p_m) in ult.items():
                dt = r.ts_est - ts_m
                if 0 <= dt <= 300 and (mejor is None or dt < mejor[0]):
                    mejor = (dt, lado_m, p_m)
            if mejor is None:
                continue
            dt, lado_m, p_m = mejor
            tipo = "REFUERZA" if lado_m == r.lado else "CUBRE"
            fee = float(r.fee or 0)
            gana = 1.0 if des[mkt] == r.lado else 0.0
            pnl = r.acc * gana - r.usdc - fee
            if tipo == "CUBRE":
                c = p_m + r.p + fee / r.acc
                sub = "par<0,95" if c < 0.95 else ("par0,95-1" if c < 1.0 else "par>=1")
            else:
                d = r.p - p_m
                sub = "más barato" if d < -0.01 else ("igual" if d <= 0.01 else "más caro")
            T = r.fin - r.ts_est
            ev.append((tipo, next(f"{a}-{b}s" for a, b in DT if a <= dt < b or (b == 300 and dt == 300)),
                       next(n for a, b, n in TT if a <= T < b), sub, mkt, r.dia, pnl, r.usdc))
    return pd.DataFrame(ev, columns=["tipo", "dt", "TT", "sub", "mkt", "dia", "pnl", "usdc"])


def ic_mercados(df, B=1000, seed=3):
    g = df.groupby("mkt")[["pnl", "usdc"]].sum()
    if len(g) < 5:
        return float("nan"), float("nan")
    r = np.random.default_rng(seed)
    idx = r.integers(0, len(g), (B, len(g)))
    p, u = g.pnl.values, g.usdc.values
    s = p[idx].sum(1) / u[idx].sum(1)
    return float(np.quantile(s, 0.05)), float(np.quantile(s, 0.95))


def main():
    lines = []

    def L(s=""):
        print(s, flush=True)
        lines.append(s)
    tok = mapa_tokens()
    E = cargar(EXT, tok)
    V = cargar(VAL, tok)
    des = desenlaces(set(E.mkt) | set(V.mkt))
    e, v = eventos(E, des), eventos(V, des)
    L(f"H-C híbrido en TODO el 15m: órdenes tomadoras <=300 s tras un relleno maker propio (mismo mercado). "
      f"EXT {len(e)} órdenes / {e.mkt.nunique()} merc. | VAL {len(v)} / {v.mkt.nunique()}")
    for nom, df in (("EXTRACCIÓN 05-07", e), ("VALIDACIÓN 08-12", v)):
        L(f"\n== {nom}: total PnL/€ {df.pnl.sum() / df.usdc.sum():+.4f}")
        for t, g in df.groupby("tipo"):
            lo, hi = ic_mercados(g)
            L(f"   {t:8s} n={len(g):6d} vol {g.usdc.sum():9.0f} $ PnL/€ {g.pnl.sum() / g.usdc.sum():+.4f} IC90 merc. ({lo:+.4f},{hi:+.4f})")
    claves = ["tipo", "dt", "TT", "sub"]
    ce = e.groupby(claves).agg(n=("pnl", "size"), pnl=("pnl", "sum"), usdc=("usdc", "sum"))
    ce["ev"] = ce.pnl / ce.usdc
    elegidas = ce[(ce.n >= 100) & (ce.ev > 0)].sort_values("ev", ascending=False)
    L(f"\nCeldas EXT con n>=100 y PnL/€>0: {len(elegidas)} de {len(ce)} (con n>=100: {(ce.n >= 100).sum()})")
    L(f"{'celda':58s} {'EXT n':>6s} {'EXT EV':>8s} | {'VAL n':>6s} {'VAL EV':>8s} {'IC90 merc.':>20s} días+")
    ok = 0
    for k, r in elegidas.iterrows():
        g = v[(v.tipo == k[0]) & (v.dt == k[1]) & (v["TT"] == k[2]) & (v["sub"] == k[3])]
        if len(g) == 0:
            L(f"{' '.join(k):58s} {int(r.n):6d} {r.ev:+8.4f} | sin datos")
            continue
        lo, hi = ic_mercados(g)
        dias = g.groupby("dia").apply(lambda x: x.pnl.sum() / x.usdc.sum())
        evv = g.pnl.sum() / g.usdc.sum()
        ok += (evv > 0 and lo > 0)
        L(f"{' '.join(k):58s} {int(r.n):6d} {r.ev:+8.4f} | {len(g):6d} {evv:+8.4f} ({lo:+.4f},{hi:+.4f}) {(dias > 0).sum()}/{len(dias)}")
    L(f"\nCeldas que REPITEN en validación (EV>0 e IC90 por mercados >0): {ok} de {len(elegidas)} "
      f"(con ~{len(elegidas)} miradas, por azar se esperan ~{0.05 * len(elegidas):.1f})")
    INF.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"-> {INF}")


if __name__ == "__main__":
    main()
