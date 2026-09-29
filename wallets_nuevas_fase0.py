#!/usr/bin/env python3
"""wallets_nuevas_fase0.py -- FASE 0 (solo observación), ronda2 #2 (Javi 29-Sep:
"parece una señal, tenemos que explotarla"). Retrospectivo 9-29 Sep: BUY >=100 USD
a precio 0,02-0,50 de wallets NUEVAS (primer trade no-updown en los últimos 3
días) en mercados de evento: EV/€ +0,034 (n=369, 215 cond., IC90 [-0,36,+0,70]),
precio<=0,15: +0,63 (n=113); control wallets antiguas en las mismas condiciones
-0,39 (n=1.217). Prometedor pero medido a PRECIO DE LA WALLET, no copiable.

Este observador mide lo que falta, con el principio micro-latencia: detecta el
BUY de una wallet nueva en cuanto entra en el firehose (cola de fichero 1 s),
pide el token a libro_estado_ws (WS) y registra el ASK/BID REAL a +0 (REST),
+1/+3/+10/+30 s (libro WS, ms) y +60/+300 s (REST con profundidad), más quién
es la wallet (edad en días, tamaño). El desenlace se cruza a posteriori
(gamma closed=true) en analisis_wallets_nuevas_fase0.py: EV al ask copiable a
cada latencia. Estado: data/shadow/wallets_nuevas_conocidas.json {wallet:
primer día visto (no-updown)}, sembrado con el histórico 9-29 Sep.
NO coloca órdenes. Se fusiona en observadores_fase0.py.
"""
import csv
import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import libro_estado_ws as LE  # noqa: E402
from stink_bids_fase0 import _token, _libro, _depth, _archivo, _append  # noqa: E402

DIR = REPO / "data" / "shadow"
CONOCIDAS = DIR / "wallets_nuevas_conocidas.json"
OUT = DIR / "wallets_nuevas_fase0.csv"
SEG = DIR / "wallets_nuevas_fase0_seguimiento.csv"
USD_MIN, P_MIN, P_MAX, DIAS_NUEVA = 100.0, 0.02, 0.50, 2
SEGS = (1, 3, 10, 30, 60, 300)
COLS = ["event_id", "ts_evento_utc", "ts_deteccion_utc", "lag_deteccion_s", "wallet", "edad_dias", "condition_id",
        "outcome", "market_slug", "title", "precio_wallet", "usd", "es_deporte", "ask0", "bid0", "prof_ask_usd",
        "n_wallets_nuevas_mismo_mercado"]
COLS_SEG = ["event_id", "delta_s", "ts_utc", "best_bid", "best_ask", "prof_ask_usd"]
DEP = re.compile(r" vs\.? |o/u|exact score|spread|moneyline|game \d|map \d|set \d|both teams|handicap|winner:|"
                 r"leading at half|to win the", re.I)


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def main():
    _log("arrancado -- BUY de wallets nuevas (>=100 USD, precio 0,02-0,50, no updown): ask/bid real a +0/1/3/10/30/60/300 s")
    LE.iniciar(("15min",))
    try:
        conocidas = json.loads(CONOCIDAS.read_text(encoding="utf-8"))
    except Exception:
        conocidas = {}
    pend, vistos, por_mercado = [], set(), {}
    archivo = _archivo()
    pos = archivo.stat().st_size if archivo.exists() else 0
    cab = None
    ult_guardado = time.time()
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
                fin = datos.rfind("\n")
                filas_ev = []
                if fin >= 0:
                    cuerpo = datos[:fin + 1]
                    pos += len(cuerpo.encode("utf-8"))
                    for row in csv.DictReader(cuerpo.splitlines(), fieldnames=cab):
                        if row["activo"] or not row["condition_id"]:
                            continue
                        w = row["wallet"]
                        dia = row["timestamp_utc"][:10]
                        primera = conocidas.setdefault(w, dia)
                        try:
                            p, u = float(row["price"]), float(row["usd_value"])
                        except ValueError:
                            continue
                        if row["side"] != "BUY" or u < USD_MIN or not P_MIN <= p <= P_MAX:
                            continue
                        edad = (datetime.fromisoformat(dia) - datetime.fromisoformat(primera)).days
                        if edad > DIAS_NUEVA:
                            continue
                        eid = row["transaction_hash"] or f"{w}|{row['condition_id']}|{row['ws_timestamp']}"
                        if eid in vistos:
                            continue
                        vistos.add(eid)
                        tok = _token(row["condition_id"], row["outcome"])
                        if not tok:
                            continue
                        LE.pedir([tok], 400)
                        bids, asks = _libro(tok)
                        ahora = datetime.now(timezone.utc)
                        try:
                            lag = round(ahora.timestamp() - int(row["ws_timestamp"]), 1)
                        except ValueError:
                            lag = ""
                        km = (row["condition_id"], row["outcome"])
                        por_mercado.setdefault(km, set()).add(w)
                        filas_ev.append({"event_id": eid, "ts_evento_utc": row["timestamp_utc"],
                                         "ts_deteccion_utc": ahora.isoformat(timespec="seconds"), "lag_deteccion_s": lag,
                                         "wallet": w, "edad_dias": edad, "condition_id": row["condition_id"],
                                         "outcome": row["outcome"], "market_slug": row["market_slug"],
                                         "title": row["title"][:120], "precio_wallet": p, "usd": u,
                                         "es_deporte": int(bool(DEP.search(row["title"]))),
                                         "ask0": asks[0][0] if asks else "", "bid0": bids[0][0] if bids else "",
                                         "prof_ask_usd": _depth(asks, asks[0][0], asks[0][0] + 0.02) if asks else 0,
                                         "n_wallets_nuevas_mismo_mercado": len(por_mercado[km])})
                        for d in SEGS:
                            pend.append((time.time() + d, eid, d, tok))
                        _log(f"NUEVA wallet {w[:8]} {row['title'][:45]} {row['outcome']} p={p} usd={u:.0f} ask0={asks[0][0] if asks else '-'}")
                    if filas_ev:
                        _append(OUT, COLS, filas_ev)
            pend.sort()
            segs = []
            ahora_s = time.time()
            while pend and pend[0][0] <= ahora_s:
                _, eid, d, tok = pend.pop(0)
                if d <= 30:
                    e = LE.en(tok, int(time.time() * 1000))
                    segs.append({"event_id": eid, "delta_s": d, "ts_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                 "best_bid": "" if not e or e["best_bid"] is None else e["best_bid"],
                                 "best_ask": "" if not e or e["best_ask"] is None else e["best_ask"], "prof_ask_usd": ""})
                else:
                    bids, asks = _libro(tok)
                    segs.append({"event_id": eid, "delta_s": d, "ts_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                 "best_bid": bids[0][0] if bids else "", "best_ask": asks[0][0] if asks else "",
                                 "prof_ask_usd": _depth(asks, asks[0][0], asks[0][0] + 0.02) if asks else 0})
            _append(SEG, COLS_SEG, segs)
            if time.time() - ult_guardado > 120:
                CONOCIDAS.write_text(json.dumps(conocidas), encoding="utf-8")
                ult_guardado = time.time()
        except Exception as e:
            _log(f"WARN ciclo fallido: {type(e).__name__}: {e}")
        time.sleep(1)


if __name__ == "__main__":
    main()
