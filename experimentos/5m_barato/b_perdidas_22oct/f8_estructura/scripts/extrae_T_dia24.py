"""F8: extrae las ordenes TOMADORAS (taker==EXCH) de m5_onchain del 24-Oct con la MISMA logica que f6 e1_extrae.py (solo T; 05-23 se leen de agentes_datos/f6)."""
import sys, gzip
sys.path.insert(0, "/root/polymarket-research")
import numpy as np, pandas as pd
from analisis_5m_barato_quien_gana import mapas, EXCH
from archivo_volumen import VOL
d = sys.argv[1]; OUT = "/root/polymarket-research-datalogs/f8_estructura/T_%s.parquet" % d
tk = mapas(d)["5min"]
act = {t: v[0] for t, v in tk.items()}; mk = {t: v[1] for t, v in tk.items()}; ci = {t: v[2] for t, v in tk.items()}; la = {t: v[3] for t, v in tk.items()}
T = []
with gzip.open(VOL / "m5_onchain" / f"m5_onchain_{d}.csv.gz", "rt") as fh:
    for x in pd.read_csv(fh, chunksize=300_000, dtype={"token_id": str, "maker": str, "taker": str, "tx": str},
                         usecols=["tipo", "ts_est", "tx", "maker", "taker", "side", "token_id", "maker_amt", "taker_amt", "fee"]):
        x = x[(x.tipo == "F") & x.token_id.isin(tk.keys())]
        if not len(x): continue
        ist = (x.taker == EXCH).values; buy = (x.side.values == 0)
        acc = np.where(buy, x.taker_amt.values, x.maker_amt.values).astype(float); usd = np.where(buy, x.maker_amt.values, x.taker_amt.values).astype(float)
        base = pd.DataFrame({"ts": x.ts_est.astype(float).values, "tx": x.tx.values, "tok": x.token_id.values, "act": x.token_id.map(act).values, "mkt": x.token_id.map(mk).values,
                             "cierre": x.token_id.map(ci).values, "lado": x.token_id.map(la).values, "buy": buy, "acc": acc, "usd": usd, "p": usd / np.maximum(acc, 1e-9), "fee": x.fee.astype(float).values})
        t = base[ist].copy(); t["w"] = x.maker.str.lower().values[ist]; T.append(t)
T = pd.concat(T, ignore_index=True)
for c in ("act", "lado", "tok", "w"): T[c] = T[c].astype("category")
T.to_parquet(OUT); print(d, "taker rows", len(T))
