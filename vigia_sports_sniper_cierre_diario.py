#!/usr/bin/env python3
"""vigia_sports_sniper_cierre_diario.py -- Informe DIARIO explícito (petición
Javi, 29-Sep, mismo patrón que el resto de vigías FASE 0 nuevas) del progreso
de sports_sniper_cierre_fase0.py (ronda 1 #6 de las 30 propuestas).

SIEMPRE envía un mensaje. Puramente informativo.
Cron sugerido: diario, 08:20 UTC.
"""
import csv
import sys
import statistics
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

OUT = REPO / "data" / "shadow" / "sports_sniper_cierre_fase0.csv"


def main():
    if not OUT.exists():
        msg = "🏈 *Sports sniper cierre (FASE 0)*: todavía sin datos."
        print(msg)
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram(msg, bot="cripto")
        except Exception as e:
            print(f"error Telegram: {e}")
        return

    with open(OUT, encoding="utf-8") as f:
        filas = list(csv.DictReader(f))

    resueltos = [r for r in filas if r.get("resuelto_en_esta_corrida") == "True"]
    con_ask = [r for r in filas if r.get("ask_real_ganador") not in (None, "") and r.get("resuelto_en_esta_corrida") != "True"]
    con_estimacion = [r for r in filas if r.get("expected_settlement_time") and r.get("resuelto_en_esta_corrida") != "True"]

    # tiempo real de asentamiento para los ya desaparecidos (resuelto_en_esta_corrida)
    tiempos_reales_h = []
    for r in resueltos:
        try:
            pv = datetime.fromisoformat(r["primera_vez_visto_utc"])
            ts = datetime.fromisoformat(r["timestamp_utc"])
            tiempos_reales_h.append((ts - pv).total_seconds() / 3600)
        except Exception:
            continue

    mercados_activos = {}
    for r in filas:
        if r.get("resuelto_en_esta_corrida") == "True":
            mercados_activos.pop(r["condition_id"], None)
        elif r.get("condition_id"):
            mercados_activos[r["condition_id"]] = r

    n_activos = len(mercados_activos)
    n_ask = sum(1 for r in mercados_activos.values() if r.get("ask_real_ganador"))

    partes = [
        "🏈 *Sports sniper fin de partido (FASE 0, ronda1 #6)* — informe diario",
        f"{n_activos} mercados terminados-sin-resolver vigilados ahora mismo, "
        f"{n_ask} con ask real disponible ({n_ask/n_activos*100:.0f}%)" if n_activos else "0 mercados vigilados ahora mismo.",
        f"{len(con_estimacion)}/{max(n_activos,1)} filas con expected_settlement_time (campo nuevo API) presente.",
    ]
    if tiempos_reales_h:
        partes.append(f"Tiempo real hasta desaparecer (n={len(tiempos_reales_h)}): "
                       f"media={statistics.mean(tiempos_reales_h):.1f}h mediana={statistics.median(tiempos_reales_h):.1f}h")
    else:
        partes.append("Todavía ningún mercado ha desaparecido (resuelto) desde que arrancó el observador.")

    msg = "\n".join(partes)
    print(msg)
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram(msg, bot="cripto")
    except Exception as e:
        print(f"[vigia_sports_sniper_cierre_diario] error enviando Telegram: {e}")


if __name__ == "__main__":
    main()
