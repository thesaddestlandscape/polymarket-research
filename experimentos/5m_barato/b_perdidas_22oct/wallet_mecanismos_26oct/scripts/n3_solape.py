#!/usr/bin/env python3
"""n3: ¿W y MM se rellenan en los MISMOS barridos (misma tx) o mercados? 05-14 Oct (cachés existentes). EV de cada una
dentro/fuera de las tx compartidas; si el edge vive en el barrido (quién barre), debería concentrarse en las compartidas."""
import sys, glob
sys.path.insert(0, "/root/polymarket-research")
import numpy as np, pandas as pd
rng = np.random.default_rng(3)
def ev(g):
    if len(g) < 20: return f"n={len(g)}"
    dd = g.groupby("dc")[["pnl", "usd"]].sum().values; bs = []
    for _ in range(500):
        s = dd[rng.integers(0, len(dd), len(dd))].sum(0); bs.append(s[0] / s[1])
    return f"EV {g.pnl.sum()/g.usd.sum():+.3f} IC90d ({np.percentile(bs,5):+.3f},{np.percentile(bs,95):+.3f}) n={len(g)} $={g.usd.sum():.0f}"
X = pd.read_csv("/root/polymarket-research-datalogs/wallet_mecanismos_26oct/n1_W_pob.csv.gz", usecols=["esW"]).shape  # noqa
W = pd.read_csv("/root/polymarket-research-datalogs/wallet_pspspsps5/fills.csv.gz", dtype={"mkt": str})
W = W[(W.rol == "M") & W.compra & (W.dia_cierre <= "2026-10-14")].copy(); W["usd"] = W.usdc
W["dc"] = W.dia_cierre
from analisis_maker_cancelacion_binance import desenlaces
M = pd.concat([pd.read_csv(f, dtype={"mkt": str}) for f in sorted(glob.glob("/root/polymarket-research-datalogs/mo_money/rellenos_*.csv.gz"))])
M = M[(M.rol == "M") & M.compra].copy(); d = desenlaces(set(M.mkt)); M["win"] = (M.lado == M.mkt.map(d)).astype(float)
M["usd"] = M.usdc; M["pnl"] = M.win * M.acc - M.usd; M["dc"] = pd.to_datetime(M.cierre, unit="s").dt.strftime("%Y-%m-%d")
tw, tm = set(W.tx), set(M.tx); mw, mmk = set(W.mkt), set(M.mkt)
print(f"tx W {len(tw)} MM {len(tm)} compartidas {len(tw & tm)} | mercados W {len(mw)} MM {len(mmk)} compartidos {len(mw & mmk)}")
for nom, Z, otra_tx, otra_m in (("W", W, tm, mmk), ("MM", M, tw, mw)):
    for lo, hi in ((0, .1), (.1, .4), (.4, 1.01)):
        S = Z[(Z.p >= lo) & (Z.p < hi)]
        print(f"{nom} p[{lo},{hi}) tx compartida: {ev(S[S.tx.isin(otra_tx)])} | no: {ev(S[~S.tx.isin(otra_tx)])} | mercado compartido: {ev(S[S.mkt.isin(otra_m)])} | no: {ev(S[~S.mkt.isin(otra_m)])}")
