#!/usr/bin/env python3
"""
Análisis de timing: ¿cuándo entran las wallets 'smart' (P16) en mercados
Up/Down de 15min, comparado con nuestro sistema (GBM_LATE_15M, mediana
restante_min=10.6)? Motivado por 2 hipótesis de ejecución refutadas el
14-Jul (refrescar precio_yes_mercado, subir umbral de edge) — ver memoria
idea_timing_wallets_smart_vs_sistema_14jul.

Reutiliza:
  - wallet_pnl_diario.fetch_activity() — /activity real de cada wallet
  - shadow_resolve.fetch_mercados_paralelo()/parse_outcome_prices() —
    resolución OFICIAL vía gamma-api, no un proxy de precio

Mapeo condition_id->market_id: /tmp/cond_market_map.csv (generado con
`cut -d',' -f2,3 data/markets/*.csv | sort -u`, seguro porque market_id y
condition_id van antes de cualquier coma incrustada en 'question').

Puramente análisis/shadow — no toca live_trade.py/config_live.json.
Uso: python3 analisis_timing_wallets_smart.py [--n-wallets 25] [--max-events 500]
"""
import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

from wallet_pnl_diario import fetch_activity
from shadow_resolve import fetch_mercados_paralelo, parse_outcome_prices

DIR = Path(__file__).parent
SMART_WALLETS = DIR / "data/shadow/smart_money_wallets.json"
COND_MAP = Path("/tmp/cond_market_map.csv")
PATRON_VENTANA = re.compile(r"(\d{1,2}):(\d{2})(AM|PM)-(\d{1,2}):(\d{2})(AM|PM) ET")


def parse_dt(s: str) -> datetime:
    dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def duracion_ventana_min(title: str) -> int | None:
    m = PATRON_VENTANA.search(title or "")
    if not m:
        return None
    h1, m1, ap1, h2, m2, ap2 = m.groups()
    t1 = int(h1) % 12 + (12 if ap1 == "PM" else 0)
    t2 = int(h2) % 12 + (12 if ap2 == "PM" else 0)
    dur = (t2 * 60 + int(m2)) - (t1 * 60 + int(m1))
    if dur < 0:
        dur += 24 * 60
    return dur


def cargar_top_wallets_smart(n: int) -> list[str]:
    data = json.loads(SMART_WALLETS.read_text())
    smart = [(k, v) for k, v in data.items()
             if v.get("clasificacion") == "smart" and (v.get("n") or 0) > 0]
    smart.sort(key=lambda kv: -(kv[1].get("pnl_total") or 0))
    return [k for k, _ in smart[:n]]


