import sys; sys.path.insert(0, "/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f6_tipo_tomador/scripts")
from lib import *
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, log_loss
U = carga(); out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); out.append(s); open(D + "e5_salida.txt", "w").write("\n".join(out))
U["share_rep"] = U.fl_usd_rep200 / U.fl_usd_all.replace(0, np.nan); U["share_bot"] = U.fl_usd_bot2000 / U.fl_usd_all.replace(0, np.nan)
U["lado_y"] = (U.lado_c == "YES").astype(float)
for a in ("ETH", "SOL"): U["is_" + a] = (U.act == a).astype(float)
U["lfl"] = np.log1p(U.fl_usd_all); U["lflrep"] = np.log1p(U.fl_usd_rep200); U["lflbot"] = np.log1p(U.fl_usd_bot2000)
base = ["pc", "T", "hora", "is_ETH", "is_SOL", "lado_y"]
ctx = ["dp5", "dp30", "dp60", "hi60", "rng60", "d_open", "vol30", "vol_all", "flow60", "bb", "ba", "bs", "as_", "spread", "depth_ticks", "imb", "b15", "a15", "lvl15", "gap15", "r60f", "rpre_s", "z"]
flo = ["lfl", "lflrep", "lflbot", "share_rep", "share_bot", "fl_n_all"]
F_ALL = base + ctx + flo; F_NOFLOW = base + ctx; F_BASE = base
def fit_pred(tr, te, feats, kind, C=0.1):
    Xtr = tr[feats].astype(float); Xte = te[feats].astype(float)
    if kind == "hgb":
        m = HistGradientBoostingClassifier(max_depth=3, max_iter=150, learning_rate=0.05, l2_regularization=1.0, min_samples_leaf=200, random_state=20261024)
        m.fit(Xtr, tr.y); return m.predict_proba(Xte)[:, 1]
    med = Xtr.median(); ind = [c for c in feats if Xtr[c].isna().any()]
    def prep(X):
        Z = X.fillna(med)
        for c in ind: Z[c + "_na"] = X[c].isna().astype(float)
        return Z
    sc = StandardScaler().fit(prep(Xtr)); m = LogisticRegression(C=C, max_iter=300)
    m.fit(sc.transform(prep(Xtr)), tr.y); return m.predict_proba(sc.transform(prep(Xte)))[:, 1]
def walk(target, feats, kind, test_days, C=0.1):
    pr = pd.Series(np.nan, index=U.index)
    for d in test_days:
        tr = U[(U.dia < d) & (U.per != "X")]; te = U[U.dia == d]
        pr[te.index] = fit_pred(tr.assign(y=target[tr.index]), te, feats, kind, C)
    return pr
def auc_ic(y, p, cid, B=300, seed=5):
    a0 = roc_auc_score(y, p); rng = np.random.default_rng(seed); ids = np.unique(cid); g = {k: np.where(cid == k)[0] for k in ids}
    r = []
    for _ in range(B):
        s = rng.choice(ids, len(ids)); ix = np.concatenate([g[k] for k in s])
        if len(np.unique(y[ix])) < 2: continue
        r.append(roc_auc_score(y[ix], p[ix]))
    return a0, np.percentile(r, 5), np.percentile(r, 95)
def evalua(nm, target, pr, days):
    S = U[U.dia.isin(days)]; y = target[S.index].values.astype(int); p = pr[S.index].values
    a, lo, hi = auc_ic(y, p, S.cid.values)
    q = np.quantile(p, 0.8); top = p >= q
    # lift con bootstrap por cierre
    rng = np.random.default_rng(7); ids = np.unique(S.cid.values); cidv = S.cid.values; lifts = []
    # por-cierre sumas
    dfc = pd.DataFrame({"cid": cidv, "y": y, "top": top}); gg = dfc.groupby("cid").apply(lambda s: pd.Series({"yt": s.y[s.top].sum(), "nt": s.top.sum(), "ya": s.y.sum(), "na": len(s)})).values
    n = len(gg); idx = rng.integers(0, n, (400, n)); ss = gg[idx].sum(axis=1); lift = (ss[:, 0] / ss[:, 1]) / (ss[:, 2] / ss[:, 3])
    l0 = (y[top].mean() / y.mean())
    # placebo: permutar y dentro de dia x moneda con las mismas predicciones
    stt = pd.factorize(S.dia + S.act.astype(str))[0]; ap = []
    rng2 = np.random.default_rng(11)
    for _ in range(60):
        k = np.lexsort((rng2.random(len(y)), stt)); yy = np.empty(len(y), int); o0 = np.argsort(stt, kind="stable"); yy[o0] = y[o0][k]; ap.append(roc_auc_score(yy, p))
    P(f"{nm:34s} n {len(y):6d} base {y.mean():.3f} AUC {a:.3f} IC90cierre ({lo:.3f},{hi:.3f}) | quintil sup Y {y[top].mean():.3f} lift {l0:.2f} IC90 ({np.percentile(lift,5):.2f},{np.percentile(lift,95):.2f}) | placebo AUC p95 {np.percentile(ap,95):.3f}")
    return a
DAYS_D = ["2026-10-%02d" % d for d in (12, 13, 14)]; DAYS_H = ["2026-10-%02d" % d for d in range(15, 21)]
yN = U.nrep.astype(int); yB = (U.tk_n >= 2000).astype(int)
P("### H2 (prereg): Y = NO-REP (tk_n<=199), walk-forward")
res = {}
for nm, feats, kind, C in (("BASE logit (pc,T,hora,moneda,lado)", F_BASE, "logit", 0.1), ("CTX logit C=.1", F_NOFLOW, "logit", 0.1),
                           ("CTX+FLOW logit C=.1", F_ALL, "logit", 0.1), ("CTX+FLOW hgb", F_ALL, "hgb", 0)):
    pr = walk(yN, feats, kind, DAYS_D + DAYS_H, C); res[nm] = pr
    P("-- " + nm); evalua(" DISC", yN, pr, DAYS_D); evalua(" HOLD", yN, pr, DAYS_H); pd.DataFrame(res).to_pickle(D + "e5_preds.pkl")
P("\n### EXPLORATORIO: Y = BOT (tk_n>=2000)")
for nm, feats, kind, C in (("CTX+FLOW logit C=.1", F_ALL, "logit", 0.1),):
    pr = walk(yB, feats, kind, DAYS_D + DAYS_H, C); res["B_" + nm] = pr
    P("-- " + nm); evalua(" DISC", yB, pr, DAYS_D); evalua(" HOLD", yB, pr, DAYS_H)
pd.DataFrame(res).to_pickle(D + "e5_preds.pkl")
open(D + "e5_salida.txt", "w").write("\n".join(out))
