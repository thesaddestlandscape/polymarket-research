#!/usr/bin/env python3
"""analisis_15m_C_colas.py -- MISIÓN DEFINITIVA 15m, línea C (06-Oct): ¿se puede ANTICIPAR la cola del dinero?
Objetivo = EUROS NETOS CAPTURABLES, no probabilidad. Fijado antes de mirar:
ESCALA ms (datalogs/m15_maestro_06oct.csv, rejilla ~1 s, ejecución EXACTA a +215 ms): unidad (mercado, lado, fila);
  € capturables con stake S = min(S/ask215, tamaño nivel 1 a 215) · (gana − ask − 0,07·ask(1−ask)). Corte: DISC 05-Oct
  16:00 → 06-Oct 02:00 | EMB → 03:30 | VALID → 09:30 | FINAL → fin del dataset (bloqueado salvo que VALID pase).
ESCALA MES (datalogs/m15mes, fotos ~45 s, sin tamaños): € con stake 2 € a la cota PESIMISTA (ask de la foto siguiente).
  DESC 16-28 Sep | embargo 29 | PRUEBA 30-Sep..05-Oct. Rasgos de flujo EXCLUIDOS (firehose mezcla tomador y maker).
1. Concentración retrospectiva: % del € positivo total en el top 1/5/10 % de unidades (y cuántas hay).
2. Prospectivo: HistGradientBoosting que predice € capturables (stake 2 €) con SOLO estado previo (shock Binance y
   Chainlink, spread, profundidad y desequilibrio, volatilidad, flujo del registro ms -auditado-, edad de la cotización,
   tiempo al cierre, desviación Chainlink, 5m, nivel de precio); entrenado en DISC/DESC. Regla: actuar en las unidades cuya
   predicción supera el percentil 99/95/90 de las predicciones de DISC/DESC; una operación por (mercado, lado, minuto).
   Controles: PLACEBO (predicción permutada dentro de hora × tramo de mid 0,10), INVERSIÓN (el decil inferior), LOMO
   (entrenar sin la moneda y medir en ella). Concentración: sin mejor cierre/día, sin top 1 % y top 5 % de operaciones,
   sin BTC. Capacidad (ms): stakes 0,5..100 €.
Uso: (ulimit -v 4500000; python3 analisis_15m_C_colas.py)   Solo lectura.
"""
import glob
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_15m_A_quote_age import DISC, VALID, FINAL  # noqa: E402

FEE = 0.07
DL = Path("/root/polymarket-research-datalogs")
STAKES = [0.5, 1, 2, 5, 10, 25, 50, 100]


def euros(ask, sz, win, stake):
    ok = np.isfinite(ask) & (ask > 0.01) & (ask < 0.99)
    a = np.where(ok, ask, 0.5)
    sh = np.where(ok, np.minimum(stake / a, np.where(np.isfinite(sz), sz, 1e9)), 0.0)
    return np.where(ok, sh * (win - a - FEE * a * (1 - a)), np.nan), np.where(ok, sh * (a + FEE * a * (1 - a)), np.nan)


def concentracion(e):
    e = e[np.isfinite(e)]
    pos = np.sort(e[e > 0])[::-1]
    out = []
    for q in (0.01, 0.05, 0.10):
        k = max(1, int(q * len(e)))
        top = np.sort(e)[::-1][:k]
        out.append(f"top {q:.0%} ({k} uds): {top.sum() / pos.sum():.0%} del € positivo, media {top.mean():+.3f}")
    return f"n={len(e)} € total {e.sum():+.1f} € positivo {pos.sum():+.1f} | " + " | ".join(out)


