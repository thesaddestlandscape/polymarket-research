import sys; sys.path.insert(0, "/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f6_tipo_tomador/scripts")
from lib import *
U = carga(); PR = pd.read_pickle(D + "e5_preds.pkl"); out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); out.append(s)
MOD = sys.argv[1] if len(sys.argv) > 1 else "CTX+FLOW logit C=.1"
p = PR[MOD]; U["ph"] = p
Dd = U[U.dia.isin(["2026-10-12", "2026-10-13", "2026-10-14"])]; H = U[U.dia.isin(HOLD)].copy()
P("modelo", MOD, "| DISC test 12-14 n", len(Dd), "HOLD n", len(H))
def politica(S, thr_by_coin):
    return S.ph.values >= S.act.map(thr_by_coin).values
def stats(S, keep, nm, nperm=2000, seed=3):
    sk = ~keep; pnl = S.pnl.values; c = S.c.values
    dP = -pnl[sk].sum(); evr = pnl[keep].sum() / c[keep].sum(); evt = pnl.sum() / c.sum()
    g = pd.DataFrame({"cid": S.cid.values, "dia": S.dia.values, "dp": np.where(sk, -pnl, 0.0), "c": c, "ck": np.where(keep, c, 0.0), "pk": np.where(keep, pnl, 0.0)})
    gc = g.groupby("cid")[["dp", "ck", "pk", "c"]].sum().values; rng = np.random.default_rng(seed); n = len(gc)
    idx = rng.integers(0, n, (2000, n)); s = gc[idx].sum(axis=1); lo, hi = np.percentile(s[:, 0], [5, 95])
    gd = g.groupby("dia")[["dp"]].sum().dp; top2 = gd.sort_values(ascending=False).index[:2]
    sin2 = gd.drop(top2).sum()
    # placebo: retener al azar con la tasa de keep del estrato dia x act x bp
    st = pd.factorize(S.dia.astype(str) + S.act.astype(str) + S.bp.astype(str))[0]; o0 = np.argsort(st, kind="stable"); st_s = st[o0]; ks = keep[o0]; pn = pnl[o0]
    nulls = np.empty(nperm); r2 = np.random.default_rng(seed + 1)
    for b in range(nperm):
        k = np.lexsort((r2.random(len(ks)), st_s)); kk = ks[k]; nulls[b] = -pn[~kk].sum()
    pperm = (nulls >= dP).mean()
    ret_c = c[keep].sum(); dias = S.dia.nunique()
    P(f"  {nm:26s} retiene {100*ret_c/c.sum():5.1f}% EUR ({keep.sum()} u.) EV_ret {evr:+.4f} vs total {evt:+.4f} | dPnL {dP:+8.1f} EUR (haircut50 {dP/2:+.1f}) IC90cierre ({lo:+.1f},{hi:+.1f}) | sin2mejoresdias {sin2:+.1f} | dias>0 {int((gd>0).sum())}/{len(gd)} | placebo p {pperm:.4f} (nulo medio {nulls.mean():+.1f}, p95 {np.percentile(nulls,95):+.1f}) | EUR/dia retenido {ret_c/dias:.0f}")
    return dP, evr
# umbrales en DISC: cuantil por moneda que retiene frac del EUR
def thr_for(frac):
    thr = {}
    for a in ("ETH", "SOL", "XRP"):
        s = Dd[Dd.act == a].sort_values("ph", ascending=False); cs = s.c.cumsum() / s.c.sum(); i = np.searchsorted(cs.values, frac)
        thr[a] = s.ph.values[min(i, len(s) - 1)]
    return thr
P("\n== DISC (test 12-14, solo seleccion del nivel)")
best = None
for fr in (0.5, 0.3, 0.2):
    thr = thr_for(fr); k = politica(Dd, thr); P(" nivel", fr, {a: round(v, 3) for a, v in thr.items()})
    dp, evr = stats(Dd, k, "DISC top %d%%" % (fr * 100), nperm=300)
    if evr > Dd.pnl.sum() / Dd.c.sum() and (best is None or dp > best[1]): best = (fr, dp)
P("nivel elegido en DISC:", best)
P("\n== HOLD (15-20) una pasada: nivel elegido + los otros 2 descriptivos")
for fr in (0.5, 0.3, 0.2):
    thr = thr_for(fr); k = politica(H, thr); tag = "ELEGIDO " if best and fr == best[0] else "descript."
    stats(H, k, f"{tag}top {int(fr*100)}%")
    stats(H, ~k, f"  INVERSION top {int(fr*100)}%", nperm=500)
P("\n== ORACULO (clase real): retener solo NO-REP / retener solo REP")
stats(H, H.nrep.values, "ORACULO retener NO-REP"); stats(H, ~H.nrep.values, "ORACULO retener REP")
stats(Dd, Dd.nrep.values, "ORACULO NO-REP en DISC(12-14)", nperm=500)
# retener solo por moneda (descartar XRP, hallazgo conocido)? no: no es de F6
open(D + "e6_salida_%s.txt" % MOD.replace(" ", "_").replace("+", "p").replace("=", ""), "w").write("\n".join(out))
