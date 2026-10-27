"""f24: precio del otro lado. gap=(1-opp_last)-p (opp_last = ultimo precio operado del token opuesto en bloque anterior); inc = own_last_prev+opp_last-1."""
import sys
sys.path.insert(0, "/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/wallet_pspspsps5/senales_externas/scripts")
from f20_carga import *
P = cargar(); P = P[P.gap.notna() & P.per.isin(["DESC", "HOLD"])].copy()
print("fills con opp_last:", len(P), "W", int(P.esW.sum()), "cobertura de fills (todos):", "ver f21"); print("opp_age p50/p90 s", P.opp_age.quantile([.5, .9]).round(1).tolist())
P["inc"] = P.own_last_prev + P.opp_last - 1
for f, b in (("gap", [-9, -.05, -.02, 0, .02, .05, 9]), ("inc", [-9, -.1, -.03, .03, .1, 9]), ("opp_age", [-1, 2, 10, 30, 9999])):
    print("\n=====", f)
    for per in ("DESC", "HOLD"):
        for nm, X in (("POB", P[(~P.esW) & (P.per == per)]), ("W  ", P[P.esW & (P.per == per)])):
            print("--", per, nm)
            for k, s in X.groupby(pd.cut(X[f], b), observed=True): print(lin(str(k), s))
