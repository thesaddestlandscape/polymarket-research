#!/usr/bin/env python3
"""
gbm_late_15min_executor.py — Ejecutor de baja latencia para
GBM_LATE_15M#{ETH,SOL,XRP}#15min (BUY_YES o BUY_NO, según el signo del edge).

04-Ago (mismo día, más tarde): añadido XRP -- candidata del cementerio
NUNCA promovida, con el gap de latencia más extremo medido en todo el
sistema (+249.5s, 44.9% de señales perdidas, n=1730/1029, ver paso 4 de
project_barrido_definitivo_latencia_17_combos_03ago). Puramente
observacional -- XRP no está en pares_permitidos_live, así que
puede_operar_live() la bloquea siempre por whitelist, con o sin DRY_RUN.
El objetivo es medir si, capturando la señal sin el lag del ciclo lento,
el edge que hoy se pierde por veto_profundidad/senal_caducada era real --
justificación para reintentar reactivarla, no prueba de que funcionará.

Origen (04-Ago, petición explícita Javi tras el barrido de latencia de
ayer): GBM_LATE_15M#ETH#15min y #SOL#15min (ambas LIVE) pierden 68.9% y
56.8% de sus señales por veto_profundidad/senal_caducada -- el lag
mediano entre "señal generada" (shadow_predict.py, dentro del ciclo
~100-130s de run_fast.sh) y "libro consultado" (live_trade.py, mismo
ciclo o el siguiente) es de +93.0s y +91.0s respectivamente. Ver
project_barrido_definitivo_latencia_17_combos_03ago (memoria) -- mismo
mecanismo, mismo patrón de solución (ejecutor dedicado, mismo ciclo
detección→ejecución) ya usado en ballenas_executor_*/favorito_*
_executor*.py.

Diseño (decisión explícita, distinta del resto de ejecutores de baja
latencia): la fórmula de GBM_LATE_15M (log-normal, d=ln(spot/ref)/
(sigma*sqrt(T)), p_up=norm_cdf(d)) es sustancialmente más compleja que
los umbrales simples que replican a mano favorito_confirmado_btc60min_
buyno_executor.py/favorito_altaconviccion_executor_15min.py -- el riesgo
de un bug de transcripción (signo, sqrt, unidades de tiempo) produciendo
un prob_yes mal calibrado con dinero real es demasiado alto para
duplicarla a mano, y CLAUDE.md exige cautela extra específicamente sobre
el prob_yes de esta familia (P17 meta-score). Por eso este ejecutor
IMPORTA _s_gbm_late() directamente de shadow_predict.py -- la MISMA
función que usa el ciclo lento, cero riesgo de divergencia de fórmula --
en vez de reimplementarla. Sí se replican a mano (como el resto de
ejecutores) los filtros de la capa exterior de s_gbm_late_15min()
(dirección por signo de edge, restricciones SOL, gate_bucket_propio):
son comparaciones simples, mismo criterio de riesgo que ya se acepta en
los otros ejecutores.

Gate de volumen: GATE_VOLUMEN_VALIDADO en shadow_predict.py exige
n_total_lado>=35 para GBM_LATE_15M#ETH#15min#BUY_YES (validado, vetante)
y solo OBSERVA (nunca veta) para SOL -- pero _gate_volumen_ballenas()
depende de smart_money_tracker.trades_de_mercado(), la MISMA API rota
diagnosticada esta noche (lag de indexación de minutos/horas + tope de
250) para BALLENAS_TARDIAS#ETH#5min. Aquí se usa en su lugar
ballenas_firehose_cache.py (ampliado hoy mismo a 15min) -- mismo arreglo,
otro marco temporal.

⚠️ DRY_RUN=True por defecto -- OBLIGATORIO. Ambas tuplas YA ESTÁN en
pares_permitidos_live (dinero real) vía el pipeline lento; si este
proceso arrancara con DRY_RUN=False empezaría a operar real de inmediato
en cuanto detectara la primera señal, sin revisión previa. Cambiar a
False SOLO tras revisión + aprobación explícita de Javi + /code-review,
mismo patrón en dos fases que TODOS los ejecutores anteriores.

⚠️ Doble camino de ejecución (mismo patrón ya aceptado en producción):
GBM_LATE_15M sigue viva en shadow_predict.py/live_trade.py (el ciclo
lento sigue intentando ejecutar ETH/SOL también) -- exactamente la misma
situación que FAVORITO_CONFIRMADO#BTC#60min#BUY_NO, que tiene su propio
ejecutor rápido (favorito_confirmado_btc60min_buyno_executor.py) MIENTRAS
shadow_predict.py sigue generando la misma tupla para el ciclo lento. La
idempotencia depende de lt._ya_operados_hoy() (ledger por market_id),
mismo mecanismo ya en producción para ese caso -- no se introduce ningún
lock nuevo entre procesos, mismo criterio de riesgo ya aceptado.

Corre en screen propia:
  screen -dmS gbmlate15m bash -c "cd /root/polymarket-research && .venv/bin/python gbm_late_15min_executor.py >> logs/gbm_late_15min_executor.log 2>&1"
"""
import json
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

