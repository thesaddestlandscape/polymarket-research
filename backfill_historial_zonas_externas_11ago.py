#!/usr/bin/env python3
"""backfill_historial_zonas_externas_11ago.py — rellena
data/shadow/zonas_validadas_externas_historial.json con observaciones
sintéticas de instantes PASADOS, usando SOLO datos que ya existían en
ballenas_timing_history.csv en ese instante.

Motivo (11-Ago, petición explícita Javi: "puedes cargarle todos los
datos post twap y ya tiene algo con lo que trabajar"): el mecanismo de
estabilidad (analisis_zonas_validadas_externas_post_twap_10ago.py::
_es_estable) arrancó el 10-Ago ~16:21 UTC y solo tenía entradas reales
desde entonces (una por cada corrida del cron `43 6 * * *` + las
corridas manuales de ayer) -- pero ballenas_timing_history.csv YA tiene
datos post-TWAP desde el 07-Ago 00:00 UTC, ~3.7 días sin usar para la
capa de estabilidad. Reconstruir esos ~15 puntos (cada 6h) es un
backtest legítimo, no fabricar datos: cada cutoff solo ve las filas con
ts_trade<=cutoff, exactamente lo que una regeneración real habría visto
en ese momento.

11-Ago (perf, primera versión con cargar(hasta=cutoff) releía las 1.6M
filas del CSV una vez por cada (tupla,cutoff) -- ~420 escaneos completos,
inviable en el VPS compartido): el CSV se lee UNA sola vez por tupla, ya
particionado por bucket con timestamps, y cada cutoff solo filtra en
memoria sobre esa partición ya cargada.

11-Ago (/code-review, hallazgo real): la primera versión escribía claves
por-tupla ("STRATEGY#ACTIVO#MARCO#DIRECCION#bucket"), pero el mismo día
main() de analisis_zonas_validadas_externas_post_twap_10ago.py se
refactorizó a claves por-GRUPO ("ACTIVO|MARCO|DIRECCION#bucket",
compartidas entre todas las estrategias del mismo (activo,marco,
dirección) -- ver migrar_historial_a_grupos_11ago.py, ya corrido una vez
para migrar lo que este script había insertado. Esta versión escribe
directamente en formato de grupo (usa _grupos_desde_config(), la misma
fuente que main() -- una sola entrada por grupo, no una por cada tupla
que lo comparte) y NO vuelve a poder ejecutarse dos veces: crea
data/shadow/.backfill_zonas_externas_11ago_done al terminar y se niega a
correr si ya existe -- este backfill es un evento histórico de una sola
vez (rellenar el hueco 07→10-Ago), no una operación repetible; correrlo
dos veces no añadiría nada (los cortes son fijos) y el guardado es solo
para que un futuro `python3 backfill_historial_zonas_externas_11ago.py`
accidental no sea un no-op silencioso sin explicar por qué.

Las entradas sintéticas se insertan ANTES de las reales ya existentes
(orden cronológico), sin tocar ni duplicar ninguna entrada real. Tras
este backfill, corre analisis_zonas_validadas_externas_post_twap_10ago.py
normal para que recalcule "estable" con el historial ya enriquecido +
una observación real de HOY.
"""
import bisect
import csv
import json
import sys
from datetime import datetime, timedelta, timezone

from analisis_zonas_validadas_externas_post_twap_10ago import (
    HISTORIAL, BALLENAS_HIST, FECHA_CAMBIO_TWAP,
    MARCOS_TWAP_AFECTADOS, bucket, evaluar_zona, _grupos_desde_config,
)

PASO_HORAS = 6
# primera entrada REAL de historial (arranque del mecanismo, 10-Ago) --
# el backfill se detiene justo antes para no duplicar/pisar nada real.
CORTE_MECANISMO_REAL = datetime(2026, 8, 10, 16, 21, 0, tzinfo=timezone.utc)
MARCADOR_UNA_VEZ = HISTORIAL.parent / ".backfill_zonas_externas_11ago_done"


