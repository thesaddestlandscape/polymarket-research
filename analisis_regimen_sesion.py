#!/usr/bin/env python3
"""Regimen de sesion (13-Jul, peticion Javi tras diagnosticar la racha
09-13Jul): sigma_h instantaneo (20min, el que ya alimenta el modelo GBM) no
es un filtro estable por trade -- se probo en la sesion anterior y el signo
se invierte entre el periodo bueno (06-08Jul) y el malo (09-13Jul) para ETH.

Hipotesis a probar aqui: un indicador de VOLATILIDAD REALIZADA A NIVEL DE
SESION (ventana mucho mas larga -- 1 a 6h -- terminando en el instante de
cada prediccion) puede capturar si TODO el periodo esta comprimido, en vez
de si esa ventana concreta de 15/20min se movio o no. Es distinto de:
  - sigma_h (20min, ya en el modelo GBM)
  - sigma_ewma_delta_pct (aceleracion/desaceleracion vs su propia media
    ewma de 10min, ya promocionado en ETH#15min BUY_YES)
Este es un tercer eje: nivel absoluto de vol en las ultimas N horas.

Metodologia: SOLO ANALISIS, no toca shadow_predict.py ni live_trade.py.
Para cada prediccion de la familia GBM (GBM_LATE_15M + variantes,
UPDOWN_GBM) en results.csv, calcula sigma_regimen_Wh = vol realizada de
log-retornos en las W horas anteriores al instante de la prediccion
(misma formula que _estimar_vol_h, ventana mas larga). Bucketiza por
mediana dentro de cada (estrategia, activo, horizonte, direccion) y calcula
ic_bayes por bucket, para varios tamanos de ventana W. Exige, antes de
proponer nada:
  1. n>=40 por celda (listón de promocion a vivo)
  2. Monotonicidad / diferencia clara entre bucket alto y bajo
  3. Test de permutacion (20k shuffles) sobre la mejor ventana
  4. Consistencia split-half temporal (primera mitad del periodo vs segunda)
  5. Coherencia de signo cross-asset

Uso: python3 analisis_regimen_sesion.py
"""
import bisect
import csv
import json
import math
import random
import statistics
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

REPO = Path(__file__).resolve().parent
DIR_PRICES = REPO / "data/prices"
RESULTS = REPO / "data/shadow/results.csv"
SYMS = ["BTC", "ETH", "SOL", "XRP"]
ESTRATEGIAS_GBM = {"GBM_LATE_15M", "GBM_LATE_15M_TARDIO", "GBM_LATE_15M_ESPACIO_ATR", "UPDOWN_GBM"}
WINDOWS_H = [1, 2, 3, 4, 6]
N_MIN_CELDA = 40


def _parse_ts(s):
    try:
        ts = datetime.fromisoformat(s.replace("Z", "+00:00"))
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
        return ts
    except Exception:
        return None


def cargar_precios():
    """sym -> (lista_ts_ordenada, lista_precio) para bisect O(log n)."""
    por_asset = {sym: ([], []) for sym in SYMS}
    buf_por_ts = defaultdict(dict)
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
                buf_por_ts[(asset, ts)] = v
    for (asset, ts), v in sorted(buf_por_ts.items(), key=lambda x: x[0][1]):
        por_asset[asset][0].append(ts)
        por_asset[asset][1].append(v)
    return por_asset


