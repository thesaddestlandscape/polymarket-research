"""f23: contraparte (quien VENDE a la bid <0,10). Rellenos pasivos de compra p<0,10 en BTC/ETH/SOL 5m con la direccion del tomador. Pregunta: la ventaja de W
viene de a QUIEN le vende (tomadores distintos / menos informados) o es la misma contraparte a mejor precio/seleccion? Test: tomadores que venden a W y a otros makers el mismo dia."""
import sys, gzip, glob
sys.path.insert(0, "/root/polymarket-research")
import numpy as np, pandas as pd
from pathlib import Path
from analisis_5m_barato_quien_gana import mapas, EXCH
from archivo_volumen import VOL
from analisis_maker_cancelacion_binance import desenlaces
W = "0xb0f85baa97990910a3e8ac2b4a58a322f01ecef5"
DIAS = ["2026-10-%02d" % d for d in (5, 6, 7, 8, 9, 10, 11, 12, 17, 18, 19, 20, 21, 22, 23)]
rows = []
for d in DIAS:
    tok = mapas(d)["5min"]; tok = {k: v for k, v in tok.items() if v[0] in ("BTC", "ETH", "SOL")}
    with gzip.open(VOL / "m5_onchain" / f"m5_onchain_{d}.csv.gz", "rt") as fh:
        for x in pd.read_csv(fh, chunksize=400_000, dtype={"token_id": str, "maker": str, "taker": str}, usecols=["tipo", "ts_est", "maker", "taker", "side", "token_id", "maker_amt", "taker_amt"]):
            x = x[(x.tipo == "F") & x.token_id.isin(tok.keys()) & (x.side == 0) & (x.taker != EXCH)]
            if not len(x): continue
            acc = x.taker_amt.values.astype(float); usd = x.maker_amt.values.astype(float); p = usd / np.maximum(acc, 1e-9)
            k = p < 0.10
            if not k.any(): continue
            x = x[k]; acc = acc[k]; p = p[k]
            rows.append(pd.DataFrame({"d": d, "mkt": x.token_id.map(lambda t: tok[t][1]).values, "lado": x.token_id.map(lambda t: tok[t][3]).values, "cierre": x.token_id.map(lambda t: tok[t][2]).values,
                                      "p": p, "acc": acc, "esW": (x.maker.str.lower() == W).values, "taker": x.taker.str.lower().values}))
P = pd.concat(rows, ignore_index=True)
des = desenlaces(set(P.mkt)); P["des"] = P.mkt.map(des).fillna(""); P = P[P.des != ""].copy()
P["win"] = (P.lado == P.des).astype("float32"); P["c"] = P.p * P.acc; P["pnl"] = P.acc * P.win - P.c
P["dia"] = pd.to_datetime(P.cierre, unit="s").dt.strftime("%Y-%m-%d"); P["per"] = np.where(P.dia <= "2026-10-12", "DESC", np.where(P.dia >= "2026-10-17", "HOLD", "x"))
rng = np.random.default_rng(3)
def ev(s): return s.pnl.sum() / s.c.sum() if s.c.sum() > 0 else np.nan
def bs(df, B=800):
    g = df.groupby("dia")[["pnl", "c"]].sum().values; n = len(g)
    if n < 3: return (np.nan, np.nan)
    r = [g[i, 0].sum() / g[i, 1].sum() for i in (rng.integers(0, n, n) for _ in range(B))]; return tuple(np.round(np.percentile(r, [5, 95]), 2))
print("fills", len(P), "W", int(P.esW.sum()), "tomadores distintos", P.taker.nunique(), "| W: tomadores distintos", P[P.esW].taker.nunique())
for nm, X in (("POB", P[~P.esW]), ("W", P[P.esW])):
    c = X.groupby("taker").c.sum().sort_values(ascending=False); print(nm, "top1/top10/top50 tomador % del $:", [round(100 * c.iloc[:k].sum() / c.sum(), 1) for k in (1, 10, 50)])
Wt = set(P[P.esW].taker); Ot = set(P[~P.esW].taker)
# tomadores que venden a W: fraccion de su volumen que va a W
tk = P.groupby("taker").apply(lambda s: pd.Series({"cW": s[s.esW].c.sum(), "cO": s[~s.esW].c.sum(), "nW": int(s.esW.sum()), "nO": int((~s.esW).sum())}))
sh = tk[(tk.nW >= 20) & (tk.nO >= 20)].index
print("tomadores con >=20 fills a W y >=20 a otros:", len(sh), "| $ a W cubierto %.1f%% del $ de W" % (100 * tk.loc[sh].cW.sum() / tk.cW.sum()))
for per in ("DESC", "HOLD"):
    A = P[(P.per == per) & P.taker.isin(sh)]
    for nm, X in (("W    (mismos tomadores)", A[A.esW]), ("otros (mismos tomadores)", A[~A.esW])):
        print("%s %-26s n %7d $%8.0f EV %+.3f IC90 %s hit/p %.2f" % (per, nm, len(X), X.c.sum(), ev(X), bs(X), X.win.mean() / X.p.mean()))
    B = P[(P.per == per) & ~P.taker.isin(sh)]
    for nm, X in (("W    (resto tomadores)", B[B.esW]), ("otros (resto tomadores)", B[~B.esW])):
        if len(X) > 30: print("%s %-26s n %7d $%8.0f EV %+.3f IC90 %s hit/p %.2f" % (per, nm, len(X), X.c.sum(), ev(X), bs(X), X.win.mean() / X.p.mean()))
# por tomador: EV a W vs EV a otros (ponderado por $ de W) 
g = P[P.taker.isin(sh)].groupby(["taker", "esW"]).apply(lambda s: pd.Series({"c": s.c.sum(), "pnl": s.pnl.sum()})).unstack()
g = g.dropna(); g["evW"] = g[("pnl", True)] / g[("c", True)]; g["evO"] = g[("pnl", False)] / g[("c", False)]; w = g[("c", True)]
print("media ponderada por $W de EV por tomador: a W %+.3f | a otros %+.3f | n tomadores %d | tomadores con evW>evO: %.0f%%" % ((g.evW * w).sum() / w.sum(), (g.evO * w).sum() / w.sum(), len(g), 100 * (g.evW > g.evO).mean()))
# Tomadores 'repetidores' (mismo tomador vende a muchos niveles en el mismo bloque): fracc de fills de W cuyo tomador es top-20 de la poblacion
top = P[~P.esW].groupby("taker").c.sum().sort_values(ascending=False).index[:20]
for per in ("DESC", "HOLD"):
    A = P[P.per == per]
    for nm, X in (("W", A[A.esW]), ("POB", A[~A.esW])):
        s = X[X.taker.isin(top)]; r = X[~X.taker.isin(top)]
        print(per, nm, "top-20 tomadores: %.1f%% del $, EV %+.3f | resto EV %+.3f" % (100 * s.c.sum() / X.c.sum(), ev(s), ev(r)))
