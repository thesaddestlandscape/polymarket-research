#!/usr/bin/env python3
"""
resolution_sniper_naive_executor_dryrun.py — P34 FASE 1, 19-Ago.

Continuación directa de resolution_sniper_naive_depth_fase0.py: el gate
riguroso completo (analisis_gate_riguroso_resolution_sniper_naive_depth_19ago.py,
n=472 con outcome_real resuelto) confirmó que apostar CON la dirección
implícita de Chainlink en offset 0-3s post-cierre, CON profundidad real
verificada (ratio>=5x), da 6/6 combos GATE OK en 5min — BTC/ETH/SOL/XRP/
DOGE/BNB, pnl/tr +0.51€ a +0.96€ (stake 1.05€), wilson90lo muy por encima
del ask_medio, p_shuffle=0.0000-0.0025, split-half consistente. 15min NO
tiene aún muestra suficiente con profundidad confirmada -- excluido aquí.

Mismo hueco que P24 (wallet_mirror) señaló el 03-Ago: medir profundidad
en el INSTANTE DE DETECCIÓN no basta -- hace falta saber cuánto se
degrada la oportunidad entre "la detectamos" y "la hubiéramos podido
ejecutar de verdad" (tras el resto del pipeline de decisión: circuit
breakers, cálculo de stake). Este script añade exactamente ese tramo,
mismo patrón que wallet_mirror_executor_dryrun.py (P24 FASE 1):
  1. Se engancha a resolution_sniper_fade_depth_fase0.py::observar_ventana
     (mismo hilo, mismo reloj, NINGÚN hilo/proceso/screen nuevo -- criterio
     de presupuesto de CPU ya aplicado hoy mismo en esa fusión, py-spy
     encontró 85 hilos vivos en observadores_fase0.py).
  2. Cuando el combo (activo,marco) es uno de los 6 confirmados en 5min Y
     la profundidad en el instante de detección ya es fillable (ratio>=5x)
     Y el ask está en la banda accionable -- espera DECISION_LATENCY_S
     (simula el tiempo real que tardaría live_guard.puede_operar_live +
     live_stake.calcular_stake + circuit breakers antes de poder enviar
     una orden) y vuelve a consultar el libro completo (ambos ask, no solo
     profundidad al ask viejo -- el precio también pudo moverse).
  3. Registra ambas mediciones + el delta en
     data/shadow/resolution_sniper_naive_executor_dryrun.csv.

Seguridad -- por qué esto es DRY_RUN real, no una promesa (mismo criterio
que wallet_mirror_executor_dryrun.py):
  1. `DRY_RUN=True` -- guardián #1, primero en comprobarse. Con
     DRY_RUN=True el tramo de envío real ni se evalúa.
  2. Aunque alguien cambiara DRY_RUN a mano, el guardián #2 (fail-closed
     independiente) sigue en pie: la tupla sintética
     "RESOLUTION_SNIPER_NAIVE#{activo}#{marco}#BUY_{Up|Down}" NUNCA puede
     estar en `pares_permitidos_live` hasta que Javi la añada a mano
     (verificado explícitamente vía `_en_whitelist`, no asumido) -- no es
     una estrategia que shadow_predict.py reconozca.
  3. Activar de verdad exige, en este orden: (a) n>=40 en ESTE csv por
     combo (mide degradación con latencia real); (b) /code-review
     adversarial del diff que amplía COMBOS_CONFIRMADOS -- toca el camino
     de envío de orden, mismo criterio que cualquier cambio en
     live_trade.py; (c) decisión explícita de Javi para añadir la tupla
     EXACTA (activo+marco+dirección) a `pares_permitidos_live`. `DRY_RUN`
     ya está en `False` desde el 25-Ago (aprobado entonces) -- el único
     guardián real hoy es la whitelist (c) + COMBOS_CONFIRMADOS.

25-Ago, P34 FASE 2 (ingeniería, petición explícita Javi "adelante,
constrúyelo"): se añade el tramo de decisión completo (whitelist,
`live_guard.puede_operar_live`, `live_stake.calcular_stake`,
`resolution_sniper_naive_gate_bucket.evaluar()` fail-closed, techo de
correlación, circuit breaker) y el TRAMO de envío de orden real
(`lt._ejecutar_orden_polymarket`) -- mismo patrón exacto que
wallet_mirror_executor_dryrun.py (P24 FASE 2). Mismo día, `DRY_RUN` pasa
a `False` tras revisión manual (bloqueado en la práctica por la whitelist
vacía hasta que Javi decida promocionar una tupla).

Parametrizado por marco desde el diseño (petición explícita Javi 25-Ago:
"lo vamos a hacer también para 15 y 60 minutos") -- `COMBOS_CONFIRMADOS`
es el único punto que decide qué (activo,marco) se mide y qué puede
llegar a operar dinero real. 22-Sep: ampliado a 5min+15min (12 combos)
tras re-correr el gate riguroso completo con un mes de datos acumulado
(n=6.404 fillable, 14x el original de 19-Ago) -- 12/12 combos pasan
Wilson90+shuffle+split-half+BH-FDR, también desagregado por activo x
dirección x marco sin excepción (ver _pares_resolutionsnipernaive_5min_
promocion_nota_2026-09-22 / _15min_promocion_nota_2026-09-22 en
config_live.json para el detalle completo). 60min queda FUERA de este
fichero por completo -- no tiene ni observador de profundidad propio ni
slug determinista en gamma-api, es trabajo de una sesión futura (ver
project_pendiente_resolution_sniper_naive_60min_25ago).

NO coloca, cancela ni modifica ninguna orden real salvo que la tupla
exacta esté en `pares_permitidos_live` -- fail-closed por whitelist,
independiente de `DRY_RUN`.
"""
import csv
import json
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt
from live_guard import puede_operar_live
from live_stake import calcular_stake, bloquear_por_circuit_breaker
import resolution_sniper_naive_gate_bucket as rsngb

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
CONFIG_LIVE = REPO / "data" / "live" / "config_live.json"
OUT = DIR_SHADOW / "resolution_sniper_naive_executor_dryrun.csv"

