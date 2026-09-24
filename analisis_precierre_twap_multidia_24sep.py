#!/usr/bin/env python3
"""analisis_precierre_twap_multidia_24sep.py -- validación multi-día (10 días)
de la ventana de precierre con dirección por TWAP PROYECTADO, usando Chainlink
(RTDS, capturado desde julio) como aproximación del TWAP oficial (TWAP60 =
media del spot en [fin-60, fin]). Complementa analisis_precierre_twap_ventana_
24sep.py (PolyBolt oficial, solo desde 24-Sep 08:00).

Primero resuelve empíricamente la REGLA de resolución a T=0 (qué referencia de
apertura -- spot o TWAP -- reproduce el outcome real), y luego mide, a cada
offset: acierto, fracción con ask operable del lado predicho (libro_book_ws,
best_ask <=25 s de antigüedad, [0.05,0.95)), ask medio, EV/€ neto de fee 7 %,
por día (para ver persistencia). Solo lectura.
"""
import bisect
import csv
import glob
import gzip
import json
import sys
import time
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
DATALOGS = Path("/root/polymarket-research-datalogs")
OFFSETS = [-60, -45, -30]
MAX_EDAD_ASK = float(__import__("os").environ.get("MAX_EDAD_ASK", "25"))
DUR = {"5min": 300, "15min": 900}
FEE = 0.07
DIAS = int(sys.argv[1]) if len(sys.argv) > 1 else 10
OUT = REPO / f"data/shadow/precierre_twap_multidia_24sep_edad{__import__('os').environ.get('MAX_EDAD_ASK','25')}.json"


def ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()


def abrir(p):
    return gzip.open(p, "rt") if str(p).endswith(".gz") else open(p)


def chainlink_dias(dias):
    serie = defaultdict(lambda: ([], []))
    for d in dias:
        for p in glob.glob(str(REPO / f"data/prices/chainlink_{d}.csv*")):
            with abrir(p) as f:
                for r in csv.DictReader(f):
                    try:
                        t = int(r["ws_timestamp_ms"]) / 1000; v = float(r["price_usd"])
                    except (ValueError, TypeError):
                        continue
                    serie[r["asset"]][0].append(t); serie[r["asset"]][1].append(v)
    for a in serie:
        orden = sorted(set(zip(*serie[a])))
        serie[a] = ([x for x, _ in orden], [y for _, y in orden])
    return serie


def valor_en(s, t, tol=3):
    xs, ys = s
    i = bisect.bisect_right(xs, t) - 1
    return ys[i] if i >= 0 and t - xs[i] <= tol else None


def media(s, t0, t1):
    xs, ys = s
    i, j = bisect.bisect_left(xs, t0), bisect.bisect_right(xs, t1)
    return (sum(ys[i:j]) / (j - i), j - i) if j > i else (None, 0)


def libros_dia(d):
    L = defaultdict(lambda: {"meta": None, "tok": defaultdict(list)})
    for p in glob.glob(str(DATALOGS / f"libro_book_ws_{d}.csv*")):
        with abrir(p) as f:
            for r in csv.DictReader(f):
                if r["marco"] not in DUR:
                    continue
                try:
                    ask = float(r["best_ask_ultimo"])
                except ValueError:
                    continue
                m = L[r["market_id"]]
                m["meta"] = (r["activo"], r["marco"])
                m["tok"][r["asset_id"]].append((ts(r["timestamp_utc"]), ask))
    return L


def outcomes(mids):
    out = {}
    mids = list(mids)
    for i in range(0, len(mids), 20):
        for _ in range(3):
            try:
                r = requests.get("https://gamma-api.polymarket.com/markets",
                                 params=[("id", m) for m in mids[i:i + 20]] + [("closed", "true")], timeout=20)
                for m in r.json():
                    pr = [float(x) for x in json.loads(m["outcomePrices"])]
                    if max(pr) >= 0.99:
                        out[str(m["id"])] = (pr.index(max(pr)), json.loads(m["clobTokenIds"]), ts(m["endDate"]))
                break
            except Exception:
                time.sleep(2)
        time.sleep(0.2)
    return out


