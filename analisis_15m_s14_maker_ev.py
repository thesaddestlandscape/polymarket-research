#!/usr/bin/env python3
"""analisis_15m_s14_maker_ev.py -- MISIÓN DEFINITIVA 15m §14 (07-Oct): MAKER EV(state).
§10: cada relleno maker pierde ~6 c en 5 s (selección adversa) -> el dinero está en saber CUÁNDO cotizar.
Unidad: las órdenes virtuales de §10 (puja de 5 acciones al final de la cola del mejor bid cada 5 s, vida 60 s, relleno
pesimista). Objetivo = EV por ORDEN colocada = PnL a resolución + rebate si se llena, 0 si no (dinero, §26).
Estado en la colocación (solo información disponible entonces; Binance por hora de RECEPCIÓN):
  P, spread, imb N1, Q0, t al cierre | edad del precio del bid, cambios del libro 5 s | operaciones 5 s, volumen vendedor 5 s
  | momentum del mid 5/30 s | Binance 1/5/30 s con el SIGNO del token (+ = a favor de este lado) y |Binance 30 s|.
Modelos (§33, entrenados SOLO en DISC): cotizar siempre | Ridge | HistGradientBoosting. Política = cotizar solo si la
predicción supera el umbral del top 20 % de DISC. Medido en VALID y FINAL: EV por orden, P(fill), IC90 por cierres,
por moneda y sin BTC. Solo lectura. Uso: (ulimit -v 4500000; nice -n 10 python3 analisis_15m_s14_maker_ev.py)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from m15_ms_cache import cargar  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from analisis_15m_A_quote_age import periodo, MON  # noqa: E402
from analisis_15m_s10_cola import virtuales  # noqa: E402

FEATS = ["P", "spread", "imb", "Q0", "t_cierre", "edad_bid", "camb5", "ntr5", "venta5", "mom5", "mom30",
         "bn1", "bn5", "bn30", "bnabs30"]


def binance(C):
    x = C["x"]
    out = {}
    for si, act in enumerate(MON):
        m = x["s"] == si
        T, P = x["tr"][m], x["p"][m]
        o = np.argsort(T, kind="stable")
        out[act] = (T[o], P[o])
    return out


def ret_en(T, P, t, w):
    k1 = np.searchsorted(T, t, side="right") - 1
    k0 = np.searchsorted(T, t - w, side="right") - 1
    if k1 < 0 or k0 < 0:
        return np.nan
    return (P[k1] / P[k0] - 1) * 1e4


def main():
    C = cargar()
    q, tt = C["q"], C["t"]
    toks = C["tokens"]
    des = desenlaces({k[2] for k in toks})
    BN = binance(C)
    bq = np.searchsorted(q["tok"], np.arange(len(toks) + 1))
    bt = np.searchsorted(tt["tok"], np.arange(len(toks) + 1))
    filas = []
    for i, (tk, act, mid_, fin, lado) in enumerate(toks):
        if mid_ not in des or act not in BN:
            continue
        a, b = bq[i], bq[i + 1]
        if b - a < 50:
            continue
        te = q["te"][a:b]
        bb, ba = q["bb"][a:b].astype(np.float64), q["ba"][a:b].astype(np.float64)
        bs, as_ = q["bs"][a:b].astype(np.float64), q["as_"][a:b].astype(np.float64)
        ta, tb = bt[i], bt[i + 1]
        T_te, T_p = tt["te"][ta:tb], tt["p"][ta:tb].astype(np.float64)
        T_side, T_sz = tt["side"][ta:tb], tt["sz"][ta:tb].astype(np.float64)
        gana = 1.0 if des[mid_] == lado else 0.0
        sg = 1.0 if lado in ("YES", "Up") else -1.0
        bbf = np.nan_to_num(bb, nan=-1)
        cambio_bid = np.flatnonzero(np.r_[True, bbf[1:] != bbf[:-1]])
        mid = (bb + ba) / 2
        T_bn, P_bn = BN[act]
        for f in virtuales(te, bb, ba, bs, as_, T_te, T_p, T_side, T_sz, (fin - 900) * 1000, fin * 1000, gana):
            ts = f["ts"]
            k = np.searchsorted(te, ts, side="right") - 1
            kc = cambio_bid[np.searchsorted(cambio_bid, k, side="right") - 1]
            j0, j1 = np.searchsorted(T_te, ts - 5000, side="right"), np.searchsorted(T_te, ts, side="right")
            k5, k30 = np.searchsorted(te, ts - 5000, side="right") - 1, np.searchsorted(te, ts - 30_000, side="right") - 1
            f.update(act=act, mkt=mid_, fin=fin, lado=lado,
                     edad_bid=(ts - te[kc]) / 1000, camb5=k - k5, ntr5=j1 - j0,
                     venta5=float(T_sz[j0:j1][T_side[j0:j1] == 0].sum()),
                     mom5=mid[k] - mid[k5] if k5 >= 0 else np.nan, mom30=mid[k] - mid[k30] if k30 >= 0 else np.nan,
                     bn1=sg * ret_en(T_bn, P_bn, ts, 1000), bn5=sg * ret_en(T_bn, P_bn, ts, 5000),
                     bn30=sg * ret_en(T_bn, P_bn, ts, 30_000), bnabs30=abs(ret_en(T_bn, P_bn, ts, 30_000)))
            filas.append(f)
    R = pd.DataFrame(filas)
    R["per"] = periodo(R["ts"].values)
    R["y"] = R["res_pes"].fillna(0.0)
    R.to_parquet("/root/polymarket-research-datalogs/m15_ms_cache/s14_maker_ev.parquet")
    evaluar(R)


def evaluar(R):
    from sklearn.ensemble import HistGradientBoostingRegressor
    from sklearn.linear_model import Ridge
    rng = np.random.default_rng(14)
    X = R[FEATS].astype(float)
    D = (R.per == "DISC").values
    med = X[D].median()
    Xf = X.fillna(med)
    mods = {"ridge": Ridge(alpha=1.0).fit((Xf[D] - Xf[D].mean()) / Xf[D].std(), R.y[D]),
            "gbm": HistGradientBoostingRegressor(max_iter=200, max_depth=4, learning_rate=0.05, min_samples_leaf=200,
                                                 random_state=14).fit(X[D], R.y[D])}
    pred = {"siempre": np.zeros(len(R)),
            "ridge": mods["ridge"].predict((Xf - Xf[D].mean()) / Xf[D].std()),
            "gbm": mods["gbm"].predict(X)}

    def ic(m):
        g = R[m].groupby("fin")["y"].agg(["sum", "count"])
        S, N = g["sum"].values, g["count"].values
        if len(S) < 5:
            return np.nan, np.nan
        bs = [S[k].sum() / N[k].sum() for k in (rng.integers(0, len(S), len(S)) for _ in range(1000))]
        return np.percentile(bs, 5), np.percentile(bs, 95)
    print(f"órdenes virtuales: {len(R)} | DISC {D.sum()} VALID {(R.per == 'VALID').sum()} FINAL {(R.per == 'FINAL').sum()}")
    print(f"{'modelo':8} {'per':5} | {'n cotiza':>8} {'P(fill)':>7} {'EV/orden c':>10} {'IC90 cierres':>20} | sin BTC | por moneda (c/orden)")
    for nom, p in pred.items():
        thr = -np.inf if nom == "siempre" else np.quantile(p[D], 0.8)
        for per in ("DISC", "VALID", "FINAL"):
            m = (R.per == per).values & (p >= thr)
            lo, hi = ic(m)
            sb = m & (R.act != "BTC").values
            pm = " ".join(f"{a}:{100 * R.y[m & (R.act == a).values].mean():+.2f}" for a in sorted(R.act.unique())
                          if (m & (R.act == a).values).sum() > 200)
            print(f"{nom:8} {per:5} | {m.sum():8} {R.lleno_pes[m].mean():7.3f} {100 * R.y[m].mean():+10.3f} "
                  f"({100 * lo:+.3f},{100 * hi:+.3f}) | {100 * R.y[sb].mean():+.3f} | {pm}")
    imp = pd.Series(np.abs(mods["ridge"].coef_), index=FEATS).sort_values(ascending=False)
    print("\nRidge |coef| (estandarizado): " + " ".join(f"{k}:{v * 100:.3f}" for k, v in imp.head(8).items()))
    print("\nEV/orden (c) por quintil de cada rasgo en DISC -> VALID (¿monótono y estable?):")
    for f in ("bn5", "bn30", "mom5", "edad_bid", "venta5", "t_cierre", "spread", "bnabs30"):
        qs = np.nanquantile(X[f][D], [0.2, 0.4, 0.6, 0.8])
        lin = []
        for per in ("DISC", "VALID", "FINAL"):
            mp = (R.per == per).values
            b = np.digitize(X[f].fillna(med[f]), qs)
            lin.append(per[0] + ":" + "/".join(f"{100 * R.y[mp & (b == k)].mean():+.2f}" for k in range(5)))
        print(f"   {f:9} " + "  ".join(lin))


if __name__ == "__main__":
    if "--solo-evaluar" in sys.argv:
        evaluar(pd.read_parquet("/root/polymarket-research-datalogs/m15_ms_cache/s14_maker_ev.parquet"))
    else:
        main()
