"""f20_carga: carga comun (ext_D + lado_D + desenlace oficial). Uso: from f20_carga import cargar ; P = cargar()"""
import sys, glob
sys.path.insert(0, "/root/polymarket-research")
import numpy as np, pandas as pd
from pathlib import Path
from analisis_maker_cancelacion_binance import desenlaces
X = Path("/root/polymarket-research-datalogs/wallet_pspspsps5/senales_externas")
def cargar(acts=("BTC", "ETH", "SOL")):
    L = []
    for f in sorted(glob.glob(str(X / "ext_2026-*.csv.gz"))):
        d = f.split("ext_")[1][:10]; e = pd.read_csv(f, dtype={"mkt": str})
        g = X / f"lado_{d}.csv.gz"
        if g.exists(): e = e.merge(pd.read_csv(g, dtype={"mkt": str}), on=["ts", "li", "mkt", "lado"], how="left")
        e = e[e.act.isin(acts)]
        for c in e.columns:
            if e[c].dtype == "float64": e[c] = e[c].astype("float32")
        e["act"] = e.act.astype("category"); e["lado"] = e.lado.astype("category")
        L.append(e)
    P = pd.concat(L, ignore_index=True)
    P["act"] = P.act.astype(str); P["lado"] = P.lado.astype(str)
    P["dia"] = pd.to_datetime(P.cierre, unit="s").dt.strftime("%Y-%m-%d")
    des = desenlaces(set(P.mkt.astype(str))); P["des"] = P.mkt.map(des).fillna(""); P = P[P.des != ""].copy(); P["mkt"] = P.mkt.astype("category")
    P["win"] = (P.lado == P.des).astype("float32"); P["c"] = (P.p * P.acc).astype("float32"); P["pnl"] = (P.acc * P.win - P.c).astype("float32")
    sg = np.where(P.lado == "YES", 1.0, -1.0).astype("float32")
    for a, b in (("z", "zs_bn"), ("z_cl", "zs_cl"), ("d_cl", "ds_cl"), ("d_bps", "ds_bn"), ("mov10", "m10_bn"), ("mov10_cl", "m10_cl"), ("mov30_cl", "m30_cl"),
                 ("fwd5_cl", "f5_cl"), ("fwd30_cl", "f30_cl"), ("fwd5_bn", "f5_bn"), ("fwd30_bn", "f30_bn"), ("imb", "imb_s"), ("z_BTC", "zs_BTC"), ("z_ETH", "zs_ETH"), ("z_SOL", "zs_SOL"), ("basis", "basis_s")):
        P[b] = (P[a] * sg).astype("float32")
    P = P.drop(columns=[c for c in ("d_bps", "mov10", "mov30", "mov10_cl", "mov30_cl", "fwd5_cl", "fwd30_cl", "fwd5_bn", "fwd30_bn", "imb", "z", "z_BTC", "z_ETH", "z_SOL", "des", "li") if c in P.columns])
    if "opp_last" in P: P["gap"] = (1 - P.opp_last) - P.p
    P["per"] = np.where(P.dia <= "2026-10-12", "DESC", np.where(P.dia >= "2026-10-17", "HOLD", "x"))
    return P
rng = np.random.default_rng(11)
def ev(s): return s.pnl.sum() / s.c.sum() if len(s) and s.c.sum() > 0 else np.nan
def bs(df, B=1000):
    g = df.groupby("dia")[["pnl", "c"]].sum().values; n = len(g)
    if n < 3: return (np.nan, np.nan)
    r = [g[i, 0].sum() / g[i, 1].sum() for i in (rng.integers(0, n, n) for _ in range(B))]
    return tuple(float(x) for x in np.round(np.percentile(r, [5, 95]), 2))
def lin(nm, s, minn=40):
    if len(s) < minn: return "  %-28s n=%d" % (nm, len(s))
    return "  %-28s n %7d $%8.0f EV %+.3f (%+.2f,%+.2f) hit/p %.2f d%d" % ((nm, len(s), s.c.sum(), ev(s)) + bs(s) + (s.win.mean() / s.p.mean(), s.dia.nunique()))
