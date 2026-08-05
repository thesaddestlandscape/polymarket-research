#!/usr/bin/env python3
"""
favorito_5min_altaconviccion_logger.py — Logger de sondeo frecuente para
FAVORITO_CONFIRMADO en #5min, los 6 activos (BTC/ETH/SOL/XRP/DOGE/BNB),
AMBAS direcciones. Solo shadow -- NO ejecuta nada, NO toca dinero.

Origen (30-Jul, petición explícita Javi): construido primero solo para
FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION (umbral 0.70, lado YES), que
llevaba 0 predicciones en 3 días -- diagnóstico verificado: la estrategia
BASE FAVORITO_CONFIRMADO#*#5min (umbral 0.55/0.45, más laxo) solo
disparaba 21 veces en 3 días con el sondeo del fast loop (~20-25s),
demasiado lento para una ventana de 5min. Verificado en producción: en
30s de sondeo a 1.5s ya se capturaron más predicciones que en 3 días del
pipeline lento.

Extendido el mismo día (petición explícita: "pasalo a todas las monedas
de favorito confirmado en 5 minutos, tanto para el lado yes como para el
lado no") a la estrategia BASE completa -- las dos estrategias comparten
el mismo `py` de entrada y se evalúan de forma independiente en cada
poll (igual que hace shadow_predict.py con ambas funciones sobre el
mismo mercado):
  - FAVORITO_CONFIRMADO:                py>=0.55 (BUY_YES) / py<=0.45 (BUY_NO)
  - FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION: py>=0.70 (solo BUY_YES,
    la mother function no tiene rama ALTACONVICCION para BUY_NO)

Por qué NO se extiende al resto de estrategias de 5min (STREAK_MOM_5M/
STREAK_FADE_5M/GBM_LATE_5M/ORDER_FLOW_5M/LIQUIDACIONES_5M): verificado
con datos reales que NINGUNA de ellas sufre este problema -- ya generan
187-218 predicciones/3días vía el pipeline normal (GBM_LATE_5M/STREAK_*),
o dependen de features caras/eventos externos (drift/sigma, flujo de
volumen, liquidaciones reales) que un sondeo más frecuente no ataca y
podría incluso empeorar (mismo razonamiento ya documentado en
favorito_altaconviccion_executor_15min.py sobre por qué GBM_LATE_15M NO
es candidato). Solo FAVORITO_CONFIRMADO es puramente model-free (un
cruce de precio contra un umbral fijo), barato de vigilar en un poll
rápido.

Ninguna de las dos estrategias está en pares_permitidos_live -- son
candidatos de cobertura sin evidencia todavía, no ejecutores de dinero
real. n_total_lado se registra siempre (compras del lado UP/YES o
DOWN/NO en todo el mercado, según decisión) para poder calibrar un
umbral de volumen futuro con datos reales, aunque GATE_VOLUMEN_VALIDADO
no tenga entradas para 5min hoy.

Mercados 5min SÍ tienen slug determinista resoluble (a diferencia de
60min/hourly).

⚠️ 05-Ago: fusionado dentro de observadores_fase0.py (screen "observadores"),
NO tiene screen propia -- corre como hilo. NUNCA lanzar `screen -dmS
fav5malt ...` suelto: duplica el proceso. Ver observadores_fase0.py y
pipeline_watchdog.py::SCREENS_RETIRADAS.
"""
import csv
import fcntl
import json
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

from smart_money_tracker import trades_de_mercado
from ballenas_banda_fina_gate import evaluar as _gate_banda_fina_ballenas
from gate_bucket_propio import evaluar as _gate_bucket_propio

DIR = Path(__file__).resolve().parent
DIR_SHADOW = DIR / "data" / "shadow"
PREDICTIONS_LOCK_PATH = DIR_SHADOW / ".predictions_lock"

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"

STRATEGY_BASE = "FAVORITO_CONFIRMADO"
STRATEGY_ALT = "FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION"
VENTANA_MIN = 5
ACTIVOS = ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")

POLL_INTERVAL_S = 1.5
HARD_FLOOR_S = 3.0

# Mismos valores exactos que shadow_predict.py (FAVORITO_CONFIRMADO_UMBRAL/
# _UMBRAL_BAJO/_NUDGE, FAVORITO_5MIN_ALTACONVICCION_TH) -- duplicados aquí,
# mismo criterio que el resto de ejecutores/loggers de baja latencia. Si
# cambian allí, replicar aquí a mano.
UMBRAL_ALT = 0.70          # FAVORITO_5MIN_ALTACONVICCION_TH
UMBRAL_BASE_ALTO = 0.55    # FAVORITO_CONFIRMADO_UMBRAL
UMBRAL_BASE_BAJO = 0.45    # FAVORITO_CONFIRMADO_UMBRAL_BAJO
NUDGE = 0.06

