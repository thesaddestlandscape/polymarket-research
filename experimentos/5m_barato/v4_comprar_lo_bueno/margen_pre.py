#!/usr/bin/env python3
"""Margen (bid15 - ask5 - fee) ANTES del trigger frente a instantes aleatorios del mismo mercado; antelación del margen hasta cruzar 0,05."""
import json, sys, bisect, random, collections, statistics as st
S = sys.argv[1]
O = json.load(open(f'{S}/cron2_out.json'))
def fee(p): return 0.07 * p * (1 - p)
def fl(x): return None if x in ('', 'None') else float(x)
rng = random.Random(5)
res = []
byd = collections.defaultdict(list)
for r in O: byd[r['dia']].append(r)
M_ev = {250: [], 500: [], 1000: [], 3000: []}; M_pl = []
lead_cross = []
for dia, rs in sorted(byd.items()):
    toks = json.load(open(f'{S}/toks_{dia}.json'))
    ts = {t for v in toks.values() for t in v if t}
    q = collections.defaultdict(list)
    for fn in (f'{S}/qt5_{dia}.txt', f'{S}/qt15_{dia}.txt'):
        for ln in open(fn):
            if ln[0] != 'q': continue
            c = ln.rstrip('\n').split(',')
            if c[2] in ts:
                try: q[c[2]].append((int(c[7]), fl(c[3]), fl(c[4])))
                except Exception: pass
    for k in q: q[k].sort(key=lambda x: x[0])
    for r in rs:
        k5, k15 = toks[r['event_id']]
        Q5, Q15 = q.get(k5, []), q.get(k15, [])
        if not Q5 or not Q15: continue
        a5 = [x[0] for x in Q5]; a15 = [x[0] for x in Q15]
        def marg(t):
            i = bisect.bisect_right(a5, t) - 1; j = bisect.bisect_right(a15, t) - 1
            if i < 0 or j < 0: return None
            ask, bid = Q5[i][2], Q15[j][1]
            if ask is None or bid is None: return None
            return round(bid - ask - fee(ask), 4)
        t0 = r['t0']
        for w in M_ev:
            m = marg(t0 - w)
            if m is not None: M_ev[w].append(m)
        # instantes aleatorios del mismo mercado/ventana viva
        lo = (r['cierre'] - 300) * 1000 + 1500; hi = r['cierre'] * 1000 - 10000
        for _ in range(200):
            m = marg(rng.randint(lo, hi))
            if m is not None: M_pl.append(m)
        # tiempo desde que margen >= 0.0 (cruce de 0) hasta t0
        t = t0; 
        while t > t0 - 20000 and (marg(t - 50) or -1) >= 0.0: t -= 50
        lead_cross.append(t0 - t)
def pct(v, thr): return round(sum(1 for x in v if x >= thr) / len(v), 3) if v else None
print('margen a t0-w (eventos V4), n:', {w: len(v) for w, v in M_ev.items()})
for thr in (-0.05, 0.0, 0.02, 0.03, 0.04):
    print(f'  P(margen>={thr}):', {w: pct(v, thr) for w, v in M_ev.items()}, '| instantes aleatorios del mismo mercado (n=%d):' % len(M_pl), pct(M_pl, thr))
print('ms durante los que margen>=0 ANTES de t0 (retrocediendo en pasos de 50 ms, tope 20 s): P10/25/50/75/90',
      [sorted(lead_cross)[min(len(lead_cross) - 1, int(p * len(lead_cross)))] for p in (.1, .25, .5, .75, .9)])
