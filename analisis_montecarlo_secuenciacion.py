#!/usr/bin/env python3
"""analisis_montecarlo_secuenciacion.py — hueco de robustez #1 de
`idea_huecos_robustez_metodologia_21jul` (memoria nativa, checklist de 10
tests de validación quant compartido por Javi 21-Jul).

Pregunta: los circuit breakers reales (freno diario -30%, freno ventana
-20%, racha=4 pérdidas consecutivas, suelo bankroll_minimo=1€) son
sensibles al ORDEN en que llegan los trades, no solo a CUÁLES ganan/pierden
— una mala racha al principio del día dispara distinto que la misma racha
al final. Este script mide cuánto: toma el CONJUNTO real de resultados
(pnl_neto_eur) de `data/live/trades.csv` (dinero real, n=226 CLOSED), fija
la estructura temporal real (mismo número de trades por día/ventana que
realmente ocurrió — reutiliza `ventana_en`/`madrid_dt`/`cargar_config` de
shadow_pnl_fiel.py, no reinventa), y permuta miles de veces QUÉ resultado
cae en QUÉ hueco temporal, re-simulando la misma cascada de frenos.

Reporta: cómo se compara el orden REAL (lo que de hecho pasó) contra la
distribución Monte Carlo de la MISMA cartera de resultados en otros
órdenes — si el real es un percentil extremo (muy afortunado o muy
desafortunado), o si cae dentro de lo típico.

Solo lectura. No decide nada, no toca ningún parámetro de config_live.json.
"""
import argparse
import csv
import random
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from shadow_pnl_fiel import cargar_config, madrid_dt, ventana_en, parse_ts

REPO = Path(__file__).resolve().parent
TRADES_CSV = REPO / "data" / "live" / "trades.csv"

N_SHUFFLES = 5000


def cargar_trades_reales():
    """Lista de (close_ts, pnl_neto_eur) para trades CLOSED reales,
    ordenada cronológicamente por close_timestamp (cuándo el PnL realmente
    impactó el bankroll, no cuándo se envió la orden)."""
    filas = []
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "CLOSED":
                continue
            ts = parse_ts(row.get("close_timestamp", ""))
            if ts is None:
                continue
            try:
                pnl = float(row["pnl_neto_eur"])
            except (KeyError, ValueError, TypeError):
                continue
            filas.append((ts, pnl))
    filas.sort(key=lambda x: x[0])
    return filas


