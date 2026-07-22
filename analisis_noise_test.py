#!/usr/bin/env python3
"""analisis_noise_test.py — hueco de robustez #2 de
`idea_huecos_robustez_metodologia_21jul` (checklist de 10 tests quant,
Javi 21-Jul). Parameter Stability (22-Jul) ya probó que barrer el UMBRAL
±20-30% no revela picos frágiles en los 4 parámetros centrales. Este test
ataca el problema desde el otro lado: en vez de mover el umbral, perturba
ligeramente el VALOR DE LA FEATURE (ruido de medición pequeño y plausible
-- el mismo tipo de ruido que ya medimos entre fuentes de precio reales,
ver fetch_chainlink_prices.py/nested_arb) y mide si la clasificación
dentro/fuera de cada filtro_causal/patron_ganador (`strategy_params.json`)
cambia de forma desproporcionada. Si el "edge" de un filtro se evapora con
un empujón minúsculo, la frontera está pegada a un borde frágil (síntoma
de sobreajuste al valor exacto de los datos históricos), no a una región
robusta.

Reusa `_feature_match` de live_trade.py (mismo criterio que usa
shadow_predict.py en producción para decidir skip/boost) -- no reinventa
la lógica de comparación condicion/umbral.

Solo lectura. No decide nada, no toca strategy_params.json.
"""
import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

import numpy as np

from live_trade import _feature_match

REPO = Path(__file__).resolve().parent
RESULTS_CSV = REPO / "data" / "shadow" / "results.csv"
PARAMS_JSON = REPO / "data" / "shadow" / "strategy_params.json"

N_MIN = 30          # mismo listón que Parameter Stability / análisis del proyecto
NOISE_FRAC = 0.05   # ruido = 5% de la std histórica de la propia feature en esa población
N_DRAWS = 300
SEED = 22072026

MARCOS = {"5min", "15min", "60min", "240min", "atexpiry", "daily", "reach", "sniper"}


def parse_key(strategy_full_key: str, strategy_nombre: str):
    """'UPDOWN_GBM#SOL#5min' -> (activo='SOL', marco='5min'); 'UPDOWN_GBM#SOL'
    -> (activo='SOL', marco=None); 'UPDOWN_GBM#5min' -> (None, '5min');
    'UPDOWN_GBM' -> (None, None). Mismos segmentos que construye shadow_
    predict.py::lookup_keys, deconstruidos."""
    resto = strategy_full_key[len(strategy_nombre):].lstrip("#")
    if not resto:
        return None, None
    partes = resto.split("#")
    activo = marco = None
    for p in partes:
        if p in MARCOS:
            marco = p
        else:
            activo = p
    return activo, marco


