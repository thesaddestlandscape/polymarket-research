#!/usr/bin/env python3
"""Sigue forward si las wallets de data/shadow/wallets_sospechosas.json
(descubiertas 12-Jul: aparecen desproporcionadamente en el lado ganador de
nuestras pérdidas reales en GBM_LATE_15M SOL/ETH BUY_YES vs nuestras
ganancias, z=+1.45 a +3.05 con n=49/48) siguen prediciendo nuestro resultado
con muestra fresca acumulada día a día.

Asíncrono y post-hoc (como maker_pilot_sim.py) — NO añade ninguna llamada a
la ruta de ejecución en vivo (live_trade.py), cero latencia añadida, cero
riesgo. Read-only, no toca dinero ni config. Log en
data/shadow/wallet_contraparte.csv, idempotente por market_id.

Próximo paso (no antes de n>=40 forward con z sostenido): si se confirma,
proponer un veto real requeriría añadir la consulta al tape ANTES de
ejecutar en live_trade.py -- decisión explícita de Javi por el riesgo de
latencia añadida a la ruta caliente.
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

TRADES = REPO / "data/live/trades.csv"
SOSPECHOSAS = REPO / "data/shadow/wallets_sospechosas.json"
OUT = REPO / "data/shadow/wallet_contraparte.csv"
GAMMA = "https://gamma-api.polymarket.com"
DATA_API = "https://data-api.polymarket.com"
H = {"User-Agent": "Mozilla/5.0 (compatible; polymarket-research/1.0)"}
TIMEOUT = 10
VENTANA_S = 120

_CAMPOS = ["market_id", "subtype", "outcome_real", "n_wallets_sospechosas_activas",
           "wallets_vistas", "resultado_nuestro"]


def _ya_procesados():
    if not OUT.exists():
        return set()
    with open(OUT, encoding="utf-8") as f:
        return {r["market_id"] for r in csv.DictReader(f)}


def _condition_id(market_id):
    try:
        r = requests.get(f"{GAMMA}/markets/{market_id}", timeout=TIMEOUT, headers=H)
        d = r.json() if r.status_code == 200 else None
        if isinstance(d, list) and d:
            d = d[0]
        return d.get("conditionId") if isinstance(d, dict) else None
    except Exception:
        return None


def main() -> int:
    if not TRADES.exists() or not SOSPECHOSAS.exists():
        return 0
    sospechosas = set(json.loads(SOSPECHOSAS.read_text()).get("wallets", {}).keys())
    ya = _ya_procesados()
    nuevo_archivo = not OUT.exists() or OUT.stat().st_size == 0
    nuevas = 0

    with open(TRADES, encoding="utf-8") as f:
        trades = [r for r in csv.DictReader(f)
                  if r.get("strategy") == "GBM_LATE_15M" and r.get("direction") == "BUY_YES"
                  and r.get("subtype") in ("SOL#15min", "ETH#15min")
                  and r.get("status") == "CLOSED" and "maker_pilot=1" not in (r.get("notas") or "")
                  and r.get("market_id") not in ya]

    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=_CAMPOS)
        if nuevo_archivo:
            w.writeheader()
        for t in trades:
            mid = t["market_id"]
            try:
                ts_exec = datetime.fromisoformat(t["timestamp_utc"].replace("Z", "+00:00"))
            except Exception:
                continue
            cid = _condition_id(mid)
            if not cid:
                continue
            try:
                r = requests.get(f"{DATA_API}/trades", params={"market": cid, "limit": 200},
                                  headers=H, timeout=TIMEOUT)
                tr = r.json() if r.status_code == 200 else []
            except Exception:
                tr = []
            time.sleep(0.15)

            lado_ganador = "Down" if t["outcome_real"] == "NO" else "Up"
            vistas = set()
            for x in tr:
                try:
                    tt = datetime.fromtimestamp(x["timestamp"], tz=timezone.utc)
                except Exception:
                    continue
                if abs((tt - ts_exec).total_seconds()) > VENTANA_S:
                    continue
                if x.get("outcome") == lado_ganador and x.get("side") == "BUY":
                    pw = x.get("proxyWallet")
                    if pw in sospechosas:
                        vistas.add(pw)

            w.writerow({
                "market_id": mid, "subtype": t["subtype"], "outcome_real": t["outcome_real"],
                "n_wallets_sospechosas_activas": len(vistas),
                "wallets_vistas": ";".join(sorted(vistas)),
                "resultado_nuestro": "PERDIDA" if t["outcome_real"] == "NO" else "GANANCIA",
            })
            nuevas += 1

    if nuevas:
        print(f"wallet_contraparte_tracker: {nuevas} trades nuevos procesados")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[wallet_contraparte_tracker] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
