#!/usr/bin/env python3
"""resolver_wallet_first_buy_longshot_dryrun.py -- rellena outcome_real en
wallet_first_buy_longshot_executor_dryrun.csv (29-Sep). Mismo patrón que
resolver_mean_reversion_penny_clipper_fase0.py (condition_id vía gamma-api).

Cron sugerido: cada 5min.
"""
import csv
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from resolver_mean_reversion_penny_clipper_fase0 import (  # noqa: E402
    _CACHE, _cids_vencidos, precargar_desenlaces, reescribir_con_candado)

RESOLVE_DELAY_S = 90
OUT = REPO / "data" / "shadow" / "wallet_first_buy_longshot_executor_dryrun.csv"
COLUMNAS = ["ts_trade", "wallet", "slug", "market_id", "condition_id", "activo", "marco", "outcome",
            "p_wallet", "usd", "tte_s", "lag_deteccion_s", "offset_s", "t_real_s",
            "ask", "bid", "profundidad_eur", "ratio_vs_stake", "lat_libro_ms",
            "decision_dry_run", "stake_sim_eur", "error", "outcome_real", "resolved_ts"]

LOCK = Path(str(OUT) + ".lock")     # el mismo candado que wallet_first_buy_longshot_executor_dryrun.py::_escribir


def _fin(r) -> float:
    # tte medido desde el trade: fin de ronda ~ ts_trade + tte
    return datetime.fromisoformat(r["ts_trade"].replace("Z", "+00:00")).timestamp() + float(r.get("tte_s") or 0)


def main():
    if not OUT.exists():
        return
    precargar_desenlaces(_cids_vencidos(OUT, _fin))

    def _resolver(rows) -> bool:
        cambiado = False
        for r in rows:
            out = None if r.get("outcome_real") else _CACHE.get(r.get("condition_id"))
            if out:
                r["outcome_real"] = out          # "Up"/"Down", mismo vocabulario que la columna "outcome"
                r["resolved_ts"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
                cambiado = True
        return cambiado

    reescribir_con_candado(OUT, LOCK, COLUMNAS, _resolver)


if __name__ == "__main__":
    main()
