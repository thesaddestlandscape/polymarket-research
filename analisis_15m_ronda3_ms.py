#!/usr/bin/env python3
"""analisis_15m_ronda3_ms.py -- misión 15m, RONDA 3 parte ms (07-Oct, Javi opción (b)): SECUENCIAS finas a 1 s sobre el
registro ms (datalogs/m15_maestro_06oct.csv; libro y operaciones con reloj del exchange, Binance/Chainlink por recepción).
Catálogo: M15 #105 (operación -> cancelación -> cambio de cotización), #106 (5m se mueve -> 15m se mueve -> ¿continúa?),
y las mismas secuencias con Binance y Chainlink como primer paso; regímenes finos (cotización vieja, spread, actividad).

PROTOCOLO (fijado ANTES de mirar; cortes = los de A1-A3): DISC 05-Oct 16:00 -> 06-Oct 02:00 | EMB -> 03:30 |
VALID 03:30 -> 09:30 | FINAL 09:30 -> fin BLOQUEADO (solo se abre para una señal que pase TODO en VALID).
  - Señal con signo (+ = comprar YES). Umbral P90 de |señal| en DISC (binarias: 0,5). 1 operación por (mercado, minuto).
  - INFORMACIÓN (sin costes): markout firmado del mid YES a +1/+5/+30 s, en céntimos.
  - DINERO: tomador al ask REAL a +215 ms (Y_askY_215 / Y_askN_215), a resolución oficial y en ida y vuelta vendiendo al
    bid a +215 ms + 5 s; comisión 0,07·p(1-p) por pata; por € arriesgado.
  - IC90 por bootstrap de CIERRES (todas las monedas que cierran a la vez = una apuesta).
  - Control: 200 permutaciones de la señal dentro de (cierre, minuto del contrato, tramo de mid 0,1); p individual y
    familiar (max-stat) sobre el markout de 5 s y sobre el EV a resolución.
  - SUPERVIVIENTE VALID = info 5 s > 0 en DISC y VALID con p_fam(info) < 0,10 Y EV resolución > 0 en DISC y VALID con
    IC90 de cierres > 0 en VALID. Solo entonces se mide en FINAL.
Uso: (ulimit -v 4000000; nice -n 10 python3 analisis_15m_ronda3_ms.py) > informes/m15_ronda3_ms_07oct.txt
"""
import argparse
from datetime import datetime, timezone

import numpy as np
import pandas as pd

CSV = "/root/polymarket-research-datalogs/m15_maestro_06oct.csv"
FEE = 0.07


def ms(s):
    return int(datetime.fromisoformat(s).replace(tzinfo=timezone.utc).timestamp() * 1000)


DISC = (ms("2026-10-05T16:00"), ms("2026-10-06T02:00"))
VALID = (ms("2026-10-06T03:30"), ms("2026-10-06T09:30"))
FINAL = (ms("2026-10-06T09:30"), ms("2026-10-07T00:00"))
COLS = ["moneda", "market", "cierre", "t", "desenlace", "t_desde_inicio_s", "t_hasta_cierre_s",
        "y_bid", "y_ask", "y_asz", "y_spread", "y_mid", "y_edad_mid", "y_cambios_1s", "y_menos_ask_1s", "y_ntr_1s",
        "y_flujo_1s", "y_desde_trade", "y_vel_1s", "y_vel_5s",
        "n_ask", "n_asz", "n_menos_ask_1s", "n_ntr_1s", "n_flujo_1s", "n_vel_1s", "n_desde_trade",
        "cl_ret_5s_bps", "m5_vel_1s", "bn_ret_1s_bps", "bn_ret_5s_bps",
        "Y_mid_1000", "Y_mid_5000", "Y_mid_30000", "Y_askY_215", "Y_askN_215", "Y_bidY_5000", "Y_bidN_5000"]


def fee(p):
    return FEE * p * (1 - p)


