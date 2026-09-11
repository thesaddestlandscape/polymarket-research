#!/usr/bin/env python3
"""
analisis_gate_riguroso_touch_vs_win_28jul.py — gate riguroso (Wilson +
shuffle + split-half) sobre la tasa "toca-pero-pierde" en
data/live/smart_exit_prices.csv (dinero real), para calibrar P18 (Smart
Exit) por familia. Continuación de analisis_touch_vs_win_smartexit_28jul.py
tras el fix del bug de smart_exit_logger.py (28-Jul).

Corrección metodológica importante (encontrada al preparar este script):
el "máximo precio tocado" se calcula SOLO sobre ticks con mkt_closed=='0'
(vividos, mientras el trade seguía abierto) -- el tick de cierre sintético
vale exactamente 0.0 o 1.0 (el resultado), así que incluirlo haría que
TODO trade ganador "tocara" 1.0 trivialmente por su propia resolución, no
por movimiento real de precio en vida. Eso mediría una tautología, no una
señal real de "toca alto y luego revierte".

Pregunta que responde: de los trades que tocaron un umbral X EN VIDA
(antes de resolver), ¿qué fracción aun así PERDIÓ? Esa fracción es el
"harvestable edge" de un take-profit -- si es baja y estadísticamente
distinguible del azar, vender al tocar X habría evitado esas pérdidas sin
sacrificar casi nada de las ganadoras.

Solo lectura. No toca prob_yes/decision/stake de ninguna tupla.
"""
import csv
import math
import random
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
PRICES_CSV = REPO / "data/live/smart_exit_prices.csv"  # 29-Jul: era relativo --
# crasheaba bajo cron (vigia_touch_vs_win_p18.py, 06:58 UTC) porque el cron
# no hace cd al repo. Mismo patrón que vigia_supervivencia_diaria.py (mismo
# día) y vigia_gate_bucket_propio.py (28-Jul).
UMBRALES = [0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85]
N_MIN_GATE = 40
N_SHUFFLE = 5000
Z_90 = 1.645
FEE_RATE_TAKER_CRYPTO = 0.07  # misma fee verificada en CLAUDE.md/live_trade.py


def wilson_ci(aciertos, n, z=Z_90):
    if n == 0:
        return (0.0, 0.0)
    phat = aciertos / n
    denom = 1 + z * z / n
    centro = phat + z * z / (2 * n)
    ajuste = z * math.sqrt(phat * (1 - phat) / n + z * z / (4 * n * n))
    return ((centro - ajuste) / denom, (centro + ajuste) / denom)


def cargar(strategy: str):
    """(market_id) -> (max_precio_vivo, gano, ts_cierre) para trades con
    al menos un tick vivo Y un tick de cierre."""
    ticks = defaultdict(list)
    for r in csv.DictReader(open(PRICES_CSV, encoding="utf-8")):
        if r["strategy"] != strategy:
            continue
        try:
            precio = float(r["precio_lado"])
            stake = float(r["stake_eur"])
            entry = float(r["entry_price"])
        except (ValueError, TypeError):
            continue
        ticks[r["market_id"]].append((r["mkt_closed"], precio, r["ts_utc"], stake, entry))

    resultados = []
    for mid, filas in ticks.items():
        vivos = [p for c, p, _, _, _ in filas if c == "0"]
        cierres = [(p, ts, s, e) for c, p, ts, s, e in filas if c == "1"]
        if not vivos or not cierres:
            continue
        max_vivo = max(vivos)
        precio_final, ts_cierre, stake, entry = sorted(cierres, key=lambda x: x[1])[-1]
        gano = precio_final >= 0.9
        resultados.append((mid, max_vivo, gano, ts_cierre, stake, entry))
    resultados.sort(key=lambda r: r[3])  # orden cronológico por cierre
    return resultados


def pnl_hold_euros(resultados) -> float:
    total = 0.0
    for _, _, gano, _, stake, entry in resultados:
        if entry <= 0:
            continue
        shares = stake / entry
        fee = stake * FEE_RATE_TAKER_CRYPTO * (1 - entry)
        total += (shares * 1.0 - stake - fee) if gano else -stake
    return total


def pnl_tp_euros(resultados, umbral) -> tuple[float, int]:
    """PnL agregado (€) si se vende (taker) en cuanto precio_lado toca
    `umbral` en vida, y se sostiene hasta resolución si nunca lo toca.
    Misma aproximación de fee que pnl_hold_euros (fee sobre stake, no
    sobre el valor de venta -- consistente con cómo se calcula ya en
    todo el proyecto para trades reales)."""
    total = 0.0
    n_vendidos = 0
    for _, max_vivo, gano, _, stake, entry in resultados:
        if entry <= 0:
            continue
        shares = stake / entry
        fee = stake * FEE_RATE_TAKER_CRYPTO * (1 - entry)
        if max_vivo >= umbral:
            total += shares * umbral - stake - fee
            n_vendidos += 1
        else:
            total += (shares * 1.0 - stake - fee) if gano else -stake
    return total, n_vendidos


