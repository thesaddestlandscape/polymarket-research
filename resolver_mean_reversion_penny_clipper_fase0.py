#!/usr/bin/env python3
"""resolver_mean_reversion_penny_clipper_fase0.py -- rellena outcome_real/
resolved_ts en mean_reversion_reactivo_fase0.csv y penny_clipper_fase0.csv
(29-Sep). Mismo patron que resolution_sniper_observer.py::resolver_pendientes(),
adaptado a condition_id (estos dos CSV no tienen market_id numerico de
Gamma, solo condition_id -- ver mean_reversion_penny_clipper_fase0.py).

Cron sugerido: cada 5min (mismo orden que otros resolvers de FASE 0).
"""
import csv
import fcntl
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


def _desenlace(m: dict):
    pr = m.get("outcomePrices")
    pr = json.loads(pr) if isinstance(pr, str) else pr
    if pr and len(pr) >= 2:
        if float(pr[0]) >= 0.999:
            return "Up"
        if float(pr[1]) >= 0.999:
            return "Down"
    return None


def precargar_desenlaces(cids, lote: int = 40) -> None:
    """Rellena _CACHE por lotes. 30-Sep: gamma-api NO devuelve mercados CERRADOS por `condition_ids` a secas
    (hay que pedir `closed=true`); sin eso solo se resolvía lo que se pillaba en el hueco entre resolución y
    cierre (307 de 12.802 filas en el dry-run de longshot) y la muestra resuelta quedaba sesgada."""
    pend = [c for c in dict.fromkeys(cids) if c and c not in _CACHE]
    for k in range(0, len(pend), lote):
        trozo = pend[k:k + lote]
        for extra in ({"closed": "true"}, {}):
            try:
                r = _SESSION.get(f"{GAMMA}/markets", timeout=15,
                                 params=[("condition_ids", c) for c in trozo] + [("limit", str(len(trozo)))] + list(extra.items()))
                if r.status_code != 200:
                    continue
                for m in r.json() or []:
                    out = _desenlace(m)
                    if out and m.get("conditionId"):
                        _CACHE[m["conditionId"]] = out
            except Exception:
                continue


def outcome_oficial_por_cid(cid: str):
    if cid not in _CACHE:
        precargar_desenlaces([cid])
    return _CACHE.get(cid)


def reescribir_con_candado(path: Path, lock_path: Path, columnas: list, resolver_filas) -> None:
    """Lee, resuelve y reescribe bajo el MISMO flock que usa el escritor: sin él, una fila añadida entre la
    lectura y el replace se perdía. La consulta a gamma va ANTES (fuera del candado) vía precargar_desenlaces."""
    lock_f = open(lock_path, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != columnas:
                _log(f"⚠️ {path.name} cabecera inesperada ({reader.fieldnames}) -- saltado")
                return
            rows = list(reader)
        if not resolver_filas(rows):
            return
        tmp = path.with_suffix(".tmp")
        with open(tmp, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=columnas)
            w.writeheader()
            w.writerows(rows)
        tmp.replace(path)
        _log(f"{path.name}: {sum(1 for r in rows if r.get('outcome_real'))}/{len(rows)} resueltas")
    finally:
        fcntl.flock(lock_f, fcntl.LOCK_UN)
        lock_f.close()


def _cids_vencidos(path: Path, fin_de) -> list:
    """condition_id sin desenlace cuya ronda acabó hace más de RESOLVE_DELAY_S (lectura sin candado, solo para
    saber qué pedir a gamma)."""
    ahora, cids = time.time(), []
    with open(path, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("outcome_real") or not r.get("condition_id"):
                continue
            try:
                if ahora - fin_de(r) >= RESOLVE_DELAY_S:
                    cids.append(r["condition_id"])
            except Exception:
                continue
    return cids


def resolver_fichero(path: Path, columnas: list) -> None:
    if not path.exists():
        return
    precargar_desenlaces(_cids_vencidos(path, lambda r: float(r["ts_end"])))

    def _resolver(rows) -> bool:
        cambiado = False
        for r in rows:
            out = None if r.get("outcome_real") else _CACHE.get(r.get("condition_id"))
            if out:
                # decision es "BUY_YES"/"BUY_NO"; el desenlace oficial es "Up"/"Down" ("Up" == YES gana)
                r["outcome_real"] = "YES" if out == "Up" else "NO"
                r["resolved_ts"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
                cambiado = True
        return cambiado

    reescribir_con_candado(path, Path(str(path) + ".lock"), columnas, _resolver)


def main():
    for nombre, (path, columnas) in FICHEROS.items():
        resolver_fichero(path, columnas)


if __name__ == "__main__":
    main()
