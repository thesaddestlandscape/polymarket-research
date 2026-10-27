import sys; sys.path.insert(0, "/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f6_tipo_tomador/scripts")
from lib import *
U = carga(); out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); out.append(s)
tk90 = U[U.per == "DISC"].tk_ticket.quantile(0.9)
roi = U.tk_roi_pnl / U.tk_roi_cost.replace(0, np.nan)
ejes = {
 "ndias<=2 vs 5": (U.tk_ndias <= 2, None),
 "ticket grande (>p90 DISC=%.1f)" % tk90: (U.tk_ticket > tk90, None),
 "informado previo (roi>=.02,cost>=50)": ((roi >= 0.02) & (U.tk_roi_cost >= 50), None),
 "perdedor previo (roi<=-.02,cost>=50)": ((roi <= -0.02) & (U.tk_roi_cost >= 50), None),
 "tk_n<=19": (U.tk_n <= 19, None), "tk_n 200-1999": ((U.tk_n >= 200) & (U.tk_n < 2000), None), "tk_n>=2000": (U.tk_n >= 2000, None),
 "tk_n>=20000": (U.tk_n >= 20000, None), "tk_n<=199": (U.tk_n <= 199, None),
 "tk_n 2000-19999": ((U.tk_n >= 2000) & (U.tk_n < 20000), None),
}
P("K POST-HOC declarado = %d ejes (descriptivo, no gate). dif = EV(flag) - EV(~flag); IC90 por cierre." % len(ejes))
for nm, (f, _) in ejes.items():
    f = f.fillna(False).astype(bool); line = [f"{nm:42s}"]
    for per in ("DISC", "HOLD"):
        S = U[U.per == per]; ff = f[S.index]
        if ff.sum() < 100: line.append(per + " n<100"); continue
        d = boot_diff(S, ff, ~ff, B=1000)
        line.append(f"{per}: n {int(ff.sum()):6d} %EUR {100*S.c[ff].sum()/S.c.sum():4.1f} EV {ev(S.pnl[ff],S.c[ff]):+.3f} vs {ev(S.pnl[~ff],S.c[~ff]):+.3f} dif {d[0]:+.3f} ({d[1]:+.3f},{d[2]:+.3f})")
    P(" | ".join(line))
open(D + "e4_salida.txt", "w").write("\n".join(out))