def main():
    hoy = datetime.now(timezone.utc).date()
    dias = [(hoy - timedelta(days=k)).isoformat() for k in range(DIAS, 0, -1)]  # días completos, sin hoy
    acum = defaultdict(lambda: defaultdict(float))
    regla = defaultdict(lambda: [0, 0])
    for d in dias:
        prev = (datetime.fromisoformat(d) - timedelta(days=1)).date().isoformat()
        cl = chainlink_dias([prev, d])
        L = libros_dia(d)
        res = outcomes(L.keys())
        print(f"{d}: mercados con libro {len(L)}, resueltos {len(res)}", flush=True)
        for mid, (gan, toks, fin) in res.items():
            activo, marco = L[mid]["meta"]
            s = cl.get(activo)
            if not s or not s[0]:
                continue
            ini = fin - DUR[marco]
            spot_ini = valor_en(s, ini)
            twap_ini, n_i = media(s, ini - 60, ini)
            twap_fin, n_f = media(s, fin - 60, fin)
            spot_fin = valor_en(s, fin)
            if None in (spot_ini, twap_ini, twap_fin, spot_fin) or n_i < 20 or n_f < 20:
                continue
            # regla de resolución (T=0): 4 combinaciones
            for nombre, (a, b) in {"twapfin>twapini": (twap_fin, twap_ini), "twapfin>spotini": (twap_fin, spot_ini),
                                   "spotfin>spotini": (spot_fin, spot_ini), "spotfin>twapini": (spot_fin, twap_ini)}.items():
                regla[(marco, nombre)][0] += 1
                regla[(marco, nombre)][1] += int((0 if a > b else 1) == gan)
            for off in OFFSETS:
                t = fin + off
                spot_t = valor_en(s, t)
                if spot_t is None:
                    continue
                m_con, n_con = media(s, fin - 60, t)
                resto = max(0, -off) if off > -60 else 60
                proy = ((m_con * n_con if m_con else 0) + spot_t * resto) / ((n_con if m_con else 0) + resto)
                for nombre, up in {"A_spot": spot_t > spot_ini, "C_proy_vs_twapini": proy > twap_ini,
                                   "C_proy_vs_spotini": proy > spot_ini}.items():
                    idx = 0 if up else 1
                    k = (marco, off, nombre)
                    a = acum[k]
                    a["n"] += 1
                    ac = int(idx == gan)
                    a["ok"] += ac
                    serie = L[mid]["tok"].get(toks[idx], [])
                    prevs = [x for x in serie if x[0] <= t and t - x[0] <= MAX_EDAD_ASK]
                    if prevs and 0.05 <= prevs[-1][1] < 0.95:
                        ask = prevs[-1][1]
                        ev = ((1 - ask) / ask - FEE * (1 - ask)) if ac else -1.0
                        a["op"] += 1; a["ask"] += ask; a["ev"] += ev
                        a[f"ev_{d}"] += ev; a[f"op_{d}"] += 1
                        banda = f"banda_{min(int(ask*20)/20,0.9):.2f}"
                        a[banda + "_n"] += 1; a[banda + "_ev"] += ev
        del cl, L
    print("\n=== REGLA DE RESOLUCIÓN (acierto a T=0) ===")
    for (marco, nombre), (n, ok) in sorted(regla.items()):
        print(f"  {marco} {nombre:18s} n={n} acierto={ok/n:.4f}")
    salida = {"regla": {f"{k[0]}|{k[1]}": v[1] / v[0] for k, v in regla.items()}, "offsets": {}}
    for marco in DUR:
        print(f"\n=== {marco} ===")
        for off in OFFSETS:
            for nombre in ("A_spot", "C_proy_vs_twapini", "C_proy_vs_spotini"):
                a = acum.get((marco, off, nombre))
                if not a or not a["n"]:
                    continue
                dias_pos = sum(1 for d in dias if a.get(f"op_{d}") and a[f"ev_{d}"] > 0)
                dias_op = sum(1 for d in dias if a.get(f"op_{d}"))
                fila = {"n": int(a["n"]), "acierto": round(a["ok"] / a["n"], 4),
                        "frac_operable": round(a["op"] / a["n"], 3),
                        "ask_medio": round(a["ask"] / a["op"], 3) if a["op"] else None,
                        "ev_por_eur": round(a["ev"] / a["op"], 4) if a["op"] else None,
                        "n_op": int(a["op"]), "dias_ev_pos": f"{dias_pos}/{dias_op}"}
                fila["bandas"] = {k[:-2]: (int(a[k]), round(a[k[:-2] + "_ev"] / a[k], 3))
                                  for k in sorted(a) if k.startswith("banda_") and k.endswith("_n")}
                salida["offsets"][f"{marco}|{off}|{nombre}"] = fila
                print(f"  T{off:+4d}s {nombre:18s} n={fila['n']:5d} acierto={fila['acierto']:.3f} "
                      f"operable={fila['frac_operable']:.2f} ask={fila['ask_medio']} EV/€={fila['ev_por_eur']} "
                      f"n_op={fila['n_op']} días_EV+={fila['dias_ev_pos']}")
    OUT.write_text(json.dumps(salida, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
