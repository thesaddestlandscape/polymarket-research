#!/usr/bin/env python3
"""Read-only, one-off (17-Jul, petición Javi tras el hallazgo de que no hay
margen temprano explotable DENTRO de la propia señal de ballenas -- ver
project_ballenas_primer_movimiento_17jul): ¿nuestro propio modelo
(FAVORITO_CONFIRMADO, que dispara por precio/momentum, sin mirar
ballenas) YA "ve" la misma dirección que las ballenas confirman más
tarde, y con margen de tiempo suficiente? Si es así, el problema no es
"necesitamos un indicador más listo" -- es que algo en el pipeline
(latencia, orden de chequeos, cadencia del ciclo) nos hace llegar tarde a
una señal que YA teníamos temprano.

Método: cruza los disparos reales de FAVORITO_CONFIRMADO#SOL/ETH#15min
#BUY_YES en results.csv (con restante_min de las features JSON, ya
calculado en el momento exacto de la señal) contra
ballenas_timing_history.csv (vía market_id->condition_id) para el MISMO
mercado: ¿a qué restante_min alcanzan las ballenas la confirmación
estándar (n>=3, concentración>=0.6) en la banda [0.7,0.9)? Si nuestro
restante_min de disparo es sistemáticamente MAYOR (más temprano) que el
de la confirmación de ballenas, vamos por delante en principio -- el
cuello de botella sería operativo, no de señal. Si es menor o similar,
las ballenas ya nos ganan de mano con este tipo de señal.

No escribe nada, no toca dinero ni config.
Uso: python3 analisis_gbm_vs_ballenas_timing_17jul.py
"""
import csv
import json
from collections import defaultdict
from pathlib import Path

from analisis_ballenas_fillability_16jul import mapear_condition_a_market

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data" / "shadow" / "results.csv"
BALLENAS = REPO / "data" / "shadow" / "ballenas_timing_history.csv"

ACTIVOS = ("SOL", "ETH")
MARCO_BALLENAS = "15m"
BANDA_LO, BANDA_HI = 0.7, 0.9
UMBRAL_PCT = 0.6
MIN_TRADES = 3


def cargar_senales_favorito():
    """market_id -> {'activo':.., 'restante_min':.., 'py_entrada':.., 'outcome_real':.., 'acierto':..}
    Solo FAVORITO_CONFIRMADO#{SOL,ETH}#15min#BUY_YES con acierto conocido."""
    senales = {}
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r["strategy"] != "FAVORITO_CONFIRMADO" or r["decision"] != "BUY_YES"
                    or r.get("acierto") not in ("0", "1")):
                continue
            activo, marco = (r["subtype"].split("#", 1) + [""])[:2]
            if activo not in ACTIVOS or marco != "15min":
                continue
            try:
                feats = json.loads(r.get("features") or "{}")
                restante = float(feats.get("restante_min"))
            except (ValueError, TypeError):
                continue
            senales[r["market_id"]] = {
                "activo": activo, "restante_min": restante,
                "py_entrada": float(r.get("precio_yes_mercado", 0) or 0),
                "outcome_real": r.get("outcome_real"), "acierto": r["acierto"],
            }
    return senales