def p_lose_touched(resultados, umbral):
    tocaron = [r for r in resultados if r[1] >= umbral]
    if not tocaron:
        return None
    perdieron = sum(1 for r in tocaron if not r[2])
    return len(tocaron), perdieron, perdieron / len(tocaron)


def shuffle_test(resultados, umbral, n_shuffle=N_SHUFFLE):
    """Baraja las etiquetas gano/pierde entre TODOS los trades resueltos
    (manteniendo fija la pertenencia al grupo "tocó"), recalcula la tasa
    de pérdida del grupo tocado bajo esa baraja n_shuffle veces. p-valor
    (una cola) = fracción de barajas con tasa <= la observada -- prueba
    si tocar el umbral predice perder MENOS de lo que el azar predeciría."""
    tocaron_idx = [i for i, r in enumerate(resultados) if r[1] >= umbral]
    n_tocaron = len(tocaron_idx)
    if n_tocaron == 0:
        return None
    ganaron_flags = [r[2] for r in resultados]
    n_total = len(ganaron_flags)
    obs_perdidas, obs_n, obs_tasa = (
        sum(1 for i in tocaron_idx if not ganaron_flags[i]),
        n_tocaron,
        None,
    )
    obs_tasa = obs_perdidas / obs_n

    contador = 0
    idxs = list(range(n_total))
    for _ in range(n_shuffle):
        random.shuffle(idxs)
        muestreados = idxs[:n_tocaron]
        perdidas_sh = sum(1 for i in muestreados if not ganaron_flags[i])
        tasa_sh = perdidas_sh / n_tocaron
        if tasa_sh <= obs_tasa:
            contador += 1
    return contador / n_shuffle


def split_half(resultados, umbral):
    mitad = len(resultados) // 2
    primera, segunda = resultados[:mitad], resultados[mitad:]
    return p_lose_touched(primera, umbral), p_lose_touched(segunda, umbral)


def main():
    for strat in ["GBM_LATE_15M", "FAVORITO_CONFIRMADO"]:
        resultados = cargar(strat)
        n = len(resultados)
        print(f"\n{'='*90}\n{strat} — n(con tick vivo + cierre)={n}")
        if n < N_MIN_GATE:
            print(f"  n<{N_MIN_GATE} -- SOLO observacional, no continuar con gate riguroso.")
            continue
        gano_total = sum(1 for r in resultados if r[2])
        tasa_perdida_base = 1 - gano_total / n
        pnl_hold = pnl_hold_euros(resultados)
        print(f"  win-rate hold-to-resolution: {gano_total}/{n} = {100*gano_total/n:.1f}% "
              f"(tasa de pérdida base = {100*tasa_perdida_base:.1f}%)")
        print(f"  PnL real hold-to-resolution: {pnl_hold:+.2f}€ ({pnl_hold/n:+.3f}€/trade)")
        print(f"  {'umbral':>7} {'n_tocó':>7} {'perdidas':>9} {'tasa_perdida':>13} "
              f"{'wilson90%':>20} {'p_shuffle':>10} {'split1':>10} {'split2':>10} "
              f"{'PnL_TP€':>10} {'mejora€':>10}")
        for u in UMBRALES:
            r = p_lose_touched(resultados, u)
            if r is None:
                continue
            n_toc, perd, tasa = r
            lo, hi = wilson_ci(perd, n_toc)
            p_sh = shuffle_test(resultados, u)
            (s1, s2) = split_half(resultados, u)
            t1 = f"{100*s1[2]:.0f}%(n={s1[0]})" if s1 else "n/a"
            t2 = f"{100*s2[2]:.0f}%(n={s2[0]})" if s2 else "n/a"
            pnl_tp, _ = pnl_tp_euros(resultados, u)
            print(f"  {u:>7.2f} {n_toc:>7} {perd:>9} {100*tasa:>12.1f}% "
                  f"[{100*lo:>5.1f}%,{100*hi:>5.1f}%] {p_sh:>10.4f} {t1:>10} {t2:>10} "
                  f"{pnl_tp:>+9.2f}€ {pnl_tp-pnl_hold:>+9.2f}€")


if __name__ == "__main__":
    main()