import live_trade as lt
from live_guard import puede_operar_live
from live_stake import bloquear_por_circuit_breaker, calcular_stake
from ballenas_banda_fina_gate import evaluar as _gate_banda_fina_ballenas
from gate_bucket_propio import evaluar as _gate_bucket_propio
import ballenas_firehose_cache as _fc
from shadow_predict import (
    _s_gbm_late,
    cargar_precios_intraday,
    _cargar_spot,
    GBM_LATE_15M_REST_MIN_LO,
    GBM_LATE_15M_REST_MIN_HI,
    GBM_LATE_15M_SOL_HORAS_BUENAS_UTC,
    GBM_LATE_15M_SOL_PY_MIN,
    GBM_LATE_ESPACIO_K,
)

DIR = Path(__file__).resolve().parent
DIR_SHADOW = DIR / "data" / "shadow"
CONFIG_LIVE_PATH = DIR / "data" / "live" / "config_live.json"

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"

STRATEGY = "GBM_LATE_15M"
VENTANA_MIN = 15
ACTIVOS = ("ETH", "SOL", "XRP", "BTC", "BNB")  # 07-Ago: BNB añadida -- solo para ESPACIO_ATR, ver docstring
# XRP añadido 04-Ago (petición Javi, paso 4 del plan de acción de
# project_barrido_definitivo_latencia_17_combos_03ago): candidata NUNCA
# promovida, con el gap de latencia MÁS EXTREMO de todo el sistema
# (+249.5s, 44.9% de señales perdidas, n=1730/1029) -- no está en
# pares_permitidos_live, así que puede_operar_live() la bloquea siempre
# (whitelist), incluso si algún día DRY_RUN pasara a False por error en
# otra tupla. Sin gate de volumen validado propio (GATE_VOLUMEN_VALIDADO
# no tiene entrada para XRP) ni restricciones de hora/precio (esas son
# específicas de SOL, confirmadas 29-Jul) -- se trata igual que SOL antes
# de su gate propio: solo observación, nunca veta.

DRY_RUN = True  # 04-Ago v1 -- ver docstring, NO cambiar sin revisión + aprobación explícita + /code-review.

POLL_INTERVAL_S = 2.0    # ventana más ancha (9min) que el resto de ejecutores -- no hace falta 1-1.5s
HARD_FLOOR_S = 5.0       # margen de seguridad antes del cierre del mercado
REFRESCO_CTX_S = 20.0    # cadencia de recarga de precios_intraday/spot -- mismo orden que el propio
# fichero de precios (capturado cada ciclo del fast loop, ~20-100s), no hace falta releerlo cada poll

UMBRAL_VOL_ETH = 35  # mismo umbral validado que GATE_VOLUMEN_VALIDADO[("GBM_LATE_15M","ETH","15min","BUY_YES")]

