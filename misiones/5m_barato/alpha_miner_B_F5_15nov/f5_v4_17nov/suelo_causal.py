"""suelo_causal.py -- clasificador CAUSAL de la clase de suelo rx-ex (lo ~19 ms / hi ~39,5 ms) de las filas q del WS del libro. SPEC_F5_V4_17nov.md (sha en SPEC_F5_V4_17nov.sha256).
Dos fachadas con la MISMA logica (`clase_de_ventanas`): (1) `SueloCausalLive`: incremental, para el vigia en vivo: update(rx_ms, ex_ms) por cada fila q, clase(t_ms) solo con datos RX < bin(t).
(2) batch por dia: `tabla_clases(H, H_prev_tail, H_next_head)` sobre histogramas de 10 s. Solo stdlib + numpy. Sin I/O. Sin estado global.
Causalidad: clase(t) usa SOLO bins de 10 s COMPLETOS anteriores a t (rx < floor(t/10 s)*10 s <= t). Una fila con rx >= t nunca cambia clase(t)."""
import numpy as np
from collections import deque
BIN_MS = 10_000; NBINS_DIA = 8640; D_LO, D_HI = -50, 400; ND = D_HI - D_LO + 1      # 451 bins de 1 ms
W_HALF = 30; W_FULL = 60                                                         # bins de 10 s: 5 y 10 min
TOT_W, TOT_HALF = 200, 100
C_LO, C_HI, TOL = 19.25, 39.5, 5.0
def p5_de(h):
    """p5 de un histograma (ND,) de d = rx-ex; NaN si vacio. Identico a ADD2/ADD3: menor d con cum >= max(1, trunc(0,05*tot))."""
    tot = int(h.sum())
    if tot <= 0: return np.nan, 0
    cum = np.cumsum(h); k = max(1, int(0.05 * tot)); return float(np.argmax(cum >= k) + D_LO), tot
def clase_p5(p5, tot, minimo):
    """lo/hi/indet a partir de p5 y n filas (umbrales ADD2 sin tocar)."""
    if tot < minimo or not np.isfinite(p5): return 'indet'
    if abs(p5 - C_LO) <= TOL: return 'lo'
    if abs(p5 - C_HI) <= TOL: return 'hi'
    return 'indet'
def clase_de_ventanas(h1, h2):
    """h1 = bins B-60..B-31 sumados (ND,), h2 = bins B-30..B-1 sumados. -> (clase final, dict de diagnostico). Clases: lo|hi (puras), mixta, indet."""
    h = h1 + h2; p, t = p5_de(h); p1, t1 = p5_de(h1); p2, t2 = p5_de(h2)
    cW, c1, c2 = clase_p5(p, t, TOT_W), clase_p5(p1, t1, TOT_HALF), clase_p5(p2, t2, TOT_HALF)
    if cW == c1 == c2 and cW in ('lo', 'hi'): f = cW
    elif {c1, c2} == {'lo', 'hi'}: f = 'mixta'
    else: f = 'indet'
    return f, dict(p5=p, tot=t, p5_1=p1, tot_1=t1, p5_2=p2, tot_2=t2, cW=cW, c1=c1, c2=c2)
def clase_futura(h):
    """clase de futuro (solo VALIDACION, mira hacia delante): bins B..B+29 sumados, tot >= 100."""
    p, t = p5_de(h); return clase_p5(p, t, TOT_HALF)
