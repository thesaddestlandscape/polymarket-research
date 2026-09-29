#!/usr/bin/env python3
"""resolver_wallet_first_buy_longshot_dryrun.py -- rellena outcome_real en
wallet_first_buy_longshot_executor_dryrun.csv (29-Sep). Mismo patrón que
resolver_mean_reversion_penny_clipper_fase0.py (condition_id vía gamma-api).

Cron sugerido: cada 5min.
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
from resolution_sniper_observer import GAMMA  # noqa: E402

RESOLVE_DELAY_S = 90
OUT = REPO / "data" / "shadow" / "wallet_first_buy_longshot_executor_dryrun.csv"
COLUMNAS = ["ts_trade", "wallet", "slug", "market_id", "condition_id", "activo", "marco", "outcome",
            "p_wallet", "usd", "tte_s", "lag_deteccion_s", "offset_s", "t_real_s",
            "ask", "bid", "profundidad_eur", "ratio_vs_stake", "lat_libro_ms",
            "decision_dry_run", "stake_sim_eur", "error", "outcome_real", "resolved_ts"]

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
            pr = json.loads(pr) if isinstance(pr, str) else pr
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


def main():
    if not OUT.exists():
        return
    with open(OUT, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != COLUMNAS:
            _log(f"⚠️ cabecera inesperada ({reader.fieldnames}) -- saltado")
            return
        rows = list(reader)

    ahora = time.time()
    cambiado = False
    pendientes_por_cid: dict = {}
    for r in rows:
        if r.get("outcome_real") or not r.get("condition_id"):
            continue
        try:
            tte = float(r.get("tte_s") or 0)
            ts_trade = datetime.fromisoformat(r["ts_trade"].replace("Z", "+00:00")).timestamp()
        except Exception:
            continue
        ts_end = ts_trade + tte  # aproximación: tte medido desde el trade, fin de ronda ~ts_trade+tte
        if ahora - ts_end < RESOLVE_DELAY_S:
            continue
        pendientes_por_cid.setdefault(r["condition_id"], []).append(r)

    for cid, filas in pendientes_por_cid.items():
        out = outcome_oficial_por_cid(cid)
        if not out:
            continue
        outcome_real_yesno = out  # "Up"/"Down", mismo vocabulario que la columna "outcome"
        for r in filas:
            r["outcome_real"] = outcome_real_yesno
            r["resolved_ts"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            cambiado = True

    if cambiado:
        tmp = OUT.with_suffix(".tmp")
        with open(tmp, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNAS)
            w.writeheader()
            w.writerows(rows)
        tmp.replace(OUT)
        n_res = sum(1 for r in rows if r.get("outcome_real"))
        _log(f"{n_res}/{len(rows)} resueltas")


if __name__ == "__main__":
    main()
