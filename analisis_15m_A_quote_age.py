#!/usr/bin/env python3
"""analisis_15m_A_quote_age.py -- MISIÓN DEFINITIVA 15m, línea A (06-Oct): ¿la toxicidad de un relleno maker depende de
cuánto lleva publicada la cotización, más allá de los confusores? ¿se puede anticipar el repricing?

Datos: caché del registro ms (m15_ms_cache.py; reloj del EXCHANGE para libro y operaciones; resolución real = ms del
exchange, las filas q son CADA cambio de precio o tamaño del mejor nivel). Chainlink RTDS (recepción) y Binance aggTrade
(recepción) solo como estado previo. Desenlace oficial.
Corte temporal FIJADO ANTES DE MIRAR: DISC 05-Oct 16:00 → 06-Oct 02:00 | EMBARGO 02:00 → 03:30 | VALID 03:30 → 09:30 |
FINAL 09:30 → fin (bloqueado: aquí NO se mira; solo lo usa la política de A3 al final).

A1. Cada operación del CLOB es un relleno de un maker: taker SELL -> se consumió el bid (el maker compró a p); taker BUY
    -> se consumió el ask (el maker vendió a p). Estado = última fila q ESTRICTAMENTE anterior a la operación.
    edad_precio = t − última vez que cambió el PRECIO de ese lado del top; edad_tamaño = t − último cambio de su tamaño;
    t desde la última cancelación (baja de tamaño al mismo precio sin operación). Markout del maker por acción:
    s·(mid(t+h) − p), h = 1, 5, 10, 25, 50, 100, 215, 250, 500 ms, 1 s, 5 s, 30 s, y a resolución s·(gana − p)
    (= PnL del maker, que no paga comisión). Tóxico = markout 5 s <= −0,01 (un tick en contra).
    Confusores: spread, profundidad propia y contraria, desequilibrio, microprecio − mid, volatilidad propia (cambios del
    mid en 30 s y movimiento 5 s), intensidad (operaciones en 10 s), flujo firmado 5 s, t desde la última operación,
    tiempo al cierre, nivel de precio, Chainlink (FV − mid) y Binance (retorno 1 s y 200 ms), todo con el signo del maker.
    (Estado del 5m: no está en la caché del 15m; el subyacente entra por Chainlink y Binance.)
    ¿Información incremental de la edad? Modelos con y sin las variables de edad, entrenados en DISC y medidos en VALID
    (R² del markout 5 s y de resolución, log-loss de tóxico), IC por bootstrap de CIERRES.
A2. Rejilla cada 500 ms (reloj del exchange) de cada token: P(el precio del bid/ask cambia en los próximos X ms), X = 1, 5,
    10, 25, 50, 100, 215 ms, por edad del precio y por movimiento previo de Binance; AUC de una señal previa de repricing
    a 215 ms (entrenada en DISC, medida en VALID).
Uso: (ulimit -v 5000000; python3 analisis_15m_A_quote_age.py)    Solo lectura.
"""
import collections
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from m15_ms_cache import cargar  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from analisis_15m_dataset_maestro import cargar_chainlink, refs  # noqa: E402

ms = lambda s: int(datetime.fromisoformat(s).replace(tzinfo=timezone.utc).timestamp() * 1000)
DISC = (ms("2026-10-05T16:00"), ms("2026-10-06T02:00"))
VALID = (ms("2026-10-06T03:30"), ms("2026-10-06T09:30"))
FINAL = (ms("2026-10-06T09:30"), ms("2026-10-07T00:00"))
H = [1, 5, 10, 25, 50, 100, 215, 250, 500, 1000, 5000, 30000]
HZ = [1, 5, 10, 25, 50, 100, 215]
MON = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]


def periodo(t):
    return np.where((t >= DISC[0]) & (t < DISC[1]), "DISC", np.where((t >= VALID[0]) & (t < VALID[1]), "VALID",
                    np.where(t >= FINAL[0], "FINAL", "EMB")))


def preparar_cl():
    cl = cargar_chainlink(["2026-10-05", "2026-10-06"])
    tw = refs(["2026-10-05", "2026-10-06"])
    clv = {a: (np.frombuffer(s.t, dtype=np.int64), np.frombuffer(s.p, dtype=np.float64)) for a, s in cl.items()}
    return clv, tw


