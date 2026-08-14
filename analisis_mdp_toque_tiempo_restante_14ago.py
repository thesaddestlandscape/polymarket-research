#!/usr/bin/env python3
"""analisis_mdp_toque_tiempo_restante_14ago.py — primer paso hacia el MDP
de parada óptima decidido el 12-Ago (idea_mdp_optimal_stopping_smart_exit_13jul
/ project_mdp_favorito_confirmado_decidido_12ago), nunca implementado.

Antes de construir el value-iteration completo (caro, requiere discretizar
un espacio de estados y validar convergencia), esta es la prueba barata de
la hipótesis central que motiva el MDP: un umbral FIJO de venta (P18,
analisis_gate_riguroso_touch_vs_win_28jul.py) ya falló en las dos familias
probadas (FAVORITO_CONFIRMADO: negativo en €, GBM_LATE_15M: no pasa
split-half) -- la hipótesis es que el umbral óptimo depende de CUÁNTO
TIEMPO QUEDA cuando se toca el precio: vender agresivo con poco tiempo
restante (el continuation value es bajo, no hay margen para que suba más)
debería ser bueno, vender agresivo con mucho tiempo restante (continuation
value alto) debería ser malo -- exactamente el punto ciego que un umbral
constante no distingue.

Segmenta cada evento de "toque" del umbral por `seg_hasta_fin` (tiempo
restante hasta el cierre del mercado, ya logueado en
smart_exit_prices.csv) en 3 buckets, y compara el signo/magnitud de la
mejora € del take-profit dentro de cada bucket. Si el signo cambia entre
buckets (positivo con poco tiempo, negativo con mucho tiempo), confirma
que la dependencia temporal es real y justifica construir el MDP completo
en vez de seguir buscando un umbral fijo mejor.

Solo lectura. No toca prob_yes/decision/stake de ninguna tupla.
"""
import csv
import math
import random
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
PRICES_CSV = REPO / "data/live/smart_exit_prices.csv"

UMBRALES = [0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85]
# Buckets de tiempo restante al momento del toque (segundos hasta el cierre
# del mercado 15min = 900s máximo). Cortes ~1/3 y ~2/3 del marco 15min.
BUCKETS_TIEMPO = [("poco (<300s)", 0, 300), ("medio (300-600s)", 300, 600), ("mucho (>=600s)", 600, 10**9)]
FEE_RATE_TAKER_CRYPTO = 0.07
N_MIN_BUCKET = 5
N_SHUFFLE = 3000
Z_90 = 1.645


def wilson_ci(aciertos, n, z=Z_90):
    if n == 0:
        return (0.0, 0.0)
    phat = aciertos / n
    denom = 1 + z * z / n
    centro = phat + z * z / (2 * n)
    ajuste = z * math.sqrt(phat * (1 - phat) / n + z * z / (4 * n * n))
    return ((centro - ajuste) / denom, (centro + ajuste) / denom)


def cargar(strategy: str):
    """market_id -> lista de ticks vivos (precio, seg_hasta_fin) + resultado final."""
    ticks = defaultdict(list)
    for r in csv.DictReader(open(PRICES_CSV, encoding="utf-8")):
        if r["strategy"] != strategy:
            continue
        try:
            precio = float(r["precio_lado"])
            stake = float(r["stake_eur"])
            entry = float(r["entry_price"])
            seg_fin = float(r["seg_hasta_fin"])
        except (ValueError, TypeError):
            continue
        ticks[r["market_id"]].append((r["mkt_closed"], precio, r["ts_utc"], stake, entry, seg_fin))

    resultados = []
    for mid, filas in ticks.items():
        vivos = [(p, sf) for c, p, _, _, _, sf in filas if c == "0"]
        cierres = [(p, ts, s, e) for c, p, ts, s, e, _ in filas if c == "1"]
        if not vivos or not cierres:
            continue
        precio_final, ts_cierre, stake, entry = sorted(cierres, key=lambda x: x[1])[-1]
        gano = precio_final >= 0.9
        resultados.append((mid, vivos, gano, ts_cierre, stake, entry))
    resultados.sort(key=lambda r: r[3])
    return resultados


def primer_toque(vivos, umbral):
    """Primer tick vivo (cronológicamente, ya vienen en orden de captura)
    que cruza el umbral -- devuelve seg_hasta_fin en ese instante, o None."""
    for precio, seg_fin in vivos:
        if precio >= umbral:
            return seg_fin
    return None


def pnl_trade_hold(gano, stake, entry):
    if entry <= 0:
        return None
    shares = stake / entry
    fee = stake * FEE_RATE_TAKER_CRYPTO * (1 - entry)
    return (shares * 1.0 - stake - fee) if gano else -stake


def pnl_trade_tp(umbral, stake, entry):
    if entry <= 0:
        return None
    shares = stake / entry
    fee = stake * FEE_RATE_TAKER_CRYPTO * (1 - entry)
    return shares * umbral - stake - fee


def main():
    for strategy in ("FAVORITO_CONFIRMADO", "GBM_LATE_15M"):
        resultados = cargar(strategy)
        print("=" * 100)
        print(f"{strategy} -- n(con tick vivo+cierre)={len(resultados)}")
        for umbral in UMBRALES:
            eventos = []  # (seg_fin_al_tocar, gano, stake, entry)
            for mid, vivos, gano, ts_cierre, stake, entry in resultados:
                sf = primer_toque(vivos, umbral)
                if sf is not None:
                    eventos.append((sf, gano, stake, entry))
            if len(eventos) < 3 * N_MIN_BUCKET:
                continue
            print(f"\n  umbral={umbral} (n_tocaron={len(eventos)})")
            for nombre, lo, hi in BUCKETS_TIEMPO:
                grupo = [e for e in eventos if lo <= e[0] < hi]
                if len(grupo) < N_MIN_BUCKET:
                    print(f"    {nombre:20s} n={len(grupo)} (insuficiente, <{N_MIN_BUCKET})")
                    continue
                perdidas = sum(1 for _, gano, _, _ in grupo if not gano)
                tasa = perdidas / len(grupo)
                lo_ci, hi_ci = wilson_ci(len(grupo) - perdidas, len(grupo))
                pnl_hold_total = sum(pnl_trade_hold(gano, s, e) for _, gano, s, e in grupo)
                pnl_tp_total = sum(pnl_trade_tp(umbral, s, e) for _, gano, s, e in grupo)
                mejora = pnl_tp_total - pnl_hold_total
                print(f"    {nombre:20s} n={len(grupo):3d} perd={perdidas:3d} tasa_perdida={tasa:5.1%} "
                      f"wilson90_win=[{lo_ci:.1%},{hi_ci:.1%}] pnl_hold={pnl_hold_total:+7.2f}EUR "
                      f"pnl_tp={pnl_tp_total:+7.2f}EUR mejora={mejora:+7.2f}EUR")


if __name__ == "__main__":
    main()
