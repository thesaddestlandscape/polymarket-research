#!/usr/bin/env python3
"""gbm_late_reactivo_fase0.py -- FASE 0 (solo medición, NUNCA orden real),
25-Ago. Mide si Arquetipo A (GBM_LATE) tiene una ventana de profundidad
real capturable en los primeros cientos de milisegundos tras el tick de
Binance que cruza el umbral de edge, algo que el sondeo actual a 2s
(`gbm_late_15min_executor.py::POLL_INTERVAL_S=2.0`) no puede ver.

Contexto (ver idea_arquetipo_a_palancas_probadas_25ago en memoria): FAK/
orden parcial ya descartado (99.9% de vetos con profundidad LITERALMENTE
CERO en 4 familias -- no hay nada que un fill parcial pudiera rescatar).
El websocket de FUTUROS de Binance (fstream.binance.com, usado para
liquidaciones) está bloqueado para esta VPS -- pero el de SPOT
(stream.binance.com:9443, el precio que usa GBM_LATE) está CONFIRMADO
funcionando sin bloqueo (307 msj/10s, verificado 30-Jul). Este script
construye el consumidor de ese websocket spot que nunca se había hecho.

Diseño (experimento de medición, no réplica exacta del modelo GBM):
para cada mercado GBM_LATE#15min activo (6 monedas), toma como
referencia el primer tick de precio visto tras el inicio de la ventana
de 15min (mismo rol que `ref` en shadow_predict.py::_s_gbm_late). En
cada tick nuevo, si el movimiento acumulado desde esa referencia supera
GBM_LATE_DRIFT_VENT_MIN_PCT (0.03%, mismo umbral real que usa el modelo)
y no se ha disparado ya para ese mercado, consulta INMEDIATAMENTE el
libro real de Polymarket (mismo `_consultar_profundidad_libro` que usan
los ejecutores live) y registra la latencia tick->consulta y la
profundidad encontrada.

NO calcula d_gbm/sigma_h/p_up completos -- el objetivo es solo medir
profundidad en el INSTANTE del cruce, comparable contra el baseline ya
conocido (99.9% profundidad=0 con sondeo a 2s).

NO coloca, cancela ni modifica ninguna orden real. Se fusiona en
observadores_fase0.py (screen "observadores") si funciona bien standalone.
"""
import asyncio
import csv
import fcntl
import json
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path

import requests
import websockets

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import live_trade as lt  # noqa: E402 -- CLOB_BOOK_URL solo, ver _libro_unico()
from resolution_sniper_observer import mercado_slot, token_ids  # noqa: E402
from libro_multinivel_fase0 import _imbalance, _slope  # noqa: E402
import ballenas_firehose_cache as _fc  # noqa: E402
from shadow_predict import _cargar_bot_wallets  # noqa: E402

# 25-Ago (propuesta #15, Javi: "averigua exactamente qué es, tenemos que
# explotarlo a nuestro favor"): investigado el outlier de latencia
# compartido en las 6 monedas -- causa real encontrada, no especulada:
# `_consultar_profundidad_libro()` (agregado) y `_libro_completo()`
# (multi-nivel) hacían DOS peticiones HTTP SEPARADAS al mismo endpoint
# /book para el mismo token, casi al mismo instante, cada una con
# `requests.get()` suelto (sin Session -> sin reutilizar conexión TCP/TLS,
# cada llamada paga el handshake completo desde cero). `_libro_unico()`
# fusiona ambas en UNA sola petición sobre una Session compartida a nivel
# de módulo (keep-alive real entre triggers) -- debería reducir tanto la
# latencia base como la frecuencia de outliers de conexión fría.
_SESSION = requests.Session()


def _libro_unico(token_id: str, precio_entrada: float, stake_eur: float):
    """Una sola petición a /book -- devuelve (fill_dict, asks, bids) donde
    fill_dict tiene el mismo shape que _consultar_profundidad_libro()
    (mejor_ask/profundidad_eur/ratio_vs_stake/n_niveles/ok) y asks/bids
    son las listas completas [(price,size),...] que antes daba
    _libro_completo() -- mismo cálculo, una sola llamada de red."""
    try:
        r = _SESSION.get(lt.CLOB_BOOK_URL, params={"token_id": token_id}, timeout=10)
        r.raise_for_status()
        book = r.json()
    except Exception as e:
        return {"ok": False, "error": str(e)}, [], []

    asks_raw = book.get("asks") or []
    bids_raw = book.get("bids") or []
    asks = sorted([(float(a["price"]), float(a["size"])) for a in asks_raw])
    bids = sorted([(float(a["price"]), float(a["size"])) for a in bids_raw], reverse=True)

    techo = precio_entrada * 1.05
    profundidad_eur = 0.0
    mejor_ask = None
    for p, s in asks:
        if mejor_ask is None or p < mejor_ask:
            mejor_ask = p
        if p <= techo:
            profundidad_eur += p * s
    ratio = (profundidad_eur / stake_eur) if stake_eur > 0 else None
    fill = {
        "ok": True, "mejor_ask": mejor_ask, "profundidad_eur": round(profundidad_eur, 2),
        "n_niveles": len(asks), "ratio_vs_stake": round(ratio, 1) if ratio is not None else None,
    }
    return fill, asks, bids

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "gbm_late_reactivo_fase0.csv"
OUT_LOCK = DIR_SHADOW / "gbm_late_reactivo_fase0.csv.lock"

