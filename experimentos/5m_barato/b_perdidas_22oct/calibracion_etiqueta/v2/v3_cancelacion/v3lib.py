"""v3lib.py: replay MECANICO de la regla de cancelacion/repegado de B (experimento_maker_h47.py, H35 DEEP_PEG) sobre el libro q
grabado (recepcion) + carrera de latencia. Reutiliza v2lib (Dia, consumos, lleno). Solo lectura."""
import sys, numpy as np
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/calibracion_etiqueta/v2')
from v2lib import Dia, lleno, wilson, auc, DL  # noqa
K = {'eth': 2, 'sol': 1, 'xrp': 1}
T_STOP = 60.0

def obj_vec(bid, ask, k):
    """objetivo_h35 + en_banda vectorizado (milesimas). NaN = sin objetivo (fuera de banda / libro invalido / cruzado)."""
    b = np.round(bid * 1000).astype(np.int64); a = np.round(ask * 1000).astype(np.int64)
    rej = (b % 10 == 0)
    o = np.where(rej, b - k * 10, (b // 10 - (k - 1)) * 10)
    ok = rej & (a > 0) & (b < a) & (b > 110) & (b <= 300) & (o >= 100) & (o <= 300) & (o < b) & (o < a)
    # nota: el codigo exige en_rejilla(bid) para 'valido'; fuera de rejilla -> no valido (cancel tras 2 s); aqui se trata como sin objetivo
    return np.where(ok, o / 1000.0, np.nan), (rej & (b < a))

class Libro:
    """serie del objetivo por token: t (ms recepcion), obj (precio o NaN), valido (bool)."""
    def __init__(s, D, tk, k):
        a = D.q.get(tk)
        if a is None: s.t = np.zeros(0); s.obj = np.zeros(0); s.val = np.zeros(0, bool); return
        s.t = a[:, 0]; s.obj, s.val = obj_vec(a[:, 1], a[:, 2], k)
    def idx_at(s, t):
        return np.searchsorted(s.t, t, 'right') - 1
    def obj_at(s, t):
        i = s.idx_at(t)
        return (np.nan, False) if i < 0 else (s.obj[i], s.val[i])
    def primer_cambio(s, t_desde, p, t_hasta):
        """primer instante (recepcion) > t_desde con objetivo != p (incluye NaN), o None. Libro invalido >=2 s cuenta tambien."""
        i0 = np.searchsorted(s.t, t_desde, 'right'); i1 = np.searchsorted(s.t, t_hasta, 'right')
        if i1 <= i0: return None
        o = s.obj[i0:i1]
        vv = s.val[i0:i1]
        dif = vv & ~(np.abs(o - p) < 1e-9)     # solo filas de libro VALIDO (bid en rejilla y < ask); NaN valido = fuera de banda -> cambio
        j = np.argmax(dif) if dif.any() else -1
        return None if j < 0 else float(s.t[i0 + j])
    def primer_valido(s, t_desde, t_hasta):
        """primer instante >= t_desde con objetivo valido (precio), o (None, None)."""
        i0 = max(np.searchsorted(s.t, t_desde, 'right') - 1, 0); i1 = np.searchsorted(s.t, t_hasta, 'right')
        if i1 <= i0: return None, None
        o = s.obj[i0:i1]; ok = ~np.isnan(o)
        if not ok.any(): return None, None
        j = int(np.argmax(ok)); return max(float(s.t[i0 + j]), t_desde), float(o[j])

def simular_puja(D, L, tk, t_dec0, cie_ms, lat, E, F, G, shift=0, size=5.0, max_ord=400):
    """Replay de la maquina de estados de B para una puja desde la decision t_dec0 (ms). lat: dict con funciones/valores
    react (ms libro->intencion de cancelar), post_half (ms decision->t_ini), asentar (ms intencion_cancel->siguiente decision).
    Relleno: regla de consumo de la Capa 1 (e=E holgura, g, f) en [t_ini, t_cancel+30ms]. Devuelve dict."""
    t_stop_ms = cie_ms - T_STOP * 1000; ordenes = []; td = t_dec0; fill_t = None
    while td < t_stop_ms - 2000 and len(ordenes) < max_ord:
        p, v = L.obj_at(td)
        if np.isnan(p):
            tv, p = L.primer_valido(td, t_stop_ms - 2000)
            if tv is None: break
            td = tv + lat['react']()
            if td >= t_stop_ms - 2000: break
            p2, _ = L.obj_at(td)
            if np.isnan(p2): continue
            p = p2
        ti = td + lat['post_half']()
        tch = L.primer_cambio(td, p, t_stop_ms)
        tc = min(tch + lat['react']() if tch is not None else t_stop_ms, t_stop_ms)
        tc = max(tc, ti)
        tf = tc + 30.0
        cons = [(t - shift, sz, sw) for (t, sz, sw) in D.consumos(tk, p, ti + shift, tf + E + shift)]
        lt = lleno(cons, ti, tf, E, F, G, size, 0.0)
        ordenes.append((td, ti, tc, p, lt))
        if lt is not None: fill_t = lt; break
        td = tc + lat['asentar']()
    return dict(n_ord=len(ordenes), fill=fill_t is not None, fill_t=fill_t, ordenes=ordenes)
