#!/usr/bin/env python3
"""f14: estructura de las posiciones de W (mercado+lado): escalones, distancias, tamanos, tiempos; sesgo de lado."""
import numpy as np, pandas as pd
R = pd.read_csv("/root/polymarket-research-datalogs/wallet_pspspsps5/fills.csv.gz", dtype={"mkt": str}).sort_values(["mkt", "lado", "ts", "li"])
g = R.groupby(["mkt", "lado"], sort=False)
R["k"] = g.cumcount(); R["nf"] = g.p.transform("size"); R["p_prev"] = g.p.shift(1); R["ts_prev"] = g.ts.shift(1); R["acc_cum"] = g.acc.cumsum() - R.acc
R["dp"] = R.p - R.p_prev; R["dt"] = R.ts - R.ts_prev
print("fills", len(R), "unidades", g.ngroups, "nf mediana %d p75 %d p90 %d max %d" % (R.nf.median(), R.nf.quantile(.75), R.nf.quantile(.9), R.nf.max()))
U = g.agg(n=("p", "size"), p0=("p", "first"), pmin=("p", "min"), pmax=("p", "max"), T0=("T", "max"), acc=("acc", "sum"), usd=("usdc", "sum"), win=("win", "first"), act=("act", "first")).reset_index()
print("primer fill: precio mediana %.3f ; p<0.10 %.1f%% ; 0.10-0.40 %.1f%% ; 0.40-0.90 %.1f%% ; >=0.90 %.1f%%" % (U.p0.median(), *(100 * ((U.p0 >= lo) & (U.p0 < hi)).mean() for lo, hi in ((0, .1), (.1, .4), (.4, .9), (.9, 1.1)))))
print("T primer fill: p10 %.0f p50 %.0f p90 %.0f" % tuple(U.T0.quantile([.1, .5, .9])))
print("lado: YES(Up) %.1f%% de unidades; por moneda:" % (100 * (U.lado == "YES").mean()), U.groupby("act").apply(lambda x: round(100 * (x.lado == "YES").mean(), 1)).to_dict())
# escalones: pasos en precio dentro de unidad (fills sucesivos, solo cuando precio cambia)
S = R[R.k > 0]
print("\npaso de precio entre fills sucesivos (misma unidad): mediana %.3f ; baja %.1f%% sube %.1f%% igual %.1f%% ; dt mediana %.1f s p90 %.0f s" % (S.dp.median(), 100 * (S.dp < -1e-9).mean(), 100 * (S.dp > 1e-9).mean(), 100 * (S.dp.abs() <= 1e-9).mean(), S.dt.median(), S.dt.quantile(.9)))
# razon de precio sucesivo cuando baja
dn = S[S.dp < -1e-9]; print("cuando baja: razon p/p_prev mediana %.2f p25 %.2f p75 %.2f ; paso abs mediana %.3f" % ((dn.p / dn.p_prev).median(), (dn.p / dn.p_prev).quantile(.25), (dn.p / dn.p_prev).quantile(.75), (-dn.dp).median()))
# precios: niveles redondos
rp = R.p.round(2); lv = rp.value_counts().head(12); print("niveles mas frecuentes (redondeo 0.01):", {float(k): int(v) for k, v in lv.items()})
print("fraccion de fills <0.10 en precio exacto multiplo de 0.01: %.1f%%" % (100 * (np.abs(R[R.p < .1].p * 100 - np.round(R[R.p < .1].p * 100)) < 1e-6).mean()))
# tamanos
for lo, hi in ((0, .03), (.03, .06), (.06, .1), (.1, .2), (.2, .4), (.4, .6), (.6, .9), (.9, 1.1)):
    s = R[(R.p >= lo) & (R.p < hi)]; print("  p[%.2f,%.2f): fills %5d acc mediana %6.1f usd mediana %6.2f media %6.2f" % (lo, hi, len(s), s.acc.median(), s.usdc.median(), s.usdc.mean()))
# repetido: mismo precio varias veces? (reposicion)
print("fills con mismo precio que el previo: %.1f%%" % (100 * (S.dp.abs() <= 1e-9).mean()))
# bajo en escalera: razon tamano $ del fill bajo / alto previo

# distribucion de precios del primer fill cuando unidad tiene fill <0.10
E1 = U[U.pmin < .1]; print("\nunidades con algun fill <0.10: %d ; primer fill >=0.10: %.1f%% ; precio primer fill mediana %.3f ; pmax mediana %.3f" % (len(E1), 100 * (E1.p0 >= .1).mean(), E1.p0.median(), E1.pmax.median()))
print("de ellas con >=3 fills: %.1f%%; hit %.2f%%" % (100 * (E1.n >= 3).mean(), 100 * E1.win.mean()))
# participacion por dia: mercados con fills W / mercados 5m posibles de sus 3 monedas
M = R.groupby("mkt").agg(act=("act", "first"), dia=("dia_cierre", "first")); print("mercados/dia por moneda:", (M.groupby(["dia", "act"]).size().unstack().mean()).round(0).to_dict(), "de 288 posibles")
print("hora UTC de cierre (distribucion de coste %):"); R["h"] = pd.to_datetime(R.cierre, unit="s").dt.hour; print((R.groupby("h").c.sum() / R.c.sum() * 100 if "c" in R else R.groupby("h").usdc.sum() / R.usdc.sum() * 100).round(1).to_dict())
