#!/usr/bin/env python3
"""Read-only, one-off (16-Jul, petición Javi): en vez de esperar días
construyendo un vigía en vivo para BTC#15min (Fase 1 propuesta), responder
la pregunta de viabilidad con la MUESTRA que ya tenemos — los propios
trades reales de ballenas dentro de la ventana degenerada [0.07,0.53]min.

Un trade de ballena EJECUTADO a un precio dentro de la banda [0.7,0.9) en
ese instante es evidencia directa de que el libro SÍ tenía profundidad
fillable en ese momento (alguien compró ahí de verdad) — no hace falta
esperar a loguear nuestro propio intento. Este script re-pide /trades
para la misma muestra de mercados BTC#15m que
analisis_ballenas_dosis_respuesta_16jul.py, pero en vez de mirar
"quién acertó", mide `size` (acciones) × `price` = profundidad real
consumida en USD por cada trade dentro de banda+ventana — proxy directo
de si nuestro stake (~1.05-2€) habría cabido.

20-Jul: generalizado a cualquier combo activo#marco (antes hardcodeado a
BTC#15m) para responder la misma pregunta sobre ETH/SOL/XRP#15m antes de
plantear extender ballenas_executor_btc15m.py — mismo método exacto,
solo parametrizado, sin duplicar el fichero. Sin argumento se comporta
igual que el 16-Jul (BTC#15m), para no romper el uso histórico.

Uso: python3 analisis_ballenas_btc15m_fillability_retro_16jul.py [COMBO]
     (COMBO por defecto: BTC#15m — ej. ETH#15m, SOL#15m, XRP#15m)
"""
import sys
from pathlib import Path

from smart_money_tracker import trades_de_mercado
from shadow_resolve import fetch_mercados_paralelo, parse_outcome_prices

import analisis_ballenas_dosis_respuesta_16jul as base

DIR = Path(__file__).parent
STAKE_EUR_REF = 1.05  # suelo de stake real vigente hoy (config_live.json)


def main():
    combo = sys.argv[1] if len(sys.argv) > 1 else "BTC#15m"
    base.COMBOS = [combo]
    bandas = base.cargar_bandas()
    print(f"Banda {combo}: {bandas}")
    if combo not in bandas:
        print(f"{combo} no está marcado 'significativo' en ballenas_timing_state.json — nada que analizar.")
        return

    lo, hi, rest_lo, rest_hi = bandas[combo]
    seleccion = base.muestrear_mercados(bandas)
    cids = seleccion.get(combo, [])
    print(f"Muestra {combo} con >=3 trades históricos en banda+ventana: {len(cids)} mercados")

    mapa_cid_mid = base.mapear_condition_a_market()
    print(f"  mapa: {len(mapa_cid_mid)} condition_id conocidos")

    tamanos_usd = []      # cada trade individual dentro de banda+ventana (cualquier wallet)
    profundidad_por_mercado = []  # suma USD por mercado (cuánto volumen total pasó por ahí)
    n_mercados_con_trade = 0
    n_mercados_procesados = 0

    for i, cid in enumerate(cids):
        mid = mapa_cid_mid.get(cid)
        if mid is None:
            continue
        resueltos = fetch_mercados_paralelo([mid], workers=1)
        mercado = resueltos.get(mid)
        if not mercado:
            continue
        end_str = mercado.get("endDate", "")
        try:
            from datetime import datetime, timezone
            end_dt = datetime.fromisoformat(end_str.replace("Z", "+00:00"))
            if end_dt.tzinfo is None:
                end_dt = end_dt.replace(tzinfo=timezone.utc)
        except Exception:
            continue
        n_mercados_procesados += 1

        trades = trades_de_mercado(cid)
        usd_mercado = 0.0
        n_trade_mercado = 0
        for t in trades:
            if (t.get("side") or "").strip().upper() != "BUY":
                continue
            precio_t = t.get("price")
            outcome_t = (t.get("outcome") or "").strip().lower()
            ts = t.get("timestamp")
            size_t = t.get("size")
            if precio_t is None or outcome_t not in ("up", "down", "yes", "no") or ts is None:
                continue
            try:
                precio_t = float(precio_t)
                from datetime import datetime, timezone
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
            n_trade_mercado += 1
        if n_trade_mercado > 0:
            n_mercados_con_trade += 1
            profundidad_por_mercado.append((cid, n_trade_mercado, round(usd_mercado, 2)))
        if (i + 1) % 20 == 0:
            print(f"  {i+1}/{len(cids)} procesados...")

    print(f"\nMercados procesados: {n_mercados_procesados}, con >=1 trade real en banda+ventana: {n_mercados_con_trade}")
    if not tamanos_usd:
        print("Sin trades con dato completo (size+timestamp) — no se puede concluir.")
        return

    tamanos_usd.sort()
    n = len(tamanos_usd)
    def pct(p):
        return tamanos_usd[int(n * p)] if n else 0
    print(f"\nTamaño individual de cada trade de ballena en banda+ventana (USD), n={n}:")
    print(f"  min={tamanos_usd[0]:.2f}  p10={pct(0.10):.2f}  mediana={pct(0.50):.2f}  p90={pct(0.90):.2f}  max={tamanos_usd[-1]:.2f}")
    n_bajo_stake = sum(1 for u in tamanos_usd if u < STAKE_EUR_REF)
    print(f"  trades por debajo de nuestro stake ({STAKE_EUR_REF}€): {n_bajo_stake}/{n} ({n_bajo_stake/n*100:.1f}%)")

    print(f"\nProfundidad TOTAL por mercado (suma de todos los trades en banda+ventana), n_mercados={len(profundidad_por_mercado)}:")
    usds_mercado = sorted(u for _, _, u in profundidad_por_mercado)
    nm = len(usds_mercado)
    print(f"  min={usds_mercado[0]:.2f}  mediana={usds_mercado[nm//2]:.2f}  max={usds_mercado[-1]:.2f}")
    ratio_vs_stake = [u / STAKE_EUR_REF for u in usds_mercado]
    n_ratio_bajo = sum(1 for r in ratio_vs_stake if r < 5.0)  # mismo umbral que min_profundidad_ratio_libro
    print(f"  mercados con profundidad total < 5x nuestro stake: {n_ratio_bajo}/{nm} ({n_ratio_bajo/nm*100:.1f}%)")

    print(f"\nConclusión: {n_mercados_con_trade}/{n_mercados_procesados} mercados tuvieron AL MENOS un trade real "
          f"ejecutado dentro de la banda+ventana degenerada -- eso ya prueba que el libro SÍ tuvo profundidad "
          f"fillable en ese instante exacto para al menos ese tamaño. La pregunta que esto NO responde es "
          f"latencia (¿nuestro pipeline puede reaccionar en <32s reales?), solo la pregunta de PROFUNDIDAD.")


if __name__ == "__main__":
    sys.exit(main() or 0)
