#!/usr/bin/env python3
"""
ballenas_executor_btc15m.py — Ejecutor de baja latencia para
BALLENAS_TARDIAS#BTC#15min#BUY_YES.

Origen (16-Jul, decisión Javi): BTC#15min quedó fuera de veto_ballenas
porque la ventana en la que el flujo de ballenas confirma el resultado es
[0.07,0.53]min = 4-32s antes del cierre — más estrecha que el ciclo fast
(~20-23s). analisis_ballenas_dosis_respuesta_16jul.py (n=366) y
analisis_ballenas_btc15m_fillability_retro_16jul.py (36/36 mercados con
profundidad real, commit ba531d7e98) confirmaron que el edge y la
profundidad SÍ existen ahí — el único obstáculo es la latencia de
nuestro propio pipeline. Ver plan completo en
/root/.claude/plans/rosy-cooking-mist.md.

Estrategia SEPARADA de GBM_LATE_15M_ESPACIO_ATR/UPDOWN_GBM_15M_TARDIO (que
ya operan BTC#15min#BUY_YES entre ~3-12min antes del cierre y cuya propia
ventana de reintento expira minutos antes de que empiece esta): la señal
aquí nace directamente de la confirmación de ballenas en tiempo real, no
del GBM. Solo BUY_YES en v1 (mismo lado que las tuplas BTC#15min ya
aprobadas -- introducir BUY_NO repetiría el patrón de selección adversa ya
visto en FAVORITO_CONFIRMADO#*#15min#BUY_NO sin haberlo comprobado para
este mecanismo).

DRY_RUN=True por defecto: loguea qué habría hecho, nunca llama a
_ejecutar_orden_polymarket. Cambiar a False solo tras /code-review y
aprobación explícita de Javi (código que toca dinero real).

27-Jul: gate real de volumen (UMBRAL_N_YES_TOTAL=35, n_yes_total =
compras YES en TODO el mercado sin filtrar por banda) — ver
project_volumen_ballenas_patron_universal_27jul en memoria. Validado con
las 173 señales reales de esta tupla: n_yes_total>=35 → n=115 hit=95.7%
PnL/trade=+0.838€ GATE OK; <35 → n=58 hit=1.7% PnL/trade=-1.19€. Mismo
mecanismo que BALLENAS_TARDIAS#ETH#5min (ballenas_executor_5min.py).
Coste de red cero: reutiliza la misma llamada a trades_de_mercado() que
concentracion_ballenas() ya hacía.

Corre en screen propia:
  screen -dmS ballenas_fast bash -c "cd /root/polymarket-research && .venv/bin/python ballenas_executor_btc15m.py >> logs/ballenas_fast.log 2>&1"
"""
import csv
import fcntl
import json
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import requests

import live_trade as lt
from live_guard import puede_operar_live
from live_stake import bloquear_por_circuit_breaker, calcular_stake
from smart_money_tracker import MAX_TRADES_POR_MERCADO, trades_de_mercado
from ballenas_banda_fina_gate import evaluar as _gate_banda_fina_ballenas

DIR = Path(__file__).resolve().parent
DIR_SHADOW = DIR / "data" / "shadow"
LOG_PATH = DIR / "logs" / "ballenas_fast.log"
STRATEGY_PARAMS_PATH = DIR_SHADOW / "strategy_params.json"

# 23-Jul: mismo fix de calibración dinámica + consenso ponderado por wallet
# ya aplicado a ballenas_executor_5min.py (ver su docstring/comentarios para
# el hallazgo completo -- XRP#5min llevaba desde el 18-Jul con un
# prob_bucket hardcodeado que quedó 22pp desalineado tras un recalibrado
# silencioso del observer). Este executor SÍ opera dinero real
# (DRY_RUN=False) así que el mismo riesgo de fondo (un número congelado en
# vez de releído fresco de ballenas_timing_state.json) es más grave aquí,
# no menos -- de ahí extenderlo. A diferencia de 5min, esto NO se ha
# re-verificado con un cruce de franja milimétrica específico para BTC#15m
# (esa verificación solo se hizo para ETH/SOL/XRP#5min) -- el principio
# generaliza (no hardcodear lo que el observer recalibra) pero el hallazgo
# concreto de desalineación de timing/prob_bucket para BTC#15m en concreto
# no está medido de forma independiente. Vigilar tras desplegar.
WALLET_EDGE_POR_ACTIVO_MARCO = DIR_SHADOW / "wallet_edge_score_por_activo_marco.json"
PESO_MIN, PESO_MAX = 0.2, 3.0
_wallet_edge_cache = {"mtime": None, "data": {}}


def _cargar_wallet_edge_activo_marco():
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
    return _wallet_edge_cache["data"]


def _peso_wallet(wallet: str) -> float:
    """1.0 (neutro) salvo wallet validada (n>=15, sig_bhfdr=True) en
    (BTC,15m) exacto -- mismo criterio que ballenas_executor_5min._peso_wallet."""
    db = _cargar_wallet_edge_activo_marco()
    d = db.get((wallet, ASSET, "15m"))
    if d is None or not d.get("sig_bhfdr"):
        return 1.0
    peso = 1.0 + d["edge_pp"] / 25.0
    return max(PESO_MIN, min(PESO_MAX, peso))


