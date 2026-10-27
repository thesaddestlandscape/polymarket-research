#!/usr/bin/env python3
"""n2 (H-NIDO15 para mo-money, 05-14 Oct, caché rellenos_D de analisis_mo_money_pares_5m): cuota de $ en el lado s implicado
por TWAP60 oficial en los 5m que cierran con un 15m, EV s vs ¬s, por rol y banda. Solo lectura."""
import sys, glob
sys.path.insert(0, "/root/polymarket-research"); sys.argv = [sys.argv[0]]
exec(open("/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/wallet_mecanismos_26oct/scripts/n1_nido.py").read().split("W = pd.read_csv")[0])
R = pd.concat([pd.read_csv(f, dtype={"mkt": str}) for f in sorted(glob.glob("/root/polymarket-research-datalogs/mo_money/rellenos_*.csv.gz"))])
R = R[R.compra].copy(); des = desenlaces(set(R.mkt)); R["des"] = R.mkt.map(des)
print("cobertura", R.des.notna().mean()); R = R[R.des.notna()]
R["win"] = (R.lado == R.des).astype(float); R["usd"] = R.usdc; R["pnl"] = R.win * R.acc - R.usd - R.fee
R["dc"] = pd.to_datetime(R.cierre, unit="s").dt.strftime("%m-%d")
for d in sorted(set(pd.to_datetime(R.cierre - 900, unit="s").dt.strftime("%Y-%m-%d"))): cargar_tw(d)
R["nido"] = R.cierre % 900 == 0
g = [((tw.get((a, c - 900)) or np.nan) - (tw.get((a, c - 300)) or np.nan)) / (tw.get((a, c - 300)) or np.nan) * 1e4 if n else np.nan for a, c, n in zip(R.act, R.cierre, R.nido)]
R["gap"] = g; R["ens"] = R.nido & (R.gap.abs() >= 1) & (R.lado == np.where(R.gap > 0, "YES", "NO")); R["nos"] = R.nido & (R.gap.abs() >= 1) & ~R.ens
print("cuota nido $", round(R[R.nido].usd.sum() / R.usd.sum(), 3), "cobertura refs", round(R[R.nido].gap.notna().mean(), 3))
for rol in ("M", "T"):
    for lo, hi in ((0, .3), (.3, .7), (.7, 1.01)):
        S = R[(R.rol == rol) & (R.p >= lo) & (R.p < hi)]
        print(f"\n{rol} p[{lo},{hi}) todo {ev(S)}\n  no-nido {ev(S[~S.nido])}\n  nido s  {ev(S[S.ens])}  cuota s={S[S.ens].usd.sum()/max(S[S.ens|S.nos].usd.sum(),1e-9):.2f}\n  nido ¬s {ev(S[S.nos])}")
