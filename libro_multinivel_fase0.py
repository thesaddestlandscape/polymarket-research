#!/usr/bin/env python3
"""libro_multinivel_fase0.py -- FASE 0 (solo observación), Ángulo B del
backlog 22-Ago (project_backlog_semana_25ago_javi punto 1): "¿un
desbalance calculado sobre VARIOS niveles del libro predice mejor el
resultado que el nivel agregado actual?".

25-Ago: verificado antes de construir (petición Javi: "si crees que hay
indicios de que pueda funcionar") -- consulta directa al book real de
varios mercados activos mostró 18-78 niveles reales con tamaños variados
(no un libro degenerado de 1-2 niveles), y el endpoint /book del CLOB YA
devuelve la lista completa de niveles GRATIS -- el resto del proyecto
(`_consultar_profundidad_libro` en live_trade.py, `libro()` en
resolution_sniper_observer.py) la descarta y se queda solo con el mejor
nivel. Precondición real para que un desbalance multi-nivel pueda aportar
algo: SÍ existe estructura, nunca se ha capturado.

Reusa mercado_slot()/token_ids() de resolution_sniper_observer.py (mismo
descubrimiento de mercados, sin duplicar) -- mismas ventanas 5min de las
6 monedas, capturando en offsets 0-3s tras el cierre nominal (mismo punto
que resolution_sniper_fade/naive, así el resultado es directamente
comparable con lo que YA se sabe de esa fuente).

Métricas candidatas calculadas por captura (agnóstico de cuál acabará
siendo útil -- se decide con datos, no se hardcodea un umbral):
  - imbalance_top1: (bid_size1 - ask_size1) / (bid_size1 + ask_size1)
    del lado YES -- equivalente al agregado actual, sirve de baseline.
  - imbalance_top5/top10: mismo cálculo sumando tamaño de los primeros
    5/10 niveles de cada lado.
  - slope_ask/slope_bid: pendiente (regresión simple tamaño~nivel) de
    los primeros 10 niveles -- ¿el libro se "engorda" o "adelgaza" según
    te alejas del mejor precio?

NO coloca, cancela ni modifica ninguna orden real. Se fusiona en
observadores_fase0.py (screen "observadores"), nunca screen suelta.
"""
import csv
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from resolution_sniper_observer import ASSETS, CLOB, mercado_slot, token_ids  # noqa: E402
from wallet_mirror_tracker import outcome_por_slug  # noqa: E402 -- resolvedor de outcome reusable

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "libro_multinivel_fase0.csv"
VISTOS_PATH = DIR_SHADOW / "libro_multinivel_fase0_vistos.json"
OUT_LOCK = DIR_SHADOW / "libro_multinivel_fase0.csv.lock"

MARCO_TAG = "5m"
DUR_S = 300
OFFSETS_S = [0, 1, 2, 3]
N_TOP = 10
MAX_SLUGS_POR_CICLO = 150

COLUMNS = [
    "timestamp_utc", "activo", "slug", "market_id", "condition_id", "ts_end", "offset_s",
    "ask_yes_top1_precio", "ask_yes_top1_size", "bid_yes_top1_precio", "bid_yes_top1_size",
    "imbalance_top1", "imbalance_top5", "imbalance_top10",
    "slope_ask", "slope_bid", "n_niveles_ask", "n_niveles_bid",
    "outcome_real", "resolved_ts",
]


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _libro_completo(token_id: str):
    try:
        r = requests.get(f"{CLOB}/book", params={"token_id": token_id}, timeout=8)
        if r.status_code != 200:
            return None, None
        b = r.json()
        asks = sorted([(float(a["price"]), float(a["size"])) for a in (b.get("asks") or [])])
        bids = sorted([(float(a["price"]), float(a["size"])) for a in (b.get("bids") or [])], reverse=True)
        return asks, bids
    except Exception:
        return None, None


def _slope(niveles: list) -> float | None:
    """Pendiente tamaño~índice de nivel (regresión simple), primeros N_TOP."""
    if len(niveles) < 3:
        return None
    y = np.array([sz for _, sz in niveles[:N_TOP]], dtype=np.float64)
    x = np.arange(len(y), dtype=np.float64)
    try:
        pendiente = float(np.polyfit(x, y, 1)[0])
    except Exception:
        return None
    return round(pendiente, 4)


def _imbalance(asks: list, bids: list, top_n: int) -> float | None:
    suma_ask = sum(sz for _, sz in asks[:top_n])
    suma_bid = sum(sz for _, sz in bids[:top_n])
    total = suma_ask + suma_bid
    if total <= 0:
        return None
    return round((suma_bid - suma_ask) / total, 4)