def cargar_resultados():
    filas = []
    with open(RESULTS_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            dec = row.get("decision")
            if dec not in ("BUY_YES", "BUY_NO"):
                continue
            try:
                feats = json.loads(row.get("features") or "{}")
            except Exception:
                continue
            filas.append({
                "strategy": row.get("strategy", ""),
                "subtype": row.get("subtype", ""),
                "decision": dec,
                "acierto": row.get("acierto") == "1",
                "features": feats,
            })
    return filas


def poblacion_para(filas, strategy, activo, marco, direccion):
    out = []
    for r in filas:
        if r["strategy"] != strategy:
            continue
        if direccion and r["decision"] != direccion:
            continue
        st = r["subtype"]
        if activo and not st.startswith(f"{activo}#"):
            continue
        if marco and not st.endswith(f"#{marco}"):
            continue
        out.append(r)
    return out


def evaluar_filtro(pob, feature, condicion, umbral, rng):
    """Devuelve None si la feature no está presente en suficientes filas.
    Si no, dict con gap_clean, flip_rate medio y gap_noisy medio sobre
    N_DRAWS perturbaciones gaussianas de la feature (std=NOISE_FRAC*std
    poblacional de esa feature)."""
    vals, aciertos = [], []
    for r in pob:
        fv = r["features"].get(feature)
        if fv is None:
            continue
        try:
            vals.append(float(fv))
            aciertos.append(r["acierto"])
        except (TypeError, ValueError):
            continue
    n = len(vals)
    if n < N_MIN:
        return None
    vals = np.array(vals)
    aciertos = np.array(aciertos)
    std = vals.std()
    if std == 0:
        return None

    dentro_clean = np.array([_feature_match(v, condicion, umbral) for v in vals])
    n_dentro, n_fuera = dentro_clean.sum(), (~dentro_clean).sum()
    if n_dentro < N_MIN // 2 or n_fuera < N_MIN // 2:
        return None
    hit_dentro_clean = aciertos[dentro_clean].mean()
    hit_fuera_clean = aciertos[~dentro_clean].mean()
    gap_clean = hit_dentro_clean - hit_fuera_clean

    ruido = rng.normal(0, NOISE_FRAC * std, size=(N_DRAWS, n))
    vals_noisy = vals[None, :] + ruido  # (N_DRAWS, n)

    flip_rates = []
    gaps_noisy = []
    for draw in vals_noisy:
        dentro_n = np.array([_feature_match(v, condicion, umbral) for v in draw])
        flip_rates.append((dentro_n != dentro_clean).mean())
        nd, nf = dentro_n.sum(), (~dentro_n).sum()
        if nd < 3 or nf < 3:
            continue
        gaps_noisy.append(aciertos[dentro_n].mean() - aciertos[~dentro_n].mean())
    if not gaps_noisy:
        return None

    gap_noisy_medio = float(np.mean(gaps_noisy))
    retencion = (gap_noisy_medio / gap_clean) if abs(gap_clean) > 1e-9 else None

    return {
        "n": n, "n_dentro": int(n_dentro), "n_fuera": int(n_fuera),
        "gap_clean": round(float(gap_clean), 4),
        "flip_rate_medio": round(float(np.mean(flip_rates)), 4),
        "gap_noisy_medio": round(gap_noisy_medio, 4),
        "retencion": round(retencion, 3) if retencion is not None else None,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--top", type=int, default=40, help="cuántos filtros más frágiles mostrar")
    args = ap.parse_args()

    filas = cargar_resultados()
    print(f"Filas de results.csv cargadas (BUY_YES/BUY_NO con features): {len(filas)}")

    params = json.load(open(PARAMS_JSON, encoding="utf-8")).get("estrategias", {})
    rng = np.random.default_rng(seed=SEED)

    resultados = []
    n_evaluados = n_sin_datos = 0
    for key, entry in params.items():
        strategy = key.split("#", 1)[0]
        activo, marco = parse_key(key, strategy)
        for tipo, lista in (("filtro_causal", entry.get("filtros_causales", [])),
                            ("patron_ganador", entry.get("patrones_ganadores", []))):
            for f in lista:
                if tipo == "filtro_causal":
                    n_hint = (f.get("n_malo", 0) or 0) + (f.get("n_bueno", 0) or 0)
                else:  # patron_ganador: solo trae n_patron, no un recuento del lado base
                    n_hint = f.get("n_patron", 0) or 0
                if n_hint < N_MIN:
                    continue
                pob = poblacion_para(filas, strategy, activo, marco, f.get("direccion"))
                r = evaluar_filtro(pob, f.get("feature", ""), f.get("condicion", ""),
                                   f.get("umbral", 999), rng)
                if r is None:
                    n_sin_datos += 1
                    continue
                n_evaluados += 1
                resultados.append({
                    "key": key, "tipo": tipo, "feature": f.get("feature"),
                    "condicion": f.get("condicion"), "umbral": f.get("umbral"),
                    "direccion": f.get("direccion"), **r,
                })

    print(f"Filtros/patrones con n>=({N_MIN}) evaluables con ruido: {n_evaluados}  (sin datos suficientes hoy: {n_sin_datos})")

    con_retencion = [r for r in resultados if r["retencion"] is not None]
    con_retencion.sort(key=lambda r: r["retencion"])

    fragiles = [r for r in con_retencion if r["retencion"] < 0.5]
    print(f"\nFrágiles (retención del gap <50% bajo ruido {NOISE_FRAC*100:.0f}% de la std de la feature): {len(fragiles)}/{len(con_retencion)}")
    print(f"\n{'key':32} {'tipo':15} {'feature':22} {'n':>5} {'gap_clean':>10} {'gap_noisy':>10} {'retención':>10} {'flip_rate':>10}")
    for r in con_retencion[:args.top]:
        print(f"{r['key']:32} {r['tipo']:15} {r['feature']:22} {r['n']:5} "
              f"{r['gap_clean']:+10.3f} {r['gap_noisy_medio']:+10.3f} "
              f"{(str(r['retencion'])+'x'):>10} {r['flip_rate_medio']*100:9.1f}%")

    print("\n=== Lectura ===")
    print(f"Retención=1.0 -> el gap dentro/fuera del filtro sobrevive intacto a ruido pequeño (robusto).")
    print(f"Retención cercana a 0 o negativa -> el 'edge' del filtro depende de un borde frágil,")
    print(f"probablemente sobreajustado al valor exacto de los datos históricos usados para fijarlo.")
    print(f"Retención NO es lo mismo que n bajo -- aquí ya se exige n>={N_MIN} en ambos lados.")


if __name__ == "__main__":
    main()
