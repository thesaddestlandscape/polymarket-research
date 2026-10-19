#!/usr/bin/env python3
"""extrae_fills.py -- misión 5m barato, wallets 18-Oct. Extrae de m5_onchain_D TODOS los fills de mercados 5m de las 6 monedas
(filas F; taker != contrato = relleno de una orden MAKER, columna `taker` = wallet de la orden TOMADORA; taker == contrato = resumen
de la orden tomadora con su fee, flag is_tk=1) a parquet compacto en el volumen. Solo lectura de on-chain; sin red.
Uso: nice -n 19 ionice -c3 python3 -I extrae_fills.py DIA [--max-chunks N]   (ulimit -v 1500000)
Salida: /mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/fills_D.parquet
"""
import sys, gzip, os
from datetime import date, datetime, timedelta
import numpy as np, pandas as pd, pyarrow as pa, pyarrow.parquet as pq
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"
CACHE = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/"
d = sys.argv[1]
maxch = int(sys.argv[sys.argv.index("--max-chunks") + 1]) if "--max-chunks" in sys.argv else 10**9
kdir = os.environ.get("KMAP_DIR", CACHE)
tok = {}
for k in (-1, 0, 1):
    dd = (date.fromisoformat(d) + timedelta(days=k)).isoformat()
    try:
        fh = open(kdir + f"kmap_{dd}.txt")
    except FileNotFoundError:
        print("falta kmap", dd, file=sys.stderr); continue
    for ln in fh:
        c = ln.rstrip("\n").split(",")
        if len(c) >= 8 and c[4] == "5min":
            tok[c[2]] = (c[3], int(c[5]), int(datetime.fromisoformat(c[6]).timestamp()), c[7])
print(d, "tokens 5m", len(tok), flush=True)
ta = {t: v[0] for t, v in tok.items()}; tm = {t: v[1] for t, v in tok.items()}
tf = {t: v[2] for t, v in tok.items()}; tl = {t: v[3] for t, v in tok.items()}
out = CACHE + f"fills_{d}.parquet"
w = None; n = 0; nk = 0
with gzip.open(f"/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz", "rt") as fh:
    for i, x in enumerate(pd.read_csv(fh, chunksize=150000, dtype={"token_id": str, "tx": str, "maker": str, "taker": str, "order_hash": str},
                                      usecols=["tipo", "bloque", "ts_est", "tx", "log_index", "maker", "taker", "side", "token_id", "maker_amt", "taker_amt", "fee"])):
        if i >= maxch: break
        x = x[(x.tipo == "F") & x.token_id.isin(tok.keys())]
        if not len(x): continue
        tk = x.token_id
        t = pd.DataFrame({
            "tx": x.tx.str[2:18].apply(lambda s: int(s, 16)).values.astype("int64"),
            "li": x.log_index.astype("int32").values, "bloque": x.bloque.astype("int32").values,
            "is_tk": (x.taker == EXCH).values.astype("int8"),
            "maker": x.maker.str.lower().values, "taker": x.taker.str.lower().values,
            "side": x.side.astype("int8").values, "tok": tk.values,
            "act": tk.map(ta).values, "mkt": tk.map(tm).values.astype("int32"), "lado": tk.map(tl).values,
            "fin": tk.map(tf).values.astype("int64"), "ts": x.ts_est.astype("float64").values,
            "maker_amt": x.maker_amt.astype("float64").values, "taker_amt": x.taker_amt.astype("float64").values,
            "fee": x.fee.astype("float64").values})
        tb = pa.Table.from_pandas(t, preserve_index=False)
        if w is None: w = pq.ParquetWriter(out, tb.schema, compression="zstd")
        w.write_table(tb); n += len(t); nk += int(t.is_tk.sum())
if w: w.close()
print(d, "filas", n, "resumenes tomador", nk, "->", out)
