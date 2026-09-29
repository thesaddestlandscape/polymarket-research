#!/usr/bin/env python3
"""analisis_sniper_listados_fase0.py -- lectura de sniper_listados_fase0*.csv
(ronda3 #7). Para cada mercado recién listado y cada foto del libro:
 (a) disponibilidad: % con cotización a dos lados por edad (+1/5/15/30/60 min)
     y spread mediano; tiempo hasta la primera cotización a dos lados.
 (b) escaleras cripto ('above K'): precio JUSTO P(S_T>K)=Phi(ln(S/K)/(sigma*sqrt(T)))
     con S = spot Binance de la foto, sigma = vol realizada 1m de los 60 min
     previos (klines Binance REST), T = minutos hasta end_date. Edge al ASK
     real: comprar YES si justo-ask>=margen; comprar NO (a 1-bid) si
     bid-justo>=margen. EV al desenlace final (gamma por condition_id, fee
     7 %*(p*(1-p)) por acción, cripto) por edad de la foto, IC90 por días.
Decidir con n>=40 y >=10 días. Solo lectura.
"""
import csv
import json
import math
import random
import statistics as st
import sys
from bisect import bisect_left, bisect_right
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
LIST = REPO / "data/shadow/sniper_listados_fase0.csv"
SEG = REPO / "data/shadow/sniper_listados_fase0_seguimiento.csv"
FEE = 0.07
MARGEN = 0.05
_S = requests.Session()


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()


def _phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def _klines(activo, t0, t1):
    out, cur = [], int(t0 * 1000)
    while cur < t1 * 1000:
        try:
            j = _S.get("https://api.binance.com/api/v3/klines", params={"symbol": f"{activo}USDT", "interval": "1m",
                       "startTime": cur, "endTime": int(t1 * 1000), "limit": 1000}, timeout=15).json()
        except Exception:
            break
        if not isinstance(j, list) or not j:
            break
        out += [(k[0] / 1000, float(k[4])) for k in j]
        cur = j[-1][0] + 60000
    return out


def _vol_1m(ks_t, ks_p, t, ventana_min=60):
    i, j = bisect_left(ks_t, t - ventana_min * 60), bisect_right(ks_t, t)
    px = ks_p[i:j]
    if len(px) < 20:
        return None
    r = [math.log(px[k + 1] / px[k]) for k in range(len(px) - 1)]
    return st.pstdev(r)


def _finales(cids):
    fin = {}
    for c in cids:
        try:
            j = _S.get("https://gamma-api.polymarket.com/markets", params={"condition_ids": c}, timeout=15).json()
            if j and j[0].get("closed"):
                pr = [float(x) for x in json.loads(j[0]["outcomePrices"])]
                if pr and max(pr) > 0.99:
                    fin[c] = (1 if pr[0] > 0.99 else 0, j[0].get("endDate", ""))   # (YES ganó, endDate)
        except Exception:
            continue
    return fin


EVT = REPO / "data/shadow/sniper_listados_fase0_eventos.csv"


def _eventos_ms(L):
    """Latencia de listado y tiempo (ms desde el listado) hasta la primera cotización: cualquier libro,
    dos lados, y 'útil' (spread<=0,20), por mercado de escalera cripto con seguimiento WS."""
    if not EVT.exists():
        return {}
    por = defaultdict(list)
    for r in csv.DictReader(open(EVT, encoding="utf-8")):
        por[r["market_id"]].append(r)
    primero, dos, util, semilla = [], [], [], []
    for mid, ev in por.items():
        ev.sort(key=lambda r: int(r["edad_ms"]))
        primero.append(int(ev[0]["edad_ms"]))
        hecho_dos = hecho_util = False
        for r in ev:
            bb, ba = _f(r["best_bid"]), _f(r["best_ask"])
            if bb is None or ba is None or ba <= bb:
                continue
            if not hecho_dos:
                dos.append(int(r["edad_ms"]))
                semilla.append(ba - bb)
                hecho_dos = True
            if not hecho_util and ba - bb <= 0.20:
                util.append(int(r["edad_ms"]))
                hecho_util = True
    lat = [int(r["latencia_ms"]) for r in L.values() if r.get("latencia_ms") not in ("", None)]
    med = lambda v: round(st.median(v)) if v else None
    return {"mercados_ms": len(por), "latencia_deteccion_ms_mediana": med(lat),
            "primer_evento_ms_mediana": med(primero), "primera_cotizacion_dos_lados_ms_mediana": med(dos),
            "n_dos_lados": len(dos), "primera_util_spread_le_20c_ms_mediana": med(util), "n_util": len(util),
            "spread_semilla_mediano": round(st.median(semilla), 3) if semilla else None}


