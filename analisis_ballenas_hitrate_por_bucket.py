#!/usr/bin/env python3
"""analisis_ballenas_hitrate_por_bucket.py — 15-Sep, petición explícita
Javi ("masterizar" SNIPER/DISPERSO/WALLET_MIRROR/CANDIDATA9, punto 4):
cruce SISTEMÁTICO con ballenas para las 4 familias, como REFUERZO de
confianza -- nunca como veto duro ("me parece bien como refuerzo, pero
no como veto", textual).

Origen: ninguna de las 4 familias cruzaba con ballenas de forma
sistemática -- solo se hacía a mano, puntualmente, cuando alguien lo
pedía en una sesión concreta (CLAUDE.md pt.8 dice que ballenas debería
ser "la lente por defecto", pero en la práctica solo lo era de memoria).

Mecanismo: agrega `ballenas_timing_history.csv` (histórico completo de
mercado, NO nuestras propias señales) por (activo, marco, bucket de
precio 0.05) -- convierte cada trade de ballena a precio en perspectiva
YES (`py_yes = precio si compro_yes==1, si no 1-precio`) y calcula el
hit-rate de que YES gane en esa zona de precio exacta. Esto da una base
de comparación independiente: si nuestra estrategia apuesta a favor de
esa misma dirección en esa misma zona, ¿coincide con lo que el mercado
de ballenas en agregado dice, o va en contra?

Salida: data/shadow/ballenas_hitrate_por_bucket.json, clave
"activo#marco#bucket" -> {"hit_rate_yes": ..., "n": ...}. Marco en
formato nativo de ballenas_timing_history.csv (5m/15m/60m/240m/weekly).
Consumido por ballenas_cross_check.py (lookup ligero, mtime-cache) desde
las 4 familias -- SOLO añade un campo informativo al gate
(`ballenas_hit_rate_yes`/`ballenas_n`/`ballenas_coincide`), NUNCA
degrada ni promueve un veredicto. La decisión de cuánto pesa queda para
cuando haya suficiente experiencia acumulada revisándolo -- hoy es
puramente informativo.

Cron diario (ver crontab, franja de vigías 06:00-08:33 UTC).
"""
import csv
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import shadow_postmortem as sp  # noqa: E402 -- reusa es_pre_twap/TWAP_MARCOS_AFECTADOS

# ballenas_timing_history.csv usa "5m"/"15m"/"60m"/"240m"/"weekly";
# TWAP_MARCOS_AFECTADOS usa "5min"/"15min"/"240min" -- mapeo necesario
# para poder reusar es_pre_twap() sin reimplementar la comparación.
_MARCO_A_TWAP = {"5m": "5min", "15m": "15min", "60m": "60min", "240m": "240min"}

IN = REPO / "data" / "shadow" / "ballenas_timing_history.csv"
OUT = REPO / "data" / "shadow" / "ballenas_hitrate_por_bucket.json"
STEP = 0.05
N_MIN = 30  # umbral informativo, no el n>=40 de una promoción real -- esto nunca decide nada por sí solo


def _bucket(p: float) -> float:
    return round(math.floor(p / STEP + 1e-9) * STEP, 4)


def main() -> int:
    grupos = defaultdict(lambda: [0, 0])  # (activo,marco,bucket) -> [n, hits_yes]
    total = 0
    excluidas_twap = 0
    with open(IN, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            total += 1
            marco_r = r.get("marco", "?")
            # 15-Sep (/code-review propio antes de confiar en los
            # resultados): "240min" está en TWAP_MARCOS_AFECTADOS (cambio
            # 07/13-Ago) -- sin este filtro, hallazgos aparentemente
            # espectaculares en 240min podían ser artefacto de mezclar
            # dos regímenes de resolución distintos, mismo hueco que ya
            # se cerró en el resto del proyecto (gate_bucket_propio.py/
            # kelly_precio_gate.py/live_trade.py::_clv_tupla). "weekly" no
            # está en la lista -- no se excluye.
            marco_twap = _MARCO_A_TWAP.get(marco_r, marco_r)
            if sp.es_pre_twap(marco_twap, r.get("ts_trade", "")):
                excluidas_twap += 1
                continue
            try:
                precio = float(r["precio"])
            except (TypeError, ValueError):
                continue
            if not (0.0 < precio < 1.0):
                continue
            compro_yes = r.get("compro_yes") in ("1", "True", "true")
            acierto = r.get("acierto")
            if acierto not in ("0", "1"):
                continue
            gano_wallet = int(acierto)
            # outcome_yes: True si el mercado resolvió YES
            outcome_yes = gano_wallet == 1 if compro_yes else gano_wallet == 0
            py_yes = precio if compro_yes else round(1.0 - precio, 4)
            b = _bucket(py_yes)
            clave = (r.get("activo", "?"), r.get("marco", "?"), b)
            grupos[clave][0] += 1
            grupos[clave][1] += int(outcome_yes)

    resultado = {}
    n_confirmados = 0
    for (activo, marco, b), (n, hits) in grupos.items():
        if n < N_MIN:
            continue
        clave_str = f"{activo}#{marco}#{b:.2f}"
        resultado[clave_str] = {"hit_rate_yes": round(hits / n, 4), "n": n}
        n_confirmados += 1

    tmp = OUT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(resultado, indent=1, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    tmp.replace(OUT)

    print(f"[analisis_ballenas_hitrate_por_bucket] {total} filas leídas "
          f"({excluidas_twap} excluidas por pre-TWAP en marcos afectados), "
          f"{len(grupos)} combos (activo,marco,bucket), {n_confirmados} con n>={N_MIN} escritos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
