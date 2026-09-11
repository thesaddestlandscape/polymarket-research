#!/usr/bin/env python3
"""
analisis_smart_exit_dependiente_tiempo_19ago.py — primer paso real hacia
Smart Exit como parada óptima (MDP), retomando
idea_mdp_optimal_stopping_smart_exit_13jul.py (13-Jul, nunca implementado
-- bloqueado por datos).

La versión ya calibrada (analisis_gate_riguroso_touch_vs_win_28jul.py)
prueba un UMBRAL FIJO de precio para vender anticipadamente. La hipótesis
de parada óptima dice que el umbral correcto depende del tiempo restante:
tocar un precio alto con MUCHO tiempo restante todavía tiene continuation
value (puede revertir); tocar el mismo precio con POCO tiempo restante ya
no (poco margen para que se mueva más). Si eso es cierto, la tasa de
"toca pero pierde" (el harvestable edge de un TP) debería ser MAYOR en
touches tempranos que en touches tardíos, para el mismo umbral de precio.

Este script NO hace value iteration/Bellman completo todavía -- eso exige
estimar transiciones de estado, que necesita mucho más n del que hay hoy
(BALLENAS_TARDIAS n=33 al 19-Ago, gate real=40, vigia_touch_vs_win_p18.py
lo vigila). Es el primer test empírico, más simple, que decide SI merece
la pena construir el aparato completo: ¿el harvestable edge de un TP
cambia con el tiempo restante, o es constante? Si es constante, un umbral
fijo ya captura todo lo que hay que capturar y el MDP no aporta nada
nuevo (memoria 13-Jul: "no asumir que la más sofisticada gana sin medir").

Reusa cargar()/FEE_RATE_TAKER_CRYPTO de analisis_gate_riguroso_touch_vs_
win_28jul.py (decisión ladder CLAUDE.md, no duplicar), añade el corte por
tiempo restante en el momento del touch (dato que YA está en
smart_exit_prices.csv vía seg_hasta_fin, simplemente no se usaba).

Solo lectura. No toca prob_yes/decision/stake de ninguna tupla.
"""
import csv
import math
import random
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_gate_riguroso_touch_vs_win_28jul import (  # noqa: E402
    PRICES_CSV, FEE_RATE_TAKER_CRYPTO, UMBRALES, N_SHUFFLE, wilson_ci,
)

N_MIN_CELDA = 15  # mismo mínimo de rigor que el resto del proyecto (nunca 40 aquí -- es exploratorio, se etiqueta como tal, no como gate de promoción)
CORTE_TIEMPO_S = 30  # "temprano" = tocó con >=30s restantes; "tardío" = <30s. Punto medio razonable para ventanas 5min/15min, no calibrado -- si hay n, revisar con más cortes.


def cargar_con_tiempo(strategy: str):
    """market_id -> lista de (seg_hasta_fin, precio, mkt_closed) + resultado final,
    a diferencia de cargar() (que solo guarda el máximo tocado, sin cuándo)."""
    ticks = {}
    for r in csv.DictReader(open(PRICES_CSV, encoding="utf-8")):
        if r["strategy"] != strategy:
            continue
        try:
            precio = float(r["precio_lado"])
            stake = float(r["stake_eur"])
            entry = float(r["entry_price"])
            seg_rest = float(r["seg_hasta_fin"]) if r["seg_hasta_fin"] not in ("", None) else None
        except (ValueError, TypeError):
            continue
        ticks.setdefault(r["market_id"], []).append(
            (r["mkt_closed"], precio, r["ts_utc"], stake, entry, seg_rest))

    resultados = []
    for mid, filas in ticks.items():
        vivos = [(p, seg) for c, p, _, _, _, seg in filas if c == "0" and seg is not None]
        cierres = [(p, ts, s, e) for c, p, ts, s, e, _ in filas if c == "1"]
        if not vivos or not cierres:
            continue
        precio_final, ts_cierre, stake, entry = sorted(cierres, key=lambda x: x[1])[-1]
        gano = precio_final >= 0.9
        resultados.append({
            "mid": mid, "vivos": vivos, "gano": gano,
            "ts_cierre": ts_cierre, "stake": stake, "entry": entry,
        })
    resultados.sort(key=lambda r: r["ts_cierre"])
    return resultados


def touch_temprano_tardio(resultados, umbral, corte_s=CORTE_TIEMPO_S):
    """Para cada trade, ¿tocó `umbral` alguna vez con >=corte_s restantes
    (temprano) y/o alguna vez con <corte_s restantes (tardío)? Un mismo
    trade puede contar en ambos grupos si tocó el umbral más de una vez
    en momentos distintos -- se clasifica por el PRIMER touch de cada tipo,
    que es lo que importaría para una decisión de venta en tiempo real."""
    temprano, tardio = [], []
    for r in resultados:
        toco_temprano = any(p >= umbral and seg >= corte_s for p, seg in r["vivos"])
        toco_tardio = any(p >= umbral and seg < corte_s for p, seg in r["vivos"])
        if toco_temprano:
            temprano.append(r)
        if toco_tardio:
            tardio.append(r)
    return temprano, tardio


