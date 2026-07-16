#!/usr/bin/env python3
"""Read-only, one-off (16-Jul, petición Javi): ¿la CONCENTRACIÓN del flujo de
ballenas EN UN MERCADO CONCRETO predice el resultado más allá de lo que ya
predice el agregado histórico banda+ventana que usa PYCONFIRMADO?

Contexto: ballenas_timing_history.csv (hasta hoy) solo guardaba si cada
trade de ballena acertó, no de qué LADO apostó — sin el lado no se puede
medir "concentración" (cuánto se inclina el flujo de ese mercado hacia un
lado) sin volver a pedir datos crudos. `ballenas_observer.py` ya se
corrigió para guardar el lado hacia adelante (compro_yes), pero eso tarda
días en acumular n. Este script responde la pregunta AHORA re-pidiendo
/trades para una muestra de mercados YA RESUELTOS que ballenas_observer ya
procesó (mismo método que
idea_ballenas_explica_seleccion_adversa_favoritoconfirmado_16jul, pero
generalizado a dosis-respuesta en vez de un corte binario fillable/no).

Metodología:
1. Para cada combo (activo, marco) con banda significativa en
   ballenas_timing_state.json (SOL/ETH/XRP #15m — BTC#15m excluido, ventana
   [0.07,0.52]min es degenerada, ver idea_vigia_ballenas_tiempo_real_no_viable_16jul),
   toma una muestra de condition_id de ballenas_timing_history.csv con >=3
   trades dentro de banda+ventana.
2. Re-pide /trades (trades_de_mercado, mismo endpoint que ballenas_observer)
   para esa muestra, filtra BUY dentro de banda+ventana, calcula
   pct_mayoria = fracción del volumen de ballenas en el lado mayoritario.
3. Re-pide la resolución oficial (gamma-api, fetch_mercados_paralelo) vía
   condition_id -> market_id (mapeo desde data/markets/*.csv reciente).
4. Bucketiza por pct_mayoria y mide si el lado mayoritario acierta más
   cuanto más concentrado está el flujo (dosis-respuesta) — si es plano, el
   agregado histórico ya captura todo el valor y el chequeo en vivo no
   añade nada; si es monótono, hay señal incremental real.

No escribe nada en data/ ni toca ningún proceso live.
Uso: python3 analisis_ballenas_dosis_respuesta_16jul.py
"""
import csv
import json
import random
import sys
import time
from collections import defaultdict
from pathlib import Path

from smart_money_tracker import trades_de_mercado
from shadow_resolve import fetch_mercados_paralelo, parse_outcome_prices

DIR = Path(__file__).parent
HISTORY_CSV = DIR / "data/shadow/ballenas_timing_history.csv"
STATE_JSON = DIR / "data/shadow/ballenas_timing_state.json"
DIR_MARKETS = DIR / "data/markets"

COMBOS = ["SOL#15m", "ETH#15m", "XRP#15m"]  # BTC#15m excluido (ventana degenerada)
if len(sys.argv) > 1:
    # extensión 16-Jul tarde (roadmap ballenas paso 1, combos 60min): permite
    # re-usar el mismo método sin duplicar código para cualquier lista de
    # combos vía argv, en vez de hardcodear un segundo script casi idéntico.
    COMBOS = sys.argv[1].split(",")
MUESTRA_MAX_POR_COMBO = 250  # ampliado 16-Jul (1ª pasada 90/combo, n=247, 2 buckets bajos <15
                              # -- petición Javi: replicar con muestra más grande antes de decidir nada)
MIN_TRADES_MERCADO = 3
ARCHIVOS_MARKETS_RECIENTES = 5  # últimos N días de data/markets/*.csv


def cargar_bandas():
    estado = json.loads(STATE_JSON.read_text())
    bandas = {}
    for combo in COMBOS:
        if combo not in estado:
            print(f"  aviso: '{combo}' no existe en {STATE_JSON.name} (typo?)")
        e = estado.get(combo, {})
        if not e.get("significativo"):
            continue
        bandas[combo] = (e["banda_lo"], e["banda_hi"], e["rest_lo_min"], e["rest_hi_min"])
    return bandas


def muestrear_mercados(bandas):
    """condition_id -> (activo, marco) para mercados con >=MIN_TRADES_MERCADO
    trades ya vistos en banda+ventana, según el histórico ya acumulado."""
    por_combo = defaultdict(set)
    conteo = defaultdict(int)
    with open(HISTORY_CSV) as f:
        for row in csv.DictReader(f):
            combo = f"{row['activo']}#{row['marco']}"
            if combo not in bandas:
                continue
            lo, hi, rl, rh = bandas[combo]
            try:
                precio = float(row["precio"]); rm = float(row["restante_min"])
            except (ValueError, KeyError):
                continue
            if not (lo <= precio < hi) or not (rl <= rm <= rh):
                continue
            conteo[(combo, row["condition_id"])] += 1

    seleccion = defaultdict(list)
    for (combo, cid), n in conteo.items():
        if n >= MIN_TRADES_MERCADO:
            seleccion[combo].append(cid)
    for combo in seleccion:
        random.shuffle(seleccion[combo])
        seleccion[combo] = seleccion[combo][:MUESTRA_MAX_POR_COMBO]
    return seleccion


