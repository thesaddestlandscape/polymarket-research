#!/usr/bin/env python3
"""dem_hook_v2.py (ver_todos_17nov, 18-Nov) -- variantes del PREREG_VER_TODOS_v2_18nov (sha b3374be3...). SOLO LECTURA, 0 ordenes.
C1 tfill, C2 DEMe/DEMt sin tx con filas nuestras, C3 COLA_viva (resta tamano VIVO propio), C4 placebos +-30 s y rnd (20 semillas), paso 2a L2Q (L2 por nivel,
cola_vs_cruce/mk, recepcion ms -> t_ex = rx - SUELO), C5 caps de ventana. dem_hook.py (v1) NO se toca; se reutiliza su construir() para los eventos."""
import os, gzip, json, numpy as np, pandas as pd
import dem_hook as DH
TOLP = DH.TOLP; FLOOR = DH.FLOOR; MK = '/root/polymarket-research-datalogs/cola_vs_cruce/mk/'
TOKM = json.load(open('/root/polymarket-research-datalogs/cola_vs_cruce/tokens.json'))
CAPS = (605, 2675)       # p50/p90 vida de las NO rellenadas (prereg)
NRND = 20


def add_tfill(ev):
    """resid_t = S_T*tfill/mA - f_aj - f_own (C1). tfill = takerFillAmount (calldata w(96)), en unidades del makerAmount del tomador."""
    have = {}
    for c in DH.CACHES:
        if os.path.exists(c):
            for l in open(c):
                j = json.loads(l); have[j['tx']] = j['input']
    fr = []
    for r in ev.itertuples():
        inp = have.get(r.tx)
        if r.dec != 'ok' or inp is None: fr.append(np.nan); continue
        b = bytes.fromhex(inp[10:]); w = lambda i: int.from_bytes(b[i:i + 32], 'big'); tk = DH._parse_taker(inp)
        fr.append(w(96) / tk['mA'] if tk['mA'] else np.nan)
    ev['tfrac'] = fr; ev['resid_t'] = ev.S_T * ev.tfrac - ev.f_aj - ev.f_own
    return ev


def live_fn(size, own):
    ot = np.array([a for a, _ in own], float); osz = np.array([b for _, b in own], float)
    def live(t):
        t = np.asarray(t, float)
        if len(ot) == 0: return np.full(t.shape, size)
        return size - (osz[None, :] * (ot[None, :] < t[:, None])).sum(1)
    return live


def inject(prints, st, ss, L):
    pt, pp, ps = prints
    if len(st) == 0: return prints
    T_ = np.concatenate([np.asarray(pt, np.int64), np.asarray(st, np.int64)]); P_ = np.concatenate([np.asarray(pp, float), np.full(len(st), L)])
    Z_ = np.concatenate([np.asarray(ps, float), np.asarray(ss, float)]); o = np.argsort(T_, kind='stable')
    return T_[o], P_[o], Z_[o]


def bk_cola(D, k, L, ta, cola):
    bk = D.book(k, ta)
    if bk is None: return None
    if bk[0] > L + 1e-6 and np.isfinite(cola): bk = (L, bk[1], float(cola), bk[3])
    return bk


def q_viva(qt, v0, v2, prev, prevt, live):
    v2 = np.clip(np.asarray(v2, float) - live(qt), 0, None)
    prev = np.asarray(prev, float); pv = np.clip(prev - live(prevt), 0, None); pv[~np.isfinite(prev)] = np.nan
    return qt, v0, v2, pv