_session = requests.Session()

_pares_live_cache = {"mtime": None, "set": set()}
CONFIG_LIVE_PATH = DIR / "data" / "live" / "config_live.json"


def log(msg: str, activo: str = "") -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    prefijo = f"[{activo}] " if activo else ""
    print(f"[{ts}] {prefijo}{msg}", flush=True)


def _pares_live_hoy_set() -> set:
    """Mismo patrón fail-closed que shadow_predict.py::_pares_live_hoy_set
    -- ninguna de las dos estrategias está en pares_permitidos_live hoy,
    así que gate_bucket_propio nunca bloqueará nada aquí (solo se loguea
    el veredicto), pero se mantiene el mismo chequeo por si algún día se
    promociona alguna."""
    try:
        mtime = CONFIG_LIVE_PATH.stat().st_mtime
    except OSError:
        return _pares_live_cache["set"]
    if _pares_live_cache["mtime"] != mtime:
        try:
            data = json.loads(CONFIG_LIVE_PATH.read_text(encoding="utf-8"))
            _pares_live_cache["set"] = set(data.get("pares_permitidos_live", []))
            _pares_live_cache["mtime"] = mtime
        except Exception:
            pass
    return _pares_live_cache["set"]


def resolver_mercado(activo: str, ts_start: int) -> dict | None:
    """Mismo patrón determinista que los ejecutores 15min -- 5min SÍ tiene
    slug resoluble (a diferencia de 60min/hourly)."""
    slug = f"{activo.lower()}-updown-{VENTANA_MIN}m-{ts_start}"
    try:
        r = _session.get(f"{GAMMA}/events", params={"slug": slug}, timeout=5)
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
            "end_date": mkt.get("endDate", ""),
        }
    except Exception as e:
        log(f"resolver_mercado error: {e}", activo)
        return None


def libro_publico(token_id: str) -> dict | None:
    try:
        r = _session.get(f"{CLOB}/book", params={"token_id": token_id}, timeout=5)
        if r.status_code != 200:
            return None
        b = r.json()
        asks = [(float(a["price"]), float(a["size"])) for a in (b.get("asks") or [])]
        best_ask = min((p for p, _ in asks), default=None)
        return {"best_ask": best_ask}
    except Exception:
        return None


def _n_lado_total(condition_id: str, direccion: str) -> int | None:
    """Compras del lado UP/YES (BUY_YES) o DOWN/NO (BUY_NO) en TODO el
    mercado -- mismo cálculo que _gate_volumen_ballenas en shadow_predict.py.
    Sin gate todavía para 5min, se registra solo para calibrar un umbral
    futuro con datos reales."""
    try:
        trades = trades_de_mercado(condition_id, timeout=3)
    except Exception:
        return None
    lado_check = ("up", "yes") if direccion == "BUY_YES" else ("down", "no")
    return sum(1 for t in trades if (t.get("side") or "").strip().upper() == "BUY"
               and (t.get("outcome") or "").strip().lower() in lado_check)


def _registrar_prediccion(strategy: str, activo: str, mercado: dict, py: float, prob_yes: float,
                           direccion: str, restante_s: float, n_lado_total: int | None,
                           gate_bp_veredicto: str) -> None:
    """Mismo formato que shadow_predict.py -- shadow_resolve.py/
    shadow_postmortem.py lo resuelven y aprenden de él sin duplicar esa
    lógica aquí, igual que el resto de ejecutores/loggers de baja
    latencia de este proyecto. edge SIEMPRE en perspectiva YES (CLAUDE.md:
    "edge_neto SIEMPRE en perspectiva YES: en filas BUY_NO el edge a
    favor es -edge_neto") -- prob_yes-py ya lo respeta en ambas ramas."""
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    archivo = DIR_SHADOW / f"predictions_{ts[:10]}.csv"
    subtype = f"{activo}#{VENTANA_MIN}min"
    edge = prob_yes - py
    gate_bf = _gate_banda_fina_ballenas(activo, f"{VENTANA_MIN}min", py, restante_s / 60.0)
    features = json.dumps({
        "py_entrada": round(py, 4), "n_total_lado": n_lado_total,
        "restante_min": round(restante_s / 60.0, 2),
        "hora_utc": datetime.now(timezone.utc).hour,
        "banda_fina_vetaria_fase1": gate_bf["vetaria_fase1"], "banda_fina_motivo": gate_bf["motivo"],
        "gate_bucket_propio_veredicto": gate_bp_veredicto,
        "logger_sondeo_frecuente": True,
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
                        ts, strategy, mercado["market_id"], "", mercado.get("end_date", ""),
                        f"{restante_s / 3600:.4f}", f"{py:.4f}", f"{prob_yes:.4f}",
                        f"{edge:.4f}", f"{edge:.4f}", f"{edge:.4f}", direccion,
                        "favorito_confirmado momentum-consenso (logger sondeo frecuente)", subtype,
                        "1.05", features,
                    ])
            finally:
                fcntl.flock(lock_f, fcntl.LOCK_UN)
    except Exception as e:
        log(f"aviso: no se pudo registrar predicción para postmortem: {e}", activo)