def _wilson_lower(aciertos: int, n: int, z: float = 1.96) -> float:
    """Límite inferior del IC de Wilson al 95% -- mismo cálculo que
    ballenas_executor_5min._wilson_lower."""
    if n <= 0:
        return 0.0
    phat = aciertos / n
    denom = 1 + z * z / n
    centro = phat + z * z / (2 * n)
    ajuste = z * ((phat * (1 - phat) / n + z * z / (4 * n * n)) ** 0.5)
    return (centro - ajuste) / denom
# Mismo motivo que TRADES_LOCK_PATH en live_trade.py (16-Jul, este mismo
# executor): predictions_YYYY-MM-DD.csv ahora tiene DOS escritores
# concurrentes (el ciclo normal de shadow_predict.py + este proceso
# persistente) -- sin lock, dos escrituras podrían entrelazarse a nivel de
# fichero. flock() barato, nunca contended en la práctica.
PREDICTIONS_LOCK_PATH = DIR_SHADOW / ".predictions_lock"

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"

STRATEGY = "BALLENAS_TARDIAS"
ASSET = "BTC"
VENTANA_MIN = 15
COMBO = "BTC#15m"

DRY_RUN = False  # Fase 2 (17-Jul, activada: aprobación explícita Javi + /code-review +
                  # gate formal de dosis-respuesta corrido para BTC#15m específicamente,
                  # ver _pares_ballenas_tardias_btc15m_promocion_nota_2026-07-17 en config_live.json

POLL_INTERVAL_S = 1.0    # cadencia del bucle rápido
HARD_FLOOR_S = 3.0       # por debajo de esto, se abandona -- fail-closed por timing
CONCENTRACION_MIN = 0.9  # bucket con 98.5% acierto + profundidad confirmada 16-Jul
MIN_TRADES_BALLENA = 3

# 27-Jul: gate de volumen (n_yes_total, compras YES en TODO el mercado sin
# filtrar por banda) -- ver project_volumen_ballenas_patron_universal_27jul
# en memoria. Validado con las 173 señales reales de esta tupla:
# n_yes_total>=35 -> n=115 hit=95.7% PnL/trade=+0.838€ GATE OK; <35 -> n=58
# hit=1.7% PnL/trade=-1.19€. Mismo umbral que BALLENAS_TARDIAS#ETH#5min.
UMBRAL_N_YES_TOTAL = 35

# 23-Jul: MARGEN_WATCH_S/MARGEN_CONFIRM_S sustituyen a WATCH_LEAD_S/PROB_BUCKET
# fijos -- mismo patrón que ballenas_executor_5min.py (ver comentario junto a
# WALLET_EDGE_POR_ACTIVO_MARCO arriba). cargar_calibracion() ahora deriva todo
# fresco de ballenas_timing_state.json en cada ventana: prob_bucket (Wilson
# 95% inferior de n/n_ganadoras de la banda operativa ACTUAL, no el 0.985
# congelado del 16-Jul) y confirm_ceiling_s (techo real de confirmación
# rest_hi_min, no un WATCH_LEAD_S=90s fijo que podía disparar en cuanto se
# cumplía concentración aunque aún faltara tiempo para la ventana real de
# 4-32s). watch_window ya no dispara hasta estar dentro de confirm_ceiling_s.
MARGEN_WATCH_S = 60
MARGEN_CONFIRM_S = 15

# 28-Jul: "adelantar la escucha" -- diagnóstico completo en memoria
# idea_desajuste_banda_precio_vs_consenso_ballenas_btc15m_28jul: en 11 días
# de dinero real esta tupla nunca ejecutó un trade (n=0) porque el consenso
# de ballenas casi siempre se forma MUCHO antes de confirm_ceiling_s (~40s
# antes del cierre) -- para cuando restante cae dentro de esa ventana, el
# propio volumen que generó el consenso ya movió el precio fuera de banda.
# Reconstruido el histórico completo (47 mercados, trades reales vía la
# API ya corregida del bug de truncación del mismo día): 37/47 mercados
# tuvieron algún instante con concentración>=0.9+n>=3+precio en banda, pero
# solo 2/37 cayeron dentro de la ventana tardía actual. El otro grupo
# (restante>=150s, n=35) da hit=91.4% (Wilson90% lo=0.804) y PnL/trade
# bootstrap CI90%=[+0.118,+0.328] -- tan bueno como el tardío, sin cruzar
# cero. FASE 0 (esta constante): solo observacional -- amplía cuánto
# ANTES empieza a vigilar el bucle (más polls, más log), pero NO toca el
# disparo real todavía (sigue exigiendo restante<=confirm_ceiling_s, ver
# watch_window). El disparo temprano de verdad es un cambio aparte,
# pendiente de n>=40 fresco acumulado con esta observación + /code-review
# + aprobación explícita antes de tocar el trigger real.
WATCH_LEAD_TEMPRANO_S = VENTANA_MIN * 60 - 30  # casi toda la ventana, deja 30s de margen tras la apertura

# requests.Session persistente (keep-alive) -- evita repetir handshake
# TCP/TLS en cada llamada del bucle rápido, ver presupuesto de latencia
# en el plan.
_session = requests.Session()


def log(msg: str):
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    line = f"[{ts}] {msg}"
    print(line, flush=True)


