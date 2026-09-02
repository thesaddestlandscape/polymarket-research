#!/usr/bin/env python3
"""
analisis_arb_precio_kalshi_polymarket_02sep.py — mide si existe una
brecha de PRECIO simultánea (no de timing/lead-lag, ya refutado el
19-Ago, ver idea_kalshi_lidera_binance_leadlag_19ago) entre Kalshi
(KXBTC15M, escalera de floor_strike) y Polymarket (BTC Up/Down 15min,
umbral = precio de referencia de apertura de la ventana) para la MISMA
ventana horaria y el strike más cercano al umbral real de Polymarket.

Origen (02-Sep, propuesta B8 del barrido "edge sin capturar"): el campo
`kalshi_mid` ya logueado en gbm_late_reactivo_fase0.csv NO sirve para
esto -- es literalmente la última fila leída de kalshi_btc15m_*.csv en
el instante de la consulta (`_kalshi_ultimo_btc()`), sin emparejar por
`floor_strike` ni por `close_time` con la ventana de Polymarket. Este
script hace el cruce correcto: por cada fila BTC del reactivo (tiene
precio_ref=umbral real, mejor_ask, ts_end) busca en kalshi_btc15m_*.csv
la fila con MISMO close_time (misma ventana de 15min) y floor_strike
MÁS CERCANO a precio_ref (aproxima el mismo instrumento: "¿BTC sube del
umbral de apertura?"), a un timestamp cercano al de la fila Polymarket.

IMPORTANTE -- esto NO es un arbitraje ejecutable directo: floor_strike
de Kalshi rara vez coincide EXACTO con precio_ref de Polymarket (la
escalera tiene paso discreto, no continuo), así que el precio Kalshi
resultante es una aproximación de la probabilidad real en ese umbral,
no el mismo contrato. Sirve para medir si hay divergencia SISTEMÁTICA
de probabilidad implícita entre plataformas, no para colocar una orden
de cobertura 1:1.

Solo lectura -- no toca ninguna decisión. Genera
data/shadow/arb_precio_kalshi_polymarket.json.
"""
import csv
import glob
import json
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
OUT = REPO / "data" / "shadow" / "arb_precio_kalshi_polymarket.json"
MAX_DELTA_STRIKE_PCT = 0.005   # floor_strike a <=0.5% de precio_ref (aproximación razonable)
MAX_DELTA_TS_S = 30            # snapshots Kalshi/Polymarket a <=30s de diferencia


def _cargar_kalshi() -> list[dict]:
    filas = []
    for f in sorted(glob.glob(str(REPO / "data/prices/kalshi_btc15m_2026-*.csv"))):
        with open(f, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                try:
                    row["_close_ts"] = datetime.fromisoformat(
                        row["close_time"].replace("Z", "+00:00")
                    ).timestamp()
                    row["_ts"] = datetime.fromisoformat(
                        row["timestamp_utc"].replace("Z", "+00:00")
                    ).timestamp()
                    row["_floor"] = float(row["floor_strike"])
                    row["_yes_ask"] = float(row["yes_ask"])
                    row["_yes_bid"] = float(row["yes_bid"])
                except (ValueError, KeyError):
                    continue
                filas.append(row)
    return filas


def _indexar_por_cierre(kalshi_filas: list[dict]) -> dict:
    idx: dict[float, list[dict]] = {}
    for row in kalshi_filas:
        idx.setdefault(row["_close_ts"], []).append(row)
    return idx


def main() -> None:
    kalshi = _cargar_kalshi()
    print(f"[arb_precio_kalshi_polymarket] {len(kalshi)} filas Kalshi cargadas")
    por_cierre = _indexar_por_cierre(kalshi)

    poly = [x for x in csv.DictReader(open(REPO / "data/shadow/gbm_late_reactivo_fase0.csv", encoding="utf-8"))
            if x["activo"] == "BTC"]

    matches = []
    for row in poly:
        try:
            ts_end = float(row["ts_end"])
            precio_ref = float(row["precio_ref"])
            ask_poly = float(row["mejor_ask"])
            ts_poly = datetime.fromisoformat(
                row["timestamp_utc"].replace("Z", "+00:00")
            ).timestamp()
        except (ValueError, KeyError):
            continue
        candidatos = por_cierre.get(ts_end)
        if not candidatos:
            continue
        # strike mas cercano a precio_ref, dentro de tolerancia
        mejor = None
        for k in candidatos:
            delta_ts = abs(k["_ts"] - ts_poly)
            if delta_ts > MAX_DELTA_TS_S:
                continue
            delta_strike_pct = abs(k["_floor"] - precio_ref) / precio_ref
            if delta_strike_pct > MAX_DELTA_STRIKE_PCT:
                continue
            score = delta_strike_pct  # prioriza strike más cercano
            if mejor is None or score < mejor[0]:
                mejor = (score, k, delta_ts, delta_strike_pct)
        if mejor is None:
            continue
        _, k, delta_ts, delta_strike_pct = mejor
        ask_kalshi = k["_yes_ask"]
        matches.append({
            "ts_end": ts_end, "precio_ref": precio_ref, "floor_strike": k["_floor"],
            "delta_strike_pct": round(delta_strike_pct, 5), "delta_ts_s": round(delta_ts, 1),
            "ask_poly": ask_poly, "ask_kalshi": ask_kalshi,
            "gap": round(ask_poly - ask_kalshi, 4),
        })

    n = len(matches)
    print(f"[arb_precio_kalshi_polymarket] {n} pares emparejados (de {len(poly)} filas Polymarket BTC)")
    resultado = {"n_pares": n, "matches": matches}
    if n:
        gaps = [m["gap"] for m in matches]
        resultado["gap_medio"] = round(sum(gaps) / n, 4)
        resultado["gap_abs_medio"] = round(sum(abs(g) for g in gaps) / n, 4)
        resultado["gap_min"] = round(min(gaps), 4)
        resultado["gap_max"] = round(max(gaps), 4)
        n_gap_grande = sum(1 for g in gaps if abs(g) > 0.05)
        resultado["n_gap_mayor_5c"] = n_gap_grande
        print(f"  gap medio={resultado['gap_medio']} gap_abs_medio={resultado['gap_abs_medio']} "
              f"[{resultado['gap_min']}, {resultado['gap_max']}] "
              f"n_gap>5c={n_gap_grande}/{n}")
    OUT.write_text(json.dumps(resultado, indent=1, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
