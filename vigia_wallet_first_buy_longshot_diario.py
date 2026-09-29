#!/usr/bin/env python3
"""vigia_wallet_first_buy_longshot_diario.py -- Informe DIARIO explícito
(petición Javi, 29-Sep) del progreso de
wallet_first_buy_longshot_executor_dryrun.py -- único segmento CONFIRMADO
por el gate riguroso completo de wallet_first_buy_fwd_tracker.py.

SIEMPRE envía un mensaje. Puramente informativo -- DRY_RUN puro.
Cron sugerido: diario, 08:25 UTC.
"""
import csv
import math
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

FEE = 0.07
OUT = REPO / "data" / "shadow" / "wallet_first_buy_longshot_executor_dryrun.csv"

# mismo umbral de promoción que el resto del proyecto
N_MIN_PROMOCION = 40


def wilson_lo(hits, n, z=1.645):
    if n == 0:
        return 0.0
    p = hits / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centro - margen) / denom


def main():
    if not OUT.exists():
        msg = "🐣 *Wallet first-buy longshot (executor DRY_RUN)*: todavía sin datos."
        print(msg)
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram(msg, bot="cripto")
        except Exception as e:
            print(f"error Telegram: {e}")
        return

    with open(OUT, encoding="utf-8") as f:
        filas = list(csv.DictReader(f))

    ejecutados = [r for r in filas if r.get("decision_dry_run") == "EJECUTADO_DRY_RUN"]
    resueltos = [r for r in ejecutados if r.get("outcome_real")]
    n_total = len(filas)
    n_ejec = len(ejecutados)
    n_fillable_pct = (n_ejec / n_total * 100) if n_total else 0

    partes = [
        "🐣 *Wallet first-buy longshot (executor DRY_RUN, candidata confirmada)* — informe diario",
        f"{n_total} señales longshot detectadas (p_wallet<0,30), {n_ejec} fillable "
        f"(ratio≥5x, {n_fillable_pct:.0f}%), {len(resueltos)} resueltas hasta ahora.",
    ]

    if resueltos:
        hits = sum(1 for r in resueltos if r["outcome"] == r["outcome_real"])
        hit = hits / len(resueltos)
        wlo = wilson_lo(hits, len(resueltos))
        pnl = []
        for r in resueltos:
            try:
                p = float(r["ask"])
            except (KeyError, ValueError, TypeError):
                continue
            win = r["outcome"] == r["outcome_real"]
            pnl.append((1 - p) / p * (1 - FEE) if win else -1.0)
        pnl_medio = sum(pnl) / len(pnl) if pnl else None
        partes.append(f"Resueltas: n={len(resueltos)} hit={hit*100:.1f}% (Wilson90lo={wlo*100:.1f}%) "
                       f"pnl_medio_sim={pnl_medio:+.3f}€/tr" if pnl_medio is not None else
                       f"Resueltas: n={len(resueltos)} hit={hit*100:.1f}%")
        if len(resueltos) >= N_MIN_PROMOCION:
            partes.append(f"⭐ n≥{N_MIN_PROMOCION} alcanzado -- listo para evaluar checklist de 6 categorías.")
        else:
            partes.append(f"Faltan {N_MIN_PROMOCION - len(resueltos)} resoluciones para el mínimo de promoción (n≥{N_MIN_PROMOCION}).")
    else:
        partes.append("Ninguna señal resuelta todavía.")

    msg = "\n".join(partes)
    print(msg)
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram(msg, bot="cripto")
    except Exception as e:
        print(f"[vigia_wallet_first_buy_longshot_diario] error enviando Telegram: {e}")


if __name__ == "__main__":
    main()
