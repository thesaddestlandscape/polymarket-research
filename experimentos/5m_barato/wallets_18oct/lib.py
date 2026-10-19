"""lib.py -- utilidades comunes (misión 5m barato, wallets 18-Oct). Solo lectura. Fee cripto 0,07·p(1-p) por acción (tomador)."""
import json
import numpy as np, pandas as pd
CACHE = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/"
FEE = 0.07
DES = json.load(open("/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json"))   # mkt(gamma id, str) -> 'YES'/'NO'
CELDA = dict(pc_lo=0.10, pc_hi=0.30, T_lo=60.0, T_hi=300.0)   # H5M: pc (0,10-0,30], T (60-300] s


def deriva(F):
    """F: filas is_tk==0 (relleno de una orden MAKER). Devuelve columnas en la óptica del MAKER (adquiere lado_c a pc)."""
    venta = F.side.values == 1
    sh = np.where(venta, F.maker_amt.values, F.taker_amt.values)
    usd = np.where(venta, F.taker_amt.values, F.maker_amt.values)
    X = F.copy()
    X["venta"] = venta
    X["sh"] = sh
    X["lado_c"] = np.where(venta, np.where(X.lado == "YES", "NO", "YES"), X.lado)
    X["pc"] = np.where(venta, 1 - usd / sh, usd / sh)
    X["coste_m"] = np.where(venta, sh - usd, usd)
    X["T"] = X.fin.values.astype(float) - X.ts.values
    return X[(X.sh > 0) & (X.coste_m > 0)]


def en_celda(X):
    return X[(X.pc > CELDA["pc_lo"]) & (X.pc <= CELDA["pc_hi"]) & (X["T"] > CELDA["T_lo"]) & (X["T"] <= CELDA["T_hi"])]


def con_resultado(X):
    """añade des, pnl_m, pnl_t (tomador: contraparte, con su fee), coste_t (todo incluido). Sin desenlace -> se descarta y se informa."""
    des = X.mkt.astype(str).map(DES)
    cob = des.notna().mean() if len(X) else float("nan")
    X = X[des.notna().values].copy()
    X["des"] = des[des.notna()].values
    gana_c = (X.lado_c.values == X.des.values)
    X["pnl_m"] = np.where(gana_c, X.sh, 0.0) - X.coste_m
    fee_t = FEE * X.sh * X.pc * (1 - X.pc)
    X["fee_t"] = fee_t
    X["coste_t"] = X.sh * (1 - X.pc) + fee_t
    X["pnl_t"] = np.where(~gana_c, X.sh, 0.0) - X.sh * (1 - X.pc) - fee_t
    return X, cob


def boot_ic(v, n=10000, seed=1, q=(0.05, 0.95)):
    v = np.asarray(v, float)
    r = np.random.default_rng(seed)
    m = v[r.integers(0, len(v), (n, len(v)))].mean(1)
    return tuple(np.quantile(m, q).round(4))


def ev_pond_ic(df, clave, num="pnl_m", den="coste_m", n=5000, seed=1):
    """EV ponderado por € = Σnum/Σden con IC90 bootstrap por clúster `clave` (p. ej. cierre o día)."""
    g = df.groupby(clave)[[num, den]].sum()
    a, b = g[num].values, g[den].values
    r = np.random.default_rng(seed)
    i = r.integers(0, len(g), (n, len(g)))
    e = a[i].sum(1) / b[i].sum(1)
    return a.sum() / b.sum(), tuple(np.quantile(e, [0.05, 0.95]).round(4)), len(g)
