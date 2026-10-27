"""l0: ledger de B -> tabla de ordenes armadas (armado, cancelacion, relleno). Solo lectura del ledger."""
import json, pandas as pd, numpy as np, datetime as dt
L = "/root/polymarket-research-datalogs/experimento_h47_B_ledger.jsonl"
P, C, R, V, CL, REP = {}, {}, {}, {}, {}, []
def ep(s): return dt.datetime.fromisoformat(s).timestamp()
for l in open(L):
    try: d = json.loads(l)
    except Exception: continue
    t = d["tipo"]; o = d.get("oid")
    if t == "puja_post": P.setdefault(o, d)
    elif t == "post_lat": V[o] = d
    elif t == "intencion_cancel": C.setdefault(o, ep(d["ts"]))
    elif t == "fuera_libro": CL.setdefault(o, (ep(d["ts"]), d.get("origen")))
    elif t == "lectura" and d.get("f", 0) > 0: R.setdefault(o, d)
    elif t == "repega": REP.append(d)
rows = []
for o, d in P.items():
    v = V.get(o, {}); r = R.get(o)
    ta = v.get("t_ret") or d["t_dec"]
    tc = CL.get(o, (None, None))
    rows.append(dict(oid=o, slug=d["slug"], coin=d["coin"], lado=d["lado"], precio=d["precio"], size=d["size"], cola=d["cola"], T_post=d["T"],
                     t_dec=d["t_dec"], t_arm=ta, t_cancel_int=C.get(o), t_out=tc[0], out_origen=tc[1],
                     filled=r is not None, f=(r or {}).get("f", 0.0), espera_s=(r or {}).get("espera_s"), T_fill=(r or {}).get("T"), tras_cancel=(r or {}).get("tras_cancel"),
                     dia=d["ts"][:10], variante=d.get("variante"), k=d.get("k"), n_orden=d.get("n_orden"),
                     bid_dec=(d["libro"]["bids"][0][0] if d["libro"]["bids"] else np.nan), ask_dec=(d["libro"]["asks"][0][0] if d["libro"]["asks"] else np.nan)))
df = pd.DataFrame(rows)
df["vida_s"] = df.t_out - df.t_arm
df["cierre"] = df.slug.str.rsplit("-", n=1).str[1].astype(int) + 300
df.to_pickle("/mnt/HC_Volume_106538179/agentes_datos/b_sin_flujo/ordenes_B.pkl") if __import__("os").makedirs("/mnt/HC_Volume_106538179/agentes_datos/b_sin_flujo", exist_ok=True) is None else None
print(len(df), "ordenes; con relleno", int(df.filled.sum()), "acc llenas", df.f.sum())
print(df.groupby("dia").agg(n=("oid","size"), fills=("filled","sum"), vida_med=("vida_s","median"), vida_p90=("vida_s", lambda x: x.quantile(.9)), Tpost=("T_post","median")))
print(df.vida_s.describe(percentiles=[.1,.25,.5,.75,.9,.99]))
print("vida por filled:", df.groupby("filled").vida_s.describe())
print("fill espera_s:", df.espera_s.describe(percentiles=[.1,.25,.5,.75,.9]))
print("T_post:", df.T_post.describe(percentiles=[.1,.5,.9]))
