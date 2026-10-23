#!/usr/bin/env python3
"""d1_l2_motor.py -- PREREG_CONTROL (sha 37f710e2...). Motor L2 sobre el libro5 por mercado (cola_vs_cruce/mk, 20-22 Oct, ETH/SOL/XRP 5m, bids, libro unificado, recepcion en ms).
Genera: (a) eventos = prints de consumo de nivel (normalizados al libro de bids del token) en bandas A (0,10-0,30] y B (0,30-0,70], T 50-300 s, con S(q,t-1000)>=5, mas 3 controles aleatorios
por evento (mismo mercado-token-nivel, +-60 s, sin print en [t-1000,t+3000]); metricas de retirada neta y features causales a t_f=m-300 ms (nivel, top, imbalance de cima, flujo tomador);
(b) agregados por nivel para la dinamica de cancelacion. Salidas (fuera de git): DL/cola_posicion/l2_eventos.csv.gz, l2_agregado.csv.gz."""
import sys, os, json, gzip, hashlib, bisect, glob, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); DL = '/root/polymarket-research-datalogs/cola_posicion/'
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_CONTROL.md'), 'rb').read()).hexdigest().startswith('37f710e298664193')
TM = json.load(open('/root/polymarket-research-datalogs/cola_vs_cruce/tokens.json'))
FIN = {}
for t, (act, mid, lado, fin) in TM.items(): FIN[(act, mid)] = fin
MK = '/root/polymarket-research-datalogs/cola_vs_cruce/mk/'
def mills(p): return int(round(float(p) * 1000))
def banda(q): return 'A' if 100 < q <= 300 else ('B' if 300 < q <= 700 else None)
def carga(path):
    bids = {'Y': {}, 'N': {}}; valid = {'Y': False, 'N': False}
    lv = {}; topT = {'Y': [], 'N': []}; topV = {'Y': [], 'N': []}; pr = {}; allp = {'Y': [], 'N': []}
    def upd(L, q, sz, r):
        e = lv.get((L, q))
        if e is None: e = lv[(L, q)] = ([], [])
        e[0].append(r); e[1].append(sz)
    def push_top(L, r):
        b = max(bids[L]) if (valid[L] and bids[L]) else -1
        if not topV[L] or topV[L][-1] != b: topT[L].append(r); topV[L].append(b)
    with gzip.open(path, 'rt', errors='replace') as f:
        try:
            for ln in f:
                c = ln.rstrip('\n').split(',')
                if len(c) < 4: continue
                L, ty = c[0], c[1]
                try:
                    if ty == 'd':
                        if not valid[L]: continue
                        r = int(c[2]); q = mills(c[3]); sz = float(c[4]); old = bids[L].get(q, 0.0)
                        if sz > 0: bids[L][q] = sz
                        else: bids[L].pop(q, None)
                        if abs(sz - old) > 1e-9: upd(L, q, sz, r)
                        push_top(L, r)
                    elif ty == 'B':
                        r = int(c[2]); nb = {}
                        for x in c[3].split(';'):
                            if ':' in x:
                                p, z = x.split(':'); z = float(z)
                                if z > 0: nb[mills(p)] = z
                        for q in set(bids[L]) | set(nb):
                            if abs(nb.get(q, 0.0) - bids[L].get(q, 0.0)) > 1e-9 or not valid[L]: upd(L, q, nb.get(q, 0.0), r)
                        bids[L] = nb; valid[L] = True; push_top(L, r)
                    elif ty == 'G':
                        valid[L] = False; push_top(L, int(c[2]))
                    elif ty == 'T':
                        r = int(c[2]); q = mills(c[4]); a = float(c[5]); O = 'N' if L == 'Y' else 'Y'
                        if c[3] == 'SELL': pr.setdefault((L, q), []).append((r, a)); allp[L].append((r, q, a))
                        else: pr.setdefault((O, 1000 - q), []).append((r, a)); allp[O].append((r, 1000 - q, a))
                except (ValueError, IndexError): continue
        except (EOFError, OSError): pass
    lvn = {k: (np.array(a, np.int64), np.array(b, float)) for k, (a, b) in lv.items()}
    prn = {}
    for k, v in pr.items():
        v.sort(); keep = []
        for r, a in v:
            if keep and abs(a - keep[-1][1]) < 1e-3 and r - keep[-1][0] < 50: continue
            keep.append((r, a))
        prn[k] = (np.array([x[0] for x in keep], np.int64), np.array([x[1] for x in keep], float))
    tp = {L: (np.array(topT[L], np.int64), np.array(topV[L], np.int64)) for L in 'YN'}
    ap = {L: (np.array(sorted(x)) if x else np.zeros((0, 3))) for L, x in allp.items()}
    return lvn, prn, tp, ap
