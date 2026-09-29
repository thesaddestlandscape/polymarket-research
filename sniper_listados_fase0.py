#!/usr/bin/env python3
"""
sniper_listados_fase0.py -- FASE 0 (solo observación, NUNCA orden real),
ronda3 #7 (29-Sep, Javi: "vamos con 3 #7"): sniper de mercados recién
listados -- "los primeros 30 min están lejos del precio justo".

Hallazgo de partida (sondeo gamma 29-Sep): los mercados más nuevos son
escaleras horarias/diarias de cripto ("Ethereum above 2.630 on September
29, 7AM ET?"), ~30 strikes por activo listados de golpe, con libro vacío
(bid 0 / ask 1) los primeros minutos hasta que los market makers
siembran cotizaciones. Ese tramo es modelable: P(S_T > K) con spot y
volatilidad conocidos. Este observador captura la EVOLUCIÓN del libro
tras el listado para medir (a) cuánto tardan en aparecer cotizaciones a
dos lados, (b) si el primer precio ejecutable está lejos del justo, (c) si
se puede comprar al ask inicial y valer más a los +5/+15/+30 min.

Por mercado NUEVO (createdAt posterior al arranque; excluidos up/down 5-15
min y weather, repo aparte; deportes sí, etiquetados):
  - fila de listado en data/shadow/sniper_listados_fase0.csv (una vez)
  - fotos del libro del token YES en la primera vista y a +1/+5/+15/+30/+60
    min desde createdAt en data/shadow/sniper_listados_fase0_seguimiento.csv
    (bid/ask/profundidad USD/niveles + spot Binance del activo si es cripto)
El precio justo y el EV se calculan a posteriori en
analisis_sniper_listados_fase0.py (vol realizada de klines 1m + desenlace
final por gamma). NO coloca ni cancela órdenes. Se fusiona en
observadores_fase0.py.

30-Sep (Javi: "¿no interesa micro-latencia aquí?" -- SÍ): el polling de gamma
cada 45 s tenía minutos de resolución, pero la prueba en vivo con el canal
WS del CLOB (custom_feature_enabled=true, assets_ids=[]) mostró que (a) el
evento `new_market` llega EN EL INSTANTE del listado (timestamp ms) con
condition_id, assets_ids, fee_schedule y `active` y (b) al suscribirse a
sus tokens llega el libro a los ~370 ms y los market makers ya han sembrado
(ej. bid 0,01 x 11.890 en un up/down). El observador ahora es dirigido por
eventos: detecta el listado por WS, se suscribe a sus dos tokens y registra
CADA evento del libro con timestamp ms durante los primeros 120 s
(sniper_listados_fase0_eventos.csv) para medir tiempo hasta la primera
cotización a dos lados y a qué precio siembran frente al justo; las fotos
REST con profundidad a +1/+5/+15/+30/+60 min se mantienen. Solo se hace
seguimiento ms de las escaleras cripto (above/reach/dip de BTC/ETH/SOL/
XRP/DOGE/BNB); el resto de listados (deportes, etc.) solo deja fila de
listado. El spot se une a posteriori con binance_bookticker (ms) del
datalog, no aquí.
"""
import asyncio
import csv
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
import websockets

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from sports_wallet_edge_tracker import clasificar  # noqa: E402

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"
BINANCE = "https://api.binance.com/api/v3/ticker/price"
DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "sniper_listados_fase0.csv"
OUT_SEG = DIR_SHADOW / "sniper_listados_fase0_seguimiento.csv"
VISTOS = DIR_SHADOW / "sniper_listados_fase0_vistos.json"
PEND = DIR_SHADOW / "sniper_listados_fase0_pend.json"   # escaleras en seguimiento: sobrevive a reinicios de observadores

WS_URL = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
VENTANA_MS_S = 120           # eventos del libro con timestamp ms durante los primeros N s
SEGUIMIENTO_MAX_S = 3600     # se mantiene la suscripción WS hasta +60 min
MAX_SEGUIDOS = 200
RECV_TIMEOUT_S = 30
EV_OUT = DIR_SHADOW / "sniper_listados_fase0_eventos.csv"
COLS_EV = ["market_id", "condition_id", "token", "t_evento_ms", "edad_ms", "tipo", "side", "precio", "size",
           "best_bid", "best_ask"]
