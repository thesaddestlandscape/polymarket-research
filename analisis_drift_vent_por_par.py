#!/usr/bin/env python3
"""Profundiza el hallazgo de barrido_vecinos.py (propuesta #5, franja
marginal) sobre GBM_LATE_DRIFT_VENT_MIN_PCT=0.02 (shadow_predict.py:2108,
filtro de GBM_LATE_15M — EN VIVO SOL/ETH#15min#BUY_YES): el agregado de
las 4 monedas mostraba franja marginal consistentemente mala justo por
encima del umbral actual (0.00-0.03 con hit 33-43%). ¿Es uniforme por par,
o lo arrastra uno o dos activos? Selección adversa direccional ya
confirmada en el proyecto (BUY_NO peor que BUY_YES) — se rompe también por
dirección para no mezclar la única dirección que vive en live (BUY_YES)
con BUY_NO (solo shadow).

Solo lectura, results.csv. Correr desde la raíz del repo:
    python3 analisis_drift_vent_por_par.py
"""
import csv
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "data", "shadow", "results.csv")
ROWS = list(csv.DictReader(open(RES)))
N_MIN = 15
STEPS = [0.00, 0.01, 0.02, 0.03, 0.05, 0.08]
CURRENT = 0.02
ACTIVOS = ["BTC", "ETH", "SOL", "XRP"]
LIVE_HOY = {("SOL", "BUY_YES"), ("ETH", "BUY_YES")}  # pares_permitidos_live hoy


def _features(r):
    try:
        return json.loads(r["features"]) if r["features"] else {}
    except Exception:
        return {}


def sedge(r):
    try:
        e = abs(float(r["edge_neto"]))
        return e if r["acierto"] == "1" else -e
    except Exception:
        return None


def agg(rows):
    n = len(rows)
    if not n:
        return (0, 0.0, 0.0)
    hit = sum(1 for r in rows if r["acierto"] == "1") / n
    ses = [x for x in (sedge(r) for r in rows) if x is not None]
    return (n, hit, sum(ses) / len(ses) if ses else 0.0)


def base_rows(activo, decision=None):
    out = []
    for r in ROWS:
        if r["strategy"] != "GBM_LATE_15M":
            continue
        subtype = r.get("subtype", "")
        a = subtype.split("#", 1)[0] if "#" in subtype else subtype
        if a != activo:
            continue
        if decision and r.get("decision") != decision:
            continue
        out.append(r)
    return out


def barrer(label, rows, es_live):
    marca_live = "  ⚠️ EN VIVO HOY" if es_live else "  (solo shadow)"
    print(f"\n### {label}{marca_live}")
    pre = []
    for r in rows:
        f = _features(r)
        v = f.get("drift_ventana_pct")
        if v is None:
            continue
        pre.append((r, v))
    if len(pre) < N_MIN:
        print(f"  n total con feature disponible = {len(pre)} (insuficiente, skip)")
        return

    resultados = []
    sel_por_umbral = {}
    for umbral in sorted(set(STEPS + [CURRENT])):
        sel = [r for r, v in pre if abs(v) >= umbral]
        sel_por_umbral[umbral] = set(id(r) for r in sel)
        resultados.append((umbral, *agg(sel)))

    for i, (umbral, n, hit, edge) in enumerate(resultados):
        marca = "  <- ACTUAL" if abs(umbral - CURRENT) < 1e-9 else ""
        if n < N_MIN:
            print(f"  umbral={umbral:<7} n={n:<5} (insuficiente){marca}")
        else:
            print(f"  umbral={umbral:<7} n={n:<5} hit={hit*100:5.1f}%  edge_real={edge:+.4f}{marca}")
        if i > 0:
            umbral_prev = resultados[i - 1][0]
            marginal_ids = sel_por_umbral[umbral] ^ sel_por_umbral[umbral_prev]
            marginal_rows = [r for r, _ in pre if id(r) in marginal_ids]
            n_m, hit_m, edge_m = agg(marginal_rows)
            if n_m >= N_MIN:
                print(f"           franja marginal vs {umbral_prev}: n={n_m:<4} "
                      f"hit={hit_m*100:5.1f}%  edge_real={edge_m:+.4f}")
            elif n_m > 0:
                print(f"           franja marginal vs {umbral_prev}: n={n_m} (insuficiente)")


def main():
    print("=" * 78)
    print("GBM_LATE_DRIFT_VENT_MIN_PCT por par y dirección — profundiza propuesta #5")
    print("=" * 78)

    for activo in ACTIVOS:
        rows_activo = base_rows(activo)
        es_live = any((activo, d) in LIVE_HOY for d in ("BUY_YES", "BUY_NO"))
        barrer(f"{activo} — todas direcciones", rows_activo, es_live)
        for dec in ("BUY_YES", "BUY_NO"):
            rows_dec = base_rows(activo, decision=dec)
            barrer(f"{activo}#{dec}", rows_dec, (activo, dec) in LIVE_HOY)

    print("\n" + "=" * 78)
    print("Fin. Disciplina: n<15 no concluye nada. Live hoy = SOL/ETH#BUY_YES únicamente")
    print("(GBM_LATE_15M, pares_permitidos_live) — cualquier cambio de umbral las afecta")
    print("directamente en dinero real; BTC/XRP y BUY_NO son solo referencia shadow.")


if __name__ == "__main__":
    main()
