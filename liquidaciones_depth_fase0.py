#!/usr/bin/env python3
"""
liquidaciones_depth_fase0.py -- FASE 0 (SOLO OBSERVACIÓN) de profundidad
real en baja latencia para TODA la familia LIQUIDACIONES_5M/15M/60M
(6 monedas x 3 marcos x 2 direcciones) -- petición explícita Javi 22-Sep:
"ponle el requote y baja latencia a todas las estrategias y a todos los
dry_run que lo necesiten". Generaliza la versión inicial (solo ETH#5min
#BUY_YES[0.47,0.49)) tras auditar el resto del universo Arquetipo B y
confirmar que YA tenía cobertura (FAVORITO_CONFIRMADO*, BALLENAS_TARDIAS/
CONFIRMADAS_15M, WALLET_MIRROR, SNIPER/DISPERSO/WEEKLY_*, MOMENTUM_IBS_*_
BALLENA -- todos con ejecutor/segunda-consulta propia ya construidos).
LIQUIDACIONES era el único hueco real (CLAUDE.md pt.20, pendiente desde
27-Ago).

Mismo patrón EXACTO que favorito_confirmado_depth_fase0.py (no
reinventar) -- la diferencia es la condición de disparo: FAVORITO_
CONFIRMADO dispara por un umbral de PRECIO fijo; LIQUIDACIONES dispara
por una condición COMPUESTA que replica _s_liquidaciones de shadow_
predict.py EXACTAMENTE (no reimplementar la fórmula del imbalance
aparte, solo leer el mismo JSON que ya escribe fetch_binance_
liquidations.py/screen liqs):
  1. imbalance del lookback correspondiente disponible (n>=1) y su signo
     implica la dirección (imbalance>0 -> BUY_YES, <0 -> BUY_NO).
  2. minutos_vividos >= minutos_min_abierto (mismo piso que la estrategia
     real, distinto por marco: 5min=1.0, 15min=1.5, 60min=5.0).
  3. |precio YES - 0.5| <= LIQUIDACIONES_LAG_MAX=0.12 -- MISMO filtro que
     la estrategia real (no una zona más estrecha inventada aquí): se
     observa el rango completo donde la estrategia real consideraría
     operar, para que el gate_bucket_propio de esta familia pueda
     confirmar/descartar CUALQUIER micro-bucket con datos reales, no solo
     el que el quirúrgico ya encontró.

⚠️ Un thread por (activo, marco) cubre AMBAS direcciones a la vez (mismo
mercado/libro, evita duplicar consultas a la API) -- 18 threads en total
(6 monedas x 3 marcos), no 36.

En el PRIMER instante en que las 3 condiciones se cumplen a la vez para
CADA dirección, consulta profundidad real del lado correspondiente
(lt._consultar_profundidad_libro, solo lectura, nunca ordena). Escribe
con STRATEGY sintética "LIQUIDACIONES_DEPTH_FASE0" (nunca puede estar en
pares_permitidos_live, mismo aislamiento que FAVORITO_CONFIRMADO_DEPTH_
FASE0/WALLET_MIRROR -- no contamina el aprendizaje causal ni gate_bucket_
propio de la familia real LIQUIDACIONES_5M/15M/60M).

⚠️ NO coloca, cancela ni modifica ninguna orden real, y esto NO cambia el
principio de fondo del proyecto: cualquier ejecutor REAL que llegue a
construirse sobre esta familia en el futuro tiene que exigir
gate_bucket_propio.evaluar()=="bueno_confirmado" fail-closed antes de
disparar -- exactamente igual que ballenas_executor_15min.py/momentum_
ibs_ballena_executor.py ya hacen hoy (verificado en código, 22-Sep). No
se entra nunca a un precio fuera de un micro-bucket confirmado en vivo.

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

ACTIVOS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
# (ventana_min, lookback, minutos_min_abierto) -- MISMOS valores exactos que
# s_liquidaciones_5min/15min/60min en shadow_predict.py, no reinventar.
MARCOS = [(5, "2min", 1.0), (15, "5min", 1.5), (60, "15min", 5.0)]
LIQUIDACIONES_LAG_MAX = 0.12  # idéntico a shadow_predict.py::LIQUIDACIONES_LAG_MAX

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


def _procesar_direccion(activo: str, ventana_min: int, direccion: str, mercado: dict,
                         py: float, imbalance: float, n_liq: int, restante: float,
                         ts_start: float, now: float) -> None:
    ts_deteccion = datetime.now(timezone.utc).isoformat(timespec="seconds")
    lag_apertura_s = now - ts_start
    token_lado = mercado["yes_token"] if direccion == "BUY_YES" else mercado["no_token"]
    precio_lado = py if direccion == "BUY_YES" else round(1.0 - py, 6)
    prob_yes = min(0.97, py + NUDGE) if direccion == "BUY_YES" else max(0.03, py - NUDGE)

    try:
        prof = lt._consultar_profundidad_libro(None, token_lado, precio_lado, STAKE_REFERENCIA_EUR)
    except Exception:
        prof = None

    log(f"[{mercado['market_id']}] CONFIRMADO py={py:.3f} imbalance={imbalance:+.3f} "
        f"lag_apertura={lag_apertura_s:.1f}s restante={restante:.1f}s "
        f"ratio={prof.get('ratio_vs_stake') if prof and prof.get('ok') else None}",
        activo, ventana_min, direccion)

    _vistos.add(f"{mercado['market_id']}|{direccion}")
    _escribir_auditoria({
        "ts_deteccion_utc": ts_deteccion,
        "market_id": mercado["market_id"],
        "activo": activo, "ventana_min": ventana_min, "direccion": direccion,
        "lag_apertura_s": round(lag_apertura_s, 2),
        "restante_s": round(restante, 1),
        "py_ask_yes": round(py, 4),
        "imbalance": round(imbalance, 4),
        "liq_n": n_liq,
        "profundidad_ratio": prof.get("ratio_vs_stake") if prof and prof.get("ok") else "",
        "profundidad_ask": prof.get("mejor_ask") if prof and prof.get("ok") else "",
    })
    _registrar_prediccion(activo, ventana_min, direccion, mercado, py, prob_yes,
                          restante, lag_apertura_s, prof)


def watch_window(activo: str, ventana_min: int, lookback: str, minutos_min_abierto: float,
                  ts_end: int) -> None:
    """Cubre BUY_YES y BUY_NO a la vez -- mismo mercado, mismo libro."""
    ts_start = ts_end - ventana_min * 60
    mercado = None
    pendientes = {"BUY_YES", "BUY_NO"}
    while pendientes:
        now = time.time()
        restante = ts_end - now
        if restante < HARD_FLOOR_S:
            return

        if mercado is None:
            mercado = resolver_mercado(activo, ts_start, ventana_min)
            if mercado is None:
                time.sleep(POLL_INTERVAL_S)
                continue
            pendientes = {d for d in ("BUY_YES", "BUY_NO")
                         if f"{mercado['market_id']}|{d}" not in _vistos}
            if not pendientes:
                return

        minutos_vividos = ventana_min - restante / 60.0
        if minutos_vividos < minutos_min_abierto:
            time.sleep(POLL_INTERVAL_S)
            continue

        datos = _cargar_liquidaciones().get(activo, {}).get(lookback)
        if not datos or datos.get("imbalance") is None or datos.get("n", 0) < 1:
            time.sleep(POLL_INTERVAL_S)
            continue
        imbalance = datos["imbalance"]
        direccion_implicada = "BUY_YES" if imbalance > 0 else ("BUY_NO" if imbalance < 0 else None)
        if direccion_implicada is None or direccion_implicada not in pendientes:
            time.sleep(POLL_INTERVAL_S)
            continue

        libro = libro_publico(mercado["yes_token"])
        py = libro.get("best_ask") if libro else None
        if py is None:
            time.sleep(POLL_INTERVAL_S)
            continue

        if abs(py - 0.5) <= LIQUIDACIONES_LAG_MAX:
            _procesar_direccion(activo, ventana_min, direccion_implicada, mercado, py,
                               imbalance, datos["n"], restante, ts_start, now)
            pendientes.discard(direccion_implicada)

        time.sleep(POLL_INTERVAL_S)


def hilo_marco(activo: str, ventana_min: int, lookback: str, minutos_min_abierto: float) -> None:
    log("hilo arrancado", activo, ventana_min)
    while True:
        try:
            now = time.time()
            paso_s = ventana_min * 60
            ts_end = (int(now) // paso_s + 1) * paso_s
            watch_window(activo, ventana_min, lookback, minutos_min_abierto, ts_end)
            time.sleep(max(1, ts_end + 2 - time.time()))
        except Exception as e:
            log(f"error en hilo: {e} -- reintenta en 5s", activo, ventana_min)
            time.sleep(5)


def main():
    global _vistos
    _vistos = _cargar_vistos()
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    n_hilos = len(ACTIVOS) * len(MARCOS)
    log(f"arrancado -- {n_hilos} hilos ({len(ACTIVOS)} monedas x {len(MARCOS)} marcos, "
        f"ambas direcciones por hilo)")
    hilos = []
    for activo in ACTIVOS:
        for ventana_min, lookback, minutos_min_abierto in MARCOS:
            t = threading.Thread(target=hilo_marco,
                                 args=(activo, ventana_min, lookback, minutos_min_abierto),
                                 daemon=True)
            t.start()
            hilos.append(t)
            time.sleep(0.3)
    while True:
        time.sleep(3600)


if __name__ == "__main__":
    main()
