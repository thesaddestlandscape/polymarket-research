import glob, numpy as np, pandas as pd
D = "/root/polymarket-research-datalogs/m5_maker_banda_deep_peg/"
df = pd.concat(pd.read_csv(f) for f in sorted(glob.glob(D + "unidades_*.csv.gz")))
df = df[(df.lleno > 0) & (df.coste > 0) & df.t_fill_s.notna()]
print("t_fill_s ejemplos", df.t_fill_s.describe()[["min", "50%", "max"]].round(1).to_dict())
for nom, m in {"JOIN": "JOIN|C0|CONS|5", "DEEP_k1": "DEEP_k1|C0|CONS|5", "DEEP_k2": "DEEP_k2|C0|CONS|5"}.items():
    d = df[df.motor == m].copy()
    d["tb"] = pd.cut(d.t_fill_s, [0, 90, 120, 150, 180, 210, 240, 270, 310])
    print(f"\n=== {nom} (EV/€ por segundos restantes al primer relleno; DESC 05-10 | OOS 14)")
    for b, g in d.groupby("tb", observed=True):
        a, o = g[g.dia < "2026-10-11"], g[g.dia >= "2026-10-14"]
        dias = [h.pnl.sum() / h.coste.sum() for _, h in a.groupby("dia")]
        print(f"  {str(b):12s} DESC n={len(a):5d} EV {a.pnl.sum()/a.coste.sum():+.3f} días+ {sum(x > 0 for x in dias)}/{len(dias)} | "
              f"OOS n={len(o):4d} EV {o.pnl.sum()/max(o.coste.sum(),1e-9):+.3f}")
