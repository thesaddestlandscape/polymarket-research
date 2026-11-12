#!/usr/bin/env python3
"""engine_v3.py -- fill_segment con DEDUPE de cola (doble conteo print/fila de libro) + DayEngV3. FICHERO NUEVO: engine.py (dev) NO se edita. Solo calculo, 0 ordenes.

PROBLEMA (visto leyendo engine.fill_segment BASE; aqui MEDIDO con test_v3.py y diag): un consumo de S acciones en el nivel L del mejor bid llega dos veces al motor:
  (a) como FILA de libro (bid == L, szb baja S)  -> `ahead = min(ahead, v)` (evento tipo 0, reloj EXCHANGE de la fila),
  (b) como PRINT del tx (S acciones)              -> `ahead -= s` (evento tipo 1, sello tm).
Si el print va sellado en/tras la fila (sort por (t, tipo) pone el libro antes que el print), la cola se descuenta DOS veces: la cola 'ahead' baja a v - S en vez de v y el siguiente
consumidor rellena un relleno FANTASMA. Con el sello correcto (tm = ex(fila) - 1 ms) el print va antes de su fila y el min() es neutro.
FIX (dedupe=True): cada grupo de prints (mismo sello y nivel L) cuya suma coincide (+-tol) con la caida de szb de una fila en (t_print - row_win, t_print] se procesa ANTES de esa fila
(clave de orden (t_fila, -1)). Solo se toca el ORDEN, no los tamanos, y solo para prints con fila emparejada por tamano EXACTO (la firma del consumo). dedupe=False == engine.fill_segment original.
qupd extendido: (t, v0, v2, v2prev) con v2prev = szb de la fila anterior del token si su bid era L (si no NaN: no es consumo 'dec')."""
import sys, numpy as np
import engine_clock as EC
G = EC.G
EPS, TOLP, INF = G.EPS, G.TOLP, G.INF


def fill_segment_v3(book_arr, xa, qupd, prints, L, t_arr, t_end, rem, variant, dedupe=True, row_win=100, tol_s=0.015, diag=None):
    if book_arr is None: return 0.0, None, 'sin_libro'
    bid, ask, bsz, _ = book_arr
    if not (ask > L + EPS): return 0.0, None, 'seria_taker'
    top = abs(bid - L) < EPS
    if variant == 'OPT': ahead = 0.0
    elif bid > L + EPS: ahead = INF
    elif top: ahead = bsz + (xa if variant == 'CONS' else 0.0)
    else: ahead = xa if variant == 'CONS' else 0.0
    rows = []          # (t, v2, v2prev)
    if variant == 'BASE':
        qt, v0, v2 = qupd[0], qupd[1], qupd[2]; v2p = qupd[3] if len(qupd) > 3 else None
        for j in np.where(np.abs(np.asarray(v0, float) - L) < EPS)[0]: rows.append((int(qt[j]), float(v2[j]), float(v2p[j]) if v2p is not None else float('nan')))
    pt, pp, ps = prints
    pr = [(int(pt[j]), float(pp[j]), float(ps[j])) for j in range(len(pt))]
    first_before = set()                                              # indices de print que se reordenan antes de su fila
    pair_t = {}
    if dedupe and rows and pr:
        # grupos de prints en L con el mismo sello: suma = consumo de un tx
        grp = {}
        for i, (t, q, s) in enumerate(pr):
            if abs(q - L) <= TOLP: grp.setdefault(t, []).append(i)
        used = set()
        for t, idxs in sorted(grp.items()):
            S = sum(pr[i][2] for i in idxs); best = None
            for r, (tr, v, vp) in enumerate(rows):
                if r in used or not np.isfinite(vp): continue
                if t - row_win <= tr <= t and abs((vp - v) - S) <= tol_s: best = r if best is None or tr > rows[best][0] else best     # fila mas reciente <= sello
            if best is not None:
                used.add(best)
                for i in idxs: first_before.add(i); pair_t[i] = rows[best][0]
    evs = []
    for (t, v, vp) in rows: evs.append((t, 1, 0, v))                  # (t, orden, tipo, dato): fila
    for i, (t, q, s) in enumerate(pr):
        if i in first_before: evs.append((pair_t[i], 0, 1, (q, s, t)))   # print antes de su fila (tf conserva el sello ORIGINAL del print)
        else: evs.append((t, 2, 1, (q, s, t)))                         # orden normal: fila (1) antes que print (2) en empates, como el original
    evs.sort(key=lambda e: (e[0], e[1]))
    if variant == 'BASE' and top: ahead = min(ahead, bsz)
    qty = 0.0; tf = None
    for (t, _o, kind, v) in evs:
        if kind == 0:
            ahead = min(ahead, v); continue
        q, s, t = v                                                   # t = sello original del print (no el de la fila con la que se reordena)
        if q < L - TOLP: g = rem - qty; qty += g; tf = t if tf is None else tf; break
        if abs(q - L) <= TOLP:
            if ahead >= s - 1e-9: ahead -= s
            else:
                g = min(rem - qty, s - ahead); ahead = 0.0; qty += g; tf = t if tf is None else tf
                if qty >= rem - 1e-9: break
    if diag is not None: diag['paired'] = diag.get('paired', 0) + len(first_before)
    return qty, tf, 'ok'


