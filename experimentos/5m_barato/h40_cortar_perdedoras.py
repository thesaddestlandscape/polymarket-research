# H40 (exploratorio, 17-Oct): cortar perdedoras. Regla: a +T s (T=5/30/120) del relleno, si el markout por € <= -θ,
# vender al bid (mid - medio tick) pagando comisión de tomador; si no, mantener a resolución. Con las cachés de H35.
import glob, numpy as np, pandas as pd
D = "/root/polymarket-research-datalogs/m5_maker_banda_deep_peg/"
df = pd.concat(pd.read_csv(f) for f in sorted(glob.glob(D + "unidades_*.csv.gz")))
df = df[(df.lleno > 0) & (df.coste > 0)]
MOT = {"JOIN": "JOIN|C0|CONS|5", "DEEP_k1": "DEEP_k1|C0|CONS|5", "DEEP_k2": "DEEP_k2|C0|CONS|5"}
def ev(g, col):
    return g[col].sum() / g.coste.sum()
for nom, m in MOT.items():
    d = df[df.motor == m].copy()
    if not len(d): continue
    p = d.precio_m.clip(0.02, 0.98)
    coste_salida = (0.005 / p + 0.07 * (1 - p)) * d.coste     # medio tick + comisión tomador, en $ sobre lo invertido
    print(f"\n=== {nom}: unidades con relleno {len(d)} | EV mantener {ev(d, 'pnl'):+.4f} €/€ | días {sorted(d.dia.unique())}")
    for T in (5, 30, 120):
        ok = d[f"mo{T}_n"] > 0
        mo = np.where(ok, d[f"mo{T}_pnl"] / d[f"mo{T}_cost"].replace(0, np.nan), np.nan)   # markout por €
        salida = np.where(ok, d[f"mo{T}_pnl"] / d[f"mo{T}_cost"].replace(0, np.nan) * d.coste - coste_salida, np.nan)
        for th in (0.10, 0.20, 0.30, 0.50):
            corta = ok & (mo <= -th)
            pnl = np.where(corta, salida, d.pnl)
            d["_p"] = pnl
            r = {}
            for parte, sel in (("DESC", d.dia < "2026-10-11"), ("OOS", d.dia >= "2026-10-14")):
                g = d[sel]
                if not len(g): continue
                c = corta[sel.values]
                dias = [(x, (g[g.dia == x]._p.sum() - g[g.dia == x].pnl.sum()) / g[g.dia == x].coste.sum()) for x in sorted(g.dia.unique())]
                r[parte] = (g._p.sum() / g.coste.sum() - ev(g, "pnl"), c.mean(), sum(v > 0 for _, v in dias), len(dias),
                            g[c].pnl.sum() / max(g[c].coste.sum(), 1e-9))
            s = " | ".join(f"{k}: mejora {v[0]:+.4f} €/€ (corta {v[1]:.0%}, días mejor {v[2]}/{v[3]}, EV mantener de las cortadas {v[4]:+.3f})" for k, v in r.items())
            print(f"  T={T:3d}s θ={th:.2f}  {s}")