def cargar_cond_market_map() -> dict:
    mapa = {}
    if not COND_MAP.exists():
        print(f"  ⚠️ {COND_MAP} no existe — generar con:\n"
              f"     for f in data/markets/2026-07-*.csv; do cut -d',' -f2,3 \"$f\"; done "
              f"| sort -u -t',' -k2,2 > {COND_MAP}")
        return mapa
    with open(COND_MAP, newline="", encoding="utf-8") as f:
        for line in f:
            parts = line.rstrip("\n").split(",")
            if len(parts) != 2:
                continue
            mid, cid = parts
            if mid and cid and mid != "market_id":
                mapa[cid] = mid
    return mapa


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-wallets", type=int, default=25)
    ap.add_argument("--max-events", type=int, default=500)
    args = ap.parse_args()

    wallets = cargar_top_wallets_smart(args.n_wallets)
    print(f"Wallets smart seleccionadas: {len(wallets)}")

    cond_to_market = cargar_cond_market_map()
    print(f"Mapeo condition_id->market_id: {len(cond_to_market)} entradas")

    # 1. Recolectar trades BUY en ventanas Up/Down de 15min
    trades_15m = []
    for i, w in enumerate(wallets):
        evs = fetch_activity(w, max_events=args.max_events)
        n_trades = 0
        for e in evs:
            if e.get("type") != "TRADE" or e.get("side") != "BUY":
                continue
            title = e.get("title", "")
            if duracion_ventana_min(title) != 15:
                continue
            if "up or down" not in title.lower():
                continue
            trades_15m.append(e)
            n_trades += 1
        print(f"  [{i+1}/{len(wallets)}] {w[:12]}...: {n_trades} trades 15min de {len(evs)} eventos")

    print(f"\nTotal trades BUY en ventanas 15min: {len(trades_15m)}")

    # 2. Mercados únicos a resolver (vía market_id, no condition_id)
    market_ids_necesarios = set()
    for t in trades_15m:
        cid = t.get("conditionId", "")
        mid = cond_to_market.get(cid)
        if mid:
            market_ids_necesarios.add(mid)
    print(f"Mercados únicos a resolver: {len(market_ids_necesarios)}")

    print("Consultando resolución oficial (gamma-api, throttled 3 workers)...")
    resueltos = fetch_mercados_paralelo(list(market_ids_necesarios), workers=3)
    n_ok = sum(1 for v in resueltos.values() if v)
    print(f"Mercados con respuesta: {n_ok}/{len(market_ids_necesarios)}")

    # 3. Determinar outcome_real por mercado (YES/NO, señal primaria outcomePrices)
    outcome_por_market = {}
    for mid, mercado in resueltos.items():
        if not mercado:
            continue
        precios = parse_outcome_prices(mercado.get("outcomePrices"))
        if not precios or len(precios) < 2:
            continue
        try:
            py, pn = float(precios[0]), float(precios[1])
        except (ValueError, TypeError):
            continue
        if abs(py - 1.0) < 0.01:
            outcome_por_market[mid] = "YES"
        elif abs(pn - 1.0) < 0.01:
            outcome_por_market[mid] = "NO"
        # si no está liquidado (~0.5/0.5 o similar), se descarta — no hay resolución fiable

    print(f"Mercados con outcome_real determinado: {len(outcome_por_market)}")

    # 4. Cruzar cada trade con outcome + restante_min al momento del trade
    resultados = []  # (restante_min, precio, acierto)
    end_dates_cache = {}
    for t in trades_15m:
        cid = t.get("conditionId", "")
        mid = cond_to_market.get(cid)
        if not mid or mid not in outcome_por_market:
            continue
        mercado = resueltos[mid]
        end_str = mercado.get("endDate", "")
        if not end_str:
            continue
        try:
            end_dt = parse_dt(end_str)
            t_dt = datetime.fromtimestamp(t["timestamp"], tz=timezone.utc)
            restante_min = (end_dt - t_dt).total_seconds() / 60
            precio = float(t.get("price", 0))
        except Exception:
            continue
        if not (-2 <= restante_min <= 16):
            continue
        outcome_idx = t.get("outcomeIndex")
        compro_yes = (outcome_idx == 0)
        outcome_real = outcome_por_market[mid]
        acierto = (compro_yes and outcome_real == "YES") or (not compro_yes and outcome_real == "NO")
        resultados.append((restante_min, precio, acierto))

    print(f"\nTrades con resolución real + timing válido: {len(resultados)}")
    if len(resultados) < 40:
        print("⚠️  n<40 — NO SUFICIENTE para concluir nada (umbral estándar del proyecto). "
              "Ampliar --n-wallets o --max-events.")

    # 5. Estadísticas: global + por zona (tardía 0-7min vs temprana 8-15min)
    def stats(nombre, rs):
        n = len(rs)
        if n == 0:
            print(f"  {nombre}: n=0")
            return
        hit = sum(1 for r, p, a in rs if a) / n * 100
        precio_medio = sum(p for r, p, a in rs) / n
        ev = sum((1 - p if a else -p) for r, p, a in rs) / n
        print(f"  {nombre}: n={n} hit={hit:.1f}% precio_medio={precio_medio:.3f} EV/1USD={ev:+.3f}")

    print("\n=== RESULTADOS (n>=40 requerido para concluir) ===")
    stats("TODOS", resultados)
    stats("Zona tardía (restante 0-7min, donde concentran volumen)",
          [r for r in resultados if r[0] <= 7])
    stats("Zona temprana (restante 8-15min)",
          [r for r in resultados if r[0] > 7])

    # Distribución de timing (comparar contra mediana 10.6min de nuestro sistema)
    restantes = sorted(r for r, p, a in resultados)
    if restantes:
        n = len(restantes)
        print(f"\nMediana restante_min (wallets smart): {restantes[n//2]:.1f} "
              f"(nuestro sistema GBM_LATE_15M: 10.6)")


if __name__ == "__main__":
    sys.exit(main() or 0)
