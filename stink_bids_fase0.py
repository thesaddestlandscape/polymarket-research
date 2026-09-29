#!/usr/bin/env python3
"""
stink_bids_fase0.py -- FASE 0 (solo observación), ronda3 #1 (29-Sep, Javi:
"una fase 0 con libro real y tamaño ejecutado antes de pensar en un
ejecutor").

Hallazgo previo (analisis retrospectivo 12-28 Sep, firehose): en mercados NO
up/down hay ~13 eventos/día en los que un SELL taker ejecuta >=5c por debajo
de la mediana de los trades previos (ventana 10 min, >=3 previos) y el
precio recupera una mediana de +13,7c a 5 min y +35c a 30 min frente a ~0
del control. Falta lo que decide si es cobrable: ¿había/queda profundidad de
bid pasiva a ese precio?, ¿cuánto USD se ejecutó?, ¿a qué precio podríamos
salir (bid real) a +1/+5/+30 min?

Este observador sigue el firehose (datalogs/polymarket_activity_YYYY-MM-DD.
csv, cola incremental por posición de fichero -- mismo patrón que los demás
fase0), detecta el evento en cuanto aparece y consulta UNA vez el libro
público del token vendido (bids/asks, profundidad cerca del precio del
evento y hasta la referencia). Después sigue el mismo token a +60 s, +300 s y
+1800 s (bid/ask reales + último trade). El resultado permite medir, con
precios EJECUTABLES (no last-trade), cuánto habría ganado un bid pasivo
puesto al precio del evento y vendido al bid real a +5/+30 min.

Salidas (CSV propios, no tocan nada más):
  data/shadow/stink_bids_fase0.csv            una fila por evento (detección)
  data/shadow/stink_bids_fase0_seguimiento.csv una fila por (evento, delta)
NO coloca, cancela ni modifica ninguna orden real. Se fusiona en
observadores_fase0.py.
"""
import bisect
import csv
import json
import statistics as st
import sys
import time
from collections import defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
DATALOGS = Path("/root/polymarket-research-datalogs")
DIR_SHADOW = REPO / "data" / "shadow"
OUT_EV = DIR_SHADOW / "stink_bids_fase0.csv"
OUT_SEG = DIR_SHADOW / "stink_bids_fase0_seguimiento.csv"
VISTOS_PATH = DIR_SHADOW / "stink_bids_fase0_vistos.json"

CLOB = "https://clob.polymarket.com"
VENTANA_S = 600
N_PREVIOS_MIN = 3
DEV_MIN = 0.05
USD_MIN = 1.0
PRECIO_MIN, PRECIO_MAX = 0.05, 0.95
SEGUIMIENTO_S = (60, 300, 1800)
POLL_S = 1.0
TOKEN_TTL_S = 6 * 3600

_SESSION = requests.Session()
_SESSION.mount("https://", requests.adapters.HTTPAdapter(pool_maxsize=10))

COLS_EV = ["event_id", "ts_evento_utc", "ts_deteccion_utc", "lag_deteccion_s", "condition_id", "outcome",
           "market_slug", "title", "precio_evento", "ref_mediana", "desviacion", "n_previos", "usd_evento",
           "size_evento", "wallet_vendedora", "best_bid_post", "best_ask_post", "spread_post",
           "depth_bid_hasta_ref_usd", "depth_bid_cerca_evento_usd", "depth_ask_cerca_ref_usd",
           "n_niveles_bid", "n_niveles_ask"]
COLS_SEG = ["event_id", "delta_s", "ts_utc", "best_bid", "best_ask", "ultimo_trade", "bid_size_top",
            "depth_bid_cerca_evento_usd"]


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _append(path: Path, cols: list, filas: list) -> None:
    if not filas:
        return
    nuevo = not path.exists()
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(cols)
        for fila in filas:
            w.writerow([fila.get(c, "") for c in cols])


_TOKENS: dict = {}  # condition_id -> (ts, {outcome_lower: token_id})