def resolver_mercado(ts_start: int) -> dict | None:
    """Una sola llamada gamma-api por ventana de 15min -- mismo patrón
    determinista que photo_finish_logger.mercado_slot() y
    shadow_predict.fetch_slots_directos() (slug computado, sin escanear
    mercados)."""
    slug = f"{ASSET.lower()}-updown-{VENTANA_MIN}m-{ts_start}"
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
        # índice 0 = Up/YES, 1 = Down/NO -- misma convención que
        # photo_finish_logger.py / shadow_predict.py.
        return {
            "market_id": mkt.get("id", ""),
            "condition_id": mkt.get("conditionId", ""),
            "yes_token": tokens[0],
            "no_token": tokens[1],
            "end_date": mkt.get("endDate", ""),
        }
    except Exception as e:
        log(f"  resolver_mercado error: {e}")
        return None


def libro_publico(token_id: str) -> dict | None:
    """Lectura pública del libro (sin auth) -- mismo endpoint que
    live_trade._fetch_book_publico, reimplementado aquí para usar la
    Session persistente en vez de requests.get() suelto."""
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


def concentracion_ballenas(condition_id: str, banda_lo: float, banda_hi: float) -> tuple[float | None, float | None, int, str, list, int, int]:
    """(pct_yes_crudo, pct_yes_ponderado, n, motivo, wallets_yes,
    n_yes_total, n_trades_crudo) del flujo BUY de ballenas en
    `condition_id`, dentro de la banda de precio, que compró YES -- mide
    AMBOS lados (a diferencia de live_trade._ballenas_conviccion_mercado,
    que solo mide el lado que ya decidimos nosotros) porque aquí la
    dirección todavía no está fijada: la decide el lado mayoritario de
    las ballenas.

    23-Jul: pct_yes_ponderado pesa cada trade según _peso_wallet() -- mismo
    fix que ballenas_executor_5min.py (ver comentario junto a
    WALLET_EDGE_POR_ACTIVO_MARCO). n sigue siendo el conteo CRUDO (el gate
    MIN_TRADES_BALLENA no cambia). pct_yes_crudo se conserva para auditar
    en el log cuándo diverge del ponderado.

    27-Jul: n_yes_total -- compras YES en TODO el mercado, sin filtrar por
    banda (ver UMBRAL_N_YES_TOTAL). n_trades_crudo=len(trades), respuesta
    cruda ANTES de filtrar -- lo que realmente toca el cap
    MAX_TRADES_POR_MERCADO=100 (mismo fix que ballenas_executor_5min.py
    27-Jul, /code-review: comparar n_yes_total contra el cap sería código
    muerto, un subconjunto casi nunca alcanza el tamaño del conjunto
    completo).

    `motivo` distingue 'error_api' (trades_de_mercado lanzó excepción) de
    'sin_trades_en_banda' (la API respondió bien pero 0 trades BUY caen en
    la banda ahora mismo) -- antes ambos devolvían (None,0) indistinguibles.
    17-Jul: un hueco de log de 87s sin una sola línea obligó a reconstruir
    a mano si era un fallo silencioso o solo ausencia de actividad (resultó
    ser lo segundo, el mercado ya cotizaba en extremos a T-90s) -- no debe
    hacer falta esa arqueología cada vez."""
    try:
        trades = trades_de_mercado(condition_id)
    except Exception:
        return None, None, 0, "error_api", [], 0, 0
    n_trades_crudo = len(trades)
    n_yes = n_no = 0
    n_yes_total = 0
    peso_yes = peso_no = 0.0
    wallets_yes = []
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
        if outcome_t in ("up", "yes"):
            n_yes_total += 1
        if not (banda_lo <= precio_t < banda_hi):
            continue
        w = (t.get("proxyWallet") or "").lower()
        peso = _peso_wallet(w) if w else 1.0
        if outcome_t in ("up", "yes"):
            n_yes += 1
            peso_yes += peso
            if w:
                wallets_yes.append(w)
        else:
            n_no += 1
            peso_no += peso
    n = n_yes + n_no
    if n == 0:
        return None, None, 0, "sin_trades_en_banda", [], n_yes_total, n_trades_crudo
    pct_crudo = n_yes / n
    pct_ponderado = peso_yes / (peso_yes + peso_no) if (peso_yes + peso_no) > 0 else pct_crudo
    return pct_crudo, pct_ponderado, n, "ok", wallets_yes, n_yes_total, n_trades_crudo


def _resumen_wallet_edge(wallets: list) -> str:
    """Texto corto para el log -- mismo formato que
    ballenas_executor_5min._resumen_wallet_edge."""
    db = _cargar_wallet_edge_activo_marco()
    filas = [db[(w, ASSET, "15m")] for w in wallets if (w, ASSET, "15m") in db]
    edges = [f["edge_pp"] for f in filas]
    n_sig_neg = sum(1 for f in filas if f["sig_bhfdr"] and f["edge_pp"] < 0)
    n_sig_pos = sum(1 for f in filas if f["sig_bhfdr"] and f["edge_pp"] > 0)
    if not edges:
        return "wallet_edge=sin_dato"
    medio = sum(edges) / len(edges)
    return f"wallet_edge_medio={medio:+.2f}pp(n_con_score={len(edges)},n_sig_pos={n_sig_pos},n_sig_neg={n_sig_neg})"


