#!/usr/bin/env python3
"""Retest para GBM_LATE_15M (13-Jul, ver idea_retest_gbm_late_15m_13jul):
inspirado en un estudio de Opening Range Breakout donde "romper y esperar
el retest" bate al "romper y entrar ya" -- el primer impulso suele ser el
fake-out que el mercado rechaza.

Hipotesis: entre las senales de GBM_LATE_15M (+_TARDIO+_ESPACIO_ATR) donde
el precio se alejo de la referencia de apertura y LUEGO volvio
parcialmente hacia ella antes de que dispare la senal (un "retest"),
¿el acierto es mejor que en las senales donde el precio siguio
moviendose sin pullback?

Metodologia: reconstruye el camino de precio intra-ventana desde
data/prices/*.csv (consenso, ~1 punto/min, NO el cache de klines que solo
guarda ~25 velas rodantes -- este SI tiene historico real acumulado).
Para cada prediccion: ref=precio en la apertura de la ventana (end_date-15min),
camino=todos los puntos entre apertura y el instante de la senal,
excursion_max=maximo alejamiento de ref en la direccion final, retest_pct=
cuanto se retrocedio desde ese maximo antes de disparar. Bucketiza y
compara IC, con permutacion. NO toca shadow_predict.py ni ninguna decision.

Uso: python3 analisis_retest_gbm_late.py
"""
import csv
import json
import math
import random
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
DIR_PRICES = REPO / "data/prices"
RESULTS = REPO / "data/shadow/results.csv"
FAMILIA = {"GBM_LATE_15M", "GBM_LATE_15M_TARDIO", "GBM_LATE_15M_ESPACIO_ATR"}
SYMS = ["BTC", "ETH", "SOL", "XRP"]


def _parse_ts(s):
    try:
        ts = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return ts.replace(tzinfo=timezone.utc) if ts.tzinfo is None else ts
    except Exception:
        return None


def cargar_precios():
    por_asset = {sym: ([], []) for sym in SYMS}
    tmp = defaultdict(dict)
    for path in sorted(DIR_PRICES.glob("*.csv")):
        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if "asset" not in (reader.fieldnames or []):
                continue
            for row in reader:
                ts = _parse_ts(row.get("timestamp_utc", ""))
                if ts is None:
                    continue
                asset = (row.get("asset") or "").strip().upper()
                if asset not in SYMS:
                    continue
                try:
                    v = float(row.get("price_usd", ""))
                except (ValueError, TypeError):
                    continue
                tmp[(asset, ts)] = v
    for (asset, ts), v in sorted(tmp.items(), key=lambda x: x[0][1]):
        por_asset[asset][0].append(ts)
        por_asset[asset][1].append(v)
    return por_asset


import bisect


def camino_ventana(ts_list, p_list, t0, t1):
    i0 = bisect.bisect_left(ts_list, t0)
    i1 = bisect.bisect_right(ts_list, t1)
    return list(zip(ts_list[i0:i1], p_list[i0:i1]))


def ic_bayes(aciertos, n):
    return (aciertos + 1) / (n + 2) - 0.5


def cargar_resultados():
    rows = []
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["strategy"] not in FAMILIA:
                continue
            if r["decision"] not in ("BUY_YES", "BUY_NO"):
                continue
            if "#" not in r["subtype"] or not r["subtype"].endswith("15min"):
                continue
            activo = r["subtype"].split("#", 1)[0]
            if activo not in SYMS:
                continue
            pred_ts = _parse_ts(r.get("prediction_timestamp", ""))
            end_ts = _parse_ts(r.get("end_date", ""))
            if pred_ts is None or end_ts is None:
                continue
            try:
                acierto = int(r["acierto"])
            except (ValueError, TypeError):
                continue
            rows.append({
                "strategy": r["strategy"], "activo": activo, "decision": r["decision"],
                "pred_ts": pred_ts, "window_start": end_ts - timedelta(minutes=15),
                "acierto": acierto, "fecha": r.get("resolution_timestamp", "")[:10],
            })
    return rows