def fv_en(clv, tw, act, fin, t):
    """FV del YES (Φ(z), σ de 300 s de ticks) en los instantes t (ms) con datos de recepción <= t."""
    if act not in clv or (fin - 900) not in tw.get(act, {}):
        return np.full(len(t), np.nan)
    ct, cp = clv[act]
    ref = tw[act][fin - 900]
    k = np.searchsorted(ct, t, side="right") - 1
    out = np.full(len(t), np.nan)
    lr = np.diff(np.log(cp))
    cs = np.concatenate([[0.0], np.cumsum(np.where(lr != 0, lr * lr, 0.0))])
    k0 = np.searchsorted(ct, t - 300_000)
    ok = (k >= 0) & (k - k0 >= 20)
    var = (cs[np.clip(k, 0, None)] - cs[np.clip(k0, 0, None)]) / np.maximum(1.0, (ct[np.clip(k, 0, None)] - ct[k0.clip(0, len(ct) - 1)]) / 1000)
    sg = np.sqrt(np.maximum(var, 1e-18))
    T = np.maximum(1.0, fin - t / 1000)
    z = np.log(cp[np.clip(k, 0, None)] / ref) / (sg * np.sqrt(T))
    from math import erf
    out[ok] = 0.5 * (1 + np.vectorize(erf)(z[ok] / math.sqrt(2)))
    return out


def binance_ret(C, s_idx, t, w):
    x = C["x"]
    m = x["s"] == s_idx
    tr, p = x["tr"][m], x["p"][m]
    o = np.argsort(tr, kind="stable")
    tr, p = tr[o], p[o]
    k1 = np.searchsorted(tr, t, side="right") - 1
    k0 = np.searchsorted(tr, t - w, side="right") - 1
    ok = (k1 >= 0) & (k0 >= 0)
    out = np.full(len(t), np.nan)
    out[ok] = (p[k1[ok]] / p[k0[ok]] - 1) * 1e4
    return out


