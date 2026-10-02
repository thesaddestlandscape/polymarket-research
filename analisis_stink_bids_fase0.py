#!/usr/bin/env python3
"""analisis_stink_bids_fase0.py -- lectura de stink_bids_fase0*.csv (ronda3 #1).
Para cada evento (SELL taker >=5c bajo la mediana de 10 min, mercados no
updown) mide con precios EJECUTABLES: ganancia por acción de un bid pasivo
puesto al precio del evento y vendido al BID real a +60/+300/+1800 s
(seguimiento del libro), capacidad (USD ejecutados en el evento) y
profundidad de bid restante cerca del precio del evento (cola por delante:
si hay mucho, un bid nuestro no habría sido el primero). Sin fee (maker no
paga; la salida al bid es taker con fee según mercado -> orientativo).
Decidir con n>=40 eventos, >=10 días, IC90 por clusters de mercado>0.
"""
import csv
import random
import statistics as st
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
EV = REPO / "data/shadow/stink_bids_fase0.csv"
SEG = REPO / "data/shadow/stink_bids_fase0_seguimiento.csv"
STAKE_EUR = 2.0


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _desenlaces(cids) -> dict:
    """{condition_id: {outcome: precio}} SOLO de mercados cerrados (gamma exige closed=true para
    devolver cerrados por condition_ids). 02-Oct: sin esto, los eventos cuyo mercado se había
    resuelto antes de +delta (sin libro -> sin bid) se caían de la muestra: 70 de 192, media -19,9c,
    20/70 ganaban. Con ellos la salida a +1800 s pasa de +9,8c (IC90>0) a +2,4c (IC90 cruza 0)."""
    import json
    import requests
    out, cids = {}, sorted(c for c in cids if c)
    for i in range(0, len(cids), 20):
        try:
            r = requests.get("https://gamma-api.polymarket.com/markets", timeout=20,
                             params=[("condition_ids", c) for c in cids[i:i + 20]] + [("closed", "true"), ("limit", 100)])
            for m in r.json():
                out[m["conditionId"]] = dict(zip(json.loads(m["outcomes"]), [float(x) for x in json.loads(m["outcomePrices"])]))
        except Exception:
            continue
    return out


def evaluar():
    if not EV.exists():
        return {"n_eventos": 0}
    evs = list(csv.DictReader(open(EV, encoding="utf-8")))
    seg = defaultdict(dict)
    if SEG.exists():
        for r in csv.DictReader(open(SEG, encoding="utf-8")):
            seg[r["event_id"]][int(r["delta_s"])] = r
    out = {"n_eventos": len(evs), "dias": len({e["ts_evento_utc"][:10] for e in evs}),
           "mercados": len({e["condition_id"] for e in evs}), "por_delta": {}}
    usd = [_f(e["usd_evento"]) for e in evs if _f(e["usd_evento"])]
    dev = [_f(e["desviacion"]) for e in evs if _f(e["desviacion"])]
    dcerca = [_f(e["depth_bid_cerca_evento_usd"]) for e in evs if _f(e["depth_bid_cerca_evento_usd"]) is not None]
    out.update({"usd_evento_mediana": round(st.median(usd), 2) if usd else None,
                "desviacion_mediana": round(st.median(dev), 3) if dev else None,
                "depth_bid_cerca_mediana": round(st.median(dcerca), 2) if dcerca else None})
    resueltos = _desenlaces({e["condition_id"] for e in evs})
    for d in (1, 3, 10, 30, 60, 300, 1800):
        gan, cl, eur, n_resuelto = [], defaultdict(list), [], 0
        for e in evs:
            s = seg.get(e["event_id"], {}).get(d)
            bid, p = _f((s or {}).get("best_bid")), _f(e["precio_evento"])
            if bid is None:
                # mercado ya resuelto (sin libro): vale su desenlace oficial, nunca se descarta
                v = resueltos.get(e["condition_id"], {}).get(e.get("outcome"))
                if v is not None and (v > 0.98 or v < 0.02):
                    bid, n_resuelto = float(round(v)), n_resuelto + 1
            if bid is None or not p:
                continue
            g = bid - p
            gan.append(g)
            cl[e["condition_id"]].append(g)
            cap = min(STAKE_EUR, _f(e["usd_evento"]) or STAKE_EUR)
            eur.append(cap / p * g)
        if len(gan) < 3:
            out["por_delta"][d] = {"n": len(gan)}
            continue
        g = list(cl.values())
        random.seed(2)
        b = sorted(st.mean([v for k in random.choices(g, k=len(g)) for v in k]) for _ in range(1000))
        out["por_delta"][d] = {"n": len(gan), "mediana_c": round(100 * st.median(gan), 1),
                               "media_c": round(100 * st.mean(gan), 1),
                               "frac_pos": round(sum(x > 0 for x in gan) / len(gan), 2),
                               "ic90_clusters_c": [round(100 * b[50], 1), round(100 * b[950], 1)],
                               "eur_por_evento": round(st.mean(eur), 3),
                               "eur_total": round(sum(eur), 2), "n_valorados_por_desenlace": n_resuelto}
    return out


if __name__ == "__main__":
    import json
    print(json.dumps(evaluar(), indent=1, ensure_ascii=False))
