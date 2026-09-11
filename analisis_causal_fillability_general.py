#!/usr/bin/env python3
"""Generaliza analisis_causal_fillability_favorito.py a TODAS las estrategias
con snapshots de libro (candidato_evaluacion): ¿los patrones_ganadores
descubiertos hoy sobreviven en el subconjunto que de verdad habría
ejecutado (ratio_vs_stake>=5x), o solo existen en el shadow "de papel"?

Petición Javi (12-Jul): "mira el resto de estrategias, puede ser que el
alcance sea mucho mayor" — tras confirmar que FAVORITO_CONFIRMADO no se
rescataba, generalizar el cruce a GBM_LATE_15M_ESPACIO_ATR, GBM_LATE_15M_
TARDIO, UPDOWN_GBM, STREAK_FADE_15M (las que tienen snapshots).

Solo lectura, no toca dinero ni config.
"""
import csv
import glob
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data/shadow/results.csv"
LIBRO = REPO / "data/live/libro_snapshots.csv"
STRATEGY_PARAMS = REPO / "data/shadow/strategy_params.json"
RATIO_MIN = 5.0


def cargar_results_idx(strategy):
    idx = {}
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["strategy"] != strategy:
                continue
            try:
                feats = json.loads(r.get("features") or "{}")
            except Exception:
                feats = {}
            idx[(r["market_id"], r["decision"])] = {
                "pnl_neto": r.get("pnl_neto"), "acierto": r.get("acierto"), "feats": feats,
            }
    return idx


def cargar_fillable(strategy, idx):
    fillable = []
    with open(LIBRO, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("motivo") != "candidato_evaluacion" or r["strategy"] != strategy:
                continue
            try:
                ratio = float(r.get("ratio_vs_stake") or 0)
            except ValueError:
                ratio = 0
            if ratio < RATIO_MIN:
                continue
            info = idx.get((r["market_id"], r["direction"]))
            if not info or info["pnl_neto"] in (None, ""):
                continue
            activo = (r.get("subtype") or "").split("#", 1)[0]
            fillable.append((r["direction"], activo, info))
    return fillable


def _eval(feats, feature, condicion, umbral):
    v = feats.get(feature)
    if v is None:
        return None
    try:
        v = float(v)
    except (TypeError, ValueError):
        return None
    if condicion == "gt": return v > umbral
    if condicion == "lt": return v < umbral
    if condicion == "abs_gt": return abs(v) > umbral
    if condicion == "abs_lt": return abs(v) < umbral
    return None


def stats(rows):
    """rows: lista de tuplas cuyo ÚLTIMO elemento es el dict info (pnl_neto/acierto)."""
    n = len(rows)
    if n == 0:
        return None
    pnl = sum(float(row[-1]["pnl_neto"]) for row in rows)
    hit = sum(int(row[-1]["acierto"]) for row in rows) / n
    return n, hit, pnl / n


def main():
    params = json.loads(STRATEGY_PARAMS.read_text())
    est = params.get("estrategias", params)

    estrategias = ["FAVORITO_CONFIRMADO", "GBM_LATE_15M_ESPACIO_ATR",
                   "GBM_LATE_15M_TARDIO", "UPDOWN_GBM", "STREAK_FADE_15M"]

    for strategy in estrategias:
        idx = cargar_results_idx(strategy)
        fillable = cargar_fillable(strategy, idx)
        base = stats(fillable)
        print(f"=== {strategy} === fillable total: n={len(fillable)}"
              + (f" hit={base[1]*100:.1f}% pnl/trade={base[2]:+.4f}" if base else ""))
        if len(fillable) < 10:
            print("  (muestra insuficiente, se salta)\n")
            continue

        # Recoger patrones_ganadores de todas las claves de esta estrategia
        patrones = []
        for clave, v in est.items():
            if clave != strategy and not clave.startswith(f"{strategy}#"):
                continue
            for p in v.get("patrones_ganadores", []) or []:
                patrones.append((clave, p))

        if not patrones:
            print("  sin patrones_ganadores\n")
            continue

        activos = sorted({a for _, a, _ in fillable})
        # DESAGREGADO por (activo, dirección) — nunca solo por dirección
        # agregando activos: la lección del 12-Jul (sigma_h/hora_utc
        # contradicen en SOL pero no en ETH) exige mirar cada combinación
        # por separado antes de creer un número mezclado.
        for activo in activos + [None]:  # None = agregado, al final, de referencia
            for direccion in ("BUY_YES", "BUY_NO"):
                subset = [(d, a, x) for d, a, x in fillable
                          if d == direccion and (activo is None or a == activo)]
                sb = stats(subset)
                if not sb or sb[0] < 5:
                    continue
                etiqueta = f"{activo}#{direccion}" if activo else f"TODOS_ACTIVOS#{direccion}"
                print(f"  [{etiqueta}] fillable: n={sb[0]} hit={sb[1]*100:.1f}% pnl/trade={sb[2]:+.4f}")
                for clave, p in patrones:
                    if p.get("direccion") != direccion:
                        continue
                    filtrado = [(d, a, x) for d, a, x in subset
                                if _eval(x["feats"], p["feature"], p["condicion"], p["umbral"])]
                    sf = stats(filtrado)
                    if sf and sf[0] >= 5:
                        mejora = "🟢" if sf[2] > sb[2] else "🔴"
                        print(f"      + [{clave}] {p['feature']} {p['condicion']} {p['umbral']} "
                              f"(shadow ic={p['ic_patron']:+.3f}): n={sf[0]} hit={sf[1]*100:.1f}% "
                              f"pnl/trade={sf[2]:+.4f} {mejora}")
        print()


if __name__ == "__main__":
    main()
