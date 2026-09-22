#!/usr/bin/env python3
"""
liquidaciones_depth_fase0.py -- FASE 0 (SOLO OBSERVACIÓN) de profundidad
real en baja latencia para LIQUIDACIONES_5M#ETH#5min#BUY_YES, zona
[0.47,0.49) -- petición explícita Javi 22-Sep, tras el hallazgo del edge
quirúrgico universal (train n=44 +0,255€ -> fwd n=18 +0,709€, fill-ability
33,9% medida con el observador genérico de detección, ver CLAUDE.md pt.20
"LIQUIDACIONES_5M/60M -- pendiente de instrumentar fill-ability").

Mismo patrón EXACTO que favorito_confirmado_depth_fase0.py (no
reinventar) -- la diferencia es la condición de disparo: FAVORITO_
CONFIRMADO dispara por un umbral de PRECIO fijo; LIQUIDACIONES_5M
dispara por una condición COMPUESTA (replica _s_liquidaciones de
shadow_predict.py, ventana_min=5/lookback=2min/minutos_min_abierto=1.0,
ver ese módulo -- no reimplementar la fórmula del imbalance aparte, solo
leer el mismo JSON que ya escribe fetch_binance_liquidations.py/screen
liqs):
  1. imbalance del lookback 2min disponible (n>=1) y su signo implica
     BUY_YES (imbalance>0 -> p_yes=0.5+imbalance*0.5>0.5).
  2. minutos_vividos>=1.0 (mismo piso que la estrategia real).
  3. precio YES (ask público) dentro de la zona objetivo [0.47,0.49) --
     más estrecho que el LIQUIDACIONES_LAG_MAX=0.12 genérico de la
     estrategia real, es justo la zona que confirmó el quirúrgico.

En el PRIMER instante en que las 3 condiciones se cumplen a la vez,
consulta profundidad real del lado YES (lt._consultar_profundidad_libro,
solo lectura, nunca ordena). Escribe con STRATEGY sintética
"LIQUIDACIONES_DEPTH_FASE0" (nunca puede estar en pares_permitidos_live,
mismo aislamiento que FAVORITO_CONFIRMADO_DEPTH_FASE0/WALLET_MIRROR --
no contamina el aprendizaje causal ni gate_bucket_propio de la familia
real LIQUIDACIONES_5M).

NO coloca, cancela ni modifica ninguna orden real.

Se fusiona en observadores_fase0.py (screen "observadores") -- NUNCA
lanzar una screen suelta para este script.
"""
import csv
import fcntl
import json
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

import live_trade as lt

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "liquidaciones_depth_fase0.csv"
PREDICTIONS_LOCK_PATH = DIR_SHADOW / ".predictions_lock"
LIQUIDACIONES_STATE = DIR_SHADOW / "liquidaciones_bybit_state.json"
GAMMA = "https://gamma-api.polymarket.com"
CLOB_BOOK_URL = "https://clob.polymarket.com/book"

STRATEGY = "LIQUIDACIONES_DEPTH_FASE0"  # sintética, nunca en pares_permitidos_live

# (activo, ventana_min, direccion, lookback, minutos_min_abierto, zona_lo, zona_hi)
TUPLAS = [
    ("ETH", 5, "BUY_YES", "2min", 1.0, 0.47, 0.49),
]

NUDGE = 0.06
POLL_INTERVAL_S = 1.0
HARD_FLOOR_S = 3.0
STAKE_REFERENCIA_EUR = 1.05
TIMEOUT = 5

COLUMNS = ["ts_deteccion_utc", "market_id", "activo", "ventana_min", "direccion",
           "lag_apertura_s", "restante_s", "py_ask_yes", "imbalance", "liq_n",
           "profundidad_ratio", "profundidad_ask"]

_session = requests.Session()
_lock_out = threading.Lock()
_liquidaciones_cache = {"mtime": None, "data": {}}
_vistos: set[str] = set()


def log(msg: str, activo: str = "", ventana: int = 0, direccion: str = "") -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    prefijo = f"[{activo}#{ventana}min#{direccion}] " if activo else ""
    print(f"[{ts}] {prefijo}{msg}", flush=True)


def _cargar_liquidaciones() -> dict:
    try:
        mtime = LIQUIDACIONES_STATE.stat().st_mtime
    except OSError:
        return {}
    if _liquidaciones_cache["mtime"] != mtime:
        try:
            _liquidaciones_cache["data"] = json.loads(LIQUIDACIONES_STATE.read_text(encoding="utf-8"))
        except Exception:
            _liquidaciones_cache["data"] = {}
        _liquidaciones_cache["mtime"] = mtime
    return _liquidaciones_cache["data"]


