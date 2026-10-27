#!/usr/bin/env python3
"""f7: POBLACION. Rellenos pasivos de compra (maker, side 0) a p<0.10 en mercados 5m (todas las monedas), con la historia previa del
mismo token (max precio de operaciones en bloques ESTRICTAMENTE anteriores) -> poblacion_D.csv.gz en datalogs. Solo lectura on-chain."""
import sys, gzip
sys.path.insert(0, "/root/polymarket-research")
from pathlib import Path
import numpy as np, pandas as pd
from analisis_5m_barato_quien_gana import mapas, EXCH
from archivo_volumen import VOL
W = "0xb0f85baa97990910a3e8ac2b4a58a322f01ecef5"
OUT = Path("/root/polymarket-research-datalogs/wallet_pspspsps5")
for d in sys.argv[1:]:
    c = OUT / f"poblacion_{d}.csv.gz"
    if c.exists(): continue
    tok = mapas(d)["5min"]
    f = VOL / "m5_onchain" / f"m5_onchain_{d}.csv.gz"
    parts = []
    with gzip.open(f, "rt") as fh:
        for x in pd.read_csv(fh, chunksize=400_000, dtype={"token_id": str, "maker": str, "taker": str, "tx": str},
                             usecols=["tipo", "ts_est", "log_index", "maker", "taker", "side", "token_id", "maker_amt", "taker_amt"]):
            x = x[(x.tipo == "F") & x.token_id.isin(tok.keys())]
            if not len(x): continue
            compra = x.side.values == 0
            acc = np.where(compra, x.taker_amt.values, x.maker_amt.values).astype(float)
            usd = np.where(compra, x.maker_amt.values, x.taker_amt.values).astype(float)
            parts.append(pd.DataFrame({"tok": x.token_id.values, "ts": x.ts_est.astype(float).values, "li": x.log_index.values,
                "p": usd / np.maximum(acc, 1e-9), "acc": acc, "pasivo_compra": compra & (x.taker.values != EXCH),
                "esW": x.maker.str.lower().values == W}))
    X = pd.concat(parts, ignore_index=True)
    # historia: max de p por (tok, ts) -> cummax por token -> desplazado un bloque
    g = X.groupby(["tok", "ts"], sort=True).p.max().reset_index()
    g["pm"] = g.groupby("tok").p.cummax()
    g["pmax_prev"] = g.groupby("tok").pm.shift(1)
    g["n_prev"] = g.groupby("tok").cumcount()
    Y = X[X.pasivo_compra & (X.p < 0.10)].merge(g[["tok", "ts", "pmax_prev", "n_prev"]], on=["tok", "ts"], how="left")
    Y["act"] = Y.tok.map(lambda t: tok[t][0]); Y["mkt"] = Y.tok.map(lambda t: tok[t][1])
    Y["cierre"] = Y.tok.map(lambda t: tok[t][2]); Y["lado"] = Y.tok.map(lambda t: tok[t][3])
    Y["T"] = Y.cierre - Y.ts
    Y.drop(columns=["tok"]).to_csv(c, index=False, compression="gzip")
    print(d, len(X), len(Y), flush=True)
