#!/usr/bin/env python3
"""mean_reversion_penny_clipper_fase0.py -- FASE 0 (solo medicion, NUNCA
orden real), 29-Sep. Instrumenta dos hipotesis nuevas encontradas al leer
el codigo fuente publico de AutoPilotPM (github.com/recogardtech/AutoPilotPM,
solo lectura, nunca instalado ni ejecutado -- ver idea_mean_reversion_penny_
clipper_autopilotpm_29sep) y validadas en backtest retrospectivo contra
results.csv (36.392 señales Mean Reversion, edge +1 a +3pp por bucket
Wilson90; 7.438 señales Penny Clipper, edge +2 a +18pp por bucket).

Hallazgo de sensibilidad a latencia (mismo backtest, 29-Sep, confirmado
antes de escribir una sola linea de este archivo):
  - MEAN REVERSION: el edge SOLO existe si se reacciona en el instante del
    cruce de zona (confirm_delay=0s -> edge=+1.58pp; esperar 30-300s ->
    edge NEGATIVO, -0.84 a -1.47pp). Por eso este modulo la implementa como
    reactiva de verdad: doble websocket (RTDS Polymarket + Binance spot),
    consulta el libro en el MISMO instante del trigger, igual que
    gbm_late_reactivo_fase0.py.
  - PENNY CLIPPER: al reves, el edge MEJORA con mas historial de
    confirmacion (window=60s edge+3.73pp -> window=300s edge+5.68pp) y no
    depende de la frescura del ultimo tick. Se implementa sobre el MISMO
    stream de trades pero con ventana de 300s, sin exigir reaccion
    instantanea.

NO coloca, cancela ni modifica ninguna orden real -- solo mide fill-ability
(libro real en el instante exacto del trigger) para decidir mas adelante,
con datos, si vale la pena construir un ejecutor real. Igual que
gbm_late_reactivo_fase0.py, candidato a fusionarse en observadores_fase0.py
si funciona bien standalone.
"""
import asyncio
import csv
import fcntl
import json
import re
import sys
import time
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

import requests
import websockets

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import live_trade as lt  # noqa: E402 -- CLOB_BOOK_URL
from resolution_sniper_observer import GAMMA, token_ids  # noqa: E402
from libro_multinivel_fase0 import _imbalance, _slope  # noqa: E402
from shadow_predict import _parse_updown_tipo, identificar_activo  # noqa: E402

DIR_SHADOW = REPO / "data" / "shadow"
OUT_MR = DIR_SHADOW / "mean_reversion_reactivo_fase0.csv"
OUT_PC = DIR_SHADOW / "penny_clipper_fase0.csv"
LOCK_MR = DIR_SHADOW / "mean_reversion_reactivo_fase0.csv.lock"
LOCK_PC = DIR_SHADOW / "penny_clipper_fase0.csv.lock"

ACTIVOS = {"BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"}
MARCOS_TRACKEADOS = {"5min", "15min"}
DUR_S = {"5min": 300, "15min": 900}
_RE_UPDOWN_SLUG = re.compile(r"^([a-z]+)-updown-(\d+)(m|h)-\d+$")

# ---- Mean Reversion (parametros = mismos que el backtest retrospectivo) ----
MR_CHEAP = 0.30
MR_EXPENSIVE = 0.72
MR_MIN_ROUND_AGE_S = 120
MR_MAX_SPOT_MOVE_PCT = 0.08     # spot real (Binance), no proxy de poly
MR_SPOT_WINDOW_S = 90

# ---- Penny Clipper (parametros = mismos que el backtest retrospectivo) ----
PC_ZONA_MIN = 0.08
PC_ZONA_MAX = 0.50
PC_WINDOW_S = 300
PC_MIN_OSC_RANGE = 0.03
PC_MIN_REVERSALS = 3
PC_REVERSAL_STEP = 0.01
PC_ENTRY_DISCOUNT = 0.01