def cargar_calibracion() -> dict | None:
    """Sustituye a cargar_banda_btc15m() -- TODO releído fresco cada
    ventana desde ballenas_timing_state.json: banda_lo/hi (como antes),
    más prob_bucket (Wilson 95% inferior de n/n_ganadoras de la banda
    operativa ACTUAL, ya no PROB_BUCKET=0.985 congelado del 16-Jul) y
    confirm_ceiling_s (derivado de rest_hi_min real + margen, ya no
    WATCH_LEAD_S=90s fijo). Fail-closed (None) si el combo no es
    significativo o falta cualquier dato -- mismo criterio que
    ballenas_executor_5min.cargar_calibracion."""
    try:
        estado = json.loads((DIR_SHADOW / "ballenas_timing_state.json").read_text())
    except Exception:
        return None
    e = estado.get(COMBO, {})
    if not e.get("significativo"):
        return None
    lo, hi = e.get("banda_lo"), e.get("banda_hi")
    n, n_gan, rest_hi = e.get("n"), e.get("n_ganadoras"), e.get("rest_hi_min")
    if not (isinstance(lo, (int, float)) and isinstance(hi, (int, float))
            and isinstance(n, (int, float)) and n > 0
            and isinstance(n_gan, (int, float)) and 0 <= n_gan <= n
            and isinstance(rest_hi, (int, float))):
        return None
    prob_bucket = _wilson_lower(int(n_gan), int(n))
    confirm_ceiling_s = rest_hi * 60 + MARGEN_CONFIRM_S
    # 28-Jul: watch_lead_s se amplía a WATCH_LEAD_TEMPRANO_S (ver constante,
    # "adelantar la escucha") -- el disparo real SIGUE exigiendo
    # restante<=confirm_ceiling_s (sin cambios abajo en watch_window), esto
    # solo hace que el bucle empiece a vigilar/loguear mucho antes para
    # poder registrar observacionalmente la confirmación temprana.
    watch_lead_s = max(confirm_ceiling_s + MARGEN_WATCH_S, WATCH_LEAD_TEMPRANO_S)
    return {"banda_lo": lo, "banda_hi": hi, "prob_bucket": prob_bucket,
            "confirm_ceiling_s": confirm_ceiling_s, "watch_lead_s": watch_lead_s,
            "n_banda": int(n)}


def _activa_permite_disparo() -> tuple[bool, str]:
    """20-Jul (Javi: "por qué no haces que aprenda como el resto del
    sistema"): este executor no pasa por shadow_predict.py, así que no
    hereda gratis el gate `activa` que frena a cualquier otra estrategia
    cuando su IC real cae. Replica el mismo lookup en cascada que usa
    shadow_predict.py (más específico -> más general) sobre el MISMO
    strategy_params.json que alimenta shadow_postmortem.py -- en cuanto
    _registrar_prediccion() acumule resoluciones reales, el postmortem
    calculará un ic_bayes propio para BALLENAS_TARDIAS y podrá desactivarlo
    solo, igual que cualquier otra estrategia. Fail-open si no hay entrada
    todavía (n insuficiente) -- mismo criterio que el resto del sistema:
    bloquea por evidencia negativa explícita, no por falta de dato."""
    subtype = f"{ASSET}#{VENTANA_MIN}min"
    lookup_keys = [f"{STRATEGY}#{subtype}", f"{STRATEGY}#{ASSET}", f"{STRATEGY}#{VENTANA_MIN}min"]
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


ADELANTADO_DRY_CSV = DIR_SHADOW / "ballenas_btc15m_adelantado_dry.csv"
ADELANTADO_DRY_COLS = ["timestamp_utc", "market_id", "condition_id", "end_date",
                        "restante_s", "py", "concentracion_ponderada", "n_ballenas",
                        "n_yes_total", "profundidad_eur", "ratio_vs_stake", "n_niveles_libro",
                        "outcome_real", "acierto"]
STAKE_REF_EUR = 1.05  # mismo suelo/techo pineado que live_stake.py hoy -- referencia realista


def _registrar_confirmacion_temprana_dry(mercado: dict, py: float, restante_s: float,
                                          pct_ponderado: float, n_ballenas: int,
                                          n_yes_total: int) -> None:
    """28-Jul, "adelantar la escucha" (FASE 0, solo observación -- ver
    WATCH_LEAD_TEMPRANO_S y memoria idea_desajuste_banda_precio_vs_
    consenso_ballenas_btc15m_28jul): registra la 1ª vez por ventana que se
    habría cumplido la condición de disparo si no exigiéramos esperar a
    confirm_ceiling_s -- incluye profundidad REAL del libro en ese instante
    (nunca medida antes tan pronto en la ventana) para poder evaluar
    fill-ability antes de tocar el trigger real. NO llama a disparar() ni
    a ninguna función de live_trade que coloque órdenes -- solo lee el
    libro público (mismo _consultar_profundidad_libro ya auditado que usa
    live_trade.py, client=None -> endpoint público, sin credenciales)."""
    try:
        prof = lt._consultar_profundidad_libro(None, mercado["yes_token"], py, STAKE_REF_EUR)
    except Exception as e:
        prof = {"ok": False, "error": str(e)}
    fila = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "market_id": mercado.get("market_id", ""),
        "condition_id": mercado.get("condition_id", ""),
        "end_date": mercado.get("end_date", ""),
        "restante_s": round(restante_s, 1),
        "py": py,
        "concentracion_ponderada": pct_ponderado,
        "n_ballenas": n_ballenas,
        "n_yes_total": n_yes_total,
        "profundidad_eur": prof.get("profundidad_eur", "") if prof.get("ok") else "",
        "ratio_vs_stake": prof.get("ratio_vs_stake", "") if prof.get("ok") else "",
        "n_niveles_libro": prof.get("n_niveles", "") if prof.get("ok") else "",
        "outcome_real": "", "acierto": "",
    }
    nuevo = not ADELANTADO_DRY_CSV.exists()
    with open(ADELANTADO_DRY_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=ADELANTADO_DRY_COLS)
        if nuevo:
            w.writeheader()
        w.writerow(fila)
    log(f"[{mercado.get('market_id')}] 🔬 adelantado-dry registrado: restante={restante_s:.1f}s "
        f"py={py:.3f} ratio_vs_stake={fila['ratio_vs_stake']}")


