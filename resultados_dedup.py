#!/usr/bin/env python3
"""Loader compartido de data/shadow/results.csv con deduplicación por
(strategy, market_id, decision).

Origen (12-Jul): auditoría general encontró 1 predicción resuelta dos veces
(carrera entre shadow_resolve.py y el stash/rebase/push de run_fast.sh,
merge=union preserva ambas copias en vez de detectar el choque). El dedup
se arregló primero solo dentro de shadow_postmortem.py — pero
hypothesis_tracker.py, vigia_gates_pendientes.py y otros consumidores
seguían leyendo el CSV crudo, cada uno viendo un n/IC ligeramente distinto
si la carrera se repite. Propuesta #4 lista puntos ciegos (13-Jul):
extraído a módulo único para que todo el que necesite results.csv "limpio"
importe de aquí en vez de reimplementar su propio csv.DictReader.

Se queda la fila con resolution_timestamp más temprano (la resolución
real); las demás son el eco de la re-resolución.
"""
import csv
from pathlib import Path

RESULTS_PATH = Path(__file__).resolve().parent / "data/shadow/results.csv"


def cargar_results_dedup(path=None) -> list:
    p = Path(path) if path else RESULTS_PATH
    if not p.exists():
        return []
    with open(p, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    vistas = {}
    for r in rows:
        clave = (r.get("strategy", ""), r.get("market_id", ""), r.get("decision", ""))
        actual = vistas.get(clave)
        if actual is None or r.get("resolution_timestamp", "") < actual.get("resolution_timestamp", ""):
            vistas[clave] = r
    return list(vistas.values())
