#!/usr/bin/env python3
"""¿Los patrones causales descubiertos hoy en FAVORITO_CONFIRMADO (py_entrada
extremo, libro_liquidez alta) rescatan la candidata que falló fill-ability
8/8? Petición Javi 13-Jul (propuesta #1 de la lista de puntos ciegos).

Cruza libro_snapshots.csv (motivo=candidato_evaluacion, ratio_vs_stake>=5x =
subconjunto que SÍ habría ejecutado) con results.csv (pnl_neto/acierto +
features py_entrada/libro_liquidez) para FAVORITO_CONFIRMADO.

Resultado (13-Jul): mejora direccional pero NO rescata ninguna. El patrón
más fuerte de papel (BUY_NO py_entrada<=0.265, IC+0.327) da hit=75.9% en el
subconjunto fillable pero pnl/trade sigue en -0.185€ -- a precio ~0.735 el
breakeven bruto ya exige >73.5% de acierto, así que el margen que queda es
tan fino que fees+slippage lo consumen entero. El problema no es solo
volumen/selección adversa direccional: FAVORITO_CONFIRMADO concentra su
edge en buckets de precio alto/hit alto con margen bruto insuficiente para
sobrevivir a los costes reales de ejecución.

Solo lectura, no toca dinero ni config.
"""
import csv
import json

RESULTS = "data/shadow/results.csv"
LIBRO = "data/live/libro_snapshots.csv"
RATIO_MIN = 5.0

PATRONES = {
    ("BUY_YES", "py_entrada>=0.725"):     lambda x: x["py_entrada"] is not None and float(x["py_entrada"]) >= 0.725,
    ("BUY_YES", "libro_liquidez>=2319"):  lambda x: x["libro_liquidez"] is not None and float(x["libro_liquidez"]) >= 2319.76,
    ("BUY_NO", "py_entrada<=0.265"):      lambda x: x["py_entrada"] is not None and float(x["py_entrada"]) <= 0.265,
    ("BUY_NO", "libro_liquidez>=5897"):   lambda x: x["libro_liquidez"] is not None and float(x["libro_liquidez"]) >= 5897.73,
}


def cargar_results_idx():
    idx = {}
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["strategy"] != "FAVORITO_CONFIRMADO":
                continue
            try:
                feats = json.loads(r.get("features") or "{}")
            except Exception:
                feats = {}
            idx[(r["market_id"], r["decision"])] = {
                "pnl_neto": r.get("pnl_neto"), "acierto": r.get("acierto"),
                "py_entrada": feats.get("py_entrada"), "libro_liquidez": feats.get("libro_liquidez"),
            }
    return idx


def cargar_fillable(idx):
    fillable = []
    with open(LIBRO, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("motivo") != "candidato_evaluacion" or r["strategy"] != "FAVORITO_CONFIRMADO":
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
            fillable.append((r["direction"], info))
    return fillable


def stats(rows, nombre):
    n = len(rows)
    if n == 0:
        print(f"{nombre}: n=0")
        return
    pnl = sum(float(x["pnl_neto"]) for _, x in rows)
    hit = sum(int(x["acierto"]) for _, x in rows) / n
    print(f"{nombre:55s} n={n:4d} hit={hit*100:5.1f}% pnl/trade={pnl/n:+.4f}")


def main():
    idx = cargar_results_idx()
    fillable = cargar_fillable(idx)
    stats(fillable, "BASELINE (todo FAVORITO_CONFIRMADO fillable)")
    for direccion in ("BUY_YES", "BUY_NO"):
        subset = [(d, x) for d, x in fillable if d == direccion]
        stats(subset, f"{direccion} fillable (todo)")
        for (dcond, nombre), cond in PATRONES.items():
            if dcond != direccion:
                continue
            filtrado = [(d, x) for d, x in subset if cond(x)]
            stats(filtrado, f"  {direccion} + patrón causal ({nombre})")


if __name__ == "__main__":
    main()
