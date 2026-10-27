"""f22: q calibrada ex ante (logit sobre rasgos pre-decision: logit p, zs_cl, zs_bn, m10_cl, imb, basis, zs_BTC, ln T) entrenada SOLO con poblacion ex-W de un periodo y evaluada en el otro.
Pregunta: (1) q anade info sobre el precio en la poblacion (log-loss vs solo precio)? (2) W compra donde q/p es mayor? (3) dentro de cada decil de q/p, W-pob.
Sin markouts (mirarian el futuro). K declarado: 2 direcciones de entrenamiento."""
import sys
sys.path.insert(0, "/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/wallet_pspspsps5/senales_externas/scripts")
from f20_carga import *
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss, roc_auc_score
P = cargar(); P = P[np.isfinite(P.zs_cl) & np.isfinite(P.zs_bn) & (P.lag_cl < 10) & P.per.isin(["DESC", "HOLD"])].copy()
P["zb"] = np.where(P.act == "BTC", 0.0, P.zs_BTC.fillna(0.0)); P["lnT"] = np.log(np.maximum(P["T"], 1.0)); P["lp"] = np.log(P.p / (1 - P.p))
F0 = ["lp"]; F1 = ["lp", "zs_cl", "zs_bn", "m10_cl", "imb_s", "basis_s", "zb", "lnT"]
for f in F1[1:]: P[f] = P[f].clip(P[f].quantile(.001), P[f].quantile(.999))
def run(tr, te):
    A = P[(~P.esW) & (P.per == tr)]; A = A.sample(min(len(A), 600_000), random_state=1); B = P[P.per == te].copy()
    mu = A[F1].mean(); sd = A[F1].std()
    m0 = LogisticRegression(C=10, max_iter=300).fit(A[F0], A.win); m1 = LogisticRegression(C=10, max_iter=300).fit(((A[F1] - mu) / sd), A.win)
    B["q0"] = m0.predict_proba(B[F0])[:, 1]; B["q"] = m1.predict_proba((B[F1] - mu) / sd)[:, 1]
    Bp = B[~B.esW]
    print("\n##### entrena %s (pob ex-W n=%d) -> prueba %s (pob %d, W %d)" % (tr, len(A), te, len(Bp), int(B.esW.sum())))
    print("log-loss pob  solo-precio %.5f | con rasgos %.5f | AUC %.4f -> %.4f" % (log_loss(Bp.win, Bp.q0), log_loss(Bp.win, Bp.q), roc_auc_score(Bp.win, Bp.q0), roc_auc_score(Bp.win, Bp.q)))
    print("coef (std):", dict(zip(F1, np.round(m1.coef_[0], 3))))
    W = B[B.esW]
    print("log-loss W   solo-precio %.5f | con rasgos %.5f | AUC %.4f -> %.4f" % (log_loss(W.win, W.q0), log_loss(W.win, W.q), roc_auc_score(W.win, W.q0), roc_auc_score(W.win, W.q)))
    B["r"] = B.q / B.p; B["r0"] = B.q0 / B.p
    qs = np.quantile(B[~B.esW].r, [0, .2, .4, .6, .8, 1.0]); qs[0] = -1; qs[-1] = 1e9
    B["rb"] = pd.cut(B.r, qs, labels=False)
    print("quintil q/p (cortes de la pob): %s" % np.round(qs[1:-1], 2))
    for k in range(5):
        a, w = B[(B.rb == k) & (~B.esW)], B[(B.rb == k) & B.esW]
        print("  Q%d  POB n %7d $%8.0f EV %+.3f (%+.2f,%+.2f) hit/p %.2f | W n %5d $%6.0f EV %+.3f hit/p %.2f | %%$ W %.1f%% vs pob %.1f%% | mean q/p pob %.2f W %.2f" % (
            k + 1, len(a), a.c.sum(), ev(a), *bs(a), a.win.mean() / a.p.mean(), len(w), w.c.sum(), ev(w), (w.win.mean() / w.p.mean()) if len(w) else np.nan,
            100 * w.c.sum() / max(B[B.esW].c.sum(), 1), 100 * a.c.sum() / a.c.sum() * (a.c.sum() / Bp.c.sum()), a.r.mean(), w.r.mean() if len(w) else np.nan))
    top = B[(B.rb == 4) & (~B.esW)]
    print("  regla ex ante 'q/p en el quintil superior' sobre pob: EV %+.3f IC90 dias (%+.2f,%+.2f) n=%d (%d dias)" % (ev(top), *bs(top), len(top), top.dia.nunique()))
    top2 = B[(B.r >= B[~B.esW].r.quantile(.95)) & (~B.esW)]
    print("  top 5%%: EV %+.3f IC90 (%+.2f,%+.2f) n=%d" % (ev(top2), *bs(top2), len(top2)))
    # placebo: permutar q dentro de dias (rompe la relacion q-win)
    rr = np.random.default_rng(5); ev_pl = []
    for _ in range(100):
        pr = Bp.groupby("dia").q.transform(lambda s: rr.permutation(s.values)); rk = pr / Bp.p; sel = Bp[rk >= rk.quantile(.8)]; ev_pl.append(ev(sel))
    print("  placebo (q permutada por dia, quintil superior): EV media %+.3f sd %.3f" % (np.mean(ev_pl), np.std(ev_pl)))
run("DESC", "HOLD"); run("HOLD", "DESC")
