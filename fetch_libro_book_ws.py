#!/usr/bin/env python3
"""
fetch_libro_book_ws.py — Captura continua, PUSH (no polling), del libro
real de Polymarket vía el websocket público y oficial del CLOB
(wss://ws-subscriptions-clob.polymarket.com/ws/market — distinto del RTDS
interno que ya usan fetch_chainlink_prices.py/fetch_polymarket_activity_ws.py).
Solo lectura, no toca dinero ni ninguna decisión.

Origen (01-Sep, CLAUDE.md pt.21b, propuesta #1 de "edge NO capturado" —
footprint pre-trade de wallets informadas): un fork de verificación marcó
esta idea "no factible" asumiendo que había que sondear el libro entero
cada 1-2s (coste de CPU/red no trivial con el sistema ya cargado). Javi
objetó ("hemos ampliado cores/ram/cpu, puede hacerse de alguna forma") —
al investigar se encontró que el fork solo conocía 2 de 3 fuentes: este
canal del CLOB no estaba usado en el repo hasta hoy y es PUSH (empuja un
snapshot inicial del libro + eventos `price_changes` incrementales con
best_bid/best_ask/size/side en tiempo real, sub-segundo, verificado en
vivo con un token real de BTC#5min) — mucho más barato que un poller: el
proceso está inactivo hasta que hay un cambio real, sin round-trip HTTP
repetido. Ver memoria idea_3_propuestas_edge_no_capturado_verificadas_01sep
(sección #1, corregida) para el detalle completo de la verificación.

Alcance deliberadamente ACOTADO (no todo el histórico, no todos los
mercados posibles): solo el universo activo AHORA MISMO de 6
monedas×{5,15,60}min (misma fuente que fetch_libro_ambos_lados.py,
`_universo_activo()` sobre data/markets/HOY.csv), y solo el token YES de
cada mercado (el NO es complementario, basta un lado para detectar
movimiento anómalo de libro). Esto mantiene el nº de asset_ids por
conexión pequeño (~12-18 mercados vivos a la vez, no cientos), coherente
con el hallazgo de esta misma sesión de que el VPS está con la memoria
muy ajustada (swap-in activo) — no se justifica ampliar el alcance sin
medir primero el coste real de esto en producción.

El canal no se probó para actualizar la suscripción en caliente (añadir/
quitar assets sin reconectar) — para no arriesgar perder mensajes con un
protocolo no verificado, este script simplemente RECONECTA cada
REFRESCO_UNIVERSO_S con la lista de tokens recalculada. Barato: el propio
snapshot inicial que manda el servidor al reconectar ya es información
útil (estado del libro en ese instante).

Salida: data/shadow/libro_book_ws_YYYY-MM-DD.csv (fuera del repo, en
DIR_DATALOGS — mismo patrón que polymarket_activity_*.csv, para no repetir
el incidente de HOY mismo con predictions_2026-09-01.csv >100MB bloqueando
GitHub). Este script SOLO captura; el cruce contra el timestamp real del
trade de una wallet (ya capturado por fetch_polymarket_activity_ws.py) es
un análisis posterior, pendiente de construir en otra sesión.

Pensado para correr como hilo async dentro de fetchers_fase0.py (mismo
patrón que los otros 5 fetchers ya consolidados ahí) — NO screen propia,
para no añadir un proceso persistente nuevo mientras el VPS está cargado.
Si se corre standalone (deploy inicial / debug), usar:
  screen -dmS libroBookWs bash -c "cd /root/polymarket-research && nice -n 10 .venv/bin/python fetch_libro_book_ws.py >> logs/libro_book_ws.log 2>&1"
"""

import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import asyncio
import websockets

sys.path.insert(0, str(Path(__file__).resolve().parent))
import live_trade as lt  # noqa: E402  -- solo lectura: _get_token_ids
from fetch_libro_ambos_lados import _universo_activo  # noqa: E402  -- solo lectura

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
DIR_DATALOGS = Path("/root/polymarket-research-datalogs")
DIR_DATALOGS.mkdir(parents=True, exist_ok=True)

