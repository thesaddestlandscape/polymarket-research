"""
fetch_polybolt_prices.py -- captura continua de PolyBolt (websocket nuevo de
Polymarket, 15-Sep-2026), solo lectura.

Motivo (24-Sep, aviso del vigía de actualizaciones + petición Javi):
- `price.crypto.twap` (ventana 60 s) es el precio de REFERENCIA con el que se
  resuelven los mercados up/down de cripto desde el cambio TWAP (07/14-Ago).
  Hasta hoy lo reconstruíamos a mano desde el feed spot de Chainlink; aquí
  llega el número oficial en tiempo real (1 punto/s por moneda) -- base para
  precierre/resolution sniper (dirección de resolución casi fijada a T-2s).
- RTDS pasa a "legacy" para precios: `crypto_prices_chainlink` (lo que usa
  fetch_chainlink_prices.py) se retirará "un mes después del SDK 0.11.0",
  sin fecha fija. `price.crypto` es su sustituto -- se captura en paralelo
  para poder migrar sin hueco. El topic `activity` sigue en RTDS (docs:
  "It has no PolyBolt channel"), el firehose no se toca.

Docs: https://docs.polymarket.com/api-reference/wss/polybolt
Auth con credenciales CLOB (data/live/.env). Solo suscripción, nunca opera.

Salida: data/prices/polybolt_YYYY-MM-DD.csv (gitignorado, ~70 MB/día),
columnas timestamp_utc,asset,canal,value,event_ts_ms,snapshot
  canal = spot (price.crypto) | twap60 (price.crypto.twap, window 60)
  snapshot = 1 para los puntos del snapshot de 2 min tras (re)suscribir
             (duplican lo ya capturado; deduplicar por asset,canal,event_ts_ms)

Corre como hilo dentro de fetchers_fase0.py (screen `fetchers`).
"""

import asyncio
import csv
import json
import random
import time
from datetime import datetime, timezone
from pathlib import Path

import websockets
from dotenv import dotenv_values

REPO = Path(__file__).resolve().parent
DIR_PRICES = REPO / "data" / "prices"
ENV = REPO / "data" / "live" / ".env"

WS_URL = "wss://ws-live-v2.polymarket.com/ws"
SIMBOLOS = ["btcusd", "ethusd", "solusd", "xrpusd", "dogeusd", "bnbusd"]
CANALES = {"price.crypto": "spot", "price.crypto.twap": "twap60"}
# 24-Sep, failover de Chainlink (Javi: "no correr ni un riesgo"): RTDS
# `crypto_prices_chainlink` se retirará sin fecha fija y ~20 consumidores leen
# data/prices/chainlink_YYYY-MM-DD.csv. Si fetch_chainlink_prices.py (mismo
# proceso fetchers_fase0.py) lleva > FALLBACK_TRAS_S sin tick RTDS, este hilo
# escribe su spot `price.crypto` (sucesor oficial de ese topic, docs de
# migración) en ESE MISMO CSV con source=polybolt_fallback, y avisa por
# Telegram al entrar y al salir. Solo se activa si fetchers_fase0 lo habilita
# (FALLBACK_CHAINLINK=True), nunca al ejecutar este módulo suelto.
FALLBACK_CHAINLINK = False
FALLBACK_TRAS_S = 20
_T_ARRANQUE = time.time()
_en_fallback = False
RECV_TIMEOUT_S = 30          # mismo criterio que fetch_chainlink_prices.py (cuelgue silencioso 28-Jul)
RECONNECT_ESPERA_S = 5
ESPERA_FALLO_DURO_S = 300    # 4001 auth / 4008 policy: docs "do not blindly reconnect"


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _asset(symbol) -> str | None:
    if symbol in SIMBOLOS:
        return symbol[:-3].upper()
    return None


