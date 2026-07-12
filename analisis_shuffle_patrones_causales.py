#!/usr/bin/env python3
"""Control aleatorio (shuffle) + corrección por tests múltiples (BH-FDR) sobre
TODOS los filtros_causales/patrones_ganadores que aprender_patrones_causales
ya escribió en strategy_params.json.

Origen (13-Jul, propuesta #2 lista de puntos ciegos): el gate de whitelist ya
exige Wilson+shuffle+BH-FDR (analisis_gate_riguroso.py) antes de proponer una
tupla a live. Pero `aprender_patrones_causales` mina ~59 claves × ~6-14
features × 5 percentiles × 2 direcciones = miles de comparaciones con un
umbral fijo (IC_FILTRO_MIN=-0.12, IC_PATRON_MIN=+0.12, N_BUCKET_MIN=15), SIN
ninguna corrección por multiplicidad. Mientras el stake esté pineado (hoy)
el impacto es cero -- pero es precisamente el tipo de mina que puede explotar
al despinear, como ya pasó una vez con el des-pineo de 07-Jul.

Método (reusa exactamente la lógica de shadow_postmortem.aprender_patrones_
causales para reconstruir el bucket real de cada patrón/filtro, y el mismo
shuffle de analisis_gate_riguroso.py): para cada patrón/filtro guardado,
recompone la subpoblación exacta (mismo _extraer_features + misma condición)
y corre 2000 barajados de outcome_real al 50/50 para ver qué % de tiradas
aleatorias iguala o supera el IC encontrado. BH-FDR con K=nº total de
patrones+filtros evaluados HOY (no solo las candidatas a whitelist).

Solo lectura, NO modifica strategy_params.json ni desactiva nada -- es una
capa de escepticismo adicional para decidir con ojos abiertos, igual que el
gate riguroso ya hace con las candidatas.
"""
import json
import random
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import shadow_postmortem as sp  # noqa: E402 — reusa cargar_results/_extraer_features/FEATURE_RULES

N_SHUFFLE = 2000
FDR = 0.10


def _ic_bayes(aciertos, n):
    return (aciertos + 1) / (n + 2) - 0.5


def _posibles(s, sub):
    posibles = {s}
    if "#" in sub:
        a_part, d_part = sub.split("#", 1)
        posibles |= {f"{s}#{sub}", f"{s}#{a_part}", f"{s}#{d_part}"}
    elif sub:
        posibles.add(f"{s}#{sub}")
    return posibles


def _feature_match(feat_val, cond, umbral):
    try:
        v, u = float(feat_val), float(umbral)
        if cond == "abs_gt": return abs(v) > u
        if cond == "abs_lt": return abs(v) < u
        if cond == "gt": return v > u
        if cond == "lt": return v < u
    except (TypeError, ValueError):
        pass
    return False


def _shuffle_pvalue(outcomes_yes, ic_real, n_shuffle=N_SHUFFLE):
    n = len(outcomes_yes)
    if n == 0:
        return 1.0
    supera = 0
    for _ in range(n_shuffle):
        aciertos_sim = sum(1 for oy in outcomes_yes if (random.random() < 0.5) == oy)
        if _ic_bayes(aciertos_sim, n) >= ic_real:
            supera += 1
    return supera / n_shuffle


def benjamini_hochberg(pvals, fdr=FDR):
    indexed = sorted(range(len(pvals)), key=lambda i: pvals[i])
    n = len(pvals)
    keep = [False] * n
    cutoff = -1
    for rank, i in enumerate(indexed, start=1):
        if pvals[i] <= fdr * rank / n:
            cutoff = rank
    if cutoff >= 0:
        for rank, i in enumerate(indexed, start=1):
            if rank <= cutoff:
                keep[i] = True
    return keep