def _cargar_vistos() -> set:
    if not OUT.exists():
        return set()
    with open(OUT, encoding="utf-8") as f:
        return {f"{r['market_id']}|{r['direccion']}" for r in csv.DictReader(f)}


def _escribir_auditoria(fila: dict) -> None:
    with _lock_out:
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)


def resolver_mercado(activo: str, ts_start: int, ventana_min: int) -> dict | None:
    """Mismo patrón determinista que favorito_confirmado_depth_fase0.py/
    ballenas_executor_5min.py."""
    slug = f"{activo.lower()}-updown-{ventana_min}m-{ts_start}"
    try:
        r = _session.get(f"{GAMMA}/events", params={"slug": slug}, timeout=TIMEOUT)
        if r.status_code != 200:
            return None
        ev = r.json()
        if not ev or not ev[0].get("markets"):
            return None
        mkt = ev[0]["markets"][0]
        tokens = json.loads(mkt.get("clobTokenIds") or "[]")
        if len(tokens) < 2:
            return None
        return {
            "market_id": mkt.get("id", ""),
            "condition_id": mkt.get("conditionId", ""),
            "yes_token": tokens[0],
            "no_token": tokens[1],
            "end_date": mkt.get("endDate", ""),
        }
    except Exception:
        return None


def libro_publico(token_id: str) -> dict | None:
    try:
        r = _session.get(CLOB_BOOK_URL, params={"token_id": token_id}, timeout=TIMEOUT)
        if r.status_code != 200:
            return None
        book = r.json()
        asks = (book.get("asks") if isinstance(book, dict) else None) or []
        best = min((float(a["price"]) for a in asks), default=None)
        return {"best_ask": best}
    except Exception:
        return None


def _registrar_prediccion(activo: str, ventana_min: int, direccion: str, mercado: dict,
                           py: float, prob_yes: float, restante_s: float,
                           lag_apertura_s: float, profundidad: dict | None) -> None:
    """Mismo formato que favorito_confirmado_depth_fase0.py -- shadow_
    resolve.py/shadow_postmortem.py lo resuelven sin duplicar lógica aquí."""
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    archivo = DIR_SHADOW / f"predictions_{ts[:10]}.csv"
    subtype = f"{activo}#{ventana_min}min"
    edge = prob_yes - py
    features = json.dumps({
        "py_entrada": round(py, 4),
        "restante_min": round(restante_s / 60.0, 2),
        "hora_utc": datetime.now(timezone.utc).hour,
        "lag_apertura_s": round(lag_apertura_s, 2),
        "profundidad_ratio": profundidad.get("ratio_vs_stake") if profundidad else None,
        "fase0_solo_observacion": True,
    }, separators=(",", ":"))
    try:
        with open(PREDICTIONS_LOCK_PATH, "w") as lock_f:
            fcntl.flock(lock_f, fcntl.LOCK_EX)
            try:
                nuevo = not archivo.exists()
                with open(archivo, "a", newline="", encoding="utf-8") as f:
                    w = csv.writer(f)
                    if nuevo:
                        w.writerow([
                            "timestamp_utc", "strategy", "market_id", "question", "end_date",
                            "horas_a_vencimiento", "precio_yes_mercado", "prob_yes_modelo",
                            "edge_bruto", "edge_neto", "edge_direccional", "decision", "razon",
                            "subtype", "apuesta", "features",
                        ])
                    w.writerow([
                        ts, STRATEGY, mercado["market_id"], "", mercado.get("end_date", ""),
                        f"{restante_s / 3600:.4f}", f"{py:.4f}", f"{prob_yes:.4f}",
                        f"{edge:.4f}", f"{edge:.4f}", f"{edge:.4f}", direccion,
                        "liquidaciones depth fase0 (solo observación)", subtype,
                        "1.05", features,
                    ])
            finally:
                fcntl.flock(lock_f, fcntl.LOCK_UN)
    except Exception as e:
        log(f"aviso: no se pudo registrar predicción: {e}", activo, ventana_min, direccion)


