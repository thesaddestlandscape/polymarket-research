import sys; sys.path.insert(0, "/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f6_tipo_tomador/scripts")
from lib import *
U = carga(); PR = pd.read_pickle(D + "e5_preds.pkl"); out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); out.append(s)
for mod in ("CTX+FLOW hgb", "BASE logit (pc,T,hora,moneda,lado)", "CTX logit C=.1"):
    U["ph"] = PR[mod]
    for per, days in (("DISC12-14", ["2026-10-12", "2026-10-13", "2026-10-14"]), ("HOLD", HOLD)):
        S = U[U.dia.isin(days)]
        thr = S.ph.quantile(0.8) if False else None
        # umbral por EUR 20%: cuantil por moneda sobre el propio periodo (descriptivo)
        top = np.zeros(len(S), bool)
        for a in ("ETH", "SOL", "XRP"):
            s = S[S.act == a].sort_values("ph", ascending=False); cs = (s.c.cumsum() / s.c.sum()).values; i = np.searchsorted(cs, 0.2); top[np.where(S.act.values == a)[0][np.argsort(-S.ph.values[S.act.values == a])[:i + 1]]] = True
        S = S.assign(top=top)
        line = f"{mod[:22]:22s} {per:9s} top20%EUR: "
        for nm, m in (("todo", np.ones(len(S), bool)), ("NO-REP", S.nrep.values), ("REP", ~S.nrep.values)):
            a = S[m & S.top.values]; b = S[m & ~S.top.values]
            line += f"[{nm}] top n{len(a)} EV {ev(a.pnl,a.c):+.3f} | resto n{len(b)} EV {ev(b.pnl,b.c):+.3f} ;  "
        d = boot_diff(S, S.top, ~S.top, B=1000); line += f"|| dif top-resto {d[0]:+.3f} IC90cierre ({d[1]:+.3f},{d[2]:+.3f})  %top NO-REP {100*S.nrep[S.top].mean():.0f}% vs {100*S.nrep[~S.top].mean():.0f}%"
        P(line)
open(D + "e7_salida.txt", "w").write("\n".join(out))
