#!/usr/bin/env python3
"""vigia_negrisk_arb_diario.py -- Informe DIARIO explícito (petición Javi,
29-Sep: "ponerlo en marcha en dry_run... me pones aviso diario") del
progreso de negrisk_arb_scanner_fase0.py (cron cada 15min).

SIEMPRE envía un mensaje (mismo criterio que el resto de vigías diarios
del proyecto). Puramente informativo -- el scanner es FASE 0, nunca
coloca ninguna orden real.

Cron sugerido: diario, 08:15 UTC.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

OUT = REPO / "data" / "shadow" / "negrisk_arb_fase0.csv"


def main():
    if not OUT.exists():
        msg = "🧩 *NegRisk arb (FASE 0)*: todavía sin datos -- primer cron no ha corrido o falló."
        print(msg)
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram(msg, bot="cripto")
        except Exception as e:
            print(f"error Telegram: {e}")
        return

    with open(OUT, encoding="utf-8") as f:
        filas = list(csv.DictReader(f))

    n_total = len(filas)
    completos = [r for r in filas if r.get("coste_total")]
    accionables = [r for r in filas if r.get("accionable") == "True"]

    margenes = defaultdict(list)
    for r in completos:
        try:
            margenes[r["event_slug"]].append(float(r["margen_pct"]))
        except (KeyError, ValueError):
            continue

    mejor = None
    if margenes:
        ultimos = {slug: vals[-1] for slug, vals in margenes.items()}
        mejor = max(ultimos.items(), key=lambda x: x[1])

    partes = [
        "🧩 *NegRisk arb (conversión NO-basket, FASE 0)* — informe diario",
        f"{n_total} filas históricas, {len(completos)} evaluables (todos los legs con ask), "
        f"{len(accionables)} veces accionable (margen≥2%) hasta ahora.",
    ]
    if mejor:
        slug, m = mejor
        partes.append(f"Mejor margen última lectura: *{slug}* = {m*100:+.2f}%")
    else:
        partes.append("Ningún grupo evaluado completo todavía.")

    msg = "\n".join(partes)
    print(msg)
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram(msg, bot="cripto")
    except Exception as e:
        print(f"[vigia_negrisk_arb_diario] error enviando Telegram: {e}")


if __name__ == "__main__":
    main()
