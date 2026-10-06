#!/usr/bin/env python3
"""analisis_15m_mineria.py -- minería de alpha del 15m como activo autónomo sobre el dataset maestro
(analisis_15m_dataset_maestro.py). 06-Oct. Métrica principal: EUROS NETOS por € arriesgado comprando como TOMADOR al ask
real a +215 ms (YES si señal > 0, NO si < 0), comisión 0,07·p·(1-p), tamaño limitado al nivel 1 disponible, a
RESOLUCIÓN oficial; secundaria: ida y vuelta (vender al bid a +215 ms + H, H = 30/60 s, con comisión de tomador).
Protocolo (fijado antes de mirar resultados):
  - DESCUBRIMIENTO = primer 60 % de las horas del dataset; PRUEBA = último 40 % (temporal, sin mezclar).
  - umbral = percentil 90 de |señal| en DESCUBRIMIENTO; en PRUEBA se aplica tal cual.
  - una operación como máximo por (mercado, minuto): la primera fila que supera el umbral.
  - control negativo: la misma regla con la señal PERMUTADA entre filas del mismo minuto-del-contrato (rompe la relación
    señal->mercado, conserva la distribución); 20 permutaciones.
  - multiplicidad: nº de hipótesis con EV>0 en PRUEBA vs el de controles.
Uso: --csv <dataset> [--stake 2]
"""
import argparse
import math

import numpy as np
import pandas as pd

FEE = 0.07


def fee(p):
    return FEE * p * (1 - p)