class DayEngV3(EC.DayEngClock):
    """DayEngClock + D con rx alineado (with_otro) + run_segment con dedupe. `dedupe` e instrumentos en self.dedupe / self.diag."""
    def __init__(self, d, tape_mode, chain=None, bad_hours=None, universe=('ETH', 'SOL', 'XRP'), modo='causal', dedupe=True):
        import pandas as pd
        R = EC.R
        assert modo in EC.MODOS, modo
        self.modo = modo; fc, kc = EC.MODOS[modo]; self.clock_fill, self.clock_know = fc, kc
        self.capt = R.capt; self.d = d
        D = self.D = R.Day2(d, fc, with_otro=(fc == 'ex'))
        self.K = D if kc == fc else R.Day2(d, kc, light=True, with_otro=(kc == 'rx' and fc == 'ex'))
        self.tape = G.Tape(tape_mode, D, chain); self.bad = bad_hours or set()
        self.day0 = int(pd.Timestamp(d, tz='UTC').timestamp()) * 1000; self.day1 = self.day0 + 86400000
        self.ks = [k for k in range(len(D.toks)) if D.marco[k] == '5min' and D.act[k] in universe]
        self.S = {}; self.dedupe = dedupe; self.diag = {}

    def qupd3(self, k, L, t0, t1):
        D = self.D; a, b = D.qb[k], D.qb[k + 1]; qt = D.qt[a:b]; i0 = np.searchsorted(qt, t0, side='right'); i1 = np.searchsorted(qt, t1, side='right')
        s, e = a + i0, a + i1
        prev = np.full(e - s, np.nan)
        if e > s:
            j = np.arange(s, e) - 1; ok = j >= a
            pv0 = np.where(ok, D.v0[np.maximum(j, 0)], np.nan); pv2 = np.where(ok, D.v2[np.maximum(j, 0)], np.nan)
            prev = np.where(ok & (np.abs(pv0.astype(float) - L) < EPS), pv2, np.nan)
        return qt[i0:i1], D.v0[s:e], D.v2[s:e], prev

    def run_segment(self, k, L, t_arr, t_end, rem, variant):
        return fill_segment_v3(self.D.book(k, t_arr), self.xa(k, L, t_arr) if variant == 'CONS' else 0.0, self.qupd3(k, L, t_arr, t_end) if variant == 'BASE' else None,
                               self.tape.get(k, L, t_arr, t_end), L, t_arr, t_end, rem, variant, dedupe=self.dedupe, diag=self.diag)