def calcular_retest(row, precios):
    ts_list, p_list = precios[row["activo"]]
    camino = camino_ventana(ts_list, p_list, row["window_start"], row["pred_ts"])
    if len(camino) < 4:
        return None
    ref = camino[0][1]
    if ref <= 0:
        return None
    # signo final: hacia donde se movio el precio al momento de la senal
    final_price = camino[-1][1]
    signo_final = 1 if final_price > ref else -1
    # excursion maxima EN LA DIRECCION FINAL a lo largo del camino
    excursion_max = 0.0
    idx_max = 0
    for i, (t, p) in enumerate(camino):
        dev = (p - ref) / ref * signo_final
        if dev > excursion_max:
            excursion_max = dev
            idx_max = i
    dev_final = (final_price - ref) / ref * signo_final
    if excursion_max <= 1e-9:
        return None  # nunca se alejo en la direccion final -> no aplica
    retest_pct = max(0.0, (excursion_max - dev_final) / excursion_max)
    return retest_pct


def permutacion(rows_lo, rows_hi, n_iter=20000, seed=42):
    n_lo, n_hi = len(rows_lo), len(rows_hi)
    aciertos = [r["acierto"] for r in rows_lo] + [r["acierto"] for r in rows_hi]
    obs_gap = ic_bayes(sum(r["acierto"] for r in rows_hi), n_hi) - ic_bayes(sum(r["acierto"] for r in rows_lo), n_lo)
    rnd = random.Random(seed)
    extremos = 0
    for _ in range(n_iter):
        rnd.shuffle(aciertos)
        a_lo, a_hi = sum(aciertos[:n_lo]), sum(aciertos[n_lo:])
        gap = ic_bayes(a_hi, n_hi) - ic_bayes(a_lo, n_lo)
        if abs(gap) >= abs(obs_gap):
            extremos += 1
    return obs_gap, extremos / n_iter


