#!/usr/bin/env python3
"""
ballenas_firehose_cache.py — Cache en memoria de trades reales Up/Down
5min y 15min (ETH/SOL/XRP/DOGE/BNB), alimentado por una conexión WEBSOCKET PROPIA
a RTDS (wss://ws-live-data.polymarket.com, topic activity/trades) — mismo
endpoint que ya usan fetch_polymarket_activity_ws.py y
wallet_mirror_sniper.py, pero conexión INDEPENDIENTE (no depende de que
el screen `polyactivity` esté vivo).

Origen (04-Ago): diagnóstico de por qué BALLENAS_TARDIAS#ETH#5min#BUY_YES
(LIVE) lleva desde el 29-Jul sin generar señales confirmadas — ver
idea_bug_trades_de_mercado_ballenas_tardias_eth5min_muda_03ago (memoria).
Causa raíz confirmada 04-Ago con pruebas en vivo: data-api.polymarket.com/
trades (usado por smart_money_tracker.trades_de_mercado(), la fuente que
ballenas_executor_5min.py consultaba hasta hoy) tiene (a) lag de indexación
de MINUTOS/HORAS — a los 25s de cerrado un mercado con miles de trades
reales, la API seguía devolviendo 4 — y (b) un tope duro de 250 resultados
que ignora el parámetro `limit` por completo. Para un ejecutor que dispara
tarde en la ventana (por diseño, "tardías"), esa combinación deja el gate
de volumen (n_yes_total>=35) prácticamente ciego. Este módulo sustituye
esa fuente por el firehose en tiempo real, que en la misma prueba mostró
2773 trades en el mismo instante donde la API mostraba 4.

Diseño: un solo hilo (arrancado una vez, idempotente) corre su propio
event loop de asyncio con la conexión websocket, parseando y guardando
en un dict en memoria condition_id -> [trades]. trades_de_mercado_firehose()
devuelve la lista en el MISMO shape que la API vieja (side/price/outcome/
proxyWallet) para que concentracion_ballenas() en ballenas_executor_5min.py
no necesite cambiar su lógica de filtrado, solo la fuente de datos.

Fail-closed (mismo principio que el resto del proyecto, CLAUDE.md): si no
ha llegado NINGÚN mensaje del firehose en los últimos STALE_S segundos
(hilo no arrancado, conexión caída, reconectando), trades_de_mercado_firehose()
devuelve [] — nunca sirve datos que podrían estar parados sin avisar. El
motivo se loguea explícitamente en el caller (ver "firehose_no_sano" en
ballenas_executor_5min.py) para que una caída sea visible, no silenciosa
— exactamente el tipo de fallo que causó este mismo bug (nadie notó que
trades_de_mercado() llevaba días devolviendo casi nada).

⚠️ Limitación conocida, aceptada conscientemente (no arreglada hoy): NO
hay backfill al conectar. El cache solo ve trades que ocurren MIENTRAS la
conexión está viva. Si el proceso (screen ballenas_5m) se reinicia a
mitad de la ventana de vigilancia de un mercado, ese mercado concreto
empezaría a contar desde cero en vez de desde su apertura real —
podría, en el peor caso, no llegar a cruzar el umbral de volumen para
ESE mercado aunque el volumen real total sí lo cruzara. Riesgo bajo
(la screen corre 24/7 y solo se reinicia por watchdog/deploy, no cada
ventana) y muchísimo menor en magnitud que el bug que esto sustituye
(que afectaba a TODAS las ventanas, no solo a las que coinciden con un
reinicio) -- no bloquea el fix, pero si se ve un patrón de "muda justo
tras un restart", esta es la primera hipótesis a revisar.
"""
import asyncio
import json
import os
import tempfile
import threading
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import websockets

from fetch_polymarket_activity_ws import WS_URL, _parse_updown