def _escribir(filas: list) -> None:
    """Abre-escribe-cierra por mensaje (ver _escribir_tick de
    fetch_chainlink_prices.py: un handle abierto puede quedar escribiendo en
    un inodo huérfano si otro proceso reemplaza el fichero)."""
    if not filas:
        return
    archivo = DIR_PRICES / f"polybolt_{datetime.now(timezone.utc):%Y-%m-%d}.csv"
    with open(archivo, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if f.tell() == 0:
            w.writerow(["timestamp_utc", "asset", "canal", "value", "event_ts_ms", "snapshot"])
        w.writerows(filas)


def _filas_de(msg: dict) -> list:
    canal = CANALES.get(msg.get("channel"))
    payload = msg.get("payload")
    if not canal or not isinstance(payload, dict):
        return []
    ahora = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
    snap = 1 if msg.get("snapshot") else 0
    puntos = payload.get("data") if snap and isinstance(payload.get("data"), list) else [payload]
    filas = []
    for p in puntos:
        asset = _asset(p.get("symbol") or payload.get("symbol"))
        if not asset:
            continue
        v = p.get("full_accuracy_value") or p.get("value")
        try:
            v = float(v)
        except (TypeError, ValueError):
            continue
        filas.append([ahora, asset, canal, v, p.get("timestamp"), snap])
    return filas


def _avisar(texto: str) -> None:
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram(texto)
    except Exception as e:
        _log(f"(no se pudo avisar por Telegram: {e})")


def _failover_chainlink(filas: list) -> None:
    global _en_fallback
    import fetch_chainlink_prices as fcp
    ultimo = fcp.ULTIMO_TICK_RTDS_TS or _T_ARRANQUE
    callado = time.time() - ultimo
    if callado > FALLBACK_TRAS_S:
        if not _en_fallback:
            _en_fallback = True
            _log(f"🚨 FAILOVER: RTDS Chainlink sin ticks {callado:.0f}s -- escribiendo PolyBolt en chainlink_*.csv")
            _avisar(f"🚨 Chainlink RTDS sin ticks {callado:.0f}s: FAILOVER a PolyBolt activo "
                    f"(chainlink_*.csv sigue alimentado, source=polybolt_fallback). Revisar RTDS.")
        for _, asset, canal, v, ev_ts, _snap in filas:
            if canal == "spot":
                fcp._escribir_tick(asset, v, ev_ts, source="polybolt_fallback")
    elif _en_fallback:
        _en_fallback = False
        _log("✅ RTDS Chainlink ha vuelto -- failover desactivado")
        _avisar("✅ Chainlink RTDS ha vuelto: failover PolyBolt desactivado.")


class _FalloDuro(Exception):
    pass


async def _correr_una_conexion(cred: dict) -> None:
    async with websockets.connect(WS_URL, open_timeout=10, close_timeout=5,
                                  ping_interval=None) as ws:  # el servidor hace ping cada 25 s; la lib responde pong sola
        await ws.send(json.dumps({"op": "auth", "rid": "a1", "auth": cred}))
        resp = json.loads(await asyncio.wait_for(ws.recv(), timeout=10))
        if resp.get("op") != "authed":
            raise _FalloDuro(f"auth rechazada: {str(resp)[:200]}")
        subs = [{"channel": "price.crypto", "filter": {"symbol": s}} for s in SIMBOLOS]
        subs += [{"channel": "price.crypto.twap", "filter": {"symbol": s, "window_seconds": 60}}
                 for s in SIMBOLOS]
        await ws.send(json.dumps({"op": "subscribe", "rid": "s1", "subscriptions": subs}))
        _log(f"Conectado a {WS_URL}, suscrito a {len(subs)} (canal,símbolo)")
        n = 0
        while True:
            raw = await asyncio.wait_for(ws.recv(), timeout=RECV_TIMEOUT_S)
            try:
                msg = json.loads(raw)
            except (json.JSONDecodeError, TypeError):
                continue
            if msg.get("op") == "error":
                _log(f"error del servidor: {str(msg)[:300]}")
                continue
            if msg.get("dropped"):
                _log(f"⚠️ el servidor reporta {msg['dropped']} frames perdidos en {msg.get('channel')}")
            filas = _filas_de(msg)
            _escribir(filas)
            if FALLBACK_CHAINLINK and filas and not filas[0][5]:
                _failover_chainlink(filas)
            n += 1
            if n % 5000 == 0:
                _log(f"{n} mensajes en esta conexión")


async def main() -> None:
    DIR_PRICES.mkdir(parents=True, exist_ok=True)
    while True:
        espera = RECONNECT_ESPERA_S
        try:
            e = dotenv_values(ENV)
            cred = {"apiKey": e.get("POLY_API_KEY"), "secret": e.get("POLY_API_SECRET"),
                    "passphrase": e.get("POLY_API_PASSPHRASE")}
            if not all(cred.values()):
                raise _FalloDuro("faltan credenciales CLOB en data/live/.env")
            await _correr_una_conexion(cred)
        except _FalloDuro as ex:
            _log(f"🚨 {ex} -- reintento en {ESPERA_FALLO_DURO_S}s")
            espera = ESPERA_FALLO_DURO_S
        except websockets.exceptions.ConnectionClosed as ex:
            code = getattr(ex.rcvd, "code", None) if getattr(ex, "rcvd", None) else None
            if code in (4001, 4008):
                _log(f"🚨 cierre {code} (auth/policy) -- no se reconecta a ciegas, espera {ESPERA_FALLO_DURO_S}s")
                espera = ESPERA_FALLO_DURO_S
            elif code == 4003:
                espera = random.uniform(0, 10)  # server draining: docs piden 0-10 s uniforme
                _log(f"cierre 4003 (server draining) -- reconexión en {espera:.1f}s")
            else:
                _log(f"Conexión cerrada ({code}: {ex}) -- reintentando en {espera}s")
        except (OSError, asyncio.TimeoutError) as ex:
            _log(f"Conexión perdida ({type(ex).__name__}: {ex}) -- reintentando en {espera}s")
        except Exception as ex:
            _log(f"Error inesperado ({type(ex).__name__}: {ex}) -- reintentando en {espera}s")
        await asyncio.sleep(espera)


if __name__ == "__main__":
    asyncio.run(main())
