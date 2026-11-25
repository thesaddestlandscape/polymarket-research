#!/usr/bin/env python3
"""so_rem_a1.py (ADENDA_SO_A1c_19nov, ANULA A1/A1b): carga de tomador_202.pkl con la definicion ORIGINAL del resto: rem_sh = tk_rem * tk_sz (= rem_usdc / limite en compras; acciones AL LIMITE).
Verificado en calldata por el agente de datos (7 casos): en compras tsz = takerAmount (acciones al limite), limite = mA/tA, resto = (mA - takerFillAmount)/limite = tk_rem*tsz. NO hay categoria 'negativo'.
Fail-closed: tk_rem o tk_sz no finitos / tk_sz<=0 => rem_estado='sin_dato', rem_sh y tk_rem NaN (fuera de toda poblacion)."""
import hashlib, os, pickle
import numpy as np, pandas as pd
V = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/..')
PKL_SHA256 = '521e2da84b4ac54d81dc17f235a535b23c8fe3dbc9108ad77866d422b5af568b'
def rem_limite(mA, tA, tfill, side=0):
    """Resto desde la calldata (unidades 1e6). Compra (side 0): limite = mA/tA, rem_usdc = (mA-tfill)/1e6, rem_sh = rem_usdc/limite (acciones AL LIMITE; mejora de precio con fill completo => 0). Venta (side 1): rem_sh = (mA-tfill)/1e6 acciones, limite = tA/mA, rem_usdc NaN."""
    if side == 0:
        lim = mA / tA; ru = (mA - tfill) / 1e6; return lim, ru, ru / lim
    return tA / mA, float('nan'), (mA - tfill) / 1e6
def cargar_tomador(base=None, verificar_sha=True):
    base = base or (V + '/'); pk = base + 'tomador_202.pkl'
    if verificar_sha: assert hashlib.sha256(open(pk, 'rb').read()).hexdigest() == PKL_SHA256, 'tomador_202.pkl distinto del congelado'
    d = pickle.load(open(pk, 'rb')).copy(); r = d.tk_rem.astype(float).values; z = d.tk_sz.astype(float).values
    ok = np.isfinite(r) & np.isfinite(z) & (z > 0)
    d['tk_rem_old'] = r; d['rem_sh_old'] = r * z      # identicos a tk_rem/rem_sh (se conservan los nombres de v2)
    d['rem_estado'] = np.where(ok, 'ok', 'sin_dato'); d['rem_sh'] = np.where(ok, r * z, np.nan); d['tk_rem'] = np.where(ok, r, np.nan)
    return d
def resumen_rem(d):
    return {k: int(v) for k, v in d.rem_estado.value_counts().items()}