# 04-Ago paso 5 del plan de latencia: GBM_LATE_15M_ESPACIO_ATR#{BTC,SOL}#15min
# (cementerio, pausadas 20-Jul por "selección adversa confirmada, shuffle
# p=0.000") -- misma _s_gbm_late(), solo difiere en espacio_k (ver
# s_gbm_late_15min_espacio_atr en shadow_predict.py). Puramente
# observacional: ninguna de las 2 está en pares_permitidos_live.
# Deliberadamente SIN las restricciones de hora/precio de SOL (esas están
# validadas solo para GBM_LATE_15M#SOL#15min#BUY_YES base, no transfieren
# sin evidencia propia a esta variante distinta) ni el veto de volumen de
# ETH (ETH no está en el alcance de esta variante).
#
# 07-Ago: ETH/BNB añadidas -- gate_bucket_propio.json tiene micro-buckets
# bueno_confirmado nunca instrumentados con baja latencia:
# ETH#15min#BUY_NO [0.60,0.65) n=46 pnl=+1.150€, [0.80,0.85) n=36
# pnl=+1.281€; BNB#15min#BUY_NO [0.50,0.55) n=100 pnl=+1.781€ -- todos
# medidos solo con el polling lento de candidato_evaluacion. BNB no
# estaba en absoluto en ACTIVOS (ningún hilo la vigilaba); ETH ya tenía
# hilo por la variante base pero no evaluaba ESPACIO_ATR. Mismo criterio
# que la generalización de UPDOWN_GBM_15M_TARDIO a XRP/BNB/SOL esta misma
# sesión: instrumentación, no promoción -- DRY_RUN sigue en True, ninguna
# de las 4 monedas está en pares_permitidos_live para esta variante.
STRATEGY_ESPACIO_ATR = "GBM_LATE_15M_ESPACIO_ATR"
ACTIVOS_ESPACIO_ATR = ("BTC", "SOL", "ETH", "BNB")

_session = requests.Session()
_orden_lock = threading.Lock()
_pares_live_cache = {"mtime": None, "set": set()}
_ctx_cache = {"ts": 0.0, "precios_intraday": [], "spot": {}}


def log(msg: str, activo: str = "") -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    prefijo = f"[{activo}] " if activo else ""
    print(f"[{ts}] {prefijo}{msg}", flush=True)


def _pares_live_hoy_set() -> set:
    """Mismo patrón fail-closed que el resto de ejecutores de baja latencia."""
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


def _ctx_ligero() -> dict:
    """precios_intraday + spot, recargados cada REFRESCO_CTX_S -- NO se
    construye el ctx completo de shadow_predict.py::construir_contexto()
    (funding rates, cross-source consensus, trades_1h/smart-flow, VWAP,
    QHE...) porque _s_gbm_late() solo necesita precios_intraday (spot se
    lee aparte, propia función _cargar_spot() sin ctx) -- el resto de
    features que construir_contexto() alimentaría (dist_vwap_pct,
    volumen_regimen) son PURO LOGUEO dentro de _s_gbm_late (no cambian
    prob_yes/edge/decisión, ver su docstring), así que faltar en ctx solo
    deja esos dos campos en None -- sin impacto en la decisión real."""
    ahora = time.time()
    if ahora - _ctx_cache["ts"] > REFRESCO_CTX_S:
        _ctx_cache["precios_intraday"] = cargar_precios_intraday()
        _ctx_cache["spot"] = _cargar_spot()
        _ctx_cache["ts"] = ahora
    return {"precios_intraday": _ctx_cache["precios_intraday"]}


def resolver_mercado(activo: str, ts_start: int) -> dict | None:
    """Una sola llamada gamma-api por ventana de 15min -- mismo patrón
    determinista que ballenas_executor_15min.py/_btc15m.py. Captura
    TAMBIÉN question/spread/liquidity (gratis, misma respuesta) --
    _s_gbm_late() los necesita (identificar_activo/_parse_updown_tipo
    sobre question; spread/liquidity solo para _libro_calidad, logueo)."""
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
            "question": mkt.get("question", ""),
            "spread": mkt.get("spread"),
            "liquidity": mkt.get("liquidity"),
            "yes_token": tokens[0],
            "no_token": tokens[1],
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


