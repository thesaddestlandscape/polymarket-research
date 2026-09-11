#!/usr/bin/env python3
"""migrar_historial_a_grupos_11ago.py — migración de un solo uso: reescribe
data/shadow/zonas_validadas_externas_historial.json de claves por-tupla
("STRATEGY#ACTIVO#MARCO#DIRECCION#bucket") a claves por-grupo
("ACTIVO|MARCO_BALLENAS|DIRECCION#bucket"), tras el refactor de
analisis_zonas_validadas_externas_post_twap_10ago.py que agrupa el
cálculo por (activo,marco,dirección) en vez de por tupla exacta.

No hay pérdida de datos: las tuplas antiguas (las 15 de la lista OBJETIVO
estática) que compartían (activo,marco,dirección) ya tenían series
IDÉNTICAS (mismo cálculo duplicado bajo 2+ claves, verificado a mano
antes de escribir esto) -- se fusionan deduplicando por timestamp.
"""
import json
from pathlib import Path

from analisis_zonas_validadas_externas_post_twap_10ago import HISTORIAL, MARCO_BALLENAS_MAP

historial = json.loads(HISTORIAL.read_text(encoding="utf-8"))
nuevo: dict = {}
migradas = 0
sin_migrar = 0

for clave, entradas in historial.items():
    *tupla_partes, bucket = clave.rsplit("#", 1)
    tupla_str = "#".join(tupla_partes)
    partes = tupla_str.split("#")
    if len(partes) != 4:
        sin_migrar += 1
        nuevo[clave] = entradas  # fail-safe: conserva lo que no se puede parsear
        continue
    _strategy, activo, marco, direccion = partes
    marco_b = MARCO_BALLENAS_MAP.get(marco, marco)  # ya viene en convención ballenas si es de OBJETIVO viejo
    grupo_key = f"{activo}|{marco_b}|{direccion}#{bucket}"
    existentes = nuevo.setdefault(grupo_key, [])
    ts_ya = {e["ts"] for e in existentes}
    for e in entradas:
        if e["ts"] not in ts_ya:
            existentes.append(e)
            ts_ya.add(e["ts"])
    migradas += 1

for k in nuevo:
    nuevo[k] = sorted(nuevo[k], key=lambda e: e["ts"])

HISTORIAL.write_text(json.dumps(nuevo, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"{migradas} claves antiguas migradas, {sin_migrar} sin parsear (conservadas tal cual), "
      f"{len(nuevo)} claves finales -> {HISTORIAL}")