ACTIVOS_TRACKED = {"BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"}
# 04-Ago: ampliado a 15min (antes solo 5min) -- lo necesita
# gbm_late_15min_executor.py para el gate de volumen de GBM_LATE_15M#ETH
# #15min (GATE_VOLUMEN_VALIDADO en shadow_predict.py, umbral=35), que
# hasta hoy dependía de la misma trades_de_mercado() rota que se
# diagnosticó y arregló esta noche para BALLENAS_TARDIAS#ETH#5min --
# mismo mecanismo, mismo arreglo, otro marco temporal.
# 04-Ago (misma noche): ampliado también a "60min" + BTC -- lo necesita
# el diseño de idea_veto_ballenas_firehose_snapshot_diseno_04ago (paso 1),
# ya que veto_ballenas.combos_validados en config_live.json incluye
# SOL#60m/BTC#60m/ETH#60m junto a los 5/15min ya cubiertos. Ampliar aquí
# no cambia el comportamiento de los consumidores existentes (ballenas_5m/
# gbmlate15m/updowngbmtardio) -- solo capturan más datos de los que ya
# filtran por su propio condition_id, sin coste real (misma conexión,
# el firehose ya recibe estos trades y los descartaba antes de guardarlos).
MARCOS_TRACKED = {"5min", "15min", "60min"}
# 04-Ago: subido de 30 a 65min al añadir soporte 60min arriba -- un mercado
# de 60min necesita hasta 60min de histórico propio para no perder
# cobertura de su ventana completa; 30min lo truncaba a mitad de vida.
# +5min de margen sobre el máximo (60min) para arranque/latencia de purga.
VENTANA_RETENCION_S = 65 * 60
STALE_S = 15  # sin ningún mensaje en 15s -> algo está roto, fail-closed
PING_INTERVAL_S = 5
RECV_TIMEOUT_S = 30  # mismo valor y mismo motivo que fetch_polymarket_activity_ws.py (bug 29-Jul: sin
# timeout, una conexión muerta en silencio deja el bucle bloqueado para siempre sin reconectar)
RECONNECT_ESPERA_S = 5

_lock = threading.Lock()
_trades_por_mercado = defaultdict(list)  # condition_id -> [trade,...]
_tx_vistos_por_mercado = defaultdict(set)  # condition_id -> {transaction_hash,...}, dedup (04-Ago paso 1)
_ultimo_mensaje_ts = 0.0
_hilo_iniciado = False
_n_mensajes_relevantes = 0


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[firehose_cache {ts}] {msg}", flush=True)


def _purgar_viejos() -> None:
    corte = time.time() - VENTANA_RETENCION_S
    with _lock:
        vacios = []
        for cid, trades in _trades_por_mercado.items():
            trades[:] = [t for t in trades if t["_recibido_ts"] >= corte]
            if not trades:
                vacios.append(cid)
        for cid in vacios:
            del _trades_por_mercado[cid]
            _tx_vistos_por_mercado.pop(cid, None)


def ingerir_trade(activo: str, marco: str, condition_id: str, trade: dict) -> bool:
    """Guarda un trade YA PARSEADO (side/price/outcome/proxyWallet/
    transaction_hash) en el cache en memoria, si activo/marco están
    trackeados y el condition_id es válido. Deduplicado por
    transaction_hash dentro del mismo mercado (por si el emisor reenvía
    algo ya visto en una reconexión).

    Extraído 04-Ago (paso 1 de idea_veto_ballenas_firehose_snapshot_diseno_
    04ago) para que `fetch_polymarket_activity_ws.py` pueda alimentar este
    MISMO almacén sin abrir una segunda conexión websocket -- reutiliza el
    trade que ese proceso ya recibe y parsea, en su propia copia del
    módulo (proceso separado, sin estado compartido entre screens).
    `_correr_una_conexion()` (la conexión propia de este módulo, usada por
    ballenas_5m/gbmlate15m/updowngbmtardio) también pasa por aquí, para no
    duplicar la lógica de filtro/dedup/purga.

    Devuelve True si se guardó, False si se descartó (fuera de universo,
    condition_id vacío o duplicado)."""
    global _ultimo_mensaje_ts, _n_mensajes_relevantes
    if activo not in ACTIVOS_TRACKED or marco not in MARCOS_TRACKED or not condition_id:
        return False
    tx = trade.get("transaction_hash") or trade.get("_transaction_hash")
    with _lock:
        if tx and tx in _tx_vistos_por_mercado[condition_id]:
            return False
        if tx:
            _tx_vistos_por_mercado[condition_id].add(tx)
        _trades_por_mercado[condition_id].append(trade)
    _ultimo_mensaje_ts = time.time()
    _n_mensajes_relevantes += 1
    return True


async def _mantener_ping(ws) -> None:
    try:
        while True:
            await asyncio.sleep(PING_INTERVAL_S)
            await ws.send("PING")
    except (asyncio.CancelledError, websockets.exceptions.ConnectionClosed):
        pass