def sigma_regimen(ts_list, precio_list, t_fin, window_h):
    """Vol realizada (misma formula que _estimar_vol_h: sqrt(var/avg_dur*60))
    de los log-retornos en (t_fin - window_h, t_fin]. None si <5 puntos."""
    t0 = t_fin - timedelta(hours=window_h)
    i0 = bisect.bisect_left(ts_list, t0)
    i1 = bisect.bisect_right(ts_list, t_fin)
    ts_sub = ts_list[i0:i1]
    p_sub = precio_list[i0:i1]
    if len(ts_sub) < 5:
        return None
    log_r = [math.log(p_sub[i] / p_sub[i-1])
             for i in range(1, len(p_sub)) if p_sub[i-1] > 0 and p_sub[i] > 0]
    if len(log_r) < 4:
        return None
    var = sum(r * r for r in log_r) / len(log_r)
    durs = [(ts_sub[i] - ts_sub[i-1]).total_seconds() / 60 for i in range(1, len(ts_sub))]
    avg_dur = sum(durs) / len(durs)
    if avg_dur <= 0:
        return None
    return math.sqrt(var / avg_dur * 60)


def ic_bayes(aciertos, n):
    return (aciertos + 1) / (n + 2) - 0.5


def cargar_resultados():
    rows = []
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["strategy"] not in ESTRATEGIAS_GBM:
                continue
            if r["decision"] not in ("BUY_YES", "BUY_NO"):
                continue
            if "#" not in r["subtype"]:
                continue
            activo, horiz = r["subtype"].split("#", 1)
            if activo not in SYMS:
                continue
            ts = _parse_ts(r.get("prediction_timestamp", ""))
            if ts is None:
                continue
            try:
                acierto = int(r["acierto"])
                pnl = float(r["pnl_neto"])
            except (ValueError, TypeError):
                continue
            rows.append({
                "strategy": r["strategy"], "activo": activo, "horiz": horiz,
                "decision": r["decision"], "ts": ts, "acierto": acierto, "pnl": pnl,
                "fecha": r.get("prediction_timestamp", "")[:10],
            })
    return rows


def permutacion_gap(rows_lo, rows_hi, n_iter=20000, seed=42):
    """p-value de que el gap ic(hi)-ic(lo) observado sea puro azar,
    mezclando las etiquetas acierto entre los dos grupos."""
    n_lo, n_hi = len(rows_lo), len(rows_hi)
    aciertos = [r["acierto"] for r in rows_lo] + [r["acierto"] for r in rows_hi]
    obs_lo = sum(r["acierto"] for r in rows_lo)
    obs_hi = sum(r["acierto"] for r in rows_hi)
    obs_gap = ic_bayes(obs_hi, n_hi) - ic_bayes(obs_lo, n_lo)
    rnd = random.Random(seed)
    extremos = 0
    for _ in range(n_iter):
        rnd.shuffle(aciertos)
        a_lo = sum(aciertos[:n_lo])
        a_hi = sum(aciertos[n_lo:])
        gap = ic_bayes(a_hi, n_hi) - ic_bayes(a_lo, n_lo)
        if abs(gap) >= abs(obs_gap):
            extremos += 1
    return obs_gap, extremos / n_iter


