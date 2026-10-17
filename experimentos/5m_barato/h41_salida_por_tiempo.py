# H41 (exploratorio): salida POR TIEMPO de TODO relleno a +T s (al mid - medio tick, comisión de tomador) vs mantener,
# en el MISMO subconjunto (unidades con markout a +T disponible). Cachés de H35.
import glob, numpy as np, pandas as pd
D = "/root/polymarket-research-datalogs/m5_maker_banda_deep_peg/"
df = pd.concat(pd.read_csv(f) for f in sorted(glob.glob(D + "unidades_*.csv.gz")))
df = df[(df.lleno > 0) & (df.coste > 0)]
for nom, m in {"JOIN": "JOIN|C0|CONS|5", "DEEP_k1": "DEEP_k1|C0|CONS|5", "DEEP_k2": "DEEP_k2|C0|CONS|5"}.items():
    d0 = df[df.motor == m]
    print(f"\n=== {nom}")
    for T in (30, 120):
        d = d0[(d0[f"mo{T}_n"] > 0) & (d0[f"mo{T}_cost"] > 0) & (d0[f"mo{T}_miss"] == 0)].copy()
        p = d.precio_m.clip(0.02, 0.98)
        mo = d[f"mo{T}_pnl"] / d[f"mo{T}_cost"]
        d["salida"] = mo * d.coste - (0.005 / p + 0.07 * (1 - p)) * d.coste
        for parte, sel in (("DESC", d.dia < "2026-10-11"), ("OOS ", d.dia >= "2026-10-14")):
            g = d[sel]
            if not len(g): continue
            hold, sal = g.pnl.sum() / g.coste.sum(), g.salida.sum() / g.coste.sum()
            dias = [(g[g.dia == x].salida.sum() - g[g.dia == x].pnl.sum()) / g[g.dia == x].coste.sum() for x in sorted(g.dia.unique())]
            mon = {a: round((h.salida.sum() - h.pnl.sum()) / h.coste.sum(), 3) for a, h in g.groupby("act")}
            print(f"  T={T:3d}s {parte} n={len(g):5d} mantener {hold:+.4f} | salir {sal:+.4f} | dif {sal-hold:+.4f} "
                  f"| días salir>mantener {sum(x > 0 for x in dias)}/{len(dias)} | por moneda {mon}")
