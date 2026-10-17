# Rasgos CAUSALES de Binance (aggTrade por RECEPCIÓN) en t0 = rx - H - shift. Solo usa trades con rx_trade <= t0.
import numpy as np, pandas as pd
P = "/tmp/claude-0/-root-polymarket-research/a0c96fc2-2902-4388-9cab-9cffc412228c/scratchpad/pred/"
COINS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]

def load_x(D):
    X = pd.read_csv(P + f"xq_{D}.csv.gz", names=["mon", "T", "p", "q", "m", "E", "rx"], dtype={"mon": str}).dropna()
    X = X.sort_values("rx", kind="stable").drop_duplicates(["mon", "T", "p", "q", "m"], keep="first")
    out = {}
    for mon, g in X.groupby("mon"):
        out[mon] = dict(t=g.rx.values.astype(np.int64), p=g.p.values.astype(np.float64), q=g.q.values.astype(np.float64),
                        m=g.m.values.astype(np.int8))
    return out

class Coin:
    def __init__(s, d):
        s.t, s.p, s.q, s.m = d["t"], d["p"], d["q"], d["m"]
        n = len(s.t); s.n = n
        notl = s.p * s.q
        s.cb = np.concatenate([[0.0], np.cumsum(np.where(s.m == 0, notl, 0.0))])   # agresor comprador (m=0)
        s.cs = np.concatenate([[0.0], np.cumsum(np.where(s.m == 1, notl, 0.0))])   # agresor vendedor (m=1)
        lp = np.log(s.p)
        s.cab = np.concatenate([[0.0], np.cumsum(np.abs(np.diff(lp, prepend=lp[0])))])  # suma |dlogP| por trade
        s.notl = notl
        # tablas dispersas max/min de precio y max de notional
        s.mx = [s.p.astype(np.float32)]; s.mn = [s.p.astype(np.float32)]; s.mq = [notl.astype(np.float32)]
        k = 1
        while (1 << k) <= n:
            h = 1 << (k - 1)
            a, b, c = s.mx[-1], s.mn[-1], s.mq[-1]
            s.mx.append(np.maximum(a[:-h], a[h:])); s.mn.append(np.minimum(b[:-h], b[h:])); s.mq.append(np.maximum(c[:-h], c[h:]))
            k += 1
    def idx(s, t):                       # nº de trades con rx <= t
        return np.searchsorted(s.t, t, side="right")
    def rq(s, tab, i0, i1, fn):          # consulta rango [i0,i1) (vacío -> nan)
        ln = i1 - i0
        ok = ln > 0
        res = np.full(len(i0), np.nan)
        if ok.any():
            lg = np.floor(np.log2(np.maximum(ln, 1))).astype(int)
            for k in np.unique(lg[ok]):
                sel = ok & (lg == k)
                a = tab[k][i0[sel]]; b = tab[k][i1[sel] - (1 << k)]
                res[sel] = fn(a, b)
        return res
    def price_at(s, t):
        i = s.idx(t) - 1
        return np.where(i >= 0, s.p[np.maximum(i, 0)], np.nan), i

