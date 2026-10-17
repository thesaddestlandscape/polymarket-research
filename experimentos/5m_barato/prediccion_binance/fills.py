# Etapa 1: tabla de rellenos con rx (misma lógica de emparejamiento por los DOS tokens que h26ms.py). Solo lectura.
import sys, numpy as np, pandas as pd
B = "/tmp/claude-0/-root-polymarket-research/ca5de530-b5e1-4080-aa20-e0ab73669cdb/scratchpad/B/"
OUT = "/tmp/claude-0/-root-polymarket-research/a0c96fc2-2902-4388-9cab-9cffc412228c/scratchpad/pred/"
for D in sys.argv[1].split(","):
    k = pd.read_csv(B + f"k_{D}.csv.gz", names=["tok", "act", "mkt", "lado"], dtype=str)
    tokmap = {(r.mkt, r.lado): r.tok for r in k.itertuples()}
    T = pd.read_csv(B + f"t_{D}.csv.gz", names=["te", "tok", "p", "side", "q", "rx"], dtype={"tok": str}).dropna(subset=["te", "rx"])
    T["te"] = T.te.astype(np.int64); T["rx"] = T.rx.astype(np.int64)
    rxmap = {}
    for r in T.itertuples(index=False):
        rxmap.setdefault((r.tok, r.te), []).append((r.p, r.q, r.rx))
    F = pd.read_csv(B + f"feat_{D}.csv.gz", dtype={"mkt": str, "wallet": str},
                    usecols=["wallet", "act", "mkt", "lado_c", "pc", "acc", "coste", "pnl", "dia", "cls", "tex_ms", "T", "ts"])
    F = F[F.cls == "exact"].copy()
    rx = []
    for r in F.itertuples(index=False):
        otro = "NO" if r.lado_c == "YES" else "YES"
        ok = []
        for lado, precio in ((r.lado_c, r.pc), (otro, 1 - r.pc)):
            tok = tokmap.get((str(r.mkt), lado))
            for c in (rxmap.get((tok, int(r.tex_ms))) or []) if tok else []:
                if abs(c[0] - precio) < 0.006 and abs(c[1] - r.acc) < 0.02:
                    ok.append(c[2])
        rx.append(ok[0] if len(set(ok)) == 1 else np.nan)
    F["rx"] = rx
    F = F.dropna(subset=["rx"]).copy()
    F["rx"] = F.rx.astype(np.int64)
    F.to_pickle(OUT + f"fills_{D}.pkl")
    print(D, len(F), flush=True)