DRY_RUN = False  # 25-Ago: activado con aprobación explícita de Javi tras revisión manual
# 23-Sep (petición explícita Javi: enviar 0-3s tras el cierre): cuando es True, el envío real pasa
# al camino rápido de resolution_sniper_precierre_executor.py (NAIVE_CAMINO_RAPIDO_ACTIVO, T+0s,
# envío ~0,3-0,5s). Este ejecutor decidía a T+4,1s de mediana y llegaba con el libro cerrado.
# Sigue observando/registrando igual. /code-review 23-Sep: interruptor ÚNICO compartido con el
# camino rápido -- clave de config_live.json (leída en cada decisión, sin flags a sincronizar).
CLAVE_CONFIG_CAMINO_RAPIDO = "resolution_sniper_naive_camino_rapido"


def _envio_delegado_camino_rapido() -> bool:
    """True -> no enviar desde aquí. Si la config no se puede leer, True (fail-closed: mejor
    no enviar desde ningún lado que arriesgar doble orden; el camino rápido también se para)."""
    try:
        return lt._cargar_config().get(CLAVE_CONFIG_CAMINO_RAPIDO) is True
    except Exception:
        return True
# completa (sin /code-review, por presupuesto de tokens) -- guardianes #2 (whitelist real)
# y #3 (gate_bucket fail-closed, ahora con recheck post-requote correcto, ver
# idea_wallet_mirror_recheck_postrequote_fuente_equivocada_25ago) siguen en pie. Restringido
# a los 12 combos 5min+15min confirmados (COMBOS_CONFIRMADOS) -- 60min NUNCA entra aquí
# hasta que cruce su propio gate.

# Los combos que se MIDEN (fillability post-latencia, este script). 22-Sep:
# 15min añadido tras re-correr el gate riguroso completo con el mes de datos
# acumulado desde el 19-Ago (n=6.404 fillable, 14x el original) -- 12/12
# combos (activo,marco) pasan Wilson90+shuffle+split-half+BH-FDR, TAMBIÉN
# desagregado por activo x dirección (Up/Down) x marco sin excepción, ver
# _pares_resolutionsnipernaive_15min_promocion_nota_2026-09-22 en
# config_live.json para el detalle completo. 60min no entra en este
# fichero, ver docstring.
COMBOS_CONFIRMADOS = {("BTC", "5min"), ("ETH", "5min"), ("SOL", "5min"),
                      ("XRP", "5min"), ("DOGE", "5min"), ("BNB", "5min"),
                      ("BTC", "15min"), ("ETH", "15min"), ("SOL", "15min"),
                      ("XRP", "15min"), ("DOGE", "15min"), ("BNB", "15min")}

