"""
wallet_mirror_executor_dryrun.py — P24 FASE 1, conecta wallet_mirror a un
pipeline de decisión real (petición explícita Javi, 03-Ago: "conecta el
ejecutor... hay que ir a milisegundos también").

Diferencia con wallet_mirror_sniper.py (que solo detecta y mide la
fill-ability EN EL INSTANTE DE DETECCIÓN): este script añade el tramo que
faltaba -- vuelve a consultar el libro real una SEGUNDA vez, unos
milisegundos después, simulando el momento en que una orden de verdad se
enviaría (después de calcular_stake/circuit-breakers). Así se mide, con
milisegundos reales, cuánto se degrada la oportunidad entre "la detectamos"
y "la hubiéramos podido ejecutar" -- la pregunta exacta de Javi, no una
aproximación.

06-Ago, P24 FASE 2 (DISEÑO, petición explícita Javi: "para seguir todas
las monedas, no solo BTC, de ahí ya vamos viendo, de ahí vamos minando N
y en unos días pego un análisis extensivo"): se añade el TRAMO de envío
de orden real (`lt._ejecutar_orden_polymarket`), pero **DRY_RUN sigue
en True** -- el propósito de este cambio es dejar el código listo y
revisado, no activarlo hoy. Cubre TODAS las monedas de `wallets`
(no hay ningún filtro por activo, igual que el resto del script) --
la decisión de qué monedas promocionar primero se toma más adelante,
con el análisis del gate riguroso por (tipo,activo,es_jugada_grande)
que ya distingue SEGUIR de FADE y detecta selección adversa por moneda
(ver `idea_wallet_mirror_edge_masivo_seguir_btc_06ago`).

Seguridad -- por qué esto sigue siendo DRY_RUN real, no solo una promesa:
  1. `DRY_RUN=True` (abajo) es el primer guardián -- con DRY_RUN=True el
     tramo de envío real ni se evalúa.
  2. Aunque alguien cambiara DRY_RUN a mano, el SEGUNDO guardián
     (fail-closed independiente) sigue en pie: la tupla sintética
     "WALLET_MIRROR#{activo}#{marco}#BUY_{lado}" NUNCA puede estar en
     `pares_permitidos_live` (no es una estrategia que
     shadow_predict.py/live_trade.py reconozcan) -- verificado
     explícitamente (`en_wl`) y logueado, no asumido. Sin la tupla en la
     whitelist, el tramo de envío real se salta igual.
  3. Activar esto de verdad (P24 FASE 2 real) exige: (a) `/code-review`
     adversarial de este mismo diff -- toca el camino de envío de orden,
     mismo criterio que cualquier cambio en live_trade.py; (b) añadir la
     tupla exacta a `pares_permitidos_live` -- decisión explícita de
     Javi, nunca autónoma; (c) flip manual de `DRY_RUN` a False. Ninguno
     de los tres ha pasado todavía.

Salida: data/shadow/wallet_mirror_executor_dryrun.csv -- una fila por
MATCH de tipo SEGUIR con fill-ability OK en la detección, con las DOS
mediciones de libro (detección y decisión) y el delta entre ambas.

Corre en screen propia:
  screen -dmS wmexec bash -c "cd /root/polymarket-research && .venv/bin/python wallet_mirror_executor_dryrun.py >> logs/wallet_mirror_executor.log 2>&1"
"""
import asyncio
import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import websockets

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from wallet_mirror_tracker import (  # noqa: E402
    wallets_operativas_recientes, _opuesto, _fillability_mirror, _market_id_y_direccion,
)
from fetch_polymarket_activity_ws import _parse_updown  # noqa: E402
import live_trade as lt  # noqa: E402
from live_guard import puede_operar_live  # noqa: E402
from live_stake import calcular_stake, bloquear_por_circuit_breaker  # noqa: E402
import wallet_mirror_gate_bucket as wmgb  # noqa: E402

