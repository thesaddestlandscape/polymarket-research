#!/usr/bin/env python3
"""
fetch_bybit_liquidations.py — Captura continua del stream público de
liquidaciones de Bybit Futures (wss://stream.bybit.com/v5/public/linear,
topic `allLiquidation.{symbol}`, sin autenticación, sin API key). Solo
lectura. SUSTITUYE a fetch_binance_liquidations.py (30-Jul, petición
explícita Javi).

Origen del reemplazo (30-Jul): diagnóstico completo confirmó que
`wss://fstream.binance.com` (el dominio de futuros USDⓈ-M de Binance) está
bloqueado/throttled a nivel de datos específicamente para esta IP de
datacenter (Hetzner Helsinki) -- handshake WS se acepta pero CERO mensajes
fluyen, incluso en el stream de mayor volumen del mercado entero
(!forceOrder@arr, aggTrade). Verificado con pruebas aisladas: REST de
Binance SÍ funciona, spot WS de Binance SÍ funciona, solo el dominio
fstream específicamente no. Ver memoria idea_binance_liquidaciones_
bloqueadas_ip_29jul (detalle completo del diagnóstico).

Por qué Bybit y no Coinbase ni un agregador de pago (evaluado en la misma
sesión): Coinbase (Advanced Trade / Exchange) es spot puro -- no existe el
concepto de liquidación ahí (sin apalancamiento). Coinbase International
Exchange sí tiene perpetuos pero es un mercado institucional/gateado, sin
evidencia de un canal público de liquidaciones documentado ni volumen
comparable. Coinglass (agregador especializado, "el más rápido" del
mercado) tiene el dato pero el WebSocket en tiempo real es de pago desde
$35/mes -- coste recurrente injustificado hoy: la familia LIQUIDACIONES_
5M/15M/60M todavía no tiene NINGUNA evidencia de generar edge real (0
datos hasta este bloqueo). Bybit es el 2º/3er mercado de futuros por
volumen mundial (después de Binance), con un stream público de
liquidaciones de mercado completo, gratis, sin auth, y VERIFICADO
funcionando sin bloqueo desde este VPS (handshake + suscripción + ack
confirmados en pruebas aisladas 30-Jul) -- mismo criterio que el resto del
proyecto: preferir la fuente gratis de un exchange de primera mano sobre
un agregador de pago (mismo patrón que fetch_polymarket_activity_ws.py
replicando gratis lo que un agregador de terceros cobra).

Diferencias de protocolo vs Binance (mismo comportamiento agregado, API
distinta):
- Requiere handshake de suscripción explícito tras conectar
  ({"op":"subscribe","args":["allLiquidation.BTCUSDT", ...]}), Binance
  codificaba el stream en la URL.
- Bybit exige un ping de aplicación periódico (no solo ping de protocolo
  WS) para no ser desconectado por inactividad -- ver `_mantener_ping`.
- El campo de lado es "S":"Sell"/"Buy" en vez de "S":"SELL"/"BUY", y
  "Sell" = se liquidó una posición LARGA (mismo significado que Binance,
  distinta cadena exacta) -- verificado contra la documentación oficial
  (bybit-exchange.github.io/docs/v5/websocket/public/all-liquidation).
- Cada mensaje trae una LISTA de eventos en "data" (Binance mandaba uno
  por mensaje) -- puede agrupar varias liquidaciones simultáneas.
- No hay campo de precio promedio de ejecución ("ap"), solo precio de
  bancarrota ("p") -- aproximación razonable al valor nocional real
  (usd = v * p), mismo nivel de precisión que Binance usaba (ap≈p en la
  gran mayoría de liquidaciones FILLED).

Mantiene en memoria una ventana rodante de liquidaciones recientes (hasta
LOOKBACK_MAX_MIN) por activo, y escribe cada ~10s un JSON agregado con
totales long/short en varias ventanas (2/5/15/60min) -- MISMO formato de
salida que fetch_binance_liquidations.py (solo cambia el nombre de
fichero, ver STATE_PATH) para no tener que tocar los consumidores
(shadow_predict.py::LIQUIDACIONES_5M/15M/60M ya apunta al nuevo path).

Salida: data/shadow/liquidaciones_bybit_state.json (sobrescrito, no CSV).
Puramente shadow/observacional, NO toca dinero ni ninguna decisión
directamente.

Corre en screen propia (reemplaza a la screen `liqs` que corría
fetch_binance_liquidations.py):
  screen -dmS liqs bash -c "cd /root/polymarket-research && .venv/bin/python fetch_bybit_liquidations.py >> logs/bybit_liquidations.log 2>&1"
"""

import json
import time
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

import asyncio
import websockets

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
STATE_PATH = DIR_SHADOW / "liquidaciones_bybit_state.json"

WS_URL = "wss://stream.bybit.com/v5/public/linear"
RECONNECT_ESPERA_S = 5
RECV_TIMEOUT_S = 30  # mismo fix de timeout ya aplicado a chainlink/polyactivity/binance
APP_PING_INTERVAL_S = 20  # Bybit documenta desconexión por inactividad sin ping de aplicación
ESCRITURA_INTERVALO_S = 10
LOOKBACK_MAX_MIN = 65  # cubre la ventana más larga (60min) con margen

ACTIVOS_TRACKEADOS = {"BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"}
VENTANAS_MIN = [2, 5, 15, 60]


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


# {activo: deque[(epoch_s, lado, usd)]}  lado: "long" (se liquidó un long -> venta forzada) / "short"
_eventos: dict[str, deque] = {a: deque() for a in ACTIVOS_TRACKEADOS}


