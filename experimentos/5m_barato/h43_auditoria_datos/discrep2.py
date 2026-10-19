"""Tabla de discrepancias por causa, escalon a escalon: DISC_ALL (descubrimiento) -> DISC_BTC (solo BTC) -> DISC_BTC_T (T de entrada <=270) -> VIG (cum por fichero + dia de fichero)."""
import sys
from stats import load
from collections import defaultdict
chain=["DISC_ALL","DISC_BTC","DISC_BTC_T","VIG"]
causa={"DISC_BTC":"otra moneda (descubrimiento no filtraba BTC)","DISC_BTC_T":"fila K con T en (270,300] (descubrimiento no filtraba T de entrada)","VIG":"dia de fichero vs dia de cierre / cum reiniciado en medianoche"}
dias=sys.argv[1:]
sets={v:load(v) for v in chain}
def por_dia(v,d):
    g=defaultdict(lambda:[0.0,0.0])
    for u in sets[v]:
        if u["dia"]==d: g[(u["mkt"],u["lado"])]=[u["c"],u["p"]]
    return g
for d in dias:
    print(f"== {d}")
    prev=None
    for v in chain:
        g=por_dia(v,d); n=len(g); c=sum(x[0] for x in g.values()); p=sum(x[1] for x in g.values())
        line=f"  {v:11s} n={n:3d} coste={c:8.2f} pnl={p:+9.2f} EV={p/c:+.4f}" if c else f"  {v}: vacio"
        if prev is not None:
            ks=set(g)|set(prev); dif=[k for k in ks if k not in g or k not in prev or abs(g[k][0]-prev[k][0])>1e-3]
            line+=f" | vs anterior: {len(dif)} unidades cambian ({causa[v]})"
        print(line); prev=g