def evaluar():
    if not LIST.exists() or not SEG.exists():
        return {"n_mercados": 0}
    L = {r["market_id"]: r for r in csv.DictReader(open(LIST, encoding="utf-8"))}
    seg = list(csv.DictReader(open(SEG, encoding="utf-8")))
    out = {"n_mercados": len(L), "por_categoria": defaultdict(int), "disp": {}}
    for r in L.values():
        out["por_categoria"][r["categoria"]] += 1
    out["por_categoria"] = dict(out["por_categoria"])
    # (a) disponibilidad por edad objetivo
    por_off = defaultdict(list)
    for s in seg:
        por_off[int(s["offset_obj_s"])].append(s)
    for off, xs in sorted(por_off.items()):
        dos = [x for x in xs if _f(x["best_bid"]) is not None and _f(x["best_ask"]) is not None]
        sp = [_f(x["best_ask"]) - _f(x["best_bid"]) for x in dos]
        out["disp"][off] = {"n": len(xs), "frac_dos_lados": round(len(dos) / len(xs), 3) if xs else None,
                            "spread_mediano": round(st.median(sp), 3) if sp else None}
    out["ms"] = _eventos_ms(L)
    # (b) escaleras cripto: precio justo y EV
    esc = [x for x in seg if L.get(x["market_id"], {}).get("categoria") == "cripto_escalera"
           and _f(x["spot"]) and _f(L[x["market_id"]]["strike"])]
    if not esc:
        out["ev"] = {}
        return out
    kl = {}
    for a in {L[x["market_id"]]["activo"] for x in esc}:
        ts = [_ts(x["ts_utc"]) for x in esc if L[x["market_id"]]["activo"] == a]
        k = _klines(a, min(ts) - 3700, max(ts) + 60)
        kl[a] = ([t for t, _ in k], [p for _, p in k])
    fin = _finales({L[x["market_id"]]["condition_id"] for x in esc})
    filas = defaultdict(list)
    for x in esc:
        m = L[x["market_id"]]
        c = m["condition_id"]
        if c not in fin:
            continue
        t = _ts(x["ts_utc"])
        end = m["end_date"] or fin[c][1]
        if not end:
            continue
        Tmin = (_ts(end) - t) / 60
        if Tmin <= 1:
            continue
        sg = _vol_1m(*kl[m["activo"]], t)
        if not sg:
            continue
        S_, K = _f(x["spot"]), _f(m["strike"])
        fair = _phi(math.log(S_ / K) / (sg * math.sqrt(Tmin)))
        bid, ask = _f(x["best_bid"]), _f(x["best_ask"])
        dia = x["ts_utc"][:10]
        yes = fin[c][0]
        if ask is not None and 0.02 < ask < 0.98 and fair - ask >= MARGEN:
            ev = (yes - ask) - FEE * ask * (1 - ask)
            filas[(int(x["offset_obj_s"]), "compra YES")].append((dia, ev / ask))
        if bid is not None and 0.02 < bid < 0.98 and bid - fair >= MARGEN:
            cost = 1 - bid
            ev = ((1 - yes) - cost) - FEE * cost * (1 - cost)
            filas[(int(x["offset_obj_s"]), "compra NO")].append((dia, ev / cost))
    ev_out = {}
    for k, v in sorted(filas.items()):
        d = defaultdict(list)
        for dia, e in v:
            d[dia].append(e)
        g = list(d.values())
        random.seed(3)
        b = sorted(st.mean([e for s_ in random.choices(g, k=len(g)) for e in s_]) for _ in range(1000)) if len(g) >= 2 else [None] * 1000
        ev_out[f"{k[0]}s {k[1]}"] = {"n": len(v), "dias": len(d), "ev_eur": round(st.mean(e for _, e in v), 3),
                                     "ic90": [None if b[50] is None else round(b[50], 3), None if b[950] is None else round(b[950], 3)]}
    out["ev"] = ev_out
    return out


if __name__ == "__main__":
    print(json.dumps(evaluar(), indent=1, ensure_ascii=False, default=str))
