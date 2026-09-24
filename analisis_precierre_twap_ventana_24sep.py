#!/usr/bin/env python3
"""analisis_precierre_twap_ventana_24sep.py -- ¿en qué instante antes del
cierre hay a la vez (a) dirección fiable y (b) ask operable del lado ganador?
(24-Sep, Javi: "soluciona esto para que precierre y naive puedan operar").

Motivo: a T-2s el lado ganador ya no tiene asks (0,14-0,21 % de lecturas) y
los asks residuales de 0,01 son trampas (la dirección spot pierde 40/40) -- el
TWAP de 60 s oficial fija el resultado antes del cierre.

Fuentes:
  - PolyBolt (data/prices/polybolt_*.csv): spot 1 Hz y TWAP60 OFICIAL.
  - libro_book_ws_*.csv (datalogs): best_ask por token (YES y NO) cada ~20 s.
  - outcome real: gamma-api por market_id (closed=true).
Predictores de dirección en T+t (t<0):
  A spot(T+t) vs spot(apertura)            -- lo que usa hoy el precierre
  B twap60(T+t) vs twap60(apertura)
  C twap proyectado al cierre vs twap60(apertura): media de los spot ya
    conocidos en [T-60, T+t] + spot(T+t) para el resto
Para cada (marco, t, predictor): n, acierto, fracción con ask del lado
predicho en [0.05, 0.95), ask medio, EV/€ neto (fee cripto 7 % sobre ganancia).
Solo lectura.
"""
import bisect
import csv
import glob
import json
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
DATALOGS = Path("/root/polymarket-research-datalogs")
OFFSETS = [-90, -60, -45, -30, -20, -10, -5]
DUR = {"5min": 300, "15min": 900}
FEE = 0.07
OUT = REPO / "data/shadow/precierre_twap_ventana_24sep.json"


def ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()


def cargar_polybolt():
    serie = defaultdict(lambda: {"spot": ([], []), "twap60": ([], [])})
    for f in sorted(glob.glob(str(REPO / "data/prices/polybolt_*.csv"))):
        for r in csv.DictReader(open(f)):
            try:
                t = int(r["event_ts_ms"]) / 1000; v = float(r["value"])
            except (ValueError, TypeError):
                continue
            a, b = serie[r["asset"]][r["canal"]]
            a.append(t); b.append(v)
    for asset in serie:
        for canal in ("spot", "twap60"):
            a, b = serie[asset][canal]
            orden = sorted(set(zip(a, b)))
            serie[asset][canal] = ([x for x, _ in orden], [y for _, y in orden])
    return serie


def valor_en(ser, t):
    xs, ys = ser
    i = bisect.bisect_right(xs, t) - 1
    return ys[i] if i >= 0 and t - xs[i] <= 3 else None


def media_spot(ser, t0, t1):
    xs, ys = ser
    i, j = bisect.bisect_left(xs, t0), bisect.bisect_right(xs, t1)
    v = ys[i:j]
    return (sum(v) / len(v), len(v)) if v else (None, 0)


def cargar_libros(desde):
    """{market_id: {'meta': (activo, marco), 'tokens': {asset_id: [(t, ask)]}}}"""
    libros = defaultdict(lambda: {"meta": None, "tokens": defaultdict(list)})
    for f in sorted(glob.glob(str(DATALOGS / "libro_book_ws_*.csv"))):
        if Path(f).name < f"libro_book_ws_{desde[:10]}":
            continue
        for r in csv.DictReader(open(f)):
            if r["marco"] not in DUR:
                continue
            t = ts(r["timestamp_utc"])
            if t < ts(desde):
                continue
            try:
                ask = float(r["best_ask_ultimo"])
            except ValueError:
                continue
            m = libros[r["market_id"]]
            m["meta"] = (r["activo"], r["marco"])
            m["tokens"][r["asset_id"]].append((t, ask))
    return libros


