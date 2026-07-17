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

Corre en screen propia:
  screen -dmS ballenas_fast bash -c "cd /root/polymarket-research && .venv/bin/python ballenas_executor_btc15m.py >> logs/ballenas_fast.log 2>&1"
"""
import json
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import requests

import live_trade as lt
from live_guard import puede_operar_live
from live_stake import calcular_stake, verificar_circuit_breaker
from smart_money_tracker import trades_de_mercado

DIR = Path(__file__).resolve().parent
DIR_SHADOW = DIR / "data" / "shadow"
LOG_PATH = DIR / "logs" / "ballenas_fast.log"

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"

STRATEGY = "BALLENAS_TARDIAS"
ASSET = "BTC"
VENTANA_MIN = 15
COMBO = "BTC#15m"

DRY_RUN = False  # Fase 2 (17-Jul, activada: aprobación explícita Javi + /code-review +
                  # gate formal de dosis-respuesta corrido para BTC#15m específicamente,
                  # ver _pares_ballenas_tardias_btc15m_promocion_nota_2026-07-17 en config_live.json

WATCH_LEAD_S = 90        # empieza a vigilar 90s antes del cierre (antes de que
                          # abra la ventana real de 4-32s, para tener margen)
POLL_INTERVAL_S = 1.0    # cadencia del bucle rápido
HARD_FLOOR_S = 3.0       # por debajo de esto, se abandona -- fail-closed por timing
CONCENTRACION_MIN = 0.9  # bucket con 98.5% acierto + profundidad confirmada 16-Jul
MIN_TRADES_BALLENA = 3
PROB_BUCKET = 0.985      # probabilidad empírica calibrada del bucket [0.9,1.0)
                          # (analisis_ballenas_dosis_respuesta_16jul.py, n=273)

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


def concentracion_ballenas(condition_id: str, banda_lo: float, banda_hi: float) -> tuple[float | None, int, str]:
    """(pct_yes, n, motivo) del flujo BUY de ballenas en `condition_id`,
    dentro de la banda de precio, que compró YES -- mide AMBOS lados (a
    diferencia de live_trade._ballenas_conviccion_mercado, que solo mide el
    lado que ya decidimos nosotros) porque aquí la dirección todavía no
    está fijada: la decide el lado mayoritario de las ballenas.

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
        return None, 0, "error_api"
    n_yes = n_no = 0
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
        if not (banda_lo <= precio_t < banda_hi):
            continue
        if outcome_t in ("up", "yes"):
            n_yes += 1
        else:
            n_no += 1
    n = n_yes + n_no
    if n == 0:
        return None, 0, "sin_trades_en_banda"
    return n_yes / n, n, "ok"


def cargar_banda_btc15m() -> tuple[float, float] | None:
    """Banda de precio calibrada por ballenas_observer.py -- leída fresca
    cada ventana, nunca hardcodeada (puede moverse si el observer
    recalibra)."""
    try:
        estado = json.loads((DIR_SHADOW / "ballenas_timing_state.json").read_text())
    except Exception:
        return None
    e = estado.get(COMBO, {})
    if not e.get("significativo"):
        return None
    lo, hi = e.get("banda_lo"), e.get("banda_hi")
    if not (isinstance(lo, (int, float)) and isinstance(hi, (int, float))):
        return None
    return lo, hi


