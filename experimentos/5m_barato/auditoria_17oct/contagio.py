# EXPLORATORIO, solo DESC (10-11 Oct): ¿un BARRIDO multinivel en OTRA moneda (mismo cierre 5m, misma dirección adversa),
# recibido por nosotros >=120 ms antes de la recepción del relleno, precede a rellenos maker peores? Placebo: ventana -30 s.
import sys, numpy as np, pandas as pd
B = "/tmp/claude-0/-root-polymarket-research/ca5de530-b5e1-4080-aa20-e0ab73669cdb/scratchpad/B/"
P = "/tmp/claude-0/-root-polymarket-research/a0c96fc2-2902-4388-9cab-9cffc412228c/scratchpad/pred/"
W = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
res = []
for D in sys.argv[1].split(","):
    k = pd.read_csv(B + f"k_{D}.csv.gz", names=["tok", "act", "mkt", "lado"], dtype=str)
    F = pd.read_pickle(P + f"fills_{D}.pkl")
    cier = (F.ts + F["T"]).round(-1)
    m2c = dict(zip(F.mkt.astype(str), cier))
    k["cierre"] = k.mkt.map(m2c)
    k = k.dropna(subset=["cierre"])
    tk = {r.tok: (r.act, r.lado, r.cierre) for r in k.itertuples()}
    T = pd.read_csv(B + f"t_{D}.csv.gz", names=["te", "tok", "p", "side", "q", "rx"], dtype={"tok": str}, usecols=[0, 1, 2, 3, 4, 5]).dropna()
    T = T[T.tok.isin(tk.keys())]
    g = T.groupby(["tok", "te"]).agg(np_=("p", "nunique"), side=("side", "first"), rx=("rx", "min")).reset_index()
    g = g[g.np_ >= 2]
    info = g.tok.map(tk)
    g["act"] = [x[0] for x in info]; g["lado"] = [x[1] for x in info]; g["cierre"] = [x[2] for x in info]
    # dirección sobre Up: SELL de YES o BUY de NO => Up baja (-1); BUY YES o SELL NO => Up sube (+1)
    up = np.where(g.lado == "YES", 1, -1) * np.where(g.side == "BUY", 1, -1)
    g["d"] = up
    ev_ = {}
    for (c, dd), x in g.groupby(["cierre", "d"]):
        ev_[(c, dd)] = (x.rx.values.astype(np.int64), x.act.values)
    # rellenos: 1 por (mkt,lado,pc,tex) y tope 5 acciones
    F = F.groupby(["mkt", "lado_c", "pc", "tex_ms"]).agg(act=("act", "first"), rx=("rx", "min"), ts=("ts", "first"), T=("T", "first"),
                 acc=("acc", "sum"), coste=("coste", "sum"), pnl=("pnl", "sum"), dia=("dia", "first")).reset_index()
    f = np.minimum(F.acc, 5) / F.acc; F["coste"] *= f; F["pnl"] *= f
    F["cierre"] = (F.ts + F["T"]).round(-1)
    dadv = np.where(F.lado_c == "YES", -1, 1)
    pre = np.zeros(len(F), bool); plc = np.zeros(len(F), bool)
    for i, (c, da, a, rx) in enumerate(zip(F.cierre.values, dadv, F.act.values, F.rx.values)):
        e = ev_.get((c, da))
        if e is None: continue
        t, ac = e; o = ac != a
        lo, hi = np.searchsorted(t, [rx - W, rx - 120]); pre[i] = o[lo:hi].any()
        lo, hi = np.searchsorted(t, [rx - W - 30000, rx - 120 - 30000]); plc[i] = o[lo:hi].any()
    F["pre"] = pre; F["plc"] = plc
    res.append(F[["dia", "act", "cierre", "coste", "pnl", "pre", "plc", "T"]])
    print(D, "rellenos(5acc)", len(F), "barridos otra moneda", len(g), flush=True)
d = pd.concat(res, ignore_index=True)
rng = np.random.default_rng(1)
def ev(x): return x.pnl.sum() / x.coste.sum()
def dif(x, col, nb=400):
    t = x.groupby(["cierre", col]).agg(p=("pnl", "sum"), c=("coste", "sum")).unstack(fill_value=0)
    p1, c1, p0, c0 = t[("p", True)].values, t[("c", True)].values, t[("p", False)].values, t[("c", False)].values
    k = len(t); o = []
    for _ in range(nb):
        i = rng.integers(0, k, k); o.append(p1[i].sum() / max(c1[i].sum(), 1e-9) - p0[i].sum() / c0[i].sum())
    return np.percentile(o, [5, 95]).round(3)
for col in ("pre", "plc"):
    for nm, x in [("TODOS", d)] + list(d.groupby("dia")) + [("BTC", d[d.act == "BTC"]), ("ALT", d[d.act != "BTC"])]:
        s, n_ = x[x[col]], x[~x[col]]
        print(f"{col} W={W} {nm:12s} con n={len(s):6d} ({len(s)/len(x):.1%}) EV {ev(s):+.3f} | sin n={len(n_):6d} EV {ev(n_):+.3f} | dif {ev(s)-ev(n_):+.3f} IC90clu {dif(x, col)}")
