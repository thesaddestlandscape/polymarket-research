#!/usr/bin/env python3
"""momentum_ibs_reactivo_fase0.py -- FASE 0 (solo medición, NUNCA orden
real), 01-Sep. Propuesta #1 de Arquetipo A (ver project_5_propuestas_
arquetipo_a_01sep en memoria nativa, petición explícita Javi: "empieza
con la propuesta 1: generalizar el patrón reactivo a Momentum_IBS"):
generaliza el mecanismo de gbm_late_reactivo_fase0.py (25-Ago, único
mecanismo con éxito parcial real contra Arquetipo A -- fill-ability
20-35% vs 0.1-8% del sondeo normal) a MOMENTUM_IBS_5M/15M.

Diferencia real con GBM_LATE (por qué no es un copia-pega): GBM_LATE
dispara cuando el precio se mueve X% desde una referencia FIJA al inicio
de la ventana -- un solo número que comparar. MOMENTUM_IBS necesita
drift_pct e IBS (posición dentro del rango [min,max]) sobre una VENTANA
RODANTE de N minutos (7 para #5min, 20 para #15min, ver shadow_predict.py
::_drift_e_ibs_ventana/MOMENTUM_IBS_5M_LOOKBACK_MIN/MOMENTUM_IBS_15M_
LOOKBACK_MIN) -- hace falta mantener un buffer de precios en memoria y
recalcular la ventana en cada tick, no comparar contra un único ref.

Mismo criterio de disparo EXACTO que shadow_predict.py::s_momentum_ibs_5m/
s_momentum_ibs_15m (UMBRAL=0.7, ver MOMENTUM_IBS_5M_UMBRAL/15M_UMBRAL):
  drift_pct > 0 and ibs >= 0.7   -> BUY_YES (momentum alcista en extremo alto)
  drift_pct < 0 and ibs <= 0.3   -> BUY_NO  (momentum bajista en extremo bajo)
El mismo trigger sirve para medir la hipótesis directa Y la FADE
(MOMENTUM_IBS_*_FADE invierte la decisión sobre el MISMO evento) -- no
hace falta duplicar el disparo, el post-análisis decide qué lado evaluar.

NO calcula ballena_activa_n/bot_consenso (a diferencia de gbm_late_
reactivo) -- primera versión centrada en la pregunta esencial (¿hay
profundidad real capturable en el instante del cruce?), ampliable si
esto confirma señal.

NO coloca, cancela ni modifica ninguna orden real. Se fusiona en
observadores_fase0.py (screen "observadores") si funciona bien standalone,
mismo criterio que el resto de fase0 del proyecto.
"""
import asyncio
import bisect
import csv
import fcntl
import json
import sys
import time
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

import websockets

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from resolution_sniper_observer import mercado_slot, token_ids  # noqa: E402
from gbm_late_reactivo_fase0 import _libro_unico  # noqa: E402 -- reusa la
# petición única de red (fill+niveles), Session con keep-alive ya afinada
# el 25-Ago tras investigar el outlier de latencia real -- no reimplementar.
from libro_multinivel_fase0 import _imbalance, _slope  # noqa: E402

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "momentum_ibs_reactivo_fase0.csv"
OUT_LOCK = DIR_SHADOW / "momentum_ibs_reactivo_fase0.csv.lock"

ASSETS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
SYMBOLS = {"BTC": "btcusdt", "ETH": "ethusdt", "SOL": "solusdt",
           "XRP": "xrpusdt", "DOGE": "dogeusdt", "BNB": "bnbusdt"}
_SYM_A_ACTIVO = {v: k for k, v in SYMBOLS.items()}

# (marco_tag, dur_s, lookback_min) -- mismos valores exactos que
# shadow_predict.py::MOMENTUM_IBS_5M_LOOKBACK_MIN/15M_LOOKBACK_MIN.
MARCOS = {
    "5min": {"marco_tag": "5m", "dur_s": 300, "lookback_min": 7},
    "15min": {"marco_tag": "15m", "dur_s": 900, "lookback_min": 20},
}
UMBRAL = 0.7  # mismo que MOMENTUM_IBS_5M_UMBRAL/15M_UMBRAL
STAKE_REF_EUR = 1.05
BUFFER_MAX_MIN = 21  # cubre el lookback mas largo (20min) + margen

WS_URL = "wss://stream.binance.com:9443/stream?streams=" + "/".join(
    f"{s}@aggTrade" for s in SYMBOLS.values())