def _registrar_prediccion(mercado: dict, py: float, edge: float, restante_s: float,
                           pct_yes: float, n_ballenas: int, banda_lo: float, banda_hi: float,
                           prob_bucket: float):
    """Deja rastro en predictions_YYYY-MM-DD.csv con el MISMO formato que
    escribe shadow_predict.py -- así shadow_resolve.py lo resuelve y
    shadow_postmortem.py aprende de él exactamente igual que de cualquier
    otra estrategia, sin duplicar esa lógica aquí. Se registra SIEMPRE que
    se confirma la señal, se ejecute luego de verdad o no (switch OFF,
    whitelist, breaker...) -- igual que libro_snapshots acumula 24/7, el
    aprendizaje no debe depender de si hubo bankroll para actuar."""
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    archivo = DIR_SHADOW / f"predictions_{ts[:10]}.csv"
    subtype = f"{ASSET}#{VENTANA_MIN}min"
    gate_bf = _gate_banda_fina_ballenas(ASSET, f"{VENTANA_MIN}min", py, restante_s / 60.0)
    features = json.dumps({
        "concentracion_yes": round(pct_yes, 4), "n_ballenas": n_ballenas,
        "restante_s_al_confirmar": round(restante_s, 2),
        "banda_lo": banda_lo, "banda_hi": banda_hi,
        "banda_fina_vetaria_fase1": gate_bf["vetaria_fase1"], "banda_fina_motivo": gate_bf["motivo"],
    }, separators=(",", ":"))
    try:
        with open(PREDICTIONS_LOCK_PATH, "w") as lock_f:
            fcntl.flock(lock_f, fcntl.LOCK_EX)
            try:
                nuevo = not archivo.exists()  # re-comprobar bajo el lock
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
                        f"{restante_s / 3600:.4f}", f"{py:.4f}", f"{prob_bucket:.4f}",
                        f"{edge:.4f}", f"{edge:.4f}", f"{edge:.4f}", "BUY_YES",
                        "ballenas_confirmado", subtype, "1.05", features,
                    ])
            finally:
                fcntl.flock(lock_f, fcntl.LOCK_UN)
    except Exception as e:
        log(f"  aviso: no se pudo registrar predicción para postmortem: {e}")


