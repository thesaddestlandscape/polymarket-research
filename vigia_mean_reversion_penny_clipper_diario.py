#!/usr/bin/env python3
"""vigia_mean_reversion_penny_clipper_diario.py -- Informe DIARIO explícito
(petición Javi, 29-Sep: "me pones aviso diario por telegram para saber
como evolucionan") del progreso de los dos observadores FASE 0 nuevos
(mean_reversion_reactivo_fase0.csv / penny_clipper_fase0.csv, hilo dentro
de la screen `observadores`).

SIEMPRE envía un mensaje (no solo si hay cambios) -- mismo criterio que
el resto de vigías diarios del proyecto (CLAUDE.md pt.20). Puramente
informativo -- no toca ninguna decisión, ambos observadores son FASE 0
(solo lectura, sin órdenes reales).

Cron sugerido: diario, 08:10 UTC (no coincide con el resto de vigías de
la franja 07:00-08:00).
"""
import csv
import math
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

FICHEROS = {
    "MEAN REVERSION": REPO / "data/shadow/mean_reversion_reactivo_fase0.csv",
    "PENNY CLIPPER": REPO / "data/shadow/penny_clipper_fase0.csv",
}
STEP = 0.05


def wilson_lo(hits, n, z=1.645):
    if n == 0:
        return 0.0
    p = hits / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centro - margen) / denom


def cargar(path: Path) -> list:
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def resumen(nombre: str, path: Path) -> str:
    filas = cargar(path)
    n_total = len(filas)
    resueltas = [r for r in filas if r.get("outcome_real")]
    n_res = len(resueltas)
    if n_res == 0:
        return f"*{nombre}*: {n_total} señales capturadas, 0 resueltas todavía (esperando cierre de ronda + resolver cada 5min)."

    por_bucket = defaultdict(list)
    for r in resueltas:
        try:
            price = float(r["price_yes"])
            decision = r["decision"]
            outcome = r["outcome_real"]
        except (KeyError, ValueError):
            continue
        p_lado = price if decision == "BUY_YES" else (1 - price)
        win = (decision == "BUY_YES" and outcome == "YES") or (decision == "BUY_NO" and outcome == "NO")
        b = round(math.floor(p_lado / STEP) * STEP, 2)
        por_bucket[b].append((p_lado, win))

    hits_total = sum(1 for r in resueltas
                      if (r["decision"] == "BUY_YES" and r["outcome_real"] == "YES")
                      or (r["decision"] == "BUY_NO" and r["outcome_real"] == "NO"))
    hit_total = hits_total / n_res
    breakeven_total = sum(
        (float(r["price_yes"]) if r["decision"] == "BUY_YES" else 1 - float(r["price_yes"]))
        for r in resueltas
    ) / n_res
    edge_total = (hit_total - breakeven_total) * 100

    buckets_ok = []
    for b, vals in sorted(por_bucket.items()):
        n = len(vals)
        if n < 10:
            continue
        hits = sum(1 for _, w in vals if w)
        breakeven = sum(p for p, _ in vals) / n
        wlo = wilson_lo(hits, n)
        if wlo > breakeven:
            buckets_ok.append(f"[{b:.2f},{b+STEP:.2f})n={n}")

    linea = (f"*{nombre}*: {n_total} señales, {n_res} resueltas — "
             f"hit={hit_total*100:.1f}% breakeven={breakeven_total*100:.1f}% edge={edge_total:+.1f}pp")
    if buckets_ok:
        linea += f"\n  buckets con Wilson90>breakeven: {', '.join(buckets_ok)}"
    else:
        linea += "\n  ningún bucket con n≥10 supera Wilson90 todavía"
    return linea


def main():
    partes = ["🔬 *Mean Reversion / Penny Clipper (AutoPilotPM, FASE 0)* — informe diario"]
    for nombre, path in FICHEROS.items():
        partes.append(resumen(nombre, path))
    msg = "\n\n".join(partes)
    print(msg)
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram(msg, bot="cripto")
    except Exception as e:
        print(f"[vigia_mean_reversion_penny_clipper_diario] error enviando Telegram: {e}")


if __name__ == "__main__":
    main()
