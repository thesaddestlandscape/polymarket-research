#!/usr/bin/env python3
"""
ballenas_confirmadas_15m_buyno_depth_fase0.py — FASE 0 (SOLO OBSERVACIÓN)
de baja latencia + profundidad real para BALLENAS_CONFIRMADAS_15M#BUY_NO
en {ETH,SOL,XRP,DOGE}#15min.

Origen (19-Ago, petición explícita Javi): `ballenas_executor_15min.py`
(el ejecutor de baja latencia YA en producción para esta familia) está
hardcodeado a BUY_YES únicamente -- nunca cubrió BUY_NO. Mismo día se
amplió la banda BUY_NO de la estrategia (shadow_predict.py,
BALLENAS_CONFIRMADAS_BANDA_NO_LO 0.5->0.3) tras confirmar edge real en
py∈[0.60,0.70) para SOL#15min (validador de zonas externas, n=1407/1334,
margen +4.8pp/+6.1pp) -- sin este observador, la única forma de medir
fill-ability de esa señal seguiría siendo el camino genérico (~20s), el
mismo error ya corregido hoy para 5 tuplas distintas
(feedback_contrastar_fuente_correcta_por_tupla_19ago).

Mecanismo (mismo cálculo de concentración EXACTO que
s_ballenas_confirmadas_15m en shadow_predict.py -- lógica ya validada en
shadow, aquí solo se envuelve en un poll rápido con profundidad real, no
se reinventa):
  1. Un hilo por (activo) de BALLENAS_CONFIRMADAS_ACTIVOS, mercados #15min.
  2. En cada poll, lee el snapshot reciente del firehose
     (ballenas_firehose_cache.leer_snapshot_reciente), cuenta trades BUY
     dentro de la banda NO [BANDA_NO_LO,BANDA_NO_HI) por lado (YES/NO),
     igual que la función shadow.
  3. Si la concentración NO cruza BALLENAS_CONFIRMADAS_UMBRAL_PCT con
     volumen total suficiente (BALLENAS_CONFIRMADAS_UMBRAL_VOLUMEN) Y
     _banda_confirmada_ballenas() confirma la banda para (activo,15m) --
     mismos 3 gates exactos que la estrategia real -- consulta
     profundidad real del token NO (lt._consultar_profundidad_libro).
  4. Persiste en su propio CSV + predictions_YYYY-MM-DD.csv con STRATEGY
     sintética (nunca puede estar en pares_permitidos_live, no contamina
     el aprendizaje causal real de BALLENAS_CONFIRMADAS_15M).

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
import ballenas_firehose_cache as _fc
from shadow_predict import (
    _banda_confirmada_ballenas,
    BALLENAS_CONFIRMADAS_ACTIVOS,
    BALLENAS_CONFIRMADAS_BANDA_NO_LO,
    BALLENAS_CONFIRMADAS_BANDA_NO_HI,
    BALLENAS_CONFIRMADAS_UMBRAL_PCT,
    BALLENAS_CONFIRMADAS_MIN_TRADES,
    BALLENAS_CONFIRMADAS_UMBRAL_VOLUMEN,
)

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "ballenas_confirmadas_15m_buyno_depth_fase0.csv"
PREDICTIONS_LOCK_PATH = DIR_SHADOW / ".predictions_lock"
GAMMA = "https://gamma-api.polymarket.com"
CLOB_BOOK_URL = "https://clob.polymarket.com/book"

STRATEGY = "BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0"  # sintética
DIRECTION = "BUY_NO"
VENTANA_MIN = 15
POLL_INTERVAL_S = 1.5
HARD_FLOOR_S = 3.0
STAKE_REFERENCIA_EUR = 1.05
TIMEOUT = 5

COLUMNS = ["ts_deteccion_utc", "market_id", "activo", "restante_s",
           "py_ask_yes", "precio_no", "pct_no_banda", "n_banda", "n_no_total",
           "profundidad_ratio", "profundidad_ask"]

_session = requests.Session()
_lock_out = threading.Lock()
_vistos: set[str] = set()


def log(msg: str, activo: str = "") -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    prefijo = f"[{activo}] " if activo else ""
    print(f"[{ts}] {prefijo}{msg}", flush=True)


def _cargar_vistos() -> set:
    if not OUT.exists():
        return set()
    with open(OUT, encoding="utf-8") as f:
        return {r["market_id"] for r in csv.DictReader(f)}


def _escribir_auditoria(fila: dict) -> None:
    with _lock_out:
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)


def resolver_mercado(activo: str, ts_start: int) -> dict | None:
    slug = f"{activo.lower()}-updown-{VENTANA_MIN}m-{ts_start}"
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


def _registrar_prediccion(activo: str, mercado: dict, py: float, precio_no: float,
                           restante_s: float, prof: dict | None) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    archivo = DIR_SHADOW / f"predictions_{ts[:10]}.csv"
    subtype = f"{activo}#{VENTANA_MIN}min"
    prob_yes = max(0.03, py - 0.06)  # mismo nudge conceptual que el resto de familia
    edge = prob_yes - py
    features = json.dumps({
        "py_entrada": round(py, 4), "precio_no_entrada": round(precio_no, 4),
        "restante_min": round(restante_s / 60.0, 2),
        "hora_utc": datetime.now(timezone.utc).hour,
        "profundidad_ratio": prof.get("ratio_vs_stake") if prof else None,
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
                        f"{edge:.4f}", f"{edge:.4f}", f"{edge:.4f}", DIRECTION,
                        "ballenas_confirmadas_15m buyno depth fase0 (solo observación)", subtype,
                        "1.05", features,
                    ])
            finally:
                fcntl.flock(lock_f, fcntl.LOCK_UN)
    except Exception as e:
        log(f"aviso: no se pudo registrar predicción: {e}", activo)


def watch_window(activo: str, ts_end: int) -> None:
    ts_start = ts_end - VENTANA_MIN * 60
    mercado = None
    n_polls = 0
    while True:
        now = time.time()
        restante = ts_end - now
        if restante < HARD_FLOOR_S:
            return

        if mercado is None:
            mercado = resolver_mercado(activo, ts_start)
            if mercado is None:
                time.sleep(POLL_INTERVAL_S)
                continue
            if mercado["market_id"] in _vistos:
                return

        libro = libro_publico(mercado["yes_token"])
        n_polls += 1
        py = libro.get("best_ask") if libro else None
        if py is None:
            time.sleep(POLL_INTERVAL_S)
            continue
        precio_no = round(1.0 - py, 6)
        if not (BALLENAS_CONFIRMADAS_BANDA_NO_LO <= precio_no < BALLENAS_CONFIRMADAS_BANDA_NO_HI):
            time.sleep(POLL_INTERVAL_S)
            continue

        # Mismo cálculo EXACTO que s_ballenas_confirmadas_15m (shadow_predict.py).
        trades = _fc.leer_snapshot_reciente(mercado["condition_id"])
        if not trades:
            time.sleep(POLL_INTERVAL_S)
            continue
        n_no = n_yes = n_no_total = n_yes_total = 0
        for t in trades:
            if (t.get("side") or "").strip().upper() != "BUY":
                continue
            precio_t = t.get("price")
            outcome_t = (t.get("outcome") or "").strip().lower()
            if precio_t is None or outcome_t not in ("up", "down", "yes", "no"):
                continue
            try:
                precio_t = float(precio_t)
            except (ValueError, TypeError):
                continue
            if outcome_t in ("down", "no"):
                n_no_total += 1
            else:
                n_yes_total += 1
            if not (BALLENAS_CONFIRMADAS_BANDA_NO_LO <= precio_t < BALLENAS_CONFIRMADAS_BANDA_NO_HI):
                continue
            if outcome_t in ("down", "no"):
                n_no += 1
            else:
                n_yes += 1
        n = n_no + n_yes
        if n < BALLENAS_CONFIRMADAS_MIN_TRADES:
            time.sleep(POLL_INTERVAL_S)
            continue
        pct_no = n_no / n
        if pct_no < BALLENAS_CONFIRMADAS_UMBRAL_PCT or n_no_total < BALLENAS_CONFIRMADAS_UMBRAL_VOLUMEN:
            time.sleep(POLL_INTERVAL_S)
            continue

        banda_info = _banda_confirmada_ballenas(activo, "15m", BALLENAS_CONFIRMADAS_BANDA_NO_LO,
                                                 BALLENAS_CONFIRMADAS_BANDA_NO_HI)
        if banda_info is None:
            time.sleep(POLL_INTERVAL_S)
            continue

        ts_deteccion = datetime.now(timezone.utc).isoformat(timespec="seconds")
        try:
            prof = lt._consultar_profundidad_libro(None, mercado["no_token"], precio_no,
                                                    STAKE_REFERENCIA_EUR)
        except Exception:
            prof = None

        log(f"[{mercado['market_id']}] CONFIRMADO py={py:.3f} precio_no={precio_no:.3f} "
            f"pct_no={pct_no:.2f} n={n} n_no_total={n_no_total} restante={restante:.1f}s "
            f"ratio={prof.get('ratio_vs_stake') if prof and prof.get('ok') else None} ({n_polls} polls)", activo)

        _vistos.add(mercado["market_id"])
        _escribir_auditoria({
            "ts_deteccion_utc": ts_deteccion,
            "market_id": mercado["market_id"], "activo": activo,
            "restante_s": round(restante, 1), "py_ask_yes": round(py, 4),
            "precio_no": round(precio_no, 4), "pct_no_banda": round(pct_no, 4),
            "n_banda": n, "n_no_total": n_no_total,
            "profundidad_ratio": prof.get("ratio_vs_stake") if prof and prof.get("ok") else "",
            "profundidad_ask": prof.get("mejor_ask") if prof and prof.get("ok") else "",
        })
        _registrar_prediccion(activo, mercado, py, precio_no, restante, prof)
        return


def hilo_activo(activo: str) -> None:
    log("hilo arrancado", activo)
    while True:
        try:
            now = time.time()
            paso_s = VENTANA_MIN * 60
            ts_end = (int(now) // paso_s + 1) * paso_s
            watch_window(activo, ts_end)
            time.sleep(max(1, ts_end + 2 - time.time()))
        except Exception as e:
            log(f"error en hilo: {e} -- reintenta en 5s", activo)
            time.sleep(5)


def main():
    global _vistos
    _vistos = _cargar_vistos()
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    activos = sorted(BALLENAS_CONFIRMADAS_ACTIVOS)
    log(f"arrancado -- activos={activos} banda_no=[{BALLENAS_CONFIRMADAS_BANDA_NO_LO},{BALLENAS_CONFIRMADAS_BANDA_NO_HI})")
    hilos = []
    for activo in activos:
        t = threading.Thread(target=hilo_activo, args=(activo,), daemon=True)
        t.start()
        hilos.append(t)
        time.sleep(0.5)
    while True:
        time.sleep(3600)


if __name__ == "__main__":
    main()
