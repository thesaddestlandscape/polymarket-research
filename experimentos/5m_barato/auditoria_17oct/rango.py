# EV/€ por RANGO de la acción dentro de la unidad (wallet,mkt,lado): ¿las acciones tardías ganan por precio/T o por el rango mismo?
import sys, numpy as np, pandas as pd
B = "/tmp/claude-0/-root-polymarket-research/ca5de530-b5e1-4080-aa20-e0ab73669cdb/scratchpad/B/"
cols = ["wallet", "act", "mkt", "ts", "T", "acc", "pc", "coste", "pnl", "dia", "lado_c", "barrido"]
d = pd.concat([pd.read_csv(B + f"feat_{D}.csv.gz", usecols=cols, dtype={"mkt": str, "wallet": "category", "act": "category", "lado_c": "category"}) for D in sys.argv[1].split(",")], ignore_index=True)
d = d.sort_values(["wallet", "mkt", "lado_c", "ts"], kind="stable")
d["prev"] = d.groupby(["wallet", "mkt", "lado_c"], observed=True).acc.cumsum() - d.acc
d["rb"] = pd.cut(d.prev, [-1, 4.99, 24.99, 99.99, 499.99, 1e9], labels=["0-5", "5-25", "25-100", "100-500", ">500"])
d["pb"] = pd.cut(d.pc, [0.0999, 0.15, 0.20, 0.25, 0.3001], labels=["10-15", "15-20", "20-25", "25-30"])
d["tb"] = pd.cut(d["T"], [59, 120, 180, 240, 301], labels=["a", "b", "c", "d"])
d["clu"] = (d.ts // 300).astype(np.int64)
def ev(x): return x.pnl.sum() / x.coste.sum()
ref = d.groupby(["pb", "tb"], observed=True).coste.sum(); ref = ref / ref.sum()
rng = np.random.default_rng(1)
for rb, x in d.groupby("rb", observed=True):
    cel = x.groupby(["pb", "tb"], observed=True).apply(lambda y: ev(y))
    est = (cel * ref).sum() / ref[cel.index].sum()
    g = x.groupby("clu"); s = g.pnl.sum().values; c = g.coste.sum().values; k = len(s)
    bs = [s[i].sum() / c[i].sum() for i in (rng.integers(0, k, k) for _ in range(300))]
    top = x.groupby("clu").pnl.sum().abs().nlargest(5).index; x2 = x[~x.clu.isin(top)]
    print(f"rango {rb:8s} n={len(x):7d} coste ${x.coste.sum():9.0f} precio med {np.average(x.pc, weights=x.coste):.3f} T med {x['T'].median():.0f} "
          f"EV {ev(x):+.3f} IC90clu {np.percentile(bs,[5,95]).round(3)} | EV estandarizado precio×T {est:+.3f} | sin top5 cierres {ev(x2):+.3f} | barrido {x.barrido.mean():.0%}")