async def _correr_una_conexion() -> None:
    global _ultimo_mensaje_ts
    async with websockets.connect(WS_URL, open_timeout=10, close_timeout=5) as ws:
        sub = {"action": "subscribe", "subscriptions": [{"topic": "activity", "type": "trades"}]}
        await ws.send(json.dumps(sub))
        _log("conectado a RTDS, suscrito a activity/trades")
        ping_task = asyncio.create_task(_mantener_ping(ws))
        ultima_purga = time.time()
        try:
            while True:
                raw = await asyncio.wait_for(ws.recv(), timeout=RECV_TIMEOUT_S)
                _ultimo_mensaje_ts = time.time()  # latido de la conexión, aunque el mensaje no sea relevante
                if not raw:
                    continue
                try:
                    msg = json.loads(raw)
                except (json.JSONDecodeError, TypeError):
                    continue
                payload = msg.get("payload")
                if not isinstance(payload, dict) or "proxyWallet" not in payload:
                    continue
                event_slug = payload.get("eventSlug", "")
                activo, marco = _parse_updown(event_slug, payload.get("title", ""))
                cid = payload.get("conditionId", "")
                try:
                    price = float(payload.get("price", 0) or 0)
                except (TypeError, ValueError):
                    continue
                trade = {
                    "side": payload.get("side", ""),
                    "price": price,
                    "outcome": payload.get("outcome", ""),
                    "proxyWallet": payload.get("proxyWallet", ""),
                    "transaction_hash": payload.get("transactionHash", ""),
                    "_recibido_ts": time.time(),
                }
                ingerir_trade(activo or "", marco or "", cid, trade)
                if time.time() - ultima_purga > 60:
                    _purgar_viejos()
                    ultima_purga = time.time()
        finally:
            ping_task.cancel()


async def _bucle_reconexion() -> None:
    while True:
        try:
            await _correr_una_conexion()
        except (websockets.exceptions.ConnectionClosed, OSError, asyncio.TimeoutError) as e:
            _log(f"conexión perdida ({e}), reconectando en {RECONNECT_ESPERA_S}s")
        except Exception as e:
            _log(f"error inesperado ({e}), reconectando en {RECONNECT_ESPERA_S}s")
        await asyncio.sleep(RECONNECT_ESPERA_S)


def _hilo_asyncio() -> None:
    asyncio.run(_bucle_reconexion())


def iniciar() -> None:
    """Arranca el hilo de captura en background. Idempotente."""
    global _hilo_iniciado
    if _hilo_iniciado:
        return
    _hilo_iniciado = True
    t = threading.Thread(target=_hilo_asyncio, daemon=True, name="firehose_cache")
    t.start()
    _log("hilo de captura arrancado")


def esta_sano() -> bool:
    """True si hemos recibido al menos un mensaje relevante en los
    últimos STALE_S segundos. Falso en los primeros segundos tras
    iniciar() (todavía conectando) o si la conexión se cayó."""
    return _hilo_iniciado and (time.time() - _ultimo_mensaje_ts) < STALE_S


def trades_de_mercado_firehose(condition_id: str) -> list:
    """Mismo shape que smart_money_tracker.trades_de_mercado() (lista de
    dicts con side/price/outcome/proxyWallet) para no tocar la lógica de
    concentracion_ballenas(), solo la fuente. [] si el cache no está sano
    (fail-closed) o si el mercado no tiene trades vistos todavía."""
    if not esta_sano():
        return []
    with _lock:
        return list(_trades_por_mercado.get(condition_id, []))


SNAPSHOT_PATH = Path(__file__).resolve().parent / "data" / "live" / "ballenas_recientes.json"


def escribir_snapshot(path: Path = SNAPSHOT_PATH) -> tuple[int, int, int]:
    """Vuelca snapshot_para_json() a disco de forma ATÓMICA (fichero
    temporal en el mismo directorio + os.rename) -- en POSIX, cualquier
    lector ve siempre el fichero anterior completo o el nuevo completo,
    nunca algo a medio escribir (paso 2 de idea_veto_ballenas_firehose_
    snapshot_diseno_04ago). Incluye `generado_en` para que el lector
    (live_trade.py, todavía no cableado) pueda decidir si el snapshot es
    demasiado viejo para fiarse (mismo principio fail-open con aviso
    explícito que el resto de fail-open del proyecto).

    Devuelve (n_mercados, n_trades, bytes_escritos) para que el caller
    pueda loguear/vigilar el tamaño real sin tener que releer el fichero."""
    snap = snapshot_para_json()
    payload = {
        "generado_en": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "mercados": snap,
    }
    js = json.dumps(payload)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=str(path.parent), prefix=".tmp_ballenas_recientes_")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(js)
        os.rename(tmp_path, path)
    except Exception:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    n_trades = sum(len(v) for v in snap.values())
    return len(snap), n_trades, len(js)


