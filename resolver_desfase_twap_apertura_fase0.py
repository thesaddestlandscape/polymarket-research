#!/usr/bin/env python3
"""resolver_desfase_twap_apertura_fase0.py -- rellena outcome_real en
desfase_twap_apertura_fase0.csv (29-Sep). Mismo patrón que el resto de
resolvers FASE 0 nuevos (gamma-api por market_id numérico, este observador
ya lo guarda directo).

Cron sugerido: cada 5min.
"""
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from resolution_sniper_observer import GAMMA  # noqa: E402

OUT = REPO / "data" / "shadow" / "desfase_twap_apertura_fase0.csv"
CAMPOS = ["timestamp_utc", "activo", "marco", "market_id", "ts_start", "ts_desde_apertura_s",
          "twap60_pre", "n_ticks_twap", "spot_apertura", "desfase_pct",
          "ask_up", "profundidad_up_eur", "ask_down", "profundidad_down_eur",
          "mid_up", "error", "outcome_real", "resolved_ts"]
RESOLVE_DELAY_S = 90

_SESSION = requests.Session()
_CACHE: dict = {}


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _outcome(market_id: str):
    if market_id in _CACHE:
        return _CACHE[market_id]
    out = None
    try:
        r = _SESSION.get(f"{GAMMA}/markets/{market_id}", timeout=8)
        if r.status_code == 200:
            m = r.json()
            pr = m.get("outcomePrices")
            pr = json.loads(pr) if isinstance(pr, str) else pr
            if pr and len(pr) >= 2:
                if float(pr[0]) >= 0.999:
                    out = "Up"
                elif float(pr[1]) >= 0.999:
                    out = "Down"
    except Exception:
        pass
    if out:
        _CACHE[market_id] = out
    return out


def main():
    if not OUT.exists():
        return
    with open(OUT, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != CAMPOS:
            _log(f"⚠️ cabecera inesperada ({reader.fieldnames}) -- saltado")
            return
        rows = list(reader)

    ahora = datetime.now(timezone.utc)
    dur = {"5m": 300, "15m": 900}
    cambiado = False
    for r in rows:
        if r.get("outcome_real") or not r.get("market_id") or r.get("error"):
            continue
        try:
            ts_start = float(r["ts_start"])
            marco = r["marco"]
            fin = ts_start + dur.get(marco, 0)
        except (KeyError, ValueError):
            continue
        if ahora.timestamp() - fin < RESOLVE_DELAY_S:
            continue
        out = _outcome(r["market_id"])
        if not out:
            continue
        r["outcome_real"] = out
        r["resolved_ts"] = ahora.isoformat(timespec="seconds")
        cambiado = True

    if cambiado:
        tmp = OUT.with_suffix(".tmp")
        with open(tmp, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CAMPOS)
            w.writeheader()
            w.writerows(rows)
        tmp.replace(OUT)
        n_res = sum(1 for r in rows if r.get("outcome_real"))
        _log(f"{n_res}/{len(rows)} resueltas")


if __name__ == "__main__":
    main()
