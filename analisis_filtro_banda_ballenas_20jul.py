#!/usr/bin/env python3
"""Read-only: valida el filtro de banda de ballenas [banda_lo,banda_hi) de
ballenas_timing_state.json (por activo#15m) sobre las candidatas que
idea_filtro_banda_ballenas_generalizado_19jul.md identificó con salto
fuerte de hit-rate, aplicando el mismo gate riguroso (Wilson+shuffle+PnL
bootstrap, analisis_gate_riguroso.gate) y el gate de crecimiento
logarítmico (analisis_log_growth) al SUBCONJUNTO filtrado, no al agregado.

BUY_YES: se queda con las filas DENTRO de la banda (coincidir con las
ballenas). BUY_NO: se queda con las filas FUERA de la banda (evitar pelear
contra el favorito que las ballenas también quieren).

No toca config_live.json ni ningún gate real. Solo lectura.
"""
import csv, json, math
from pathlib import Path

from analisis_gate_riguroso import gate as gate_riguroso
from analisis_log_growth import _retorno

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data" / "shadow" / "results.csv"
BALLENAS_STATE = REPO / "data" / "shadow" / "ballenas_timing_state.json"
CONFIG_LIVE = REPO / "data" / "live" / "config_live.json"

CANDIDATAS = [
    # (strategy, subtype, decision, activo) -- ampliado 20-Jul: escaneadas las
    # 71 candidatas #15min de candidatos_evaluacion_live (antes solo 9), se
    # quedan las que tienen n>=15 en ambos lados y gap>=10pp en la dirección
    # esperada (BUY_YES mejor dentro, BUY_NO mejor fuera).
    ("GBM_LATE_15M", "BTC#15min", "BUY_YES", "BTC"),
    ("UPDOWN_GBM", "BTC#15min", "BUY_YES", "BTC"),
    ("UPDOWN_GBM", "ETH#15min", "BUY_YES", "ETH"),
    ("GBM_LATE_15M_ESPACIO_ATR", "ETH#15min", "BUY_YES", "ETH"),
    ("GBM_LATE_15M_ESPACIO_ATR", "BTC#15min", "BUY_YES", "BTC"),
    ("GBM_LATE_15M_TARDIO", "BTC#15min", "BUY_YES", "BTC"),
    ("GBM_LATE_15M_TARDIO", "ETH#15min", "BUY_YES", "ETH"),
    ("GBM_LATE_15M_ESPACIO_ATR", "BTC#15min", "BUY_NO", "BTC"),
    ("GBM_LATE_15M_ESPACIO_ATR", "ETH#15min", "BUY_NO", "ETH"),
    ("GBM_LATE_15M_ESPACIO_ATR", "SOL#15min", "BUY_NO", "SOL"),
    ("GBM_LATE_15M", "ETH#15min", "BUY_NO", "ETH"),
    ("GBM_LATE_15M", "BTC#15min", "BUY_NO", "BTC"),
    ("GBM_LATE_15M", "SOL#15min", "BUY_NO", "SOL"),
    ("GBM_LATE_15M_TARDIO", "BTC#15min", "BUY_NO", "BTC"),
    ("GBM_LATE_15M_TARDIO", "ETH#15min", "BUY_NO", "ETH"),
    ("GBM_LATE_15M_TARDIO", "SOL#15min", "BUY_NO", "SOL"),
    # ya LIVE hoy -- mismo patrón, informativo (no se "promociona", se mira
    # si el filtro de banda serviría para refinar algo ya en producción)
    ("FAVORITO_CONFIRMADO", "ETH#15min", "BUY_YES", "ETH"),
    ("FAVORITO_CONFIRMADO", "SOL#15min", "BUY_YES", "SOL"),
    ("FAVORITO_CONFIRMADO", "BTC#15min", "BUY_YES", "BTC"),
]


def cargar_bandas():
    d = json.loads(BALLENAS_STATE.read_text())
    bandas = {}
    for k, v in d.items():
        if not isinstance(v, dict):
            continue
        if v.get("banda_lo") is None:
            continue
        bandas[k] = (v["banda_lo"], v["banda_hi"])
    return bandas


def cargar_filas(claves):
    wanted = {(s, sub, d) for s, sub, d, _ in claves}
    filas = {k: [] for k in wanted}
    with open(RESULTS) as f:
        for row in csv.DictReader(f):
            if row.get("acierto") not in ("0", "1"):
                continue
            k = (row["strategy"], row["subtype"], row["decision"])
            if k in wanted:
                filas[k].append(row)
    return filas


def growth(rows, f):
    if not rows:
        return None
    rs = [_retorno(r) for r in rows]
    return sum(math.log(1 + f * x) for x in rs) / len(rows)


def main():
    bandas = cargar_bandas()
    filas_por_clave = cargar_filas(CANDIDATAS)
    f_bankroll = json.loads(CONFIG_LIVE.read_text())["riesgo"]["max_pct_bankroll_por_trade"]

    for strategy, subtype, decision, activo in CANDIDATAS:
        tupla = f"{strategy}#{subtype}#{decision}"
        banda_key = f"{activo}#15m"
        if banda_key not in bandas:
            print(f"--- {tupla} --- SIN banda calibrada ({banda_key}), omitida")
            continue
        lo, hi = bandas[banda_key]
        rows = filas_por_clave[(strategy, subtype, decision)]

        dentro, fuera = [], []
        for r in rows:
            try:
                p = float(r["precio_yes_mercado"])
            except Exception:
                continue
            (dentro if lo <= p < hi else fuera).append(r)

        objetivo = dentro if decision == "BUY_YES" else fuera
        etiqueta = "DENTRO" if decision == "BUY_YES" else "FUERA"

        print(f"--- {tupla}  (banda {banda_key}=[{lo},{hi}), filtro={etiqueta}) ---")
        print(f"  agregado sin filtrar: n={len(rows)}")
        g_todo = gate_riguroso(rows)
        if g_todo:
            print(f"    todo-n:    n={g_todo['n']:4d} hit={g_todo['hit']*100:5.1f}% "
                  f"IC={g_todo['ic']:+.3f} → {g_todo['veredicto']}")

        g_filtrado = gate_riguroso(objetivo)
        if g_filtrado is None:
            print(f"  filtrado ({etiqueta}): n=0, sin dato")
        else:
            print(f"  filtrado ({etiqueta}): n={g_filtrado['n']:4d} hit={g_filtrado['hit']*100:5.1f}% "
                  f"IC={g_filtrado['ic']:+.3f} Wilson=[{g_filtrado['lo']:.3f},{g_filtrado['hi']:.3f}] "
                  f"p_shuf={g_filtrado['p_shuf']:.3f} → {g_filtrado['veredicto']}")
            if "pnl_media" in g_filtrado:
                print(f"    PnL/trade={g_filtrado['pnl_media']:+.4f} "
                      f"CI90%=[{g_filtrado['pnl_lo']:+.4f},{g_filtrado['pnl_hi']:+.4f}]")
            g_growth = growth(objetivo, f_bankroll)
            if g_growth is not None:
                flag = "PASA" if g_growth > 0 else "NO -- payout inverso"
                print(f"    g(f={f_bankroll:.0%})={g_growth:+.5f}  {flag}")
        print()


if __name__ == "__main__":
    main()
