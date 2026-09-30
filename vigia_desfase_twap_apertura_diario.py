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


CORTE_H1 = "2026-09-30T12:45"     # hipótesis congelada el 30-Sep: solo cuenta lo posterior
FEE = 0.07


def _ev_al_ask(resueltas: list) -> list:
    """30-Sep: EV de comprar al ask real el lado que marca el desfase (comisión real 7 % x (1-precio), profundidad
    >= 5x de 1,05). Resultado con 29-30 Sep: 5m −0,080 (IC90 <0, n=1.757) -> descartado; 15m +0,034 (IC cruza 0).
    Al mirar celdas apareció 15m con |desfase| >= 0,03 % y ask < 0,60: +0,24 (n=65, 34 aperturas). Se mira entre ~25
    celdas, así que queda CONGELADA como H1 y solo cuenta el forward desde CORTE_H1.
    Confirmada = n>=40, >=10 días, EV>=+0,10, IC90 por días >0."""
    import random
    from collections import defaultdict
    grupos = {"5m todo": defaultdict(list), "15m todo": defaultdict(list), "H1 antes": defaultdict(list), "H1 forward": defaultdict(list)}
    for r in resueltas:
        try:
            d = float(r["desfase_pct"])
            lado = "Up" if d > 0 else "Down"
            a = float(r["ask_up"] if d > 0 else r["ask_down"])
            prof = float((r["profundidad_up_eur"] if d > 0 else r["profundidad_down_eur"]) or 0)
        except (KeyError, ValueError):
            continue
        if not 0.05 <= a < 0.95 or prof < 5.25 or r["outcome_real"] not in ("Up", "Down"):
            continue
        pnl = (1 if r["outcome_real"] == lado else 0) / a - 1 - FEE * (1 - a)
        dia = r["timestamp_utc"][:10]
        grupos[f"{r['marco']} todo"][dia].append(pnl) if f"{r['marco']} todo" in grupos else None
        if r["marco"] == "15m" and abs(d) >= 0.03 and a < 0.60:
            grupos["H1 forward" if r["timestamp_utc"] >= CORTE_H1 else "H1 antes"][dia].append(pnl)
    out = ["EV al ask real comprando el lado del desfase:"]
    for nombre, pd in grupos.items():
        x = [v for dd in pd.values() for v in dd]
        if not x:
            out.append(f"· {nombre}: sin datos")
            continue
        ic = ""
        ks = [k for k in pd if pd[k]]
        if len(ks) >= 3:
            rng, ms = random.Random(1), []
            for _ in range(1000):
                smp = [y for k in (rng.choice(ks) for _ in ks) for y in pd[k]]
                ms.append(sum(smp) / len(smp))
            ms.sort()
            ic = f" IC90 ({ms[50]:+.3f},{ms[950]:+.3f})"
        ev = sum(x) / len(x)
        marca = ""
        if nombre == "H1 forward":
            marca = " ✅ CONFIRMADA (checklist + /code-review + OK Javi)" if (len(x) >= 40 and len(ks) >= 10 and ev >= 0.10 and ic and ms[50] > 0) \
                else f" (gate: n>=40, >=10 días, EV>=+0,10, IC90>0; van {len(ks)} días)"
        out.append(f"· {nombre}: n={len(x)} días={len(ks)} EV {ev:+.3f}{ic}{marca}")
    return out


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
        partes += _ev_al_ask(resueltas)
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
