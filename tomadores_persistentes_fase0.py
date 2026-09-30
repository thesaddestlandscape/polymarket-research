#!/usr/bin/env python3
"""tomadores_persistentes_fase0.py -- FASE 0, SOLO OBSERVACIÓN (hilo de observadores_fase0.py).

Mide lo que costaría copiar, con NUESTRA latencia real, a las tomadoras que ganan de forma
persistente (universo diario de seleccion_tomadores_persistentes.py). No envía ni simula
órdenes: por cada PRIMERA compra de una wallet del universo en un mercado up/down de 5/15 min
registra el instante de detección (ms), el retraso respecto a su trade y el ASK REAL del libro
en ese instante, con profundidad.

Contexto (30-Sep): copiar a esas wallets con ~8 s de retraso da EV -3,8 % por €; el precio ya
ha subido 5,7 c en los 5 s previos a su compra y sube ~1 c más en los 1-2 s siguientes. La
pregunta que responde este observador es cuánto queda llegando en ~1 s.

Salida (fuera de git, un fichero por día; seleccion_tomadores_persistentes.py comprime y caduca):
/root/polymarket-research-datalogs/tomadores_persistentes_fase0_YYYY-MM-DD.csv
"""
import csv
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

from wallet_mirror_tracker import _fillability_mirror, leer_activity_incremental

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
DATALOGS = Path("/root/polymarket-research-datalogs")
UNIVERSO = DIR_SHADOW / "tomadores_persistentes_universo.json"
CHECKPOINT = DIR_SHADOW / "tomadores_persistentes_fase0_activity_checkpoint.json"
POLL_S = 0.5
MARCOS = ("5min", "15min")
LAG_MAX_MS = 20000            # trades más viejos que esto al detectarlos (arranque/atasco) no se miden
VISTOS_MAX = 60000
COLUMNS = ["ts_deteccion_utc", "trade_timestamp", "lag_ms", "lat_libro_ms", "wallet", "activo", "marco",
           "market_slug", "condition_id", "lado", "precio_wallet", "usd_trade", "mejor_ask",
           "profundidad_eur", "ratio_vs_stake"]
_lock = threading.Lock()


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _cargar_universo(estado: dict) -> set:
    try:
        mt = UNIVERSO.stat().st_mtime
    except OSError:
        return estado.get("wallets", set())
    if estado.get("mtime") != mt:
        try:
            estado["wallets"] = set(json.loads(UNIVERSO.read_text(encoding="utf-8")).get("wallets", {}))
            estado["mtime"] = mt
            _log(f"universo cargado: {len(estado['wallets'])} wallets")
        except Exception as e:
            _log(f"no se pudo leer el universo ({type(e).__name__}: {e}) -- se mantiene el anterior")
    return estado.get("wallets", set())


def _medir(row: dict, t_det: float) -> None:
    try:
        fill = _fillability_mirror(row.get("market_slug", ""), row.get("outcome", ""), row.get("price", ""))
        lat = (time.time() - t_det) * 1000      # desde la detección: incluye la espera en la cola del pool
        if not fill.get("ok"):
            return
        try:
            t_trade = datetime.fromisoformat(row["timestamp_utc"]).timestamp()
            lag = (t_det - t_trade) * 1000
        except (ValueError, KeyError):
            lag = ""
        fila = {
            "ts_deteccion_utc": datetime.fromtimestamp(t_det, timezone.utc).isoformat(timespec="milliseconds"),
            "trade_timestamp": row.get("timestamp_utc", ""), "lag_ms": round(lag) if lag != "" else "",
            "lat_libro_ms": round(lat), "wallet": (row.get("wallet") or "").lower(),
            "activo": row.get("activo", ""), "marco": row.get("marco", ""),
            "market_slug": row.get("market_slug", ""), "condition_id": row.get("condition_id", ""),
            "lado": row.get("outcome", ""), "precio_wallet": row.get("price", ""),
            "usd_trade": row.get("usd_value", ""), "mejor_ask": fill.get("mejor_ask", ""),
            "profundidad_eur": fill.get("profundidad_eur", ""), "ratio_vs_stake": fill.get("ratio_vs_stake", ""),
        }
        ruta = DATALOGS / f"tomadores_persistentes_fase0_{datetime.now(timezone.utc):%Y-%m-%d}.csv"
        with _lock:
            nuevo = not ruta.exists()
            with open(ruta, "a", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=COLUMNS)
                if nuevo:
                    w.writeheader()
                w.writerow(fila)
    except Exception as e:
        _log(f"error midiendo {row.get('market_slug', '')}: {type(e).__name__}: {e}")


def main() -> None:
    estado, vistos, orden = {}, set(), []
    pool = ThreadPoolExecutor(max_workers=4, thread_name_prefix="tomadores_fase0")
    _log("tomadores_persistentes_fase0 arrancado (solo observación)")
    primera = True
    n = 0
    while True:
        try:
            wallets = _cargar_universo(estado)
            for row in leer_activity_incremental(CHECKPOINT):
                if primera or not wallets:
                    continue          # primer pase: solo avanzar el checkpoint, no medir histórico
                if row.get("side") != "BUY" or row.get("marco") not in MARCOS or row.get("categoria_updown_tracked") != "1":
                    continue
                w = (row.get("wallet") or "").lower()
                if w not in wallets:
                    continue
                clave = f"{w}|{row.get('market_slug', '')}"
                if clave in vistos:
                    continue
                vistos.add(clave)
                orden.append(clave)
                if len(orden) > VISTOS_MAX:
                    for k in orden[:VISTOS_MAX // 3]:
                        vistos.discard(k)
                    del orden[:VISTOS_MAX // 3]
                t_det = time.time()
                try:
                    if (t_det - datetime.fromisoformat(row["timestamp_utc"]).timestamp()) * 1000 > LAG_MAX_MS:
                        continue
                except (ValueError, KeyError):
                    continue
                pool.submit(_medir, row, t_det)
                n += 1
                if n % 500 == 0:
                    _log(f"{n} primeras compras medidas")
            primera = False
        except Exception as e:
            _log(f"🚨 error en ciclo: {type(e).__name__}: {e}")
        time.sleep(POLL_S)


if __name__ == "__main__":
    main()