DIR_SHADOW = REPO / "data" / "shadow"
CONFIG_LIVE = REPO / "data" / "live" / "config_live.json"
OUT = DIR_SHADOW / "wallet_mirror_executor_dryrun.csv"
VISTOS_PATH = DIR_SHADOW / "wallet_mirror_executor_vistos.json"

WS_URL = "wss://ws-live-data.polymarket.com"
PING_INTERVAL_S = 5
RECONNECT_ESPERA_S = 5
RECV_TIMEOUT_S = 30
REFRESCO_WALLETS_S = 1800
STAKE_REF_EUR = 1.05  # mismo suelo que el resto del sistema

DRY_RUN = False  # 11-Ago: activado con aprobación explícita de Javi tras checklist
# de conexión completo (ballenas cross-check + gates B/C N/A arquitectónicamente,
# documentado + D/E/F verificados wireados). Restringido a SEGUIR#BTC#5min#grande
# [0.50,0.55) n=234 p=0.004 y [0.70,0.75) n=219 p=0.006 (wallet_mirror_gate_bucket.json)
# vía el guardián #2 (whitelist real, pares_permitidos_live) + guardián #3
# (gate_bucket_propio-style, fail-closed a esas 2 zonas exactas).
                # (P24 FASE 2). Aunque se cambiara, el fail-closed de la
                # whitelist (ver docstring) impide ejecución real igualmente.

COLUMNS = ["timestamp_utc", "trade_timestamp", "wallet", "tipo", "edge_pp_validado",
           "n_validado", "activo", "marco", "mirror_lado", "market_slug",
           "lag_ws_ms", "lag_deteccion_a_decision_ms",
           "ratio_deteccion", "ask_deteccion", "ratio_decision", "ask_decision",
           "degradacion_ask_pct", "sigue_fillable_en_decision",
           "stake_dryrun_eur", "tupla_sintetica", "en_whitelist_real",
           "puede_operar_ventana",
           # 03-Ago: cruce con el hallazgo "grandes jugadas" (idea_grandes_
           # jugadas_wallets_validadas_29jul) -- mismo cálculo que
           # wallet_mirror_tracker.py, para ver si la fill-ability real en
           # milisegundos difiere cuando la wallet apuesta con convicción
           # extra (>=2x su propia mediana) vs una jugada normal suya.
           "usd_trade", "size_mediana_wallet", "ratio_vs_mediana_propia",
           "es_jugada_grande"]


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
    print(f"[{ts}] {msg}", flush=True)