def main():
    print("Cargando precios...")
    precios = cargar_precios()
    for sym in SYMS:
        print(f"  {sym}: {len(precios[sym][0])} puntos")

    print("Cargando results.csv (familia GBM)...")
    resultados = cargar_resultados()
    print(f"  n_total={len(resultados)}")

    # Precalcula sigma_regimen para cada (fila, ventana)
    for row in resultados:
        ts_list, p_list = precios[row["activo"]]
        row["sigma"] = {}
        for w in WINDOWS_H:
            row["sigma"][w] = sigma_regimen(ts_list, p_list, row["ts"], w)

    # Agrupa por celda (estrategia, activo, horiz, decision)
    celdas = defaultdict(list)
    for row in resultados:
        celdas[(row["strategy"], row["activo"], row["horiz"], row["decision"])].append(row)

    print(f"\n{'='*100}")
    print(f"{'celda':45s} {'W':>3s} {'n':>4s} {'ic_bajo':>9s} {'ic_alto':>9s} {'gap':>8s}")
    print("=" * 100)

    resumen = []
    for celda, rows in sorted(celdas.items(), key=lambda x: -len(x[1])):
        if len(rows) < N_MIN_CELDA:
            continue
        nombre = "#".join(celda)
        mejor = None
        for w in WINDOWS_H:
            sub = [r for r in rows if r["sigma"].get(w) is not None]
            if len(sub) < N_MIN_CELDA:
                continue
            sub_sorted = sorted(sub, key=lambda r: r["sigma"][w])
            mediana = sub_sorted[len(sub_sorted) // 2]["sigma"][w]
            lo = [r for r in sub if r["sigma"][w] < mediana]
            hi = [r for r in sub if r["sigma"][w] >= mediana]
            if len(lo) < 15 or len(hi) < 15:
                continue
            ic_lo = ic_bayes(sum(r["acierto"] for r in lo), len(lo))
            ic_hi = ic_bayes(sum(r["acierto"] for r in hi), len(hi))
            gap = ic_hi - ic_lo
            print(f"{nombre:45s} {w:3d} {len(sub):4d} {ic_lo:9.4f} {ic_hi:9.4f} {gap:8.4f}")
            if mejor is None or abs(gap) > abs(mejor["gap"]):
                mejor = {"w": w, "n": len(sub), "ic_lo": ic_lo, "ic_hi": ic_hi,
                         "gap": gap, "lo": lo, "hi": hi, "mediana": mediana}
        if mejor:
            resumen.append((celda, mejor))
        print("-" * 100)

    print(f"\n{'='*100}")
    print("RIGOR sobre la mejor ventana de cada celda (permutacion 20k + split-half)")
    print(f"{'='*100}")
    hallazgos = []
    for celda, m in resumen:
        nombre = "#".join(celda)
        obs_gap, p = permutacion_gap(m["lo"], m["hi"])
        rows_celda = m["lo"] + m["hi"]
        fechas = sorted(r["fecha"] for r in rows_celda)
        mid_fecha = fechas[len(fechas) // 2]
        primera = [r for r in rows_celda if r["fecha"] < mid_fecha]
        segunda = [r for r in rows_celda if r["fecha"] >= mid_fecha]

        def gap_periodo(subset):
            lo = [r for r in subset if r["sigma"][m["w"]] < m["mediana"]]
            hi = [r for r in subset if r["sigma"][m["w"]] >= m["mediana"]]
            if len(lo) < 8 or len(hi) < 8:
                return None
            return ic_bayes(sum(r["acierto"] for r in hi), len(hi)) - ic_bayes(sum(r["acierto"] for r in lo), len(lo))

        gap_p1 = gap_periodo(primera)
        gap_p2 = gap_periodo(segunda)
        mismo_signo = (gap_p1 is not None and gap_p2 is not None
                        and (gap_p1 > 0) == (gap_p2 > 0) == (obs_gap > 0))
        veredicto = "CANDIDATO" if p < 0.05 and mismo_signo else ("p<0.05 sin split-half" if p < 0.05 else "no significativo")
        print(f"{nombre:45s} W={m['w']}h n={m['n']:4d} gap={obs_gap:+.4f} p={p:.4f} "
              f"split1={gap_p1} split2={gap_p2} mismo_signo={mismo_signo} -> {veredicto}")
        hallazgos.append({
            "celda": nombre, "window_h": m["w"], "n": m["n"], "gap": round(obs_gap, 4),
            "p_valor": round(p, 4), "gap_split1": round(gap_p1, 4) if gap_p1 is not None else None,
            "gap_split2": round(gap_p2, 4) if gap_p2 is not None else None,
            "mismo_signo_split": mismo_signo, "veredicto": veredicto,
            "ic_bajo": round(m["ic_lo"], 4), "ic_alto": round(m["ic_hi"], 4),
            "mediana_sigma": round(m["mediana"], 6),
        })

    out = REPO / "data/shadow/analisis_regimen_sesion.json"
    out.write_text(json.dumps(hallazgos, ensure_ascii=False, indent=2))
    print(f"\nGuardado: {out}")


if __name__ == "__main__":
    main()