def main():
    C = cargar()
    q, tt = C["q"], C["t"]
    toks = C["tokens"]
    des = desenlaces({x[2] for x in toks})
    clv, tw = preparar_cl()
    sim = {m: i for i, m in enumerate(MON)}
    bq = np.searchsorted(q["tok"], np.arange(len(toks) + 1))
    bt = np.searchsorted(tt["tok"], np.arange(len(toks) + 1))
    filas, rej = [], []
    for i, (tk, act, mid_, fin, lado) in enumerate(toks):
        if mid_ not in des or act not in sim:
            continue
        a, b = bq[i], bq[i + 1]
        if b - a < 50:
            continue
        te = q["te"][a:b]
        bb, ba, bs, as_ = (q[c][a:b].astype(np.float64) for c in ("bb", "ba", "bs", "as_"))
        mid = (bb + ba) / 2
        gana = 1.0 if des[mid_] == lado else 0.0
        sl = 1.0 if lado in ("YES", "Up") else -1.0                 # signo del subyacente para este token
        # edades
        def edad_desde(cambio):
            idx = np.where(cambio, np.arange(len(te)), 0)
            return np.maximum.accumulate(idx)
        bb_f, ba_f = np.nan_to_num(bb, nan=-1), np.nan_to_num(ba, nan=-1)
        cb = np.r_[True, bb_f[1:] != bb_f[:-1]]
        ca = np.r_[True, ba_f[1:] != ba_f[:-1]]
        csb = cb | np.r_[True, bs[1:] != bs[:-1]]
        csa = ca | np.r_[True, as_[1:] != as_[:-1]]
        ub, ua, usb, usa = edad_desde(cb), edad_desde(ca), edad_desde(csb), edad_desde(csa)
        # operaciones del token
        ta, tb_ = bt[i], bt[i + 1]
        T_te, T_p, T_side, T_sz = tt["te"][ta:tb_], tt["p"][ta:tb_].astype(np.float64), tt["side"][ta:tb_], tt["sz"][ta:tb_]
        # cancelación = baja de tamaño al mismo precio sin operación en (te[i-1], te[i]]
        kt = np.searchsorted(T_te, te, side="right") - np.searchsorted(T_te, np.r_[te[0] - 1, te[:-1]], side="right")
        canc_b = np.r_[False, (~cb[1:]) & (bs[1:] < bs[:-1])] & (kt == 0)
        canc_a = np.r_[False, (~ca[1:]) & (as_[1:] < as_[:-1])] & (kt == 0)
        ucb, uca = edad_desde(canc_b), edad_desde(canc_a)
        t_ini, t_fin = (fin - 900) * 1000 + 5000, fin * 1000 - 10_000
        # -------------------------------------------------- A1: rellenos
        if len(T_te):
            k = np.searchsorted(te, T_te, side="left") - 1           # estado estrictamente anterior
            ok = (k >= 0) & (T_te >= t_ini) & (T_te <= t_fin)
            ok &= ~np.isnan(mid[np.clip(k, 0, None)])
            for j in np.flatnonzero(ok):
                kk = k[j]
                s = 1.0 if T_side[j] == 0 else -1.0                 # taker SELL -> maker compró (bid)
                top = bb[kk] if s > 0 else ba[kk]
                if np.isnan(top):
                    continue
                f = {"tok": i, "act": act, "mkt": mid_, "fin": fin, "t": int(T_te[j]), "s": s, "p": T_p[j],
                     "sz": float(T_sz[j]), "en_top": abs(T_p[j] - top) < 0.005, "lado_bid": s > 0}
                f["edad_precio"] = T_te[j] - te[ub[kk] if s > 0 else ua[kk]]
                f["edad_tam"] = T_te[j] - te[usb[kk] if s > 0 else usa[kk]]
                f["t_ult_canc"] = T_te[j] - te[ucb[kk] if s > 0 else uca[kk]]
                f["spread"] = ba[kk] - bb[kk]
                f["prof_propia"] = bs[kk] if s > 0 else as_[kk]
                f["prof_contra"] = as_[kk] if s > 0 else bs[kk]
                f["imb"] = s * (bs[kk] - as_[kk]) / max(1e-9, bs[kk] + as_[kk])
                micro = (bb[kk] * as_[kk] + ba[kk] * bs[kk]) / max(1e-9, bs[kk] + as_[kk])
                f["micro_mid"] = s * (micro - mid[kk])
                f["mid"] = mid[kk]
                f["tte"] = fin - T_te[j] / 1000
                k30 = np.searchsorted(te, T_te[j] - 30_000)
                f["vol30"] = int(np.count_nonzero(np.diff(mid[k30:kk + 1]))) if kk > k30 else 0
                k5 = np.searchsorted(te, T_te[j] - 5000, side="right") - 1
                f["mov5"] = s * (mid[kk] - mid[k5]) if k5 >= 0 else np.nan
                j10 = np.searchsorted(T_te, T_te[j] - 10_000)
                f["ntr10"] = j - j10
                j5 = np.searchsorted(T_te, T_te[j] - 5000)
                f["flujo5"] = s * float(np.sum(np.where(T_side[j5:j] == 1, 1, -1) * T_sz[j5:j])) if j > j5 else 0.0
                f["t_ult_trade"] = T_te[j] - T_te[j - 1] if j > 0 else np.nan
                for h in H:
                    kh = np.searchsorted(te, T_te[j] + h, side="right") - 1
                    f[f"mk_{h}"] = s * (mid[kh] - T_p[j]) if kh >= 0 and not np.isnan(mid[kh]) else np.nan
                f["mk_res"] = s * (gana - T_p[j])
                filas.append(f)
        # -------------------------------------------------- A2: rejilla 500 ms
        g = np.arange(t_ini, t_fin, 500, dtype=np.int64)
        kg = np.searchsorted(te, g, side="right") - 1
        okg = kg >= 0
        g, kg = g[okg], kg[okg]
        if len(g):
            nb = np.searchsorted(np.flatnonzero(cb) if cb.any() else np.array([], int), kg, side="right")
            ib = np.flatnonzero(cb)
            nxt = np.where(nb < len(ib), te[ib[np.minimum(nb, len(ib) - 1)]], np.iinfo(np.int64).max)
            dirb = np.where(nb < len(ib), np.sign(bb_f[ib[np.minimum(nb, len(ib) - 1)]] - bb_f[kg]), 0)
            rej.append(pd.DataFrame({"tok": i, "act": act, "fin": fin, "sl": sl, "t": g, "dt_next": nxt - g,
                                     "dir": dirb, "edad": g - te[ub[kg]], "spread": ba[kg] - bb[kg], "mid": mid[kg],
                                     "imb": (bs[kg] - as_[kg]) / np.maximum(1e-9, bs[kg] + as_[kg]),
                                     "tte": fin - g / 1000}))
    F = pd.DataFrame(filas)
    R = pd.concat(rej, ignore_index=True)
    # estado del subyacente (Chainlink FV y Binance) con signo del maker
    F["fv_mid"] = np.nan
    F["bn1s"] = np.nan
    F["bn200"] = np.nan
    for (act, fin), idx in F.groupby(["act", "fin"]).groups.items():
        sub = F.loc[idx]
        sl = np.where(sub["tok"].map(lambda x: toks[x][4] in ("YES", "Up")), 1.0, -1.0)
        fv = fv_en(clv, tw, act, fin, sub["t"].values)
        fv_tok = np.where(sl > 0, fv, 1 - fv)
        F.loc[idx, "fv_mid"] = sub["s"].values * (fv_tok - sub["mid"].values)
    for act, idx in F.groupby("act").groups.items():
        sub = F.loc[idx]
        sl = np.where(sub["tok"].map(lambda x: toks[x][4] in ("YES", "Up")), 1.0, -1.0)
        F.loc[idx, "bn1s"] = sub["s"].values * sl * binance_ret(C, sim[act], sub["t"].values, 1000)
        F.loc[idx, "bn200"] = sub["s"].values * sl * binance_ret(C, sim[act], sub["t"].values, 200)
    for act, idx in R.groupby("act").groups.items():
        sub = R.loc[idx]
        R.loc[idx, "bn1s_abs"] = np.abs(binance_ret(C, sim[act], sub["t"].values, 1000))
    F["per"] = periodo(F["t"].values)
    R["per"] = periodo(R["t"].values)
    out = Path("/root/polymarket-research-datalogs/m15_ms_cache")
    F.to_parquet(out / "A_rellenos.parquet")
    R.to_parquet(out / "A_rejilla.parquet")
    informe(F, R)


