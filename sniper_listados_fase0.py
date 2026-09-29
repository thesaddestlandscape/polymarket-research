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
"""
import csv
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

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

POLL_S = 45
OFFSETS_S = (60, 300, 900, 1800, 3600)
MAX_PAGINAS = 4
ACTIVOS = {"bitcoin": "BTC", "ethereum": "ETH", "solana": "SOL", "xrp": "XRP", "dogecoin": "DOGE", "bnb": "BNB"}

COLS = ["market_id", "condition_id", "question", "slug", "categoria", "activo", "strike", "created_at_utc",
        "visto_utc", "lag_visto_s", "end_date", "volumen_inicial", "yes_token"]
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


def _nuevos(vistos, t_arranque):
    """Mercados creados tras el arranque y aún no vistos (gamma, más recientes primero)."""
    out = []
    for pag in range(MAX_PAGINAS):
        try:
            r = _S.get(f"{GAMMA}/markets", params={"limit": 100, "offset": pag * 100, "order": "createdAt",
                                                    "ascending": "false", "closed": "false"}, timeout=20)
            j = r.json()
        except Exception as e:
            _log(f"WARN listado pag {pag}: {type(e).__name__}")
            break
        if not isinstance(j, list) or not j:
            break
        todos_vistos = True
        for m in j:
            mid = str(m.get("id"))
            if mid in vistos:
                continue
            todos_vistos = False
            try:
                creado = datetime.fromisoformat(m["createdAt"].replace("Z", "+00:00"))
            except Exception:
                continue
            if creado.timestamp() < t_arranque - 120:
                vistos[mid] = 0            # anterior al arranque: se ignora
                continue
            out.append((m, creado))
        if todos_vistos:
            break
        time.sleep(0.2)
    return out


def main():
    _log("arrancado -- mercados recién listados: libro a +1/+5/+15/+30/+60 min (solo observación)")
    try:
        vistos = json.loads(VISTOS.read_text(encoding="utf-8"))
    except Exception:
        vistos = {}
    t_arranque = time.time()
    pendientes = []        # (due_ts, offset, info)
    while True:
        try:
            filas, segs = [], []
            for m, creado in _nuevos(vistos, t_arranque):
                mid = str(m.get("id"))
                vistos[mid] = 1
                if _excluido(m):
                    continue
                try:
                    toks = json.loads(m.get("clobTokenIds") or "[]")
                except Exception:
                    continue
                if not toks:
                    continue
                q = m.get("question", "")
                cat = clasificar(q, m.get("groupItemTitle") or m.get("slug", "")) or (
                    "cripto_escalera" if re.search(r"above|reach|dip", q, re.I) and _activo(q) else "otros")
                info = {"market_id": mid, "cid": m.get("conditionId", ""), "yes_token": toks[0],
                        "created": creado.isoformat(), "activo": _activo(q)}
                filas.append({"market_id": mid, "condition_id": info["cid"], "question": q[:140],
                              "slug": m.get("slug", ""), "categoria": cat, "activo": info["activo"],
                              "strike": _strike(q), "created_at_utc": creado.isoformat(timespec="seconds"),
                              "visto_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                              "lag_visto_s": round(time.time() - creado.timestamp(), 1), "end_date": m.get("endDate", ""),
                              "volumen_inicial": m.get("volumeNum", ""), "yes_token": toks[0]})
                f0 = _foto(info, 0)
                if f0:
                    segs.append(f0)
                for off in OFFSETS_S:
                    pendientes.append((creado.timestamp() + off, off, info))
            pendientes.sort(key=lambda x: x[0])
            ahora = time.time()
            while pendientes and pendientes[0][0] <= ahora:
                _, off, info = pendientes.pop(0)
                f = _foto(info, off)
                if f:
                    segs.append(f)
            _append(OUT, COLS, filas)
            _append(OUT_SEG, COLS_SEG, segs)
            if filas:
                VISTOS.write_text(json.dumps(dict(list(vistos.items())[-30000:])), encoding="utf-8")
                _log(f"{len(filas)} mercados nuevos registrados, {len(pendientes)} fotos pendientes")
        except Exception as e:
            _log(f"WARN ciclo fallido: {type(e).__name__}: {e}")
        time.sleep(POLL_S)


if __name__ == "__main__":
    main()