def S(lvn, L, q, t):
    e = lvn.get((L, q))
    if e is None: return 0.0
    i = np.searchsorted(e[0], t, 'right') - 1
    return float(e[1][i]) if i >= 0 else 0.0
def best(tp, L, t):
    a, b = tp[L]; i = np.searchsorted(a, t, 'right') - 1
    return int(b[i]) if i >= 0 else -1
def cons_between(prn, L, q, t0, t1):
    e = prn.get((L, q))
    if e is None: return 0.0, 0
    i0 = np.searchsorted(e[0], t0, 'right'); i1 = np.searchsorted(e[0], t1, 'right'); return float(e[1][i0:i1].sum()), int(i1 - i0)
def metricas(lvn, prn, L, q, t):
    s1 = S(lvn, L, q, t - 1000); s2 = S(lvn, L, q, t - 150)
    c, n = cons_between(prn, L, q, t - 1000, t - 150)
    e = lvn.get((L, q)); upd = adds = canc = 0.0
    if e is not None:
        i0 = np.searchsorted(e[0], t - 1000, 'right'); i1 = np.searchsorted(e[0], t - 150, 'right')
        seg = e[1][max(i0 - 1, 0):i1]
        if i0 == 0: seg = np.r_[0.0, seg]
        if len(seg) > 1:
            d = np.diff(seg); upd = float(len(d)); adds = float(d[d > 0].sum()); canc = float(-d[d < 0].sum())
    return s1, s2, c, n, upd, adds, canc
