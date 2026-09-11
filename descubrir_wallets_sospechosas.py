#!/usr/bin/env python3
"""Re-descubrimiento periódico de wallets contraparte tóxicas — la semilla
de data/shadow/wallets_sospechosas.json (12-Jul) es estática; un market
maker nuevo que empiece a operar la semana que viene sería invisible para
wallet_contraparte_tracker.py (que solo SIGUE a las wallets ya conocidas,
nunca descubre otras nuevas). Propuesta #5 lista puntos ciegos (13-Jul).

Mismo método validado el 12-Jul: compara wallets activas en el lado
ganador de nuestras últimas N pérdidas reales (GBM_LATE_15M SOL/ETH
BUY_YES) vs nuestras últimas N ganancias (control), z-test de proporciones.
Cualquier wallet con z>=UMBRAL_Z se AÑADE a wallets_sospechosas.json
(merge, nunca se borran las ya conocidas) para que wallet_contraparte_
tracker.py empiece a seguirla también.

Pensado para cron semanal (coste de API no trivial: 2 llamadas por
mercado). Solo lectura salvo la propia actualización de la semilla —
no toca dinero ni config_live.json.
"""
import csv
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

TRADES = REPO / "data/live/trades.csv"
SOSPECHOSAS = REPO / "data/shadow/wallets_sospechosas.json"
GAMMA = "https://gamma-api.polymarket.com"
DATA_API = "https://data-api.polymarket.com"
H = {"User-Agent": "Mozilla/5.0 (compatible; polymarket-research/1.0)"}
TIMEOUT = 10
VENTANA_S = 120
N_MUESTRA = 60      # últimas N pérdidas / N ganancias
UMBRAL_Z = 2.0
UMBRAL_N_MIN_WALLET = 3  # no fiarse de una wallet vista en <3 mercados


def _condition_id(market_id):
    try:
        r = requests.get(f"{GAMMA}/markets/{market_id}", headers=H, timeout=TIMEOUT)
        d = r.json() if r.status_code == 200 else None
        if isinstance(d, list) and d:
            d = d[0]
        return d.get("conditionId") if isinstance(d, dict) else None
    except Exception:
        return None


def _trades_tape(cond_id):
    try:
        r = requests.get(f"{DATA_API}/trades", params={"market": cond_id, "limit": 200},
                          headers=H, timeout=TIMEOUT)
        return r.json() if r.status_code == 200 else []
    except Exception:
        return []


def _wallets_por_lado(muestra, lado_fn):
    """Devuelve {wallet: set(market_ids)} de quien compró el lado indicado
    (lado_fn(trade) -> 'Up'/'Down') en ventana ±VENTANA_S de la ejecución."""
    resultado = {}
    for t in muestra:
        mid = t["market_id"]
        try:
            ts0 = datetime.fromisoformat(t["timestamp_utc"].replace("Z", "+00:00"))
        except Exception:
            continue
        cid = _condition_id(mid)
        if not cid:
            continue
        tape = _trades_tape(cid)
        time.sleep(0.15)
        lado = lado_fn(t)
        for x in tape:
            try:
                tt = datetime.fromtimestamp(x["timestamp"], tz=timezone.utc)
            except Exception:
                continue
            if abs((tt - ts0).total_seconds()) > VENTANA_S:
                continue
            if x.get("outcome") == lado and x.get("side") == "BUY":
                w = x.get("proxyWallet")
                if w:
                    resultado.setdefault(w, set()).add(mid)
    return resultado


def main():
    if not TRADES.exists():
        return
    trades = list(csv.DictReader(open(TRADES, encoding="utf-8")))
    base = [t for t in trades if t["strategy"] == "GBM_LATE_15M" and t["direction"] == "BUY_YES"
            and t["subtype"] in ("SOL#15min", "ETH#15min") and t["status"] == "CLOSED"
            and "maker_pilot=1" not in t["notas"]]

    perdidas = [t for t in base if t["outcome_real"] == "NO"][-N_MUESTRA:]
    ganadas = [t for t in base if t["outcome_real"] == "YES"][-N_MUESTRA:]
    print(f"Muestra: {len(perdidas)} pérdidas / {len(ganadas)} ganancias (últimas {N_MUESTRA} c/u)")

    n_p, n_g = len(perdidas), len(ganadas)
    if n_p < 15 or n_g < 15:
        print("Muestra insuficiente, abortando (n<15 en algún lado).")
        return

    wm_perdidas = _wallets_por_lado(perdidas, lambda t: "Down" if t["direction"] == "BUY_YES" else "Up")
    wm_ganadas = _wallets_por_lado(ganadas, lambda t: "Down" if t["direction"] == "BUY_YES" else "Up")

    try:
        semilla = json.loads(SOSPECHOSAS.read_text())
    except Exception:
        semilla = {"wallets": {}}
    ya_conocidas = set(semilla.get("wallets", {}).keys())

    nuevas = []
    todas = set(wm_perdidas) | set(wm_ganadas)
    for w in todas:
        cp, cg = len(wm_perdidas.get(w, [])), len(wm_ganadas.get(w, []))
        if cp < UMBRAL_N_MIN_WALLET:
            continue
        p1, p2 = cp / n_p, cg / n_g
        p_pool = (cp + cg) / (n_p + n_g)
        se = math.sqrt(p_pool * (1 - p_pool) * (1 / n_p + 1 / n_g)) if 0 < p_pool < 1 else 0
        z = (p1 - p2) / se if se > 0 else 0
        if z >= UMBRAL_Z and w not in ya_conocidas:
            nuevas.append((w, z, cp, cg))

    print(f"Wallets nuevas con z>={UMBRAL_Z}: {len(nuevas)}")
    for w, z, cp, cg in nuevas:
        print(f"  {w}: z={z:+.2f} perdidas={cp}/{n_p} ganadas={cg}/{n_g}")
        semilla["wallets"][w] = {
            "z_inicial": round(z, 2), "clasificacion": "por_verificar",
            "descubierta": datetime.now(timezone.utc).date().isoformat(),
            "n_perdidas_muestra": cp, "n_ganadas_muestra": cg,
        }

    if nuevas:
        SOSPECHOSAS.write_text(json.dumps(semilla, ensure_ascii=False, indent=2))
        print(f"wallets_sospechosas.json actualizado: {len(semilla['wallets'])} wallets totales")
    else:
        print("Sin cambios en la semilla.")


if __name__ == "__main__":
    main()
