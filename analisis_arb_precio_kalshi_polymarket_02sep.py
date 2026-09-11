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
`floor_strike` ni por `close_time` con la ventana de Polymarket.

02-Sep, corrección tras primera pasada (petición explícita Javi: "no
dejes cosas a medias, verifícalo"): la primera versión comparaba
ask_polymarket contra ask_kalshi -- NO es limpio, cada plataforma tiene
su propio spread bid-ask, así que un gap ask-a-ask mezcla mispricing
real con diferencia de spread. Esta versión usa MID-PRICE real en
AMBOS lados: Polymarket vía `libro_ambos_lados_YYYY-MM-DD.csv`
(bid_yes/ask_yes reales, no solo el ask que loguea el reactivo) y
Kalshi vía (yes_bid+yes_ask)/2. También separa por dirección (mid>0.5
vs mid<0.5, es decir "BTC probablemente sube" vs "baja" respecto al
umbral) -- si el gap es consistente en ambas direcciones es más
sospechoso de mispricing real; si es solo en una dirección, apunta a
un sesgo de definición/semántica del contrato, no a arbitraje.

Cruce por MISMO `close_time`(Kalshi)/`end_date`(Polymarket) y
`floor_strike` más cercano a `precio_ref` (<0,5% tolerancia), con
`market_id` de Polymarket resuelto desde gbm_late_reactivo_fase0.csv
(único fichero que loguea precio_ref, el umbral real de cada ventana).

Solo lectura -- no toca ninguna decisión. Genera
data/shadow/arb_precio_kalshi_polymarket.json.
"""
import csv
import glob
import gzip
import json
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent
OUT = REPO / "data" / "shadow" / "arb_precio_kalshi_polymarket.json"
MAX_DELTA_STRIKE_PCT = 0.005
MAX_DELTA_TS_S = 60


def _abrir(path: str):
    return gzip.open(path, "rt", encoding="utf-8") if path.endswith(".gz") else open(path, encoding="utf-8")


def _cargar_kalshi() -> list[dict]:
    filas = []
    for f in sorted(glob.glob(str(REPO / "data/prices/kalshi_btc15m_2026-*.csv"))):
        with _abrir(f) as fh:
            for row in csv.DictReader(fh):
                try:
                    row["_close_ts"] = datetime.fromisoformat(
                        row["close_time"].replace("Z", "+00:00")
                    ).timestamp()
                    row["_ts"] = datetime.fromisoformat(
                        row["timestamp_utc"].replace("Z", "+00:00")
                    ).timestamp()
                    row["_floor"] = float(row["floor_strike"])
                    yb, ya = float(row["yes_bid"]), float(row["yes_ask"])
                except (ValueError, KeyError):
                    continue
                if not (0.0 <= yb <= 1.0 and 0.0 <= ya <= 1.0) or ya < yb:
                    continue
                row["_mid"] = (yb + ya) / 2
                filas.append(row)
    return filas


def _precio_ref_por_market_id() -> dict[str, tuple[float, float]]:
    """market_id -> (precio_ref, ts_end) desde gbm_late_reactivo_fase0.csv (BTC)."""
    mapa = {}
    with open(REPO / "data/shadow/gbm_late_reactivo_fase0.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["activo"] != "BTC":
                continue
            try:
                mapa[row["market_id"]] = (float(row["precio_ref"]), float(row["ts_end"]))
            except (ValueError, KeyError):
                continue
    return mapa


def _cargar_libro_ambos_lados_poly(market_ids: set) -> list[dict]:
    """Filas Polymarket BTC#15min con mid real (bid_yes+ask_yes)/2, solo
    para los market_id que ya tienen precio_ref conocido."""
    filas = []
    patrones = sorted(glob.glob("/root/polymarket-research-datalogs/libro_ambos_lados_2026-*.csv*"))
    for f in patrones:
        with _abrir(f) as fh:
            for row in csv.DictReader(fh):
                if row.get("activo") != "BTC" or row.get("marco") != "15min":
                    continue
                if row.get("market_id") not in market_ids:
                    continue
                try:
                    ay, by = float(row["ask_yes"]), float(row["bid_yes"])
                    ts = datetime.fromisoformat(
                        row["timestamp_utc"].replace("Z", "+00:00")
                    ).timestamp()
                except (ValueError, TypeError, KeyError):
                    continue
                if not (0.0 <= by <= 1.0 and 0.0 <= ay <= 1.0) or ay < by:
                    continue
                filas.append({"market_id": row["market_id"], "_ts": ts, "_mid": (ay + by) / 2})
    return filas


def main() -> None:
    ref_map = _precio_ref_por_market_id()
    print(f"[arb_precio_kalshi_polymarket] {len(ref_map)} market_id BTC con precio_ref conocido")

    poly = _cargar_libro_ambos_lados_poly(set(ref_map.keys()))
    print(f"[arb_precio_kalshi_polymarket] {len(poly)} filas Polymarket con mid real (bid+ask ambos poblados)")

    kalshi = _cargar_kalshi()
    print(f"[arb_precio_kalshi_polymarket] {len(kalshi)} filas Kalshi cargadas")
    por_cierre: dict[float, list[dict]] = {}
    for row in kalshi:
        por_cierre.setdefault(row["_close_ts"], []).append(row)

    matches = []
    for p in poly:
        precio_ref, ts_end = ref_map[p["market_id"]]
        candidatos = por_cierre.get(ts_end)
        if not candidatos:
            continue
        mejor = None
        for k in candidatos:
            delta_ts = abs(k["_ts"] - p["_ts"])
            if delta_ts > MAX_DELTA_TS_S:
                continue
            delta_strike_pct = abs(k["_floor"] - precio_ref) / precio_ref
            if delta_strike_pct > MAX_DELTA_STRIKE_PCT:
                continue
            if mejor is None or delta_strike_pct < mejor[1]:
                mejor = (k, delta_strike_pct, delta_ts)
        if mejor is None:
            continue
        k, delta_strike_pct, delta_ts = mejor
        matches.append({
            "ts_end": ts_end, "precio_ref": precio_ref, "floor_strike": k["_floor"],
            "delta_strike_pct": round(delta_strike_pct, 5), "delta_ts_s": round(delta_ts, 1),
            "mid_poly": round(p["_mid"], 4), "mid_kalshi": round(k["_mid"], 4),
            "gap": round(p["_mid"] - k["_mid"], 4),
        })

    n = len(matches)
    print(f"[arb_precio_kalshi_polymarket] {n} pares MID-a-MID emparejados")
    resultado = {"n_pares_mid": n, "matches": matches}
    if n:
        tight = [m for m in matches if m["delta_strike_pct"] < 0.001]
        gaps_tight = [m["gap"] for m in tight]
        resultado["n_tight"] = len(tight)
        if tight:
            resultado["gap_medio_tight"] = round(sum(gaps_tight) / len(tight), 4)
            resultado["gap_abs_medio_tight"] = round(sum(abs(g) for g in gaps_tight) / len(tight), 4)
        arriba = [m for m in tight if m["mid_poly"] > 0.5]
        abajo = [m for m in tight if m["mid_poly"] <= 0.5]
        for nombre, grupo in (("direccion_arriba_mid>0.5", arriba), ("direccion_abajo_mid<=0.5", abajo)):
            if grupo:
                g = [m["gap"] for m in grupo]
                resultado[nombre] = {"n": len(grupo), "gap_medio": round(sum(g) / len(g), 4)}
        print(f"  n_tight={len(tight)} gap_medio_tight={resultado.get('gap_medio_tight')} "
              f"gap_abs_medio_tight={resultado.get('gap_abs_medio_tight')}")
        print(f"  por dirección: {resultado.get('direccion_arriba_mid>0.5')} / "
              f"{resultado.get('direccion_abajo_mid<=0.5')}")
    OUT.write_text(json.dumps(resultado, indent=1, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
