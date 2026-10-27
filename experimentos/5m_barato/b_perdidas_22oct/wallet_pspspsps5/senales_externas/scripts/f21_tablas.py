"""f21: tablas por senal externa: EV de W y de la poblacion (BTC/ETH/SOL, fills pasivos <0,10) por bins de cada rasgo, DESC (05-12 Oct) y HOLD (17-23 Oct). K declarado = 8 rasgos x 5 bins."""
import sys
sys.path.insert(0, "/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/wallet_pspspsps5/senales_externas/scripts")
from f20_carga import *
P = cargar()
print("fills", len(P), "W", int(P.esW.sum()), "dias", sorted(P.dia.unique()))
P = P[np.isfinite(P.zs_cl) & np.isfinite(P.zs_bn) & (P.lag_cl < 10)]
print("tras filtro finitos y lag_cl<10:", len(P), "W", int(P.esW.sum()))
print("lag_cl p50/p90/p99", P.lag_cl.quantile([.5, .9, .99]).round(2).tolist(), " basis_bps |p50| %.2f p90 %.2f" % (P.basis.abs().median(), P.basis.abs().quantile(.9)))
feats = {"zs_bn": [-99, -3, -2, -1, 0, 1, 99], "zs_cl": [-99, -3, -2, -1, 0, 1, 99], "basis_s": [-99, -2, -.5, .5, 2, 99], "m10_cl": [-99, -2, -.5, .5, 2, 99], "imb_s": [-2, -.5, -.1, .1, .5, 2],
         "f5_cl": [-99, -2, -.5, .5, 2, 99], "f30_cl": [-99, -4, -1, 1, 4, 99]}
if "gap" in P: feats["gap"] = [-9, -.05, -.02, 0, .02, .05, 9]
for f, b in feats.items():
    print("\n=====", f, "(signo + = a favor del lado comprado)")
    for per in ("DESC", "HOLD"):
        for nm, X in (("POB", P[(~P.esW) & (P.per == per)]), ("W  ", P[P.esW & (P.per == per)])):
            print("--", per, nm)
            c = pd.cut(X[f], b)
            for k, s in X.groupby(c, observed=True): print(lin(str(k), s))
# cross-asset: solo ETH/SOL (BTC como lider)
print("\n===== cross-asset: fills de ETH/SOL segun zs_BTC (BTC signed con el lado comprado)")
Q = P[P.act.isin(["ETH", "SOL"])]
for per in ("DESC", "HOLD"):
    for nm, X in (("POB", Q[(~Q.esW) & (Q.per == per)]), ("W  ", Q[Q.esW & (Q.per == per)])):
        print("--", per, nm)
        for k, s in X.groupby(pd.cut(X.zs_BTC, [-99, -3, -2, -1, 0, 1, 99]), observed=True): print(lin(str(k), s))
print("\n===== 2D zs_bn x zs_cl (discordancia Binance vs Chainlink), $-ponderado")
b3 = [-99, -2, -1, 0, 99]
for per in ("DESC", "HOLD"):
    for nm, X in (("POB", P[(~P.esW) & (P.per == per)]), ("W  ", P[P.esW & (P.per == per)])):
        print("--", per, nm)
        for (a, c_), s in X.groupby([pd.cut(X.zs_bn, b3), pd.cut(X.zs_cl, b3)], observed=True):
            if len(s) >= 60: print(lin("bn%s cl%s" % (a, c_), s))