def procesa(path, act, mid, rng):
    fin = FIN[(act, mid)]; lvn, prn, tp, ap = carga(path)
    dia = pd.Timestamp(fin - 1, unit='s').strftime('%Y-%m-%d'); rows = []; agg = []
    for (L, q), (rt, rs) in prn.items():
        bd = banda(q)
        if bd is None: continue
        O = 'N' if L == 'Y' else 'Y'
        for r, a in zip(rt, rs):
            T = fin - r / 1000
            if not (50 <= T <= 300): continue
            s1, s2, c, n, upd, adds, canc = metricas(lvn, prn, L, q, r)
            s1ok = int(s1 >= 5)
            if not s1ok and bd != 'A': continue
            tf = r - 300
            bL = best(tp, L, tf); bO = best(tp, O, tf)
            row = dict(grp='E', s1ok=s1ok, mid=mid, act=act, L=L, fin=fin, dia=dia, r=int(r), q=q, banda=bd, T=T, size=a, S1000=s1, S150=s2, cons=c, ncons=n, upd=upd, adds=adds, canc=canc)
            # features causales a t_f = r-300
            sf = S(lvn, L, q, tf); s1f = S(lvn, L, q, tf - 1000); cf, nf = cons_between(prn, L, q, tf - 1000, tf)
            e = lvn.get((L, q)); updf = addf = canf = 0.0; ageL = 60000
            if e is not None:
                i0 = np.searchsorted(e[0], tf - 1000, 'right'); i1 = np.searchsorted(e[0], tf, 'right'); seg = e[1][max(i0 - 1, 0):i1]
                if i0 == 0: seg = np.r_[0.0, seg]
                if len(seg) > 1:
                    d = np.diff(seg); updf = float(len(d)); addf = float(d[d > 0].sum()); canf = float(-d[d < 0].sum())
                z = np.where(e[1][:i1] <= 0)[0]
                ageL = min(60000, int(tf - e[0][z[-1]])) if len(z) else 60000
            bsz = S(lvn, L, bL, tf) if bL > 0 else 0.0; asz = S(lvn, O, bO, tf) if bO > 0 else 0.0
            ta = tp[L][0]; tv = tp[L][1]
            def top_at(tt): return best(tp, L, tt)
            i2 = np.searchsorted(ta, tf, 'right'); i1_ = np.searchsorted(ta, tf - 1000, 'right')
            ap_L = ap[L]; ap_O = ap[O]
            def flow(arr, t0, t1):
                if len(arr) == 0: return 0.0, 0.0, 0
                m = (arr[:, 0] > t0) & (arr[:, 0] <= t1); x = arr[m]
                return float(x[:, 2].sum()), float((x[:, 2] * (x[:, 1] > q)).sum()), int(len(x))
            f1, f1b, n1 = flow(ap_L, tf - 1000, tf); f3, f3b, n3 = flow(ap_L, tf - 3000, tf); g1, _, gn1 = flow(ap_O, tf - 1000, tf); g3, _, gn3 = flow(ap_O, tf - 3000, tf)
            row.update(Sf=sf, S1000f=s1f, consf=cf, updf=updf, addf=addf, cancf=canf, ageL=ageL, bestL=bL, bestO=bO, dist=(bL - q) / 10 if bL > 0 else np.nan,
                       bsz=bsz, asz=asz, spread=(1000 - bO - bL) if (bL > 0 and bO > 0) else np.nan, dtop300=top_at(tf) - top_at(tf - 300), dtop1000=top_at(tf) - top_at(tf - 1000), ntop1s=int(i2 - i1_),
                       flow1=f1, flow1_better=f1b, nflow1=n1, flow3=f3, away1=g1, away3=g3, awayn1=gn1)
            rows.append(row)
            # controles
            kk = 0
            for _ in range(15 if s1ok else 0):
                if kk >= 3: break
                t = int(r + rng.integers(-60000, 60001)); Tt = fin - t / 1000
                if not (50 <= Tt <= 300) or abs(t - r) < 4000: continue
                cc, nn = cons_between(prn, L, q, t - 1000, t + 3000)
                if nn > 0: continue
                m1, m2, c1, n1_, u1, a1, k1 = metricas(lvn, prn, L, q, t)
                if m1 < 5: continue
                rows.append(dict(grp='C', mid=mid, act=act, L=L, fin=fin, dia=dia, r=t, q=q, banda=bd, T=Tt, size=a, S1000=m1, S150=m2, cons=c1, ncons=n1_, upd=u1, adds=a1, canc=k1,
                                 bestL=best(tp, L, t - 150), pair=int(r))); kk += 1
    # agregado por nivel
    for (L, q), (te, se) in lvn.items():
        bd = banda(q)
        if bd is None or len(te) < 2: continue
        T = fin - te / 1000; m = (T >= 50) & (T <= 290)
        d = np.diff(se, prepend=0.0); idx = np.where(m)[0]
        if len(idx) == 0: continue
        bt = tp[L]; bi = np.searchsorted(bt[0], te[idx], 'right') - 1; bb = np.where(bi >= 0, bt[1][np.maximum(bi, 0)], -1); dist = (bb - q) / 10
        rk = np.where(dist <= 0, 'best', np.where(dist <= 1, 'b1', 'b2+')); half = np.where(T[idx] > 170, 'T170-290', 'T50-170')
        dd = d[idx]; pe = prn.get((L, q))
        dfa = pd.DataFrame(dict(rk=rk, half=half, dec=np.where(dd < 0, -dd, 0.0), inc=np.where(dd > 0, dd, 0.0), n=1))
        g = dfa.groupby(['rk', 'half']).sum().reset_index()
        for _, x in g.iterrows():
            p_sum = 0.0
            agg.append(dict(act=act, mid=mid, dia=dia, banda=bd, rk=x.rk, half=x.half, dec=x.dec, inc=x.inc, n=x.n))
        if pe is not None:
            Tp = fin - pe[0] / 1000; mp = (Tp >= 50) & (Tp <= 290)
            if mp.any():
                bi = np.searchsorted(bt[0], pe[0][mp], 'right') - 1; bb = np.where(bi >= 0, bt[1][np.maximum(bi, 0)], -1); dist = (bb - q) / 10
                rk = np.where(dist <= 0, 'best', np.where(dist <= 1, 'b1', 'b2+')); half = np.where(Tp[mp] > 170, 'T170-290', 'T50-170')
                gp = pd.DataFrame(dict(rk=rk, half=half, pr=pe[1][mp])).groupby(['rk', 'half']).pr.sum().reset_index()
                for _, x in gp.iterrows(): agg.append(dict(act=act, mid=mid, dia=dia, banda=bd, rk=x.rk, half=x.half, dec=0.0, inc=0.0, n=0, prints=x.pr))
    return rows, agg
if __name__ == '__main__':
    files = sorted(glob.glob(MK + '*.gz')); rng = np.random.default_rng(20261022); R = []; A = []
    ini = int(sys.argv[1]) if len(sys.argv) > 1 else 0; fin_i = int(sys.argv[2]) if len(sys.argv) > 2 else len(files)
    for k, f in enumerate(files[ini:fin_i]):
        act, mid = os.path.basename(f)[:-3].split('_')
        try: r, a = procesa(f, act, mid, rng)
        except Exception as e: print('fallo', f, type(e).__name__, e, flush=True); continue
        R += r; A += a
        if k % 200 == 0: print(k, len(R), flush=True)
    pd.DataFrame(R).to_csv(DL + f'l2_eventos_{ini}.csv.gz', index=False); pd.DataFrame(A).to_csv(DL + f'l2_agregado_{ini}.csv.gz', index=False)
    print('eventos', len(R), 'agregado', len(A))
