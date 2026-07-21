#!/usr/bin/env python3
"""
punto_confirmacion_logger.py — Captura de datos para validar fill-ability en
el "punto de confirmación" por moneda (solo logging, NO ejecuta).

Origen (2026-07-21): analisis conjunto precio×restante_min sobre
ballenas_timing_history.csv (#15min) -- el bucket con MÁS margen de tiempo
donde el límite inferior de un IC de Wilson al 95% ya supera 95% de
acierto, con precio<0.90 (edge real, no solo certeza sin margen):

    BTC: ~1min antes del cierre, precio~0.875  (edge +9.8pp)
    ETH: ~5min antes del cierre, precio~0.875  (edge +9.1pp)
    SOL: ~8min antes del cierre, precio~0.775  (edge +18.6pp)
    XRP: ~13min antes del cierre, precio~0.725 (edge +22.7pp)

Ese dato viene de compras REALES de ballenas -- confirma que el edge
existe, pero no dice si el LIBRO aguanta una orden nuestra justo ahí.
Cruce con libro_snapshots.csv (señales que ya hemos disparado, aunque no
apuntaran a este punto a propósito) dio: BTC n=0, XRP n=0 (sin dato),
ETH n=11 (45.5% fillable), SOL n=63 (69.8% fillable) -- insuficiente para
concluir en las 4, especialmente BTC/XRP sin ningún dato.

Este logger captura DELIBERADAMENTE el libro del lado favorito (precio>0.5)
en cada mercado #15min de BTC/ETH/SOL/XRP, en el instante exacto de cada
punto (con tolerancia), sin filtrar por precio en captura (se filtra en el
análisis) -- para no perder ocurrencias por un gate demasiado estricto.
Resuelve el outcome oficial después, igual que photo_finish_logger.py.

Puramente observacional: no toca prob_yes, no ejecuta, no decide nada.

Corre en screen propio:
  screen -dmS puntoconf bash -c "cd /root/polymarket-research && .venv/bin/python punto_confirmacion_logger.py >> logs/punto_confirmacion.log 2>&1"
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

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"
TIMEOUT = 5

VENTANA_MIN = 15
# activo -> (segundos antes del cierre a capturar, tolerancia en segundos)
OBJETIVOS_S = {
    "btc": (60, 20),
    "eth": (300, 30),
    "sol": (480, 40),
    "xrp": (780, 45),
}
RESOLVE_DELAY_S = 90

COLUMNS = [
    "timestamp_utc", "slug", "market_id", "condition_id", "activo",
    "end_date", "restante_s_objetivo", "restante_s_real",
    "precio_yes", "lado_favorito", "best_ask_favorito", "ask_usd_le5c",
    "best_bid_favorito", "profundidad_favorito_usd", "n_niveles_favorito",
    "outcome_real", "favorito_gano",
]


def _log(msg: str):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _csv_path(dt: datetime) -> Path:
    return DIR_SHADOW / f"punto_confirmacion_{dt.strftime('%Y-%m-%d')}.csv"


def mercado_slot(asset: str, ts_start: int):
    slug = f"{asset}-updown-{VENTANA_MIN}m-{ts_start}"
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


def libro(token_id: str):
    """(best_ask, usd<=5c, best_bid, profundidad_usd_total, n_niveles)."""
    try:
        r = requests.get(f"{CLOB}/book", params={"token_id": token_id}, timeout=TIMEOUT)
        if r.status_code != 200:
            return None
        b = r.json()
        asks = [(float(a["price"]), float(a["size"])) for a in (b.get("asks") or [])]
        best_ask = min((p for p, _ in asks), default=None)
        best_bid = max((float(a["price"]) for a in (b.get("bids") or [])), default=None)
        le5 = round(sum(p * s for p, s in asks if best_ask is not None and p <= best_ask + 0.05), 2)
        profundidad = round(sum(p * s for p, s in asks), 2)
        return best_ask, le5, best_bid, profundidad, len(asks)
    except Exception:
        return None


def outcome_oficial(market_id: str):
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


def snapshot_asset(asset: str, ts_end: int, objetivo_s: int):
    ts_start = ts_end - VENTANA_MIN * 60
    slug, mkt = mercado_slot(asset, ts_start)
    if not mkt:
        return None
    try:
        tokens = json.loads(mkt.get("clobTokenIds") or "[]")
        pr = mkt.get("outcomePrices")
        pr = json.loads(pr) if isinstance(pr, str) else pr
        py_yes = float(pr[0]) if pr else None
    except Exception:
        return None
    if len(tokens) < 2 or py_yes is None:
        return None

    lado_favorito = "Up" if py_yes >= 0.5 else "Down"
    token_fav = tokens[0] if lado_favorito == "Up" else tokens[1]
    lb = libro(token_fav)
    if lb is None:
        return None
    best_ask, le5, best_bid, profundidad, n_niveles = lb

    now = datetime.now(timezone.utc)
    return {
        "timestamp_utc": now.isoformat(timespec="seconds"),
        "slug": slug,
        "market_id": mkt.get("id", ""),
        "condition_id": mkt.get("conditionId", ""),
        "activo": asset.upper(),
        "end_date": datetime.fromtimestamp(ts_end, timezone.utc).isoformat(timespec="seconds"),
        "restante_s_objetivo": objetivo_s,
        "restante_s_real": round(ts_end - now.timestamp(), 1),
        "precio_yes": py_yes,
        "lado_favorito": lado_favorito,
        "best_ask_favorito": best_ask if best_ask is not None else "",
        "ask_usd_le5c": le5,
        "best_bid_favorito": best_bid if best_bid is not None else "",
        "profundidad_favorito_usd": profundidad,
        "n_niveles_favorito": n_niveles,
        "outcome_real": "",
        "favorito_gano": "",
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


def resolver_pendientes():
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
                r["favorito_gano"] = "1" if out == r["lado_favorito"] else "0"
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


def main():
    _log(f"punto_confirmacion_logger arrancado — objetivos(s antes del cierre): {OBJETIVOS_S}")
    while True:
        now = time.time()
        ts_end = (int(now) // (VENTANA_MIN * 60) + 1) * (VENTANA_MIN * 60)

        eventos = sorted(
            (ts_end - obj_s, asset, obj_s) for asset, (obj_s, _tol) in OBJETIVOS_S.items()
        )
        for despertar, asset, obj_s in eventos:
            if despertar <= time.time():
                continue
            try:
                resolver_pendientes()
            except Exception as e:
                _log(f"resolver error: {e}")
            resto = despertar - time.time()
            if resto > 0:
                time.sleep(resto)
            fila = None
            try:
                fila = snapshot_asset(asset, ts_end, obj_s)
            except Exception as e:
                _log(f"snapshot error {asset}: {e}")
            if fila:
                guardar([fila])
                _log(f"{fila['activo']} objetivo={obj_s}s real={fila['restante_s_real']}s "
                     f"precio_yes={fila['precio_yes']} favorito={fila['lado_favorito']} "
                     f"ask={fila['best_ask_favorito']} prof=${fila['profundidad_favorito_usd']}")

        time.sleep(max(0, ts_end + 5 - time.time()))


if __name__ == "__main__":
    main()
