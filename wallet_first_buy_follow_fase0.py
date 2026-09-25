#!/usr/bin/env python3
"""wallet_first_buy_follow_fase0.py -- "seguir wallets informadas EMPEZANDO a comprar", FASE 0 en
tiempo real (25-Sep, Javi: "construye"). SOLO OBSERVACIÓN: nunca envía órdenes.

Lee (tail, sondeo 0,2 s) el firehose de trades de hoy (fetch_polymarket_activity_ws.py ->
/root/polymarket-research-datalogs/polymarket_activity_YYYY-MM-DD.csv). Ante la PRIMERA compra de una
wallet de la watchlist (data/shadow/wallet_first_buy/watchlist.json, la genera cada día
wallet_first_buy_fwd_tracker.py con selección congelada) en un mercado 5/15min con tte>=20 s, lee el
libro PÚBLICO del mismo token a OFFSETS_S segundos de la DETECCIÓN y registra ask/bid/profundidad.
Objetivo: medir el ASK REAL al que se podría seguir (el tracker diario usa el precio del siguiente
trade como proxy) y el lag de detección real. El resultado (EV al ask, por bucket de precio) se calcula
después con el resultado oficial; el componente rentable del backtest (25-Sep) fue el LONGSHOT
(pf<0,3: +0,62 EUR/EUR pool 3 días forward, t_cluster 4,0, sin top5 +0,38 t 3,3), no el resto.
-> /root/polymarket-research-datalogs/wallet_first_buy_follow_fase0.csv (fuera de git, ~11 MB/día)
"""
import csv
import json
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt
from resolution_sniper_observer import mercado_slot, token_ids

REPO = Path(__file__).resolve().parent
DATALOGS = Path("/root/polymarket-research-datalogs")
WATCHLIST = REPO / "data" / "shadow" / "wallet_first_buy" / "watchlist.json"
OUT = DATALOGS / "wallet_first_buy_follow_fase0.csv"   # fuera de git: ~11 MB/día
OFFSETS_S = [0.3, 1.0, 3.0]
STAKE = 1.05
POLL_S = 0.2
TTE_MIN = 20
CAMPOS = ["ts_trade", "wallet", "slug", "market_id", "activo", "marco", "outcome", "p_wallet", "usd", "tte_s",
          "lag_deteccion_s", "offset_s", "t_real_s", "ask", "bid", "profundidad_eur", "ratio_vs_stake",
          "lat_libro_ms", "error"]
_lock = threading.Lock()
_pool = ThreadPoolExecutor(max_workers=8)
_vistos = set()


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _escribir(fila):
    with _lock:
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CAMPOS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)


def _libro(token_id):
    book = lt._fetch_book_publico(token_id)
    if book is None:
        return None, None, None, None, "sin respuesta del libro"
    try:
        asks = [(float(l["price"]), float(l["size"])) for l in (book.get("asks") or [])]
        bids = [(float(l["price"]), float(l["size"])) for l in (book.get("bids") or [])]
    except (TypeError, ValueError, KeyError):
        return None, None, None, None, "libro ilegible"
    ask = min((p for p, _ in asks), default=None)
    bid = max((p for p, _ in bids), default=None)
    prof = sum(p * s for p, s in asks if ask is not None and p <= ask * 1.05) if ask is not None else 0.0
    return ask, bid, round(prof, 2), round(prof / STAKE, 1), ""


def _seguir(base, activo, marco, ini, outcome, t_det):
    """Hilo por evento: resuelve el mercado (gamma, cacheado), y lee el libro a cada offset."""
    tag = "5m" if marco == "5min" else "15m"
    try:
        _, mkt = mercado_slot(activo, tag, ini)
    except Exception:
        mkt = None
    tok = None
    if mkt:
        ty, tn = token_ids(mkt)
        tok = ty if outcome == "Up" else tn
        base["market_id"] = mkt.get("id", "")
    for off in OFFSETS_S:
        espera = t_det + off - time.time()
        if espera > 0:
            time.sleep(espera)
        t = time.perf_counter()
        ask, bid, prof, ratio, err = _libro(tok) if tok else (None, None, None, None, "sin_mercado_o_token")
        fila = dict(base)
        fila.update({"offset_s": off, "t_real_s": round(time.time() - t_det, 3), "ask": ask, "bid": bid,
                     "profundidad_eur": prof, "ratio_vs_stake": ratio,
                     "lat_libro_ms": round((time.perf_counter() - t) * 1000), "error": err})
        _escribir(fila)


def _cargar_watchlist(prev):
    try:
        d = json.loads(WATCHLIST.read_text(encoding="utf-8"))
        w = {k.lower() for k in d.get("wallets", {})}
        if w != prev:
            _log(f"watchlist: {len(w)} wallets (para_dia={d.get('para_dia')}, train={d.get('train_dias')})")
        return w
    except Exception:
        return prev


def _fila(linea, cab):
    try:
        r = next(csv.reader([linea]))
        return dict(zip(cab, r)) if len(r) >= len(cab) else None
    except Exception:
        return None


def main():
    _log(f"wallet_first_buy_follow_fase0 arrancado (offsets {OFFSETS_S}, solo observación)")
    watch, t_watch = set(), 0.0
    arch, pos, buf, cab = None, 0, "", None
    while True:
        try:
            ahora = time.time()
            if ahora - t_watch > 300:
                watch, t_watch = _cargar_watchlist(watch), ahora
            hoy = DATALOGS / f"polymarket_activity_{datetime.now(timezone.utc):%Y-%m-%d}.csv"
            if hoy != arch:
                arch, buf, cab = hoy, "", None
                pos = hoy.stat().st_size if hoy.exists() else 0
                _vistos.clear()
            if arch.exists() and watch:
                with open(arch, encoding="utf-8", errors="replace", newline="") as f:
                    if cab is None:
                        cab = next(csv.reader([f.readline()]))
                    f.seek(pos)
                    datos = f.read()
                    pos = f.tell()
                if datos:
                    buf += datos
                    *lineas, buf = buf.split("\n")
                    for ln in lineas:
                        r = _fila(ln, cab) if ln else None
                        if not r or r.get("side") != "BUY" or r.get("marco") not in ("5min", "15min"):
                            continue
                        w = (r.get("wallet") or "").lower()
                        if w not in watch:
                            continue
                        m = re.search(r"-(\d{10})$", r.get("market_slug") or "")
                        if not m:
                            continue
                        key = (r["market_slug"], w, r["outcome"])
                        if key in _vistos:
                            continue
                        _vistos.add(key)
                        ini = int(m.group(1))
                        dur = 300 if r["marco"] == "5min" else 900
                        try:
                            t_tr = datetime.fromisoformat(r["timestamp_utc"].replace("Z", "+00:00")).timestamp()
                        except ValueError:
                            continue
                        tte = ini + dur - t_tr
                        if tte < TTE_MIN:
                            continue
                        t_det = time.time()
                        base = {"ts_trade": r["timestamp_utc"], "wallet": w, "slug": r["market_slug"], "market_id": "",
                                "activo": r["activo"], "marco": r["marco"], "outcome": r["outcome"],
                                "p_wallet": r["price"], "usd": r["usd_value"], "tte_s": round(tte, 1),
                                "lag_deteccion_s": round(t_det - t_tr, 3)}
                        _pool.submit(_seguir, base, r["activo"], r["marco"], ini, r["outcome"], t_det)
            time.sleep(POLL_S)
        except Exception as e:
            _log(f"error en el bucle ({type(e).__name__}: {e})")
            time.sleep(2)


if __name__ == "__main__":
    main()