def simular(pnls_en_orden, config, bankroll_inicial, slots_ts):
    """Misma cascada de frenos que live_stake.py::verificar_circuit_breaker
    (freno diario, racha, freno ventana, suelo) aplicada a UN bankroll de
    cartera compartido (no aislado por tupla — los frenos reales SON a
    nivel de cartera). `pnls_en_orden` es la secuencia de PnL a aplicar,
    `slots_ts` son los timestamps REALES (fijos) que definen la estructura
    de día/ventana — separar ambos es lo que permite el shuffle: el
    timestamp de cada hueco no cambia, solo qué PnL cae en él."""
    riesgo = config.get("riesgo", {})
    cb = riesgo.get("circuit_breaker", {})
    freno_diario_pct = cb.get("freno_diario_pct", 0.30)
    freno_ventana_pct = cb.get("freno_ventana_pct", 0.20)
    bankroll_minimo = cb.get("bankroll_minimo_eur", 1.00)
    max_racha = cb.get("max_perdidas_consecutivas", 4)

    bankroll = bankroll_inicial
    dia_actual = None
    bankroll_inicio_dia = bankroll_inicial
    racha = 0
    freno_diario_activo_hoy = False
    ventana_actual = None
    bankroll_inicio_ventana = bankroll_inicial
    pnl_ventana = 0.0
    latches_ventana = set()

    n_bloqueados = 0
    n_ejecutados = 0
    dias_con_freno_diario = set()
    ventanas_con_freno = 0
    bust = False
    ts_bust = None

    for ts, pnl in zip(slots_ts, pnls_en_orden):
        if bust:
            break
        fecha_md = madrid_dt(ts, config).date()
        if dia_actual != fecha_md:
            dia_actual = fecha_md
            bankroll_inicio_dia = bankroll
            racha = 0
            freno_diario_activo_hoy = False

        nombre_v = ventana_en(ts, config)
        clave_v = (fecha_md, nombre_v)
        if ventana_actual != clave_v:
            ventana_actual = clave_v
            bankroll_inicio_ventana = bankroll
            pnl_ventana = 0.0

        if (freno_diario_activo_hoy or clave_v in latches_ventana
                or racha >= max_racha):
            n_bloqueados += 1
            continue

        bankroll += pnl
        pnl_ventana += pnl
        n_ejecutados += 1
        racha = racha + 1 if pnl < 0 else 0

        if bankroll <= bankroll_minimo:
            bust = True
            ts_bust = ts
            break
        if bankroll_inicio_dia > 0 and (bankroll_inicio_dia - bankroll) / bankroll_inicio_dia >= freno_diario_pct:
            freno_diario_activo_hoy = True
            dias_con_freno_diario.add(fecha_md)
        if pnl_ventana < 0 and bankroll_inicio_ventana > 0 and abs(pnl_ventana) / bankroll_inicio_ventana >= freno_ventana_pct:
            if clave_v not in latches_ventana:
                ventanas_con_freno += 1
            latches_ventana.add(clave_v)

    return {
        "bankroll_final": round(bankroll, 4),
        "bust": bust,
        "ts_bust": ts_bust.isoformat() if ts_bust else None,
        "n_ejecutados": n_ejecutados,
        "n_bloqueados": n_bloqueados,
        "n_dias_freno_diario": len(dias_con_freno_diario),
        "n_ventanas_freno": ventanas_con_freno,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--bankroll-inicial", type=float, default=25.44)
    ap.add_argument("--n-shuffles", type=int, default=N_SHUFFLES)
    ap.add_argument("--seed", type=int, default=22072026)
    args = ap.parse_args()

    config = cargar_config(REPO)
    trades = cargar_trades_reales()
    print(f"Trades reales CLOSED cargados: {len(trades)}")
    if len(trades) < 15:
        print("n<15 -- no hay base suficiente para concluir nada (CLAUDE.md).")
        return

    slots_ts = [t[0] for t in trades]
    pnls_reales = [t[1] for t in trades]

    baseline = simular(pnls_reales, config, args.bankroll_inicial, slots_ts)
    print("\n=== Orden REAL (lo que de hecho pasó) ===")
    for k, v in baseline.items():
        print(f"  {k}: {v}")

    rng = random.Random(args.seed)
    resultados = []
    for _ in range(args.n_shuffles):
        pnls_shuf = pnls_reales[:]
        rng.shuffle(pnls_shuf)
        resultados.append(simular(pnls_shuf, config, args.bankroll_inicial, slots_ts))

    n_bust = sum(1 for r in resultados if r["bust"])
    finales = sorted(r["bankroll_final"] for r in resultados)
    n_freno_diario = [r["n_dias_freno_diario"] for r in resultados]
    n_freno_ventana = [r["n_ventanas_freno"] for r in resultados]

    percentil_real = sum(1 for f in finales if f <= baseline["bankroll_final"]) / len(finales)

    print(f"\n=== Monte Carlo: {args.n_shuffles} reordenaciones del MISMO conjunto de {len(trades)} resultados ===")
    print(f"P(bust / suelo tocado) bajo reordenación aleatoria: {n_bust/len(resultados)*100:.1f}%  ({n_bust}/{len(resultados)})")
    print(f"Bankroll final -- real: {baseline['bankroll_final']:.2f}€  "
          f"| MC p10={finales[int(0.10*len(finales))]:.2f}€  p50={finales[int(0.50*len(finales))]:.2f}€  p90={finales[int(0.90*len(finales))]:.2f}€")
    print(f"Percentil del orden REAL dentro de la distribución MC de bankroll final: {percentil_real*100:.1f}%")
    print(f"Días con freno diario activado -- real: {baseline['n_dias_freno_diario']}  | MC media: {sum(n_freno_diario)/len(n_freno_diario):.2f}  max: {max(n_freno_diario)}")
    print(f"Ventanas con freno activado   -- real: {baseline['n_ventanas_freno']}     | MC media: {sum(n_freno_ventana)/len(n_freno_ventana):.2f}  max: {max(n_freno_ventana)}")

    print("\n=== Lectura ===")
    if percentil_real <= 0.10:
        print("El orden real cayó en el 10% MÁS DESAFORTUNADO de reordenaciones posibles del mismo")
        print("conjunto de resultados -- la mala racha del período no es (solo) mala suerte de qué")
        print("trades ganaron/perdieron, también de EN QUÉ ORDEN llegaron. Los frenos amplifican esto")
        print("por diseño (cortan tras una mala racha, no reparten el riesgo en el tiempo).")
    elif percentil_real >= 0.90:
        print("El orden real cayó en el 10% MÁS AFORTUNADO -- con otro orden de los mismos resultados,")
        print("probablemente habría ido peor. No usar el resultado real como referencia sin este contexto.")
    else:
        print("El orden real es TÍPICO dentro de la distribución Monte Carlo -- no hay evidencia de que")
        print("la secuenciación específica (buena o mala suerte de orden) explique el resultado real,")
        print("más allá del propio conjunto de resultados.")
    print(f"\nP(bust) de {n_bust/len(resultados)*100:.1f}% bajo pura reordenación es la métrica clave para")
    print("calibrar si racha=4/freno_diario=30%/freno_ventana=20%/suelo=1€ dan margen suficiente --")
    print("no una promesa de nunca disparar, sino qué fracción de las 'malas suertes' plausibles evita el bust.")


if __name__ == "__main__":
    main()