def preparar(df, stake):
    for c in df.columns:
        if c not in ("moneda", "dia", "desenlace"):
            df[c] = pd.to_numeric(df[c], errors="coerce")
    df["win_yes"] = (df["desenlace"] == "YES").astype(float)
    aY, aN = df["Y_askY_215"], df["Y_askN_215"]
    shY = np.minimum(stake / aY, df["Y_askYsz_215"])
    shN = np.minimum(stake / aN, df["Y_askNsz_215"])
    df["pnl_res_Y"] = shY * (df["win_yes"] - aY - fee(aY))
    df["pnl_res_N"] = shN * ((1 - df["win_yes"]) - aN - fee(aN))
    df["rk_Y"], df["rk_N"] = shY * (aY + fee(aY)), shN * (aN + fee(aN))
    for H in (30000, 60000):
        bY, bN = df[f"Y_bidY_{H}"], df[f"Y_bidN_{H}"]
        df[f"pnl_rt{H // 1000}_Y"] = shY * (bY - aY - fee(aY) - fee(bY))
        df[f"pnl_rt{H // 1000}_N"] = shN * (bN - aN - fee(aN) - fee(bN))
    df["minuto"] = (df["t"] // 60000).astype(np.int64)
    df["min_contrato"] = (df["t_desde_inicio_s"] // 60).astype(int)
    return df


def hipotesis(df):
    """Señales con signo (+ = comprar YES). Nombre -> serie. Familias en el prefijo."""
    H = {}
    g = lambda c: df[c] if c in df else pd.Series(np.nan, index=df.index)
    # microestructura del propio 15m
    H["micro.imb_yes"] = g("y_imb")
    H["micro.imb_no_inv"] = -g("n_imb")
    H["micro.imb_neto"] = g("y_imb") - g("n_imb")
    H["micro.microprecio_yes"] = g("y_micro") - g("y_mid")
    H["micro.microprecio_no_inv"] = -(g("n_micro") - g("n_mid"))
    H["micro.agotamiento_ask_yes_1s"] = g("y_menos_ask_1s") - g("n_menos_ask_1s")
    H["micro.agotamiento_ask_5s"] = g("y_menos_ask_5s") - g("n_menos_ask_5s")
    H["micro.edad_asimetrica"] = np.log1p(g("n_edad_ask")) - np.log1p(g("y_edad_ask"))
    H["micro.suma_asks_baja"] = -(g("suma_asks") - 1) * np.sign(g("y_imb").fillna(0) + 1e-9)
    # flujo agregado
    for w in (1, 5, 30):
        H[f"flujo.compras_yes_{w}s"] = g(f"y_flujo_{w}s") - g(f"n_flujo_{w}s")
        H[f"flujo.reversion_{w}s"] = -(g(f"y_flujo_{w}s") - g(f"n_flujo_{w}s"))
    H["flujo.intensidad_x_dir"] = (g("y_ntr_5s") + g("n_ntr_5s")) * np.sign(g("y_vel_5s").fillna(0))
    # impulso / reversión del propio precio
    for w in (1, 5):
        H[f"precio.impulso_{w}s"] = g(f"y_vel_{w}s")
        H[f"precio.reversion_{w}s"] = -g(f"y_vel_{w}s")
    H["precio.aceleracion"] = g("y_acel")
    H["precio.aceleracion_inv"] = -g("y_acel")
    # fair value / Chainlink
    H["fv.misp"] = g("fv_yes") - g("y_mid")
    H["fv.misp_ejecutable"] = g("misp_yes") - g("misp_no")
    H["fv.z"] = g("z")
    H["fv.z_inv"] = -g("z")
    H["fv.dist_ref"] = g("dist_ref_bps")
    for w in (5, 30):
        H[f"chainlink.impulso_{w}s"] = g(f"cl_ret_{w}s_bps")
        H[f"chainlink.reversion_{w}s"] = -g(f"cl_ret_{w}s_bps")
    H["chainlink.adelanto_vs_libro"] = g("cl_ret_5s_bps") * 1e-4 * 50 - g("y_vel_5s")
    # 5m
    for w in (1, 5):
        H[f"m5.impulso_{w}s"] = g(f"m5_vel_{w}s")
        H[f"m5.adelanto_{w}s"] = g(f"m5_vel_{w}s") - g(f"y_vel_{w}s")
    # Binance
    for w in (1, 5, 30):
        H[f"binance.impulso_{w}s"] = g(f"bn_ret_{w}s_bps")
        H[f"binance.reversion_{w}s"] = -g(f"bn_ret_{w}s_bps")
    H["binance.adelanto_vs_libro"] = g("bn_ret_5s_bps") * 1e-4 * 50 - g("y_vel_5s")
    # calibración por nivel de precio (constante por tramo: comprar el lado barato/caro)
    for lo in np.arange(0.0, 1.0, 0.1):
        m = (g("y_mid") >= lo) & (g("y_mid") < lo + 0.1)
        H[f"calib.compra_yes_{lo:.1f}"] = m.astype(float).where(m, np.nan)
        H[f"calib.compra_no_{lo:.1f}"] = (-m.astype(float)).where(m, np.nan)
    # tiempo hasta el cierre x fair value
    late = g("t_hasta_cierre_s") < 120
    H["expira.fv_tarde"] = (g("fv_yes") - g("y_mid")).where(late)
    H["expira.impulso_tarde"] = g("y_vel_5s").where(late)
    early = g("t_desde_inicio_s") < 180
    H["expira.reversion_temprana"] = (-g("y_vel_5s")).where(early)
    # régimen de volatilidad x fair value
    alta = g("sigma_bps_s") > g("sigma_bps_s").median()
    H["regimen.fv_vol_alta"] = (g("fv_yes") - g("y_mid")).where(alta)
    H["regimen.fv_vol_baja"] = (g("fv_yes") - g("y_mid")).where(~alta)
    # secuencias
    H["secuencia.cl_mueve_libro_quieto"] = g("cl_ret_5s_bps").where(g("y_edad_mid") > 3000)
    H["secuencia.m5_mueve_15_quieto"] = g("m5_vel_5s").where(g("y_edad_mid") > 3000)
    H["secuencia.flujo_y_agotamiento"] = (g("y_flujo_5s") - g("n_flujo_5s")) * (1 + g("y_menos_ask_5s"))
    return H


def evaluar(df, s, thr, filas):
    """Aplica la regla sobre `filas` (máscara): |s| >= thr, primera por (mercado, minuto). -> métricas."""
    d = df.loc[filas & (s.abs() >= thr) & s.notna()].copy()
    if d.empty:
        return None
    d["s"] = s[d.index]
    d = d.sort_values("t").drop_duplicates(["market", "minuto"])
    yes = d["s"] > 0
    out = {}
    for tgt in ("res", "rt30", "rt60"):
        pn = np.where(yes, d[f"pnl_{tgt}_Y"], d[f"pnl_{tgt}_N"])
        rk = np.where(yes, d["rk_Y"], d["rk_N"])
        ok = ~np.isnan(pn) & ~np.isnan(rk) & (rk > 0)
        out[f"ev_{tgt}"] = pn[ok].sum() / rk[ok].sum() if ok.any() else np.nan
        out[f"pnl_{tgt}"] = pn[ok].sum()
        if tgt == "res":
            out["n"] = int(ok.sum())
            out["mercados"] = d.loc[ok, "market"].nunique()
            dd = d.loc[ok].assign(p=pn[ok], r=rk[ok]).groupby("dia")[["p", "r"]].sum()
            out["dias"] = len(dd)
            # desglose por moneda (dejar una fuera)
            mon = d.loc[ok].assign(p=pn[ok], r=rk[ok]).groupby("moneda")[["p", "r"]].sum()
            out["por_moneda"] = {m: round(r.p / r.r, 3) for m, r in mon.iterrows() if r.r > 0}
            out["sin_mejor_mercado"] = (pn[ok].sum() - d.loc[ok].assign(p=pn[ok]).groupby("market")["p"].sum().max()) / rk[ok].sum()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--stake", type=float, default=2.0)
    a = ap.parse_args()
    df = preparar(pd.read_csv(a.csv), a.stake)
    t0, t1 = df["t"].min(), df["t"].max()
    corte = t0 + 0.6 * (t1 - t0)
    desc, prueba = df["t"] < corte, df["t"] >= corte
    print(f"filas {len(df)} | mercados {df['market'].nunique()} | desde {pd.to_datetime(t0, unit='ms')} hasta "
          f"{pd.to_datetime(t1, unit='ms')} | corte DESCUBRIMIENTO/PRUEBA {pd.to_datetime(corte, unit='ms')}")
    # línea base: comprar SIEMPRE el lado del mid > 0,5 (favorito) / el barato
    H = hipotesis(df)
    rng = np.random.default_rng(3)
    res = []
    for nombre, s in H.items():
        sd = s[desc].dropna()
        if len(sd) < 200 or sd.abs().max() == 0:
            continue
        thr = sd.abs().quantile(0.9) if sd.nunique() > 2 else 0.5
        rd = evaluar(df, s, thr, desc)
        rp = evaluar(df, s, thr, prueba)
        if not rd or not rp:
            continue
        # control negativo: permutar la señal dentro del minuto del contrato (en PRUEBA)
        ctl = []
        for _ in range(20):
            sp = s.copy()
            idx = df.index[prueba & s.notna()]
            grupos = df.loc[idx, "min_contrato"]
            perm = sp[idx].groupby(grupos).transform(lambda x: x.sample(frac=1, random_state=int(rng.integers(1e9))).values)
            sp[idx] = perm.values
            r = evaluar(df, sp, thr, prueba)
            if r and r["n"] >= 10:
                ctl.append(r["ev_res"])
        res.append((nombre, rd, rp, np.mean(ctl) if ctl else np.nan, np.percentile(ctl, 95) if ctl else np.nan))
    res.sort(key=lambda x: -(x[2]["ev_res"] if not math.isnan(x[2]["ev_res"]) else -9))
    print(f"\nhipótesis evaluadas: {len(res)}")
    print(f"{'hipótesis':38} {'DESC ev_res':>11} {'n':>5} | {'PRUEBA ev_res':>13} {'n':>5} {'merc':>5} {'rt30':>7} {'rt60':>7} | "
          f"{'control μ':>9} {'control p95':>11} | sin mejor mercado | por moneda (prueba)")
    for nombre, rd, rp, cm, c95 in res:
        print(f"{nombre:38} {rd['ev_res']:+11.3f} {rd['n']:5} | {rp['ev_res']:+13.3f} {rp['n']:5} {rp['mercados']:5} "
              f"{rp['ev_rt30']:+7.3f} {rp['ev_rt60']:+7.3f} | {cm:+9.3f} {c95:+11.3f} | {rp['sin_mejor_mercado']:+.3f} | "
              + " ".join(f"{k}:{v:+.2f}" for k, v in sorted(rp["por_moneda"].items())))
    pos_desc_y_prueba = [r for r in res if r[1]["ev_res"] > 0 and r[2]["ev_res"] > 0 and r[2]["ev_res"] > r[4]]
    print(f"\nPositivas en DESCUBRIMIENTO y en PRUEBA y por encima del p95 de su control: {len(pos_desc_y_prueba)} de {len(res)}")
    for r in pos_desc_y_prueba:
        print(f"   {r[0]}: desc {r[1]['ev_res']:+.3f} (n={r[1]['n']}) prueba {r[2]['ev_res']:+.3f} (n={r[2]['n']}, mercados {r[2]['mercados']})")
    # modelo combinado
    try:
        from sklearn.ensemble import HistGradientBoostingRegressor
        feats = [c for c in df.columns if not c.startswith(("Y_", "pnl_", "rk_", "win_")) and c not in
                 ("moneda", "market", "cierre", "t", "desenlace", "dia", "minuto", "min_contrato")]
        for lado in ("Y", "N"):
            y = df[f"pnl_res_{lado}"] / df[f"rk_{lado}"]
            m = desc & y.notna()
            mdl = HistGradientBoostingRegressor(max_iter=200, learning_rate=0.05, max_leaf_nodes=15, min_samples_leaf=200)
            mdl.fit(df.loc[m, feats], y[m])
            pr = pd.Series(mdl.predict(df[feats]), index=df.index)
            thr = pr[desc].quantile(0.9)
            s = pr.where(pr >= thr) * (1 if lado == "Y" else -1)
            rp = evaluar(df, s.fillna(np.nan), 0, prueba & (pr >= thr))
            if rp:
                print(f"\nMODELO combinado (gradient boosting, entrenado SOLO en descubrimiento), comprar {'YES' if lado == 'Y' else 'NO'} "
                      f"en su decil superior: PRUEBA ev_res {rp['ev_res']:+.3f} n={rp['n']} mercados={rp['mercados']} "
                      f"rt30 {rp['ev_rt30']:+.3f} rt60 {rp['ev_rt60']:+.3f} | por moneda {rp['por_moneda']}")
    except Exception as e:
        print(f"modelo: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
