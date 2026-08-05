"""
analisis_contraparte_timing_03ago.py — ángulo NUEVO sobre la hipótesis
"contraparte informada" (petición explícita Javi, 03-Ago, tras el
hallazgo de wallet_mirror: la selección adversa que vimos ahí era un
problema de LATENCIA de medición, no de ausencia de señal -- aplicar la
misma lente al contraparte).

Diferencia con wallet_contraparte_tracker.py (REFUTADO 29-Jul, ver
idea_wallet_contraparte_refutado_29jul):
  1. Aquella versión solo miraba PRESENCIA binaria de una wallet de
     `wallets_sospechosas.json` (lista descubierta de forma circular,
     nunca replicó forward) dentro de una ventana de +-120s sin dirección
     de tiempo. Aquí se usa el pool de wallets con edge REALMENTE
     validado (wallet_edge_score_por_activo_marco.json, sig_bhfdr=True,
     edge_pp>0, n>=15 -- el mismo criterio riguroso que ya usa
     wallet_mirror_sniper.py) y se calcula el LAG CON SIGNO (wallet
     operó X segundos ANTES o DESPUÉS de nuestra propia ejecución).
  2. Generalizado a TODAS las tuplas live con trades reales, no solo
     GBM_LATE_15M#{SOL,ETH}#15min#BUY_YES.

Hipótesis a probar: si una wallet con edge validado opera en el lado que
resulta GANADOR, ANTES de que nosotros ejecutemos (lag negativo = wallet
antes que nosotros), eso es una señal de alerta temprana explotable
-- análogo a lo que wallet_mirror hace pero en sentido contrario
(contraparte que nos avisa de que vamos a perder, no que copiamos).

Solo lectura -- no toca live_trade.py/config_live.json/prob_yes. Cachea
condition_id + trade tape por market_id (idempotente, throttle 0.15s)
en data/shadow/contraparte_timing_cache.json para poder repetir sin
regastar llamadas API. Salida: data/shadow/contraparte_timing_03ago.csv.
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
EDGE_SCORE = REPO / "data/shadow/wallet_edge_score_por_activo_marco.json"
CACHE = REPO / "data/shadow/contraparte_timing_cache.json"
OUT = REPO / "data/shadow/contraparte_timing_03ago.csv"
GAMMA = "https://gamma-api.polymarket.com"
DATA_API = "https://data-api.polymarket.com"
H = {"User-Agent": "Mozilla/5.0 (compatible; polymarket-research/1.0)"}
TIMEOUT = 10
VENTANA_S = 300  # +-5min, mas ancho que el original (120s) para no perder señal por timing

_CAMPOS = ["market_id", "strategy", "subtype", "direction", "ts_exec", "outcome_real",
           "resultado_nuestro", "n_validadas_lado_ganador", "n_validadas_lado_perdedor",
           "lag_min_ganador_s", "lags_ganador_s"]


def _cargar_cache():
    if CACHE.exists():
        try:
            return json.loads(CACHE.read_text())
        except Exception:
            return {}
    return {}


def _guardar_cache(c):
    CACHE.write_text(json.dumps(c))


def _condition_id(market_id, cache):
    if market_id in cache.get("cid", {}):
        return cache["cid"][market_id]
    try:
        r = requests.get(f"{GAMMA}/markets/{market_id}", timeout=TIMEOUT, headers=H)
        d = r.json() if r.status_code == 200 else None
        if isinstance(d, list) and d:
            d = d[0]
        cid = d.get("conditionId") if isinstance(d, dict) else None
    except Exception:
        cid = None
    cache.setdefault("cid", {})[market_id] = cid
    return cid


def _trade_tape(cid, cache):
    if cid in cache.get("tape", {}):
        return cache["tape"][cid]
    try:
        r = requests.get(f"{DATA_API}/trades", params={"market": cid, "limit": 500},
                          headers=H, timeout=TIMEOUT)
        tr = r.json() if r.status_code == 200 else []
    except Exception:
        tr = []
    cache.setdefault("tape", {})[cid] = tr
    return tr


def _ya_procesados():
    if not OUT.exists():
        return set()
    with open(OUT, encoding="utf-8") as f:
        return {r["market_id"] for r in csv.DictReader(f)}


def main():
    if not TRADES.exists() or not EDGE_SCORE.exists():
        print("faltan ficheros de entrada"); return 0

    edge_data = json.loads(EDGE_SCORE.read_text())
    validadas = {v["wallet"] for v in edge_data.values()
                 if v.get("sig_bhfdr") and v.get("edge_pp", 0) > 0 and v.get("n", 0) >= 15}
    print(f"wallets con edge validado: {len(validadas)}")

    ya = _ya_procesados()
    cache = _cargar_cache()
    nuevo_archivo = not OUT.exists() or OUT.stat().st_size == 0

    with open(TRADES, encoding="utf-8") as f:
        trades = [r for r in csv.DictReader(f)
                  if r.get("status") == "CLOSED" and r.get("market_id") not in ya]

    print(f"trades reales a procesar: {len(trades)}")

    procesados = 0
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
            cid = _condition_id(mid, cache)
            if not cid:
                continue
            tr = _trade_tape(cid, cache)
            time.sleep(0.15)

            direction = t["direction"]
            ganador_outcome = "Down" if t["outcome_real"] == "NO" else "Up"
            perdedor_outcome = "Up" if ganador_outcome == "Down" else "Down"

            lags_ganador = []
            n_perdedor = 0
            for x in tr:
                try:
                    tt = datetime.fromtimestamp(x["timestamp"], tz=timezone.utc)
                except Exception:
                    continue
                if abs((tt - ts_exec).total_seconds()) > VENTANA_S:
                    continue
                if x.get("side") != "BUY":
                    continue
                pw = x.get("proxyWallet")
                if pw not in validadas:
                    continue
                lag = (tt - ts_exec).total_seconds()
                if x.get("outcome") == ganador_outcome:
                    lags_ganador.append(lag)
                elif x.get("outcome") == perdedor_outcome:
                    n_perdedor += 1

            resultado_nuestro = "GANANCIA" if float(t.get("pnl_neto_eur", 0)) > 0 else "PERDIDA"
            lag_min = min((abs(l) for l in lags_ganador), default=None)
            w.writerow({
                "market_id": mid, "strategy": t["strategy"], "subtype": t["subtype"],
                "direction": direction, "ts_exec": t["timestamp_utc"],
                "outcome_real": t["outcome_real"], "resultado_nuestro": resultado_nuestro,
                "n_validadas_lado_ganador": len(lags_ganador),
                "n_validadas_lado_perdedor": n_perdedor,
                "lag_min_ganador_s": round(lag_min, 2) if lag_min is not None else "",
                "lags_ganador_s": ";".join(f"{l:.1f}" for l in lags_ganador),
            })
            procesados += 1
            if procesados % 20 == 0:
                print(f"  ... {procesados}/{len(trades)} procesados", flush=True)
                _guardar_cache(cache)

    _guardar_cache(cache)
    print(f"Total procesados esta corrida: {procesados}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[analisis_contraparte_timing] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
