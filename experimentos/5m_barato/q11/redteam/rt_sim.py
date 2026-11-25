#!/usr/bin/env python3
"""Red-team R1 (DISENO_RT.md sha 1b93653e). DEV, solo lectura, 0 ordenes. Uso: nice -n 19 ionice -c3 python3 -I rt_sim.py DIA -> out/RT_<D>.pkl
Segmentos y cinta = passC5c/passC5d de barrido_corr (copiados literal); solo cambia el modelo de relleno."""
import sys, os, json, time, gc, numpy as np, pandas as pd
T0 = time.time()
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = H + 'out/'; BC = H + '../barrido_corr/out/'
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
sys.path.insert(0, P2 + 'escalera_B'); import engine as G
PB = P2 + 'precursores_barrido/out/'
d = sys.argv[1]
if os.path.exists(OUT + f'RT_{d}.pkl'): print('ya', d); sys.exit(0)
tape = pd.read_pickle(PB + f'tape_{d}.pkl'); bad = {tuple(x) for x in json.load(open(PB + f'bad_{d}.json'))['bad']}
E = G.DayEng(d, 'chain', tape, bad); D = E.D
tp = tape.assign(k=tape.token_id.map(D.tokidx)); tp = tp[tp.k.notna()].copy(); tp['k'] = tp.k.astype(int)
ev = tp.groupby(['k', 'tx']).agg(t=('t_ws_ms', 'min'), pmin=('price', 'min')).reset_index()
tm = np.empty(len(ev), np.int64); evk = ev.k.values; evt = ev.t.values.astype(np.int64); evp = ev.pmin.values
for i in range(len(ev)):
    k = evk[i]; t = evt[i]; pm = evp[i]
    a, b = D.qb[k], D.qb[k + 1]; qt = D.qt[a:b]; v0 = D.v0[a:b]
    i0 = np.searchsorted(qt, t - 400, side='left'); i1 = np.searchsorted(qt, t, side='right'); tm[i] = t - 63
    if i1 > i0 and i0 > 0:
        lo = v0[i0 - 1:i1] <= pm + G.TOLP; w = np.where(lo[1:] & ~lo[:-1])[0]
        if len(w): tm[i] = int(qt[i0 + w[0]])
ev['tm'] = tm
tp = tp.merge(ev[['k', 'tx', 'tm']], on=['k', 'tx'], how='left'); tp['t_ws_ms'] = tp.tm.astype(np.int64)
E.tape = G.Tape('chain', D, tp.drop(columns=['k', 'tm'])); del tp, tape, ev; gc.collect()
ks = [k for k in E.ks if E.sane(k) == 'ok' and G.capt_outcome(E, k) is not None]
FE = {k: E.feats(k) for k in ks}
SC = {}; thr = None
if os.path.exists(BC + f'Po_{d}.pkl'):
    P = pd.read_pickle(BC + f'Po_{d}.pkl')[['k', 'L', 't', 'p_OWN']]; thr = json.load(open(BC + 'C2o_thr.json'))[d]['OWN']['0.5']
    for (k, L), g in P.groupby(['k', 'L']): SC[(int(k), round(float(L), 2))] = (g.t.values.astype(np.int64), g.p_OWN.values.astype(float))
    del P
def series(k, L, g):
    out = np.full(len(g), np.nan); a = SC.get((k, L))
    if a is None: return out
    idx = np.searchsorted(g, a[0]); ok = (idx < len(g)) & (g[np.minimum(idx, len(g) - 1)] == a[0]); out[idx[ok]] = a[1][ok]; return out
def segs(grid, can_arm, Gm, fin):
    n = len(grid); out = []; hard = (fin - G.TMIN) * 1000 + 60; falsos = np.where(~Gm)[0]; i = 0
    while i < n:
        if not can_arm[i]: i += 1; continue
        t = int(grid[i]); t_arr = t + G.LAT_POST; pos = np.searchsorted(falsos, i + 1); j = falsos[pos] if pos < len(falsos) else n
        t_end = min(int(grid[j]) + 60 if j < n else hard, hard)
        if t_end > t_arr: out.append((t, t_arr, t_end))
        i = max(i + 1, int(np.searchsorted(grid, t_end)))
    return out