def outcomes(mids):
    """{market_id: (indice_ganador, [token_yes, token_no], end_ts)}"""
    out = {}
    mids = list(mids)
    for i in range(0, len(mids), 20):
        try:
            r = requests.get("https://gamma-api.polymarket.com/markets",
                             params=[("id", m) for m in mids[i:i + 20]] + [("closed", "true")], timeout=20)
            for m in r.json():
                pr = [float(x) for x in json.loads(m["outcomePrices"])]
                if max(pr) < 0.99:
                    continue
                toks = json.loads(m["clobTokenIds"])
                out[str(m["id"])] = (pr.index(max(pr)), toks, ts(m["endDate"]))
        except Exception as e:
            print("gamma error", e)
        time.sleep(0.25)
    return out


def main():
    pb = cargar_polybolt()
    t_pb0 = min(pb[a]["twap60"][0][0] for a in pb if pb[a]["twap60"][0])
    desde = datetime.fromtimestamp(t_pb0 + 60, timezone.utc).isoformat()
    libros = cargar_libros(desde)
    res = outcomes(libros.keys())
    print(f"polybolt desde {desde}; mercados con libro {len(libros)}; resueltos {len(res)}")
    acum = defaultdict(lambda: {"n": 0, "ok": 0, "con_ask": 0, "ask_sum": 0.0, "ev_sum": 0.0, "ev_n": 0})
    for mid, (gan, toks, fin) in res.items():
        L = libros[mid]
        activo, marco = L["meta"]
        ini = fin - DUR[marco]
        s = pb.get(activo)
        if not s:
            continue
        spot_ini = valor_en(s["spot"], ini)
        twap_ini = valor_en(s["twap60"], ini)
        for off in OFFSETS:
            t = fin + off
            spot_t = valor_en(s["spot"], t)
            twap_t = valor_en(s["twap60"], t)
            m_conocida, n_con = media_spot(s["spot"], fin - 60, t)
            preds = {}
            if spot_t and spot_ini:
                preds["A_spot"] = spot_t > spot_ini
            if twap_t and twap_ini:
                preds["B_twap"] = twap_t > twap_ini
            if twap_ini and spot_t and m_conocida is not None:
                resto = max(0, -off)
                proy = (m_conocida * n_con + spot_t * resto) / (n_con + resto) if (n_con + resto) else None
                if proy:
                    preds["C_twap_proy"] = proy > twap_ini
            for nombre, up in preds.items():
                idx = 0 if up else 1  # outcomes [Up, Down]
                a = acum[(marco, off, nombre)]
                a["n"] += 1
                acierto = int(idx == gan)
                a["ok"] += acierto
                serie = L["tokens"].get(toks[idx], [])
                prev = [x for x in serie if x[0] <= t and t - x[0] <= 25]
                if prev:
                    ask = prev[-1][1]
                    if 0.05 <= ask < 0.95:
                        a["con_ask"] += 1; a["ask_sum"] += ask
                        a["ev_sum"] += ((1 - ask) / ask - FEE * (1 - ask)) if acierto else -1.0
                        a["ev_n"] += 1
    salida = {}
    for marco in DUR:
        print(f"\n== {marco}")
        for off in OFFSETS:
            for nombre in ("A_spot", "B_twap", "C_twap_proy"):
                a = acum.get((marco, off, nombre))
                if not a or not a["n"]:
                    continue
                fila = {"n": a["n"], "acierto": round(a["ok"] / a["n"], 3),
                        "frac_ask_operable": round(a["con_ask"] / a["n"], 3),
                        "ask_medio": round(a["ask_sum"] / a["con_ask"], 3) if a["con_ask"] else None,
                        "ev_eur_por_eur": round(a["ev_sum"] / a["ev_n"], 3) if a["ev_n"] else None,
                        "n_operables": a["ev_n"]}
                salida[f"{marco}|{off}|{nombre}"] = fila
                print(f"  T{off:+4d}s {nombre:12s} n={fila['n']:4d} acierto={fila['acierto']:.3f} "
                      f"ask_operable={fila['frac_ask_operable']:.2f} ask_medio={fila['ask_medio']} "
                      f"EV/€={fila['ev_eur_por_eur']} (n_op={fila['n_operables']})")
    OUT.write_text(json.dumps(salida, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