COLUMNS = [
    "timestamp_utc", "activo", "marco", "market_id", "condition_id", "ts_end",
    "ts_tick_binance_ms", "ts_consulta_libro_ms", "latencia_ms",
    "drift_pct", "ibs", "lado", "restante_min",
    "mejor_ask", "profundidad_eur", "ratio_vs_stake", "n_niveles",
    "imbalance_top1", "imbalance_top5", "imbalance_top10",
    "slope_ask", "slope_bid", "n_niveles_ask", "n_niveles_bid",
    "dia_semana",
]


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


class _EstadoVentana:
    """Por (activo, marco) -- ventana de mercado actual + dedup, mismo
    patrón que _EstadoActivo de gbm_late_reactivo_fase0.py."""
    __slots__ = ("ts_end", "mkt", "disparado")

    def __init__(self):
        self.ts_end = None
        self.mkt = None
        self.disparado = False


def _ts_precios(buffer: deque):
    """Snapshot (listas) del buffer, orden ascendente por ts -- se calcula
    UNA vez por tick (no una por marco) y se reusa vía bisect en
    _drift_e_ibs, evitando escanear el buffer entero (hasta 21min de
    ticks de Binance) dos veces por cada tick entrante (05-Sep, hallazgo
    code-review: el filtro `if ts>=corte_ms` sobre el buffer completo,
    repetido para 5min y 15min en cada tick, es carga real de CPU en el
    mismo hilo/loop que multiplexa los 6 símbolos y hace las peticiones
    bloqueantes a _libro_unico)."""
    if not buffer:
        return [], []
    ts_list, precios_list = zip(*buffer)
    return list(ts_list), list(precios_list)


def _drift_e_ibs(ts_list: list, precios_list: list, lookback_min: float):
    """Misma fórmula EXACTA que shadow_predict.py::_drift_e_ibs_ventana,
    pero sobre el snapshot en memoria de ticks del websocket (ts_ms, precio)
    en vez de precios_intraday (polling de fichero) -- mismo cálculo,
    fuente más fresca. `ts_list` ya viene ordenado ascendente (orden de
    llegada de los ticks), así que el subconjunto por lookback se localiza
    con bisect en O(log n) en vez de un filtro O(n).

    Hallazgo real (01-Sep, verificado en la prueba en vivo antes de
    desplegar): con el buffer recién arrancado (proceso nuevo), 5 ticks
    del stream de alta frecuencia de Binance llegan en 1-2 SEGUNDOS, no
    en los 7-20 minutos que el lookback pretende cubrir -- `len(subset)>=5`
    se satisface trivialmente sin que la ventana tenga sentido temporal
    (ibs sale exactamente 0 o 1, drift≈0.00%, disparo espurio). En
    producción (precios_intraday, historial de días) esto nunca pasa; en
    este script sí, cada vez que arranca. Exige que el tick más viejo del
    buffer esté a al menos el 90% del lookback -- si el buffer no lleva
    corriendo lo suficiente, no hay ventana real todavía."""
    if not ts_list:
        return None, None
    ahora_ms = time.time() * 1000
    corte_ms = ahora_ms - lookback_min * 60_000
    idx = bisect.bisect_left(ts_list, corte_ms)
    subset = precios_list[idx:]
    if len(subset) < 5:
        return None, None
    if ahora_ms - ts_list[0] < lookback_min * 60_000 * 0.9:
        return None, None  # buffer aun no cubre una ventana real
    ref_p, now_p = subset[0], subset[-1]
    if ref_p <= 0:
        return None, None
    drift_pct = (now_p / ref_p - 1) * 100
    lo, hi = min(subset), max(subset)
    ibs = (now_p - lo) / (hi - lo) if (hi - lo) > 1e-9 else 0.5
    return round(drift_pct, 4), round(ibs, 4)


