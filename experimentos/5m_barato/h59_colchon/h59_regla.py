"""h59_regla.py -- DECISION PURA (sin E/S, sin red, sin firma) de H59: V4 como TOMADOR con colchon de precio.

UNICO sitio donde vive la regla: el vigia forward (`vigia_5m_barato_h59_forward.py`) y el brazo sombra de F2 (parche en
`f2_h59.patch`) IMPORTAN estas funciones; no se copian. Cambiar cualquier constante = nueva VERSION y nuevo OOS.

La SENAL es la de V4 congelada (vigia_5m_barato_forward.py, hash_config 77a75859ae5cf22e): se importa su `margen`, `p_limite`
y CONFIG (no se replica la formula). Unica diferencia con V4: el limite de la FOK es p_limite(bid15(t0)) + K y la llegada se
valida contra el TAMANO real del nivel 1 (FOK = todo o nada).

  senal(t)   : margen_neto(redondeado a 4 decimales, como V4) >= 0,05 con libro no cruzado en ambas patas, t en la ventana de V4
  limite     : round(p_limite(bid15(t0)) + K, 2), tope 0,99.  K = 0,02 (principal); 0, 0,01, 0,03, 0,05 solo descriptivos.
  acciones   : max(5, ceil(2 / limite * 100) / 100)   (= `tam_orden` de F2: la orden prefirmada real)
  llegada    : t0 + 215 ms; estado del libro = ultima fila q con recepcion <= t0 + 215 ms (nunca posterior)
  relleno    : ask_llegada <= limite + 1e-9 Y tamano_ask_llegada >= acciones  (nivel 1, FOK todo-o-nada; sin niveles 2-3: conservador)
  precio     : ask_llegada (no el limite).  PnL = acc * (pago - precio - fee(precio)); coste = acc * (precio + fee(precio)).
"""
import math
import sys
from pathlib import Path

import numpy as np

REPO = next(p for p in Path(__file__).resolve().parents if (p / "vigia_5m_barato_forward.py").exists())   # raiz del repo (tambien si se copia a la raiz)
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))
import vigia_5m_barato_forward as V4  # noqa: E402  (solo se IMPORTA; no se edita ni se ejecuta nada)

VERSION = 1
K_PRINCIPAL = 0.02
K_COLCHONES = (0.0, 0.01, 0.02, 0.03, 0.05)     # los 5 probados en descubrimiento; solo K_PRINCIPAL cuenta para el gate
LAT_TOMADOR_MS = V4.CONFIG["latencia_oficial_ms"]            # 215
UMBRAL = V4.CONFIG["umbral_margen_neto"]                     # 0,05
MIN_ACCIONES = V4.CONFIG["min_acciones"]                     # 5
STAKE_EUR = V4.CONFIG["stake_eur"]                           # 2
REF_CONOCIBLE_MS = V4.CONFIG["ref_conocible_ms"]             # 1500
FIN_MARGEN_S = V4.CONFIG["fin_margen_s"]                     # 10
GAP_MIN_BPS = V4.CONFIG["gap_min_bps"]                       # 1
MAX_EDAD_LIBRO_MS = 60_000                                    # como V4: libro de llegada mas viejo -> UNKNOWN


def fee(p):
    return V4.fee(p)


def senal_v4(ask5, bid15, bid5, ask15):
    """Disparo V4 en cada instante (arrays o escalares). Identico a `vigia_5m_barato_forward.procesar`:
    V4.margen (redondeado a 4 decimales) >= umbral, ambos datos presentes, y NO libro cruzado (bid > ask) en ninguna pata.
    Las comparaciones con NaN son False (= dato ausente de V4, que usa None)."""
    a5, b15 = np.atleast_1d(np.asarray(ask5, float)), np.atleast_1d(np.asarray(bid15, float))
    a15, b5 = np.atleast_1d(np.asarray(ask15, float)), np.atleast_1d(np.asarray(bid5, float))
    out = np.zeros(a5.shape, dtype=bool)
    with np.errstate(invalid="ignore"):
        m = b15 - a5 - V4.CONFIG["fee_tomador"] * a5 * (1 - a5)
        cand = m >= UMBRAL - 5e-5                      # el redondeo a 4 decimales solo mueve el margen < 5e-5
        cruz = (b15 > a15) | (b5 > a5)
    for i in np.flatnonzero(cand & ~np.isnan(m)):
        out[i] = V4.margen(float(b15[i]), float(a5[i])) >= UMBRAL
    return out & ~cruz


def limite_fok(bid15_t0, k):
    """Limite de la FOK = p_limite de V4 + colchon k (rejilla de 1 c, tope 0,99). None si V4 no tiene limite."""
    pl = V4.p_limite(float(bid15_t0))
    if pl is None:
        return None
    return min(0.99, round(pl + k, 2))


def acciones_objetivo(limite):
    """Tamano de la orden FOK: igual que `tam_orden` de F2 (max(5, ceil(2/p*100)/100))."""
    return max(MIN_ACCIONES, math.ceil(STAKE_EUR / limite * 100) / 100)


def llegada(ask_llegada, asz_llegada, limite, acc_obj):
    """Resultado de la FOK al llegar. -> (clase, acciones, precio). Clases: llena | repreciado | corte_tamano | sin_libro.
    corte_tamano = el precio cabe en el limite pero el nivel 1 no tiene `acc_obj` acciones: la FOK muere (no hay parciales)."""
    if limite is None or ask_llegada is None or ask_llegada != ask_llegada:
        return "sin_libro", 0.0, None
    if ask_llegada > limite + 1e-9:
        return "repreciado", 0.0, None
    if asz_llegada is None or asz_llegada != asz_llegada or asz_llegada < acc_obj - 1e-9:
        return "corte_tamano", 0.0, None
    return "llena", float(acc_obj), float(ask_llegada)


def pnl(acc, precio, gana):
    """(pnl, coste). gana None -> (None, coste): desenlace ausente es PENDIENTE, nunca 0."""
    if acc <= 0 or precio is None:
        return 0.0, 0.0
    coste = acc * (precio + fee(precio))
    return (None if gana is None else acc * (float(gana) - precio - fee(precio))), coste


def evaluar_evento(ask0, bid15_t0, ask_llegada, asz_llegada, edad_llegada_ms, ks=K_COLCHONES):
    """Una entrada V4 (primera senal del cierre) -> dict por colchon k. Pura: no mira nada posterior a la llegada."""
    out = {}
    for k in ks:
        lim = limite_fok(bid15_t0, k)
        if lim is None:
            out[k] = dict(lim=None, acc_obj=0.0, clase="sin_libro", acc=0.0, precio=None)
            continue
        acc_obj = acciones_objetivo(lim)
        if edad_llegada_ms is None or edad_llegada_ms > MAX_EDAD_LIBRO_MS:
            out[k] = dict(lim=lim, acc_obj=acc_obj, clase="UNKNOWN", acc=0.0, precio=None)
            continue
        clase, acc, pr = llegada(ask_llegada, asz_llegada, lim, acc_obj)
        out[k] = dict(lim=lim, acc_obj=acc_obj, clase=clase, acc=acc, precio=pr)
    return out