class L2Day:
    def __init__(self): self.cache = {}; self.order = []
    def _parse(self, fn):
        lv = {'Y': {}, 'N': {}}; book = {'Y': {}, 'N': {}}
        def rec(L_, p, t, s):
            e = lv[L_].get(p)
            if e is None: e = lv[L_][p] = ([], [])
            e[0].append(t); e[1].append(s)
        try:
            with gzip.open(fn, 'rt', errors='replace') as f:
                for ln in f:
                    c = ln.rstrip('\n').split(',')
                    if len(c) < 4 or c[0] not in lv: continue
                    L_, ty = c[0], c[1]
                    try:
                        if ty == 'B':
                            t = int(c[2]); new = {}
                            for it in c[3].split(';'):
                                if ':' in it: p, s = it.split(':'); new[int(round(float(p) * 1000))] = float(s)
                            old = book[L_]
                            for p in set(old) | set(new):
                                if abs(old.get(p, 0.0) - new.get(p, 0.0)) > 1e-9: rec(L_, p, t, new.get(p, 0.0))
                            book[L_] = new
                        elif ty == 'd':
                            t = int(c[2]); p = int(round(float(c[3]) * 1000)); s = float(c[4]); o = book[L_].get(p, 0.0)
                            if s > 0: book[L_][p] = s
                            else: book[L_].pop(p, None)
                            if abs(s - o) > 1e-9: rec(L_, p, t, s)
                    except (ValueError, IndexError): continue
        except (EOFError, OSError): pass
        return {L_: {p: (np.array(a, np.int64), np.array(b, float)) for p, (a, b) in d.items()} for L_, d in lv.items()}
    def series(self, tok, L):
        m = TOKM.get(str(tok))
        if m is None: return None
        act, mid, lado, _ = m; fn = MK + f'{act}_{mid}.gz'
        if not os.path.exists(fn): return None
        if fn not in self.cache:
            self.cache[fn] = self._parse(fn); self.order.append(fn)
            if len(self.order) > 6: self.cache.pop(self.order.pop(0), None)
        return self.cache[fn]['Y' if lado == 'YES' else 'N'].get(int(round(L * 1000)), (np.array([], np.int64), np.array([])))


def l2_q(ser, L, ta, te, size, live, suelo, shift=0, opt=False):
    """-> (ahead0, q) o None si no hay L2 antes de ta. q = filas (t, v0=L, v, prev) en (ta, te]."""
    t_rx, sz = ser
    if len(t_rx) == 0: return 0.0, (np.array([], np.int64), np.array([]), np.array([]), np.array([])), 0
    tx = t_rx - suelo + shift
    i0 = np.searchsorted(tx, ta, side='right')
    ahead0 = float(sz[i0 - 1]) if i0 > 0 else 0.0
    # aparicion de nuestra alta
    d = np.diff(np.concatenate([[0.0], sz])); cand = np.where((tx >= ta - 60) & (tx <= ta + 300) & (np.abs(d - size) <= 0.02))[0]
    found = int(len(cand) > 0); t_add = tx[cand[0]] if found else ta
    sub = np.where(tx >= t_add, live(tx), 0.0); vv = np.clip(sz - sub, 0, None)
    if found and cand[0] < i0: ahead0 = float(np.clip(sz[i0 - 1] - live(np.array([ta]))[0], 0, None))
    i1 = np.searchsorted(tx, te, side='right'); idx = np.arange(i0, i1)
    v = vv[idx]; prev = np.where(idx > 0, vv[np.maximum(idx - 1, 0)], np.nan)
    if opt:
        a = ahead0; out = []
        pvv = np.concatenate([[ahead0 if i0 == 0 else vv[i0 - 1]], v])
        for j in range(len(v)):
            a = max(0.0, min(a - max(0.0, pvv[j] - v[j]), v[j])); out.append(a)
        v = np.array(out, float); prev = np.concatenate([[ahead0], v[:-1]]) if len(v) else v
    return ahead0, (tx[idx], np.full(len(idx), L), v, prev), found


def dem_arrays(g, L, ta, te, kind, shift=0):
    if g is None or len(g) == 0: return np.array([], np.int64), np.array([])
    base = (g['eq'].values <= L + TOLP) & (g.n_aj.values > 0) & (g.f_own.values <= 0)
    rs = g.resid.values if kind == 'e' else g.resid_t.values
    t2 = g.t.values + (shift if np.isscalar(shift) else shift)
    m = base & (rs > FLOOR) & (t2 >= ta) & (t2 <= te)
    return t2[m].astype(np.int64), rs[m].astype(float)
