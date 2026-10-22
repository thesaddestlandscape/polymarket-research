"""h61b_regla.py -- H61b H23-CANCEL-BIN500-X05: regla CONGELADA (21-Oct 12:07Z, H61b_CONGELADA.json, sha256[:16]=238cffd0e77f0142). Pura: sin red, sin disco de produccion.
Cambiar CUALQUIER constante = hipotesis nueva (preregistrar aparte), nunca un retoque de esta. La senal es EXACTAMENTE la de ../h61/h61_sim.py::retW (celda elegida W=500 ms, X=0,5 bps):
  ret(t) = p(ultimo aggTrade con rx<=t) / p(ultimo aggTrade con rx<=t-500) - 1, en bps, orientado al lado s (Up: +ret; Down: -ret), hora de RECEPCION.
  Sin dato en la ventana, o ultimo trade con antiguedad > 5 s  ->  NaN -> la defensa NO dispara (se sigue pujando).
  Defensa: ret < -0,5 bps -> cancelar / no pujar; cuando deja de cumplirse se re-puja con el retardo de v3 (150 ms). El relleno se evita si la decision es >= 60 ms (cancelacion)
  antes del print: eso lo aplica el simulador (lat_cancel_ms = 60), no la senal.
"""
import hashlib
from pathlib import Path
import numpy as np

CONGELADA = Path(__file__).resolve().parent.parent / "H61b_CONGELADA.json"
SHA_CONGELADA = "238cffd0e77f0142"
W_MS, X_BPS, MAX_ANTIG_MS, REPUJA_MS = 500, 0.5, 5000, 150
DATOS_VALIDOS_DESDE = "2026-10-22"          # JSON: relleno posterior a la congelacion (>= 2026-10-22)
GATE = dict(retencion_min=0.60, n_cierres_C_min=15, h23=dict(n=40, dias=10, ev_pond_min=0.10, sin2_min=0.0), kill=dict(n=20, ev_pond_sin2_max=-0.15))
CODIGO_SHA = None


def verificar_congelada():
    """Falla ruidosamente si el JSON congelado no es el que se firmo (fail-closed)."""
    sha = hashlib.sha256(CONGELADA.read_bytes()).hexdigest()[:16]
    if sha != SHA_CONGELADA:
        raise RuntimeError(f"H61b_CONGELADA.json cambiado: {sha} != {SHA_CONGELADA}")
    return sha


def ret_bps(rx, p, t, lado, W=W_MS, max_antig=MAX_ANTIG_MS):
    """Retorno (bps) del aggTrade en la ventana W hasta t (hora de recepcion), orientado al lado s. rx ordenado, int64 ms. NaN si no hay dato / viejo."""
    t = np.asarray(t, dtype=np.int64)
    out = np.full(len(t), np.nan)
    if rx is None or len(rx) == 0:
        return out
    i1 = np.searchsorted(rx, t, "right") - 1
    i0 = np.searchsorted(rx, t - W, "right") - 1
    ok = (i0 >= 0) & (i1 >= 0) & (rx[np.maximum(i1, 0)] >= t - max_antig)
    out[ok] = (p[i1[ok]] / p[i0[ok]] - 1.0) * 1e4
    return out if lado == "Up" else -out


def permitido(rx, p, t, lado, X=X_BPS):
    """True = se puede pujar. NaN -> True (la defensa no dispara sin dato)."""
    return ~(ret_bps(rx, p, t, lado) < -X)


def hash_codigo():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:16]
