#!/usr/bin/env python3
"""gate_dias_independientes.py -- criterio de robustez por DIAS INDEPENDIENTES
(21-Sep, aprobado por Javi).

Problema: los gates cuentan FILAS, pero las filas de un mismo dia/regimen no
son independientes. Verificado el 21-Sep: SNIPER#BTC#15min[0.10,0.15) (sin los
2 mejores dias: -0,047 EUR/tr), DISPERSO#DOGE#15min[0.15,0.20) (6 de 21 dias
positivos), `?#BTC#5min[0.21,0.26)` (3 wallets, 62% una) pasaban `bueno_
confirmado` con n=53-160 y no aguantan quitar 2-3 dias. WALLET_MIRROR SEGUIR#
ETH#15min#1 fino SI (sin 3 mejores dias +0,114).

Criterio (solo DEGRADA, nunca promueve): un bucket es robusto si tras quitar los
K mejores dias el pnl medio sigue >= PISO_EUR y hay al menos MIN_DIAS dias.
Mismas unidades que los gates (retorno por 1 EUR de stake, ya neto de fee)."""
from collections import defaultdict

ENFORCE = True   # False = solo calcula y publica los campos, sin degradar
K_MEJORES_DIAS = 2
PISO_EUR = 0.10          # = UMBRAL_ABSOLUTO_EUR del resto de gates (12-Sep)
MIN_DIAS = 2 * K_MEJORES_DIAS + 3   # 7: con menos, "quitar los mejores" no deja muestra util


def robustez_dias(filas, k=K_MEJORES_DIAS, piso=PISO_EUR, min_dias=MIN_DIAS) -> dict:
    """filas: iterable de (ts, pnl) -- ts = cadena/fecha ISO (se usan los 10
    primeros caracteres como dia). Devuelve {"robusto": bool, "n_dias": int,
    "pnl_sin_mejores": float|None, "n_sin_mejores": int, "dias_positivos": int}.
    Fail-closed: sin datos o con pocos dias -> robusto=False."""
    por_dia = defaultdict(list)
    for ts, pnl in filas:
        por_dia[str(ts)[:10]].append(float(pnl))
    n_dias = len(por_dia)
    res = {"robusto": False, "n_dias": n_dias, "pnl_sin_mejores": None, "n_sin_mejores": 0,
           "dias_positivos": sum(1 for v in por_dia.values() if sum(v) > 0)}
    if n_dias < min_dias:
        return res
    orden = sorted(por_dia, key=lambda d: sum(por_dia[d]), reverse=True)
    excl = set(orden[:k])
    resto = [p for d, v in por_dia.items() if d not in excl for p in v]
    if not resto:
        return res
    m = sum(resto) / len(resto)
    res.update({"pnl_sin_mejores": round(m, 4), "n_sin_mejores": len(resto), "robusto": m >= piso})
    return res
