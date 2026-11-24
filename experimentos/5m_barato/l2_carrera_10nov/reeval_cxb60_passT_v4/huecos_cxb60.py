#!/usr/bin/env python3
"""huecos_cxb60.py -- ESPEC E8(b): detector de huecos de la reeval CXB60 a nivel de FICHERO maker_ms (recepcion por moneda), en lugar de `hueco_feed` del runner (degenerado: 100 % true, vac_max 50-59 s; DICTAMEN 4).
DECLARACION (v3, 24-Nov): (1) FEED DE LA MONEDA = filas `q` (cambio de mejor nivel) y `t` (trade) de CUALQUIER token (YES/NO, 5m/15m) que las filas `k` del propio fichero asignan a la moneda; NO cuentan h/l/L (snapshots/niveles sin columna de recepcion), ni las filas Binance. (2) RELOJ = RECEPCION: columna c[7] (campo 8) en `q`, recv (campo 7) en `t`;
nunca el t_ms de exchange. (3) UNA SOLA VENTANA: PRE_S = 332 s (= VENT_PRE_S del runner: 300 s de mercado + 32 s de calentamiento vol30/b300) en las dos medidas (continua en ms `vac_max_mercado` y por segundos `vac_max_seg`); el 300 anterior queda retirado.
vac_max_mercado = mayor intervalo SIN filas de la moneda (rx) dentro de la ventana del mercado [fin-PRE_S, fin] incluidos los bordes; sin filas en la ventana => PRE_S (toda la ventana ciega, fail-closed).
La sensibilidad EXCLUYE los mercados con vac_max >= 5 s. Funciones puras; el lector real (huecos_real.py) y su aceptacion en 13-17 Nov (no ciegos) estan en huecos_real_*.json. 0 ordenes, 0 red."""
import numpy as np
UMBRAL_S = 5.0; PRE_S = 332; FILAS_FEED = ("q", "t")

def vac_max_mercado(rx_ms, fin_s, pre_s=PRE_S):
    lo, hi = (fin_s - pre_s) * 1000, fin_s * 1000
    if rx_ms is None or len(rx_ms) == 0: return float(pre_s)
    t = np.asarray(rx_ms, np.int64); t = t[(t >= lo) & (t <= hi)]
    if len(t) == 0: return float(pre_s)
    p = np.concatenate([[lo], np.sort(t), [hi]]); return float(np.max(np.diff(p)) / 1000.0)

def excluye_mercados(vac_por_mercado, umbral_s=UMBRAL_S):
    """{mercado: vac_max_s} -> conjunto de mercados a excluir en la sensibilidad (vac_max >= umbral). Valor ausente/NaN => excluido (nunca imputado)."""
    return {m for m, v in vac_por_mercado.items() if v is None or not np.isfinite(v) or v >= umbral_s}

def vac_max_seg(secs, fin_s, pre_s=PRE_S):
    """mayor racha de SEGUNDOS consecutivos sin ningun mensaje de la moneda en [fin-pre, fin] (misma medida que calidad_feed del runner, pero con los segundos de TODO el fichero maker_ms de la moneda). secs: set/array de segundos enteros con mensajes."""
    S = set(int(x) for x in secs) if not isinstance(secs, set) else secs; run = best = 0
    for s in range(fin_s - pre_s, fin_s + 1):
        if s in S: run = 0
        else: run += 1; best = max(best, run)
    return best
