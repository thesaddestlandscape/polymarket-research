#!/usr/bin/env python3
"""
gbm_late_imbalance_fase0.py -- FASE 0 (solo observación), ronda2 #9
(29-Sep, petición explícita Javi: "hazlo") -- timing de entrada por
desequilibrio de libro DENTRO de una señal real de modelo GBM_LATE.

Hueco que cierra: el 29-Sep se midió el desequilibrio con
gbm_late_reactivo_fase0.csv (3.469 mercados, hit≈ask, EV/€ -0,048, sin
edge), pero ese logger dispara por dirección del drift, NO por la
probabilidad del modelo GBM_LATE; y libro_snapshots.csv (live) no guarda
imbalance. Este observador sigue las señales REALES del modelo
(predictions_YYYY-MM-DD.csv: strategy GBM_LATE*, UPDOWN_GBM_15M_TARDIO,
decisión BUY_YES/BUY_NO) y, en el instante de detección (~15 s), consulta
UNA vez el libro público del token que se compraría y registra
imbalance_top1/5/10 + pendientes + ask/profundidad. El resultado
(outcome_real) se cruza DESPUÉS con results.csv por market_id: EV al ask
real por tercil de imbalance, desagregado por moneda x marco x variante
(CLAUDE.md pt.17). Decidir con n>=40 por celda y >=10 días.

Imbalance = (suma tamaño bids - suma tamaño asks)/(total) del libro del
token COMPRADO (>0 = presión compradora en nuestro lado; mismo criterio
que libro_multinivel_fase0/gbm_late_reactivo_fase0).

NO coloca, cancela ni modifica ninguna orden real. CSV propio aparte, no
escribe en predictions/results. Se fusiona en observadores_fase0.py.
"""
import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import live_trade as lt  # noqa: E402
from libro_multinivel_fase0 import _imbalance, _slope  # noqa: E402

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "gbm_late_imbalance_fase0.csv"
VISTOS_PATH = DIR_SHADOW / "gbm_late_imbalance_fase0_vistos.json"

POLL_S = 5
STAKE_REFERENCIA_EUR = 1.05
_SESSION = requests.Session()
_SESSION.mount("https://", requests.adapters.HTTPAdapter(pool_maxsize=10))

COLUMNS = ["ts_deteccion_utc", "ts_prediccion_utc", "lag_deteccion_s", "market_id",
           "strategy", "activo", "marco", "decision", "precio_yes_mercado",
           "prob_yes_modelo", "edge_neto", "horas_a_vencimiento",
           "mejor_ask", "profundidad_eur", "ratio_vs_stake", "n_niveles_ask",
           "n_niveles_bid", "imbalance_top1", "imbalance_top5", "imbalance_top10",
           "slope_ask", "slope_bid"]


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _es_objetivo(strategy: str, decision: str) -> bool:
    return decision in ("BUY_YES", "BUY_NO") and (
        strategy.startswith("GBM_LATE") or strategy == "UPDOWN_GBM_15M_TARDIO")


