#!/usr/bin/env python3
"""maker_pilot_sim.py — sigue testeando el piloto maker-sobre-vetadas SIN dinero
real, tras apagarlo el 12-Jul (n=8, hit 37.5%, -11.08€, ver config_live.json
maker_pilot._nota_apagado_2026-07-12).

Reusa la población elegible REAL del piloto (libro_snapshots.csv motivo=
veto_profundidad — señal que ya pasó todos los gates de live_trade y solo
murió por profundidad de libro) y la MISMA fórmula de precio que usaba la
orden real (precio_limit = min(precio_plan, mejor_ask-0.01), ver
live_trade._colocar_orden_maker). Método de fill idéntico al ya usado en
maker_sim.py / analisis_maker_xrp_tardio.py: print real en el tape público
(data-api/trades) a precio<=limit dentro de [snapshot_ts, end_date-cancelar].

Solo lectura (gamma-api + data-api), no coloca ninguna orden ni toca CLOB.
Idempotente: solo procesa (market_id, direction) que no estén ya en
data/shadow/maker_pilot_sim.csv. Pensado para cron periódico.
"""
import csv
import json
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
LIBRO = REPO / "data/live/libro_snapshots.csv"
RESULTS = REPO / "data/shadow/results.csv"
CONFIG = REPO / "data/live/config_live.json"
OUT = REPO / "data/shadow/maker_pilot_sim.csv"
GAMMA_API = "https://gamma-api.polymarket.com"
DATA_API = "https://data-api.polymarket.com"
H = {"User-Agent": "Mozilla/5.0 (compatible; polymarket-research/1.0)"}
TIMEOUT = 10
REQUOTE_PRECIO_MAX = 0.95  # mismo tope que live_trade.REQUOTE_PRECIO_MAX

_CAMPOS = ["market_id", "strategy", "subtype", "direction", "precio_plan",
           "precio_limit", "mejor_ask_veto", "ts_snapshot", "end_date",
           "filled", "acierto", "pnl1_maker"]


def _parse_ts(s):
    try:
        dt = datetime.fromisoformat((s or "").replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except Exception:
        return None


def _cancelar_antes_fin_seg():
    try:
        cfg = json.loads(CONFIG.read_text()).get("maker_pilot", {})
        return int(cfg.get("cancelar_antes_fin_seg", 240))
    except Exception:
        return 240


def _ya_procesados():
    if not OUT.exists():
        return set()
    with open(OUT, encoding="utf-8") as f:
        return {(r["market_id"], r["direction"]) for r in csv.DictReader(f)}


def _primeras_vetos():
    """Primera snapshot veto_profundidad por (market_id, direction) — momento
    en que la orden maker real se habría colocado."""
    primeras = {}
    with open(LIBRO, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("motivo") != "veto_profundidad":
                continue
            k = (row["market_id"], row["direction"])
            if k not in primeras or row["timestamp_utc"] < primeras[k]["timestamp_utc"]:
                primeras[k] = row
    return primeras


def _resultados_idx():
    idx = {}
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            idx[(row["market_id"], row["decision"])] = row
    return idx


def _condition_id(market_id, cache):
    if market_id in cache:
        return cache[market_id]
    try:
        r = requests.get(f"{GAMMA_API}/markets/{market_id}", timeout=TIMEOUT, headers=H)
        data = r.json() if r.status_code == 200 else None
        if isinstance(data, list) and data:
            data = data[0]
        cid = data.get("conditionId") if isinstance(data, dict) else None
    except Exception:
        cid = None
    cache[market_id] = cid
    return cid


def _trades_de(cond_id):
    try:
        r = requests.get(f"{DATA_API}/trades", params={"market": cond_id, "limit": 500},
                          headers=H, timeout=TIMEOUT)
        return (r.json() or []) if r.status_code == 200 else []
    except Exception:
        return []


def main():
    if not LIBRO.exists() or not RESULTS.exists():
        return
    cancel_seg = _cancelar_antes_fin_seg()
    ya = _ya_procesados()
    vetos = _primeras_vetos()
    resultados = _resultados_idx()
    cache_cid = {}
    nuevas = 0

    nuevo_archivo = not OUT.exists() or OUT.stat().st_size == 0
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=_CAMPOS)
        if nuevo_archivo:
            w.writeheader()

        for (mid, direction), snap in vetos.items():
            if (mid, direction) in ya:
                continue
            res = resultados.get((mid, direction))
            if not res or res.get("acierto") not in ("0", "1", "True", "False"):
                continue  # todavía sin resolver, se reintenta el próximo run

            precio_plan = float(snap.get("precio_plan") or 0)
            mejor_ask = float(snap.get("mejor_ask") or 0)
            if mejor_ask <= 0:
                continue
            precio_limit = round(min(precio_plan, mejor_ask - 0.01), 2)
            if precio_limit < 0.01 or precio_limit > REQUOTE_PRECIO_MAX:
                continue

            t0 = _parse_ts(snap.get("timestamp_utc"))
            end = _parse_ts(res.get("end_date"))
            if not t0 or not end:
                continue
            t1 = end - timedelta(seconds=cancel_seg)
            if t1 <= t0:
                continue

            cid = _condition_id(mid, cache_cid)
            if not cid:
                continue
            trades = _trades_de(cid)
            time.sleep(0.15)

            lado = "Up" if direction == "BUY_YES" else "Down"
            filled = 0
            for t in trades:
                if t.get("outcome") != lado:
                    continue
                try:
                    p = float(t.get("price") or 0)
                    tt = datetime.fromtimestamp(int(t["timestamp"]), tz=timezone.utc)
                except Exception:
                    continue
                if p <= precio_limit and t0 <= tt <= t1:
                    filled = 1
                    break

            acierto = res.get("acierto") in ("1", "True")
            pnl1 = (round(1 / precio_limit - 1, 4) if acierto else -1.0) if filled else 0.0

            w.writerow({
                "market_id": mid, "strategy": snap.get("strategy", ""),
                "subtype": snap.get("subtype", ""), "direction": direction,
                "precio_plan": precio_plan, "precio_limit": precio_limit,
                "mejor_ask_veto": mejor_ask, "ts_snapshot": snap.get("timestamp_utc"),
                "end_date": res.get("end_date"), "filled": filled,
                "acierto": int(acierto), "pnl1_maker": pnl1,
            })
            nuevas += 1

    if nuevas:
        print(f"maker_pilot_sim: {nuevas} señales nuevas simuladas")


if __name__ == "__main__":
    main()