ASSETS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
SYMBOLS = {"BTC": "btcusdt", "ETH": "ethusdt", "SOL": "solusdt",
           "XRP": "xrpusdt", "DOGE": "dogeusdt", "BNB": "bnbusdt"}
MARCO_TAG = "15m"
DUR_S = 900
DRIFT_MIN_PCT = 0.03  # mismo umbral que GBM_LATE_DRIFT_VENT_MIN_PCT en shadow_predict.py
STAKE_REF_EUR = 1.05

WS_URL = "wss://stream.binance.com:9443/stream?streams=" + "/".join(
    f"{s}@aggTrade" for s in SYMBOLS.values())

COLUMNS = [
    "timestamp_utc", "activo", "market_id", "condition_id", "ts_end",
    "ts_tick_binance_ms", "ts_consulta_libro_ms", "latencia_ms",
    "precio_ref", "precio_tick", "drift_pct", "restante_min",
    "mejor_ask", "profundidad_eur", "ratio_vs_stake", "n_niveles",
    "imbalance_top1", "imbalance_top5", "imbalance_top10",
    "slope_ask", "slope_bid", "n_niveles_ask", "n_niveles_bid",
    "kalshi_mid", "kalshi_ts_utc", "kalshi_delta_ms",
    "bot_n_trades", "bot_lado_mayoria", "bot_coincide_direccion",
]
# 25-Ago (propuesta #14, Javi): en el instante del trigger, ¿ya hay bot
# wallets (bot_wallets_universo_25ago.json, edge confirmado) operando en
# ESTE mercado? Mide si vamos por delante del dinero informado (bot_
# n_trades=0 -- el mercado sigue "limpio" cuando reaccionamos) o a
# rebufo (bot_n_trades>0, y si coinciden con nuestra dirección o no).
# Reusa _cargar_bot_wallets() de shadow_predict.py (frozenset cacheado
# por mtime, ya en uso en producción) y leer_snapshot_reciente() del
# firehose (mismo mecanismo de baja latencia que _gate_volumen_ballenas,
# cero llamadas de red nuevas).
# 25-Ago (propuesta #13, Javi, versión ligera -- medir antes de construir
# un pipeline paralelo completo): solo para BTC (único activo con mercado
# Kalshi 15min direccional, KXBTC15M), lee la ÚLTIMA fila ya capturada por
# fetch_kalshi_btc.py (poll cada 2s, sin necesidad de construir nada
# nuevo de captura) y mide si su timestamp es ANTERIOR al tick de Binance
# que nos disparó -- kalshi_delta_ms negativo = Kalshi se adelantó,
# positivo = Kalshi va detrás. Con esto (barato, reusa datos que ya se
# están grabando) se puede ver si merece la pena construir un trigger
# propio sobre Kalshi antes de invertir en ello -- ver hallazgo previo
# (idea_kalshi_leadlag_refutado_primera_pasada_24ago): la señal agregada
# es débil, solo +1s/+2s marginalmente significativos, dominada por la
# dirección contraria. Este cruce con GBM_LATE es un ángulo NUEVO, no
# repite ese análisis.

DIR_PRICES = REPO / "data" / "prices"


def _kalshi_ultimo_btc() -> tuple[float | None, str | None]:
    """Última fila de hoy en kalshi_btc15m_YYYY-MM-DD.csv -- lectura
    barata (solo el final del fichero, igual que el resto de tails del
    proyecto), sin abrir conexión nueva ni depender de que Kalshi tenga
    websocket público (no verificado, no asumido)."""
    path = DIR_PRICES / f"kalshi_btc15m_{date.today().isoformat()}.csv"
    if not path.exists():
        return None, None
    try:
        with open(path, "rb") as f:
            f.seek(0, 2)
            tam = f.tell()
            f.seek(max(0, tam - 4096))
            ultimas = f.read().decode("utf-8", errors="replace").splitlines()
        for linea in reversed(ultimas):
            if not linea or linea.startswith("timestamp_utc"):
                continue
            partes = linea.split(",")
            if len(partes) < 6:
                continue
            ts_utc, _ticker, _floor, yes_bid, yes_ask, _last = partes[:6]
            mid = (float(yes_bid) + float(yes_ask)) / 2
            return mid, ts_utc
    except Exception:
        pass
    return None, None