def _vistos_cargar() -> set:
    try:
        return set(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return set()


def _vistos_guardar(vistos: set) -> None:
    VISTOS_PATH.write_text(json.dumps(list(vistos)[-30000:]), encoding="utf-8")


def _guardar(filas: list) -> None:
    if not filas:
        return
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(COLUMNS)
        for fila in filas:
            w.writerow([fila.get(c, "") for c in COLUMNS])


def _archivo_hoy() -> Path:
    return DIR_SHADOW / f"predictions_{datetime.now(timezone.utc).date().isoformat()}.csv"


def _libro(token_id: str, precio_entrada: float):
    """Una petición a /book. Devuelve (ok, asks, bids) ordenados."""
    try:
        r = _SESSION.get(lt.CLOB_BOOK_URL, params={"token_id": token_id}, timeout=10)
        r.raise_for_status()
        book = r.json()
    except Exception as e:
        _log(f"WARN libro {token_id[:10]}: {type(e).__name__}: {e}")
        return False, [], []
    asks = sorted((float(a["price"]), float(a["size"])) for a in (book.get("asks") or []))
    bids = sorted(((float(a["price"]), float(a["size"])) for a in (book.get("bids") or [])),
                  reverse=True)
    return True, asks, bids


def _procesar_fila(row: dict, vistos: set) -> dict | None:
    strategy = row.get("strategy", "")
    decision = row.get("decision", "")
    if not _es_objetivo(strategy, decision):
        return None
    market_id = row.get("market_id", "")
    clave = f"{market_id}|{strategy}|{decision}"
    if clave in vistos:
        return None
    vistos.add(clave)

    subtype = row.get("subtype", "")
    activo, _, marco = subtype.partition("#")
    try:
        yes_token, no_token, _ = lt._get_token_ids(market_id)
    except Exception as e:
        _log(f"WARN tokens market_id={market_id}: {e}")
        return None
    token_id = no_token if decision == "BUY_NO" else yes_token
    try:
        py = float(row.get("precio_yes_mercado", ""))
    except (TypeError, ValueError):
        return None
    precio_entrada = py if decision == "BUY_YES" else (1.0 - py)

    ok, asks, bids = _libro(token_id, precio_entrada)
    if not ok:
        return None
    techo = precio_entrada * 1.05
    prof = sum(p * s for p, s in asks if p <= techo)
    ahora = datetime.now(timezone.utc)
    try:
        lag = round((ahora - datetime.fromisoformat(
            row["timestamp_utc"].replace("Z", "+00:00"))).total_seconds(), 1)
    except Exception:
        lag = ""
    return {
        "ts_deteccion_utc": ahora.isoformat(timespec="seconds"),
        "ts_prediccion_utc": row.get("timestamp_utc", ""),
        "lag_deteccion_s": lag, "market_id": market_id, "strategy": strategy,
        "activo": activo, "marco": marco, "decision": decision,
        "precio_yes_mercado": py, "prob_yes_modelo": row.get("prob_yes_modelo", ""),
        "edge_neto": row.get("edge_neto", ""),
        "horas_a_vencimiento": row.get("horas_a_vencimiento", ""),
        "mejor_ask": asks[0][0] if asks else "",
        "profundidad_eur": round(prof, 2),
        "ratio_vs_stake": round(prof / STAKE_REFERENCIA_EUR, 1),
        "n_niveles_ask": len(asks), "n_niveles_bid": len(bids),
        "imbalance_top1": _imbalance(asks, bids, 1),
        "imbalance_top5": _imbalance(asks, bids, 5),
        "imbalance_top10": _imbalance(asks, bids, 10),
        "slope_ask": _slope(asks) if asks else "",
        "slope_bid": _slope(bids) if bids else "",
    }


def main() -> None:
    _log("arrancado -- señales GBM_LATE*/UPDOWN_GBM_15M_TARDIO, imbalance del libro al detectar")
    vistos = _vistos_cargar()
    archivo_actual = _archivo_hoy()
    posicion = 0
    cabecera = None
    # backlog del día previo al arranque: se marca visto sin consultar
    # libro (imbalance no es reconstruible retroactivamente).
    if archivo_actual.exists():
        with open(archivo_actual, encoding="utf-8") as f:
            cabecera = next(csv.reader([f.readline()]))
            for row in csv.DictReader(f, fieldnames=cabecera):
                if _es_objetivo(row.get("strategy", ""), row.get("decision", "")):
                    vistos.add(f"{row.get('market_id','')}|{row['strategy']}|{row['decision']}")
            posicion = f.tell()
        _vistos_guardar(vistos)

    while True:
        try:
            hoy = _archivo_hoy()
            if hoy != archivo_actual:
                archivo_actual, posicion, cabecera = hoy, 0, None
            if not archivo_actual.exists():
                time.sleep(POLL_S)
                continue
            with open(archivo_actual, encoding="utf-8") as f:
                if cabecera is None:
                    cabecera = next(csv.reader([f.readline()]))
                    if posicion == 0:
                        posicion = f.tell()
                f.seek(posicion)
                lineas = f.readlines()
                posicion = f.tell()
            filas = []
            for linea in lineas:
                try:
                    row = next(csv.DictReader([linea], fieldnames=cabecera))
                except Exception:
                    continue
                res = _procesar_fila(row, vistos)
                if res:
                    filas.append(res)
            if filas:
                _guardar(filas)
                _vistos_guardar(vistos)
                _log(f"{len(filas)} señales nuevas registradas")
        except Exception as e:
            _log(f"WARN ciclo fallido: {type(e).__name__}: {e}")
        time.sleep(POLL_S)


if __name__ == "__main__":
    main()