def cargar():
    df = pd.read_csv(CSV, usecols=lambda c: c in COLS)
    for c in df.columns:
        if df[c].dtype == np.float64:
            df[c] = df[c].astype(np.float32)
    df = df[(df["y_bid"] <= df["y_ask"])].sort_values(["market", "t"]).reset_index(drop=True)
    t = df["t"].values
    df["per"] = np.select([(t >= DISC[0]) & (t < DISC[1]), (t >= VALID[0]) & (t < VALID[1]), t >= FINAL[0]],
                          ["DISC", "VALID", "FINAL"], "EMB")
    w = (df["desenlace"] == "YES").astype(np.float32).values
    aY, aN = df["Y_askY_215"].values, df["Y_askN_215"].values
    okY, okN = (aY > 0) & (aY < 1), (aN > 0) & (aN < 1)
    df["evY"] = np.where(okY, (w - aY - fee(aY)) / (aY + fee(aY)), np.nan)
    df["evN"] = np.where(okN, ((1 - w) - aN - fee(aN)) / (aN + fee(aN)), np.nan)
    bY, bN = df["Y_bidY_5000"].values, df["Y_bidN_5000"].values
    df["rtY"] = np.where(okY & (bY > 0), (bY - aY - fee(aY) - fee(bY)) / (aY + fee(aY)), np.nan)
    df["rtN"] = np.where(okN & (bN > 0), (bN - aN - fee(aN) - fee(bN)) / (aN + fee(aN)), np.nan)
    for h in (1000, 5000, 30000):
        df[f"mk{h}"] = (df[f"Y_mid_{h}"] - df["y_mid"]) * 100
    df["clave"] = df["market"].astype(np.int64) * 100 + (df["t_desde_inicio_s"] // 60).astype(np.int64)
    return df


def hipotesis(df):
    g = lambda c: df[c].astype(float)
    sgn = lambda x: np.sign(x).replace(0, np.nan)
    disc = (df["per"] == "DISC").values
    H = {}
    vy, vn = g("y_vel_1s"), g("n_vel_1s")
    fy, fn = g("y_flujo_1s"), g("n_flujo_1s")
    compra = pd.Series(np.where(fy > 0, 1.0, np.where(fn > 0, -1.0, np.nan)), index=df.index)  # agresor del último 1 s
    repr_ = pd.Series(np.where(vy > 0, 1.0, np.where(vy < 0, -1.0, 0.0)), index=df.index)
    # #105 operación -> repricing en su sentido -> ¿continúa?
    H["sec.op_luego_repricing_continua"] = compra.where(repr_ == compra)
    H["sec.op_luego_repricing_revierte"] = -compra.where(repr_ == compra)
    H["sec.op_sin_repricing_sigue"] = compra.where(repr_ == 0)          # el libro aún no se ha movido
    H["sec.op_sin_repricing_revierte"] = -compra.where(repr_ == 0)
    # cancelación (baja de tamaño del ask al mismo precio, sin operaciones) -> ¿el maker sabe algo?
    cy = (g("y_menos_ask_1s") > 0) & (g("y_ntr_1s") == 0)
    cn = (g("n_menos_ask_1s") > 0) & (g("n_ntr_1s") == 0)
    canc = pd.Series(np.where(cy & ~cn, 1.0, np.where(cn & ~cy, -1.0, np.nan)), index=df.index)
    H["sec.cancelacion_ask_sigue"], H["sec.cancelacion_ask_revierte"] = canc, -canc
    H["sec.cancelacion_luego_repricing"] = canc.where(repr_ == canc)
    # #106 5m -> 15m -> ¿continúa?
    m5 = g("m5_vel_1s")
    H["sec.m5_y_15_continua"] = sgn(vy).where(sgn(m5) == sgn(vy))
    H["sec.m5_y_15_revierte"] = -sgn(vy).where(sgn(m5) == sgn(vy))
    H["sec.m5_mueve_15_quieto"] = sgn(m5).where((vy == 0) & (m5.abs() >= 0.01))
    # Binance -> 15m -> ¿continúa?
    bn = g("bn_ret_1s_bps")
    q = df.loc[disc].assign(a=bn[disc].abs()).groupby("moneda")["a"].quantile(0.9)
    grande = bn.abs() >= df["moneda"].map(q)
    H["sec.bn_y_15_continua"] = sgn(bn).where(grande & (sgn(vy) == sgn(bn)))
    H["sec.bn_y_15_revierte"] = -sgn(bn).where(grande & (sgn(vy) == sgn(bn)))
    H["sec.bn_mueve_15_quieto"] = sgn(bn).where(grande & (vy == 0))
    cl = g("cl_ret_5s_bps")
    H["sec.cl_y_15_continua"] = sgn(cl).where((cl != 0) & (sgn(vy) == sgn(cl)))
    H["sec.cl_mueve_15_quieto"] = sgn(cl).where((cl.abs() > 0) & (vy == 0))
    # regímenes finos x impulso/reversión del último segundo
    edad_p90 = np.nanquantile(g("y_edad_mid")[disc], 0.9)
    spr = g("y_spread")
    reg = {"cotiz_vieja": g("y_edad_mid") >= edad_p90, "spread_ancho": spr >= 0.02, "spread_1c": spr <= 0.01,
           "activo": g("y_cambios_1s") >= 3, "terminal": g("t_hasta_cierre_s") < 120}
    for rn, rm in reg.items():
        H[f"reg.impulso1s@{rn}"] = sgn(vy).where(rm)
        H[f"reg.reversion1s@{rn}"] = -sgn(vy).where(rm)
        H[f"reg.bn_sigue@{rn}"] = sgn(bn).where(rm & grande)
    return {k: v.astype(float) for k, v in H.items()}


class Ev:
    def __init__(self, df):
        self.clave = df["clave"].values
        self.cierre = df["cierre"].values
        self.mon = df["moneda"].values
        self.c = {k: df[k].values for k in ("evY", "evN", "rtY", "rtN", "mk1000", "mk5000", "mk30000")}

    def run(self, s, thr, mask):
        idx = np.flatnonzero(mask & ~np.isnan(s) & (np.abs(s) >= thr))
        if len(idx) == 0:
            return None
        _, f = np.unique(self.clave[idx], return_index=True)
        idx = idx[np.sort(f)]
        yes = s[idx] > 0
        sg = np.where(yes, 1.0, -1.0)
        r = {"n": len(idx), "idx": idx, "ev": np.where(yes, self.c["evY"][idx], self.c["evN"][idx]),
             "rt": np.where(yes, self.c["rtY"][idx], self.c["rtN"][idx])}
        for h in (1000, 5000, 30000):
            r[f"mk{h}"] = sg * self.c[f"mk{h}"][idx]
        return r


def ic_cierres(E, r, k, rng, B=1000):
    v, ci = r[k], E.cierre[r["idx"]]
    ok = ~np.isnan(v)
    v, ci = v[ok], ci[ok]
    if len(v) < 10:
        return np.nan, np.nan, np.nan
    u, inv = np.unique(ci, return_inverse=True)
    S, N = np.bincount(inv, v), np.bincount(inv)
    bs = [S[k_].sum() / N[k_].sum() for k_ in (rng.integers(0, len(u), len(u)) for _ in range(B))]
    o = np.argsort(-S)
    sin_mejor = (S.sum() - S[o[0]]) / (N.sum() - N[o[0]])
    return np.percentile(bs, 5), np.percentile(bs, 95), sin_mejor


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--perms", type=int, default=200)
    a = ap.parse_args()
    df = cargar()
    E = Ev(df)
    rng = np.random.default_rng(11)
    per = df["per"].values
    disc, valid, final = per == "DISC", per == "VALID", per == "FINAL"
    print(f"filas {len(df)} | mercados {df['market'].nunique()} | DISC {disc.sum()} VALID {valid.sum()} "
          f"(FINAL {final.sum()} bloqueado) | cierres VALID {df.loc[valid, 'cierre'].nunique()}")
    for lado, s in (("YES", 1.0), ("NO", -1.0)):
        sv = np.full(len(df), s)
        for p_, m in (("DISC", disc), ("VALID", valid)):
            r = E.run(sv, 0.5, m)
            print(f"línea base comprar SIEMPRE {lado} {p_}: EV res {np.nanmean(r['ev']):+.3f} rt5s {np.nanmean(r['rt']):+.3f} "
                  f"mk5s {np.nanmean(r['mk5000']):+.3f}c")
    H = hipotesis(df)
    tramo = np.clip((df["y_mid"].values * 10).astype(int), 0, 9)
    gid = pd.factorize(df["cierre"].astype(str) + "_" + (df["t_desde_inicio_s"] // 60).astype(int).astype(str)
                       + "_" + tramo.astype(str))[0]
    filas = []
    for nombre, s in H.items():
        sv = s.values
        sd = np.abs(sv[disc & ~np.isnan(sv)])
        if len(sd) < 200:
            continue
        thr = 0.5 if len(np.unique(sd[:5000])) <= 2 else np.quantile(sd, 0.9)
        rd, rv = E.run(sv, thr, disc), E.run(sv, thr, valid)
        if rd is None or rv is None or rv["n"] < 30:
            continue
        f = dict(h=nombre, sv=sv, thr=thr, nd=rd["n"], nv=rv["n"],
                 **{f"{k}_{p_}": np.nanmean(r[k]) for p_, r in (("d", rd), ("v", rv))
                    for k in ("mk1000", "mk5000", "mk30000", "ev", "rt")})
        f["lo"], f["hi"], f["sin1"] = ic_cierres(E, rv, "ev", rng)
        f["mk_lo"], f["mk_hi"], _ = ic_cierres(E, rv, "mk5000", rng)
        f["merc_v"] = len(np.unique(df["market"].values[rv["idx"]]))
        filas.append(f)
    # permutaciones dentro de grupo (los nan quedan en su sitio)
    Mmk = np.full((a.perms, len(filas)), np.nan)
    Mev = np.full((a.perms, len(filas)), np.nan)
    for b in range(a.perms):
        rk = rng.random(len(df))
        for j, f in enumerate(filas):
            sv = f["sv"]
            if "g2" not in f:
                f["g2"] = gid.astype(np.int64) * 2 + ~np.isnan(sv)
                f["ob"] = np.argsort(f["g2"], kind="stable")
            sp = np.empty_like(sv)
            sp[f["ob"]] = sv[np.lexsort((rk, f["g2"]))]
            r = E.run(sp, f["thr"], valid)
            if r is not None:
                Mmk[b, j], Mev[b, j] = np.nanmean(r["mk5000"]), np.nanmean(r["ev"])
        if (b + 1) % 50 == 0:
            print(f"   permutación {b + 1}/{a.perms}", flush=True)
    for M_, k, obs in ((Mmk, "mk", "mk5000_v"), (Mev, "ev", "ev_v")):
        mu, sd = np.nanmean(M_, 0), np.nanstd(M_, 0)
        sd[sd == 0] = np.nan
        maxZ = np.nanmax((M_ - mu) / sd, 1)
        for j, f in enumerate(filas):
            f[f"c_{k}"] = mu[j]
            f[f"pi_{k}"] = (np.sum(M_[:, j] >= f[obs]) + 1) / (a.perms + 1)
            z = (f[obs] - mu[j]) / sd[j]
            f[f"pf_{k}"] = (np.sum(maxZ >= z) + 1) / (a.perms + 1) if z == z else np.nan
    filas.sort(key=lambda f: -f["mk5000_v"])
    print(f"\nhipótesis {len(filas)} | permutaciones {a.perms}\n")
    print(f"{'hipótesis':32} {'nD':>5} {'nV':>5} {'merc':>4} | INFO mid YES firmado (c) DISC 1s/5s/30s | VALID 1s/5s/30s "
          f"| ctl μ5s p_ind p_fam | DINERO +215ms EV res D/V  IC90 cierres V  sin mejor | rt5s D/V | ctl μEV p_fam")
    for f in filas:
        print(f"{f['h']:32} {f['nd']:5} {f['nv']:5} {f['merc_v']:4} | {f['mk1000_d']:+.2f}/{f['mk5000_d']:+.2f}/{f['mk30000_d']:+.2f} "
              f"| {f['mk1000_v']:+.2f}/{f['mk5000_v']:+.2f}/{f['mk30000_v']:+.2f} | {f['c_mk']:+.2f} {f['pi_mk']:.3f} "
              f"{f['pf_mk']:.3f} | {f['ev_d']:+.3f}/{f['ev_v']:+.3f} ({f['lo']:+.3f},{f['hi']:+.3f}) {f['sin1']:+.3f} | "
              f"{f['rt_d']:+.3f}/{f['rt_v']:+.3f} | {f['c_ev']:+.3f} {f['pf_ev']:.3f}")
    info = [f for f in filas if f["mk5000_d"] > 0 and f["mk5000_v"] > 0 and f["pf_mk"] < 0.10]
    print(f"\nCON INFORMACIÓN (mk5s>0 DISC y VALID, p_fam<0,10): {len(info)} -> " + ", ".join(
        f"{f['h']} ({f['mk5000_v']:+.2f}c)" for f in info))
    sob = [f for f in info if f["ev_d"] > 0 and f["ev_v"] > 0 and f["lo"] > 0]
    print(f"SUPERVIVIENTES VALID (info + EV res >0 DISC y VALID, IC90 cierres >0): {len(sob)}")
    for f in sob:
        rf = E.run(f["sv"], f["thr"], final)
        lo, hi, s1 = ic_cierres(E, rf, "ev", rng) if rf else (np.nan,) * 3
        print(f"   FINAL {f['h']}: n={rf['n'] if rf else 0} EV {np.nanmean(rf['ev']) if rf else np.nan:+.3f} "
              f"IC90 ({lo:+.3f},{hi:+.3f}) sin mejor {s1:+.3f} mk5s {np.nanmean(rf['mk5000']) if rf else np.nan:+.2f}c")
    rt = [f for f in info if f["rt_d"] > 0 and f["rt_v"] > 0]
    print(f"Con información Y ida y vuelta a 5 s >0 en DISC y VALID: {len(rt)} -> " + ", ".join(f["h"] for f in rt))


if __name__ == "__main__":
    main()
