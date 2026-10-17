#!/usr/bin/env python3
"""Pass 1 (solo lectura): por día, rellenos MAKER de la banda H5M (pc in (0,10,0,30], T in (60,300]) con el TOMADOR que cruza,
su acción (vende s / compra no-s), su inventario en el mercado ANTES de la tx y su posición final; trayectoria de precio previa
del token s (on-chain, bloques anteriores). Además resumen diario por wallet (tomador/maker en 5m)."""
import csv, gzip, sys, json
from collections import defaultdict, deque
VOL = "/mnt/HC_Volume_106538179"
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"
d = sys.argv[1]
OUT = sys.argv[2]
tok = {}
with open(OUT + "/../kall.csv") as fh:
    for c in csv.reader(fh):
        # token, act, marco, mkt, fin_iso, lado
        if c[2] != "5min":
            continue
        from datetime import datetime
        fin = datetime.fromisoformat(c[4]).timestamp()
        tok[c[0]] = (c[1], c[3], fin, c[5])
inv = {}            # (wallet, mkt) -> [netY, netN, cash, nf, first_ts]
lastp = defaultdict(lambda: deque(maxlen=400))   # token-lado key (mkt,lado) -> (ts, price of YES-equivalent of that lado)
wstat = defaultdict(lambda: [0, 0.0, 0.0, 0, 0.0, 0.0])  # wallet -> tk_n, tk_acc, tk_usdc, mk_n, mk_acc, mk_usdc
band_takers = defaultdict(set)   # mkt -> set of taker wallets that sold in band
fin_mkt = {}
out = gzip.open(f"{OUT}/band_{d}.csv.gz", "wt")
W = csv.writer(out)
W.writerow(["ts", "tx", "li", "mkt", "act", "lado_c", "pc", "acc", "coste", "T", "maker", "taker", "tk_clase", "tk_side",
            "tk_lado", "tk_acc", "tk_px", "inv_s", "inv_ns", "cash", "nf_prev", "first_ts", "p_s_10", "p_s_30", "p_s_60", "p_s_last", "nmk"])
fin_out = gzip.open(f"{OUT}/finpos_{d}.csv.gz", "wt")
FW = csv.writer(fin_out)
FW.writerow(["mkt", "wallet", "netY", "netN", "cash", "nf", "first_ts"])

def p_hace(mkt, lado, ts, h):
    dq = lastp.get((mkt, lado))
    if not dq:
        return ""
    best = ""
    for t, p in dq:
        if t <= ts - h:
            best = p
        else:
            break
    return best

def precio_s(mkt, lado, ts, h):
    # precio de s desde trades de s (directo) o 1 - precio de no-s
    a = p_hace(mkt, lado, ts, h)
    return a

def aplicar(w, mkt, lado, side, ma, ta, ts):
    k = (w, mkt)
    v = inv.get(k)
    if v is None:
        v = inv[k] = [0.0, 0.0, 0.0, 0, ts]
    if side == 0:
        sh, usd = ta, -ma
    else:
        sh, usd = -ma, ta
    if lado == "YES":
        v[0] += sh
    else:
        v[1] += sh
    v[2] += usd
    v[3] += 1

def registrar_precio(mkt, lado, side, ma, ta, ts):
    acc = ta if side == 0 else ma
    usd = ma if side == 0 else ta
    if acc <= 0:
        return
    p = usd / acc
    lastp[(mkt, lado)].append((ts, p))
    otro = "NO" if lado == "YES" else "YES"
    lastp[(mkt, otro)].append((ts, 1 - p))