def _cargar_todo_agrupado(claves: set) -> dict:
    """Una sola pasada por el CSV completo. Devuelve
    {(activo,marco,compro_yes): [(ts, p_yes, acierto, condition_id), ...]}
    ya ordenado por ts -- de ahí cada grupo/cutoff filtra en memoria."""
    datos = {k: [] for k in claves}
    with open(BALLENAS_HIST, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            activo = row.get("activo")
            marco = row.get("marco")
            compro_yes = row.get("compro_yes")
            k = (activo, marco, compro_yes)
            if k not in datos:
                continue
            try:
                p = float(row["precio"])
                ac = int(row["acierto"])
            except (TypeError, ValueError):
                continue
            if compro_yes == "0":
                p = 1 - p
            try:
                ts = datetime.fromisoformat(row["ts_trade"])
                if ts.tzinfo is None:
                    ts = ts.replace(tzinfo=timezone.utc)
            except Exception:
                continue
            if marco in MARCOS_TWAP_AFECTADOS and ts < FECHA_CAMBIO_TWAP:
                continue
            datos[k].append((ts, p, ac, row.get("condition_id", "")))
    for k in datos:
        datos[k].sort(key=lambda x: x[0])
    return datos


def main():
    if MARCADOR_UNA_VEZ.exists():
        print(f"Ya se corrió este backfill una vez ({MARCADOR_UNA_VEZ}) -- "
              "es un evento histórico de un solo uso, no hace falta repetirlo. "
              "Borra el marcador a mano si de verdad quieres re-ejecutarlo.")
        return 1

    try:
        historial = json.loads(HISTORIAL.read_text(encoding="utf-8"))
    except Exception:
        historial = {}

    cutoffs = []
    t = FECHA_CAMBIO_TWAP + timedelta(hours=PASO_HORAS)
    while t < CORTE_MECANISMO_REAL:
        cutoffs.append(t)
        t += timedelta(hours=PASO_HORAS)
    print(f"{len(cutoffs)} cortes sintéticos entre {FECHA_CAMBIO_TWAP.isoformat()} y {CORTE_MECANISMO_REAL.isoformat()}")

    grupos = _grupos_desde_config()
    claves_csv = {(activo, marco, "1" if direccion == "BUY_YES" else "0")
                  for activo, marco, direccion in grupos}
    print(f"{len(grupos)} grupos (activo,marco,dirección) a rellenar. Leyendo "
          f"ballenas_timing_history.csv (una sola pasada)...")
    agrupado = _cargar_todo_agrupado(claves_csv)

    n_insertadas = 0
    for (activo, marco, direccion) in grupos:
        grupo_key = f"{activo}|{marco}|{direccion}"
        compro_yes = "1" if direccion == "BUY_YES" else "0"
        filas_todas = agrupado.get((activo, marco, compro_yes), [])
        if not filas_todas:
            continue
        tss = [f[0] for f in filas_todas]
        for cutoff in cutoffs:
            idx = bisect.bisect_right(tss, cutoff)
            filas_hasta = filas_todas[:idx]
            if not filas_hasta:
                continue
            por_bucket: dict = {}
            for fila in filas_hasta:
                b = bucket(fila[1])
                por_bucket.setdefault(b, []).append(fila)
            for b, filas in por_bucket.items():
                info = evaluar_zona(filas, decision=direccion)
                if info is None:
                    continue  # n<N_MIN en este cutoff -- normal en los primeros cortes
                b_key = f"{b:.2f}"
                clave = f"{grupo_key}#{b_key}"
                entradas = historial.get(clave, [])
                if any(datetime.fromisoformat(e["ts"]) <= cutoff for e in entradas):
                    continue
                entradas.append({"ts": cutoff.isoformat(timespec="seconds"), "pasa": info["pasa"],
                                  "backfill_11ago": True})
                historial[clave] = entradas
                n_insertadas += 1

    for clave in historial:
        historial[clave] = sorted(historial[clave], key=lambda e: e["ts"])

    HISTORIAL.write_text(json.dumps(historial, indent=2, ensure_ascii=False), encoding="utf-8")
    MARCADOR_UNA_VEZ.write_text(datetime.now(timezone.utc).isoformat(timespec="seconds"), encoding="utf-8")
    print(f"{n_insertadas} observaciones sintéticas insertadas en {HISTORIAL}")
    print(f"Marcador escrito en {MARCADOR_UNA_VEZ}")


if __name__ == "__main__":
    sys.exit(main() or 0)
