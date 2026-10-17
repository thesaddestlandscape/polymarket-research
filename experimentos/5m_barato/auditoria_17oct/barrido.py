# Auditoría de planteamiento (solo lectura): EV/€ de rellenos maker de la población H5M por BARRIDO, estratificado por precio, T, moneda, día; IC por cierre.
import sys, numpy as np, pandas as pd
B = "/tmp/claude-0/-root-polymarket-research/ca5de530-b5e1-4080-aa20-e0ab73669cdb/scratchpad/B/"
cols = ["act", "mkt", "ts", "T", "acc", "pc", "coste", "pnl", "dia", "barrido", "cola", "nivel", "wallet", "lado_c", "venta"]
parts = []
for D in sys.argv[1].split(","):
    d = pd.read_csv(B + f"feat_{D}.csv.gz", usecols=cols, dtype={"mkt": str, "wallet": "category", "act": "category", "cola": "category", "lado_c": "category"})
    parts.append(d)
d = pd.concat(parts, ignore_index=True); del parts
d["clu"] = (d.ts // 300).astype(np.int64)
d["pb"] = pd.cut(d.pc, [0.0999, 0.15, 0.20, 0.25, 0.3001], labels=["10-15", "15-20", "20-25", "25-30"])
d["tb"] = pd.cut(d["T"], [59, 120, 180, 240, 301], labels=["60-120", "120-180", "180-240", "240-300"])
print("n rellenos", len(d), "días", sorted(d.dia.unique()), "barrido %", round(d.barrido.mean() * 100, 1))
def ev(x): return x.pnl.sum() / x.coste.sum() if x.coste.sum() > 0 else np.nan
rng = np.random.default_rng(1)
def ic_clu(x, nb=300):
    g = x.groupby("clu")
    s = g.pnl.sum().values; c = g.coste.sum().values; k = len(s)
    out = []
    for _ in range(nb):
        i = rng.integers(0, k, k); out.append(s[i].sum() / c[i].sum())
    return np.percentile(out, [5, 95]).round(3)
def dif_clu(x, nb=300):
    g = x.groupby(["clu", "barrido"])
    t = g.agg(p=("pnl", "sum"), c=("coste", "sum")).unstack(fill_value=0)
    p1, c1, p0, c0 = t[("p", True)].values, t[("c", True)].values, t[("p", False)].values, t[("c", False)].values
    k = len(t); out = []
    for _ in range(nb):
        i = rng.integers(0, k, k); out.append(p1[i].sum() / c1[i].sum() - p0[i].sum() / c0[i].sum())
    return np.percentile(out, [5, 95]).round(3)
def linea(nm, x):
    s, n_ = x[x.barrido], x[~x.barrido]
    if len(s) < 200 or len(n_) < 200: print(f"  {nm:22s} poco n"); return
    print(f"  {nm:22s} barrido n={len(s):6d} EV {ev(s):+.3f} | sin n={len(n_):6d} EV {ev(n_):+.3f} | dif {ev(s)-ev(n_):+.3f} IC90clu {dif_clu(x)}")
linea("TOTAL", d)
print("IC90 por cierre EV barrido", ic_clu(d[d.barrido]), "sin", ic_clu(d[~d.barrido]))
# sin los 5 cierres con mayor |pnl| de barrido
top = d[d.barrido].groupby("clu").pnl.sum().abs().nlargest(5).index
linea("TOTAL sin top5 cierres", d[~d.clu.isin(top)])
for c in ["dia", "pb", "tb", "act", "cola", "venta"]:
    print(f"-- por {c}")
    for v, x in d.groupby(c, observed=True): linea(f"{c}={v}", x)
# emparejado por estrato precio x T x moneda (diferencia media ponderada por coste de barrido)
print("-- diferencia estandarizada por estrato pb x tb x act (pesos = coste barrido)")
num = den = 0.0
for k, x in d.groupby(["pb", "tb", "act"], observed=True):
    s, n_ = x[x.barrido], x[~x.barrido]
    if len(s) < 30 or len(n_) < 30: continue
    w = s.coste.sum(); num += w * (ev(s) - ev(n_)); den += w
print(f"  dif estratificada {num/den:+.3f}")
