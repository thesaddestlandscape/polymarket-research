#!/usr/bin/env python3
"""Validador independiente ALPHA-B (27-Oct). Reimplementacion propia de R1/R2/R3/placebo desde m5_registro crudo.
No lee desenlaces. Uso: vsim.py DIA  -> v_DIA.csv.gz + v_DIA_rate.json"""
import gzip, sys, json, math, datetime, csv, os
from collections import deque, defaultdict
DIA = sys.argv[1]
SRC = '/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz' % DIA
OUT = os.path.dirname(os.path.abspath(__file__)) + '/v_%s.csv.gz' % DIA
SYMS = {'BTC':'BTCUSDT','ETH':'ETHUSDT','SOL':'SOLUSDT','XRP':'XRPUSDT','DOGE':'DOGEUSDT','BNB':'BNBUSDT'}
d0 = datetime.datetime.fromisoformat(DIA + 'T00:00:00+00:00').timestamp()
EPS = 1e-9
def rd(x): return round(x + 1e-12, 2)
def cl(x): return math.ceil(x * 100 - 1e-6) / 100
def fee(p): return 0.07 * p * (1 - p)

class Tok:
    def __init__(o, tok, mk, coin, side, close):
        o.tok, o.mk, o.coin, o.side, o.close = tok, mk, coin, side, close
        o.sym = SYMS[coin]; o.comp = None; o.states = deque(); o.cur = None; o.lastt = -1e18; o.dead = False
        o.te = None; o.be = None; o.sh = 0.0; o.cost = 0.0; o.t1 = None; o.cause = ''; o.tdone = None
        o.shS = 0.0; o.costS = 0.0          # variante cola estricta
        o.shC = 0.0; o.costC = 0.0; o.lastC = None   # variante con regla C (libro cruzado)
        o.nfill = 0; o.nfill_cross = 0; o.nfill_ahead = 0
        o.pend = []                          # (tau, tipo)
        o.d_ask = None; o.d_as = None; o.d_ok = 0
        o.xa = None; o.xrem = 0.0; o.xproc = 0.0; o.xfee = 0.0; o.xmode = ''; o.xq = 0.0; o.xon = False
        o.lastbid = 'none'; o.nrep = 0; o.act_t0 = None; o.act_s = 0.0
        o.fin_mid = None; o.fin_t = None
    def lagst(o, t):
        lim = t - 130.0; s = o.states; best = None
        for st in reversed(s):
            if st[0] <= lim: best = st; break
        if best is None or lim - best[0] > 30000: return None
        return best

class BNs:
    def __init__(b): b.win = deque(); b.dn = deque(); b.up = deque(); b.last = -1e18

U = {}; BYM = {}; BN = defaultdict(BNs); reps_sec = defaultdict(int)

def td(u, t):
    b = BN.get(u.sym)
    if b is None: return False
    L = b.dn if u.side == 'YES' else b.up
    return any(t - 1000 < j <= t - 100 for j in L)

def bidprice(u, t):
    if u.te is None or u.dead: return None
    T = u.close - t / 1000.0
    if T < 60 or T > 290: return None
    if td(u, t): return None
    st = u.lagst(t)
    if st is None: return None
    if not (0.10 - EPS <= st[1] <= 0.29 + EPS and st[2] - st[1] >= 0.02 - EPS): return None
    return rd(st[1] + 0.01)

def try_te(u, t):
    if u.te is not None or u.dead: return
    T = u.close - t / 1000.0
    if T < 60 or T > 290: return
    st = u.lagst(t)
    if st is None or not (0.10 - EPS <= st[1] <= 0.29 + EPS and st[2] - st[1] >= 0.02 - EPS) or td(u, t): return
    u.te = t; u.be = rd(st[1] + 0.01); u.pend.append((t + 250, 'D'))

