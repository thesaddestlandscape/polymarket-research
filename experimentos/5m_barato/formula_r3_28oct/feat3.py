#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""formula_r3_28oct/feat3.py - manda PREREG_FORMULA_R3.md (hashes en HASHES_R3.txt).
Hereda de formula_r2_28oct/sim2.py (load15, fv15) y de alpha_miner_b_27oct/sim.py (congelado, no se toca).
Cada 2 s de reloj de RECEPCION y por token elegible de B (bb retrasado 130 ms en [0,10;0,29], spread>=0,02, T en [60;290] s,
sin TD Binance) guarda el vector de rasgos de informacion a tres retardos LR=130/60/30 ms y la marca de relleno estricto
de una puja a bb+0,01 en los 2 s siguientes (solo ETIQUETA, nunca rasgo). NO lee desenlaces (ciego).
Uso: feat3.py --dia YYYY-MM-DD [--fichero RUTA5m] [--fichero15 RUTA15m] [--outdir DIR]  |  feat3.py --selftest"""
import sys, os, gzip, math, json, time, bisect, datetime
import numpy as np
from collections import deque, Counter
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r2_28oct')
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/alpha_miner_b_27oct')
import sim as S
import sim2 as S2

BASE = '/root/polymarket-research/experimentos/5m_barato/formula_r3_28oct/'
S2.BASE = BASE
TICK = 2000.0
LRS = (130.0, 60.0, 30.0)
HF = (1000.0, 5000.0, 30000.0)
HB = (200.0, 1000.0, 5000.0)
COINS = ('BTC', 'ETH', 'SOL', 'XRP', 'DOGE', 'BNB')
FN = ['lmd', 'spr', 'dq', 'lbs', 'las', 'hasfv', 'dc0', 'dfv1', 'dfv5', 'dfv30', 'dm1', 'dm5', 'dm30',
      'fo1', 'fo5', 'fo30', 'fc1', 'fc5', 'fc30', 'cnt5', 'imp', 'tsl', 'bn02', 'bn1', 'bn5',
      'bl', 'bd1', 'bd5', 'bbn1', 'bbn5']
GN = ['ts', 'mkt', 'coin', 'yes', 'T', 'bbl', 'bal', 'm130', 'fpx', 'fsz', 'fdt']
NAMES = GN + ['%s_%d' % (n, int(lr)) for lr in LRS for n in FN]
NAN = float('nan')


def lgt(v):
    v = min(max(v, 0.001), 0.999)
    return math.log(v / (1.0 - v))


def slog(x):
    return math.copysign(math.log1p(abs(x)), x)


class U3(S.U):
    __slots__ = ('fvc', 'tk15', 'e15', 'j', 'mt', 'mv', 'ft', 'fp', 'fc', 'rs')

    def __init__(self, tok, m, coin, side, cie):
        super().__init__(tok, m, coin, side, cie)
        self.fvc = {}; self.tk15 = -1
        self.e15 = int(math.ceil(cie / 900.0 - 1e-9) * 900); self.j = int(round((cie - (self.e15 - 900)) / 300.0))
        self.mt = []; self.mv = []; self.ft = []; self.fp = []; self.fc = []; self.rs = deque()


class Sim3(S2.Sim2):
    def __init__(self, day):
        S2.Sim2.__init__(self, day)
        S.U = U3
        self.d0 = datetime.datetime.fromisoformat(day + 'T00:00:00+00:00').timestamp()
        self.tk = None; self.seen = set(); self.nU = -1; self.byend = {}; self.btcy = {}
        self.bser = {}; self.buf = deque(); self.blk = []; self.chunks = []; self.cnt = Counter()

    # ---------- utilidades de series
    @staticmethod
    def at(ts, vs, tl, maxage):
        i = bisect.bisect_right(ts, tl) - 1
        if i < 0 or tl - ts[i] > maxage: return None
        return vs[i]

    @staticmethod
    def flow(ts, cum, a, b):
        ib = bisect.bisect_right(ts, b)
        if ib == 0: return 0.0
        ia = bisect.bisect_right(ts, a)
        return cum[ib - 1] - (cum[ia - 1] if ia > 0 else 0.0)

    def ret(self, sy, tl, h):
        L = self.bser.get(sy)
        if L is None: return 0.0
        bt, bp = L[0], L[1]
        p1 = self.at(bt, bp, tl, 10000.0); p0 = self.at(bt, bp, tl - h, 10000.0)
        if p1 is None or p0 is None or p0 <= 0: return 0.0
        return (p1 / p0 - 1.0) * 1e4

    @staticmethod
    def histat(u, tl):
        for e in reversed(u.hist):
            if e[0] <= tl: return e
        return None

    # ---------- eventos (sustituyen a la logica de ordenes de B: aqui solo se observa)
    def on_q(self, u, t, bb, ba, bs, as_):
        if bb is None or ba is None or not (bb < ba - S.E): return
        u.bb = bb; u.ba = ba; u.bs = bs; u.as_ = as_; u.tq = t
        h = u.hist; h.append((t, bb, ba, bs, as_))
        while len(h) >= 2 and h[1][0] <= t - 2000: h.popleft()
        T = u.cie - t / 1000.0
        if T > S.T_HI + 40.0 or T < 0: return
        m = 0.5 * (bb + ba); lm = math.log(m / (1.0 - m))
        if u.mt:
            if t < u.mt[-1]: t = u.mt[-1]
            if lm == u.mv[-1]: return
        u.mt.append(t); u.mv.append(lm)

    def on_t(self, u, t, p, sd, sz):
        if u.ft and t < u.ft[-1]: t = u.ft[-1]
        sg = sz if sd == 'BUY' else -sz
        u.ft.append(t); u.fp.append(p); u.fc.append((u.fc[-1] if u.fc else 0.0) + sg)
        if sd == 'SELL': self.mark(u, p, sz, t)
        elif sd == 'BUY' and u.comp is not None: self.mark(u.comp, round(1.0 - p, 4), sz, t)

    def mark(self, v, pe, sz, t):
        # relleno estricto de una puja a x=bbl+0,01 (cola 0): impresion equivalente pe <= x en los 2 s siguientes al tick
        for r in v.rs:
            d = t - r[0]
            if 0.0 < d <= TICK and pe <= r[5] + 0.01 + 1e-9:
                if r[8] != r[8]: r[8] = pe; r[10] = d
                r[9] += sz

    def on_x(self, c):
        S.Sim.on_x(self, c)
        sy = c[2]
        if sy not in S.SYMV: return
        rv = c[7].strip()
        if not rv: return
        t = float(rv); p = float(c[3])
        L = self.bser.get(sy)
        if L is None: L = self.bser[sy] = [[], [], -1e18]
        bt, bp = L[0], L[1]
        if t < L[2] - 60000: bt.clear(); bp.clear()
        elif t < L[2]: t = L[2]
        L[2] = t
        bt.append(t); bp.append(p)
        if len(bt) > 40000: del bt[:20000]; del bp[:20000]

    def clock(self, t):
        if self.tk is None or t < self.tk - 70000.0:
            self.tk = (math.floor(t / TICK) + 1) * TICK
        while t >= self.tk:
            tk = self.tk; self.tk = tk + TICK
            if t - tk < 20000.0: self.sample(tk)
        S.Sim.clock(self, t)

    def ev_estop(self, u, tau, arg):
        u.fin = True
        u.rs.clear(); u.hist.clear(); u.fvc = {}
        u.mt = []; u.mv = []; u.ft = []; u.fp = []; u.fc = []

    def ev_dump(self, u, tau, arg): return
    def ev_xend(self, u, tau, arg): return
    def write(self, u, why): u.fin = True
    def chk_te(self, u, t): return
    def ecross(self, u, t): return

    # ---------- muestreo
    def sample(self, tk):
        if len(self.U) != self.nU:
            self.nU = len(self.U); self.byend = {}; self.btcy = {}
            for v in self.U.values():
                e = int(round(v.cie)); self.byend.setdefault(e, []).append(v)
                if v.coin == 'BTC' and v.side == 'YES': self.btcy[e] = v
        self.cnt['ticks'] += 1
        end = (int(tk // 300000.0) + 1) * 300
        lst = self.byend.get(end)
        if lst:
            for u in lst:
                if u.fin: continue
                T = u.cie - tk / 1000.0
                if not (S.T_LO <= T <= S.T_HI): continue
                key = (u.tok, int(tk))
                if key in self.seen: self.cnt['dup'] += 1; continue
                st = self.histat(u, tk - S.LR)
                if st is None or st[1] is None or st[2] is None or (tk - S.LR) - st[0] > S.AGE:
                    self.cnt['nostate'] += 1; continue
                if not S.Sim.elig(st): continue
                if self.tdoff(u, tk): self.cnt['td'] += 1; continue
                try:
                    m130 = 0.5 * (st[1] + st[2]); lm130 = math.log(m130 / (1.0 - m130))
                    r = [tk, float(int(u.m)) if str(u.m).isdigit() else -1.0,
                         float(COINS.index(u.coin)) if u.coin in COINS else -1.0,
                         1.0 if u.side == 'YES' else 0.0, T, st[1], st[2], m130, NAN, 0.0, NAN]
                    ok = True
                    for lr in LRS:
                        f = self.feats(u, tk, lr, lm130, end)
                        if f is None: ok = False; break
                        r += f
                except Exception as ex:
                    self.cnt['err'] += 1
                    if self.cnt['err'] <= 3: sys.stderr.write('ERR sample %r\n' % (ex,))
                    continue
                if not ok: self.cnt['nofeat'] += 1; continue
                self.seen.add(key)
                self.buf.append(r); u.rs.append(r)
                while u.rs and tk - u.rs[0][0] > 2500.0: u.rs.popleft()
                self.cnt['rows'] += 1
        while self.buf and tk - self.buf[0][0] > 3000.0:
            self.blk.append(self.buf.popleft())
        if len(self.blk) >= 20000: self.flush()

    def feats(self, u, tk, lr, lm130, end):
        tl = tk - lr
        e = self.histat(u, tl)
        if e is None or e[1] is None or e[2] is None or tl - e[0] > S.AGE: return None
        bb, ba, bs, as_ = e[1], e[2], e[3], e[4]
        m = 0.5 * (bb + ba); lm = math.log(m / (1.0 - m))
        dq = 0.0
        if bs is not None and as_ is not None and bs + as_ > 0: dq = (bs - as_) / (bs + as_)
        f = [lm - lm130, ba - bb, dq, math.log1p(bs) if bs is not None else 0.0,
             math.log1p(as_) if as_ is not None else 0.0]
        fv0 = self.fv15(u, tl)
        if fv0 is None:
            f += [0.0, 0.0, 0.0, 0.0, 0.0]
        else:
            l0 = lgt(fv0); f += [1.0, l0 - lm]
            for h in HF:
                v = self.fv15(u, tl - h)
                f.append(l0 - lgt(v) if v is not None else 0.0)
        for h in HF:
            a = self.at(u.mt, u.mv, tl - h, 60000.0)
            f.append(lm - a if a is not None else 0.0)
        s = u.comp
        for h in HF: f.append(slog(self.flow(u.ft, u.fc, tl - h, tl)))
        for h in HF: f.append(-slog(self.flow(s.ft, s.fc, tl - h, tl)) if s is not None else 0.0)
        n5 = bisect.bisect_right(u.ft, tl) - bisect.bisect_right(u.ft, tl - 5000.0)
        if s is not None: n5 += bisect.bisect_right(s.ft, tl) - bisect.bisect_right(s.ft, tl - 5000.0)
        f.append(math.log1p(n5))
        best = None
        io = bisect.bisect_right(u.ft, tl) - 1
        if io >= 0: best = (u.ft[io], u.fp[io])
        if s is not None:
            ic = bisect.bisect_right(s.ft, tl) - 1
            if ic >= 0 and (best is None or s.ft[ic] > best[0]): best = (s.ft[ic], 1.0 - s.fp[ic])
        if best is not None and tl - best[0] <= 30000.0:
            f.append(max(-0.3, min(0.3, best[1] - m))); f.append(math.log1p((tl - best[0]) / 1000.0))
        else:
            f.append(0.0); f.append(math.log1p(30.0))
        sg = 1.0 if u.side == 'YES' else -1.0
        for h in HB: f.append(sg * self.ret(u.sym, tl, h))
        bu = self.btcy.get(end)
        if u.coin == 'BTC' or bu is None or bu.fin:
            f += [0.0, 0.0, 0.0, 0.0, 0.0]
        else:
            b0 = self.at(bu.mt, bu.mv, tl, 60000.0)
            if b0 is None:
                f += [0.0, 0.0, 0.0]
            else:
                b1 = self.at(bu.mt, bu.mv, tl - 1000.0, 60000.0); b5 = self.at(bu.mt, bu.mv, tl - 5000.0, 60000.0)
                f += [sg * b0, sg * (b0 - b1) if b1 is not None else 0.0, sg * (b0 - b5) if b5 is not None else 0.0]
            f += [sg * self.ret('BTCUSDT', tl, 1000.0), sg * self.ret('BTCUSDT', tl, 5000.0)]
        return f

    def flush(self):
        if not self.blk: return
        A = np.array(self.blk, dtype=np.float64)
        A[:, 0] = A[:, 0] / 1000.0 - self.d0
        self.chunks.append(A.astype(np.float32)); self.blk = []

    def finish(self):
        while self.buf: self.blk.append(self.buf.popleft())
        self.flush()
        return np.concatenate(self.chunks) if self.chunks else np.zeros((0, len(NAMES)), np.float32)


def selftest3():
    d0 = 1792972800
    ms = lambda off: int(round((d0 + off) * 1000))
    L = ['tipo,t_ms,id,c1,c2,c3,c4,c5']
    for tkn, side in (('A', 'YES'), ('B', 'NO')):
        L.append('k,%d,%s,BTC,5min,1001,2026-10-26 00:10:00+00:00,%s' % (ms(1), tkn, side))
    q = lambda t, tk, bb, ba, bs, a: L.append('q,%d,%s,%s,%s,%s,%s,%d' % (ms(t), tk, bb, ba, bs, a, ms(t)))
    tr = lambda t, tk, p, sd, sz: L.append('t,%d,%s,%s,%s,%s,%d,' % (ms(t), tk, p, sd, sz, ms(t)))
    xx = lambda t, p: L.append('x,%d,BTCUSDT,%s,0.1,1,%d,%d' % (ms(t), p, ms(t), ms(t)))
    xx(390.0, 100000.0)
    q(399.0, 'A', 0.20, 0.25, 10, 10); q(399.0, 'B', 0.75, 0.80, 10, 10)
    xx(399.5, 100000.0)
    q(400.2, 'A', 0.20, 0.25, 10, 10)
    xx(400.9, 100050.0)
    tr(401.5, 'A', 0.20, 'SELL', 7)
    tr(405.5, 'B', 0.80, 'BUY', 5)
    tr(407.5, 'A', 0.21, 'SELL', 3)
    q(420.0, 'A', 0.20, 0.25, 10, 10); q(440.0, 'A', 0.20, 0.25, 10, 10)
    os.makedirs(BASE + 'tmp', exist_ok=True)
    p = BASE + 'tmp/selftest3.csv.gz'
    with gzip.open(p, 'wt') as f: f.write('\n'.join(L) + '\n')
    X = Sim3('2026-10-26'); X.run(p); A = X.finish()
    ix = {n: j for j, n in enumerate(NAMES)}
    def row(tk):
        k = np.nonzero(np.abs(A[:, 0] - tk) < 1e-3)[0]
        return A[k[0]] if len(k) else None
    r400, r402, r404, r406 = row(400), row(402), row(404), row(406)
    chk = []
    chk.append(A.shape[1] == len(NAMES) and X.cnt['err'] == 0)
    chk.append(int((A[:, ix['yes']] > 0.5).sum()) == 21 and int((A[:, ix['yes']] < 0.5).sum()) == 0)
    chk.append(r400 is not None and abs(r400[ix['fpx']] - 0.20) < 1e-6 and abs(r400[ix['fsz']] - 7) < 1e-6
               and abs(r400[ix['fdt']] - 1500) < 1e-3 and abs(r400[ix['T']] - 200) < 1e-3)
    chk.append(r402 is not None and r402[ix['fpx']] != r402[ix['fpx']] and r402[ix['fsz']] == 0
               and abs(r402[ix['bn1_130']] - 5.0) < 0.01 and abs(r402[ix['bn02_130']]) < 1e-6)
    chk.append(r404 is not None and abs(r404[ix['fpx']] - 0.20) < 1e-6 and abs(r404[ix['fsz']] - 5) < 1e-6
               and abs(r404[ix['fo5_130']] + math.log1p(7)) < 1e-4)
    chk.append(r406 is not None and abs(r406[ix['fpx']] - 0.21) < 1e-6 and abs(r406[ix['fsz']] - 3) < 1e-6
               and abs(r406[ix['fc1_130']] + math.log1p(5)) < 1e-4)
    chk.append(bool(np.all(np.isfinite(A[:, ix['m130']]))))
    print('SELFTEST3', [int(bool(c)) for c in chk], dict(X.cnt), 'OK' if all(chk) else 'FALLO')
    return all(chk)


if __name__ == '__main__':
    if '--selftest' in sys.argv: sys.exit(0 if selftest3() else 1)
    day = sys.argv[sys.argv.index('--dia') + 1]
    src = sys.argv[sys.argv.index('--fichero') + 1] if '--fichero' in sys.argv else S.REG % day
    p15 = sys.argv[sys.argv.index('--fichero15') + 1] if '--fichero15' in sys.argv else None
    outd = sys.argv[sys.argv.index('--outdir') + 1] if '--outdir' in sys.argv else BASE + 'out/'
    os.makedirs(outd, exist_ok=True)
    t0 = time.time(); X = Sim3(day); X.load15(p15); t1 = time.time(); X.run(src)
    A = X.finish()
    tmp = outd + 'f_%s.tmp.npz' % day
    np.savez_compressed(tmp, X=A, names=np.array(NAMES), d0=np.float64(X.d0))
    os.replace(tmp, outd + 'f_%s.npz' % day)
    ix = {n: j for j, n in enumerate(NAMES)}
    st = dict(X.st); st.update(dict(X.cnt))
    st.update(dia=day, filas=int(len(A)), seg15=round(t1 - t0), seg=round(time.time() - t0), n15=0 if X.T15 is None else int(len(X.T15)))
    if len(A):
        st['por_moneda'] = np.bincount(A[:, ix['coin']].astype(int), minlength=6).tolist()
        st['con_relleno'] = int((A[:, ix['fsz']] > 0).sum()); st['hasfv'] = round(float(A[:, ix['hasfv_130']].mean()), 3)
    print(json.dumps(st), flush=True)
