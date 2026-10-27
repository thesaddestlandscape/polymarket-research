#!/usr/bin/env python3
"""a1: para cada relleno MAKER de compra (side 0, taker!=exchange) a p<0,40 en 5m BTC del día D (on-chain), reconstruye con
libro5 (l5_D de e1) el ciclo del nivel (token, B, p): hora del casado (primer descenso del nivel en [ts_est-3,6; ts_est-1,1] s,
calibrado con libro5_tx 24-Oct: ts_est - recep p1 1,12 / p50 2,20 / p99 3,49), alta atribuida (último incremento con
|Δ-acc|<=max(0,02;1 %) antes del casado), edad, profundidad en ticks bajo el mejor bid (de los niveles <0,45) en el alta,
segundos desde la última operación del mercado en el alta, edad del nivel. Tomador «raro» = <20 tx tomadoras BTC 5m ese día.
Salida agentes_datos/replica_ganadora/a1_D.csv.gz. Solo lectura."""
import sys, gzip, csv, os, bisect
sys.path.insert(0, "/root/polymarket-research")
from collections import defaultdict
from analisis_5m_barato_quien_gana import mapas, EXCH
W = "0xb0f85baa97990910a3e8ac2b4a58a322f01ecef5"
SEC = {"0x21f4c1a1be34a39a7bc20985df4b7e5a39fb691d": "21f4", "0x86b14772a4da70f3e6d5eee06933ebef143efc87": "86b1", "0xe29042f5d913dcc4015aab3455c13c58514ca33f": "e290", W: "W"}
DD = "/mnt/HC_Volume_106538179/agentes_datos/replica_ganadora"
for d in sys.argv[1:]:
    out = f"{DD}/a1_{d}.csv.gz"
    if os.path.exists(out) or not os.path.exists(f"{DD}/l5_{d}.csv.gz"): continue
    tok = {t: v for t, v in mapas(d)["5min"].items() if v[0] == "BTC"}
    ntx = defaultdict(set); fills = []
    with gzip.open(f"/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz", "rt") as fh:
        for r in csv.DictReader(fh):
            if r["tipo"] != "F" or r["token_id"] not in tok: continue
            if r["taker"] == EXCH:
                ntx[r["maker"].lower()].add(r["tx"]); continue
            if r["side"] != "0": continue
            acc, usd = float(r["taker_amt"]), float(r["maker_amt"])
            if acc <= 0: continue
            p = usd / acc
            if p >= 0.40: continue
            fills.append((float(r["ts_est"]), r["token_id"], round(p, 2), acc, usd, r["maker"].lower() == W, r["taker"].lower(), SEC.get(r["maker"].lower(), "pob")))
    fills.sort()
    ncnt = {k: len(v) for k, v in ntx.items()}
    size = {}; inc = defaultdict(list); dec = defaultdict(list); best = {}; levels = defaultdict(dict); lastT = {}
    res = []; i = 0; nf = len(fills)
    def evalua(f):
        ts, tk, p, acc, usd, esw, tak, quien = f
        key = (tk, p)
        lo, hi = (ts - 3.6) * 1000, (ts - 1.1) * 1000
        tf = None
        for (t, dl) in dec.get(key, ()):
            if lo <= t <= hi and dl >= 0.5 * acc - 1e-9:
                tf = t; break
        has_tf = tf is not None
        if tf is None: tf = (ts - 2.2) * 1000
        alta = None; prim = None
        for (t, dl, b, la) in reversed(inc.get(key, ())):
            if t >= tf: continue
            prim = t
            if alta is None and abs(dl - acc) <= max(0.02, 0.01 * acc):
                alta = (t, b, la)
        if inc.get(key):
            prim = inc[key][0][0]
        m = tok[tk]
        row = [d, m[2], m[1], m[3], ts, p, round(acc, 4), round(usd, 4), int(esw), int(ncnt.get(tak, 0) < 20), int(has_tf)]
        if alta:
            row += [1, round((tf - alta[0]) / 1000, 3), (round((alta[1] - p) / 0.01) if alta[1] is not None else ""),
                    (round((alta[0] - alta[2]) / 1000, 3) if alta[2] is not None else "")]
        else:
            row += [0, "", "", ""]
        row += [round((tf - prim) / 1000, 3) if prim is not None and prim < tf else "", quien]
        res.append(row)
    with gzip.open(f"{DD}/l5_{d}.csv.gz", "rt") as fh:
        snap_tok = None; snap_t = None; snap_seen = set()
        for ln in fh:
            c = ln.rstrip("\n").split(",")
            k = c[0]
            try:
                t = float(c[1])
            except (ValueError, IndexError):
                continue
            while i < nf and t > (fills[i][0] - 1.0) * 1000:
                evalua(fills[i]); i += 1
            if snap_tok is not None and not (k == "L" and c[2] == snap_tok and t == snap_t):
                for pp in list(levels[snap_tok]):          # niveles que el snapshot no lista -> 0
                    if pp not in snap_seen and levels[snap_tok][pp] > 0:
                        dl = levels[snap_tok][pp]; levels[snap_tok][pp] = 0
                        dec[(snap_tok, pp)].append((snap_t, dl)); inc.pop((snap_tok, pp), None)
                b = [pp for pp, s in levels[snap_tok].items() if s > 0]; best[snap_tok] = max(b) if b else None
                snap_tok = None
            if k == "L":
                tk = c[2]
                if tk not in tok: continue
                try:
                    p = round(float(c[3]), 2); s = float(c[4])
                except ValueError:
                    continue
                if snap_tok == tk: snap_seen.add(p)
                old = levels[tk].get(p, 0.0); levels[tk][p] = s; key = (tk, p)
                if s > old + 1e-9:
                    bb = best.get(tk)
                    if bb is None or p > bb: best[tk] = bb = p
                    L = inc[key]; L.append((t, s - old, bb, lastT.get(tok[tk][1])))
                    if len(L) > 400: del L[:100]
                elif s < old - 1e-9:
                    D = dec[key]; D.append((t, old - s))
                    while D and D[0][0] < t - 12000: D.pop(0)
                    if s <= 1e-9:
                        inc.pop(key, None)
                        if best.get(tk) == p:
                            b = [pp for pp, ss in levels[tk].items() if ss > 0]; best[tk] = max(b) if b else None
            elif k == "R":
                snap_tok = c[2]; snap_t = t; snap_seen = set()
            elif k == "T":
                if c[2] in tok: lastT[tok[c[2]][1]] = t
            elif k == "G":
                if c[2] == "*":
                    inc.clear()
                elif c[2] in tok:
                    for pp in list(levels[c[2]]): inc.pop((c[2], pp), None)
        while i < nf:
            evalua(fills[i]); i += 1
    with gzip.open(out + ".tmp", "wt") as w:
        w.write("dia,cierre,mkt,lado,ts,p,acc,usd,esW,raro,has_tf,alta,edad,prof,tT,edad_nivel,quien\n")
        for r in res: w.write(",".join(map(str, r)) + "\n")
    os.rename(out + ".tmp", out)
    print(d, nf, sum(1 for r in res if r[11]), flush=True)