def watch_window(ts_end: int) -> bool:
    """Vigila un mercado BTC#15min concreto desde WATCH_LEAD_S hasta el
    cierre. True si ejecutó (o habría ejecutado en DRY_RUN)."""
    ts_start = ts_end - VENTANA_MIN * 60
    banda = cargar_banda_btc15m()
    if banda is None:
        log(f"[{ts_end}] BTC#15m no significativo en ballenas_timing_state.json -- se salta la ventana")
        return False
    banda_lo, banda_hi = banda

    mercado = None
    contadores = {"ok": 0, "sin_trades_en_banda": 0, "error_api": 0}
    while True:
        restante = ts_end - time.time()
        if restante > WATCH_LEAD_S:
            time.sleep(min(restante - WATCH_LEAD_S, 5))
            continue
        if restante < HARD_FLOOR_S:
            log(f"[{ts_end}] suelo de seguridad ({HARD_FLOOR_S}s) alcanzado sin confirmación -- se abandona "
                f"(resumen vigilancia: {sum(contadores.values())} polls, "
                f"ok={contadores['ok']} sin_trades_en_banda={contadores['sin_trades_en_banda']} "
                f"error_api={contadores['error_api']})")
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
            pct_yes, n, motivo_conc = f_conc.result()
            libro = f_libro.result()

        contadores[motivo_conc] = contadores.get(motivo_conc, 0) + 1
        if pct_yes is not None:
            log(f"[{ts_end}] restante={restante:.1f}s concentracion_yes={pct_yes:.2f} n={n} "
                f"ask={libro.get('best_ask') if libro else None}")
        elif motivo_conc == "error_api":
            # A diferencia de sin_trades_en_banda (silencioso, esperable y
            # frecuente), un fallo de API sí se loguea cada vez que ocurre
            # -- es la señal que antes quedaba escondida dentro de un hueco
            # de log indistinguible de "no hay actividad".
            log(f"[{ts_end}] restante={restante:.1f}s ⚠️ error_api consultando ballenas -- sin dato este ciclo")

        if (pct_yes is not None and n >= MIN_TRADES_BALLENA
                and pct_yes >= CONCENTRACION_MIN
                and libro and libro.get("best_ask") is not None
                and banda_lo <= libro["best_ask"] < banda_hi):
            py = libro["best_ask"]
            edge = PROB_BUCKET - py
            log(f"[{ts_end}] CONFIRMADO concentracion={pct_yes:.2f} n={n} py={py:.3f} "
                f"edge={edge:+.3f} restante={restante:.1f}s")
            return disparar(mercado, py, edge, restante)

        time.sleep(POLL_INTERVAL_S)


def disparar(mercado: dict, py: float, edge: float, restante_s: float) -> bool:
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
    # WATCH_LEAD_S=90s antes del cierre -- el fast loop (proceso
    # independiente, whitelist propia) puede operar ese mismo market_id en
    # los ~87s que pasan hasta que se dispara esta función. Repetir el check
    # aquí, lo más tarde posible antes de la orden real, no lo elimina del
    # todo (sigue sin lock cruzado entre procesos) pero cierra la mayor
    # parte de la ventana.
    if mercado["market_id"] in lt._ya_operados_hoy():
        log(f"  {mercado['market_id']} ya operado por otro proceso en la última ventana -- "
            f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}")
        return False

    ok_breaker, motivo_breaker = verificar_circuit_breaker()
    if not ok_breaker:
        log(f"  circuit breaker activo ({motivo_breaker}) -- {'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}")
        return False

    # ic_conviccion: /code-review 17-Jul encontró que se pasaba `edge` crudo
    # (PROB_BUCKET - py, ~0.02-0.08) donde calcular_stake espera un IC
    # histórico validado (ic_bayes, lo que usa cualquier otra tupla live).
    # Sin efecto en euros HOY (min_stake_eur=max_stake_eur=1.05€ pineado,
    # clamp lo absorbe) pero quedaría mal calibrado en cuanto se despinee.
    # PROB_BUCKET es la probabilidad calibrada por el backtest de
    # dosis-respuesta (n=273, analisis_ballenas_dosis_respuesta_16jul.py) --
    # el análogo real a un ic_bayes es su distancia a un lanzamiento justo.
    ic_conviccion = (PROB_BUCKET - 0.5) * 2
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
        "ic_modelo": round(PROB_BUCKET, 4),
        "edge_neto": round(edge, 4),
        "conviction_score": round(PROB_BUCKET, 4),
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
        dormir = ts_end - WATCH_LEAD_S - time.time()
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
