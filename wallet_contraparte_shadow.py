#!/usr/bin/env python3
"""Extiende wallet_contraparte_tracker.py a las señales SHADOW resueltas
(no solo las 97 ejecutadas en vivo) — mismo método, mismas wallets de
data/shadow/wallets_sospechosas.json, misma ventana ±120s alrededor del
timestamp de la señal.

Por qué: wallet_contraparte_tracker.py lleva desde el 12-Jul sin acumular
ni un solo trade nuevo (0 trades GBM_LATE_15M SOL/ETH#15min BUY_YES en vivo
desde la fecha de descubrimiento — fin de semana + ventana estrecha). Los
n=97 que reportaba "forward" en la memoria del 12-Jul son en realidad la
MISMA población 03-11jul que se usó para descubrir las wallets (z-test
pérdidas vs ganancias) — circular, no forward de verdad. Shadow resuelve
~90-100 señales/día de este mismo subtype (9x más que las ejecutadas en
vivo) porque no está limitado por ventana horaria ni por veto de
profundidad — permite acumular n de validación genuina mucho más rápido.

Columna `es_forward`: True solo si prediction_timestamp >= FORWARD_CUTOFF
(fecha de descubrimiento de la semilla, 2026-07-12). Cualquier análisis
sobre este CSV debe filtrar por es_forward antes de sacar conclusiones —
las filas anteriores son del mismo periodo usado para descubrir las
wallets y NO cuentan como validación independiente.

Asíncrono y post-hoc, igual que wallet_contraparte_tracker.py — NO añade
ninguna llamada a la ruta de ejecución en vivo. Read-only sobre
config/dinero. Log en data/shadow/wallet_contraparte_shadow.csv,
idempotente por market_id.
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

RESULTS = REPO / "data/shadow/results.csv"
SOSPECHOSAS = REPO / "data/shadow/wallets_sospechosas.json"
OUT = REPO / "data/shadow/wallet_contraparte_shadow.csv"
GAMMA = "https://gamma-api.polymarket.com"
DATA_API = "https://data-api.polymarket.com"
H = {"User-Agent": "Mozilla/5.0 (compatible; polymarket-research/1.0)"}
TIMEOUT = 10
VENTANA_S = 120
FORWARD_CUTOFF = datetime(2026, 7, 12, tzinfo=timezone.utc)
MAX_POR_CICLO = 150  # tope de llamadas API por ejecución (cron horario)

_CAMPOS = ["market_id", "subtype", "prediction_timestamp", "outcome_real",
           "n_wallets_sospechosas_activas", "wallets_vistas",
           "resultado_shadow", "es_forward"]


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
    if not RESULTS.exists() or not SOSPECHOSAS.exists():
        return 0
    sospechosas = set(json.loads(SOSPECHOSAS.read_text()).get("wallets", {}).keys())
    ya = _ya_procesados()
    nuevo_archivo = not OUT.exists() or OUT.stat().st_size == 0

    with open(RESULTS, encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f)
                if r.get("strategy") == "GBM_LATE_15M" and r.get("decision") == "BUY_YES"
                and r.get("subtype") in ("SOL#15min", "ETH#15min")
                and str(r.get("market_id")) not in ya]

    # más recientes primero: si hay backlog, prioriza acumular n forward ya
    rows.sort(key=lambda r: r.get("prediction_timestamp", ""), reverse=True)
    rows = rows[:MAX_POR_CICLO]

    nuevas = 0
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=_CAMPOS)
        if nuevo_archivo:
            w.writeheader()
        for r in rows:
            mid = str(r["market_id"])
            try:
                ts0 = datetime.fromisoformat(r["prediction_timestamp"].replace("Z", "+00:00"))
            except Exception:
                continue
            cid = _condition_id(mid)
            if not cid:
                continue
            try:
                resp = requests.get(f"{DATA_API}/trades", params={"market": cid, "limit": 200},
                                     headers=H, timeout=TIMEOUT)
                tr = resp.json() if resp.status_code == 200 else []
            except Exception:
                tr = []
            time.sleep(0.15)

            outcome_real = r["outcome_real"]
            lado_ganador = "Down" if outcome_real == "NO" else "Up"
            vistas = set()
            for x in tr:
                try:
                    tt = datetime.fromtimestamp(x["timestamp"], tz=timezone.utc)
                except Exception:
                    continue
                if abs((tt - ts0).total_seconds()) > VENTANA_S:
                    continue
                if x.get("outcome") == lado_ganador and x.get("side") == "BUY":
                    pw = x.get("proxyWallet")
                    if pw in sospechosas:
                        vistas.add(pw)

            w.writerow({
                "market_id": mid, "subtype": r["subtype"],
                "prediction_timestamp": r["prediction_timestamp"],
                "outcome_real": outcome_real,
                "n_wallets_sospechosas_activas": len(vistas),
                "wallets_vistas": ";".join(sorted(vistas)),
                "resultado_shadow": "PERDIDA" if outcome_real == "NO" else "GANANCIA",
                "es_forward": int(ts0 >= FORWARD_CUTOFF),
            })
            nuevas += 1

    if nuevas:
        print(f"wallet_contraparte_shadow: {nuevas} señales shadow nuevas procesadas")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[wallet_contraparte_shadow] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
