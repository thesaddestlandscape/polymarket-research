# H26-MS (misión 5m barato, 17-Oct): ¿en qué ms ANTES del casado real aparece el movimiento de Binance que precede a
# los rellenos maker adversos? Ancla = rx (RECEPCIÓN del trade en nuestro WS: cota superior estricta del casado), no te
# (sello de lote del CLOB, que puede ir cientos de ms antes). Binance por RECEPCIÓN (c[7]). Solo lectura; EXPLORATORIO.
import sys, gzip, numpy as np, pandas as pd
B = "/tmp/claude-0/-root-polymarket-research/ca5de530-b5e1-4080-aa20-e0ab73669cdb/scratchpad/B/"
DIAS = sys.argv[1].split(",")
BINS = [(-3000, -2000), (-2000, -1000), (-1000, -600), (-600, -400), (-400, -300), (-300, -200), (-200, -150),
        (-150, -100), (-100, -50), (-50, 0), (0, 300), (300, 1000), (1000, 2500)]
filas = []
for D in DIAS:
    k = pd.read_csv(B + f"k_{D}.csv.gz", names=["tok", "act", "mkt", "lado"], dtype=str)
    tokmap = {(r.mkt, r.lado): r.tok for r in k.itertuples()}
    T = pd.read_csv(B + f"t_{D}.csv.gz", names=["te", "tok", "p", "side", "q", "rx"], dtype={"tok": str},
                    usecols=[0, 1, 2, 3, 4, 5]).dropna(subset=["te", "rx"])
    T["te"] = T.te.astype(np.int64); T["rx"] = T.rx.astype(np.int64)
    rxmap = {}
    for r in T.itertuples(index=False):
        rxmap.setdefault((r.tok, r.te), []).append((r.p, r.q, r.rx))
    F = pd.read_csv(B + f"feat_{D}.csv.gz", dtype={"mkt": str, "wallet": str},
                    usecols=["wallet", "act", "mkt", "lado_c", "pc", "acc", "coste", "pnl", "dia", "cls", "tex_ms"])
    F = F[F.cls == "exact"].copy()
    rx = []
    for r in F.itertuples(index=False):
        otro = "NO" if r.lado_c == "YES" else "YES"
        ok = []
        for lado, precio in ((r.lado_c, r.pc), (otro, 1 - r.pc)):   # el print sale en el token del TOMADOR
            tok = tokmap.get((str(r.mkt), lado))
            for c in (rxmap.get((tok, int(r.tex_ms))) or []) if tok else []:
                if abs(c[0] - precio) < 0.006 and abs(c[1] - r.acc) < 0.02:
                    ok.append(c[2])
        v = ok[0] if len(set(ok)) == 1 else np.nan
        rx.append(v)
    F["rx"] = rx
    F = F.dropna(subset=["rx"])
    X = pd.read_csv(B + f"x_{D}.csv.gz", names=["mon", "t", "p"], dtype={"mon": str}).dropna().sort_values("t")
    bn = {m: (g.t.values.astype(np.int64), g.p.values.astype(float)) for m, g in X.groupby("mon")}
    for r in F.itertuples(index=False):
        if r.act not in bn:
            continue
        t, p = bn[r.act]
        fila = {"dia": r.dia, "act": r.act, "coste": r.coste, "pnl": r.pnl, "lat": r.rx - r.tex_ms,
                "unidad": f"{r.wallet}|{r.mkt}|{r.lado_c}"}
        for a, b in BINS:
            A, Bb = r.rx + a, r.rx + b
            i0 = int(np.searchsorted(t, A, side="right")); i1 = int(np.searchsorted(t, Bb, side="right"))
            if i0 == 0 or t[i0 - 1] < A - 60000:
                fila[f"b{a}"] = np.nan; continue
            p0 = p[i0 - 1]; seg = p[i0:i1]
            if not len(seg):
                fila[f"b{a}"] = 0.0; continue
            fila[f"b{a}"] = (p0 - seg.min()) / p0 * 1e4 if r.lado_c == "YES" else (seg.max() - p0) / p0 * 1e4
        filas.append(fila)
    print(D, "rellenos exactos con rx", len(F), flush=True)
df = pd.DataFrame(filas)
print("\nrx - te (ms): p10/50/90", np.percentile(df.lat, [10, 50, 90]).round(0), "n", len(df))
def ev(d):
    return d.pnl.sum() / d.coste.sum() if d.coste.sum() > 0 else np.nan
def ic_dias(d, rng=np.random.default_rng(1)):
    dias = d.dia.unique()
    bs = []
    for _ in range(2000):
        s = rng.choice(dias, len(dias))
        dd = pd.concat([d[d.dia == x] for x in s])
        bs.append(ev(dd))
    return np.percentile(bs, [5, 95]).round(3)
print(f"\nTOTAL EV/€ {ev(df):+.4f} n {len(df)}  días {sorted(df.dia.unique())}")
for umbral in (1.0, 2.0):
    print(f"\n=== Binance en contra >= {umbral} bp dentro del tramo (relativo a rx) ===")
    for a, b in BINS:
        c = df[f"b{a}"]
        si, no = df[c >= umbral], df[(c < umbral) & c.notna()]
        if len(si) < 200:
            print(f"  [{a:+5d},{b:+5d}) ms  contra n={len(si)} (poco)"); continue
        dif = ev(si) - ev(no)
        diario = [round(ev(si[si.dia == x]) - ev(no[no.dia == x]), 3) for x in sorted(df.dia.unique())]
        print(f"  [{a:+5d},{b:+5d}) ms  contra n={len(si):6d} EV {ev(si):+.3f} | resto {ev(no):+.3f} | dif {dif:+.3f} "
              f"días(dif<0) {sum(x < 0 for x in diario)}/{len(diario)} {diario}")