def _n_total_lado(condition_id: str, direccion: str) -> int | None:
    """Conteo de compras del lado elegido, vía firehose (04-Ago, sustituye
    la llamada rota a trades_de_mercado() que usa _gate_volumen_ballenas()
    en shadow_predict.py -- mismo diagnóstico/arreglo que
    ballenas_executor_5min.py esta noche). [] si el cache no está sano
    (fail-closed) -- devuelve None, el caller trata None como "sin dato"
    igual que antes con la API rota."""
    if not _fc.esta_sano():
        return None
    trades = _fc.trades_de_mercado_firehose(condition_id)
    lado_check = ("up", "yes") if direccion == "BUY_YES" else ("down", "no")
    return sum(1 for t in trades if (t.get("side") or "").strip().upper() == "BUY"
               and (t.get("outcome") or "").strip().lower() in lado_check)


def variantes_para(activo: str) -> list[tuple[str, dict]]:
    """(strategy_name, kwargs_extra_para__s_gbm_late) aplicables a esa
    moneda -- cada variante es una estrategia independiente (dedup por
    (strategy,market_id,decision) en shadow_resolve.py, arreglado 04-Ago),
    así que evaluar varias sobre el mismo mercado en el mismo poll es
    seguro y no se pisan entre sí."""
    variantes = []
    if activo in ("ETH", "SOL", "XRP"):
        variantes.append((STRATEGY, {}))
    if activo in ACTIVOS_ESPACIO_ATR:
        variantes.append((STRATEGY_ESPACIO_ATR, {"espacio_k": GBM_LATE_ESPACIO_K}))
    return variantes


def _registrar_prediccion(mercado: dict, activo: str, resultado: dict, direccion: str,
                           n_total_lado: int | None, restante_s: float,
                           strategy: str = STRATEGY) -> None:
    """Mismo formato que shadow_predict.py/el resto de ejecutores --
    shadow_resolve.py/shadow_postmortem.py lo resuelven sin duplicar
    lógica aquí."""
    import csv
    import fcntl
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    archivo = DIR_SHADOW / f"predictions_{ts[:10]}.csv"
    subtype = f"{activo}#{VENTANA_MIN}min"
    py = resultado["features"]["py_entrada"]
    prob_yes = resultado["prob_yes"]
    edge = prob_yes - py  # perspectiva YES, convención CLAUDE.md
    features = dict(resultado["features"])
    features["n_total_lado"] = n_total_lado
    features["ejecutor_baja_latencia"] = True
    features_json = json.dumps(features, separators=(",", ":"))
    lock_path = DIR_SHADOW / ".predictions_lock"
    try:
        with open(lock_path, "w") as lock_f:
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
                        resultado.get("razon", "") + " (ejecutor baja latencia)", subtype,
                        "1.05", features_json,
                    ])
            finally:
                fcntl.flock(lock_f, fcntl.LOCK_UN)
    except Exception as e:
        log(f"aviso: no se pudo registrar predicción para postmortem: {e}", activo)


