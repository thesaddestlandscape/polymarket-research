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
  3. Activar esto de verdad exige, en este orden: (a) n>=40 en ESTE csv
     por combo (mide degradación con latencia real, YA CUMPLIDO 5min:
     n=125, 99.2% sigue fillable) -- 15min sigue sin cumplirlo, ver más
     abajo; (b) /code-review adversarial de este mismo diff -- toca el
     camino de envío de orden, mismo criterio que cualquier cambio en
     live_trade.py; (c) decisión explícita de Javi para añadir la tupla
     EXACTA (activo+marco+dirección) a `pares_permitidos_live`; (d) flip
     manual de `DRY_RUN` a False. Ninguno de los cuatro ha pasado todavía.

25-Ago, P34 FASE 2 (ingeniería, petición explícita Javi "adelante,
constrúyelo"): se añade el tramo de decisión completo (whitelist,
`live_guard.puede_operar_live`, `live_stake.calcular_stake`,
`resolution_sniper_naive_gate_bucket.evaluar()` fail-closed, techo de
correlación, circuit breaker) y el TRAMO de envío de orden real
(`lt._ejecutar_orden_polymarket`) -- mismo patrón exacto que
wallet_mirror_executor_dryrun.py (P24 FASE 2). `DRY_RUN` sigue en `True`:
el propósito de este cambio es dejar el código listo y revisado, no
activarlo hoy.

Parametrizado por marco desde el diseño (petición explícita Javi 25-Ago:
"lo vamos a hacer también para 15 y 60 minutos") -- `COMBOS_CONFIRMADOS`
es el único punto que decide qué (activo,marco) se mide y, más adelante,
qué puede llegar a operar dinero real; añadir 15min por activo es solo
ampliar ese set cuando cada uno cruce su propio n>=40 de profundidad
(hoy: BTC=37, ETH=29, SOL=28, XRP=28, DOGE=28, BNB=12, ninguno cruza
todavía -- CLAUDE.md pt.17, nunca en bloque). 60min queda FUERA de este
fichero por completo -- no tiene ni observador de profundidad propio ni
slug determinista en gamma-api, es trabajo de una sesión futura (ver
project_pendiente_resolution_sniper_naive_60min_25ago).

NO coloca, cancela ni modifica ninguna orden real mientras DRY_RUN=True.
"""
import csv
import json
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
# completa (sin /code-review, por presupuesto de tokens) -- guardianes #2 (whitelist real)
# y #3 (gate_bucket fail-closed, ahora con recheck post-requote correcto, ver
# idea_wallet_mirror_recheck_postrequote_fuente_equivocada_25ago) siguen en pie. Restringido
# a los 6 combos 5min confirmados (COMBOS_CONFIRMADOS) -- 15min/60min NUNCA entran aquí
# hasta que crucen su propio gate.

# Los combos que se MIDEN (fillability post-latencia, este script). Solo
# 5min tiene hoy gate riguroso + profundidad real confirmada (19-Ago).
# 15min entra aquí activo por activo en cuanto cruce su propio n>=40 de
# profundidad -- NO añadir los 6 en bloque (CLAUDE.md pt.17). 60min no
# entra en este fichero, ver docstring.
COMBOS_CONFIRMADOS = {("BTC", "5min"), ("ETH", "5min"), ("SOL", "5min"),
                      ("XRP", "5min"), ("DOGE", "5min"), ("BNB", "5min")}

RATIO_FILLABLE_MIN = 5.0
ASK_MIN, ASK_MAX = 0.05, 0.95
DECISION_LATENCY_S = 0.3  # latencia realista simulada del resto del pipeline
STAKE_REF_EUR = 1.05  # mismo suelo que el resto del sistema

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
    6 combos confirmados y cuando la detección YA era fillable -- si no lo
    era en detección, no puede mejorar esperando (mismo hallazgo que P22,
    refutado 04-Ago: esperar no rescata señales, degrada)."""
    if (asset, marco) not in COMBOS_CONFIRMADOS:
        return
    if ratio_deteccion is None or ratio_deteccion < RATIO_FILLABLE_MIN:
        return
    if ask_impl is None or not (ASK_MIN <= ask_impl <= ASK_MAX):
        return

    time.sleep(DECISION_LATENCY_S)

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
         f"gate={gate_bp.get('veredicto')}")

    # --- P34 FASE 2 -- tramo de envío real. Inalcanzable con DRY_RUN=True
    # (guardián #1). Si algún día se pone DRY_RUN=False, los guardianes #2
    # (whitelist) y #3 (gate_bucket fail-closed) siguen en pie: esta tupla
    # nunca opera hasta que Javi la añada a mano a pares_permitidos_live Y
    # el gate_bucket confirme bueno_confirmado para el bucket exacto. ---
    if not DRY_RUN:
        if not en_wl:
            _log(f"  ⛔ {tupla_sintetica} no está en pares_permitidos_live -- "
                 f"fail-closed, no se ejecuta pese a DRY_RUN=False")
        elif not sigue_fillable:
            _log("  no sigue fillable en decisión -- no se ejecuta")
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
        elif (lt._posiciones_abiertas_misma_direccion(direction)
              >= lt._cargar_config().get("riesgo", {})
                  .get("max_posiciones_abiertas_misma_direccion", 2)):
            _log(f"  ⛔ techo de correlación ({direction}) alcanzado -- no se ejecuta")
        elif bloquear_por_circuit_breaker(
                lambda motivo: _log(f"  ⛔ circuit breaker activo ({motivo}) -- no se ejecuta")):
            pass
        elif ask_ref in (None, "") or stake_dryrun in (None, "") or not (float(stake_dryrun or 0) > 0):
            _log("  ⛔ precio/stake sin resolver -- fail-closed, no se ejecuta")
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
                          "tupla_sintetica": tupla_sintetica})
            _log(f"  🚨 ORDEN REAL enviada ({tupla_sintetica}): {resultado}")
            if not resultado.get("no_fill"):
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
                              if resultado.get("ok") else resultado.get("error", "")),
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
