#!/usr/bin/env python3
"""resolver_mean_reversion_penny_clipper_fase0.py -- rellena outcome_real/
resolved_ts en mean_reversion_reactivo_fase0.csv y penny_clipper_fase0.csv
(29-Sep). Mismo patron que resolution_sniper_observer.py::resolver_pendientes(),
adaptado a condition_id (estos dos CSV no tienen market_id numerico de
Gamma, solo condition_id -- ver mean_reversion_penny_clipper_fase0.py).

Cron sugerido: cada 5min (mismo orden que otros resolvers de FASE 0).
"""
import csv
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from resolution_sniper_observer import GAMMA  # noqa: E402

RESOLVE_DELAY_S = 90

FICHEROS = {
    "mean_reversion": (REPO / "data/shadow/mean_reversion_reactivo_fase0.csv",
                        ["timestamp_utc", "activo", "marco", "condition_id", "ts_end",
                         "ts_trigger_ms", "ts_consulta_libro_ms", "latencia_ms",
                         "price_yes", "decision", "round_age_s", "restante_min",
                         "spot_move_pct", "mejor_ask", "mejor_bid", "profundidad_eur",
                         "ratio_vs_stake", "n_niveles", "imbalance_top1", "imbalance_top5",
                         "outcome_real", "resolved_ts"]),
    "penny_clipper": (REPO / "data/shadow/penny_clipper_fase0.csv",
                       ["timestamp_utc", "activo", "marco", "condition_id", "ts_end",
                        "ts_trigger_ms", "ts_consulta_libro_ms", "latencia_ms",
                        "price_yes", "decision", "round_age_s", "restante_min",
                        "osc_range", "reversals", "discount", "mean_ventana",
                        "mejor_ask", "mejor_bid", "spread", "profundidad_eur",
                        "ratio_vs_stake", "n_niveles", "outcome_real", "resolved_ts"]),
}

_SESSION = requests.Session()
_CACHE: dict = {}


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def outcome_oficial_por_cid(cid: str):
    if cid in _CACHE:
        return _CACHE[cid]
    out = None
    try:
        r = _SESSION.get(f"{GAMMA}/markets", params={"condition_ids": cid}, timeout=8)
        if r.status_code == 200:
            data = r.json()
            m = data[0] if data else {}
            pr = m.get("outcomePrices")
            import json as _json
            pr = _json.loads(pr) if isinstance(pr, str) else pr
            if pr and len(pr) >= 2:
                if float(pr[0]) >= 0.999:
                    out = "Up"
                elif float(pr[1]) >= 0.999:
                    out = "Down"
    except Exception:
        pass
    if out:
        _CACHE[cid] = out
    return out


def resolver_fichero(path: Path, columnas: list) -> None:
    if not path.exists():
        return
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != columnas:
            _log(f"⚠️ {path.name} cabecera inesperada ({reader.fieldnames}) -- saltado")
            return
        rows = list(reader)
    ahora = time.time()
    cambiado = False
    pendientes_por_cid: dict = {}
    for r in rows:
        if r.get("outcome_real") or not r.get("condition_id"):
            continue
        pendientes_por_cid.setdefault(r["condition_id"], []).append(r)
    for cid, filas in pendientes_por_cid.items():
        try:
            ts_end = float(filas[0]["ts_end"])
        except (ValueError, IndexError):
            continue
        if ahora - ts_end < RESOLVE_DELAY_S:
            continue
        out = outcome_oficial_por_cid(cid)
        if not out:
            continue
        # decision es "BUY_YES"/"BUY_NO"; outcome oficial es "Up"/"Down" --
        # el mercado en si es un Up/Down, "Up" == YES gana.
        outcome_real_yesno = "YES" if out == "Up" else "NO"
        for r in filas:
            r["outcome_real"] = outcome_real_yesno
            r["resolved_ts"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            cambiado = True
    if cambiado:
        tmp = path.with_suffix(".tmp")
        with open(tmp, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=columnas)
            w.writeheader()
            w.writerows(rows)
        tmp.replace(path)
        n_res = sum(1 for r in rows if r.get("outcome_real"))
        _log(f"{path.name}: {n_res}/{len(rows)} resueltas")


def main():
    for nombre, (path, columnas) in FICHEROS.items():
        resolver_fichero(path, columnas)


if __name__ == "__main__":
    main()