_cache_lectura = {"path": None, "mtime": None, "payload": None}


def leer_snapshot_reciente(condition_id: str, max_edad_s: float = 60.0,
                            path: Path = SNAPSHOT_PATH) -> list:
    """Lee `data/live/ballenas_recientes.json` (escrito por
    `fetch_polymarket_activity_ws.py`, proceso persistente e
    INDEPENDIENTE) y devuelve los trades de `condition_id` en el mismo
    shape que `trades_de_mercado_firehose()` (side/price/outcome/
    proxyWallet). Pensada para PROCESOS EFÍMEROS como `live_trade.py`
    (invocado fresco cada ciclo, ~4-20s) que no pueden permitirse abrir su
    propia conexión websocket y esperar a que llegue el primer mensaje
    dentro de su presupuesto de latencia -- a diferencia de
    `trades_de_mercado_firehose()`, que sirve del cache EN MEMORIA de
    ESTE MISMO proceso (pensado para procesos persistentes como
    `ballenas_executor_5min.py`, que sí mantienen su propia conexión).

    Fail-closed (mismo principio que el resto del módulo): [] si el
    fichero no existe, está corrupto, o su `generado_en` tiene más de
    `max_edad_s` segundos (escritor caído/atascado) -- nunca sirve datos
    que podrían estar parados sin avisar. `max_edad_s=60` da margen de
    sobra sobre la cadencia de escritura real (10s) para tolerar un ciclo
    de reconexión del escritor sin degradar a ciegas.

    Cacheado por `mtime` del fichero (04-Ago, hallazgo del /code-review
    manual del paso 5): `_procesar_pendientes_ballenas()` en live_trade.py
    llama a esta función una vez POR ENTRADA pendiente dentro del mismo
    ciclo -- sin cache, cada llamada re-leía y re-parseaba el JSON entero
    desde disco (~30-150ms según tamaño) aunque el fichero no hubiera
    cambiado entre llamadas del mismo proceso. Con la cache, solo la
    PRIMERA llamada de cada ciclo paga ese coste; las siguientes reusan el
    payload ya parseado mientras `os.path.getmtime()` no cambie (chequeo
    de stat, no de contenido -- barato). No afecta a la frescura: la
    comprobación de `generado_en`/`max_edad_s` se sigue haciendo en CADA
    llamada sobre el payload cacheado.

    04-Ago, paso 3 de idea_veto_ballenas_firehose_snapshot_diseno_04ago --
    cableada en `_ballenas_conviccion_mercado()` (live_trade.py) tras
    revisión manual adversarial (paso 5)."""
    global _cache_lectura
    try:
        mtime = os.path.getmtime(path)
    except OSError:
        return []
    if _cache_lectura["path"] == path and _cache_lectura["mtime"] == mtime:
        payload = _cache_lectura["payload"]
    else:
        try:
            with open(path, "r", encoding="utf-8") as f:
                payload = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            return []
        if not isinstance(payload, dict):
            return []
        _cache_lectura = {"path": path, "mtime": mtime, "payload": payload}
    generado_en = payload.get("generado_en")
    if not generado_en:
        return []
    try:
        ts = datetime.fromisoformat(generado_en)
    except ValueError:
        return []
    edad_s = (datetime.now(timezone.utc) - ts).total_seconds()
    if edad_s < 0 or edad_s > max_edad_s:
        return []
    mercados = payload.get("mercados")
    if not isinstance(mercados, dict):
        return []
    return mercados.get(condition_id, [])


def snapshot_para_json() -> dict:
    """Copia serializable de TODO el cache actual, {condition_id: [{side,
    price,outcome,proxyWallet},...]} -- sin los campos internos
    (_recibido_ts, transaction_hash) para mantener el fichero ligero, ya
    que ambos solo sirven para la purga/dedup interna de este proceso, no
    para el consumidor. Usado por `fetch_polymarket_activity_ws.py` (paso
    2 de idea_veto_ballenas_firehose_snapshot_diseno_04ago) para volcar a
    `data/live/ballenas_recientes.json` de forma atómica. NO llama a
    esta_sano() -- el escritor decide su propia política de frescura."""
    with _lock:
        return {
            cid: [
                {"side": t["side"], "price": t["price"], "outcome": t["outcome"],
                 "proxyWallet": t["proxyWallet"]}
                for t in trades
            ]
            for cid, trades in _trades_por_mercado.items()
        }
