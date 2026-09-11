#!/usr/bin/env python3
"""
photo_finish_logger.py — Captura de datos para PHOTO_FINISH_SNIPER (solo logging, NO ejecuta).

Origen (2026-07-05): wallet 'egig' verificada on-chain (+$41k leaderboard oficial,
+$1.4k/día) compra el lado rezagado a 1-3c en los últimos ~2s de ventanas 5min
cuando el spot está pegado al strike (mediana 0.027% de distancia). El mercado
cobra los finales de foto como decididos cuando son ~moneda al aire.

Este logger acumula el dataset para evaluar la estrategia shadow-first:
en cada frontera de ventana 5m/15m, si |spot vs strike| < UMBRAL_DIST_PCT,
registra el libro del lado rezagado a T-~10s y luego resuelve el outcome
con outcomePrices oficial de Polymarket (no con nuestro spot — en un final
de foto el oráculo es LA verdad, nuestro spot es aproximación).

Criterio de avance (definido a priori, ver H-CUSTOM-PHOTO-FINISH-SNIPER):
n≥200 snapshots con ask≤0.05 y profundidad>0 → medir win rate real del lado
rezagado vs precio del ask. Si EV>2x sostenido → proponer watcher de ejecución.

Corre en screen propio:  screen -dmS pfinish bash -c "cd /root/polymarket-research && .venv/bin/python photo_finish_logger.py >> logs/photo_finish.log 2>&1"
"""

import csv
import json
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
DIR_KLINES = REPO / "data" / "binance"
DIR_PRICES = REPO / "data" / "prices"

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"
BINANCE = "https://api.binance.com/api/v3/ticker/price"
TIMEOUT = 5

ASSETS = ["btc", "eth", "sol", "xrp", "doge", "bnb"]
BINANCE_SYMBOL = {a: f"{a.upper()}USDT" for a in ASSETS}

# Umbral de captura: generoso a propósito (egig opera con mediana 0.027%, p75 0.043%).
# El corte fino se hace en el análisis; aquí solo se decide qué merece una llamada al libro.
UMBRAL_DIST_PCT = 0.15
ANTICIPO_S = 12          # despertar T_end - ANTICIPO_S
RESOLVE_DELAY_S = 90     # esperar tras end_date antes de pedir outcomePrices

COLUMNS = [
    "timestamp_utc", "slug", "market_id", "condition_id", "activo", "ventana_min",
    "end_date", "restante_s", "strike", "strike_src", "spot", "spot_src", "dist_pct",
    "lado_rezagado", "best_ask", "ask_usd_le2c", "ask_usd_le3c", "ask_usd_le5c",
    "best_bid", "py_yes_evento", "outcome_real", "rezagado_gano",
]


def _log(msg: str):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _csv_path(dt: datetime) -> Path:
    return DIR_SHADOW / f"photo_finish_{dt.strftime('%Y-%m-%d')}.csv"


# ── precios ────────────────────────────────────────────────────────────────

def spot_binance(asset: str):
    try:
        r = requests.get(BINANCE, params={"symbol": BINANCE_SYMBOL[asset]}, timeout=3)
        if r.status_code == 200:
            return float(r.json()["price"]), "binance_ticker"
    except Exception:
        pass
    return None, None


def strike_de_klines(asset: str, ts_start: int):
    """Open del kline 1min del minuto de apertura de la ventana (buffer rodante)."""
    sym = asset.upper()
    hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for fecha in (hoy,):
        f = DIR_KLINES / f"klines_{fecha}.json"
        if not f.exists():
            continue
        try:
            k = json.load(open(f))
            for row in k.get(sym, []):
                if int(row[0]) // 1000 == ts_start:
                    return float(row[1]), "kline_open"
        except Exception:
            pass
    return None, None