def _guardar(filas: list) -> None:
    """25-Ago (bug real encontrado por /code-review el mismo día del
    despliegue): resolver_pendientes() reescribe el CSV ENTERO con
    csv.DictWriter+writeheader() mientras los 6 hilos de captura seguían
    haciendo append aquí sin ningún lock compartido -- carrera de
    escritura concurrente que dejó cabeceras duplicadas y filas truncadas
    en el fichero (96/193 filas parseables limpias en la primera hora).
    Mismo fcntl.flock que ya protege resolver_pendientes(), ahora también
    aquí -- ambas rutinas se serializan sobre el mismo OUT_LOCK."""
    if not filas:
        return
    import fcntl
    lock_f = open(OUT_LOCK, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if nuevo:
                w.writerow(COLUMNS)
            for fila in filas:
                w.writerow([fila.get(c, "") for c in COLUMNS])
    finally:
        fcntl.flock(lock_f, fcntl.LOCK_UN)
        lock_f.close()


def _vistos_cargar() -> set:
    try:
        return set(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return set()


def _vistos_guardar(vistos: set) -> None:
    VISTOS_PATH.write_text(json.dumps(list(vistos)[-20000:]), encoding="utf-8")


def observar_ventana(asset: str, ts_end: int) -> list:
    ts_start = ts_end - DUR_S
    slug, mkt = mercado_slot(asset, MARCO_TAG, ts_start)
    if not mkt:
        return []
    market_id = mkt.get("id", "")
    condition_id = mkt.get("conditionId", "")
    token_yes, token_no = token_ids(mkt)
    if not token_yes:
        return []

    filas = []
    for offset in OFFSETS_S:
        objetivo = ts_end + offset
        espera = objetivo - time.time()
        if espera > 0:
            time.sleep(espera)
        asks, bids = _libro_completo(token_yes)
        if not asks and not bids:
            continue
        asks = asks or []
        bids = bids or []
        filas.append({
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
            "activo": asset, "slug": slug, "market_id": market_id, "condition_id": condition_id,
            "ts_end": ts_end, "offset_s": offset,
            "ask_yes_top1_precio": asks[0][0] if asks else "",
            "ask_yes_top1_size": asks[0][1] if asks else "",
            "bid_yes_top1_precio": bids[0][0] if bids else "",
            "bid_yes_top1_size": bids[0][1] if bids else "",
            "imbalance_top1": _imbalance(asks, bids, 1),
            "imbalance_top5": _imbalance(asks, bids, 5),
            "imbalance_top10": _imbalance(asks, bids, 10),
            "slope_ask": _slope(asks), "slope_bid": _slope(bids),
            "n_niveles_ask": len(asks), "n_niveles_bid": len(bids),
            "outcome_real": "", "resolved_ts": "",
        })
    return filas


def resolver_pendientes() -> int:
    """Mismo patrón que wallet_mirror_tracker.py/bot_wallets_gate_bucket_fase0.py."""
    if not OUT.exists():
        return 0
    with open(OUT, newline="", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    slugs_pendientes = sorted({r["slug"] for r in filas
                                if not r.get("outcome_real") and r.get("slug")})
    outcomes_por_slug = {}
    for slug in slugs_pendientes[:MAX_SLUGS_POR_CICLO]:
        outcome = outcome_por_slug(slug)
        if outcome is not None:
            outcomes_por_slug[slug] = outcome
    if not outcomes_por_slug:
        return 0

    import fcntl
    lock_f = open(OUT_LOCK, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        try:
            with open(OUT, newline="", encoding="utf-8") as f:
                filas = list(csv.DictReader(f))
            resueltas = 0
            for r in filas:
                if r.get("outcome_real"):
                    continue
                outcome = outcomes_por_slug.get(r.get("slug"))
                if outcome is None:
                    continue
                r["outcome_real"] = outcome
                r["resolved_ts"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
                resueltas += 1
            if resueltas:
                with open(OUT, "w", newline="", encoding="utf-8") as f:
                    w = csv.DictWriter(f, fieldnames=COLUMNS)
                    w.writeheader()
                    w.writerows(filas)
            return resueltas
        finally:
            fcntl.flock(lock_f, fcntl.LOCK_UN)
    finally:
        lock_f.close()


def worker(asset: str) -> None:
    """Un hilo por activo (mismo patrón que resolution_sniper_fade_depth_
    fase0.py::worker) -- evita el desfase de offsets que tendría un loop
    secuencial sobre los 6 activos dentro de la misma ventana de 5min."""
    while True:
        now = time.time()
        ts_end = (int(now) // DUR_S + 1) * DUR_S
        despertar = ts_end - 8
        resto = despertar - time.time()
        if resto > 0:
            time.sleep(resto)
        try:
            filas = observar_ventana(asset, ts_end)
            if filas:
                _guardar(filas)
                _log(f"[{asset}] ts_end={ts_end} {len(filas)} capturas, "
                     f"imbalance_top10={filas[-1]['imbalance_top10']}")
        except Exception as e:
            _log(f"[{asset}] error ts_end={ts_end}: {type(e).__name__}: {e}")
        resto2 = ts_end + max(OFFSETS_S) + 1 - time.time()
        if resto2 > 0:
            time.sleep(resto2)


def main() -> None:
    _log(f"libro_multinivel_fase0 arrancado -- activos={ASSETS} marco=5min offsets={OFFSETS_S}")
    with ThreadPoolExecutor(max_workers=len(ASSETS)) as ex:
        for asset in ASSETS:
            ex.submit(worker, asset)
        while True:
            try:
                n = resolver_pendientes()
                if n:
                    _log(f"resueltas: {n}")
            except Exception as e:
                _log(f"resolver_pendientes error: {type(e).__name__}: {e}")
            time.sleep(60)


if __name__ == "__main__":
    main()
