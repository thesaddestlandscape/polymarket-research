"""F6 e1: extrae por dia (5m, todas las monedas) (a) ordenes TOMADORAS (taker==EXCH: maker=wallet del tomador) y (b) rellenos maker-compra (side 0, taker!=EXCH) con p<0.45.
Solo lectura de m5_onchain; salida parquet en agentes_datos/f6. Sin calculo de EV."""
import sys, gzip
sys.path.insert(0, "/root/polymarket-research")
import numpy as np, pandas as pd
from analisis_5m_barato_quien_gana import mapas, EXCH
from archivo_volumen import VOL
OUT = VOL / "agentes_datos" / "b_sin_flujo"
dias = sys.argv[1:] or ["2026-10-%02d" % d for d in range(24, 25)]
for d in dias:
    tok = mapas(d)["5min"]
    tk = {k: v for k, v in tok.items()}
    cod = {t: i for i, t in enumerate(tk)}
    act = {t: v[0] for t, v in tk.items()}; mk = {t: v[1] for t, v in tk.items()}; ci = {t: v[2] for t, v in tk.items()}; la = {t: v[3] for t, v in tk.items()}
    T, M = [], []
    with gzip.open(VOL / "m5_onchain" / f"m5_onchain_{d}.csv.gz", "rt") as fh:
        for x in pd.read_csv(fh, chunksize=300_000, dtype={"token_id": str, "maker": str, "taker": str, "tx": str},
                             usecols=["tipo", "ts_est", "tx", "maker", "taker", "side", "token_id", "maker_amt", "taker_amt", "fee"]):
            x = x[(x.tipo == "F") & x.token_id.isin(tk.keys())]
            if not len(x): continue
            ist = (x.taker == EXCH).values
            buy = (x.side.values == 0)
            acc = np.where(buy, x.taker_amt.values, x.maker_amt.values).astype(float)
            usd = np.where(buy, x.maker_amt.values, x.taker_amt.values).astype(float)
            p = usd / np.maximum(acc, 1e-9)
            base = pd.DataFrame({"ts": x.ts_est.astype(float).values, "tx": x.tx.values, "tok": x.token_id.values, "act": x.token_id.map(act).values, "mkt": x.token_id.map(mk).values,
                                 "cierre": x.token_id.map(ci).values, "lado": x.token_id.map(la).values, "buy": buy, "acc": acc, "usd": usd, "p": p, "fee": x.fee.astype(float).values})
            t = base[ist].copy(); t["w"] = x.maker.str.lower().values[ist]; T.append(t)
            sel = (~ist) & buy & (p < 0.45)
            m = base[sel].copy(); m["maker"] = x.maker.str.lower().values[sel]; m["taker"] = x.taker.str.lower().values[sel]; M.append(m)
    T = pd.concat(T, ignore_index=True); M = pd.concat(M, ignore_index=True)
    for c in ("act", "lado", "tok"): T[c] = T[c].astype("category"); M[c] = M[c].astype("category")
    T["w"] = T.w.astype("category"); M["maker"] = M.maker.astype("category"); M["taker"] = M.taker.astype("category")
    T.to_parquet(OUT / f"T_{d}.parquet"); M.to_parquet(OUT / f"M_{d}.parquet")
    print(d, "taker rows", len(T), "maker-buy p<.45", len(M), flush=True)
