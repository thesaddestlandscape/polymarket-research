#!/usr/bin/env python3
"""Resolución persistente market_id -> condition_id (P26, 2026-07-27).

Motivación: varios análisis de esta sesión (backtests de anchura/volumen,
fill-ability de BALLENAS_CONFIRMADAS_15M) necesitaron resolver miles de
market_id -> condition_id vía gamma-api, uno a uno, cada vez desde cero.
Pero `data/markets/*.csv` (snapshots del scanner de mercados, cron slow)
YA trae ambas columnas para casi todo lo que alguna vez fue un mercado
activo en nuestro universo -- no hace falta red para eso. Solo lo que
nunca pasó por el scanner (mercados muy viejos, o resueltos entre dos
ciclos del slow loop) necesita gamma-api.

Uso:
    python3 market_id_resolver.py --build     # (re)construye el índice
                                                 desde data/markets/*.csv
    python3 market_id_resolver.py --stats     # tamaño del índice actual

Como librería:
    from market_id_resolver import resolver, resolver_lote
    cid = resolver("1068702")                  # usa índice, cae a API si falta
    mapa = resolver_lote(["1068702", "691547"]) # dict market_id -> condition_id
"""
import argparse
import glob
import json
import os
import sys
import time

import pandas as pd
import requests

BASE = os.path.dirname(os.path.abspath(__file__))
MARKETS_GLOB = os.path.join(BASE, "data", "markets", "*.csv")
INDEX_PATH = os.path.join(BASE, "data", "shadow", "market_id_condition_id_map.json")
GAMMA_API = "https://gamma-api.polymarket.com"
TIMEOUT = 8


def construir_indice_desde_csv() -> dict:
    """Escanea todo data/markets/*.csv una vez y construye {market_id: condition_id}.
    Tolerante a archivos con esquema viejo sin columna condition_id (16/17-jun,
    antes de que el scanner la incluyera)."""
    mapa = {}
    for path in sorted(glob.glob(MARKETS_GLOB)):
        try:
            df = pd.read_csv(path, usecols=["market_id", "condition_id"], dtype=str)
        except ValueError:
            continue  # esquema viejo sin condition_id -- se salta, no rompe el resto
        except Exception as e:
            print(f"  [warn] {path}: {e}", file=sys.stderr)
            continue
        df = df.dropna(subset=["market_id", "condition_id"])
        mapa.update(dict(zip(df["market_id"], df["condition_id"])))
    return mapa


def _cargar_indice() -> dict:
    try:
        with open(INDEX_PATH) as f:
            return json.load(f)
    except Exception:
        return {}


def _guardar_indice(mapa: dict) -> None:
    tmp = INDEX_PATH + ".tmp"
    with open(tmp, "w") as f:
        json.dump(mapa, f)
    os.replace(tmp, INDEX_PATH)


def _resolver_via_api(market_id: str) -> str | None:
    try:
        r = requests.get(f"{GAMMA_API}/markets/{market_id}", timeout=TIMEOUT)
        if r.status_code != 200:
            return None
        data = r.json()
        if isinstance(data, list):
            data = data[0] if data else {}
        return data.get("conditionId")
    except Exception:
        return None


def resolver(market_id: str, usar_api_fallback: bool = True) -> str | None:
    """Resuelve un solo market_id. Persiste en el índice cualquier
    resolución nueva (vía CSV o API) para que la próxima llamada sea
    gratis."""
    mapa = _cargar_indice()
    market_id = str(market_id)
    if market_id in mapa:
        return mapa[market_id] or None
    if usar_api_fallback:
        cid = _resolver_via_api(market_id)
        mapa[market_id] = cid
        _guardar_indice(mapa)
        return cid
    return None


def resolver_lote(market_ids: list[str], usar_api_fallback: bool = True,
                   sleep_entre_llamadas: float = 0.15) -> dict:
    """Resuelve una lista de market_id, minimizando llamadas de red: primero
    contra el índice persistido, luego (opcional) vía API solo para los que
    falten. Devuelve {market_id: condition_id o None}."""
    mapa = _cargar_indice()
    resultado = {}
    faltan = []
    for mid in market_ids:
        mid = str(mid)
        if mid in mapa:
            resultado[mid] = mapa[mid]
        else:
            faltan.append(mid)

    if faltan and usar_api_fallback:
        for i, mid in enumerate(faltan):
            cid = _resolver_via_api(mid)
            mapa[mid] = cid
            resultado[mid] = cid
            if sleep_entre_llamadas:
                time.sleep(sleep_entre_llamadas)
            if (i + 1) % 200 == 0:
                _guardar_indice(mapa)  # checkpoint periódico en lotes largos
        _guardar_indice(mapa)
    elif faltan:
        for mid in faltan:
            resultado[mid] = None

    return resultado


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true",
                     help="(re)construye el índice desde data/markets/*.csv y "
                          "lo fusiona con lo ya persistido (nunca borra resoluciones vía API)")
    ap.add_argument("--stats", action="store_true", help="muestra el tamaño del índice actual")
    args = ap.parse_args()

    if args.build:
        existente = _cargar_indice()
        nuevo = construir_indice_desde_csv()
        antes = len(existente)
        existente.update(nuevo)  # el CSV es autoridad más fresca que una resolución API vieja
        _guardar_indice(existente)
        print(f"Índice reconstruido: {antes} entradas antes -> {len(existente)} después "
              f"({len(nuevo)} pares vistos en data/markets/*.csv)")
    elif args.stats:
        mapa = _cargar_indice()
        con_valor = sum(1 for v in mapa.values() if v)
        print(f"Índice: {len(mapa)} market_id conocidos, {con_valor} con condition_id real "
              f"({len(mapa) - con_valor} resueltos como None -- mercado no encontrado)")
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