def watch_window(activo: str, ventana_min: int, direccion: str, lookback: str,
                  minutos_min_abierto: float, zona_lo: float, zona_hi: float,
                  ts_end: int) -> None:
    ts_start = ts_end - ventana_min * 60
    mercado = None
    n_polls = 0
    while True:
        now = time.time()
        restante = ts_end - now
        if restante < HARD_FLOOR_S:
            return

        if mercado is None:
            mercado = resolver_mercado(activo, ts_start, ventana_min)
            if mercado is None:
                time.sleep(POLL_INTERVAL_S)
                continue
            if f"{mercado['market_id']}|{direccion}" in _vistos:
                return

        minutos_vividos = ventana_min - restante / 60.0
        if minutos_vividos < minutos_min_abierto:
            time.sleep(POLL_INTERVAL_S)
            continue

        estado = _cargar_liquidaciones().get(activo, {})
        datos = estado.get(lookback)
        n_polls += 1
        if not datos or datos.get("imbalance") is None or datos.get("n", 0) < 1:
            time.sleep(POLL_INTERVAL_S)
            continue
        imbalance = datos["imbalance"]
        # direccion fija BUY_YES en TUPLAS -- imbalance>0 implica p_yes>0.5
        # (misma formula que _s_liquidaciones: p_yes=0.5+imbalance*0.5).
        if (direccion == "BUY_YES" and imbalance <= 0) or (direccion == "BUY_NO" and imbalance >= 0):
            time.sleep(POLL_INTERVAL_S)
            continue

        libro = libro_publico(mercado["yes_token"])
        py = libro.get("best_ask") if libro else None
        if py is None:
            time.sleep(POLL_INTERVAL_S)
            continue

        cruza = zona_lo <= py < zona_hi
        if cruza:
            ts_deteccion = datetime.now(timezone.utc).isoformat(timespec="seconds")
            lag_apertura_s = now - ts_start
            token_lado = mercado["yes_token"] if direccion == "BUY_YES" else mercado["no_token"]
            precio_lado = py if direccion == "BUY_YES" else round(1.0 - py, 6)
            prob_yes = min(0.97, py + NUDGE) if direccion == "BUY_YES" else max(0.03, py - NUDGE)

            try:
                prof = lt._consultar_profundidad_libro(None, token_lado, precio_lado,
                                                        STAKE_REFERENCIA_EUR)
            except Exception:
                prof = None

            log(f"[{mercado['market_id']}] CONFIRMADO py={py:.3f} imbalance={imbalance:+.3f} "
                f"lag_apertura={lag_apertura_s:.1f}s restante={restante:.1f}s "
                f"ratio={prof.get('ratio_vs_stake') if prof and prof.get('ok') else None} "
                f"({n_polls} polls)", activo, ventana_min, direccion)

            _vistos.add(f"{mercado['market_id']}|{direccion}")
            _escribir_auditoria({
                "ts_deteccion_utc": ts_deteccion,
                "market_id": mercado["market_id"],
                "activo": activo, "ventana_min": ventana_min, "direccion": direccion,
                "lag_apertura_s": round(lag_apertura_s, 2),
                "restante_s": round(restante, 1),
                "py_ask_yes": round(py, 4),
                "imbalance": round(imbalance, 4),
                "liq_n": datos["n"],
                "profundidad_ratio": prof.get("ratio_vs_stake") if prof and prof.get("ok") else "",
                "profundidad_ask": prof.get("mejor_ask") if prof and prof.get("ok") else "",
            })
            _registrar_prediccion(activo, ventana_min, direccion, mercado, py, prob_yes,
                                   restante, lag_apertura_s, prof)
            return

        time.sleep(POLL_INTERVAL_S)


def hilo_tupla(activo: str, ventana_min: int, direccion: str, lookback: str,
               minutos_min_abierto: float, zona_lo: float, zona_hi: float) -> None:
    log("hilo arrancado", activo, ventana_min, direccion)
    while True:
        try:
            now = time.time()
            paso_s = ventana_min * 60
            ts_end = (int(now) // paso_s + 1) * paso_s
            watch_window(activo, ventana_min, direccion, lookback, minutos_min_abierto,
                        zona_lo, zona_hi, ts_end)
            time.sleep(max(1, ts_end + 2 - time.time()))
        except Exception as e:
            log(f"error en hilo: {e} -- reintenta en 5s", activo, ventana_min, direccion)
            time.sleep(5)


def main():
    global _vistos
    _vistos = _cargar_vistos()
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    log(f"arrancado -- {len(TUPLAS)} tuplas: {TUPLAS}")
    hilos = []
    for activo, ventana_min, direccion, lookback, minutos_min_abierto, zona_lo, zona_hi in TUPLAS:
        t = threading.Thread(target=hilo_tupla,
                             args=(activo, ventana_min, direccion, lookback,
                                   minutos_min_abierto, zona_lo, zona_hi), daemon=True)
        t.start()
        hilos.append(t)
        time.sleep(0.5)
    while True:
        time.sleep(3600)


if __name__ == "__main__":
    main()
