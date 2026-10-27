"""v2lib.py: carga de prints/libro de los mercados de B (mk_D.csv.gz) y regla de consumo/relleno. Solo lectura."""
import gzip, csv, collections, numpy as np
DL = '/root/polymarket-research-datalogs/calibracion_etiqueta/'
def cargar_dia(dia):
    """-> trades: dict tk -> arrays ordenados por recepcion (t_ms, price, side(1=BUY,0=SELL), size, dup); comp: tk->token complementario; mk: tk->market id"""
    mk = {}; byk = collections.defaultdict(dict); T = collections.defaultdict(list); Q = collections.defaultdict(list)
    with gzip.open(DL + 'v2/mk_%s.csv.gz' % dia, 'rt', errors='replace') as f:
        for line in f:
            c = line.rstrip('\n').split(',')
            if c[0] == 'k': mk[c[2]] = c[5]; byk[c[5]][c[7]] = c[2]
            elif c[0] == 't':
                try: T[c[2]].append((int(c[6]), float(c[3]), 1 if c[4] == 'BUY' else 0, float(c[5]), int(c[1])))
                except ValueError: pass
            elif c[0] == 'q':
                try: Q[c[2]].append((int(c[7]), float(c[3]), float(c[4]), float(c[5]), float(c[6])))
                except ValueError: pass
    comp = {}
    for m, d in byk.items():
        if 'YES' in d and 'NO' in d: comp[d['YES']] = d['NO']; comp[d['NO']] = d['YES']
    tr = {}; q = {}
    for tk, L in T.items():
        a = np.array(L, dtype=float); a = a[np.argsort(a[:, 0], kind='stable')]; tr[tk] = a
    for tk, L in Q.items():
        a = np.array(L, dtype=float); q[tk] = a[np.argsort(a[:, 0], kind='stable')]
    return tr, q, comp, mk
def dedup_marcado(tr, comp):
    """marca (col 5) prints duplicados: mismo casado visto en el token y su complementario (<=300 ms, mismo tamano, precios que suman 1). Regla de vpv_f8/calib_core: se descarta el SEGUNDO (por recepcion) del par."""
    out = {}
    tks = list(tr.keys())
    for tk in tks:
        a = tr[tk]; dup = np.zeros(len(a), bool); o = comp.get(tk)
        if o is not None and o in tr and tk > o:   # solo un lado hace de 'segundo'; el orden real lo da la recepcion, ver abajo
            pass
        out[tk] = dup
    # orden real: para cada print de tk buscar en comp un print previo (recepcion anterior o igual) con mismo tamano y p+p'=1 dentro de 300 ms
    for tk in tks:
        o = comp.get(tk)
        if o is None or o not in tr: continue
        a = tr[tk]; b = tr[o]; tb = b[:, 0]
        for i in range(len(a)):
            t = a[i, 0]; lo = np.searchsorted(tb, t - 300, 'left'); hi = np.searchsorted(tb, t, 'right' if tk > o else 'left')
            for j in range(lo, hi):
                if abs(b[j, 3] - a[i, 3]) < 5e-5 and abs(b[j, 1] + a[i, 1] - 1) < 1e-9: out[tk][i] = True; break
    return out

class Dia:
    def __init__(s, dia):
        s.tr, s.q, s.comp, s.mk = cargar_dia(dia); s.dup = dedup_marcado(s.tr, s.comp)
    def consumos(s, tk, p, t0, t1):
        """prints que consumen una compra a precio p del token tk con recepcion en [t0,t1] ms: array (t, size, barrido) ordenado"""
        res = []
        a = s.tr.get(tk)
        if a is not None:
            lo, hi = np.searchsorted(a[:, 0], [t0, t1 + 1e-9]); m = (a[lo:hi, 2] == 0) & (a[lo:hi, 1] <= p + 1e-9) & (~s.dup[tk][lo:hi])
            for r in a[lo:hi][m]: res.append((r[0], r[3], r[1] < p - 1e-9))
        o = s.comp.get(tk); b = s.tr.get(o) if o else None
        if b is not None:
            lo, hi = np.searchsorted(b[:, 0], [t0, t1 + 1e-9]); m = (b[lo:hi, 2] == 1) & (b[lo:hi, 1] >= 1 - p - 1e-9) & (~s.dup[o][lo:hi])
            for r in b[lo:hi][m]: res.append((r[0], r[3], r[1] > 1 - p + 1e-9))
        res.sort(); return res

import math
def bid_at(D, tk, t, stale=30000):
    a = D.q.get(tk)
    if a is None: return None
    i = np.searchsorted(a[:, 0], t, 'right') - 1
    if i < 0 or t - a[i, 0] > stale or a[i, 1] >= a[i, 2]: return None
    return a[i, 1], a[i, 3]
def lleno(cons, ti, tf, e, f, g, s, Q):
    """cons: lista (t,sz,sweep). rellena si consumo acumulado en [ti, tf+e] >= g*s + f*Q -> devuelve instante o None"""
    acc = 0.0; thr = g * s + f * Q - 1e-9
    for t, sz, sw in cons:
        if t > tf + e: break
        if t >= ti:
            acc += sz
            if acc >= thr: return t
    return None
def wilson(k, n, z=1.96):
    if n == 0: return (float('nan'), float('nan'))
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)); return ((c - h) / d, (c + h) / d)
def auc(score, y):
    import pandas as pd
    y = np.asarray(y); s = np.asarray(score, float)
    if y.sum() == 0 or y.sum() == len(y): return float('nan')
    r = pd.Series(s).rank().values; n1 = y.sum(); n0 = len(y) - n1; return float((r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))
