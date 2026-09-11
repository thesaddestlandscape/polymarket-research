#!/usr/bin/env python3
"""
analisis_gate_riguroso_stoploss_tuplas_03ago.py — gate riguroso (Wilson +
shuffle por permutación de signo + split-half) del stop-loss de Smart Exit
(-0.30€, riesgo.smart_exit_stop_loss en config_live.json) restringido a
tuplas live concretas, en vez de la calibración agregada de 22-Jul.

Petición explícita Javi (03-Ago): antes de activar el stop-loss
globalmente, medir si mejora específicamente las tuplas que hoy muestran
payout inverso/pérdidas grandes: BALLENAS_TARDIAS#BTC#15min,
FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#{BTC,ETH}#15min y
BALLENAS_TARDIAS#ETH#5min (añadida a petición de Javi en la misma sesión).

Reusa cargar()/HAIRCUT_VENTA de analisis_smart_exit.py (mismo criterio de
realismo de venta ya validado) — no reinventa la simulación tick a tick,
solo añade granularidad por trade + rigor estadístico por tupla.

Solo lectura: no toca config_live.json ni ninguna orden real.
"""
import csv
from pathlib import Path

import numpy as np

from analisis_smart_exit import cargar, HAIRCUT_VENTA, TRADES_CSV

SL_UMBRAL_EUR = 0.30
ITERS = 20000
_rng = np.random.default_rng(20260803)

TUPLAS = [
    "BALLENAS_TARDIAS#BTC#15min#BUY_YES",
    "FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min#BUY_YES",
    "FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min#BUY_YES",
    "BALLENAS_TARDIAS#ETH#5min#BUY_YES",
]


def _split_tupla(clave: str) -> tuple[str, str, str]:
    partes = clave.split("#")
    return partes[0], "#".join(partes[1:-1]), partes[-1]


def _market_ids_de_tupla(clave: str) -> set[str]:
    strategy, subtype, direction = _split_tupla(clave)
    out = set()
    with open(TRADES_CSV, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r.get("strategy") == strategy and r.get("subtype") == subtype
                    and r.get("direction") == direction and r.get("status") == "CLOSED"):
                out.add(r["market_id"])
    return out


def _simular_por_trade(ticks: dict, cierres: dict, mids: set[str]) -> list[tuple[str, float, float, str]]:
    """Réplica del bucle interno de simular_combinado (TP desactivado,
    solo SL) pero devolviendo (market_id, pnl_real, pnl_sim, motivo) por
    trade en vez de solo el agregado — necesario para Wilson/shuffle/
    split-half por trade."""
    filas = []
    for mid in mids:
        if mid not in cierres or mid not in ticks or not ticks[mid]:
            continue
        real = cierres[mid]
        salida, tipo = None, "aguanta"
        for r in ticks[mid]:
            try:
                stake = float(r["stake_eur"])
                valor = float(r["valor_salida_eur"])
            except (ValueError, KeyError):
                continue
            valor_ajustado = valor * (1.0 - HAIRCUT_VENTA)
            pnl_ajustado = valor_ajustado - stake
            if pnl_ajustado <= -SL_UMBRAL_EUR:
                salida, tipo = pnl_ajustado, "stop_loss"
                break
        sim = salida if salida is not None else real
        filas.append((mid, real, sim, tipo))
    return filas


def _wilson90(k: int, n: int) -> tuple[float, float]:
    if n == 0:
        return (0.0, 0.0)
    z = 1.645
    p = k / n
    denom = 1 + z * z / n
    centro = (p + z * z / (2 * n)) / denom
    margen = (z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5)) / denom
    return (max(0.0, centro - margen), min(1.0, centro + margen))


def _shuffle_paired(deltas: list[float], iters: int = ITERS) -> float:
    """Permutación de signo sobre las diferencias pareadas (sim-real por
    trade) — bajo H0 (el SL no cambia nada) el signo de cada delta sería
    igual de probable +/-. Devuelve p-valor de que |suma real| se deba al
    azar."""
    d = np.asarray(deltas, dtype=np.float64)
    obs = d.sum()
    signos = _rng.choice([-1.0, 1.0], size=(iters, len(d)))
    sumas = (signos * d).sum(axis=1)
    return float(np.mean(np.abs(sumas) >= abs(obs)))


def main():
    ticks, cierres = cargar()

    for clave in TUPLAS:
        mids = _market_ids_de_tupla(clave)
        filas = _simular_por_trade(ticks, cierres, mids)
        n = len(filas)
        print(f"\n=== {clave} ===")
        if n == 0:
            print("  Sin trades con ticks de smart_exit_prices.csv (posición "
                  "resuelta antes de que smart_exit_logger empezara a cubrirla, "
                  "o sin ticks capturados) — no se puede simular.")
            continue

        pnl_real = sum(r[1] for r in filas)
        pnl_sim = sum(r[2] for r in filas)
        n_sl = sum(1 for r in filas if r[3] == "stop_loss")
        deltas = [r[2] - r[1] for r in filas]
        mejora_total = pnl_sim - pnl_real
        n_mejora = sum(1 for d in deltas if d > 0)
        n_empeora = sum(1 for d in deltas if d < 0)

        print(f"  n={n} trades con ticks | SL habría disparado en {n_sl}/{n}")
        print(f"  pnl_real (aguantar, como hoy)  = {pnl_real:+.2f}€")
        print(f"  pnl_sim  (con SL -{SL_UMBRAL_EUR}€)         = {pnl_sim:+.2f}€")
        print(f"  mejora total                    = {mejora_total:+.2f}€")
        print(f"  trades que MEJORAN con SL: {n_mejora} | EMPEORAN: {n_empeora} "
              f"| sin cambio: {n - n_mejora - n_empeora}")

        if n < 15:
            print(f"  ⚠️ n={n} < 15 — EXPLORATORIO, no cumple el listón de "
                  f"CLAUDE.md para concluir. Dirección de la señal, no gate.")

        if n_sl > 0:
            lo, hi = _wilson90(n_mejora, n)
            print(f"  Wilson90% (trades que mejoran) = [{lo*100:.1f}%, {hi*100:.1f}%]")

            p_shuffle = _shuffle_paired(deltas)
            print(f"  shuffle p-valor (mejora total ≠ 0 por azar) = {p_shuffle:.4f}")

            if n >= 8:
                mitad = n // 2
                orden = sorted(filas, key=lambda r: r[0])  # orden estable por market_id
                m1 = sum(r[2] - r[1] for r in orden[:mitad])
                m2 = sum(r[2] - r[1] for r in orden[mitad:])
                print(f"  split-half: 1ª mitad={m1:+.2f}€ | 2ª mitad={m2:+.2f}€ "
                      f"| {'consistente (mismo signo)' if (m1 >= 0) == (m2 >= 0) else 'INCONSISTENTE (signo distinto)'}")
        else:
            print("  El SL nunca se habría disparado en estos trades — no hay nada que evaluar.")


if __name__ == "__main__":
    main()
