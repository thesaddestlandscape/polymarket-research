#!/usr/bin/env python3
"""r5k_unico.py -- UNA sola definicion y UNA sola fuente para H43 R5K (solo lectura). Misma regla CONGELADA del REGISTRO (17-Oct):
BTC 5m, unidad mercado-lado s; cum_banda(s) = acciones de MAKER (compra de s, o venta de ns a 1-p) con precio equivalente en (0,10;0,30] y T en (60,300];
al cruzar 5000, las K=50 acciones SIGUIENTES (prorrata en la fila que cruza) con T en (60,270], al precio y desenlace reales (sin fees/rebate).
Dos diferencias de PROCEDIMIENTO respecto al vigia, sin efecto sobre la regla: (i) cum global entre ficheros (un mercado que cruza la medianoche no reinicia);
(ii) dia = dia de CIERRE del mercado (no del fichero). Fuente: band_D.csv.gz de pass1.py sobre m5_onchain_D (mismo script para todos los dias).
Uso: python3 r5k_unico.py [--split 2026-10-17] [--hasta D]   (primer dia de descubrimiento 2026-10-06; 05-Oct es parcial y se reporta aparte)
"""
import csv, datetime, glob, gzip, json, os, random, sys
from collections import defaultdict
OFF, K, TMIN, TMAX = 5000.0, 50.0, 60.0, 270.0
HERE = os.path.dirname(os.path.abspath(__file__))
BANDAS = ["/mnt/HC_Volume_106538179/datalogs_analisis_caches/scratch_17oct/vend/out",     # 05-16 Oct (descubrimiento)
          "/root/polymarket-research-datalogs/vigia_5m_barato_r5k/{d}/out"]               # 17-Oct en adelante (vigia)
def banda(d):
    for b in BANDAS:
        f = f"{b.format(d=d)}/band_{d}.csv.gz"
        if os.path.exists(f): return f
def desenlaces():
    des = {}
    for f in (HERE + "/des_cache_descubrimiento.json", "/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json"):
        if os.path.exists(f): des.update(json.load(open(f)))
    return des
def unidades(dias, des):
    cum = defaultdict(float); U = {}; sin = set(); nfilas = defaultdict(int)
    for d in dias:
        f = banda(d)
        if f is None: print("SIN band", d, file=sys.stderr); continue
        with gzip.open(f, "rt") as fh:
            rd = csv.reader(fh); h = next(rd); ix = {k: i for i, k in enumerate(h)}
            for c in rd:
                if c[ix["act"]] != "BTC": continue
                nfilas[d] += 1
                mkt, lado, acc, T = c[ix["mkt"]], c[ix["lado_c"]], float(c[ix["acc"]]), float(c[ix["T"]])
                k = (mkt, lado); c0 = cum[k]; cum[k] = c0 + acc
                if acc <= 0 or not (TMIN < T <= TMAX): continue
                lo, hi = max(c0 - OFF, 0.0), max(c0 + acc - OFF, 0.0)
                tk = max(min(K, hi) - min(K, lo), 0.0)
                if tk <= 0: continue
                g = des.get(mkt)
                if g is None: sin.add(mkt); continue
                ts, co = float(c[ix["ts"]]), float(c[ix["coste"]]); fin = round((ts + T) / 300) * 300
                dia = datetime.datetime.fromtimestamp(fin, datetime.timezone.utc).strftime("%Y-%m-%d")
                fr = tk / acc; u = U.setdefault((dia, mkt, lado), {"dia": dia, "fin": fin, "c": 0.0, "p": 0.0, "acc": 0.0})
                u["c"] += co * fr; u["p"] += (acc * (1.0 if g == lado else 0.0) - co) * fr; u["acc"] += tk
    return list(U.values()), sin, nfilas
def ic(us, key, B=4000, seed=11):
    g = defaultdict(lambda: [0.0, 0.0])
    for u in us: g[u[key]][0] += u["c"]; g[u[key]][1] += u["p"]
    g = list(g.values())
    if len(g) < 3: return None
    r = random.Random(seed); bs = sorted(sum(x[1] for x in m) / sum(x[0] for x in m) for m in ([r.choice(g) for _ in g] for _ in range(B)))
    return (round(bs[int(B * .05)], 3), round(bs[int(B * .95) - 1], 3))
def resumen(us, nom):
    if not us: return print(nom, "n=0")
    c, p = sum(u["c"] for u in us), sum(u["p"] for u in us); pd_ = defaultdict(lambda: [0.0, 0.0, 0])
    for u in us: x = pd_[u["dia"]]; x[0] += u["c"]; x[1] += u["p"]; x[2] += 1
    top = sorted(us, key=lambda u: u["p"], reverse=True)[20:]; mej = sorted(pd_, key=lambda d: pd_[d][1], reverse=True)[:2]
    rest = [v for d, v in pd_.items() if d not in mej]
    f = lambda a, b: round(a / b, 4) if b else None
    print(f"{nom}: n={len(us)} dias={len(pd_)} cierres={len({u['fin'] for u in us})} coste={c:.0f} EV_pond={p/c:+.4f} EV_unidad={sum(u['p']/u['c'] for u in us)/len(us):+.4f} "
          f"IC90_cierre={ic(us,'fin')} IC90_dias={ic(us,'dia')} sin2mejoresdias={f(sum(v[1] for v in rest), sum(v[0] for v in rest))} "
          f"sinTop20={f(sum(u['p'] for u in top), sum(u['c'] for u in top))} px_medio={c/sum(u['acc'] for u in us):.3f}")
    print("   por dia:", " ".join(f"{d[5:]}:{x[1]/x[0]:+.2f}({x[2]})" for d, x in sorted(pd_.items())))
def main():
    a = sys.argv[1:]; split = a[a.index("--split") + 1] if "--split" in a else "2026-10-17"
    hasta = a[a.index("--hasta") + 1] if "--hasta" in a else "2026-10-31"
    dias = [(datetime.date(2026, 10, 5) + datetime.timedelta(days=i)).isoformat() for i in range(0, 26)]
    dias = [d for d in dias if d <= hasta and banda(d)]
    us, sin, nf = unidades(dias, desenlaces())
    print("dias con band:", dias[0], "..", dias[-1], "| mercados sin desenlace:", len(sin))
    resumen([u for u in us if u["dia"] == "2026-10-05"], "05-Oct PARCIAL (fuera del descubrimiento)")
    resumen([u for u in us if "2026-10-06" <= u["dia"] < split], f"IN-SAMPLE 06..{split} (excl.)")
    resumen([u for u in us if split <= u["dia"]], f"FORWARD {split}..")
if __name__ == "__main__":
    main()