RATIO_FILLABLE_MIN = 5.0
ASK_MIN, ASK_MAX = 0.05, 0.95
DECISION_LATENCY_S = 0.3  # latencia realista simulada del resto del pipeline
STAKE_REF_EUR = 1.05  # mismo suelo que el resto del sistema

# 23-Sep (aprobado Javi, propuesta #10): guarda de RÉGIMEN. El edge vive en
# eventos en los que el libro de Polymarket se queda atascado tras el cierre
# en VARIAS monedas a la vez; una detección aislada suele ser un cierre
# ambiguo donde la dirección implícita falla. Sobre depth_fase0 (fillable,
# mercados únicos, 19-Ago..23-Sep): 1 moneda en el cierre n=114 pnl/tr -0,414
# hit 37% (71 de los 76 mercados de días tranquilos); >=2 monedas n=1580
# +0,602 hit 90%, 11/11 días positivos, sin 4 mejores días +0,48. Además,
# ask>=0,80 pierde incluso dentro de ráfaga (n=362, ~-0,07/tr): >=2 monedas
# y ask<0,80 -> n=1218 +0,802, sin 2 mejores días +0,84.
MIN_MONEDAS_SIMULTANEAS = 2
ESPERA_MONEDAS_MAX_S = 1.2
ASK_MAX_OPERAR = 0.80
_DETECCIONES_CIERRE: dict = {}
_DETECCIONES_LOCK = threading.Lock()


def _registrar_deteccion(marco: str, ts_end, asset: str) -> None:
    """Registra una detección fillable (mismo criterio que el análisis:
    ratio>=RATIO_FILLABLE_MIN y ask en [ASK_MIN,ASK_MAX]) para el cierre
    (marco, ts_end). Poda entradas de más de 1h."""
    with _DETECCIONES_LOCK:
        _DETECCIONES_CIERRE.setdefault((marco, int(ts_end)), set()).add(asset)
        limite = time.time() - 3600
        for k in [k for k in _DETECCIONES_CIERRE if k[1] < limite]:
            del _DETECCIONES_CIERRE[k]


def _n_monedas_cierre(marco: str, ts_end) -> int:
    with _DETECCIONES_LOCK:
        return len(_DETECCIONES_CIERRE.get((marco, int(ts_end)), ()))


# 23-Sep: idempotencia por mercado. evaluar() se llama una vez por offset
# (0-3s) y _ejecutar_orden_polymarket no deduplica -- sin esto, en una ráfaga
# el mismo mercado podía recibir hasta 4 órdenes reales. Reserva atómica en
# memoria + trades.csv (cubre reinicios del proceso). Fail-closed: si
# trades.csv no se puede leer, no se reserva.
_MERCADOS_RESERVADOS: set = set()
_RESERVA_LOCK = threading.Lock()


def _reservar_mercado(market_id: str) -> bool:
    if not market_id:
        return False
    with _RESERVA_LOCK:
        if market_id in _MERCADOS_RESERVADOS:
            return False
        try:
            if market_id in lt._ya_operados_hoy():
                _MERCADOS_RESERVADOS.add(market_id)
                return False
        except Exception:
            return False
        _MERCADOS_RESERVADOS.add(market_id)
        return True

COLUMNS = [
    "timestamp_utc", "activo", "marco", "slug", "market_id", "condition_id",
    "ts_end", "offset_s",
    "direccion_implicita", "ask_deteccion", "ratio_deteccion",
    "ask_decision", "ratio_decision", "delta_ask", "delta_ratio",
    "sigue_fillable_decision",
    # 25-Ago, P34 FASE 2: mismas columnas de diagnóstico que
    # wallet_mirror_executor_dryrun.py -- por qué una señal fillable no
    # llegó (o sí) al tramo de envío.
    "tupla_sintetica", "en_whitelist_real", "puede_operar_ventana",
    "stake_dryrun_eur", "gate_bucket_veredicto",
]