class SueloCausalLive:
    """Incremental. update(rx_ms, ex_ms) por fila q (bid en [0,03;0,45], tokens 5min); clase(t_ms) -> 'lo'|'hi'|'mixta'|'indet'. Memoria: <= 61 bins x 451 int32. Las filas pueden llegar desordenadas (solo cuenta rx)."""
    def __init__(self): self.bins = {}                                           # bin -> np.int32[ND]
    def update(self, rx_ms, ex_ms):
        b = int(rx_ms) // BIN_MS; d = int(min(max(rx_ms - ex_ms, D_LO), D_HI)) - D_LO
        h = self.bins.get(b)
        if h is None: h = self.bins[b] = np.zeros(ND, np.int32)
        h[d] += 1
        lim = b - 2 * W_FULL                                                       # poda (con margen para filas tardias)
        if len(self.bins) > 4 * W_FULL: 
            for k in [k for k in self.bins if k < lim]: del self.bins[k]
    def _suma(self, a, b):
        s = np.zeros(ND, np.int64)
        for k in range(a, b + 1):
            h = self.bins.get(k)
            if h is not None: s += h
        return s
    def clase(self, t_ms, diag=False):
        B = int(t_ms) // BIN_MS; f, dg = clase_de_ventanas(self._suma(B - W_FULL, B - W_HALF - 1), self._suma(B - W_HALF, B - 1))
        return (f, dg) if diag else f
def acumulado(H):
    """H (nb, ND) int -> C (nb+1, ND) int32 con C[b] = suma de bins < b."""
    C = np.zeros((H.shape[0] + 1, H.shape[1]), np.int32); np.cumsum(H, axis=0, out=C[1:]); return C
def tabla_clases(H, prev=None, nxt=None):
    """Clase causal y futura para CADA bin B del dia. H (8640, ND); prev = ultimos 60 bins del dia anterior (o None -> ceros), nxt = primeros 30 bins del dia siguiente (o None -> ceros; clase futura 'indet' si faltan).
    -> dict de arrays (nb,): cls (object), cls_fut (object), p5, tot, p5_1, p5_2, tot_1, tot_2. t = B*10 s en adelante usa la fila B."""
    nb = H.shape[0]; P = np.zeros((W_FULL, ND), H.dtype) if prev is None else prev[-W_FULL:]; N = np.zeros((W_HALF, ND), H.dtype) if nxt is None else nxt[:W_HALF]
    C = acumulado(np.concatenate([P, H, N], axis=0)).astype(np.int64)
    cls = np.empty(nb, object); fut = np.empty(nb, object); out = {k: np.full(nb, np.nan) for k in ('p5', 'tot', 'p5_1', 'p5_2', 'tot_1', 'tot_2')}
    for B in range(nb):
        i = B + W_FULL                                                             # indice de B en la serie extendida
        h1 = C[i - W_HALF] - C[i - W_FULL]; h2 = C[i] - C[i - W_HALF]; cls[B], dg = clase_de_ventanas(h1, h2)
        fut[B] = clase_futura(C[i + W_HALF] - C[i]) if (nxt is not None or B + W_HALF <= nb) else 'indet'
        for k, kk in (('p5', 'p5'), ('tot', 'tot'), ('p5_1', 'p5_1'), ('p5_2', 'p5_2'), ('tot_1', 'tot_1'), ('tot_2', 'tot_2')): out[k][B] = dg[kk]
    out['cls'] = cls; out['cls_fut'] = fut; return out