def track(u, t):   # recotizaciones (cambios de precio/estado de la puja) en eventos
    bp = bidprice(u, t); key = 'none' if bp is None else bp
    if key != u.lastbid:
        u.nrep += 1; reps_sec[int(t // 1000)] += 1
        if u.lastbid == 'none': u.act_t0 = t
        elif key == 'none' and u.act_t0 is not None: u.act_s += (t - u.act_t0) / 1000; u.act_t0 = None
        u.lastbid = key
    return bp

def done_entry(u, t):
    u.tdone = t
    if u.act_t0 is not None: u.act_s += (t - u.act_t0) / 1000; u.act_t0 = None
    if u.sh > EPS: u.pend.append((t + 150, 'X'))

def fire(u, t):
    while True:
        due = sorted(x for x in u.pend if x[0] < t)
        if not due: return
        u.pend = [x for x in u.pend if x[0] >= t]
        for tau, k in due: fire1(u, tau, k)

def fire1(u, tau, k):
        c = u.cur
        ok = c is not None and tau - c[0] <= 30000
        if k == 'D':
            if ok: u.d_ask, u.d_as = c[2], c[4]
            u.d_ok = 1 if ok else -1
        elif k == 'STOP':
            if u.tdone is None and u.te is not None: done_entry(u, tau)
        elif k == 'X':
            avg = u.cost / u.sh; a = cl(avg + 0.01); u.xrem = u.sh; u.xon = True
            if not ok: u.xa = a; u.xmode = 'behind'
            else:
                bb, ba, bs, as_ = c[1], c[2], c[3], c[4]
                if a <= bb + EPS:
                    q = min(u.xrem, bs or 0.0)
                    u.xproc += q * bb; u.xfee += q * fee(bb); u.xrem -= q; a = rd(bb + 0.01)
                u.xa = a
                if a < ba - EPS: u.xmode = 'front'
                elif abs(a - ba) < EPS: u.xmode = 'join'; u.xq = as_ or 0.0
                else: u.xmode = 'behind'
                if u.xrem <= EPS: u.xon = False

def active(u): return u.te is not None and (u.tdone is None or u.shS < 5 - EPS or u.shC < 5 - EPS)

def entry_fill(u, p, sz, t, cause, direct):
    bp = track(u, t) if u.tdone is None else bidprice(u, t)
    if bp is None: return
    if direct and p > bp + EPS: return
    if not direct and p < 1 - bp - EPS: return
    c = u.cur
    q = min(5 - u.sh, sz)
    if u.tdone is None and q > EPS:
        u.sh += q; u.cost += q * bp; u.nfill += 1
        if u.t1 is None: u.t1 = t; u.cause = cause
        if c is not None:
            if c[2] <= bp + EPS: u.nfill_cross += 1
            if c[1] >= bp - EPS: u.nfill_ahead += 1
        if u.sh >= 5 - EPS: done_entry(u, t)
    # variante estricta: solo si nadie por delante en el libro actual
    if c is not None and u.shS < 5 - EPS:
        if c[1] < bp - EPS: qs = sz
        elif abs(c[1] - bp) < EPS: qs = max(0.0, sz - (c[3] or 0.0))
        else: qs = 0.0
        qs = min(5 - u.shS, qs)
        if qs > EPS: u.shS += qs; u.costS += qs * bp
    if u.shC < 5 - EPS:
        qc = min(5 - u.shC, sz); u.shC += qc; u.costC += qc * bp

def exit_fill(u, p, sz, t):
    if not u.xon or u.xrem <= EPS or u.xa is None: return
    a = u.xa; q = 0.0
    if p > a + EPS: q = sz
    elif abs(p - a) < EPS:
        if u.xmode == 'front': q = sz
        elif u.xmode == 'join':
            if u.xq >= sz: u.xq -= sz
            else: q = sz - u.xq; u.xq = 0.0
    q = min(q, u.xrem)
    if q > EPS: u.xproc += q * a; u.xrem -= q

f = gzip.open(SRC, 'rt'); next(f); nl = 0
for ln in f:
    nl += 1; ty = ln[0]
    if ty == 'x':
        c = ln.rstrip('\n').split(',')
        if c[2] not in SYMS.values() or not c[7].strip(): continue
        b = BN[c[2]]; t = float(c[7]); p = float(c[3])
        if t < b.last - 60000: b.win.clear(); b.dn.clear(); b.up.clear()
        elif t < b.last: t = b.last
        b.last = t
        w = b.win
        while len(w) >= 2 and w[1][0] <= t - 300: w.popleft()
        if w and w[0][0] <= t - 300:
            r = (p / w[0][1] - 1) * 1e4
            if r <= -2: b.dn.append(t)
            elif r >= 2: b.up.append(t)
        w.append((t, p))
        while b.dn and b.dn[0] < t - 3000: b.dn.popleft()
        while b.up and b.up[0] < t - 3000: b.up.popleft()
        continue
    if ty == 'k':
        c = ln.rstrip('\n').split(',')
        if c[4] != '5min' or c[2] in U or c[3] not in SYMS or c[7] not in ('YES', 'NO'): continue
        close = datetime.datetime.fromisoformat(c[6]).timestamp()
        if not (d0 + 299 <= close <= d0 + 86401): continue
        u = Tok(c[2], c[5], c[3], c[7], close); U[c[2]] = u
        o = BYM.get((c[5], 'NO' if c[7] == 'YES' else 'YES'))
        if o is not None: u.comp = o; o.comp = u
        BYM[(c[5], c[7])] = u; u.pend.append((close * 1000 - 60000, 'STOP'))
        continue
    if ty not in 'qt': continue
    c = ln.rstrip('\n').split(',')
    u = U.get(c[2])
    if u is None: continue
    rv = (c[7] if ty == 'q' else c[6]).strip()
    t = float(rv) if rv else float(c[1])
    if t < u.lastt - 1000: continue
    u.lastt = max(u.lastt, t)
    end = u.close * 1000 - 2000
    if ty == 'q' and t <= u.close * 1000 and c[3] not in ('', 'None') and c[4] not in ('', 'None'):
        u.fin_mid = (float(c[3]) + float(c[4])) / 2
    if t >= end:
        if not u.dead:
            fire(u, end); u.dead = True
        continue
    v = u.comp
    fire(u, t)
    if v is not None and not v.dead: fire(v, t)
    if ty == 'q':
        if c[3] in ('', 'None') or c[4] in ('', 'None'): continue
        bb, ba = float(c[3]), float(c[4])
        if not bb < ba - EPS: continue
        bs = float(c[5]) if c[5] not in ('', 'None') else None; as_ = float(c[6]) if c[6] not in ('', 'None') else None
        st = (t, bb, ba, bs, as_); u.cur = st; u.states.append(st)
        while len(u.states) >= 2 and u.states[1][0] <= t - 2000: u.states.popleft()
        try_te(u, t)
        if v is not None and not v.dead: try_te(v, t)
        if u.te is not None and u.shC < 5 - EPS:
            bp = track(u, t) if u.tdone is None else bidprice(u, t)
            if bp is not None and ba <= 0.31 + EPS and ba <= bp + EPS and u.lastC != ba and u.shC < 5 - EPS:
                u.lastC = ba; qc = min(5 - u.shC, as_ or 0.0); u.shC += qc; u.costC += qc * bp
    else:
        p = float(c[3]); sd = c[4]; sz = float(c[5])
        try_te(u, t)
        if v is not None and not v.dead: try_te(v, t)
        vok = v is not None and not v.dead and active(v)
        if sd == 'SELL':
            if active(u): entry_fill(u, p, sz, t, 'A', True)
            if v is not None and not v.dead: exit_fill(v, 1 - p, sz, t)
        elif sd == 'BUY':
            exit_fill(u, p, sz, t)
            if vok: entry_fill(v, p, sz, t, 'B', False)
f.close()
rows = []
for u in U.values():
    if not u.dead:
        fire(u, u.close * 1000 - 2000)
    if u.te is None: continue
    rows.append(dict(dia=DIA, mercado=u.mk, coin=u.coin, lado=u.side, cierre=int(u.close), te=u.te, be=u.be,
                     sh=round(u.sh, 6), cost=round(u.cost, 6), t1=u.t1, cause=u.cause, nfill=u.nfill, nfx=u.nfill_cross,
                     nfa=u.nfill_ahead, shS=round(u.shS, 6), costS=round(u.costS, 6), shC=round(u.shC, 6), costC=round(u.costC, 6),
                     d_ask=u.d_ask, d_as=u.d_as, xa=u.xa, xrem=round(u.xrem, 6), xproc=round(u.xproc, 6), xfee=round(u.xfee, 6),
                     xmode=u.xmode, nrep=u.nrep, act_s=round(u.act_s, 2), fin_mid=u.fin_mid))
with gzip.open(OUT, 'wt', newline='') as g:
    w = csv.DictWriter(g, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
vals = sorted(reps_sec.values())
json.dump(dict(dia=DIA, lineas=nl, unidades=len(rows), seg_con_reprecio=len(vals), rep_total=sum(vals),
               rep_p99=vals[int(.99 * len(vals))] if vals else 0, rep_max=vals[-1] if vals else 0),
          open(OUT.replace('.csv.gz', '_rate.json'), 'w'))
print(DIA, nl, len(rows), flush=True)
