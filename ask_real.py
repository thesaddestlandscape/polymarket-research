#!/usr/bin/env python3
"""ask_real.py -- lector compartido del ASK REAL por señal (24-Sep, Javi: "que cuente el ask real").

Fuente única: data/shadow/ask_real_por_senal.csv, generado a diario por ask_real_por_senal.py (ver
su docstring: ask del token propio justo DESPUÉS de la señal, primera señal por
strategy+market_id+decision, últimos 21 días, marcos 5/15/60min). Lo usan
analisis_kelly_precio_gate_29jul.py y analisis_log_growth.py para medir con el precio al que de
verdad se entra, no con precio_yes_mercado (precio de la señal, desfasado).

cargar_mapa() -> {(strategy, market_id, decision): ask} o None si el fichero falta, está corrupto o
tiene más de MAX_ANTIGUEDAD_S (el llamante debe ser fail-closed: sin mapa no se calcula nada con
el precio desfasado). El ask ya es el precio del token de la decisión (no hay que invertirlo para
BUY_NO).
"""
import csv
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent
PATH = REPO / "data" / "shadow" / "ask_real_por_senal.csv"
MAX_ANTIGUEDAD_S = 36 * 3600
FEE = 0.07
_cache = {"mtime": None, "mapa": None}


def cargar_mapa():
    try:
        mtime = PATH.stat().st_mtime
    except OSError:
        return None
    if time.time() - mtime > MAX_ANTIGUEDAD_S:
        return None
    if _cache["mtime"] != mtime:
        mapa = {}
        try:
            with open(PATH, encoding="utf-8", newline="") as f:
                for r in csv.DictReader(f):
                    if r.get("ask"):
                        try:
                            mapa[(r["strategy"], r["market_id"], r["decision"])] = float(r["ask"])
                        except (ValueError, KeyError):
                            continue
        except (OSError, csv.Error):
            return None
        _cache.update({"mtime": mtime, "mapa": mapa})
    return _cache["mapa"]


def pnl_1eur(ask: float, acierto: bool) -> float:
    """PnL por 1 EUR de stake comprando al ask, fee cripto 7 % sobre la ganancia."""
    return (1 - ask) / ask * (1 - FEE) if acierto else -1.0