async def _procesar_tick(activo: str, precio: float, ts_tick_ms: int,
                          buffers: dict, estados: dict) -> None:
    buf = buffers.setdefault(activo, deque())
    buf.append((ts_tick_ms, precio))
    corte_ms = ts_tick_ms - BUFFER_MAX_MIN * 60_000
    while buf and buf[0][0] < corte_ms:
        buf.popleft()

    now = time.time()
    ts_list = precios_list = None  # snapshot perezoso, se comparte entre marcos
    for marco, cfg in MARCOS.items():
        dur_s, lookback_min, marco_tag = cfg["dur_s"], cfg["lookback_min"], cfg["marco_tag"]
        ts_end = (int(now) // dur_s + 1) * dur_s
        ts_start = ts_end - dur_s
        clave = (activo, marco)
        e = estados.setdefault(clave, _EstadoVentana())
        if e.ts_end != ts_end:
            _, mkt = mercado_slot(activo, marco_tag, ts_start)
            e.ts_end = ts_end
            e.mkt = mkt
            e.disparado = False

        if e.disparado or not e.mkt:
            continue

        if ts_list is None:
            ts_list, precios_list = _ts_precios(buf)
        drift_pct, ibs = _drift_e_ibs(ts_list, precios_list, lookback_min)
        if drift_pct is None:
            continue

        if drift_pct > 0 and ibs >= UMBRAL:
            lado = "Up"
        elif drift_pct < 0 and ibs <= (1 - UMBRAL):
            lado = "Down"
        else:
            continue

        # dedup NO se marca aquí: si el lookup de tokens o la consulta al
        # libro fallan, la ventana sigue viva y se reintenta en el próximo
        # tick -- marcar disparado antes de confirmar éxito perdía la
        # ventana entera en silencio (hallazgo code-review 01-Sep).
        token_yes, token_no = token_ids(e.mkt)
        if not token_yes:
            continue
        token_id = token_yes if lado == "Up" else token_no
        ts_consulta_ms = int(time.time() * 1000)

        try:
            fill, asks, bids = _libro_unico(token_id, 0.5, STAKE_REF_EUR)
        except Exception as ex:
            _log(f"[{activo}#{marco}] error consultando libro: {type(ex).__name__}: {ex}")
            continue
        if not fill.get("ok"):
            _log(f"[{activo}#{marco}] libro sin respuesta: {fill.get('error')}")
            continue

        e.disparado = True  # dedup: un solo trigger por (activo,marco,ventana), ya con éxito confirmado
        restante_min = round((ts_end - time.time()) / 60.0, 2)
        fila = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
            "activo": activo, "marco": marco,
            "market_id": e.mkt.get("id", ""), "condition_id": e.mkt.get("conditionId", ""),
            "ts_end": ts_end,
            "ts_tick_binance_ms": ts_tick_ms, "ts_consulta_libro_ms": ts_consulta_ms,
            "latencia_ms": ts_consulta_ms - ts_tick_ms,
            "drift_pct": drift_pct, "ibs": ibs, "lado": lado,
            "restante_min": restante_min,
            "mejor_ask": fill.get("mejor_ask"), "profundidad_eur": fill.get("profundidad_eur"),
            "ratio_vs_stake": fill.get("ratio_vs_stake"), "n_niveles": fill.get("n_niveles"),
            "imbalance_top1": _imbalance(asks, bids, 1),
            "imbalance_top5": _imbalance(asks, bids, 5),
            "imbalance_top10": _imbalance(asks, bids, 10),
            "slope_ask": _slope(asks), "slope_bid": _slope(bids),
            "n_niveles_ask": len(asks), "n_niveles_bid": len(bids),
            "dia_semana": datetime.now(timezone.utc).weekday(),
        }
        _guardar(fila)
        _log(f"[{activo}#{marco}] TRIGGER lado={lado} drift={drift_pct:+.3f}% ibs={ibs:.2f} "
             f"restante={restante_min}min latencia={fila['latencia_ms']}ms "
             f"profundidad={fila['profundidad_eur']} ask={fila['mejor_ask']} "
             f"imb10={fila['imbalance_top10']}")


async def _consumir_websocket() -> None:
    buffers: dict = {}
    estados: dict = {}
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
                        await _procesar_tick(activo, precio, ts_tick_ms, buffers, estados)
                    except Exception as ex:
                        _log(f"error procesando mensaje: {type(ex).__name__}: {ex}")
        except Exception as ex:
            _log(f"conexión perdida ({type(ex).__name__}: {ex}) — reconectando en 5s")
            await asyncio.sleep(5)


def main() -> None:
    _log(f"momentum_ibs_reactivo_fase0 arrancado -- activos={ASSETS} "
         f"marcos={list(MARCOS.keys())} umbral_ibs={UMBRAL}")
    asyncio.run(_consumir_websocket())


if __name__ == "__main__":
    main()