OFFSETS_S = (60, 300, 900, 1800, 3600)
MAX_PAGINAS = 4
ACTIVOS = {"bitcoin": "BTC", "ethereum": "ETH", "solana": "SOL", "xrp": "XRP", "dogecoin": "DOGE", "bnb": "BNB"}

COLS = ["market_id", "condition_id", "question", "slug", "categoria", "activo", "strike", "created_at_utc",
        "visto_utc", "lag_visto_s", "end_date", "volumen_inicial", "yes_token", "t_evento_ms", "t_recv_ms", "latencia_ms",
        "fees_enabled", "fee_rate"]
COLS_SEG = ["market_id", "condition_id", "offset_obj_s", "edad_real_s", "ts_utc", "best_bid", "best_ask",
            "depth_bid_usd", "depth_ask_usd", "n_bid", "n_ask", "spot"]

_S = requests.Session()
_S.mount("https://", requests.adapters.HTTPAdapter(pool_maxsize=10))
_SPOT = {}


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _append(path, cols, filas):
    if not filas:
        return
    nuevo = not path.exists()
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(cols)
        for r in filas:
            w.writerow([r.get(c, "") for c in cols])


def _excluido(m):
    q = (m.get("question") or "") + " " + (m.get("slug") or "")
    if re.search(r"up or down|updown|-5m-|-15m-", q, re.I):
        return True
    return bool(re.search(r"temperature|highest temp", q, re.I))


def _activo(q):
    ql = q.lower()
    for k, v in ACTIVOS.items():
        if k in ql:
            return v
    return ""


def _strike(q):
    m = re.search(r"above ([\d,]+(?:\.\d+)?)", q)
    return float(m.group(1).replace(",", "")) if m else ""


def _spot(activo):
    if not activo:
        return ""
    c = _SPOT.get(activo)
    if c and time.time() - c[0] < 3:
        return c[1]
    try:
        p = float(_S.get(BINANCE, params={"symbol": f"{activo}USDT"}, timeout=5).json()["price"])
        _SPOT[activo] = (time.time(), p)
        return p
    except Exception:
        return ""


def _libro(token):
    try:
        r = _S.get(f"{CLOB}/book", params={"token_id": token}, timeout=8)
        r.raise_for_status()
        b = r.json()
    except Exception:
        return None
    bids = sorted(((float(x["price"]), float(x["size"])) for x in (b.get("bids") or [])), reverse=True)
    asks = sorted((float(x["price"]), float(x["size"])) for x in (b.get("asks") or []))
    return bids, asks


def _foto(m_info, offset_obj):
    lb = _libro(m_info["yes_token"])
    if lb is None:
        return None
    bids, asks = lb
    ahora = datetime.now(timezone.utc)
    try:
        edad = round((ahora - datetime.fromisoformat(m_info["created"])).total_seconds(), 1)
    except Exception:
        edad = ""
    bb = bids[0][0] if bids else ""
    ba = asks[0][0] if asks else ""
    return {"market_id": m_info["market_id"], "condition_id": m_info["cid"], "offset_obj_s": offset_obj,
            "edad_real_s": edad, "ts_utc": ahora.isoformat(timespec="seconds"), "best_bid": bb, "best_ask": ba,
            "depth_bid_usd": round(sum(p * s for p, s in bids if bb != "" and p >= bb - 0.03), 2),
            "depth_ask_usd": round(sum(p * s for p, s in asks if ba != "" and p <= ba + 0.03), 2),
            "n_bid": len(bids), "n_ask": len(asks), "spot": _spot(m_info["activo"])}



def _pend_guardar(estado):
    try:
        PEND.write_text(json.dumps({m: {k: v for k, v in i.items()} for m, i in estado["seguidos"].items()}), encoding="utf-8")
    except Exception:
        pass