STAKE_REF_EUR = 1.05
WS_RTDS_URL = "wss://ws-live-data.polymarket.com"
SYMBOLS_BINANCE = {"BTC": "btcusdt", "ETH": "ethusdt", "SOL": "solusdt",
                    "XRP": "xrpusdt", "DOGE": "dogeusdt", "BNB": "bnbusdt"}
WS_BINANCE_URL = "wss://stream.binance.com:9443/stream?streams=" + "/".join(
    f"{s}@aggTrade" for s in SYMBOLS_BINANCE.values())
_SYM_A_ACTIVO = {v: k for k, v in SYMBOLS_BINANCE.items()}

_SESSION = requests.Session()
_SESSION.mount("https://", requests.adapters.HTTPAdapter(pool_maxsize=20))

_CACHE_MKT_CID: dict = {}


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _mkt_por_condition_id(cid: str) -> dict | None:
    """Resuelve clobTokenIds/outcomes por condition_id (gamma-api), cacheado
    en memoria por proceso -- las mismas 6 monedas x 2 marcos rotan mercado
    cada 5-15min, el cache se llena rapido y no crece sin limite."""
    if cid in _CACHE_MKT_CID:
        return _CACHE_MKT_CID[cid]
    try:
        r = _SESSION.get(f"{GAMMA}/markets", params={"condition_ids": cid}, timeout=8)
        r.raise_for_status()
        data = r.json()
        mkt = data[0] if data else None
    except Exception:
        mkt = None
    _CACHE_MKT_CID[cid] = mkt
    return mkt


def _libro_unico(token_id: str, precio_entrada: float, stake_eur: float):
    """Copia literal del helper de gbm_late_reactivo_fase0.py (mismo
    patron, evita import cruzado innecesario entre dos scripts FASE 0)."""
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
    mejor_bid = bids[0][0] if bids else None
    ratio = (profundidad_eur / stake_eur) if stake_eur > 0 else None
    fill = {"ok": True, "mejor_ask": mejor_ask, "mejor_bid": mejor_bid,
            "profundidad_eur": round(profundidad_eur, 2), "n_niveles": len(asks),
            "ratio_vs_stake": round(ratio, 1) if ratio is not None else None}
    return fill, asks, bids


def _parse_updown(event_slug: str, title: str = ""):
    """Copia del mismo parser de fetch_polymarket_activity_ws.py (no se
    importa directo para no arrastrar su conexion RTDS propia -- este
    script abre la suya)."""
    m = _RE_UPDOWN_SLUG.match(event_slug or "")
    if m:
        activo = m.group(1).upper()
        if activo in ACTIVOS:
            n, unidad = m.group(2), m.group(3)
            marco = f"{n}min" if unidad == "m" else f"{int(n)*60}min"
            return activo, marco
    if not title:
        return None, None
    activo = identificar_activo(title)
    if activo not in ACTIVOS:
        return None, None
    tipo, vent = _parse_updown_tipo(title)
    if tipo in ("slot", "hourly") and vent in (5, 15):
        return activo, f"{vent}min"
    return None, None


COLUMNS_MR = [
    "timestamp_utc", "activo", "marco", "condition_id", "ts_end",
    "ts_trigger_ms", "ts_consulta_libro_ms", "latencia_ms",
    "price_yes", "decision", "round_age_s", "restante_min",
    "spot_move_pct", "mejor_ask", "mejor_bid", "profundidad_eur",
    "ratio_vs_stake", "n_niveles", "imbalance_top1", "imbalance_top5",
    "outcome_real", "resolved_ts",
]
COLUMNS_PC = [
    "timestamp_utc", "activo", "marco", "condition_id", "ts_end",
    "ts_trigger_ms", "ts_consulta_libro_ms", "latencia_ms",
    "price_yes", "decision", "round_age_s", "restante_min",
    "osc_range", "reversals", "discount", "mean_ventana",
    "mejor_ask", "mejor_bid", "spread", "profundidad_eur",
    "ratio_vs_stake", "n_niveles",
    "outcome_real", "resolved_ts",
]


