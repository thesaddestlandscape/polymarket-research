#!/usr/bin/env python3
"""analisis_15m_v4_superficie_resolucion.py -- MISIÓN 15M v4, HIPÓTESIS A (Javi 08-Oct): superficie empírica
P(gana | estado) del contrato 15m frente al precio EJECUTABLE, y dinero neto por modelo (no AUC).

No es un fair value paramétrico (Φ(z) está sobreconfiado, trampa 06-Oct): cada modelo estima P(gana) de forma
EMPÍRICA con los días ANTERIORES (walk-forward por día, nunca mira el día que evalúa) y opera solo si
    p_hat - ask - comisión(0,07·p·(1-p)) >= umbral.
Unidad = primera señal por (mercado, lado, tramo de tiempo restante): las fotos repetidas no son independientes.
IC90 por DÍAS (bootstrap de medias diarias), EV sin los 2 mejores días, % de la moneda principal.

Modelos (columna p_hat de cada lado YES/NO):
  M1 precio solo: tasa de acierto por cubo de ask (0,05).           M2 precio + tiempo: ask × tramo T.
  M3 lead + tiempo (SUPERVIVENCIA): lead firmado del lado (bps) × T.  M4 lead + T + volatilidad (tercil σ).
  M4g HGB(lead, T, σ) sin precio.  M6 HGB(precio + lead + T + σ + microestructura común).
  Terminal (parte 2, observador precierre_multioffset 15m, TWAP proyectado [e-62,e-3]): M1t ask × offset,
  M5 z_TWAP × offset, M5g HGB(ask, z_TWAP, offset, σ implícita).
Datos: parte 1 = fotos ~45 s del mes (datalogs/m15mes, 16-Sep..05-Oct, ask REAL de la foto = cota optimista);
  holdout = dataset ms 06-07 Oct (m15_maestro_07oct.csv) ejecutando al ask REAL a +215 ms (nuestra latencia).
  Parte 2 = precierre_multioffset_fase0.csv 15m (25-Sep..), ask del lado proyectado y del contrario (desde 30-Sep).
Uso: nice -n 19 ionice -c3 python3 analisis_15m_v4_superficie_resolucion.py [--salida informes/x.txt]
"""
import argparse
import glob
import os

os.environ.setdefault("OMP_NUM_THREADS", "1")                 # 08-Oct: 1 hilo (no sumar carga al VPS de 4 núcleos)
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

DL = Path("/root/polymarket-research-datalogs")
TB = [0, 10, 30, 60, 120, 300, 600, 901]
TB_N = ["0-10", "10-30", "30-60", "60-120", "120-300", "300-600", "600-900"]
LEAD_B = [-1e9, -40, -20, -10, -5, -2, 0, 2, 5, 10, 20, 40, 1e9]
UMBRALES = (0.0, 0.03, 0.05, 0.10)
MIN_TRAIN_DIAS = 8
BLOQUE = 3
RNG = np.random.default_rng(7)


def fee(p):
    return 0.07 * p * (1 - p)


def lados_mes(d):
    """Una fila por (foto, lado). lead/z/flujo con el signo del lado."""
    out = []
    for lado, s, ask, bid in (("YES", 1, "ask_y", "bid_y"), ("NO", -1, "ask_n", "bid_n")):
        x = pd.DataFrame({
            "dia": d.dia, "moneda": d.moneda, "market": d.market, "cierre": d.cierre, "lado": lado,
            "T": d.t_hasta_cierre_s, "ask": d[ask], "spread": d.spread_y, "suma_asks": d.suma_asks,
            "lead": s * d.dist_ref_bps, "z": s * d.z, "sigma": d.sigma_bps_s, "clr30": s * d.cl_ret_30s_bps,
            "win": (d.desenlace == lado).astype(int)})
        out.append(x)
    x = pd.concat(out, ignore_index=True)
    return x[(x.ask > 0.02) & (x.ask < 0.98) & x.lead.notna() & x.sigma.notna()]


def lados_maestro(d):
    out = []
    for lado, s, ask, a215, sz in (("YES", 1, "y_ask", "Y_askY_215", "Y_askYsz_215"), ("NO", -1, "n_ask", "Y_askN_215", "Y_askNsz_215")):
        x = pd.DataFrame({
            "dia": d.dia, "moneda": d.moneda, "market": d.market, "cierre": d.cierre, "lado": lado,
            "T": d.t_hasta_cierre_s, "ask": d[ask], "ask215": d[a215], "sz215": d[sz], "spread": d.y_spread,
            "suma_asks": d.suma_asks, "lead": s * d.dist_ref_bps, "z": s * d.z, "sigma": d.sigma_bps_s,
            "clr30": s * d.cl_ret_30s_bps, "win": (d.desenlace == lado).astype(int)})
        out.append(x)
    x = pd.concat(out, ignore_index=True)
    return x[(x.ask > 0.02) & (x.ask < 0.98) & x.lead.notna() & x.sigma.notna()]


