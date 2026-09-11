#!/usr/bin/env python3
"""analisis_hedge_lado_contrario_14ago.py — respuesta a la pregunta directa
de Javi (14-Ago): en vez de "vender la posición original" (P18/Smart Exit,
ya cerrado negativo para FAVORITO_CONFIRMADO), ¿qué pasa si en su lugar se
"compra el lado contrario" (acumulación bidireccional, idea_bidirectional_
accumulation) cuando el precio del lado que tenemos cae? Y además: ¿importa
el timing de esa cobertura (tardía = poco tiempo restante vs temprana =
mucho tiempo restante), igual que ya se comprobó que sí importa para el
take-profit (analisis_mdp_toque_tiempo_restante_14ago.py)?

Reutiliza smart_exit_prices.csv, que YA loguea precio_yes/precio_no en cada
tick (no aproximado, precio real observado de ambos lados) -- no hace falta
instrumentación nueva.

Mecánica simulada: cuando el precio del lado que tenemos CAE hasta un
umbral (ej. 0.10pp/0.15pp/0.20pp por debajo de entry, o un nivel absoluto),
se compra el lado CONTRARIO con un stake igual, al precio real observado en
ese instante (fee 7% incluido, igual que el resto del proyecto). Al cierre:
si el original ganó, el hedge pierde el stake; si el original perdió, el
hedge paga a $1. Se compara el PnL combinado (original+hedge) contra
mantener solo el original (pnl_hold, sin comprar nada más).

Solo lectura. No toca prob_yes/decision/stake de ninguna tupla.
"""
import csv
import math
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
PRICES_CSV = REPO / "data/live/smart_exit_prices.csv"

FEE_RATE_TAKER_CRYPTO = 0.07
CAIDAS_PP = [0.10, 0.15, 0.20, 0.25]  # cuánto por debajo de entry dispara la cobertura
BUCKETS_TIEMPO = [("tardia (<300s)", 0, 300), ("media (300-600s)", 300, 600), ("temprana (>=600s)", 600, 10**9)]
N_MIN_BUCKET = 5


def wilson_ci(aciertos, n, z=1.645):
    if n == 0:
        return (0.0, 0.0)
    phat = aciertos / n
    denom = 1 + z * z / n
    centro = phat + z * z / (2 * n)
    ajuste = z * math.sqrt(phat * (1 - phat) / n + z * z / (4 * n * n))
    return ((centro - ajuste) / denom, (centro + ajuste) / denom)


def cargar(strategy: str):
    ticks = defaultdict(list)
    for r in csv.DictReader(open(PRICES_CSV, encoding="utf-8")):
        if r["strategy"] != strategy:
            continue
        try:
            precio = float(r["precio_lado"])
            p_yes = float(r["precio_yes"])
            p_no = float(r["precio_no"])
            stake = float(r["stake_eur"])
            entry = float(r["entry_price"])
            seg_fin = float(r["seg_hasta_fin"])
        except (ValueError, TypeError):
            continue
        ticks[r["market_id"]].append((r["mkt_closed"], precio, p_yes, p_no, r["direction"], stake, entry, seg_fin))

    resultados = []
    for mid, filas in ticks.items():
        vivos = [(p, py, pn, d, sf) for c, p, py, pn, d, _, _, sf in filas if c == "0"]
        cierres = [(p, s, e, d) for c, p, py, pn, d, s, e, sf in filas if c == "1"]
        if not vivos or not cierres:
            continue
        precio_final, stake, entry, direction = cierres[-1]
        gano = precio_final >= 0.9
        resultados.append((mid, vivos, gano, stake, entry, direction))
    return resultados


def pnl_original(gano, stake, entry):
    shares = stake / entry
    fee = stake * FEE_RATE_TAKER_CRYPTO * (1 - entry)
    return (shares * 1.0 - stake - fee) if gano else -stake


def pnl_hedge(gano_original, stake_h, precio_contrario_en_trigger):
    """El hedge gana cuando el ORIGINAL pierde (apostó al lado contrario)."""
    if precio_contrario_en_trigger <= 0 or precio_contrario_en_trigger >= 1:
        return None
    shares = stake_h / precio_contrario_en_trigger
    fee = stake_h * FEE_RATE_TAKER_CRYPTO * (1 - precio_contrario_en_trigger)
    gano_hedge = not gano_original
    return (shares * 1.0 - stake_h - fee) if gano_hedge else -stake_h


def primer_disparo(vivos, entry, caida_pp):
    """Primer tick donde precio_lado cae caida_pp por debajo de entry ->
    devuelve (seg_hasta_fin, precio_contrario) en ese instante, o None."""
    umbral = entry - caida_pp
    for precio, p_yes, p_no, direction, sf in vivos:
        if precio <= umbral:
            precio_contrario = p_no if direction == "BUY_YES" else p_yes
            return sf, precio_contrario
    return None


def main():
    for strategy in ("FAVORITO_CONFIRMADO", "GBM_LATE_15M"):
        resultados = cargar(strategy)
        print("=" * 100)
        print(f"{strategy} -- n(con tick vivo+cierre)={len(resultados)}")
        for caida in CAIDAS_PP:
            eventos = []  # (seg_fin_disparo, gano, stake, entry, precio_contrario)
            for mid, vivos, gano, stake, entry, direction in resultados:
                disparo = primer_disparo(vivos, entry, caida)
                if disparo is not None:
                    sf, precio_contrario = disparo
                    eventos.append((sf, gano, stake, entry, precio_contrario))
            if len(eventos) < 3 * N_MIN_BUCKET:
                continue
            print(f"\n  caida_disparo={caida:.2f}pp bajo entry (n_dispararon={len(eventos)})")
            for nombre, lo, hi in BUCKETS_TIEMPO:
                grupo = [e for e in eventos if lo <= e[0] < hi]
                if len(grupo) < N_MIN_BUCKET:
                    print(f"    {nombre:20s} n={len(grupo)} (insuficiente, <{N_MIN_BUCKET})")
                    continue
                pnl_hold_total = sum(pnl_original(g, s, e) for _, g, s, e, _ in grupo)
                combinados = []
                validos = 0
                for _, g, s, e, pc in grupo:
                    po = pnl_original(g, s, e)
                    ph = pnl_hedge(g, s, pc)
                    if ph is None:
                        continue
                    combinados.append(po + ph)
                    validos += 1
                if validos < N_MIN_BUCKET:
                    print(f"    {nombre:20s} n={len(grupo):3d} (precio_contrario inválido en la mayoría, saltado)")
                    continue
                pnl_combinado_total = sum(combinados)
                mejora = pnl_combinado_total - pnl_hold_total
                ganadores_original = sum(1 for _, g, _, _, _ in grupo if g)
                lo_ci, hi_ci = wilson_ci(ganadores_original, len(grupo))
                print(f"    {nombre:20s} n={len(grupo):3d} (validos={validos:3d}) win_orig={ganadores_original/len(grupo):5.1%} "
                      f"wilson90=[{lo_ci:.1%},{hi_ci:.1%}] pnl_hold={pnl_hold_total:+7.2f}EUR "
                      f"pnl_hedge={pnl_combinado_total:+7.2f}EUR mejora={mejora:+7.2f}EUR")


if __name__ == "__main__":
    main()
