#!/usr/bin/env python3
"""ya_decidido_ws_fase0.py -- FASE 0 (solo observación) de ronda3 #5 con el
principio micro-latencia (Javi, 29-Sep): el escáner de 10 min
(ya_decidido_universal_fase0.py) ve el estado horas DESPUÉS; lo que decide
si hay edge es CUÁNTO TARDA el libro en repreciar tras el hecho (publicación
de un dato macro, earnings, resultado) y si los lados ya equivocados quedan
a 0,92-0,95 durante minutos/horas (foto 29-Sep: bins de JOLTS a 0,92-0,94
1,7 h después del dato).

Diseño dirigido por el calendario: gamma da endDate de cada mercado (la hora
del hecho). Cada 30 s se buscan mercados NO deportes/updown/weather/escaleras
cripto con endDate en los próximos 20 min; a T-60 s se piden sus tokens
(YES+NO) a libro_estado_ws (WS, histórico 100 ms) y a T+620 s se vuelca a CSV
la línea temporal del libro (best bid/ask, imbalance, profundidad ask) en
offsets -30,-5,0,+1,+3,+5,+10,+30,+60,+180,+600 s respecto a endDate:
data/shadow/ya_decidido_ws_fase0.csv. Después, ya_decidido_universal_fase0
(lado ganador final) permite cruzar: ¿el lado correcto valía <0,99 a +Ns?

NO coloca ni cancela órdenes. Se fusiona en observadores_fase0.py.
"""
import csv
import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import libro_estado_ws as LE  # noqa: E402
from sports_wallet_edge_tracker import clasificar  # noqa: E402

GAMMA = "https://gamma-api.polymarket.com"
OUT = REPO / "data" / "shadow" / "ya_decidido_ws_fase0.csv"
POLL_S = 30
MAX_PEND = 60
ADELANTO_S = 60
CIERRE_S = 620
OFFSETS = (-30, -5, 0, 1, 3, 5, 10, 30, 60, 180, 600)
CAMPOS = ["market_id", "condition_id", "question", "categoria_txt", "end_date", "token", "offset_s", "t_estado_ms",
          "edad_estado_ms", "best_bid", "best_ask", "imb1", "imb5", "depth_ask5_usd"]
_S = requests.Session()


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _excluido(m):
    q = (m.get("question") or "") + " " + (m.get("slug") or "")
    if re.search(r"up or down|updown|-5m-|-15m-|temperature|highest temp|above [\d,]", q, re.I):
        return True
    # deportes que la clasificación de sports no atrapa (exact score, partidos, esports, mitades...)
    if re.search(r"exact score|game \d|map \d|set \d|round \d|leading at half|second half|first half|both teams|any player|"
                 r"odd/even|handicap|total kills|first blood|o/u|over/under| vs\.? |moneyline|spread|to win the (match|game|map|set)|"
                 r"clean sheet|goal|corners|cards|winner:", q, re.I):
        return True
    return clasificar(m.get("question", ""), m.get("groupItemTitle") or m.get("slug", "")) is not None


def _categoria(q):
    q = (q or "").lower()
    for k, pat in (("datos", r"jolts|cpi|nfp|payroll|gdp|unemployment|inflation|fed |fomc|etf flows|earnings|beat"),
                   ("elecciones", r"election|seats|mayor|president|vote"),
                   ("cripto", r"bitcoin|ethereum|solana|xrp|crypto|microstrategy"),
                   ("geopolitica", r"ukraine|russia|israel|iran|hormuz|strait|missile|war|target"),
                   ("cine", r"box office|opening weekend|movie"),
                   ("clima_sismos", r"earthquake|wind gust|hurricane")):
        if re.search(pat, q):
            return k
    return "otros"


def _candidatos():
    ahora = datetime.now(timezone.utc)
    out, off = [], 0
    while off < 600:
        try:
            j = _S.get(f"{GAMMA}/markets", params={
                "closed": "false", "limit": 100, "offset": off, "order": "endDate", "ascending": "true",
                "end_date_min": ahora.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "end_date_max": (ahora + timedelta(minutes=20)).strftime("%Y-%m-%dT%H:%M:%SZ")}, timeout=20).json()
        except Exception as e:
            _log(f"WARN listado: {type(e).__name__}")
            break
        if not isinstance(j, list) or not j:
            break
        for m in j:
            if _excluido(m):
                continue
            try:
                end = datetime.fromisoformat(m["endDate"].replace("Z", "+00:00")).timestamp()
                toks = json.loads(m.get("clobTokenIds") or "[]")
            except Exception:
                continue
            if toks:
                out.append({"mid": str(m.get("id")), "cid": m.get("conditionId", ""), "q": (m.get("question") or "")[:140],
                            "end": end, "toks": toks, "end_iso": m["endDate"], "pedido": False})
        off += 100
        if len(j) < 100:
            break
        time.sleep(0.2)
    return out


def _volcar(p):
    filas = []
    end_ms = int(p["end"] * 1000)
    cat = _categoria(p["q"])
    for i, tk in enumerate(p["toks"][:2]):
        lado = "YES" if i == 0 else "NO"
        for off in OFFSETS:
            e = LE.en(tk, end_ms + off * 1000)
            filas.append({"market_id": p["mid"], "condition_id": p["cid"], "question": p["q"], "categoria_txt": cat,
                          "end_date": p["end_iso"], "token": lado, "offset_s": off,
                          "t_estado_ms": e["t_ms"] if e else "", "edad_estado_ms": e["edad_ms"] if e else "",
                          "best_bid": "" if not e or e["best_bid"] is None else e["best_bid"],
                          "best_ask": "" if not e or e["best_ask"] is None else e["best_ask"],
                          "imb1": "" if not e or e["imb1"] is None else e["imb1"],
                          "imb5": "" if not e or e["imb5"] is None else e["imb5"],
                          "depth_ask5_usd": "" if not e else e["depth_ask5_usd"]})
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        if nuevo:
            w.writeheader()
        w.writerows(filas)


def main():
    _log("arrancado -- mercados de eventos con endDate próximo: línea temporal del libro por WS en ms alrededor del hecho")
    LE.iniciar(("15min",))
    vistos, pend = set(), {}
    prox = 0.0
    while True:
        try:
            ahora = time.time()
            if ahora >= prox:
                prox = ahora + POLL_S
                for c in _candidatos():
                    if c["mid"] not in vistos and c["mid"] not in pend and len(pend) < MAX_PEND:
                        pend[c["mid"]] = c
            for mid in list(pend):
                p = pend[mid]
                if not p["pedido"] and ahora >= p["end"] - ADELANTO_S:
                    LE.pedir(p["toks"][:2], int(p["end"] - ahora) + CIERRE_S + 30)
                    p["pedido"] = True
                if p["pedido"] and ahora >= p["end"] + CIERRE_S:
                    _volcar(p)
                    vistos.add(mid)
                    pend.pop(mid)
                    _log(f"volcado {p['q'][:50]}")
        except Exception as e:
            _log(f"WARN ciclo fallido: {type(e).__name__}: {e}")
        time.sleep(1)


if __name__ == "__main__":
    main()