def _token(condition_id: str, outcome: str) -> str | None:
    ahora = time.time()
    c = _TOKENS.get(condition_id)
    if not c or ahora - c[0] > TOKEN_TTL_S:
        try:
            r = _SESSION.get(f"{CLOB}/markets/{condition_id}", timeout=10)
            r.raise_for_status()
            toks = {(t.get("outcome") or "").lower(): t.get("token_id") for t in r.json().get("tokens", [])}
        except Exception as e:
            _log(f"WARN tokens {condition_id[:12]}: {type(e).__name__}: {e}")
            return None
        _TOKENS[condition_id] = c = (ahora, toks)
    return c[1].get(outcome.lower())


def _libro(token_id: str):
    try:
        r = _SESSION.get(f"{CLOB}/book", params={"token_id": token_id}, timeout=10)
        r.raise_for_status()
        b = r.json()
    except Exception as e:
        _log(f"WARN libro {token_id[:10]}: {type(e).__name__}: {e}")
        return None, None
    bids = sorted(((float(x["price"]), float(x["size"])) for x in (b.get("bids") or [])), reverse=True)
    asks = sorted((float(x["price"]), float(x["size"])) for x in (b.get("asks") or []))
    return bids, asks


def _depth(niveles, lo, hi):
    return round(sum(p * s for p, s in niveles if lo <= p <= hi), 2)