def _symbol_a_activo(symbol: str) -> str | None:
    for a in ACTIVOS_TRACKEADOS:
        if symbol == f"{a}USDT":
            return a
    return None


def _procesar_evento(ev: dict) -> None:
    """Un elemento de la lista "data" de un mensaje allLiquidation.*
    -- ver docstring del fichero para el schema completo."""
    symbol = ev.get("s", "")
    activo = _symbol_a_activo(symbol)
    if not activo:
        return
    # S="Sell" = se liquidó una posición LARGA (venta forzada); S="Buy" =
    # se liquidó una CORTA (compra forzada) -- mismo significado que
    # Binance forceOrder, cadena distinta ("Sell"/"Buy" vs "SELL"/"BUY").
    side = ev.get("S", "")
    lado = "long" if side == "Sell" else ("short" if side == "Buy" else None)
    if lado is None:
        return
    try:
        precio = float(ev.get("p") or 0)
        cantidad = float(ev.get("v") or 0)
    except (TypeError, ValueError):
        return
    usd = precio * cantidad
    if usd <= 0:
        return
    ahora = time.time()
    _eventos[activo].append((ahora, lado, usd))
    _purgar(activo, ahora)


def _purgar(activo: str, ahora: float) -> None:
    limite = ahora - LOOKBACK_MAX_MIN * 60
    dq = _eventos[activo]
    while dq and dq[0][0] < limite:
        dq.popleft()


def _agregar_estado() -> dict:
    ahora = time.time()
    estado = {"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "fuente": "bybit"}
    for activo in sorted(ACTIVOS_TRACKEADOS):
        _purgar(activo, ahora)
        dq = _eventos[activo]
        por_ventana = {}
        for vmin in VENTANAS_MIN:
            limite = ahora - vmin * 60
            usd_long = usd_short = 0.0
            n = 0
            for ts, lado, usd in dq:
                if ts < limite:
                    continue
                n += 1
                if lado == "long":
                    usd_long += usd
                else:
                    usd_short += usd
            total = usd_long + usd_short
            # imbalance > 0 => dominan liquidaciones LONG (venta forzada,
            # sesgo bajista) -- mismo signo que delta_ratio de ORDER_FLOW_5M.
            imbalance = round((usd_short - usd_long) / total, 4) if total > 0 else None
            por_ventana[f"{vmin}min"] = {
                "usd_long": round(usd_long, 2),
                "usd_short": round(usd_short, 2),
                "n": n,
                "imbalance": imbalance,
            }
        estado[activo] = por_ventana
    return estado


def _escribir_estado() -> None:
    estado = _agregar_estado()
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(estado, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(STATE_PATH)


async def _mantener_ping(ws):
    """Bybit documenta desconexión por inactividad sin un ping de
    APLICACIÓN periódico -- distinto del ping de protocolo WS que
    Binance/Polymarket aceptaban implícitamente."""
    try:
        while True:
            await asyncio.sleep(APP_PING_INTERVAL_S)
            await ws.send(json.dumps({"op": "ping"}))
    except (asyncio.CancelledError, websockets.exceptions.ConnectionClosed):
        pass


async def _correr_una_conexion() -> None:
    async with websockets.connect(WS_URL, open_timeout=10, close_timeout=5) as ws:
        args = [f"allLiquidation.{a}USDT" for a in sorted(ACTIVOS_TRACKEADOS)]
        await ws.send(json.dumps({"op": "subscribe", "args": args}))
        _log(f"Conectado a {WS_URL}, suscrito a {args}")
        ping_task = asyncio.create_task(_mantener_ping(ws))
        n_total = 0
        try:
            while True:
                # Mismo fix de timeout ya aplicado a chainlink/polyactivity/
                # binance_liquidations -- sin esto, una conexión muerta en
                # silencio deja el bucle bloqueado para siempre.
                raw = await asyncio.wait_for(ws.recv(), timeout=RECV_TIMEOUT_S)
                try:
                    msg = json.loads(raw)
                except (json.JSONDecodeError, TypeError):
                    continue
                if msg.get("op") in ("subscribe", "pong", "ping"):
                    continue  # acks de control, no eventos de mercado
                if not str(msg.get("topic", "")).startswith("allLiquidation."):
                    continue
                for ev in msg.get("data") or []:
                    _procesar_evento(ev)
                    n_total += 1
                if n_total and n_total % 20 == 0:
                    _log(f"{n_total} liquidaciones vistas en esta conexión")
        finally:
            ping_task.cancel()


async def main() -> None:
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    escritor = asyncio.create_task(_escritor_periodico())
    try:
        while True:
            try:
                await _correr_una_conexion()
            except (websockets.exceptions.ConnectionClosed, OSError, asyncio.TimeoutError) as e:
                _log(f"Conexión perdida ({type(e).__name__}: {e}) — reintentando en {RECONNECT_ESPERA_S}s")
            except Exception as e:
                _log(f"Error inesperado ({type(e).__name__}: {e}) — reintentando en {RECONNECT_ESPERA_S}s")
            await asyncio.sleep(RECONNECT_ESPERA_S)
    finally:
        escritor.cancel()


async def _escritor_periodico():
    while True:
        await asyncio.sleep(ESCRITURA_INTERVALO_S)
        try:
            _escribir_estado()
        except Exception as e:
            _log(f"Error escribiendo estado: {type(e).__name__}: {e}")


if __name__ == "__main__":
    asyncio.run(main())
