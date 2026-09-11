#!/usr/bin/env python3
"""
favorito_confirmado_60_240min_depth_fase0.py — FASE 0 (SOLO OBSERVACIÓN)
de profundidad real en baja latencia para las 5 combinaciones de
FAVORITO_CONFIRMADO en 60min/240min que hoy carecen de ejecutor dedicado:
  ETH#240min#BUY_YES (8 buckets estables, margen hasta +14pp -- el más
    llamativo), BTC#240min#BUY_NO, BTC#240min#BUY_YES, SOL#240min#BUY_YES,
  ETH#60min#BUY_YES.

Origen (19-Ago, ver project_pendiente_ejecutores_240min_eth60min_19ago en
memoria): al revisar zonas_validadas_externas_historial.json (buckets
confirmados de forma ESTABLE desde el 15-Ago) se encontraron estos 5 huecos
de cobertura -- la familia #240min completa y ETH#60min#BUY_YES no tenían
NINGÚN ejecutor de baja latencia+profundidad, así que ningún dato propio
puede confirmar o refutar esas zonas todavía.

Mismo patrón EXACTO que favorito_confirmado_depth_fase0.py (no
reinventar): s_favorito_confirmado() es MODEL-FREE (solo umbral de precio,
FAVORITO_CONFIRMADO_UMBRAL=0.55 / UMBRAL_BAJO=0.45, sin drift/sigma).
Watch del libro público en poll rápido, y en el PRIMER instante en que el
ask cruza el umbral de la dirección correspondiente, consulta profundidad
real del lado comprado (lt._consultar_profundidad_libro, solo lectura,
nunca ordena).

Dos caminos de descubrimiento de mercado, verificados por separado hoy:
- 240min SÍ tiene slug determinista (confirmado en vivo: gamma-api
  responde a `{activo}-updown-4h-{ts}`, igual que 5m/15m) -- mismo patrón
  que favorito_confirmado_depth_fase0.py, solo cambia el prefijo de slug
  y la duración de ventana.
- 60min (hourly) NO tiene slug determinista (confirmado en vivo: gamma-api
  responde vacío a `{activo}-updown-1h-{ts}`) -- se resuelve reusando
  _universo_activo() de fetch_libro_ambos_lados.py (clasifica por TEXTO
  de la pregunta), mismo mecanismo que favorito_confirmado_60min_executor.py.

Escribe con STRATEGY sintética "FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0"
(nunca puede estar en pares_permitidos_live, mismo aislamiento que el resto
de *_DEPTH_FASE0 -- no contamina el aprendizaje causal ni gate_bucket_propio
de la familia real FAVORITO_CONFIRMADO).

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
from fetch_libro_ambos_lados import _universo_activo

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "favorito_confirmado_60_240min_depth_fase0.csv"
PREDICTIONS_LOCK_PATH = DIR_SHADOW / ".predictions_lock"
GAMMA = "https://gamma-api.polymarket.com"
CLOB_BOOK_URL = "https://clob.polymarket.com/book"

STRATEGY = "FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0"  # sintética

# (activo, ventana_min, direccion, modo) -- modo "slug" (240min, determinista)
# o "universo" (60min, _universo_activo() por texto).
TUPLAS = [
    ("ETH", 240, "BUY_YES", "slug"),
    ("BTC", 240, "BUY_NO", "slug"),
    ("BTC", 240, "BUY_YES", "slug"),
    ("SOL", 240, "BUY_YES", "slug"),
    ("ETH", 60, "BUY_YES", "universo"),
]

# Mismos valores exactos que s_favorito_confirmado (shadow_predict.py).
UMBRAL_ALTO = 0.55
UMBRAL_BAJO = 0.45
NUDGE = 0.06

POLL_INTERVAL_S = 2.0  # más lento que el de 5/15min -- ventanas de horas, sin prisa de sub-segundo
HARD_FLOOR_S = 5.0
REFRESCO_UNIVERSO_S = 60.0  # cadencia para el modo "universo" mientras no hay mercado resuelto
STAKE_REFERENCIA_EUR = 1.05
TIMEOUT = 5

COLUMNS = ["ts_deteccion_utc", "market_id", "activo", "ventana_min", "direccion",
           "restante_s", "py_ask_yes", "profundidad_ratio", "profundidad_ask"]

_session = requests.Session()
_lock_out = threading.Lock()
_vistos: set[str] = set()
_tokens_cache: dict[str, tuple[str, str]] = {}


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


def resolver_mercado_slug(activo: str, ts_end: int, ventana_min: int) -> dict | None:
    """240min: slug determinista `{activo}-updown-4h-{ts_end}`, verificado
    en vivo el 19-Ago (gamma-api responde con evento real) -- mismo patrón
    que favorito_confirmado_depth_fase0.py para 5/15min."""
    slug = f"{activo.lower()}-updown-4h-{ts_end}"
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
            "yes_token": tokens[0], "no_token": tokens[1],
            "end_date": mkt.get("endDate", ""),
        }
    except Exception:
        return None


def resolver_mercado_universo(activo: str, ventana_min: int) -> dict | None:
    """60min (hourly): sin slug determinista (verificado en vivo el 19-Ago,
    gamma-api vacío) -- reusa _universo_activo() (clasificación por TEXTO
    de la pregunta), mismo mecanismo que favorito_confirmado_60min_executor.py."""
    marco = f"{ventana_min}min"
    try:
        universo = _universo_activo()
    except Exception as e:
        log(f"_universo_activo error: {e}", activo, ventana_min)
        return None
    candidatos = [(mid, edt) for mid, (act, m, cid, edt) in universo.items()
                  if act == activo and m == marco]
    if not candidatos:
        return None
    mid, edt = min(candidatos, key=lambda x: x[1])
    if mid in _tokens_cache:
        yes_token, no_token = _tokens_cache[mid]
    else:
        try:
            yes_token, no_token, _cid = lt._get_token_ids(mid)
        except Exception as e:
            log(f"_get_token_ids error: {e}", activo, ventana_min)
            return None
        _tokens_cache[mid] = (yes_token, no_token)
    return {"market_id": mid, "yes_token": yes_token, "no_token": no_token,
            "end_date": edt.isoformat()}


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
                           profundidad: dict | None) -> None:
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
                        "favorito_confirmado 60/240min depth fase0 (solo observación)", subtype,
                        "1.05", features,
                    ])
            finally:
                fcntl.flock(lock_f, fcntl.LOCK_UN)
    except Exception as e:
        log(f"aviso: no se pudo registrar predicción: {e}", activo, ventana_min, direccion)


def watch_window(activo: str, ventana_min: int, direccion: str, modo: str, ts_end: int) -> None:
    mercado = None
    n_polls = 0
    while True:
        now = time.time()
        restante = ts_end - now
        if restante < HARD_FLOOR_S:
            return

        if mercado is None:
            mercado = (resolver_mercado_slug(activo, ts_end, ventana_min) if modo == "slug"
                       else resolver_mercado_universo(activo, ventana_min))
            if mercado is None:
                time.sleep(REFRESCO_UNIVERSO_S if modo == "universo" else POLL_INTERVAL_S)
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
            token_lado = mercado["yes_token"] if direccion == "BUY_YES" else mercado["no_token"]
            precio_lado = py if direccion == "BUY_YES" else round(1.0 - py, 6)
            prob_yes = min(0.97, py + NUDGE) if direccion == "BUY_YES" else max(0.03, py - NUDGE)

            try:
                prof = lt._consultar_profundidad_libro(None, token_lado, precio_lado,
                                                        STAKE_REFERENCIA_EUR)
            except Exception:
                prof = None

            log(f"[{mercado['market_id']}] CONFIRMADO py={py:.3f} restante={restante:.1f}s "
                f"ratio={prof.get('ratio_vs_stake') if prof and prof.get('ok') else None} "
                f"({n_polls} polls)", activo, ventana_min, direccion)

            _vistos.add(f"{mercado['market_id']}|{direccion}")
            _escribir_auditoria({
                "ts_deteccion_utc": ts_deteccion,
                "market_id": mercado["market_id"],
                "activo": activo, "ventana_min": ventana_min, "direccion": direccion,
                "restante_s": round(restante, 1),
                "py_ask_yes": round(py, 4),
                "profundidad_ratio": prof.get("ratio_vs_stake") if prof and prof.get("ok") else "",
                "profundidad_ask": prof.get("mejor_ask") if prof and prof.get("ok") else "",
            })
            _registrar_prediccion(activo, ventana_min, direccion, mercado, py, prob_yes,
                                   restante, prof)
            return

        time.sleep(POLL_INTERVAL_S)


def hilo_tupla(activo: str, ventana_min: int, direccion: str, modo: str) -> None:
    log("hilo arrancado", activo, ventana_min, direccion)
    paso_s = ventana_min * 60
    while True:
        try:
            now = time.time()
            ts_end = (int(now) // paso_s + 1) * paso_s
            watch_window(activo, ventana_min, direccion, modo, ts_end)
            time.sleep(max(1, ts_end + 5 - time.time()))
        except Exception as e:
            log(f"error en hilo: {e} -- reintenta en 10s", activo, ventana_min, direccion)
            time.sleep(10)


def main():
    global _vistos
    _vistos = _cargar_vistos()
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    log(f"arrancado -- {len(TUPLAS)} tuplas: {TUPLAS}")
    hilos = []
    for activo, ventana_min, direccion, modo in TUPLAS:
        t = threading.Thread(target=hilo_tupla, args=(activo, ventana_min, direccion, modo), daemon=True)
        t.start()
        hilos.append(t)
        time.sleep(0.5)
    while True:
        time.sleep(3600)


if __name__ == "__main__":
    main()