buf = []      # filas de la tx actual (sin M)
cur_tx = None
last_prune = 0
def procesar_tx(rows):
    # rows: lista de (tipo, ts, tx, li, maker, taker, side, token, ma, ta)
    mk = [r for r in rows if r[5] != EXCH]
    tkr = [r for r in rows if r[5] == EXCH]
    # mapa taker wallet -> su fila EXCH (puede haber varias match en una tx)
    tkmap = {}
    for r in tkr:
        tkmap.setdefault(r[4], r)
    # snapshot de inventario de tomadores antes de aplicar la tx
    snaps = {}
    for r in mk:
        t = tok.get(r[7])
        if t is None:
            continue
        act, mkt, fin, lado = t
        side, ma, ta, ts = r[6], r[8], r[9], r[1]
        venta = side == 1
        acc = ma if venta else ta
        usdc = ta if venta else ma
        if acc <= 0:
            continue
        lado_c = ("NO" if lado == "YES" else "YES") if venta else lado
        pc = 1 - usdc / acc if venta else usdc / acc
        coste = acc - usdc if venta else usdc
        T = fin - ts
        wstat[r[4]][3] += 1; wstat[r[4]][4] += acc; wstat[r[4]][5] += usdc
        if not (0.10 < pc <= 0.30 and 60 < T <= 300 and coste > 0):
            continue
        tw = r[5]
        tr = tkmap.get(tw)
        if tr is not None and tr[7] in tok:
            tl = tok[tr[7]][3]
            tside = tr[6]
            tacc = tr[9] if tside == 0 else tr[8]
            tusd = tr[8] if tside == 0 else tr[9]
            tpx = tusd / tacc if tacc > 0 else ""
            if tside == 1 and tl == lado_c:
                cl = "VENDE_s"
            elif tside == 0 and tl != lado_c:
                cl = "COMPRA_ns"
            else:
                cl = "RARO"
        else:
            tl, tside, tacc, tpx, cl = "", "", "", "", "SIN_TK"
        k = (tw, mkt)
        if k not in snaps:
            v = inv.get(k)
            snaps[k] = list(v) if v else [0.0, 0.0, 0.0, 0, ""]
        v = snaps[k]
        inv_s = v[0] if lado_c == "YES" else v[1]
        inv_ns = v[1] if lado_c == "YES" else v[0]
        band_takers[mkt].add(tw)
        fin_mkt[mkt] = fin
        W.writerow([ts, r[2], r[3], mkt, act, lado_c, round(pc, 4), acc, round(coste, 5), round(T, 1), r[4], tw, cl, tside, tl,
                    tacc, (round(tpx, 4) if tpx != "" else ""), round(inv_s, 4), round(inv_ns, 4), round(v[2], 4), v[3], v[4],
                    precio_s(mkt, lado_c, ts, 10), precio_s(mkt, lado_c, ts, 30), precio_s(mkt, lado_c, ts, 60),
                    precio_s(mkt, lado_c, ts, 0.001), len(mk)])
    for r in tkr:
        t = tok.get(r[7])
        if t is None:
            continue
        side = r[6]
        acc = r[9] if side == 0 else r[8]
        usd = r[8] if side == 0 else r[9]
        wstat[r[4]][0] += 1; wstat[r[4]][1] += acc; wstat[r[4]][2] += usd
    for r in rows:
        t = tok.get(r[7])
        if t is None:
            continue
        aplicar(r[4], t[1], t[3], r[6], r[8], r[9], r[1])
    for r in tkr:
        t = tok.get(r[7])
        if t is not None:
            registrar_precio(t[1], t[3], r[6], r[8], r[9], r[1])

def podar(now):
    muertos = [m for m, f in fin_mkt.items() if f < now - 900]
    if not muertos:
        return
    ms = set(muertos)
    for (w, m) in [k for k in inv if k[1] in ms]:
        v = inv.pop((w, m))
        if w in band_takers.get(m, ()):
            FW.writerow([m, w, round(v[0], 4), round(v[1], 4), round(v[2], 4), v[3], v[4]])
    for m in muertos:
        fin_mkt.pop(m, None); band_takers.pop(m, None)
        lastp.pop((m, "YES"), None); lastp.pop((m, "NO"), None)

# también podar inventarios de mercados sin banda: por fin del token
fin_all = {}
for t, v in tok.items():
    fin_all[v[1]] = v[2]
def podar_todo(now):
    podar(now)
    ms = {m for m, f in fin_all.items() if f < now - 900}
    for k in [k for k in inv if k[1] in ms and k[1] not in band_takers]:
        inv.pop(k)
    for key in [k for k in lastp if k[0] in ms and k[0] not in band_takers]:
        lastp.pop(key)

nrows = 0
with gzip.open(f"{VOL}/m5_onchain/m5_onchain_{d}.csv.gz", "rt") as fh:
    rd = csv.reader(fh)
    next(rd)
    for c in rd:
        if c[0] != "F":
            continue
        nrows += 1
        try:
            r = ("F", float(c[2]), c[3], int(c[4]), c[6], c[7], int(c[8]), c[9], float(c[10]), float(c[11]))
        except ValueError:
            continue
        if r[2] != cur_tx:
            if buf:
                procesar_tx(buf)
            buf = [r]
            cur_tx = r[2]
            if r[1] - last_prune > 600:
                podar_todo(r[1]); last_prune = r[1]
        else:
            buf.append(r)
if buf:
    procesar_tx(buf)
podar_todo(1e12)
out.close(); fin_out.close()
with gzip.open(f"{OUT}/wstat_{d}.csv.gz", "wt") as fh:
    w = csv.writer(fh)
    w.writerow(["wallet", "tk_n", "tk_acc", "tk_usdc", "mk_n", "mk_acc", "mk_usdc"])
    for k, v in wstat.items():
        w.writerow([k] + [round(x, 3) if isinstance(x, float) else x for x in v])
print(d, "filas F", nrows, file=sys.stderr)