def cargar_timelines_ballenas(condition_ids: set) -> dict:
    """condition_id -> lista de (restante_min, compro_yes) ordenada de más
    temprano a más tardío -- una sola pasada del CSV de 61MB."""
    crudo = defaultdict(list)
    with open(BALLENAS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["activo"] not in ACTIVOS or r["marco"] != MARCO_BALLENAS:
                continue
            cid = r["condition_id"]
            if cid not in condition_ids:
                continue
            try:
                precio = float(r["precio"])
                restante = float(r["restante_min"])
            except (ValueError, KeyError):
                continue
            if not (BANDA_LO <= precio < BANDA_HI):
                continue
            compro_yes = r.get("compro_yes") in ("1", "True", "true")
            crudo[cid].append((restante, compro_yes))
    for cid in crudo:
        crudo[cid].sort(key=lambda x: -x[0])
    return crudo


def restante_confirmacion(timeline: list) -> float | None:
    """restante_min en el que la banda [0.7,0.9) alcanza n>=MIN_TRADES y
    concentración>=UMBRAL_PCT en algún lado -- mismo trigger que
    veto_ballenas/BALLENAS_CONFIRMADAS_15M. None si nunca se alcanza."""
    n_yes = n_no = 0
    for restante, compro_yes in timeline:
        if compro_yes:
            n_yes += 1
        else:
            n_no += 1
        n = n_yes + n_no
        if n >= MIN_TRADES and (n_yes / n >= UMBRAL_PCT or n_no / n >= UMBRAL_PCT):
            return restante
    return None


def main():
    print("Cargando señales FAVORITO_CONFIRMADO#SOL/ETH#15min#BUY_YES de results.csv...")
    senales = cargar_senales_favorito()
    print(f"Señales con restante_min conocido: {len(senales)}")

    print("Mapeando market_id -> condition_id (30 ficheros data/markets/*.csv)...")
    mapa_mid_cid = mapear_condition_a_market()
    con_cid = {mid: mapa_mid_cid[mid] for mid in senales if mid in mapa_mid_cid}
    print(f"Con condition_id conocido: {len(con_cid)}")

    print("Cargando timelines de ballenas (una pasada, 61MB)...")
    timelines = cargar_timelines_ballenas(set(con_cid.values()))
    print(f"Mercados con actividad de ballena en banda [{BANDA_LO},{BANDA_HI}): {len(timelines)}")

    gaps = []  # (activo, gap_min, nuestro_restante, restante_conf, acierta_nuestro)
    for mid, cid in con_cid.items():
        tl = timelines.get(cid)
        if not tl:
            continue
        rc = restante_confirmacion(tl)
        if rc is None:
            continue
        s = senales[mid]
        gap = s["restante_min"] - rc   # positivo = nosotros más temprano que la confirmación
        gaps.append((s["activo"], gap, s["restante_min"], rc, s["acierto"] == "1"))

    print(f"\nMercados con señal propia + confirmación de ballenas ambas presentes: {len(gaps)}")
    if not gaps:
        print("Sin datos suficientes, salir.")
        return

    adelante = sum(1 for g in gaps if g[1] > 0)
    n = len(gaps)
    gap_medio = sum(g[1] for g in gaps) / n
    nuestro_medio = sum(g[2] for g in gaps) / n
    conf_medio = sum(g[3] for g in gaps) / n
    print(f"\n=== GLOBAL (SOL+ETH) ===")
    print(f"n={n}  vamos por delante (restante propio > confirmación ballenas): {adelante}/{n} ({100*adelante/n:.1f}%)")
    print(f"restante_min medio nuestro={nuestro_medio:.2f}  confirmación ballenas={conf_medio:.2f}  gap medio={gap_medio:+.2f} min")

    for activo in ACTIVOS:
        sub = [g for g in gaps if g[0] == activo]
        if not sub:
            continue
        ad = sum(1 for g in sub if g[1] > 0)
        nn = len(sub)
        gm = sum(g[1] for g in sub) / nn
        print(f"\n{activo}: n={nn}  por delante {ad}/{nn} ({100*ad/nn:.1f}%)  gap medio={gm:+.2f} min "
              f"(nuestro={sum(g[2] for g in sub)/nn:.2f}, confirmación={sum(g[3] for g in sub)/nn:.2f})")

    # ¿El gap importa para el acierto? -- si vamos MUY por delante, ¿acertamos más?
    print(f"\n{'bucket gap (min)':<20} {'n':>5} {'hit% (nuestra señal)':>22}")
    print("-" * 50)
    buckets = [(-999, 0), (0, 2), (2, 5), (5, 999)]
    for lo, hi in buckets:
        sub = [g for g in gaps if lo <= g[1] < hi]
        if not sub:
            continue
        hit = sum(1 for g in sub if g[4]) / len(sub)
        print(f"[{lo},{hi})".ljust(20) + f"{len(sub):>5}" + f"{hit*100:>21.1f}%")


if __name__ == "__main__":
    main()
