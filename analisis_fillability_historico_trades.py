#!/usr/bin/env python3
"""
analisis_fillability_historico_trades.py — proxy de fill-ability usando
TRADES REALES de otros traders (data-api.polymarket.com/trades) en vez de
nuestro propio libro_snapshots.csv.

Motivo (idea de Javi, 28-Jul): libro_snapshots.csv solo captura profundidad
de libro cuando NOSOTROS disparamos una señal real -- para tuplas con pocos
o cero trades reales (ej. BALLENAS_TARDIAS#BTC#15min, 0 trades en 11 días),
el fill-ability medido así tiene n≈0, no porque el mercado sea realmente
ilíquido sino porque casi nunca hemos intentado ejecutar ahí. Verificado
28-Jul: data-api.polymarket.com/trades SÍ conserva histórico completo (un
mercado resuelto hace 1 mes exacto devolvió 278 trades reales con
precio/tamaño/lado/timestamp intactos).

Metodología (proxy, NO una medición directa de profundidad de libro):
para cada señal histórica ya logueada en predictions_*.csv, se resuelve
market_id->condition_id (market_id_resolver.py, cacheado) y se piden los
trades reales de ese mercado. Si hay volumen real comprado en el lado YES
a precio <= nuestro precio objetivo + tolerancia, DENTRO de la ventana
[momento de la señal, cierre del mercado], eso es evidencia de que un
comprador real consiguió que le llenaran ahí -- proxy razonable de que
nuestra propia orden marketable del mismo tamaño también se habría
llenado. No es lo mismo que ver la profundidad de libro en el instante
exacto (eso solo lo sabemos si lo capturamos en vivo), pero da MUCHO más
n que depender de nuestros propios intentos reales.

Solo lectura -- no toca config_live.json ni decide nada. Rate-limit
amable con la API (backoff simple, cache de condition_id ya lo trae
market_id_resolver.py).
"""
import csv
import glob
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from market_id_resolver import resolver

DATA_API = "https://data-api.polymarket.com"
TOLERANCIA_PRECIO = 0.02   # comprar YES hasta 2c por encima de nuestro precio objetivo cuenta como "mismo precio"
STAKE_REFERENCIA_USD = 3.0  # ~3x el stake típico (1.05-2€) -- volumen real por debajo de esto no es concluyente
TIMEOUT = 15


def _cargar_senales(strategy: str, subtype: str, decision: str) -> list[dict]:
    filas = []
    for f in sorted(glob.glob(str(REPO / "data/shadow/predictions_2026-*.csv"))):
        try:
            with open(f, encoding="utf-8") as fh:
                for row in csv.DictReader(fh):
                    if (row.get("strategy") == strategy and row.get("subtype") == subtype
                            and row.get("decision") == decision):
                        filas.append(row)
        except Exception:
            continue
    # una señal puede reintentar varias veces (cada ~20s) -- quedarnos con
    # la primera aparición por market_id, igual que analisis_fills.py hace
    # con libro_snapshots.csv (CLAUDE.md 3b: no contar reintentos como señales)
    vistos = {}
    for row in filas:
        mid = row.get("market_id")
        if mid not in vistos or row["timestamp_utc"] < vistos[mid]["timestamp_utc"]:
            vistos[mid] = row
    return list(vistos.values())


def _trades_de_mercado(condition_id: str) -> list:
    try:
        r = requests.get(f"{DATA_API}/trades", params={"market": condition_id, "limit": 2000},
                         timeout=TIMEOUT)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"    ⚠️ error /trades {condition_id}: {e}")
        return []


def _parse_ts(s: str) -> float | None:
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()
    except Exception:
        return None


def evaluar_tupla(strategy: str, subtype: str, decision: str):
    senales = _cargar_senales(strategy, subtype, decision)
    print(f"{strategy}#{subtype}#{decision}: {len(senales)} señales únicas (por market_id)")
    resultados = []
    for i, row in enumerate(senales):
        mid = row["market_id"]
        ts_senal = _parse_ts(row["timestamp_utc"])
        ts_cierre = _parse_ts(row["end_date"])
        try:
            precio_obj = float(row["precio_yes_mercado"])
        except (KeyError, ValueError, TypeError):
            continue
        if ts_senal is None or ts_cierre is None:
            continue

        cid = resolver(mid)
        if not cid:
            resultados.append({"market_id": mid, "estado": "sin_condition_id"})
            continue

        trades = _trades_de_mercado(cid)
        time.sleep(0.15)  # amable con la API, 47 mercados no necesita más

        vol_yes_a_precio = 0.0
        n_trades_relevantes = 0
        for t in trades:
            ts_t = t.get("timestamp")
            if ts_t is None or not (ts_senal <= float(ts_t) <= ts_cierre + 5):
                continue
            outcome = (t.get("outcome") or "").strip().lower()
            es_yes = outcome in ("up", "yes")
            if not es_yes:
                continue
            try:
                precio_t = float(t.get("price", 0))
                size_t = float(t.get("size", 0))
            except (TypeError, ValueError):
                continue
            if precio_t <= precio_obj + TOLERANCIA_PRECIO:
                vol_yes_a_precio += precio_t * size_t
                n_trades_relevantes += 1

        fillable = vol_yes_a_precio >= STAKE_REFERENCIA_USD
        resultados.append({
            "market_id": mid, "precio_objetivo": precio_obj,
            "vol_usd_yes_a_precio": round(vol_yes_a_precio, 2),
            "n_trades_relevantes": n_trades_relevantes,
            "fillable_proxy": fillable, "n_trades_totales_mercado": len(trades),
        })
        estado = "✅ fillable" if fillable else ("〜 mercado con trades pero sin vol suficiente" if trades else "🔴 sin trades en absoluto")
        print(f"  [{i+1}/{len(senales)}] mid={mid} precio_obj={precio_obj:.3f} "
              f"vol_yes_relevante=${vol_yes_a_precio:.2f} ({n_trades_relevantes} trades) -- {estado}")

    validos = [r for r in resultados if "fillable_proxy" in r]
    n_fillable = sum(1 for r in validos if r["fillable_proxy"])
    n_total = len(validos)
    print()
    print(f"RESUMEN {strategy}#{subtype}#{decision}: {n_fillable}/{n_total} fillable_proxy "
          f"({n_fillable/n_total*100:.1f}%)" if n_total else "sin datos válidos")
    return resultados


if __name__ == "__main__":
    strategy, subtype, decision = sys.argv[1:4] if len(sys.argv) > 3 else \
        ("BALLENAS_TARDIAS", "BTC#15min", "BUY_YES")
    resultados = evaluar_tupla(strategy, subtype, decision)
    out = REPO / f"data/shadow/fillability_historico_{strategy}_{subtype.replace('#','_')}_{decision}.json"
    out.write_text(json.dumps(resultados, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Guardado en {out}")
