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
    cargar_wallets_validadas, _opuesto, _fillability_mirror, _market_id_y_direccion,
)
from fetch_polymarket_activity_ws import _parse_updown  # noqa: E402
import live_trade as lt  # noqa: E402
from live_guard import puede_operar_live  # noqa: E402
from live_stake import calcular_stake  # noqa: E402

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

DRY_RUN = True  # NO CAMBIAR sin /code-review + aprobación explícita Javi
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


def _vistos_cargar() -> set:
    try:
        return set(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return set()


def _vistos_guardar(vistos: set) -> None:
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


async def _correr_una_conexion(wallets: dict, vistos: set) -> set:
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
                dedup_key = f"{w}|{market_slug}"
                if dedup_key in vistos:
                    continue
                vistos.add(dedup_key)

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

                fill_decision = _fillability_mirror(market_slug, mirror_lado, precio)
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
                        else:
                            market_id, direction = resuelto
                            precio_orden = ask_2 if ask_2 not in (None, "") else ask_d
                            if precio_orden in (None, "") or stake_dryrun in (None, ""):
                                _log("  ⛔ precio/stake sin resolver -- fail-closed, no se ejecuta")
                            else:
                                resultado = lt._ejecutar_orden_polymarket(
                                    market_id, direction, float(stake_dryrun), float(precio_orden),
                                    contexto={"strategy": "WALLET_MIRROR", "subtype": f"{activo}#{marco}"})
                                _log(f"  🚨 ORDEN REAL enviada ({tupla_sintetica}): {resultado}")
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
    wallets = cargar_wallets_validadas()
    ultimo_refresco = datetime.now(timezone.utc).timestamp()
    vistos = _vistos_cargar()
    _log(f"wallet_mirror_executor_dryrun arrancado -- {len(wallets)} wallets validadas, DRY_RUN={DRY_RUN}")
    while True:
        try:
            ahora_ts = datetime.now(timezone.utc).timestamp()
            if ahora_ts - ultimo_refresco > REFRESCO_WALLETS_S:
                wallets = cargar_wallets_validadas()
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