def _guardar(path: Path, lock_path: Path, columnas: list, fila: dict) -> None:
    lock_f = open(lock_path, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        nuevo = not path.exists()
        with open(path, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if nuevo:
                w.writerow(columnas)
            w.writerow([fila.get(c, "") for c in columnas])
    finally:
        fcntl.flock(lock_f, fcntl.LOCK_UN)
        lock_f.close()


class _EstadoMercado:
    __slots__ = ("ts_end", "activo", "marco", "buffer", "disparado_mr", "disparado_pc")

    def __init__(self, activo, marco, ts_end):
        self.ts_end = ts_end
        self.activo = activo
        self.marco = marco
        self.buffer: deque = deque()  # (ts_epoch, price_yes)
        self.disparado_mr = False
        self.disparado_pc = False


_ESTADO_MERCADOS: dict[str, _EstadoMercado] = {}   # condition_id -> estado
_SPOT_BUFFER: dict[str, deque] = {a: deque() for a in ACTIVOS}  # activo -> (ts,price)


def _spot_move_pct(activo: str, window_s: float) -> float | None:
    buf = _SPOT_BUFFER.get(activo)
    if not buf:
        return None
    now = buf[-1][0]
    cutoff = now - window_s
    ventana = [p for (t, p) in buf if t >= cutoff]
    if len(ventana) < 2:
        return None
    return (ventana[-1] / ventana[0] - 1) * 100 if ventana[0] else None


def _estado_para(condition_id: str, activo: str, marco: str) -> _EstadoMercado:
    dur = DUR_S[marco]
    now = time.time()
    ts_end = (int(now) // dur + 1) * dur
    e = _ESTADO_MERCADOS.get(condition_id)
    if e is None or e.ts_end != ts_end:
        e = _EstadoMercado(activo, marco, ts_end)
        _ESTADO_MERCADOS[condition_id] = e
    return e


async def _consultar_y_registrar_mr(cid, activo, marco, price_yes, decision, ts_trigger_ms,
                                     round_age_s, restante_min, spot_move):
    mkt = _mkt_por_condition_id(cid)
    if not mkt:
        return
    token_yes, token_no = token_ids(mkt)
    if not token_yes:
        return
    token_id = token_yes if decision == "BUY_YES" else token_no
    ts_consulta_ms = int(time.time() * 1000)
    fill, asks, bids = _libro_unico(token_id, price_yes if decision == "BUY_YES" else 1 - price_yes, STAKE_REF_EUR)
    if not fill.get("ok"):
        return
    fila = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
        "activo": activo, "marco": marco, "condition_id": cid,
        "ts_end": _ESTADO_MERCADOS[cid].ts_end,
        "ts_trigger_ms": ts_trigger_ms, "ts_consulta_libro_ms": ts_consulta_ms,
        "latencia_ms": ts_consulta_ms - ts_trigger_ms,
        "price_yes": round(price_yes, 4), "decision": decision,
        "round_age_s": round(round_age_s, 1), "restante_min": restante_min,
        "spot_move_pct": round(spot_move, 4) if spot_move is not None else "",
        "mejor_ask": fill.get("mejor_ask"), "mejor_bid": fill.get("mejor_bid"),
        "profundidad_eur": fill.get("profundidad_eur"), "ratio_vs_stake": fill.get("ratio_vs_stake"),
        "n_niveles": fill.get("n_niveles"),
        "imbalance_top1": _imbalance(asks, bids, 1), "imbalance_top5": _imbalance(asks, bids, 5),
        "outcome_real": "", "resolved_ts": "",
    }
    _guardar(OUT_MR, LOCK_MR, COLUMNS_MR, fila)
    _log(f"[MR] {activo}#{marco} {decision} price={price_yes:.3f} round_age={round_age_s:.0f}s "
         f"lat={fila['latencia_ms']}ms ask={fill.get('mejor_ask')} ratio={fill.get('ratio_vs_stake')}")


async def _consultar_y_registrar_pc(cid, activo, marco, price_yes, decision, ts_trigger_ms,
                                     round_age_s, restante_min, osc_range, reversals, discount, mean_v):
    mkt = _mkt_por_condition_id(cid)
    if not mkt:
        return
    token_yes, token_no = token_ids(mkt)
    if not token_yes:
        return
    token_id = token_yes if decision == "BUY_YES" else token_no
    ts_consulta_ms = int(time.time() * 1000)
    fill, asks, bids = _libro_unico(token_id, price_yes if decision == "BUY_YES" else 1 - price_yes, STAKE_REF_EUR)
    if not fill.get("ok"):
        return
    ask = fill.get("mejor_ask")
    bid = fill.get("mejor_bid")
    spread = round(ask - bid, 4) if (ask is not None and bid is not None) else ""
    fila = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
        "activo": activo, "marco": marco, "condition_id": cid,
        "ts_end": _ESTADO_MERCADOS[cid].ts_end,
        "ts_trigger_ms": ts_trigger_ms, "ts_consulta_libro_ms": ts_consulta_ms,
        "latencia_ms": ts_consulta_ms - ts_trigger_ms,
        "price_yes": round(price_yes, 4), "decision": decision,
        "round_age_s": round(round_age_s, 1), "restante_min": restante_min,
        "osc_range": round(osc_range, 4), "reversals": reversals,
        "discount": round(discount, 4), "mean_ventana": round(mean_v, 4),
        "mejor_ask": ask, "mejor_bid": bid, "spread": spread,
        "profundidad_eur": fill.get("profundidad_eur"), "ratio_vs_stake": fill.get("ratio_vs_stake"),
        "n_niveles": fill.get("n_niveles"),
        "outcome_real": "", "resolved_ts": "",
    }
    _guardar(OUT_PC, LOCK_PC, COLUMNS_PC, fila)
    _log(f"[PC] {activo}#{marco} {decision} price={price_yes:.3f} rev={reversals} "
         f"range={osc_range:.3f} disc={discount:.3f} bid={bid} ask={ask}")


async def _procesar_trade_poly(cid: str, activo: str, marco: str, price_yes: float, ts_ms: int) -> None:
    e = _estado_para(cid, activo, marco)
    now = time.time()
    e.buffer.append((now, price_yes))
    cutoff = now - max(PC_WINDOW_S, MR_SPOT_WINDOW_S) - 5
    while e.buffer and e.buffer[0][0] < cutoff:
        e.buffer.popleft()

    dur = DUR_S[marco]
    round_start = e.ts_end - dur
    round_age_s = now - round_start
    restante_min = round((e.ts_end - now) / 60.0, 2)

    # --- MEAN REVERSION: reaccion inmediata, primer cruce por ronda ---
    if not e.disparado_mr and round_age_s >= MR_MIN_ROUND_AGE_S:
        if price_yes <= MR_CHEAP:
            decision = "BUY_YES"
        elif price_yes >= MR_EXPENSIVE:
            decision = "BUY_NO"
        else:
            decision = None
        if decision:
            spot_move = _spot_move_pct(activo, MR_SPOT_WINDOW_S)
            if spot_move is None or abs(spot_move) <= MR_MAX_SPOT_MOVE_PCT:
                e.disparado_mr = True
                asyncio.create_task(_consultar_y_registrar_mr(
                    cid, activo, marco, price_yes, decision, ts_ms,
                    round_age_s, restante_min, spot_move))

    # --- PENNY CLIPPER: ventana de 300s, no exige reaccion instantanea ---
    if not e.disparado_pc:
        ventana = [p for (t, p) in e.buffer if now - t <= PC_WINDOW_S]
        if len(ventana) >= 3:
            osc_range = max(ventana) - min(ventana)
            if osc_range >= PC_MIN_OSC_RANGE:
                reversals = 0
                last_dir = None
                for a, b in zip(ventana, ventana[1:]):
                    diff = b - a
                    if abs(diff) < PC_REVERSAL_STEP:
                        continue
                    d = "up" if diff > 0 else "down"
                    if last_dir and d != last_dir:
                        reversals += 1
                    last_dir = d
                if reversals >= PC_MIN_REVERSALS:
                    mean_v = sum(ventana) / len(ventana)
                    disc_yes = mean_v - price_yes
                    disc_no = price_yes - mean_v
                    decision = None
                    discount = 0.0
                    if PC_ZONA_MIN <= price_yes <= PC_ZONA_MAX and disc_yes >= PC_ENTRY_DISCOUNT:
                        decision, discount = "BUY_YES", disc_yes
                    elif PC_ZONA_MIN <= (1 - price_yes) <= PC_ZONA_MAX and disc_no >= PC_ENTRY_DISCOUNT:
                        decision, discount = "BUY_NO", disc_no
                    if decision:
                        e.disparado_pc = True
                        asyncio.create_task(_consultar_y_registrar_pc(
                            cid, activo, marco, price_yes, decision, ts_ms,
                            round_age_s, restante_min, osc_range, reversals, discount, mean_v))


async def _consumir_rtds() -> None:
    while True:
        try:
            async with websockets.connect(WS_RTDS_URL, open_timeout=10, close_timeout=5) as ws:
                await ws.send(json.dumps({
                    "action": "subscribe",
                    "subscriptions": [{"topic": "activity", "type": "trades"}],
                }))
                _log(f"RTDS conectado, suscrito a activity/trades")
                while True:
                    raw = await asyncio.wait_for(ws.recv(), timeout=30)
                    try:
                        msg = json.loads(raw)
                    except Exception:
                        continue
                    payload = msg.get("payload") or msg
                    if not isinstance(payload, dict):
                        continue
                    cid = payload.get("conditionId")
                    if not cid:
                        continue
                    activo, marco = _parse_updown(payload.get("eventSlug", ""), payload.get("title", ""))
                    if not activo or marco not in MARCOS_TRACKEADOS:
                        continue
                    try:
                        price = float(payload.get("price", 0))
                    except (TypeError, ValueError):
                        continue
                    if not (0 < price < 1):
                        continue
                    outcome = str(payload.get("outcome", "")).strip().lower()
                    if outcome in ("up", "yes"):
                        price_yes = price
                    elif outcome in ("down", "no"):
                        price_yes = 1 - price
                    else:
                        continue
                    ts_ms = int(payload.get("timestamp", time.time() * 1000))
                    if ts_ms < 10**12:  # por si viene en segundos
                        ts_ms *= 1000
                    await _procesar_trade_poly(cid, activo, marco, price_yes, ts_ms)
        except (asyncio.TimeoutError, Exception) as ex:
            _log(f"RTDS desconectado ({type(ex).__name__}: {ex}) -- reconectando en 5s")
            await asyncio.sleep(5)


async def _consumir_binance() -> None:
    while True:
        try:
            async with websockets.connect(WS_BINANCE_URL, ping_interval=20, ping_timeout=20) as ws:
                _log("Binance spot conectado")
                async for raw in ws:
                    try:
                        msg = json.loads(raw)
                        data = msg.get("data", {})
                        sym = data.get("s", "").lower()
                        activo = _SYM_A_ACTIVO.get(sym)
                        if not activo:
                            continue
                        precio = float(data.get("p", 0))
                        if precio <= 0:
                            continue
                        buf = _SPOT_BUFFER[activo]
                        now = time.time()
                        buf.append((now, precio))
                        cutoff = now - MR_SPOT_WINDOW_S - 5
                        while buf and buf[0][0] < cutoff:
                            buf.popleft()
                    except Exception:
                        continue
        except Exception as ex:
            _log(f"Binance desconectado ({type(ex).__name__}: {ex}) -- reconectando en 5s")
            await asyncio.sleep(5)


async def _main_async() -> None:
    await asyncio.gather(_consumir_rtds(), _consumir_binance())


def main() -> None:
    _log(f"mean_reversion_penny_clipper_fase0 arrancado -- activos={sorted(ACTIVOS)} "
         f"marcos={sorted(MARCOS_TRACKEADOS)} (FASE 0, solo lectura, sin ordenes reales)")
    asyncio.run(_main_async())


if __name__ == "__main__":
    main()
