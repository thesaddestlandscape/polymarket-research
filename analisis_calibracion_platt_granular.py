#!/usr/bin/env python3
"""
analisis_calibracion_platt_granular.py — Recalibración Platt de
prob_yes_modelo, granularidad extrema: (estrategia, activo) Y
(estrategia, activo, marco), para TODAS las estrategias del sistema.

Petición explícita Javi (06-Ago): "hacerlo desagregado y granulado para
cada estrategia, moneda y marco temporal para seguir con rigor los
objetivos y misiones del proyecto" -- tras encontrar que BALLENAS_TARDIAS
(tupla live ETH#5min) estaba mal_calibrado_confirmado y sin corrección
porque el fit solo se hacía a nivel AGREGADO (6 monedas mezcladas nunca
pasaba n>=200 individualmente en el caso base, o mezclaba dinámicas muy
distintas).

Por qué vive FUERA de shadow_postmortem.py (hot path del fast loop, ciclo
~20-25s): el 30-Jul ya se probó sin restricción y el fit extra para solo
42 combinaciones (estrategia,activo) con n>=200 tardó >100s -- habría
bloqueado el trading en vivo (documentado en shadow_postmortem.py, ver
git blame de CALIB_POR_ACTIVO_ESTRATEGIAS, retirada el mismo día que este
script se creó). Aquí, sin ese límite de tiempo, se puede calcular
CUALQUIER granularidad (activo Y activo+marco, todas las estrategias) con
el mismo rigor exacto (walk-forward + bootstrap + estabilidad,
_fit_calibracion_prob reusado de shadow_postmortem.py sin duplicar
lógica).

Salida: data/shadow/calibracion_platt_granular.json
  {"ESTRATEGIA#ACTIVO": {...calib...}, "ESTRATEGIA#ACTIVO#MARCO": {...}, ...}
Solo se guarda una entrada cuando el propio fit pasa sus 3 barras de rigor
(walk-forward mejora, bootstrap CI excluye 0, (a,b) estables) -- igual que
el fit de nivel base que ya vive en shadow_postmortem.py. shadow_predict.py
la consulta en caliente (lectura de fichero cacheada por mtime, igual
patrón que gate_bucket_propio.json/kelly_precio_gate.json).

Cron diario -- no bloquea nada, no toca dinero ni config. Ver
vigia_gate_calibracion.py para el vigía que ya revisa el gap de
calibración (ese es el diagnóstico; este script es la corrección).
"""
import json
import sys
import time
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import shadow_postmortem as sp  # noqa: E402 -- reusa _fit_calibracion_prob, CALIB_MIN_N,
                                 # TWAP_MARCOS_AFECTADOS/TWAP_FECHA_CAMBIO

RESULTS = REPO / "data/shadow/results.csv"
OUT = REPO / "data/shadow/calibracion_platt_granular.json"


def _cargar_calib_pairs_granular():
    """calib_pairs a nivel (estrategia,activo) y (estrategia,activo,marco)
    -- el nivel base (sin '#') ya lo calcula shadow_postmortem.py, no se
    duplica aquí.

    11-Ago: excluye filas pre-TWAP (07-Ago) de marcos afectados (5min/
    15min/240min) reusando shadow_postmortem.py::_excluir_pre_twap
    directamente (11-Ago, /code-review: antes reimplementaba la misma
    lógica fail-closed en línea, dos copias que podían divergir) -- hallazgo
    real que motivó el fix: BALLENAS_TARDIAS#ETH#5min (la propia tupla live
    que motivó este script el 06-Ago) recalibraba su corrección Platt
    mezclando régimen pre/post TWAP sin que nadie lo hubiera revisado."""
    import csv
    pairs = defaultdict(list)
    # 11-Ago (/code-review): _excluir_pre_twap() solo itera (no indexa ni
    # pide len()), así que se le pasa el DictReader directo -- evita
    # materializar el CSV completo en una lista antes de filtrar (doblaba
    # el pico de memoria en un fichero que ya pesa ~86MB y crece ~3.2MB/día).
    with open(RESULTS, encoding="utf-8") as f:
        for r in sp._excluir_pre_twap(csv.DictReader(f)):
            s = r.get("strategy", "")
            subtype = r.get("subtype", "")
            if not s:
                continue
            tripla = (r.get("prediction_timestamp", ""), r.get("prob_yes_modelo"),
                      r.get("outcome_real"))
            if "#" in subtype:
                a_part, d_part = subtype.split("#", 1)
                pairs[f"{s}#{a_part}"].append(tripla)             # nivel activo
                pairs[f"{s}#{subtype}"].append(tripla)             # nivel activo+marco (más granular)
            elif subtype:
                # estrategias sin marco (ej. WEEKLY_PRICE#BTC, SMART_FLOW_1H#BTC)
                # -- activo=subtype completo, ya es el nivel más granular posible.
                pairs[f"{s}#{subtype}"].append(tripla)
    return pairs


def main() -> int:
    t0 = time.time()
    pairs = _cargar_calib_pairs_granular()
    candidatas = {k: v for k, v in pairs.items() if len(v) >= sp.CALIB_MIN_N}
    print(f"[calibracion_granular] {len(pairs)} claves (activo/activo+marco) totales, "
          f"{len(candidatas)} con n>={sp.CALIB_MIN_N} (candidatas a fit)")

    resultado = {}
    intentadas = 0
    confirmadas = 0
    for clave, triples in sorted(candidatas.items()):
        intentadas += 1
        calib = sp._fit_calibracion_prob(triples)
        # Se registra SIEMPRE el intento (n, si pasó o no) -- así el
        # runtime puede distinguir "nunca evaluado, cae al nivel más
        # coarse" de "evaluado y NO pasó rigor" (evidencia real de que la
        # corrección no aplica aquí, no se debe caer al agregado en ese
        # caso -- mismo principio que evitó el falso positivo de
        # FAVORITO_CONFIRMADO el 30-Jul).
        resultado[clave] = {"n": len(triples), "calibracion_prob": calib}
        if calib:
            confirmadas += 1

    OUT.write_text(json.dumps(resultado, indent=2, ensure_ascii=False))
    dt = time.time() - t0
    print(f"[calibracion_granular] {intentadas} intentadas, {confirmadas} confirmadas "
          f"(pasan rigor) en {dt:.1f}s -- guardado en {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
