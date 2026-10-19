"""Solo lectura: quien rellena las primeras 50 acc tras cruzar 5000 (R5K) y su EV; T y precio en el cruce; in-sample 06-16 vs fuera (05,17,18)."""
import csv, gzip, json, sys, os, datetime, math
from collections import defaultdict
DISC = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/scratch_17oct/vend/out"
VIGC = "/root/polymarket-research-datalogs/vigia_5m_barato_r5k"
AUD = "/root/polymarket-research/experimentos/5m_barato/h43_auditoria_datos"
des = json.load(open(AUD + "/des_cache_descubrimiento.json")); des.update(json.load(open("/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json")))
def banda(d):
    for f in (f"{DISC}/band_{d}.csv.gz", f"{VIGC}/{d}/out/band_{d}.csv.gz"):
        if os.path.exists(f): return f
cum = defaultdict(float)
W = defaultdict(lambda: defaultdict(lambda: [0.0, 0.0, 0.0]))  # per -> maker -> acc,c,p
X = defaultdict(list)   # per -> (T al cruce, pc al cruce, nmk)
unit_pnl = defaultdict(lambda: [0.0, 0.0])
seen = set()
def per(d): return "IN" if "2026-10-06" <= d <= "2026-10-16" else "OUT"
for d in sys.argv[1:]:
    with gzip.open(banda(d), "rt") as fh:
        rd = csv.reader(fh); h = next(rd); ix = {k: i for i, k in enumerate(h)}
        for c in rd:
            if c[ix["act"]] != "BTC": continue
            mkt, lado = c[ix["mkt"]], c[ix["lado_c"]]; acc = float(c[ix["acc"]]); T = float(c[ix["T"]])
            k = (mkt, lado); c0 = cum[k]; cum[k] = c0 + acc
            if acc <= 0 or not (60 < T <= 270): continue
            g = des.get(mkt)
            if g is None: continue
            lo, hi = max(c0 - 5000, 0.0), max(c0 + acc - 5000, 0.0)
            tk = max(min(50, hi) - min(50, lo), 0.0)
            if tk <= 0: continue
            ts = float(c[ix["ts"]]); fin = round((ts + T) / 300) * 300
            dia = datetime.datetime.fromtimestamp(fin, datetime.timezone.utc).strftime("%Y-%m-%d")
            fr = tk / acc; co = float(c[ix["coste"]]) * fr; pn = (acc * (1.0 if g == lado else 0.0) - float(c[ix["coste"]])) * fr
            P = per(dia); w = W[P][c[ix["maker"]]]; w[0] += tk; w[1] += co; w[2] += pn
            u = unit_pnl[(P, dia, mkt, lado)]; u[0] += co; u[1] += pn
            if (dia, mkt, lado) not in seen:
                seen.add((dia, mkt, lado)); X[P].append((T, float(c[ix["pc"]]), int(c[ix["nmk"]] or 0), dia))
for P in ("IN", "OUT"):
    tot = sum(v[0] for v in W[P].values()); top = sorted(W[P].items(), key=lambda kv: -kv[1][0])[:8]
    print(P, "acc", round(tot), "makers", len(W[P]))
    for m, (a, co, pn) in top: print("   ", m[:10], f"share {a/tot:.3f} EV {pn/co:+.3f} acc {a:.0f}")
    t = sorted(x[0] for x in X[P]); p = sorted(x[1] for x in X[P])
    print("   T al cruce p25/50/75", [round(t[int(len(t)*q)]) for q in (.25, .5, .75)], " precio p25/50/75", [round(p[int(len(p)*q)], 3) for q in (.25, .5, .75)])
    us = [v for k, v in unit_pnl.items() if k[0] == P]; C = sum(u[0] for u in us); Pn = sum(u[1] for u in us)
    r = [u[1]/u[0] for u in us]; m_ = sum(r)/len(r); sd = math.sqrt(sum((x-m_)**2 for x in r)/(len(r)-1))
    print(f"   unidades {len(us)} EV pond {Pn/C:+.3f} sd por unidad {sd:.2f}")
# overlap de makers top IN con OUT
inset = {m for m, v in sorted(W['IN'].items(), key=lambda kv: -kv[1][0])[:20]}
outacc = sum(v[0] for v in W['OUT'].values()); ov = sum(v[0] for m, v in W['OUT'].items() if m in inset)
print("share OUT de los top-20 makers IN:", round(ov/outacc, 3))
newm = {m: v for m, v in W['OUT'].items() if m not in W['IN']}
na = sum(v[0] for v in newm.values()); print("share OUT de makers que NO aparecen IN:", round(na/outacc, 3), "EV", round(sum(v[2] for v in newm.values())/max(sum(v[1] for v in newm.values()),1e-9), 3))
