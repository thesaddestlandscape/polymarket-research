#!/usr/bin/env python3
"""
analisis_zona_no_alcanzable.py — 26-Ago, propuesta #3 aprobada por Javi
en el barrido de candidatos_evaluacion_live de la sesión: varios buckets
grandes de `gate_bucket_propio.json`/`gate_bucket_fino.json` (shadow,
n grande, pnl_medio llamativo) resultaron tener CERO o casi cero
fill-ability real al comprobarlo a mano (ej. WEEKLY_PRICE#SOL#BUY_NO
[0.47,0.52) n=197 shadow, 0 fillable; GBM_LATE_15M_ESPACIO_ATR#BNB
#15min#BUY_NO [0.94,0.99) n=32 shadow, 0 fillable) -- no es que falte
esperar más n, ese precio simplemente casi nunca ocurre en el libro
real para esa tupla. Repetir esta comprobación a mano cada sesión es
el trabajo que este script ahorra.

Anota (SOLO INFORMATIVO, fichero separado -- no toca gate_bucket_propio.
json/gate_bucket_fino.json ni su campo "veredicto", que es lo que
consumen los ejecutores live fail-closed; esto es una capa de metadata
adicional, cero riesgo sobre dinero real) qué buckets de
gate_bucket_propio.json tienen fill-ability real casi nula pese a tener
n de shadow suficiente -- "zona_no_alcanzable": true cuando
n_fillable_real < UMBRAL_MIN_FILLABLE Y n_shadow >= N_MIN.

Salida: data/shadow/zona_no_alcanzable.json,
  {"STRATEGY#SUBTYPE#DECISION": {"0.45": {"n_shadow": .., "n_fillable_real": ..,
   "zona_no_alcanzable": bool}, ...}, ...}
"""
import csv
import json
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from libro_snapshots_prioridad import prio  # noqa: E402

GATE_PROPIO = REPO / "data/shadow/gate_bucket_propio.json"
LIBRO_PATH = REPO / "data/live/libro_snapshots.csv"
RESULTS_PATH = REPO / "data/shadow/results.csv"
OUT_PATH = REPO / "data/shadow/zona_no_alcanzable.json"

N_MIN = 15
RATIO_MIN = 5.0
UMBRAL_MIN_FILLABLE = 3  # menos de 3 señales fillable reales = prácticamente inalcanzable
BUCKET_STEP = 0.05


def bucket(p: float) -> str:
    b = round((p // BUCKET_STEP) * BUCKET_STEP, 2)
    return f"{b:.2f}"


def main() -> int:
    gate = json.loads(GATE_PROPIO.read_text(encoding="utf-8"))

    # tuplas con al menos un bucket n>=N_MIN en el gate (candidatas a comprobar)
    tuplas = set()
    for tupla_str, buckets_dict in gate.items():
        for b, info in buckets_dict.items():
            if info.get("n", 0) >= N_MIN:
                tuplas.add(tupla_str)
                break

    strategies = {t.split("#")[0] for t in tuplas}
    print(f"Tuplas con algún bucket n>={N_MIN}: {len(tuplas)} ({len(strategies)} estrategias)")

    # colapsar libro_snapshots por (strategy,subtype,direction,market_id)
    print("Cargando libro_snapshots.csv...")
    best = {}
    with open(LIBRO_PATH) as f:
        r = csv.DictReader(f)
        for row in r:
            if row["strategy"] not in strategies:
                continue
            key = (row["strategy"], row["subtype"], row["direction"])
            mid = row["market_id"]
            p = prio(row["motivo"])
            cur = best.get((key, mid))
            if cur is None or p < cur[0]:
                best[(key, mid)] = (p, row)

    fillable_por_key_bucket = {}
    for (key, mid), (p, row) in best.items():
        try:
            ratio = float(row["ratio_vs_stake"])
            pp = float(row["precio_plan"])
        except (TypeError, ValueError):
            continue
        if ratio < RATIO_MIN:
            continue
        b = bucket(pp)
        fillable_por_key_bucket.setdefault(key, {}).setdefault(b, 0)
        fillable_por_key_bucket[key][b] += 1

    salida = {}
    for tupla_str in tuplas:
        parts = tupla_str.split("#")
        if len(parts) != 4:
            continue
        strategy, activo, marco, decision = parts
        subtype = f"{activo}#{marco}"
        key = (strategy, subtype, decision)
        fillable_buckets = fillable_por_key_bucket.get(key, {})
        entrada = {}
        for b, info in gate[tupla_str].items():
            n_shadow = info.get("n", 0)
            if n_shadow < N_MIN:
                continue
            n_fillable = fillable_buckets.get(b, 0)
            entrada[b] = {
                "n_shadow": n_shadow,
                "n_fillable_real": n_fillable,
                "zona_no_alcanzable": n_fillable < UMBRAL_MIN_FILLABLE,
            }
        if entrada:
            salida[tupla_str] = entrada

    OUT_PATH.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")

    n_zonas_no_alcanzables = sum(
        1 for tabla in salida.values() for b in tabla.values() if b["zona_no_alcanzable"]
    )
    n_total_buckets = sum(len(tabla) for tabla in salida.values())
    print(f"\n{n_zonas_no_alcanzables}/{n_total_buckets} buckets marcados zona_no_alcanzable")
    print(f"Guardado en {OUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
