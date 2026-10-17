import sys, numpy as np, pandas as pd, warnings
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier, HistGradientBoostingRegressor
from sklearn.metrics import roc_auc_score
warnings.filterwarnings("ignore")
P = "/tmp/claude-0/-root-polymarket-research/a0c96fc2-2902-4388-9cab-9cffc412228c/scratchpad/pred/"
DIAS = ["2026-10-10", "2026-10-11", "2026-10-12", "2026-10-13"]
BIN = ["stale", "R100", "R250", "R500", "R1000", "R3000", "R10000", "A100_250", "A250_1000", "n100", "n250", "n1000", "n5000",
       "int_rel", "vol1s", "vol5s", "rng1s", "rng5s", "pos_adv5", "pos_fav5", "imb250", "imb1000", "nl250", "nl1000", "maxnl1000",
       "lastnl", "lastadv", "streak", "dlast2", "R10_last", "btcR100", "btcR250", "btcR1000", "btcR3000", "btc_int"]
COINS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]

def load(H, pref="ds"):
    d = pd.concat([pd.read_pickle(P + f"{pref}_{D}_H{H}.pkl") for D in DIAS], ignore_index=True)
    for c in COINS: d["c_" + c] = (d.act == c).astype(float)
    d["y"] = (d.pnl / d.coste).clip(-1, 9)
    d["Y1"] = (d.adv100 >= 1).astype(int); d["Y3"] = (d.adv_gap >= 1).astype(int)
    d["clu"] = (d.rx // 300000).astype(np.int64)      # cierre de 5 min (todas las monedas = una apuesta)
    d["unit"] = d.wallet + "|" + d.mkt + "|" + d.lado_c
    return d

CODE = ["c_" + c for c in COINS] + ["sgn"]
CTX = ["pc", "T"] + CODE
def X_hgb(d, cols): return d[cols].values.astype(float)
def X_lin(d, cols, st=None):
    A = d[cols].copy()
    for c in cols:
        if c in ("R100","R250","R500","R1000","R3000","R10000","A100_250","A250_1000","pos_adv5","pos_fav5","dlast2","R10_last","btcR100","btcR250","btcR1000","btcR3000"):
            A[c] = np.arcsinh(A[c] * 3)
        elif c in ("stale","n100","n250","n1000","n5000","vol1s","vol5s","rng1s","rng5s","btc_int"):
            A[c] = np.log1p(A[c].clip(lower=0))
    if "rng1s" in cols: A["rng1s_na"] = d.rng1s.isna().astype(float)
    A = A.fillna(0.0)
    if st is None: st = (A.mean(), A.std().replace(0, 1))
    return ((A - st[0]) / st[1]).values, st

def mk_clf(): return HistGradientBoostingClassifier(max_depth=3, learning_rate=0.05, max_iter=120, min_samples_leaf=300, l2_regularization=10.0, random_state=0)
def mk_reg(): return HistGradientBoostingRegressor(max_depth=3, learning_rate=0.05, max_iter=120, min_samples_leaf=500, l2_regularization=10.0, random_state=0)

def fit_score(tr, te, cols, target, kind, reg=False, oof_on=True):
    """devuelve (score_te, score_tr_oof). Logística o HGB; OOF por día dentro del train si hay >=2 días."""
    def one(a, b):
        if reg:
            m = mk_reg(); m.fit(X_hgb(a, cols), a[target].values, sample_weight=np.minimum(a.coste.values, 5)); return m.predict(X_hgb(b, cols))
        if kind == "lin":
            Xa, st = X_lin(a, cols); Xb, _ = X_lin(b, cols, st)
            m = LogisticRegression(C=0.05, max_iter=300); m.fit(Xa, a[target].values); return m.decision_function(Xb)
        m = mk_clf(); m.fit(X_hgb(a, cols), a[target].values); return m.predict_proba(X_hgb(b, cols))[:, 1]
    ste = one(tr, te)
    if not oof_on: return ste, None
    ds = sorted(tr.dia.unique())
    if len(ds) >= 2:
        oof = np.zeros(len(tr))
        for i, dd in enumerate(ds):
            m_ = (tr.dia == dd).values
            oof[m_] = one(tr[~m_], tr[m_])
    else:
        oof = one(tr, tr)
    return ste, oof

def auc(y, s):
    return roc_auc_score(y, s) if 0 < y.sum() < len(y) else np.nan

def ev(d): return d.pnl.sum() / d.coste.sum() if len(d) and d.coste.sum() > 0 else np.nan

def boot_clu(d, f, n=1000, seed=1):
    """bootstrap por cierre de 5 min; f(sub)->valor; IC90."""
    rng = np.random.default_rng(seed)
    g = {k: v for k, v in d.groupby("clu")}
    keys = np.array(list(g.keys()))
    out = []
    for _ in range(n):
        ks = rng.choice(keys, len(keys))
        out.append(f(pd.concat([g[k] for k in ks])))
    return np.nanpercentile(out, [5, 95])
