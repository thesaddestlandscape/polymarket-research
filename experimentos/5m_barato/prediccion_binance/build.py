import sys, numpy as np, pandas as pd
from featlib import *
H_LIST = [150, 250, 400]
for D in sys.argv[1].split(","):
    fl = pd.read_pickle(P + f"fills_{D}.pkl").reset_index(drop=True)
    coins = {m: Coin(d) for m, d in load_x(D).items()}
    act = fl.act.values; sgn = np.where(fl.lado_c.values == "YES", -1.0, 1.0); rxv = fl.rx.values.astype(np.int64)
    base = fl[["dia", "act", "wallet", "mkt", "lado_c", "pc", "acc", "coste", "pnl", "T", "rx"]].copy()
    base["sgn"] = sgn
    for H in H_LIST:
        Fx = feats(coins, act, sgn, rxv, H); Fy = targets(coins, act, sgn, rxv, H)
        Fx.columns = [c for c in Fx.columns]
        pd.concat([base, Fy, Fx], axis=1).to_pickle(P + f"ds_{D}_H{H}.pkl")
        Fp = feats(coins, act, sgn, rxv, H, shift=30000)
        pd.concat([base, Fy, Fp], axis=1).to_pickle(P + f"dsplc_{D}_H{H}.pkl")
        print(D, H, len(base), flush=True)
