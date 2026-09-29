#!/usr/bin/env python3
"""analisis_wallets_nuevas_fase0.py -- EV al precio COPIABLE (ask real a +0/1/3/10/30 s tras el BUY de una
wallet nueva) frente al desenlace (gamma closed=true), fee 4 % aprox. IC90 por condición. Desagregado
deporte/no deporte. Decidir con n>=40 resueltos y >=10 días."""
import csv
import json
import random
import statistics as st
from collections import defaultdict
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
EV, SEG = REPO / "data/shadow/wallets_nuevas_fase0.csv", REPO / "data/shadow/wallets_nuevas_fase0_seguimiento.csv"
FEE = 0.04
_S = requests.Session()


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _final(c):
    try:
        j = _S.get("https://gamma-api.polymarket.com/markets", params={"condition_ids": c, "closed": "true"}, timeout=15).json()
        if j:
            pr = [float(x) for x in json.loads(j[0]["outcomePrices"])]
            outs = json.loads(j[0]["outcomes"])
            if max(pr) > 0.99:
                return outs[pr.index(max(pr))]
    except Exception:
        pass
    return None


def evaluar():
    if not EV.exists():
        return {"n_eventos": 0}
    evs = list(csv.DictReader(open(EV, encoding="utf-8")))
    seg = defaultdict(dict)
    if SEG.exists():
        for r in csv.DictReader(open(SEG, encoding="utf-8")):
            seg[r["event_id"]][int(r["delta_s"])] = _f(r["best_ask"])
    fin = {}
    for c in {e["condition_id"] for e in evs}:
        v = _final(c)
        if v:
            fin[c] = v
    out = {"n_eventos": len(evs), "wallets": len({e["wallet"] for e in evs}), "resueltos": 0, "filas": {}}
    def ev(p, win):
        return ((1 - p) / p if win else -1) - FEE * (1 - p)
    for nombre, filtro in (("todas", lambda e: True), ("no deporte", lambda e: e["es_deporte"] == "0"),
                           ("deporte", lambda e: e["es_deporte"] == "1")):
        for lat in ("wallet", 0, 1, 3, 10, 30):
            filas = []
            for e in evs:
                if e["condition_id"] not in fin or not filtro(e):
                    continue
                p = _f(e["precio_wallet"]) if lat == "wallet" else (_f(e["ask0"]) if lat == 0 else seg[e["event_id"]].get(lat))
                if p is None or not 0.02 <= p <= 0.95:
                    continue
                filas.append((e["condition_id"], ev(p, fin[e["condition_id"]] == e["outcome"]), e["ts_evento_utc"][:10]))
            if len(filas) < 8:
                continue
            cl = defaultdict(list)
            for c, v, d in filas:
                cl[c].append(v)
            g = list(cl.values())
            random.seed(1)
            b = sorted(st.mean([v for k in random.choices(g, k=len(g)) for v in k]) for _ in range(1000)) if len(g) >= 3 else [None] * 1000
            out["filas"][f"{nombre} @ {'precio wallet' if lat == 'wallet' else f'ask +{lat}s'}"] = {
                "n": len(filas), "cond": len(cl), "dias": len({d for _, _, d in filas}),
                "ev": round(st.mean(v for _, v, _ in filas), 3), "ic90": [None if b[50] is None else round(b[50], 2), None if b[950] is None else round(b[950], 2)]}
    out["resueltos"] = sum(1 for e in evs if e["condition_id"] in fin)
    return out


if __name__ == "__main__":
    print(json.dumps(evaluar(), indent=1, ensure_ascii=False))
