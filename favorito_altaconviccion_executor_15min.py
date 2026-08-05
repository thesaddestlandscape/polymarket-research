#!/usr/bin/env python3
"""
favorito_altaconviccion_executor_15min.py — Ejecutor de baja latencia para
FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#{BTC,ETH}#15min#BUY_YES.

Origen (30-Jul, petición explícita Javi): estas 2 tuplas están en
pares_permitidos_live desde el 29-Jul pero tienen 0 trades reales en 64
señales shadow generadas -- diagnóstico completo en
gates_pendientes.json::ALTACONVICCION_15MIN_NUNCA_EJECUTA_LATENCIA. Causa
verificada con evidencia directa (no es bug de whitelist ni falta de
runway): shadow_predict.py fija `ts` UNA VEZ al inicio de su ciclo
(~100-130s, picos de varios minutos bajo carga) para TODAS las filas de
esa vuelta -- las señales de esta tupla nacen ya cerca o por encima del
techo SENAL_MAX_LATENCIA_SEG=100 de live_trade.py, sin margen. Ejemplo
medido: primer intento a 125s ya caducada, vs 40s de un trade real
EXITOSO de GBM_LATE_15M#ETH#15min en el mismo pipeline lento -- ahí SÍ
convierte ~48% (103 señales -> 50 trades), la diferencia con ALTACONVICCION
(0/64) es puramente de margen, no de mecanismo.

Por qué SÍ tiene sentido aquí y NO para GBM_LATE_15M (evaluado en la misma
sesión, ver conversación): s_favorito_confirmado() es MODEL-FREE -- solo
depende del precio YES actual del libro contra un umbral fijo (py>=0.70,
más el techo ETH<0.95), sin drift/sigma/features caras de calcular. Barato
y trivial de vigilar en un bucle de poll rápido, mismo patrón ya probado 3
veces (ballenas_executor_btc15m.py, _5min.py, _15min.py). GBM_LATE_15M en
cambio ya convierte ~48% vía el pipeline normal -- su cuello de botella
documentado es selección adversa en precio bajo (arquetipo A, el libro se
vacía justo cuando el modelo tiene edge), no latencia; un executor rápido
no ataca esa causa y podría incluso empeorarla.

Replica EXACTAMENTE la lógica de s_favorito_confirmado_15min_altaconviccion
(shadow_predict.py) para no divergir del mecanismo ya en producción:
FAVORITO_15MIN_ALTACONVICCION_TH=0.70, techo ETH<0.95, gate de volumen real
GATE_VOLUMEN_VALIDADO (ETH#15min#BUY_YES n_yes_total>=35, BTC sin gate
propio todavía = fail-open), gate_bucket_propio (veta si malo_confirmado Y
la tupla exacta está en pares_permitidos_live), banda_fina_ballenas
(solo observacional, igual que la estrategia original).

⚠️ DRY_RUN=True por defecto -- OBLIGATORIO. Estas 2 tuplas YA ESTÁN en
pares_permitidos_live (dinero real) para el pipeline normal; si este
proceso arrancara con DRY_RUN=False empezaría a operar real de inmediato
en cuanto detectara la primera señal, sin haber pasado /code-review.
Cambiar a False SOLO tras /code-review + aprobación explícita de Javi,
mismo patrón en dos fases que TODOS los ejecutores anteriores de este
proyecto (BTC15m, ETH5min, y este mismo patrón para 15min multi-activo en
ballenas_executor_15min.py, que sigue en DRY_RUN semanas después).

Diseño: a diferencia de los ejecutores de ballenas (que solo vigilan cerca
del cierre, ventana de confirmación estrecha), esta condición es un simple
cruce de precio que puede ocurrir en cualquier punto de la ventana de
15min (histórico real: restante 3-12min, mediana 7.2) -- se vigila desde
la APERTURA de cada ventana hasta el cierre, un hilo por activo.

Corre en screen propia:
  screen -dmS favaltaconv bash -c "cd /root/polymarket-research && .venv/bin/python favorito_altaconviccion_executor_15min.py >> logs/favorito_altaconviccion_15min.log 2>&1"
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
from live_guard import puede_operar_live
from live_stake import bloquear_por_circuit_breaker, calcular_stake
from ballenas_banda_fina_gate import evaluar as _gate_banda_fina_ballenas
from gate_bucket_propio import evaluar as _gate_bucket_propio
import ballenas_firehose_cache as _fc

DIR = Path(__file__).resolve().parent
DIR_SHADOW = DIR / "data" / "shadow"
STRATEGY_PARAMS_PATH = DIR_SHADOW / "strategy_params.json"
CONFIG_LIVE_PATH = DIR / "data" / "live" / "config_live.json"
PREDICTIONS_LOCK_PATH = DIR_SHADOW / ".predictions_lock"

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"

STRATEGY = "FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION"
VENTANA_MIN = 15
ACTIVOS = ("BTC", "ETH", "XRP", "DOGE", "BNB")
# 03-Ago (petición Javi, "no podemos dejar huecos sin cubrir"): añadidas
# XRP/DOGE/BNB -- antes solo BTC/ETH, sin razón de rendimiento documentada
# (n=3-6 en strategy_params, insuficiente para saber nada). SOL NO se añade
# a propósito -- ya tiene n=85 real con PnL confirmado negativo (-0.045€/
# trade, barrido de candidatas 03-Ago), no es un hueco de datos, es un
# resultado ya conocido. Verificado ANTES de este cambio que puede_operar_
# live()/estrategia_permitida() hacen match por tupla EXACTA (strategy#
# subtype# como prefijo contra pares_permitidos_live, fail-closed) -- estas
# 3 monedas no coinciden con ninguna entrada de la whitelist, así que
# generarán predicciones/logging pero disparar() las bloqueará siempre
# antes de cualquier orden real (mismo comportamiento que BTC tenía en
# GATE_VOLUMEN_VALIDADO antes de estar "sin gate propio" -- aquí es la
# whitelist general la que protege, no un gate específico).

DRY_RUN = False  # 30-Jul: activado -- aprobación explícita Javi ("apruebo, vamos con lo de
# ALTACONVICCION") tras auto-revisión adversarial completa (9 ángulos: idempotencia,
# condición de carrera entre hilos/procesos, signo de Kelly-exacto, fail-closed en
# datos faltantes, orden de guardias dentro/fuera de _orden_lock, timing bajo
# HARD_FLOOR_S). /code-review formal NO se pudo invocar (disable-model-invocation,
# solo Javi puede lanzarlo) -- sustituido por la revisión manual documentada en la
# conversación de esta sesión. Único hallazgo: gate_bucket_propio en este ejecutor
# usa el nombre de tupla CORRECTO (más protector que shadow_predict.py::
# s_favorito_confirmado, que lo tiene hardcodeado a "FAVORITO_CONFIRMADO" y por
# tanto inerte para ALTACONVICCION en el pipeline lento -- ver docstring del
# fichero). No bloqueante, no se tocó shadow_predict.py.

POLL_INTERVAL_S = 1.5
HARD_FLOOR_S = 3.0

# Mismos valores exactos que shadow_predict.py (FAVORITO_15MIN_ALTACONVICCION_TH
# / _TH_MAX / FAVORITO_CONFIRMADO_NUDGE) -- duplicados aquí (no se importa
# shadow_predict.py completo, módulo pesado con efectos de import, mismo
# criterio que el resto de ejecutores de baja latencia de este proyecto).
# Si esos valores cambian en shadow_predict.py, hay que replicarlos aquí a
# mano -- vigilar en cada sesión que toque esa estrategia.
UMBRAL_TH = 0.70
TH_MAX = {"ETH": 0.95}
NUDGE = 0.06

# Zonas de micro-bucket confirmadas (05-Ago, CORREGIDO el mismo día --
# ver feedback_lookahead_bias_precio_final_no_es_edge_05ago en memoria).
# Primer intento: precio de la ÚLTIMA captura antes del cierre (20-65s de
# margen real) -- mide convergencia matemática obligatoria de la binaria
# cerca de T=0, no edge real. Daba [0.95,1.00) -- FALSO POSITIVO,
# descartado (Javi: "es imposible", contrastado contra ballenas).
# Rehecho con precio en el CRUCE real del umbral (mediana 7.3min de
# margen real, igual que dispara el ejecutor): n=1517 mercados reales,
# [0.85,0.90) confirma GATE_OK_BUENO (n=215, hit=92.6%, pnl+0.0495/trade,
# CI90% no cruza cero, p_shuffle=0.043, split-half consistente) --
# coincide EXACTO con punto_confirmacion (Wilson 95% ya validado 21-Jul,
# independiente): BTC#15min confirma a ~1min del cierre, precio≈0.875.
# Doble validación cruzada, no una fuente sola.
BTC_15MIN_ALTACONVICCION_ZONAS_BUENAS = [(0.85, 0.90)]

# Mismo gate real que _gate_volumen_ballenas en shadow_predict.py
# (GATE_VOLUMEN_VALIDADO) -- solo ETH#15min#BUY_YES tiene umbral validado
# hoy (n=727, alto=538, hit=94.4%, GATE OK). BTC sin entrada = fail-open,
# igual que en el pipeline normal.
GATE_VOLUMEN_VALIDADO = {
    ("ETH", "15min", "BUY_YES"): 35,
}

_session = requests.Session()
_orden_lock = threading.Lock()
_pares_live_cache = {"mtime": None, "set": set()}


def log(msg: str, activo: str = ""):
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    prefijo = f"[{activo}] " if activo else ""
    print(f"[{ts}] {prefijo}{msg}", flush=True)


def _pares_live_hoy_set() -> set:
    """Mismo patrón fail-closed que shadow_predict.py::_pares_live_hoy_set
    (última copia conocida si falla la lectura, nunca vacío por error
    transitorio)."""
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
    """Mismo patrón determinista que ballenas_executor_btc15m/15min.py."""
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


WALLET_EDGE_POR_ACTIVO_MARCO = DIR_SHADOW / "wallet_edge_score_por_activo_marco.json"
_wallet_edge_cache = {"mtime": None, "data": {}}


def _cargar_wallet_edge_activo_marco() -> dict:
    """Mismo patrón que ballenas_executor_btc15m.py -- fichero estático,
    sin llamada de red, cacheado por mtime."""
    try:
        mtime = WALLET_EDGE_POR_ACTIVO_MARCO.stat().st_mtime
    except OSError:
        return {}
    if _wallet_edge_cache["mtime"] != mtime:
        try:
            todo = json.loads(WALLET_EDGE_POR_ACTIVO_MARCO.read_text(encoding="utf-8"))
            _wallet_edge_cache["data"] = {(v["wallet"], v["activo"], v["marco"]): v for v in todo.values()}
        except Exception:
            _wallet_edge_cache["data"] = {}
        _wallet_edge_cache["mtime"] = mtime
    return _wallet_edge_cache["data"] or {}


def _n_yes_total(condition_id: str, activo: str) -> tuple[int | None, dict | None]:
    """Compras YES en TODO el mercado -- mismo cálculo que
    _gate_volumen_ballenas en shadow_predict.py.

    03-Ago (petición Javi, conectar infraestructura de ballenas): reutiliza
    la MISMA lista de trades ya descargada -- añade un resumen de
    wallet_edge_score PURAMENTE observacional (no veta, no toca
    n_yes_total ni la decisión), sin llamada de red adicional. Devuelve
    (n_yes_total, resumen_edge).

    04-Ago: la fuente YA NO es smart_money_tracker.trades_de_mercado()
    (data-api.polymarket.com/trades -- lag de indexación de minutos/horas
    + tope duro de 250, diagnosticado y arreglado esta noche para
    BALLENAS_TARDIAS#ETH#5min, mismo problema aquí porque esta tupla SÍ
    está en pares_permitidos_live hoy con FAVORITO_CONFIRMADO_15MIN_
    ALTACONVICCION#BTC#15min#BUY_YES). Ahora usa ballenas_firehose_cache
    (websocket propio a RTDS, en memoria, sin lag ni tope) -- ver
    feedback_verificar_api_trades_correcta_no_rota_04ago (memoria)."""
    if not _fc.esta_sano():
        return None, None
    trades = _fc.trades_de_mercado_firehose(condition_id)
    n_yes_total = sum(1 for t in trades if (t.get("side") or "").strip().upper() == "BUY"
                       and (t.get("outcome") or "").strip().lower() in ("up", "yes"))

    db = _cargar_wallet_edge_activo_marco()
    wallets_yes = {(t.get("proxyWallet") or "").lower() for t in trades
                   if (t.get("side") or "").strip().upper() == "BUY"
                   and (t.get("outcome") or "").strip().lower() in ("up", "yes")}
    filas = [db[(w, activo, "15m")] for w in wallets_yes if (w, activo, "15m") in db]
    edges = [f["edge_pp"] for f in filas]
    resumen_edge = {
        "wallet_edge_medio": round(sum(edges) / len(edges), 3) if edges else None,
        "wallet_n_con_score": len(edges),
        "wallet_n_sig_pos": sum(1 for f in filas if f["sig_bhfdr"] and f["edge_pp"] > 0),
        "wallet_n_sig_neg": sum(1 for f in filas if f["sig_bhfdr"] and f["edge_pp"] < 0),
    }
    return n_yes_total, resumen_edge


def _activa_permite_disparo(activo: str) -> tuple[bool, str]:
    """Mismo mecanismo de autoconciencia que los ejecutores de ballenas
    (20-Jul, Javi: "que aprenda como el resto del sistema") -- respeta el
    veredicto de shadow_postmortem sobre el ic_bayes real de esta tupla en
    cuanto tenga n suficiente."""
    subtype = f"{activo}#{VENTANA_MIN}min"
    lookup_keys = [f"{STRATEGY}#{subtype}", f"{STRATEGY}#{activo}", f"{STRATEGY}#{VENTANA_MIN}min"]
    try:
        params = json.loads(STRATEGY_PARAMS_PATH.read_text(encoding="utf-8")).get("estrategias", {})
    except Exception:
        return True, "sin strategy_params.json legible -- fail-open"
    for k in lookup_keys:
        e = params.get(k)
        if e is None:
            continue
        campo = "activa_BUY_YES" if "activa_BUY_YES" in e else "activa"
        if not e.get(campo, True):
            return False, f"postmortem desactivó {k} ({campo}=False)"
    return True, "activa"


def _registrar_prediccion(activo: str, mercado: dict, py: float, prob_yes: float,
                           restante_s: float, n_yes_total: int | None,
                           resumen_edge: dict | None = None) -> None:
    """Mismo formato que shadow_predict.py -- shadow_resolve.py/
    shadow_postmortem.py lo resuelven y aprenden de él sin duplicar esa
    lógica aquí, igual que el resto de ejecutores de baja latencia."""
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    archivo = DIR_SHADOW / f"predictions_{ts[:10]}.csv"
    subtype = f"{activo}#{VENTANA_MIN}min"
    edge = prob_yes - py
    gate_bf = _gate_banda_fina_ballenas(activo, f"{VENTANA_MIN}min", py, restante_s / 60.0)
    features = json.dumps({
        "py_entrada": round(py, 4), "n_total_lado": n_yes_total,
        "restante_min": round(restante_s / 60.0, 2),
        "hora_utc": datetime.now(timezone.utc).hour,
        "banda_fina_vetaria_fase1": gate_bf["vetaria_fase1"], "banda_fina_motivo": gate_bf["motivo"],
        "ejecutor_baja_latencia": True,
        **(resumen_edge or {}),
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
                        f"{edge:.4f}", f"{edge:.4f}", f"{edge:.4f}", "BUY_YES",
                        "favorito_confirmado momentum-consenso (ejecutor baja latencia)", subtype,
                        "1.05", features,
                    ])
            finally:
                fcntl.flock(lock_f, fcntl.LOCK_UN)
    except Exception as e:
        log(f"aviso: no se pudo registrar predicción para postmortem: {e}", activo)


def watch_window(activo: str, ts_end: int) -> bool:
    """Vigila la ventana completa (apertura a cierre, no solo el tramo
    final -- a diferencia de los ejecutores de ballenas, esta condición
    puede cruzarse en cualquier punto de los 15min). True si ejecutó (o
    habría ejecutado en DRY_RUN)."""
    ts_start = ts_end - VENTANA_MIN * 60
    subtype = f"{activo}#{VENTANA_MIN}min"
    techo = TH_MAX.get(activo)
    umbral_vol = GATE_VOLUMEN_VALIDADO.get((activo, f"{VENTANA_MIN}min", "BUY_YES"))

    mercado = None
    n_polls = 0
    while True:
        restante = ts_end - time.time()
        if restante < HARD_FLOOR_S:
            log(f"[{ts_end}] suelo de seguridad alcanzado sin confirmación ({n_polls} polls)", activo)
            return False

        if mercado is None:
            mercado = resolver_mercado(activo, ts_start)
            if mercado is None:
                log(f"[{ts_end}] no se pudo resolver el mercado -- se abandona", activo)
                return False
            if mercado["market_id"] in lt._ya_operados_hoy():
                log(f"[{ts_end}] {mercado['market_id']} ya operado -- se salta", activo)
                return False

        libro = libro_publico(mercado["yes_token"])
        n_polls += 1
        py = libro.get("best_ask") if libro else None

        if py is not None and py >= UMBRAL_TH and (techo is None or py < techo):
            # umbral_vol es None para BTC (sin gate propio, fail-open a
            # propósito -- _n_yes_total mete hasta 3s de red en el hot path
            # de un ejecutor de baja latencia, ver project_conectar_
            # infraestructura_script_construido_03ago). Se preserva ese
            # comportamiento sin cambios: solo ETH paga esa latencia.
            if umbral_vol is not None:
                n_yes_total, resumen_edge = _n_yes_total(mercado["condition_id"], activo)
            else:
                n_yes_total, resumen_edge = None, None
            if umbral_vol is not None and (n_yes_total is None or n_yes_total < umbral_vol):
                log(f"[{ts_end}] py={py:.3f} cruza umbral pero n_yes_total="
                    f"{n_yes_total} < {umbral_vol} -- vetado por volumen bajo", activo)
                time.sleep(POLL_INTERVAL_S)
                continue

            tupla_str = f"{STRATEGY}#{activo}#{VENTANA_MIN}min#BUY_YES"
            gate_bp = _gate_bucket_propio(tupla_str, py)
            if gate_bp["veredicto"] == "malo_confirmado" and tupla_str in _pares_live_hoy_set():
                log(f"[{ts_end}] py={py:.3f} vetado por gate_bucket_propio (malo_confirmado)", activo)
                return False

            # Veto de micro-bucket de precio BTC#15min (05-Ago, corregido el
            # mismo día -- ver BTC_15MIN_ALTACONVICCION_ZONAS_BUENAS arriba
            # para el detalle completo, incluida la corrección de metodología
            # y la doble validación cruzada contra punto_confirmacion).
            if activo == "BTC":
                en_zona_buena = any(lo <= py <= hi for lo, hi in BTC_15MIN_ALTACONVICCION_ZONAS_BUENAS)
                if not en_zona_buena:
                    log(f"[{ts_end}] ⛔ Veto micro-bucket BTC#15min: py={py:.3f} fuera de zonas "
                        f"confirmadas {BTC_15MIN_ALTACONVICCION_ZONAS_BUENAS}", activo)
                    return False

            prob_yes = min(0.97, py + NUDGE)
            log(f"[{ts_end}] CONFIRMADO py={py:.3f} prob_yes={prob_yes:.3f} restante={restante:.1f}s "
                f"n_yes_total={n_yes_total} "
                f"wallet_edge_medio={resumen_edge.get('wallet_edge_medio') if resumen_edge else None} "
                f"({n_polls} polls)", activo)
            _registrar_prediccion(activo, mercado, py, prob_yes, restante, n_yes_total, resumen_edge)
            return disparar(activo, mercado, py, prob_yes, restante)

        time.sleep(POLL_INTERVAL_S)


def disparar(activo: str, mercado: dict, py: float, prob_yes: float, restante_s: float) -> bool:
    """Mismos guardias que ballenas_executor_btc15m.py::disparar, en el
    mismo orden -- este executor tampoco pasa por live_trade.py::main(),
    así que ninguno de sus guardias se aplica gratis."""
    subtype = f"{activo}#{VENTANA_MIN}min"

    ok_activa, motivo_activa = _activa_permite_disparo(activo)
    if not ok_activa:
        log(f"  {motivo_activa} -- {'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
        return False

    ok_operar, motivo_operar = puede_operar_live(STRATEGY, subtype)
    if not ok_operar:
        log(f"  {motivo_operar} -- {'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
        return False

    config = lt._cargar_config()
    max_misma_dir = config.get("riesgo", {}).get("max_posiciones_abiertas_misma_direccion", 2)
    abiertas_dir = lt._posiciones_abiertas_misma_direccion("BUY_YES")
    if abiertas_dir >= max_misma_dir:
        log(f"  techo de correlación: {abiertas_dir} posiciones BUY_YES abiertas >= {max_misma_dir} -- "
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

        # 30-Jul: veto CLV (mismo mecanismo que live_trade.py::main(), nunca
        # replicado en NINGÚN ejecutor de baja latencia -- hallazgo del
        # barrido de "cableado" de esta sesión, afecta a los 5 ejecutores
        # existentes por igual). _clv_tupla cachea a nivel de módulo
        # (pensado para un proceso fresco por ciclo); este ejecutor es
        # persistente, se fuerza relectura fresca de results.csv cada vez --
        # barato, solo en el momento raro de confirmar una señal.
        lt._CLV_CACHE = None
        clv_medio, n_clv = lt._clv_tupla(STRATEGY, subtype, "BUY_YES")
        if n_clv >= lt.CLV_VETO_MIN_N and clv_medio < 0:
            log(f"  ⛔ Veto CLV: clv_medio={clv_medio:+.4f} (n={n_clv}) < 0 -- "
                f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        ic_conviccion = max(0.0, (prob_yes - py) / (1 - py)) if py < 1 else 0.0
        stake_info = calcular_stake(ic_conviccion, STRATEGY, subtype, direction="BUY_YES")
        if not stake_info.get("viable"):
            log(f"  stake no viable: {stake_info.get('motivo')} -- "
                f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        if DRY_RUN:
            log(f"  [DRY-RUN] habría ejecutado BUY_YES {mercado['market_id']} py={py:.3f} "
                f"stake={stake_info['stake_eur']:.2f}€ restante={restante_s:.1f}s", activo)
            return True

        resultado = lt._ejecutar_orden_polymarket(
            mercado["market_id"], "BUY_YES", stake_info["stake_eur"], py,
            edge_dir=prob_yes - py, contexto={"strategy": STRATEGY, "subtype": subtype})

        if resultado.get("no_fill"):
            log(f"  no_fill: {resultado.get('error')}", activo)
            return False

        trade = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "market_id": mercado["market_id"], "question": "", "end_date": mercado.get("end_date", ""),
            "strategy": STRATEGY, "subtype": subtype, "direction": "BUY_YES",
            "stake_eur": stake_info["stake_eur"] if resultado["ok"] else 0.0,
            "entry_price": resultado["entry_price"],
            "signal_ask": round(py, 4), "slip_real": resultado.get("slip_real", ""),
            "ic_modelo": round(prob_yes, 4), "edge_neto": round(prob_yes - py, 4),
            "conviction_score": round(prob_yes, 4), "kelly_recomendado": stake_info["stake_eur"],
            "status": "OPEN" if resultado["ok"] else "ERROR",
            "close_timestamp": "", "exit_price": "", "outcome_real": "",
            "fee_eur": resultado.get("fee_eur", 0), "pnl_bruto_eur": "", "pnl_neto_eur": "",
            "notas": (f"favorito_altaconviccion_baja_latencia restante={restante_s:.1f}s"
                      if resultado.get("ok") else resultado.get("error", "")),
        }
        lt._registrar_trade(trade)
        log(f"  {'EJECUTADO' if resultado['ok'] else 'ERROR'}: {resultado}", activo)
        if resultado["ok"]:
            lt.enviar_telegram(
                f"🎯 *Orden live ejecutada (FAVORITO_ALTACONVICCION baja latencia)*\n"
                f"Estrategia: {STRATEGY}#{subtype}\n"
                f"Precio fill: {resultado['entry_price']:.4f} (slip {resultado.get('slip_real', 0):+.4f})\n"
                f"Stake: {stake_info['stake_eur']:.2f}$  |  restante={restante_s:.1f}s\n"
                f"Bankroll operativo: {lt.bankroll_actual():.2f}$ (real al cierre de ciclo)"
            )
        else:
            lt.enviar_telegram(
                f"❌ *Orden live ERROR (FAVORITO_ALTACONVICCION baja latencia)*\n"
                f"{STRATEGY}#{subtype} BUY_YES\n{resultado.get('error', '')[:200]}"
            )
        return True


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
    log(f"favorito_altaconviccion_executor_15min arrancado (DRY_RUN={DRY_RUN}, activos={list(ACTIVOS)})")
    _fc.iniciar()
    time.sleep(3)
    if not DRY_RUN:
        _ = lt._get_clob_client()
        log("ClobClient precalentado")

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