def evaluar(U, pred, thr, mask, etiqueta, pen=True):
    sel = U[mask & (pred >= thr) & U["e"].notna().values].copy()   # solo unidades con ask ejecutable
    sel = sel.sort_values("t").drop_duplicates(["mkt", "lado", "minuto"])
    if len(sel) < 5:
        return f"{etiqueta}: n={len(sel)}"
    e, r = sel["e"].values, sel["r"].values
    g = sel.groupby("blk")[["e", "r"]].sum()
    rng = np.random.default_rng(4)
    bs = [g.iloc[rng.integers(0, len(g), len(g))].pipe(lambda x: x.e.sum() / x.r.sum()) for _ in range(800)]
    o = np.argsort(-e)
    k1, k5 = max(1, len(e) // 100), max(1, len(e) // 20)
    mejor = g["e"].idxmax()
    sinb = sel[sel.blk != mejor]
    sinbtc = sel[sel.act != "BTC"]
    return (f"{etiqueta}: n={len(sel)} merc={sel.mkt.nunique()} € {e.sum():+.1f} EV/€ {e.sum() / r.sum():+.3f} "
            f"IC90 bloques ({np.percentile(bs, 5):+.3f},{np.percentile(bs, 95):+.3f}) | sin mejor bloque "
            f"{sinb.e.sum() / max(1e-9, sinb.r.sum()):+.3f} sin top1% {e[o[k1:]].sum() / r[o[k1:]].sum():+.3f} sin top5% "
            f"{e[o[k5:]].sum() / r[o[k5:]].sum():+.3f} sin BTC {sinbtc.e.sum() / max(1e-9, sinbtc.r.sum()):+.3f}")


def bloque_ms(U, feats, nombre):
    Dm, Vm = U["per"] == "DISC", U["per"] == "VALID"
    print(f"\n=== {nombre}: unidades DISC {Dm.sum()} VALID {Vm.sum()} | rasgos {len(feats)}")
    print("Concentración retrospectiva (DISC+VALID): " + concentracion(U.loc[Dm | Vm, "e"].values))
    m = Dm & U["e"].notna()
    mdl = HistGradientBoostingRegressor(max_iter=200, learning_rate=0.05, min_samples_leaf=300, random_state=0)
    mdl.fit(U.loc[m, feats].astype(float), U.loc[m, "e"])
    pred = mdl.predict(U[feats].astype(float))
    pd_ = pred[Dm.values]
    rng = np.random.default_rng(9)
    clave = U["hora"].astype(str) + "_" + U["tramo"].astype(str)
    plac = pd.Series(pred).groupby(clave.values).transform(lambda x: rng.permutation(x.values)).values
    for q in (0.99, 0.95, 0.90):
        thr = np.quantile(pd_, q)
        print("  " + evaluar(U, pred, thr, Vm.values, f"VALID top {1 - q:.0%} predicho"))
        print("  " + evaluar(U, plac, thr, Vm.values, f"   PLACEBO top {1 - q:.0%}"))
        print("  " + evaluar(U, -pred, np.quantile(-pd_, q), Vm.values, f"   INVERSIÓN (peor {1 - q:.0%})"))
    # LOMO top 5 %
    tot_e = tot_r = 0.0
    pos = 0
    for act in sorted(U["act"].unique()):
        mm = m & (U["act"] != act)
        md = HistGradientBoostingRegressor(max_iter=200, learning_rate=0.05, min_samples_leaf=300, random_state=0)
        md.fit(U.loc[mm, feats].astype(float), U.loc[mm, "e"])
        pr = md.predict(U[feats].astype(float))
        thr = np.quantile(pr[(Dm & (U["act"] != act)).values], 0.95)
        sel = U[(Vm & (U["act"] == act) & U["e"].notna()).values & (pr >= thr)].sort_values("t").drop_duplicates(["mkt", "lado", "minuto"])
        if len(sel):
            tot_e += sel.e.sum()
            tot_r += sel.r.sum()
            pos += sel.e.sum() > 0
    print(f"  LOMO top 5 %: EV/€ en las monedas dejadas fuera {tot_e / max(1e-9, tot_r):+.3f}, monedas positivas {pos}/{U['act'].nunique()}")
    return mdl, pred


def main():
    # ---------------- escala ms
    cols = ["moneda", "market", "t", "desenlace", "hora", "t_hasta_cierre_s", "y_mid", "y_spread", "n_spread", "y_bsz",
            "y_asz", "n_bsz", "n_asz", "y_imb", "n_imb", "y_edad_ask", "n_edad_ask", "y_flujo_5s", "n_flujo_5s",
            "y_ntr_5s", "y_vel_5s", "sigma_bps_s", "z", "fv_yes", "cl_ret_5s_bps", "cl_ret_30s_bps", "m5_vel_5s",
            "bn_ret_1s_bps", "bn_ret_5s_bps", "Y_askY_215", "Y_askYsz_215", "Y_askN_215", "Y_askNsz_215"]
    M = pd.read_csv(DL / "m15_maestro_06oct.csv", usecols=cols, dtype={"market": str})
    M = M[M["t_hasta_cierre_s"] >= 10]
    w = (M["desenlace"] == "YES").astype(float).values
    partes = []
    for lado, sg in (("YES", 1.0), ("NO", -1.0)):
        a = M["Y_askY_215" if lado == "YES" else "Y_askN_215"].values
        s = M["Y_askYsz_215" if lado == "YES" else "Y_askNsz_215"].values
        e, r = euros(a, s, w if lado == "YES" else 1 - w, 2.0)
        U = pd.DataFrame({"t": M["t"].values, "mkt": M["market"].values, "act": M["moneda"].values, "lado": lado,
                          "hora": M["hora"].values, "e": e, "r": r, "ask": a,
                          "tramo": np.clip((np.where(sg > 0, M["y_mid"], 1 - M["y_mid"]) * 10).astype(int), 0, 9),
                          "tte": M["t_hasta_cierre_s"].values, "mid_l": np.where(sg > 0, M["y_mid"], 1 - M["y_mid"]),
                          "spread_l": M["y_spread"].values if lado == "YES" else M["n_spread"].values,
                          "prof_ask": s, "imb_l": sg * (M["y_imb"].values - M["n_imb"].values),
                          "edad_ask": M["y_edad_ask"].values if lado == "YES" else M["n_edad_ask"].values,
                          "flujo_l": sg * (M["y_flujo_5s"].values - M["n_flujo_5s"].values), "ntr5": M["y_ntr_5s"].values,
                          "vel_l": sg * M["y_vel_5s"].values, "sigma": M["sigma_bps_s"].values,
                          "cl_dev": np.where(sg > 0, M["fv_yes"] - M["y_mid"], M["y_mid"] - M["fv_yes"]),
                          "z_l": sg * M["z"].values, "cl5": sg * M["cl_ret_5s_bps"].values,
                          "cl30": sg * M["cl_ret_30s_bps"].values, "m5": sg * M["m5_vel_5s"].values,
                          "bn1": sg * M["bn_ret_1s_bps"].values, "bn5": sg * M["bn_ret_5s_bps"].values,
                          "win": w if lado == "YES" else 1 - w, "sz": s})
        partes.append(U)
    U = pd.concat(partes, ignore_index=True)
    U["per"] = np.where((U.t >= DISC[0]) & (U.t < DISC[1]), "DISC", np.where((U.t >= VALID[0]) & (U.t < VALID[1]), "VALID",
                        np.where(U.t >= FINAL[0], "FINAL", "EMB")))
    U["minuto"] = U.t // 60000
    U["blk"] = U["mkt"]          # bloque de bootstrap = mercado (en ms no hay días)
    feats = ["tte", "mid_l", "spread_l", "prof_ask", "imb_l", "edad_ask", "flujo_l", "ntr5", "vel_l", "sigma", "cl_dev",
             "z_l", "cl5", "cl30", "m5", "bn1", "bn5"]
    mdl, pred = bloque_ms(U, feats, "ESCALA ms (+215 ms exacto, stake 2 €)")
    # capacidad de la regla top 5 % en VALID
    thr = np.quantile(pred[(U.per == "DISC").values], 0.95)
    sel = U[(U.per == "VALID").values & (pred >= thr) & U["e"].notna().values].sort_values("t").drop_duplicates(["mkt", "lado", "minuto"])
    caps = []
    for S in STAKES:
        e, r = euros(sel["ask"].values, sel["sz"].values, sel["win"].values, S)
        caps.append(f"{S}€:{np.nansum(e):+.1f}€ ({np.nansum(e) / np.nansum(r):+.3f}/€)")
    print("  capacidad top 5 % VALID: " + " ".join(caps))
    # ---------------- escala mes
    fs = sorted(glob.glob(str(DL / "m15mes" / "m15mes_2026-*.csv")))
    D = pd.concat([pd.read_csv(f, dtype={"market": str}) for f in fs], ignore_index=True)
    w = (D["desenlace"] == "YES").astype(float).values
    partes = []
    for lado, sg in (("YES", 1.0), ("NO", -1.0)):
        a = D["ask_y_sig" if lado == "YES" else "ask_n_sig"].values
        e, r = euros(a, np.full(len(D), np.nan), w if lado == "YES" else 1 - w, 2.0)
        mid_l = D["mid"].values if lado == "YES" else 1 - D["mid"].values
        partes.append(pd.DataFrame({
            "t": D["t"].values, "mkt": D["market"].values, "act": D["moneda"].values, "lado": lado, "hora": D["hora"].values,
            "dia": D["dia"].values, "e": e, "r": r, "tramo": np.clip((mid_l * 10).astype(int), 0, 9), "mid_l": mid_l,
            "tte": D["t_hasta_cierre_s"].values, "spread": D["spread_y"].values, "suma_asks": D["suma_asks"].values,
            "vel1": sg * D["vel1"].values, "vel2": sg * D["vel2"].values, "sigma": D["sigma_bps_s"].values,
            "cl_dev": np.where(sg > 0, D["fv_yes"] - D["mid"], D["mid"] - D["fv_yes"]), "z_l": sg * D["z"].values,
            "cl30": sg * D["cl_ret_30s_bps"].values, "cl60": sg * D["cl_ret_60s_bps"].values,
            "cl300": sg * D["cl_ret_300s_bps"].values, "cl_edad": D["cl_edad_ms"].values,
            "m5": sg * D["m5_vel"].values, "m5_nivel": np.where(sg > 0, D["m5_mid"] - D["mid"], D["mid"] - D["m5_mid"])}))
    U2 = pd.concat(partes, ignore_index=True)
    U2["per"] = np.where(U2.dia <= "2026-09-28", "DISC", np.where(U2.dia >= "2026-09-30", "VALID", "EMB"))
    U2["minuto"] = U2.t // 60000
    U2["blk"] = U2["dia"]
    feats2 = ["mid_l", "tte", "spread", "suma_asks", "vel1", "vel2", "sigma", "cl_dev", "z_l", "cl30", "cl60", "cl300",
              "cl_edad", "m5", "m5_nivel"]
    bloque_ms(U2, feats2, "ESCALA MES (cota pesimista, stake 2 €; 'VALID' = PRUEBA 30-Sep..05-Oct, bloque = DÍA)")


if __name__ == "__main__":
    main()
