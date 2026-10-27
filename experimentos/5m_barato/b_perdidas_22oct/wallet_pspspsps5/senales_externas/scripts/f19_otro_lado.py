#!/usr/bin/env python3
"""f19: precio del OTRO lado. Para cada fill de ext_D: ultimo precio operado (cualquier fill on-chain, bloque estrictamente anterior) del token opuesto
(opp_last) y del propio (own_last, distinto del propio fill), y edad. gap = (1-opp_last) - p : cuanto mas barato esta el lado propio que lo implicado por el otro.
Salida lado_D.csv.gz (ts, li, mkt, lado, opp_last, opp_age, opp_n30, own_last_prev)."""
import sys, gzip
sys.path.insert(0, "/root/polymarket-research")
from pathlib import Path
import numpy as np, pandas as pd
from analisis_5m_barato_quien_gana import mapas
from archivo_volumen import VOL
O = Path("/root/polymarket-research-datalogs/wallet_pspspsps5"); X = O / "senales_externas"
for d in sys.argv[1:]:
    out = X / f"lado_{d}.csv.gz"
    if out.exists(): continue
    tok = mapas(d)["5min"]; F = pd.read_csv(X / f"ext_{d}.csv.gz", dtype={"mkt": str}, usecols=["ts", "li", "mkt", "lado", "p"])
    mk = {t: (v[1], v[3]) for t, v in tok.items()}
    parts = []
    with gzip.open(VOL / "m5_onchain" / f"m5_onchain_{d}.csv.gz", "rt") as fh:
        for x in pd.read_csv(fh, chunksize=400_000, dtype={"token_id": str}, usecols=["tipo", "ts_est", "side", "token_id", "maker_amt", "taker_amt"]):
            x = x[(x.tipo == "F") & x.token_id.isin(tok.keys())]
            if not len(x): continue
            compra = x.side.values == 0
            acc = np.where(compra, x.taker_amt.values, x.maker_amt.values).astype(float); usd = np.where(compra, x.maker_amt.values, x.taker_amt.values).astype(float)
            parts.append(pd.DataFrame({"mkt": x.token_id.map(lambda t: mk[t][0]).values, "lado": x.token_id.map(lambda t: mk[t][1]).values, "ts": x.ts_est.astype(float).values, "pp": usd / np.maximum(acc, 1e-9)}))
    T = pd.concat(parts, ignore_index=True).sort_values("ts")
    T["k"] = T.mkt + "|" + T.lado
    F["opp"] = np.where(F.lado == "YES", "NO", "YES"); F["ko"] = F.mkt + "|" + F.opp; F["kk"] = F.mkt + "|" + F.lado
    Fs = F.sort_values("ts")
    def last(Fk, key):
        tt = T[["k", "ts", "pp"]].rename(columns={"ts": "tl", "pp": "pl"})
        # bloque estrictamente anterior
        m = pd.merge_asof(Fs.assign(tq=Fs.ts - 1e-6).sort_values("tq"), tt.sort_values("tl"), left_on="tq", right_on="tl", left_by=key, right_by="k", direction="backward")
        return m
    mo = last(Fs, "ko"); mo = mo.rename(columns={"pl": "opp_last", "tl": "opp_t"})
    mw = last(Fs, "kk")[["ts", "li", "mkt", "lado", "pl", "tl"]].rename(columns={"pl": "own_last_prev", "tl": "own_t"})
    R = mo[["ts", "li", "mkt", "lado", "opp_last", "opp_t"]].merge(mw, on=["ts", "li", "mkt", "lado"], how="left")
    R["opp_age"] = R.ts - R.opp_t; R["own_age"] = R.ts - R.own_t
    R.drop(columns=["opp_t", "own_t"]).drop_duplicates(["ts", "li", "mkt", "lado"]).to_csv(out, index=False, compression="gzip"); print(d, len(R), flush=True)