async def _reanudar(ws, estado):
    """Tras un reinicio: re-suscribe y reprograma las fotos de las escaleras aún dentro de su hora de seguimiento."""
    try:
        prev = json.loads(PEND.read_text(encoding="utf-8"))
    except Exception:
        return
    ahora = time.time()
    for mid, info in prev.items():
        if info.get("hasta", 0) < ahora:
            continue
        estado["seguidos"][mid] = info
        for tk in info["toks"]:
            estado["por_token"][tk] = info
        await ws.send(json.dumps({"assets_ids": list(info["toks"]), "operation": "subscribe"}))
        for off in OFFSETS_S:
            due = info["t0_ms"] / 1000 + off
            if due + 60 < ahora:
                continue                       # foto ya vencida hace >1 min: se descarta, no se falsea la edad
            asyncio.get_running_loop().call_later(max(0.0, due - ahora),
                                                  lambda i=info, o=off: asyncio.ensure_future(_foto_async(i, o)))
    _log(f"reanudadas {len(estado['seguidos'])} escaleras tras reinicio")


def _clasificar(q, slug):
    cat = clasificar(q, slug) or (
        "cripto_escalera" if re.search(r"above|reach|dip", q, re.I) and _activo(q) else "otros")
    return cat


async def _foto_async(info, off):
    loop = asyncio.get_running_loop()
    f = await loop.run_in_executor(None, _foto, info, off)
    if f:
        _append(OUT_SEG, COLS_SEG, [f])


async def _sesion(estado):
    """Una conexión WS: escucha new_market (empty assets_ids) y añade suscripciones dinámicas."""
    async with websockets.connect(WS_URL, ping_interval=20, ping_timeout=20) as ws:
        await ws.send(json.dumps({"type": "market", "assets_ids": [], "custom_feature_enabled": True}))
        _log("WS conectado, escuchando new_market")
        if not estado.get("reanudado"):
            estado["reanudado"] = True
            await _reanudar(ws, estado)
        while True:
            try:
                raw = await asyncio.wait_for(ws.recv(), RECV_TIMEOUT_S)
            except asyncio.TimeoutError:
                # mismo patrón que chainlink/polyactivity: sin timeout una conexión muerta bloquea en silencio
                await ws.ping()
                continue
            t_recv = int(time.time() * 1000)
            try:
                j = json.loads(raw)
            except Exception:
                continue
            for e in (j if isinstance(j, list) else [j]):
                if not isinstance(e, dict):
                    continue
                tipo = e.get("event_type") or e.get("type")
                if tipo == "new_market":
                    await _on_nuevo(e, t_recv, ws, estado)
                else:
                    _on_libro(e, t_recv, estado)
            _limpiar(estado, ws)


async def _on_nuevo(e, t_recv, ws, estado):
    mid = str(e.get("id"))
    if mid in estado["vistos"]:
        return
    estado["vistos"][mid] = 1
    q = e.get("question", "")
    slug = e.get("slug", "")
    if re.search(r"up or down|updown|-5m-|-15m-|temperature|highest temp", q + " " + slug, re.I):
        return
    toks = e.get("clob_token_ids") or e.get("assets_ids") or []
    if not toks:
        return
    outs = e.get("outcomes") or []
    yes_idx = 0
    for i, o in enumerate(outs):
        if str(o).lower() == "yes":
            yes_idx = i
    cat = _clasificar(q, slug)
    t_ev = int(e.get("timestamp") or t_recv)
    act = _activo(q)
    fs = e.get("fee_schedule") or {}
    fila = {"market_id": mid, "condition_id": e.get("condition_id") or e.get("market", ""), "question": q[:140],
            "slug": slug, "categoria": cat, "activo": act, "strike": _strike(q),
            "created_at_utc": datetime.fromtimestamp(t_ev / 1000, timezone.utc).isoformat(timespec="milliseconds"),
            "visto_utc": datetime.fromtimestamp(t_recv / 1000, timezone.utc).isoformat(timespec="milliseconds"),
            "lag_visto_s": round((t_recv - t_ev) / 1000, 3), "end_date": "", "volumen_inicial": "",
            "yes_token": toks[yes_idx] if yes_idx < len(toks) else toks[0], "t_evento_ms": t_ev, "t_recv_ms": t_recv,
            "latencia_ms": t_recv - t_ev, "fees_enabled": e.get("fees_enabled", ""), "fee_rate": fs.get("rate", "")}
    _append(OUT, COLS, [fila])
    if cat != "cripto_escalera" or len(estado["seguidos"]) >= MAX_SEGUIDOS:
        return
    info = {"market_id": mid, "cid": fila["condition_id"], "yes_token": fila["yes_token"],
            "created": datetime.fromtimestamp(t_ev / 1000, timezone.utc).isoformat(), "activo": act,
            "t0_ms": t_ev, "toks": list(toks), "hasta": time.time() + SEGUIMIENTO_MAX_S}
    estado["seguidos"][mid] = info
    _pend_guardar(estado)
    for tk in toks:
        estado["por_token"][tk] = info
    await ws.send(json.dumps({"assets_ids": list(toks), "operation": "subscribe"}))
    _log(f"ESCALERA {q[:50]} listada, latencia {t_recv - t_ev} ms, suscrita")
    for off in OFFSETS_S:
        asyncio.get_running_loop().call_later(max(0.0, t_ev / 1000 + off - time.time()),
                                              lambda i=info, o=off: asyncio.ensure_future(_foto_async(i, o)))


