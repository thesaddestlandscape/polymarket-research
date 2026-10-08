#!/usr/bin/env python3
"""vigia_5m_barato_desde_archivo.py -- reprocesa un día del vigía 5m barato leyendo el ARCHIVO de larga retención
(/mnt/HC_Volume_106538179/registro_5m_barato/, extraer_registro_5m_barato.py) en vez del registro ms de 4 días. NO modifica el fichero
congelado del vigía (su hash no cambia): solo apunta su DL al archivo. Salida idéntica a leer los originales salvo la
incidencia "fichero_truncado" (verificado 08-Oct sobre 05-Oct completo y 6 h del 07-Oct).
Uso: python3 vigia_5m_barato_desde_archivo.py --dia YYYY-MM-DD
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import extraer_registro_5m_barato as E  # noqa: E402
import vigia_5m_barato_forward as V  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--dia", required=True)
a = ap.parse_args()
V.DL = E.OUT
V.procesar(a.dia)
