#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""predictor_as_b_28oct/pred_extract.py - extraccion CIEGA (no lee desenlaces) de rasgos ex-ante sobre la simulacion P de
alpha_miner_b_27oct/sim.py (importada SIN cambios; esta clase solo OBSERVA). Reloj = RECEPCION. Ver PREREG_PREDICTOR.md.
Salida out/p_<dia>.npz: fills (primer relleno de P, rasgos a t_f-L para L en OFFS) y snaps (instantaneas cada >= SNAP_MS)."""
import sys, os, gzip, json, math, time, datetime
from collections import deque
from array import array
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/alpha_miner_b_27oct')
import sim as S

BASE = '/root/polymarket-research/experimentos/5m_barato/predictor_as_b_28oct/'
NAN = float('nan')
COINS = ['BTC', 'ETH', 'SOL', 'XRP', 'DOGE', 'BNB']
OFFS = (100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1500, 2000)
SNAP_MS = 4000.0
WIN_PM = 3600.0; WIN_BN = 6000.0
AGE_S = S.AGE; LR = S.LR
FN = ['T', 'coin', 'side', 'hour', 'te_age', 'lvl', 'bb', 'ba', 'bs', 'as', 'spr', 'mid', 'dist', 'st_age',
      'dbb300', 'dba300', 'dmid300', 'dbb1000', 'dba1000', 'dmid1000', 'nupd1000', 'nbbchg1000', 'nbachg1000',
      'das1000', 'dbs1000', 'bb_age', 'ba_age',
      'cbb', 'cba', 'cbs', 'cas', 'gap_bb', 'gap_ba', 'dcmid300', 'dcmid1000', 'cst_age',
      'npr1000', 'bear1000', 'bull1000', 'imb1000', 'lastpr_age',
      'r300', 'r1000', 'r3000', 'rabs1000', 'bn_n1000', 'bn_imb1000', 'bn_age', 'v60',
      'b15', 'a15', 'db15_300', 'db15_1000', 'b15_minus_a5', 'st15_age']
NF = len(FN); NFX = 12


def sat(h, tau):
    for e in reversed(h):
        if e[0] <= tau: return e
    return None


def nz(x): return NAN if x is None else x


class PSim(S.Sim):
    def __init__(s, day):
        S.Sim.__init__(s, day)
        s.hq = {}; s.hp = {}; s.htk = {}; s.m15 = {}; s.by15 = {}; s.h15d = {}
        s.cur = None; s.lsnap = {}
        s.FM = []; s.FK = []; s.FF = array('f')
        s.SM = []; s.SK = []; s.SF = array('f'); s.SX = array('f')

    # ---------------- rasgos ----------------
    def feat(s, u, tau):
        d = {}
        sgn = 1.0 if u.side == 'YES' else -1.0
        c = u.comp
        hu = s.hq[u.tok]
        d['T'] = u.cie - tau / 1000.0
        d['coin'] = float(COINS.index(u.coin)) if u.coin in COINS else NAN
        d['side'] = 1.0 if u.side == 'YES' else 0.0
        d['hour'] = float(int(tau // 3600000.0) % 24)
        d['te_age'] = (tau - u.te) if u.te is not None else NAN
        s0 = sat(hu, tau)
        if s0 is not None and tau - s0[0] <= AGE_S:
            t0_, bb, ba, bs, as_ = s0
            d['bb'] = bb; d['ba'] = ba; d['bs'] = nz(bs); d['as'] = nz(as_)
            d['spr'] = ba - bb; d['mid'] = 0.5 * (ba + bb); d['st_age'] = tau - t0_
            s1 = sat(hu, tau - LR); lvl = NAN
            if s1 is not None and (tau - LR) - s1[0] <= AGE_S: lvl = round(s1[1] + 0.01 + 1e-12, 2)
            d['lvl'] = lvl; d['dist'] = (ba - lvl) if lvl == lvl else NAN
            for W in (300, 1000):
                sw = sat(hu, tau - W)
                if sw is not None:
                    d['dbb%d' % W] = bb - sw[1]; d['dba%d' % W] = ba - sw[2]
                    d['dmid%d' % W] = 0.5 * (ba + bb) - 0.5 * (sw[1] + sw[2])
                    if W == 1000:
                        if sw[2] == ba and sw[4] is not None and as_ is not None: d['das1000'] = as_ - sw[4]
                        if sw[1] == bb and sw[3] is not None and bs is not None: d['dbs1000'] = bs - sw[3]
            n = 0; nb = 0; na = 0; prev = None
            for e in reversed(hu):
                if e[0] > tau: continue
                if e[0] <= tau - 1000: break
                n += 1
                if prev is not None:
                    if e[1] != prev[1]: nb += 1
                    if e[2] != prev[2]: na += 1
                prev = e
            d['nupd1000'] = float(n); d['nbbchg1000'] = float(nb); d['nbachg1000'] = float(na)
            tb = s0[0]
            for e in reversed(hu):
                if e[0] > tau: continue
                if e[1] != bb: break
                tb = e[0]
            d['bb_age'] = tau - tb
            ta = s0[0]
            for e in reversed(hu):
                if e[0] > tau: continue
                if e[2] != ba: break
                ta = e[0]
            d['ba_age'] = tau - ta
        if c is not None:
            sc = sat(s.hq[c.tok], tau)
            if sc is not None and tau - sc[0] <= AGE_S:
                cbb, cba = sc[1], sc[2]
                d['cbb'] = cbb; d['cba'] = cba; d['cbs'] = nz(sc[3]); d['cas'] = nz(sc[4]); d['cst_age'] = tau - sc[0]
                if 'bb' in d:
                    d['gap_bb'] = (1.0 - cba) - d['bb']; d['gap_ba'] = (1.0 - cbb) - d['ba']
                cmid = 0.5 * (cbb + cba)
                for W in (300, 1000):
                    sw = sat(s.hq[c.tok], tau - W)
                    if sw is not None: d['dcmid%d' % W] = -(cmid - 0.5 * (sw[1] + sw[2]))
        bear = 0.0; bull = 0.0; npr = 0; lastp = None
        for tok, own in ((u.tok, True), (c.tok if c is not None else None, False)):
            if tok is None: continue
            for e in reversed(s.hp[tok]):
                if e[0] > tau: continue
                if lastp is None or e[0] > lastp: lastp = e[0]
                if e[0] <= tau - 1000: break
                npr += 1
                sell = (e[2] == 'SELL')
                if own:
                    if sell: bear += e[3]
                    else: bull += e[3]
                else:
                    if sell: bull += e[3]
                    else: bear += e[3]
        d['npr1000'] = float(npr); d['bear1000'] = bear; d['bull1000'] = bull
        tot = bear + bull
        d['imb1000'] = (bear - bull) / tot if tot > 0 else NAN
        d['lastpr_age'] = (tau - lastp) if lastp is not None else NAN
        sym = S.SYM.get(u.coin)
        tk = s.htk.get(sym)
        if tk:
            k0 = sat(tk, tau)
            if k0 is not None and tau - k0[0] <= 5000:
                d['bn_age'] = tau - k0[0]
                for W in (300, 1000, 3000):
                    kw = sat(tk, tau - W)
                    if kw is not None and kw[1] > 0: d['r%d' % W] = sgn * (k0[1] / kw[1] - 1.0) * 1e4
                if 'r1000' in d: d['rabs1000'] = abs(d['r1000'])
                nb_ = 0; vb = 0.0; vs = 0.0
                for e in reversed(tk):
                    if e[0] > tau: continue
                    if e[0] <= tau - 1000: break
                    nb_ += 1
                    if e[3]: vs += e[2]
                    else: vb += e[2]
                d['bn_n1000'] = float(nb_)
                if vb + vs > 0: d['bn_imb1000'] = sgn * (vb - vs) / (vb + vs)
        bn = s.bn.get(sym)
        if bn is not None and bn.sec:
            si = int(tau // 1000.0) - 1; pn = None; p60 = None
            for sx, px in reversed(bn.sec):
                if pn is None and sx <= si: pn = px
                if sx <= si - 60: p60 = px; break
            if pn is not None and p60 is not None and p60 > 0: d['v60'] = abs(pn / p60 - 1.0) * 1e4
        ci = int(round(u.cie)); e15 = ((ci + 899) // 900) * 900
        t15 = s.by15.get((u.coin, e15, u.side))
        if t15 is not None:
            h15 = s.h15d[t15]; q15 = sat(h15, tau)
            if q15 is not None and tau - q15[0] <= AGE_S:
                d['b15'] = q15[1]; d['a15'] = q15[2]; d['st15_age'] = tau - q15[0]
                if 'ba' in d: d['b15_minus_a5'] = q15[1] - d['ba']
                q3 = sat(h15, tau - 300); q1 = sat(h15, tau - 1000)
                if q3 is not None: d['db15_300'] = q15[1] - q3[1]
                if q1 is not None: d['db15_1000'] = q15[1] - q1[1]
        return [d.get(k, NAN) for k in FN]

    def fut(s, u, tau, tnow):
        out = []; c = u.comp
        for X in (250.0, 1000.0):
            v = [NAN] * 6; tx = tau + X
            if tx <= tnow and c is not None:
                sc = sat(s.hq[c.tok], tx); so = sat(s.hq[u.tok], tx)
                if sc is not None and tx - sc[0] <= AGE_S: v[0] = sc[1]; v[1] = sc[2]; v[2] = nz(sc[3]); v[3] = nz(sc[4])
                if so is not None and tx - so[0] <= AGE_S: v[4] = so[1]; v[5] = so[2]
            out.extend(v)
        return out

    # ---------------- ganchos (solo observan) ----------------
    def eprint_direct(s, u, p, sz, t):
        s.cur = (p, sz, t, 0); S.Sim.eprint_direct(s, u, p, sz, t); s.cur = None

    def eprint_mirror(s, u, p, sz, t):
        s.cur = (p, sz, t, 1); S.Sim.eprint_mirror(s, u, p, sz, t); s.cur = None

    def efill(s, u, k, e, sz, bp, t, cause):
        first = (k == 'P' and e.t1 is None)
        S.Sim.efill(s, u, k, e, sz, bp, t, cause)
        if first and e.t1 is not None:
            cur = s.cur
            p, psz, pt, kind = cur if cur is not None else (NAN, NAN, t, -1)
            if kind == 0: swept = 1.0 if p < bp - 1e-9 else 0.0; dp = (bp - p) * 100.0
            elif kind == 1: swept = 1.0 if p > (1.0 - bp) + 1e-9 else 0.0; dp = (p - (1.0 - bp)) * 100.0
            else: swept = NAN; dp = NAN
            s.FM.append((t, bp, p, psz, float(kind), swept, dp, u.cie, u.te if u.te is not None else NAN))
            s.FK.append((u.tok, u.m, u.coin, u.side))
            for L in OFFS:
                s.FF.extend(s.feat(u, t - L)); s.FF.extend(s.fut(u, t - L, t))

    def on_q(s, u, t, bb, ba, bs, as_):
        if bb is not None and ba is not None and bb < ba - S.E:
            h = s.hq.get(u.tok)
            if h is not None:
                h.append((t, bb, ba, bs, as_)); lim = t - WIN_PM
                while len(h) >= 2 and h[1][0] <= lim: h.popleft()
        S.Sim.on_q(s, u, t, bb, ba, bs, as_)
        if u.te is not None:
            e = u.ent['P']
            if e.t1 is None and e.tc is None and not e.stop and t - s.lsnap.get(u.tok, -1e18) >= SNAP_MS:
                T = u.cie - t / 1000.0
                if 62.0 <= T <= 289.0 and not s.tdoff(u, t):
                    st = sat(s.hq[u.tok], t - LR)
                    if st is not None and (t - LR) - st[0] <= AGE_S and S.Sim.elig(st):
                        lvl = S.r2(st[1] + 0.01); s.lsnap[u.tok] = t; idx = len(s.SM)
                        s.SM.append((t, lvl, u.cie, float(COINS.index(u.coin)) if u.coin in COINS else NAN, 1.0 if u.side == 'YES' else 0.0))
                        s.SK.append((u.tok, u.m, u.coin, u.side))
                        s.SF.extend(s.feat(u, t)); s.SX.extend([NAN] * NFX)
                        s.push(t + 250.0, 'csnap', u, (idx, 0)); s.push(t + 1000.0, 'csnap', u, (idx, 1))

    def on_t(s, u, t, p, sd, sz):
        h = s.hp.get(u.tok)
        if h is not None:
            h.append((t, p, sd, sz)); lim = t - WIN_PM
            while h and h[0][0] < lim: h.popleft()
        S.Sim.on_t(s, u, t, p, sd, sz)

    def on_x(s, c):
        S.Sim.on_x(s, c)
        bn = s.bn.get(c[2])
        if bn is None or not c[7].strip(): return
        tk = s.htk.get(c[2])
        if tk is None: tk = s.htk[c[2]] = deque()
        t = bn.last
        tk.append((t, float(c[3]), float(c[4]), c[5].strip() == '1'))
        lim = t - WIN_BN
        while tk and tk[0][0] < lim: tk.popleft()

    def ev_csnap(s, u, tau, arg):
        idx, which = arg; c = u.comp; base = idx * NFX + which * 6; X = s.SX
        if c is not None and c.ba is not None and tau - c.tq <= AGE_S:
            X[base] = c.bb; X[base + 1] = c.ba; X[base + 2] = nz(c.bs); X[base + 3] = nz(c.as_)
        if u.ba is not None and tau - u.tq <= AGE_S:
            X[base + 4] = u.bb; X[base + 5] = u.ba

    # ---------------- bucle (copia de Sim.run + 15m) ----------------
    def run(s, path):
        st = s.st
        with gzip.open(path, 'rt') as f:
            next(f)
            for ln in f:
                st['lineas'] += 1
                ty = ln[0]
                if ty == 'q' or ty == 't':
                    c0 = ln.split(',', 3); tok = c0[2]
                    u = s.U.get(tok)
                    if u is None:
                        if ty == 'q' and tok in s.m15:
                            c = ln.rstrip('\n').split(',')
                            t = float(c[7]) if c[7].strip() else float(c[1])
                            bb = S.fl(c[3]); ba = S.fl(c[4])
                            if bb is not None and ba is not None and bb < ba - S.E:
                                h = s.h15d[tok]; h.append((t, bb, ba)); lim = t - WIN_PM
                                while len(h) >= 2 and h[1][0] <= lim: h.popleft()
                        continue
                    if u.fin: continue
                    c = ln.rstrip('\n').split(',')
                    rv = c[7] if ty == 'q' else c[6]
                    if rv.strip(): t = float(rv)
                    else: t = float(c[1]); st['sin_recv'] += 1
                    s.clock(t)
                    if u.fin: continue
                    if t < u.last - 1000: st['descartadas_retro'] += 1; continue
                    if t > u.last: u.last = t
                    if ty == 'q': s.on_q(u, t, S.fl(c[3]), S.fl(c[4]), S.fl(c[5]), S.fl(c[6]))
                    else: s.on_t(u, t, float(c[3]), c[4], float(c[5]))
                elif ty == 'x':
                    s.on_x(ln.rstrip('\n').split(','))
                elif ty == 'k':
                    c = ln.rstrip('\n').split(',')
                    if c[4] == '15min':
                        if c[2] not in s.m15 and c[7] in ('YES', 'NO'):
                            ci = int(round(datetime.datetime.fromisoformat(c[6]).timestamp()))
                            s.m15[c[2]] = (c[3], ci, c[7]); s.by15[(c[3], ci, c[7])] = c[2]; s.h15d[c[2]] = deque()
                        continue
                    if c[4] != '5min' or c[2] in s.U: continue
                    cie = datetime.datetime.fromisoformat(c[6]).timestamp()
                    if not (s.cmin <= cie <= s.cmax) or c[7] not in ('YES', 'NO'): continue
                    u = S.U(c[2], c[5], c[3], c[7], cie); s.U[c[2]] = u
                    s.hq[c[2]] = deque(); s.hp[c[2]] = deque()
                    o = s.other.get((c[5], 'NO' if c[7] == 'YES' else 'YES'))
                    if o is not None: u.comp = o; o.comp = u
                    s.other[(c[5], c[7])] = u
                    s.push(cie * 1000 - 60000, 'estop', u)
                    s.push((cie - S.T_DUMP) * 1000 + S.LT, 'dump', u)
                    s.push(cie * 1000 - 2000, 'xend', u)
        for u in s.U.values():
            if not u.fin and u.te is not None: s.write(u, 'eof')

    def save(s, path):
        import numpy as np
        nF = len(s.FM); nS = len(s.SM); W = NF + NFX
        fm = np.array(s.FM, dtype=np.float64).reshape(nF, 9)
        ff = np.array(s.FF, dtype=np.float32).reshape(nF, len(OFFS), W)
        fk = np.array(s.FK, dtype='<U100').reshape(nF, 4)
        sm = np.array(s.SM, dtype=np.float64).reshape(nS, 5)
        sf = np.array(s.SF, dtype=np.float32).reshape(nS, NF)
        sx = np.array(s.SX, dtype=np.float32).reshape(nS, NFX)
        sk = np.array(s.SK, dtype='<U100').reshape(nS, 4)
        tmp = path[:-4] + '.tmp.npz'
        np.savez_compressed(tmp, fm=fm, ff=ff, fk=fk, sm=sm, sf=sf, sx=sx, sk=sk, fn=np.array(FN), offs=np.array(OFFS),
                            stats=np.array(json.dumps(s.st)))
        os.replace(tmp, path)


if __name__ == '__main__':
    day = sys.argv[sys.argv.index('--dia') + 1]
    out = BASE + 'out/p_%s.npz' % day
    if os.path.exists(out): print('ya existe', out); sys.exit(0)
    t0 = time.time(); Z = PSim(day); Z.run(S.REG % day); Z.save(out)
    print(json.dumps({'dia': day, 'fills': len(Z.FM), 'snaps': len(Z.SM), 'seg': round(time.time() - t0), **Z.st}), flush=True)
