#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""alpha_miner_b_27oct/sim.py — manda PREREG_ALPHA_B.md (hashes en HASHES.txt).
Simula sobre m5_registro (reloj = RECEPCIÓN) la entrada maker de B (puja virtual 5 acc a bb+0,01 con cancelación TD
Binance), salidas alternativas, placebo y el tomador incondicional (frente 4). NO lee desenlaces (ciego).
Uso: sim.py --dia YYYY-MM-DD [--fichero RUTA] [--out RUTA]   |   sim.py --selftest
"""
import gzip, sys, os, json, math, time, heapq, datetime, csv
from collections import deque

REG = '/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz'
BASE = '/root/polymarket-research/experimentos/5m_barato/alpha_miner_b_27oct/'
SYM = {'BTC': 'BTCUSDT', 'ETH': 'ETHUSDT', 'SOL': 'SOLUSDT', 'XRP': 'XRPUSDT', 'DOGE': 'DOGEUSDT', 'BNB': 'BNBUSDT'}
SYMV = set(SYM.values())
LR = 130.0; LX = 150.0; LT = 250.0
TD_K = 2.0; TD_W = 300.0; TD_C = 100.0; TD_OFF = 1000.0
T_HI = 290.0; T_LO = 60.0; T_END = 2.0; T_DUMP = 30.0
BB_LO = 0.10; BB_HI = 0.29; SPR = 0.02; NSH = 5.0; AGE = 30000.0; E = 1e-9
LIVES = (('P', None, False), ('PC', None, True), ('L1', 1000.0, False), ('L5', 5000.0, False))
ORDS = ('P_X1', 'P_X2', 'P_X3', 'P_XI', 'PC_X1', 'L1_X1', 'L5_X1', 'PL_X1', 'D_X1')
PROBES = ('D', 'DI', 'X4', 'X5', 'X3')


def ceil2(x): return math.ceil(x * 100.0 - 1e-6) / 100.0
def r2(x): return round(x + 1e-12, 2)
def fee(p): return 0.07 * p * (1.0 - p)
def fl(x):
    x = x.strip()
    if x in ('', 'None'): return None
    return float(x)


class BN:
    __slots__ = ('dq', 'last', 'jd', 'ju', 'sec')
    def __init__(s): s.dq = deque(); s.last = -1e18; s.jd = deque(); s.ju = deque(); s.sec = deque()


class Ent:
    __slots__ = ('life', 'cr', 'sh', 'cost', 't1', 'tc', 'tx', 'stop', 'nexta', 'bp', 'npart', 'cause', 'lastx')
    def __init__(s, life, cr=False):
        s.life = life; s.cr = cr; s.sh = 0.0; s.cost = 0.0; s.t1 = None; s.tc = None; s.tx = None; s.stop = False
        s.nexta = None; s.bp = None; s.npart = 0; s.cause = ''; s.lastx = None


class Ord:
    __slots__ = ('a', 'base', 'rem', 'sh0', 'proc', 'fee', 'mode', 'qa', 'placed', 'done', 'tf', 'lastx')
    def __init__(s, a, sh, base):
        s.a = a; s.base = base; s.rem = sh; s.sh0 = sh; s.proc = 0.0; s.fee = 0.0; s.mode = ''; s.qa = 0.0
        s.placed = False; s.done = False; s.tf = None; s.lastx = None


class U:
    __slots__ = ('tok', 'm', 'coin', 'side', 'cie', 'comp', 'hist', 'bb', 'ba', 'bs', 'as_', 'tq', 'last', 'te',
                 'info', 'ent', 'ords', 'pr', 'fin', 'sym')
    def __init__(s, tok, m, coin, side, cie):
        s.tok = tok; s.m = m; s.coin = coin; s.side = side; s.cie = cie; s.comp = None
        s.hist = deque(); s.bb = None; s.ba = None; s.bs = None; s.as_ = None; s.tq = -1e18; s.last = -1e18
        s.te = None; s.info = {}; s.ent = {k: Ent(L, cr) for k, L, cr in LIVES}; s.ords = {}; s.pr = {}; s.fin = False
        s.sym = SYM.get(coin)


class Sim:
    def __init__(s, day):
        s.day = day
        d0 = datetime.datetime.fromisoformat(day + 'T00:00:00+00:00').timestamp()
        s.cmin = d0 + 300 - 1; s.cmax = d0 + 86400 + 1
        s.U = {}; s.other = {}; s.bn = {}; s.heap = []; s.seq = 0; s.now = -1e18; s.out = []
        s.st = dict(lineas=0, sin_recv=0, descartadas_retro=0, reinicios=0, cortadas=0, unidades=0)

    # ---------- utilidades ----------
    def push(s, t, kind, u, arg=None):
        s.seq += 1; heapq.heappush(s.heap, (t, s.seq, kind, u, arg))

    def clock(s, t):
        if t < s.now - 60000:
            s.st['reinicios'] += 1
            keep = []
            for ev in s.heap:
                u = ev[3]
                if u.fin: continue
                if u.te is None: keep.append(ev)
                else: s.write(u, 'cortada'); s.st['cortadas'] += 1
            heapq.heapify(keep); s.heap = keep; s.now = t
            return
        if t > s.now:
            h = s.heap
            while h and h[0][0] < t:
                tau, _, kind, u, arg = heapq.heappop(h)
                if u.fin: continue
                getattr(s, 'ev_' + kind)(u, tau, arg)
            s.now = t

    def lag(s, u, t):
        h = u.hist; lim = t - LR
        while len(h) >= 2 and h[1][0] <= lim: h.popleft()
        if h and h[0][0] <= lim and lim - h[0][0] <= AGE: return h[0]
        return None

    @staticmethod
    def elig(st):
        return BB_LO - E <= st[1] <= BB_HI + E and st[2] - st[1] >= SPR - E

    def tdoff(s, u, t):
        bn = s.bn.get(u.sym)
        if bn is None: return False
        dq = bn.jd if u.side == 'YES' else bn.ju
        for j in reversed(dq):
            if j <= t - TD_OFF: break
            if j <= t - TD_C: return True
        return False

    def chk_te(s, u, t):
        T = u.cie - t / 1000.0
        if not (T_LO <= T <= T_HI): return
        st = s.lag(u, t)
        if st is None or not s.elig(st) or s.tdoff(u, t): return
        u.te = t; be = r2(st[1] + 0.01)
        bn = s.bn.get(u.sym); v60 = None
        if bn is not None and bn.sec:
            si = int((t - 60000) // 1000)
            for (sx, px) in bn.sec:
                if sx >= si:
                    v60 = round(abs(bn.sec[-1][1] / px - 1.0) * 1e4, 3); break
        u.info = dict(te=t, Te=round(T, 2), be=be, bb_e=st[1], ba_e=st[2], bs_e=st[3], as_e=st[4], v60=v60,
                      hora=datetime.datetime.utcfromtimestamp(t / 1000.0).hour)
        s.push(t + LT, 'probe', u, ('D', 0)); s.push(t + LT, 'probe', u, ('DI', 1))
        u.ords['PL_X1'] = Ord(ceil2(be + 0.01), NSH, be); s.push(t + LX, 'xplace', u, 'PL_X1')
        s.st['unidades'] += 1

    def bidp(s, u, e, t):
        if e.tc is not None or e.stop or u.te is None: return None
        T = u.cie - t / 1000.0
        if not (T_LO <= T <= T_HI): return None
        if s.tdoff(u, t): return None
        if e.life is None:
            st = s.lag(u, t)
            if st is None or not s.elig(st): return None
            return r2(st[1] + 0.01)
        if e.nexta is None or t >= e.nexta:
            k = int((t - u.te) // e.life); e.nexta = u.te + (k + 1) * e.life
            st = s.lag(u, t)
            e.bp = r2(st[1] + 0.01) if (st is not None and s.elig(st)) else None
        return e.bp

    # ---------- entrada ----------
    def efill(s, u, k, e, sz, bp, t, cause):
        q = min(NSH - e.sh, sz)
        if q <= E: return
        e.sh += q; e.cost += q * bp; e.npart += 1
        if e.t1 is None: e.t1 = t; e.cause = cause
        if e.sh >= NSH - E:
            e.tc = t; s.entry_done(u, k, t)

    def entry_done(s, u, k, t):
        e = u.ent[k]; e.tx = t; sh = e.sh; avg = e.cost / sh
        if k == 'P':
            u.ords['P_X1'] = Ord(ceil2(avg + 0.01), sh, avg)
            u.ords['P_X2'] = Ord(ceil2(avg + 0.02), sh, avg)
            u.ords['P_X3'] = Ord(ceil2(avg + 0.01), sh, avg)
            u.ords['P_XI'] = Ord(None, sh, avg)
            for nm in ('P_X1', 'P_X2', 'P_X3', 'P_XI'): s.push(t + LX, 'xplace', u, nm)
            s.push(t + LT, 'probe', u, ('X4', 0)); s.push(t + LT, 'probe', u, ('X5', 1))
        else:
            nm = k + '_X1'; u.ords[nm] = Ord(ceil2(avg + 0.01), sh, avg); s.push(t + LX, 'xplace', u, nm)

    def eprint_direct(s, u, p, sz, t):   # SELL del token a p: llena pujas con b' >= p
        for k, e in u.ent.items():
            bp = s.bidp(u, e, t)
            if bp is not None and p <= bp + E: s.efill(u, k, e, sz, bp, t, 'A')

    def eprint_mirror(s, u, p, sz, t):   # BUY del complementario a p: llena pujas con 1-b' <= p
        for k, e in u.ent.items():
            bp = s.bidp(u, e, t)
            if bp is not None and p >= 1.0 - bp - E: s.efill(u, k, e, sz, bp, t, 'B')

    def ecross(s, u, t):
        ba = u.ba
        if ba > 0.31 + E: return
        for k, e in u.ent.items():
            if not e.cr or e.tc is not None or e.stop: continue
            bp = s.bidp(u, e, t)
            if bp is not None and ba <= bp + E and e.lastx != ba:
                e.lastx = ba; s.efill(u, k, e, u.as_ or 0.0, bp, t, 'C')

    # ---------- salida ----------
    def ofill(s, o, q, t, px=None):
        q = min(q, o.rem)
        if q <= E: return
        o.proc += q * (o.a if px is None else px); o.rem -= q
        if o.rem <= E: o.done = True; o.tf = t

    def place(s, u, o, t):
        o.placed = True
        if u.ba is None or t - u.tq > AGE:
            if o.a is None: o.a = r2(o.base - 0.01)
            o.mode = 'behind'; return
        if o.a is None: o.a = max(r2(o.base - 0.01), r2(u.bb + 0.01))
        if o.a <= u.bb + E:     # marcable al llegar: venta tomadora al bid, resto a bb+0,01
            q = min(o.rem, u.bs or 0.0)
            if q > E:
                o.proc += q * u.bb; o.fee += q * fee(u.bb); o.rem -= q
            if o.rem <= E: o.done = True; o.tf = t; return
            o.a = r2(u.bb + 0.01)
        if o.a < u.ba - E: o.mode = 'front'
        elif abs(o.a - u.ba) < E: o.mode = 'join'; o.qa = u.as_ or 0.0
        else: o.mode = 'behind'

    def oprint(s, u, p, sz, t):   # p = precio equivalente de COMPRA del token u
        for o in u.ords.values():
            if not o.placed or o.done: continue
            if p > o.a + E: s.ofill(o, sz, t)
            elif abs(p - o.a) < E:
                if o.mode == 'front': s.ofill(o, sz, t)
                elif o.mode == 'join':
                    if o.qa >= sz: o.qa -= sz
                    else: s.ofill(o, sz - o.qa, t); o.qa = 0.0

    def ocross(s, u, t):
        bb = u.bb
        for o in u.ords.values():
            if not o.placed or o.done: continue
            if bb > o.a + E or (o.mode == 'front' and bb > o.a - E):
                if o.lastx != bb: o.lastx = bb; s.ofill(o, u.bs or 0.0, t)

    # ---------- eventos ----------
    def ev_probe(s, u, tau, arg):
        nm, which = arg
        tk = u if which == 0 else u.comp
        if tk is None or tk.ba is None or tau - tk.tq > AGE: u.pr[nm] = None
        else: u.pr[nm] = (tk.bb, tk.bs, tk.ba, tk.as_)
        if nm == 'D':
            v = u.pr[nm]
            if v is not None and v[3] is not None and v[3] >= NSH - E:
                u.ords['D_X1'] = Ord(ceil2(v[2] + 0.01), NSH, v[2]); s.push(tau + LX, 'xplace', u, 'D_X1')

    def ev_xplace(s, u, tau, nm):
        s.place(u, u.ords[nm], tau)

    def ev_estop(s, u, tau, arg):
        for k, e in u.ent.items():
            if e.tc is None and not e.stop:
                e.stop = True
                if e.sh > E: s.entry_done(u, k, tau)

    def ev_dump(s, u, tau, arg):
        o = u.ords.get('P_X3')
        if o is None or not o.placed or o.done: return
        if u.bb is None or tau - u.tq > AGE:
            u.pr['X3'] = None; o.done = True; return
        u.pr['X3'] = (u.bb, u.bs, u.ba, u.as_)
        q = min(o.rem, u.bs or 0.0)
        if q > E: o.proc += q * u.bb; o.fee += q * fee(u.bb); o.rem -= q
        o.done = True

    def ev_xend(s, u, tau, arg):
        s.write(u, 'ok')

    def write(s, u, why):
        if u.fin: return
        u.fin = True
        if u.te is None: return
        r = {'dia': s.day, 'mercado': u.m, 'coin': u.coin, 'lado': u.side, 'cierre': int(u.cie), 'fin': why}
        r.update(u.info)
        for k, e in u.ent.items():
            r[k + '_sh'] = round(e.sh, 6); r[k + '_cost'] = round(e.cost, 6); r[k + '_t1'] = e.t1
            r[k + '_tc'] = e.tc; r[k + '_tx'] = e.tx; r[k + '_cause'] = e.cause; r[k + '_np'] = e.npart
        for nm in ORDS:
            o = u.ords.get(nm)
            if o is None: continue
            r[nm + '_a'] = o.a; r[nm + '_sh0'] = round(o.sh0, 6); r[nm + '_rem'] = round(o.rem, 6)
            r[nm + '_proc'] = round(o.proc, 6); r[nm + '_fee'] = round(o.fee, 6); r[nm + '_mode'] = o.mode
            r[nm + '_tf'] = o.tf; r[nm + '_placed'] = int(o.placed)
        for nm in PROBES:
            if nm not in u.pr: r[nm] = ''
            else:
                v = u.pr[nm]; r[nm] = 'NA' if v is None else '|'.join('' if x is None else repr(x) for x in v)
        s.out.append(r)

    # ---------- filas ----------
    def on_q(s, u, t, bb, ba, bs, as_):
        if bb is None or ba is None or not (bb < ba - E): return
        u.bb = bb; u.ba = ba; u.bs = bs; u.as_ = as_; u.tq = t
        h = u.hist; h.append((t, bb, ba, bs, as_))
        while len(h) >= 2 and h[1][0] <= t - 2000: h.popleft()
        T = u.cie - t / 1000.0
        if T > T_HI + 1 or T < 0: return
        comp = u.comp
        if u.te is None: s.chk_te(u, t)
        if comp is not None and comp.te is None and not comp.fin: s.chk_te(comp, t)
        if u.te is not None:
            s.ecross(u, t)   # ADENDA1: sin cruce de salida (ocross) y C solo en PC

    def on_t(s, u, t, p, sd, sz):
        comp = u.comp
        T = u.cie - t / 1000.0
        if T > T_HI + 1 or T < 0: return
        if u.te is None: s.chk_te(u, t)
        if comp is not None and comp.te is None and not comp.fin: s.chk_te(comp, t)
        cok = comp is not None and comp.te is not None and not comp.fin
        if sd == 'SELL':
            if u.te is not None: s.eprint_direct(u, p, sz, t)
            if cok: s.oprint(comp, 1.0 - p, sz, t)       # venta del token = compra del comp a 1-p (merge)
        elif sd == 'BUY':
            if u.te is not None: s.oprint(u, p, sz, t)
            if cok: s.eprint_mirror(comp, p, sz, t)      # compra del token = puja del comp a 1-p (espejo)

    def on_x(s, c):
        bn = s.bn.get(c[2])
        if bn is None:
            if c[2] not in SYMV: return
            bn = s.bn[c[2]] = BN()
        rv = c[7].strip()
        if not rv: return
        t = float(rv); p = float(c[3])
        if t < bn.last - 60000: bn.dq.clear(); bn.jd.clear(); bn.ju.clear(); bn.sec.clear()
        elif t < bn.last: t = bn.last
        bn.last = t
        dq = bn.dq; lim = t - TD_W
        while len(dq) >= 2 and dq[1][0] <= lim: dq.popleft()
        if dq and dq[0][0] <= lim:
            r = (p / dq[0][1] - 1.0) * 1e4
            if r <= -TD_K: bn.jd.append(t)
            elif r >= TD_K: bn.ju.append(t)
        dq.append((t, p))
        while bn.jd and bn.jd[0] < t - 3000: bn.jd.popleft()
        while bn.ju and bn.ju[0] < t - 3000: bn.ju.popleft()
        si = int(t // 1000)
        if not bn.sec or bn.sec[-1][0] != si:
            bn.sec.append((si, p))
            while bn.sec[0][0] < si - 120: bn.sec.popleft()

    def run(s, path):
        st = s.st
        with gzip.open(path, 'rt') as f:
            next(f)
            for ln in f:
                st['lineas'] += 1
                ty = ln[0]
                if ty == 'q' or ty == 't':
                    c0 = ln.split(',', 3)
                    u = s.U.get(c0[2])
                    if u is None or u.fin: continue
                    c = ln.rstrip('\n').split(',')
                    rv = c[7] if ty == 'q' else c[6]
                    if rv.strip(): t = float(rv)
                    else: t = float(c[1]); st['sin_recv'] += 1
                    s.clock(t)
                    if u.fin: continue
                    if t < u.last - 1000: st['descartadas_retro'] += 1; continue
                    if t > u.last: u.last = t
                    if ty == 'q': s.on_q(u, t, fl(c[3]), fl(c[4]), fl(c[5]), fl(c[6]))
                    else: s.on_t(u, t, float(c[3]), c[4], float(c[5]))
                elif ty == 'x':
                    s.on_x(ln.rstrip('\n').split(','))
                elif ty == 'k':
                    c = ln.rstrip('\n').split(',')
                    if c[4] != '5min' or c[2] in s.U: continue
                    cie = datetime.datetime.fromisoformat(c[6]).timestamp()
                    if not (s.cmin <= cie <= s.cmax) or c[7] not in ('YES', 'NO'): continue
                    u = U(c[2], c[5], c[3], c[7], cie); s.U[c[2]] = u
                    o = s.other.get((c[5], 'NO' if c[7] == 'YES' else 'YES'))
                    if o is not None: u.comp = o; o.comp = u
                    s.other[(c[5], c[7])] = u
                    s.push(cie * 1000 - 60000, 'estop', u)
                    s.push((cie - T_DUMP) * 1000 + LT, 'dump', u)
                    s.push(cie * 1000 - 2000, 'xend', u)
        for u in s.U.values():
            if not u.fin and u.te is not None: s.write(u, 'eof')

    def dump_csv(s, out):
        keys = []
        for r in s.out:
            for k in r:
                if k not in keys: keys.append(k)
        tmp = out + '.tmp'
        with gzip.open(tmp, 'wt', newline='') as f:
            w = csv.DictWriter(f, fieldnames=keys); w.writeheader()
            for r in s.out: w.writerow(r)
        os.replace(tmp, out)


def selftest():
    d0 = 1792972800
    ms = lambda off: int(round((d0 + off) * 1000))
    L = ['tipo,t_ms,id,c1,c2,c3,c4,c5']
    k = lambda t, tok, mk, end, side: L.append('k,%d,%s,BTC,5min,%s,%s,%s' % (ms(t), tok, mk, end, side))
    q = lambda t, tok, bb, ba, bs, as_: L.append('q,%d,%s,%s,%s,%s,%s,%d' % (ms(t), tok, bb, ba, bs, as_, ms(t)))
    tr = lambda t, tok, p, sd, sz: L.append('t,%d,%s,%s,%s,%s,%d,' % (ms(t), tok, p, sd, sz, ms(t)))
    x = lambda t, p: L.append('x,%d,BTCUSDT,%s,1.0,0,%d,%d' % (ms(t), p, ms(t), ms(t)))
    k(1, 'A', 'M1', '2026-10-26 00:10:00+00:00', 'YES'); k(1, 'B', 'M1', '2026-10-26 00:10:00+00:00', 'NO')
    k(1, 'C', 'M2', '2026-10-26 00:15:00+00:00', 'YES'); k(1, 'D', 'M2', '2026-10-26 00:15:00+00:00', 'NO')
    x(380.0, 100000.0); x(380.2, 100000.0)
    q(400.0, 'A', 0.20, 0.25, 10, 10); q(400.0, 'B', 0.75, 0.80, 10, 10); q(400.2, 'A', 0.20, 0.25, 10, 10)
    tr(401.0, 'A', 0.20, 'SELL', 3); tr(401.5, 'B', 0.80, 'BUY', 2)
    q(402.0, 'A', 0.19, 0.22, 10, 7); q(402.0, 'B', 0.78, 0.81, 7, 10)
    tr(403.0, 'A', 0.22, 'BUY', 4); tr(404.0, 'B', 0.77, 'SELL', 5)
    q(599.0, 'A', 0.19, 0.22, 10, 7)
    q(699.0, 'C', 0.15, 0.20, 10, 10); q(699.0, 'D', 0.80, 0.85, 10, 10); q(699.5, 'C', 0.15, 0.20, 10, 10)
    x(699.6, 100000.0); x(700.0, 99970.0)
    tr(700.5, 'C', 0.15, 'SELL', 10); tr(701.5, 'C', 0.15, 'SELL', 10)
    q(899.0, 'C', 0.15, 0.20, 10, 10)
    p = sys.argv[2] if len(sys.argv) > 2 else '/tmp/selftest_alpha_b.csv.gz'
    with gzip.open(p, 'wt') as f: f.write('\n'.join(L) + '\n')
    S = Sim('2026-10-26'); S.run(p)
    R = {(r['mercado'], r['lado']): r for r in S.out}
    a = R[('M1', 'YES')]; c = R[('M2', 'YES')]
    for kk in ('te', 'be', 'P_sh', 'P_cost', 'P_t1', 'P_tc', 'P_cause', 'P_X1_a', 'P_X1_mode', 'P_X1_proc', 'P_X1_rem',
               'P_X2_proc', 'P_X3_proc', 'P_XI_a', 'P_XI_proc', 'PL_X1_proc', 'D_X1_a', 'D_X1_mode', 'D_X1_rem',
               'L1_sh', 'L1_X1_proc', 'L5_sh', 'D', 'DI', 'X4', 'X5', 'X3'):
        print('A', kk, a.get(kk))
    print('C te', c['te'], 'P_t1', c['P_t1'], 'P_sh', c['P_sh'], 'P_cause', c['P_cause'], 'stats', S.st)
    chk = [a['P_sh'] == 5, abs(a['P_cost'] - 1.05) < 1e-9, a['P_cause'] == 'A', abs(a['P_X1_proc'] - 1.10) < 1e-9,
           abs(a['P_X2_proc'] - 1.15) < 1e-9, abs(a['P_XI_proc'] - 1.05) < 1e-9, abs(a['PL_X1_proc'] - 1.10) < 1e-9,
           a['D_X1_mode'] == 'behind', a['D_X1_rem'] == 5, a['X5'] == '0.75|10.0|0.8|10.0', a['te'] == ms(400.2),
           c['P_t1'] == ms(701.5), c['P_sh'] == 5, a['L1_sh'] == 5, abs(a['L1_X1_proc'] - 1.10) < 1e-9]
    print('SELFTEST', 'OK' if all(chk) else 'FALLO %s' % chk)
    return all(chk)


if __name__ == '__main__':
    if sys.argv[1] == '--selftest':
        sys.exit(0 if selftest() else 1)
    day = sys.argv[sys.argv.index('--dia') + 1]
    src = sys.argv[sys.argv.index('--fichero') + 1] if '--fichero' in sys.argv else REG % day
    out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else BASE + 'units/u_%s.csv.gz' % day
    t0 = time.time(); S = Sim(day); S.run(src); S.dump_csv(out)
    S.st['filas'] = len(S.out); S.st['seg'] = round(time.time() - t0)
    print(json.dumps({'dia': day, **S.st}), flush=True)