def strike_de_prices(asset: str, ts_start: int, tol_s: int = 90):
    """Fallback: fila de prices CSV más cercana al inicio de ventana (fuente != coingecko)."""
    sym = asset.upper()
    hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    f = DIR_PRICES / f"{hoy}.csv"
    if not f.exists():
        return None, None
    best = None
    try:
        with open(f, encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                if r.get("asset") != sym or r.get("source") == "coingecko":
                    continue
                ts = int(datetime.fromisoformat(
                    r["timestamp_utc"].replace("Z", "+00:00")).timestamp())
                d = abs(ts - ts_start)
                if d <= tol_s and (best is None or d < best[0]):
                    best = (d, float(r["price_usd"]))
    except Exception:
        return None, None
    return (best[1], "prices_csv") if best else (None, None)


# ── polymarket ─────────────────────────────────────────────────────────────

def mercado_slot(asset: str, ventana_min: int, ts_start: int):
    slug = f"{asset}-updown-{ventana_min}m-{ts_start}"
    try:
        r = requests.get(f"{GAMMA}/events", params={"slug": slug}, timeout=TIMEOUT)
        if r.status_code != 200:
            return slug, None
        ev = r.json()
        if not ev or not ev[0].get("markets"):
            return slug, None
        return slug, ev[0]["markets"][0]
    except Exception:
        return slug, None


def libro_asks(token_id: str):
    """(best_ask, usd≤2c, usd≤3c, usd≤5c, best_bid) del libro del token."""
    try:
        r = requests.get(f"{CLOB}/book", params={"token_id": token_id}, timeout=TIMEOUT)
        if r.status_code != 200:
            return None
        b = r.json()
        asks = [(float(a["price"]), float(a["size"])) for a in (b.get("asks") or [])]
        bids = [(float(a["price"]), float(a["size"])) for a in (b.get("bids") or [])]
        best_ask = min((p for p, _ in asks), default=None)
        best_bid = max((p for p, _ in bids), default=None)
        usd = lambda tope: round(sum(p * s for p, s in asks if p <= tope), 2)
        return best_ask, usd(0.02), usd(0.03), usd(0.05), best_bid
    except Exception:
        return None


def outcome_oficial(market_id: str):
    """'Up'/'Down' desde outcomePrices oficial, o None si aún no resuelto."""
    try:
        r = requests.get(f"{GAMMA}/markets/{market_id}", timeout=TIMEOUT)
        if r.status_code != 200:
            return None
        m = r.json()
        pr = m.get("outcomePrices")
        pr = json.loads(pr) if isinstance(pr, str) else pr
        if not pr or len(pr) < 2:
            return None
        if float(pr[0]) >= 0.999:
            return "Up"
        if float(pr[1]) >= 0.999:
            return "Down"
    except Exception:
        pass
    return None


# ── snapshot ───────────────────────────────────────────────────────────────

def snapshot_asset(asset: str, ventana_min: int, ts_end: int):
    ts_start = ts_end - ventana_min * 60
    spot, spot_src = spot_binance(asset)
    if spot is None:
        return None
    strike, strike_src = strike_de_klines(asset, ts_start)
    if strike is None:
        strike, strike_src = strike_de_prices(asset, ts_start)
    if strike is None:
        return None
    dist_pct = (spot / strike - 1) * 100
    if abs(dist_pct) > UMBRAL_DIST_PCT:
        return None

    slug, mkt = mercado_slot(asset, ventana_min, ts_start)
    if not mkt:
        return None
    try:
        tokens = json.loads(mkt.get("clobTokenIds") or "[]")
        pr = mkt.get("outcomePrices")
        pr = json.loads(pr) if isinstance(pr, str) else pr
        py_yes = float(pr[0]) if pr else ""
    except Exception:
        return None
    if len(tokens) < 2:
        return None

    # índice 0 = Up/YES, 1 = Down/NO (convención outcomePrices ya usada en shadow_predict)
    lado_rezagado = "Down" if dist_pct > 0 else "Up"
    token_rez = tokens[1] if lado_rezagado == "Down" else tokens[0]
    libro = libro_asks(token_rez)
    if libro is None:
        return None
    best_ask, le2, le3, le5, best_bid = libro

    now = datetime.now(timezone.utc)
    return {
        "timestamp_utc": now.isoformat(timespec="seconds"),
        "slug": slug,
        "market_id": mkt.get("id", ""),
        "condition_id": mkt.get("conditionId", ""),
        "activo": asset.upper(),
        "ventana_min": ventana_min,
        "end_date": datetime.fromtimestamp(ts_end, timezone.utc).isoformat(timespec="seconds"),
        "restante_s": round(ts_end - now.timestamp(), 1),
        "strike": strike,
        "strike_src": strike_src,
        "spot": spot,
        "spot_src": spot_src,
        "dist_pct": round(dist_pct, 5),
        "lado_rezagado": lado_rezagado,
        "best_ask": best_ask if best_ask is not None else "",
        "ask_usd_le2c": le2,
        "ask_usd_le3c": le3,
        "ask_usd_le5c": le5,
        "best_bid": best_bid if best_bid is not None else "",
        "py_yes_evento": py_yes,
        "outcome_real": "",
        "rezagado_gano": "",
    }


def guardar(filas: list):
    if not filas:
        return
    path = _csv_path(datetime.now(timezone.utc))
    nuevo = not path.exists()
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        if nuevo:
            w.writeheader()
        for fila in filas:
            w.writerow(fila)


# ── resolver ───────────────────────────────────────────────────────────────

def resolver_pendientes():
    """Rellena outcome_real/rezagado_gano con outcomePrices oficial (hoy + ayer)."""
    ahora = datetime.now(timezone.utc)
    for delta_dias in (0, 1):
        dt = datetime.fromtimestamp(ahora.timestamp() - delta_dias * 86400, timezone.utc)
        path = _csv_path(dt)
        if not path.exists():
            continue
        with open(path, encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        cambiado = False
        for r in rows:
            if r["outcome_real"] or not r["market_id"]:
                continue
            end = datetime.fromisoformat(r["end_date"])
            if end.tzinfo is None:
                end = end.replace(tzinfo=timezone.utc)
            if (ahora - end).total_seconds() < RESOLVE_DELAY_S:
                continue
            out = outcome_oficial(r["market_id"])
            if out:
                r["outcome_real"] = out
                r["rezagado_gano"] = "1" if out == r["lado_rezagado"] else "0"
                cambiado = True
        if cambiado:
            tmp = path.with_suffix(".tmp")
            with open(tmp, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=COLUMNS)
                w.writeheader()
                w.writerows(rows)
            tmp.replace(path)
            n_res = sum(1 for r in rows if r["outcome_real"])
            _log(f"resolver: {path.name} {n_res}/{len(rows)} resueltas")


# ── loop ───────────────────────────────────────────────────────────────────

def main():
    _log(f"photo_finish_logger arrancado — umbral dist {UMBRAL_DIST_PCT}% | anticipo {ANTICIPO_S}s")
    while True:
        now = time.time()
        ts_end = (int(now) // 300 + 1) * 300           # próxima frontera 5min
        despertar = ts_end - ANTICIPO_S
        if despertar > now:
            try:
                resolver_pendientes()
            except Exception as e:
                _log(f"resolver error: {e}")
            resto = despertar - time.time()
            if resto > 0:
                time.sleep(resto)

        ventanas = [5]
        if ts_end % 900 == 0:
            ventanas.append(15)

        trabajos = [(a, v) for v in ventanas for a in ASSETS]
        filas = []
        with ThreadPoolExecutor(max_workers=len(trabajos)) as ex:
            futs = [ex.submit(snapshot_asset, a, v, ts_end) for a, v in trabajos]
            for fu in futs:
                try:
                    r = fu.result(timeout=ANTICIPO_S)
                    if r:
                        filas.append(r)
                except Exception:
                    pass
        guardar(filas)
        if filas:
            det = " | ".join(f"{f['activo']}#{f['ventana_min']}m d={f['dist_pct']:+.4f}% "
                             f"ask={f['best_ask']} ${f['ask_usd_le5c']}" for f in filas)
            _log(f"frontera {datetime.fromtimestamp(ts_end, timezone.utc).strftime('%H:%M')}: "
                 f"{len(filas)} photo finish → {det}")
        time.sleep(max(0, ts_end + 5 - time.time()))


if __name__ == "__main__":
    main()