def watch_window(activo: str, mercado: dict) -> bool:
    """Vigila un mercado {activo}#15min concreto -- entra en juego en
    cuanto restante_min cae dentro de [GBM_LATE_15M_REST_MIN_LO,
    GBM_LATE_15M_REST_MIN_HI] (mismo rango que la estrategia madre) y
    sale sola cuando restante_min < LO (ventana cerrada) o el mercado
    cierra. Evalúa TODAS las variantes aplicables a `activo` (ver
    variantes_para) en el mismo poll, sobre el mismo precio -- cada una
    con sus propias reglas, sin heredar restricciones de otra variante
    (SOL-horas/precio y volumen-ETH son específicas de STRATEGY base,
    nunca se aplican a ESPACIO_ATR). True si alguna ejecutó (o habría
    ejecutado en DRY_RUN)."""
    try:
        end_dt = datetime.fromisoformat(mercado["end_date"].replace("Z", "+00:00"))
        if end_dt.tzinfo is None:
            end_dt = end_dt.replace(tzinfo=timezone.utc)
    except Exception:
        log(f"end_date ilegible: {mercado.get('end_date')} -- se abandona", activo)
        return False
    ts_end = end_dt.timestamp()
    n_polls = 0
    contadores = {"ok_sin_edge": 0, "sin_dato": 0, "vetado_volumen": 0, "vetado_gate_bucket": 0}
    variantes = variantes_para(activo)

    while True:
        restante_s = ts_end - time.time()
        restante_min = restante_s / 60.0
        if restante_s < HARD_FLOOR_S or restante_min < GBM_LATE_15M_REST_MIN_LO:
            log(f"[{mercado['market_id']}] fuera de ventana (restante={restante_min:.1f}min) -- "
                f"se abandona ({n_polls} polls, {contadores})", activo)
            return False
        if mercado["market_id"] in lt._ya_operados_hoy():
            log(f"[{mercado['market_id']}] ya operado -- se abandona", activo)
            return False
        if restante_min > GBM_LATE_15M_REST_MIN_HI:
            time.sleep(min((restante_min - GBM_LATE_15M_REST_MIN_HI) * 60, 5))
            continue

        libro = libro_publico(mercado["yes_token"])
        n_polls += 1
        py = libro.get("best_ask") if libro else None
        if py is None:
            contadores["sin_dato"] += 1
            time.sleep(POLL_INTERVAL_S)
            continue

        market_full = dict(mercado)
        market_full["_precio_yes"] = py
        ctx = _ctx_ligero()

        hubo_confirmacion = False
        for strategy, kwargs_extra in variantes:
            resultado = _s_gbm_late(market_full, ctx, ventana_min=VENTANA_MIN,
                                    rest_lo=GBM_LATE_15M_REST_MIN_LO, rest_hi=GBM_LATE_15M_REST_MIN_HI,
                                    **kwargs_extra)
            if resultado is None:
                contadores["ok_sin_edge"] += 1
                continue

            py_edge = resultado["features"]["py_entrada"]
            prob_yes_dir = resultado["prob_yes"]
            direccion = "BUY_YES" if prob_yes_dir >= py_edge else "BUY_NO"

            if strategy == STRATEGY and activo == "SOL" and direccion == "BUY_YES":
                if datetime.now(timezone.utc).hour not in GBM_LATE_15M_SOL_HORAS_BUENAS_UTC:
                    continue
                if py_edge < GBM_LATE_15M_SOL_PY_MIN:
                    continue

            n_total_lado = _n_total_lado(mercado["condition_id"], direccion)
            if strategy == STRATEGY and activo == "ETH" and (n_total_lado is None or n_total_lado < UMBRAL_VOL_ETH):
                contadores["vetado_volumen"] += 1
                log(f"[{mercado['market_id']}] {strategy} py={py:.3f} edge cruza pero n_total_lado="
                    f"{n_total_lado} < {UMBRAL_VOL_ETH} -- vetado por volumen bajo", activo)
                continue

            restante_min_actual = resultado["features"]["restante_min"]
            gate_bf = _gate_banda_fina_ballenas(activo, f"{VENTANA_MIN}min", py_edge, restante_min_actual)
            resultado["features"]["banda_fina_vetaria_fase1"] = gate_bf["vetaria_fase1"]
            resultado["features"]["banda_fina_motivo"] = gate_bf["motivo"]

            tupla_str = f"{strategy}#{activo}#{VENTANA_MIN}min#{direccion}"
            gate_bp = _gate_bucket_propio(tupla_str, py_edge)
            resultado["features"]["gate_bucket_propio_veredicto"] = gate_bp["veredicto"]
            if gate_bp["veredicto"] == "malo_confirmado" and tupla_str in _pares_live_hoy_set():
                contadores["vetado_gate_bucket"] += 1
                log(f"[{mercado['market_id']}] {strategy} py={py_edge:.3f} vetado por "
                    f"gate_bucket_propio (malo_confirmado)", activo)
                continue

            log(f"[{mercado['market_id']}] {strategy} CONFIRMADO {direccion} py={py_edge:.3f} "
                f"prob_yes={prob_yes_dir:.3f} restante={restante_s:.1f}s n_total_lado={n_total_lado} "
                f"d={resultado['features']['d_gbm']} ({n_polls} polls)", activo)
            _registrar_prediccion(mercado, activo, resultado, direccion, n_total_lado, restante_s,
                                  strategy=strategy)
            disparar(activo, mercado, py_edge, prob_yes_dir, direccion, restante_s, strategy=strategy)
            hubo_confirmacion = True

        if hubo_confirmacion:
            return True
        time.sleep(POLL_INTERVAL_S)


