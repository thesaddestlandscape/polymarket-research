#!/usr/bin/env python3
"""Resuelve el tracker de ballenas_executor_5min.py (data/shadow/
ballenas_5min_dry_run.csv) contra el outcome OFICIAL de Polymarket
(gamma-api, mismo mecanismo que shadow_resolve.py -- resolutionSource real
de estos mercados, no un proxy de klines).

Origen (21-Jul): 3 días de señales CONFIRMADO sin ningún tracker de
resultados -- gap detectado tras corrección de Javi sobre revisar SIEMPRE
la infraestructura de ballenas. El ejecutor SIEMPRE apuesta BUY_YES (única
dirección que dispara), así que acierto = outcome_real == "YES".

No usa el margen de confirmación temporal de shadow_resolve.evaluar() a
propósito: los mercados de este tracker llevan horas/días cerrados cuando
se resuelven aquí (no monitoreo en vivo de un asentamiento inestable), así
que basta con outcomePrices ya estable en 0/1 -- exigir margen adicional
solo retrasaría sin motivo.

Cron sugerido: cada 10min, igual de barato que el resto de vigías de
análisis. Solo lectura de gamma-api + escritura de este CSV -- no toca
config_live.json, no ejecuta nada, no toca dinero.
"""
import csv
import fcntl
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from shadow_resolve import estado_mercado, parse_outcome_prices  # noqa: E402

TRACKER = REPO / "data/shadow/ballenas_5min_dry_run.csv"
# 27-Jul (/code-review): mismo fichero de lock que ballenas_executor_5min.py
# -- ese proceso (screen ballenas_5m, persistente) también reescribe
# TRACKER entero (migración de columna + backfill), y este script corre
# como cron aparte. Sin flock compartido, una reescritura completa de
# cualquiera de los dos procesos puede solapar con la del otro y perder
# outcome_real/acierto ya resueltos.
TRACKER_LOCK = REPO / "data/shadow/ballenas_5min_dry_run.csv.lock"
UMBRAL_RESUELTO = 0.98  # mismo espíritu que shadow_resolve (cerca de 1.0/0.0)


def _outcome(mercado: dict) -> str | None:
    precios = parse_outcome_prices(mercado.get("outcomePrices"))
    if not precios or len(precios) < 2:
        return None
    try:
        p_yes, p_no = float(precios[0]), float(precios[1])
    except (TypeError, ValueError):
        return None
    if p_yes >= UMBRAL_RESUELTO:
        return "YES"
    if p_no >= UMBRAL_RESUELTO:
        return "NO"
    return None


def main():
    if not TRACKER.exists():
        print("Sin tracker todavía -- ballenas_executor_5min.py no ha confirmado nada aún.")
        return 0

    # 27-Jul (/code-review, 2ª pasada): el lock NO puede envolver las
    # llamadas de red a gamma-api (estado_mercado, con reintentos/backoff
    # en 429 -- puede tardar varios segundos) -- ballenas_executor_5min.py
    # llama a _registrar_tracker() de forma SÍNCRONA en el hot path de una
    # confirmación real (antes de disparar()), y si ese proceso se queda
    # esperando este flock mientras aquí se hacen llamadas de red lentas,
    # se retrasa la decisión de una señal con dinero real en juego --
    # exactamente la sensibilidad de timing que el proyecto vigila siempre.
    # Diseño: 1) leer sin lock, 2) resolver TODAS las llamadas de red sin
    # lock, 3) adquirir el lock solo para el tramo final (releer fresco por
    # si el executor añadió filas mientras tanto, fusionar, escribir).
    with open(TRACKER, newline="", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))

    pendientes = [r for r in filas if not r.get("outcome_real")]
    print(f"Filas totales: {len(filas)} | pendientes de resolver: {len(pendientes)}")

    outcomes_por_market_id = {}
    for r in pendientes:
        mid = r.get("market_id")
        if not mid:
            continue
        mercado = estado_mercado(mid)  # red, sin lock
        if mercado is None:
            continue
        outcome = _outcome(mercado)
        if outcome is None:
            continue
        outcomes_por_market_id[mid] = outcome

    resueltas_ahora = 0
    if outcomes_por_market_id:
        lock_f = open(TRACKER_LOCK, "w")
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        try:
            # Releer fresco bajo el lock -- el executor puede haber añadido
            # filas nuevas mientras hacíamos las llamadas de red de arriba.
            with open(TRACKER, newline="", encoding="utf-8") as f:
                filas = list(csv.DictReader(f))
            from datetime import datetime, timezone
            for r in filas:
                mid = r.get("market_id")
                outcome = outcomes_por_market_id.get(mid)
                if outcome is None or r.get("outcome_real"):
                    continue
                r["outcome_real"] = outcome
                r["acierto"] = "1" if outcome == "YES" else "0"  # siempre BUY_YES
                r["resolved_ts"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
                resueltas_ahora += 1
            if resueltas_ahora:
                with open(TRACKER, "w", newline="", encoding="utf-8") as f:
                    w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
                    w.writeheader()
                    w.writerows(filas)
        finally:
            fcntl.flock(lock_f, fcntl.LOCK_UN)
            lock_f.close()
    print(f"Resueltas en este ciclo: {resueltas_ahora}")

    resueltas = [r for r in filas if r.get("outcome_real")]
    if resueltas:
        print(f"\n=== Resumen acumulado (n={len(resueltas)}) ===")
        from collections import defaultdict
        por_activo = defaultdict(lambda: [0, 0])
        for r in resueltas:
            por_activo[r["activo"]][1] += 1
            if r["acierto"] == "1":
                por_activo[r["activo"]][0] += 1
        wins_total = sum(int(r["acierto"]) for r in resueltas)
        n_total = len(resueltas)
        print(f"TOTAL: n={n_total} hit={wins_total/n_total*100:.1f}%")
        for activo, (w_, n_) in sorted(por_activo.items()):
            print(f"  {activo}: n={n_} hit={w_/n_*100:.1f}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())