def watch_window(ts_end: int) -> bool:
    """Vigila un mercado BTC#15min concreto desde watch_lead_s hasta el
    cierre. True si ejecutó (o habría ejecutado en DRY_RUN).

    23-Jul: calibración (banda, prob_bucket, watch_lead_s, confirm_ceiling_s)
    releída fresca vía cargar_calibracion() -- ya no hay WATCH_LEAD_S/
    PROB_BUCKET fijos. No confirma en cuanto se cumple concentración: solo
    dentro de confirm_ceiling_s (ver cargar_calibracion), y usa la
    concentración PONDERADA por calidad de wallet, no la cruda -- mismo
    patrón que ballenas_executor_5min.watch_window."""
    ts_start = ts_end - VENTANA_MIN * 60
    calib = cargar_calibracion()
    if calib is None:
        log(f"[{ts_end}] BTC#15m no significativo o calibración incompleta en ballenas_timing_state.json -- se salta la ventana")
        return False
    banda_lo, banda_hi = calib["banda_lo"], calib["banda_hi"]
    watch_lead_s, confirm_ceiling_s = calib["watch_lead_s"], calib["confirm_ceiling_s"]
    prob_bucket = calib["prob_bucket"]

    mercado = None
    contadores = {"ok": 0, "sin_trades_en_banda": 0, "error_api": 0}
    contador_prematuro = 0  # cumple condición pero aún fuera de confirm_ceiling_s -- solo para el log final
    registrado_temprano = False  # 28-Jul "adelantar la escucha": solo la 1ª vez por ventana
    while True:
        restante = ts_end - time.time()
        if restante > watch_lead_s:
            time.sleep(min(restante - watch_lead_s, 5))
            continue
        if restante < HARD_FLOOR_S:
            log(f"[{ts_end}] suelo de seguridad ({HARD_FLOOR_S}s) alcanzado sin confirmación -- se abandona "
                f"(resumen vigilancia: {sum(contadores.values())} polls, "
                f"ok={contadores['ok']} sin_trades_en_banda={contadores['sin_trades_en_banda']} "
                f"error_api={contadores['error_api']} prematuros={contador_prematuro})")
            return False

        if mercado is None:
            mercado = resolver_mercado(ts_start)
            if mercado is None:
                log(f"[{ts_end}] no se pudo resolver el mercado -- se abandona")
                return False
            # Defensa en profundidad (ver plan, sección idempotencia): en la
            # práctica la ventana de reintento de la señal GBM normal para
            # este mismo market_id ya expiró minutos antes de llegar aquí
            # (SENAL_MAX_LATENCIA_SEG=100s desde una señal creada a >=3min
            # del cierre), así que el solape real es ~imposible -- este
            # check es barato y cierra el caso igualmente.
            if mercado["market_id"] in lt._ya_operados_hoy():
                log(f"[{ts_end}] {mercado['market_id']} ya operado -- se salta")
                return False

        with ThreadPoolExecutor(max_workers=2) as ex:
            f_conc = ex.submit(concentracion_ballenas, mercado["condition_id"], banda_lo, banda_hi)
            f_libro = ex.submit(libro_publico, mercado["yes_token"])
            pct_crudo, pct_ponderado, n, motivo_conc, wallets_yes, n_yes_total, n_trades_crudo = f_conc.result()
            libro = f_libro.result()

        if n_trades_crudo >= MAX_TRADES_POR_MERCADO:
            log(f"[{ts_end}] ⚠️ respuesta de trades_de_mercado con {n_trades_crudo} filas "
                f"toca el cap de la API ({MAX_TRADES_POR_MERCADO}) -- posible truncación "
                f"(n_yes_total={n_yes_total} puede estar incompleto)")

        contadores[motivo_conc] = contadores.get(motivo_conc, 0) + 1
        if pct_ponderado is not None:
            log(f"[{ts_end}] restante={restante:.1f}s concentracion_yes_cruda={pct_crudo:.2f} "
                f"ponderada={pct_ponderado:.2f} n={n} n_yes_total={n_yes_total} "
                f"ask={libro.get('best_ask') if libro else None}")
        elif motivo_conc == "error_api":
            # A diferencia de sin_trades_en_banda (silencioso, esperable y
            # frecuente), un fallo de API sí se loguea cada vez que ocurre
            # -- es la señal que antes quedaba escondida dentro de un hueco
            # de log indistinguible de "no hay actividad".
            log(f"[{ts_end}] restante={restante:.1f}s ⚠️ error_api consultando ballenas -- sin dato este ciclo")

        if (pct_ponderado is not None and n >= MIN_TRADES_BALLENA
                and pct_ponderado >= CONCENTRACION_MIN and n_yes_total < UMBRAL_N_YES_TOTAL):
            log(f"[{ts_end}] concentración OK pero n_yes_total={n_yes_total}<{UMBRAL_N_YES_TOTAL} -- "
                f"vetado por volumen bajo (gate 27-Jul)")

        cumple_concentracion = (pct_ponderado is not None and n >= MIN_TRADES_BALLENA
                                 and n_yes_total >= UMBRAL_N_YES_TOTAL
                                 and pct_ponderado >= CONCENTRACION_MIN
                                 and libro and libro.get("best_ask") is not None
                                 and banda_lo <= libro["best_ask"] < banda_hi)
        if cumple_concentracion and restante > confirm_ceiling_s:
            # 23-Jul: cumple la condición pero todavía fuera de la ventana
            # real de confirmación (rest_hi_min de la banda operativa) --
            # se sigue vigilando en vez de disparar ya.
            contador_prematuro += 1
            if not registrado_temprano:
                registrado_temprano = True
                _registrar_confirmacion_temprana_dry(mercado, libro["best_ask"], restante,
                                                       pct_ponderado, n, n_yes_total)
            time.sleep(POLL_INTERVAL_S)
            continue

        if cumple_concentracion:
            py = libro["best_ask"]
            edge = prob_bucket - py
            log(f"[{ts_end}] CONFIRMADO concentracion_ponderada={pct_ponderado:.2f} (cruda={pct_crudo:.2f}) "
                f"n={n} py={py:.3f} prob_bucket={prob_bucket:.3f} edge={edge:+.3f} restante={restante:.1f}s "
                f"confirm_ceiling_s={confirm_ceiling_s:.1f} {_resumen_wallet_edge(wallets_yes)}")
            _registrar_prediccion(mercado, py, edge, restante, pct_ponderado, n, banda_lo, banda_hi, prob_bucket)
            return disparar(mercado, py, edge, restante, prob_bucket)

        time.sleep(POLL_INTERVAL_S)