def cubos(x, sig_cortes):
    x = x.copy()
    x["tb"] = pd.cut(x["T"], TB, right=False, labels=False)
    x["ab"] = np.clip((x.ask / 0.05).astype(int), 0, 19)
    x["lb"] = pd.cut(x.lead, LEAD_B, labels=False)
    x["sb"] = np.searchsorted(sig_cortes, x.sigma.values)
    return x


def p_tabla(tr, te, claves, prior=20):
    """Tasa de acierto por celda en train con prior Beta centrado en el ask medio de la celda (encoge al mercado)."""
    g = tr.groupby(claves).agg(w=("win", "sum"), n=("win", "size"), a=("ask", "mean")).reset_index()
    g["p"] = (g.w + prior * g.a) / (g.n + prior)
    g = g[g.n >= 30]
    m = te[claves].merge(g[claves + ["p"]], on=claves, how="left")
    return m["p"].values


FEAT_G = ["lead", "T", "sigma"]
FEAT_6 = ["ask", "lead", "T", "sigma", "spread", "suma_asks", "clr30"]


def hgb(tr, te, feats):
    m = HistGradientBoostingClassifier(max_iter=200, learning_rate=0.05, max_leaf_nodes=31, min_samples_leaf=200,
                                       l2_regularization=1.0, random_state=0)
    m.fit(tr[feats].values, tr.win.values)
    return m.predict_proba(te[feats].values)[:, 1]


def predecir(tr, te):
    P = {"M1": p_tabla(tr, te, ["ab"]), "M2": p_tabla(tr, te, ["ab", "tb"]), "M3": p_tabla(tr, te, ["lb", "tb"]),
         "M4": p_tabla(tr, te, ["lb", "tb", "sb"]), "M4g": hgb(tr, te, FEAT_G), "M6": hgb(tr, te, FEAT_6)}
    return P


def unidades(te, p, thr, ask_col="ask"):
    """Primera señal por (mercado, lado, tramo T) con edge neto >= thr. Devuelve filas con pnl por acción."""
    e = p - te[ask_col].values - fee(te[ask_col].values)
    sel = te[(e >= thr) & np.isfinite(e)].copy()
    sel["edge"] = e[(e >= thr) & np.isfinite(e)]
    sel = sel.sort_values("T", ascending=False).groupby(["market", "lado", "tb"], as_index=False).first()
    return sel


def resumen(u, precio="ask"):
    if len(u) == 0:
        return None
    px = u[precio].values
    u = u.assign(pnl_acc=u.win.values - px - fee(px), pnl_eur=(u.win.values - px - fee(px)) / px)
    dm = u.groupby("dia").pnl_eur.mean()
    bs = [dm.sample(len(dm), replace=True, random_state=int(RNG.integers(1e9))).mean() for _ in range(400)] if len(dm) > 1 else [np.nan]
    dsum = u.groupby("dia").pnl_eur.sum().sort_values()
    sin2 = u[~u.dia.isin(dsum.index[-2:])].pnl_eur.mean() if len(dsum) > 2 else np.nan
    return {"n": len(u), "merc": u.market.nunique(), "dias": u.dia.nunique(), "dias_pos": int((dm > 0).sum()),
            "acierto": u.win.mean(), "ask": px.mean(), "edge_prev": u.edge.mean(), "ev_acc": u.pnl_acc.mean(),
            "ev_eur": u.pnl_eur.mean(), "ic_lo": np.nanpercentile(bs, 5), "ic_hi": np.nanpercentile(bs, 95),
            "sin2": sin2, "top_mon": u.moneda.value_counts(normalize=True).iloc[0],
            "eur_dia_1acc": u.pnl_acc.sum() / max(1, u.dia.nunique())}


def fmt(r):
    if r is None:
        return "  (sin señales)"
    return (f"n={r['n']:5d} merc={r['merc']:5d} días={r['dias']:2d} (+{r['dias_pos']:2d}) acierto={r['acierto']:.3f} "
            f"ask={r['ask']:.3f} edge_prev={r['edge_prev']:+.3f} EV/acc={r['ev_acc']:+.4f} EV/€={r['ev_eur']:+.4f} "
            f"IC90d=({r['ic_lo']:+.3f},{r['ic_hi']:+.3f}) sin2mej={r['sin2']:+.4f} top_mon={r['top_mon']:.0%} "
            f"€/día@1acc={r['eur_dia_1acc']:+.2f}")


