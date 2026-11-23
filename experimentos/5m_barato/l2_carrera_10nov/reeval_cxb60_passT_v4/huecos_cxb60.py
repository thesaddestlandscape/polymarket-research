#!/usr/bin/env python3
"""huecos_cxb60.py -- ESPEC E8(b): detector de huecos de la reeval CXB60 a nivel de FICHERO maker_ms (recepcion por moneda), en lugar de `hueco_feed` del runner (degenerado: 100 % true, vac_max 50-59 s; DICTAMEN 4).
vac_max_mercado = mayor intervalo SIN filas de la moneda (rx) dentro de la ventana del mercado [fin-pre, fin] incluidos los bordes; sin filas en la ventana => pre (toda la ventana ciega, fail-closed).
La sensibilidad EXCLUYE los mercados con vac_max >= 5 s. Funciones puras; la lectura de maker_ms (zcat) y el test de aceptacion en datos reales (vac_max p50 de ~55 s a <10 s en 13-17 Nov, no ciegos) estan PENDIENTES. 0 ordenes, 0 red."""
import numpy as np
UMBRAL_S = 5.0

def vac_max_mercado(rx_ms, fin_s, pre_s=300):
    lo, hi = (fin_s - pre_s) * 1000, fin_s * 1000
    if rx_ms is None or len(rx_ms) == 0: return float(pre_s)
    t = np.asarray(rx_ms, np.int64); t = t[(t >= lo) & (t <= hi)]
    if len(t) == 0: return float(pre_s)
    p = np.concatenate([[lo], np.sort(t), [hi]]); return float(np.max(np.diff(p)) / 1000.0)

def excluye_mercados(vac_por_mercado, umbral_s=UMBRAL_S):
    """{mercado: vac_max_s} -> conjunto de mercados a excluir en la sensibilidad (vac_max >= umbral). Valor ausente/NaN => excluido (nunca imputado)."""
    return {m for m, v in vac_por_mercado.items() if v is None or not np.isfinite(v) or v >= umbral_s}