def disparar(mercado: dict, py: float, edge: float, restante_s: float, prob_bucket: float) -> bool:
    """Decide y (si no es DRY_RUN) ejecuta. Reutiliza circuit breaker +
    stake de live_stake.py y _ejecutar_orden_polymarket de live_trade.py
    -- comparten trades.csv/config_live.json, así que el freno diario y
    los circuit breakers son el MISMO presupuesto de riesgo que el resto
    del sistema, no un silo aparte."""
    subtype = f"{ASSET}#{VENTANA_MIN}min"

    # Este executor es un proceso PERSISTENTE aparte de live_trade.py y nunca
    # pasa por su pipeline principal (llama _ejecutar_orden_polymarket
    # directo) -- así que ninguno de los guardias que viven ahí se aplica
    # solo, hay que repetirlos aquí explícitamente. Hallazgo del /code-review
    # 17-Jul (angle "reuse"): la primera versión llamaba switch_activo() +
    # en_ventana_horaria() por separado, reinventando 2/3 de
    # puede_operar_live() y dejando fuera la 3ª pieza -- la whitelist
    # (pares_permitidos_live). BALLENAS_TARDIAS#BTC#15min#BUY_YES no estaba
    # en la lista y este executor no tenía NINGÚN mecanismo para
    # comprobarla; corregido usando la función real combinada, no una
    # reimplementación parcial. Fail-closed: bloquea si falta cualquiera de
    # las tres piezas.
    # 20-Jul (Javi: "que aprenda como el resto del sistema"): antes de
    # cualquier otro guardia, respeta el veredicto del postmortem sobre SU
    # PROPIO ic_bayes real -- una vez tenga n>=15 resoluciones (vía
    # _registrar_prediccion), si el edge no se sostiene esto lo apaga solo,
    # igual que cualquier otra estrategia vía shadow_predict.py.
    ok_activa, motivo_activa = _activa_permite_disparo()
    if not ok_activa:
        log(f"  {motivo_activa} -- {'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}")
        return False

    ok_operar, motivo_operar = puede_operar_live(STRATEGY, subtype)
    if not ok_operar:
        log(f"  {motivo_operar} -- {'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}")
        return False

    config = lt._cargar_config()
    max_misma_dir = config.get("riesgo", {}).get("max_posiciones_abiertas_misma_direccion", 2)
    abiertas_dir = lt._posiciones_abiertas_misma_direccion("BUY_YES")
    if abiertas_dir >= max_misma_dir:
        log(f"  techo de correlación: {abiertas_dir} posiciones BUY_YES abiertas ≥ {max_misma_dir} -- "
            f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}")
        return False

    # Rechequeo de idempotencia (/code-review 17-Jul): watch_window solo
    # comprueba _ya_operados_hoy() UNA vez al resolver el mercado, hasta
    # watch_lead_s antes del cierre -- el fast loop (proceso independiente,
    # whitelist propia) puede operar ese mismo market_id en el hueco que
    # pasa hasta que se dispara esta función. Repetir el check aquí, lo más
    # tarde posible antes de la orden real, no lo elimina del todo (sigue
    # sin lock cruzado entre procesos) pero cierra la mayor parte de la
    # ventana.
    if mercado["market_id"] in lt._ya_operados_hoy():
        log(f"  {mercado['market_id']} ya operado por otro proceso en la última ventana -- "
            f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}")
        return False

    # 27-Jul (/code-review): usa el helper único bloquear_por_circuit_breaker
    # en vez de reimplementar el chequeo aquí -- este mismo chequeo,
    # reimplementado por separado en este fichero y en
    # ballenas_executor_5min.py, se invirtió de forma IDÉNTICA en ambos
    # (bug crítico corregido el mismo día: esta tupla estuvo 10 días en
    # live con cero trades reales). Centralizado en live_stake.py para
    # que no pueda repetirse.
    if bloquear_por_circuit_breaker(
            lambda motivo: log(f"  circuit breaker activo ({motivo}) -- "
                                f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}")):
        return False

    # ic_conviccion: /code-review 17-Jul encontró que se pasaba `edge` crudo
    # (PROB_BUCKET - py, ~0.02-0.08) donde calcular_stake espera un IC
    # histórico validado (ic_bayes, lo que usa cualquier otra tupla live).
    # Sin efecto en euros HOY (min_stake_eur=max_stake_eur=1.05€ pineado,
    # clamp lo absorbe) pero quedaría mal calibrado en cuanto se despinee.
    # 23-Jul: prob_bucket ya no es el PROB_BUCKET=0.985 fijo del backtest de
    # dosis-respuesta (n=273, analisis_ballenas_dosis_respuesta_16jul.py) --
    # llega como parámetro, calculado fresco en cargar_calibracion() para
    # esta ventana concreta (Wilson 95% inferior de la banda operativa
    # actual). El análogo real a un ic_bayes sigue siendo su distancia a un
    # lanzamiento justo.
    # 29-Jul: reemplaza (prob_bucket-0.5)*2 -- esa fórmula asume que el
    # precio de referencia es ~0.5, y se rompe en bandas baratas (DOGE/BNB
    # ~0.20): daba magnitudes de conviccion enormes (~0.55-0.58) para un
    # edge real de solo 5-9pp, saturando el stake al techo absoluto sin
    # relacion con el edge verdadero. Kelly-exacto real para binarias,
    # f*=(p-pi)/(1-pi) (misma formula ya validada hoy en
    # analisis_kelly_precio_gate_29jul.py/kelly_precio_gate.py): usa el
    # PRECIO REAL pagado (py, el ask del libro en el momento de confirmar),
    # no un 0.5 generico. Verificado antes de desplegar (ver memoria
    # project_ballenas_executor_15min_construido_29jul): para BTC#15min y
    # ETH#5min (las 2 tuplas con dinero real de esta familia) el stake
    # FINAL no cambia -- ambas formulas superan el techo absoluto de 2€,
    # asi que el cambio es inerte para dinero real hoy. Para DOGE/BNB pasa
    # de una magnitud inflada (satura el techo) a una realista y pequeña
    # (cerca del suelo), acorde a su edge real.
    ic_conviccion = max(0.0, (prob_bucket - py) / (1 - py)) if py < 1 else 0.0
    stake_info = calcular_stake(ic_conviccion, STRATEGY, subtype, direction="BUY_YES")
    if not stake_info.get("viable"):
        log(f"  stake no viable: {stake_info.get('motivo')} -- {'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}")
        return False

    if DRY_RUN:
        log(f"  [DRY-RUN] habría ejecutado BUY_YES {mercado['market_id']} py={py:.3f} "
            f"edge={edge:+.3f} stake={stake_info['stake_eur']:.2f}€ restante={restante_s:.1f}s")
        return True

    resultado = lt._ejecutar_orden_polymarket(
        mercado["market_id"], "BUY_YES", stake_info["stake_eur"], py,
        edge_dir=edge, contexto={"strategy": STRATEGY, "subtype": subtype})

    if resultado.get("no_fill"):
        log(f"  no_fill: {resultado.get('error')}")
        return False

    trade = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "market_id": mercado["market_id"],
        "question": "",
        "end_date": mercado.get("end_date", ""),
        "strategy": STRATEGY, "subtype": subtype, "direction": "BUY_YES",
        "stake_eur": stake_info["stake_eur"] if resultado["ok"] else 0.0,
        "entry_price": resultado["entry_price"],
        "signal_ask": round(py, 4),
        "slip_real": resultado.get("slip_real", ""),
        "ic_modelo": round(prob_bucket, 4),
        "edge_neto": round(edge, 4),
        "conviction_score": round(prob_bucket, 4),
        "kelly_recomendado": stake_info["stake_eur"],
        "status": "OPEN" if resultado["ok"] else "ERROR",
        "close_timestamp": "", "exit_price": "", "outcome_real": "",
        "fee_eur": resultado.get("fee_eur", 0),
        "pnl_bruto_eur": "", "pnl_neto_eur": "",
        "notas": (f"ballenas_tardias restante={restante_s:.1f}s"
                  if resultado.get("ok") else resultado.get("error", "")),
    }
    lt._registrar_trade(trade)
    log(f"  {'EJECUTADO' if resultado['ok'] else 'ERROR'}: {resultado}")
    # 28-Jul: mismo fix que ballenas_executor_5min.py -- este executor
    # reusaba lt._ejecutar_orden_polymarket() pero nunca el aviso de
    # Telegram (vive en el bucle de live_trade.py main(), no en el helper
    # compartido). BALLENAS_TARDIAS#BTC#15min es tupla live desde 17-Jul y
    # no avisaba NUNCA de sus fills/errores reales. Mismo criterio anti-spam
    # que live_trade.py: solo fills/errores reales, nunca el no_fill
    # silencioso (ya cortado arriba).
    if resultado["ok"]:
        lt.enviar_telegram(
            f"🎯 *Orden live ejecutada (BALLENAS_TARDIAS)*\n"
            f"Estrategia: {STRATEGY}#{subtype}\n"
            f"Dirección: BUY_YES\n"
            f"Precio fill: {resultado['entry_price']:.4f} "
            f"(slip {resultado.get('slip_real', 0):+.4f})\n"
            f"Stake: {stake_info['stake_eur']:.2f}$  |  restante={restante_s:.1f}s\n"
            f"Bankroll operativo: {lt.bankroll_actual():.2f}$ (real al cierre de ciclo)"
        )
    else:
        lt.enviar_telegram(
            f"❌ *Orden live ERROR (BALLENAS_TARDIAS)*\n"
            f"{STRATEGY}#{subtype} BUY_YES\n"
            f"{resultado.get('error', '')[:200]}"
        )
    return True


