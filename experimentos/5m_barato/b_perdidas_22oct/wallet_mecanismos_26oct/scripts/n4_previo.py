#!/usr/bin/env python3
"""n4: control de look-ahead de n3. Para cada relleno pasivo de compra (W y población ex-W, <0,40 W / <0,10 pob, 05-14 Oct)
¿había un relleno de MM en el MISMO mercado ANTES (ts_MM <= ts − 3 s)? Y ¿mercado compartido sólo por actividad posterior?
Si la ventaja sólo aparece con actividad posterior => es selección por resultado, no señal."""
import sys, glob
sys.path.insert(0, "/root/polymarket-research")
import numpy as np, pandas as pd
from analisis_maker_cancelacion_binance import desenlaces
rng = np.random.default_rng(5)
def ev(g):
    if len(g) < 20: return f"n={len(g)}"
    dd = g.groupby("dc")[["pnl", "usd"]].sum().values; bs = []
    for _ in range(500):
        s = dd[rng.integers(0, len(dd), len(dd))].sum(0); bs.append(s[0] / s[1])
    return f"EV {g.pnl.sum()/g.usd.sum():+.3f} ({np.percentile(bs,5):+.3f},{np.percentile(bs,95):+.3f}) n={len(g)} hit/p={g.win.mean()/g.p.mean():.2f}"
M = pd.concat([pd.read_csv(f, dtype={"mkt": str}) for f in sorted(glob.glob("/root/polymarket-research-datalogs/mo_money/rellenos_*.csv.gz"))])
first = M.groupby("mkt").ts.min(); last = M.groupby("mkt").ts.max()
W = pd.read_csv("/root/polymarket-research-datalogs/wallet_pspspsps5/fills.csv.gz", dtype={"mkt": str})
W = W[(W.rol == "M") & W.compra & (W.dia_cierre <= "2026-10-14") & (W.p < 0.40)].copy(); W["usd"] = W.usdc; W["dc"] = W.dia_cierre
P = pd.concat([pd.read_csv(f, dtype={"mkt": str}) for f in sorted(glob.glob("/root/polymarket-research-datalogs/wallet_pspspsps5/poblacion_*.csv.gz")) if f[-16:-6] <= "2026-10-14"])
P = P[P.pasivo_compra & ~P.esW.astype(bool)].copy(); d = desenlaces(set(P.mkt)); P["win"] = (P.lado == P.mkt.map(d)).astype(float)
P["usd"] = P.p * P.acc; P["pnl"] = P.win * P.acc - P.usd; P["dc"] = pd.to_datetime(P.cierre, unit="s").dt.strftime("%Y-%m-%d")
P = P[P.dc <= "2026-10-14"]
for nom, Z in (("W<0.10", W[W.p < .1]), ("W0.10-0.40", W[W.p >= .1]), ("POB<0.10", P)):
    f0 = Z.mkt.map(first); l0 = Z.mkt.map(last)
    pre = f0.notna() & (f0 <= Z.ts - 3); solo_post = f0.notna() & ~pre; nunca = f0.isna()
    print(f"{nom}: MM antes {ev(Z[pre])} | MM solo después {ev(Z[solo_post])} | MM nunca {ev(Z[nunca])}")
print("\n--- ex ante estricto (MM antes vs AÚN NO), por moneda ---")
for nom, Z in (("W<0.10", W[W.p < .1]), ("W0.10-0.40", W[W.p >= .1]), ("POB<0.10", P)):
    f0 = Z.mkt.map(first); pre = f0.notna() & (f0 <= Z.ts - 3)
    for a in ("BTC", "ETH", "SOL"):
        S = Z[Z.act == a]; pr = pre[Z.act == a]
        print(f"{nom} {a}: MM antes {ev(S[pr])} | aún no {ev(S[~pr])}")