def feats(coins, act, sgn, rxv, H, shift=0):
    """act: array de monedas; sgn=-1 (lado YES: adverso = baja) / +1 (NO: adverso = sube); devuelve DataFrame de rasgos."""
    n = len(rxv); t0 = rxv - H - shift
    out = {}
    cols = ["stale", "R100", "R250", "R500", "R1000", "R3000", "R10000", "A100_250", "A250_1000",
            "n100", "n250", "n1000", "n5000", "int_rel", "vol1s", "vol5s", "rng1s", "rng5s", "pos_adv5", "pos_fav5",
            "imb250", "imb1000", "nl250", "nl1000", "maxnl1000", "lastnl", "lastadv", "streak", "dlast2", "R10_last",
            "btcR100", "btcR250", "btcR1000", "btcR3000", "btc_int"]
    F = {c: np.full(n, np.nan) for c in cols}
    for mon in COINS:
        sel = np.where(act == mon)[0]
        if not len(sel) or mon not in coins: continue
        C = coins[mon]; tt = t0[sel]; sg = sgn[sel]
        i1 = C.idx(tt); last = i1 - 1
        ok = last >= 0
        P0 = np.where(ok, C.p[np.maximum(last, 0)], np.nan)
        F["stale"][sel] = np.where(ok, tt - C.t[np.maximum(last, 0)], np.nan)
        def adv(w0, w1):   # retorno adverso entre t0-w0 y t0-w1 (w0>w1)
            pa, _ = C.price_at(tt - w0); pb, _ = C.price_at(tt - w1)
            return sg * (pb - pa) / pa * 1e4
        for w in (100, 250, 500, 1000, 3000, 10000):
            F[f"R{w}"][sel] = adv(w, 0)
        F["A100_250"][sel] = adv(250, 100); F["A250_1000"][sel] = adv(1000, 250)
        def cnt(w): return i1 - C.idx(tt - w)
        for w in (100, 250, 1000, 5000): F[f"n{w}"][sel] = cnt(w)
        r60 = cnt(60000) / 60.0
        F["int_rel"][sel] = np.log1p(cnt(1000)) - np.log1p(r60)
        for w, nm in ((1000, "1s"), (5000, "5s")):
            ia = C.idx(tt - w)
            F[f"vol{nm}"][sel] = (C.cab[i1] - C.cab[np.minimum(ia + 0, C.n)] ) * 1e4
            mxp = C.rq(C.mx, ia, i1, np.maximum); mnp = C.rq(C.mn, ia, i1, np.minimum)
            F[f"rng{nm}"][sel] = (mxp - mnp) / P0 * 1e4
            if nm == "5s":
                F["pos_adv5"][sel] = np.where(sg < 0, (mxp - P0), (P0 - mnp)) / P0 * 1e4
                F["pos_fav5"][sel] = np.where(sg < 0, (P0 - mnp), (mxp - P0)) / P0 * 1e4
        for w in (250, 1000):
            ia = C.idx(tt - w)
            b = C.cb[i1] - C.cb[ia]; s_ = C.cs[i1] - C.cs[ia]
            adv_v = np.where(sg < 0, s_, b); fav_v = np.where(sg < 0, b, s_)
            tot = adv_v + fav_v
            F[f"imb{w}"][sel] = np.where(tot > 0, (adv_v - fav_v) / np.maximum(tot, 1e-12), 0.0)
            F[f"nl{w}"][sel] = np.log1p(tot)
        ia = C.idx(tt - 1000)
        F["maxnl1000"][sel] = np.log1p(np.nan_to_num(C.rq(C.mq, ia, i1, np.maximum), nan=0.0))
        F["lastnl"][sel] = np.log1p(C.notl[np.maximum(last, 0)])
        la = np.where(sg < 0, C.m[np.maximum(last, 0)] == 1, C.m[np.maximum(last, 0)] == 0)
        F["lastadv"][sel] = la.astype(float)
        # racha y últimos movimientos de precio (últimos 6 trades)
        K = 6
        ix = last[:, None] - np.arange(K)[None, :]
        okk = ix >= 1
        pk = C.p[np.maximum(ix, 0)]; pk1 = C.p[np.maximum(ix - 1, 0)]
        d = sg[:, None] * (pk - pk1) / pk * 1e4
        d = np.where(okk, d, np.nan)
        st = np.zeros(len(sel))
        alive = np.ones(len(sel), bool)
        for j in range(K):
            dj = d[:, j]
            nz = np.nan_to_num(dj) != 0
            cont = alive & (np.nan_to_num(dj) > 0)
            st += cont
            alive = alive & (np.nan_to_num(dj) > 0) | (alive & ~nz)    # ceros no rompen la racha
        F["streak"][sel] = st
        F["dlast2"][sel] = np.nansum(d[:, :2], axis=1)
        F["R10_last"][sel] = np.nansum(d, axis=1)
        # BTC (liderazgo cruzado)
        if "BTC" in coins:
            B = coins["BTC"]
            pb0, _ = B.price_at(tt)
            for w in (100, 250, 1000, 3000):
                pa, _ = B.price_at(tt - w)
                F[f"btcR{w}"][sel] = sg * (pb0 - pa) / pa * 1e4
            F["btc_int"][sel] = np.log1p(B.idx(tt) - B.idx(tt - 1000))
    df = pd.DataFrame(F)
    return df

def targets(coins, act, sgn, rxv, H, shift=0):
    n = len(rxv); t0 = rxv - H
    Y = {k: np.full(n, np.nan) for k in ("adv100", "adv_gap")}
    for mon in COINS:
        sel = np.where(act == mon)[0]
        if not len(sel) or mon not in coins: continue
        C = coins[mon]; sg = sgn[sel]; rx = rxv[sel]
        # h26ms: base = ultimo precio <= rx-100, extremo adverso en (rx-100, rx]
        ia = C.idx(rx - 100); ib = C.idx(rx)
        P0 = np.where(ia > 0, C.p[np.maximum(ia - 1, 0)], np.nan)
        mxp = C.rq(C.mx, ia, ib, np.maximum); mnp = C.rq(C.mn, ia, ib, np.minimum)
        ex = np.where(sg < 0, P0 - mnp, mxp - P0) / P0 * 1e4        # adverso = baja (YES) o sube (NO)
        Y["adv100"][sel] = np.where(np.isnan(mxp), 0.0, np.maximum(ex, 0.0))
        # desde t0 (último precio <= t0) hasta rx
        i0 = C.idx(t0[sel]); P1 = np.where(i0 > 0, C.p[np.maximum(i0 - 1, 0)], np.nan)
        mxp = C.rq(C.mx, i0, ib, np.maximum); mnp = C.rq(C.mn, i0, ib, np.minimum)
        ex = np.where(sg < 0, P1 - mnp, mxp - P1) / P1 * 1e4
        Y["adv_gap"][sel] = np.where(np.isnan(mxp), 0.0, np.maximum(ex, 0.0))
    return pd.DataFrame(Y)
