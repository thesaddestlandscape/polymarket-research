#!/usr/bin/env python3
"""
favorito_ultimosegundo_5min.py — captura FAVORITO_CONFIRMADO en el instante
decisivo de XRP/DOGE/BNB#5min (T-~10s antes del cierre de ventana).

Origen (2026-07-28, misma sesión que idea_xrp_doge_bnb_5min_confirmacion_
ultimo_segundo_28jul): diagnosticado que XRP/DOGE/BNB#5min están en ~50/50
casi toda su ventana de 300s y solo colapsan hacia el resultado real en una
franja muy estrecha cerca del cierre (confirmado con photo_finish_logger.py,
que SÍ cubre los 6 activos y muestra ask≤0.05 en 55-70% de sus snapshots a
T-10s). El fast loop normal (ciclo ~100-130s) tiene una probabilidad baja
(~5-10%) de que su única llamada por ciclo caiga justo en esa franja
decisiva — por eso s_favorito_confirmado() casi nunca dispara para estos 3
activos en 5min (n=10/4/1 histórico vs n=390-416 en ETH/SOL, que sí tienen
movimiento sostenido durante toda la ventana).

Mismo patrón de scheduling que photo_finish_logger.py (wake a T-ANTICIPO_S,
proceso independiente, no bloquea el fast loop) pero SIN el filtro
|dist_pct|<0.15% de aquél — ese filtro captura justo lo contrario de lo que
aquí interesa (queremos los casos donde el precio SÍ diverge fuerte, no los
"casi empate"). Reutiliza el umbral de s_favorito_confirmado
(FAVORITO_CONFIRMADO_UMBRAL=0.55/0.45) importado directamente de
shadow_predict.py para no duplicar lógica.

Puramente shadow/observacional: NO ejecuta nada, NO toca dinero, NO se
integra con predictions_YYYY-MM-DD.csv (evita carrera de escritura con el
fast loop) — escribe su propio CSV, se resuelve con outcome oficial de
Polymarket, igual que photo_finish_logger.py. Objetivo: medir si, capturado
en el instante correcto, FAVORITO_CONFIRMADO SÍ tiene edge real en estos 3
activos (arquetipo B, coin-específico) antes de proponer integrarlo en el
pipeline de predicciones normal.

Corre en screen propio:  screen -dmS favultsec bash -c "cd /root/polymarket-research && .venv/bin/python favorito_ultimosegundo_5min.py >> logs/favorito_ultimosegundo.log 2>&1"
"""

import csv
import json
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import requests

from shadow_predict import FAVORITO_CONFIRMADO_UMBRAL, FAVORITO_CONFIRMADO_UMBRAL_BAJO

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"
TIMEOUT = 5

# Los 3 activos donde FAVORITO_CONFIRMADO#5min casi no dispara con el
# cadence normal (BTC/ETH/SOL ya tienen cobertura razonable, ver memoria
# idea_xrp_doge_bnb_5min_confirmacion_ultimo_segundo_28jul).
ASSETS = ["xrp", "doge", "bnb"]

ANTICIPO_S = 10  # despertar T_end - ANTICIPO_S (mismo orden que photo_finish, ANTICIPO_S=12)
RESOLVE_DELAY_S = 90

COLUMNS = [
    "timestamp_utc", "slug", "market_id", "condition_id", "activo",
    "end_date", "restante_s", "py_yes", "lado", "direccion",
    "best_bid", "best_ask", "spread",
    "outcome_real", "acierto",
]


def _log(msg: str):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _csv_path(dt: datetime) -> Path:
    return DIR_SHADOW / f"favorito_ultimosegundo_{dt.strftime('%Y-%m-%d')}.csv"


def mercado_slot(asset: str, ts_start: int):
    slug = f"{asset}-updown-5m-{ts_start}"
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


def libro_bid_ask(token_id: str):
    try:
        r = requests.get(f"{CLOB}/book", params={"token_id": token_id}, timeout=TIMEOUT)
        if r.status_code != 200:
            return None, None
        b = r.json()
        asks = [float(a["price"]) for a in (b.get("asks") or [])]
        bids = [float(a["price"]) for a in (b.get("bids") or [])]
        return (min(asks) if asks else None), (max(bids) if bids else None)
    except Exception:
        return None, None


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


def snapshot_asset(asset: str, ts_end: int):
    ts_start = ts_end - 300
    slug, mkt = mercado_slot(asset, ts_start)
    if not mkt:
        return None
    try:
        pr = mkt.get("outcomePrices")
        pr = json.loads(pr) if isinstance(pr, str) else pr
        py = float(pr[0]) if pr else None
    except Exception:
        return None
    if py is None:
        return None

    if py >= FAVORITO_CONFIRMADO_UMBRAL:
        lado, direccion = "Up", "BUY_YES"
    elif py <= FAVORITO_CONFIRMADO_UMBRAL_BAJO:
        lado, direccion = "Down", "BUY_NO"
    else:
        return None  # zona coinflip -- mismo criterio que s_favorito_confirmado

    try:
        tokens = json.loads(mkt.get("clobTokenIds") or "[]")
    except Exception:
        tokens = []
    best_bid = best_ask = spread = ""
    if len(tokens) >= 2:
        token_yes = tokens[0]
        ask, bid = libro_bid_ask(token_yes)
        best_bid, best_ask = bid, ask
        if bid is not None and ask is not None:
            spread = round(ask - bid, 4)

    now = datetime.now(timezone.utc)
    return {
        "timestamp_utc": now.isoformat(timespec="seconds"),
        "slug": slug,
        "market_id": mkt.get("id", ""),
        "condition_id": mkt.get("conditionId", ""),
        "activo": asset.upper(),
        "end_date": datetime.fromtimestamp(ts_end, timezone.utc).isoformat(timespec="seconds"),
        "restante_s": round(ts_end - now.timestamp(), 1),
        "py_yes": py,
        "lado": lado,
        "direccion": direccion,
        "best_bid": best_bid if best_bid is not None else "",
        "best_ask": best_ask if best_ask is not None else "",
        "spread": spread,
        "outcome_real": "",
        "acierto": "",
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
                r["acierto"] = "1" if out == r["lado"] else "0"
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
    _log(f"favorito_ultimosegundo_5min arrancado — activos={ASSETS} anticipo={ANTICIPO_S}s "
         f"umbral=[{FAVORITO_CONFIRMADO_UMBRAL_BAJO},{FAVORITO_CONFIRMADO_UMBRAL})")
    while True:
        now = time.time()
        ts_end = (int(now) // 300 + 1) * 300
        despertar = ts_end - ANTICIPO_S
        if despertar > now:
            try:
                resolver_pendientes()
            except Exception as e:
                _log(f"resolver error: {e}")
            resto = despertar - time.time()
            if resto > 0:
                time.sleep(resto)

        filas = []
        with ThreadPoolExecutor(max_workers=len(ASSETS)) as ex:
            futs = [ex.submit(snapshot_asset, a, ts_end) for a in ASSETS]
            for fu in futs:
                try:
                    r = fu.result(timeout=ANTICIPO_S)
                    if r:
                        filas.append(r)
                except Exception:
                    pass
        guardar(filas)
        if filas:
            det = " | ".join(f"{f['activo']} py={f['py_yes']:.3f} {f['direccion']} "
                              f"ask={f['best_ask']}" for f in filas)
            _log(f"frontera {datetime.fromtimestamp(ts_end, timezone.utc).strftime('%H:%M:%S')}: "
                 f"{len(filas)} señal(es) → {det}")
        time.sleep(max(0, ts_end + 5 - time.time()))


if __name__ == "__main__":
    main()