def tasa_perdida(grupo):
    if not grupo:
        return None
    perdidas = sum(1 for r in grupo if not r["gano"])
    return len(grupo), perdidas, perdidas / len(grupo)


def shuffle_diff(temprano, tardio, n_shuffle=N_SHUFFLE):
    """¿La diferencia de tasa de pérdida (temprano - tardío) observada es
    mayor de lo que daría barajar las etiquetas gano/pierde entre los dos
    grupos al azar (manteniendo fijo el tamaño de cada grupo)?"""
    n1, n2 = len(temprano), len(tardio)
    if n1 == 0 or n2 == 0:
        return None
    perd1 = sum(1 for r in temprano if not r["gano"])
    perd2 = sum(1 for r in tardio if not r["gano"])
    diff_obs = perd1 / n1 - perd2 / n2
    combinado = [not r["gano"] for r in temprano] + [not r["gano"] for r in tardio]
    random.seed(42)
    mayor_igual = 0
    for _ in range(n_shuffle):
        random.shuffle(combinado)
        g1, g2 = combinado[:n1], combinado[n1:]
        diff_shuf = sum(g1) / n1 - sum(g2) / n2
        if diff_shuf >= diff_obs:
            mayor_igual += 1
    return diff_obs, mayor_igual / n_shuffle


def analizar_estrategia(strategy: str):
    resultados = cargar_con_tiempo(strategy)
    print(f"\n=== {strategy} — n trades resueltos con tick vivo+cierre: {len(resultados)} ===")
    if len(resultados) < N_MIN_CELDA:
        print(f"  n={len(resultados)} < {N_MIN_CELDA} -- ni siquiera el corte más grueso es fiable. Sin conclusión.")
        return

    filas_resumen = []
    for umbral in UMBRALES:
        temprano, tardio = touch_temprano_tardio(resultados, umbral)
        r1 = tasa_perdida(temprano)
        r2 = tasa_perdida(tardio)
        if r1 is None and r2 is None:
            continue
        linea = f"  umbral={umbral:.2f}: "
        if r1:
            n1, p1, t1 = r1
            wlo1, whi1 = wilson_ci(p1, n1)
            linea += f"temprano(>={CORTE_TIEMPO_S}s) n={n1} pierde={t1*100:.1f}% [{wlo1*100:.0f}-{whi1*100:.0f}%]  "
        else:
            linea += "temprano: sin touches  "
        if r2:
            n2, p2, t2 = r2
            wlo2, whi2 = wilson_ci(p2, n2)
            linea += f"tardío(<{CORTE_TIEMPO_S}s) n={n2} pierde={t2*100:.1f}% [{wlo2*100:.0f}-{whi2*100:.0f}%]"
        else:
            linea += "tardío: sin touches"
        print(linea)

        if r1 and r2 and r1[0] >= N_MIN_CELDA and r2[0] >= N_MIN_CELDA:
            diff_obs, p_shuf = shuffle_diff(temprano, tardio)
            print(f"    -> AMBOS con n>={N_MIN_CELDA}: diff(temprano-tardío)={diff_obs*100:+.1f}pp p_shuffle={p_shuf:.4f}")
            filas_resumen.append((umbral, diff_obs, p_shuf, r1[0], r2[0]))
        else:
            print(f"    -> n insuficiente en al menos un grupo (mínimo {N_MIN_CELDA}) -- sin test formal, solo referencia")

    print()
    if not filas_resumen:
        print(f"  CONCLUSIÓN {strategy}: ningún umbral tiene n>={N_MIN_CELDA} en AMBOS grupos todavía -- "
              f"no se puede decidir si el umbral óptimo depende del tiempo restante. Sigue el gate de "
              f"vigia_touch_vs_win_p18.py (n>=40 total) como paso previo obligatorio.")
    else:
        confirmados = [f for f in filas_resumen if f[2] < 0.05 and f[1] > 0]
        if confirmados:
            print(f"  CONCLUSIÓN {strategy}: {len(confirmados)} umbral(es) con evidencia de que tocar "
                  f"TEMPRANO pierde más que tocar TARDE -- soporta la hipótesis de parada óptima "
                  f"dependiente del tiempo. Construir value iteration completo sería el siguiente paso.")
        else:
            print(f"  CONCLUSIÓN {strategy}: con la n disponible, ningún umbral muestra diferencia "
                  f"significativa entre temprano/tardío -- de momento el umbral fijo (paso 1) no pierde "
                  f"nada frente a un umbral dependiente del tiempo. No construir el MDP completo todavía.")


def main():
    for strategy in ("FAVORITO_CONFIRMADO", "GBM_LATE_15M", "BALLENAS_TARDIAS"):
        analizar_estrategia(strategy)


if __name__ == "__main__":
    main()