def qall(k, t0, t1):
    a, b = D.qb[k], D.qb[k + 1]; qt = D.qt[a:b]; i0 = np.searchsorted(qt, t0, side='right'); i1 = np.searchsorted(qt, t1, side='right')
    return qt[i0:i1], D.v0[a + i0:a + i1], D.v1[a + i0:a + i1], D.v2[a + i0:a + i1], D.v3[a + i0:a + i1]
def mid_at(k, t):
    bk = D.book(k, t); return np.nan if bk is None else (bk[0] + bk[1]) / 2
def cross_events(k, L, t_arr, t_end):
    """(libros cruzados/bloqueados excluidos) (t, size) en que la orden real habria sido CRUZADA: ask propio <= L o bid del complementario >= 1-L (vigente en t_arr o nuevo dentro)."""
    evs = []
    bk = D.book(k, t_arr)
    if bk is not None and bk[1] <= L + G.EPS and bk[1] > bk[0] + G.EPS: evs.append((t_arr, float(bk[3])))
    qt, v0, v1, v2, v3 = qall(k, t_arr, t_end)
    for j in np.where((np.asarray(v1, float) <= L + G.EPS) & (np.asarray(v1, float) > np.asarray(v0, float) + G.EPS))[0]: evs.append((int(qt[j]), float(v3[j])))
    kX = D.comp(k)
    if kX is not None:
        bx = D.book(kX, t_arr)
        if bx is not None and bx[0] >= 1 - L - G.EPS and bx[1] > bx[0] + G.EPS: evs.append((t_arr, float(bx[2])))
        qt, v0, v1, v2, v3 = qall(kX, t_arr, t_end)
        for j in np.where((np.asarray(v0, float) >= 1 - L - G.EPS) & (np.asarray(v1, float) > np.asarray(v0, float) + G.EPS))[0]: evs.append((int(qt[j]), float(v2[j])))
    evs.sort(); return evs
def fill_v(k, L, t_arr, t_end, rem, fv):
    if fv in ('BASE', 'OPT'):
        q, tf, _ = E.run_segment(k, L, t_arr, t_end, rem, fv); return q, tf
    book = D.book(k, t_arr)
    if book is None or not (book[1] > L + G.EPS): return 0.0, None
    pt, pp, ps = E.tape.get(k, L, t_arr, t_end)
    if fv == 'STRICT':
        j = np.where(pp < L - G.TOLP)[0]
        return (rem, int(pt[j[0]])) if len(j) else (0.0, None)
    if fv == 'THIN':
        bid, ask, bsz, _ = book; top = abs(bid - L) < G.EPS
        ahead = float('inf') if bid > L + G.EPS else (bsz if top else 0.0)
        qt, v0, v2 = E.qupd(k, t_arr, t_end); evs = [(int(qt[j]), 0, float(v2[j])) for j in np.where(np.abs(np.asarray(v0, float) - L) < G.EPS)[0]]
        evs += [(int(pt[j]), 1, (float(pp[j]), float(ps[j]))) for j in range(len(pt))]; evs.sort(key=lambda e: (e[0], e[1]))
        qty = 0.0; tf = None
        for t, kind, v in evs:
            if kind == 0: ahead = min(ahead, v); continue
            p, s = v
            if p < L - G.TOLP: g = min(rem - qty, s); qty += g; tf = t if tf is None else tf
            elif abs(p - L) <= G.TOLP:
                if ahead >= s - 1e-9: ahead -= s
                else: g = min(rem - qty, s - ahead); ahead = 0.0; qty += g; tf = t if tf is None else tf
            if qty >= rem - 1e-9: break
        return qty, tf
    if fv == 'CROSS':
        q, tf, _ = E.run_segment(k, L, t_arr, t_end, rem, 'BASE')
        ce = cross_events(k, L, t_arr, t_end)
        if ce and (tf is None or ce[0][0] < tf):
            # relleno temprano por cruce (todo el resto pendiente: cota alta); si BASE ya rellena despues, se adelanta
            return rem, int(ce[0][0])
        return q, tf
