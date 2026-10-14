#!/usr/bin/env python3
"""lab_5m_barato_replay.py -- LABORATORIO (misión 5m barato, Javi 14-Oct): re-ejecuta la MISMA maquinaria del vigía v4
(vigia_5m_barato_forward.procesar, importada; el fichero congelado NO se modifica y su hash no cambia) sobre el ARCHIVO
del registro (registro_5m_barato, desde 05-Oct) con salida a otro directorio y SIN manifiesto, cambiando SOLO:
  - latencias de diagnóstico: + 355 ms (llegada al casado P50 medida 14-Oct: pre-envío + ida ~34 + taker delay 150) y
    475 ms (P90), 600 ms (cola);
  - latencia oficial (columnas cap* de capacidad por stake, controles B3/B4) = 355 ms;
  - opcionalmente el umbral (--umbral) para estudiar el mecanismo con más n (las métricas con umbral distinto NO son v4).
Uso: python3 lab_5m_barato_replay.py --dia D [--umbral 0.05] [--tag lat]
Salida: datalogs/m5barato_mision/lab_<tag>/eventos_D.csv, controles_D.csv, calidad_D.csv
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import extraer_registro_5m_barato as E  # noqa: E402
import vigia_5m_barato_forward as V  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--dia", required=True)
ap.add_argument("--umbral", type=float, default=0.05)
ap.add_argument("--tag", default="lat")
a = ap.parse_args()
V.DL = E.OUT
V.SALIDA = Path("/root/polymarket-research-datalogs/m5barato_mision") / f"lab_{a.tag}"
V.manifiesto = lambda dia: None
V.CONFIG["latencias_diagnostico_ms"] = [150, 215, 300, 355, 475, 600]
V.CONFIG["umbral_margen_neto"] = a.umbral
V.CONFIG["latencia_oficial_ms"] = 355          # capacidad (cap*), jitter y controles B3/B4 a la llegada P50 medida
V.procesar(a.dia)