def _en_whitelist(tupla: str) -> bool:
    """Mismo patrón exacto que wallet_mirror_executor_dryrun.py::
    _en_whitelist() -- fail-closed: un config_live.json corrupto/faltante
    se trata como "no está en whitelist", nunca como "todo permitido"."""
    try:
        cfg = json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
        return tupla in set(cfg.get("pares_permitidos_live", []))
    except Exception:
        return False


def _log(msg: str):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _veto_clv(asset: str, marco: str, direction: str, ask_ref) -> bool:
    """True si hay que vetar por CLV negativo. Mismo mecanismo exacto que
    momentum_ibs_ballena_executor.py/live_trade.py::main() -- 31-Ago
    (pendiente #4 checkpoint 31-Ago, hallazgo real): este ejecutor era el
    único de los live que NO lo tenía conectado, pese a que trades.csv
    todavía no acumula evidencia (n=0 RESOLUTION_SNIPER_NAIVE hoy) --
    fail-open por ausencia de evidencia, no por diseño (n_clv<CLV_VETO_MIN_N
    siempre da False hoy, cero cambio de comportamiento actual; listo para
    cuando el volumen real empiece a acumularse)."""
    try:
        py = float(ask_ref) if ask_ref not in (None, "") else None
    except (TypeError, ValueError):
        py = None
    lt._CLV_CACHE = None
    clv_medio, n_clv = lt._clv_tupla("RESOLUTION_SNIPER_NAIVE", f"{asset}#{marco}", direction, py=py)
    return n_clv >= lt.CLV_VETO_MIN_N and clv_medio < 0


def _guardar(fila: dict):
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(COLUMNS)
        w.writerow([fila.get(c, "") for c in COLUMNS])


