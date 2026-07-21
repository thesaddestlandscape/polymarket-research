#!/usr/bin/env python3
"""
punto_confirmacion_logger.py — Captura de datos para validar fill-ability en
el "punto de confirmación" por (moneda, marco temporal) (solo logging, NO
ejecuta).

Origen (2026-07-21): análisis conjunto precio×restante_min sobre
ballenas_timing_history.csv (5min/15min/60min/240min/weekly, las 5 monedas)
-- el bucket con MÁS margen de tiempo donde el límite inferior de un IC de
Wilson al 95% ya supera 95% de acierto, con precio<0.90 (edge real, no solo
certeza sin margen). 240min y weekly no dieron ningún punto con n>=30
(probablemente falta de dato, esos marcos resuelven poco -- no "no existe").
Los que sí cualifican, TODOS cubiertos aquí (petición explícita Javi:
"no podemos dejar escapar nada"):

    ETH#5min:  ~3min antes del cierre, precio~0.825  (edge +16.5pp)
    SOL#5min:  ~4min antes del cierre, precio~0.825  (edge +17.4pp)
    BTC#15min: ~1min antes del cierre, precio~0.875  (edge +12.3pp)
    ETH#15min: ~5min antes del cierre, precio~0.875  (edge +11.6pp)
    SOL#15min: ~8min antes del cierre, precio~0.875  (edge +10.8pp)
    XRP#15min: ~13min antes del cierre, precio~0.725 (edge +25.2pp)
    ETH#60min: ~20min antes del cierre, precio~0.825 (edge +15.1pp)

(BTC/XRP/DOGE#5min, DOGE#15min, BTC/SOL#60min: sin punto con n>=30.
XRP/DOGE no tienen mercados 60min/weekly en el histórico -- no se
capturan, no hay nada que capturar.)

Ese dato viene de compras REALES de ballenas -- confirma que el edge
existe, pero no dice si el LIBRO aguanta una orden nuestra justo ahí.
Cruce inicial con libro_snapshots.csv (señales que ya disparamos por otros
motivos, no dirigidas a estos puntos): BTC/XRP#15min sin dato, ETH#15min
n=11 (45.5% fillable), SOL#15min n=63 (69.8% fillable, mejor de todos) --
insuficiente para concluir en ninguno.

Este logger captura DELIBERADAMENTE el libro del lado favorito (precio del
lado que compra_yes o no según toque) en el instante exacto de cada punto
(con tolerancia), para las 7 combinaciones (activo,marco) que sí cualifican
-- sin filtrar por precio en captura (se filtra en el análisis), para no
perder ocurrencias por un gate demasiado estricto. Resuelve el outcome
oficial después, igual que photo_finish_logger.py.

Scheduler tipo heap: cada (activo,marco) tiene su propio ciclo de cierre
(5/15/60 min) -- un solo heap de "próximo despertar" cubre las 7 a la vez
sin necesitar un loop por marco.

Puramente observacional: no toca prob_yes, no ejecuta, no decide nada.

Corre en screen propio:
  screen -dmS puntoconf bash -c "cd /root/polymarket-research && .venv/bin/python punto_confirmacion_logger.py >> logs/punto_confirmacion.log 2>&1"
"""

import csv
import heapq
import json
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"
TIMEOUT = 5
RESOLVE_DELAY_S = 90
RESOLVER_CADA_S = 60

# (activo, marco_label) -> (ventana_min, segundos antes del cierre, tolerancia_s)
# Solo las combinaciones que cualificaron (n>=30, Wilson_lo>=95%, precio<0.90)
# en el análisis del 21-Jul -- no capturar donde no hay evidencia de punto.
OBJETIVOS = {
    ("eth", "5min"):  (5,  180, 20),
    ("sol", "5min"):  (5,  240, 20),
    ("btc", "15min"): (15,  60, 20),
    ("eth", "15min"): (15, 300, 30),
    ("sol", "15min"): (15, 480, 40),
    ("xrp", "15min"): (15, 780, 45),
    ("eth", "60min"): (60, 1200, 60),
}

COLUMNS = [
    "timestamp_utc", "slug", "market_id", "condition_id", "activo", "marco",
    "end_date", "restante_s_objetivo", "restante_s_real",
    "precio_yes", "lado_favorito", "best_ask_favorito", "ask_usd_le5c",
    "best_bid_favorito", "profundidad_favorito_usd", "n_niveles_favorito",
    "outcome_real", "favorito_gano",
]


def _log(msg: str):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _csv_path(dt: datetime) -> Path:
    return DIR_SHADOW / f"punto_confirmacion_{dt.strftime('%Y-%m-%d')}.csv"


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


def snapshot_asset(asset: str, marco: str, ventana_min: int, ts_end: int, objetivo_s: int):
    ts_start = ts_end - ventana_min * 60
    slug, mkt = mercado_slot(asset, ventana_min, ts_start)
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
        "marco": marco,
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


def _proximo_cierre(ventana_min: int, ahora_ts: float) -> int:
    paso = ventana_min * 60
    return (int(ahora_ts) // paso + 1) * paso


def main():
    _log(f"punto_confirmacion_logger arrancado — {len(OBJETIVOS)} combinaciones (activo,marco): "
         f"{sorted(OBJETIVOS.keys())}")

    # heap de (wake_ts, activo, marco, ventana_min, objetivo_s, ts_end)
    heap = []
    ahora = time.time()
    for (activo, marco), (ventana_min, objetivo_s, _tol) in OBJETIVOS.items():
        ts_end = _proximo_cierre(ventana_min, ahora)
        wake = ts_end - objetivo_s
        while wake <= ahora:
            ts_end += ventana_min * 60
            wake = ts_end - objetivo_s
        heapq.heappush(heap, (wake, activo, marco, ventana_min, objetivo_s, ts_end))

    ultimo_resolver = 0.0
    while True:
        ahora = time.time()
        if ahora - ultimo_resolver > RESOLVER_CADA_S:
            try:
                resolver_pendientes()
            except Exception as e:
                _log(f"resolver error: {e}")
            ultimo_resolver = time.time()

        wake, activo, marco, ventana_min, objetivo_s, ts_end = heap[0]
        resto = wake - time.time()
        if resto > 0:
            time.sleep(min(resto, RESOLVER_CADA_S))
            continue

        heapq.heappop(heap)
        fila = None
        try:
            fila = snapshot_asset(activo, marco, ventana_min, ts_end, objetivo_s)
        except Exception as e:
            _log(f"snapshot error {activo}#{marco}: {e}")
        if fila:
            guardar([fila])
            _log(f"{fila['activo']}#{marco} objetivo={objetivo_s}s real={fila['restante_s_real']}s "
                 f"precio_yes={fila['precio_yes']} favorito={fila['lado_favorito']} "
                 f"ask={fila['best_ask_favorito']} prof=${fila['profundidad_favorito_usd']}")

        # reprogramar la siguiente ocurrencia de esta misma combinación
        ts_end_next = ts_end + ventana_min * 60
        wake_next = ts_end_next - objetivo_s
        heapq.heappush(heap, (wake_next, activo, marco, ventana_min, objetivo_s, ts_end_next))


if __name__ == "__main__":
    main()
