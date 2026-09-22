#!/usr/bin/env python3
"""perps_rastreador_posiciones.py -- (22-Sep, PLAN 22-Sep paso 1, ver memoria
project_perps_estado_y_plan_22sep). MODO LECTURA, solo agregación de datos ya
capturados por fetch_polymarket_perps_wallet_fills.py.

## Problema que resuelve
El hallazgo decisivo del 21-Sep: contar FILAS de fills como si fueran
operaciones independientes es el mismo error ya diagnosticado para SNIPER
(ver project_lecciones_aprendidas_estrategias) -- 72.900 fills = solo 201
APERTURAS de posición real. Un wallet con una sola posición grande vendida
en 2.000 trozos (0x0034 NEAR-LONG) cuenta como n=1 operación independiente,
no n=2.000. Este script reconstruye la POSICIÓN (apertura -> cierre) como
unidad estadística, no el fill.

## Semántica de los datos (leída del CSV real, `previous_size` es el campo
ground-truth -- tamaño de la posición ANTES de este fill, según la API)
Para cada (address, instrument_id), ordenado por fill_timestamp_utc:
  - Un fill con previous_size == 0 (con tolerancia float) ABRE una posición
    nueva (o reabre tras haber cerrado del todo).
  - Todos los fills siguientes pertenecen a la MISMA posición hasta el
    fill anterior al próximo previous_size == 0 (o hasta el final de los
    datos si la posición sigue abierta -- se marca `abierta=True`, no se
    usa en el gate, mismo criterio fail-closed que el resto del proyecto).
  - pnl de la posición = suma de `pnl` de todos sus fills (cada fill trae
    su pnl realizado en el momento, 0 mientras la posición solo crece).
⚠️ Asunción NO verificada más allá del propio dato (documentarlo, no
ocultarlo): se asume que `previous_size == 0` es un ground-truth fiable de
"posición plana antes de este fill" tal y como lo devuelve la API de
Polymarket Perps -- no hay forma de verificarlo de forma independiente sin
la cuenta propia. Sanity check en main(): el nº de aperturas debe rondar el
mismo orden de magnitud que el hallazgo manual del 21-Sep (~201 en 13 días
de 05-18 Sep) -- si diverge mucho, hay que revisar el supuesto antes de
confiar en la salida.

## Salida
data/shadow/perps_posiciones.csv -- una fila por posición (wallet,
instrumento, ts_apertura, ts_cierre, lado, n_fills, pnl_total, abierta).
Es la población que gate_dias_independientes-style / forward rodante debe
usar para Perps -- NUNCA los fills crudos.
"""
import csv
import glob
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
GLOB_IN = str(REPO / "data/shadow/polymarket_perps_wallet_fills_*.csv")
OUT = REPO / "data/shadow/perps_posiciones.csv"

TOL = 1e-6


def cargar_fills() -> dict:
    """(address, instrument_id) -> [(fill_ts, side, price, qty, previous_size,
    pnl, symbol), ...] ordenado por fill_ts. Dedup por trade_id (los ficheros
    diarios se solapan en el borde de medianoche -- el fetcher los reescribe
    con overlap deliberado, ver docstring de fetch_polymarket_perps_wallet_fills.py)."""
    grupos = defaultdict(list)
    vistos = set()
    for arch in sorted(glob.glob(GLOB_IN)):
        with open(arch, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                tid = r.get("trade_id", "")
                if tid and tid in vistos:
                    continue
                if tid:
                    vistos.add(tid)
                try:
                    qty = float(r["quantity"])
                    prev = float(r["previous_size"])
                    pnl = float(r.get("pnl") or 0)
                except (KeyError, ValueError, TypeError):
                    continue
                clave = (r["address"], r["instrument_id"])
                grupos[clave].append((r["fill_timestamp_utc"], r.get("side", ""),
                                      float(r.get("price") or 0), qty, prev, pnl,
                                      r.get("symbol", "")))
    for clave in grupos:
        grupos[clave].sort(key=lambda x: x[0])
    return grupos


def segmentar_posiciones(fills: list) -> list:
    """fills: lista ordenada de un (address,instrument_id). Devuelve lista de
    posiciones: {ts_apertura, ts_cierre, lado_apertura, n_fills, pnl_total, abierta}."""
    posiciones = []
    actual = None
    for ts, side, price, qty, prev, pnl, symbol in fills:
        if abs(prev) <= TOL:
            if actual is not None:
                posiciones.append(actual)
            actual = {"ts_apertura": ts, "ts_cierre": ts, "lado_apertura": side,
                      "symbol": symbol, "n_fills": 0, "pnl_total": 0.0}
        if actual is None:
            # primer fill del historico para este wallet/instrumento ya con
            # posicion abierta (previous_size>0) -- no hay apertura visible en
            # los datos capturados, se descarta (no es una posicion completa).
            continue
        actual["n_fills"] += 1
        actual["pnl_total"] += pnl
        actual["ts_cierre"] = ts
    if actual is not None:
        actual["abierta"] = True  # sigue abierta al final de los datos capturados
        posiciones.append(actual)
    for p in posiciones:
        p.setdefault("abierta", False)
    return posiciones


def main() -> int:
    grupos = cargar_fills()
    print(f"[perps_rastreador_posiciones] {len(grupos)} pares (wallet,instrumento) con fills")

    filas_out = []
    n_aperturas_cerradas = 0
    for (address, instrument_id), fills in grupos.items():
        for p in segmentar_posiciones(fills):
            filas_out.append({
                "address": address, "instrument_id": instrument_id, "symbol": p["symbol"],
                "ts_apertura": p["ts_apertura"], "ts_cierre": p["ts_cierre"],
                "lado_apertura": p["lado_apertura"], "n_fills": p["n_fills"],
                "pnl_total": round(p["pnl_total"], 6), "abierta": p["abierta"],
            })
            if not p["abierta"]:
                n_aperturas_cerradas += 1

    n_abiertas = sum(1 for f in filas_out if f["abierta"])
    print(f"[perps_rastreador_posiciones] {len(filas_out)} posiciones totales "
          f"({n_aperturas_cerradas} cerradas, {n_abiertas} siguen abiertas)")
    print("[perps_rastreador_posiciones] ⚠️ sanity check: el hallazgo manual del 21-Sep "
          "contó ~201 aperturas en 05-18 Sep (13 días) -- si esta cifra diverge mucho "
          "en orden de magnitud, revisar el supuesto de previous_size==0 antes de usar "
          "esta salida para nada.")

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["address", "instrument_id", "symbol",
                                          "ts_apertura", "ts_cierre", "lado_apertura",
                                          "n_fills", "pnl_total", "abierta"])
        w.writeheader()
        w.writerows(filas_out)
    print(f"[perps_rastreador_posiciones] guardado en {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
