#!/usr/bin/env python3
"""Read-only, one-off (17-Jul, petición Javi tras corregir el rumbo:
"investigar un indicador MÁS TEMPRANO, antes de que la banda 0.7-0.9 se
vacíe"). El veto_ballenas/BALLENAS_CONFIRMADAS_15M ya viven en la banda
[0.7,0.9) -- para cuando la concentración ahí es medible (n>=3), la
profundidad ya está consumida (hallazgo de esta sesión). Pregunta nueva:
¿el/los PRIMEROS trades de ballena en un mercado (los que llegan más
temprano, a precio más bajo, con más restante_min) ya predicen hacia
dónde va a converger el mercado, ANTES de que el resto de la manada
llegue y se coma la profundidad?

Método: ballenas_timing_history.csv (ts_trade + restante_min + precio +
compro_yes + acierto, sin llamadas de red) -- para cada mercado SOL/ETH
#15min, ordena sus trades de ballena por restante_min DESCENDENTE (el más
temprano primero) y mide, para las primeras K=1,2,3 operaciones: ¿su lado
mayoritario coincide con la resolución final? ¿A qué precio y con cuánto
restante_min llegan (para saber si de verdad dejan margen de entrada
antes de que la banda [0.7,0.9) se vacíe)?

No escribe nada, no toca dinero ni config.
Uso: python3 analisis_ballenas_primer_movimiento_17jul.py
"""
import csv
from collections import defaultdict
from pathlib import Path

from analisis_gate_riguroso import wilson_ci, ic_bayes, Z_90

REPO = Path(__file__).resolve().parent
BALLENAS = REPO / "data" / "shadow" / "ballenas_timing_history.csv"

ACTIVOS = ("SOL", "ETH")
MARCO = "15m"
MIN_TRADES_MERCADO = 1   # aquí SÍ interesan mercados con 1 solo trade temprano


def cargar_timelines() -> dict:
    """condition_id -> lista de (restante_min, precio, compro_yes) ordenada
    de más temprano (restante_min alto) a más tardío. resuelto_yes aparte."""
    crudo = defaultdict(list)
    resueltos = {}
    acuerdo = defaultdict(lambda: True)
    with open(BALLENAS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["activo"] not in ACTIVOS or r["marco"] != MARCO:
                continue
            cid = r["condition_id"]
            try:
                precio = float(r["precio"])
                restante = float(r["restante_min"])
            except (ValueError, KeyError):
                continue
            compro_yes = r.get("compro_yes") in ("1", "True", "true")
            acierto = r.get("acierto") in ("1", "True", "true")
            resuelto_fila = compro_yes == acierto
            if cid not in resueltos:
                resueltos[cid] = resuelto_fila
            elif resueltos[cid] != resuelto_fila:
                acuerdo[cid] = False
            crudo[cid].append((restante, precio, compro_yes, r["activo"]))

    timelines = {}
    for cid, filas in crudo.items():
        if not acuerdo[cid]:
            continue
        filas.sort(key=lambda x: -x[0])  # restante_min desc = más temprano primero
        timelines[cid] = {"trades": filas, "resuelto_yes": resueltos[cid],
                           "activo": filas[0][3]}
    return timelines


def main():
    print(f"Cargando {BALLENAS.name} ({ACTIVOS} #{MARCO}, una pasada)...")
    timelines = cargar_timelines()
    print(f"Mercados con timeline completo y consistente: {len(timelines)}")

    for K in (1, 2, 3):
        filas = []  # (activo, restante_medio, precio_medio, acierta)
        for cid, info in timelines.items():
            trades = info["trades"]
            if len(trades) < K:
                continue
            primeros = trades[:K]
            n_yes = sum(1 for t in primeros if t[2])
            lado_mayoria_yes = n_yes >= (K / 2)
            if K > 1 and n_yes == K / 2:
                continue  # empate exacto (solo posible con K par) -- sin mayoría clara, descartar
            restante_medio = sum(t[0] for t in primeros) / K
            precio_medio = sum(t[1] for t in primeros) / K
            acierta = int(lado_mayoria_yes == info["resuelto_yes"])
            filas.append((info["activo"], restante_medio, precio_medio, acierta))

        if not filas:
            print(f"\n=== K={K} primeros trades: sin datos ===")
            continue
        aciertos = sum(f[3] for f in filas)
        n = len(filas)
        lo, hi = wilson_ci(aciertos, n, Z_90)
        ic = ic_bayes(aciertos, n)
        rest_medio_global = sum(f[1] for f in filas) / n
        precio_medio_global = sum(f[2] for f in filas) / n
        print(f"\n=== K={K} primer(os) trade(s) de ballena por mercado ===")
        print(f"n={n}  hit={100*aciertos/n:.1f}%  Wilson90%=[{lo:.3f},{hi:.3f}]  ic_bayes={ic:+.4f}  "
              f"restante_min medio={rest_medio_global:.2f}  precio medio={precio_medio_global:.3f}")
        for activo in ACTIVOS:
            sub = [f for f in filas if f[0] == activo]
            if not sub:
                continue
            ac = sum(f[3] for f in sub)
            nn = len(sub)
            loA, hiA = wilson_ci(ac, nn, Z_90)
            rest_a = sum(f[1] for f in sub) / nn
            precio_a = sum(f[2] for f in sub) / nn
            print(f"  {activo}: n={nn} hit={100*ac/nn:.1f}% Wilson90%=[{loA:.3f},{hiA:.3f}] "
                  f"restante_min medio={rest_a:.2f} precio medio={precio_a:.3f}")

    # Comparación directa: precio/restante del PRIMER trade vs el momento en
    # que el mercado alcanza concentración>=0.6 con n>=3 (el trigger actual
    # de BALLENAS_CONFIRMADAS_15M/veto_ballenas) -- ¿cuánto margen real se
    # gana entrando en el primer trade en vez de esperar la confirmación?
    print("\n=== Margen ganado: primer trade vs momento de confirmación (n>=3, conc>=0.6) ===")
    margenes_precio, margenes_restante = [], []
    for cid, info in timelines.items():
        trades = info["trades"]
        if len(trades) < 3:
            continue
        primer_restante, primer_precio = trades[0][0], trades[0][1]
        n_yes = n_no = 0
        momento_confirma = None
        for t in trades:
            if t[2]:
                n_yes += 1
            else:
                n_no += 1
            n_tot = n_yes + n_no
            if n_tot >= 3 and (n_yes / n_tot >= 0.6 or n_no / n_tot >= 0.6):
                momento_confirma = t
                break
        if momento_confirma is None:
            continue
        margenes_precio.append(momento_confirma[1] - primer_precio)
        margenes_restante.append(primer_restante - momento_confirma[0])

    if margenes_precio:
        n = len(margenes_precio)
        print(f"n={n} mercados con confirmación n>=3 alcanzada")
        print(f"  precio: primer trade más barato en {sum(margenes_precio)/n:+.3f} de media "
              f"(precio sube según se confirma)")
        print(f"  tiempo: primer trade llega {sum(margenes_restante)/n:+.2f} min ANTES de la "
              f"confirmación de media")


if __name__ == "__main__":
    main()