def main():
    resultados = sp.cargar_results()
    pred_index = sp.cargar_predicciones_index()
    params = json.loads((REPO / "data/shadow/strategy_params.json").read_text())
    est = params.get("estrategias", params)

    candidatas = []  # (strat_key, tipo, feature, condicion, umbral, direccion, ic_reportado, n_reportado)
    for strat_key in sp.FEATURE_RULES:
        entry = est.get(strat_key, {})
        for f in entry.get("filtros_causales", []) or []:
            candidatas.append((strat_key, "FILTRO", f["feature"], f["condicion"], f["umbral"],
                                f["direccion"], f["ic_malo"], f["n_malo"]))
        for p in entry.get("patrones_ganadores", []) or []:
            candidatas.append((strat_key, "PATRON", p["feature"], p["condicion"], p["umbral"],
                                p["direccion"], p["ic_patron"], p["n_patron"]))

    print(f"Total filtros+patrones a validar: {len(candidatas)} (K para BH-FDR)\n")

    resultados_shuffle = []
    for strat_key, tipo, feature, cond, umbral, direccion, ic_reportado, n_reportado in candidatas:
        s = strat_key.split("#")[0]
        posibles_de_fila = None
        filas = []
        for r in resultados:
            if r.get("decision") != direccion:
                continue
            s_row, sub_row = r.get("strategy", ""), r.get("subtype", "")
            if strat_key not in _posibles(s_row, sub_row):
                continue
            clave_pred = (s_row, r.get("market_id", ""), direccion)
            pred = pred_index.get(clave_pred)
            feats = sp._extraer_features(r, pred)
            fv = feats.get(feature)
            if fv is not None and _feature_match(fv, cond, umbral):
                # OJO: "acierto" ya viene resuelto en perspectiva de la decisión
                # tomada (BUY_NO gana si outcome_real=="NO") -- usar esta
                # columna directamente, NUNCA reinterpretar outcome_real=="YES"
                # como "ganó" de forma universal (invierte el signo en BUY_NO).
                filas.append(int(r.get("acierto", 0) or 0) == 1)

        n_reconstruido = len(filas)
        if n_reconstruido == 0:
            continue
        aciertos = sum(filas)
        ic_reconstruido = _ic_bayes(aciertos, n_reconstruido)
        p = _shuffle_pvalue(filas, ic_reconstruido)
        resultados_shuffle.append({
            "clave": strat_key, "tipo": tipo, "feature": feature, "direccion": direccion,
            "n": n_reconstruido, "ic": ic_reconstruido, "p_shuffle": p,
        })

    pvals = [r["p_shuffle"] for r in resultados_shuffle]
    sobrevive = benjamini_hochberg(pvals, FDR)

    n_ok = sum(sobrevive)
    print(f"Reconstruidos: {len(resultados_shuffle)} | sobreviven BH-FDR(10%): {n_ok} | "
          f"NO sobreviven: {len(resultados_shuffle)-n_ok}\n")

    print(f"{'clave':38s} {'tipo':6s} {'feature':22s} {'dir':8s} {'n':>5s} {'IC':>8s} {'p_shuf':>8s} veredicto")
    print("-" * 110)
    for r, ok in sorted(zip(resultados_shuffle, sobrevive), key=lambda x: x[0]["p_shuffle"]):
        veredicto = "✅ sobrevive" if ok else "⚠️  RUIDO probable"
        print(f"{r['clave']:38s} {r['tipo']:6s} {r['feature']:22s} {r['direccion']:8s} "
              f"{r['n']:5d} {r['ic']:+8.3f} {r['p_shuffle']:8.3f} {veredicto}")

    import csv as _csv
    out_path = REPO / "data/shadow/shuffle_patrones_causales.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = _csv.DictWriter(f, fieldnames=["clave", "tipo", "feature", "direccion", "n", "ic", "p_shuffle", "sobrevive_bh_fdr"])
        w.writeheader()
        for r, ok in zip(resultados_shuffle, sobrevive):
            w.writerow({**r, "sobrevive_bh_fdr": int(ok)})
    print(f"\nGuardado: {out_path}")


if __name__ == "__main__":
    main()
