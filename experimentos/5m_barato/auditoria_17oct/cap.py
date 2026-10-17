# Igual que barrido.py pero con tamaño TOPADO a 5 acciones por relleno (lo que sería nuestra puja) y 1 relleno por (mkt,lado,tx-nivel) implícito.
import sys, numpy as np, pandas as pd
B = "/tmp/claude-0/-root-polymarket-research/ca5de530-b5e1-4080-aa20-e0ab73669cdb/scratchpad/B/"
cols = ["act", "mkt", "ts", "T", "acc", "pc", "coste", "pnl", "dia", "barrido", "lado_c", "tx"]
d = pd.concat([pd.read_csv(B + f"feat_{D}.csv.gz", usecols=cols, dtype={"mkt": str, "act": "category", "lado_c": "category", "tx": str}) for D in sys.argv[1].split(",")], ignore_index=True)
# una fila por (tx, mkt, lado, precio): la puja de 5 acc de un maker en ese nivel en esa casación
d = d.groupby(["tx", "mkt", "lado_c", "pc"], observed=True).agg(act=("act", "first"), ts=("ts", "first"), T=("T", "first"), acc=("acc", "sum"),
        coste=("coste", "sum"), pnl=("pnl", "sum"), dia=("dia", "first"), barrido=("barrido", "max")).reset_index()
f = np.minimum(d.acc, 5.0) / d.acc
d["coste"] = d.coste * f; d["pnl"] = d.pnl * f
d["clu"] = (d.ts // 300).astype(np.int64)
rng = np.random.default_rng(1)
def ev(x): return x.pnl.sum() / x.coste.sum()
def dif_clu(x, nb=300):
    t = x.groupby(["clu", "barrido"]).agg(p=("pnl", "sum"), c=("coste", "sum")).unstack(fill_value=0)
    p1, c1, p0, c0 = t[("p", True)].values, t[("c", True)].values, t[("p", False)].values, t[("c", False)].values
    k = len(t); out = []
    for _ in range(nb):
        i = rng.integers(0, k, k); out.append(p1[i].sum() / c1[i].sum() - p0[i].sum() / c0[i].sum())
    return np.percentile(out, [5, 95]).round(3)
def linea(nm, x):
    s, n_ = x[x.barrido], x[~x.barrido]
    print(f"  {nm:24s} barrido n={len(s):6d} EV {ev(s):+.3f} | sin n={len(n_):6d} EV {ev(n_):+.3f} | dif {ev(s)-ev(n_):+.3f} IC90clu {dif_clu(x)}")
print("casaciones-nivel (5 acc topadas):", len(d))
linea("TOTAL", d)
top = d[d.barrido].groupby("clu").pnl.sum().abs().nlargest(5).index
linea("sin top5 cierres", d[~d.clu.isin(top)])
top20 = d.groupby("clu").pnl.sum().abs().nlargest(20).index
linea("sin top20 cierres (todos)", d[~d.clu.isin(top20)])
for v, x in d.groupby("dia"): linea(f"dia={v}", x)
d["bt"] = np.where(d.act == "BTC", "BTC", "ALT")
for v, x in d.groupby("bt"): linea(f"{v}", x)
# por cierre: fracción de cierres en que barrido > sin (cierres con ambos)
t = d.groupby(["clu", "barrido"]).apply(lambda x: ev(x)).unstack()
t = t.dropna()
print("  cierres con ambos:", len(t), " % cierres barrido>sin:", round(((t[True] > t[False]).mean()) * 100, 1), " mediana dif:", round((t[True] - t[False]).median(), 3))