# ======================================================================================================================================================
# DETECTOR RAPIDO lo/no-lo (17-Nov, peticion de Javi: el p5 de 10 min tarda ~5 min en ver lo->hi y eso implica perdidas). Causal, fail-closed.
# Idea: en lo (suelo ~19 ms) una fraccion apreciable de filas q llega con d = rx-ex < C (p. ej. 30 ms); en hi (suelo ~39,5 ms) casi ninguna. Se mira solo la ventana corta de los ULTIMOS W s COMPLETOS.
# estado = 'lo' solo si, en cada uno de los ultimos H segundos, la ventana de W s tiene >= nmin filas y la fraccion con d < C es >= rho. Cualquier otra cosa (poco trafico, hi, duda) -> 'nolo' = NO OPERAR.
# Subida (nolo->lo) exige H segundos consecutivos de evidencia; bajada (lo->nolo) es inmediata (1 segundo sin evidencia). Bandas de 2 ms (BANDAS): banda 0 = d<=9, b=1..25 -> [10+2(b-1), 11+2(b-1)], 26 = d>=60.
NBAND = 27
def banda_de(d):
    d = int(d); return 0 if d <= 9 else (NBAND - 1 if d >= 60 else (d - 10) // 2 + 1)
def nbandas_bajo(C):
    """numero de bandas (desde la 0) con d < C; C par en [10, 60]."""
    assert C % 2 == 0 and 10 <= C <= 60, C; return (C - 10) // 2 + 1
class ParamsDetector:
    def __init__(s, W=2, C=30, rho=0.05, nmin=20, H=2): s.W, s.C, s.rho, s.nmin, s.H = int(W), int(C), float(rho), int(nmin), int(H)
    def __repr__(s): return f'W{s.W}_C{s.C}_rho{s.rho:g}_n{s.nmin}_H{s.H}'
def lo_crudo(S, p, prev=None):
    """S (ns, NBAND) cuentas por segundo (ns segundos consecutivos); prev (>= W filas del tramo anterior) o None (= ceros -> nolo al inicio, fail-closed).
    -> bool (ns,): crudo[t] = evidencia de lo usando SOLO los segundos [t-W, t-1] (completos, anteriores a t)."""
    ns = S.shape[0]; P = np.zeros((p.W, NBAND), np.int64) if prev is None else np.asarray(prev, np.int64)[-p.W:]
    if P.shape[0] < p.W: P = np.vstack([np.zeros((p.W - P.shape[0], NBAND), np.int64), P])
    X = np.vstack([P, S.astype(np.int64)]); nl = nbandas_bajo(p.C)
    tot = np.cumsum(np.concatenate([[0], X.sum(1)])); low = np.cumsum(np.concatenate([[0], X[:, :nl].sum(1)]))
    t = np.arange(ns) + p.W; n = tot[t] - tot[t - p.W]; c = low[t] - low[t - p.W]            # fila i de X = segundo i-W; ventana = X[t-W : t) = segundos [i-W, i-1]
    return (n >= p.nmin) & (c >= p.rho * np.maximum(n, 1))
def estado_lo(crudo, p, prev_crudo=None):
    """H segundos consecutivos de evidencia (incluido el actual). prev_crudo: ultimos H-1 crudos del tramo anterior (o None -> False)."""
    pc = np.zeros(p.H - 1, bool) if prev_crudo is None else np.asarray(prev_crudo, bool)[-(p.H - 1):] if p.H > 1 else np.zeros(0, bool)
    if len(pc) < p.H - 1: pc = np.concatenate([np.zeros(p.H - 1 - len(pc), bool), pc])
    x = np.concatenate([pc, crudo]).astype(np.int64); c = np.cumsum(np.concatenate([[0], x]))
    return (c[np.arange(len(crudo)) + p.H] - c[np.arange(len(crudo))]) == p.H
class DetectorRapidoLive:
    """Incremental para el vigia en vivo: update(rx_ms, ex_ms) por fila q; estado(t_ms) -> 'lo' | 'nolo' (identico al batch sobre los mismos segundos). Solo cuenta filas con rx < segundo(t)*1000 (segundos completos)."""
    def __init__(s, p=None): s.p = p or ParamsDetector(); s.seg = {}
    def update(s, rx_ms, ex_ms):
        k = int(rx_ms) // 1000; a = s.seg.get(k)
        if a is None: a = s.seg[k] = np.zeros(NBAND, np.int64)
        a[banda_de(rx_ms - ex_ms)] += 1
        if len(s.seg) > 200: lim = k - 100; s.seg = {j: v for j, v in s.seg.items() if j >= lim}
    def _crudo(s, T):
        """crudo del segundo T (ventana [T-W, T-1])."""
        n = c = 0; nl = nbandas_bajo(s.p.C)
        for j in range(T - s.p.W, T):
            a = s.seg.get(j)
            if a is not None: n += int(a.sum()); c += int(a[:nl].sum())
        return n >= s.p.nmin and c >= s.p.rho * max(n, 1)
    def estado(s, t_ms):
        T = int(t_ms) // 1000; return 'lo' if all(s._crudo(T - i) for i in range(s.p.H)) else 'nolo'