def main():
    log(f"ballenas_executor_btc15m arrancado (DRY_RUN={DRY_RUN})")
    if not DRY_RUN:
        # Precalienta el import pesado de py_clob_client_v2 (~270ms, ver
        # live_trade.py:642-652) UNA vez al arrancar -- no en cada intento,
        # que es lo que hace live_trade.py al ser un subproceso fresco por
        # ciclo. Este proceso es persistente: el coste se paga una vez cada
        # 15min de vida útil en vez de una vez por trade.
        _ = lt._get_clob_client()
        log("ClobClient precalentado")

    while True:
        now = time.time()
        ts_end = (int(now) // (VENTANA_MIN * 60) + 1) * (VENTANA_MIN * 60)
        # 23-Jul: watch_lead_s ya no es estático (WATCH_LEAD_S=90 fijo) --
        # se relee vía cargar_calibracion() en cada vuelta (puede recalibrar
        # entre ventanas, cada hora, vía el cron de ballenas_observer.py).
        # Si no es significativo ahora mismo, duerme hasta la siguiente
        # ventana en vez de reintentar en bucle apretado -- mismo patrón que
        # ballenas_executor_5min.hilo_activo.
        calib = cargar_calibracion()
        if calib is None:
            log("BTC#15m no significativo ahora mismo -- duerme hasta la siguiente ventana")
            time.sleep(max(5, ts_end + 2 - time.time()))
            continue
        dormir = ts_end - calib["watch_lead_s"] - time.time()
        if dormir > 0:
            time.sleep(dormir)
        try:
            watch_window(ts_end)
        except Exception as e:
            log(f"error en watch_window: {e}")
        # margen de seguridad antes de recalcular la siguiente ventana
        time.sleep(max(0, ts_end + 2 - time.time()))


if __name__ == "__main__":
    main()