def _procesar_confirmacion(strategy: str, activo: str, mercado: dict, py: float,
                            direccion: str, restante_s: float) -> None:
    prob_yes = min(0.97, py + NUDGE) if direccion == "BUY_YES" else max(0.03, py - NUDGE)
    n_lado_total = _n_lado_total(mercado["condition_id"], direccion)
    tupla_str = f"{strategy}#{activo}#{VENTANA_MIN}min#{direccion}"
    gate_bp = _gate_bucket_propio(tupla_str, py)
    log(f"CONFIRMADO {strategy} py={py:.3f} prob_yes={prob_yes:.3f} {direccion} "
        f"restante={restante_s:.1f}s n_lado_total={n_lado_total} gate_bucket={gate_bp['veredicto']}", activo)
    _registrar_prediccion(strategy, activo, mercado, py, prob_yes, direccion,
                          restante_s, n_lado_total, gate_bp["veredicto"])


def watch_window(activo: str, ts_end: int) -> None:
    """Vigila la ventana completa (apertura a cierre) -- la condición
    puede cruzarse en cualquier punto de los 5min. Registra hasta 3
    predicciones independientes por ventana (BASE#BUY_YES, BASE#BUY_NO,
    ALT#BUY_YES -- mutuamente excluyentes salvo BASE_ALTO/ALT que SÍ
    pueden coexistir si el precio cruza 0.70), cada una solo una vez.
    Nunca ejecuta nada real."""
    ts_start = ts_end - VENTANA_MIN * 60
    mercado = None
    n_polls = 0
    logueado_base = False   # BUY_YES o BUY_NO, mutuamente excluyentes entre sí
    logueado_alt = False
    while True:
        restante = ts_end - time.time()
        if restante < HARD_FLOOR_S:
            if n_polls:
                log(f"[{ts_end}] suelo alcanzado ({n_polls} polls, base={logueado_base} alt={logueado_alt})", activo)
            return
        if logueado_base and logueado_alt:
            return  # nada más que vigilar en esta ventana

        if mercado is None:
            mercado = resolver_mercado(activo, ts_start)
            if mercado is None:
                log(f"[{ts_end}] no se pudo resolver el mercado -- se abandona", activo)
                return

        libro = libro_publico(mercado["yes_token"])
        n_polls += 1
        py = libro.get("best_ask") if libro else None

        if py is not None:
            if not logueado_base:
                if py >= UMBRAL_BASE_ALTO:
                    _procesar_confirmacion(STRATEGY_BASE, activo, mercado, py, "BUY_YES", restante)
                    logueado_base = True
                elif py <= UMBRAL_BASE_BAJO:
                    _procesar_confirmacion(STRATEGY_BASE, activo, mercado, py, "BUY_NO", restante)
                    logueado_base = True
            if not logueado_alt and py >= UMBRAL_ALT:
                _procesar_confirmacion(STRATEGY_ALT, activo, mercado, py, "BUY_YES", restante)
                logueado_alt = True

        if logueado_base and logueado_alt:
            return
        time.sleep(POLL_INTERVAL_S)


def hilo_activo(activo: str):
    log("hilo arrancado", activo)
    while True:
        try:
            now = time.time()
            ts_end = (int(now) // (VENTANA_MIN * 60) + 1) * (VENTANA_MIN * 60)
            watch_window(activo, ts_end)
            time.sleep(max(0, ts_end + 2 - time.time()))
        except Exception as e:
            log(f"error en hilo_activo: {e} -- reintenta en 5s", activo)
            time.sleep(5)


def main():
    log(f"favorito_5min_logger arrancado (activos={list(ACTIVOS)}, "
        f"BASE umbral={UMBRAL_BASE_ALTO}/{UMBRAL_BASE_BAJO} + ALT umbral={UMBRAL_ALT}, solo shadow)")
    hilos = [threading.Thread(target=hilo_activo, args=(activo,), daemon=True, name=activo)
             for activo in ACTIVOS]
    for h in hilos:
        h.start()

    while True:
        time.sleep(30)
        for i, h in enumerate(hilos):
            if not h.is_alive():
                activo = h.name
                log("hilo murió inesperadamente -- reiniciando", activo)
                nuevo = threading.Thread(target=hilo_activo, args=(activo,), daemon=True, name=activo)
                nuevo.start()
                hilos[i] = nuevo


if __name__ == "__main__":
    main()
