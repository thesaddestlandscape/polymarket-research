#!/usr/bin/env python3
"""Test de permutación para H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT antes de confiar
en el filtro recién escrito en shadow_predict.py (GBM_LATE_PYBAJO_LONGSHOT_MIN).

Origen (21-Jul, code-review del filtro): el gap de IC (prob_yes_modelo<0.53
vs resto) nunca pasó por el mismo control de permutación que el filtro vecino
(sigma_ewma_delta_pct, 13-Jul, "20k shuffles p=0.0026") antes de tocar un par
live (GBM_LATE_15M#ETH#15min#BUY_YES). Reusa _ic_bayes/_shuffle_pvalue/
_benjamini_hochberg de shadow_postmortem.py (misma fuente que el gate real de
patrones_ganadores) — no reinventa el test. Solo lectura, no toca config.
"""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import shadow_postmortem as sp  # noqa: E402

N_SHUFFLE = 20000
UMBRAL = 0.53


def _bucket(rows):
    n = len(rows)
    aciertos = sum(1 for r in rows if int(r.get("acierto", 0) or 0) == 1)
    pnl = sum(float(r.get("pnl_neto", 0) or 0) for r in rows)
    ic = sp._ic_bayes(aciertos, n) if n else 0.0
    return n, aciertos, ic, pnl


def main():
    resultados = sp.cargar_results()
    base = [r for r in resultados
            if r.get("strategy") == "GBM_LATE_15M" and r.get("decision") == "BUY_YES"]

    bajo, alto, sin_prob = [], [], 0
    for r in base:
        pv = r.get("prob_yes_modelo")
        try:
            pv = float(pv)
        except (TypeError, ValueError):
            sin_prob += 1
            continue
        (bajo if pv < UMBRAL else alto).append(r)

    print(f"Universo GBM_LATE_15M#BUY_YES resuelto: {len(base)} "
          f"(sin prob_yes_modelo válido: {sin_prob})\n")

    for label, rows in (("prob_yes_modelo < 0.53 (zona filtro)", bajo),
                         ("prob_yes_modelo >= 0.53 (resto)", alto)):
        n, aciertos, ic, pnl = _bucket(rows)
        if n == 0:
            print(f"{label}: n=0")
            continue
        p = sp._shuffle_pvalue(n, ic, cola="baja" if ic < 0 else "alta", n_shuffle=N_SHUFFLE)
        cola_txt = "¿sorprendentemente MALO?" if ic < 0 else "¿sorprendentemente BUENO?"
        print(f"{label}")
        print(f"  n={n} aciertos={aciertos} hit={aciertos/n*100:.1f}% "
              f"IC_bayes={ic:+.4f} PNL={pnl:+.2f}€")
        print(f"  shuffle p ({cola_txt}, {N_SHUFFLE} tiradas) = {p:.4f}")
        print(f"  veredicto: {'✅ sobrevive (p<0.05)' if p < 0.05 else '⚠️ NO distinguible de ruido (p>=0.05)'}\n")

    # BH-FDR sobre las 2 comparaciones (K=2, mismo criterio que el resto del sistema)
    n_bajo, ac_bajo, ic_bajo, pnl_bajo = _bucket(bajo)
    n_alto, ac_alto, ic_alto, pnl_alto = _bucket(alto)
    p_bajo = sp._shuffle_pvalue(n_bajo, ic_bajo, cola="baja", n_shuffle=N_SHUFFLE) if n_bajo else 1.0
    p_alto = sp._shuffle_pvalue(n_alto, ic_alto, cola="alta", n_shuffle=N_SHUFFLE) if n_alto else 1.0
    sobrevive = sp._benjamini_hochberg([p_bajo, p_alto], sp.SHUFFLE_FDR)
    print(f"BH-FDR({sp.SHUFFLE_FDR:.0%}) K=2: zona_baja sobrevive={sobrevive[0]} | "
          f"zona_alta sobrevive={sobrevive[1]}")

    # Split temporal (mismo control que ya se hizo a mano en la investigación
    # de sesiones anteriores) — primera vs segunda mitad cronológica de la zona baja.
    bajo_ts = sorted(bajo, key=lambda r: r.get("resolution_timestamp", ""))
    mitad = len(bajo_ts) // 2
    if mitad >= 5:
        print("\nSplit temporal zona_baja (control de estabilidad, no un 2º test):")
        for label, chunk in (("1ª mitad", bajo_ts[:mitad]), ("2ª mitad", bajo_ts[mitad:])):
            n, aciertos, ic, pnl = _bucket(chunk)
            print(f"  {label}: n={n} IC={ic:+.4f} PNL={pnl:+.2f}€")


if __name__ == "__main__":
    main()
