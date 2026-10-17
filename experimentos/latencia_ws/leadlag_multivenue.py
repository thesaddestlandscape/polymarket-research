# Lead-lag de bolsas con NUESTRO reloj de recepción (multivenue_ms, 17-Oct). Para cada moneda: eventos en los que el
# mid de una bolsa se mueve >= U bps respecto a su valor de hace 1 s; para cada evento, cuándo cruza el MISMO umbral y
# sentido cada otra bolsa (ventana ±2 s). Mediana de (t_bolsa − t_evento) y % de veces que la bolsa llega ANTES.
import gzip, glob, os, sys, time, collections, numpy as np
U = float(sys.argv[1]) if len(sys.argv) > 1 else 2.0
mid = collections.defaultdict(list)   # (bolsa, sym) -> [(recv, mid)]
for f in glob.glob("/mnt/HC_Volume_106538179/multivenue_ms/multivenue_ms_2026-10-17_*.csv.gz"):
    try:
        for l in gzip.open(f, "rt"):
            x = l.rstrip("\n").split(",")
            if x[1] != "Q" or not x[4].isdigit(): continue
            try: b, a = float(x[5]), float(x[6])
            except ValueError: continue
            if b > 0 and a > 0 and a >= b: mid[(x[0], x[2])].append((int(x[4]), (a + b) / 2))
    except EOFError: pass
series = {k: (np.array([t for t, _ in sorted(v)]), np.array([m for _, m in sorted(v)])) for k, v in mid.items() if len(v) > 50}
def cruces(t, m):
    """instantes en que el mid se aparta >= U bps de su valor 1 s antes (un evento por segundo y sentido)."""
    ev, ult = [], {1: -1e18, -1: -1e18}
    j = 0
    for i in range(len(t)):
        while t[j] < t[i] - 1000: j += 1
        r = (m[i] / m[j] - 1) * 1e4
        s = 1 if r >= U else (-1 if r <= -U else 0)
        if s and t[i] - ult[s] > 1000:
            ev.append((t[i], s)); ult[s] = t[i]
    return ev
for sym in ("BTC", "ETH", "SOL", "XRP", "DOGE"):
    bolsas = [b for (b, s) in series if s == sym]
    if "binance_perp" not in bolsas: continue
    print(f"\n=== {sym} (umbral {U} bps en 1 s) bolsas: {sorted(bolsas)}")
    ev_ref = cruces(*series[("binance_perp", sym)])
    cr = {b: cruces(*series[(b, sym)]) for b in bolsas}
    for b in sorted(bolsas):
        if b == "binance_perp": continue
        ts = np.array([t for t, _ in cr[b]]); ss = np.array([s for _, s in cr[b]])
        difs = []
        for t0, s0 in ev_ref:
            sel = (np.abs(ts - t0) <= 2000) & (ss == s0) if len(ts) else []
            if len(ts) and sel.any():
                difs.append(int(ts[sel][np.argmin(np.abs(ts[sel] - t0))] - t0))
        if difs:
            d = np.array(difs)
            print(f"  {b:15s} vs binance_perp: eventos perp {len(ev_ref)}, emparejados {len(d)} | t_bolsa − t_perp mediana {np.median(d):+.0f} ms "
                  f"p25/p75 {np.percentile(d,25):+.0f}/{np.percentile(d,75):+.0f} | llega ANTES en {100*(d<0).mean():.0f} %")
