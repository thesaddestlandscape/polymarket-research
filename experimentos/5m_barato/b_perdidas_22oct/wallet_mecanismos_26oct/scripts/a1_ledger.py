#!/usr/bin/env python3
"""a1: ledger on-chain 5m de W (pspspsps5) y MM (mo-money) desde tx_D (x1), con tipo de contraparte por relleno maker:
VENTA (el tomador vende el MISMO token) / MINT (el tomador COMPRA el token complementario) / otro. Desenlace oficial."""
import sys, glob, os
sys.path.insert(0, "/root/polymarket-research")
import numpy as np, pandas as pd
from analisis_maker_cancelacion_binance import desenlaces
D = "/root/polymarket-research-datalogs/wallet_mecanismos_26oct"
EX = "0xe111180000d2663c0091e4f400237545b87b996b"
WAL = {"W": "0xb0f85baa97990910a3e8ac2b4a58a322f01ecef5", "MM": "0x32ed2e546b187ca15e2841edc82b22c713cf8ec3"}
tok = {}
for f in sorted(glob.glob(f"{D}/k_m*_registro_*.csv")):
    for ln in open(f):
        c = ln.rstrip("\n").split(",")
        if len(c) >= 8 and c[4] == "5min":
            tok[c[2]] = (c[3], c[5], int(pd.Timestamp(c[6]).timestamp()), c[7])
comp = {}
bym = {}
for t, v in tok.items(): bym.setdefault(v[1], {})[v[3]] = t
for m, dd in bym.items():
    if "YES" in dd and "NO" in dd: comp[dd["YES"]] = dd["NO"]; comp[dd["NO"]] = dd["YES"]
out = []
for f in sorted(glob.glob(f"{D}/tx_*.csv.gz")):
    x = pd.read_csv(f, dtype={"token_id": str, "maker": str, "taker": str, "tx": str, "order_hash": str})
    x = x[x.tipo == "F"]; x["maker"] = x.maker.str.lower(); x["taker"] = x.taker.str.lower()
    tk = x[x.taker == EX].set_index(["tx", "maker"])[["side", "token_id"]]
    tk = tk[~tk.index.duplicated()]
    for nom, a in WAL.items():
        y = x[(x.maker == a) & x.token_id.isin(tok.keys())].copy()
        if not len(y): continue
        y["wal"] = nom; y["rol"] = np.where(y.taker == EX, "T", "M")
        y["compra"] = y.side == 0
        y["acc"] = np.where(y.compra, y.taker_amt, y.maker_amt).astype(float)
        y["usd"] = np.where(y.compra, y.maker_amt, y.taker_amt).astype(float)
        cpk = list(zip(y.tx, y.taker)); j = tk.reindex(cpk)
        y["cp_side"] = j.side.values; y["cp_tok"] = j.token_id.values
        same = y.cp_tok.values == y.token_id.values
        compl = np.array([comp.get(a1) == b1 for a1, b1 in zip(y.token_id, y.cp_tok)])
        y["cpt"] = np.where(y.rol == "T", "-", np.where(same & (y.cp_side != y.side), "CRUCE", np.where(compl & (y.cp_side == y.side), "MINT_MERGE", "otro")))
        v = y.token_id.map(tok)
        y["act"] = [t[0] for t in v]; y["mkt"] = [t[1] for t in v]; y["cierre"] = [t[2] for t in v]; y["lado"] = [t[3] for t in v]
        out.append(y[["wal", "ts_est", "bloque", "tx", "log_index", "order_hash", "taker", "rol", "compra", "acc", "usd", "fee", "cpt", "act", "mkt", "cierre", "lado"]])
    print(f, flush=True)
R = pd.concat(out, ignore_index=True)
R["p"] = R.usd / R.acc; R["T"] = R.cierre - R.ts_est
des = desenlaces(set(R.mkt.astype(str))); R["des"] = R.mkt.astype(str).map(des)
print("cobertura desenlace", round(R.des.notna().mean(), 4), "filas", len(R))
R["win"] = (R.lado == R.des).astype(float)
R["pnl"] = np.where(R.compra, R.win * R.acc - R.usd, R.usd - R.win * R.acc) - R.fee
R["dc"] = pd.to_datetime(R.cierre, unit="s").dt.strftime("%m-%d")
R.to_csv(f"{D}/ledger.csv.gz", index=False, compression="gzip")
print(R.groupby(["wal", "rol", "cpt"]).agg(n=("usd", "size"), usd=("usd", "sum"), pnl=("pnl", "sum")))