def boot_cierres(df, col, B=1000, seed=1):
    rng = np.random.default_rng(seed)
    g = df.groupby("fin")[col].agg(["sum", "count"])
    s, n = g["sum"].values, g["count"].values
    bs = []
    for _ in range(B):
        k = rng.integers(0, len(s), len(s))
        bs.append(s[k].sum() / n[k].sum())
    return np.percentile(bs, [5, 95])


def informe(F, R):
    D = F[F["per"].isin(["DISC", "VALID"]) & F["en_top"]].copy()
    print(f"A1 rellenos en el top (DISC+VALID; FINAL bloqueado): {len(D)} | mercados {D['mkt'].nunique()} | "
          f"cierres {D['fin'].nunique()} | DISC {sum(D.per == 'DISC')} VALID {sum(D.per == 'VALID')}")
    print("\nE[markout del maker por acción | edad del PRECIO de la cotización] (DISC+VALID, IC90 bootstrap de cierres)")
    D["b_edad"] = pd.cut(D["edad_precio"], [-1, 100, 1000, 5000, 30000, 1e12], labels=["<0,1s", "0,1-1s", "1-5s", "5-30s", ">30s"])
    cols = ["mk_1", "mk_25", "mk_215", "mk_1000", "mk_5000", "mk_30000", "mk_res"]
    print(f"{'edad':8} {'n':>6} " + " ".join(f"{c:>9}" for c in cols) + f" {'IC90 res':>17} {'P(tóx)':>7}")
    D["toxico"] = (D["mk_5000"] <= -0.0099).astype(float)
    for b, g in D.groupby("b_edad", observed=True):
        ic = boot_cierres(g, "mk_res")
        print(f"{b:8} {len(g):6} " + " ".join(f"{g[c].mean():+9.4f}" for c in cols)
              + f" ({ic[0]:+.4f},{ic[1]:+.4f}) {g['toxico'].mean():7.3f}")
    print("\nTodos los horizontes (media, DISC+VALID): " + " ".join(f"{h}ms:{D[f'mk_{h}'].mean():+.4f}" for h in H)
          + f" res:{D['mk_res'].mean():+.4f}")
    # incremental: con y sin edad
    from sklearn.ensemble import HistGradientBoostingRegressor, HistGradientBoostingClassifier
    from sklearn.metrics import log_loss, r2_score
    ctrl = ["spread", "prof_propia", "prof_contra", "imb", "micro_mid", "mid", "tte", "vol30", "mov5", "ntr10",
            "flujo5", "t_ult_trade", "fv_mid", "bn1s", "bn200", "lado_bid"]
    edad = ["edad_precio", "edad_tam", "t_ult_canc"]
    Dd, Dv = D[D.per == "DISC"], D[D.per == "VALID"]
    print(f"\n¿Aporta la EDAD información incremental? (entrena DISC n={len(Dd)}, mide VALID n={len(Dv)})")
    rng = np.random.default_rng(3)
    for y, tipo in (("mk_5000", "r"), ("mk_res", "r"), ("toxico", "c")):
        res = {}
        for nom, X in (("controles", ctrl), ("controles+edad", ctrl + edad), ("solo edad", edad)):
            m = Dd[y].notna()
            if tipo == "r":
                mdl = HistGradientBoostingRegressor(max_iter=200, learning_rate=0.05, min_samples_leaf=200, random_state=0)
                mdl.fit(Dd.loc[m, X].astype(float), Dd.loc[m, y])
                mv = Dv[y].notna()
                pr = mdl.predict(Dv.loc[mv, X].astype(float))
                res[nom] = (pr, Dv.loc[mv, y].values, Dv.loc[mv, "fin"].values)
            else:
                mdl = HistGradientBoostingClassifier(max_iter=200, learning_rate=0.05, min_samples_leaf=200, random_state=0)
                mdl.fit(Dd.loc[m, X].astype(float), Dd.loc[m, y])
                mv = Dv[y].notna()
                pr = mdl.predict_proba(Dv.loc[mv, X].astype(float))[:, 1]
                res[nom] = (pr, Dv.loc[mv, y].values, Dv.loc[mv, "fin"].values)
        def met(p, yv):
            return r2_score(yv, p) if tipo == "r" else -log_loss(yv, np.clip(p, 1e-4, 1 - 1e-4))
        base, con = res["controles"], res["controles+edad"]
        fins = np.unique(base[2])
        dif = []
        for _ in range(300):
            sel = np.isin(base[2], rng.choice(fins, len(fins)))
            dif.append(met(con[0][sel], con[1][sel]) - met(base[0][sel], base[1][sel]))
        print(f"  {y:8} {'R²' if tipo == 'r' else '−logloss'}: controles {met(*base[:2]):+.4f} | +edad {met(*con[:2]):+.4f} | "
              f"solo edad {met(*res['solo edad'][:2]):+.4f} | mejora por la edad IC90 cierres ({np.percentile(dif, 5):+.4f},"
              f"{np.percentile(dif, 95):+.4f})")
    # A2
    Rv = R[R["per"].isin(["DISC", "VALID"])].copy()
    print(f"\nA2 hazard de repricing del BID (rejilla 500 ms, DISC+VALID, n={len(Rv)})")
    Rv["b_edad"] = pd.cut(Rv["edad"], [-1, 100, 1000, 5000, 30000, 1e12], labels=["<0,1s", "0,1-1s", "1-5s", "5-30s", ">30s"])
    Rv["b_bn"] = pd.cut(Rv["bn1s_abs"], [-1, 0.5, 2, 5, 1e9], labels=["<0,5bps", "0,5-2", "2-5", ">5bps"])
    for col in ("b_edad", "b_bn"):
        print(f"  por {col}:  " + " | ".join(f"{x}ms" for x in HZ))
        for b, g in Rv.groupby(col, observed=True):
            print(f"    {str(b):8} n={len(g):7} " + " ".join(f"{(g['dt_next'] <= x).mean():.4f}" for x in HZ))
    from sklearn.metrics import roc_auc_score
    from sklearn.ensemble import HistGradientBoostingClassifier as HGC
    Xc = ["edad", "spread", "mid", "imb", "tte", "bn1s_abs"]
    y = (Rv["dt_next"] <= 215).astype(int)
    md = Rv.per == "DISC"
    mdl = HGC(max_iter=150, learning_rate=0.05, min_samples_leaf=500, random_state=0).fit(Rv.loc[md, Xc], y[md])
    p = mdl.predict_proba(Rv.loc[~md, Xc])[:, 1]
    print(f"  señal previa de repricing a 215 ms: AUC VALID {roc_auc_score(y[~md], p):.3f} (base {y[~md].mean():.4f}); "
          f"top 1 % de la señal: P(repricing<=215ms) {y[~md].values[p >= np.quantile(p, 0.99)].mean():.3f}")


if __name__ == "__main__":
    main()
