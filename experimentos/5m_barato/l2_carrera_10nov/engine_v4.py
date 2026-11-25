#!/usr/bin/env python3
"""engine_v4.py -- engine_v3 SIN POLVO (16-Nov). FICHERO NUEVO: engine_v3.py y engine.py (dev) NO se editan. Solo calculo, 0 ordenes.

DEFECTO CORREGIDO ("polvo"): la cola `ahead` sale del libro en float32 y el print en float64. Si el print agota la cola EXACTAMENTE (cola 16,2 y print 16,2 -> resto ~1e-7),
`ahead >= s - 1e-9` falla y la rama else devolvia `s - ahead` (~2e-7) como relleno FANTASMA (23-Oct ETH x=40 cola 16,2; SOL x=35 cola 19,78; passT 26-Oct..09-Nov: 5 de 4.601 rellenos G0).
REGLA UNICA (funcion `relleno` + `suelo`, usadas por TODOS los sitios; ningun umbral suelto fuera de este fichero):
  * todo relleno < FLOOR (1e-3 acciones) vale 0 y NO fecha tf;
  * cola agotada = agotada: si ahead - s <= tol (tol = max(FLOOR, RTOL*s), RTOL=1e-6) la cola queda en 0 y no hay relleno por ese print;
  * ahead siempre float64.
`es_fill(q)` (q >= FLOOR) es el unico criterio de "hay relleno" para verif/passT. `assert_sin_polvo(q)` falla si 0 < q < FLOOR.
El resto (dedupe de cola, orden de eventos) es engine_v3.fill_segment_v3 sin cambios."""
import sys, numpy as np
import engine_clock as EC
import engine_v3 as E3
G = EC.G
EPS, TOLP, INF = G.EPS, G.TOLP, G.INF
FLOOR = 1e-3          # acciones: suelo absoluto de relleno
RTOL = 1e-6           # tolerancia relativa al tamano del print
VERSION = 'engine_v4 (sin polvo, FLOOR=1e-3, RTOL=1e-6)'


def suelo(g):
    """relleno por debajo del suelo = 0."""
    g = float(g); return g if g >= FLOOR else 0.0


def es_fill(q):
    """criterio unico de 'hay relleno' (en vez de q > 1e-9)."""
    return float(q) >= FLOOR


def assert_sin_polvo(q, ctx=''):
    q = float(q)
    assert q == 0.0 or q >= FLOOR, f'polvo: 0 < q={q!r} < {FLOOR} {ctx}'
    return q


def relleno(s, ahead, rem=INF):
    """Un print de s acciones en el nivel L con `ahead` acciones de cola por delante y `rem` acciones aun por llenar.
    -> (ahead_nuevo, g): g = relleno bruto (0 o >= FLOOR, acotado por rem); ahead_nuevo en float64."""
    s = float(s); ahead = float(ahead); tol = max(FLOOR, RTOL * s)
    rest = ahead - s
    if rest > tol: return rest, 0.0                   # cola no agotada (INF - s = INF tambien)
    ex = -rest                                        # s - ahead (puede ser ~0 o negativo-polvo: cola agotada exacta)
    return 0.0, (suelo(min(float(rem), ex)) if ex > tol else 0.0)


def fill_segment_v4(book_arr, xa, qupd, prints, L, t_arr, t_end, rem, variant, dedupe=True, row_win=100, tol_s=0.015, diag=None):
    if book_arr is None: return 0.0, None, 'sin_libro'
    bid, ask, bsz, _ = book_arr
    if not (ask > L + EPS): return 0.0, None, 'seria_taker'
    bsz = float(bsz); xa = float(xa)
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
    first_before = set(); pair_t = {}
    if dedupe and rows and pr:
        grp = {}
        for i, (t, q, s) in enumerate(pr):
            if abs(q - L) <= TOLP: grp.setdefault(t, []).append(i)
        used = set()
        for t, idxs in sorted(grp.items()):
            S = sum(pr[i][2] for i in idxs); best = None
            for r, (tr, v, vp) in enumerate(rows):
                if r in used or not np.isfinite(vp): continue
                if t - row_win <= tr <= t and abs((vp - v) - S) <= tol_s: best = r if best is None or tr > rows[best][0] else best
            if best is not None:
                used.add(best)
                for i in idxs: first_before.add(i); pair_t[i] = rows[best][0]
    evs = []
    for (t, v, vp) in rows: evs.append((t, 1, 0, v))
    for i, (t, q, s) in enumerate(pr):
        if i in first_before: evs.append((pair_t[i], 0, 1, (q, s, t)))
        else: evs.append((t, 2, 1, (q, s, t)))
    evs.sort(key=lambda e: (e[0], e[1]))
    if variant == 'BASE' and top: ahead = min(ahead, bsz)
    qty = 0.0; tf = None
    for (t, _o, kind, v) in evs:
        if kind == 0:
            ahead = min(ahead, v); continue
        q, s, t = v
        if q < L - TOLP:                                              # barrido: relleno completo de lo que falta
            g = suelo(rem - qty)
            if g > 0.0: qty += g; tf = t if tf is None else tf
            break
        if abs(q - L) <= TOLP:
            ahead, g = relleno(s, ahead, rem - qty)
            if g > 0.0:
                qty += g; tf = t if tf is None else tf
                if qty >= rem - FLOOR: break
    assert_sin_polvo(qty, f'L={L} t_arr={t_arr}')
    if diag is not None: diag['paired'] = diag.get('paired', 0) + len(first_before)
    return qty, tf, 'ok'


class DayEngV4(E3.DayEngV3):
    """DayEngV3 con fill_segment_v4 (sin polvo). Mismo constructor."""
    def run_segment(self, k, L, t_arr, t_end, rem, variant):
        return fill_segment_v4(self.D.book(k, t_arr), self.xa(k, L, t_arr) if variant == 'CONS' else 0.0, self.qupd3(k, L, t_arr, t_end) if variant == 'BASE' else None,
                               self.tape.get(k, L, t_arr, t_end), L, t_arr, t_end, rem, variant, dedupe=self.dedupe, diag=self.diag)
