#!/usr/bin/env python3
"""analisis_15m_ronda3_mes.py -- misión "15m como activo autónomo", RONDA 3 (07-Oct, Javi: opción (b) "completar lo que
no hicimos: secuencias, regímenes y efectos de segundo orden"). Catálogo informes/m15_hipotesis_catalogo_06oct.md:
M4 #30-31, M12 #98, M14 #102-103, M15 #106, M16 #107 + secuencias entre mercados consecutivos.

PROTOCOLO: el MISMO de la ronda 2 (analisis_15m_mineria_mes.py, se reutiliza su main() tal cual: DESC 16-28 Sep,
embargo 29, PRUEBA 30-Sep..05-Oct, umbral P90 de DESC, 1 op por mercado-minuto, cotas OPT/PES, 200 permutaciones dentro
de día x minuto x tramo de mid, max-stat, IC90 por días, sin 2 mejores días, LOMO >=4/6, concentración <=60 %). Solo
cambia el catálogo de señales. Fijado ANTES de mirar resultados.
  - Todo rasgo es CAUSAL: solo fotos anteriores del mismo mercado o mercados ya CERRADOS (cierre <= t - 5 s).
  - Los umbrales de régimen salen SOLO de DESC (cuantiles por moneda donde aplica).
  - NO se usan flujo_*/ntr_* (firehose = 2 filas por casación, tomador sin identificar: trampa 06-Oct).
Segundo orden: además de la versión operable (lado barato con vol prevista alta / favorito con vol baja), un informe
descriptivo: correlación de Spearman, en PRUEBA y por día, de cada rasgo con |movimiento del bid a +60/+300 s| y con el
spread actual -> ¿se anticipa la volatilidad / la liquidez del 15m? (sirve para el maker, no es alpha de tomador).
Uso: (ulimit -v 3500000; nice -n 10 python3 analisis_15m_ronda3_mes.py [--perms 200]) > informes/m15_ronda3_mes_07oct.txt
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import analisis_15m_mineria_mes as M  # noqa: E402

DESC, PRUEBA = M.DESC, M.PRUEBA


def _rasgos(df):
    """Rasgos causales añadidos al dataset del mes (df ordenado por market, t)."""
    g = df.groupby("market", sort=False)
    df["vel1_prev"] = g["vel1"].shift(1)
    df["vel1_prev2"] = g["vel1"].shift(2)
    df["runmax"] = g["mid"].transform(lambda s: s.shift(1).cummax())
    df["runmin"] = g["mid"].transform(lambda s: s.shift(1).cummin())
    df["mid0"] = g["mid"].transform("first")
    df["camino"] = g["vel1"].transform(lambda s: s.abs().fillna(0).cumsum())
    df["eficiencia"] = (df["mid"] - df["mid0"]).abs() / df["camino"].replace(0, np.nan)   # 1 = tendencia limpia
    df["cl_prev"] = g["cl_ret_60s_bps"].shift(1)
    # mercados anteriores de la misma moneda (cierre <= inicio de este): desenlace conocido
    mk = df.drop_duplicates("market")[["market", "moneda", "cierre", "desenlace"]].sort_values(["moneda", "cierre"])
    mk["y"] = np.where(mk["desenlace"] == "YES", 1.0, -1.0)
    mk["prev1"] = mk.groupby("moneda")["y"].shift(1)
    mk["prev2"] = mk.groupby("moneda")["y"].shift(2)
    mk["cierre_prev"] = mk.groupby("moneda")["cierre"].shift(1)
    df = df.merge(mk[["market", "prev1", "prev2", "cierre_prev"]], on="market", how="left")
    ok = df["t"] / 1000 >= df["cierre_prev"] + 5
    df.loc[~ok, ["prev1", "prev2"]] = np.nan
    # dirección de la última hora (todas las monedas): fracción YES de los mercados cerrados en (t-3600, t-5]
    cz = mk.sort_values("cierre")
    c_t, c_y = cz["cierre"].values.astype(float), (cz["y"].values > 0).astype(float)
    cum = np.concatenate([[0.0], np.cumsum(c_y)])
    ts = df["t"].values / 1000
    hi = np.searchsorted(c_t, ts - 5, side="right")
    lo = np.searchsorted(c_t, ts - 3600, side="right")
    n = hi - lo
    df["dir_hora"] = np.where(n >= 12, (cum[hi] - cum[lo]) / np.maximum(n, 1), np.nan)
    return df.sort_values(["market", "t"]).reset_index(drop=True)


def hipotesis(df):
    dia = df["dia"].values
    desc = (dia >= DESC[0]) & (dia <= DESC[1])
    g = lambda c: df[c].astype(float)
    sgn = lambda x: np.sign(x).replace(0, np.nan)
    H = {}
    v1, vp, vp2 = g("vel1"), g("vel1_prev"), g("vel1_prev2")
    # ---- M4/M15 secuencias dentro del mercado
    r2 = (sgn(v1) == sgn(vp))
    r3 = r2 & (sgn(vp) == sgn(vp2))
    H["sec.racha2_continua"] = sgn(v1).where(r2)
    H["sec.racha2_revierte"] = -sgn(v1).where(r2)
    H["sec.racha3_continua"] = sgn(v1).where(r3)
    H["sec.racha3_revierte"] = -sgn(v1).where(r3)
    H["sec.giro_continua"] = sgn(v1).where(sgn(v1) == -sgn(vp))           # tras un giro, ¿sigue el nuevo sentido?
    nuevo_max = (g("mid") > g("runmax")) & g("runmax").notna()
    nuevo_min = (g("mid") < g("runmin")) & g("runmin").notna()
    rup = pd.Series(np.where(nuevo_max, 1.0, np.where(nuevo_min, -1.0, np.nan)), index=df.index)
    H["sec.ruptura_continua"], H["sec.ruptura_revierte"] = rup, -rup
    rango = (g("runmax") - g("runmin")).where(lambda x: x >= 0.05)
    pos = (g("mid") - g("runmin")) / rango - 0.5
    H["sec.posicion_rango_impulso"], H["sec.posicion_rango_reversion"] = pos, -pos
    # M15 #106: 5m se mueve -> 15m se mueve igual -> ¿continuación?
    m5 = g("m5_vel")
    H["sec.m5_y_15_continua"] = sgn(v1).where(sgn(m5) == sgn(v1))
    H["sec.m5_y_15_revierte"] = -sgn(v1).where(sgn(m5) == sgn(v1))
    H["sec.m5_mueve_15_quieto"] = sgn(m5).where((v1 == 0) & (m5.abs() >= 0.02))
    # Chainlink se movió en la foto anterior y el libro lo siguió en esta -> ¿continúa?
    H["sec.cl_luego_libro_continua"] = sgn(v1).where(sgn(g("cl_prev")) == sgn(v1))
    # ---- secuencias entre mercados consecutivos de la misma moneda
    H["sec.mercado_previo_continua"], H["sec.mercado_previo_revierte"] = g("prev1"), -g("prev1")
    dos = g("prev1").where(g("prev1") == g("prev2"))
    H["sec.dos_previos_continua"], H["sec.dos_previos_revierte"] = dos, -dos
    # ---- M16/M12 regímenes (umbrales SOLO de DESC)
    dh = g("dir_hora")
    dir_h = pd.Series(np.where(dh >= 0.6, 1.0, np.where(dh <= 0.4, -1.0, np.nan)), index=df.index)
    H["reg.dir_hora_continua"], H["reg.dir_hora_revierte"] = dir_h, -dir_h
    sig = g("sigma_bps_s")
    q_sig = df[desc].groupby("moneda")["sigma_bps_s"].quantile([1 / 3, 2 / 3]).unstack()
    sig_lo = df["moneda"].map(q_sig[1 / 3]); sig_hi = df["moneda"].map(q_sig[2 / 3])
    spr_p75 = np.nanquantile(df.loc[desc, "spread_y"], 0.75)
    efi_med = np.nanmedian(df.loc[desc, "eficiencia"])
    reg = {"volalta": sig >= sig_hi, "volbaja": sig <= sig_lo,
           "iliquido": g("spread_y") >= max(spr_p75, 0.02), "liquido": g("spread_y") < max(spr_p75, 0.02),
           "tendencia": g("eficiencia") >= efi_med, "rango": g("eficiencia") < efi_med,
           "terminal": g("t_hasta_cierre_s") < 180, "temprano": g("t_desde_inicio_s") < 300,
           "dia_yes": dh >= 0.6, "dia_no": dh <= 0.4}
    base = {"impulso": v1, "reversion": -v1, "fv": g("fv_yes") - g("mid"), "fv_inv": -(g("fv_yes") - g("mid")),
            "m5_adelanto": m5 - v1, "previo": g("prev1"), "previo_inv": -g("prev1")}
    for rn, rm in reg.items():
        for bn, bs in base.items():
            H[f"reg.{bn}@{rn}"] = bs.where(rm.fillna(False))
    # M12 #98 shocks: |Chainlink 30 s| > P99 de DESC por moneda
    q99 = df[desc].assign(a=df["cl_ret_30s_bps"].abs()).groupby("moneda")["a"].quantile(0.99)
    shock = g("cl_ret_30s_bps").abs() >= df["moneda"].map(q99)
    H["reg.shock_cl_continua"] = sgn(g("cl_ret_30s_bps")).where(shock)
    H["reg.shock_cl_revierte"] = -sgn(g("cl_ret_30s_bps")).where(shock)
    # ---- M14 segundo orden operable: vol prevista alta -> lado barato (convexidad); baja -> favorito
    lado_barato = pd.Series(np.where(g("mid") < 0.5, 1.0, -1.0), index=df.index)
    fuera_centro = (g("mid") - 0.5).abs() >= 0.15
    for xn, x in {"abs_cl30": g("cl_ret_30s_bps").abs(), "abs_vel1": v1.abs(), "abs_m5": m5.abs(),
                  "sigma": sig, "spread": g("spread_y")}.items():
        xd = x[desc & fuera_centro.values]
        p90, p10 = np.nanquantile(xd, 0.9), np.nanquantile(xd, 0.1)
        H[f"seg.{xn}_alta_barato"] = lado_barato.where(fuera_centro & (x >= p90))
        H[f"seg.{xn}_baja_favorito"] = (-lado_barato).where(fuera_centro & (x <= p10))
    return {k: pd.Series(v, index=df.index).astype(float) for k, v in H.items()}


def segundo_orden_descriptivo(df):
    """¿Algún rasgo anticipa la volatilidad o la liquidez futura del 15m? Spearman en PRUEBA, por día."""
    dia = df["dia"].values
    pr = (dia >= PRUEBA[0]) & (dia <= PRUEBA[1])
    d = df[pr].copy()
    d["mov60"] = (d["bid_y_60"] - d["bid_y"]).abs()
    d["mov300"] = (d["bid_y_300"] - d["bid_y"]).abs()
    d["spread_fut"] = (d.groupby("market")["spread_y"].shift(-1))
    X = {"|cl_ret_30s|": d["cl_ret_30s_bps"].abs(), "|cl_ret_300s|": d["cl_ret_300s_bps"].abs(),
         "sigma_bps_s": d["sigma_bps_s"], "|vel1|": d["vel1"].abs(), "|m5_vel|": d["m5_vel"].abs(),
         "spread_y": d["spread_y"], "|mid-0,5| (inv)": -(d["mid"] - 0.5).abs(), "cl_edad_ms": d["cl_edad_ms"],
         "t_hasta_cierre (inv)": -d["t_hasta_cierre_s"]}
    print("\n=== SEGUNDO ORDEN (descriptivo, PRUEBA): Spearman por día, estratificado por tramo de |mid-0,5| (media y días con el mismo signo) ===")
    print(f"{'rasgo':24} | {'|mov bid 60 s|':>18} | {'|mov bid 300 s|':>18} | {'spread foto siguiente':>22}")
    for xn, x in X.items():
        celdas = []
        for yn in ("mov60", "mov300", "spread_fut"):
            rs = []
            # ESTRATIFICADO por tramo de |mid-0,5| (0,1): cerca de 0,5 todo se mueve más (delta binaria) y eso
            # contamina cualquier rasgo correlado con el nivel de precio; media ponderada de Spearman por tramo
            tramo = np.minimum((d["mid"] - 0.5).abs() // 0.1, 4) if "inv)" not in xn or "mid" not in xn else 0
            for _, dd in d.assign(_x=x, _tr=tramo).groupby("dia"):
                num, den = 0.0, 0
                for _, de in dd.groupby("_tr"):
                    ok = de["_x"].notna() & de[yn].notna()
                    if ok.sum() > 100 and de.loc[ok, "_x"].nunique() > 1:
                        num += ok.sum() * de.loc[ok, "_x"].rank().corr(de.loc[ok, yn].rank()); den += ok.sum()
                if den:
                    rs.append(num / den)
            rs = np.array(rs)
            celdas.append(f"{np.mean(rs):+.3f} ({(np.sign(rs) == np.sign(np.mean(rs))).sum()}/{len(rs)})" if len(rs) else "-")
        print(f"{xn:24} | {celdas[0]:>18} | {celdas[1]:>18} | {celdas[2]:>22}")


_cargar_orig = M.cargar


def _cargar(d):
    df = _rasgos(_cargar_orig(d))
    segundo_orden_descriptivo(df)
    return df


if __name__ == "__main__":
    M.cargar = _cargar
    M.hipotesis = hipotesis
    M.EQUIV_MS = {}
    M.RONDA1 = Path("/nonexistent")
    M.main()