def _on_libro(e, t_recv, estado):
    filas = []

    def reg(info, token, t_ev, tipo, side, precio, size, bb, ba):
        edad = t_ev - info["t0_ms"]
        if edad > VENTANA_MS_S * 1000:
            return
        filas.append({"market_id": info["market_id"], "condition_id": info["cid"], "token": "YES" if token == info["yes_token"] else "NO",
                      "t_evento_ms": t_ev, "edad_ms": edad, "tipo": tipo, "side": side, "precio": precio, "size": size,
                      "best_bid": bb, "best_ask": ba})

    if "price_changes" in e:
        for pc in e["price_changes"]:
            info = estado["por_token"].get(pc.get("asset_id"))
            if info:
                reg(info, pc.get("asset_id"), int(e.get("timestamp") or t_recv), "price_change", pc.get("side"),
                    pc.get("price"), pc.get("size"), pc.get("best_bid"), pc.get("best_ask"))
    else:
        info = estado["por_token"].get(e.get("asset_id"))
        if info:
            tipo = e.get("event_type") or "book"
            bids, asks = e.get("bids") or [], e.get("asks") or []
            bb = max((float(x["price"]) for x in bids), default="")
            ba = min((float(x["price"]) for x in asks), default="")
            reg(info, e.get("asset_id"), int(e.get("timestamp") or t_recv), tipo, "", e.get("price", ""), e.get("size", ""), bb, ba)
    _append(EV_OUT, COLS_EV, filas)


def _limpiar(estado, ws):
    ahora = time.time()
    caducados = [m for m, i in estado["seguidos"].items() if i["hasta"] < ahora]
    for m in caducados:
        info = estado["seguidos"].pop(m)
        for tk in info["toks"]:
            estado["por_token"].pop(tk, None)
        asyncio.ensure_future(ws.send(json.dumps({"assets_ids": info["toks"], "operation": "unsubscribe"})))
    if caducados:
        _pend_guardar(estado)


def main():
    _log("arrancado (dirigido por eventos WS new_market): libro con timestamp ms 120 s + fotos REST +1/5/15/30/60 min")
    try:
        vistos = json.loads(VISTOS.read_text(encoding="utf-8"))
    except Exception:
        vistos = {}
    estado = {"vistos": vistos, "seguidos": {}, "por_token": {}}
    while True:
        try:
            asyncio.run(_sesion(estado))
        except Exception as e:
            _log(f"WARN sesión WS caída: {type(e).__name__}: {e}; reconecta en 5 s")
        try:
            VISTOS.write_text(json.dumps(dict(list(estado["vistos"].items())[-30000:])), encoding="utf-8")
        except Exception:
            pass
        time.sleep(5)


if __name__ == "__main__":
    main()