def _vistos_cargar() -> dict:
    """dict en vez de set: mismo fix que wallet_mirror_sniper.py (01-Sep) --
    Python preserva orden de inserción en dict (NO en set), necesario para
    que el cap de abajo descarte las entradas más VIEJAS, no un subconjunto
    arbitrario por hash."""
    try:
        return dict.fromkeys(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return {}


def _vistos_guardar(vistos: dict) -> None:
    VISTOS_PATH.write_text(json.dumps(list(vistos)[-50000:]), encoding="utf-8")


def _guardar_fila(fila: dict) -> None:
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        if nuevo:
            w.writeheader()
        w.writerow(fila)


def _en_whitelist(tupla: str) -> bool:
    try:
        c = json.loads(CONFIG_LIVE.read_text())
        return tupla in set(c.get("pares_permitidos_live", []))
    except Exception:
        return False


async def _mantener_ping(ws):
    try:
        while True:
            await asyncio.sleep(PING_INTERVAL_S)
            await ws.send("PING")
    except (asyncio.CancelledError, websockets.exceptions.ConnectionClosed):
        pass


async def _correr_una_conexion(wallets: dict, vistos: dict) -> dict:
    async with websockets.connect(WS_URL, open_timeout=10, close_timeout=5) as ws:
        sub = {"action": "subscribe", "subscriptions": [{"topic": "activity", "type": "trades"}]}
        await ws.send(json.dumps(sub))
        _log(f"Conectado -- {len(wallets)} wallets validadas, DRY_RUN={DRY_RUN}")
        ping_task = asyncio.create_task(_mantener_ping(ws))
        n_trades = n_matches = n_fillable_decision = 0
        try:
            while True:
                raw = await asyncio.wait_for(ws.recv(), timeout=RECV_TIMEOUT_S)
                if not raw:
                    continue
                try:
                    msg = json.loads(raw)
                except (json.JSONDecodeError, TypeError):
                    continue
                payload = msg.get("payload")
                if not isinstance(payload, dict) or "proxyWallet" not in payload:
                    continue
                n_trades += 1
                if (payload.get("side") or "").strip().upper() != "BUY":
                    continue
                w = (payload.get("proxyWallet") or "").lower()
                event_slug = payload.get("eventSlug", "")
                activo, marco = _parse_updown(event_slug, payload.get("title", ""))
                if activo is None:
                    continue
                info = wallets.get((w, activo, marco))
                if info is None or info["tipo"] != "SEGUIR":
                    continue  # FADE ya descartado (hit=31.9% en fillable, sin valor)

                market_slug = payload.get("slug", "")
                # 01-Sep (petición explícita Javi, mismo fix que
                # wallet_mirror_sniper.py -- este SÍ es el ejecutor live,
                # DRY_RUN=False): antes el dedup era f"{w}|{market_slug}",
                # PERMANENTE -- una wallet que añade convicción operando el
                # MISMO mercado varias veces solo se capturaba la primera
                # vez, para siempre. NO se pierde ninguna protección contra
                # abrir 2 posiciones reales en el mismo mercado: eso ya lo
                # bloquea live_trade.py::_ya_operados_hoy() de forma
                # independiente (fail-closed sobre trades.csv real, no sobre
                # este dedup de detección). Incluir transaction_hash hace
                # que este dedup solo bloquee una redelivery EXACTA del
                # mismo trade (reconexión del websocket), no trades reales
                # distintos de la misma wallet en el mismo mercado.
                tx_hash = payload.get("transactionHash", "")
                dedup_key = f"{w}|{market_slug}|{tx_hash}" if tx_hash else f"{w}|{market_slug}|{payload.get('timestamp')}"
                if dedup_key in vistos:
                    continue
                vistos[dedup_key] = None

                t_deteccion = time.monotonic()
                ahora = datetime.now(timezone.utc)
                ws_ts = payload.get("timestamp")
                try:
                    lag_ws_ms = round((ahora.timestamp() - float(ws_ts)) * 1000, 1) if ws_ts else None
                except (TypeError, ValueError):
                    lag_ws_ms = None

                lado_wallet = payload.get("outcome", "")
                mirror_lado = lado_wallet  # SEGUIR siempre
                precio = payload.get("price", "")

                ratio_size = None
                size_mediana = info.get("size_mediana")
                try:
                    usd_trade = float(precio or 0) * float(payload.get("size", 0) or 0)
                except (TypeError, ValueError):
                    usd_trade = 0.0
                if size_mediana and usd_trade > 0:
                    ratio_size = round(usd_trade / size_mediana, 2)

                fill_deteccion = _fillability_mirror(market_slug, mirror_lado, precio)
                if not fill_deteccion.get("ok"):
                    continue  # sin libro en detección -- no hay nada que decidir

                # --- TRAMO NUEVO: segunda consulta simulando el instante de
                # decisión real (tras stake/circuit-breakers), no el de
                # detección. Aquí es donde se mide la degradación real. ---
                stake_dryrun, tupla_sintetica, en_wl, puede_ventana = None, None, False, None
                try:
                    ic_proxy = min(0.30, max(0.05, info["edge_pp"] / 100.0))
                    resultado_stake = calcular_stake(ic_proxy, strategy="WALLET_MIRROR",
                                                      subtype=f"{activo}#{marco}")
                    stake_dryrun = resultado_stake.get("stake_eur", STAKE_REF_EUR)
                except Exception:
                    stake_dryrun = STAKE_REF_EUR

                tupla_sintetica = f"WALLET_MIRROR#{activo}#{marco}#BUY_{mirror_lado}"
                en_wl = _en_whitelist(tupla_sintetica)
                try:
                    puede_ventana, _motivo = puede_operar_live("WALLET_MIRROR", f"{activo}#{marco}")
                except Exception:
                    puede_ventana = None

                # 12-Ago (perfilado latencia, petición Javi): reusar el
                # token_id ya resuelto en fill_deteccion -- eliminar la
                # 2ª resolución gamma-api redundante (mismo mercado
                # inmutable), medida 90-300ms. Ver docstring de
                # _fillability_mirror en wallet_mirror_tracker.py.
                fill_decision = _fillability_mirror(
                    market_slug, mirror_lado, precio,
                    token_id_precargado=fill_deteccion.get("token_id"))
                t_decision = time.monotonic()
                lag_dec_ms = round((t_decision - t_deteccion) * 1000, 2)

                ask_d = fill_deteccion.get("mejor_ask")
                ask_2 = fill_decision.get("mejor_ask") if fill_decision.get("ok") else None
                degradacion_pct = None
                if ask_d not in (None, "") and ask_2 not in (None, ""):
                    try:
                        degradacion_pct = round((float(ask_2) - float(ask_d)) / float(ask_d) * 100, 3)
                    except (TypeError, ValueError, ZeroDivisionError):
                        degradacion_pct = None

                ratio_2 = fill_decision.get("ratio_vs_stake") if fill_decision.get("ok") else None
                sigue_fillable = bool(ratio_2 is not None and ratio_2 != "" and float(ratio_2) >= 5)
                if sigue_fillable:
                    n_fillable_decision += 1

                fila = {
                    "timestamp_utc": ahora.isoformat(timespec="milliseconds"),
                    "trade_timestamp": datetime.fromtimestamp(float(ws_ts), timezone.utc).isoformat(timespec="milliseconds") if ws_ts else "",
                    "wallet": w, "tipo": info["tipo"], "edge_pp_validado": info["edge_pp"],
                    "n_validado": info["n"], "activo": activo, "marco": marco,
                    "mirror_lado": mirror_lado, "market_slug": market_slug,
                    "lag_ws_ms": lag_ws_ms if lag_ws_ms is not None else "",
                    "lag_deteccion_a_decision_ms": lag_dec_ms,
                    "ratio_deteccion": fill_deteccion.get("ratio_vs_stake", ""),
                    "ask_deteccion": ask_d if ask_d is not None else "",
                    "ratio_decision": ratio_2 if ratio_2 is not None else "",
                    "ask_decision": ask_2 if ask_2 is not None else "",
                    "degradacion_ask_pct": degradacion_pct if degradacion_pct is not None else "",
                    "sigue_fillable_en_decision": int(sigue_fillable),
                    "stake_dryrun_eur": stake_dryrun if stake_dryrun else "",
                    "tupla_sintetica": tupla_sintetica,
                    "en_whitelist_real": int(en_wl),
                    "puede_operar_ventana": puede_ventana if puede_ventana is not None else "",
                    "usd_trade": usd_trade if usd_trade > 0 else "",
                    "size_mediana_wallet": size_mediana if size_mediana else "",
                    "ratio_vs_mediana_propia": ratio_size if ratio_size is not None else "",
                    "es_jugada_grande": int(ratio_size >= 2.0) if ratio_size is not None else "",
                }
                _guardar_fila(fila)
                n_matches += 1
                _log(f"🎯 DRY_RUN {activo}#{marco} lag_ws={lag_ws_ms}ms lag_dec={lag_dec_ms}ms "
                     f"degrad_ask={degradacion_pct}% sigue_fillable={sigue_fillable} "
                     f"stake_sim={stake_dryrun} en_whitelist_real={en_wl}")

                # --- P24 FASE 2 (diseño 06-Ago) -- tramo de envío real.
                # Inalcanzable con DRY_RUN=True (guardián #1). Si algún día
                # se pone DRY_RUN=False, el guardián #2 (en_wl) sigue
                # fail-closed: WALLET_MIRROR nunca está en
                # pares_permitidos_live hasta que Javi lo decida a mano. ---
                if not DRY_RUN:
                    if not en_wl:
                        _log(f"  ⛔ {tupla_sintetica} no está en pares_permitidos_live -- "
                             f"fail-closed, no se ejecuta pese a DRY_RUN=False")
                    elif not sigue_fillable:
                        _log("  no sigue fillable en decisión -- no se ejecuta")
                    elif puede_ventana is False:
                        _log("  fuera de ventana horaria live -- no se ejecuta")
                    else:
                        resuelto = _market_id_y_direccion(market_slug, mirror_lado)
                        if resuelto is None:
                            _log("  ⛔ no se pudo resolver market_id/dirección con seguridad "
                                 "(outcomes inesperados o Gamma sin datos) -- fail-closed, no se ejecuta")
                        market_id, direction, end_date_real = resuelto if resuelto else (None, None, "")
                        # 11-Ago: precio de referencia (fallback decisión->
                        # detección) calculado UNA vez y reusado tanto para
                        # el veto de micro-bucket como para la orden -- antes
                        # se recalculaba la misma expresión dos veces
                        # (/code-review).
                        ask_ref = ask_2 if ask_2 not in (None, "") else ask_d
                        # 11-Ago (P24 FASE 2, ingeniería completada -- DRY_RUN
                        # sigue en True, este bloque sigue inalcanzable):
                        # gates que faltaban comparados con el precedente ya
                        # en producción (ballenas_executor_5min.py) --
                        # techo de correlación, circuit breaker y el veto de
                        # micro-bucket (gate_bucket_propio-style, CLAUDE.md
                        # pt.12: TODO ejecutor live exige bueno_confirmado,
                        # fail-closed). _ejecutar_orden_polymarket() NO
                        # comprueba ninguno de los tres internamente (viven
                        # en el bucle externo de live_trade.py::main() o son
                        # específicos de cada ejecutor), así que cualquier
                        # ejecutor fuera de ese bucle tiene que replicarlos
                        # a mano. Sin el veto de micro-bucket, la edge de
                        # Wallet Mirror (concentrada en 1-2 buckets estrechos
                        # confirmados, ver wallet_mirror_gate_bucket.json)
                        # se destruiría en cuanto DRY_RUN=False, disparando
                        # en CUALQUIER bucket de cualquier match SEGUIR.
                        # 11-Ago (/code-review): NO se replica el veto CLV
                        # (`lt._clv_tupla`) que sí usan los ejecutores
                        # hermanos -- ese veto lee results.csv por
                        # strategy="WALLET_MIRROR", pero Wallet Mirror es un
                        # pipeline paralelo que NUNCA escribe en results.csv
                        # (ver docstring del módulo), así que siempre
                        # devolvería n=0 y sería un no-op silencioso; se deja
                        # fuera explícitamente en vez de simular protección
                        # que no protege nada.
                        # `direction` YA resuelto (arriba), no el
                        # mirror_lado crudo -- el correlation cap y el veto
                        # de micro-bucket son sobre BUY_YES/BUY_NO reales.
                        gate_bp = wmgb.evaluar(
                            info["tipo"], activo, marco, ask_ref,
                            bool(ratio_size is not None and ratio_size >= 2.0),
                        ) if resuelto is not None and ask_ref not in (None, "") else {"veredicto": "sin_concluir"}
                        if resuelto is None:
                            pass
                        elif gate_bp["veredicto"] != "bueno_confirmado":
                            _log(f"  ⛔ veto micro-bucket (solo opera en bueno_confirmado): "
                                 f"veredicto={gate_bp['veredicto']} -- no se ejecuta")
                        elif (lt._posiciones_abiertas_misma_direccion(direction)
                              >= lt._cargar_config().get("riesgo", {})
                                  .get("max_posiciones_abiertas_misma_direccion", 2)):
                            _log(f"  ⛔ techo de correlación ({direction}) alcanzado -- no se ejecuta")
                        elif bloquear_por_circuit_breaker(
                                lambda motivo: _log(f"  ⛔ circuit breaker activo ({motivo}) -- no se ejecuta")):
                            pass
                        else:
                            ask_lado = ask_ref
                            if ask_lado in (None, "") or stake_dryrun in (None, "") or not (float(stake_dryrun or 0) > 0):
                                _log("  ⛔ precio/stake sin resolver -- fail-closed, no se ejecuta")
                            else:
                                # /code-review 06-Ago: `ask_lado` es el ask del
                                # token del propio `mirror_lado` (consultado
                                # directamente vía _token_para_lado), pero
                                # _ejecutar_orden_polymarket espera SIEMPRE
                                # entry_price en perspectiva YES (hace
                                # 1-entry_price internamente para BUY_NO) --
                                # pasar el ask del lado NO tal cual lo invertía
                                # DOS veces. Convertir aquí antes de llamar.
                                ask_lado_f = float(ask_lado)
                                precio_orden_yes = ask_lado_f if direction == "BUY_YES" else round(1.0 - ask_lado_f, 6)
                                # /code-review 06-Ago: sin edge_dir,
                                # _ejecutar_orden_polymarket se salta el
                                # re-quote/abort si el edge se evaporó entre
                                # detección y decisión (_decidir_requote) --
                                # el mismo guardián que exige el resto de
                                # ejecutores live (CLAUDE.md: "aborta si
                                # edge<0.02"). info["edge_pp"] ya es el edge
                                # validado A FAVOR de esta dirección (solo
                                # SEGUIR llega aquí, edge_pp>0 por construcción).
                                edge_dir = info["edge_pp"] / 100.0
                                resultado = lt._ejecutar_orden_polymarket(
                                    market_id, direction, float(stake_dryrun), precio_orden_yes,
                                    edge_dir=edge_dir,
                                    contexto={"strategy": "WALLET_MIRROR", "subtype": f"{activo}#{marco}",
                                              # 25-Ago: tupla_sintetica + jugada_grande añadidos --
                                              # el re-chequeo post-requote de _ejecutar_orden_polymarket
                                              # los necesita para consultar wallet_mirror_gate_bucket.py
                                              # (el gate PROPIO) en vez de cualquier fuente distinta.
                                              "tupla_sintetica": tupla_sintetica,
                                              "jugada_grande": bool(ratio_size is not None and ratio_size >= 2.0)})
                                _log(f"  🚨 ORDEN REAL enviada ({tupla_sintetica}): {resultado}")
                                # 11-Ago: cablear ledger+Telegram en el
                                # camino de éxito -- ANTES de este fix, un
                                # fill real no habría quedado registrado en
                                # trades.csv ni habría avisado por Telegram
                                # (mismo hallazgo/hueco que ballenas_executor_
                                # 5min.py tuvo hasta el 28-Jul).
                                if not resultado.get("no_fill"):
                                    trade = {
                                        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                        "market_id": market_id, "question": "", "end_date": end_date_real,
                                        "strategy": "WALLET_MIRROR", "subtype": f"{activo}#{marco}",
                                        "direction": direction,
                                        "stake_eur": float(stake_dryrun) if resultado.get("ok") else 0.0,
                                        "entry_price": resultado.get("entry_price", ""),
                                        "signal_ask": round(ask_lado_f, 4),
                                        "slip_real": resultado.get("slip_real", ""),
                                        "ic_modelo": round(ic_proxy, 4) if "ic_proxy" in locals() else "",
                                        "edge_neto": round(edge_dir, 4),
                                        "conviction_score": round(info["edge_pp"] / 100.0, 4),
                                        "kelly_recomendado": stake_dryrun,
                                        "status": "OPEN" if resultado.get("ok") else "ERROR",
                                        "close_timestamp": "", "exit_price": "", "outcome_real": "",
                                        "fee_eur": resultado.get("fee_eur", 0),
                                        "pnl_bruto_eur": "", "pnl_neto_eur": "",
                                        # 24-Ago: "grande=" añadido a notas -- el kill-switch de
                                        # micro-bucket de WALLET_MIRROR (vigia_micro_bucket_kill_
                                        # switch_wallet_mirror.py) necesita jugada_grande para
                                        # reconstruir la MISMA clave que usó wmgb.evaluar() al
                                        # decidir (tipo#activo#marco#grande#bucket), y trades.csv no
                                        # tenía columna propia para ese dato.
                                        "notas": (f"wallet_mirror wallet={w} tipo={info['tipo']} "
                                                  f"grande={int(ratio_size is not None and ratio_size >= 2.0)}"
                                                  if resultado.get("ok") else resultado.get("error", "")),
                                    }
                                    lt._registrar_trade(trade)
                                    if resultado.get("ok"):
                                        lt.enviar_telegram(
                                            f"🎯 *Orden live ejecutada (WALLET_MIRROR)*\n"
                                            f"Tupla: {tupla_sintetica}\n"
                                            f"Wallet copiada: {w} (tipo {info['tipo']})\n"
                                            f"Precio fill: {resultado['entry_price']:.4f} "
                                            f"(slip {resultado.get('slip_real', 0):+.4f})\n"
                                            f"Stake: {float(stake_dryrun):.2f}€\n"
                                            f"Bankroll operativo: {lt.bankroll_actual():.2f}$ (real al cierre de ciclo)"
                                        )
                                    else:
                                        lt.enviar_telegram(
                                            f"❌ *Orden live ERROR (WALLET_MIRROR)*\n"
                                            f"{tupla_sintetica}\n"
                                            f"{str(resultado.get('error', ''))[:200]}"
                                        )
                if n_matches % 20 == 0:
                    _vistos_guardar(vistos)
                    _log(f"resumen: {n_matches} matches SEGUIR-fillable, "
                         f"{n_fillable_decision} siguen fillable en decisión "
                         f"({n_fillable_decision/n_matches*100:.1f}%)")
        finally:
            ping_task.cancel()
    return vistos


async def main() -> None:
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    # 13-Ago: wallets_operativas_recientes(), NO cargar_wallets_validadas() --
    # este proceso toca dinero real (DRY_RUN=False), exige además rendimiento
    # reciente no degradado, ver wallet_mirror_tracker.py.
    # 24-Ago: asyncio.to_thread() -- desde que _historial_reciente_wallet_
    # mirror() también lee ballenas_timing_history.csv (1.8M filas, ~25-30s
    # de parseo), una llamada síncrona aquí congelaría el event loop entero
    # (ping/websocket/detección de trades) durante ese tiempo, cada 30min.
    # En un hilo aparte, el loop sigue respondiendo mientras se recalcula.
    wallets = await asyncio.to_thread(wallets_operativas_recientes)
    ultimo_refresco = datetime.now(timezone.utc).timestamp()
    vistos = _vistos_cargar()
    _log(f"wallet_mirror_executor_dryrun arrancado -- {len(wallets)} wallets validadas, DRY_RUN={DRY_RUN}")
    while True:
        try:
            ahora_ts = datetime.now(timezone.utc).timestamp()
            if ahora_ts - ultimo_refresco > REFRESCO_WALLETS_S:
                wallets = await asyncio.to_thread(wallets_operativas_recientes)
                ultimo_refresco = ahora_ts
            vistos = await _correr_una_conexion(wallets, vistos)
        except (websockets.exceptions.ConnectionClosed, OSError, asyncio.TimeoutError) as e:
            _log(f"Conexión perdida ({type(e).__name__}: {e}) — reintentando en {RECONNECT_ESPERA_S}s")
        except Exception as e:
            _log(f"Error inesperado ({type(e).__name__}: {e}) — reintentando en {RECONNECT_ESPERA_S}s")
        _vistos_guardar(vistos)
        await asyncio.sleep(RECONNECT_ESPERA_S)


if __name__ == "__main__":
    asyncio.run(main())
