#!/usr/bin/env python3
"""vigia_desfase_twap_apertura_diario.py -- Informe DIARIO explícito
(petición Javi, 29-Sep) del progreso de desfase_twap_apertura_fase0.py
(ronda1 #2 de las 30 propuestas).

SIEMPRE envía un mensaje. Puramente informativo -- solo observación.
Cron sugerido: diario, 08:30 UTC.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

OUT = REPO / "data" / "shadow" / "desfase_twap_apertura_fase0.csv"


def main():
    if not OUT.exists():
        msg = "📐 *Desfase TWAP apertura (FASE 0, ronda1 #2)*: todavía sin datos."
        print(msg)
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram(msg, bot="cripto")
        except Exception as e:
            print(f"error Telegram: {e}")
        return

    with open(OUT, encoding="utf-8") as f:
        filas = list(csv.DictReader(f))

    validas = [r for r in filas if r.get("desfase_pct") not in (None, "") and r.get("ask_up") and r.get("ask_down")]
    resueltas = [r for r in validas if r.get("outcome_real")]

    partes = [
        "📐 *Desfase TWAP apertura (FASE 0, ronda1 #2)* — informe diario",
        f"{len(filas)} aperturas capturadas, {len(validas)} con ambos lados del libro, "
        f"{len(resueltas)} resueltas.",
    ]

    if resueltas:
        # correlación cualitativa: ¿el signo del desfase predice mid_up>0.5?
        coincide = 0
        for r in resueltas:
            try:
                desfase = float(r["desfase_pct"])
                mid_up = float(r["mid_up"])
            except (KeyError, ValueError):
                continue
            if (desfase > 0 and mid_up > 0.5) or (desfase < 0 and mid_up < 0.5):
                coincide += 1
        if resueltas:
            partes.append(f"Libro ya sesgado en la MISMA dirección que el desfase pre-apertura: "
                           f"{coincide}/{len(resueltas)} ({coincide/len(resueltas)*100:.0f}%) — "
                           f"si es alto, el libro absorbe el momentum desde el primer instante, "
                           f"contradice la premisa 'abre cerca de 0,50'.")
    else:
        partes.append("Ninguna apertura resuelta todavía.")

    msg = "\n".join(partes)
    print(msg)
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram(msg, bot="cripto")
    except Exception as e:
        print(f"[vigia_desfase_twap_apertura_diario] error enviando Telegram: {e}")


if __name__ == "__main__":
    main()
