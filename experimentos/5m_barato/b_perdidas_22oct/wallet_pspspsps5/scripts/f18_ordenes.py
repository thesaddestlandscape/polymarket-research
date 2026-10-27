#!/usr/bin/env python3
"""f18: fills de W con order_hash, tx, bloque, contraparte (taker) y cantidades crudas, por dia -> ordenes_D.csv.gz (datalogs). Solo lectura."""
import sys, gzip
sys.path.insert(0, "/root/polymarket-research")
from pathlib import Path
import numpy as np, pandas as pd
from analisis_5m_barato_quien_gana import mapas, EXCH
from archivo_volumen import VOL
W = "0xb0f85baa97990910a3e8ac2b4a58a322f01ecef5"; OUT = Path("/root/polymarket-research-datalogs/wallet_pspspsps5")
for d in sys.argv[1:]:
    c = OUT / f"ordenes_{d}.csv.gz"
    if c.exists(): continue
    tok = mapas(d)["5min"]; parts = []
    with gzip.open(VOL / "m5_onchain" / f"m5_onchain_{d}.csv.gz", "rt") as fh:
        for x in pd.read_csv(fh, chunksize=400_000, dtype={"token_id": str, "maker": str, "taker": str, "tx": str, "order_hash": str}):
            x = x[(x.tipo == "F") & (x.maker.str.lower() == W) & x.token_id.isin(tok.keys())]
            if len(x): parts.append(x)
    X = pd.concat(parts, ignore_index=True)
    compra = X.side.values == 0
    X["acc"] = np.where(compra, X.taker_amt, X.maker_amt).astype(float); X["usdc"] = np.where(compra, X.maker_amt, X.taker_amt).astype(float)
    X["act"] = X.token_id.map(lambda t: tok[t][0]); X["mkt"] = X.token_id.map(lambda t: tok[t][1]); X["cierre"] = X.token_id.map(lambda t: tok[t][2]); X["lado"] = X.token_id.map(lambda t: tok[t][3])
    X["p"] = X.usdc / X.acc; X["T"] = X.cierre - X.ts_est.astype(float); X["cp"] = np.where(X.taker.str.lower() == EXCH, "EXCH", X.taker.str.lower())
    X[["ts_est", "bloque", "tx", "log_index", "order_hash", "cp", "side", "act", "mkt", "cierre", "lado", "acc", "usdc", "p", "T", "fee"]].to_csv(c, index=False, compression="gzip")
    print(d, len(X), flush=True)