WS_URL = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
REFRESCO_UNIVERSO_S = 90.0  # cada cuánto se recalcula el universo activo y se reconecta
PING_INTERVAL_S = 10
RECONNECT_ESPERA_S = 5
RECV_TIMEOUT_S = 30  # mismo bug ya cazado en chainlink/polyactivity 28/29-Jul --
# sin timeout, una conexión muerta en silencio (sin frame de cierre) deja el
# bucle bloqueado para siempre sin lanzar excepción que main() pueda capturar.

# 01-Sep, corrección tras probar EN VIVO el diseño original (loguear cada
# price_change crudo, 1 fila por evento): con 171 tokens suscritos a la vez
# (universo activo real) llegaron ~1.450 eventos/s -- a ese ritmo, ~34GB/día,
# EL MISMO incidente que se acaba de arreglar hoy mismo con
# predictions_2026-09-01.csv (>200MB bloqueando GitHub), solo que aquí fuera
# de git. Rediseñado a AGREGACIÓN por ventana: en vez de 1 fila por evento,
# 1 fila-resumen por (market, ventana de FLUSH_INTERVALO_S) -- acota el
# volumen a un techo fijo independiente de cuánto churn tenga el libro,
# preservando la señal que de verdad importa para "footprint pre-trade"
# (¿hubo movimiento/churn anómalo en los últimos N segundos?), no el replay
# tick-a-tick.
FLUSH_INTERVALO_S = 20.0  # 01-Sep: medido en vivo, ~158MB/día a 10s -- el
# disco raíz está al 92%/6.2GB libres (presión orgánica ya existente, no
# causada por este script -- ver hallazgo en la sesión), 20s reduce el
# volumen a la mitad manteniendo resolución suficiente para detectar
# churn anómalo pre-trade.

COLUMNS = [
    "timestamp_utc", "market", "asset_id", "activo", "marco", "market_id",
    "n_price_changes", "price_min", "price_max", "size_sum",
    "best_bid_ultimo", "best_ask_ultimo", "best_bid_inicio", "best_ask_inicio",
]


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _archivo_hoy() -> Path:
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return DIR_DATALOGS / f"libro_book_ws_{fecha}.csv"


