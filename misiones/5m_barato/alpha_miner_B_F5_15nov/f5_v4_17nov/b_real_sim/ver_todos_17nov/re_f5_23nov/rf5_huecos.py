#!/usr/bin/env python3
"""rf5_huecos.py -- ESPEC E5: sensibilidad FAIL-CLOSED por huecos de stream. Huecos reales de recepcion >= 5 s por moneda (maker_ms / filas q de la moneda, y ticks Binance); las ordenes cuya vida solapa un hueco se EXCLUYEN en la sensibilidad
(se publica EV con y sin ellas); si la exclusion cambia el signo en >=2 de 3 monedas => FRAGIL_HUECOS (no CONFIRMADA). Dato ausente = excluir, nunca imputar. Funciones puras. 0 ordenes, 0 red."""
import numpy as np, pandas as pd
UMBRAL_MS = 5000

def huecos(rx, umbral_ms=UMBRAL_MS):
    """rx: instantes de recepcion (ms) de TODAS las filas de la moneda (cualquier orden). Devuelve [(t_prev, t_next)] con t_next - t_prev >= umbral (intervalo SIN datos). Vacio/None => None (sin datos: no se puede afirmar 'sin hueco')."""
    if rx is None or len(rx) == 0: return None
    t = np.unique(np.asarray(rx, np.int64)); d = np.diff(t); i = np.where(d >= umbral_ms)[0]; return [(int(t[k]), int(t[k + 1])) for k in i]

def solapa(t0, t1, gaps):
    """True si [t0, t1] solapa algun hueco; gaps None (moneda sin datos) => True (fail-closed: excluir)."""
    if gaps is None: return True
    return any(a < t1 and b > t0 for a, b in gaps)

def marca_huecos(R, gaps_por_moneda, fin_ms_col='fin'):
    """R: ordenes (cols coin, t_dec, fin[s]). Vida conservadora = [t_dec, fin*1000] (la orden vive hasta el fin del mercado como maximo). Devuelve serie bool 'hueco' (True = excluir en la sensibilidad)."""
    return pd.Series([solapa(int(td), int(fn) * 1000, gaps_por_moneda.get(str(c).lower())) if pd.notna(td) and pd.notna(fn) else True for c, td, fn in zip(R.coin, R.t_dec, R[fin_ms_col])], index=R.index)

def mercados_excluidos(R, pol='base', bloq=0):
    """conjunto (dia, mid) con ALGUNA orden de la base en hueco: el mercado entero se excluye de todas las politicas (pareado)."""
    X = R[(R.pol == pol) & (R.bloq == bloq)]
    if 'hueco' not in X.columns: return None
    return set(zip(X.dia[X.hueco.fillna(True).astype(bool)], X.mid[X.hueco.fillna(True).astype(bool)]))

def excluye(R, excl):
    """R sin las filas de mercados excluidos (excl None => ValueError: no se puede hacer la sensibilidad sin la marca de huecos, fail-closed)."""
    if excl is None: raise ValueError('sin columna hueco: sensibilidad imposible (fail-closed)')
    k = list(zip(R.dia, R.mid)); m = np.array([x in excl for x in k]); return R[~m]

def veredicto_fragil(valor_con, valor_sin, monedas=('eth', 'sol', 'xrp')):
    """valor_con/valor_sin: {coin: estadistico (Delta o EV)}. FRAGIL_HUECOS si el signo cambia (o falta el dato sin huecos) en >=2 de 3 monedas. Falta de dato en la sensibilidad cuenta como cambio de signo (fail-closed)."""
    cambios = 0; det = {}
    for c in monedas:
        a, b = valor_con.get(c), valor_sin.get(c); ch = (a is None or b is None or not np.isfinite(a) or not np.isfinite(b) or (a > 0) != (b > 0)); det[c] = dict(con=a, sin=b, cambia_signo=bool(ch)); cambios += int(ch)
    return dict(estado=('FRAGIL_HUECOS' if cambios >= 2 else 'OK_HUECOS'), cambios=cambios, por_moneda=det)

def gaps_de_motor(E, umbral_ms=UMBRAL_MS):
    """huecos por moneda (minuscula) a partir de las filas q (RX) de todos los tokens 5m de la moneda en el motor del dia (E.K.qt/qb por token k, E.D.act = moneda). None por moneda sin filas."""
    por = {}
    for k in E.ks:
        a, b = int(E.K.qb[k]), int(E.K.qb[k + 1]); por.setdefault(str(E.D.act[k]).lower(), []).append(np.asarray(E.K.qt[a:b], np.int64))
    return {c: huecos(np.concatenate(v), umbral_ms) for c, v in por.items()}

def gaps_binance(bsrc, umbral_ms=UMBRAL_MS):
    return {c: huecos(t, umbral_ms) for c, (t, p) in bsrc.items()}