def parte1(L):
    dm = sorted(glob.glob(str(DL / "m15mes" / "m15mes_*.csv")))
    mes = lados_mes(pd.concat([pd.read_csv(f) for f in dm], ignore_index=True))
    sig_c = np.nanpercentile(mes.sigma, [33.3, 66.7])
    mes = cubos(mes, sig_c)
    dias = sorted(mes.dia.unique())
    L(f"PARTE 1 — fotos del mes: {len(mes)} filas-lado, {mes.market.nunique()} mercados, {len(dias)} días "
      f"({dias[0]}..{dias[-1]}); walk-forward desde el día {MIN_TRAIN_DIAS + 1}")
    # calibración descriptiva in-sample (superficie de supervivencia, sin dinero): P(lado con lead gana) por |lead| × T
    lid = mes[mes.lead > 0]
    tab = lid.groupby(["tb", pd.cut(lid.lead, [0, 2, 5, 10, 20, 40, 1e9])], observed=True).agg(
        n=("win", "size"), p_gana=("win", "mean"), ask=("ask", "mean")).reset_index()
    tab["gap"] = tab.p_gana - tab.ask
    L("\nSUPERVIVENCIA DEL LEAD (descriptiva, todo el mes; lado que va por delante): P(gana) vs ask medio de ese lado")
    for _, r in tab.iterrows():
        L(f"  T {TB_N[int(r.tb)]:>8s} lead {str(r.lead):>12s}: n={int(r.n):6d} P(gana)={r.p_gana:.3f} ask={r.ask:.3f} gap={r.gap:+.3f}")
    preds = []
    for i in range(MIN_TRAIN_DIAS, len(dias), BLOQUE):      # reentreno por bloques de días (coste), nunca ve su bloque
        bl = dias[i:i + BLOQUE]
        tr, te = mes[mes.dia < bl[0]], mes[mes.dia.isin(bl)].copy()
        for k, v in predecir(tr, te).items():
            te[k] = v
        preds.append(te)
    P = pd.concat(preds, ignore_index=True)
    L(f"\nOOS walk-forward: {P.dia.nunique()} días de prueba, {P.market.nunique()} mercados. Ejecución = ask de la FOTO (optimista).")
    for m in ("M1", "M2", "M3", "M4", "M4g", "M6"):
        L(f"\n== {m} ==")
        for thr in UMBRALES:
            u = unidades(P, P[m].values, thr)
            L(f" umbral {thr:.2f} TODOS  {fmt(resumen(u))}")
            if thr in (0.03, 0.05):
                for tb in range(len(TB_N)):
                    ut = u[u.tb == tb]
                    if len(ut) >= 15:
                        L(f"    T {TB_N[tb]:>8s} {fmt(resumen(ut))}")
    # holdout ms 06-07 Oct, modelos entrenados con TODO el mes, ejecución al ask REAL a +215 ms
    ma = pd.read_csv(DL / "m15_maestro_07oct.csv", usecols=lambda c: c in {
        "dia", "moneda", "market", "cierre", "t", "desenlace", "t_hasta_cierre_s", "y_ask", "n_ask", "Y_askY_215",
        "Y_askN_215", "Y_askYsz_215", "Y_askNsz_215", "y_spread", "suma_asks", "dist_ref_bps", "z", "sigma_bps_s",
        "cl_ret_30s_bps"})
    ma = ma[ma.t % 15000 < 1000]                                  # una foto cada ~15 s por mercado
    H = cubos(lados_maestro(ma), sig_c)
    pr = predecir(mes, H)
    L(f"\nHOLDOUT ms 06-07 Oct ({H.market.nunique()} mercados): señal con el ask de t, compra al ask REAL a +215 ms "
      f"(si sube y deja de cumplir el umbral: no se compra)")
    for m, p in pr.items():
        H[m] = p
        for thr in (0.03, 0.05, 0.10):
            u = unidades(H, p, thr)
            u = u[u.ask215.notna() & (u.ask215 > 0) & (u[m] - u.ask215 - fee(u.ask215) >= thr)]
            r = resumen(u, "ask215")
            L(f" {m:4s} umbral {thr:.2f} {fmt(r)}" + (f" prof_mediana={u.sz215.median():.0f} acc" if len(u) else ""))
    return P, H