FV = ('BASE', 'STRICT', 'OPT', 'CROSS', 'THIN')
POL = [('G0', None), ('GEO6', 'geo')] + ([('PG_O50', 'pg')] if SC else [])
FILLS = []; DIAG = []; SEGN = []
for name, kind in POL:
    for k in ks:
        g, bid, ask, b15, vol, hora = FE[k]; fin = int(D.fin[k]); gana = G.capt_outcome(E, k)
        for L in G.LEVELS:
            Gm = G.gate_vec('G', L, b15, vol, hora)
            with np.errstate(invalid='ignore'):
                if kind is None: pm = np.ones(len(g), bool)
                elif kind == 'geo': pm = np.isfinite(bid) & ((bid - L) >= 0.06 - 1e-6)
                else: pm = series(k, round(L, 2), g) <= thr
            can = Gm & pm & np.isfinite(ask) & (ask > L + G.EPS); rem = {f: 5.0 for f in FV}
            for si, (t_dec, t_arr, t_end) in enumerate(segs(g, can, Gm, fin)):
                if all(rem[f] <= 1e-9 for f in FV): break
                SEGN.append((name, k, L, si, t_dec, t_arr, t_end))
                res = {}
                for f in FV:
                    if rem[f] <= 1e-9: continue
                    q, tf = fill_v(k, L, t_arr, t_end, rem[f], f); res[f] = (q, tf)
                    if q > 1e-9:
                        rem[f] -= q
                        FILLS.append((name, f, d, D.act[k], D.lado[k], fin, k, L, float(q), int(tf), gana, si, t_dec))
                if 'BASE' in res and res['BASE'][0] > 1e-9:
                    tfb = res['BASE'][1]; qt, v0, v1, v2, v3 = qall(k, t_arr, tfb)
                    bk0 = D.book(k, t_arr); bel = np.where(np.asarray(v0, float) < L - G.EPS)[0]
                    t_below = t_arr if (bk0 is not None and bk0[0] < L - G.EPS) else (int(qt[bel[0]]) if len(bel) else -1)
                    ce = cross_events(k, L, t_arr, tfb); t_cr = ce[0][0] if ce else -1
                    tc = res.get('CROSS', (0, None))[1]
                    DIAG.append((name, d, k, L, si, t_dec, t_arr, tfb, t_below, t_cr, bk0[0] if bk0 else np.nan, mid_at(k, tfb - 300), mid_at(k, tc - 300) if tc else np.nan, gana))
R = pd.DataFrame(FILLS, columns=['pol', 'fv', 'dia', 'act', 'lado', 'fin', 'k', 'L', 'q', 'tf', 'gana', 'seg', 't_dec'])
R['cost'] = R.q * R.L; R['pnl'] = R.q * (R.gana - R.L) + R.q * 0.2 * 0.07 * R.L * (1 - R.L)
DG = pd.DataFrame(DIAG, columns=['pol', 'dia', 'k', 'L', 'seg', 't_dec', 't_arr', 'tf', 't_below', 't_cross', 'bid_arr', 'm_tf300', 'm_tc300', 'gana'])
# chequeo espejo: ask YES vs 1 - bid NO en la rejilla (muestra)
mir = []
for k in ks[:200]:
    kX = D.comp(k); g = FE[k][0][::20]
    for t in g:
        a = D.book(k, t); b = D.book(kX, t)
        if a and b and np.isfinite(a[1]) and np.isfinite(b[0]): mir.append(abs(a[1] - (1 - b[0])) < 1e-6)
R.to_pickle(OUT + f'RT_{d}.pkl.tmp'); DG.to_pickle(OUT + f'DG_{d}.pkl')
os.replace(OUT + f'RT_{d}.pkl.tmp', OUT + f'RT_{d}.pkl')
print('ok', d, 'espejo', round(float(np.mean(mir)), 3) if mir else None, {(p, f): (len(x), round(float(x.pnl.sum()), 1)) for (p, f), x in R.groupby(['pol', 'fv'], sort=False)}, round(time.time() - T0, 1), 's', flush=True)
