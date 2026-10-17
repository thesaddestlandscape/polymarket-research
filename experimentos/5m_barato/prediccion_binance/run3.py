from model import *
import sys
tag = sys.argv[1] if len(sys.argv) > 1 else "ds"
QS = [0.01, 0.02, 0.05, 0.10]
rng = np.random.default_rng(7)
def report(nm, te, sc, oof, higher_is_bad, H):
    for q in QS:
        thr = np.quantile(oof, 1 - q) if higher_is_bad else np.quantile(oof, q)
        av = (sc > thr) if higher_is_bad else (sc < thr)
        a, k = te[av], te[~av]
        if len(a) < 20: continue
        dpnl = -a.pnl.sum()                                 # $ ganados al evitar (pnl evitado negativo => positivo)
        dias = {x: (round(ev(a[a.dia == x]), 3), int((a.dia == x).sum()), round(ev(k[k.dia == x]), 3)) for x in DIAS[2:]}
        ic_a = boot_clu(a, ev, 400); ic_d = boot_clu(te.assign(av=av), lambda s: ev(s[~s.av]) - ev(s[s.av]), 300)
        # sin los 5 cierres con mayor |pnl| evitado
        top = a.groupby("clu").pnl.sum().abs().nlargest(5).index
        a2 = a[~a.clu.isin(top)]
        # azar: mismo nº de rellenos evitados al azar
        r = []
        for _ in range(300):
            ix = rng.choice(len(te), len(a), replace=False); r.append(ev(te.iloc[ix]))
        p = np.mean(np.array(r) <= ev(a))
        print(f"  {nm:8s} H={H} q={q:.2f} av n={len(a):6d} ({len(a)/len(te):.1%} rell, {a.coste.sum()/te.coste.sum():.1%} coste, {a.unit.nunique()} unid) "
              f"EV_ev {ev(a):+.3f} IC90{ic_a.round(3)} | EV_cons {ev(k):+.3f} | dif(cons-ev) IC90 {ic_d.round(3)} | dPnL ${dpnl:+.1f} (tot ${te.pnl.sum():+.1f}) "
              f"| sin top5 cierres EV_ev {ev(a2):+.3f} | dias(EV_ev,n,EV_cons) {dias} | p_azar {p:.3f}", flush=True)
for H in [int(sys.argv[2])]:
    d = load(H, tag); tr = d[d.dia.isin(DIAS[:2])].reset_index(drop=True); te = d[d.dia.isin(DIAS[2:])].reset_index(drop=True)
    print(f"\n=== {tag} H={H} OOS n={len(te)} EV_total {ev(te):+.4f} pnl ${te.pnl.sum():+.1f} | h26ms-oraculo Y1: n={te.Y1.sum()} EV {ev(te[te.Y1==1]):+.3f}, Y3 n={te.Y3.sum()} EV {ev(te[te.Y3==1]):+.3f}")
    for nm, tgt, kind, cols, reg in (("Y1lin", "Y1", "lin", BIN + CODE, False), ("Y3hgb", "Y3", "hgb", BIN + CODE, False), ("EVhgb", "y", "hgb", BIN + CTX, True), ("EVbin", "y", "hgb", BIN + CODE, True),
                                      ("EVctx", "y", "hgb", CTX, True)):
        if tag != "ds" and nm == "EVctx": continue
        sc, oof = fit_score(tr, te, cols, tgt, kind, reg=reg)
        print(f" modelo {nm} AUC OOS (win={int((te.pnl>0).sum())}): corr(score, y)={np.corrcoef(sc, te.y)[0,1]:+.4f}  AUC(-score vs pnl>0)={auc((te.pnl>0).astype(int).values, -sc if reg else sc):.3f}")
        report(nm, te, sc, oof, higher_is_bad=not reg, H=H)