def disparar(activo: str, mercado: dict, py: float, prob_yes: float, direccion: str,
             restante_s: float, strategy: str = STRATEGY) -> bool:
    """Mismos guardias, mismo orden, que el resto de ejecutores de baja
    latencia (favorito_confirmado_btc60min_buyno_executor.py/
    ballenas_executor_5min.py) -- este ejecutor tampoco pasa por
    live_trade.py::main(), ninguno de sus guardias se aplica gratis.
    `strategy` (04-Ago): GBM_LATE_15M o GBM_LATE_15M_ESPACIO_ATR según la
    variante que confirmó -- whitelist/CLV/stake/registro siempre con el
    nombre exacto de la variante que disparó, nunca el de la base a
    ciegas."""
    subtype = f"{activo}#{VENTANA_MIN}min"

    ok_operar, motivo_operar = puede_operar_live(strategy, subtype)
    if not ok_operar:
        log(f"  {motivo_operar} -- {'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
        return False

    config = lt._cargar_config()
    max_misma_dir = config.get("riesgo", {}).get("max_posiciones_abiertas_misma_direccion", 2)
    abiertas_dir = lt._posiciones_abiertas_misma_direccion(direccion)
    if abiertas_dir >= max_misma_dir:
        log(f"  techo de correlación: {abiertas_dir} posiciones {direccion} abiertas >= {max_misma_dir} -- "
            f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
        return False

    with _orden_lock:
        if mercado["market_id"] in lt._ya_operados_hoy():
            log(f"  {mercado['market_id']} ya operado por otro proceso -- "
                f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        if bloquear_por_circuit_breaker(
                lambda motivo: log(f"  circuit breaker activo ({motivo}) -- "
                                    f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)):
            return False

        lt._CLV_CACHE = None
        clv_medio, n_clv = lt._clv_tupla(strategy, subtype, direccion)
        if n_clv >= lt.CLV_VETO_MIN_N and clv_medio < 0:
            log(f"  ⛔ Veto CLV: clv_medio={clv_medio:+.4f} (n={n_clv}) < 0 -- "
                f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        # Kelly exacto real para binarias (mismo criterio ya usado en
        # ballenas_executor_15min.py/favorito_confirmado_btc60min_buyno_executor.py):
        # BUY_YES: f*=(p-py)/(1-py); BUY_NO: f*=(py-p)/py. precio_entrada en
        # perspectiva de la DECISIÓN (calcular_stake resuelve 1-py si BUY_NO).
        if direccion == "BUY_YES":
            edge_dir = prob_yes - py
            ic_conviccion = max(0.0, edge_dir / (1 - py)) if py < 1 else 0.0
            precio_decision = py
        else:
            edge_dir = py - prob_yes
            ic_conviccion = max(0.0, edge_dir / py) if py > 0 else 0.0
            precio_decision = round(1.0 - py, 6)

        stake_info = calcular_stake(ic_conviccion, strategy, subtype, direction=direccion,
                                    precio_entrada=precio_decision)
        if not stake_info.get("viable"):
            log(f"  stake no viable: {stake_info.get('motivo')} -- "
                f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        if DRY_RUN:
            log(f"  [DRY-RUN] habría ejecutado {direccion} {mercado['market_id']} py={py:.3f} "
                f"prob_yes={prob_yes:.3f} stake={stake_info['stake_eur']:.2f}€ restante={restante_s:.1f}s",
                activo)
            return True

        resultado = lt._ejecutar_orden_polymarket(
            mercado["market_id"], direccion, stake_info["stake_eur"], py,
            edge_dir=edge_dir, contexto={"strategy": strategy, "subtype": subtype})

        if resultado.get("no_fill"):
            log(f"  no_fill: {resultado.get('error')}", activo)
            return False

        trade = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "market_id": mercado["market_id"], "question": "", "end_date": mercado.get("end_date", ""),
            "strategy": strategy, "subtype": subtype, "direction": direccion,
            "stake_eur": stake_info["stake_eur"] if resultado["ok"] else 0.0,
            "entry_price": resultado["entry_price"],
            "signal_ask": round(py, 4), "slip_real": resultado.get("slip_real", ""),
            "ic_modelo": round(prob_yes, 4), "edge_neto": round(prob_yes - py, 4),
            "conviction_score": round(prob_yes, 4), "kelly_recomendado": stake_info["stake_eur"],
            "status": "OPEN" if resultado["ok"] else "ERROR",
            "close_timestamp": "", "exit_price": "", "outcome_real": "",
            "fee_eur": resultado.get("fee_eur", 0), "pnl_bruto_eur": "", "pnl_neto_eur": "",
            "notas": (f"{strategy.lower()}_baja_latencia restante={restante_s:.1f}s"
                      if resultado.get("ok") else resultado.get("error", "")),
        }
        lt._registrar_trade(trade)
        log(f"  {'EJECUTADO' if resultado['ok'] else 'ERROR'}: {resultado}", activo)
        if resultado["ok"]:
            lt.enviar_telegram(
                f"🎯 *Orden live ejecutada ({strategy} baja latencia)*\n"
                f"Estrategia: {strategy}#{subtype}#{direccion}\n"
                f"Precio fill: {resultado['entry_price']:.4f} (slip {resultado.get('slip_real', 0):+.4f})\n"
                f"Stake: {stake_info['stake_eur']:.2f}$  |  restante={restante_s:.1f}s\n"
                f"Bankroll operativo: {lt.bankroll_actual():.2f}$ (real al cierre de ciclo)"
            )
        else:
            lt.enviar_telegram(
                f"❌ *Orden live ERROR ({strategy} baja latencia)*\n"
                f"{strategy}#{subtype} {direccion}\n{resultado.get('error', '')[:200]}"
            )
        return True


def hilo_activo(activo: str) -> None:
    log("hilo arrancado", activo)
    mercado_vigilado = None
    while True:
        try:
            now = time.time()
            ts_end = (int(now) // (VENTANA_MIN * 60) + 1) * (VENTANA_MIN * 60)
            ts_start = ts_end - VENTANA_MIN * 60
            if ts_start == mercado_vigilado:
                time.sleep(5)
                continue
            mercado = resolver_mercado(activo, ts_start)
            if mercado is None:
                time.sleep(10)
                continue
            mercado_vigilado = ts_start
            watch_window(activo, mercado)
        except Exception as e:
            log(f"error en hilo: {e} -- reintenta en 5s", activo)
            time.sleep(5)


def main():
    log(f"gbm_late_15min_executor arrancado (DRY_RUN={DRY_RUN}, activos={list(ACTIVOS)})")
    _fc.iniciar()
    time.sleep(3)
    if not DRY_RUN:
        _ = lt._get_clob_client()
        log("ClobClient precalentado")

    hilos = [threading.Thread(target=hilo_activo, args=(activo,), daemon=True, name=activo)
             for activo in ACTIVOS]
    for h in hilos:
        h.start()

    ciclos_firehose_no_sano = 0
    while True:
        time.sleep(30)
        for i, h in enumerate(hilos):
            if not h.is_alive():
                activo = h.name
                log("hilo murió inesperadamente -- reiniciando", activo)
                nuevo = threading.Thread(target=hilo_activo, args=(activo,), daemon=True, name=activo)
                nuevo.start()
                hilos[i] = nuevo

        if _fc.esta_sano():
            ciclos_firehose_no_sano = 0
        else:
            ciclos_firehose_no_sano += 1
            if ciclos_firehose_no_sano >= 4:
                log(f"⚠️ cache de firehose lleva ~{ciclos_firehose_no_sano * 30}s no sano -- "
                    f"revisar conexión RTDS/logs")


if __name__ == "__main__":
    main()
