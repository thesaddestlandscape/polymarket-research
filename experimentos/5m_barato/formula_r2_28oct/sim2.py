#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""formula_r2_28oct/sim2.py — manda PREREG_FORMULA_R2.md. Hereda de alpha_miner_b_27oct/sim.py (congelado, no se toca).
Puja virtual 5 acc a bb_retrasado+delta (delta en +0,01; 0; -0,01; -0,02), reposicionada con el estado retrasado como la vida P de B,
cancelacion TD de B, parada a T=60 s, reloj de RECEPCION. Relleno estricto: travesia (pe<x) rellena; en el nivel (pe=x) solo con cola:
delta=+0,01 cola 0; delta=0 cola=bs visible al reposicionar; delta<0 nunca (cola no observable). Cotas optimistas O_* (cola 0).
Compuerta eps=q^-mid (q^=sigma(logit m + A2*dC15 + A3*dQ), coef fijados de R1 clase E). No lee desenlaces (ciego)."""
import sys, os, gzip, math, json, time, datetime, subprocess, glob
import numpy as np
from statistics import NormalDist
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/alpha_miner_b_27oct')
import sim as S

E = 1e-9; INF = 1e18
A2 = 0.026; A3 = 0.085
ND = NormalDist()
R15 = '/mnt/HC_Volume_106538179/m15_registro/m15_registro_%s.csv.gz'
BASE = '/root/polymarket-research/experimentos/5m_barato/formula_r2_28oct/'
AWKBIN = os.environ.get('AWKBIN', 'awk')
DELTAS = (('p1', 0.01), ('z0', 0.0), ('m1', -0.01), ('m2', -0.02))
GATES = (('U', 'N', 0.0), ('G10', 'L', -0.010), ('G5', 'L', -0.005), ('GP5', 'L', 0.005), ('I5', 'H', 0.005))
LIVES2 = tuple((g + '_' + d, dl, gk, cut, False) for g, gk, cut in GATES for d, dl in DELTAS) + \
    (('O_z0', 0.0, 'N', 0.0, True), ('O_m1', -0.01, 'N', 0.0, True), ('O_m2', -0.02, 'N', 0.0, True))
AWK15 = r'''BEGIN { n = 0 }
$1 == "k" { if ($5 == "15min") { if (!($3 in ID)) ID[$3] = n++; print $3 "|" ID[$3] "|" $4 "|" $8 "|" $7 > KF }; next }
$1 == "q" {
  tok = $3
  if (!(tok in ID)) ID[tok] = n++
  r = $8; if (r == "") r = $2
  b = int(r / 250)
  if ((tok in LB) && LB[tok] != b) print ID[tok], LR[tok], LM[tok]
  LB[tok] = b; LR[tok] = r
  if ($4 ~ /^[0-9.]+$/ && $5 ~ /^[0-9.]+$/ && ($4 + 0) < ($5 + 0)) LM[tok] = ($4 + $5) / 2; else LM[tok] = -1
}
END { for (t in LB) print ID[t], LR[t], LM[t] }'''


class Ent2(S.Ent):
    __slots__ = ('name', 'delta', 'gk', 'cut', 'opt', 'px', 'qrem')
    def __init__(self, name, delta, gk, cut, opt):
        S.Ent.__init__(self, None, False)
        self.name = name; self.delta = delta; self.gk = gk; self.cut = cut; self.opt = opt; self.px = None; self.qrem = 0.0


class U2(S.U):
    __slots__ = ('fvc', 'tk15', 'e15', 'j', 'lbb', 'tchg')
    def __init__(self, tok, m, coin, side, cie):
        super().__init__(tok, m, coin, side, cie)
        self.ent = {nm: Ent2(nm, dl, gk, cut, opt) for nm, dl, gk, cut, opt in LIVES2}
        self.fvc = {}; self.tk15 = -1; self.lbb = None; self.tchg = -1e18
        self.e15 = int(math.ceil(cie / 900.0 - 1e-9) * 900); self.j = int(round((cie - (self.e15 - 900)) / 300.0))


class Sim2(S.Sim):
    def __init__(self, day):
        S.Sim.__init__(self, day)
        S.U = U2
        self.T15 = None; self.M15 = None; self.off = {}; self.map15 = {}

    def load15(self, p=None):
        p = p or (R15 % self.day)
        if not os.path.exists(p):
            g = glob.glob('/mnt/HC_Volume_106538179/**/m15_registro_%s*' % self.day, recursive=True)
            if not g:
                sys.stderr.write('SIN m15 %s\n' % self.day); return
            p = g[0]
        d = BASE + 'tmp/'; os.makedirs(d, exist_ok=True)
        tag = '%s_%d' % (self.day, os.getpid()); kf = d + 'k15_' + tag + '.txt'; df = d + 'd15_' + tag + '.txt'
        cmd = "nice -n 19 ionice -c3 zcat '%s' | %s -F, -v KF='%s' '%s' > '%s'" % (p, AWKBIN, kf, AWK15, df)
        subprocess.run(['bash', '-c', cmd], check=True)
        A = np.fromfile(df, sep=' ') if os.path.getsize(df) > 0 else np.zeros(0)
        os.remove(df)
        if A.size >= 3:
            A = A[: (A.size // 3) * 3].reshape(-1, 3)
            A = A[(A[:, 2] > 0.0) & (A[:, 2] < 1.0)]
            A = A[np.lexsort((A[:, 1], A[:, 0]))]
            tid = A[:, 0].astype(np.int64)
            self.T15 = np.ascontiguousarray(A[:, 1]); self.M15 = A[:, 2].astype(np.float32)
            ids, idx, cnt = np.unique(tid, return_index=True, return_counts=True)
            self.off = {int(i): (int(a), int(a + c)) for i, a, c in zip(ids, idx, cnt)}
            del A, tid
        if os.path.exists(kf):
            for ln in open(kf):
                q = ln.rstrip('\n').split('|')
                if len(q) < 5: continue
                try: e15 = int(datetime.datetime.fromisoformat(q[4]).timestamp())
                except Exception: continue
                self.map15[(q[2], q[3], e15)] = int(q[1])
            os.remove(kf)

    def mid15(self, tid, tms, maxage):
        o = self.off.get(tid)
        if o is None: return None
        lo, hi = o
        i = int(np.searchsorted(self.T15[lo:hi], tms, side='right')) - 1
        if i < 0 or tms - self.T15[lo + i] > maxage: return None
        return float(self.M15[lo + i])

    def fv15(self, u, tl):
        if self.T15 is None: return None
        b = int(tl // 250)
        c = u.fvc
        if b in c: return c[b]
        tid = u.tk15
        if tid == -1:
            tid = self.map15.get((u.coin, u.side, u.e15), -2); u.tk15 = tid
        v = None
        if tid >= 0:
            m = self.mid15(tid, tl, 15000.0)
            if m is not None and 0.02 < m < 0.98:
                ts = tl / 1000.0; T15 = u.e15 - ts; T5 = u.cie - ts
                if T15 > 1.0 and T5 > 1.0:
                    zc = ND.inv_cdf(m); w = None
                    if u.j <= 1: w = math.sqrt(T15) * zc / math.sqrt(T5)
                    else:
                        m0 = self.mid15(tid, (u.cie - 300.0) * 1000.0, 30000.0)
                        if m0 is not None and 0.02 < m0 < 0.98:
                            w = (math.sqrt(T15) * zc - math.sqrt(u.e15 - (u.cie - 300.0)) * ND.inv_cdf(m0)) / math.sqrt(T5)
                    if w is not None: v = ND.cdf(w)
        if len(c) > 4000: c.clear()
        c[b] = v
        return v

    def eps(self, u, st, tl):
        bb, ba, bs, as_ = st[1], st[2], st[3], st[4]
        m = 0.5 * (bb + ba); lg = math.log(m / (1.0 - m))
        dq = 0.0
        if bs is not None and as_ is not None and bs + as_ > 0: dq = (bs - as_) / (bs + as_)
        fv = self.fv15(u, tl); dc = 0.0
        if fv is not None:
            fv = min(max(fv, 0.001), 0.999); dc = math.log(fv / (1.0 - fv)) - lg
        qh = 1.0 / (1.0 + math.exp(-(lg + A2 * dc + A3 * dq)))
        return qh - m, dc, dq, fv is not None

    def ctx(self, u, t):
        if u.te is None: return None
        T = u.cie - t / 1000.0
        if not (S.T_LO <= T <= S.T_HI): return None
        if self.tdoff(u, t): return None
        st = self.lag(u, t)
        if st is None or not self.elig(st): return None
        return st, self.eps(u, st, t - S.LR)[0]

    @staticmethod
    def price(e, cx):
        if cx is None or e.tc is not None or e.stop: return None
        st, ep = cx; gk = e.gk
        if gk == 'L' and ep < e.cut: return None
        if gk == 'H' and ep > e.cut: return None
        return S.r2(st[1] + e.delta)

    @staticmethod
    def repeg(e, bp, st):
        e.px = bp
        if e.opt or e.delta > E: e.qrem = 0.0
        elif e.delta > -E: e.qrem = float(st[3]) if st[3] is not None else INF
        else: e.qrem = INF

    def eprint(self, u, pe, sz, t, cause):
        cx = self.ctx(u, t)
        for k, e in u.ent.items():
            bp = self.price(e, cx)
            if bp is None:
                e.px = None; continue
            if e.px is None or abs(bp - e.px) > E: self.repeg(e, bp, cx[0])
            if pe < bp - E: self.efill(u, k, e, sz, bp, t, cause)
            elif pe <= bp + E and e.qrem < INF / 2:
                c = min(e.qrem, sz); e.qrem -= c
                if sz - c > E: self.efill(u, k, e, sz - c, bp, t, cause)

    def eprint_direct(self, u, p, sz, t): self.eprint(u, p, sz, t, 'A')
    def eprint_mirror(self, u, p, sz, t): self.eprint(u, 1.0 - p, sz, t, 'B')
    def ecross(self, u, t): return
    def entry_done(self, u, k, t): u.ent[k].tx = t

    def chk_te(self, u, t):
        T = u.cie - t / 1000.0
        if not (S.T_LO <= T <= S.T_HI): return
        st = self.lag(u, t)
        if st is None or not self.elig(st) or self.tdoff(u, t): return
        u.te = t
        ep, dc, dq, fa = self.eps(u, st, t - S.LR)
        u.info = dict(te=t, Te=round(T, 2), bb_e=st[1], ba_e=st[2], bs_e=st[3], as_e=st[4], eps_e=round(ep, 6),
                      dc_e=round(dc, 5), dq_e=round(dq, 5), fv_e=int(fa),
                      hora=datetime.datetime.fromtimestamp(t / 1000.0, datetime.timezone.utc).hour)
        self.st['unidades'] += 1

    def on_q(self, u, t, bb, ba, bs, as_):
        S.Sim.on_q(self, u, t, bb, ba, bs, as_)
        if u.te is None or bb is None: return
        if bb != u.lbb: u.lbb = bb; u.tchg = t
        elif t - u.tchg > 300.0: return
        cx = self.ctx(u, t)
        for e in u.ent.values():
            if e.delta != 0.0 or e.tc is not None or e.stop: continue
            bp = self.price(e, cx)
            if bp is None: e.px = None
            elif e.px is None or abs(bp - e.px) > E: self.repeg(e, bp, cx[0])

    def write(self, u, why):
        if u.fin: return
        u.fin = True
        if u.te is None: return
        r = {'dia': self.day, 'mercado': u.m, 'coin': u.coin, 'lado': u.side, 'cierre': int(u.cie), 'fin': why}
        r.update(u.info)
        for k, e in u.ent.items():
            r[k + '_sh'] = round(e.sh, 6); r[k + '_cost'] = round(e.cost, 6); r[k + '_t1'] = e.t1; r[k + '_np'] = e.npart
        self.out.append(r)


def selftest2():
    d0 = 1792972800
    ms = lambda off: int(round((d0 + off) * 1000))
    L = ['tipo,t_ms,id,c1,c2,c3,c4,c5']
    k = lambda t, tok, mk, end, side: L.append('k,%d,%s,BTC,5min,%s,%s,%s' % (ms(t), tok, mk, end, side))
    q = lambda t, tok, bb, ba, bs, as_: L.append('q,%d,%s,%s,%s,%s,%s,%d' % (ms(t), tok, bb, ba, bs, as_, ms(t)))
    tr = lambda t, tok, p, sd, sz: L.append('t,%d,%s,%s,%s,%s,%d,' % (ms(t), tok, p, sd, sz, ms(t)))
    for mk, a, b, end in (('M1', 'A', 'B', '00:10:00'), ('M2', 'C', 'D', '00:15:00'), ('M3', 'E', 'F', '00:20:00')):
        k(1, a, mk, '2026-10-26 %s+00:00' % end, 'YES'); k(1, b, mk, '2026-10-26 %s+00:00' % end, 'NO')
    q(400.0, 'A', 0.20, 0.25, 10, 10); q(400.0, 'B', 0.75, 0.80, 10, 10); q(400.2, 'A', 0.20, 0.25, 10, 10); q(400.2, 'B', 0.75, 0.80, 10, 10)
    tr(401.0, 'A', 0.21, 'SELL', 2); tr(402.0, 'A', 0.20, 'SELL', 4); tr(403.0, 'A', 0.20, 'SELL', 8)
    tr(404.0, 'A', 0.19, 'SELL', 5); tr(405.0, 'A', 0.17, 'SELL', 5)
    q(699.0, 'C', 0.20, 0.25, 2, 18); q(699.0, 'D', 0.75, 0.80, 18, 2); q(699.2, 'C', 0.20, 0.25, 2, 18)
    tr(700.5, 'C', 0.21, 'SELL', 5)
    q(999.0, 'E', 0.20, 0.25, 10, 10); q(999.0, 'F', 0.75, 0.80, 10, 10); q(999.2, 'E', 0.20, 0.25, 10, 10); q(999.2, 'F', 0.75, 0.80, 10, 10)
    tr(1000.5, 'F', 0.79, 'BUY', 5)
    q(1199.0, 'E', 0.20, 0.25, 10, 10)
    p = BASE + 'tmp/selftest2.csv.gz'
    with gzip.open(p, 'wt') as f: f.write('\n'.join(L) + '\n')
    X = Sim2('2026-10-26'); X.run(p)
    R = {(r['mercado'], r['lado']): r for r in X.out}
    a = R[('M1', 'YES')]; c = R[('M2', 'YES')]; e3 = R[('M3', 'YES')]
    cl = lambda r, n, sh, cost: r[n + '_sh'] == sh and abs(r[n + '_cost'] - cost) < 1e-9
    chk = [cl(a, 'U_p1', 5, 1.05), cl(a, 'U_z0', 5, 1.00), cl(a, 'U_m1', 5, 0.95), cl(a, 'U_m2', 5, 0.90),
           cl(a, 'O_z0', 5, 1.00), a['O_z0_t1'] == ms(402.0), cl(a, 'O_m1', 5, 0.95), a['O_m1_t1'] == ms(404.0),
           a['G10_p1_sh'] == 5, a['G5_p1_sh'] == 5, a['GP5_p1_sh'] == 0, a['I5_p1_sh'] == 5, a['U_z0_t1'] == ms(403.0),
           c['U_p1_sh'] == 5, c['G10_p1_sh'] == 0, c['G5_p1_sh'] == 0, c['GP5_p1_sh'] == 0, c['I5_p1_sh'] == 5,
           cl(e3, 'U_p1', 5, 1.05)]
    print('eps C', c['eps_e'], 'A', a['eps_e'], 'chk', [int(x) for x in chk])
    print('SELFTEST2', 'OK' if all(chk) else 'FALLO')
    return all(chk)


if __name__ == '__main__':
    if '--selftest' in sys.argv: sys.exit(0 if selftest2() else 1)
    day = sys.argv[sys.argv.index('--dia') + 1]
    src = sys.argv[sys.argv.index('--fichero') + 1] if '--fichero' in sys.argv else S.REG % day
    p15 = sys.argv[sys.argv.index('--fichero15') + 1] if '--fichero15' in sys.argv else None
    outd = sys.argv[sys.argv.index('--outdir') + 1] if '--outdir' in sys.argv else BASE + 'out/'
    os.makedirs(outd, exist_ok=True)
    t0 = time.time(); X = Sim2(day); X.load15(p15); t1 = time.time(); X.run(src)
    X.dump_csv(outd + 's_%s.csv.gz' % day)
    X.st['filas'] = len(X.out); X.st['seg15'] = round(t1 - t0); X.st['seg'] = round(time.time() - t0)
    X.st['n15'] = 0 if X.T15 is None else int(len(X.T15)); X.st['map15'] = len(X.map15)
    print(json.dumps({'dia': day, **X.st}), flush=True)
