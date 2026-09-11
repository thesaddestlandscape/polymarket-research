#!/usr/bin/env python3
"""
favorito_confirmado_depth_fase0.py — FASE 0 (SOLO OBSERVACIÓN) de
profundidad real en baja latencia para las combinaciones de
FAVORITO_CONFIRMADO que hoy carecen de ejecutor dedicado:
  BTC#5min#BUY_YES, BTC#5min#BUY_NO, BTC#15min#BUY_NO, SOL#5min#BUY_YES,
  ETH#5min#BUY_NO.

Origen (19-Ago, petición explícita Javi tras cazar un error real de
metodología: la primera vez que se midió fill-ability de estas 4 tuplas
se usó el camino GENÉRICO de live_trade.py (_snapshots_candidatos_
evaluacion, ciclo ~20s) en vez de un chequeo en el instante real de
confirmación -- mismo patrón exacto que ya se corrigió para DOGE#5min
#BUY_NO con favorito5min_bajalatencia_fase0.py, y para BTC/SOL#60min
#BUY_YES con favorito_confirmado_60min_executor.py hoy mismo. Ver
feedback_contrastar_fuente_correcta_por_tupla_19ago (memoria).

27-Ago: añadida ETH#5min#BUY_NO -- mismo error de metodología encontrado
de nuevo (petición explícita Javi de repasar todo el barrido de
zonas_validadas_externas con más rigor): esta tupla se venía midiendo con
candidatas_sin_fillability_depth_fase0.py (poll 15s), pero ese script
solo está validado/justificado para ETH#60min#BUY_NO (su propio docstring
dice "ninguna de las 3 necesita baja latencia" -- juicio hecho para el
60min, nunca verificado para 5min, donde el libro se mueve mucho más
rápido). Sin observador reactivo dedicado, la conclusión de fill-ability
sobre el 5min no era fiable -- movida aquí (poll 1s), mismo patrón que
las otras 4.

Mismo patrón EXACTO que favorito5min_bajalatencia_fase0.py (no
reinventar): s_favorito_confirmado() es MODEL-FREE (solo umbral de
precio, FAVORITO_CONFIRMADO_UMBRAL=0.55 / UMBRAL_BAJO=0.45, sin drift/
sigma). Watch del libro público en poll rápido (1s vs los ~20-40s del
ciclo normal), y en el PRIMER instante en que el ask cruza el umbral de
la dirección correspondiente, consulta profundidad real del lado
comprado (lt._consultar_profundidad_libro, solo lectura, nunca ordena).

Escribe con STRATEGY sintética "FAVORITO_CONFIRMADO_DEPTH_FASE0" (nunca
puede estar en pares_permitidos_live, mismo aislamiento que WALLET_MIRROR
y FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA -- no contamina el aprendizaje
causal ni gate_bucket_propio de la familia real FAVORITO_CONFIRMADO).

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
OUT = DIR_SHADOW / "favorito_confirmado_depth_fase0.csv"
PREDICTIONS_LOCK_PATH = DIR_SHADOW / ".predictions_lock"
GAMMA = "https://gamma-api.polymarket.com"
CLOB_BOOK_URL = "https://clob.polymarket.com/book"

STRATEGY = "FAVORITO_CONFIRMADO_DEPTH_FASE0"  # sintética, nunca en pares_permitidos_live

# (activo, ventana_min, direccion)
TUPLAS = [
    ("BTC", 5, "BUY_YES"),
    ("BTC", 5, "BUY_NO"),
    ("BTC", 15, "BUY_NO"),
    ("SOL", 5, "BUY_YES"),
    ("ETH", 5, "BUY_NO"),  # 27-Ago: movida desde candidatas_sin_fillability_depth_fase0.py (poll
                            # 15s, no validado para 5min) -- ver docstring del módulo.
]

# Mismos valores exactos que s_favorito_confirmado (shadow_predict.py).
UMBRAL_ALTO = 0.55
UMBRAL_BAJO = 0.45
NUDGE = 0.06

POLL_INTERVAL_S = 1.0
HARD_FLOOR_S = 3.0
STAKE_REFERENCIA_EUR = 1.05
TIMEOUT = 5

COLUMNS = ["ts_deteccion_utc", "market_id", "activo", "ventana_min", "direccion",
           "lag_apertura_s", "restante_s", "py_ask_yes",
           "profundidad_ratio", "profundidad_ask"]

_session = requests.Session()
_lock_out = threading.Lock()
_vistos: set[str] = set()


def log(msg: str, activo: str = "", ventana: int = 0, direccion: str = "") -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    prefijo = f"[{activo}#{ventana}min#{direccion}] " if activo else ""
    print(f"[{ts}] {prefijo}{msg}", flush=True)


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
    """Mismo patrón determinista que ballenas_executor_5min.py/15min.py,
    parametrizado por ventana (este fichero cubre 5min y 15min a la vez,
    a diferencia de los ejecutores hermanos que solo cubren una)."""
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
    """Mismo formato que el resto de ejecutores de baja latencia --
    shadow_resolve.py/shadow_postmortem.py la resuelven sin duplicar
    lógica aquí. STRATEGY sintética: no toca el stream real."""
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    archivo = DIR_SHADOW / f"predictions_{ts[:10]}.csv"
    subtype = f"{activo}#{ventana_min}min"
    edge = prob_yes - py  # perspectiva YES, por convención (CLAUDE.md)
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
                        "favorito_confirmado depth fase0 (solo observación)", subtype,
                        "1.05", features,
                    ])
            finally:
                fcntl.flock(lock_f, fcntl.LOCK_UN)
    except Exception as e:
        log(f"aviso: no se pudo registrar predicción: {e}", activo, ventana_min, direccion)


def watch_window(activo: str, ventana_min: int, direccion: str, ts_end: int) -> None:
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

        libro = libro_publico(mercado["yes_token"])
        n_polls += 1
        py = libro.get("best_ask") if libro else None
        if py is None:
            time.sleep(POLL_INTERVAL_S)
            continue

        cruza = (direccion == "BUY_YES" and py >= UMBRAL_ALTO) or \
                (direccion == "BUY_NO" and py <= UMBRAL_BAJO)
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

            log(f"[{mercado['market_id']}] CONFIRMADO py={py:.3f} lag_apertura={lag_apertura_s:.1f}s "
                f"restante={restante:.1f}s ratio={prof.get('ratio_vs_stake') if prof and prof.get('ok') else None} "
                f"({n_polls} polls)", activo, ventana_min, direccion)

            _vistos.add(f"{mercado['market_id']}|{direccion}")
            _escribir_auditoria({
                "ts_deteccion_utc": ts_deteccion,
                "market_id": mercado["market_id"],
                "activo": activo, "ventana_min": ventana_min, "direccion": direccion,
                "lag_apertura_s": round(lag_apertura_s, 2),
                "restante_s": round(restante, 1),
                "py_ask_yes": round(py, 4),
                "profundidad_ratio": prof.get("ratio_vs_stake") if prof and prof.get("ok") else "",
                "profundidad_ask": prof.get("mejor_ask") if prof and prof.get("ok") else "",
            })
            _registrar_prediccion(activo, ventana_min, direccion, mercado, py, prob_yes,
                                   restante, lag_apertura_s, prof)
            return

        time.sleep(POLL_INTERVAL_S)


def hilo_tupla(activo: str, ventana_min: int, direccion: str) -> None:
    log("hilo arrancado", activo, ventana_min, direccion)
    while True:
        try:
            now = time.time()
            paso_s = ventana_min * 60
            ts_end = (int(now) // paso_s + 1) * paso_s
            watch_window(activo, ventana_min, direccion, ts_end)
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
    for activo, ventana_min, direccion in TUPLAS:
        t = threading.Thread(target=hilo_tupla, args=(activo, ventana_min, direccion), daemon=True)
        t.start()
        hilos.append(t)
        time.sleep(0.5)
    while True:
        time.sleep(3600)


if __name__ == "__main__":
    main()
