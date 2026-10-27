#!/usr/bin/env python3
"""p1: rellenos MAKER de compra a p>=0,60 en 5m (6 monedas), TODA la población, por día D (m5_onchain). Profundidad proxy en la
barrida: ticks = (precio máximo de los makers compradores del MISMO token en la MISMA tx − p)/0,01 (una toma vendedora empieza en
el mejor bid; MINT del complementario también barre desde el mejor). Guarda order_hash, maker (W/MM/otro + hash corto), acc, T.
Idempotente por día; espera load5<8 y MemAvailable>2,5 GB, fuera de 06-09:30Z. Solo lectura."""
import sys, glob, gzip, os, time
import numpy as np, pandas as pd
D = "/root/polymarket-research-datalogs/wallet_mecanismos_26oct"; V = "/mnt/HC_Volume_106538179/m5_onchain"
EX = "0xe111180000d2663c0091e4f400237545b87b996b"
W = "0xb0f85baa97990910a3e8ac2b4a58a322f01ecef5"; MM = "0x32ed2e546b187ca15e2841edc82b22c713cf8ec3"
def espera():
    while True:
        h = time.gmtime().tm_hour * 100 + time.gmtime().tm_min
        l5 = float(open("/proc/loadavg").read().split()[1])
        m = int([x for x in open("/proc/meminfo") if x.startswith("MemAvailable")][0].split()[1])
        if not (600 <= h < 930) and l5 < 8 and m > 2_600_000: return
        time.sleep(60)
def tokmap(d):
    tok = {}
    for k in (-1, 0, 1):
        dd = (pd.Timestamp(d) + pd.Timedelta(days=k)).strftime("%Y-%m-%d")
        f = f"{D}/k_m5_registro_{dd}.csv"
        if os.path.exists(f):
            for ln in open(f):
                c = ln.rstrip("\n").split(",")
                if len(c) >= 8 and c[4] == "5min": tok[c[2]] = (c[3], c[5], int(pd.Timestamp(c[6]).timestamp()), c[7])
    return tok
for d in sys.argv[1:]:
    out = f"{D}/fav_{d}.csv.gz"
    if os.path.exists(out): continue
    espera(); tok = tokmap(d); P = []
    with gzip.open(f"{V}/m5_onchain_{d}.csv.gz", "rt") as fh:
        for x in pd.read_csv(fh, chunksize=400_000, dtype={"token_id": str, "maker": str, "taker": str, "tx": str, "order_hash": str},
                             usecols=["tipo", "ts_est", "tx", "order_hash", "maker", "taker", "side", "token_id", "maker_amt", "taker_amt"]):
            x = x[(x.tipo == "F") & (x.side == 0) & (x.taker.str.lower() != EX)]
            x = x[x.token_id.isin(tok.keys())]
            p = x.maker_amt.values / x.taker_amt.values
            x = x.assign(p=p)[p >= 0.60]
            P.append(x[["ts_est", "tx", "order_hash", "maker", "token_id", "taker_amt", "maker_amt", "p"]])
    X = pd.concat(P, ignore_index=True)
    X["pmax"] = X.groupby(["tx", "token_id"]).p.transform("max")
    X["ticks"] = np.round((X.pmax - X.p) / 0.01).astype(int)
    v = X.token_id.map(tok)
    X["act"] = [t[0] for t in v]; X["mkt"] = [t[1] for t in v]; X["cierre"] = [t[2] for t in v]; X["lado"] = [t[3] for t in v]
    mk = X.maker.str.lower(); X["quien"] = np.where(mk == W, "W", np.where(mk == MM, "MM", "otro"))
    X["mk"] = mk.str[2:10]; X["oh"] = X.order_hash.str[2:14]
    X = X.rename(columns={"taker_amt": "acc", "maker_amt": "usd", "ts_est": "ts"})
    X[["ts", "tx", "oh", "mk", "quien", "act", "mkt", "cierre", "lado", "p", "acc", "usd", "ticks"]].to_csv(out, index=False, compression="gzip")
    print(d, len(X), (X.quien == "W").sum(), (X.quien == "MM").sum(), time.strftime("%H:%M", time.gmtime()), flush=True)
