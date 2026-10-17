# ¿La EV/€ «confirmada» de H5M (media por unidad mercado-lado de Σpnl/Σcoste) es un artefacto de media de cocientes?
import sys, numpy as np, pandas as pd
B = "/tmp/claude-0/-root-polymarket-research/ca5de530-b5e1-4080-aa20-e0ab73669cdb/scratchpad/B/"
cols = ["mkt", "lado_c", "ts", "acc", "pc", "coste", "pnl", "dia", "act", "T"]
for D in sys.argv[1].split(","):
    d = pd.read_csv(B + f"feat_{D}.csv.gz", usecols=cols, dtype={"mkt": str, "lado_c": "category", "act": "category"})
    d = d[(d.pc > 0.10) & (d.pc <= 0.30) & (d["T"] > 60) & (d["T"] <= 300)].sort_values("ts", kind="stable")
    u = d.groupby(["mkt", "lado_c"], observed=True).agg(p=("pnl", "sum"), c=("coste", "sum"), acc=("acc", "sum"), act=("act", "first"))
    u["ev"] = u.p / u.c
    gan = (u.p > 0)
    # primeras 5 acciones del mercado-lado (cualquier maker): nuestra puja si fuéramos los primeros
    d["cum"] = d.groupby(["mkt", "lado_c"], observed=True).acc.cumsum(); d["prev"] = d.cum - d.acc
    f = (np.clip(5 - d.prev, 0, None).clip(upper=d.acc)) / d.acc
    d5 = d.assign(coste=d.coste * f, pnl=d.pnl * f)
    u5 = d5[f > 0].groupby(["mkt", "lado_c"], observed=True).agg(p=("pnl", "sum"), c=("coste", "sum"))
    print(f"{D} unidades {len(u)} | vigía (media de cocientes) {u.ev.mean():+.4f} | ponderada por € (Σpnl/Σcoste) {u.p.sum()/u.c.sum():+.4f} "
          f"| primeras 5 acc: media {(u5.p/u5.c).mean():+.4f} ponderada {u5.p.sum()/u5.c.sum():+.4f} | € medio en unidades ganadoras {u.c[gan].mean():.1f} vs perdedoras {u.c[~gan].mean():.1f} "
          f"| acierto unidades {gan.mean():.3f} | sin BTC media {u[u.act!='BTC'].ev.mean():+.4f} pond {u[u.act!='BTC'].p.sum()/u[u.act!='BTC'].c.sum():+.4f}")