def _escribir_filas(filas: list) -> None:
    if not filas:
        return
    archivo = _archivo_hoy()
    nuevo = not archivo.exists()
    with open(archivo, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        if nuevo:
            w.writeheader()
        for fila in filas:
            w.writerow(fila)


def _tokens_activos() -> dict:
    """{asset_id: (market_id, activo, marco, lado)} del universo activo AHORA
    (misma fuente que fetch_libro_ambos_lados.py, cacheada 15s ahí). Incluye
    AMBOS lados (YES y NO) -- el canal de mercado del CLOB manda price_changes
    de los dos tokens del mismo "market" aunque solo te suscribas a uno, así
    que sin esto la mitad de las filas quedaban con activo/marco vacíos."""
    universo = _universo_activo()
    tokens = {}
    for mid, (activo, marco, _cid, _edt) in universo.items():
        try:
            yes_token, no_token, _cid_real = lt._get_token_ids(mid)
        except Exception:
            continue
        if yes_token:
            tokens[yes_token] = (mid, activo, marco, "YES")
        if no_token:
            tokens[no_token] = (mid, activo, marco, "NO")
    return tokens


async def _mantener_ping(ws):
    try:
        while True:
            await asyncio.sleep(PING_INTERVAL_S)
            await ws.send("PING")
    except (asyncio.CancelledError, websockets.exceptions.ConnectionClosed):
        pass


def _flush_agregados(agregados: dict, tokens: dict) -> int:
    """Vuelca a CSV una fila-resumen por asset_id con actividad en la ventana
    (min/max/último de precio y libro, nº de eventos, size acumulado) y
    limpia el acumulador. Devuelve nº de filas escritas."""
    if not agregados:
        return 0
    ahora_iso = datetime.now(timezone.utc).isoformat(timespec="seconds")
    filas = []
    for asset_id, ag in agregados.items():
        info = tokens.get(asset_id)
        filas.append({
            "timestamp_utc": ahora_iso,
            "market": ag["market"],
            "asset_id": asset_id,
            "activo": info[1] if info else "",
            "marco": info[2] if info else "",
            "market_id": info[0] if info else "",
            "n_price_changes": ag["n"],
            "price_min": ag["price_min"] if ag["price_min"] is not None else "",
            "price_max": ag["price_max"] if ag["price_max"] is not None else "",
            "size_sum": round(ag["size_sum"], 4),
            "best_bid_ultimo": ag["best_bid_ultimo"] if ag["best_bid_ultimo"] is not None else "",
            "best_ask_ultimo": ag["best_ask_ultimo"] if ag["best_ask_ultimo"] is not None else "",
            "best_bid_inicio": ag["best_bid_inicio"] if ag["best_bid_inicio"] is not None else "",
            "best_ask_inicio": ag["best_ask_inicio"] if ag["best_ask_inicio"] is not None else "",
        })
    _escribir_filas(filas)
    return len(filas)


async def _correr_una_conexion() -> None:
    tokens = _tokens_activos()
    if not tokens:
        _log("universo activo vacío (sin mercados abiertos ahora) — reintentando en breve")
        await asyncio.sleep(RECONNECT_ESPERA_S)
        return
    # 01-Sep, fix probado en vivo: suscribirse a los 338 tokens (YES+NO) de
    # golpe hace que NUESTRO propio mensaje de subscribe supere el límite de
    # frame del servidor (1.048.576 bytes) -- cierra la conexión con 1009
    # "message too big" antes de mandar nada. No hace falta de todas formas:
    # el canal manda price_changes de AMBOS lados del mismo "market" aunque
    # solo suscribas el token YES (visto en la 1ª prueba: llegaban asset_ids
    # no suscritos, resultaron ser el lado NO). `tokens` sigue mapeando
    # ambos lados para poder atribuir activo/marco/market_id correctamente
    # al recibir esas filas del lado NO, solo el envío de suscripción se
    # limita al YES.
    asset_ids = [aid for aid, info in tokens.items() if info[3] == "YES"]

    async with websockets.connect(WS_URL, open_timeout=10, close_timeout=5) as ws:
        sub = {"type": "market", "assets_ids": asset_ids}
        await ws.send(json.dumps(sub))
        n_monedas = len({v[1] for v in tokens.values() if v[1]})
        _log(f"Conectado a {WS_URL}, suscrito a {len(asset_ids)} tokens "
             f"({n_monedas} monedas, universo activo, agregando cada {FLUSH_INTERVALO_S:.0f}s)")
        ping_task = asyncio.create_task(_mantener_ping(ws))
        n_mensajes = n_filas_totales = 0
        t_reconectar = time.time() + REFRESCO_UNIVERSO_S
        t_flush = time.time() + FLUSH_INTERVALO_S
        agregados: dict = {}  # asset_id -> dict de agregación de la ventana actual
        try:
            while time.time() < t_reconectar:
                restante = min(t_reconectar, t_flush) - time.time()
                try:
                    raw = await asyncio.wait_for(ws.recv(), timeout=min(RECV_TIMEOUT_S, max(restante, 0.05)))
                except asyncio.TimeoutError:
                    raw = None

                ahora = time.time()
                if ahora >= t_flush:
                    n_filas_totales += _flush_agregados(agregados, tokens)
                    agregados = {}
                    t_flush = ahora + FLUSH_INTERVALO_S
                if ahora >= t_reconectar:
                    break
                if raw is None or not raw:
                    continue
                try:
                    msg = json.loads(raw)
                except (json.JSONDecodeError, TypeError):
                    continue
                if not isinstance(msg, dict):
                    continue

                # snapshot inicial de libro (dict con "bids"/"asks") o evento
                # incremental (dict con "price_changes": [...]) -- ambos
                # comparten "market"/"asset_id". Solo se acumula en memoria,
                # NUNCA se escribe fila por evento -- ver comentario de
                # FLUSH_INTERVALO_S arriba (evita el ~34GB/día del diseño
                # original probado en vivo).
                if "price_changes" in msg:
                    market = msg.get("market", "")
                    for pc in msg.get("price_changes", []):
                        n_mensajes += 1
                        asset_id = pc.get("asset_id", "")
                        if not asset_id:
                            continue
                        try:
                            price = float(pc.get("price"))
                        except (TypeError, ValueError):
                            price = None
                        try:
                            size = float(pc.get("size") or 0)
                        except (TypeError, ValueError):
                            size = 0.0
                        try:
                            bb = float(pc.get("best_bid"))
                        except (TypeError, ValueError):
                            bb = None
                        try:
                            ba = float(pc.get("best_ask"))
                        except (TypeError, ValueError):
                            ba = None
                        ag = agregados.get(asset_id)
                        if ag is None:
                            ag = agregados[asset_id] = {
                                "market": market, "n": 0, "price_min": None, "price_max": None,
                                "size_sum": 0.0, "best_bid_inicio": bb, "best_ask_inicio": ba,
                                "best_bid_ultimo": bb, "best_ask_ultimo": ba,
                            }
                        ag["n"] += 1
                        ag["size_sum"] += size
                        if price is not None:
                            ag["price_min"] = price if ag["price_min"] is None else min(ag["price_min"], price)
                            ag["price_max"] = price if ag["price_max"] is None else max(ag["price_max"], price)
                        if bb is not None:
                            ag["best_bid_ultimo"] = bb
                        if ba is not None:
                            ag["best_ask_ultimo"] = ba
                elif "asset_id" in msg and ("bids" in msg or "asks" in msg):
                    n_mensajes += 1
                    asset_id = msg.get("asset_id", "")
                    if not asset_id:
                        continue
                    bids = msg.get("bids") or []
                    asks = msg.get("asks") or []
                    bb = max((float(b.get("price", 0)) for b in bids), default=None) if bids else None
                    ba = min((float(a.get("price", 0)) for a in asks), default=None) if asks else None
                    ag = agregados.get(asset_id)
                    if ag is None:
                        ag = agregados[asset_id] = {
                            "market": msg.get("market", ""), "n": 0, "price_min": None, "price_max": None,
                            "size_sum": 0.0, "best_bid_inicio": bb, "best_ask_inicio": ba,
                            "best_bid_ultimo": bb, "best_ask_ultimo": ba,
                        }
                    if bb is not None:
                        ag["best_bid_ultimo"] = bb
                    if ba is not None:
                        ag["best_ask_ultimo"] = ba
                if n_mensajes and n_mensajes % 5000 == 0:
                    _log(f"{n_mensajes} eventos procesados, {n_filas_totales} filas-resumen escritas en esta conexión")
        finally:
            ping_task.cancel()
            n_filas_totales += _flush_agregados(agregados, tokens)  # no perder la ventana parcial al reconectar
        _log(f"reconectando para refrescar universo (última conexión: {n_mensajes} eventos, {n_filas_totales} filas-resumen)")


async def main() -> None:
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    while True:
        try:
            await _correr_una_conexion()
        except (websockets.exceptions.ConnectionClosed, OSError, asyncio.TimeoutError) as e:
            _log(f"Conexión perdida ({type(e).__name__}: {e}) — reintentando en {RECONNECT_ESPERA_S}s")
        except Exception as e:
            _log(f"Error inesperado ({type(e).__name__}: {e}) — reintentando en {RECONNECT_ESPERA_S}s")
        await asyncio.sleep(RECONNECT_ESPERA_S)


if __name__ == "__main__":
    asyncio.run(main())