def _cargar_vistos() -> set:
    try:
        return set(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return set()


def _guardar_vistos(v: set) -> None:
    VISTOS_PATH.write_text(json.dumps(list(v)[-20000:]), encoding="utf-8")


def _archivo(dt=None) -> Path:
    d = (dt or datetime.now(timezone.utc)).date().isoformat()
    return DATALOGS / f"polymarket_activity_{d}.csv"


class Estado:
    def __init__(self):
        self.trades = defaultdict(lambda: deque())   # key -> deque[(t, price)]
        self.ultimo = {}                              # key -> (t, price)
        self.pendientes = []                          # [(due_ts, event_id, delta, cond, outcome, precio_evento)]

    def previos(self, key, t):
        d = self.trades[key]
        while d and d[0][0] < t - VENTANA_S:
            d.popleft()
        return [p for _, p in d]


def _procesar_fila(row: dict, est: Estado, vistos: set, ahora_ts: float):
    """Devuelve dict de evento o None. Actualiza el estado SIEMPRE."""
    if row["activo"]:                      # updown de las monedas trackeadas: otro régimen, ya medido (sin reversión)
        return None
    cond = row["condition_id"]
    if not cond:
        return None
    try:
        t = int(row["ws_timestamp"])
        p = float(row["price"])
        usd = float(row["usd_value"])
    except (ValueError, KeyError):
        return None
    key = (cond, row["outcome"])
    ev = None
    if row["side"] == "SELL" and usd >= USD_MIN and PRECIO_MIN <= p <= PRECIO_MAX:
        prev = est.previos(key, t)
        if len(prev) >= N_PREVIOS_MIN:
            ref = st.median(prev)
            dev = ref - p
            eid = row["transaction_hash"] or f"{cond}|{row['outcome']}|{t}|{p}"
            if dev >= DEV_MIN and eid not in vistos:
                ev = {"event_id": eid, "ts_evento_utc": row["timestamp_utc"], "condition_id": cond,
                      "outcome": row["outcome"], "market_slug": row["market_slug"], "title": row["title"],
                      "precio_evento": p, "ref_mediana": round(ref, 4), "desviacion": round(dev, 4),
                      "n_previos": len(prev), "usd_evento": usd, "size_evento": row["size"],
                      "wallet_vendedora": row["wallet"], "_t": t}
    est.trades[key].append((t, p))
    est.ultimo[key] = (t, p)
    return ev


def _consultar_evento(ev: dict, est: Estado, vistos: set):
    tok = _token(ev["condition_id"], ev["outcome"])
    if not tok:
        return None
    bids, asks = _libro(tok)
    if bids is None:
        return None
    ahora = datetime.now(timezone.utc)
    p, ref = ev["precio_evento"], ev["ref_mediana"]
    ev["ts_deteccion_utc"] = ahora.isoformat(timespec="seconds")
    try:
        ev["lag_deteccion_s"] = round(ahora.timestamp() - ev["_t"], 1)
    except Exception:
        ev["lag_deteccion_s"] = ""
    ev["best_bid_post"] = bids[0][0] if bids else ""
    ev["best_ask_post"] = asks[0][0] if asks else ""
    ev["spread_post"] = round(asks[0][0] - bids[0][0], 4) if bids and asks else ""
    ev["depth_bid_hasta_ref_usd"] = _depth(bids, p, ref)
    ev["depth_bid_cerca_evento_usd"] = _depth(bids, p - 0.02, p + 0.02)
    ev["depth_ask_cerca_ref_usd"] = _depth(asks, ref - 0.02, ref + 0.02)
    ev["n_niveles_bid"], ev["n_niveles_ask"] = len(bids), len(asks)
    vistos.add(ev["event_id"])
    for d in SEGUIMIENTO_S:
        est.pendientes.append((time.time() + d, ev["event_id"], d, ev["condition_id"], ev["outcome"], p))
    est.pendientes.sort()
    return ev


def _seguimientos(est: Estado):
    ahora = time.time()
    filas = []
    while est.pendientes and est.pendientes[0][0] <= ahora:
        _, eid, d, cond, outcome, p = est.pendientes.pop(0)
        tok = _token(cond, outcome)
        bids, asks = _libro(tok) if tok else (None, None)
        ult = est.ultimo.get((cond, outcome))
        filas.append({"event_id": eid, "delta_s": d, "ts_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                      "best_bid": bids[0][0] if bids else "", "best_ask": asks[0][0] if asks else "",
                      "ultimo_trade": ult[1] if ult else "", "bid_size_top": bids[0][1] if bids else "",
                      "depth_bid_cerca_evento_usd": _depth(bids, p - 0.02, p + 0.02) if bids is not None else ""})
    _append(OUT_SEG, COLS_SEG, filas)


def main() -> None:
    _log("arrancado -- eventos stink (SELL >=5c bajo mediana 10 min) en mercados no updown, libro real + seguimiento")
    est = Estado()
    vistos = _cargar_vistos()
    archivo = _archivo()
    pos = archivo.stat().st_size if archivo.exists() else 0   # arranca en el final: sin backlog
    cab = None
    while True:
        try:
            hoy = _archivo()
            if hoy != archivo:
                archivo, pos, cab = hoy, 0, None
            if archivo.exists():
                with open(archivo, encoding="utf-8", newline="") as f:
                    if cab is None:
                        cab = next(csv.reader([f.readline()]))
                        if pos == 0:
                            pos = f.tell()
                    f.seek(pos)
                    datos = f.read()
                # solo líneas completas
                fin = datos.rfind("\n")
                if fin >= 0:
                    cuerpo = datos[:fin + 1]
                    pos += len(cuerpo.encode("utf-8"))
                    nuevos = []
                    for row in csv.DictReader(cuerpo.splitlines(), fieldnames=cab):
                        ev = _procesar_fila(row, est, vistos, time.time())
                        if ev:
                            nuevos.append(ev)
                    filas = []
                    for ev in nuevos:
                        r = _consultar_evento(ev, est, vistos)
                        if r:
                            filas.append(r)
                            _log(f"EVENTO {r['market_slug'][:40]} {r['outcome']} p={r['precio_evento']} "
                                 f"ref={r['ref_mediana']} usd={r['usd_evento']} bid={r['best_bid_post']} "
                                 f"depth_bid_cerca={r['depth_bid_cerca_evento_usd']}")
                    if filas:
                        _append(OUT_EV, COLS_EV, filas)
                        _guardar_vistos(vistos)
            _seguimientos(est)
        except Exception as e:
            _log(f"WARN ciclo fallido: {type(e).__name__}: {e}")
        time.sleep(POLL_S)


if __name__ == "__main__":
    main()