def mapear_condition_a_market():
    mapa = {}
    archivos = sorted(DIR_MARKETS.glob("*.csv"))[-ARCHIVOS_MARKETS_RECIENTES:]
    for archivo in archivos:
        with open(archivo, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                cid = row.get("condition_id", "")
                mid = row.get("market_id", "")
                if cid and mid:
                    mapa[cid] = mid
    return mapa


def main():
    bandas = cargar_bandas()
    print(f"Bandas significativas usadas: {bandas}")

    seleccion = muestrear_mercados(bandas)
    total = sum(len(v) for v in seleccion.values())
    print(f"Muestra: {[(k, len(v)) for k, v in seleccion.items()]} (total {total} mercados)")

    print("Construyendo mapa condition_id -> market_id desde data/markets/*.csv reciente...")
    mapa_cid_mid = mapear_condition_a_market()
    print(f"  mapa: {len(mapa_cid_mid)} condition_id conocidos")

    filas_resultado = []  # (combo, cid, pct_mayoria, n, acierta_mayoria)
    for combo, cids in seleccion.items():
        activo, marco = combo.split("#")
        lo, hi, rl, rh = bandas[combo]
        for i, cid in enumerate(cids):
            mid = mapa_cid_mid.get(cid)
            if mid is None:
                continue
            resueltos = fetch_mercados_paralelo([mid], workers=1)
            mercado = resueltos.get(mid)
            if not mercado:
                continue
            precios = parse_outcome_prices(mercado.get("outcomePrices"))
            if not precios or len(precios) < 2:
                continue
            try:
                py, pn = float(precios[0]), float(precios[1])
            except (ValueError, TypeError):
                continue
            if abs(py - 1.0) < 0.01:
                outcome_real = "YES"
            elif abs(pn - 1.0) < 0.01:
                outcome_real = "NO"
            else:
                continue

            trades = trades_de_mercado(cid)
            n_yes = n_no = 0
            for t in trades:
                if (t.get("side") or "").strip().upper() != "BUY":
                    continue
                precio_t = t.get("price")
                outcome_t = (t.get("outcome") or "").strip().lower()
                if precio_t is None or outcome_t not in ("up", "down", "yes", "no"):
                    continue
                try:
                    precio_t = float(precio_t)
                except (ValueError, TypeError):
                    continue
                if not (lo <= precio_t < hi):
                    continue
                # restante_min real requeriría end_dt otra vez; se reutiliza el
                # filtro ya aplicado al construir la muestra (>=3 trades ya
                # vistos en banda+ventana para este cid) como proxy razonable
                # -- aquí solo hace falta el LADO, no re-filtrar por tiempo.
                compro_yes = outcome_t in ("up", "yes")
                if compro_yes:
                    n_yes += 1
                else:
                    n_no += 1
            n = n_yes + n_no
            if n < MIN_TRADES_MERCADO:
                continue
            pct_yes = n_yes / n
            lado_mayoria = "YES" if pct_yes >= 0.5 else "NO"
            pct_mayoria = max(pct_yes, 1 - pct_yes)
            acierta = int(lado_mayoria == outcome_real)
            filas_resultado.append((combo, cid, pct_mayoria, n, acierta))
            if (i + 1) % 20 == 0:
                print(f"  [{combo}] {i+1}/{len(cids)} procesados...")

    print(f"\nMercados con dato completo (lado+resolución): {len(filas_resultado)}")
    if not filas_resultado:
        print("Sin datos suficientes, salir.")
        return

    # Bucketiza por fuerza de concentración (pct_mayoria) y mide accuracy del
    # lado mayoritario en cada bucket -- dosis-respuesta.
    buckets = [(0.5, 0.6), (0.6, 0.7), (0.7, 0.8), (0.8, 0.9), (0.9, 1.01)]
    print(f"\n{'bucket pct_mayoria':<22} {'n':>5} {'accuracy lado mayoria':>24}")
    print("-" * 55)
    for lo, hi in buckets:
        sub = [f for f in filas_resultado if lo <= f[2] < hi]
        if not sub:
            print(f"[{lo:.1f},{hi:.1f})".ljust(22) + f"{0:>5}" + f"{'--':>24}")
            continue
        acc = sum(f[4] for f in sub) / len(sub)
        print(f"[{lo:.1f},{hi:.1f})".ljust(22) + f"{len(sub):>5}" + f"{acc*100:>23.1f}%")

    acc_global = sum(f[4] for f in filas_resultado) / len(filas_resultado)
    print(f"\nAccuracy global (lado mayoritario del flujo de ballenas): {acc_global*100:.1f}% (n={len(filas_resultado)})")

    # Desagregado por combo (16-Jul tarde, roadmap 60min): el agregado
    # arriba mezcla activos -- necesario para decidir combo por combo si
    # entra en combos_validados, no solo "el fenómeno existe en general".
    print(f"\n{'combo':<10} {'bucket pct_mayoria':<20} {'n':>5} {'accuracy':>10}")
    print("-" * 50)
    for combo in sorted(set(f[0] for f in filas_resultado)):
        sub_combo = [f for f in filas_resultado if f[0] == combo]
        for lo, hi in buckets:
            sub = [f for f in sub_combo if lo <= f[2] < hi]
            if not sub:
                continue
            acc = sum(f[4] for f in sub) / len(sub)
            print(f"{combo:<10} [{lo:.1f},{hi:.1f})".ljust(30) + f"{len(sub):>5}" + f"{acc*100:>9.1f}%")
        acc_c = sum(f[4] for f in sub_combo) / len(sub_combo)
        print(f"{combo:<10} {'TOTAL':<20} {len(sub_combo):>5} {acc_c*100:>9.1f}%")


if __name__ == "__main__":
    sys.exit(main() or 0)