def parte2(L):
    d = pd.read_csv(DL / "precierre_multioffset_fase0.csv", low_memory=False)
    d = d[(d.marco == "15m") & d.market_id.notna() & d.error.isna()].copy()
    d["market"] = d.market_id.astype(int).astype(str)
    des = desenlaces(set(d.market))
    d["des"] = d.market.map(des)
    d = d[d.des.notna()]
    d["dia"] = d.ts_utc.str[:10]
    d["zt"] = d.z_v2.where(d.z_v2.notna(), d.z).abs()
    d["moneda"] = d.activo
    filas = []
    for lado_lider, ask_c, sgn in ((True, "ask", 1), (False, "ask_contrario", -1)):
        x = d[["dia", "moneda", "market", "offset_s", "zt", ask_c, "direccion", "des"]].rename(columns={ask_c: "ask"})
        gana_lider = ((x.direccion == "Up") & (x.des == "YES")) | ((x.direccion == "Down") & (x.des == "NO"))
        x["win"] = (gana_lider if lado_lider else ~gana_lider).astype(int)
        x["lado"] = "lider" if lado_lider else "contrario"
        x["z"] = sgn * x.zt
        filas.append(x)
    X = pd.concat(filas, ignore_index=True)
    X = X[(X.ask > 0.02) & (X.ask < 0.98)].copy()
    X["T"] = -X.offset_s
    X["tb"] = X.offset_s
    X["ab"] = np.clip((X.ask / 0.05).astype(int), 0, 19)
    X["zb"] = pd.cut(X.z, [-1e9, -3, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 3, 5, 1e9], labels=False)
    dias = sorted(X.dia.unique())
    L(f"\nPARTE 2 — TERMINAL (TWAP proyectado), {len(X)} filas-lado con ask comprable, {X.market.nunique()} mercados, "
      f"{len(dias)} días ({dias[0]}..{dias[-1]}); lado contrario solo desde 30-Sep")
    tab = X.groupby(["offset_s", "lado", pd.cut(X.zt if "zt" in X else X.z.abs(), [0, 1, 1.5, 2, 3, 5, 1e9])], observed=True).agg(
        n=("win", "size"), p=("win", "mean"), ask=("ask", "mean")).reset_index()
    L("Superficie terminal descriptiva: P(gana) vs ask medio por offset × lado × |z_TWAP|")
    for _, r in tab[tab.n >= 30].iterrows():
        L(f"  off {int(r.offset_s):5d} {r.lado:9s} |z| {str(r.zt):>11s}: n={int(r.n):5d} P={r.p:.3f} ask={r.ask:.3f} gap={r.p - r.ask:+.3f}")
    preds = []
    for i in range(5, len(dias), 2):
        bl = dias[i:i + 2]
        tr, te = X[X.dia < bl[0]], X[X.dia.isin(bl)].copy()
        te["M1t"] = p_tabla(tr, te, ["ab", "tb"])
        te["M5"] = p_tabla(tr, te, ["zb", "tb"])
        te["M5g"] = hgb(tr, te, ["ask", "z", "T"])
        preds.append(te)
    P = pd.concat(preds, ignore_index=True)
    L(f"OOS walk-forward terminal: {P.dia.nunique()} días de prueba. Ejecución = ask leído por el observador (latencia del libro ~60-100 ms)")
    for m in ("M1t", "M5", "M5g"):
        for thr in UMBRALES:
            u = unidades(P, P[m].values, thr)
            L(f" {m:4s} umbral {thr:.2f} TODOS {fmt(resumen(u))}")
            if thr == 0.03:
                for off in sorted(P.offset_s.unique()):
                    for lado in ("lider", "contrario"):
                        ut = u[(u.tb == off) & (u.lado == lado)]
                        if len(ut) >= 15:
                            L(f"    off {off:5d} {lado:9s} {fmt(resumen(ut))}")
    return P


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default="informes/m15v4_superficie_resolucion_08oct.txt")
    a = ap.parse_args()
    lineas = []

    def L(s=""):
        print(s, flush=True)
        lineas.append(s)
    P1, H = parte1(L)
    P2 = parte2(L)
    Path(a.salida).write_text("\n".join(lineas) + "\n")
    cache = DL / "m15_ms_cache"
    P1.to_parquet(cache / "v4_superficie_oos_mes.parquet")
    H.to_parquet(cache / "v4_superficie_holdout_ms.parquet")
    P2.to_parquet(cache / "v4_superficie_terminal.parquet")


if __name__ == "__main__":
    main()