# 25-Ago (propuesta #11, Javi): `restante_min` permite filtrar a
# posteriori qué hermanos de GBM_LATE (TARDIO/ESPACIO_ATR/PYCONFIRMADO/
# MULTIHORIZONTE/base, ver _s_gbm_late en shadow_predict.py) tenían su
# ventana rest_lo/rest_hi activa en el instante del trigger -- sin
# duplicar 6 lógicas de disparo distintas (cada hermano usa su propio
# rest_lo/rest_hi y ESPACIO_ATR incluso su propio umbral en vez de
# GBM_LATE_DRIFT_VENT_MIN_PCT), este único trigger de 0.03% ya captura
# el instante compartido; restante_min es lo que falta para poder
# segmentar el análisis por hermano después.
# 25-Ago (propuesta #12, Javi): imbalance/slope multi-nivel en el MISMO
# instante reactivo (no en un timer aparte de 5min como libro_
# multinivel_fase0.py) -- reusa sus mismas funciones de cálculo.

_SYM_A_ACTIVO = {v: k for k, v in SYMBOLS.items()}


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _guardar(fila: dict) -> None:
    lock_f = open(OUT_LOCK, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if nuevo:
                w.writerow(COLUMNS)
            w.writerow([fila.get(c, "") for c in COLUMNS])
    finally:
        fcntl.flock(lock_f, fcntl.LOCK_UN)
        lock_f.close()


class _EstadoActivo:
    __slots__ = ("ts_end", "mkt", "ref", "disparado")

    def __init__(self):
        self.ts_end = None
        self.mkt = None
        self.ref = None
        self.disparado = False


async def _procesar_tick(activo: str, precio: float, ts_tick_ms: int, estado: dict) -> None:
    now = time.time()
    ts_end = (int(now) // DUR_S + 1) * DUR_S
    ts_start = ts_end - DUR_S

    e = estado.setdefault(activo, _EstadoActivo())
    if e.ts_end != ts_end:
        # nueva ventana -- resolver mercado (barato, cacheado por
        # mercado_slot) y resetear referencia/disparo
        slug, mkt = mercado_slot(activo, MARCO_TAG, ts_start)
        e.ts_end = ts_end
        e.mkt = mkt
        e.ref = precio
        e.disparado = False
        return

    if e.ref is None or e.ref <= 0:
        e.ref = precio
        return
    if e.disparado or not e.mkt:
        return

    drift_pct = (precio / e.ref - 1) * 100
    if abs(drift_pct) < DRIFT_MIN_PCT:
        return

    e.disparado = True  # dedup: solo el primer cruce por ventana
    token_yes, token_no = token_ids(e.mkt)
    if not token_yes:
        return
    token_id = token_yes if drift_pct > 0 else token_no
    ts_consulta_ms = int(time.time() * 1000)

    # propuesta #15 (fix de la investigación del outlier de latencia,
    # 25-Ago): UNA sola petición de red para el agregado (#fill) y los
    # niveles completos (#12), sobre una Session con keep-alive -- antes
    # eran 2 peticiones separadas sin reutilizar conexión.
    try:
        fill, asks, bids = _libro_unico(token_id, 0.5, STAKE_REF_EUR)
    except Exception as ex:
        _log(f"[{activo}] error consultando libro: {type(ex).__name__}: {ex}")
        return
    if not fill.get("ok"):
        _log(f"[{activo}] libro sin respuesta: {fill.get('error')}")
        return

    restante_min = round((ts_end - time.time()) / 60.0, 2)

    bot_n_trades, bot_lado_mayoria, bot_coincide_direccion = 0, "", ""
    try:
        bots = _cargar_bot_wallets()
        condition_id = e.mkt.get("conditionId", "")
        if bots and condition_id:
            trades_recientes = _fc.leer_snapshot_reciente(condition_id)
            votos: dict = {}
            for t in trades_recientes:
                if (t.get("side") or "").strip().upper() != "BUY":
                    continue
                if (t.get("proxyWallet") or "").lower() not in bots:
                    continue
                lado = t.get("outcome", "")
                if lado:
                    votos[lado] = votos.get(lado, 0) + 1
            bot_n_trades = sum(votos.values())
            if bot_n_trades:
                bot_lado_mayoria = max(votos, key=votos.get)
                lado_nuestro = "Up" if drift_pct > 0 else "Down"
                bot_coincide_direccion = "1" if bot_lado_mayoria == lado_nuestro else "0"
    except Exception as ex:
        _log(f"[{activo}] error consultando bot_consenso: {type(ex).__name__}: {ex}")

    kalshi_mid, kalshi_ts_utc, kalshi_delta_ms = "", "", ""
    if activo == "BTC":
        try:
            kalshi_mid, kalshi_ts_utc = _kalshi_ultimo_btc()
            if kalshi_ts_utc:
                kalshi_ts = datetime.fromisoformat(kalshi_ts_utc.replace("Z", "+00:00"))
                kalshi_delta_ms = int(kalshi_ts.timestamp() * 1000) - ts_tick_ms
        except Exception as ex:
            _log(f"[{activo}] error leyendo kalshi: {type(ex).__name__}: {ex}")
            kalshi_mid, kalshi_ts_utc, kalshi_delta_ms = "", "", ""

    fila = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
        "activo": activo, "market_id": e.mkt.get("id", ""),
        "condition_id": e.mkt.get("conditionId", ""), "ts_end": ts_end,
        "ts_tick_binance_ms": ts_tick_ms, "ts_consulta_libro_ms": ts_consulta_ms,
        "latencia_ms": ts_consulta_ms - ts_tick_ms,
        "precio_ref": e.ref, "precio_tick": precio, "drift_pct": round(drift_pct, 4),
        "restante_min": restante_min,
        "mejor_ask": fill.get("mejor_ask") if fill.get("ok") else "",
        "profundidad_eur": fill.get("profundidad_eur") if fill.get("ok") else "",
        "ratio_vs_stake": fill.get("ratio_vs_stake") if fill.get("ok") else "",
        "n_niveles": fill.get("n_niveles") if fill.get("ok") else "",
        "imbalance_top1": _imbalance(asks, bids, 1),
        "imbalance_top5": _imbalance(asks, bids, 5),
        "imbalance_top10": _imbalance(asks, bids, 10),
        "slope_ask": _slope(asks), "slope_bid": _slope(bids),
        "n_niveles_ask": len(asks), "n_niveles_bid": len(bids),
        "kalshi_mid": kalshi_mid, "kalshi_ts_utc": kalshi_ts_utc,
        "kalshi_delta_ms": kalshi_delta_ms,
        "bot_n_trades": bot_n_trades, "bot_lado_mayoria": bot_lado_mayoria,
        "bot_coincide_direccion": bot_coincide_direccion,
    }
    _guardar(fila)
    extra_kalshi = f" kalshi_delta={kalshi_delta_ms}ms" if activo == "BTC" else ""
    extra_bot = f" bot_n={bot_n_trades} bot_coincide={bot_coincide_direccion}" if bot_n_trades else ""
    _log(f"[{activo}] TRIGGER drift={drift_pct:+.3f}% restante={restante_min}min "
         f"latencia={fila['latencia_ms']}ms profundidad={fila['profundidad_eur']} "
         f"ask={fila['mejor_ask']} imb10={fila['imbalance_top10']}{extra_kalshi}{extra_bot}")


async def _consumir_websocket() -> None:
    estado: dict = {}
    while True:
        try:
            async with websockets.connect(WS_URL, ping_interval=20, ping_timeout=20) as ws:
                _log(f"conectado a {WS_URL[:60]}...")
                async for raw in ws:
                    try:
                        msg = json.loads(raw)
                        data = msg.get("data", {})
                        sym = data.get("s", "").lower()
                        activo = _SYM_A_ACTIVO.get(sym)
                        if not activo:
                            continue
                        precio = float(data.get("p", 0))
                        ts_tick_ms = int(data.get("T", time.time() * 1000))
                        if precio <= 0:
                            continue
                        await _procesar_tick(activo, precio, ts_tick_ms, estado)
                    except Exception as ex:
                        _log(f"error procesando mensaje: {type(ex).__name__}: {ex}")
        except Exception as ex:
            _log(f"conexión perdida ({type(ex).__name__}: {ex}) — reconectando en 5s")
            await asyncio.sleep(5)


def main() -> None:
    _log(f"gbm_late_reactivo_fase0 arrancado -- activos={ASSETS} marco=15min "
         f"umbral_drift={DRIFT_MIN_PCT}%")
    asyncio.run(_consumir_websocket())


if __name__ == "__main__":
    main()
