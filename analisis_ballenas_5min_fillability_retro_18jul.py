#!/usr/bin/env python3
"""Read-only, one-off (18-Jul, petición Javi: "investiga, yo creo que si
compensa" sobre construir un ejecutor de baja latencia para GBM_LATE_5M,
igual que se hizo para BALLENAS_TARDIAS#BTC#15min).

Generaliza analisis_ballenas_btc15m_fillability_retro_16jul.py (mismo
método: re-pedir /trades sobre mercados ya resueltos y medir el tamaño USD
real de los trades de ballena dentro de banda+ventana) a los 4 combos 5m
que ballenas_timing_state.json ya marca "significativo" hoy — antes de
decidir si construir el ejecutor, responder con datos reales si el libro
tiene profundidad fillable en esa ventana, no solo si las ballenas tienen
edge.

Uso: python3 analisis_ballenas_5min_fillability_retro_18jul.py [MUESTRA_MAX]
"""
import sys
from datetime import datetime, timezone
from pathlib import Path

from smart_money_tracker import trades_de_mercado
from shadow_resolve import fetch_mercados_paralelo

import analisis_ballenas_dosis_respuesta_16jul as base

STAKE_EUR_REF = 1.05
COMBOS = ["BTC#5m", "ETH#5m", "SOL#5m", "XRP#5m"]


def analizar_combo(combo: str, bandas: dict, mapa_cid_mid: dict, muestra_max: int):
    if combo not in bandas:
        print(f"\n=== {combo}: no significativo, saltando ===")
        return
    lo, hi, rest_lo, rest_hi = bandas[combo]
    base.COMBOS = [combo]
    seleccion = base.muestrear_mercados(bandas)
    cids = seleccion.get(combo, [])[:muestra_max]
    print(f"\n=== {combo}: banda=[{lo},{hi}) ventana=[{rest_lo:.2f},{rest_hi:.2f}]min | "
          f"muestra {len(cids)} mercados ===")

    tamanos_usd = []
    profundidad_por_mercado = []
    n_procesados = 0
    n_con_trade = 0

    for cid in cids:
        mid = mapa_cid_mid.get(cid)
        if mid is None:
            continue
        resueltos = fetch_mercados_paralelo([mid], workers=1)
        mercado = resueltos.get(mid)
        if not mercado:
            continue
        try:
            end_dt = datetime.fromisoformat(mercado.get("endDate", "").replace("Z", "+00:00"))
            if end_dt.tzinfo is None:
                end_dt = end_dt.replace(tzinfo=timezone.utc)
        except Exception:
            continue
        n_procesados += 1

        trades = trades_de_mercado(cid)
        usd_mercado = 0.0
        n_trade = 0
        for t in trades:
            if (t.get("side") or "").strip().upper() != "BUY":
                continue
            precio_t, outcome_t, ts, size_t = (t.get("price"), (t.get("outcome") or "").strip().lower(),
                                                t.get("timestamp"), t.get("size"))
            if precio_t is None or outcome_t not in ("up", "down", "yes", "no") or ts is None:
                continue
            try:
                precio_t = float(precio_t)
                t_dt = datetime.fromtimestamp(float(ts), tz=timezone.utc)
                size_t = float(size_t or 0)
            except (ValueError, TypeError, OSError):
                continue
            restante_min = (end_dt - t_dt).total_seconds() / 60.0
            if not (lo <= precio_t < hi) or not (rest_lo <= restante_min <= rest_hi):
                continue
            usd = size_t * precio_t
            if usd <= 0:
                continue
            tamanos_usd.append(usd)
            usd_mercado += usd
            n_trade += 1
        if n_trade > 0:
            n_con_trade += 1
            profundidad_por_mercado.append(round(usd_mercado, 2))

    print(f"  procesados={n_procesados} con>=1 trade en banda+ventana={n_con_trade}")
    if not tamanos_usd:
        print("  sin trades con dato completo -- no se puede concluir.")
        return
    tamanos_usd.sort()
    n = len(tamanos_usd)
    def pct(p): return tamanos_usd[int(n * p)]
    print(f"  tamaño trade individual USD n={n}: min={tamanos_usd[0]:.2f} mediana={pct(0.5):.2f} "
          f"p90={pct(0.9):.2f} max={tamanos_usd[-1]:.2f}")
    profundidad_por_mercado.sort()
    nm = len(profundidad_por_mercado)
    ratio = [u / STAKE_EUR_REF for u in profundidad_por_mercado]
    n_bajo5x = sum(1 for r in ratio if r < 5.0)
    print(f"  profundidad TOTAL/mercado USD n={nm}: min={profundidad_por_mercado[0]:.2f} "
          f"mediana={profundidad_por_mercado[nm//2]:.2f} max={profundidad_por_mercado[-1]:.2f}")
    print(f"  mercados con profundidad<5x stake({STAKE_EUR_REF}€): {n_bajo5x}/{nm} ({n_bajo5x/nm*100:.1f}%)")


def main():
    muestra_max = int(sys.argv[1]) if len(sys.argv) > 1 else 15
    base.COMBOS = COMBOS
    bandas = base.cargar_bandas()
    mapa_cid_mid = base.mapear_condition_a_market()
    print(f"mapa condition_id->market_id: {len(mapa_cid_mid)} conocidos")
    for combo in COMBOS:
        analizar_combo(combo, bandas, mapa_cid_mid, muestra_max)


if __name__ == "__main__":
    sys.exit(main() or 0)