def evaluar(asset: str, marco: str, slug: str, market_id: str, condition_id: str,
            ts_end: int, offset: int, direccion_impl: str, ask_impl,
            token_impl: str, ratio_deteccion, libro_fn, token_yes: str, token_no: str):
    """Se llama desde resolution_sniper_fade_depth_fase0.py::observar_ventana
    justo después de medir la profundidad de detección. Solo actúa sobre los
    combos en COMBOS_CONFIRMADOS (12 desde 22-Sep: 6 monedas x {5min,15min})
    y cuando la detección YA era fillable -- si no lo era en detección, no
    puede mejorar esperando (mismo hallazgo que P22, refutado 04-Ago: esperar
    no rescata señales, degrada)."""
    if (asset, marco) not in COMBOS_CONFIRMADOS:
        return
    if ratio_deteccion is None or ratio_deteccion < RATIO_FILLABLE_MIN:
        return
    if ask_impl is None or not (ASK_MIN <= ask_impl <= ASK_MAX):
        return

    _registrar_deteccion(marco, ts_end, asset)
    time.sleep(DECISION_LATENCY_S)
    # /code-review 23-Sep: cada hilo hace libro()+2 consultas de profundidad
    # antes de registrar, así que 0,3s no bastan para ver a las demás monedas
    # del mismo cierre. Sondear hasta ESPERA_MONEDAS_MAX_S y salir en cuanto
    # haya quorum -- solo retrasa a la primera moneda de una ráfaga; una
    # detección aislada espera y se rechaza igual.
    limite_espera = time.time() + ESPERA_MONEDAS_MAX_S - DECISION_LATENCY_S
    n_monedas = _n_monedas_cierre(marco, ts_end)
    while n_monedas < MIN_MONEDAS_SIMULTANEAS and time.time() < limite_espera:
        time.sleep(0.05)
        n_monedas = _n_monedas_cierre(marco, ts_end)

    ask_yes2, ask_no2, _, _ = libro_fn(token_yes, token_no)
    ask_decision = ask_yes2 if direccion_impl == "Up" else ask_no2
    depth2 = lt._consultar_profundidad_libro(None, token_impl, ask_decision or ask_impl, 1.05)
    ratio_decision = depth2.get("ratio_vs_stake")

    delta_ask = (ask_decision - ask_impl) if ask_decision is not None else ""
    delta_ratio = (ratio_decision - ratio_deteccion) if ratio_decision is not None else ""
    sigue_fillable = bool(ratio_decision is not None and ratio_decision >= RATIO_FILLABLE_MIN)

    # --- TRAMO NUEVO 25-Ago (P34 FASE 2): mismo patrón que
    # wallet_mirror_executor_dryrun.py -- calcular lo que el resto del
    # pipeline de decisión real haría, para poder loguearlo SIEMPRE (con o
    # sin DRY_RUN) y así medir en este mismo csv qué fracción de señales
    # fillable-en-decisión también pasarían whitelist/ventana/gate. ---
    tupla_sintetica = f"RESOLUTION_SNIPER_NAIVE#{asset}#{marco}#BUY_{direccion_impl}"
    direction = "BUY_YES" if direccion_impl == "Up" else "BUY_NO"
    en_wl = _en_whitelist(tupla_sintetica)
    try:
        # /code-review 25-Ago: si esto lanza, puede_ventana quedaba en None
        # -- ni True ni False -- y el guardián de abajo (`is False`) NO lo
        # trataba como bloqueo, dejando pasar hacia el resto de checks pese
        # a no saber si estamos en ventana horaria live. Fail-closed real:
        # cualquier cosa que no sea True explícito bloquea (ver más abajo).
        puede_ventana, _motivo = puede_operar_live("RESOLUTION_SNIPER_NAIVE", f"{asset}#{marco}")
    except Exception:
        puede_ventana = None
    try:
        # 19-Ago, gate riguroso: pnl/tr +0.51 a +0.96€ sobre stake 1.05€ --
        # ic_proxy conservador acotado al mismo rango que wallet_mirror usa
        # para su edge_pp/100 (nunca inventar un IC sin medirlo).
        ic_proxy = 0.15
        # /code-review 25-Ago: direction= añadido -- sin él, calcular_stake()
        # se salta _inventory_penalty() y _hrp_exposure_factor() (ambos
        # exigen direction truthy), perdiendo la reducción por inventario
        # correlacionado y el techo de exposición HRP que el resto de
        # tuplas live sí tienen.
        resultado_stake = calcular_stake(ic_proxy, strategy="RESOLUTION_SNIPER_NAIVE",
                                          subtype=f"{asset}#{marco}", direction=direction)
        stake_dryrun = resultado_stake.get("stake_eur", STAKE_REF_EUR)
    except Exception:
        stake_dryrun = STAKE_REF_EUR
    ask_ref = ask_decision if ask_decision is not None else ask_impl
    gate_bp = (rsngb.evaluar(asset, marco, direccion_impl, ask_ref)
               if ask_ref is not None else {"veredicto": "sin_concluir"})

    fila = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
        "activo": asset, "marco": marco, "slug": slug,
        "market_id": market_id, "condition_id": condition_id,
        "ts_end": ts_end, "offset_s": offset,
        "direccion_implicita": direccion_impl,
        "ask_deteccion": ask_impl, "ratio_deteccion": ratio_deteccion,
        "ask_decision": ask_decision if ask_decision is not None else "",
        "ratio_decision": ratio_decision if ratio_decision is not None else "",
        "delta_ask": delta_ask, "delta_ratio": delta_ratio,
        "sigue_fillable_decision": sigue_fillable,
        "tupla_sintetica": tupla_sintetica,
        "en_whitelist_real": int(en_wl),
        "puede_operar_ventana": puede_ventana if puede_ventana is not None else "",
        "stake_dryrun_eur": stake_dryrun if stake_dryrun else "",
        "gate_bucket_veredicto": gate_bp.get("veredicto", "sin_concluir"),
    }
    _guardar(fila)
    _log(f"[{asset}#{marco}] ts_end={ts_end} offset={offset} dir={direccion_impl} "
         f"deteccion={ask_impl}(ratio={ratio_deteccion}) "
         f"decision={ask_decision}(ratio={ratio_decision}) "
         f"sigue_fillable={sigue_fillable} en_whitelist_real={en_wl} "
         f"gate={gate_bp.get('veredicto')} monedas_cierre={n_monedas}")

    # --- P34 FASE 2 -- tramo de envío real. Inalcanzable con DRY_RUN=True
    # (guardián #1). Si algún día se pone DRY_RUN=False, los guardianes #2
    # (whitelist) y #3 (gate_bucket fail-closed) siguen en pie: esta tupla
    # nunca opera hasta que Javi la añada a mano a pares_permitidos_live Y
    # el gate_bucket confirme bueno_confirmado para el bucket exacto. ---
    if not DRY_RUN and _envio_delegado_camino_rapido():
        _log("  ↪ envío real delegado al camino rápido (resolution_sniper_precierre_executor.py, "
             "T+0s) -- este tramo solo mide")
    elif not DRY_RUN:
        if not en_wl:
            _log(f"  ⛔ {tupla_sintetica} no está en pares_permitidos_live -- "
                 f"fail-closed, no se ejecuta pese a DRY_RUN=False")
        elif not sigue_fillable:
            _log("  no sigue fillable en decisión -- no se ejecuta")
        elif n_monedas < MIN_MONEDAS_SIMULTANEAS:
            _log(f"  ⛔ detección aislada ({n_monedas} moneda(s) en este cierre, mínimo "
                 f"{MIN_MONEDAS_SIMULTANEAS}) -- régimen tranquilo, no se ejecuta")
        elif ask_impl >= ASK_MAX_OPERAR or (ask_decision is not None and ask_decision >= ASK_MAX_OPERAR):
            _log(f"  ⛔ ask>={ASK_MAX_OPERAR} (deteccion={ask_impl}, decision={ask_decision}) "
                 f"-- payout inverso, no se ejecuta")
        elif puede_ventana is not True:
            # /code-review 25-Ago: `is not True` (no `is False`) -- None
            # (puede_operar_live lanzó excepción, ej. config_live.json a
            # medio escribir por el fast loop) debe bloquear igual que
            # False. "sin datos -> no operar", nunca al revés.
            _log(f"  ⛔ no se pudo confirmar ventana horaria live (puede_ventana={puede_ventana}) "
                 f"-- fail-closed, no se ejecuta")
        elif gate_bp.get("veredicto") != "bueno_confirmado":
            _log(f"  ⛔ veto micro-bucket (solo opera en bueno_confirmado): "
                 f"veredicto={gate_bp.get('veredicto')} -- no se ejecuta")
        elif _veto_clv(asset, marco, direction, ask_ref):
            _log("  ⛔ veto CLV: clv_medio<0 con n suficiente -- no se ejecuta")
        elif (lt._posiciones_abiertas_misma_direccion(direction)
              >= lt._cargar_config().get("riesgo", {})
                  .get("max_posiciones_abiertas_misma_direccion", 2)):
            _log(f"  ⛔ techo de correlación ({direction}) alcanzado -- no se ejecuta")
        elif bloquear_por_circuit_breaker(
                lambda motivo: _log(f"  ⛔ circuit breaker activo ({motivo}) -- no se ejecuta")):
            pass
        elif ask_ref in (None, "") or stake_dryrun in (None, "") or not (float(stake_dryrun or 0) > 0):
            _log("  ⛔ precio/stake sin resolver -- fail-closed, no se ejecuta")
        elif not _reservar_mercado(market_id):
            _log(f"  ⛔ mercado {market_id} ya operado/reservado (u trades.csv ilegible) "
                 f"-- idempotencia, no se ejecuta")
        else:
            ask_ref_f = float(ask_ref)
            precio_orden_yes = ask_ref_f if direction == "BUY_YES" else round(1.0 - ask_ref_f, 6)
            # edge_dir: mismo ic_proxy usado para el stake -- sin esto,
            # _ejecutar_orden_polymarket se salta el re-quote/abort si el
            # edge se evaporó entre detección y decisión (_decidir_requote,
            # mismo guardián que el resto de ejecutores live exige,
            # CLAUDE.md: "aborta si edge<0.02").
            edge_dir = ic_proxy
            resultado = lt._ejecutar_orden_polymarket(
                market_id, direction, float(stake_dryrun), precio_orden_yes,
                edge_dir=edge_dir,
                contexto={"strategy": "RESOLUTION_SNIPER_NAIVE", "subtype": f"{asset}#{marco}",
                          "tupla_sintetica": tupla_sintetica,
                          "precio_max_token": ASK_MAX_OPERAR})
            _log(f"  🚨 ORDEN REAL enviada ({tupla_sintetica}): {resultado}")
            if resultado.get("no_fill"):
                # /code-review 23-Sep: sin posición -> liberar para que el
                # offset siguiente pueda reintentar. Excepción arriba = no se
                # sabe si la orden salió -> la reserva se mantiene (fail-closed).
                with _RESERVA_LOCK:
                    _MERCADOS_RESERVADOS.discard(market_id)
            else:
                end_date_real = datetime.fromtimestamp(int(ts_end), timezone.utc).isoformat()
                trade = {
                    "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                    "market_id": market_id, "question": "", "end_date": end_date_real,
                    "strategy": "RESOLUTION_SNIPER_NAIVE", "subtype": f"{asset}#{marco}",
                    "direction": direction,
                    "stake_eur": float(stake_dryrun) if resultado.get("ok") else 0.0,
                    "entry_price": resultado.get("entry_price", ""),
                    "signal_ask": round(ask_ref_f, 4),
                    "slip_real": resultado.get("slip_real", ""),
                    "ic_modelo": round(ic_proxy, 4),
                    "edge_neto": round(edge_dir, 4),
                    "conviction_score": "",
                    "kelly_recomendado": stake_dryrun,
                    "status": "OPEN" if resultado.get("ok") else "ERROR",
                    "close_timestamp": "", "exit_price": "", "outcome_real": "",
                    "fee_eur": resultado.get("fee_eur", 0),
                    "pnl_bruto_eur": "", "pnl_neto_eur": "",
                    "notas": (f"resolution_sniper_naive offset={offset}s"
                              if resultado.get("ok") else lt.notas_error_con_order_id(resultado)),
                }
                # /code-review 25-Ago: registro+alerta de un FILL REAL
                # aislados en su propio try/except -- antes, si
                # _registrar_trade() lanzaba (lock de trades.csv, campo
                # inesperado), la excepción se propagaba hasta el
                # `except Exception` genérico de observar_ventana() y la
                # engullía en silencio: la orden ya habría movido dinero
                # real pero jamás quedaría en trades.csv (rompe dedup de
                # _ya_operados_hoy, bankroll, PnL) y sin ningún aviso. Un
                # fallo aquí NUNCA puede quedar silencioso.
                try:
                    lt._registrar_trade(trade)
                    if resultado.get("ok"):
                        lt.enviar_telegram(
                            f"🎯 *Orden live ejecutada (RESOLUTION_SNIPER_NAIVE)*\n"
                            f"Tupla: {tupla_sintetica}\n"
                            f"Precio fill: {resultado['entry_price']:.4f} "
                            f"(slip {resultado.get('slip_real', 0):+.4f})\n"
                            f"Stake: {float(stake_dryrun):.2f}€\n"
                            f"Bankroll operativo: {lt.bankroll_actual():.2f}$ (real al cierre de ciclo)"
                        )
                    else:
                        lt.enviar_telegram(
                            f"❌ *Orden live ERROR (RESOLUTION_SNIPER_NAIVE)*\n"
                            f"{tupla_sintetica}\n"
                            f"{str(resultado.get('error', ''))[:200]}"
                        )
                except Exception as e:
                    _log(f"  🚨🚨 FALLO registrando trade REAL tras fill/{resultado.get('ok')} "
                         f"({tupla_sintetica}): {e} -- POSICIÓN REAL POSIBLEMENTE SIN REGISTRAR, "
                         f"revisar trades.csv y el libro de la wallet manualmente YA")
                    try:
                        lt.enviar_telegram(
                            f"🚨 *FALLO CRÍTICO (RESOLUTION_SNIPER_NAIVE)*\n"
                            f"Orden real puede haberse ejecutado pero el registro/aviso falló: {e}\n"
                            f"Tupla: {tupla_sintetica} — revisar manualmente."
                        )
                    except Exception:
                        pass