def main():
    print("Cargando precios (histórico real, no cache rodante)...")
    precios = cargar_precios()
    for sym in SYMS:
        print(f"  {sym}: {len(precios[sym][0])} puntos")

    print("Cargando resultados GBM_LATE_15M familia...")
    resultados = cargar_resultados()
    print(f"  n_total={len(resultados)}")

    con_retest_calculado = []
    for row in resultados:
        rp = calcular_retest(row, precios)
        if rp is not None:
            row["retest_pct"] = rp
            con_retest_calculado.append(row)
    print(f"  n con retest calculable={len(con_retest_calculado)}")

    # retest_pct esta zero-inflado (muchas senales nunca retroceden -> retest_pct
    # exactamente 0.0), lo que descuadra un split por mediana (puede caer justo
    # en 0.0 y desequilibrar los buckets). Split binario mas robusto y natural:
    # "nunca retrocedio" (==0) vs "retrocedio algo" (>0).
    sin_retest = [r for r in con_retest_calculado if r["retest_pct"] == 0.0]
    con_retest = [r for r in con_retest_calculado if r["retest_pct"] > 0.0]

    print(f"\n{'='*90}\nGLOBAL (familia completa, todos los activos/direcciones)\n{'='*90}")
    ic_sin = ic_bayes(sum(r["acierto"] for r in sin_retest), len(sin_retest))
    ic_con = ic_bayes(sum(r["acierto"] for r in con_retest), len(con_retest))
    print(f"retest_pct==0 (nunca retrocedio): n={len(sin_retest)} ic={ic_sin:+.4f}")
    print(f"retest_pct>0  (retrocedio algo):  n={len(con_retest)} ic={ic_con:+.4f}")
    gap, p = permutacion(sin_retest, con_retest)
    print(f"gap (con-sin) = {gap:+.4f}   p-valor permutación = {p:.4f}")

    # Por celda (strategy, activo, direccion) con n>=40
    print(f"\n{'='*90}\nPOR CELDA (n>=40)\n{'='*90}")
    celdas = defaultdict(list)
    for r in con_retest_calculado:
        celdas[(r["strategy"], r["activo"], r["decision"])].append(r)
    hallazgos = []
    for celda, rows in sorted(celdas.items(), key=lambda x: -len(x[1])):
        if len(rows) < 40:
            continue
        lo = [r for r in rows if r["retest_pct"] == 0.0]
        hi = [r for r in rows if r["retest_pct"] > 0.0]
        if len(lo) < 15 or len(hi) < 15:
            continue
        ic_lo = ic_bayes(sum(r["acierto"] for r in lo), len(lo))
        ic_hi = ic_bayes(sum(r["acierto"] for r in hi), len(hi))
        gap_c, p_c = permutacion(lo, hi)
        nombre = "#".join(celda)
        print(f"{nombre:45s} n={len(rows):4d} ic_sin={ic_lo:+.4f} ic_con={ic_hi:+.4f} gap={gap_c:+.4f} p={p_c:.4f}")
        hallazgos.append({"celda": nombre, "n": len(rows), "gap": round(gap_c,4), "p": round(p_c,4)})

    # BH-FDR sobre las celdas evaluadas (alpha=0.05)
    m = len(hallazgos)
    if m:
        orden = sorted(range(m), key=lambda i: hallazgos[i]["p"])
        max_k = -1
        for rank, idx in enumerate(orden, start=1):
            if hallazgos[idx]["p"] <= (rank / m) * 0.05:
                max_k = rank
        sobreviven = set(orden[:max_k]) if max_k > 0 else set()
        for i, h in enumerate(hallazgos):
            h["bh_fdr_sobrevive"] = i in sobreviven

    # Split temporal (1a vs 2a mitad por fecha) para las celdas que sobreviven BH-FDR
    print(f"\n{'='*90}\nSPLIT TEMPORAL (celdas BH-FDR supervivientes)\n{'='*90}")
    for h in hallazgos:
        if not h.get("bh_fdr_sobrevive"):
            continue
        strategy, activo, decision = h["celda"].split("#")
        rows = celdas[(strategy, activo, decision)]
        rows_sorted = sorted(rows, key=lambda r: r["fecha"])
        mid = len(rows_sorted) // 2
        mitades = []
        for label, subset in [("1a", rows_sorted[:mid]), ("2a", rows_sorted[mid:])]:
            lo = [r for r in subset if r["retest_pct"] == 0.0]
            hi = [r for r in subset if r["retest_pct"] > 0.0]
            if len(lo) < 10 or len(hi) < 10:
                mitades.append({"mitad": label, "n": len(subset), "gap": None})
                continue
            g = ic_bayes(sum(r["acierto"] for r in hi), len(hi)) - ic_bayes(sum(r["acierto"] for r in lo), len(lo))
            mitades.append({"mitad": label, "n": len(subset), "gap": round(g, 4)})
        gaps_validos = [x["gap"] for x in mitades if x["gap"] is not None]
        estable = len(gaps_validos) == 2 and (gaps_validos[0] > 0) == (gaps_validos[1] > 0)
        h["split_temporal"] = mitades
        h["split_temporal_estable"] = estable
        print(f"{h['celda']:45s} " + " | ".join(f"{x['mitad']} n={x['n']} gap={x['gap']}" for x in mitades) + f"  estable={estable}")

    out = REPO / "data/shadow/analisis_retest_gbm_late.json"
    out.write_text(json.dumps({"global_gap": round(gap,4), "global_p": round(p,4),
                                "global_n": len(con_retest_calculado), "por_celda": hallazgos},
                               ensure_ascii=False, indent=2))
    print(f"\nGuardado: {out}")


if __name__ == "__main__":
    main()
