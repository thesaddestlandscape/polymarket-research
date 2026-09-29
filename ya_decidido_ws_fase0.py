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
MAX_PEND = 120
ADELANTO_S = 60
CIERRE_S = 620
OFFSETS = (-30, -5, 0, 1, 3, 5, 10, 30, 60, 180, 600)
# modo "escaleras" (29-Sep, ronda2 #8 con micro-latencia): escaleras cripto 'above K' cerca del dinero, precierre a T-60..T-2 s
OFFSETS_ESC = (-60, -30, -20, -10, -5, -2, 0, 1, 2, 5, 10, 30, 60)
OUT_ESC = REPO / "data" / "shadow" / "escaleras_cierre_ws_fase0.csv"
ACTIVOS = {"bitcoin": "BTC", "ethereum": "ETH", "solana": "SOL", "xrp": "XRP"}
BINANCE = "https://api.binance.com/api/v3/ticker/price"
COLAS_MIN, COLAS_MAX = 0.01, 0.06      # modo "colas" (ronda2 #6): strikes entre 1 % y 6 % del spot (colas de la distribución horaria)
OFFSETS_COLAS = (-1800, -900, -300, -60, 0, 60)
OUT_COLAS_DIR = Path("/root/polymarket-research-datalogs")   # gz diario fuera de git, retención 14 días
CERCA_PCT = 0.04            # solo strikes a <=4 % del spot (los que aún pueden decidirse en la última hora)
CAMPOS = ["market_id", "condition_id", "question", "categoria_txt", "end_date", "token", "offset_s", "t_estado_ms",
          "edad_estado_ms", "best_bid", "best_ask", "imb1", "imb5", "depth_ask5_usd", "bid_size", "ask_size", "dist_spot_pct"]
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


def _spot(activo):
    try:
        return float(_S.get(BINANCE, params={"symbol": f"{activo}USDT"}, timeout=5).json()["price"])
    except Exception:
        return None


def _candidatos(modo="eventos"):
    ahora = datetime.now(timezone.utc)
    out, off, spots = [], 0, {}
    while off < 600:
        try:
            j = _S.get(f"{GAMMA}/markets", params={
                "closed": "false", "limit": 100, "offset": off, "order": "endDate", "ascending": "true",
                "end_date_min": ahora.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "end_date_max": (ahora + timedelta(minutes=35 if modo == "colas" else 20)).strftime("%Y-%m-%dT%H:%M:%SZ")}, timeout=20).json()
        except Exception as e:
            _log(f"WARN listado: {type(e).__name__}")
            break
        if not isinstance(j, list) or not j:
            break
        for m in j:
            if modo in ("escaleras", "colas"):
                q = m.get("question") or ""
                mm = re.search(r"above ([\d,]+(?:\.\d+)?)", q)
                act = next((v for k, v in ACTIVOS.items() if k in q.lower()), None)
                if not mm or not act or re.search(r"up or down", q, re.I):
                    continue
                sp = spots.get(act) or spots.setdefault(act, _spot(act))
                dist = abs(float(mm.group(1).replace(",", "")) / sp - 1) if sp else None
                if dist is None:
                    continue
                if modo == "colas":
                    if not COLAS_MIN <= dist <= COLAS_MAX:
                        continue
                elif dist > CERCA_PCT:
                    continue
            elif _excluido(m):
                continue
            try:
                end = datetime.fromisoformat(m["endDate"].replace("Z", "+00:00")).timestamp()
                toks = json.loads(m.get("clobTokenIds") or "[]")
            except Exception:
                continue
            if toks:
                out.append({"dist": (round(dist * 100, 2) if modo in ("escaleras", "colas") else ""), "mid": str(m.get("id")), "cid": m.get("conditionId", ""), "q": (m.get("question") or "")[:140],
                            "end": end, "toks": toks, "end_iso": m["endDate"], "pedido": False})
        off += 100
        if len(j) < 100:
            break
        time.sleep(0.2)
    return out


def _volcar(p, modo="eventos"):
    offs, out = (OFFSETS_ESC, OUT_ESC) if modo == "escaleras" else ((OFFSETS_COLAS, None) if modo == "colas" else (OFFSETS, OUT))
    filas = []
    end_ms = int(p["end"] * 1000)
    cat = _categoria(p["q"])
    for i, tk in enumerate(p["toks"][:2]):
        lado = "YES" if i == 0 else "NO"
        for off in offs:
            e = LE.en(tk, end_ms + off * 1000)
            filas.append({"market_id": p["mid"], "condition_id": p["cid"], "question": p["q"], "categoria_txt": cat,
                          "end_date": p["end_iso"], "token": lado, "offset_s": off,
                          "t_estado_ms": e["t_ms"] if e else "", "edad_estado_ms": e["edad_ms"] if e else "",
                          "best_bid": "" if not e or e["best_bid"] is None else e["best_bid"],
                          "best_ask": "" if not e or e["best_ask"] is None else e["best_ask"],
                          "imb1": "" if not e or e["imb1"] is None else e["imb1"],
                          "imb5": "" if not e or e["imb5"] is None else e["imb5"],
                          "depth_ask5_usd": "" if not e else e["depth_ask5_usd"],
                          "bid_size": "" if not e or e.get("bid_size") is None else e["bid_size"],
                          "ask_size": "" if not e or e.get("ask_size") is None else e["ask_size"],
                          "dist_spot_pct": p.get("dist", "")})
    if modo == "colas":
        import gzip
        hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        out = OUT_COLAS_DIR / f"colas_escaleras_ws_{hoy}.csv.gz"
        corte = time.time() - 14 * 86400
        for f_ in OUT_COLAS_DIR.glob("colas_escaleras_ws_*.csv.gz"):
            try:
                if f_.stat().st_mtime < corte:
                    f_.unlink()
            except OSError:
                pass
        nuevo = not out.exists()
        with gzip.open(out, "at", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CAMPOS)
            if nuevo:
                w.writeheader()
            w.writerows(filas)
        return
    nuevo = not out.exists()
    with open(out, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        if nuevo:
            w.writeheader()
        w.writerows(filas)


def main(modo="eventos"):
    if modo == "colas":
        adelanto, cierre = 1900, 70     # pide los tokens 31 min antes (T-30 min) y vuelca a T+70 s
    else:
        adelanto, cierre = (90, 100) if modo == "escaleras" else (ADELANTO_S, CIERRE_S)
    _log(f"arrancado [{modo}] -- línea temporal del libro por WS en ms alrededor de endDate")
    LE.iniciar(("15min",))
    vistos, pend = set(), {}
    prox = 0.0
    while True:
        try:
            ahora = time.time()
            if ahora >= prox:
                prox = ahora + POLL_S
                for c in _candidatos(modo):
                    if c["mid"] not in vistos and c["mid"] not in pend and len(pend) < MAX_PEND:
                        pend[c["mid"]] = c
            for mid in list(pend):
                p = pend[mid]
                if not p["pedido"] and ahora >= p["end"] - adelanto:
                    LE.pedir(p["toks"][:2], int(p["end"] - ahora) + cierre + 30)
                    p["pedido"] = True
                if p["pedido"] and ahora >= p["end"] + cierre:
                    _volcar(p, modo)
                    vistos.add(mid)
                    pend.pop(mid)
                    _log(f"volcado {p['q'][:50]}")
        except Exception as e:
            _log(f"WARN ciclo fallido: {type(e).__name__}: {e}")
        time.sleep(1)


if __name__ == "__main__":
    main()
