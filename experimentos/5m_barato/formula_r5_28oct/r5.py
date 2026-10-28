#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""formula_r5_28oct/r5.py - manda PREREG_FORMULA_R5.md (hashes en HASHES_R5.txt).
Modos: ext DIA... | sim DIA... | fam --is D,D --oos D,D --tag T
sim3-BTC: puja pasiva PROPIA en BTC 5m condicionada a S (barrido en el registro, reloj de RECEPCION), L1 retrasado LR, cola estricta
(travesia rellena; en el nivel solo tras la cola visible), cancelacion TD (Binance 2 bps/300 ms) y parada por T. Precio fijo por intervalo.
Desenlaces SOLO para valorar fills. Sin produccion, sin ordenes."""
import sys, os, json, math, time, subprocess, datetime, traceback
import numpy as np
from collections import deque
from scipy import stats
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r4_28oct')
import r4
I = r4.I
BASE = '/root/polymarket-research/experimentos/5m_barato/formula_r5_28oct/'
EXT = BASE + 'ext/'; SIMO = BASE + 'simout/'; TMP = BASE + 'tmp/'
LR = 130.0; TD_K = 2.0; TD_W = 300.0; TD_C = 100.0; TD_OFF = 1000.0
BB_HI = 0.29; SPR = 0.02; AGE = 30000.0; E = 1e-9; INF = 1e18
NS = (5.0, 10.0, 20.0, 50.0)
THETAS = (400.0, 800.0, 1600.0); W1S = (1.0, 5.0); W2S = (30.0, 60.0, 120.0)
TREMS = ((60.0, 290.0), (120.0, 240.0)); DELTAS = (0.01, 0.0, -0.01); BANDS = (0.10, 0.20)
LINES = []


def P(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); LINES.append(s)


def make_specs():
    L = []
    for th in THETAS:
        for w1 in W1S:
            for w2 in W2S:
                for ti in range(2):
                    for td in (0, 1): L.append(('S', th, w1, w2, ti, td))
    for ti in range(2):
        for td in (0, 1): L.append(('A', 0.0, 0.0, 0.0, ti, td))
    return L


SPECS = make_specs()
VARS = [(si, di, bi) for si in range(len(SPECS)) for di in range(3) for bi in range(2)]
NV = len(VARS)
def vid(si, di, bi): return (si * 3 + di) * 2 + bi


def vlabel(v):
    si, di, bi = VARS[v]; sp = SPECS[si]
    if sp[0] == 'A': s = 'SIEMPRE T%d-%d TD%d' % (TREMS[sp[4]][0], TREMS[sp[4]][1], sp[5])
    else: s = 'S th%d w%d-%d T%d-%d TD%d' % (sp[1], sp[2], sp[3], TREMS[sp[4]][0], TREMS[sp[4]][1], sp[5])
    return '%s d%+.2f b%.2f' % (s, DELTAS[di], BANDS[bi])


AWK = r'''BEGIN { FS = ","; n = 0 }
$1 == "k" { if ($4 == "BTC" && $5 == "5min" && ($8 == "YES" || $8 == "NO") && !($3 in ID)) { split($7, a, /[-:T +]/); c = mktime(a[1] " " a[2] " " a[3] " " a[4] " " a[5] " " a[6]); if (c >= CMIN && c <= CMAX) { ID[$3] = n++; CIE[$3] = c; print $3 "|" ID[$3] "|" $6 "|" $8 "|" $7 "|" c > KF } }; next }
$1 == "q" { if ($3 in ID) { r = $8; if (r !~ /^[0-9.]+$/) r = $2; rn = r + 0; if (rn >= LAST[$3] - 1000) { if (rn > LAST[$3]) LAST[$3] = rn; if ($4 ~ /^[0-9.]+$/ && $5 ~ /^[0-9.]+$/ && ($4 + 0) < ($5 + 0) - 0.000000001) { T = CIE[$3] - rn / 1000; if (T >= 0 && T <= 291) { s = ($6 ~ /^[0-9.]+$/) ? $6 : -1; key = $4 "," $5 "," s; if (key != LK[$3]) { LK[$3] = key; print r, ID[$3], $4, $5, s > QF } } } } }; next }
$1 == "t" { if (($3 in ID) && ($5 == "SELL" || $5 == "BUY") && $4 ~ /^[0-9.]+$/ && $6 ~ /^[0-9.]+$/) { r = $7; if (r !~ /^[0-9.]+$/) r = $2; rn = r + 0; if (rn >= LAST[$3] - 1000) { if (rn > LAST[$3]) LAST[$3] = rn; p = $4 + 0; if (($5 == "SELL" && p <= 0.32) || ($5 == "BUY" && p >= 0.68)) print r, $2, ID[$3], $4, $6, ($5 == "SELL" ? 0 : 1) > TF } }; next }
$1 == "x" { if ($3 == "BTCUSDT" && $8 ~ /^[0-9.]+$/ && $4 ~ /^[0-9.]+$/) print $8, $4 > XF }'''


def read_chunks(path, ncol, CH=1000000):
    if not os.path.exists(path): return
    with open(path, 'rb') as fh:
        while True:
            a = np.fromfile(fh, dtype=np.float64, count=ncol * CH, sep=' ')
            if a.size == 0: break
            yield a[:(a.size // ncol) * ncol].reshape(-1, ncol)


def ext(day):
    out = EXT + 'b_%s.npz' % day
    if os.path.exists(out): P('[%s] ext ya hecho' % day); return
    t0 = time.time(); os.makedirs(EXT, exist_ok=True); os.makedirs(TMP, exist_ok=True)
    pid = os.getpid(); kf = TMP + 'k_%s_%d.txt' % (day, pid); qf, tf_, xf = [TMP + '%s_%s_%d.txt' % (nm, day, pid) for nm in ('q', 't', 'x')]
    d0 = datetime.datetime.fromisoformat(day + 'T00:00:00+00:00').timestamp(); cmin = int(d0 + 299); cmax = int(d0 + 86401)
    cmd = ("nice -n 19 ionice -c3 zcat '%s' | TZ=UTC LC_ALL=C gawk -v CMIN=%d -v CMAX=%d -v KF='%s' -v QF='%s' -v TF='%s' -v XF='%s' '%s'"
           % (I.REG % day, cmin, cmax, kf, qf, tf_, xf, AWK))
    subprocess.run(['bash', '-c', cmd], check=True)
    t1 = time.time()
    rows = [ln.rstrip('\n').split('|') for ln in open(kf)]; os.remove(kf)
    n = len(rows); cie = np.array([float(r[5]) for r in rows]); side = np.array([0 if r[3] == 'YES' else 1 for r in rows], np.int8)
    mks = [r[2] for r in rows]; bym = {(mks[i], int(side[i])): i for i in range(n)}
    comp = np.array([bym.get((mks[i], 1 - int(side[i])), -1) for i in range(n)], np.int32)
    qr = []; qk = []; qb = []; qa = []; qs = []
    for c in read_chunks(qf, 5):
        qr.append(c[:, 0].copy()); qk.append(c[:, 1].astype(np.int32)); qb.append(c[:, 2].copy()); qa.append(c[:, 3].copy()); qs.append(c[:, 4].astype(np.float32))
    nq = sum(len(x) for x in qr)
    if nq:
        qr = np.concatenate(qr); qk = np.concatenate(qk); qb = np.concatenate(qb); qa = np.concatenate(qa); qs = np.concatenate(qs)
        o = np.lexsort((qr, qk)); qr = qr[o]; qk = qk[o]; qb = qb[o]; qa = qa[o]; qs = qs[o]; del o
    else: qr = np.zeros(0); qk = np.zeros(0, np.int32); qb = np.zeros(0); qa = np.zeros(0); qs = np.zeros(0, np.float32)
    pr = [c.copy() for c in read_chunks(tf_, 6)]
    Pm = np.concatenate(pr) if pr else np.zeros((0, 6)); del pr
    if len(Pm):
        o = np.lexsort((Pm[:, 0], Pm[:, 2])); Pm = Pm[o]
    jd = []; ju = []; dq = deque(); last = -1e18; nx = 0
    for c in read_chunks(xf, 2):
        nx += len(c)
        for t, p in zip(c[:, 0].tolist(), c[:, 1].tolist()):
            if t < last - 60000: dq.clear()
            elif t < last: t = last
            last = t; lim = t - TD_W
            while len(dq) >= 2 and dq[1][0] <= lim: dq.popleft()
            if dq and dq[0][0] <= lim:
                r = (p / dq[0][1] - 1.0) * 1e4
                if r <= -TD_K: jd.append(t)
                elif r >= TD_K: ju.append(t)
            dq.append((t, p))
    for f in (qf, tf_, xf):
        if os.path.exists(f): os.remove(f)
    np.savez_compressed(out, tok_cie=cie, tok_ok=np.ones(n, bool), tok_side=side, tok_comp=comp, tok_mk=np.array(mks),
                        qtok=qk, qt=qr, qbb=qb, qba=qa, qbs=qs,
                        ptok=Pm[:, 2].astype(np.int32), pt=Pm[:, 0], pex=Pm[:, 1], ppx=Pm[:, 3], psz=Pm[:, 4], psd=Pm[:, 5].astype(np.int8),
                        jd=np.array(jd), ju=np.array(ju))
    P('[%s] EXT ok: tokens=%d q=%d prints=%d x=%d jd=%d ju=%d | awk %.0f s total %.0f s' % (day, n, nq, len(Pm), nx, len(jd), len(ju), t1 - t0, time.time() - t0))


def merge_off(j):
    if len(j) == 0: return np.zeros(0), np.zeros(0)
    s = j + TD_C; e = j + TD_OFF; ms = [float(s[0])]; me = [float(e[0])]
    for a, b in zip(s[1:].tolist(), e[1:].tolist()):
        if a <= me[-1]: me[-1] = max(me[-1], b)
        else: ms.append(a); me.append(b)
    return np.array(ms), np.array(me)


def pestream(u, comp, plo, phi, pt, ppx, psz, psd):
    a, b = int(plo[u]), int(phi[u]); m = psd[a:b] == 0
    t1 = pt[a:b][m]; e1 = ppx[a:b][m]; s1 = psz[a:b][m]; c = int(comp[u])
    if c < 0: return t1, e1, s1
    a2, b2 = int(plo[c]), int(phi[c]); m2 = psd[a2:b2] == 1
    t2 = pt[a2:b2][m2]; e2 = 1.0 - ppx[a2:b2][m2]; s2 = psz[a2:b2][m2]
    t = np.concatenate([t1, t2]); o = np.argsort(t, kind='stable')
    return t[o], np.concatenate([e1, e2])[o], np.concatenate([s1, s2])[o]


def sub_intervals(kind, ev, w1, w2, lo, hi, td, offs, offe):
    if kind == 'A': base = [(lo, hi)]
    else:
        if ev is None or len(ev) == 0: return []
        a0 = int(np.searchsorted(ev, lo - w2 * 1000.0, 'right')); a1 = int(np.searchsorted(ev, hi - w1 * 1000.0, 'left'))
        base = []
        for e in ev[a0:a1].tolist():
            a = max(e + w1 * 1000.0, lo); b = min(e + w2 * 1000.0, hi)
            if b <= a: continue
            if base and a <= base[-1][1]: base[-1] = (base[-1][0], max(base[-1][1], b))
            else: base.append((a, b))
    if not td or len(offs) == 0: return base
    out = []; m = len(offs)
    for a, b in base:
        i = int(np.searchsorted(offe, a, 'right')); cur = a
        while i < m and offs[i] < b:
            if offs[i] > cur: out.append((cur, float(offs[i])))
            cur = max(cur, float(offe[i])); i += 1
            if cur >= b: break
        if cur < b: out.append((cur, b))
    return out


def fill_sub(st, se, ss, t0, t1, b, q0):
    i0 = int(np.searchsorted(st, t0, 'left')); i1 = int(np.searchsorted(st, t1, 'left'))
    if i1 <= i0: return None
    pe = se[i0:i1]; sz = ss[i0:i1]; tr = pe < b - E
    f = np.where(tr, sz, 0.0)
    if q0 < INF / 2:
        eq = np.abs(pe - b) <= E
        if eq.any():
            eqs = np.where(eq, sz, 0.0); ce = np.cumsum(eqs) - eqs
            f = f + np.where(eq, np.maximum(0.0, sz - np.maximum(0.0, q0 - ce)), 0.0)
    pos = f > 0
    if not pos.any(): return None
    fp = f[pos]; cs = np.cumsum(fp)
    return float(cs[-1]), cs - fp, fp, st[i0:i1][pos]


def orders_in(qtt, bbv, bav, bsv, a, b, blo):
    n = len(qtt)
    ia = int(np.searchsorted(qtt, a, 'right')) - 1
    ib = int(np.searchsorted(qtt, b, 'left'))
    if ia < 0: ia = 0
    if ia >= n: return []
    if ib <= ia: ib = ia + 1
    tt = qtt[ia:ib]; rb = bbv[ia:ib]; ra = bav[ia:ib]
    inb = (rb >= blo - E) & (rb <= BB_HI + E)
    if not inb.any(): return []
    good = inb & ((ra - rb) >= SPR - E)
    if not good.any(): return []
    dd = np.diff(inb.astype(np.int8)); starts = (np.flatnonzero(dd == 1) + 1).tolist(); ends = (np.flatnonzero(dd == -1) + 1).tolist()
    if inb[0]: starts = [0] + starts
    if inb[-1]: ends = ends + [len(inb)]
    out = []
    for s0, e0 in zip(starts, ends):
        gi = np.flatnonzero(good[s0:e0])
        if len(gi) == 0: continue
        rd = s0 + int(gi[0]); t_r = float(tt[rd]); td_ = max(a, t_r)
        if td_ - t_r > AGE: continue
        tend = b if e0 >= len(tt) else min(b, float(tt[e0]))
        out.append((td_, tend, float(rb[rd]), float(ra[rd]), float(bsv[ia + rd])))
    return out


def run_day(day, G, only=None, detail=None):
    z = np.load(EXT + 'b_%s.npz' % day); Z = {k: z[k] for k in z.files}
    cie = Z['tok_cie']; okt = Z['tok_ok']; side = Z['tok_side']; comp = Z['tok_comp']; mkstr = Z['tok_mk']; n = len(cie)
    qt = Z['qt']; qtok = Z['qtok']; qbb = Z['qbb']; qba = Z['qba']; qbs = Z['qbs']
    pt = Z['pt']; ptok = Z['ptok']; ppx = Z['ppx']; psz = Z['psz']; psd = Z['psd']; pex = Z['pex']
    ids = np.arange(n)
    qlo = np.searchsorted(qtok, ids, 'left'); qhi = np.searchsorted(qtok, ids, 'right')
    plo = np.searchsorted(ptok, ids, 'left'); phi = np.searchsorted(ptok, ids, 'right')
    zone = ((psd == 0) & (ppx >= 0.085) & (ppx <= 0.315)) | ((psd == 1) & (ppx >= 0.685) & (ppx <= 0.915))
    nz = int(zone.sum())
    Dz = {'pr_sd': psd[zone].astype(np.int8), 'pr_ex': pex[zone], 'pr_rec': pt[zone], 'pr_tk': ptok[zone].astype(np.int64),
          'pr_sz': psz[zone], 'pr_coin': np.zeros(nz, np.int8)}
    size, crec, _ = r4.build_clusters(Dz, 'ALL')
    EV = {th: np.sort(crec[size >= th]) for th in THETAS}
    jd = np.sort(Z['jd']); ju = np.sort(Z['ju']); offY = merge_off(jd); offN = merge_off(ju)
    R = np.zeros((NV, len(NS), 6)); rows = []; nunres = 0; ntok = 0
    for u in range(n):
        if not okt[u]: continue
        a0, a1 = int(qlo[u]), int(qhi[u])
        if a1 <= a0: continue
        win = G.get(str(mkstr[u]))
        if win not in ('YES', 'NO'): nunres += 1; continue
        y = 1.0 if win == ('YES' if side[u] == 0 else 'NO') else 0.0
        ntok += 1; qtt = qt[a0:a1]
        st, se, ss = pestream(u, comp, plo, phi, pt, ppx, psz, psd)
        offs, offe = offY if side[u] == 0 else offN
        adv = jd if side[u] == 0 else ju
        c1000 = float(cie[u]) * 1000.0
        for si, sp in enumerate(SPECS):
            if only is not None and si not in only: continue
            kind, th, w1, w2, ti, td = sp
            tmin, tmax = TREMS[ti]
            lo = c1000 - tmax * 1000.0; hi = c1000 - tmin * 1000.0
            ivs = sub_intervals(kind, EV[th] if kind == 'S' else None, w1, w2, lo, hi, td, offs, offe)
            if not ivs: continue
            fl = np.zeros((3, 2, len(NS)))
            bbv = qbb[a0:a1]; bav = qba[a0:a1]; bsv = qbs[a0:a1]
            for (a, b) in ivs:
                if b - a <= LR: continue
                for bi, blo in enumerate(BANDS):
                    for (td_, tend, bb, ba, bs) in orders_in(qtt, bbv, bav, bsv, a, b, blo):
                        if tend - td_ <= LR: continue
                        for di, dl in enumerate(DELTAS):
                            bpx = round(bb + dl + 1e-12, 2)
                            if dl > E: q0 = 0.0
                            elif dl > -E: q0 = bs if bs >= 0 else INF
                            else: q0 = INF
                            v = vid(si, di, bi); R[v, 0, 5] += 1.0
                            r = fill_sub(st, se, ss, td_ + LR, tend, bpx, q0)
                            if r is None: continue
                            tot, starts, fp, tpos = r
                            fv = fl[di, bi]; takes = []
                            for ni, Nn in enumerate(NS):
                                rem = Nn - fv[ni]
                                if rem <= E: takes.append(0.0); continue
                                tkk = min(tot, rem); nex = int(np.searchsorted(starts, rem - E, 'left'))
                                R[v, ni, 0] += tkk; R[v, ni, 1] += tkk * bpx; R[v, ni, 2] += tkk * (y - bpx); R[v, ni, 3] += nex
                                if fv[ni] <= E and tkk > 0: R[v, ni, 4] += 1.0
                                fv[ni] += tkk; takes.append(tkk)
                            if detail is not None and v in detail:
                                tf = float(tpos[0]); k = int(np.searchsorted(adv, tf, 'right'))
                                adv5 = 1 if (k < len(adv) and adv[k] <= tf + 5000.0) else 0
                                rows.append((v, u, str(mkstr[u]), y, bpx, min(q0, 1e9), takes[0], takes[1], takes[2], takes[3], tf, float(cie[u]) - tf / 1000.0, adv5))
    return R, rows, dict(nunres=nunres, ntok=ntok, ncl=[len(EV[t]) for t in THETAS])


def simday(day, G, show=False):
    out = SIMO + 'r_%s.npz' % day
    if os.path.exists(out) and not show: P('[%s] sim ya hecho' % day); return
    t0 = time.time(); os.makedirs(SIMO, exist_ok=True)
    R, rows, inf = run_day(day, G)
    np.savez_compressed(out, R=R, nunres=inf['nunres'], ntok=inf['ntok'], ncl=np.array(inf['ncl']))
    P('[%s] SIM ok: tokens con desenlace=%d sin desenlace=%d clusters(>=400,800,1600)=%s | %.0f s' % (day, inf['ntok'], inf['nunres'], inf['ncl'], time.time() - t0))
    if show:
        for si, sp in enumerate(SPECS):
            if sp[0] == 'A' or (sp[1] == 800.0 and sp[2] == 5.0 and sp[3] == 60.0):
                for di in range(3):
                    v = vid(si, di, 0); c = R[v, 2, 1]; p = R[v, 2, 2]
                    P('   %-44s N=20: ejec=%5.0f acc=%7.1f coste=%8.1f pnl=%+8.2f EV/E=%+.3f ord=%5.0f' % (vlabel(v), R[v, 2, 3], R[v, 2, 0], c, p, (p / c if c > 0 else float('nan')), R[v, 0, 5]))


def tstats(M):
    n = M.shape[0]; m = M.mean(0)
    if n > 1:
        s = M.std(0, ddof=1); se = s / math.sqrt(n)
        t = np.where(se > 0, m / np.where(se > 0, se, 1.0), 0.0); lo = m - stats.t.ppf(0.95, n - 1) * se
    else:
        s = np.zeros(M.shape[1]); t = np.zeros(M.shape[1]); lo = m.copy()
    return m, s, t, lo


def s800_flow(day):
    D = r4.load_day(day); ok = np.isfinite(D['y'])
    size, crec, ccoin = r4.build_clusters(D, 'ALL'); k = size >= 800.0
    S = r4.eval_state(r4.prep_state(crec[k], ccoin[k], None), D['rhat'], D['coin'])
    m = ok & S & (D['coin'] == 0)
    return float(D['sz'][m].sum()), float((D['sz'] * D['p'])[m].sum())


def fam(is_days, oos_days, tag, dev_days=()):
    alld = list(is_days) + list(oos_days) + list(dev_days); nis = len(is_days); no = len(oos_days); nd = len(alld)
    R = np.stack([np.load(SIMO + 'r_%s.npz' % d)['R'] for d in alld])
    ni = 2
    cost = R[:, :, ni, 1]; pnl = R[:, :, ni, 2]; nex = R[:, :, ni, 3]
    ratio = np.where(cost > 0, pnl / np.maximum(cost, 1e-12), 0.0)
    P('== FAMILIA sim3-BTC: %d variantes x 4 tamanos | IS=%s | OOS=%s | N de seleccion=20' % (NV, ','.join(d[-2:] for d in is_days), ','.join(d[-2:] for d in oos_days)))
    gate = ((cost[:nis] > 0).mean(0) >= 0.8) & (nex[:nis].mean(0) >= 100.0)
    m, s, t, lo = tstats(ratio[:nis]); cand = np.nonzero(gate)[0]
    P('compuerta IS (opera >=80 %% de los dias y >=100 ejec/dia a N=20): pasan %d de %d' % (len(cand), NV))
    if len(cand) == 0:
        P('NINGUNA variante pasa la compuerta IS; se muestran las 8 con mas ejecuciones')
        for v in np.argsort(-nex[:nis].mean(0))[:8]: P('  %-56s ejec/dia IS %.0f EV/E dia medio %+.3f' % (vlabel(int(v)), nex[:nis, v].mean(), m[v]))
        return
    o = cand[np.argsort(-lo[cand])]
    P('-- IS: 12 mejores por cota inferior IC90 (por dias) del EV/E diario')
    for v in o[:12]: P('  v%03d %-56s media %+.3f lo90 %+.3f t %+.2f ejec/dia %.0f' % (v, vlabel(int(v)), m[v], lo[v], t[v], nex[:nis, v].mean()))
    vstar = int(o[0])
    K = 5000; rng = np.random.default_rng(2813); Rm = ratio[:nis][:, cand]; ssq = (Rm ** 2).sum(0)
    if nis > 1:
        F = rng.choice([-1.0, 1.0], size=(K, nis)); M = (F @ Rm) / nis
        var = np.maximum((ssq / nis - M ** 2) * nis / (nis - 1), 1e-18); Tm = (M / np.sqrt(var / nis)).max(1)
        padj = float((1 + (Tm >= t[vstar]).sum()) / (K + 1))
    else: padj = float('nan')
    P('ELEGIDA en IS: v%03d %s | t_IS=%+.2f | p ajustado max-estadistico (volteo de signos por dias, K=%d, %d candidatas) = %.4f' % (vstar, vlabel(vstar), t[vstar], K, len(cand), padj))
    sp = SPECS[VARS[vstar][0]]; di = VARS[vstar][1]; bi = VARS[vstar][2]
    P('   FORMULA: S=%s theta=%d acc, ventana tras el barrido [%d s, %d s], T_rem [%d,%d] s, cancelacion TD=%d, cotizar bb%+.2f (cola %s), banda bb>=%.2f, tamanos 5/10/20/50 acc'
      % (sp[0], sp[1], sp[2], sp[3], TREMS[sp[4]][0], TREMS[sp[4]][1], sp[5], DELTAS[di], 'visible' if DELTAS[di] == 0.0 else ('0' if DELTAS[di] > 0 else 'solo travesia'), BANDS[bi]))
    oidx = list(range(nis, nis + no)); didx = list(range(nis + no, nd))
    fa = [s800_flow(d) for d in oos_days]; flow_acc = float(np.mean([x[0] for x in fa])); flow_cost = float(np.mean([x[1] for x in fa]))
    P('flujo S800 de TODOS los makers en BTC (OOS): %.0f acc/dia, %.0f EUR/dia de coste' % (flow_acc, flow_cost))
    def block(v, idx, label):
        P('-- %s | v%03d' % (label, v))
        for nn, Nn in enumerate(NS):
            c = R[idx, v, nn, 1]; p = R[idx, v, nn, 2]; a = R[idx, v, nn, 0]; ne = R[idx, v, nn, 3]
            r = np.where(c > 0, p / np.maximum(c, 1e-12), 0.0); pooled = float(p.sum() / max(c.sum(), 1e-12)); mu, l9, h9 = r4.tci(r)
            nday = len(idx); eurd = float(p.mean())
            P('   N=%2d | EV/E agreg %+.3f | dia medio %+.3f IC90[%+.3f,%+.3f] dias+ %d/%d | ejec/dia %.0f acc/dia %.0f (%.2f %% del flujo S800 BTC) coste/dia %.0f pnl/dia %+.1f => %+.0f EUR/anio'
              % (Nn, pooled, mu, l9, h9, int((r > 0).sum()), nday, ne.mean(), a.mean(), 100 * a.mean() / max(flow_acc, 1e-9), c.mean(), eurd, eurd * 365))
    block(vstar, oidx, 'OOS de la elegida')
    block(vstar, list(range(nis)), 'IS de la elegida (referencia, seleccionada aqui)')
    if didx: block(vstar, didx, 'DEV (dias no usados en la seleccion ni en la OOS): ' + ','.join(alld[j][-2:] for j in didx))
    r20 = ratio[oidx, vstar]
    P('   dias OOS (N=20): ' + ' '.join('%s:%+.2f' % (alld[j][-2:], ratio[j, vstar]) for j in oidx))
    # walk-forward
    wf = []
    for j in oidx:
        g = ((cost[:j] > 0).mean(0) >= 0.8) & (nex[:j].mean(0) >= 100.0)
        if g.sum() == 0 or j < 2: wf.append((0.0, 0.0, -1)); continue
        _, _, _, lo_j = tstats(ratio[:j]); cj = np.nonzero(g)[0]; vj = int(cj[np.argmax(lo_j[cj])]); wf.append((pnl[j, vj], cost[j, vj], vj))
    wp = np.array([x[0] for x in wf]); wc = np.array([x[1] for x in wf]); wr = np.where(wc > 0, wp / np.maximum(wc, 1e-12), 0.0); mu, l9, h9 = r4.tci(wr)
    from collections import Counter
    P('-- WALK-FORWARD (re-elige con los dias previos y mide el siguiente; N=20): EV/E agreg %+.3f | dia medio %+.3f IC90[%+.3f,%+.3f] dias+ %d/%d | elecciones: %s'
      % (wp.sum() / max(wc.sum(), 1e-12), mu, l9, h9, int((wr > 0).sum()), len(wr), dict(Counter(x[2] for x in wf).most_common(4))))
    ev_oos = pnl[nis:nis + no].sum(0) / np.maximum(cost[nis:nis + no].sum(0), 1e-12); ev_is = pnl[:nis].sum(0) / np.maximum(cost[:nis].sum(0), 1e-12)
    from scipy.stats import spearmanr
    rho = spearmanr(m[cand], ratio[nis:nis + no][:, cand].mean(0))[0]
    P('-- estabilidad de la seleccion: Spearman(media diaria IS, media diaria OOS) entre las %d candidatas = %+.3f' % (len(cand), rho))
    P('-- EFECTOS MARGINALES (candidatas IS; EV/E agregado OOS medio, ejec/dia OOS medias, N=20)')
    def attr(v):
        si, di_, bi_ = VARS[v]; sp_ = SPECS[si]
        return dict(tipo=sp_[0], theta=sp_[1], w1=sp_[2], w2=sp_[3], T=sp_[4], TD=sp_[5], delta=di_, banda=bi_)
    AT = [attr(int(v)) for v in cand]
    for f in ('tipo', 'theta', 'w1', 'w2', 'T', 'TD', 'delta', 'banda'):
        lv = sorted(set(a[f] for a in AT), key=str); cells = []
        for l in lv:
            ix = [cand[k] for k, a in enumerate(AT) if a[f] == l]
            cells.append('%s=%s: EV %+.3f ej %.0f (n=%d)' % (f, l, float(np.mean(ev_oos[ix])), float(nex[nis:nis + no][:, ix].mean()), len(ix)))
        P('   ' + ' | '.join(cells))
    dd = []
    for v in cand:
        si, di_, bi_ = VARS[int(v)]; sp_ = SPECS[si]
        if sp_[0] != 'S': continue
        sa = [k for k, q in enumerate(SPECS) if q[0] == 'A' and q[4] == sp_[4] and q[5] == sp_[5]][0]; va = vid(sa, di_, bi_)
        dd.append((sp_[1], ev_oos[int(v)] - ev_oos[va]))
    if dd: P('-- S menos SIEMPRE (mismos T/TD/delta/banda), EV/E OOS: media %+.3f, mediana %+.3f, rango [%+.3f,%+.3f] (n=%d); por theta: %s'
             % (np.mean([x[1] for x in dd]), np.median([x[1] for x in dd]), min(x[1] for x in dd), max(x[1] for x in dd), len(dd),
                {int(th): round(float(np.mean([x[1] for x in dd if x[0] == th])), 3) for th in THETAS}))
    P('-- BASE "COTIZAR SIEMPRE" (sin S): EV/E agreg IS | OOS | ejec/dia OOS (N=20)')
    for si, sp_ in enumerate(SPECS):
        if sp_[0] != 'A': continue
        for di_ in range(3):
            v = vid(si, di_, 0); P('   %-44s %+.3f | %+.3f | %.0f' % (vlabel(v), ev_is[v], ev_oos[v], nex[nis:nis + no, v].mean()))
    # detalle de la elegida
    G = json.load(open(I.CACHE)); rows = []
    for d in oos_days:
        _, rw, _ = run_day(d, G, only={VARS[vstar][0]}, detail={vstar}); rows += rw
    P('-- DETALLE OOS de la elegida: %d registros (suborden con relleno)' % len(rows))
    if rows:
        Rw = np.array([(x[3], x[4], x[5], x[8], x[11], x[12]) for x in rows]); mkk = np.array([x[2] for x in rows])
        y_, b_, q0_, tk_, tr_, adv_ = Rw.T; pn = tk_ * (y_ - b_); cs = tk_ * b_
        P('   EV/E (detalle, N=20) %+.3f sobre %.0f EUR de coste, %d mercados' % (pn.sum() / cs.sum(), cs.sum(), len(set(mkk.tolist()))))
        u_, inv = np.unique(mkk, return_inverse=True); pm = np.bincount(inv, weights=pn); cm = np.bincount(inv, weights=cs)
        rg = np.random.default_rng(2814); bs_ = []
        for _ in range(2000):
            ix = rg.integers(0, len(u_), len(u_)); bs_.append(pm[ix].sum() / cm[ix].sum())
        P('   bootstrap por MERCADO: IC90 [%+.3f, %+.3f]' % tuple(np.percentile(bs_, [5, 95])))
        def grp(name, edges, x):
            cells = []
            for lo_, hi_ in zip(edges[:-1], edges[1:]):
                k = (x >= lo_) & (x < hi_)
                if k.sum() == 0: continue
                cells.append('[%g,%g): EV %+.3f coste %.0f n=%d' % (lo_, hi_, pn[k].sum() / cs[k].sum(), cs[k].sum(), int(k.sum())))
            P('   por %s: ' % name + ' | '.join(cells))
        grp('T_rem del primer relleno', [0, 60, 120, 180, 240, 301], tr_)
        grp('precio de puja', [0.09, 0.15, 0.20, 0.25, 0.31], b_)
        for lab, k in (('cola 0 (bb+0.01)', q0_ <= 0), ('cola visible (bb)', (q0_ > 0) & (q0_ < 1e8)), ('solo travesia (bb-0.01)', q0_ >= 1e8), ('salto adverso <=5 s tras el relleno', adv_ == 1), ('sin salto adverso', adv_ == 0)):
            if k.sum(): P('   %-40s EV %+.3f coste %.0f n=%d' % (lab, pn[k].sum() / cs[k].sum(), cs[k].sum(), int(k.sum())))
    # capacidad
    P('-- CAPACIDAD de la elegida (OOS, EUR ~ pUSD sin FX): rampa de tamano; para 200.000 EUR/anio hace falta multiplicar')
    for nn, Nn in enumerate(NS):
        p = float(R[oidx, vstar, nn, 2].mean()); a = float(R[oidx, vstar, nn, 0].mean()); c = float(R[oidx, vstar, nn, 1].mean())
        P('   N=%2d: %.0f acc/dia (cuota %.2f %% del flujo S800 BTC), coste %.0f EUR/dia, pnl %+.1f EUR/dia = %+.0f EUR/anio; factor para 200 k: %s'
          % (Nn, a, 100 * a / max(flow_acc, 1e-9), c, p, p * 365, ('%.0fx' % (200000.0 / (p * 365))) if p > 0 else 'n/a (EV<=0)'))
    return


if __name__ == '__main__':
    t0 = time.time(); mode = sys.argv[1]; a = sys.argv; tag = a[a.index('--tag') + 1] if '--tag' in a else (a[2] if len(a) > 2 else '')
    try:
        if mode == 'ext':
            for d in a[2:]: ext(d)
        elif mode == 'sim':
            G = json.load(open(I.CACHE)); show = '--show' in a
            for d in [x for x in a[2:] if not x.startswith('--')]: simday(d, G, show)
        elif mode == 'fam':
            g = lambda k: a[a.index(k) + 1].split(',')
            fam(g('--is'), g('--oos'), tag, g('--dev') if '--dev' in a else [])
        else: P('modo desconocido')
    except Exception: P('ERROR', mode, traceback.format_exc()[-3500:])
    P('fin %s %.0f s' % (mode, time.time() - t0))
    if mode == 'fam': open(BASE + 'salida_fam_%s.txt' % tag, 'w').write('\n'.join(LINES) + '\n')
